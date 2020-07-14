---
title: Boolean/Option Tag Values
type: platform
---

Tags for **True/False** and **Option** type questions are evaluated as follows:

|Tag|Result In Form|Result Everywhere Else|
|&lt;&lt;MyTrueFalseQuestion&gt;&gt;|true or false|Yes or No|
|&lt;&lt;MyOption&gt;&gt;|true or false|Text for the Prompt or &lt;blank&gt;|

The intent is to display a user-friendly value for these questions by default, however this can lead to confusion when you want to reference them in expressions.

To make it more explicit, you can now use the **Value** tag property to refer to the underlying value for true/false or option questions.

|Expression Using Value Property|Equivalent To|
|'&lt;&lt;MyTrueFalseQuestion.Value&gt;&gt;' == 'true'|'&lt;&lt;MyTrueFalseQuestion&gt;&gt;' == 'Yes'|
|'&lt;&lt;MyOption.Value&gt;&gt;' == 'true'|'&lt;&lt;MyOption&gt;&gt;' != ''|