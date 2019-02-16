#!/usr/bin/env python
import os
import sys
import shutil

#this script requires jarsigner, apktool, and ~/.android/debug.keystore
#~/.android/debug.keystore will only exist if you've built an APK with Android Studio in the past
#tested on macOS

if len( sys.argv ) == 1:
	print "syntax: python " + sys.argv[0] + " <apkfilename>"
	sys.exit()

os.system( "apktool d -sf -o .out " + sys.argv[1] + "&>/dev/null" )

if not os.path.exists(".out/res/xml"):
	os.makedirs(".out/res/xml")

f = open( ".out/res/xml/network_security_config.xml", "w" )
f.write(
"""\
<network-security-config>
    <base-config>
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" />
        </trust-anchors>
    </base-config>
</network-security-config>
"""
)

f.close()

f = open(".out/AndroidManifest.xml", "r")

xml = f.read()

if 'android:networkSecurityConfig="@xml/network_security_config"' not in xml:
	xml = xml.replace('<application','<application android:networkSecurityConfig="@xml/network_security_config"')

f.close()

f = open(".out/AndroidManifest.xml", "w")

f.write(xml)

f.close()

newapk = sys.argv[1]

newapk = newapk.replace('.apk','-patched.apk')

os.system("apktool b -o ./" + newapk + " .out &>/dev/null")

os.system("jarsigner -keystore ~/.android/debug.keystore -storepass android -keypass android " + newapk + " androiddebugkey &>/dev/null")

if os.path.exists(".out"):
	shutil.rmtree('.out', ignore_errors=True)

if os.path.exists(newapk):
	print "all good! now just adb install " + newapk
else :
	print "couldn't create patched APK, something went wrong. sorry! :("
