camp_list = ["tent", "sleeping bag", "food", "water", "cooker"]
camp_site = ["Postern Hill", 404, 27.7, True]
#camp_list.extend(["toilet paper, " + "bidet"])
camp_list.insert(0, "bidet")
camp_list.insert(-1, "toilet paper")
print(camp_list.pop(1))
camp_list.pop(2)
print(camp_list) 