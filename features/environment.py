from behave.fixture import fixture, use_fixture_by_tag
from AutoTest.Lib.Log import Log
from AutoTest.Lib.NonAppSpecific import create_driver


@fixture
def browser(context):
    driver_name = context.config.userdata.get("name", "Firefox")
    driver = create_driver(driver_name,
                           context.feature.filename.split("features/")[1].split(".")[0])
    context.driver = driver
    yield context
    # -- CLEANUP-FIXTURE PART:
    if context.aborted or context.failed:
        error = ""
        try:
            error = context.error_msg
        except:
            pass
        Log.screenshot("", True)
        Log.screenshot("Test failed. {}".format(error))
    else:
        Log.screenshot("Test ended successfully", True)
    context.driver.close()


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


fixture_registry = {
    "fixture.browser": browser
}
