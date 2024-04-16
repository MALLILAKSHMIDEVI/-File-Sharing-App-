import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class FileSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sharing App")
        self.root.geometry("600x400")  # Adjusted window size
        
        self.username = None
        
        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)
        
        # Username Label and Entry
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Password Label and Entry
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Login Button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def login(self):
        self.username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Implement your authentication logic here
        # For simplicity, let's assume username and password are 'admin'
        if self.username == 'admin' and password == 'admin':
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_main_menu(self):
        # Destroy login frame and show main menu
        self.login_frame.destroy()

        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack(padx=20, pady=20)

        # File Upload Button
        self.upload_button = tk.Button(self.main_menu_frame, text="Upload File", command=self.upload_file)
        self.upload_button.grid(row=0, column=0, padx=5, pady=5)

        # File Download Button
        self.download_button = tk.Button(self.main_menu_frame, text="Download File", command=self.download_file)
        self.download_button.grid(row=0, column=1, padx=5, pady=5)

    def upload_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File to Upload")
        if filename:
            # Implement file upload logic here
            messagebox.showinfo("Upload Successful", "File uploaded successfully")

    def download_file(self):
        # Implement file download logic here
        messagebox.showinfo("Download Successful", "File downloaded successfully")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSharingApp(root)
    root.mainloop()
