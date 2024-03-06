from playwright.sync_api import sync_playwright
import pytest


# If we want run faster our tests we need use this structure, because user will be logged in.
# pytest.fixture(scope="function")
# def browser_session_twoo(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     page.set_default_timeout(3000)
#     # teardown step:
#     page.close()


@pytest.fixture(scope="function")
def browser_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield page
        finally:
            context.close()


@pytest.fixture(scope="function")
def setup_and_teardown(request):
    # Step 1: Befor test -> Set up resource/test data
    # After test:
    def teardown():
        pass
        # Check status of test
        # if request.node.rep_call.passed:
        # Delete resource/data

    # Register function to invoke it
    # request.addfinalizer(teardown)
    # Return needed data for test, for example random name
    # return random_name
