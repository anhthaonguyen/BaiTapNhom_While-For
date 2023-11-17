def compute_gpa():
    grade_points = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
    total_points = 0.0
    count = 0

    while True:
        grade = input("Nhap diem chu(de trong de ket thuc): ")
        if grade == "":
            break
        total_points += grade_points.get(grade, 0.0)
        count += 1

    if count > 0:
        gpa = total_points / count
        print("Diem trung binh(GPA):", gpa)
    else:
        print("Khong co diem chu nao duoc nhap")

compute_gpa()