# FormsByAir knowledge base

Q&A-style troubleshooting articles, newest first, merged from the documentation site's knowledge base.

## 2024-12-04 — Cliniko Integration - Custom patient fields

Cliniko has allowed you to create custom fields in the Patient Details section, I can't seem to map to it. Can you please advise?

Ive attempted to just use the name field - this resulted in nothing appearing

Ive attempted to treat the field as an entity \(like the phone number entry\) - but this didn't work either and caused the integration to fail

Thank you


---
## 1 Answers

Please map custom fields as per example below...

```
{
  "Entities": [
    {
      "Name": "patient",
      "Attributes": [
      ],
      "Entities": [
        {
          "Name": "custom_fields",
          "Attributes": [
            {
              "Name": "section",
              "Value": "General Practitioner Details"
            },
            {
              "Name": "name",
              "Value": "Practitioner Name"
            },
            {
              "Name": "value",
              "Value": "<<PractitionerName>>"
            }
          ]
        },
        {
          "Name": "custom_fields",
          "Attributes": [
            {
              "Name": "section",
              "Value": "General Practitioner Details"
            },
            {
              "Name": "name",
              "Value": "Practice Name"
            },
            {
              "Name": "value",
              "Value": "<<PracticeName>>"
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 2024-12-02 — Australian address integration

Is there any Australian address integration options available, similar to the NZPost address integration? Preferably a free one!


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
The only free option we have for Australia is our standard "Address Picker" \(Google\), see configuration below.

Addressable and Address Finder support Australia, but require a paid subscription.

[![enter image description here](/images/kb/8eec105db4b0482aae668779b67392a6.png)](/images/kb/8eec105db4b0482aae668779b67392a6.png)
</div>

---

## 2024-11-17 — How can I determined that a form is a Third Party Request?

We have a requirement for a item to be mandatory if it is made in a third party request, but if that same item is currently displayed in the main form, then it is not mandatory.

This is to allow capture of information from the main form filler, but only require active confirmation of that \(basically a I declare this is true and correct tickbox\) if it is actually farmed out as a Third Party Request.


---
## 1 Answers

Try using $scope.isThirdPartyRequest like this...

[![enter image description here](/images/kb/fd82431b718a43ec827042984300c3c5.png)](/images/kb/fd82431b718a43ec827042984300c3c5.png)

[![enter image description here](/images/kb/a55d2b3f2e87489da840f4d26c7da375.png)](/images/kb/a55d2b3f2e87489da840f4d26c7da375.png)

---

## 2024-11-13 — Save email fails with error \"No recipients\

I've setup an email integration to send "On Save" with recipient &lt;&lt;MainContactEmailAddress&gt;&gt;

If I start my form, click "Save & Finish Later" enter my email address, and click Save, I don't get the email, and the integration has an error "No Recipients"


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
The element\(s\) with tag name "MainContactEmailAddress" are probably behind an inactive conditional path, so the email address you enter is not getting saved in the form. Try using an email address field that is always visible, or add a hidden formula field to store the email address.
</div>

---

## 2024-10-14 — Output the repeater title and number # in the output file

I am creating a custom word doc template for my form output. Is it possible to output the repeater title and number from the form in the output file? I can hard code the title into my word doc, and I have tried count and sum but this gives me the total of repeaters that have been used in the form. Or, it outputs "1" for each repeater.

[![enter image description here](/images/kb/297791ea4c804531b62c7997e3681f8c.png)](/images/kb/297791ea4c804531b62c7997e3681f8c.png)


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Use the **&lt;&lt;\[Index\]&gt;&gt;** tag in your template, for example

```
Locality #<<[Index]>>
```

> **Comments:**
> * Hey @ShaunDavis. Do I need to use an escape character before my greater than symbol '>' if I only want to output the index number when the repeater is greater than 1. I've tried using the following syntax and I broke my word doc template:  <<[Condition:'<<[Index]>>' > '1':#<<[Index]>>]>>Thanks in advance for your help.
> * Hi @ChrissyBrown  just amend slightly to remove the ' and addition of extra open and close brackets <<<[Condition:<<[Index]>> > 1: #<<[Index]>>]>>>
</div>

---

## 2024-10-02 — How do you add the option to add additional items in a linked repeater?

I have a 'staged' form where the person initiating the form can add multiple items to a repeater. These items are being output for the third party to review and amend \(if required\). The third party also needs to be able to add or remove the repeater items.

The "Add Another Item" button, and the "x" \(removal\) are not visible in the linked repeater.

**Repeater - filled in by form 'initiator'**

[![enter image description here](/images/kb/c5fb81187bec4e9a93f46c672d18f6be.png)](/images/kb/c5fb81187bec4e9a93f46c672d18f6be.png)

Third party receives email with link to form. The repeater items are displayed correctly, however, there is no option to remove the repeater items, or add additional items.

[![enter image description here](/images/kb/42696e3cc95640d18fc54be1ff1d5c90.png)](/images/kb/42696e3cc95640d18fc54be1ff1d5c90.png)

How do I make the "Add Another Condition" and removal option visible for the third party?


---
## 2 Answers

You can't used a linked repeater if you want to add/remove items in the second repeater. You would instead need to set a **Default Value** on the second repeater like this:

```
<<[ForEach:FirstRepeater]>>
```

> **Comments:**
> * Thank you @ShaunDavis. The 'ForEach' option in the Default Value is showing the correct number of repeater items in the second repeater BUT, it's not outputting the values from the First Repeater questions. I think I may have the syntax wrong.

---
<div class='accepted-answer-box' markdown='1'>
Use this syntax to output the values from the first repeater

[![enter image description here](/images/kb/9e4db79ecf54403eb53587fd255fa44f.png)](/images/kb/9e4db79ecf54403eb53587fd255fa44f.png)

[![enter image description here](/images/kb/ebf679aae47b4093a12f9ab9fc36936a.png)](/images/kb/ebf679aae47b4093a12f9ab9fc36936a.png)
</div>

---

## 2024-10-01 — Forms not functioning on older model iPads

We are having issues with our older model iPads not loading FBA forms for the past 2 weeks, we have tried with iOS12, 15 and 16.3.

We are getting to the forms \(it is affecting more then just one form\) via a web link, which works without issue when using iPhone iOS 17 & 18 or from a desktop

We have tried using, Safari, DuckDuckGo and Firefox and none have loaded the page, it is just a white page with no content

Can you please advise

Thank you


---
## 2 Answers

It looks like there may be a problem with iOS 16.3 and earlier, iOS 16.4 and above seems OK.

We're investigating, but in the meantime, are you able to update iOS on the affected devices to 16.4 or newer?

---
We've now resolved the issue with iPad/iOS compatibility, we've tested back to iOS 12.4

---

## 2024-09-24 — Embedding images into custom pdf template

Is it possible to embed uploaded images into a custom pdf template? Ideally in conjunction with Condition and ForEach tags.

> **Comments:**
> * just to check - are you talking about embedding images that were attached as part of a form submission to PDF output (instead of delivering them as separate files)
> * @ShaunDavis Correct - embed uploaded image(s) into the pdf output, instead of separate files, so you end up with one (PDF) file.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Unfortunately we have no way to do that right now, we'd have to look at it as a future enhancement to our platform
</div>

---

## 2024-09-11 — FormsbyAir Comment box text formatting to flow through to Cliniko

I have a comment box in a form that I have created, I would like to have the formatting of the text in the box preserved when it goes through the json file to then create the entry in Cliniko with line breaks carried across, is this possible?

I have tried to wrap the tag in &lt;pre&gt; and &lt;/pre&gt; in the json file but this has not changed the output in Cliniko.

Thank you

> **Comments:**
> * Can you clarify which field you're trying to populate in Cliniko
> * @ShaunDavis Hi Shaun, trying to populate into a treatment note. Thanks Shaun.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Please edit your Cliniko mapping file and change the value for **type** from "text" to "paragraph" for each applicable treatment note field

```
        {
          "Name": "treatment_notes",
          "Attributes": [
            {
              "Name": "name",
              "Value": "Presenting complaint"
            },
            {
              "Name": "type",
              "Value": "paragraph"
            },
            {
              "Name": "answer",
              "Value": "<<ReasonForVisit>>"
            }
          ]
        }
```

> **Comments:**
> * Hi Shaun,
</div>

---

## 2024-08-25 — How do I simplify a list containing duplicate text items, to a new list containing only the unique values?

How do I simplify a list containing duplicate text items, to a new list containing only the unique values?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Add a "new Set Expression", such as:

\[...new Set\('a|b|c|a|b|c'.split\('|'\)\)\].join\(", "\)

If the string were 'a|b|c|a|b|c', splitting it with | would give you 'a, b, c'

Note: Each value in the original list is separated buy a '|' character.

Example:  \[...new Set\('&lt;&lt;\[ForEach:Fund\[|\]:&lt;&lt;FundName&gt;&gt;\]&gt;&gt;'.split\('|'\)\)\].join\(", "\)

The expression starts with a string, splits it into parts based on |, removes duplicates, and then joins those parts back together into a single string, separated by commas.
</div>

---

## 2024-08-20 — How can I dynamically choose who can Authorise a document in workflow?

How can I dynamically choose who can Authorise a document in workflow?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
With "Requires Authorisation" under form settings checked.

Add an "Authorisation Assignment Expression", like the below example:

'&lt;&lt;Authoriser&gt;&gt;' != '' ? '&lt;&lt;Authoriser&gt;&gt;' : 'daniel@formsbyair.com'

Note: The expression needs to default to something non-blank so that the portal will display the "Request Authorisation" button.

You can use &lt;&lt;\[DocumentWorkflowUserEmail\]&gt;&gt; as the "Recipient Email Address\*\*"\*\* in the email integration to notify the authoriser.

[![enter image description here](/images/kb/2c0c8b4435e34d748b683ecd1022e7a8.png)](/images/kb/2c0c8b4435e34d748b683ecd1022e7a8.png)
</div>

---

## 2024-07-23 — Custom footer on the last page of automated PDF

I have a form with a lot of conditions and questions that generates a 20 pages PDf.
This PDF uses a WORD template but it is not a custom word due to the amount of questions and conditions.
We need to display some information on the last page of this PDF.
Is there a way to insert a Custom footer on the last page of automated PDF ?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Yes that's fine, just create a new **section** in your Word document, and add content \(or a footer\) to that section.

FBA will inject form data in the first section of your document as long as it's left blank.

[![enter image description here](/images/kb/e07595297c90492bb4466fdbf06e1d3e.png)](/images/kb/e07595297c90492bb4466fdbf06e1d3e.png)
</div>

---

## 2024-06-18 — Unable to output ForEach expression in Display Content because custom html code is being converted

I need to output special condition items as Display Content in a form. The items are from a repeater item, so there may be one item, or there could be 10. Ideally I'd like the items output as an alpha list. This is the syntax I'm trying to add to the Display Content in the form:

&lt;ol type="a"&gt;

&lt;&lt;\[ForEach:SpecialConditionItems\[&lt;/li&gt;\]:&lt;li&gt;&lt;&lt;SpecialConditionItem&gt;&gt;\]&gt;&gt;

&lt;/li&gt;&lt;/ol&gt;

I've tried adding the above syntax to both the Code Editor and directly into the Editor.

**Above code added to Code Editor:**

[![enter image description here](/images/kb/fde124957fa34816ad3a8b86967966da.png)](/images/kb/fde124957fa34816ad3a8b86967966da.png)

**Preview in Editor after adding above code:**

[![enter image description here](/images/kb/fabd20bbabf142e2a619d8fda681e87c.png)](/images/kb/fabd20bbabf142e2a619d8fda681e87c.png)

**Check code after preview in editor - syntax has been translated:**

[![enter image description here](/images/kb/559e3003e4614e58acd017079657f631.png)](/images/kb/559e3003e4614e58acd017079657f631.png)

**Adding syntax/html code directly into Editor:**

[![enter image description here](/images/kb/ab0861f9b64e4107a6b7f4022f64bf68.png)](/images/kb/ab0861f9b64e4107a6b7f4022f64bf68.png)

**The above is then translated to:**

[![enter image description here](/images/kb/79396104b89c448092e8500ff333a0f1.png)](/images/kb/79396104b89c448092e8500ff333a0f1.png)

**Form output if I use the above option:** [![enter image description here](/images/kb/a02ab2fa86294cccb8d68085da975a3c.png)](/images/kb/a02ab2fa86294cccb8d68085da975a3c.png)

In principal, this option is at least outputting the repeater items BUT how do I stop the html code being converted to text so the form output reads the html code?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
You can generate a **bullet point** list in Display Content as follows...

```
<div>&lt;&lt;[ForEach:SpecialConditionItems[<br>]:* &lt;&lt;SpecialConditionItem&gt;&gt;]&gt;&gt;</div>
```

This uses markdown syntax for each bullet point, and ensures the PDF output will also be a bullet point list.

Unfortunately using HTML syntax for a numbered list &lt;ol&gt;&lt;li&gt; isn't going to work, this also wouldn't render in PDF output.
</div>

---

## 2024-06-14 — Amount of digits for a number question

how do I set a question to have exactly 6 digits, not less, not more ?

It is a number question type.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Change the type of your question to **Pattern** and set Input Mask to 999999

> **Comments:**
> * Thank you !
</div>

---

## 2024-05-07 — Custom styles for Word Template - List 1 and List 2

Is is possible to have a custom style for word template, that would allow me to customize my lists levels. Example Form List1 , Form List2 ?


---
## 1 Answers

Just to check - are you saying that you have "Display Content" in your form \(with bullet points or numbered lists\) that you want to apply formatting to in the PDF output \(using a Word template\) ?

As it stands, you can use Word styles for some elements \(as per [https://docs.formsbyair.com/templates/word/](https://docs.formsbyair.com/templates/word/)\) but not list items.

Another option would be to use a Word template with &lt;&lt;tags&gt;&gt; so we're populating specific data rather than dumping out everything in the form. You can then "hard code" display content in to the template using whatever formatting you need.

> **Comments:**
> * Hey Shaun,
> * Hey Shaun,Yes, that is what I am saying. My words template already have all the Custom Styles that are listed here https://docs.formsbyair.com/templates/word. We were trying to avoid using a custom word as our original source is a 40 pages word document. The question if was possible to add style into ordered and unordered lists in our word template was to save time on making a word template with the tags.

---

## 2024-05-02 — Converting Excel PMT and FV functions to a FBA formula

We are trying to convert a calculated Excel document into a Form. "Google" has provided some options for converting the Excel function to a math formula, but we can't work out how to get the formula to work, or how/if we need to convert/use the ^ \(power of\) symbol in the FBA formula.

The Excel functions are:

=PMT\(C13/12,G11,-C11,0,0\)

=FV\(C13/12,G15,G13,-C11\)

Where:

C13 = 3.95% \(interest rate\)

G11 = 360 \(initial loan term - months\)

C11 = $516,490 \(Initial loan\)

G15 = 288 \(Remaining working term of borrower - months\)

[![enter image description here](/images/kb/831c1b7ec14d4b5db8be3f6a8dd73167.png)](/images/kb/831c1b7ec14d4b5db8be3f6a8dd73167.png)

[![enter image description here](/images/kb/6e2665ed456440a6a4ba9c349fcf9150.png)](/images/kb/6e2665ed456440a6a4ba9c349fcf9150.png)

This is PMT formula we've found on Google that we thought might work:

\(\(516490 \* \(0.0365/12\)\) / \(1 - \(\(1 + \(0.0395/12\)\)^\(-1 \* 360\)\)\)\)

We broke this down into multiple formula fields in FBA, on the assumption this would be easier for the final calculation, but clearly we've gone wrong somewhere.

[![enter image description here](/images/kb/0b7b8db7609d439e8cfac235d1bd40ba.png)](/images/kb/0b7b8db7609d439e8cfac235d1bd40ba.png)

Is is possible to convert the Excel formulas to FBA functions? If yes, can we have some help on how to do this please.

TIA.


---
## 1 Answers

FBA uses Javascript for formulas, so we need to convert Excel's PMT\(\) and FV\(\) functions to Javascript.

I used ChatGPT to do this, which can be then be implement using a few formula questions as follows:

```
MonthlyRate
<<AnnualRate>> / 12

PMTFactor
Math.pow(1 + <<MonthlyRate>>, <<NumberOfPayments>>)

Payment
- (<<PresentValue>> * <<PMTFactor>>) * <<MonthlyRate>> / (<<PMTFactor>> - 1)

FVFactor
Math.pow(1 + <<MonthlyRate>>, <<RemainingWorkingTerm>>)

FutureValue
- (<<PresentValue>> * <<FVFactor>> + <<Payment>> * (1 + <<MonthlyRate>> * 0) * (<<FVFactor>> - 1) / <<MonthlyRate>>)
```

[![enter image description here](/images/kb/aff87dec6e484a409871c131002583b9.png)](/images/kb/aff87dec6e484a409871c131002583b9.png)

---

## 2024-04-10 — Can I use conditional statements in the Confirmation Editor?

I'm trying to output custom text in the confirmation message on submit of the form.

This is the syntax I'm using in the editor:

&lt;&lt;\[Condition:'&lt;&lt;\[DocumentStage\]&gt;&gt;' == '1\_Admin':An email has been sent to the broker.\]&gt;&gt;

&lt;&lt;\[Condition:'&lt;&lt;\[DocumentStage\]&gt;&gt;' == '2\_Broker':Your acknowledgement form has been sent to your regional manager for sign off.\]&gt;&gt;

&lt;&lt;\[Condition:'&lt;&lt;\[DocumentStage\]&gt;&gt;' == '3\_RegionalManager':The acknowledgement form has been sent to the general manager for final sign off.\]&gt;&gt;

Below is a screenshot of output on submit of the first stage \(1\_Admin\) - all conditional options are being output with some of the conditional syntax:

[![enter image description here](/images/kb/9f514ec6bc064c138c9844540662e5f3.png)](/images/kb/9f514ec6bc064c138c9844540662e5f3.png)

Is the syntax incorrect, or is not possible to have conditional statements in the Confirmation type editor?

Not sure if this is relevant - the conditional syntax was added directly into the editor. When previewing the code, the angle brackets "&lt;", "&gt;" had been converted to html entities:

[![enter image description here](/images/kb/c19305e1e9ff499ea847585032064f67.png)](/images/kb/c19305e1e9ff499ea847585032064f67.png)


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
The Confirmation Editor only supports tag replacement, it doesn't evaluate expressions.

You'd need to use a hidden formula field for your expression\(s\), then refer to that with a tag in the Confirmation Editor.
</div>

---

## 2024-03-25 — How do I use bold formatting in a word template

When creating a word template to be used for a PDF integration, I am trying to get a some bold text within the condition but the output document doesn't work.

I've tried &lt;b&gt; and &lt;strong&gt; but those don't work either.

&lt;&lt;\[Condition:'&lt;&lt;tag&gt;&gt;' != '' :&lt;br&gt;Your data has changed:&lt;br&gt;FROM:&lt;br&gt;**Existing 1**: &lt;&lt;Existing1&gt;&gt;TO:&lt;br&gt;**New 1**: &lt;&lt;New1&gt;&gt;\]&gt;&gt;


---
## 1 Answers

The best option here is to use &lt;&lt;\[Condition\]&gt;&gt; with a table cell in Word. If the condition is true the contents of the cell \(with all formatting\) will be displayed, otherwise the table cell will be removed. You can hide the border of the table/cell if not required.

[![enter image description here](/images/kb/64015b20d6a4469f97485bc7c0dede19.png)](/images/kb/64015b20d6a4469f97485bc7c0dede19.png)

---

## 2024-03-12 — Count responses in a multi-select

How can I count the number of responses in a multi-select?

for example if I need a conditional path if 2 or more responses have been selected?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Use this expression to get the number of selected options where **Option** is the Tag Name for all of your option elements.

```
<<[Count:Option{'<<Option>>' == 'true'}]>>
```
</div>

---

## 2024-02-12 — Updating Azure Cosmos data

an issue we've come across is with our updating details form.

The existing integration for updating, is changing the types of all the variables into strings. E.g the GrantPrice should be a Number \(34\), but upon submitting update these change into a string \("34"\). In our json map we've put "type": "Int" but that seems to do nothing.

We need some variables to stay as strings and others to be numbers. Just wondering where we state what type a variable need to save in.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
No problem... please add Setter: float to your mapping file for all number types...

```
        {
          "Name": "GrantPrice",
          "Value": "<<GrantPrice>>",
          "Setter": "float"
        }
```
</div>

---

## 2024-02-08 — Workflow notifications

For one of our forms, employees seem to be receiving 'New Submission' - Workflow emails without having their email address on any kind of notification, or submission email list. Just wondering how this is happening and if it is something that I have set up.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Yes, our system will send workflow notifications to users by default.

If you've setup custom notifications, or don't need notifications at all, you can disable this behaviour in form settings...

[![enter image description here](/images/kb/f24c38e9a46d4f579b342991107737be.png)](/images/kb/f24c38e9a46d4f579b342991107737be.png)
</div>

---

## 2024-01-31 — Get current item when iterating over an array of tags with the same name

If I have an number of tags, all with the same name that are not contained in a repeater, I can iterate over them in a Map by using the tag name, but, how do I then specify the current item being iterated if I want the value of it?

e.g. We have a tag of **Item** which is used several times on various questions.

In the map we have

```
{
    "Name": "Items",
    "ForEach": "Item",
    "Setter": "array",
    "Attributes": [
        {
            "Name": "Description",
            "Value": "<<Item>>"
        }
    ]
}
```

The resulting XML from this is

```
<Items><Description></Description></Items>
```

How do I get the Description element populated with the contents of the current Item node?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
We can't produce XML output like this...

```
<?xml version="1.0" encoding="utf-8"?>
<Items>
    <Description>1</Description>
    <Description>2</Description>
    <Description>3</Description>
</Items>
```

The closest we can get would be this...

```
<?xml version="1.0" encoding="utf-8"?>
<Items>
  <Item>
    <Description>1</Description>
  </Item>
  <Item>
    <Description>2</Description>
  </Item>
  <Item>
    <Description>3</Description>
  </Item>
</Items>
```

...which you can generate with this map...

```
{
  "Name": "Items",
  "Entities": [
    {
      "Name": "Item",
      "ForEach": "Item",
      "Setter": "array",
      "Attributes": [
        {
          "Name": "Description",
          "Value": "<<[This]>>"
        }
      ]
    }
  ]
}
```

> **Comments:**
> * Sure, I left out some of the parent info in the map, so yes we are wrapping in an outer Entities array.  But, you answered the question with the <<[This]>>  value which is what I need.  Cheers,
</div>

---

## 2023-12-14 — Request Expiry

Is there a maximum number of days we can use for the Document Request Expiry option? Can we set it to 90 days? And does the Document request expiry apply to both the save and finish later option and the first Send Request email?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
You can set request expiry to whatever you need, 90 days is fine.

**Request Expiry** applies where a form has been prefilled, and the client hasn't added any data themselves yet.

**Save Expiry** applies as soon as a form is saved the first time. It's a rolling 30 day expiry, and extends out every time you re-save. It's a smaller window on purpose because the form is higher risk once the client starts entering their data.
</div>

---

## 2023-08-30 — Send form attachments via email

How can I send the attachments to a form via email?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Form attachments can’t be sent on their own, they get included when you generate a file for a form e.g. a PDF

The easiest option is to create an integration with “Send form data in a file” and Delivery Method “Email Attachment”.

Alternatively, you can create an Email integration and set “Attach Email Files” to Internal. Then create a File integration and make sure the “Internal Email” checkbox is checked.

We strongly recommend that you don’t attach photos of identity documents to emails – safer to deliver them direct to an application or file storage.
</div>

---

## 2023-08-28 — PDF/Word section breaks

My form has many, small sections - how can I make them flow one after the other in PDF/Word output instead of starting a new page for each section?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Create a new Word document to use as a template. Go to Page Setup, and then Layout. Change "Section start" to **Continuous** instead of **New Page.** Upload this template to your integration.

[![enter image description here](/images/kb/b4e9e5296fc8462c9ac05fb3b3e16703.png)](/images/kb/b4e9e5296fc8462c9ac05fb3b3e16703.png)
</div>

---

## 2023-06-19 — How do I resize a Signature in a Word template?

How do I resize a Signature in a Word template?


---
## 1 Answers

Assuming the Tag Name of the Signature field is Signature, use the syntax &lt;&lt;Signature|500&gt;&gt;

Where the number eg. 500 is the desired width in pixels of the Signature's Image.

---

## 2023-06-14 — Hidden fields in PDF output

How do I output a hidden field in an auto generated PDF file?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
There's a few options...

Instead of using a Hidden field you could use a regular display field **inside** a Workflow element. This won't display in the regular form view, but will be included in PDF output.

You could include it in the Filename of the PDF \(especially if it's just a reference\)

You could setup a Word template for the PDF file, and use tags to display the hidden field in the header or footer.
</div>

---

## 2023-05-17 — Unique IRD Number

I need to check that each person in my form enters a unique IRD Number - how can I add validation to check that?


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Add a hidden formula element **outside** of your repeater as follows...

[![enter image description here](/images/kb/890bca8667834836a3411b6fec2423cf.png)](/images/kb/890bca8667834836a3411b6fec2423cf.png)
</div>

---

## 2023-05-14 — How can i use an expression for the recipient of an email

I need to send an email using an email address captured in my form, or if that is blank, to another default email address.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
You can use the &lt;&lt;\[Expression\]&gt;&gt; tag for the recipient of your email as follows:

&lt;&lt;\[Expression:'&lt;&lt;EmailAddress&gt;&gt;' != '' ? '&lt;&lt;EmailAddress&gt;&gt;' : 'default-email-address@formsbyair.com'\]&gt;&gt;

This assume the content of the email is the same. If you want to send a *different* email if no email address has been provided you should use multiple email integrations with conditional expressions.
</div>

---

## 2023-05-05 — Form dates in PDF

How can I include submit or approval dates in PDF output


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
1. Create a Word template for your file i.e. just a new Word document
2. Edit the **footer** of your template to include tags for the dates you want e.g. &lt;&lt;\[DocumentReceivedDateTime\]&gt;&gt; &lt;&lt;\[DocumentWorkflowDateTime:Approved\]&gt;&gt;
3. Close and save the document
4. Change your FBA integration to "PDF From Template" and upload the template you created
</div>

---

## 2023-05-02 — Google Analytics not working for embedded form

If I access my form direct then GA events are logged OK, but if I access the form through my website \(which has the form embedded\) then no events are recorded.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
You need to set cookie\_flags as follows to log events from embedded forms \(in iframe\)

gtag\('config', 'G-XXXXXXX', \{ cookie\_flags: 'max-age=7200;secure;samesite=none' \}\);
</div>

---

## 2023-05-02 — How can I track submit events for multiple forms in Google Analytics

They all come through with the "submit" event so I can't distinguish which form it is


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Setup new custom events that filter for event\_label equal to "Form Name" - then use the custom events for conversions [https://support.google.com/analytics/answer/11053454?sjid=5511550407714015213-AP#conversion_event_parameters](https://support.google.com/analytics/answer/11053454?sjid=5511550407714015213-AP#conversion_event_parameters)
</div>

---

## 2023-04-06 — Rounding issue with percents?

I'm adding multiple percentage fields in a form that should total 100% but it's not working


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
This is due to a rounding issue with floating point numbers in Javascript.

FBA stores percentages as a decimal, so 50% = 0.5

In Javascript, adding 0.7 + 0.2 + 0.1 = 0.999999999 instead of 1

As such you need to round as follows...

Math.round\(&lt;&lt;TotalPercent&gt;&gt; \* 100\) / 100

This assumes you're dealing with percentages to 0dp e.g. 50%

If you're dealing with higher precision e.g. 1dp or 50.5% then you need to implement as follows...

Math.round\(&lt;&lt;TotalPercent&gt;&gt; \* 1000\) / 1000
</div>

---

## 2023-03-28 — Minimum date validation

I want to put a minimum date in place, so user can only select T+5 days for example. I have tried putting "=DateTime.Today.AddWeekDays\(5\)" in the minimum value cell but doesnt work


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Instead of setting Min Value on your date field, use a separate hidden formula field with an Expression like this...

'&lt;&lt;StartDate&gt;&gt;' == '' || moment\('&lt;&lt;StartDate&gt;&gt;'\).isAfter\(moment\(\).add\(5, 'days'\)\)
</div>

---

## 2023-03-09 — Auto populate address from two different sources

How can I populate an address field from either an address lookup **or** a companies office lookup


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Set Default value to an expression as follows using the logical OR operator ||

'&lt;&lt;NZPost.Address1&gt;&gt;' || '&lt;&lt;Company.RegisteredAddress.Address1&gt;&gt;'

So NZPost.Address1 will be used if not blank, otherwise Company.RegisteredAddress.Address1
</div>

---

## 2023-03-06 — How do I see all of the options in the pdf if I select \"None of the above\" in a multi-select question?

If you have a multi-select option question and you want all of the options to appear in the auto generated pdf if an option like 'none of the above' is selected.


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
One option is to change these questions from "Option" to "True/False", they will then display in the pdf as shown below.

[![enter image description here](/images/kb/b1bc06495081428da3fe345ceee054bc.png)](/images/kb/b1bc06495081428da3fe345ceee054bc.png)

Another option \(if you don't want to alter the structure of the fields/form\) is to add a 'Display Content' field if 'None of the above' is selected with details of the options not chosen.

[![enter image description here](/images/kb/845b1a068fb14508b5fc825f88405d7c.png)](/images/kb/845b1a068fb14508b5fc825f88405d7c.png)
</div>

---

## 2023-02-15 — How do I use conditions in Word templates with images or complex layouts/formatting

My conditions have images and special formatting so the usual approach of &lt;&lt;\[Condition:XXX == true:My text and images\]&gt;&gt; doesn't work properly


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Use tables \(you can set the borders to be invisible\)

If the condition evaluates to **true** the table row will be retained and we’ll just remove the condition statement

If the condition evaluates to **false** then the whole row will be removed

[![enter image description here](/images/kb/75765fba6cc245559c07d0392de06453.png)](/images/kb/75765fba6cc245559c07d0392de06453.png)
</div>

---

## 2023-02-07 — How do I get the unique ID for an element in a form?

I need the ID to check against some JSON output. This element doesn't have a tag.


---
## 2 Answers

Download the XSD schema for the form by selecting Actions &gt; Versions &gt; Action &gt; Download Schema, then open the file in a code editor.

Alternatively, click **Get Help** for the element in the form designer, than grab the value for ElementId from your address bar for the Help Request form.

[![enter image description here](/images/kb/1e2abe344e0a44e0aefa0e3f714ee498.png)](/images/kb/1e2abe344e0a44e0aefa0e3f714ee498.png)

---
<div class='accepted-answer-box' markdown='1'>
Element Id now appears bottom-right when you expand an element in the form designer
</div>

---

## 2023-01-18 — Why am I not receiving form submissions on my OneDrive/Google Drive/Dropbox

Recent form submissions are not coming through to my OneDrive/Google Drive/Dropbox


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Go to Documents &gt; Log in our portal and check a recent submission - if our logs indicate that delivery was successful then this is almost certainly a synching issue between OneDrive/GoogleDrive/Dropbox and your local device. Please log in to OneDrive/GoogleDrive/Dropbox in a web browser to check. If the files exist online then check the OneDrive/GoogleDrive/Dropbox software on your device.
</div>

---

## 2023-01-17 — How can I filter the values in an Option Name/Value list based on some other value in the form

I would like to avoid having multiple Option Name/Value lists behind conditional paths


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Change your question to a Lookup, put the values in a Data Table, and use a Filter like this

table.ColumnName == &lt;&lt;SomeOtherFieldInTheForm&gt;&gt;
</div>

---

## 2023-01-17 — Can I filter data for a Lookup where the column name is a variable

For example, I want do something like this

table.'&lt;&lt;AccountType&gt;&gt;' == 1


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Just change the filter to this \(without quotes\)...

table.&lt;&lt;AccountType.Value&gt;&gt; == 1

Bear in mind…

- This will error if AccountType is blank so make sure your Lookup appears later in the form when you definitely have an AccountType
- Make sure the values for AccountType match **exactly** to column names in your table
</div>

---

## 2023-01-17 — Use two sets of data to populate a repeater

I want to know if in a repeater I can use two sets of data to populate e.g.

&lt;&lt;\[ForEach:AccountName.BeneficialOwners\]&gt;&gt; AND &lt;&lt;\[ForEach:OtherEntity.BeneficialOwners\]&gt;&gt;


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Yes that’s fine, syntax as follows…

&lt;&lt;\[ForEach:AccountName.BeneficialOwners:OtherEntity.BeneficialOwners\]&gt;&gt;
</div>

---

## 2022-12-22 — Why are dates formatting as numbers in Google Sheets?

I have mapped a date question through to Google Sheets but the value shows as a number...

[![enter image description here](/images/kb/d7da9444b49f44e597aa12c8a6fd40e2.png)](/images/kb/d7da9444b49f44e597aa12c8a6fd40e2.png)


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Just select the whole column for your date, then select Format &gt; Number &gt; Date as shown below.

This will re-format all existing values, and new values will be in the correct format as well.

[![enter image description here](/images/kb/800e8bf2f3de488690c949a902c8861b.png)](/images/kb/800e8bf2f3de488690c949a902c8861b.png)
</div>

---

## 2022-12-19 — Can I have the navigation tabs span over multiple lines?

How do I make the navigation tabs wrap to the next line?

[![enter image description here](/images/kb/2dd3e00051ca4f35806efce4feb4e090.png)](/images/kb/2dd3e00051ca4f35806efce4feb4e090.png)


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Add this script to the style section:

```
<style>   
    ul.nav-wizard {
        flex-flow: wrap;
        padding-right: 10px;
    }
</style>
```

[![enter image description here](/images/kb/64b22a1923e44634b464fb9eea30b8c0.png)](/images/kb/64b22a1923e44634b464fb9eea30b8c0.png)
</div>

---

## 2022-12-11 — Why is MBIE company validation failing?

When I click on CHECK status I see this error

```
Cannot build uri when url segment parameter(s) 'companyNumber' value is null. (Parameter 'request')
```


---
## 1 Answers

<div class='accepted-answer-box' markdown='1'>
Check these things...

- Your validation service element must have a Validation Service selected

    [![enter image description here](/images/kb/50635cf0b1b14ffeb1c4f1f9ec477b1a.png)](/images/kb/50635cf0b1b14ffeb1c4f1f9ec477b1a.png)
- You must have a Company Number element **within** the validation service element

    [![enter image description here](/images/kb/6cf89cbe70d24b89ac3ccbada298ae4a.png)](/images/kb/6cf89cbe70d24b89ac3ccbada298ae4a.png)
- Your Company Number element should be mapped to Company Number in your MBIE integration

    [![enter image description here](/images/kb/034ec337ed144687b3f097dd77ab6d1b.png)](/images/kb/034ec337ed144687b3f097dd77ab6d1b.png)
</div>

---
