---
title: Types > Phone
category: Questions
order: 8
---

\* Under Construction \*  
Free text entry of a phone number. 

#### Format Options

* Auto
* International
* International Mobile

#### Validation Errors  

Validation of phone numbers is done for for International and International Mobile numbers only and will need a valid country code.  

To configure this, go to Advanced Settings and set the format to 'International' or 'International Mobile' and then enter a valid Country Code. 
eg. **NZ** for New Zealand or **AU** for Australia  
For other countries please refer to the Alpha-2 codes found on [the ISO website](https://www.iso.org/publication/PUB500001.html){:target="_blank"}

If validation fails an error message will appear. eg. for an invalid New Zealand phone number  
"Not a valid NZ phone number, please check | Ignore"

or for an invalid International Australian Mobile Number  
"Not a valid AU mobile number, please check | Ignore"

These error conditions are evaluated when the user attempts to move to the next section, or submit.  

There is an option to ignore invalid numbers and if this is selected the user is able to continue to the next section or submit the form. This is because sometimes the system will block legitimate entries.  

If the phone number is valid the number will be formatted according to standard internationl rules.  
eg. for a format of 'International Mobile' with a Counrty Code set to 'NZ' an entry of `0223709899` will be formatted as `+64 22 370 9899`