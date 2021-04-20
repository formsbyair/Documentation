---
title: Types > Display Content
category: Questions
order: 5
---

Display static text and images in a form

#### Basic formatting

Use the toolbar in **Editor** view to make text Bold/Italic/Underline, and insert hyperlinks and images.

Image URLs must point to existing images on the internet, you can't upload custom images via our portal or API currently.

Hyperlinks and images can be edited by clicking on them and using the popup toolbar.

#### Bullet points and numbering

Use the following markdown-based syntax for bullet points and numbered lists. This will ensure they are formatted correctly in your form and output documents. 

\*(space)My bullet point  
(space)(space)\*(space)My indented bullet point  

1.(space)My numbered point  
b.(space)My numbered point  
iii.(space)My numbered point  
(space)(space)1.(space)My indented numbered point

HTML tags &lt;ul&gt; &lt;ol&gt; may render OK in your form but won't be translated correctly in output documents.

#### Advanced formatting

To apply custom formatting to Display Content, select the Style tab in the form designer and define a custom CSS class, for example:

&lt;style&gt;  
.my-class {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;color: red;  
}  
&lt;style&gt;

Then use the **HTML** view for your Display Content to add a span including class name containing your text as follows:

&lt;span class=&quot;my-class&quot;&gt;My text&lt;/span&gt;


Advanced formatting or any HTML tags apart from those used for Basic formatting will not be rendered in output documents.