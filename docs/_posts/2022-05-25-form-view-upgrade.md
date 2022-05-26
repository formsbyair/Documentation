---
title: Form View Upgrade
type: platform
---

As part of our mission to always provide the best online forms experience, we are announcing an upgrade to our form view engine to incorporate the very latest web technologies.

Your forms will look and behave almost exactly the same as they do today, they'll just be a little sharper, faster and even more secure.

A big part of the efficiency and performance improvements come from us being able to leverage functionality now built-in to modern web browsers like Chrome, Edge, Safari & Firefox, but it does mean we'll need to end support for all versions of Internet Explorer.

Microsoft has been phasing out IE in favour of Edge for some time. It's currently running at ~0.5% global use, and will be officially retired by Microsoft on 15 June 2022. Any users that do access your forms with IE will be presented with the following message:

* Our forms require a modern web browser to run.
* Internet Explorer has been retired by Microsoft, please upgrade using the link below.
* [Get Started with Microsoft Edge](https://go.microsoft.com/fwlink/?linkid=2192466)

We're planning to execute this upgrade in two phases beginning Wednesday 1st June 2022. You will receive more details about the process via email.

Here is a summary of the technical changes in our form view upgrade:

* Upgrade from AngularJS 1.8.2 to [Angular 13.3.9](https://angular.io/)
* Upgrade from Bootstrap 3.4.1 to [Bootstrap 5.1.3](https://getbootstrap.com/)
* Upgrade from Angular UI Bootstrap 2.5.0 to [Angular Bootstrap 12.1.2](https://ng-bootstrap.github.io/#/home)
* Drop support for all versions of Internet Explorer
* Default font size has been increased by 1pt for desktop and mobile view
* Removed drop-shadow from form border
* Improved Date Picker
* Slight colour change to buttons (unless overridden with custom styling)
* Slimmer progress bar
* New "outline style" icons for warning & validation messages