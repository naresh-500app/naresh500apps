from cgitb import text
from distutils import text_file
from behave import *
from urllib.parse import urljoin
from selenium.webdriver.common.action_chains import ActionChains
from behave_webdriver.steps import *
from apps.lib.automation_base import Base
from apps.finder.features.steps.locators import Locators
from apps.lib.core_steps import *


elements = Locators()

base_methods = Base()


@then('I verified the count of the emails "{count}" using the element "{element}"')
def domain_validations(context, count, element):
    emails = context.behave_driver.find_elements_by_xpath(element)
    assert len(emails) == int(count)


@when('I scroll the form using infinity scroll')
def scroll_in_the_form(context):
    base_methods.move_to_element(context, elements.move_to_25th_row)


@when('I click on create list "{text}" button')
def click_create_list_button(context, text):
    base_methods.click_element(
        context, f"//div[@id='createListForm']//fieldset[@id='listname']//div//button[@type='submit'][normalize-space()='{text}']")


@then('I expect error message as "{text}"')
def verify_error_messages(context, text):
    base_methods.element_visible(
        context, f"//small[normalize-space()='{text}']")


@then('I expect error message "{text}" is visible')
def verify_error_messages(context, text):
    base_methods.element_visible(
        context, f"//span[contains(@class,'text-danger mt-1 small')]")


@when('I click on "{text}" button of the list "{listname}"')
def delete_list(context, text, listname):
    base_methods.action_click(
        context, f"//a[contains(text(),'{listname}')]//ancestor::tr//descendant::td[3]//span[@title='{text}']")


@then('I expect the free domain error message as "{text}"')
def verify_free_domain_error_message(context, text):
    base_methods.element_visible(context, f"//td[normalize-space()='{text}']")


@when('I click on element "{text}"')
def domain_verify(context, text):
    base_methods.action_click(
        context, f"//tbody/tr[1]/td[3]/div[1]/div[1]/a[text()='Verify']")


@when('I click on the button text "{text}"')
def add_to_crm(context, text):
    base_methods.action_click(
        context, f"//p[@role='button']")


@when('I click on the button having text "{text}"')
def save_crm(context, text):
    base_methods.action_click(
        context, f"//button[@type='submit'][normalize-space()='Save']")


@when('I click on "{text}" icon in contacts')
def step_impl(context, text):
    base_methods.action_click(
        context, f"//h3[contains(text(),'Contacts')]//following::span[@title='{text}']")


@when('I select category "{attr}" "{text}" in domainsearch')
def click_on_drop_down(context, attr, text):
    base_methods.select_option_by(context, attr, text, f"//select[@class='mr-2 select-option custom-select custom-select-sm']")


@when('I add "{text}" into search field "{header}"')
def add_input(context, text, header):
    base_methods.input_text_locator(
        context, text, f"//div[contains(text(),'{header}')]//preceding::input[@placeholder='Search'][1]")

# i wrote


@when('I add "{text}" into a placeholder "{placeholder}"')
def step_impl(context, text, placeholder):
    base_methods.input_data_with_contains_placeholder(context, text, placeholder)


@when('I click on button text "{button}"')
def click_on_lable(context, button):
    base_methods.click_element(context, f"//button[text()=' Verify ']")


@when('I wait for the  element "{text}" with in "{time}" seconds')
def wait_for_element_clickable(context, text, time):
    time = int(time)
    base_methods.wait_element_clickable(
        context, time, text)


@then('I expect that element contains the text "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//p[text()='{text}']")


@then('I click on button linktext "{button}"')
def click_on_lable(context, button):
    base_methods.click_element(context, f"//a[text()='Verify']")


@then('I expect that element status text is "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//*[text()='{text}']")


@then('I expect that element text is there "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//div[text()='{text}']")


@then('I expect that element contains is text "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//*[text()='{text}']")


@then('I click on button to clearall "{text}"')
def step_impl(context, text):
    base_methods.action_click(context, f"//span[text()='Clear All']")


@then('I click on button "{text}"')
def step_impl(context, text):
    base_methods.action_click(context, f"//a[@role='button']")


@then('I click on linklist "{text}"')
def step_impl(context, text):
    base_methods.action_click(context, f"//span[text()='Create New']")


@When('I add "{text}" into "{email_verify}" list name')
def step_impl(context, text, email_verify):
    base_methods.input_text_locator(context, text, f"//div[@id='modal-add-to-list-{email_verify}___BV_modal_body_']//following::input")


@When('I click on "{text}" label "{name}" button with this index number "{num}"')
def click_on_text_buttons(context, num, text, name):
    base_methods.action_click(context, f"//*[normalize-space()='{text}']//following::*[normalize-space()='{name}'][{num}]")


@When('I click on button "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//button[text()='{text}']")


# @when('I wait for element "{text}" with in "5" seconds')
# def step_impl(context, text):
#     base_methods.click_element(context, f"//a[normalize-space() = ' Lists ']")


@then('I expect that in Lists element "{text}" it visible')
def step_impl(context, text):
    base_methods.action_click(context, f"//div[text()=' 500apps.com ']")


@then('I click on button "{button}" is visible')
def click_button_text(context, button):
    base_methods.click_button_text(context, f"//select[@required='required']")


@when('I click on a textlink "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//a[text()='{text}']")


@when('I click on a text "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//a[text()=' Engineering1 ']")


@then('I expect that element textlink "{text}" is visible')
def step_impl(context, text):
    base_methods.click_element(context, f"//div[text()=' 500apps.com ']")


@when('I click on "{text}" in Contacts')
def step_impl(context, text):
    base_methods.click_element(context, f"//h3[contains(text(),'Contacts')]//following::span[@title='{text}']")


@when('I click the button "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//button[text()='Confirm']")


@when('I click on "{text}" in row')
def step_impl(context, text):
    base_methods.click_element(context, f"//span[@title='Delete']")

    # @when('I click  the button "Confirm"')
    # def step_impl(context):
    #     raise NotImplementedError(u'STEP: When I click  the button "Confirm"')


@then('I expect that element with  "Engineering1" does not exist "yes"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I expect that element with  "Engineering1" does not exist "yes"')


@when('I click on element text "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//small[text()=' Switch to Bulk Email Verify']")


@when('I upload file "{file_name}" in "{app_name}" app using class name "{text}"')
def step_impl(context, file_name, app_name, text):
    base_methods.upload_files(context, file_name, f"//input[contains(@class,'{text}')]", app_name)


@when('I wait an a element "{text}" with in "{time}" seconds')
def wait_for_element_clickable(context, text, time):
    time = int(time)
    base_methods.wait_element_clickable(
        context, time, text)


@then('I expect that "{text}" is visible')
def step_impl(context, text):
    base_methods.click_element(context, f"//button[text()='Export']")


@when('I click on that "{text}" is visible')
def step_impl(context, text):
    base_methods.click_element(context, f"//span[text()='Reset']")


@then('I expect that contains text "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//a[text()=' Engineering1 ']")
