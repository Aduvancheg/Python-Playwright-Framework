from swagger_playwright import SecretKey, BasePage
from api_framework_swagger import RequestPOST, RequestGET, RequestPUT, RequestDELETE
from playwright.sync_api import expect

expect.set_options(timeout=10_000)


def test_create_and_verify(browser_session):
    """This test create new record by POST method, afterwards GET
    method takes records data and verify equality of the names"""

    page = browser_session
    secret_key = SecretKey.get_secret_key(page)
    endpoint = BasePage.endpoint_coffee(secret_key)

    payload = {"Name": "New Comfy Coffee", "Description": "Never be the same!"}
    record_id = RequestPOST.post_create_record(endpoint, payload)
    record_name = RequestGET.get_record_data(endpoint, record_id)
    assert payload["Name"] == record_name


def test_create_and_update(browser_session):
    """This test create new record by POST method, afterwards PUT
    method will update Name of the Coffee"""

    page = browser_session
    secret_key = SecretKey.get_secret_key(page)
    endpoint = BasePage.endpoint_coffee(secret_key)

    payload_post = {"Name": "New Comfy Coffee", "Description": "Never be the same!"}
    record_id = RequestPOST.post_create_record(endpoint, payload_post)

    payload_put = {
        "Id": record_id,
        "Name": "Updated new Name",
        "Description": "Be the same!",
    }
    updated_name = RequestPUT.put_update_record(endpoint, payload_put)
    record_name = RequestGET.get_record_data(endpoint, record_id)
    assert updated_name == record_name


def test_create_and_delete(browser_session):
    """This test create new record by POST method, afterwards DELETE
    method will delete this record"""

    page = browser_session
    secret_key = SecretKey.get_secret_key(page)
    endpoint = BasePage.endpoint_coffee(secret_key)

    payload_post = {"Name": "New Comfy Coffee", "Description": "Never be the same!"}
    record_id = RequestPOST.post_create_record(endpoint, payload_post)
    delete_record = RequestDELETE.delete_record(endpoint, record_id)
    assert delete_record == 204


def test_log_in(browser_session):
    page = browser_session
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(30000)

    page.locator("xpath=//*[contains(@class, 'jjPduP')]").click()
    # page.click("'Log In'")
    # page.get_by_role("button", name="Log In").click()
    # page.get_by_role(role="button", name="Log In").click(timeout=3000)
    # page.locator("xpath=//*[contains(@data-testid, 'buttonElement')]").click()
    # #first check
    # email_input  = page.get_by_role(role="textbox", name="Email")
    # email_input.fill("test1")
    # expect(email_input.locator("#input_input_emailInput_SM_ROOT_COMP766")).to_contain_text('test1', timeout=5000)
    # expect(page.locator("#input_input_emailInput_SM_ROOT_COMP766")).to_contain_text('test1')
    # page.pause()
    # page.wait_for_selector("#input_input_emailInput_SM_ROOT_COMP766", timeout=5000).to_be_visible()
    # expect(page.get_by_role(role="textbox", name="Email")).to_contain_text('test1')
    # #second check
    # page.locator("#input_input_emailInput_SM_ROOT_COMP766").fill("test2")
    # expect(page.locator("#input_input_emailInput_SM_ROOT_COMP766")).to_have_text("test2")

    # page.fill('input:below(:text("Email"))', "test2")
    # expect(page.locator("#input_input_emailInput_SM_ROOT_COMP766")).to_have_text("test2")

    # page.get_by_text("Log In").click()
    # page.get_by_role("button", name="Log In").click()
    # page.get_by_test_id("signUp.switchToSignUp").click()
    # page.get_by_role("button", name="Log in with Email").click()
    # page.get_by_label("Log In").click(button="right")
    # page.fill('input:below(:text("Email"))', "test")
    # expect(page.get_by_test_id("emailAuth").get_by_label("Email")).text_content("test")
