from behave.fixture import fixture, use_fixture_by_tag

from AutoTest.Lib.Driver import Driver
from AutoTest.Lib.Log import Log


@fixture
def browser(context):
    driver_name = context.config.userdata.get("name", "Firefox")
    driver = Driver().create_driver(driver_name)
    Log(driver, context.feature.filename.split(".")[0])     #Second parameter works for command line execution
    context.driver = driver
    yield context
    # -- CLEANUP-FIXTURE PART:
    if context.aborted or context.failed:
        Log.screenshot("", True)
        Log.screenshot("".join("Test failed"))
    else:
        Log.screenshot("Test ended successfully", True)
    context.driver.close()


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


fixture_registry = {
    "fixture.browser": browser
}
