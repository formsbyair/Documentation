---
title: Types > Phone
category: Questions
order: 7
---

\* Under Construction \*  
Free text entry of a phone number. 

#### Format Options

* Auto
* International
* International Mobile

#### Validation Errors  

Validation of phone numbers is done for for International and International mobile numbers only and therefore need a valid country code.

To configure this, go to Advanced Settings and set the format to 'International' or 'International Mobile' and enter a valid Country Code. 
eg. **NZ** for New Zealand or **AU** for Australia  
(see Alpha-2 code in ISO 3166 country codes on https://www.iso.org/iso-3166-country-codes.html)  

If validation fails an error message will appear. eg. for an invalid New Zealand phone number  
<span style="color:red">! Not a valid NZ phone number | Ignore</span>

or for an invalid internation Austrlain mobile number  
<span style="color:red">! Not a valid AU mobile number | Ignore</span>

There is an option to ignore invalid numbers.  

If the phone number is valid the number will be formatted according to standard internationl rules.  
eg. for a format of 'International Mobile' with a Counrty Code set to 'NZ' an entry of `0223709899` will be formatted as `+64 22 370 9899`