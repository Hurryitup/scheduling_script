import pandas
import numpy


old_entries_location = r'/Users/adityahurry/Documents/compSci/scheduling_script/old_entries.csv'
new_entries_location = r'/Users/adityahurry/Documents/compSci/scheduling_script/new_entries.csv'

old_entries = pandas.read_csv(old_entries_location)
old_entries = old_entries[old_entries["Name"].notnull()]
old_entries = old_entries[old_entries["Scheduling Preferences"] != "NA"]

new_entries = pandas.read_csv(new_entries_location)
new_entries = new_entries[new_entries["Name"].notnull()]
new_entries = new_entries[new_entries["Scheduling Preferences"] != "NA"]

for index, old_person in old_entries.iterrows():
        found_person = False
        for index, new_person in new_entries.iterrows():
                if new_person["Name"] == old_person["Name"]:
                        found_person = True
        if not found_person:
                print old_person["Name"]
