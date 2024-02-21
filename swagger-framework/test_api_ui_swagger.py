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
