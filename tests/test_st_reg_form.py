from model.student_reg_form_page import StudentRegFormPage


def test_student_reg_form():
    registration_page = StudentRegFormPage()

    registration_page.open()

    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Dou')
    registration_page.fill_email('JohnDou@test.com')
    registration_page.select_gender('Male')
    registration_page.fill_number('1234567890')
    registration_page.fill_date_of_birth(13, 3, 1985)
    registration_page.scroll_page_to_the_end()
    registration_page.fill_subject('Maths')
    registration_page.select_hobby()
    registration_page.upload_photo()
    registration_page.fill_current_address('Some Street, some house')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Lucknow')
    registration_page.click_submit_button()

    registration_page.check_data_in_form_registration('John Dou', 'JohnDou@test.com', 'Male', '1234567890',
                                                    '13 April,1985',
                                                    'Maths', 'Sport', 'guru.png', 'Some Street, some house',
                                                    'Uttar Pradesh Lucknow')

    registration_page.close_table()