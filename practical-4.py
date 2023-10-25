"""
Program to implement Insertion and Shell sort 

Name :- Avishkar Haridas zende
Roll no. :- 73

"""
#Function for Insertion sort

def insertion_sort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while ((j >= 0) and (key < arr[j])):
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=key
	print("\n Sorted List of students by using Insertion sort")
	print(arr,end=" , ")
		

#Function for Shell sort

def Shell_sort(arr,n):
	interval=n//2
	while (interval>0):
		for i in range (interval,n):
			temp=arr[i]
			j=i
			while ((j>=interval) and (arr[j-interval]>temp)):
				arr[j]=arr[j-interval]
				j=j-interval
			arr[j]=temp
		interval=interval//2
	print("\n Sorted List of students by using Shell sort")
	print(arr,end=" , ")


n=int(input("Enter how many students Percentage you want to store:"))
array=[]
print("Enter marks for",n,"students (Press ENTER after every students marks): ")

for i in range (n):
	p=int(input("Percentage of students: "))
	array.append(p)
print("The Percentage of",n,"students are : ")	
print(array)
	
flag=1
while (flag==1):
        print("\n************MENU************\n")
        print("1. Insertion Sort of the marks")
        print("2. Shell Sort of the marks")
        print("3. Exit")
        ch=int(input("\nEnter your choice (from 1 to 3) : "))
   
        if ch==1:
        	insertion_sort(array)
        elif ch==2:
        	Shell_sort(array,n)	
        elif ch==3:
        	flag=0
        	print("Thanks for using this program!")
        else :
        	print("!!Wrong Choice!! ")
        	a=input("\n\nDo you want to continue (yes/no) :")
        	if a=="yes":
                	flag=1
        	else:
                	flag=0
                	print("Thanks for using this program!")

"""
OUTPUT :-

Enter how many students Percentage you want to store:4
Enter marks for 4 students (Press ENTER after every students marks): 
Percentage of students: 77
Percentage of students: 82
Percentage of students: 94
Percentage of students: 79
The Percentage of 4 students are : 
[77, 82, 94, 79]

************MENU************

1. Insertion Sort of the marks
2. Shell Sort of the marks
3. Exit

Enter your choice (from 1 to 3) : 1

 Sorted List of students by using Insertion sort
[77, 79, 82, 94] , 
************MENU************

1. Insertion Sort of the marks
2. Shell Sort of the marks
3. Exit

Enter your choice (from 1 to 3) : 2

 Sorted List of students by using Shell sort
[77, 79, 82, 94] , 
************MENU************

1. Insertion Sort of the marks
2. Shell Sort of the marks
3. Exit

Enter your choice (from 1 to 3) : 3
Thanks for using this program!
""" 
