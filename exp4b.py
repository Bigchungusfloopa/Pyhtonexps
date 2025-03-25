student_records = {}


student_records["Alice"] = {
    "grade": "A",
    "attendance": 95,
    "subjects": set(["Math", "Science"])
}

student_records["Bob"] = {
    "grade": "B",
    "attendance": 88,
    "subjects": set(["English", "History"])
}


student_records["Alice"]["attendance"] = 97
student_records["Alice"]["subjects"].update(["History"])


print(f"Name: Alice, Grade: {student_records['Alice']['grade']}, Attendance: "
      f"{student_records['Alice']['attendance']}%, Subjects: {', '.join(student_records['Alice']['subjects'])}")

print(f"Name: Bob, Grade: {student_records['Bob']['grade']}, Attendance: "
      f"{student_records['Bob']['attendance']}%, Subjects: {', '.join(student_records['Bob']['subjects'])}")
