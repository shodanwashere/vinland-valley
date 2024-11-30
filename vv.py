#!/usr/bin/env python3
from lxml import etree
from copy import deepcopy
import os.path as Path
import sys

# check if arg was passed
argc = len(sys.argv)
if argc < 2:
  print("Error: not enough args")
  print("Usage: " + sys.argv[0] + " <FarmName_UniqueFarmID_filename>")
  sys.exit(0)

# arg was passed
# obtain filename and check if file exists
filename = sys.argv[1]
if not Path.isfile(filename):
  print("Error: file does not exist")
  print("Usage: " + sys.argv[0] + " <FarmName_UniqueFarmID_filename>")
  sys.exit(0)

# file exists
# read file contents
# verify if save contents are parseable xml
try:
  saveTree = etree.parse(filename)
  saveRoot = saveTree.getroot()
  # get player node
  player = saveRoot.find("player")
  # get farmhand node :: TODO -> specify farmhand name to switch with main player. if they dont exist, fail and exit
  farmhand = saveRoot.find("./farmhands/Farmer")

  playerHL = player.find("homeLocation")
  farmhandHL = farmhand.find("homeLocation")
  player.remove(playerHL) 
  farmhand.remove(farmhandHL)
  player.append(farmhandHL)
  farmhand.append(playerHL)

  playerUMid = player.find("UniqueMultiplayerID")
  farmhandUMid = farmhand.find("UniqueMultiplayerID")
  player.remove(playerUMid)
  farmhand.remove(farmhandUMid)
  player.append(farmhandUMid)
  farmhand.append(playerUMid)

  playerClone = deepcopy(player)
  farmhandClone = deepcopy(farmhand)
  saveRoot.find("player").clear()
  saveRoot.find("./farmhands/Farmer").clear()
  for c in farmhandClone:
    saveRoot.find("player").append(c)
  for c in playerClone:
    saveRoot.find("./farmhands/Farmer").append(c)

  saveTree.write(filename+"_modded", xml_declaration=True)
except ParseError as e:
  print("Error: malformed XML. Re-verify file contents.")
  print("Usage: " + sys.argv[0] + " <FarmName_UniqueFarmID_filename>")
  sys.exit(0)

print("Success! Modded save file can be found on "+filename+"_modded")
