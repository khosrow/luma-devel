# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/template_plugin/AddAttributeDialogDesign.ui'
#
# Created: Wed Aug 17 15:23:49 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt4.QtGui import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x40\x00\x00\x00\x40" \
    "\x08\x06\x00\x00\x00\xaa\x69\x71\xde\x00\x00\x0c" \
    "\x04\x49\x44\x41\x54\x78\x9c\xe5\x9b\x79\x74\x54" \
    "\xd5\x1d\xc7\x3f\x6f\xb6\x64\x26\x33\xc9\xb0\x24" \
    "\x84\x00\x42\x64\xb1\x2e\x68\x4e\xd5\x5a\x5c\xa8" \
    "\xe8\xf1\xb4\xa2\x88\x4b\x51\xab\xad\x0a\x1e\x7b" \
    "\xdc\x8a\x0b\x48\xb5\xf5\x58\xad\xb6\xf5\xd4\x53" \
    "\x17\x3c\xd6\x15\x51\x8f\x95\x2e\x8a\x68\x05\x2d" \
    "\xa2\xa0\xb8\x82\xec\x12\xc2\xbe\x65\x19\xc8\x42" \
    "\x66\xcb\x64\xde\x76\xfb\xc7\x9d\xc9\x2c\xc9\x4c" \
    "\x26\xc9\x40\x4a\xfd\x9d\x73\x4f\xf2\x6e\x5e\xde" \
    "\xdc\xef\xf7\xf7\xfd\x2d\xef\xbe\x37\x8a\x10\x82" \
    "\xef\xb2\x59\xfa\x7b\x01\xfd\x6d\xdf\x79\x02\x6c" \
    "\xdd\x9d\xa0\x28\xca\xe1\x5d\xc1\xcd\x07\xbd\xe8" \
    "\xda\x0c\x5a\x77\xbf\xc7\x9b\x67\xef\x02\x0c\x20" \
    "\xaf\x71\x99\x2d\xcc\xfb\x57\x01\x37\xfb\xa6\x23" \
    "\xc4\x7a\xca\x0b\xff\x82\xe7\xd8\xd5\x9c\xfb\xd2" \
    "\xf9\x80\x13\x38\xcc\xac\x27\x4c\xe9\x2e\x09\x1e" \
    "\x16\x05\xdc\xe2\x9b\x04\xca\x93\x8c\x70\x9c\xcc" \
    "\xd9\x45\x30\xd2\x0e\xeb\x22\xf0\x66\x63\x88\x1d" \
    "\xff\xba\x96\xaf\x66\x2f\x03\x22\xe4\x49\x09\xd9" \
    "\x30\x1e\x59\x02\x6e\xab\xaf\x04\xeb\x2b\x14\xdb" \
    "\x27\x72\x96\x13\xc6\x17\xa6\xfe\x7d\x6d\x1b\x2c" \
    "\x6a\x0a\xb3\xf7\xeb\x39\xac\xb8\xf2\x35\xa0\x0d" \
    "\x30\xfb\xfa\xb1\xfd\x4f\xc0\x9d\x2d\x5e\x4c\xe3" \
    "\x29\x1c\xd6\xeb\xf8\x7e\x21\x9c\xe5\xcc\x7c\x6e" \
    "\xbd\x06\xcf\x1c\x80\xda\xb5\xbf\x65\xc5\xd4\x67" \
    "\x80\x20\x7d\x24\xa1\xff\x08\x98\xd5\xea\xc5\xd0" \
    "\xee\x06\xcb\x4c\xaa\x0a\x4b\x98\xe0\x84\xc2\x1c" \
    "\xae\x57\xa7\xc2\x5c\x1f\xec\x5b\xf5\x00\x5f\x4c" \
    "\x7b\x1a\x08\xd0\x07\x12\xfa\x87\x80\x59\xcd\xd3" \
    "\x41\x79\x82\x91\x8e\x12\xce\x71\x42\x71\x0f\xf3" \
    "\x6d\x9d\x0a\x2f\xf8\xa0\xae\xee\x5d\x96\x9f\x39" \
    "\x03\xf0\x03\x7a\x6f\x96\x72\x64\x09\xb8\xa7\x79" \
    "\x12\x58\xe7\x33\xc0\x3a\x92\x1f\x16\x42\x45\xb7" \
    "\x95\x36\xb3\x45\x4c\x78\xaa\x16\x76\xec\x7d\x8f" \
    "\xcf\x26\xde\x08\xb4\xd0\x0b\x12\x8e\x0c\x01\x73" \
    "\x1a\x2b\x51\x6c\xaf\x50\x64\x9b\xc8\x78\x07\x8c" \
    "\x71\xf4\x64\x8d\x99\x2d\x62\xc2\xdc\xfd\xb0\x63" \
    "\xff\xa7\xec\x7d\xf6\x26\x1a\xde\xd8\x0d\x68\x3d" \
    "\xb9\x44\x36\x8c\x7d\x70\x4f\x9a\x99\xa2\xb2\x78" \
    "\x88\x7d\x22\xe7\xb9\x08\x28\x4a\x0f\x97\x98\xc5" \
    "\x6c\x16\xb8\x65\x04\xbc\xc8\x44\xcc\x3b\xdf\xc3" \
    "\x88\x4e\xe5\xe0\x5b\x3b\x01\x35\x1f\x97\xcf\x5f" \
    "\x23\xa4\x45\x2d\x01\x1b\x50\xaa\x70\x62\x01\x92" \
    "\x80\x7c\x0d\x9b\x05\x6e\x19\x09\x67\x54\x8c\x65" \
    "\xd8\xec\x77\x19\x74\xc9\x58\x20\x2f\x12\xcb\xa7" \
    "\x02\x40\x08\x02\x02\xf6\x7b\x60\xb8\x0e\xb5\xc1" \
    "\xbc\x5d\x5d\xda\x55\xc3\x70\x1b\x62\x4c\xc8\xb8" \
    "\x7f\x19\xcd\xef\x9e\x01\xf8\xe8\xa3\x12\xf2\xa7" \
    "\x00\x43\x48\x12\x80\x80\x80\x5a\x2f\x9c\x30\x80" \
    "\xfc\x2a\x21\x04\xa1\xc9\xc3\x41\x38\xca\x81\x63" \
    "\x00\x77\x5f\x97\x9d\x67\x05\xa4\x4e\x55\xbb\xe1" \
    "\x04\xa0\xba\xae\x8f\xd7\x8e\x13\x60\x01\xac\xc4" \
    "\x89\x2e\x21\x0f\x61\x90\x3f\x02\x44\x42\x01\xc9" \
    "\x56\xed\x86\xe2\x0a\xa0\x16\x02\x3d\x2d\x60\x7a" \
    "\x6c\x28\x48\xe0\x4a\x6c\xc8\xcf\x89\x1f\xf5\xc9" \
    "\xf2\x16\x02\x97\x47\x3f\x18\xd5\xa1\x82\xb4\x11" \
    "\x70\x43\x45\x25\xb2\x97\xcb\x45\xea\x51\x70\x47" \
    "\xe4\xcf\x8e\x55\x26\x8f\x2e\x88\xee\xad\xf5\x99" \
    "\x80\xb6\x2b\xa8\xd4\xa6\xf1\xce\xed\xea\xeb\x2f" \
    "\x62\x88\x84\xd7\xd2\x46\x8d\x15\x18\x05\x1e\x0b" \
    "\x59\x81\x13\x06\xda\x21\x64\xd0\x19\xf8\x61\x20" \
    "\xa0\xd7\x21\x60\x5e\x89\x57\x17\x3c\x64\x73\xd8" \
    "\x66\x2a\xa3\x47\xa0\x0c\x3a\x09\x5a\x45\xf6\x3e" \
    "\xcd\x01\x9e\xb1\xc0\x36\x08\x86\x13\xd3\x1e\x2b" \
    "\x04\xdb\x63\x07\x56\x32\x03\x8f\x0f\xa3\x9f\x09" \
    "\xd0\xa7\xf1\x90\x80\x3b\x6c\xc7\x94\x97\x28\xe3" \
    "\x46\x42\x61\x01\xb4\x2a\x52\xe2\xdd\xc4\x79\x3d" \
    "\x40\x25\x8c\xab\x87\xa0\x1f\x1a\x42\xf2\x76\x0f" \
    "\x2b\xa9\xe0\xe3\x11\xfe\xbf\xa4\x00\x6d\x1a\xd3" \
    "\x2d\x0a\xbf\x53\x06\x95\x8c\x54\x8e\x1f\x0d\x1e" \
    "\x97\x5c\x8c\xa6\xcb\x61\x08\xb9\xa1\x95\x83\x0d" \
    "\x1d\x05\xac\x87\x06\x41\x76\xaf\x77\x45\xc4\x91" \
    "\x26\x40\x9d\xc6\x24\x05\x1e\xb4\xba\x0a\x26\x2a" \
    "\xe3\xc7\xc1\x80\x62\x30\x4d\x50\xf5\x58\xf6\x37" \
    "\x41\x33\xe4\xc2\x72\xcc\xf4\x41\x0b\x6c\x0b\xc4" \
    "\x56\xd0\x9d\xe4\xe3\x44\x74\x84\x40\x9f\xf7\x48" \
    "\x3a\xac\x5b\x02\x8c\x2b\x59\xa4\xd8\x6c\x53\x95" \
    "\xe3\x46\x41\x45\xa9\x04\xa9\x6a\x89\xb2\x67\xc6" \
    "\x09\x88\x29\x20\xd7\x52\x17\xf7\x7a\x36\xa9\x67" \
    "\x52\x43\xfe\xf0\xe7\xb0\x2b\x0c\x53\x95\x2b\xa6" \
    "\xc0\xc1\x3a\xe9\x71\xd3\xec\x0c\x5e\x08\xd0\x0d" \
    "\x29\xff\x5c\x09\x48\xf7\x7c\xae\x24\xf4\x4b\x19" \
    "\x54\x83\x30\x70\x88\xf4\xbc\xa6\x4b\x22\x54\x3d" \
    "\xe5\xd8\x6b\xf8\xe1\xa0\x0a\x7b\xa3\x19\x4b\x61" \
    "\xf2\x10\x5d\x95\xb9\x5c\xd5\x70\xc4\x09\xd0\x4d" \
    "\x88\x86\x60\xe8\x08\x10\xd6\x4e\xe0\x51\x75\xaa" \
    "\xac\x35\xbc\x3d\xe0\x3e\xbc\x0b\x77\xc0\xb7\x21" \
    "\xa9\x86\xee\x46\x4f\x12\x5f\x0a\x01\xf9\x8b\x81" \
    "\x1c\x09\x30\xe4\x08\xb5\x42\xd9\x10\xf9\x7b\xba" \
    "\x12\x54\x9d\x4b\x0b\x56\xb0\x7c\xe8\xaf\xf0\x7e" \
    "\xb8\x1b\x56\xfb\xb3\xab\x20\x1b\x01\xd9\xc2\x62" \
    "\x93\x1f\x0c\xb5\xad\x1f\x08\x30\x65\xf6\x0d\xf9" \
    "\xa1\xb4\x14\x0a\xdd\x12\xbc\x96\xa6\x04\xcb\x16" \
    "\x96\x97\xdd\x8a\xf7\xd3\x3d\xb0\xe4\x60\xcf\x42" \
    "\x20\x9b\x1a\x36\xfb\xe1\xde\x4d\x30\xef\x1d\x98" \
    "\xfd\x38\x5c\x52\x52\x49\x1e\xee\x07\xba\xaf\x02" \
    "\x26\xd8\xf4\x58\xa2\x8b\x27\x3f\x61\x80\xb7\x04" \
    "\x42\x61\x08\x87\x12\x09\x51\x98\x60\x0a\xaa\x94" \
    "\x2d\xac\x2b\xbb\x86\xcb\xb6\xfd\x99\xf5\xfa\xa9" \
    "\xb8\x2f\x2c\x97\xad\x6d\xca\x85\xc9\x2d\xde\x9b" \
    "\xa3\x30\x7f\x37\xd4\x6d\x86\xd9\xf3\xe0\x67\xef" \
    "\x83\xaf\xc8\x45\xd5\xe0\xb9\x4c\x70\x15\x73\x5f" \
    "\xc3\x5c\x64\x03\xdd\xab\xb8\xe8\x56\x01\xba\x49" \
    "\x22\x04\x34\x53\x4e\xe8\x06\xb4\x85\xa0\xd8\x0d" \
    "\x1e\x6f\x42\x09\x49\x21\x31\x4a\xec\x67\xf9\xc0" \
    "\x9b\xa8\xaa\x59\xc5\xd0\x8f\x1a\x20\x6c\xa4\xc4" \
    "\x7f\x87\x02\x32\xc5\x7b\xbb\x01\xcf\xed\x80\x7b" \
    "\x3f\x81\x73\x1e\x83\x35\x3f\x95\xe0\x01\xca\xc3" \
    "\x70\x56\x03\x1c\x6f\x7b\x84\x87\xcb\xee\x00\x8a" \
    "\x73\xc1\xd2\x3b\x02\x8c\x18\x0b\x9a\x99\x20\x22" \
    "\x4e\x86\x29\xc0\x53\x04\xde\x81\x5d\x57\x06\xfd" \
    "\x10\xcb\x47\xdf\x45\xd1\xb6\x4d\xb0\x60\x0f\xee" \
    "\x76\x23\x73\x0e\x88\x13\xd1\x6e\xc0\x3b\xb5\x70" \
    "\xc7\x5a\x38\xed\x51\x58\x7d\x05\xdc\xf3\x72\xe7" \
    "\x85\x95\xa8\x30\xf1\x00\x1c\x6f\x7f\x98\xc7\x86" \
    "\xfc\x09\xb9\x3f\x60\xcd\x3f\x01\xc9\x0a\x88\xe7" \
    "\x02\x3d\x89\x8c\xf6\x76\x70\x3a\xa0\xb8\x24\xa6" \
    "\x84\x18\x11\x56\x2b\x8c\x1f\x87\xb7\xaa\x82\x75" \
    "\x17\xfe\x9e\x1b\x5c\x1f\xe3\xfe\xc7\x6e\xca\x75" \
    "\x23\x73\x12\x5c\xee\x83\x39\xeb\xc0\xf6\x3c\x7c" \
    "\x3c\x15\x66\xcd\x83\xe2\x50\xe6\xc5\x79\x55\xf8" \
    "\xb1\x0f\xbe\x67\xde\xcc\x13\x65\xaf\x02\x03\xe8" \
    "\x61\x7b\xdf\xed\xb6\x78\xd3\xc5\x8a\x18\x7c\xd6" \
    "\x29\xb1\x7b\xfb\xe4\x3c\x10\x1f\x49\xf3\x85\xc5" \
    "\xd0\xdc\x02\x45\x16\x28\x2f\x95\xe5\x2a\xa9\x61" \
    "\x9a\xfe\xc5\x74\x3e\x50\xcf\x27\x74\xc1\x08\x8e" \
    "\xad\x74\xb2\x51\x47\xfa\xec\x9b\x26\x58\x5c\x07" \
    "\x95\x5f\xc2\xfd\x4f\xc2\x09\xdb\x7a\x82\x01\x54" \
    "\x0b\x2c\x1b\x00\xdb\x59\xcc\x9c\xa6\x19\xa4\x3d" \
    "\x3f\xe8\xd3\x73\x01\xdf\x85\x8a\x28\x3f\x73\x7c" \
    "\x12\xe0\x38\x01\xa4\xce\x09\xe4\xfc\xf8\x93\xa1" \
    "\xa9\x2e\x0d\xbc\x24\x60\xbd\xcb\x64\xd2\xfe\x1b" \
    "\xd1\x57\xfe\x88\x0b\xee\x1c\xcb\xd2\x83\x3a\xe1" \
    "\xb7\xf6\x81\x6b\x03\xcc\x7a\x12\x4e\x5f\xd7\x33" \
    "\xe0\xc9\xa6\x29\xb0\xc2\x03\x0d\xca\x76\x16\x86" \
    "\xa7\xf0\x69\xfb\x6e\x62\x1b\xa6\x7d\x7a\x2e\xa0" \
    "\xc5\x43\x20\xdd\xe3\xe9\x2a\x88\x1f\x07\xfd\x10" \
    "\xd5\x3b\x79\x1f\x53\xd0\x5a\x28\xa8\xba\xfe\x73" \
    "\x56\x98\x5f\xf3\xf6\x83\x77\x41\x69\x3d\x5c\xff" \
    "\x32\x5c\xb4\x44\x7e\x58\x5b\xaf\xf2\x58\xc2\x7e" \
    "\x10\x86\x4d\x05\x63\x99\xe2\x7c\x8f\x76\xf3\x52" \
    "\x56\xa9\xdb\xe3\x24\xf4\x9a\x00\xdd\x04\x0c\x43" \
    "\x16\x99\x6c\x2a\x88\x1f\xab\x06\x44\xb5\x4e\xde" \
    "\xc7\x10\xe0\x8a\x5d\xf4\x94\x0f\x61\xf8\x0e\xaa" \
    "\xce\x2d\x60\xbd\x67\x35\x84\x7b\x9c\xbb\x32\xdb" \
    "\x71\x1a\x44\x19\xc3\x65\xce\x45\xac\x52\xcf\x03" \
    "\x0e\x90\x85\x84\xdc\x08\xd0\xcc\x34\xf0\x64\x26" \
    "\x43\xd5\x63\x0a\x48\x03\x6f\x0a\x29\x53\x00\xab" \
    "\x80\x61\x3b\xd9\x53\x57\x44\x49\xd9\x00\xfc\x05" \
    "\xfe\xbc\x60\x07\x40\x81\xa2\x93\x1c\x84\xf7\xa9" \
    "\x63\x80\x11\x40\x88\xbe\x10\x10\xd1\xd9\x5c\xbb" \
    "\xdd\x77\xe2\xf0\x51\x83\x53\xa5\x9e\x89\x8c\x6c" \
    "\x04\xa8\x31\x89\x5b\x05\x58\x05\xad\x66\x10\x9a" \
    "\x05\xe7\x54\x9c\xce\xca\xf0\xda\x3e\x02\x17\x50" \
    "\x20\xc0\x69\x12\xb6\x85\xc0\xb4\x03\x78\x81\x82" \
    "\x6c\xff\xd6\x2d\x01\xcf\xed\xe5\xe2\x6b\xa2\xc1" \
    "\xa5\x91\x76\x63\x6c\xe5\xc8\x81\xd8\x2c\x4a\xf6" \
    "\x5c\x90\x42\x40\x12\x78\x53\x80\x66\x91\xe7\x58" \
    "\x93\x87\x60\x65\xcb\x3a\x4a\x1c\x1e\xfc\x91\xd8" \
    "\x46\x61\x4f\x6e\xf6\x14\x28\x72\x15\x12\xb6\x87" \
    "\xc0\x21\xc0\x16\x1b\xf2\x8e\x31\xde\x61\xf4\x9e" \
    "\x80\x67\xf7\x52\xbf\xaf\x8d\xcb\x6e\xd3\xda\x5e" \
    "\x0f\x86\xb4\xaa\x93\xc7\x0d\x4e\x90\x60\x8a\xce" \
    "\x64\xa8\x46\x22\x09\x26\x83\x37\x4d\x50\x6d\x08" \
    "\xd3\xec\x50\x80\x1c\x92\x08\xbf\x25\xc0\x89\x83" \
    "\xc7\xb0\xbf\xbe\x99\x80\x96\xa5\xf6\x27\x5b\x81" \
    "\x00\x97\x49\xd8\x1a\x06\x7b\x12\xf8\x04\x01\xdd" \
    "\x5a\x2e\x69\x57\x5d\xdc\xc8\xf6\xc9\x6b\x99\x52" \
    "\xd3\xa2\xbd\xbf\xba\xba\x09\xcd\x56\xd0\x75\x53" \
    "\x64\x18\x09\x05\xb4\xc7\x7e\x26\x0f\xd5\x90\x25" \
    "\xc9\xda\xd5\x80\xcd\x62\x3b\x94\xab\xd0\x6e\x91" \
    "\x89\xb1\x8b\xe1\x56\x3d\xa0\x2b\xd2\xdb\x05\xa6" \
    "\x04\x9b\x0e\xde\x2e\x72\xde\x39\xce\xb5\xee\xa8" \
    "\xc0\x81\x6b\x37\x33\x63\xdb\x21\x6d\xf1\x27\x6b" \
    "\x7c\xf8\x03\xaa\x04\x9c\xde\x21\xaa\xba\xac\x02" \
    "\x29\xe0\x63\xc7\xaa\x8e\x30\x45\x8a\xfc\xd3\x47" \
    "\xc0\x19\xc0\x33\xde\x42\x85\xa3\x0c\xc2\x96\xd4" \
    "\xa1\x29\x84\x94\x10\x14\x9a\x12\xa4\x5d\x80\xdd" \
    "\xec\x0c\x3e\xcf\x0a\x88\x9b\x06\x34\xdd\x50\xc3" \
    "\x8c\xad\x4d\x91\xbf\x7f\xbc\xc5\xcf\x21\xc3\xd1" \
    "\x59\x05\xaa\xd1\xb5\xf7\xe3\x0a\x48\x09\x01\xba" \
    "\x24\x23\xe8\x0c\x10\x3c\xcd\x87\xc7\xe3\x94\x9e" \
    "\xd7\x95\x0e\xb9\x77\xc4\x79\x87\xd7\x49\x1c\x27" \
    "\x2b\xe1\x30\x10\x00\xb2\xbd\x6c\xb9\x7d\x17\x33" \
    "\xd7\xf8\xc5\x43\x1f\x6c\x6c\xa1\xd9\xe6\x4e\xba" \
    "\x41\x4a\x0a\x81\x24\xef\x47\xc2\x3a\xff\xd9\xd5" \
    "\xce\xbc\xea\xf6\x98\x02\xba\x0e\x81\x64\x32\x82" \
    "\x05\x41\xdc\x17\xe8\xdc\x38\xe1\x92\x18\x70\xb3" \
    "\xb3\x97\x33\x1d\xdb\x44\xce\xbb\x46\xbd\x69\xbd" \
    "\x74\xa0\xe5\x0f\xf5\xcc\xdd\xd8\x12\x7d\xe0\xcd" \
    "\xcf\x6a\xa9\x09\xdb\x13\xb7\xca\x69\x04\x7c\xd3" \
    "\xa0\xf2\xf8\xc6\x76\x16\xec\xd3\xd7\x2d\x2d\xb3" \
    "\xbf\x24\x84\x99\xd1\xf3\xe9\x64\x34\x58\x7c\xac" \
    "\x69\xac\x4e\x05\x6a\xcf\xe2\xf5\xe4\xb9\x1c\x15" \
    "\xd0\xdb\x47\x63\x06\xd0\xfa\xa8\x8f\xa7\x6f\x1d" \
    "\x44\x30\xbc\xe9\xd0\x23\xc6\xa9\x15\x45\x27\x6a" \
    "\x8d\x1d\x55\xa0\xda\x6f\xf2\xef\x3a\x83\x5d\x11" \
    "\xb1\x75\xbd\xce\xc2\x55\x06\xab\xa8\xb0\x8f\x1a" \
    "\xdd\x49\x01\xdd\x11\xd1\x03\xaf\x27\x87\xc5\x61" \
    "\x26\x00\x64\x0b\x14\xf8\x6b\x33\xf3\x2f\x77\xb3" \
    "\x2f\xf2\x55\xfd\x6b\xe1\xaa\x21\x45\x65\x7e\x9d" \
    "\x8f\x76\x68\x7c\x1b\x14\xcd\xeb\x75\xde\x58\xa1" \
    "\xf1\x09\xd0\x08\x1c\x60\xb4\xc3\x4a\xb7\x21\x90" \
    "\x3a\x2f\x7a\x0c\x5e\xc8\xa6\xe8\x08\x10\x10\x27" \
    "\x21\xb8\x30\xc4\x52\xd3\xe4\xda\xe8\x37\x07\xfe" \
    "\xa6\x19\x28\x1b\x35\x16\x2c\x89\xb2\x14\x68\x46" \
    "\xbe\xc6\x72\x10\x08\x52\x64\x11\x9b\x5b\x77\x81" \
    "\xdb\x0a\x56\x3d\x27\x22\x84\xa5\x87\xe0\xad\x31" \
    "\xe0\x39\x96\xc1\x7c\xbc\x20\x61\x02\xe1\x45\x6d" \
    "\x7c\xb8\x08\xaa\x80\x61\x31\x08\x4d\x31\xe0\x7e" \
    "\xe4\x83\x6f\x93\xdb\x6b\x77\x06\xe6\x56\xdc\xcd" \
    "\x10\xcf\xe3\x0c\x0e\xc1\xa0\x68\x96\x10\x90\xf3" \
    "\xc2\x6a\x26\x64\x9d\x29\xde\x93\xe7\xe2\x7d\xdf" \
    "\x11\x52\x40\xdc\x04\xf2\xed\xee\x5a\xe0\x10\x72" \
    "\x19\x6d\x40\x3b\xa9\x9b\x95\x26\x33\xeb\x5f\xe4" \
    "\x06\xef\x3e\xce\x73\xbd\x8a\xcd\x2c\x62\x48\x34" \
    "\xb7\x10\xe8\x2e\x0c\xec\x24\xbc\x1f\x41\x76\xa6" \
    "\x39\x58\x1f\x6f\xc0\x53\x4c\xc4\x00\x37\x23\xbd" \
    "\xdf\xd5\x9b\xde\x02\x68\xe3\x95\xd6\xa5\x2c\x6f" \
    "\xfb\x39\x3b\x9c\xe1\xa1\xbe\x11\x99\xcb\xa1\x45" \
    "\x20\xac\x39\x78\xdd\x9e\x24\xfd\x95\xc0\x1f\x81" \
    "\x7a\x3e\x44\xf6\x2e\x59\x9f\x57\xe7\xef\x1d\xa1" \
    "\xdc\xcd\x04\x42\xcc\x6f\x5d\x0a\xe2\x9a\x86\xa8" \
    "\xf1\x02\x61\xe7\x10\x4e\x0d\x77\x0e\x03\x85\x54" \
    "\x02\xb2\xc5\xff\x5a\x60\xa9\x02\x3b\xc5\x3a\x56" \
    "\xf0\x1a\xbb\xd9\x89\xcc\x3f\x91\x6c\x8b\xe9\x0f" \
    "\x02\x20\x1e\x32\xf3\xfd\xcb\xd8\x50\x30\x99\x5f" \
    "\xb8\xff\x39\xda\x72\xfc\x68\xdf\x84\x3d\x84\xad" \
    "\x21\x09\xde\x22\x3d\xda\x91\x03\x32\x81\xdf\x2f" \
    "\xe0\x03\x05\x6a\xc4\x56\x36\x88\x85\x7c\xcd\x2a" \
    "\x64\xd5\x69\x40\xaa\x31\xeb\x53\xa4\xfe\x22\x00" \
    "\xe2\x24\xac\x8d\x56\x63\xe3\xb2\x9d\xd3\xf6\x2f" \
    "\x2c\x0a\xb8\xc6\xf0\x93\xb0\x6c\x7b\xe3\x27\x59" \
    "\x33\x48\xbe\x41\xc0\x97\xc0\x56\x9a\xd9\x20\xde" \
    "\x60\x85\x48\x94\x5b\x19\x82\x41\x64\x08\x64\x4d" \
    "\x06\xfd\x49\x00\xc4\xf3\xc6\xaa\xe8\x56\x10\x97" \
    "\x86\x27\x1b\xcf\x95\x46\x8e\x39\x9b\x69\x61\x1a" \
    "\x9d\x07\xe5\x19\x56\x21\x4f\x8b\x83\x8f\x08\xf8" \
    "\xdc\x84\x8d\xa2\x8d\x6f\xcd\x05\xbc\x2f\x3a\x97" \
    "\x5b\x79\xf3\x96\x53\x2f\xdc\x3f\xdf\x19\xea\xda" \
    "\x1c\x40\x29\xbf\x29\x7a\xa1\x74\xf4\xe0\xc9\xe2" \
    "\xaa\x36\x9a\x5c\x8d\x1c\xb7\xb9\x8a\xad\xe6\x36" \
    "\xd9\xdc\xac\x35\x60\x8b\xd9\xc6\x1e\x73\x19\x1f" \
    "\x99\xef\xd0\x44\x1d\x52\xea\xa9\xe5\x36\xcd\xfa" \
    "\xff\x2b\x33\xb9\x9b\x1d\x18\xc8\xaf\x5d\xf3\x5c" \
    "\x83\x9d\x17\x0d\xba\xda\x8d\xb3\xc5\xcb\xb6\x9a" \
    "\xad\x50\x63\xc2\x3e\xe3\x0b\x16\x99\xf3\x69\x16" \
    "\x75\x48\xd0\x07\x90\x65\x37\x42\x16\x8f\x1f\x4d" \
    "\x04\x80\x0c\xcb\x81\xfc\xb2\xe0\x5e\x67\xa5\xeb" \
    "\x2e\x4c\x41\xc4\x17\xde\xca\x12\xfd\x79\x76\x8a" \
    "\x9d\x48\xd0\x3e\xe4\xc3\x8f\x08\x39\xbc\x93\x72" \
    "\xb4\x11\x00\x92\x04\x2f\x57\xdb\xae\xa3\x51\x38" \
    "\xf8\xc8\xa8\x46\x02\xf6\x21\x13\x5c\x88\x1e\x7c" \
    "\x73\xe4\x68\x24\x00\x64\x2b\xe4\x41\x3e\xef\x53" \
    "\x90\x5f\x9c\x0a\x90\x43\x66\x4f\xb7\xa3\x95\x00" \
    "\x90\x9d\xaa\x0d\x09\xd8\xa0\x97\xef\x00\xf4\x89" \
    "\x80\xff\x77\xfb\x2f\x21\x56\xf1\x69\xe4\x2f\x96" \
    "\xd3\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"

class AddAttributeDialogDesign(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("AddAttributeDialogDesign")


        AddAttributeDialogDesignLayout = QGridLayout(self,1,1,6,6,"AddAttributeDialogDesignLayout")

        self.pixmapLabel1 = QLabel(self,"pixmapLabel1")
        self.pixmapLabel1.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.pixmapLabel1.sizePolicy().hasHeightForWidth()))
        self.pixmapLabel1.setPixmap(self.image0)
        self.pixmapLabel1.setScaledContents(1)

        AddAttributeDialogDesignLayout.addWidget(self.pixmapLabel1,0,0)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setAlignment(QLabel.WordBreak | QLabel.AlignTop)

        AddAttributeDialogDesignLayout.addWidget(self.textLabel1,0,1)

        self.line1 = QFrame(self,"line1")
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.HLine)

        AddAttributeDialogDesignLayout.addMultiCellWidget(self.line1,2,2,0,1)

        layout4 = QHBoxLayout(None,0,6,"layout4")
        spacer1 = QSpacerItem(100,21,QSizePolicy.MinimumExpanding,QSizePolicy.Minimum)
        layout4.addItem(spacer1)

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed,0,0,self.okButton.sizePolicy().hasHeightForWidth()))
        layout4.addWidget(self.okButton)

        self.cancelButton = QPushButton(self,"cancelButton")
        self.cancelButton.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed,0,0,self.cancelButton.sizePolicy().hasHeightForWidth()))
        layout4.addWidget(self.cancelButton)

        AddAttributeDialogDesignLayout.addMultiCellLayout(layout4,3,3,0,1)

        self.splitter2 = QSplitter(self,"splitter2")
        self.splitter2.setOrientation(QSplitter.Horizontal)

        self.attributeView = QListView(self.splitter2,"attributeView")
        self.attributeView.addColumn(self.__tr("Attributes"))
        self.attributeView.setMinimumSize(QSize(200,0))
        self.attributeView.setResizeMode(QListView.LastColumn)

        LayoutWidget = QWidget(self.splitter2,"layout3")
        layout3 = QGridLayout(LayoutWidget,1,1,6,6,"layout3")
        spacer3 = QSpacerItem(21,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout3.addItem(spacer3,5,2)

        self.defaultEdit = QLineEdit(LayoutWidget,"defaultEdit")

        layout3.addWidget(self.defaultEdit,4,2)

        self.textLabel3 = QLabel(LayoutWidget,"textLabel3")

        layout3.addMultiCellWidget(self.textLabel3,0,0,0,2)

        self.textLabel1_2 = QLabel(LayoutWidget,"textLabel1_2")

        layout3.addWidget(self.textLabel1_2,3,1)

        self.singleLabel = QLabel(LayoutWidget,"singleLabel")

        layout3.addWidget(self.singleLabel,2,2)

        self.binaryLabel = QLabel(LayoutWidget,"binaryLabel")

        layout3.addWidget(self.binaryLabel,3,2)
        spacer2 = QSpacerItem(16,20,QSizePolicy.Fixed,QSizePolicy.Minimum)
        layout3.addItem(spacer2,1,0)

        self.textLabel2 = QLabel(LayoutWidget,"textLabel2")

        layout3.addWidget(self.textLabel2,1,1)

        self.textLabel5 = QLabel(LayoutWidget,"textLabel5")

        layout3.addWidget(self.textLabel5,4,1)

        self.textLabel4 = QLabel(LayoutWidget,"textLabel4")

        layout3.addWidget(self.textLabel4,2,1)

        self.mustLabel = QLabel(LayoutWidget,"mustLabel")

        layout3.addWidget(self.mustLabel,1,2)

        AddAttributeDialogDesignLayout.addMultiCellWidget(self.splitter2,1,1,0,1)

        self.languageChange()

        self.resize(QSize(563,361).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.okButton,SIGNAL("clicked()"),self.accept)
        self.connect(self.cancelButton,SIGNAL("clicked()"),self.reject)
        self.connect(self.attributeView,SIGNAL("selectionChanged(QListViewItem*)"),self.attributeChanged)
        self.connect(self.defaultEdit,SIGNAL("textChanged(const QString&)"),self.defaultChanged)

        self.setTabOrder(self.attributeView,self.defaultEdit)
        self.setTabOrder(self.defaultEdit,self.okButton)
        self.setTabOrder(self.okButton,self.cancelButton)


    def languageChange(self):
        self.setCaption(self.__tr("Add attribute"))
        self.textLabel1.setText(self.__tr("Please select the attributes you want to add."))
        self.okButton.setText(self.__tr("&OK"))
        self.okButton.setAccel(self.__tr("Alt+O"))
        self.cancelButton.setText(self.__tr("&Cancel"))
        self.cancelButton.setAccel(self.__tr("Alt+C"))
        self.attributeView.header().setLabel(0,self.__tr("Attributes"))
        self.textLabel3.setText(self.__tr("<b>Attribute information</b>"))
        self.textLabel1_2.setText(self.__tr("Binary:"))
        self.singleLabel.setText(self.__tr("B","DO NOT TRANSLATE"))
        self.binaryLabel.setText(self.__tr("C"))
        self.textLabel2.setText(self.__tr("Must:"))
        self.textLabel5.setText(self.__tr("Default value:"))
        self.textLabel4.setText(self.__tr("Single:"))
        self.mustLabel.setText(self.__tr("A","DO NOT TRANSLATE"))


    def attributeChanged(self):
        print "AddAttributeDialogDesign.attributeChanged(): Not implemented yet"

    def defaultChanged(self):
        print "AddAttributeDialogDesign.defaultChanged(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("AddAttributeDialogDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = AddAttributeDialogDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
