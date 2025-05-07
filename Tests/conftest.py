import pytest
from Utilities.screenshot_util import take_screenshot

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Only capture screenshots for failures in test phase
    if rep.when == "call" and rep.failed:
        driver = item.instance.driver
        test_name = item.name
        take_screenshot(driver, test_name)
