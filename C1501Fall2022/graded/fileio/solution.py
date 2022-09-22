# Q1
SPEED_LIMIT = 80
f_obj = open("speeds.txt", "r")
num_speeders = 0

for line in f_obj:
    speed = int(line)
    if speed > SPEED_LIMIT:
        num_speeders += 1
    
f_obj.close()
print(f"There are {num_speeders} speeders.")

# Q2
f_obj = open("hikes.txt", "r")
dist_sum = 0
n_hikes = 0

for line in f_obj:
    dist = float(line)
    dist_sum += dist
    n_hikes += 1
    
f_obj.close()
print(f"The average distance is {dist_sum / n_hikes}.")

# Q3
f_obj = open("hikes.txt", "r")
max_hike = 0

for line in f_obj:
    dist = float(line)
    if dist > max_hike:
        max_hike = dist
    
f_obj.close()
print(f"The maximum distance is {max_hike}.")

# Q4
f_obj = open("student-sections.txt", "r")
n_section_5 = 0

for line in f_obj:
    section = int(line)
    if section == 5:
        n_section_5 += 1
    
f_obj.close()
print(f"There are {n_section_5} students in section 5.")

# Q5
PASS_THRESHOLD = 50
f_obj = open("grades.txt", "r")
n_passing = 0

for line in f_obj:
    grade = float(line)
    if grade >= PASS_THRESHOLD:
        n_passing += 1
    
f_obj.close()
print(f"There are {n_passing} passing students.")

# Q6
f_obj = open("grades.txt", "r")
max_grade = 0

for line in f_obj:
    grade = float(line)
    if grade > max_grade:
        max_grade = grade
    
f_obj.close()
print(f"The highest grade is {max_grade}.")
