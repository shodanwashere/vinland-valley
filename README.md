![[vinland-valley-logo.png]]
---
From one warrior to another.
This is a script made to transfer hosts in Stardew Valley multiplayer save files. Currently it is **very experimental** and has serviceable results on version 1.6.14. Use at your own peril.
## Pre-requisites:
- python3
---
## Usage
You'll need the save file you want to migrate and send to your friend. It should be in one of three locations:
- Windows: `%appdata%\StardewValley\Saves`
- MacOS/Linux: `~/.config/StardewValley/Saves
Your save file should be in a directory with this naming format: `FarmName_RandomNumbers`
To use this script, get the script and run it this way:
```bash
$ ./vv.py /path/to/FarmName_RandomNumbers
```
Once the script finishes running, you'll find a modded version of the save file on `/path/to/FarmName_RandomNumbers_modded`.
Delete the old save file and remove the `_modded` suffix from the filename, then zip the entire save file directory and send it to your friend. They should dump the save folder in the save directory on their computer. All done :)
---
## Bugs?
If you found any bugs, please report them as an issue in this repository and I will get to fixing it as soon as possible :)
Please note also that I do these kinds of things on my free time and may not be as fast as you want me to be. If you think you know the solution to fix a specific issue, maybe make a pull request that i can examine. I welcome all the help i can get :)
