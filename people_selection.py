import pandas
import numpy

location = r'/Users/adityahurry/Documents/compSci/scheduling_script/scheduling-responses-spring-schedule-b.csv'
shortLocation = 'scheduling-responses.csv'
one_upto3Specials = "1(2-3)"
one_5specials = "1(5)"
zero_5specials = "5SP"
two_noSpecials = "2"
SLOT_NAMES = ['Monday Morning', 'Monday Afternoon', 'Monday Evening', 'Tuesday Morning', 'Tuesday Afternoon', 'Tuesday Evening', 'Wednesday Morning',
             'Wednesday Afternoon', 'Wednesday Evening', 'Thursday Morning', 'Thursday Afternoon', 'Thursday Evening', 'Friday Morning', 'Friday Afternoon',
             'Friday Evening', 'Saturday Morning', 'Saturday Afternoon']
inorder_slotnames = ['Monday Morning', 'Monday Afternoon', 'Monday Evening', 'Tuesday Morning', 'Tuesday Afternoon', 'Tuesday Evening', 'Wednesday Morning',
             'Wednesday Afternoon', 'Wednesday Evening', 'Thursday Morning', 'Thursday Afternoon', 'Thursday Evening', 'Friday Morning', 'Friday Afternoon',
             'Friday Evening', 'Saturday Morning', 'Saturday Afternoon']
numpy.random.shuffle(SLOT_NAMES)
tours_per_week = "tours_per_week"


def normalize_preferences(x):
    if x == one_upto3Specials:
        return 1
    elif x == zero_5specials:
        return 0
    elif x == one_5specials:
        return 1
    elif x == two_noSpecials:
        return 2
    else:
        return numpy.nan


data = pandas.read_csv(location)
data = data[data["Name"].notnull()]
data = data[data["Scheduling Preferences"] != "NA"]
data[tours_per_week] = data['Scheduling Preferences'].map(normalize_preferences)
data = data[data[tours_per_week] > 0]
# for slot in inorder_slotnames:
#     slot_people = data[data[slot] == "yes"]
#     slot_engineers = slot_people[slot_people["Engineer"] == "Yes"]
#     print slot
#     print slot_engineers["Name"]
#     print "---------------------"

# print "> 1 tours_per_week"
# print (data[data[tours_per_week] > 1])["Name"]
# print "---------------------"

cur_slot = "Tuesday Afternoon"
print cur_slot
print (data[data[cur_slot] == "yes"])["Name"]
print "---------------------"