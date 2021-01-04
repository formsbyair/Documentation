---
title: Nested tags in javascript
type: platform
---

Nested tags are now supported in client-side javascript expressions using the number of &lt;&lt;&gt;&gt;'s to indicate depth.

This is particuarly useful for array functions with JSON data from a Data Source element, for example:

&lt;&lt;&lt;CustomerData.Orders.filter(function(order) { return &apos;<<SelectedProductCode>>&apos;.indexOf(order.ProductCodes) >= 0 })[0].ProductCode&gt;&gt;&gt;

The outer tag for CustomerData has 3 &lt;&lt;&lt;&gt;&gt;&gt;'s whereas the inner tag for SelectedProductCode has 2 &lt;&lt;&gt;&gt;