







def sum():
    # We made a range called rang_0
    range_0 = 0
    # We're asking imput from the user
    picked_range = int(input("Pick a number to set your range: "))
    # This makes a ranged for loop outa the number that was picked
    for i in range(picked_range):
        # We created a varible that adds 
        x_sum = range_0 + i 
        print(i, " : ", range_0, " Sum: ", x_sum)
        range_0 = i
    print()
  


sum()





# def sum_of_range():
#     for i in range(0)
