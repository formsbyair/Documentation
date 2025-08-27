---
title: Country Risk Rating
type: platform
---

In order to support AML/CFT requirements for risk rating, we've added a new **Risk** property to our shared **Country** data table.

This property is a number from 0 - 10 where 10 is high risk, and is based on the Basel AML Index published annually here <https://index.baselgovernance.org/>

Any form that uses our Country data table for address can now use this property to help risk-rate new clients, for example:

&lt;&lt;Country.Risk&gt;&gt; &gt; 5 ? 'High Risk Country' : 'Low Risk Country'