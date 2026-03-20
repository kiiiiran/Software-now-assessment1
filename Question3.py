# Group Name: SYDN 15
# Group Members:
# Sandesh Kandel S400512
# Kiran Subedi - S400572
# Nabin Adhikari- S401346
# Rajib Sadaula - S399118


""" Question 3
Write a program that asks the user how many students are in the class (minimum 3,
maximum 10). For each student, input their name and score (0-100). Calculate and
display:
• Each student's grade (HD: 85-100, D: 75-84, C: 65-74, P: 50-64, F: 0-49).
• Class average
• Highest and lowest score and student name
• Lowest score and student name """



#This program takes number of students, their names and scores.
#Than it shows grade, average, highest and lowest score.

#Function to find grade
def get_grade(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"


# This will get the number of students
num = int(input("How many students? (3-10): "))

# Check valid range
while num < 3 or num > 10:
    print("Please enter between 3 and 10 students.")
    num = int(input("How many students? (3-10): "))

# Lists to store data
names = []
scores = []

# Input student details
for i in range(num):
    name = input(f"Student {i+1} name: ")
    score = int(input(f"{name}'s score: "))
    
    # Check valid score
    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = int(input(f"{name}'s score: "))
    
    names.append(name)
    scores.append(score)

# Calculate average
average = sum(scores) / num

# Find highest and lowest
max_score = max(scores)
min_score = min(scores)

max_index = scores.index(max_score)
min_index = scores.index(min_score)

# Display results
print("\nResults:")

for i in range(num):
    grade = get_grade(scores[i])
    print(f"{names[i]}: {scores[i]} ({grade})")

print(f"Average score: {average:.2f}")
print(f"Highest: {names[max_index]} ({max_score})")
print(f"Lowest: {names[min_index]} ({min_score})")