from data.student import Student
from model.student_reg_form_page import StudentRegFormPage

student = Student('John', 'Dou', 'JohnDou@test.com', 'Male', '1234567890',
                  '13', 'April', '1985',
                  'Maths', 'Sport', 'guru.png', 'Some Street, some house',
                  'Uttar Pradesh', 'Lucknow')


def test_student_reg_form():
    registration_page = StudentRegFormPage()

    registration_page.open()
    registration_page.fill_up_the_registration_form(student)
    registration_page.check_data_in_form_registration(student)

    registration_page.close_table()
