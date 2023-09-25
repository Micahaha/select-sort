def sort (data, first: int):
    """Sorts a list of integers from smallest to largest
    bypassing the elements to the left of first. 

    Args:
         data (int): list of integers 
        first (int): the list index at which the sort will begin 
    """    

    # Initialize loop counter variable named i 
    i = len(data) - first - 1

    # initalize loop counter variable named j to 0 
    j = 0

    # initialize variable named big that will be used
    # to store index of the biggest value
    big = 0

    # initalize variable named temp that will be used to swap list values
    temp = 0


    # loop through list as many times as specified by 
    # len(data) and first
    # this loop represents the blue arrow
    
    while (i  >= 0):
        # set big equal to first
        small = first
        # set j = first + 1
        j = first + 1

        # loop through list starting with element at
        # first + 1 and continue until reach first + i 
        # this loop represents the yellow arrow
        while (j <= first + i):
        
        # if value in data[big] is less than data[j]
        # set big equal to j
        # increment j by 1

            if (data[small] > data[j]):
                # set big = j
                small = j

            # increment j by 1
            j += 1

        # swap the data in first + 1 with the data in big
        # set temp to value in data[first + i] 
        temp = data[first + i]
            
        # set data[first + i] to value in data[big]
        data[first + i] = data[small]

        # set data[big] to value in temp
        data[small] = temp

        i-=1