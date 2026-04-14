class School:
    def __init__(self):
        self.teachers = []
        self.no_of_teachers = 0

    def add_teacher(self, teacher_name):
        self.teachers.append(teacher_name)
        self.no_of_teachers += 1
        print(f'Teacher "{teacher_name}" added.')

    def show_teachers(self):
        if self.teachers:
            print("Teachers in the school:")
            for index, teacher in enumerate(self.teachers, start=1):
                print(f"{index}. {teacher}")
        else:
            print("No teachers in the school.")

    def get_no_of_teachers(self):
        return self.no_of_teachers


if __name__ == "__main__":
    school = School()
    school.add_teacher("mr. Nareshchandr ji")
    school.add_teacher("mr. home singh ji")
    school.add_teacher("mr. predeep ji")
    school.add_teacher("mr. pankaj ji")
    school.add_teacher("mr. shubham ji")
    school.add_teacher("mr. monika ji")
    school.add_teacher("mr. shivom ji")
    school.add_teacher("mr. khushal negi ji")

    school.show_teachers()
    print(f"Total number of teachers: {school.get_no_of_teachers()}")
