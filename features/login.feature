Feature: Logging in

  As a site user
  I want to log in to site using my credentials
  So that I can use it

  @fixture.browser
  Scenario Outline: Logging in with right credentials
     Given I have logging page "http://qa-test-dev.s3-website-eu-west-1.amazonaws.com/login.html" opened in browser
     When I input <username> as username and <password> as password
     And click "Login" button from logging page
     Then page with login information status "Login Successfull" opens
    Examples:
    | username | password |
    | batman | r00bin |

  @fixture.browser
  Scenario Outline: Logging in with wrong credentials
     Given I have logging page "http://qa-test-dev.s3-website-eu-west-1.amazonaws.com/login.html" opened in browser
     When I input <username> as username and <password> as password
     And click "Login" button from logging page
     Then page with login information status "Login failed." opens
    Examples:
    | username | password |
    | batman | JklBmNo# |
    | johndoe | pa34443 |
    | batman |  |
    |  | pa34443 |
    |  |  |

