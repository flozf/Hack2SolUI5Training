import json
from pprint import pprint

x = json.loads( '{ "hallo": [ 1, 2, 3, 4 ] }' )

pprint( x )