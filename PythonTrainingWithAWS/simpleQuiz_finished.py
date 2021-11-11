#!/usr/bin/python3

s = '''Waltzing Matilda, waltzing Matilda,
You'll come a-waltzing Matilda, with me,
And he sang as he watched and waited till his billy boiled,
You'll come a-waltzing Matilda, with me.
'''
lines = s.split("\n")

results = {"1A":"failed", "1B":"failed",
           "1C":"failed", "1D":"failed"}

# --- COMPETENCY 1A ---------------------------------------------------
# Using the list "lines", print the second word of each line.
# The code is already written, you must supply the regular
# expression.

#my_regular_expression = r'TODO'
#my_regular_expression = r"^[\w']+\s([\w,]+)"
my_regular_expression = r"\S+\s([\w,]+).*"
import re
total_match_count = 0
for line in lines:
    match = re.search(my_regular_expression, line)
    if match:
        print(match.group(1))
        total_match_count += 1
if total_match_count == 4:
    results["1A"] = "maybe-passed"


# --- COMPETENCY 1B ---------------------------------------------------
# Print the first command line argument.  Assume this program is called
# (from the command-line) as such:
#
#     python3 2021-11-02-make-up.py jumbuck
#
# You should print "jumbuck" (taken from the command line)
#
import sys
results["1B"] = "maybe-passed"
try:
    #print(TODO) # <--- TODO
    print(sys.argv[1]) # <--- TODO
except:
    pass

# --- COMPETENCY 1C -----------------
# You have a list of dictionaries called LOD.  Convert it to a string
# in JSON format.
import json
results["1C"] = "passed"
LOD = [{"summer" : "hot", "winter" : "cold"},
       {"ball" : "round", "egg" : "ovoid"}]
#lod_json = None # <--- TODO
lod_json = json.dumps(LOD)
#print(type(lod_json))
#print(lod_json)


try:
    if json.loads(lod_json)[1]["egg"] == "ovoid":
        pass
except:
    results["1C"] = "failed"


# --- COMPETENCY 1D ---------------------------------------------------
# The user is asked for some input, but presses Ctrl-C.  Trap this
# error, and continue (silently) with the program.

# TODO
try:
    input("I dare you to press Ctrl-C!!!")
except KeyboardInterrupt:
    pass

results["1D"] = "maybe-passed"

print("-"*70)
print("YOUR RESULTS:")
print(results)
