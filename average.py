print("--Welcome to Average Calculator--")
print("[1] Start")
print("[2] Exit")

user_choice = int(input("Enter (1/2): "))
while user_choice == 1:
    try:
        subjects_list = []
        user_subjects = int(input(">> Enter, how many subjects you want: "))
        for subject in range(user_subjects):
            user_value = float(input(f">> {subject} Enter a Value: "))
            subjects_list.append(user_value)
        print(">> Your values is:", subjects_list, "now I'll calculate this list.")
        print(">> Results:", sum(subjects_list) / user_subjects)
        break
    except ValueError:
        print("Enter a valid value!")
