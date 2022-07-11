







def sum():
    # We made a range called previous_number
    previous_number = 0
    # We're asking imput from the user
    picked_range = int(input("Pick a number to set your range: "))
    # This makes a ranged for loop outa the number that was picked
    for i in range(picked_range):
        # We created a varible that adds the previous_number
        # and picked_range 
        x_sum = previous_number + i 
        # This just prints everything togther 
        print(i, " : ", previous_number, " Sum: ", x_sum)
        # From my understanding, this skips an itration 
        previous_number = i
    print()
  


sum()





# def sum_of_range():
#     for i in range(0)
