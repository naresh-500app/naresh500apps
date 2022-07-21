Feature: Email Verifier module

Background:
        When  I click on the linktext "Email Verify"
          
          
Scenario: Validate the user can find the authenticity of an email with a valid email
    when  I add "preethi.thakur@wipro.com" into a placeholder "Email Address"
    And   I click on button text "Verify" 
    And   I wait for the element "//a[normalize-space()='Verify']" with in "5" seconds
    Then  I expect that element contains the text "preethi.thakur@wipro.com" is visible
    And   I expect that element status text is "80%" is visible 
    And   I expect that element text is there "Email exists" is visible 
    And  I expect that element contains is text "Save" is visible

  
Scenario: Validate the user can find teh authenticity of an email with a invalid email
    When  I add "abinav.samara@tcs.com" into a placeholder "Email Address"
    And   I click on button text "Verify"
    And   I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
    Then  I expect that element contains the text "abinav.samara@tcs.com" is visible
    And   I expect that element status text is "100%" is visible
    And   I expect that element text is there "Email supports catch all combinations." is visible
     And  I expect that element with text "Save" does not exist "yes"

Scenario: Validate the user can use the clearall button in email verify
    When  I add "naresh.gollapothu@500apps.com" into a placeholder "Email Address"
    And   I click on button text "Verify"
    And   I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
    Then  I expect that element contains the text "naresh.gollapothu@500apps.com" is visible
    And   I click on button to clearall "Clear All"
    When  I click on button text "Verify"
   

Scenario: Validate the user can add found to email to list from the verify
    When  I add "manikanta.reddi@500apps.com" into a placeholder "Email Address"
    And   I click on button text "Verify"
    And   I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
    Then  I expect that element contains the text "manikanta.reddi@500apps.com" is visible
    And   I expect that element contains is text "Save" is visible
    And   I click on button "Save"
    And   I click on linklist "Create New"
    when  I add "Engineering1" into "email-verify" list name
    And   I click on "Add to List" label "Create List" button with this index number "4"
    And   I click on button "Save"
    And  I scroll till the page up
    And  I click on a textlink " Lists "
    And  I click on a text " Engineering1 "
    Then I expect that element textlink " 500apps.com " is visible
    And  I expect that element text "Email Verify" is visible
    When I click on "Delete" in Contacts
    And  I click the button "Confirm"
    And  I click on "Delete" in row
    And  I click the button "Confirm"
    # Then I expect that element with  "Engineering1" does not exist "yes"


Scenario: Validate the user can upload the csv file and verify the search results in the bulk email verify
         when  I click on element text "Switch to Bulk Email Verify"
          And  I upload file "Bulkverify50.csv" in "finder" app using class name "file-input"
          And  I wait an a element "//button[normalize-space()='Export']" with in "30" seconds
          Then I expect that "Export" is visible
          when I click on that "Reset" is visible
          Then I expect that element with text "Bulkverify50.csv" does not exist "yes"

Scenario: Validate the user can add a success email to the list from the bulk email verify
    when  I click on element text "Switch to Bulk Email Verify"
     And  I upload file "Bulkverify50.csv" in "finder" app using class name "file-input"
    And  I wait an a element "//button[normalize-space()='Export']" with in "30" seconds
    Then I expect that "Export" is visible
    And  I click on button "Save"
    And   I click on linklist "Create New"
    when  I add "Engineering1" into "email-verify" list name
    And   I click on "Add to List" label "Create List" button with this index number "4"
     And   I click on button "Save"
    And  I scroll till the page up
#     And  I click on a textlink " Lists "
#    Then I expect that contains text "Engineering1" is visible


