print("---- Welcome to Average Calculator ----")
print("[1] Start")
print("[2] Exit")

user_choice = int(input("Enter your choice (1/2): "))
while user_choice == 1:
    try:
        subjects_list = []
        user_subjects = int(input("Enter the number of subjects: "))
            for subject in range(1, user_subjects+1):
            user_value = float(input(f"Enter value {subject}: "))
            subjects_list.append(user_value)
        print("Your values are:", subjects_list)
        print("Average of the values:", sum(subjects_list) / user_subjects)
        break
except ValueError:
print("Invalid input! Please enter a valid value.")
