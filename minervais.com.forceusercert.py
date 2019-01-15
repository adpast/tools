import os
import sys
import shutil

#this script requires jarsigner and apktool
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

#some code loaned from overlaid.net
def replace_words(base_text, device_values):
    for key, val in device_values.items():
        base_text = base_text.replace(key, val)
    return base_text

f = open(".out/AndroidManifest.xml", "r")

xml = f.read()

xml = xml.replace('<application','<application android:networkSecurityConfig="@xml/network_security_config"')

f.close()

f = open(".out/AndroidManifest.xml", "w")

f.write(xml)

f.close()

newapk = sys.argv[1]

newapk = newapk.replace('.apk','-patched.apk')

os.system("apktool b -o ./" + newapk + " .out &>/dev/null")

os.system("jarsigner -keystore .keys -storepass 111111 -keypass 111111 " + newapk + " minervais.com &>/dev/null")

if os.path.exists(".out"):
	shutil.rmtree('.out', ignore_errors=True)

if os.path.exists(newapk):
	print "all good! now just adb install " + newapk
else :
	print "couldn't created patched APK, something went wrong. sorry! :("
