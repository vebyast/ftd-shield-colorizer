#!/usr/bin/python3

import json
import argparse


shieldcolorizerblockuuid = "7d005e15-c63a-44f0-b12e-b8599a9f0424"

parser = argparse.ArgumentParser(description='Colorize shields on an FTD blueprint')
parser.add_argument('blueprint',
                    help='''The blueprint file to colorize''',
                    type=str)
parser.add_argument('--rgba',
                    help='''New color to set, as a string formatted like 'r,g,b,a'. All four are floats with two digits after the decimal. The three colors are between 0.00 and 1.00 inclusive, and alpha is between 0.10 and 10.00 inclusive. A valid example: "0.62,0.5,0.34,3.34".''',
                    type=str)
parser.add_argument('--clear',
                    help='''Set all shield alphas to zero''',
                    action='store_true')
parser = parser.parse_args()


def newcolor(colstr):
    if parser.rgba:
        return parser.rgba
    if parser.clear:
        (r, g, b, _) = colstr.split(',')
        return "{},{},{},0.10".format(r, g, b)
    return colstr


bpjson = None
with open(parser.blueprint, 'r') as bpfile:
    bpjson = json.load(bpfile)

shieldblockid = None
for blockid, blockuuid in bpjson["ItemDictionary"].items():
    if blockuuid == shieldcolorizerblockuuid:
        shieldblockid = int(blockid)

shieldblockidxs = [idx for idx, blockid in enumerate(bpjson['Blueprint']['BlockIds']) if blockid == shieldblockid]
for idx in shieldblockidxs:
    bpjson['Blueprint']['BP1'][idx] = newcolor(bpjson['Blueprint']['BP1'][idx])

print(json.dumps(bpjson))
