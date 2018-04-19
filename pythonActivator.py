# listen to firebase and detect changes


import sys
# execute video gen script wth specific tag

import script_merge_connected

print (sys.argv[1])

script_merge_connected.createNewVideoSequence(sys.argv[1])
