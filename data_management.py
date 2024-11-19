import sys

#Comment to show Assignment 5
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = int(sys.argv[5])
    numbers = [a, b, c, d, e]

    
    if any(num < 0 for num in numbers):
        print( "<h2>There's some negative number.</h2>")
        
    avg = sum(numbers) / len(numbers)
    if avg > 50:
        print("<h2>Average is greater than 50.</h2>")
    else:
        print("<h2>Average is not greater than 50.</h2>")  
       
    positive_count = sum(1 for num in numbers if num > 0)
    if positive_count & 1:
        print("<h2>The count of positive numbers is odd.</h2>")
    else:
        print("<h2>The count of positive numbers is even.</h2>")

    greater_than_10 = [num for num in numbers if num > 10]
    sorted_greater_than_10 = sorted(greater_than_10)
    
    print("<h2>Original List:</h2>", numbers)
    print("<h2>List of Values > 10:</h2>", greater_than_10)
    print("<h2>Sorted List of Values > 10:</h2>", sorted_greater_than_10)

except (ValueError, IndexError):
    print("<h2>Invalid numeric arguments for a, b, c, d and e. Please, provide integer numbers</h2>")