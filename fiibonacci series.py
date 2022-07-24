#fibonacci series
nterms = int(input("HOW MANY TERMS?"))
#first two terms 
n1,n2 = 0,1
count = 0
#check if number of terms is valid 
if nterms<0:
    print("PLEASE ENTER A POSITIVE INTEGER.")
#if there is only one term
elif nterms==1:
    print("The fibonacci series upto",nterms,":")
#generate fibonacci series 
else:
    print("fibonacci series")
    while count < nterms:
        print (n1)
        nth = n1+n2
        #update of values 
        n1=n2
        n2=nth
        count+=1
