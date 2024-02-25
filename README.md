# Django Email Authentication

A simple implementation of email authentication which include sign-in, sign-up and sign-out views in the account app.

## Usage instructions
In the following steps, I assume that your main app is called "main", you don't have an account app, your base template is called "base.html" and your project uses the bootstrap5 plugin.
 1. Copy the "accounts" folder to your Django project.
 2. Copy the "static" folder to your Django project. If you already have an "static" folder or the "static/css/styles.css" file already exists, add the content to the final css file.
 3. Copy the "main/tools" file to your "main" app folder.
 4. In the urls.py of your main app, add the element "path('accounts/', include('accounts.urls'))" in the urlpatterns list.
 5. Add the "accounts" app in the "INSTALLED_APPS" list of your settings file.
 6. Add the following variables at the end of your settings file:
    * AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']
    * AUTH_USER_MODEL = 'accounts.User'