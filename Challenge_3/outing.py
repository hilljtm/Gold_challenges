class Outing :

    def __init__(self, event_type, event_date, people_attend, cost_per_person):
        self.event_type = event_type
        self.event_date = event_date
        self.people_attend = people_attend
        self.cost_per_person = cost_per_person
        self.total_cost = people_attend * cost_per_person

    def __repr__(self):
        return f'(Event type{self.event_type}, {self.event_date}, People:{self.people_attend}'
