import json
import code
from typing import List

global_i = 0 # ensures no enumerated dictionary keys are the same. there is no doubt a better way to do this

def dictionarize(item): # this recursively turns a json into a tree of dictionaries

    # TODO: docstrings maybe???

    if type(item) == type(""):
        try:
            json.loads(item) 
            # don't run the recursive call inside here, or else any Real errors won't show up.
            # thats not the best way to do it, but wtv, it works
            # TODO: more specific error handling
        except: 
            return item # BASE CASE - a string that cannot be jsonified
        return dictionarize(json.loads(item)) 

    elif type(item) == type([]):
        global global_i
        subdictionary = {}
        for subitem in item:
            subdictionary[f"{global_i}"] = dictionarize(subitem)
            global_i = global_i + 1
        return subdictionary
    
    elif type(item) == type({}): 
        for subkey in item:
            item[subkey] = dictionarize(item[subkey]) 
        return item







def write_data(input_jsons: List[str], output_json: str) -> None:
    # have a main counter for the keys
    # for each json file:
    #   dictionarize,
    #   for each item in data:
    #       put each relevent attribute in a big dictionary[str(i)][attribute]      # this may have to rely on some hardcoding, but that's okay <3
    # write data to output_json
    for input_file in input_jsons:
        f = open(input_file, "rt")
        data = f.read()
        f.close()
        tree = dictionarize(data)
        print(type(tree))
        # for item in 

        code.interact(local = locals())

write_data(["./classes.json"], "meow.json")





# - the go is:
#   - we yoink the data into a dictionary -> json
#   - make the main thing appending to the file

# - id?:
# - termDesc
# - subjectCourse
# - sequenceNumber (i assume this is section)
# - scheduleTypeDescription
# - calc daysUsed (dictionary or hashmap)
# - startTime
# - endTime


# for each in class_list:
# well, hold on,
#   just copy all the entries we care about to dictionary, then append self to new_list
#   SEPERATE room_prefix and room_number
#   also note first number (floor)


#   json it
#   take important attributes, make key/value pairs in subdictionary
#   append k/v of id/subdictionary to class_dictionary

# that ^ gives a dictionary of dictionaries. 
# - for the subdict, thats good, but list might be best for outter pair????


# how should i save this data? when do i do that?
# save to dictionary, then to json

# json data:
# - key:id
# - room number
# - day of the week (later 
# - start time
# - end time


# class Sections:
#     def __init__(self, ):
#         # TODO
#     def is_sheduled_today(day: str) -> bool:
#         # TODO
#     def minutes_free() -> int: # probably not a float?
#         # TODO

# code.interact(local = locals())
