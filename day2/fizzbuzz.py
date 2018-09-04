def fizzbuzz(list1,list2):
    length = len(list1) + len(list2)

    if(length%3 == 0 and length%5 == 0):
        print("fizzbuzz")
    elif(length%3 == 0):
        print("fizz")
    elif(length%5 == 0):
        print("buzz")
    else:
        print(length) 

fizzbuzz([1,2,3], [])
fizzbuzz([1,2,3], [1,2])
fizzbuzz([1,2,3], [1])
    