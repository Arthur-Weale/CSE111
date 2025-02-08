
import csv


def main():
    students = r"C:/Users/Arthur/repos/CSE111/Week_5/students.csv"
    get_dict = read_dictionary(students, STUDENT_KEY_INDEX)
    return get_dict

STUDENT_KEY_INDEX = 0
STUDENT_NAME_INDEX = 1

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
        Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
        to use as the keys in the dictionary.
        Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    STUDENT_DICT = {}
    key_number = input("Enter I-Number: ")
    
    with open(filename, "rt") as students_file:
        students = csv.reader(students_file)
        next(students)
        
        for student in students:
            if len(student) != 0:
                key = student[key_column_index]
                STUDENT_DICT[key] = student
        #print(STUDENT_DICT[key])
        #print(STUDENT_DICT)
        if key_number in STUDENT_DICT:
            student_name = STUDENT_DICT[key_number]
            print(student_name)
        # for a_student_row in STUDENT_DICT:
        #     if key_number == a_student_row:
        #         print(STUDENT_DICT[a_student_row])


if __name__ == "__main__":
    main()