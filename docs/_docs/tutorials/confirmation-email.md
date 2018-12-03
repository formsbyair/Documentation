---
title: Setup a confirmation email
category: Tutorials
order: 2
---

> Topics - email integration, email template

Previous tutorial, [Build a form]({{ site.baseurl }}/tutorials/build-form)

Follow the steps in the slideshow below to setup a confirmation email

<div class="flexslider">
	<ul class="slides">	  				
		{% for image in site.static_files %}	
			{% if image.path contains 'images/confirmation-email' %}
			<li>
				<img src="{{ site.baseurl }}{{ image.path }}" />	
			</li>
			{% endif %}
		{% endfor %}		
	</ul>
</div>

Next up, [Setup PDF Delivery]({{ site.baseurl }}/tutorials/pdf-delivery)


