my_tuple = ("sasan", "reza", "neda", "omid", "reza", "ali", "Zahra", "mahan", "ashkan", "reza")

def remove(tup):
    new_tuple = ()
    for item in tup:
        if item != "reza":
            new_tuple += (item,)
    return new_tuple

print(remove(my_tuple))