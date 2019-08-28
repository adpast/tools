#minervais.com.httpsserver.py v0.1
#this script is INSECURE, use at your own risk!
#tested on Win10, RHEL7, and macOS 10.14
#ref: https://blog.anvileight.com/posts/simple-python-http-server/#python-2-x-1
import BaseHTTPServer, SimpleHTTPServer, ssl, sys, os, socket, errno

p = 8443
webroot = "www"
keyncert = "minervais.com.httpsserver.pem"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(("", p))
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        print "port " + str(p) + " already in use"
    else:
        # something else raised the socket.error exception
        print e
	
s.close()

#bind to all interfaces
h = BaseHTTPServer.HTTPServer(("", p), SimpleHTTPServer.SimpleHTTPRequestHandler)

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

keyncertcont =\
"""\
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAudYF3IupwJ1s2Q4n7AOYD7cG06iMV3PPsn7UiSMoAPx2oF6u
E9HzrhOvb5O+strLWNt5AeG4+Rv6v8NE61Z3Zr9AcOQL1swiHS5z6JCnVWNRDazK
KjTLy/gpAMgCAp8z0byAjA20+QQ56g3WoFoTBNXvmbkkAzOVJAIe92fJq1XGVRTt
Y3VMNHaj2gU9wlVjhWy2VwlSaWTzCLSWEY1FBSkRYyw0tHuWABuxYWLcr8mRhfqd
hyXPCPwRZpSLBS7fwbi88sufg8zVUCU1oxGl0jlRPbDbBnzTa4rK6CnXASGgA2Vc
mhdpBAsUbgQJpURde6JrfVJoQqAZJlec0d/i3wIDAQABAoIBABzHRQ8bXcVjW6jd
ZVdKUzET0e3TKzCb0a09sOIv3JESh7hcES8mk0sA52krAxwlf9oZ2spszz1clN8/
eRvMvx7dPTh+SEsSP7IvMGnyhMdXYwTwHjqdBHZozsi9MHqBdv/i5jFKKh1qByH0
1KjuagWUr88peac5RL5Xyb3ch8GNeh23BBU1R6201/yvYR+IcathAYdCD/Tvw/O1
V+J++k6dI5PQGj00HAeC2GAXf2iu/ypLXlNK+BWWL7r+VoKqBqsRlk3DP2qLvLqg
Cz8WloKGSoUmzOxCaphmSAB27TexuWG2Cpu/jUYqMcGOKP1A8BQcdFYxa2NTNOwQ
HcSZQKECgYEA7reQ3AjJ4UPl0t8P0ynyLl/ujXbFEYjGMhbdTX+qDq69YcNoL2pz
ZbokdczMN3MFhgx1fFzNAQB+0uekqcBqGq+Xb/dLys3AwYOk7qElPv3Tpcv5q80V
LXLQfC9N2VawoWGwhQRosX5DXAiL4TmUnJEHCDEnoHmrf6BxFMzPA08CgYEAx0pZ
N5ApMDFnYXnnEZTXgtdhvAB8+iYepJsjWDaA/o1SiGBireesmAEuwQSPzA2CvkgK
wGOMQKm3GbBzSP2FpowVG6kNiSUOCbM0/IrenTxAAkeiMjL9SB38qYKhE0RpP7lo
DT3l+4JDHm81P+tMIo7T+scKRuvTUqLoRqvSg3ECgYEAwlc7XYbiI7xNHDFxBq59
dXewFAb/RNke0aR/ohou7ikgELku1ntJWyYBjM2f6/x+ILV/6DD8zLYEidr/2RrG
xtbw6LxhPcfoByMPYR5b3j5y0eWPa2hYt1ljldZFAI1s2tVXCdOfD/EFEaX7iu5/
qD8BhI/P/PtQvWR260IZvk0CgYBmXxG/UgVmZSpmzxjcVinyYzMoQNPyJ5y8D5kz
WiQfHndT6LcoAAcPuiPLMM2xEwujNRyYwUoteUC+KH6/8sMxz2mUYN28IlW4s963
D5rVCDsVMLjnsnubDRRZ+ulFHXI3MsV5b99wt/REcPnYkMT2R4oqmw3zanaOT3Kj
wuWLcQKBgQDtUlFok0yxSlI6g7IcUc7U3T6BqLem4YMYUikC35B8aU5raTp/DIFi
R9qpjsgVfHfJWB93QmHh3ntR5s1bWdOj+G2RFpLYyxqzNJwrNmAkTIXBnCV14bOm
RgwgmvNEcHuZ2T1Mk1XlpsR/+Cx34Zzl5A8kTlhU+BSvH9jafFGpIQ==
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIICpjCCAY4CCQDDPtsyuBQh4zANBgkqhkiG9w0BAQsFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwIBcNMTkwODI4MDE0OTU5WhgPMjExOTA4MDQwMTQ5NTlaMBQxEjAQ
BgNVBAMMCWxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
ALnWBdyLqcCdbNkOJ+wDmA+3BtOojFdzz7J+1IkjKAD8dqBerhPR864Tr2+TvrLa
y1jbeQHhuPkb+r/DROtWd2a/QHDkC9bMIh0uc+iQp1VjUQ2syio0y8v4KQDIAgKf
M9G8gIwNtPkEOeoN1qBaEwTV75m5JAMzlSQCHvdnyatVxlUU7WN1TDR2o9oFPcJV
Y4VstlcJUmlk8wi0lhGNRQUpEWMsNLR7lgAbsWFi3K/JkYX6nYclzwj8EWaUiwUu
38G4vPLLn4PM1VAlNaMRpdI5UT2w2wZ802uKyugp1wEhoANlXJoXaQQLFG4ECaVE
XXuia31SaEKgGSZXnNHf4t8CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEATHjRe7Xi
5KvjSqP6gEClVxzZuOCDtgVz/3cxAiaRSnbMiriqTJR6E63nmjY/XXtNyPYKSQrh
9nbiB1rLrkj47t3nmwSmRRuPG3oYF3HLH32ONSMDFCTVg2I2NiEkGVQDcxP7wAip
LL1g3xsETA/AbJqcJEhw8j0Fz/+nkGX9+wUcS7UH4SjQ1OezShnJQKkVTdHX9LFQ
jTlujBTMJsi5p6E3ozoEFxYev3yC/PFyaTGLDfNkl0CX9hBVnFMl66rNzTAOUBWL
h0m4ad3T8Ppytb3prMu6a/+UQ5S/A+RCpeCFJ5HaZAlqELDj55TVe3QcRAWlnLco
N2U//sc3pYKLVw==
-----END CERTIFICATE-----\
"""

if not os.path.exists(keyncert):
	f = open(keyncert, "w")
	f.write(keyncertcont)
	f.close()

h.socket = ssl.wrap_socket(h.socket, keyncert, keyncert, server_side=True)

if not os.path.exists(webroot):
	os.makedirs(webroot)

os.chdir(webroot) #avoid exposing files in dir where this script is located

if p == 443:
	print "url: https://" + (str(socket.getfqdn())).lower()
else:
	print "url: https://" + (str(socket.getfqdn())).lower() + ":" + str(p)

print "webroot: " + os.getcwd()
h.serve_forever()
