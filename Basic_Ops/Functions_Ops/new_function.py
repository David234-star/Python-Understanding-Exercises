def display_student(name, age):
    print(name, age)


display_student("Rana", 23)  # calling with original name
show_student = display_student  # assigning to the new name
show_student("Rana", 23)  # calling with new name
