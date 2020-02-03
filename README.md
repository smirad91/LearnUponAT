#Automated test Framework - using 'Behave' BDD framework
##How BDD mechanism work in 'Behave'

'Behave' framework divides AUT by features.
Every feature have scenarios, every scenario have steps explained in plain english.
(example can be found in folder *\features\login.feature*)

You can say that every step written in english (example *\features\login.feature*) 
is mapped to function written in python code (example *\feature\steps\login.py*).


##Essential parts of a framework for writing automated tests

Folders that are important for writing tests and their abstract description:
- **AutoTest**
    - **ElementRepository**
        - **LoggingRepository.py** - Contains functions that return element needed for specific feature 
        (for this example it's login feature).
        - **SurveyRepository.py** - not used class, exist just for example
    - **FeatureAction**
        - **LoggingFeature.py** - This is place where we store some code that is repeated in *\features\step\* folder
        (for example file login.py)
    - **Lib**
        - **Driver.py** - Contains mechanism for starting driver
        - **Log.py** - Contains mechanism for logging. Logs will appear in folder *Logs*
        - **NonAppSpecific.py** - Contains a variety of mechanisms that can be used for testing 
        and are not bound to AUT (every AUT can use them)
- **features**
    - **login.feature** - Contains text description in plain english
    - **steps**
        - **login.py** - Contains method mapped from text description
    
## Some specifics in code
- create_driver (NonAppSpecific.py) - Method creates driver and Log instance. It takes
driver name (firefox or chrome) and name of test (ame of test will be name of log file).

This mechanism is added to automated test by using decorator **browser**. Browser decorator
is defined in *\features\environment.py*:
    @fixture
    def browser(context)

This decorator is used in login.feature as: @fixture.browser. This tag is mandatory for scenarios.

- wait_until (NonAppSpecific.py) - Method used for waiting for some condition (example of use in login.py).
Replacement for WebDriverWait.
       
- implicit_wait - workaround for time.sleep() as it does not work under 'Behave' framework

## Dependencies between classes
Classes that are in path *\features\steps\* use attributes from her mapped classes:
- mapped class from **FeatureAction** folder (example login.py uses LoggingFeature.py and survey.py uses SurveyFeature.py)
- mapped class from **ElementRepository** folder (example login.py uses LoggingRepository.py, and survey.py would use SurveyRepository.py)
- and **NonAppSpecific.py** (for example login.py and survey.py is using it)

![classes](.\classes.png)

##Logging standard
Preferred way to log:
   1. Log message explained what is going to be done
   2. Execute the action
   3. Wait for action to finish
   4. Log screenshot or info


# Setting environment for test execution(only for windows):

   1. precondition is to have python 3.8.1 installed (from python.org). after installing check python version: open cmd and execute command: **python -V**.
                Result should be in shape: Python 3.8.1
   2. for second step, choose one from two options. you can create virtual environment (use this if you have multiple projects in python with different package dependencies) 
    or use global python that you have installed
            - first way: create virtual environment 
                    -execute: **pip install env**
                    -in cmd go to folder *PythonVirtualEnvironment* (in this code repository) and execute: **python -m venv env** 
                     (folder 'env' is now inside of folder *PythonVirtualEnvironment*)
                    -in cmd navigate to mentioned folder *PythonVirtualEnvironment\env\Scripts*, and execute: **pip install behave**
                    -then execute: **pip install selenium**
                    -then execute: **pip install pyautogui**
            - second way: use global python
                    -in cmd execute: **pip install behave**
                    -execute: **pip install selenium**
                    -execute: **pip install pyautogui**
    3. set environment variable PYTHONPATH: on mycomputer open properties, advanced system settings, 
    environment variable, in system variables should be added new variable name: PYTHONPATH  (if it does not exist),
    and variable value path set to project code(example: *C:\Users\Desktop\LearnUponAT*) 

# Run tests

- if you created virtual environment, open path in cmd *PythonVirtualEnvironment\env\Scripts*
    and if you are using global python, then path in cmd is not important, no steps here
- then execute behave command with path to features folder
example: **behave C:\Users\Desktop\LearnUponAT\features**

By default tests are run in Firefox, and browser can be set by adding parameter to command line: **-D browser=chrome** 
ili **-D browser=firefox**
- example how to run test in chrome: **behave C:\Users\Desktop\LearnUponAT\features -D browser=chrome**
- after test are run, html logs can be found in LearnUponAT\Logs folder


