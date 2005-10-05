# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/base/gui/AboutDialog.ui'
#
# Created: Wed Oct 5 16:57:17 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class AboutDialog(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("AboutDialog")


        AboutDialogLayout = QVBoxLayout(self,11,6,"AboutDialogLayout")

        self.textLabel5 = QLabel(self,"textLabel5")
        self.textLabel5.setFrameShape(QLabel.NoFrame)
        self.textLabel5.setFrameShadow(QLabel.Plain)
        AboutDialogLayout.addWidget(self.textLabel5)

        self.tabWidget2 = QTabWidget(self,"tabWidget2")

        self.tab = QWidget(self.tabWidget2,"tab")
        tabLayout = QVBoxLayout(self.tab,11,6,"tabLayout")

        self.textLabel4 = QLabel(self.tab,"textLabel4")
        tabLayout.addWidget(self.textLabel4)
        self.tabWidget2.insertTab(self.tab,QString.fromLatin1(""))

        self.tab_2 = QWidget(self.tabWidget2,"tab_2")
        tabLayout_2 = QVBoxLayout(self.tab_2,11,6,"tabLayout_2")

        self.textBrowser4 = QTextBrowser(self.tab_2,"textBrowser4")
        tabLayout_2.addWidget(self.textBrowser4)
        self.tabWidget2.insertTab(self.tab_2,QString.fromLatin1(""))

        self.tab_3 = QWidget(self.tabWidget2,"tab_3")
        tabLayout_3 = QVBoxLayout(self.tab_3,11,6,"tabLayout_3")

        self.textBrowser5 = QTextBrowser(self.tab_3,"textBrowser5")
        tabLayout_3.addWidget(self.textBrowser5)
        self.tabWidget2.insertTab(self.tab_3,QString.fromLatin1(""))

        self.tab_4 = QWidget(self.tabWidget2,"tab_4")
        tabLayout_4 = QGridLayout(self.tab_4,1,1,11,6,"tabLayout_4")

        self.textBrowser4_2 = QTextBrowser(self.tab_4,"textBrowser4_2")
        self.textBrowser4_2.setTextFormat(QTextBrowser.PlainText)

        tabLayout_4.addWidget(self.textBrowser4_2,0,0)
        self.tabWidget2.insertTab(self.tab_4,QString.fromLatin1(""))
        AboutDialogLayout.addWidget(self.tabWidget2)

        layout2 = QHBoxLayout(None,0,6,"layout2")
        spacer5 = QSpacerItem(210,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout2.addItem(spacer5)

        self.pushButton1 = QPushButton(self,"pushButton1")
        self.pushButton1.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.pushButton1.sizePolicy().hasHeightForWidth()))
        layout2.addWidget(self.pushButton1)
        AboutDialogLayout.addLayout(layout2)

        self.languageChange()

        self.resize(QSize(546,459).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton1,SIGNAL("clicked()"),self.close)


    def languageChange(self):
        self.setCaption(self.__tr("About Luma"))
        self.textLabel5.setText(self.__tr("<font size=\"+2\"><b>Luma 2.2.2</b></font>","DO NOT TRANSLATE"))
        self.textLabel4.setText(self.__tr("<p align=\"center\">LDAP management made easy.<br><br>\n"
"(c) 2003-2005   Wido Depping<br><br>\n"
"http://luma.sourceforge.net\n"
"</p>","DO NOT TRANSLATE"))
        self.tabWidget2.changeTab(self.tab,self.__tr("About"))
        self.textBrowser4.setText(self.__tr("Wido Depping<br>\n"
"<blockquote>widod@users.sourceforge.net</blockquote>","DO NOT TRANSLATE"))
        self.tabWidget2.changeTab(self.tab_2,self.__tr("Authors"))
        self.textBrowser5.setText(self.__tr("This program is distributed under the terms of the GPL v2.\n"
"\n"
"		    GNU GENERAL PUBLIC LICENSE\n"
"		       Version 2, June 1991\n"
"\n"
" Copyright (C) 1989, 1991 Free Software Foundation, Inc.\n"
"                          675 Mass Ave, Cambridge, MA 02139, USA\n"
" Everyone is permitted to copy and distribute verbatim copies\n"
" of this license document, but changing it is not allowed.\n"
"\n"
"			    Preamble\n"
"\n"
"  The licenses for most software are designed to take away your\n"
"freedom to share and change it.  By contrast, the GNU General Public\n"
"License is intended to guarantee your freedom to share and change free\n"
"software--to make sure the software is free for all its users.  This\n"
"General Public License applies to most of the Free Software\n"
"Foundation's software and to any other program whose authors commit to\n"
"using it.  (Some other Free Software Foundation software is covered by\n"
"the GNU Library General Public License instead.)  You can apply it to\n"
"your programs, too.\n"
"\n"
"  When we speak of free software, we are referring to freedom, not\n"
"price.  Our General Public Licenses are designed to make sure that you\n"
"have the freedom to distribute copies of free software (and charge for\n"
"this service if you wish), that you receive source code or can get it\n"
"if you want it, that you can change the software or use pieces of it\n"
"in new free programs; and that you know you can do these things.\n"
"\n"
"  To protect your rights, we need to make restrictions that forbid\n"
"anyone to deny you these rights or to ask you to surrender the rights.\n"
"These restrictions translate to certain responsibilities for you if you\n"
"distribute copies of the software, or if you modify it.\n"
"\n"
"  For example, if you distribute copies of such a program, whether\n"
"gratis or for a fee, you must give the recipients all the rights that\n"
"you have.  You must make sure that they, too, receive or can get the\n"
"source code.  And you must show them these terms so they know their\n"
"rights.\n"
"\n"
"  We protect your rights with two steps: (1) copyright the software, and\n"
"(2) offer you this license which gives you legal permission to copy,\n"
"distribute and/or modify the software.\n"
"\n"
"  Also, for each author's protection and ours, we want to make certain\n"
"that everyone understands that there is no warranty for this free\n"
"software.  If the software is modified by someone else and passed on, we\n"
"want its recipients to know that what they have is not the original, so\n"
"that any problems introduced by others will not reflect on the original\n"
"authors' reputations.\n"
"\n"
"  Finally, any free program is threatened constantly by software\n"
"patents.  We wish to avoid the danger that redistributors of a free\n"
"program will individually obtain patent licenses, in effect making the\n"
"program proprietary.  To prevent this, we have made it clear that any\n"
"patent must be licensed for everyone's free use or not licensed at all.\n"
"\n"
"  The precise terms and conditions for copying, distribution and\n"
"modification follow.\n"
" \n"
"		    GNU GENERAL PUBLIC LICENSE\n"
"   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION\n"
"\n"
"  0. This License applies to any program or other work which contains\n"
"a notice placed by the copyright holder saying it may be distributed\n"
"under the terms of this General Public License.  The \"Program\", below,\n"
"refers to any such program or work, and a \"work based on the Program\"\n"
"means either the Program or any derivative work under copyright law:\n"
"that is to say, a work containing the Program or a portion of it,\n"
"either verbatim or with modifications and/or translated into another\n"
"language.  (Hereinafter, translation is included without limitation in\n"
"the term \"modification\".)  Each licensee is addressed as \"you\".\n"
"\n"
"Activities other than copying, distribution and modification are not\n"
"covered by this License; they are outside its scope.  The act of\n"
"running the Program is not restricted, and the output from the Program\n"
"is covered only if its contents constitute a work based on the\n"
"Program (independent of having been made by running the Program).\n"
"Whether that is true depends on what the Program does.\n"
"\n"
"  1. You may copy and distribute verbatim copies of the Program's\n"
"source code as you receive it, in any medium, provided that you\n"
"conspicuously and appropriately publish on each copy an appropriate\n"
"copyright notice and disclaimer of warranty; keep intact all the\n"
"notices that refer to this License and to the absence of any warranty;\n"
"and give any other recipients of the Program a copy of this License\n"
"along with the Program.\n"
"\n"
"You may charge a fee for the physical act of transferring a copy, and\n"
"you may at your option offer warranty protection in exchange for a fee.\n"
"\n"
"  2. You may modify your copy or copies of the Program or any portion\n"
"of it, thus forming a work based on the Program, and copy and\n"
"distribute such modifications or work under the terms of Section 1\n"
"above, provided that you also meet all of these conditions:\n"
"\n"
"    a) You must cause the modified files to carry prominent notices\n"
"    stating that you changed the files and the date of any change.\n"
"\n"
"    b) You must cause any work that you distribute or publish, that in\n"
"    whole or in part contains or is derived from the Program or any\n"
"    part thereof, to be licensed as a whole at no charge to all third\n"
"    parties under the terms of this License.\n"
"\n"
"    c) If the modified program normally reads commands interactively\n"
"    when run, you must cause it, when started running for such\n"
"    interactive use in the most ordinary way, to print or display an\n"
"    announcement including an appropriate copyright notice and a\n"
"    notice that there is no warranty (or else, saying that you provide\n"
"    a warranty) and that users may redistribute the program under\n"
"    these conditions, and telling the user how to view a copy of this\n"
"    License.  (Exception: if the Program itself is interactive but\n"
"    does not normally print such an announcement, your work based on\n"
"    the Program is not required to print an announcement.)\n"
" \n"
"These requirements apply to the modified work as a whole.  If\n"
"identifiable sections of that work are not derived from the Program,\n"
"and can be reasonably considered independent and separate works in\n"
"themselves, then this License, and its terms, do not apply to those\n"
"sections when you distribute them as separate works.  But when you\n"
"distribute the same sections as part of a whole which is a work based\n"
"on the Program, the distribution of the whole must be on the terms of\n"
"this License, whose permissions for other licensees extend to the\n"
"entire whole, and thus to each and every part regardless of who wrote it.\n"
"\n"
"Thus, it is not the intent of this section to claim rights or contest\n"
"your rights to work written entirely by you; rather, the intent is to\n"
"exercise the right to control the distribution of derivative or\n"
"collective works based on the Program.\n"
"\n"
"In addition, mere aggregation of another work not based on the Program\n"
"with the Program (or with a work based on the Program) on a volume of\n"
"a storage or distribution medium does not bring the other work under\n"
"the scope of this License.\n"
"\n"
"  3. You may copy and distribute the Program (or a work based on it,\n"
"under Section 2) in object code or executable form under the terms of\n"
"Sections 1 and 2 above provided that you also do one of the following:\n"
"\n"
"    a) Accompany it with the complete corresponding machine-readable\n"
"    source code, which must be distributed under the terms of Sections\n"
"    1 and 2 above on a medium customarily used for software interchange; or,\n"
"\n"
"    b) Accompany it with a written offer, valid for at least three\n"
"    years, to give any third party, for a charge no more than your\n"
"    cost of physically performing source distribution, a complete\n"
"    machine-readable copy of the corresponding source code, to be\n"
"    distributed under the terms of Sections 1 and 2 above on a medium\n"
"    customarily used for software interchange; or,\n"
"\n"
"    c) Accompany it with the information you received as to the offer\n"
"    to distribute corresponding source code.  (This alternative is\n"
"    allowed only for noncommercial distribution and only if you\n"
"    received the program in object code or executable form with such\n"
"    an offer, in accord with Subsection b above.)\n"
"\n"
"The source code for a work means the preferred form of the work for\n"
"making modifications to it.  For an executable work, complete source\n"
"code means all the source code for all modules it contains, plus any\n"
"associated interface definition files, plus the scripts used to\n"
"control compilation and installation of the executable.  However, as a\n"
"special exception, the source code distributed need not include\n"
"anything that is normally distributed (in either source or binary\n"
"form) with the major components (compiler, kernel, and so on) of the\n"
"operating system on which the executable runs, unless that component\n"
"itself accompanies the executable.\n"
"\n"
"If distribution of executable or object code is made by offering\n"
"access to copy from a designated place, then offering equivalent\n"
"access to copy the source code from the same place counts as\n"
"distribution of the source code, even though third parties are not\n"
"compelled to copy the source along with the object code.\n"
" \n"
"  4. You may not copy, modify, sublicense, or distribute the Program\n"
"except as expressly provided under this License.  Any attempt\n"
"otherwise to copy, modify, sublicense or distribute the Program is\n"
"void, and will automatically terminate your rights under this License.\n"
"However, parties who have received copies, or rights, from you under\n"
"this License will not have their licenses terminated so long as such\n"
"parties remain in full compliance.\n"
"\n"
"  5. You are not required to accept this License, since you have not\n"
"signed it.  However, nothing else grants you permission to modify or\n"
"distribute the Program or its derivative works.  These actions are\n"
"prohibited by law if you do not accept this License.  Therefore, by\n"
"modifying or distributing the Program (or any work based on the\n"
"Program), you indicate your acceptance of this License to do so, and\n"
"all its terms and conditions for copying, distributing or modifying\n"
"the Program or works based on it.\n"
"\n"
"  6. Each time you redistribute the Program (or any work based on the\n"
"Program), the recipient automatically receives a license from the\n"
"original licensor to copy, distribute or modify the Program subject to\n"
"these terms and conditions.  You may not impose any further\n"
"restrictions on the recipients' exercise of the rights granted herein.\n"
"You are not responsible for enforcing compliance by third parties to\n"
"this License.\n"
"\n"
"  7. If, as a consequence of a court judgment or allegation of patent\n"
"infringement or for any other reason (not limited to patent issues),\n"
"conditions are imposed on you (whether by court order, agreement or\n"
"otherwise) that contradict the conditions of this License, they do not\n"
"excuse you from the conditions of this License.  If you cannot\n"
"distribute so as to satisfy simultaneously your obligations under this\n"
"License and any other pertinent obligations, then as a consequence you\n"
"may not distribute the Program at all.  For example, if a patent\n"
"license would not permit royalty-free redistribution of the Program by\n"
"all those who receive copies directly or indirectly through you, then\n"
"the only way you could satisfy both it and this License would be to\n"
"refrain entirely from distribution of the Program.\n"
"\n"
"If any portion of this section is held invalid or unenforceable under\n"
"any particular circumstance, the balance of the section is intended to\n"
"apply and the section as a whole is intended to apply in other\n"
"circumstances.\n"
"\n"
"It is not the purpose of this section to induce you to infringe any\n"
"patents or other property right claims or to contest validity of any\n"
"such claims; this section has the sole purpose of protecting the\n"
"integrity of the free software distribution system, which is\n"
"implemented by public license practices.  Many people have made\n"
"generous contributions to the wide range of software distributed\n"
"through that system in reliance on consistent application of that\n"
"system; it is up to the author/donor to decide if he or she is willing\n"
"to distribute software through any other system and a licensee cannot\n"
"impose that choice.\n"
"\n"
"This section is intended to make thoroughly clear what is believed to\n"
"be a consequence of the rest of this License.\n"
" \n"
"  8. If the distribution and/or use of the Program is restricted in\n"
"certain countries either by patents or by copyrighted interfaces, the\n"
"original copyright holder who places the Program under this License\n"
"may add an explicit geographical distribution limitation excluding\n"
"those countries, so that distribution is permitted only in or among\n"
"countries not thus excluded.  In such case, this License incorporates\n"
"the limitation as if written in the body of this License.\n"
"\n"
"  9. The Free Software Foundation may publish revised and/or new versions\n"
"of the General Public License from time to time.  Such new versions will\n"
"be similar in spirit to the present version, but may differ in detail to\n"
"address new problems or concerns.\n"
"\n"
"Each version is given a distinguishing version number.  If the Program\n"
"specifies a version number of this License which applies to it and \"any\n"
"later version\", you have the option of following the terms and conditions\n"
"either of that version or of any later version published by the Free\n"
"Software Foundation.  If the Program does not specify a version number of\n"
"this License, you may choose any version ever published by the Free Software\n"
"Foundation.\n"
"\n"
"  10. If you wish to incorporate parts of the Program into other free\n"
"programs whose distribution conditions are different, write to the author\n"
"to ask for permission.  For software which is copyrighted by the Free\n"
"Software Foundation, write to the Free Software Foundation; we sometimes\n"
"make exceptions for this.  Our decision will be guided by the two goals\n"
"of preserving the free status of all derivatives of our free software and\n"
"of promoting the sharing and reuse of software generally.\n"
"\n"
"			    NO WARRANTY\n"
"\n"
"  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY\n"
"FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN\n"
"OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES\n"
"PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED\n"
"OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF\n"
"MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS\n"
"TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE\n"
"PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,\n"
"REPAIR OR CORRECTION.\n"
"\n"
"  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\n"
"WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR\n"
"REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,\n"
"INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING\n"
"OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED\n"
"TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY\n"
"YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER\n"
"PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE\n"
"POSSIBILITY OF SUCH DAMAGES.\n"
"\n"
"		     END OF TERMS AND CONDITIONS\n"
"","DO NOT TRANSLATE"))
        self.tabWidget2.changeTab(self.tab_3,self.__tr("License Agreement"))
        self.textBrowser4_2.setText(self.__trUtf8("\x42\x6a\x6f\x72\x6e\x20\x4f\x76\x65\x20\x47\x72\x6f\x74\x61\x6e\x0a\x43\x6f\x6e\x74\x72\x69\x62\x75\x74\x65\x64\x20\x68\x69\x73\x20\x6d\x6b\x70\x61\x73\x73\x77\x64\x20\x6d\x6f\x64\x75\x6c\x65\x2e\x0a\x54\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x20\x69\x6e\x74\x6f\x20\x4e\x6f\x72\x77\x65\x67\x69\x61\x6e\x2e\x0a\x0a\x4b\x65\x72\x73\x74\x69\x6e\x20\x49\x73\x65\x62\x72\x65\x63\x68\x74\x0a\x54\x68\x61\x6e\x6b\x73\x20\x66\x6f\x72\x20\x74\x68\x65\x20\x69\x63\x65\x20\x61\x6e\x64\x20\x61\x6c\x6c\x20\x79\x6f\x75\x72\x20\x70\x61\x74\x69\x65\x6e\x63\x65\x20\x3a\x29\x20\x0a\x0a\x4a\x6f\x65\x72\x6e\x20\x4b\x6f\x65\x72\x6e\x65\x72\x0a\x4c\x75\x6d\x61\x2d\x63\x72\x61\x73\x68\x2d\x74\x65\x73\x74\x2d\x64\x75\x6d\x6d\x79\x2e\x20\x48\x65\x20\x61\x6c\x73\x6f\x20\x68\x61\x64\x20\x74\x68\x65\x20\x69\x64\x65\x61\x20\x77\x69\x74\x68\x20\x74\x68\x65\x20\x70\x6c\x75\x67\x69\x6e\x20\x73\x75\x70\x70\x6f\x72\x74\x2e\x20\x0a\x0a\x46\x65\x72\x6e\x61\x6e\x64\x6f\x20\x4d\x61\x63\x69\x65\x6c\x20\x53\x6f\x75\x74\x6f\x20\x4d\x61\x69\x6f\x72\x0a\x50\x6f\x72\x74\x75\x67\x75\x65\x73\x65\x20\x74\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x20\x0a\x0a\x4a\x61\x6e\x20\x57\x69\x6e\x68\x75\x79\x73\x65\x6e\x0a\x4d\x79\x20\x6d\x65\x6e\x74\x6f\x72\x20\x61\x6e\x64\x20\x55\x49\x20\x74\x65\x73\x74\x65\x72\x20\x3a\x29\x20\x0a\x0a\x45\x72\x69\x63\x20\x43\x6f\x74\x65\x0a\x54\x65\x73\x74\x69\x6e\x67\x20\x67\x75\x69\x6e\x65\x61\x20\x70\x69\x67\x20\x66\x6f\x72\x20\x70\x79\x74\x68\x6f\x6e\x20\x32\x2e\x33\x0a\x0a\x4a\x69\x72\x6b\x61\x20\x4a\x75\x72\x65\x6b\x20\x28\x6a\x69\x72\x69\x2e\x6a\x75\x72\x65\x6b\x20\x61\x74\x20\x74\x72\x69\x6e\x65\x74\x2e\x61\x73\x29\x0a\x43\x7a\x65\x63\x68\x20\x74\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x0a\x0a\x4d\x61\x67\x6e\x75\x73\x20\x4d\xc3\xa4\xc3\xa4\x74\x74\xc3\xa4\x0a\x53\x77\x65\x64\x69\x73\x68\x20\x74\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x0a\x0a\x41\x6c\x65\x78\x61\x6e\x64\x65\x72\x20\x4e\x6f\x76\x69\x74\x73\x6b\x79\x0a\x52\x75\x73\x73\x69\x61\x6e\x20\x74\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x0a\x0a\x4e\x65\x78\x74\x67\x65\x6e\x73\x20\x28\x6e\x65\x78\x74\x67\x65\x6e\x73\x20\x61\x74\x20\x75\x73\x65\x72\x73\x2e\x73\x6f\x75\x72\x63\x65\x66\x6f\x72\x67\x65\x2e\x6e\x65\x74\x29\x0a\x46\x72\x65\x6e\x63\x68\x20\x74\x72\x61\x6e\x73\x6c\x61\x74\x69\x6f\x6e\x0a\x0a\x52\x65\x62\x65\x6b\x6b\x61\x20\x47\x6f\x6c\x6f\x6d\x62\x65\x6b\x20\x28\x72\x65\x62\x65\x6b\x6b\x61\x67\x6f\x6c\x6f\x6d\x62\x65\x20\x61\x74\x20\x77\x65\x62\x2e\x64\x65\x29\x0a\x4c\x75\x6d\x61\x20\x6c\x6f\x67\x6f","\x44\x4f\x20\x4e\x4f\x54\x20\x54\x52\x41\x4e\x53\x4c\x41\x54\x45"))
        self.tabWidget2.changeTab(self.tab_4,self.__tr("Credits"))
        self.pushButton1.setText(self.__tr("&Close"))


    def __tr(self,s,c = None):
        return qApp.translate("AboutDialog",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("AboutDialog",s,c,QApplication.UnicodeUTF8)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = AboutDialog()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
