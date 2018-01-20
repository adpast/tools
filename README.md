# minervais.com.webping.sh
Minimalist script that takes a file with IPs or FQDNs and displays HTTP(S) URLs identified on those targets. Script should run on default OSX and Ubuntu environments.

# requirements
Bash with `curl` or `wget` command.

# example
In this example, we assume the user has previously brute-forced subdomains using tools such as dnsmap or SubBrute. Finding active HTTP(S) URLs on brute-forced subdomains is helpful when the rules of engagement allow probing any subdomain within a given parent domain. Think Yahoo's bug bounty program (`*.yahoo.com` `*.flickr.com`), for instance.
```
$ ./minervais.com.webping.sh subs.txt
https://yahoo.com:443
http://yahoo.com:80
https://www.yahoo.com:443
http://www.yahoo.com:80
https://atsv2-fp.wg1.b.yahoo.com:443
http://atsv2-fp.wg1.b.yahoo.com:80
https://uc-vcs-e1-us.corp.ne1.yahoo.com:8443
https://uc-vcs-e3-us.corp.ne1.yahoo.com:8443
https://uc-vcs-e4-us.corp.ne1.yahoo.com:8443
https://uc-vcs-e2-us.corp.ne1.yahoo.com:8443
https://groups.yahoo.com:443
http://groups.yahoo.com:80
https://home.yahoo.com:443
http://home.yahoo.com:80
https://fd-geoycpi-uno.gycpi.b.yahoodns.net:443
http://fd-geoycpi-uno.gycpi.b.yahoodns.net:80
```
_[...SNIP...]_
