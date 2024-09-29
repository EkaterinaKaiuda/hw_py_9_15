import os
from selene import browser, be, have, command
import tests


class StudentRegFormPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, gender_type):
        browser.element(f'[name=gender][value={gender_type}]+label').click()

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def scroll_page_to_the_end(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(f'{value}').press_enter()

    def select_hobby(self):
        browser.all('#hobbiesWrapper .custom-control-label').element_by(
            have.attribute('for', 'hobbies-checkbox-1')).click()

    def upload_photo(self):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), 'resources/guru.png')
            )
        )

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(f'{value}')).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(f'{value}')).click()

    def click_submit_button(self):
        browser.element('#submit').click()

    def fill_up_the_registration_form(self, student):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.select_gender(student.gender)
        self.fill_number(student.mobile)
        self.fill_date_of_birth(student.day, student.month, student.year)
        self.scroll_page_to_the_end()
        self.fill_subject(student.subjects)
        self.select_hobby()
        self.upload_photo()
        self.fill_current_address(student.address)
        self.fill_state(student.state)
        self.fill_city(student.city)
        self.click_submit_button()

    def check_data_in_form_registration(self, student):
        browser.element('.table').all('td').should(have.texts(
            'Student Name', student.first_name + ' ' + student.last_name,
            'Student Email', student.email,
            'Gender', student.gender,
            'Mobile', student.mobile,
            'Date of Birth', student.day + ' ' + student.month + ',' + student.year,
            'Subjects', student.subjects,
            'Hobbies', student.hobbies,
            'Picture', student.picture,
            'Address', student.address,
            'State and City', student.state + ' ' + student.city
            )
        )

    def close_table(self):
        browser.element('#closeLargeModal').click()
        browser.element('#example-modal-sizes-title-lg').should(be.not_.visible)