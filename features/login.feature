Feature: Login

    Scenario Outline: Login with valid Username and Password
        Given I load the website and I go to "Login" page
        When I Enter <username> in username field
        And I Enter "<password>" in password field
        And I press the "Login" button
        Then Login should be success and user should be redirected to "dashboard" page
        And Logout from portal
        Examples:
            | username                            | password                   |
            |bgajera.contractor@libertyglobal.com | Brijesh@Bynder             |


    Scenario Outline: Login with invalid Username and Password
        Given I load the website and I go to "Login" page
        When I Enter "<username>" in username field
        And I Enter "<password>" in password field
        And I press the "Login" button
        Then Login should fail with error message "incorrect username or password"
        Examples:
            | username                            | password                   |
            |bgajera1234.contractor@libertyglobal.com | Brijesh@Bynder1234             |

    Scenario Outline: Login with valid Username and invalid Password
        Given I load the website and I go to "Login" page
        When I Enter "<username>" in username field
        And I Enter "<password>" in password field
        And I press the "Login" button
        Then Login should fail with error message "incorrect username or password"
        Examples:
            | username                            | password                   |
            |bgajera.contractor@libertyglobal.com | Brijesh@Bynder12344             |

    Scenario Outline: Login with invalid Username and valid Password
        Given I load the website and I go to "Login" page
        When I Enter "<username>" in username field
        And I Enter "<password>" in password field
        And I press the "Login" button
        Then Login should fail with error message "incorrect username or password"
        Examples:
            | username                            | password                   |
            |bgajera1234.contractor@libertyglobal.com | Brijesh@Bynder12344             |

    Scenario Outline: Login with invalid Username and valid Password
        Given I load the website and I go to "Login" page
        When I Enter "<username>" in username field
        And I Enter "<password>" in password field
        And I press the "Login" button
        Then Login should fail with error message "incorrect username or password"
        Examples:
            | username                            | password                   |
            |bgajera1234.contractor@libertyglobal.com | Brijesh@Bynder12344             |

    Scenario Outline: Login with valid Username and blank password
        Given I load the website and I go to "Login" page
        When I Enter "<username>" in username field
        And I press the "Login" button
        Then Login should fail with error message "enter your password"
        Examples:
            | username                            |
            |bgajera1234.contractor@libertyglobal.com |