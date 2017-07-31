# Romain Truchard
#cc207
#artstation.com/artist/romaintruc

import maya.cmds as cmds

if (cmds.window(RigWindow, exists=True)):

	cmds.deleteUI(RigWindow)

#sizeable=False

RigWindow = cmds.window( widthHeight=(275, 400), title="Rigging toolkit 1.0" )

form = cmds.formLayout()

tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

#separator variables 



# ---------------------------------------------------------------------------------
#                                         Tab 1                                    
# ---------------------------------------------------------------------------------

tab1 = cmds.rowColumnLayout(numberOfColumns=1)

cmds.separator(style="in", w=265, h=20)

#---Start---Text Creator---------------------------------------


cmds.text(l="Name: ")

cmds.separator(style="none", w=265, h=10)

cmds.textField()

cmds.separator(style="none", w=265, h=10)

cmds.button(label="Create Nurbs text", command=nurbsTxt)

cmds.separator(style="in", w=265, h=20)

cmds.text(label="Nurbs shapes")

#---End---Text Creator----------------------------------------

cmds.separator(style="none", w=265, h=10)

#---Start---Nurbs shapes--------------------------------------

cmds.rowLayout(numberOfColumns=6)

cmds.button(label="Joystick", w=50)
cmds.button(label="Slider",   w=45)
cmds.button(label="Square",   w=50)
cmds.button(label="Cube", w=38)
cmds.button(label="Arrow", w=45)
cmds.button(label="Pin", w=30)

cmds.setParent( '..' )

cmds.rowLayout(numberOfColumns=6)

cmds.button(label="Move", w=40)
cmds.button(label="Orient", w=44)
cmds.button(label="Cone",   w=38)
cmds.button(label="Cross",   w=40)
cmds.button(label="Rotate", w=50)
cmds.button(label="Sphere", w=45)

cmds.setParent( '..' )

#---End---Nurbs shapes----------------------------------------

cmds.separator(style="in", w=265, h=20)

#---Start---Color Picker--------------------------------------

cmds.text(label="Color picker")

cmds.separator(style="none", w=265, h=10)

cmds.rowLayout(numberOfColumns=10)

cmds.button(l="", bgc=(1, 0.224, 0.224), width=25, height=22)
cmds.button(l="", bgc=(1, 0.399, 0.321), width=25, height=22)
cmds.button(l="", bgc=(1, 0.479, 0.173), width=25, height=22)
cmds.button(l="", bgc=(1, 1, 0.390), width=25, height=22)
cmds.button(l="", bgc=(0.527, 1, 0.276), width=25, height=22)
cmds.button(l="", bgc=(0.369, 1, 0.869), width=25, height=22)
cmds.button(l="", bgc=(0.256, 0.628, 1), width=25, height=22)
cmds.button(l="", bgc=(1, 0.442, 0.706), width=25, height=22)
cmds.button(l="", bgc=(0.466, 0.200, 0.892), width=25, height=22)
cmds.button(l="R", width=25, height=22)

cmds.setParent( '..' )

cmds.radioButtonGrp( numberOfRadioButtons=3, labelArray3=['Viewport', 'Outliner', 'Both'], select=1)

#---End---Color Picker---------------------------------------

cmds.separator(style="in", w=265, h=20)

cmds.setParent( '..' )

# ---------------------------------------------------------------------------------
#                                         Tab 2                                    
# ---------------------------------------------------------------------------------

tab2 = cmds.rowColumnLayout(numberOfColumns=1)

cmds.separator(style="in", w=265, h=20)


cmds.text(label="Create and place joints :")

cmds.separator(style="none", w=265, h=10)

cmds.rowLayout(numberOfColumns=2)

cmds.button(l="To vertex", width=133)

cmds.button(l="To center of selection", width=133)

cmds.setParent( '..' )


cmds.separator(style="in", w=265, h=20)


cmds.text(label="Set joint size")

cmds.separator(style="none", w=265, h=10)

cmds.rowColumnLayout(numberOfColumns=1)

cmds.floatSliderGrp(min=0,max=100,w=255,field=True)

cmds.setParent( '..' )

cmds.separator(style="none", w=265, h=10)

cmds.button(l="Resize joint")


cmds.setParent( '..' )

# ---------------------------------------------------------------------------------
#                                         Tab 3                                   
# ---------------------------------------------------------------------------------

tab3 = cmds.rowColumnLayout(numberOfColumns=1)

cmds.separator(style="in", w=265, h=20)

cmds.text(l="Name: ")

cmds.separator(style="none", w=265, h=10)

cmds.textField()

cmds.separator(style="none", w=265, h=10)

cmds.rowLayout(numberOfColumns=6)

cmds.button(label="Joystick", w=50)
cmds.button(label="Slider",   w=45)
cmds.button(label="Square",   w=50)
cmds.button(label="Cube", w=38)
cmds.button(label="Arrow", w=45)
cmds.button(label="Pin", w=30)

cmds.setParent( '..' )

cmds.rowLayout(numberOfColumns=6)

cmds.button(label="Move", w=40)
cmds.button(label="Orient", w=44)
cmds.button(label="Cone",   w=38)
cmds.button(label="Cross",   w=40)
cmds.button(label="Rotate", w=50)
cmds.button(label="Sphere", w=45)

cmds.setParent( '..' )

cmds.separator(style="none", w=265, h=10)

cmds.radioButtonGrp( numberOfRadioButtons=2, labelArray2=['Rename', 'Append'], select=1, width=265)

cmds.separator(style="none", w=265, h=10)

cmds.rowLayout(numberOfColumns=2)

cmds.button(label="Add prefix", w=133)
cmds.button(label="Add sufix", w=133)

cmds.setParent( '..' )


cmds.separator(style="in", w=265, h=20)

cmds.setParent( '..' )

# ---------------------------------------------------------------------------------
#                                      -Init Window-                                
# ---------------------------------------------------------------------------------

cmds.tabLayout( tabs, edit=True, tabLabel=((tab1, 'Tools'), (tab2, 'Joints'), (tab3, 'Naming') ) )

cmds.showWindow(RigWindow)


def nurbsTxt(*args):
	cmds.textCurves(font="Helvetica", t="text", n="test") 















