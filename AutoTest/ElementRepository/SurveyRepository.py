"""
Example class. Not used
"""
class SurveyRepository:

    ###Elements on logging page

    @staticmethod
    def inp_survey(context):
        return context.driver.find_element_by_id("survey")