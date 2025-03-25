cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Eve", "Bob", "Grace", "Charlie"}
neet_students = {"Alice", "Frank", "Grace", "David"}

all_students = cet_students | jee_students | neet_students
print("Students appearing in any exams:", all_students)

cet_jee_common = cet_students & jee_students
print("Students appearing in both CET and JEE:", cet_jee_common)

cet_neet_difference = cet_students - neet_students
print("Students appearing in CET but not in NEET:", cet_neet_difference)

cet_jee_exclusive = cet_students ^ jee_students
print("Students in either CET or JEE but not both:", cet_jee_exclusive)