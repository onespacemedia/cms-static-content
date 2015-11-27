# onespacemedia-cms-static-content

Allow admin users to add static content pages to the CMS.

## Installation

Add `'static'` to your `INSTALLED_APPS`

Add `'static.middleware.StaticContentMiddleware'` to your `MIDDLEWARE_CLASSES`

Run `./manage.py migrate`
