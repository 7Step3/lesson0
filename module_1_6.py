my_dict = {"Stepan": 1996, "Varvara": 2003, "Egor": 1997}
print(my_dict)
print(my_dict["Varvara"])
print(my_dict.get("Mark"))
my_dict.update({"Max": 1990, "Oleg": 1998})
Egor = my_dict.pop("Egor")
print(Egor)
print(my_dict)

my_set = {"red", "blue", "green", 1, 4, "yellow", 4, "red", 2, "green"}
print(my_set)
my_set.add("black")
my_set.add(13.13)
my_set.discard("red")
print(my_set)
