# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/daten/src/cvs/luma/lib/luma/plugins/config_create/ConfigError.ui'
#
# Created: Mon Sep 1 00:18:37 2003
#      by: The PyQt User Interface Compiler (pyuic) 3.7
#
# WARNING! All changes made in this file will be lost!

###########################################################################
#    Copyright (C) 2003 by Wido Depping
#    <wido.depping@tu-clausthal.de>
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################


import sys
from qt import *

image0_data = [
"64 64 278 2",
"Qt c None",
".c c #000000",
"#7 c #010101",
"#6 c #020202",
"bZ c #030303",
"bD c #040404",
"cl c #050505",
"cm c #060606",
"#X c #070707",
"b9 c #080808",
"bs c #090909",
"cg c #0a0a0a",
"ch c #0b0b0b",
"#M c #0c0c0c",
".R c #0d0d0d",
"#U c #0e0e0e",
".j c #0f0f0f",
"#w c #101010",
"#P c #111111",
"cb c #121212",
".S c #131313",
"cn c #141414",
"#W c #151515",
"ck c #161616",
"b8 c #171717",
"bY c #181818",
"## c #191919",
"bn c #1a1a1a",
"ca c #1b1b1b",
"#I c #1c1c1c",
"cp c #1d1d1d",
"cq c #1e1e1e",
"cf c #1f1f1f",
"b5 c #202020",
"by c #212121",
"cr c #222222",
"aW c #232323",
"bm c #242424",
"#V c #252525",
"cs c #262626",
".l c #272727",
"ao c #282828",
"bX c #292929",
"bN c #2a2a2a",
"ct c #2b2b2b",
"cj c #2c2c2c",
"b4 c #2d2d2d",
"bM c #2e2e2e",
"bG c #2f2f2f",
".Y c #303030",
"c# c #313131",
"bS c #323232",
".x c #333333",
"#L c #343434",
"ce c #353535",
"bW c #363636",
".G c #373737",
"aB c #383838",
"ci c #393939",
"#s c #3a3a3a",
"aC c #3b3b3b",
"ax c #3c3c3c",
"co c #3d3d3d",
"c. c #3e3e3e",
"bV c #3f3f3f",
"#y c #404040",
"br c #414141",
"cd c #424242",
"b3 c #434343",
"#K c #444444",
"bc c #454545",
".V c #464646",
"b7 c #474747",
"bR c #484848",
"#d c #494949",
"bl c #4a4a4a",
"cc c #4b4b4b",
"#N c #4c4c4c",
"#t c #4d4d4d",
"bk c #4e4e4e",
"#i c #4f4f4f",
"b2 c #505050",
"bL c #515151",
".F c #524200",
".Q c #525252",
"bb c #535353",
"#J c #545454",
"bQ c #555555",
"bC c #565656",
"ba c #575757",
"a6 c #585858",
"b1 c #595959",
"bF c #5a5a5a",
".k c #5b5b5b",
"a5 c #5c5c5c",
"b6 c #5d5d5d",
"bK c #5e5e5e",
"bx c #5f5f5f",
".A c #604e00",
".y c #606060",
"aV c #616161",
"bU c #626262",
"#v c #636363",
"bj c #646464",
"aU c #656565",
"b0 c #666666",
"bJ c #676767",
"bq c #686868",
"a4 c #696969",
"ad c #6a6a6a",
"bP c #6b6b6b",
"bw c #6c6c6c",
"b# c #6d6d6d",
"aN c #6e6e6e",
"bT c #6f6f6f",
".H c #707070",
"bi c #717171",
"aT c #727272",
"#u c #737373",
"bI c #747474",
"bv c #757575",
"a3 c #767676",
"aA c #777777",
"bO c #787878",
"bB c #797979",
"b. c #7a7a7a",
"aM c #7b7b7b",
"aw c #7c7c7c",
"bE c #7d7d7d",
"bh c #7e7e7e",
"#. c #7f7f7f",
"#a c #808080",
"bA c #818181",
"#c c #828282",
"aL c #838383",
"an c #848484",
"bz c #858585",
"bg c #868686",
"aK c #878787",
".X c #888888",
"bH c #898989",
"bp c #8a8a8a",
"a2 c #8b8b8b",
".P c #8c8c8c",
"am c #8d8d8d",
"ae c #8e8e8e",
"a9 c #8f8f8f",
"aJ c #909090",
"ac c #919191",
"#b c #929292",
".r c #937600",
"bf c #939393",
"aS c #949494",
"av c #959595",
"ab c #969696",
"#e c #979797",
".B c #987a00",
"a1 c #989898",
"#T c #999999",
"#5 c #9a9a9a",
"ap c #9b9b9b",
"be c #9c9c9c",
"aI c #9d9d9d",
"al c #9e9e9e",
".I c #9f9f9f",
"bo c #a0a0a0",
"a0 c #a1a1a1",
"au c #a2a2a2",
".e c #a38300",
"#4 c #a3a3a3",
"bu c #a4a4a4",
".U c #a5a5a5",
".s c #a6a6a6",
".T c #a7a7a7",
"#S c #a8a8a8",
"bd c #a9a9a9",
".f c #aa8900",
"aR c #aaaaaa",
"ak c #ababab",
".O c #acacac",
"bt c #adadad",
"aZ c #aeaeae",
"az c #afafaf",
"#3 c #b0b0b0",
".w c #b18e00",
"#H c #b1b1b1",
"#r c #b2b2b2",
"aH c #b3b3b3",
"aa c #b4b4b4",
"#G c #b5b5b5",
".u c #b6b6b6",
"aQ c #b7b7b7",
"at c #b8b8b8",
"#R c #b9b9b9",
"#F c #bababa",
".E c #bb9600",
"a8 c #bbbbbb",
".J c #bcbcbc",
"a# c #bdbdbd",
"#E c #bebebe",
".i c #bf9a00",
"#j c #bfbfbf",
"aG c #c0c0c0",
"aj c #c1c1c1",
"#D c #c2c2c2",
".C c #c39d00",
"#q c #c3c3c3",
"aY c #c4c4c4",
".g c #c59e00",
"#x c #c5c5c5",
"#2 c #c6c6c6",
".D c #c7a000",
"#p c #c7c7c7",
"a7 c #c8c8c8",
"aF c #c9c9c9",
"a. c #cacaca",
"#C c #cbcbcb",
"#o c #cccccc",
"aP c #cdcdcd",
"ai c #cecece",
"#z c #cfcfcf",
".9 c #d0d0d0",
"aX c #d1d1d1",
"ay c #d2d2d2",
"#1 c #d3d3d3",
"#n c #d4d4d4",
".8 c #d5d5d5",
"aE c #d6d6d6",
"ah c #d7d7d7",
".K c #d8d8d8",
".v c #d9b210",
".7 c #d9d9d9",
"aO c #dadada",
"as c #dbdbdb",
".N c #dcdcdc",
".6 c #dddddd",
"#Y c #dfdfdf",
"#9 c #e0e0e0",
"#m c #e1e1e1",
".5 c #e2e2e2",
".o c #e3b600",
"#O c #e3e3e3",
"ag c #e4e4e4",
"#Q c #e5e5e5",
".4 c #e6e6e6",
"ar c #e8e8e8",
"#0 c #e9e9e9",
".3 c #eaeaea",
"aD c #ececec",
".p c #edbf00",
"#8 c #ededed",
".b c #eebf00",
"#B c #eeeeee",
".M c #efefef",
".n c #f1c200",
"aq c #f1f1f1",
".t c #f2f2f2",
".2 c #f3f3f3",
"#h c #f4edd4",
".L c #f4f4f4",
"#f c #f5e9b6",
"#Z c #f6f6f6",
".# c #f7c700",
".z c #f7e497",
"#l c #f7f7f7",
".d c #f8c700",
".1 c #f8f8f8",
".h c #f9c800",
"#g c #f9e079",
"af c #fafafa",
".q c #fbca00",
"#A c #fbfbfb",
".W c #fcd63d",
".0 c #fcfcfc",
".m c #fdcb00",
".Z c #fefefe",
".a c #ffcd00",
"#k c #ffffff",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.b.c.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.d.a.a.e.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.f.a.a.g.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.cQtQtQtQtQtQtQtQtQt.c.h.a.i.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.j.k.k.l.c.e.h.m.a.#.n.o.p.q.a.a.r.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.s.t.t.t.u.v.a.a.a.a.a.a.a.a.a.w.c.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQt.c.x.y.s.t.t.t.z.a.a.A.c.B.C.g.D.E.F.c.c.c.cQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.G.H.I.J.K.L.M.N.O.P.Q.R.c.c.c.c.cQt.S.T.U.V.t.t.t.W.a.W.X.c.c.c.c.c.c.c.c.c.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.Y.I.M.Z.0.1.2.M.3.4.5.6.7.8.9#.##.c.c.c.c#a#b#c#d#e.t.t#f#g#h.t#i.c.c.c.c.c.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.y#j#k.Z.0#l.2.M.3.4#m.6.7#n.9#o#p#q#r#s.c.c#t#u#v#i#w.c#e.t.t.t.t.t#x.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQt.c.c#y#z#k.Z#A#l.2#B.3.4#m.6.K#n.9#C#p#D#E#F#G#H#y#I#J#K#L#M.c.c.c#N#O.t.t.t.t.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQt.c#P.I#k.Z#A#l.t#B.3#Q#m.N.K#n#z#C#p#D#E#R#G#H.O#S#T#U#V#W#X.c.c.c.c.c.j.k.s.u.k.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQt.c.Y#Y.Z#A#Z.t#B#0#Q#m.N.K#1#z#C#2#D#E#R#G#3.O#S#4.I#5#V#6#7.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQt.c.y.Z#A#Z.t#8#0#Q#9.N.K#1#za.#2#Da##Raa#3.O.T#4.I#5abacad.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.caeaf#Z.t#8#0ag#9.Nah#1aia.#2aja##Raa#3ak.T#4al#5abacam.Xanao.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.cap#Zaq#8arag#9asah#1aia.#xaja#ataa#3ak.Taual#5avac.P.Xan#aawax.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQt.c.kaq#8arag#Yasahayaia.#xaj.Jataaazak.saual#Tavac.P.Xan#aawaA#uaB.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQt.caCaDarag#YasaEayaiaF#xaG.JataHazak.sauaI#TavaJ.PaKaL#.aMaA#uaNad.x.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.c#P.7#O#YaOaEayaPaF#xaG.JaQaHazaR.sauaI#TaSaJ.PaKaL#.aMaAaTaNadaUaVaW.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.cam#YaOaEaXaPaFaYaG.JaQaHaZaR.sa0aIa1aSaJa2aKaL#.aMa3aTaNa4aU.ya5a6#w.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.c.GaOaEaXaPa7aYaGa8aQ#raZaR.Ua0aIa1aSa9a2aK#c#.b.a3aTb#a4aU.ya5babbbc.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.c#baX#oa7aY#ja8aQ#raZbd.Ua0bea1bfa9a2bg#cbhb.a3bib#a4bj.ya5babbbkblbm.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQt.cbn#oa7#q#ja8.u#raZbd.Ubobea1bfa9bpbg#cbhb.a3bib#bqbj.y.kba.Qbkblbcbrbs#7#7#7.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQt.cba#q#j#F.u#rbtbdbubobe#ebfa9bpbg#cbhb.bvbibwbqbjbx.kba.Qbk#dbcbraxby#7#7#7#7#7#7.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQtQt.c#c#F.u#Hbtbdbuboap#ebfaebpbzbAbhbBbvbibwbq#vbx.kbC.Qbk#dbc#yaxaB.YbD#7#7#7#7#7#7#7#7.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQt.c.cal#Hbt#Sbu.Iap#e#baebpbzbAbEbBbv.Hbwbq#vbxbFbC.Q#t#d#K#yax.G.xbG.j#7#7#7#7#7#7#7#7#7#7.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQt.c.c.O#Sbu.Iapab#baebHbzbAbEbBbI.HbwbJ#vbKbFbCbL#t#d#K#yaC.G.xbMbN###7#7#7#7#7#7#7#7#7#7#7#7#7.c.c.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQt.c.c#4.Iapab#bambHbzbAbEbObI.HbPbJ#vbKbFbQbL#tbR#K#yaC.GbSbMbN#Vbn#7#7#7#7#7#7#7#7#7#7#7#7#7#7.c.c.c.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c#5abacambHan#abEbObIbTbPbJbUbKbFbQbL#NbR#KbVaCbWbSbMbX#VbybYbZ#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7.c.c.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.cbwam.Xan#aawbObIbTbPb0bUbKb1bQb2#NbRb3bVaCbWbSb4bX#Vb5#I.S#6#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7.c.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.caCan#aawbO#ubTadb0bUb6b1bQb2#Nb7b3bV#sbWbSb4bXbmb5#Ib8.R#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6.c.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.cb9bIaA#ubTadb0aVb6b1#Jb2#Nb7b3c.#sbWc#b4aobmb5cab8cb#X#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#XbD.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.cbSaNadb0aVb6a6#Jb2ccb7cdc.#scec#b4aobmcfcab8cb#MbZ#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.Rch.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c#yaVa5a6#J#iccb7cdc.cicec#cjaobmcfcackcb.Rcl#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7bZcmbs#M.jcb#P.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.cb4bb#icc.Vcdc.cice.YcjaoaWcfbnckcb#Mcl#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6clb9ch#U#Pcnb8bn.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.ccgb4cdcoci#L.Ycj.laWcfbnck#wbsbZ#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck##cpb5.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.cbD#P##cfcqcabYcb#M#XbZ#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck###Icfcr#V.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7bZcmbs#M.jcb#WbYcacqbybm.l#V.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6clb9ch#U#Pcnb8bncpb5aWcsbXcjaW.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck###Icfcr#VbXcjbGbSbn.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck###Icfcr#VaoctbMc##L.G#U.c.c.c.c.cQtQtQtQtQtQtQt",
"QtQt.c.c.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7bZcmbs#M.jcb#WbYcacqbybm.lbNb4.Y.xbWci#L.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQtQt.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6clb9ch#U#Pcnb8bncpb5aWcsbXcjbGbSceaBaCc.b5.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQtQt.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck###Icfcr#VaoctbMc#ceaBaCc.brbVbD.c.c.c.c.cQtQtQtQtQtQtQtQt",
"QtQtQt.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7#7#7#7bZcmbs.R#w.Sck###Icfcr#VaoctbMc##L.G#sco#yb3.Vbm.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#7#7bZcmbs#M.jcb#WbYcacqbybm.lbNb4.Y.xbWciaxbVcdbcbRbrcl.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.c.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#7#7#6clb9ch#U#Pcnb8bncpb5aWcsbXcjbGbSceaBaCc.br#Kb7bl#t.S.c.c.c.c.c.cQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.c.c.c.c.c.c.c.c#7#7#7#7#7#7#7#6bD#Xcg.R#w.Sck###Icfcr#VaoctbMc##L.G#scobr#Kb7bl#N#iao.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.c.c.c.c.c.c.c.c#7#7#7#7#7#7bZcmbs#M.jcb#W###Icfcr#VaoctbMc##L.G#sco#yb3.V#d#NbkbL#L.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQt.c.c.c.c.c.c.c.c#7#7#7bZcmbs#M.jcb#WbYcacqbybm.lbNb4.Y.xbWciaxbVcdbcbRccbkbL#Jce.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQt.c.c.c.c.c.c.c.c#7#6clb9ch#U#Pcnb8bncpb5aWcsbXcjbGbSceaBaCc.br#Kb7bl#tb2bbbC.G.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQt.c.c.c.c.c.c.c.c#Xcg.R#w.Sck###Icfcr#VaoctbMc##L.G#sco#yb3.V#d#N#i.QbQa6b4.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.c.c.c.c.c.c.c#6#Ucb#WbYcacqby#VaoctbMc##L.G#sco#yb3.V#d#NbkbL#Jba#ib8.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.cbDckcacqbybm.lbNb4.Y.xbWciaxbVcdbcbRccbkb2bbbCb1.xcm.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c#6bYaWcsbXcjbGbSceaBaCc.br#Kb7bl#tb2bbbCb1ci#M.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.ccgb5bMc##L.G#sco#yb3.V#d#N#i.QbQ#t.xch.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.ccmcactci#yb3.V#d#Nbk#NbVct#P.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]

class ConfigError(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap(image0_data)

        if not name:
            self.setName("ConfigError")


        ConfigErrorLayout = QGridLayout(self,1,1,11,6,"ConfigErrorLayout")

        self.pushButton6 = QPushButton(self,"pushButton6")

        ConfigErrorLayout.addMultiCellWidget(self.pushButton6,2,2,0,1)

        self.suffixIcon = QLabel(self,"suffixIcon")
        self.suffixIcon.setSizePolicy(QSizePolicy(0,0,0,0,self.suffixIcon.sizePolicy().hasHeightForWidth()))
        self.suffixIcon.setFrameShape(QLabel.NoFrame)
        self.suffixIcon.setFrameShadow(QLabel.Plain)
        self.suffixIcon.setPixmap(self.image0)
        self.suffixIcon.setScaledContents(1)

        ConfigErrorLayout.addWidget(self.suffixIcon,0,0)
        spacer = QSpacerItem(41,131,QSizePolicy.Minimum,QSizePolicy.Expanding)
        ConfigErrorLayout.addItem(spacer,1,0)

        self.errorLabel = QLabel(self,"errorLabel")

        ConfigErrorLayout.addMultiCellWidget(self.errorLabel,0,1,1,1)

        self.languageChange()

        self.resize(QSize(287,127).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton6,SIGNAL("clicked()"),self,SLOT("close()"))


    def languageChange(self):
        self.setCaption(self.__tr("Info"))
        self.pushButton6.setText(self.__tr("Ok"))
        self.errorLabel.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("ConfigError",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = ConfigError()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
