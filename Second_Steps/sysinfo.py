# coding: utf-8

# Let's retrieve some system infos

import sys

print(sys.executable)
print(sys.platform)
print(sys.version_info.major)
print(sys.version_info.minor)

major = str(sys.version_info.major)
minor = str(sys.version_info.minor)

python = (major+"."+minor)
print(python)