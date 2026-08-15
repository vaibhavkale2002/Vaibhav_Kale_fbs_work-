# # 2 Enter number of students from user. For those many students accept marks of 5
# # subje# ct marks from user and calculate percentage. Display all percentage and
# # average percentage of students.




s=int(input("Enter number of students:"))
per_total=0
for j in range(1,s+1):
    print(f"Marks of student {j}")
    total=0
    for i in range(1,6):
        mark=int(input(f"Enter the mark of sub {i}:"))
        total+=mark

    per=(total/500)*100 
    print()
    print(f"Percentage:{per}")
    per_total+=per
    print()
print(f"Total per:{per_total}")
ave_per=per_total/s
print(f"Average percentage:{ave_per}")
  

