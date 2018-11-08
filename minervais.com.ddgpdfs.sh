#!/bin/bash

#check dependencies
if ! command -v curl >/dev/null 2>&1 || ! command -v tor >/dev/null 2>&1; then
	echo "curl and tor are required"
	exit
elif [[ $# -ne 1 ]]; then
	echo -e "one argument expected. correct syntax:\n$0 <parent-domain>"
	exit
fi

url="https://duckduckgo.com/html/"
p="socks://localhost:9050"
#p="http://localhost:8080" #for debugging :)
t=5
q="site%3A$1+filetype%3Apdf"


(>&2 echo "[*] starting tor...")
(tor >/dev/null&)
sleep 5
ip=$(curl -x $p -ks -A "" --url "https://duckduckgo.com/?q=ip&ia=answer"|grep -oE '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
(>&2 echo "[*] connecting from $ip")

#initial req
body="q=$q"
curl -x $p -ks -A "" --connect-timeout $t -d $body --url $url|grep -oE 'href="([^"#]+)"'|grep -i $1|cut -d'"' -f2|grep -E ^'http:\/\/|https:\/\/'|sort|uniq
#first "next" req
body="q=$q&s=30&nextParams=&v=l&o=json&dc=31&api=%2Fd.js"
curl -x $p -ks -A "" --connect-timeout $t -d $body --url $url|grep -oE 'href="([^"#]+)"'|grep -i $1|cut -d'"' -f2|grep -E ^'http:\/\/|https:\/\/'|sort|uniq

#subsequent "Next" reqs
for((s=80;s<=230;s=$((s+50)))); do
	body="q=$q&s=$s&nextParams=&v=l&o=json&dc=$((s+1))&api=%2Fd.js"
	sleep $[($RANDOM%5)+1]
	curl -x $p -A "" -ks --connect-timeout $t -d $body --url $url|grep -oE 'href="([^"#]+)"'|grep -i $1|cut -d'"' -f2|grep -E ^'http:\/\/|https:\/\/'|sort|uniq
done
pkill tor 2>/dev/null
(>&2 echo "[*] done")
