import outing_repo

def Prompt():

    print("""
Komodo Outing Manager:
1. Display outings
2. Create outing
3. Get cost
4. Exit
    """)

while True:
    Prompt()
    choice = input(" > ")
    
    if choice == "1":
        tmp_list = outing_repo.get_outings()
        for event in tmp_list:
            print(event)   

    if choice == "2":
        e_type = input("What is the event type(golf, bowling, concert, amusement park): ")
        e_date = input("what is the event_date: ")
        e_people = int(input("How many people attended: "))
        e_cost_per = int(input("What is the cost per person: "))
        outing_repo.create_outing(e_type, e_date, e_people, e_cost_per)
        

    if choice == "3":
        print("1 = Total cost, 2 = cost by event")
        cost_choice = input("What do you want? ")
        if cost_choice == "1":
            tmp_list = outing_repo.get_outings()
            tmp_total = outing_repo.get_cost(tmp_list)
            print(f"The total for all outings is {tmp_total}")
            continue
        elif cost_choice == "2":
            tmp_type = input("What is the event type(golf, bowling, concert, amusement park)")
            tmp_list = outing_repo.get_outings()
            tmp_filtered_lists = outing_repo.filtered_lists(tmp_list, tmp_type)
            tmp_total = outing_repo.get_cost(tmp_filtered_lists)
            print(f"The total for {tmp_type} outings is {tmp_total}")
            continue

    if choice == "4": 
        exit()
    else: 
        print("Invalid input")