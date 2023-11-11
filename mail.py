import tkinter as tk
from tkinter import Text, ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailApp:
    def __init__(self, root):
        self.root = root
        root.title("Mail Application")

        # Variables for storing user input
        self.from_var = tk.StringVar()
        self.to_var = tk.StringVar()
        self.subject_var = tk.StringVar()
        self.body_text = None

        # Create the UI
        self.create_ui()

    def create_ui(self):
        # From
        ttk.Label(self.root, text="From:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.from_var).grid(row=0, column=1, pady=5)

        # To
        ttk.Label(self.root, text="To:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.to_var).grid(row=1, column=1, pady=5)

        # Subject
        ttk.Label(self.root, text="Subject:").grid(row=2, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.subject_var).grid(row=2, column=1, pady=5)

        # Body
        ttk.Label(self.root, text="Body:").grid(row=3, column=0, sticky="w")
        self.body_text = Text(self.root, height=10, width=40, wrap=tk.WORD, 
                              font=("Helvetica", 10), 
                              padx=5, pady=5,
                              bg="white",
                              fg="black")
        self.body_text.grid(row=3, column=1, pady=5)

        # Send button
        ttk.Button(self.root, text="Send", command=self.send_mail).grid(row=4, column=0, columnspan=2, pady=10)

    def send_mail(self):
        # Get email data from the UI
        from_address = self.from_var.get()
        to_address = self.to_var.get()
        subject = self.subject_var.get()
        body = self.body_text.get("1.0", tk.END)

        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = from_address
        message["To"] = to_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # TODO: Replace these placeholders with your actual email credentials
        email_address = "Your Email Address"   
        email_password = "Your App password of ur email account"

        # Connect to the SMTP server and send the email
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(email_address, email_password)
            server.sendmail(from_address, to_address, message.as_string())
            server.quit()

            messagebox.showinfo("Success", "Email Sent!")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    mail_app = MailApp(root)
    root.mainloop()

