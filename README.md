# ftd-shield-colorizer
Python script to colorize shields. No warranty, no guarantees, nothing even vaguely resembling a promise.

Theoretically, this should analyze your save file to find shield colorizer blocks, then set their parameters to change their colors. Colorizes every shield colorizer on the entire ship to the same value.

Has two arguments: `--clear` keeps your shields' RGB values but sets the alpha value to the minimum allowable. `--rgba` takes as an argument a string and sets all the shields to the encoded color values. The format for this string is described in the `--help` text.

Takes the blueprint as a positional argument and prints the new blueprint to standard output.
