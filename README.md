# minervais.com.webping.sh
Minimalist script that takes a file with IPs or FQDNs and displays HTTP(S) URLs identified on those targets. Script should run on default OSX and Ubuntu environments.

# requirements
`bash` with either `curl` or `wget` command.

# example
In this example, we assume the user has previously brute-forced subdomains using tools such as dnsmap or SubBrute. Finding active HTTP(S) URLs on brute-forced subdomains is helpful when the rules of engagement allow probing any subdomain within a given parent domain. Think Yahoo's bug bounty program (`*.yahoo.com` `*.flickr.com`), for instance.
```
$ ./minervais.com.webping.sh subs.txt
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
http://adserver.yahoo.com:80
https://adventure.yahoo.com:443
http://adventure.yahoo.com:80
https://advertising.yahoo.com:443
http://advertising.yahoo.com:80
http://advice.yahoo.com:80
http://affiliates.yahoo.com:80
http://agenda.yahoo.com:80
https://aim.yahoo.com:443
http://aim.yahoo.com:80
https://alert.yahoo.com:443
http://alert.yahoo.com:80
https://alerts.yahoo.com:443
http://alerts.yahoo.com:80
https://alliance.yahoo.com:443
http://alliance.yahoo.com:80
https://amarillas.yahoo.com:443
http://amarillas.yahoo.com:80
http://amr.yahoo.com:80
https://analytics.yahoo.com:443
http://analytics.yahoo.com:80
https://anc.yahoo.com:443
http://anc.yahoo.com:80
```
_[...snip...]_
