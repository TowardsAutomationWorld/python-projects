Feature: Saucelabs Demo Login Validation

  Scenario Outline: Login Feature Validation
    Given user launches the demo application
    When user should land on the login page
    Then user enter username as "<userName>" in the user name field
    And user enter password as "<password>" in the password field
    And user click on login button on the bottom of the section
    Then user should land on home page
    And user close the application

    Examples:
      | userName      | password     |
      | standard_user | secret_sauce |