---
title: Types > Display Content
category: Questions
order: 6
---

Display static text and images in a form

#### Basic formatting

Use the toolbar in **Editor** view to make text Bold/Italic/Underline, and insert hyperlinks and images.

Images and hyperlinks can point to existing files on the internet, or an asset that's been uploaded for a form.

Hyperlinks and images can be edited by clicking on them and using the popup toolbar.

#### Bullet points and numbering

Use the following markdown-based syntax for bullet points and numbered lists. This will ensure they are formatted correctly both in your form and auto-generated output documents. 

\*(space)My bullet point  
(space)(space)\*(space)My indented bullet point  
(space)(space)(space)(space)\*(space)My second level indented bullet point  

1.(space)My numbered point  
b.(space)My numbered point  
iii.(space)My numbered point  
(space)(space)1.(space)My indented numbered point  
(space)(space)(space)(space)a.(space)My second level indented numbered point  

List items can be indented up to 5 levels.

HTML tags &lt;ul&gt; &lt;ol&gt; may render OK in your form but won't be translated correctly in auto-generated output documents.

#### Advanced formatting

To apply custom formatting to Display Content, select the Style tab in the form designer and define a custom CSS class, for example:

&lt;style&gt;  
.my-class {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;color: red;  
}  
&lt;style&gt;

Then set **CSS Class** for your Display Content element to the name of your class e.g. my-class

Advanced formatting or any HTML tags apart from those used for Basic formatting will not be rendered in auto-generated output documents.