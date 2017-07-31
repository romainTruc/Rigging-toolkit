maya.cmds à l'importation comme cmds

# Faire une nouvelle fenêtre
#
window = cmds.window (title = "Nom long", iconName = 'Nom court', Widthheight = (200, 55))
cmds.columnLayout (adjustableColumn = True)
cmds.button (label = 'Ne rien faire)
cmds.button (label = 'Fermer', commande = ( 'cmds.deleteUI (\ "' + fenêtre + '\", fenêtre = true)))
cmds.setParent ( '..')
cmds.showWindow (fenêtre)

# Redimensionner la fenêtre principale
#

# Ceci est une solution de contournement pour obtenir MEL valeur variable globale en Python
gMainWindow = maya.mel.eval ( '$ tmpVar = $ gMainWindow')
cmds.window (gMainWindow, modifier = True, Widthheight = (900, 777))
