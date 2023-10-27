Feature: Mobile Web - Password Change

  Scenario: Mobile-web User can open change password page
    Given Open Main Log In page
    When Log in to the page
    Then Click on settings option in Mobile
    And Click on Change password option in Mobile
    And Verify the right page opens
    And Add some test password to the input fields
    And Verify the “Change password” button is available