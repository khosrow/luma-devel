# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/base/gui/MainWinDesign.ui'
#
# Created: Tue Jul 6 14:26:01 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.11
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x98\x49\x44\x41\x54\x78\x9c\xad\x95\xcf\x4b\x54" \
    "\x51\x18\x86\x9f\x73\x67\xc6\x19\x1d\x33\x49\xfa" \
    "\x65\x30\x0a\x11\x29\x84\x45\x6d\xf2\x52\x84\x61" \
    "\xd4\xb6\xa0\x45\x7f\x47\xd2\xc2\x45\x0b\xa1\x32" \
    "\x88\x56\x05\x2d\xa2\x75\x10\x49\x42\x84\x61\xb4" \
    "\x48\xb8\x2e\x2a\x21\x51\xb2\x94\x48\x33\xad\x08" \
    "\xef\x8c\xa3\x73\xc7\x99\x7b\xce\xd7\xe2\x4e\xe9" \
    "\x38\xa6\x17\xea\x83\xb3\xb9\xbc\xe7\xe1\xbd\xef" \
    "\xf9\xce\x77\x94\xe3\x38\x84\xa9\xa3\xfd\xb6\xf8" \
    "\x06\x46\xcf\x3b\x2a\x8c\xde\x0a\x23\x3a\xf2\xc4" \
    "\x16\x63\xc0\xf8\xd0\xfa\xd0\x96\xff\x06\x06\x88" \
    "\xb4\x34\x10\x6d\x69\x40\x4c\x38\x7d\x28\xb0\x31" \
    "\x50\x75\xaa\x93\x44\x47\x27\xbe\xff\x9f\xc0\x6d" \
    "\x7d\xb6\x50\x07\xec\x9f\x40\x1d\x48\x63\xd5\x41" \
    "\xd3\x83\xad\xe3\xd8\x12\x6c\x04\xaa\x4f\xb4\x03" \
    "\x63\xc0\x0b\x6a\x4f\x9f\xc1\x14\xff\xd1\xf1\xa1" \
    "\xc7\xb6\x50\x05\xd6\xc9\xdd\x80\x06\x34\xf1\x8e" \
    "\x24\x12\x87\xbd\x77\x37\x77\x1d\x05\x68\x7f\x65" \
    "\x0b\x1a\xc4\x07\x5d\x04\xad\xc1\xf7\x41\x1b\x88" \
    "\xb7\xa6\x20\x3a\xb8\xba\xa3\xea\x35\x35\x6d\x29" \
    "\xd2\x43\x33\x34\xdc\xb6\xc5\x2f\xe9\xff\x2c\x03" \
    "\xba\xc7\x51\x4a\x7a\x11\x04\x68\x4c\x22\x1a\xd8" \
    "\xd9\x04\xf1\x6d\x48\xbc\x0e\x6b\xdf\x61\x68\xca" \
    "\x43\xf4\x4e\xb9\x9d\x95\x6e\xfc\xa9\x02\xb9\x8f" \
    "\xef\x28\x66\x17\x29\x66\xb2\x64\xa7\xa6\x11\x6d" \
    "\x58\x18\xf7\xd0\x1a\x94\xdc\x40\x88\x02\x17\xbb" \
    "\x20\xf5\x09\x64\xb8\x14\xee\x37\x20\x4c\xcb\x2a" \
    "\xb0\xf6\xc0\x52\x82\xe5\x97\x79\xc6\xef\xcd\x53" \
    "\xc8\x81\x72\x1c\x87\xe3\x83\xb6\xe8\x22\x44\xcf" \
    "\xd5\x43\x4b\x3a\x04\x6c\x4d\x69\x20\x1b\xc1\x1d" \
    "\xd0\xbc\x7f\x04\x62\xc0\xba\xe9\x28\xf5\xfb\x4a" \
    "\x1f\x7b\x6a\x8b\xf6\x21\x71\xb6\x1e\xd5\x1c\x12" \
    "\xee\x03\xe9\x04\xee\x70\x9e\x0f\xfd\x41\xc6\x56" \
    "\x6f\x70\xe5\xd5\xda\x59\xd1\xd6\x17\xc0\x6b\x3b" \
    "\xe2\x58\xa9\x95\xcd\xa1\x05\x60\xa9\x1a\x77\xc4" \
    "\x63\xf2\x19\xf8\x02\xea\xfa\xea\x1c\x29\x6b\xb7" \
    "\xd1\x0b\x8e\xd2\x1a\xdc\x81\x15\xcc\x18\xb0\xb8" \
    "\xc9\xca\x40\x76\xc4\x63\xf2\x39\x18\xca\xa1\x15" \
    "\x60\x80\x89\x4b\x01\xbc\xf8\x73\x0b\xb0\x07\xf9" \
    "\xef\x60\x34\xc8\xb5\xca\x89\x17\xdd\xe8\x2f\x8d" \
    "\x40\x2c\x06\x64\x37\x4f\xa3\x26\x11\xcc\x91\x8d" \
    "\xe6\xe8\xc6\x60\x0d\xd6\x5a\x70\x0e\x28\x02\xb5" \
    "\x40\x64\x55\x97\xdc\x1e\x68\x23\x15\x84\x0d\xa2" \
    "\x68\xba\x6f\x4b\xac\xaa\x04\x5d\x04\x66\x41\xe6" \
    "\xe0\xcb\x28\x4c\x0f\x81\xcc\x94\xbe\x67\x01\x0f" \
    "\x92\xd5\x50\xb8\x5c\x79\xbd\x2b\x1c\x1b\x0d\xb1" \
    "\x08\x90\x06\x96\xc0\xcd\xc0\x0f\x17\x0a\x3e\xf8" \
    "\x1a\xdc\xb7\xb0\x6b\x07\x34\x36\x97\x5c\xc7\xc0" \
    "\xd5\x21\xa2\xd0\x06\x62\x1e\x14\x72\x30\xbb\x0c" \
    "\xf9\x42\xd0\xf4\x4b\xdd\xc1\x01\x45\xae\xda\xf2" \
    "\xf9\x2b\xcc\xcd\xc3\xc1\x46\xa8\x89\x04\x2f\xcb" \
    "\x96\x60\x11\x70\x3d\xf0\xfc\xc0\x7d\xe6\x4a\xf9" \
    "\x89\xeb\x1e\x47\x29\x20\xd7\x65\xcb\x9b\x29\x48" \
    "\x46\x03\x33\xeb\xab\x22\x63\x63\xc0\xd3\xc1\x94" \
    "\x58\xe8\xfa\xfb\xc3\x19\xbb\xe5\x28\x11\xc8\xe4" \
    "\x82\x3d\xeb\xeb\x17\xac\x49\x3e\x2d\xa3\x1e\xca" \
    "\x0d\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x18\x00\x00\x00\x18" \
    "\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\x00\x00\x04" \
    "\xcc\x49\x44\x41\x54\x78\x9c\x95\x95\x5b\x6c\x14" \
    "\x65\x14\xc7\x7f\xdf\xcc\xec\xa5\xbb\x2d\xdd\x6d" \
    "\xbb\xdb\x42\x5b\x69\x1b\x0a\x85\x82\x05\xd1\x10" \
    "\x8a\x4a\x4c\x08\x91\x27\x2f\x7d\x20\x31\x31\xf1" \
    "\xd1\x98\x60\x7c\xf6\x8d\x37\x09\xea\x8b\x26\xc6" \
    "\x28\x89\x3e\x68\x54\xd2\x60\x8c\xd8\xf0\x40\x24" \
    "\x42\xb6\x86\x00\x82\x94\x2a\x6d\xa1\xb7\x6d\xbb" \
    "\x97\xee\x6d\x76\x77\xf6\x32\x3b\xf3\xf9\x50\xba" \
    "\xa5\xb0\x6d\xe2\xff\x61\x32\x33\xdf\x9c\xf3\xfb" \
    "\xce\xf9\x4f\xbe\x23\x42\xa1\x10\xb5\xf4\xf9\xed" \
    "\xaf\x65\xa1\x29\x42\x34\xa2\x92\x2d\x1d\xc1\xe1" \
    "\x3b\x84\x55\x31\xb1\x0d\x8b\xba\x72\x84\xb1\xc2" \
    "\x8f\xec\x29\xf6\x72\xe3\xe3\xcf\x00\x08\x85\x42" \
    "\xa2\x56\x1e\xf1\x24\x20\x14\x3b\x27\xef\x2f\x4c" \
    "\xf0\x30\xad\xe3\x6f\xee\xa6\xf5\xe0\x69\xf4\xce" \
    "\x6e\x32\xb9\x06\x62\x56\x98\x62\xb9\xc0\x44\xe4" \
    "\x4b\xac\xc9\x38\x8e\x99\x34\xde\x64\x91\xc6\x44" \
    "\x81\x89\x0b\x57\x6b\x42\xb4\xc7\x1f\xce\xfd\xf9" \
    "\x9d\x34\xbc\x1a\x6d\x47\xcf\x73\xd4\xa9\xa2\xb9" \
    "\x67\x50\xb9\xc8\x4c\x78\x14\xe1\x3b\xc1\x68\x66" \
    "\x94\x42\x3e\x88\x3d\x3f\x8f\x2a\xea\xb0\x9e\x09" \
    "\x90\xf4\x27\xf0\x98\x65\x4e\xbc\x75\x9c\xc1\xc1" \
    "\x41\xf9\x64\x35\xd5\x0a\xc6\xa5\x29\x6f\x26\xbc" \
    "\xf4\x1c\x38\x40\x7f\xd3\x30\xb1\x64\x33\xb9\xc2" \
    "\x0d\x92\xc9\x2c\x33\xfa\x25\xe2\xa6\xca\x98\xee" \
    "\x22\x6a\x7a\x11\x25\x3f\x58\x1a\xd2\x54\xb1\xa4" \
    "\x4d\x7f\x29\x85\xfb\xe6\x32\x75\x19\x95\xcb\x23" \
    "\x7f\xac\x6b\x99\x06\x70\xe1\xfe\x1d\x99\x6f\xdd" \
    "\x4f\xd7\xfe\x83\x6c\xf7\x25\x78\xd6\xfd\x05\x51" \
    "\xef\x02\x73\xaa\x1b\x4d\x34\x10\xd7\x25\x19\xdb" \
    "\x81\x47\x11\x08\x55\x60\x6b\x15\x14\x5b\x05\x21" \
    "\x41\x0a\x4a\xd2\x41\x6f\x5f\x80\xf1\xab\xf3\xec" \
    "\xd8\xdb\xcf\xd4\xd8\xbd\x6a\x57\x14\x80\xba\x86" \
    "\x6e\x02\xdb\x77\x71\xc0\xf7\x33\x9d\x0f\x5a\xf8" \
    "\xe9\xd2\x5e\xbe\x3f\x5f\xc7\xc4\x78\x81\x7b\xd7" \
    "\x9a\xd1\x67\x9b\x11\xd8\x78\x55\x1b\x2c\x0d\x84" \
    "\xbd\x12\x2a\x00\xdb\xa2\x20\x05\x9a\xd3\x41\x47" \
    "\xdb\x56\xc2\xc5\x95\xc4\xab\xed\x52\x7e\x4d\x8f" \
    "\xcb\x05\xcf\x33\x74\x77\xf8\xe9\xf5\xde\xa5\x61" \
    "\xdb\x49\x8e\x1c\x3b\xc5\xee\x43\xa7\x11\x4a\x3b" \
    "\x1d\x7b\x5d\x0c\xbe\xd9\x85\xa7\x5e\xa5\x68\x09" \
    "\x50\x2d\x90\xf0\xe8\x02\x08\x6c\x55\x80\x05\x3d" \
    "\x9d\x4d\x3c\xdf\xdd\xc2\xae\x7d\x7d\x55\x88\x36" \
    "\xfd\x8f\x93\xce\x63\x3e\x5e\xa8\xff\x94\xe5\xe8" \
    "\x59\xa2\x7a\x85\x6c\xf8\x21\x03\x03\xa3\x44\x12" \
    "\x7d\x84\x63\x97\xf9\xeb\xce\x37\xe4\xb2\x1a\x65" \
    "\xe1\xc4\xb6\x35\x14\xd4\x47\xbb\x17\x20\x25\x5e" \
    "\x33\x8b\x90\x6e\xa4\x52\xc2\xa1\x98\x44\x72\xea" \
    "\xda\x5f\xd4\xd8\xec\x67\x47\x7b\x9c\x89\xf0\x0f" \
    "\xe8\x71\x2f\xb6\xa8\xa3\x54\x89\x30\xbf\xf0\x2a" \
    "\x49\xab\x9e\xb8\xad\x60\x14\x15\x8a\xa9\x22\xce" \
    "\x72\x3f\xaa\xb1\x84\x55\x31\x11\x0e\x0b\xa9\x7a" \
    "\x90\x02\x3c\xd2\x83\xb0\xc0\x2a\x5a\xa4\x7c\xbb" \
    "\xf1\xf8\xc6\xc8\xac\x02\x32\x6a\x1d\x4e\xc7\xb7" \
    "\xdc\x5f\xcc\xa2\x58\xcd\xb8\x14\x49\xae\xa2\xb0" \
    "\x34\x15\x43\x37\x97\x49\x2e\x0c\x60\xfb\x4e\xb0" \
    "\xe4\xfa\x0d\x7f\xdf\x4b\x0c\xa4\x7c\xa4\x63\x2e" \
    "\x12\x91\x3b\xa4\x94\xeb\x20\x6c\x0a\x61\x37\x69" \
    "\x67\x89\x16\xf7\x16\x5c\xad\x3b\xf1\x4e\xfe\xbd" \
    "\x56\x81\xae\x78\x98\x9c\xbd\x4d\x25\xe7\x44\xa8" \
    "\x0e\x90\x20\xa5\xc0\xb0\x54\xf2\x52\x50\x6c\x48" \
    "\x63\xcf\x6d\x65\x6a\x26\x49\xf6\xda\x19\x1a\x23" \
    "\x8d\x74\x1c\x3e\x45\xa3\xec\xc1\xb8\x7b\x1d\x3b" \
    "\xf9\x2f\x8b\x81\x93\xe8\xb1\x29\x6c\x63\x0a\xb7" \
    "\x88\xb0\xb0\x9c\x5f\x03\x98\xa6\xc1\x7c\x78\x88" \
    "\xdc\xf4\x27\x34\xb6\xd6\xa3\xd6\xbb\xb1\xa5\x46" \
    "\xc9\x14\x14\x2c\x58\xb4\xa3\xe8\xf3\xbf\xf0\xe0" \
    "\xc3\x5a\x47\xca\xd1\x1a\xef\xd6\x14\x0c\x06\xd1" \
    "\xac\x0a\x78\x76\xbf\x87\xbf\xed\x75\xb2\xe1\x8b" \
    "\xcc\xc7\xbf\x82\x7a\x05\xc3\x14\x64\x84\xca\x92" \
    "\xed\x41\xaf\x2c\x03\x10\x08\x04\x10\x42\x20\xa5" \
    "\xdc\x34\x31\x40\x3c\x1e\x5f\xa9\xc0\xca\x99\x44" \
    "\x8b\x36\x01\xff\x36\x9c\xde\xb7\x89\xde\x1b\x25" \
    "\x51\x9c\xa6\x8c\x83\x9c\xe5\xc2\xb2\x1d\xd8\xf9" \
    "\xc4\x86\x89\x86\x86\x86\xaa\xf7\x86\x61\x30\x32" \
    "\x32\xb2\x6e\x5d\x5b\x0c\x87\x29\x87\x63\x88\x9e" \
    "\x36\xdc\xaa\x9b\x82\x7b\x90\xa8\xbe\x84\x22\x3c" \
    "\x08\x5b\x45\x29\x83\x96\xf1\x6e\xba\xdb\xe1\xe1" \
    "\x61\x72\xf1\x59\x1a\x82\x5d\x4f\xad\x29\xed\x6a" \
    "\x81\xc4\xc2\x22\x09\x13\x12\x15\xe8\x68\x7d\x0d" \
    "\x4c\x0d\xb5\x5c\x87\x28\x7b\xa0\xa2\xe2\xf1\xef" \
    "\x59\x17\x24\x84\x40\x88\xb5\x83\x33\x17\x9f\x45" \
    "\x9f\xbe\x52\x13\xae\xfc\x7e\xe6\x7d\xb4\xf1\x5b" \
    "\xa4\x1f\x44\xc9\x95\x41\xaf\x28\x08\x0b\xec\xb2" \
    "\x0b\x59\x51\xb1\x4a\x36\xc5\x5c\x64\x5d\x90\x94" \
    "\xb2\xea\x83\x61\x18\x34\x04\xbb\x68\x3f\xf4\x4e" \
    "\x6d\x40\x28\x14\x12\x3b\x65\x9e\xdc\xe8\x15\x52" \
    "\x11\x93\x72\xce\x87\x23\xed\x45\x5a\x16\xd2\xae" \
    "\xe0\x4d\xb9\xd9\x12\x3c\xbc\x61\x7b\x46\x46\x46" \
    "\xaa\xc0\x5a\xe6\xaf\x9c\xa6\x67\x3f\xa0\xe3\x8d" \
    "\x77\xc9\x09\x27\xee\x7d\x2f\xd3\xd2\x76\x8a\xe4" \
    "\xd2\x47\x38\x8a\x92\x2d\xca\x73\x94\x69\xda\x10" \
    "\xb0\x6a\xb2\x61\x18\x55\xe0\x53\x80\x50\x28\x24" \
    "\x06\x07\x07\x65\x6b\xbe\x44\x3e\x3c\x89\x63\xe0" \
    "\x38\xad\xf9\x01\xd4\xbc\x45\xba\xfd\x15\x8c\xb9" \
    "\x5b\x1b\x02\x60\x73\x93\xab\x13\x6d\x15\xd2\xf9" \
    "\xe2\x1e\xe2\x73\x0f\x49\x05\xb6\x23\x3a\x7a\x91" \
    "\xa9\x12\x4a\x7a\xbd\x07\xab\x06\xaf\xb6\x64\x33" \
    "\x93\xd7\x8d\xcc\x55\x08\x8c\xe3\xec\x1a\xc0\xdd" \
    "\xe0\x43\xb6\x74\x51\x5a\x9a\xae\x7e\xf3\x64\x9f" \
    "\x57\x4d\xde\x48\x4f\x0d\x7d\x58\x1b\x16\x8f\x2b" \
    "\x16\x8b\x6d\x98\x64\x23\x05\x83\xc1\xda\x80\xcd" \
    "\x40\xff\x57\xff\x01\xd4\xfb\x58\xa3\x77\x5e\x4e" \
    "\xa0\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
image2_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x04" \
    "\xea\x49\x44\x41\x54\x78\x9c\xa5\x95\xcd\x6f\x1d" \
    "\xd5\x19\xc6\x7f\xe7\x63\x66\xee\xc7\xdc\x7b\x6d" \
    "\x7c\x6b\x82\xe3\x38\xb5\x1d\xe2\x88\xc4\x8b\x46" \
    "\x6a\x24\x6e\x04\x72\xcb\x86\x02\x0d\x48\x20\xc4" \
    "\x02\x51\x29\xea\x0a\x75\xd1\x5d\x2b\xb1\x60\x01" \
    "\x11\x7f\x00\x12\xbb\x20\x8a\x54\x5a\xa9\x6a\x69" \
    "\x41\xad\xda\x42\x54\x9a\x2a\x23\x95\x0a\x2b\xa0" \
    "\x8a\x18\x4a\x82\x9d\x98\xf8\x3a\xb6\x13\x7f\xdc" \
    "\xaf\xb9\x33\x73\x5e\x16\xe3\xeb\xa4\x6c\x99\xcd" \
    "\x39\x33\x9a\xf3\x9c\xe7\x7d\xcf\x73\x9e\x47\x45" \
    "\x51\xc4\xc9\x46\x43\x0c\x70\x3e\x8a\x14\xdf\xf2" \
    "\x79\xb0\xd1\x90\x0c\xb0\x83\x0f\xe7\xa3\x48\x9d" \
    "\x7d\x64\x4e\x0e\x04\x16\x09\x43\xb4\xd6\x88\x00" \
    "\xc8\xed\x55\x22\x77\x4c\x07\x73\xc1\x39\xc1\xf6" \
    "\x62\xae\xc6\x29\xe7\xa3\x48\x9d\x6c\x34\x44\x01" \
    "\x12\x45\x91\xfa\xe3\x63\x3f\x90\xc7\x8e\x4e\x51" \
    "\x9b\x7b\x80\xe2\x48\x15\x97\xc4\x38\x27\x80\x43" \
    "\x21\x80\x42\x70\x20\x0e\xc9\x32\xc4\x39\x44\x1c" \
    "\x20\x88\x08\x9d\xe6\x3a\xdd\xf9\x05\xfe\x7a\xb9" \
    "\xc9\xe3\xef\x9c\x53\x2a\x8a\x22\x5e\x7f\x64\x4e" \
    "\x9e\x9b\x9d\xa6\xf4\xd4\x29\xe2\xe6\x22\xdd\x95" \
    "\xeb\x08\x82\xb2\x06\x6d\x2d\x2e\x4b\x70\x49\x0a" \
    "\x4a\xd0\x9e\x87\x2d\x96\x30\x9e\x8f\x28\x50\x5a" \
    "\xa3\xb4\xc6\xab\x86\xf4\x76\x62\xdc\x7b\x1f\xf2" \
    "\xd6\x17\x2b\x79\x2b\xc6\x03\x4b\x6d\xee\x01\x5a" \
    "\xcd\x45\x36\x2f\xce\x63\xc3\x10\xe5\x7b\x48\x3f" \
    "\x23\xe9\x77\x09\xf7\x4d\x50\x9d\x9e\xc2\x86\x15" \
    "\xd2\xce\x0e\xad\xe6\x12\xbd\xad\x0d\xfc\xb0\x86" \
    "\xb2\x16\x44\x48\x36\xb7\x29\x0c\x55\x49\x67\xa7" \
    "\x18\xbf\xb6\x96\x03\x4b\x18\x52\x1c\xa9\xb2\x76" \
    "\xf1\x12\x36\x0c\xd1\xc5\x02\x2e\x89\x09\xf7\x8d" \
    "\x73\xe8\x89\xd3\x54\x66\xbe\x47\x71\xf4\x00\xa2" \
    "\x14\xb8\x8c\x4e\x73\x89\x9d\x85\xff\xf0\xe5\xfb" \
    "\xbf\x23\x4b\xfb\x18\x3f\x00\xa5\xc8\xe2\x84\x62" \
    "\xbd\x42\x1a\x78\x39\xb0\xd6\x1a\x97\xc4\x79\xf9" \
    "\xbe\x87\x4b\x7a\x8c\x1c\x9e\xe5\xd8\xcf\x5e\x21" \
    "\xa8\x8f\x41\xda\x67\x67\x69\x81\xf6\xfa\x0a\x95" \
    "\xb1\x49\xca\x63\x53\x94\xc7\xa6\xa8\x1c\xf9\x3e" \
    "\x0b\x6f\x9e\x21\x6e\x6d\xa1\x6d\x00\xc6\x80\x08" \
    "\x6a\xa0\x0a\x11\x70\x2e\xef\xa9\x8b\x53\x6a\x07" \
    "\x0e\x71\xf4\xf9\x33\x04\xf5\x31\x76\x3e\x9f\x67" \
    "\xf1\xcf\x6f\xd2\xfa\xea\x0a\xa6\x58\x06\x97\x52" \
    "\x3b\x34\xcb\xc1\x1f\x9f\xa6\x3c\x36\xc5\xcc\xb3" \
    "\xbf\xe0\xd2\x1b\x2f\x93\x89\x43\x59\x8d\x64\x0e" \
    "\x04\xf4\x40\x32\x0a\x87\x36\x06\xc9\x12\xa6\x9e" \
    "\xfc\x29\x85\xd1\x71\xb6\x3f\xfd\x90\x4f\x5e\x7b" \
    "\x81\xd5\x8f\x2f\x30\x3e\xf7\x04\x27\x5e\xfa\x0d" \
    "\xe1\xe4\x51\xbe\xfa\xf7\x7b\x2c\xfc\xea\x0c\xfd" \
    "\xad\x55\xc2\xf1\xc3\xec\x6f\xfc\x08\x97\xf6\x51" \
    "\xc6\xee\x29\x45\xdf\x29\xee\x2c\xe9\x33\x3c\x79" \
    "\x84\xe1\xc3\xc7\xc1\x65\x7c\xf1\xce\x59\xe2\x4e" \
    "\x8b\x60\xb8\x4e\x69\x64\x14\x80\xe2\x5d\x75\x0a" \
    "\x23\xa3\xb4\x56\x97\x59\xfe\xdb\xaf\x01\xa8\x1d" \
    "\x39\x41\x50\x19\xca\xb5\x2d\x72\x27\x63\x40\x81" \
    "\x4b\x13\xca\xfb\x27\xb1\x43\x75\x6e\x5e\xfa\x88" \
    "\xed\x2f\x17\xf0\x6b\xc3\x20\x0e\xe7\xdc\xa0\x38" \
    "\x10\xc1\x14\x43\xb6\x97\xff\x47\xff\xd6\x2a\xe5" \
    "\xef\xec\xa7\x5c\x1f\xdb\x03\x95\x3d\xc6\x92\x8b" \
    "\x5c\x29\x41\x15\xc3\x3d\xf6\xce\x25\x68\x63\x40" \
    "\x69\x94\xda\xe5\x60\x34\x68\x8d\xf6\x2c\xce\x65" \
    "\xa4\x49\x1f\x74\xae\x77\x65\x2c\xfc\x7f\x8f\x01" \
    "\x71\x28\xcf\x83\xb4\x97\xaf\x0f\x02\x6c\xa1\x94" \
    "\x83\x1a\xb3\xf7\xa7\x52\x3a\x07\xd0\x1a\x1b\x14" \
    "\xb1\x7e\x00\xce\xa1\x8c\x45\x1b\x0f\x71\xdf\xe8" \
    "\xb1\xb8\x0c\xe3\x07\xf4\x6f\xdd\xc0\x75\xb7\xb9" \
    "\x6b\xe6\x38\xb5\xe9\x63\xa4\xbd\x36\xa6\x50\x40" \
    "\x1b\x2f\x07\x36\x06\x13\xf8\x64\x49\x4c\xb8\x7f" \
    "\x1a\x7f\x68\x94\xce\xc6\x0a\xf1\xce\x26\xb6\x50" \
    "\xcc\x81\x07\x8c\x45\x04\xc9\x32\x6c\x29\x64\xf3" \
    "\xea\xe7\x6c\x5e\xfe\x14\xb4\x61\xfa\xd1\xe7\x08" \
    "\x2a\x55\x92\x4e\x8b\x24\x6e\x03\x90\xc6\x5d\xfa" \
    "\xed\x6d\x2a\xf7\x1c\x64\xfc\xa1\x67\x00\xe8\x35" \
    "\x2f\x93\xf6\x7b\x68\x2f\x40\x9c\x00\x72\xdb\xdd" \
    "\x44\x1c\x4a\x2b\xb4\x5f\x60\xe9\x2f\x6f\x50\x3b" \
    "\x38\x43\x78\xef\x71\xee\x7b\xf6\x97\x2c\x9e\xfb" \
    "\x2d\xd7\xfe\xf5\x2e\x37\x3e\xb9\x40\xd2\xd9\x66" \
    "\xf4\xd8\xfd\x1c\x7c\xf8\x27\xf8\xb5\x51\xba\xab" \
    "\x4b\x34\x3f\xfa\x07\x5e\xa9\x8a\x73\x82\x64\x0e" \
    "\x91\x3d\xdb\xcc\x77\x41\x29\x4c\x50\xa4\xb5\x7a" \
    "\x95\xcb\xbf\x7f\x95\x43\x4f\xff\x9c\xca\xe1\xe3" \
    "\xdc\x37\x31\x43\x7b\x65\x91\xb8\xb3\x4d\x69\x78" \
    "\x94\xf2\xdd\x13\x60\x3c\xe2\x5b\xab\x5c\x3b\xf7" \
    "\x16\x59\x96\x61\x0a\x05\x54\x96\xed\x5a\xeb\x2e" \
    "\x63\xe7\x76\x55\xa1\x35\x48\xde\x92\xb5\xcf\xe6" \
    "\xe9\x9d\x7d\x91\xf1\x07\x1f\xa7\x32\x39\x4b\x75" \
    "\xf2\xe8\xae\x72\xa0\xbf\xb9\x4e\x7b\xe9\xbf\x34" \
    "\x2f\xfe\x93\xb4\x1f\xa3\xfd\x02\xda\x7a\xb8\x4c" \
    "\x48\xdb\x5d\x04\x95\x03\xdb\x5e\x4c\xa7\xb9\x8e" \
    "\x37\x51\x27\xd9\xdc\x01\xa5\xb0\x85\x32\xed\x8d" \
    "\x26\x9f\xfd\xe1\x35\xc2\xbb\x0f\x50\xbe\xe7\xbb" \
    "\x28\xeb\xa1\x11\xba\x1b\x4d\x7a\xad\x2d\x6c\xb1" \
    "\x82\x09\xca\x68\xeb\x61\x8a\x21\xdd\xb5\x2b\xb4" \
    "\xaf\xdf\xc0\x1f\x00\x2f\xc7\x29\xdd\xf9\x05\xf4" \
    "\xf0\x09\x0a\x43\x55\xb2\x38\x41\x8c\x46\x5b\x1f" \
    "\x65\x0c\xed\xad\x0d\xda\xb7\xd6\x50\xd6\xa2\x8d" \
    "\x8f\x2d\x95\x30\x85\x72\xee\x31\x59\x86\xcb\x84" \
    "\xee\xda\x15\xae\x7f\xf0\x01\xc1\xcd\x36\xcb\xfd" \
    "\x94\xbd\x04\xf9\xd3\xa9\x87\xe4\xe1\xc9\x7d\xf8" \
    "\xb3\x53\x14\xeb\x95\xfc\xd2\x64\xbb\x29\x21\x03" \
    "\xa7\x92\x3c\x39\x5c\x86\x64\xb2\x6b\x38\x79\xf9" \
    "\xed\xeb\x37\xd0\x37\xdb\x9c\x5b\xef\x70\xea\xed" \
    "\xbf\xe7\x09\x72\xb2\xd1\x90\x0b\x51\xa4\xce\x3e" \
    "\xfa\x43\x99\x08\x2c\x69\xe0\xa1\x06\x67\xca\xed" \
    "\x6b\x7a\xe7\x7b\x1e\x49\xbb\x23\x0a\x1f\xc5\xb5" \
    "\x38\xe5\xf4\xbb\xef\xab\x93\x8d\x86\x7c\x0d\x91" \
    "\x50\x6c\x1b\x62\x01\x71\x90\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
image3_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x03" \
    "\x6b\x49\x44\x41\x54\x78\x9c\x9d\x94\xcd\x4f\x5c" \
    "\x55\x18\xc6\x7f\xe7\xde\x3b\x77\x60\xbe\x81\xb1" \
    "\x23\x85\xd4\xa6\x4d\xb1\x46\x62\x1b\x57\x0c\x11" \
    "\xbb\xe8\xa2\x4c\xd2\xe8\x4a\x63\xe2\xaa\xd1\xba" \
    "\x73\xe3\x3f\x42\x37\xed\x4a\xf0\x1f\x30\x31\xe9" \
    "\xa6\xb1\xa1\x9a\xa2\x8c\x61\x4c\x06\x07\xb0\x54" \
    "\x5a\xc3\x88\x2d\x30\x96\x41\x66\x80\x7b\xe7\x9e" \
    "\xfb\x71\x5c\x00\xa3\x7c\x85\xa9\x4f\xf2\x6e\x9e" \
    "\x73\xce\x2f\xef\xf9\x7a\x44\x3e\x9f\xe7\xbf\xaa" \
    "\xd7\x85\x4a\x26\xa3\x74\x76\x26\xb1\x6d\x87\x7a" \
    "\x7d\x1b\xcb\xb2\x09\x02\x45\x2a\x25\x04\x2d\xca" \
    "\x38\x68\x48\xe9\x12\x0e\x9b\xf4\xf5\x9d\x69\x7a" \
    "\xd5\x6a\x8d\xe9\xe9\xdf\xa8\x54\x6c\x95\xc9\x98" \
    "\x2d\xc1\xb5\x83\x46\x3a\x6d\x88\xa7\x4f\x9f\x51" \
    "\x28\xfc\xda\xf4\xba\xba\x92\x5c\xb9\xf2\x36\x91" \
    "\x48\x1b\x4b\x4b\x5b\xea\x7f\x81\x01\x7a\x7b\x23" \
    "\x62\x61\x61\x89\xc9\xc9\x52\xd3\x0b\x85\x0c\x06" \
    "\x06\xfa\x91\xd2\x6d\x85\x8b\x36\x3b\xbb\xaa\x66" \
    "\x66\x56\x0e\x75\x71\xfe\x7c\x4a\xcc\xcf\x2f\x52" \
    "\x2a\x3d\x69\x7a\xf1\x78\x84\xd3\xa7\xd3\xcc\xce" \
    "\xae\x9e\xd8\xb5\x66\x9a\x21\x84\x10\x14\x0a\xe5" \
    "\x7d\x93\x0b\x85\xb2\x8a\x44\xda\x39\x77\xae\x07" \
    "\xcf\xf3\xf1\x3c\x1f\xdf\x0f\xe8\xe8\x48\xe0\x38" \
    "\xf2\xe4\x8e\x4d\xd3\x60\x78\x38\x8b\x10\x82\x89" \
    "\x89\x05\x05\x30\x31\xb1\xa0\x12\x89\x28\xd7\xae" \
    "\x0d\xa0\xeb\x1a\x52\xba\x38\x8e\xc4\x71\x24\x86" \
    "\xa1\xd3\x68\xb4\x00\x6e\x34\x24\x89\x44\x94\x5c" \
    "\x6e\x10\x21\x04\xf7\xef\xcf\xed\x42\xb3\x68\x9a" \
    "\x86\xe3\xb8\x38\x8e\x8b\x94\x1e\x52\x7a\x3c\x7f" \
    "\xfe\xa2\xb5\x8e\xd7\xd6\x36\xd8\x81\xc7\xc8\xe5" \
    "\x06\xe9\xee\x4e\x33\x3c\x9c\x45\xd7\x75\xa4\x74" \
    "\x0f\xd5\xe2\xe2\x32\xb6\xed\x9c\x0c\xae\x54\xd6" \
    "\x29\x16\x1f\x23\xa5\x4b\x2a\x15\x27\x97\x1b\xc4" \
    "\x30\x0c\xa4\x94\xfb\xca\xb2\x1a\x94\xcb\xcb\x5c" \
    "\xba\x74\x01\x80\x57\xa6\x6f\xaa\x74\xf1\xe6\xb1" \
    "\x97\xa8\x49\xe9\x32\x3e\x5e\x60\x6d\xed\xef\xe6" \
    "\xb6\x77\xca\x6b\x96\x6d\x4b\xca\xe5\x65\x36\x37" \
    "\x2d\x94\x52\x7c\xf8\xe6\x1c\x66\x26\x84\xeb\x41" \
    "\x7c\xea\xd3\x7d\xf0\x6c\x36\xab\x00\x44\x3e\x9f" \
    "\x67\x6c\xec\x3b\x15\x89\xb4\x31\x34\x74\x99\xbe" \
    "\xbe\x33\x18\xc6\xde\x87\xdc\x59\x63\xdb\x0e\xae" \
    "\xeb\x11\x0a\x19\x88\xf9\xdb\x24\xe4\x03\xc2\xeb" \
    "\xab\x84\xfa\x7b\x59\x99\x0b\x08\x02\x90\x43\x5f" \
    "\xee\xfb\x91\x62\x2f\x2b\xee\xdc\xb9\xa7\x94\x52" \
    "\x74\x76\x26\xc9\x64\x3a\x89\xc5\xda\xa9\xd5\xb6" \
    "\x90\xd2\xe3\xfa\xf5\x77\x48\x26\x63\xd8\xc5\x5b" \
    "\x44\xad\x6f\xe9\xb0\x2a\xa4\x75\x97\x1a\x21\xec" \
    "\xb3\x3d\x2c\xcd\x28\x82\x00\xc4\xd5\x7f\xe1\xe2" \
    "\x60\x08\x8d\x8c\xdc\x3d\x74\x6e\x99\x4c\x17\x1f" \
    "\x5d\x2e\x93\x72\xc7\xe9\x36\xab\xa4\x4c\xd0\x76" \
    "\x11\x75\x4f\xb0\x99\x4c\xf3\xe4\x17\x41\x10\x28" \
    "\xda\x73\xa3\xe2\x48\xf0\x51\x5a\xfe\xe6\x73\xf5" \
    "\x5a\xaf\xcd\xc5\x9e\x0d\xa2\xa6\xce\xc1\x8c\xb3" \
    "\x1c\x9f\xaa\x8a\xf3\x68\x5a\x23\x08\x20\xf5\xde" \
    "\xa8\x38\x94\x6e\x47\xa9\x5d\xb3\x58\x7d\x06\x99" \
    "\x4c\x9c\xd8\xa9\xdd\x0d\xed\xd1\xa5\x4f\x24\xa2" \
    "\x08\xfb\x12\xd1\x1f\xa2\x58\xd4\xa9\x7c\xfd\x89" \
    "\x3a\x32\x84\x0e\xaa\xe3\xfd\x51\x21\x3d\x98\xfa" \
    "\x49\xa3\xfc\x27\x90\x68\x83\x64\xfb\xce\xa0\xe3" \
    "\x42\xa5\x8e\xbe\x52\xa3\x37\x6e\xf3\x46\x9f\x8b" \
    "\xeb\x1f\x93\x6e\x47\xa9\xfb\x83\x51\xe1\x7a\x8a" \
    "\xc9\x1f\x35\x7e\x2f\x35\x20\x16\x86\xcd\x06\x6c" \
    "\x39\xf0\x62\x13\xdc\x00\xfe\xa8\x72\xe1\x55\x9b" \
    "\x90\xe1\xb7\x0e\x06\x38\xfb\xf1\x98\x70\x3d\x78" \
    "\x38\xa1\xb1\xf0\xfd\x3a\xf8\x01\x44\x4d\x68\x78" \
    "\x60\x39\x3b\xaf\xd3\x96\x98\x7a\xf0\x72\x60\x80" \
    "\xd7\x6f\x8c\x09\xd7\x87\x07\x0f\x75\x1e\xcf\x79" \
    "\xb0\x61\xc1\xd5\x8b\x70\x2a\x0e\x51\x13\x67\xcb" \
    "\x67\xa5\xaa\xbd\x3c\x18\xe0\xad\xcf\xc6\x84\xf4" \
    "\x14\xf7\x4a\x09\x8a\x8f\x0c\x98\x5a\x84\xf5\x6d" \
    "\x9c\x6d\x9f\xbb\x3f\x27\xa8\x5b\xa2\xb5\xe7\x76" \
    "\x9c\x7e\x18\xb9\xa1\x82\x00\x12\x61\x8f\x64\x9b" \
    "\xc7\x5f\xdb\x26\xd2\xd7\x78\xf7\x8b\xaf\xc4\x3f" \
    "\x48\x07\xb7\x36\xa3\xf2\x2c\xed\x00\x00\x00\x00" \
    "\x49\x45\x4e\x44\xae\x42\x60\x82"
image4_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x03" \
    "\x29\x49\x44\x41\x54\x78\x9c\xb5\x95\xdf\x6b\x13" \
    "\x59\x14\xc7\x3f\x93\x64\x26\x69\x9a\xb6\x53\xd4" \
    "\xda\xba\x41\x93\xad\x82\xcd\x62\xca\xae\x10\x65" \
    "\xb4\x74\x15\xf4\xc1\x87\x52\xc4\x85\xfa\xd4\xc7" \
    "\x42\x7d\x12\xc1\xbf\x40\xc1\xf7\xe2\x83\x82\x5b" \
    "\x41\x7c\x10\xdf\x05\x8b\x96\x8a\x18\xad\x82\x3f" \
    "\x1e\xda\x2d\xb6\xe4\x47\xcd\x64\x57\xbb\x76\xdb" \
    "\x49\x27\xc9\x24\x9d\x8c\x0f\x0d\x53\xc7\x4e\x56" \
    "\x17\xdc\x33\x5c\x18\xce\xb9\xf7\x73\xbe\x67\xee" \
    "\xbd\x67\x84\x64\x32\xc9\xff\x61\xbe\x7f\x0b\x2a" \
    "\x37\x14\x8b\x1a\x60\x02\x35\xc0\x72\xc6\x93\xe7" \
    "\x92\x42\xa3\xb5\x82\x9b\x62\x65\xbc\x0e\xf4\x02" \
    "\x61\x60\x27\xf4\x87\xfb\x01\x78\xf3\xe7\x1b\x56" \
    "\x72\x2b\x90\x05\x2a\x8d\x13\x6c\x01\x2b\xbf\xd7" \
    "\xa1\x07\x60\xa8\x7f\x88\xd1\x1f\x47\x89\x87\xe2" \
    "\x8e\x39\xd9\x72\x96\xdb\x8b\xb7\xb9\x36\x71\x8d" \
    "\xd5\x17\xab\xae\x70\x07\x58\xb9\xa1\x58\x78\x61" \
    "\xff\xa9\xfd\x5c\x39\x7a\x85\x58\x73\xac\x51\xa5" \
    "\x00\x68\xeb\x1a\x17\x1f\x5f\x64\xf2\xee\x24\x54" \
    "\x9c\x70\x1b\xac\x5c\x57\x2c\x2c\xe8\x1e\xec\x66" \
    "\xac\x7f\x8c\x16\x6f\x0b\x00\x33\xe9\x19\x42\x42" \
    "\x88\xc8\xb6\x08\x99\xbf\x33\x74\x76\x75\xe2\x0f" \
    "\xf8\x1d\x09\x2e\x3d\xbd\xc4\xfd\x5b\xf7\x1d\xca" \
    "\x37\x37\xcf\x84\xe0\x2f\x41\xce\x1f\x3a\x8f\x5e" \
    "\xd3\x99\x55\x67\xd9\xe7\xd9\xc7\x48\xef\x88\x3d" \
    "\xe5\xc8\x0f\x47\xa8\x5a\x55\x1e\xac\x3e\x40\x37" \
    "\x75\xdb\x3f\xf4\xf3\x10\x2f\xdf\xbe\x64\x69\x7a" \
    "\xc9\xf6\x79\x00\x94\xab\x8a\x85\x0f\xfa\x8e\xf6" \
    "\x61\x62\x92\xd2\x52\xf4\xb5\xf6\x31\x10\x1b\xd8" \
    "\x52\xbe\x28\x88\x94\xcc\x12\xf9\x4a\xde\x1e\x9a" \
    "\xa9\x31\x70\x6c\x00\xa4\x3a\xcb\xa1\x78\x0f\x44" \
    "\xe4\x08\xf9\x4a\x9e\x8e\xe5\x0e\x12\x07\x13\x76" \
    "\xe8\x91\xf6\x88\x74\x39\x4d\x97\xd4\x45\xa9\x56" \
    "\xe2\xf9\xda\x73\x3b\x36\xbb\x36\xcb\xbc\x3e\x4f" \
    "\xa6\x98\x81\x3d\xc0\xfc\x86\xdf\x06\xb7\xef\x6e" \
    "\x47\xb7\x74\xf4\x8a\xce\x70\x78\xd8\x5e\x78\x39" \
    "\x77\x99\xb9\xd2\x9c\x43\x75\x71\xa5\x48\xdb\x7a" \
    "\x1b\x3b\xe4\x1d\x14\x0a\x05\xe6\x8a\xf5\x78\xa7" \
    "\x0b\xd8\x0a\x59\xa8\x15\x15\x80\x9e\x9d\x3d\x00" \
    "\x2c\x94\x17\x78\xb8\xfa\x70\xe3\x13\xac\x89\x9c" \
    "\x68\x3a\x41\x3c\x18\x27\xf1\x53\x02\x39\x28\xdb" \
    "\x89\x84\xc9\xfa\x61\x68\xd9\x4c\x6e\x83\x0d\xcb" \
    "\x20\x57\xc9\x39\x94\x2d\xaf\x2f\xdb\xbe\x91\xa6" \
    "\x11\x2e\xc4\x2f\xf0\xad\xe6\xb1\xc1\x05\x03\xd5" \
    "\x50\x51\x0d\x95\xac\x91\x05\x20\x11\x4a\xb0\xdd" \
    "\xb7\x9d\xc5\xf2\x22\xaa\xa4\x36\xa6\x88\xf5\x51" \
    "\x74\x01\xd7\xfe\xaa\x51\xaa\x3f\x37\x97\x6e\xda" \
    "\x13\xee\x75\xdf\xe3\xac\x70\x96\x57\xef\x5e\x91" \
    "\xd1\x32\x5b\x98\x53\xda\x14\x48\x6c\x8c\xf7\x9b" \
    "\xfe\xcd\x53\x91\x02\xcf\x71\x0f\xf8\x61\x6c\x79" \
    "\x8c\xc1\x6d\x83\xf4\x36\xf5\x22\x07\x65\xc6\x0f" \
    "\x8f\x37\x14\x2b\x78\x04\xbc\xa2\x17\x0c\x30\x53" \
    "\xa6\x53\x71\xf2\x5c\x52\xc0\x00\xe9\xb5\x84\xec" \
    "\xdb\xd8\x94\xd3\xa9\xd3\x24\x75\xf7\x96\x3a\x53" \
    "\x9e\xb1\xdf\xa7\xf5\x69\x64\x9f\x8c\xf4\x5a\x02" \
    "\xc3\xed\xe6\x01\xa5\x27\x25\xda\x23\xed\x04\x77" \
    "\x07\x01\x18\xce\x0c\x13\x0b\xc4\x38\xd9\x7a\x12" \
    "\x00\xcd\xd4\x98\x28\x4c\x90\xab\xe4\x38\x23\x9f" \
    "\x21\x2c\x85\xb9\xf3\xcf\x1d\xfc\xaa\x9f\x8f\x4f" \
    "\x3e\x3a\x2b\x71\x34\xa1\xab\x8a\xe5\x0d\x78\xd9" \
    "\xfb\xdb\x5e\x5a\x23\xad\x0d\xcb\xff\xdc\xb4\x8c" \
    "\xc6\xc2\xdd\x05\xcc\xb2\xe9\xde\x84\x3e\x87\x03" \
    "\x44\x7f\x8d\x12\x3d\x1c\x45\x0c\x88\xae\xc0\x6a" \
    "\xb9\x4a\xfa\x59\x9a\xf4\x54\x1a\xf8\x4a\xdb\xfc" \
    "\x12\x2e\x06\x44\x76\xf5\xec\xa2\x23\xda\x41\xb3" \
    "\xdc\x0c\x80\xbe\xa2\xf3\x21\xfd\x81\xfc\x1f\x79" \
    "\xaa\xe5\xaa\x2b\xb4\x21\xf8\xcb\x04\x8d\xec\x3f" \
    "\xff\x9a\xbe\x87\x7d\x02\x24\x35\x5a\xaa\x85\x97" \
    "\xe7\xd4\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"
image5_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x18\x00\x00\x00\x18" \
    "\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\x00\x00\x03" \
    "\x95\x49\x44\x41\x54\x78\x9c\x95\x96\x6d\x68\x5b" \
    "\x55\x1c\xc6\x7f\xe7\xe6\x26\x6d\x92\x2e\xbd\x6d" \
    "\xb0\xc5\xd6\x52\xa5\xc5\xb7\x5a\x5a\xdb\xcc\x95" \
    "\xa3\x73\x22\x29\x8a\x38\x18\x93\xfa\xf2\x41\x71" \
    "\x8a\x51\xfc\xe0\xc4\xe1\x04\xf1\x8b\x30\x9c\x30" \
    "\xf6\x45\x41\x70\xe8\x97\x31\xb5\x0c\x44\x5a\x71" \
    "\xca\xc6\x36\x45\xb9\xd0\x6d\x85\x15\x75\x4d\x48" \
    "\xd3\x4d\x52\x6b\x5b\x9b\x36\x37\xe9\xf2\xd2\x36" \
    "\x39\x7e\x98\xad\xed\xda\x1b\xd3\xe7\xd3\xe5\x3e" \
    "\xe7\xfc\x9e\xff\xff\x9c\x73\x5f\x84\x69\x9a\xd8" \
    "\x49\x4a\xa9\x6c\x4d\xc0\x34\x4d\x21\xa5\x54\x6e" \
    "\xa3\x93\x6c\xf2\xf2\x06\x0f\x40\x2b\x07\xae\xeb" \
    "\x35\xb6\x63\x2a\x6b\xee\xda\x00\x5f\x2b\xdb\x80" \
    "\xb5\xaa\xde\xb6\xc3\xd6\xcb\xcd\x47\x4a\xce\xdd" \
    "\x34\xe0\xe6\xa5\x49\xcc\xff\xb0\xe9\xe4\xc6\xde" \
    "\x10\x8d\xbd\xa1\x92\x01\xba\xad\xe1\xad\xa1\x90" \
    "\x49\x62\x18\x06\x6e\xb7\x1b\xd1\xf6\x24\xb7\x6e" \
    "\x6f\x5b\xf5\xff\xba\xf8\x3b\x8d\xdb\xbb\xe9\xa9" \
    "\xbd\x9d\x8f\xce\x1c\xb3\x2d\x52\xdc\xbc\xc9\x52" \
    "\x4a\xe5\x6a\xba\x83\x8e\x9d\x7d\x08\x5d\xf0\xc6" \
    "\x81\xb7\xa8\x72\x69\x8c\xa7\x16\xa9\x10\x82\x44" \
    "\xae\x40\x64\x2e\xcf\xcc\xec\x18\x1d\xc2\xcb\x91" \
    "\x97\x1e\x42\x08\x51\x5e\x07\x52\x4a\xd5\xd8\x1b" \
    "\x62\x57\xe8\x00\x2f\x74\xd6\xe2\xd5\x05\x17\xa6" \
    "\x73\xfc\xf4\x47\x86\xb1\x54\x11\x54\x91\x3f\x7f" \
    "\x1d\xa2\x41\xab\xe4\xfc\xe1\x67\x01\xf8\x32\x18" \
    "\xe4\xbd\xa6\x26\x3e\x9e\x9c\xc4\x2a\x14\xec\x03" \
    "\xa4\x94\xaa\xd6\xdf\xc0\x6b\x07\x5f\xe7\xe9\x3b" \
    "\x6b\x39\x15\xbb\xca\xb9\xf0\x38\x91\x99\x02\x6a" \
    "\x51\xe0\xbf\xbb\x9d\x62\xd8\xa4\xcb\x51\xc7\x57" \
    "\x1f\xec\x01\x60\xb4\xbb\x9b\x05\xcb\xe2\x50\x3c" \
    "\x5e\xba\x03\x29\xa5\x72\xb9\x5c\xbc\xb9\x7f\x3f" \
    "\xcf\x34\x6f\xe3\xc4\xf1\x13\x1c\xff\xe6\x34\xf3" \
    "\x33\xd7\xf1\x3d\xf2\x04\x3e\x8f\x81\x5b\x73\x52" \
    "\xaf\x6e\xc0\x95\x52\x84\x03\x01\xcc\x5c\x96\x57" \
    "\x63\x31\x5b\xf8\xba\x0e\x82\xc1\x20\x52\x3e\xc0" \
    "\xd1\xa3\x9f\x30\x30\xd0\x4f\x32\x99\x40\xcb\x2f" \
    "\xd2\x3c\x18\xe1\xf9\x5b\xaa\x60\xea\x02\xa1\x81" \
    "\xcf\x01\x08\x07\x02\x00\x14\xf2\x8b\x25\xe1\xa6" \
    "\x69\x0a\x5d\x4a\xa9\x3c\x1e\x0f\xad\x2d\x2d\xc4" \
    "\x62\x63\x9c\xfa\xf6\x3b\x74\x6b\x8e\x87\xab\xaa" \
    "\x38\x9d\x9b\xe5\xdd\xce\x7a\x76\x3d\xda\x85\xd5" \
    "\xb8\x03\xeb\xd2\x10\xbe\xae\xfb\x01\xf8\xd9\xb2" \
    "\x6c\xab\x5f\x79\x8a\x57\x3b\xf0\xf9\x7c\x38\x5d" \
    "\x2e\x4e\x9e\xec\x27\x3e\x19\x06\x60\x22\x9b\xe5" \
    "\xd3\xdd\xfb\x78\xb0\xee\x1a\xae\x96\x56\xf2\x3f" \
    "\x9e\x25\x5b\xfd\x35\x93\xbf\x44\x88\xb6\xfa\x60" \
    "\xd8\xbe\x72\x29\xa5\x5a\x09\xd1\x01\x8a\x4b\x4b" \
    "\x0c\x99\x26\xbf\x8d\x8e\x12\xa8\xae\xe6\x62\x32" \
    "\x89\x2a\x16\xd1\x1c\x0e\x66\x5b\x9b\x78\x2e\x32" \
    "\x47\x46\xf3\xe0\xdd\x3d\x0d\xc0\xd4\x70\xe6\x7f" \
    "\xd7\x7e\xb5\x83\xcf\xee\xbd\x87\xc7\x3a\x5b\xa9" \
    "\x68\xf0\xf3\xf2\xf8\x18\x83\x53\x33\x00\x68\x0e" \
    "\x07\x4a\x29\x84\x10\xec\x31\xea\xf1\xec\xbd\x8d" \
    "\xba\xfb\x0a\x44\xd3\x71\xde\x9e\x9e\x28\x0b\x0e" \
    "\xa0\x57\x18\x06\x75\x8f\xf7\xa0\xe5\xd2\x78\xd6" \
    "\x18\x4a\xfd\xf7\xb6\x10\x40\x4d\x9f\x40\x5b\x5e" \
    "\xe0\xc5\xc3\x69\x52\x0b\x1b\xcf\xfb\x5a\xad\xdb" \
    "\x83\xb1\xe9\x19\x66\x2f\x4f\x90\x8f\x45\x39\xd4" \
    "\x54\x8f\x10\x62\x15\x2e\x84\xe0\xca\xce\x2e\x9c" \
    "\x01\x37\x85\xdc\x08\x85\xe5\x6b\xcc\xce\x95\x5d" \
    "\x3c\x00\x9a\x2a\x16\xb1\x1c\x1a\xb9\x8c\x62\x59" \
    "\xaf\x24\xd2\xd3\x8d\xd7\xe9\x40\xd3\x34\xae\x04" \
    "\xba\x71\x4a\x0d\xdf\xbe\x11\xd2\xd6\xdf\x1c\x3c" \
    "\x66\xd0\xde\xee\x2d\xbb\x7a\x00\x7d\xb4\xcb\xa2" \
    "\xf9\x95\x28\xa9\x0f\x7d\xe8\xb8\xc0\xe7\x27\xda" \
    "\xd1\x86\xff\x9d\x11\x72\xe9\x05\x9c\xce\xab\xa4" \
    "\x16\x2b\x39\xf2\x85\x93\x70\x38\xc3\xb9\xf3\xe9" \
    "\xb2\xe1\xf0\xef\x29\x12\x85\x38\x35\xef\xeb\xb0" \
    "\x04\xaa\x18\x45\x54\xf8\xc9\xcf\x67\x49\x5e\x4f" \
    "\x30\x1c\xad\xa3\x7f\x30\xc3\x42\x6a\xc9\x16\xbe" \
    "\x19\x78\x45\x02\x50\x7d\x4f\xd5\xae\xbb\x99\x98" \
    "\x5b\xba\x71\xb1\xac\x51\x51\xe9\x00\xe0\xfb\x33" \
    "\x1b\x17\xbf\x14\x78\x5d\xc0\x66\x86\x61\xb8\x48" \
    "\x26\xed\x5f\x05\xe5\xc0\x4b\x06\x94\x52\xb9\x70" \
    "\x00\x6d\x2b\x83\xb7\x0a\x87\x35\x5f\xb4\x72\x7e" \
    "\x51\xb6\x02\x5e\xd1\x3f\x32\xcc\x75\xb0\xa8\xbe" \
    "\xcc\x64\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"

class MainWinDesign(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        self.image2 = QPixmap()
        self.image2.loadFromData(image2_data,"PNG")
        self.image3 = QPixmap()
        self.image3.loadFromData(image3_data,"PNG")
        self.image4 = QPixmap()
        self.image4.loadFromData(image4_data,"PNG")
        self.image5 = QPixmap()
        self.image5.loadFromData(image5_data,"PNG")
        if not name:
            self.setName("MainWinDesign")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        MainWinDesignLayout = QGridLayout(self.centralWidget(),1,1,11,6,"MainWinDesignLayout")

        self.splitter3 = QSplitter(self.centralWidget(),"splitter3")
        self.splitter3.setOrientation(QSplitter.Horizontal)

        self.pluginBox = QGroupBox(self.splitter3,"pluginBox")
        self.pluginBox.setSizePolicy(QSizePolicy(5,5,0,0,self.pluginBox.sizePolicy().hasHeightForWidth()))
        self.pluginBox.setMaximumSize(QSize(170,32767))
        self.pluginBox.setColumnLayout(0,Qt.Vertical)
        self.pluginBox.layout().setSpacing(6)
        self.pluginBox.layout().setMargin(11)
        pluginBoxLayout = QGridLayout(self.pluginBox.layout())
        pluginBoxLayout.setAlignment(Qt.AlignTop)

        self.taskList = QIconView(self.pluginBox,"taskList")
        self.taskList.setSizePolicy(QSizePolicy(0,3,0,0,self.taskList.sizePolicy().hasHeightForWidth()))
        self.taskList.setMinimumSize(QSize(150,0))
        self.taskList.setMaximumSize(QSize(150,32767))
        self.taskList.setDragAutoScroll(0)
        self.taskList.setSelectionMode(QIconView.Single)
        self.taskList.setGridX(100)
        self.taskList.setGridY(-1)
        self.taskList.setArrangement(QIconView.LeftToRight)
        self.taskList.setResizeMode(QIconView.Adjust)
        self.taskList.setMaxItemWidth(98)
        self.taskList.setItemsMovable(0)

        pluginBoxLayout.addWidget(self.taskList,0,0)

        self.taskBox = QGroupBox(self.splitter3,"taskBox")
        self.taskBox.setAlignment(QGroupBox.AlignTop)
        self.taskBox.setColumnLayout(0,Qt.Vertical)
        self.taskBox.layout().setSpacing(6)
        self.taskBox.layout().setMargin(11)
        taskBoxLayout = QGridLayout(self.taskBox.layout())
        taskBoxLayout.setAlignment(Qt.AlignTop)

        self.taskStack = QWidgetStack(self.taskBox,"taskStack")
        self.taskStack.setSizePolicy(QSizePolicy(5,7,0,0,self.taskStack.sizePolicy().hasHeightForWidth()))

        self.page = QWidget(self.taskStack,"page")
        self.taskStack.addWidget(self.page,0)

        taskBoxLayout.addWidget(self.taskStack,0,0)

        MainWinDesignLayout.addWidget(self.splitter3,0,0)

        self.about = QAction(self,"about")
        self.about.setIconSet(QIconSet(self.image0))
        self.editServerList = QAction(self,"editServerList")
        self.editServerList.setIconSet(QIconSet(self.image1))
        self.exitItem = QAction(self,"exitItem")
        self.exitItem.setIconSet(QIconSet(self.image2))
        self.menuConfigurePlugins = QAction(self,"menuConfigurePlugins")
        self.menuConfigurePlugins.setIconSet(QIconSet(self.image3))
        self.reload = QAction(self,"reload")
        self.reload.setIconSet(QIconSet(self.image4))
        self.selectLanguage = QAction(self,"selectLanguage")
        self.selectLanguage.setIconSet(QIconSet(self.image5))
        self.togglePluginList = QAction(self,"togglePluginList")
        self.togglePluginList.setToggleAction(1)
        self.togglePluginList.setOn(0)
        self.togglePluginList.setEnabled(1)




        self.menubar = QMenuBar(self,"menubar")


        self.PopupMenu_3 = QPopupMenu(self)
        self.reload.addTo(self.PopupMenu_3)
        self.PopupMenu_3.insertSeparator()
        self.togglePluginList.addTo(self.PopupMenu_3)
        self.PopupMenu_3.insertSeparator()
        self.exitItem.addTo(self.PopupMenu_3)
        self.PopupMenu_3.insertSeparator()
        self.menubar.insertItem(QString(""),self.PopupMenu_3,1)

        self.PopupMenu = QPopupMenu(self)
        self.editServerList.addTo(self.PopupMenu)
        self.menuConfigurePlugins.addTo(self.PopupMenu)
        self.selectLanguage.addTo(self.PopupMenu)
        self.menubar.insertItem(QString(""),self.PopupMenu,2)

        self.PopupMenu_2 = QPopupMenu(self)
        self.about.addTo(self.PopupMenu_2)
        self.menubar.insertItem(QString(""),self.PopupMenu_2,3)


        self.languageChange()

        self.resize(QSize(547,428).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.about,SIGNAL("activated()"),self.showAboutLuma)
        self.connect(self.exitItem,SIGNAL("activated()"),self.quitApplication)
        self.connect(self.editServerList,SIGNAL("activated()"),self.showServerEditor)
        self.connect(self.menuConfigurePlugins,SIGNAL("activated()"),self.configurePlugins)
        self.connect(self.reload,SIGNAL("activated()"),self.reloadPlugins)
        self.connect(self.selectLanguage,SIGNAL("activated()"),self.showLanguageDialog)
        self.connect(self.togglePluginList,SIGNAL("toggled(bool)"),self.pluginBox,SLOT("setHidden(bool)"))
        self.connect(self.taskList,SIGNAL("selectionChanged(QIconViewItem*)"),self.taskSelectionChanged)


    def languageChange(self):
        self.setCaption(self.__tr("Luma"))
        self.pluginBox.setTitle(self.__tr("Plugins"))
        self.taskBox.setTitle(self.__tr("Work Area"))
        self.about.setText(self.__tr("About Luma..."))
        self.about.setMenuText(self.__tr("About Luma..."))
        self.about.setAccel(self.__tr("Ctrl+A"))
        self.editServerList.setText(self.__tr("Edit Server List..."))
        self.editServerList.setMenuText(self.__tr("Edit Server List..."))
        self.editServerList.setAccel(self.__tr("Ctrl+E"))
        self.exitItem.setText(self.__tr("Exit"))
        self.exitItem.setMenuText(self.__tr("Exit"))
        self.exitItem.setAccel(self.__tr("Ctrl+X"))
        self.menuConfigurePlugins.setText(self.__tr("Configure Plugins..."))
        self.menuConfigurePlugins.setMenuText(self.__tr("Configure Plugins..."))
        self.menuConfigurePlugins.setAccel(self.__tr("Ctrl+C"))
        self.reload.setText(self.__tr("Reload Plugins"))
        self.reload.setMenuText(self.__tr("Reload Plugins"))
        self.reload.setAccel(self.__tr("Ctrl+R"))
        self.selectLanguage.setText(self.__tr("Language..."))
        self.selectLanguage.setMenuText(self.__tr("Language..."))
        self.selectLanguage.setAccel(self.__tr("Ctrl+L"))
        self.togglePluginList.setText(self.__tr("Hide/Show pluginlist"))
        self.togglePluginList.setMenuText(self.__tr("Hide/Show pluginlist"))
        self.togglePluginList.setAccel(self.__tr("Ctrl+P"))
        if self.menubar.findItem(1):
            self.menubar.findItem(1).setText(self.__tr("Program"))
        if self.menubar.findItem(2):
            self.menubar.findItem(2).setText(self.__tr("Settings"))
        if self.menubar.findItem(3):
            self.menubar.findItem(3).setText(self.__tr("Help"))


    def quitApplication(self):
        print "MainWinDesign.quitApplication(): Not implemented yet"

    def showServerEditor(self):
        print "MainWinDesign.showServerEditor(): Not implemented yet"

    def showAboutLuma(self):
        print "MainWinDesign.showAboutLuma(): Not implemented yet"

    def taskSelectionChanged(self):
        print "MainWinDesign.taskSelectionChanged(): Not implemented yet"

    def loadPlugins(self):
        print "MainWinDesign.loadPlugins(): Not implemented yet"

    def unloadPlugins(self):
        print "MainWinDesign.unloadPlugins(): Not implemented yet"

    def configurePlugins(self):
        print "MainWinDesign.configurePlugins(): Not implemented yet"

    def reloadPlugins(self):
        print "MainWinDesign.reloadPlugins(): Not implemented yet"

    def showLanguageDialog(self):
        print "MainWinDesign.showLanguageDialog(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("MainWinDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = MainWinDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
