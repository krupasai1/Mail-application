# Mail-application
This Python application provides a simple and intuitive graphical user interface (GUI) for sending emails. Built using the Tkinter library, it allows users to compose emails with a specified sender, recipient, subject, and body

## Prerequisites
- Python installed on your machine.
- A Gmail account.

## Steps to Use
### 1. Enable Two-Step Verification
- Go to your [Google Account Security](https://myaccount.google.com/security-checkup) settings.
- Enable "Two-Step Verification."

### 2. Generate an App Password
- Visit the [App passwords](https://myaccount.google.com/apppasswords) page.
- From the "Select app" dropdown, choose "Mail."
- From the "Select device" dropdown, choose "Other (Custom name)."
- Click "Generate."
- Copy the generated password; you'll use it in the code.

### 3. Update Code with Your Credentials
In the Python script (`mail_app.py`), replace the following placeholders:
# Replace with your actual Gmail email address
email_address = "Your Email Address"
# Replace with the App Password generated in step 2
email_password = "Your App Password of your email account"
