highway_number = int(input())

''' Type your code here. '''
if highway_number >= 1 and highway_number <= 99:
    pri_int = "is primary, "

    print("I-{}".format(highway_number), pri_int , end="")

    if (highway_number%2) == 0:

        print("going east/west.")

    else:

        print("going north/south.")
        
elif (highway_number%100) == 0:

    print(highway_number , "is not a valid interstate highway number.")

elif highway_number >= 100 and highway_number <= 999:
    aux_int = "is auxiliary, "


    print("I-{}".format(highway_number), aux_int , end="")
    print("serving I-{}, ".format(highway_number%100), end="")


    if (highway_number%2) == 0:

        print("going east/west.")

    else:

        print("going north/south.")

else:

    print(highway_number , "is not a valid interstate highway number.")