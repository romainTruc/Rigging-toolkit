import maya.cmds as cmds

#----------------------------------------------SHORTCUT FUNCTIONS START---------------------------------------------#


def sel(thingToSelect):

	cmds.select(thingToSelect, r=True)

def selAdd(thingToSelect):

	cmds.select(thingToSelect, add=True)


def parent(firstItem, allOtherItems):

	sel(firstItem)

	selAdd(allOtherItems)

	cmds.parent()

	sel(allOtherItems)




def mergeTheseCurves(firstCurve, allOthers):

	shapeOfAll = cmds.listRelatives(allOthers, shapes=True)#put all shapes in array

	sel(shapeOfAll)

	selAdd(firstCurve)

	cmds.parent(r=True, s=True)

	sel(allOthers)

	cmds.delete()



def delIfExists(thingToDelete):

	if cmds.objExists(thingToDelete):
		cmds.delete(thingToDelete)



def colorBtt(command, buttonColor):

	cmds.button(c=command, bgc=buttonColor, label="", w=26, h=22)

	
def doRed(e):

	print "red"

	curSel = cmds.ls(sl=True) #put everything in array

	sel(curSel)

	print curSel

	curSel.remove(ent)

	print curSel
	# cmds.setAttr(curSel + ".overrideEnabled" ,1)
	# cmds.setAttr(curSel + ".overrideColor", 18 )



def doRedPale(e):

	print "redPale"

def doOrange(e):

	print "orange"


def doYellow(e):

	print "yellow"


def doGreen(e):

	print "green"


def doCyan(e):

	print "cyan"


def doBlue(e):

	print "blue"


def doPink(e):

	print "pink"


def doPurple(e):

	print "purple"




def scaleToX(objectToScale, value):

	cmds.setAttr(objectToScale + ".scaleX", value)

def scaleToY(objectToScale, value):

	cmds.setAttr(objectToScale + ".scaleY", value)

def scaleToZ(objectToScale, value):

	cmds.setAttr(objectToScale + ".scaleZ", value)

def scaleAll(objectToScale, value):

	cmds.setAttr(objectToScale + ".scaleX", value)
	cmds.setAttr(objectToScale + ".scaleY", value)
	cmds.setAttr(objectToScale + ".scaleZ", value)

def lockAllButTx(thingToLock):

	cmds.setAttr(thingToLock + ".ty", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".tz", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".rx", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".ry", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".rz", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".sx", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".sy", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".sz", lock=True, channelBox=False, keyable=False)
	cmds.setAttr(thingToLock + ".v", lock=True, channelBox=False, keyable=False)




def lockEverything(thingToLock):

	cmds.setAttr(thingToLock + ".tx", lock=True) 
	cmds.setAttr(thingToLock + ".ty", lock=True)
	cmds.setAttr(thingToLock + ".tz", lock=True)
	cmds.setAttr(thingToLock + ".rx", lock=True)
	cmds.setAttr(thingToLock + ".ry", lock=True)
	cmds.setAttr(thingToLock + ".rz", lock=True)
	cmds.setAttr(thingToLock + ".sx", lock=True)
	cmds.setAttr(thingToLock + ".sy", lock=True)
	cmds.setAttr(thingToLock + ".sz", lock=True)


def UnlockEverything(thingToLock):

	cmds.setAttr(thingToLock + ".tx", lock=False) 
	cmds.setAttr(thingToLock + ".ty", lock=False)
	cmds.setAttr(thingToLock + ".tz", lock=False)
	cmds.setAttr(thingToLock + ".rx", lock=False)
	cmds.setAttr(thingToLock + ".ry", lock=False)
	cmds.setAttr(thingToLock + ".rz", lock=False)
	cmds.setAttr(thingToLock + ".sx", lock=False)
	cmds.setAttr(thingToLock + ".sy", lock=False)
	cmds.setAttr(thingToLock + ".sz", lock=False)




#----------------------------------------------SHORTCUT FUNCTIONS END---------------------------------------------#


delIfExists("*_temp_curve")

tmpCrvs = ""

tempString = "_temp_curve"

#Show default circle part1

cmds.circle(n="Circle_shape_temp_curve")

cmds.setAttr("Circle_shape_temp_curve" + '.overrideEnabled', 1)
cmds.setAttr ("Circle_shape_temp_curve" + ".overrideColor", 14)
cmds.setAttr("Circle_shape_temp_curve" + ".ty", 80000)

lockEverything("Circle_shape_temp_curve")






def changeMinValue(*args):

	global minValueToInject

	intFieldMin = cmds.intField(minCtrlValue, query=True, value=True)#get user input

	intFieldMax = cmds.intSliderGrp(maxCtrlValue, query=True, value=True)#get user input

	checkBoxValue = cmds.checkBox(sliderCheckBox, query=True, value=True)#get user input

	if(checkBoxValue==True):

		minValueToInject = 0

		intFieldMin = cmds.intField(minCtrlValue, edit=True, value=minValueToInject)#get user input

	elif(checkBoxValue==False):

		minValueToInject = ( -(intFieldMax))

		intFieldMin = cmds.intField(minCtrlValue, edit=True, value=minValueToInject)#get user input


	






def lockAndScaleSlider(thingToLock):

	print minValueToInject

	intFieldMin = cmds.intField(minCtrlValue, query=True, value=True)#get user input
	
	intFieldMax = cmds.intSliderGrp(maxCtrlValue, query=True, value=True)#get user input

	floatFieldMax = float(intFieldMax)

	scaleRatioMax = floatFieldMax / (floatFieldMax*floatFieldMax)

	sliderBox = cmds.curve(n="sliderTemp", p=[[intFieldMax, 0, 0], [intFieldMax, 0.1, 0], [minValueToInject, 0.1, -0], [minValueToInject, 0, -0], [intFieldMax, 0, 0]],d=1)

	cmds.transformLimits(thingToLock, tx=[minValueToInject, intFieldMax], etx=[1, 1])

	parent("tempMainCurve", "sliderTemp")

	scaleToX(sliderBox, scaleRatioMax)

	scaleToX("tempMainCurve", intFieldMax)

	lockAllButTx('tempMainCurve')

	cmds.rename("sliderTemp", "Slider")

	cmds.rename("tempMainCurve", "Controler")



#Show default circle part1 END



def setNurbsTxt(*args):#romain truchard 2017
  
  #1-create text---

  fontName = cmds.optionMenu(fontOptionMenu, q=True, value=True)#query selected font

  nameFormat = ("\"" + fontName + "\"")#add quotation marks to selected font

  nurbsTextFieldValue = cmds.textField(nurbsTextField, query=True, text=True)#get user input

  tempCurveTxt = cmds.textCurves(font=nameFormat, text=nurbsTextFieldValue, name="txtTemp")#create textCurves with correct font

  #2-merge the curves---

  cmds.select(r=True, hi=True)#select everything : transform shpes etc

  curSel = cmds.ls(sl=True) #put everything in array

  shapes = cmds.ls(curSel, shapes=True)#put all shapes in array

  transforms = cmds.ls(curSel, transforms=True)#put all transforms in array

  tempGrp = cmds.group(em=True, n="grpTemp")#create empty group to put all shapes

  cmds.select(transforms)#select all transforms

  cmds.FreezeTransformations(transforms)#freeze transformations

  cmds.select(shapes)#select all shapes

  cmds.select(tempGrp, add=True)#add empty group to selection

  cmds.parent(r=True, s=True)#parent -r -s (merge curves in empty group)

  finalText = cmds.rename("grpTemp", nurbsTextFieldValue)#rename group with user input

  cmds.select(transforms[0])#select remaining transforms

  cmds.delete()#delete them

  cmds.select(finalText)

  boundingBox = cmds.xform(finalText, query=True, bb=True)

  halfOfXboundingBox = boundingBox[3] / 2

  cmds.xform(finalText, ws=True, piv=[halfOfXboundingBox, 0, 0])

  worldPosition = cmds.xform(finalText, q=True, piv=True, ws=True)

  cmds.xform(finalText, translation=(-worldPosition[0],-worldPosition[1],-worldPosition[2]))

  cmds.FreezeTransformations(finalText)



#------------------------------------------------------------------------------------------------------

#ALL CURVES--------------------------------------------------------------------------------------------------


#-------------CURVES------------------CURVES---------------CURVES-------------CRUVES--------------CURVES------------CURVES


def ctrl_Slide(*args):

	

	cmds.curve(n="tempMainCurve", p=[[0, -1.110223025e-16, 1.204591982e-15], [0.025, 0.1, 1.182387521e-15], [0.05, 0.1, 1.182387521e-15], [0.05, 0.1, 1.182387521e-15], [0.05, 0.1, 1.182387521e-15], [0.05, 0.2033434935, 1.159440656e-15], [-0.05, 0.2033434935, 1.159440656e-15], [-0.05, 0.1, 1.182387521e-15], [-0.025, 0.1, 1.182387521e-15], [0, -1.110223025e-16, 1.204591982e-15], [0, -1.110223025e-16, 1.204591982e-15], [0, -1.110223025e-16, 1.204591982e-15], [0, -1.110223025e-16, 1.204591982e-15]],d=1) 

	cmds.curve(n="tempSecondaryCurve1", p=[[-0.02844540985, 0.1842523583, 1.131662451e-15], [0.02844540985, 0.1273615386, 1.14429475e-15], [0, 0.1558069485, 1.1379786e-15], [0.02844540985, 0.1842523583, 1.131662451e-15], [0, 0.1558069485, 1.1379786e-15], [-0.02844540985, 0.1273615386, 1.14429475e-15]],d=1) 

	mergeTheseCurves("tempMainCurve", "tempSecondaryCurve*")
	
	cmds.select('tempMainCurve', r=True)

	lockAndScaleSlider('tempMainCurve')



def ctrl_Joy(e):

	print "OK"
	
	crv1 = cmds.curve(n="Joystick", p=[[-1, 1, -2.220446049e-16], [1, 1, -2.220446049e-16], [1, -1, 2.220446049e-16], [0, -1, 2.220446049e-16], [-1, -1, 2.220446049e-16], [-1, 1, -2.220446049e-16], [-1, 0, 0], [-0.8999999762, 0, 0], [-1, 0, 0], [-1, -1, 2.220446049e-16], [0, -1, 2.220446049e-16], [0, -0.8999999762, 4.786660061e-26], [0, -1, 2.220446049e-16], [1, -1, 2.220446049e-16], [1, 0, 0], [0.8999999762, 0, 0], [1, 0, 0], [1, 1, -2.220446049e-16], [0, 1, -2.220446049e-16], [0, 0.8999999762, -4.786660061e-26], [0, 1, -2.220446049e-16], [-1, 1, -2.220446049e-16], [-1, 1, -2.220446049e-16], [-1, 1, -2.220446049e-16]],d=1) 
	cmds.curve(n="tempCrv1", p=[[0.1006069316, 0, 0], [0.1670520627, 0, 0], [0.2334971938, 0, 0], [0.2999423249, 0, 0]],d=1) 
	cmds.curve(n="tempCrv2", p=[[-4.467845276e-17, 0.1006069316, 0], [-7.418601853e-17, 0.1670520627, 0], [-1.036935843e-16, 0.2334971938, 0], [-1.332011501e-16, 0.2999423249, 0]],d=1) 
	cmds.curve(n="tempCrv3", p=[[-0.1006069316, -8.935690552e-17, 0], [-0.1670520627, -1.483720371e-16, 0], [-0.2334971938, -2.073871686e-16, 0], [-0.2999423249, -2.664023001e-16, 0]],d=1) 
	cmds.curve(n="tempCrv4", p=[[6.701767914e-17, -0.1006069316, 0], [1.112790278e-16, -0.1670520627, 0], [1.555403764e-16, -0.2334971938, 0], [1.998017251e-16, -0.2999423249, 0]],d=1) 

	mergeTheseCurves(crv1, "tempCrv*")

	crv3 = cmds.curve(p=[[-0.04098660341, 0.04098660341, 0], [0.04098660341, -0.04098660341, 0], [0, 0, 0], [0.04098660341, 0.04098660341, 0], [-0.04098660341, -0.04098660341, 0]],d=1) 
	crv4 = cmds.circle(r=.1)
	mergeTheseCurves(crv3, crv4)



def Square_shape():

	cmds.curve(n="Square_shape", p=[[1.0, -1.0, 0.0], [1.0, 1.0, 0.0], [-1.0, 1.0, -0.0], [-1.0, -1.0, -0.0], [1.0, -1.0, 0.0]],d=1)

def Circle_shape(*args):

	cmds.circle(n="Circle_shape")

def Cube_shape(*args):

	cmds.curve(n="Cube_shape", p=[[-0.5, 0.5, -0.5], [-0.5, 0.5, 0.499886], [0.498585, 0.5, 0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.498802, -0.5, -0.5], [-0.5, -0.499632, 0.5], [-0.5, 0.5, 0.499886], [0.5, 0.5, 0.5], [0.5, -0.492074, 0.5], [-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.492602, 0.5], [0.5, 0.5, 0.5], [-0.499904, 0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.499034, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [0.498947, 0.5, 0.5], [0.5, -0.495186, 0.5]],d=1) 
	
def Arrow_shape(*args):

	cmds.curve(p=[[-0.75, 0.25, -5.551115123e-17], [0.25, 0.25, -5.551115123e-17], [0.25, 0.5, -1.110223025e-16], [0.75, 1.110223025e-16, -2.465190329e-32], [0.25, -0.5, 1.110223025e-16], [0.25, -0.25, 5.551115123e-17], [-0.75, -0.25, 5.551115123e-17], [-0.75, 0.25, -5.551115123e-17]],d=1, n="Arrow_shape") 

def Orient_shape(*args):

	cmds.curve(n="Orient_shape", p=[[-0.0987656, 0.0959835, 0.3020005], [-0.0987656, 0.500783, 0.1984575], [-0.0987656, 0.751175, 0.0258855], [-0.0987656, 0.751175, 0.0258855], [-0.336638, 0.751175, 0.0258855], [-0.336638, 0.751175, 0.0258855], [6.705758171e-17, 1.001567, -0.3020005], [6.705758171e-17, 1.001567, -0.3020005], [0.336638, 0.751175, 0.0258855], [0.336638, 0.751175, 0.0258855], [0.0987656, 0.751175, 0.0258855], [0.0987656, 0.751175, 0.0258855], [0.0987656, 0.500783, 0.1984575], [0.0987656, 0.0959835, 0.3020005], [0.0987656, 0.0959835, 0.3020005], [0.500783, 0.0959835, 0.1984575], [0.751175, 0.0959835, 0.0258855], [0.751175, 0.0959835, 0.0258855], [0.751175, 0.336638, 0.0258855], [0.751175, 0.336638, 0.0258855], [1.001567, 0, -0.3020005], [1.001567, 0, -0.3020005], [0.751175, -0.336638, 0.0258855], [0.751175, -0.336638, 0.0258855], [0.751175, -0.0959835, 0.0258855], [0.751175, -0.0959835, 0.0258855], [0.500783, -0.0959835, 0.1984575], [0.0987656, -0.0959835, 0.3020005], [0.0987656, -0.0959835, 0.3020005], [0.0987656, -0.500783, 0.1984575], [0.0987656, -0.751175, 0.0258855], [0.0987656, -0.751175, 0.0258855], [0.336638, -0.751175, 0.0258855], [0.336638, -0.751175, 0.0258855], [6.705758171e-17, -1.001567, -0.3020005], [6.705758171e-17, -1.001567, -0.3020005], [-0.336638, -0.751175, 0.0258855], [-0.336638, -0.751175, 0.0258855], [-0.0987656, -0.751175, 0.0258855], [-0.0987656, -0.751175, 0.0258855], [-0.0987656, -0.500783, 0.1984575], [-0.0987656, -0.0959835, 0.3020005], [-0.0987656, -0.0959835, 0.3020005], [-0.500783, -0.0959835, 0.1984575], [-0.751175, -0.0959835, 0.0258855], [-0.751175, -0.0959835, 0.0258855], [-0.751175, -0.336638, 0.0258855], [-0.751175, -0.336638, 0.0258855], [-1.001567, 0, -0.3020005], [-1.001567, 0, -0.3020005], [-0.751175, 0.336638, 0.0258855], [-0.751175, 0.336638, 0.0258855], [-0.751175, 0.0959835, 0.0258855], [-0.751175, 0.0959835, 0.0258855], [-0.0987656, 0.0959835, 0.3020005]],d=3) 

def Cone_shape(*args):

	cmds.curve( n="Cone_shape", p=[[-1, 0, -1], [1, 0, -1], [1, 0, 1], [-1, 0, 1], [0, 2, 0], [1, 0, -1], [-1, 0, -1], [0, 2, 0], [1, 0, 1], [-1, 0, 1], [-1, 0, -1], [-1, 0, -1]],d=1) 

def Foot_shape(*args):

	cmds.curve(n="Foot_shape", p=[[-1.288552668, 2.202085294e-16, 0.991731051], [-1.289021855, 2.362831868e-16, 1.064124872], [-1.289803833, 2.523115417e-16, 1.136310165], [-1.289960229, 2.683398967e-16, 1.208495459], [-1.288552668, 2.844145541e-16, 1.28088928], [-1.263390341, 3.612148374e-16, 1.626767007], [-1.208200045, 4.365334432e-16, 1.965971852], [-1.115891841, 5.099999522e-16, 2.296835595], [-0.9793757925, 5.812439449e-16, 2.617690014], [-0.8691342179, 6.237264167e-16, 2.809014058], [-0.7388739966, 6.623657876e-16, 2.983030314], [-0.586509853, 6.967453356e-16, 3.137862034], [-0.4099565115, 7.264483391e-16, 3.271632469], [-0.3053278039, 7.400188072e-16, 3.332748424], [-0.196007226, 7.50926886e-16, 3.381874044], [-0.0810564037, 7.583622832e-16, 3.415360096], [0.04046303698, 7.615147064e-16, 3.429557348], [0.2698954945, 7.559931426e-16, 3.404690435], [0.4704468837, 7.380856811e-16, 3.324042398], [0.6461834923, 7.096675698e-16, 3.196058603], [0.8011716078, 6.726140569e-16, 3.029184416], [0.8966424796, 6.427837218e-16, 2.89484053], [0.9777249493, 6.112170458e-16, 2.75267686], [1.044210489, 5.7812239e-16, 2.60363178], [1.095890572, 5.437081151e-16, 2.448643665], [1.140167925, 5.062687487e-16, 2.280031748], [1.179857673, 4.684821141e-16, 2.109855875], [1.215376868, 4.304639674e-16, 1.938637363], [1.247142568, 3.923300647e-16, 1.766897533], [1.276162655, 3.451633312e-16, 1.55447745], [1.289960229, 2.97811388e-16, 1.341223256], [1.288743818, 2.5036684e-16, 1.127552007], [1.27272195, 2.02922292e-16, 0.9138807587], [1.232093829, 1.437092118e-16, 0.6472087528], [1.172906754, 8.556108735e-17, 0.3853328811], [1.099122749, 2.824640645e-17, 0.1272105056], [1.014703838, -2.846634296e-17, -0.1282010115], [0.9944940413, -4.138857712e-17, -0.1863975805], [0.9739714531, -5.424135766e-17, -0.2442813581], [0.9532403373, -6.704783577e-17, -0.3019566082], [0.9324049577, -7.983116267e-17, -0.3595275945], [0.9314665836, -8.038679173e-17, -0.3620299253], [0.9032806072, -1.342596593e-16, -0.6046517515], [0.8982064364, -2.061441688e-16, -0.928390802], [0.9043927543, -2.691386135e-16, -1.212092559], [0.910162017, -2.961560765e-16, -1.333768396], [0.9809745039, -3.627389588e-16, -1.633631039], [1.032915246, -4.29321841e-16, -1.933493683], [1.060458262, -4.961825379e-16, -2.234607493], [1.058077572, -5.635988637e-16, -2.538223633], [1.048276777, -5.839873634e-16, -2.630045272], [1.031386044, -6.042832582e-16, -2.721449856], [1.008656539, -6.243013385e-16, -2.811603275], [0.9813394271, -6.438563945e-16, -2.899671418], [0.9259232258, -6.714564963e-16, -3.023971227], [0.8491329486, -6.953755556e-16, -3.131693093], [0.7525325523, -7.156367236e-16, -3.222941282], [0.6376859939, -7.322631515e-16, -3.297820056], [0.526384404, -7.437963131e-16, -3.349760798], [0.4112250542, -7.52296666e-16, -3.388042984], [0.2925207357, -7.58065176e-16, -3.414022044], [0.1705842399, -7.614028089e-16, -3.429053406], [0.02263392986, -7.615147064e-16, -3.429557348], [-0.1188520255, -7.563712791e-16, -3.406393411], [-0.2532480436, -7.455326539e-16, -3.357580582], [-0.3799285416, -7.285589578e-16, -3.281137851], [-0.5269926095, -6.98651452e-16, -3.146446419], [-0.6397538923, -6.639516455e-16, -2.990172383], [-0.723529843, -6.253161332e-16, -2.816173505], [-0.7836379147, -5.836015099e-16, -2.628307542], [-0.8351442242, -5.278881211e-16, -2.377396745], [-0.8653807216, -4.716422544e-16, -2.124087881], [-0.883105565, -4.150722708e-16, -1.869319324], [-0.8970769121, -3.583865311e-16, -1.614029448], [-0.9134115716, -3.323375604e-16, -1.496715313], [-0.9576889254, -2.679733358e-16, -1.206844615], [-1.022819036, -1.843010014e-16, -0.8300179214], [-1.101711966, -1.003277013e-16, -0.4518357982], [-1.111512762, -9.159969483e-17, -0.4125283515], [-1.130905826, -7.384271614e-17, -0.3325580289], [-1.149881835, -5.636355198e-17, -0.2538388717], [-1.158431465, -4.84689891e-17, -0.2182849212], [-1.210980412, 1.851518084e-17, 0.08338496155], [-1.251851816, 8.537587766e-17, 0.3844987708], [-1.278543344, 1.526069938e-16, 0.6872808006], [-1.288552668, 2.202085294e-16, 0.991731051]],d=1) 

def Hand_shape():

	cmds.curve(n="Hand_shape", p=[[-0.1698003126, -3.451335679e-16, -1.802565504], [-0.183856709, -3.689084274e-16, -1.86538899], [-0.1761113477, -3.614081201e-16, -1.931654859], [-0.1448430373, -3.183331068e-16, -1.968660474], [0.3049616483, 3.262049792e-16, -2.052616365], [0.754766334, 9.70806762e-16, -2.135424796], [1.20457102, 1.615408545e-15, -2.218233227], [1.654375705, 2.259946631e-15, -2.302189118], [1.789823906, 2.452810159e-15, -2.349521882], [1.879660535, 2.577963907e-15, -2.430704743], [1.924172457, 2.63591745e-15, -2.54401651], [1.923646537, 2.627180361e-15, -2.687735992], [1.876600639, 2.551755296e-15, -2.823279814], [1.783656304, 2.411948613e-15, -2.925260405], [1.655140679, 2.223190879e-15, -2.98421121], [1.501380914, 2.000912663e-15, -2.990665678], [0.8063542651, 1.003231127e-15, -2.892605579], [0.1133356725, 9.005146038e-18, -2.784505197], [-0.5756668067, -9.783097234e-16, -2.656324248], [-1.258645116, -1.955257926e-15, -2.498022451], [-1.662742608, -2.532253436e-15, -2.385714712], [-2.058807873, -3.096429949e-15, -2.25131835], [-2.441103607, -3.638790281e-15, -2.08192443], [-2.803892506, -4.150337249e-15, -1.864624016], [-3.04041289, -4.480661293e-15, -1.665682977], [-3.222715746, -4.730934287e-15, -1.434326166], [-3.344776903, -4.892318288e-15, -1.167971797], [-3.400572191, -4.955975354e-15, -0.8640380824], [-3.407361334, -4.957748251e-15, -0.7194580048], [-3.408986904, -4.952068613e-15, -0.5748779273], [-3.404875169, -4.93810838e-15, -0.4302978498], [-3.394452399, -4.915039495e-15, -0.2857177723], [-3.311787401, -4.768839237e-15, 0.1987019849], [-3.150808194, -4.511710867e-15, 0.6452555312], [-2.897458382, -4.123876505e-15, 1.044763179], [-2.537681569, -3.58555827e-15, 1.388045242], [-2.064067069, -2.882182848e-15, 1.744953403], [-1.599058526, -2.190702817e-15, 2.111328116], [-1.151261897, -1.522949873e-15, 2.497783396], [-0.7292831391, -8.907557114e-16, 2.914933256], [-0.6452794366, -7.661221547e-16, 2.976035551], [-0.5552515643, -6.353736977e-16, 2.990665678], [-0.4680923443, -5.11249716e-16, 2.960544828], [-0.3926945988, -4.064895851e-16, 2.887394194], [-0.296116637, -2.766196142e-16, 2.715896595], [-0.2511744171, -2.214501563e-16, 2.541243479], [-0.2670476267, -2.542142376e-16, 2.363721711], [-0.3529159531, -3.881448844e-16, 2.183618155], [-0.4280746442, -5.024144283e-16, 2.079247021], [-0.5066757181, -6.215090108e-16, 1.977457674], [-0.5887191748, -7.454127074e-16, 1.87853698], [-0.6742050143, -8.741095941e-16, 1.782771803], [-0.876349382, -1.178063131e-15, 1.562985223], [-1.100295507, -1.51470909e-15, 1.321110021], [-1.281785578, -1.787498929e-15, 1.125706986], [-1.356561782, -1.899884107e-15, 1.04533691], [-1.320177709, -1.84725987e-15, 1.047344966], [-1.23531341, -1.724505372e-15, 1.052221675], [-1.138400772, -1.584297928e-15, 1.058245845], [-1.065871679, -1.479314858e-15, 1.063696285], [-0.7152267427, -9.718152959e-16, 1.08922729], [-0.3651555364, -4.653030352e-16, 1.111889644], [-0.01508433018, 4.114552874e-17, 1.133404536], [0.3355606065, 5.484540005e-16, 1.155493159], [0.862866716, 1.311550553e-15, 1.19225972], [1.38931223, 2.073420942e-15, 1.229313146], [1.915184013, 2.834495119e-15, 1.266940302], [2.440768931, 3.595203039e-15, 1.305428055], [2.618242889, 3.850863726e-15, 1.296678665], [2.747523487, 4.034180685e-15, 1.237727859], [2.829758187, 4.146762262e-15, 1.127715043], [2.86609445, 4.190216803e-15, 0.9657796184], [2.849982186, 4.156882104e-15, 0.7841939258], [2.778504932, 4.04570982e-15, 0.6399007135], [2.658260589, 3.866700363e-15, 0.5415059385], [2.495847056, 3.62985414e-15, 0.4976155578], [2.180916841, 3.17394374e-15, 0.472849526], [1.86512603, 2.7168231e-15, 0.4486572247], [1.548761489, 2.2588744e-15, 0.4244649234], [1.232110082, 1.800479822e-15, 0.3996988916], [1.045743302, 1.530728854e-15, 0.3858337386], [0.8588027919, 1.260117979e-15, 0.3713948552], [0.6718622816, 9.894434067e-16, 0.3558085109], [0.4854955017, 7.195013485e-16, 0.3385009752], [0.423676044, 6.295985142e-16, 0.3262613919], [0.3718968694, 5.534223569e-16, 0.3002522774], [0.3379033393, 5.018968912e-16, 0.255883788], [0.3294408149, 4.859461315e-16, 0.18856608], [0.3472264593, 5.080675262e-16, 0.1246429438], [0.3845189397, 5.597283478e-16, 0.08567708298], [0.437875873, 6.356895281e-16, 0.06679178846], [0.5038548767, 7.307119989e-16, 0.0631103513], [0.7930628426, 1.148759913e-15, 0.07458496063], [1.082557674, 1.567221857e-15, 0.08605956996], [1.372626235, 1.986511861e-15, 0.09753417928], [1.663555393, 2.407043953e-15, 0.1090087886], [2.007793673, 2.904513911e-15, 0.1204355871], [2.352031952, 3.401967945e-15, 0.1315755203], [2.696270232, 3.899390131e-15, 0.142141723], [3.040508512, 4.396764544e-15, 0.1518473301], [3.159414151, 4.56770573e-15, 0.1397033686], [3.257378628, 4.706671084e-15, 0.09600423137], [3.331820156, 4.810093581e-15, 0.02361857087], [3.380156948, 4.874406195e-15, -0.07458496063], [3.408986904, 4.903690834e-15, -0.2966186511], [3.353765347, 4.812620224e-15, -0.5014404276], [3.20158334, 4.584665024e-15, -0.6511840793], [2.93953195, 4.203295895e-15, -0.7079833955], [2.281367483, 3.253190618e-15, -0.7112823457], [1.623776747, 2.303451598e-15, -0.7229003876], [0.9661860108, 1.353489639e-15, -0.7385345429], [0.3080215441, 4.027155451e-16, -0.7538818328], [0.2773269642, 3.58424983e-16, -0.7536905893], [0.2460586538, 3.132426647e-16, -0.7546468068], [0.2159378043, 2.695253745e-16, -0.759045407], [0.1886856071, 2.29629897e-16, -0.7691813119], [0.1643020623, 1.921310144e-16, -0.8107289599], [0.1588516229, 1.804771399e-16, -0.8789550745], [0.1706130974, 1.938242898e-16, -0.9443125368], [0.1978652946, 2.313284804e-16, -0.9772542277], [0.2837814319, 3.545129331e-16, -0.9919799764], [0.3711318954, 4.800860188e-16, -1.00096842], [0.4590560894, 6.066782545e-16, -1.006514482], [0.5466934182, 7.329201574e-16, -1.010913082], [1.024037166, 1.420716385e-15, -1.031615189], [1.501380914, 2.108496689e-15, -1.052604162], [1.978724662, 2.796245144e-15, -1.074166866], [2.45606841, 3.483945826e-15, -1.096590165], [2.585731496, 3.669834547e-15, -1.119156896], [2.683265675, 3.807568428e-15, -1.173852534], [2.752113331, 3.902052129e-15, -1.261824539], [2.795716846, 3.958190311e-15, -1.384220372], [2.803318775, 3.957500261e-15, -1.594301344], [2.739491261, 3.855341086e-15, -1.775122063], [2.61886443, 3.674325177e-15, -1.899717196], [2.45606841, 3.437064925e-15, -1.941121411], [2.21103769, 3.084189532e-15, -1.927160637], [1.966867566, 2.732747319e-15, -1.909757479], [1.723271172, 2.382196863e-15, -1.891206861], [1.479961643, 2.031996739e-15, -1.873803703], [1.076055395, 1.450465481e-15, -1.848177076], [0.6721491468, 8.689342228e-16, -1.822550448], [0.2682428985, 2.873392679e-16, -1.798071282], [-0.1356633499, -2.943830809e-16, -1.775887037], [-0.1698003126, -3.451335679e-16, -1.802565504]],d=1) 


def HalfSphere_shape():

	crv =cmds.curve(p=[[0, 0.81, 0], [-0.30997323, 0.7483428, 0], [-0.57275667, 0.57275667, 0], [-0.7483428, 0.30997323, 0], [-0.81, 0, 0], [0.81, 0, 0], [0.7483428, 0.30997323, 0], [0.57275667, 0.57275667, 0], [0.30997323, 0.7483428, 0], [0, 0.81, 0], [0, 0.7483428, 0.30997323], [0, 0.57275667, 0.57275667], [0, 0.30997323, 0.7483428], [0, 0, 0.81], [0, 0, -0.81], [0, 0.30997323, -0.7483428], [0, 0.57275667, -0.57275667], [0, 0.7483428, -0.30997323], [0, 0.81, 0], [-0.30997323, 0.7483428, 0], [-0.57275667, 0.57275667, 0], [-0.7483428, 0.30997323, 0], [-0.81, 0, 0], [-0.7483428, 0, 0.30997323], [-0.57275667, 0, 0.57275667], [-0.30997323, 0, 0.7483428], [0, 0, 0.81], [0.30997323, 0, 0.7483428], [0.57275667, 0, 0.57275667], [0.7483428, 0, 0.30997323], [0.81, 0, 0], [0.7483428, 0, -0.30997323], [0.57275667, 0, -0.57275667], [0.30997323, 0, -0.7483428], [0, 0, -0.81], [-0.30997323, 0, -0.7483428], [-0.57275667, 0, -0.57275667], [-0.7483428, 0, -0.30997323], [-0.81, 0, 0], [-0.81, 0, 0]],d=1, n="HalfSphere_shape") 

	cmds.select(crv, r=True)


def Sphere_shape():

	crv =cmds.curve(p=[[0, 0.81, 0], [-0.30997323, 0.7483428, 0], [-0.57275667, 0.57275667, 0], [-0.7483428, 0.30997323, 0], [-0.81, 0, 0], [-0.7483428, -0.30997323, 0], [-0.57275667, -0.57275667, 0], [-0.30997323, -0.7483428, 0], [0, -0.81, 0], [0.30997323, -0.7483428, 0], [0.57275667, -0.57275667, 0], [0.7483428, -0.30997323, 0], [0.81, 0, 0], [0.7483428, 0.30997323, 0], [0.57275667, 0.57275667, 0], [0.30997323, 0.7483428, 0], [0, 0.81, 0], [0, 0.7483428, 0.30997323], [0, 0.57275667, 0.57275667], [0, 0.30997323, 0.7483428], [0, 0, 0.81], [0, -0.30997323, 0.7483428], [0, -0.57275667, 0.57275667], [0, -0.7483428, 0.30997323], [0, -0.81, 0], [0, -0.7483428, -0.30997323], [0, -0.57275667, -0.57275667], [0, -0.30997323, -0.7483428], [0, 0, -0.81], [0, 0.30997323, -0.7483428], [0, 0.57275667, -0.57275667], [0, 0.7483428, -0.30997323], [0, 0.81, 0], [-0.30997323, 0.7483428, 0], [-0.57275667, 0.57275667, 0], [-0.7483428, 0.30997323, 0], [-0.81, 0, 0], [-0.7483428, 0, 0.30997323], [-0.57275667, 0, 0.57275667], [-0.30997323, 0, 0.7483428], [0, 0, 0.81], [0.30997323, 0, 0.7483428], [0.57275667, 0, 0.57275667], [0.7483428, 0, 0.30997323], [0.81, 0, 0], [0.7483428, 0, -0.30997323], [0.57275667, 0, -0.57275667], [0.30997323, 0, -0.7483428], [0, 0, -0.81], [-0.30997323, 0, -0.7483428], [-0.57275667, 0, -0.57275667], [-0.7483428, 0, -0.30997323], [-0.81, 0, 0], [-0.81, 0, 0]],d=1, n="Sphere_shape") 



def Move_shape():

	crv1 = cmds.curve(n="Move_shape", p=[[4.8046875, 2.602085214e-18, -0.01171875], [3.671875, 2.168404345e-16, -0.9765625], [3.671875, 1.127570259e-16, -0.5078125], [3.359375, 1.127570259e-16, -0.5078125], [3.024414062, 3.434345907e-16, -1.546691895], [2.393554688, 5.348369317e-16, -2.408691406], [1.526855469, 6.737096775e-16, -3.034118652], [0.484375, 7.467984564e-16, -3.36328125], [0.484375, 8.153200337e-16, -3.671875], [0.94921875, 8.153200337e-16, -3.671875], [-0.015625, 1.066854938e-15, -4.8046875], [-0.9765625, 8.153200337e-16, -3.671875], [-0.5078125, 8.153200337e-16, -3.671875], [-0.5078125, 7.459310947e-16, -3.359375], [-1.541687012, 6.72002059e-16, -3.026428223], [-2.400878906, 5.331022082e-16, -2.400878906], [-3.026428223, 3.423232834e-16, -1.541687012], [-3.359375, 1.127570259e-16, -0.5078125], [-3.671875, 1.127570259e-16, -0.5078125], [-3.671875, 2.168404345e-16, -0.9765625], [-4.8046875, 2.602085214e-18, -0.01171875], [-3.671875, -2.116362641e-16, 0.953125], [-3.671875, -1.084202172e-16, 0.48828125], [-3.36328125, -1.084202172e-16, 0.48828125], [-3.032165527, -3.409951358e-16, 1.535705566], [-2.401855469, -5.339695699e-16, 2.404785156], [-1.533508301, -6.737638876e-16, 3.034362793], [-0.48828125, -7.467984564e-16, 3.36328125], [-0.48828125, -8.153200337e-16, 3.671875], [-0.953125, -8.153200337e-16, 3.671875], [0.01171875, -1.066854938e-15, 4.8046875], [0.9765625, -8.153200337e-16, 3.671875], [0.5078125, -8.153200337e-16, 3.671875], [0.5078125, -7.459310947e-16, 3.359375], [1.546691895, -6.715548256e-16, 3.024414062], [2.408691406, -5.31475905e-16, 2.393554688], [3.034118652, -3.390300193e-16, 1.526855469], [3.36328125, -1.075528555e-16, 0.484375], [3.671875, -1.075528555e-16, 0.484375], [3.671875, -2.107689023e-16, 0.94921875], [4.8046875, 2.602085214e-18, -0.01171875]],d=1) 
	crv2 = cmds.circle(n="Move_shape", nr=(0, 1, 0), r=3)

	mergeTheseCurves(crv1, crv2)


def Pin_shape():

	crv =cmds.curve(n="Pin_shape", p=[[0, 1.552153134, 0], [0.1758525114, 1.575924979, 7.809420284e-17], [0.3397910862, 1.643830744, 1.50897555e-16], [0.480946564, 1.751367866, 2.135831796e-16], [0.5884836849, 1.892523343, 2.613392547e-16], [0.6563894515, 2.056461918, 2.914954729e-16], [0.6801612958, 2.23231443, 3.020522924e-16], [0.6563894515, 2.40816694, 2.914954729e-16], [0.5884836849, 2.572105046, 2.613392547e-16], [0.480946564, 2.713260993, 2.135831796e-16], [0.3397910862, 2.820797644, 1.50897555e-16], [0.1758525114, 2.888704352, 7.809420284e-17], [0, 2.912470075, 0], [-0.1758525114, 2.888704352, -7.809420284e-17], [-0.3397910862, 2.820797644, -1.50897555e-16], [-0.480946564, 2.713260993, -2.135831796e-16], [-0.5884836849, 2.572105046, -2.613392547e-16], [-0.6563894515, 2.40816694, -2.914954729e-16], [-0.6801612958, 2.23231443, -3.020522924e-16], [-0.6563894515, 2.056461918, -2.914954729e-16], [-0.5884836849, 1.892523343, -2.613392547e-16], [-0.480946564, 1.751367866, -2.135831796e-16], [-0.3397910862, 1.643830744, -1.50897555e-16], [-0.1758525114, 1.575924979, -7.809420284e-17], [0, 1.552153134, 0], [0, 0.01455445921, 0], [0, 1.552153134, 0]],d=1) 






#-------------CURVES------------------CURVES---------------CURVES-------------CRUVES--------------CURVES------------CURVES

	

def fitCamera(*args):


	cam = "cameraForShapes1"

	cmds.viewFit( cam,  f=0.75)
	cmds.setAttr(cam + '.overrideEnabled', 1)
	cmds.setAttr (cam + '.overrideDisplayType', 2)
	cmds.select(clear=True)





def processCurve(*args):

	listScrollFieldQuery = cmds.textScrollList(listScroll, query=True, si=True)#get user input`

	for t in listScrollFieldQuery:

		crvShape = (t + "_shape")

		crvTmpShape = (t + "_shape_temp_curves_camera")

		if cmds.objExists(crvShape):

			cmds.select(crvShape, add=True)

			bbox = cmds.xform(crvShape, q=1, os=1, bb=1) 

			del bbox[0]
			del bbox[0]
			del bbox[0]

			import operator

			myNumber = 0

			closestValue = min(bbox, key=lambda x:abs(x-myNumber))#Function that gets the closest value to 0 in array

			closestIndex = bbox.index(closestValue)

			if cmds.objExists('helpingJoint'):

				cmds.delete('helpingJoint')

			cmds.joint(n="helpingJoint", rad=5)

			if closestIndex == 1:

				cmds.setAttr("helpingJoint.rx", -90 )

			elif closestIndex == 0:

				cmds.setAttr("helpingJoint.ry", -90 )

			sel("cameraForShapes1")

			selAdd("helpingJoint")

			cmds.MatchRotation()

			cmds.delete('helpingJoint')

			distance = 80000

			sel(crvShape)

			cmds.setAttr(crvShape + '.translateY', distance)

			
			cmds.setAttr(crvShape + '.overrideEnabled', 1)
			
			cmds.setAttr (crvShape + ".overrideColor", 14)

			lockEverything(crvShape)
			

			fitCamera()

			lockEverything("cameraForShapes1")

			#cmds.select(crvShape, r=True)

			if cmds.objExists(crvShape):

				global tmpCrvs

				tmpCrvs = cmds.rename(crvShape, crvShape + tempString)

				


def drawTheCurves():

	listScrollFieldQuery = cmds.textScrollList(listScroll, query=True, si=True)#get user input`

	for t in listScrollFieldQuery:

		crvFunc = (t + "_shape()")

		eval(crvFunc)

		cmds.select(clear=True)





#User actions--------------------------------------------------------------------------

# def changeEditor(*args):

# 	print "it changed"


def changeImage(*args):


	delIfExists("Circle_shape_temp_curve")

	#cmds.SelectTool()

	UnlockEverything('cameraForShapes1')

	delIfExists(tmpCrvs)

	drawTheCurves()

	processCurve()

	# test = cmds.window( q=True, fw=True )

	# print test

	#cmds.doHideInOutliner(tmpCrvs)

	#cmds.setAttr(tmpCrvs + ".doHideInOutliner", 1)

	#cmds.select(tmpCrvs)

	#cmds.nodeOutliner(remove=tmpCrvs)


def scollListFunction(*args):

	drawTheCurves()

	#cmds.select(tmpCrvs)

grey = [0.227, 0.227, 0.227]

blueGreen = [0.071, 1, 0.776]



red = [1, 0.224, 0.224]

redPale = [1, 0.399, 0.321]

orange = [1, 0.479, 0.173]

yellow = [1, 1, 0.390]

green = [0.527, 1, 0.276]

cyan = [0.321, 1, 0.869]

blue = [0.256, 0.628, 1]

pink = [1, 0.442, 0.706]

purple = [0.466, 0.200, 0.892]




##									 --
##									----							##
##								—————————————						##
##								  -WINDOW-				     		##
##								—————————————						##
##									-----							##
##									  --

window = "Rigging_ToolKit"

if cmds.window(window, exists=True):
    cmds.deleteUI(window)

cmds.window(window, title=window, s=True, w=285)

tabWindow = cmds.tabLayout(w=285, h=450)

def separator():
	cmds.separator(style="in", w=275, h=10)

def space():
	cmds.text(l="", h=4)

def close():
	cmds.setParent('..')

def rowOf1():
	cmds.rowLayout(nc=1)

def rowOf2():
	cmds.rowLayout(nc=2)

def rowOf3():
	cmds.rowLayout(nc=3)

def rowOf4():
	cmds.rowLayout(nc=4)

def rowOf5():
	cmds.rowLayout(nc=5)

def rowOf10():
	cmds.rowLayout(nc=10)








# --------------------------------------------------------------------------------
#                                         Tab 1                                    
#---------------------------------------------------------------------------------

tab1 = cmds.columnLayout()

separator()#------------------------------------------------------------------------------------

cmds.text(l="NURBS TEXT CREATOR", h=15, w=275, bgc=grey)

space()

rowOf2()

nurbsTextField = cmds.textField(ec=setNurbsTxt, w=248)

#cmds.button(c=setNurbsTxt,l="GO", font="boldLabelFont", w=24, h=20, bgc=blueGreen)

cmds.iconTextButton( c=setNurbsTxt, style='iconOnly', image1='arrowRight.png',w=24, h=20, bgc=blueGreen)

close()#closeRowof2

fonts = cmds.fontDialog(FontList=True)

fontOptionMenu = cmds.optionMenu(w=275) 

for i in fonts:    
	fontList = cmds.menuItem(label=i)

separator()#------------------------------------------------------------------------------------

cmds.text(l="NURBS SHAPES", h=15, w=275, bgc=grey)

space()

rowOf2()

cmds.formLayout(w=136)

cmds.paneLayout(h=100, w=135)

editor = cmds.modelEditor( grid=False)

close()#close paneLayout

close()#close formLayout1

cmds.formLayout(w=275)

listScroll = cmds.textScrollList(
	numberOfRows=8,
	fn="plainLabelFont",
	allowMultiSelection=False, 
	h=105, w= 136, 
	dcc=scollListFunction, 
	sc=changeImage,
	sii=1,
	append=[
	'Circle',
	'Square', 
	'Cube', 
	'Arrow', 
	'Orient', 
	'Cone', 
	'Foot', 
	'Hand',
	'HalfSphere', 
	'Sphere', 
	'Move', 
	'Pin'
	])


close()#close formLayout2


delIfExists('cameraForShapes*')


cameraShapes = cmds.camera(position=[0, 80000, 0],rotation=[0, 0, 0], n="cameraForShapes") 

cmds.modelEditor(editor, edit=True, camera=cameraShapes[0])





close()#closeRowof2



rowOf2()

cmds.button(c=ctrl_Joy, l="Joystick", w=137.5, h=20)
cmds.button(c=ctrl_Slide,l="Slider", w=137.5, h=20)




close()#closerowOf2


rowOf4()

cmds.text(l="Min ")

minCtrlValue = cmds.intField(en=False,minValue=-100, maxValue=0, h=20, value=0, width=44)

sliderCheckBox = cmds.checkBox( label=' Is Zero  |', value=True, w=70, ofc=changeMinValue, onc=changeMinValue)

maxCtrlValue = cmds.intSliderGrp(label="Max", field=True,cw3=[25,40,60], min=1, max=100, h=20, value=1, cc=changeMinValue)

close()#closerowOf4

separator()#------------------------------------------------------------------------------------

cmds.text(l="COLOR PICKER", h=15, w=275, bgc=grey)

space()

rowOf10()


buttons= [
colorBtt(doRed,red),
colorBtt(doRedPale,redPale),
colorBtt(doOrange, orange),
colorBtt(doYellow, yellow),
colorBtt(doGreen, green),
colorBtt(doCyan, cyan),
colorBtt(doBlue, blue),
colorBtt(doPink, pink),
colorBtt(doPurple, purple)

]

close()#closeRowOf10



close()#close tab1

# --------------------------------------------------------------------------------
#                                         Tab 2                                    
#---------------------------------------------------------------------------------

tab2 = cmds.columnLayout()




close()

# --------------------------------------------------------------------------------
#                                         Tab 3                                    
#---------------------------------------------------------------------------------


tab3 = cmds.columnLayout()



close()


cmds.tabLayout(tabWindow, edit=True, tabLabel=( (tab1,"Tools"),(tab2,"Joints"),(tab3,"Face") ) )


cmds.showWindow(window)



#Show default circle part2

sel("Circle_shape_temp_curve")

cmds.viewFit( "cameraForShapes1",  f=0.75)

cmds.select(clear=True)

lockEverything("cameraForShapes1")
