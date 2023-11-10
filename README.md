## forceusercert.py
Patch APK so it can be MITM'd on Android >=7. It essentially automates [this](https://github.com/pagvac/how-tos/blob/master/android-7-apps-mitm.md).
```
$ forceusercert.py base.apk 
all good! now just adb install base-patched.apk
$ adb install base-patched.apk
Success
```

## ddgpdfs.sh
Get URLs of public-facing PDFs on a given domain. Uses DuckDuckGo, no API key required.

### requirements
`bash` with `curl` and `tor`.

### example
Get PDF URLs
```
$ ./ddgpdfs.sh acme.com
[*] starting tor...
[*] connecting from 5.187.21.43
https://acme.com/doc.pdf
https://acme.com/doc2.pdf
```
_[...snip...]_

Save PDF URLs to file, excluding debug messages
```
$ ./ddgpdfs.sh acme.com>urls.txt
[*] starting tor...
[*] connecting from 178.239.176.73
```
_[...snip...]_

```
$ head -n2 urls.txt
https://acme.com/doc.pdf
https://acme.com/doc2.pdf
```
_[...snip...]_

## webping.sh
Minimalist script that takes a file with IPs or FQDNs and displays HTTP(S) URLs identified on those targets. Script should run on default OSX and Ubuntu environments.

### requirements
`bash` with either `curl` or `wget` command.

### example
In this example, we assume the user has previously brute-forced subdomains using tools such as dnsmap or SubBrute. Finding active HTTP(S) URLs on brute-forced subdomains is helpful when the rules of engagement allow probing any subdomain within a given parent domain. Think Yahoo's bug bounty program (`*.yahoo.com` `*.flickr.com`), for instance.
```
$ ./webping.sh subs.txt
http://3d.yahoo.com:80
https://about.yahoo.com:443
http://about.yahoo.com:80
http://account.yahoo.com:80
https://acer.yahoo.com:443
http://acer.yahoo.com:80
https://ads.yahoo.com:443
http://ads.yahoo.com:80
http://ads.yahoo.com:8081
https://adserver.yahoo.com:443
```
_[...snip...]_
