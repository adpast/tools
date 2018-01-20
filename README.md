# minervais.com.webping.sh
Minimalist script that takes a file with IPs or FQDNs and displays http(s) URLs identified on those targets. Script should run on default OSX and Ubuntu environments.

# requirements
Bash with `curl` or `wget`.

# example
In this example, we assume the user has previously brute-forced subdomains using tools such as dnsmap or SubBrute. Finding active http(s) URLs on brute-forced subdomains is helpful when the rules of engagement allow probing any subdomain within a given parent domain. Think Yahoo's bug bounty program (`*.yahoo.com` `*.flickr.com`), for instance.

`$ ./minervais.com.webping.sh subs.txt`
