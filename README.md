# LearnUponAT

# Standard for actions in test:
# 1. log message
 # 2. do the action
 # 3. wait for action to finish
# 4. log screenshot or info

How to execute tests

-Setting environment (only for windows):
* precondition is to have python 3 installed (python.org). first check python version, open cmd and execute command: python -V.
                Result should be in shape: Python 3.8
* you can create virtual environment (use this if you have multiple projects in python with different package dependencies) 
    or use global python that you have installed:
            1. to create virtual environment 
                -execute: pip install env
                -in cmd go to folder PythonVirtualEnvironment and execute: python -m venv env (folder env is now inside of folder PythonVirtualEnvironment)
                -in cmd navigate to new folder, PythonVirtualEnvironment\env\Scripts, and execute: pip install behave
                -then execute: pip install selenium
                -then execute: pip install pyautogui
            2. to use global python
                -in cmd execute: pip install behave
                -execute: pip install selenium
                -execute: pip install pyautogui
*set environment variable PYTHONPATH: on mycomputer open properties, advanced system settings, 
environment variable, in system variables should be added if not exist new variable name: PYTHONPATH,
and variable value path to project code(example: C:\Users\Desktop\LearnUponAT) 