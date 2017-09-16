largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if (num == "done") : break
    if (len(num) < 1) : break
        
    try:
        n = int(num)
    except:
        print 'Invalid input'
        continue
    
    if largest is None:
    	largest = n
    if smallest is None:
    	smallest = n    
    
    if(n < smallest):
    	smallest = n 
    if (n > largest):
        largest = n
    

print ("Maximum is", largest)
print ("Minimum is", smallest)
