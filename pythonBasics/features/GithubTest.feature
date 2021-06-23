# Created by ajay at 23/06/21
Feature: GitHub Api Validation

  # We are going to hit

  Scenario: Session management verification
    Given I have github access token
    When I hit github user resource
    Then status code of response should be 200