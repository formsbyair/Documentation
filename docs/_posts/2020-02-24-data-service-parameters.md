---
title: Data service parameters
type: feature
---

Added new **Parameters** property for Data Service elements to pass form data to a service instead of querystring values.

Parameters are defined in querystring syntax, and can reference form data with &lt;&lt;tags&gt;&gt;, for example

category=<<Category>>&amount=<<Amount>>

You can reference these parameters in a REST API integration endpoint as follows

https://sampleservice/api/v1/categories/{category}/products?amount={amount}