camp_list = ["tent", "sleeping bag", "food", "water", "cooker"]
camp_site = ["Postern Hill", 404, 27.7, True]
me = (camp_list)
you = (camp_list)
#camp_list.extend(["toilet paper, " + "bidet"])
camp_list.insert(0, "bidet")
camp_list.insert(-1, "toilet paper")
#print(me[4])
#print(you[-2])
print(camp_list)