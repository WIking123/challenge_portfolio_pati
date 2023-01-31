from pages.base_page import BasePage


class loginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sing in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sing in"
    title_of_box = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scovts panel'


    def type_in_emeil(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.login_field_xpath, password)
    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get_pege_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_tex(self.driver, self.title_of_box_xpath, self.header_of_box)