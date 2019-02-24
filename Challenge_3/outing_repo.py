
from outing import Outing
outings = []


def create_outing(event_type, event_date, people_attend, cost_per_person):
    new_outing = Outing(event_type, event_date, people_attend, cost_per_person)
    outings.append(new_outing)

def get_outings():
    return outings

def get_cost(outing_list):
    total = 0
    for event in outing_list:
        total += event.total_cost

    return total

def filtered_lists(event_list, event_type):
    filtered_list = []
    for event in event_list:
        if event_type == event.event_type:
            filtered_list.append(event)

    return filtered_list

