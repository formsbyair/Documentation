---
title: Build a form
category: Tutorials
order: 1
---

Follow the steps in the slideshow below to build a simple form

<div class="flexslider">
	<ul class="slides">	  				
		{% for image in site.static_files %}	
			{% if image.path contains 'images/build-form' %}
			<li>
				<img src="{{ site.baseurl }}{{ image.path }}" />	
			</li>
			{% endif %}
		{% endfor %}		
	</ul>
</div>

Next up, [Setup a confirmation email]({{ site.baseurl }}/tutorials/confirmation-email)
