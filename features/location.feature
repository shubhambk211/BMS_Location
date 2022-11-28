Feature: Location

  Background: common steps
    Given launch the browser
    When open BookMyshow homepage
    And search for city

  Scenario: click on location button
    And click on location button
    And search for another city
    Then verify city is selected

  Scenario: select popular city
    And click on location button
    And click on popular city
    Then verify popular city selected

  Scenario: select other city
    And click on location button
    And click on View All Cities
    And click on other city
    Then verify other city selected

