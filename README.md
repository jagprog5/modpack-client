# John's 1.12.2

[Structure Showcase](https://youtu.be/tyVnWifNTvY)🔗

This is a CurseForge profile for Minecraft 1.12.2.  
It contains [these mods](./modlist.md), with a focus on simplicity and exploration.

1. Download CurseForge [here](https://www.curseforge.com/download/app).
2. Download the profile [here](https://github.com/jagprog5/modpack-client/releases/latest/download/profile.zip).
3. Import the profile into CurseForge.

# Optional Java Settings

Cleanroom Relaunch is used by distant horizons. On first-time launch in the GUI
consider setting:

- under "Advanced Settings"
- in "Java Arguments" append "-XX:+UseShenandoahGC"

# Server

This modpack can be played on a server. The server code is [here](https://github.com/jagprog5/modpack-server). It's pretty stable.

### Updating

Do not update the mods, as this will lead to incompatible mod versions with the
server. This repo may be updated and if it is then the server mods will be kept in sync.

## Troubleshooting

If the game starts with a blank screen then delete `options.txt` and restart; this issues was seen on a MacBook.

# Development

For better diff viewing:

```bash
git config diff.nbt.textconv "python3 scripts/nbt_textconv.py"
git config diff.json.textconv "python3 -c 'import sys,json;json.dump(json.load(open(sys.argv[1])),sys.stdout,indent=2);print()'"
```