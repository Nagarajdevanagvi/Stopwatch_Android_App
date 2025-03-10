import customtkinter as ctk
import time

class ModernStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Stopwatch")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Set dark mode theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Stopwatch Variables
        self.start_time = None
        self.running = False

        # Title Label
        self.title_label = ctk.CTkLabel(root, text="Stopwatch", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Stopwatch Time Display
        self.label = ctk.CTkLabel(root, text="00:00.00", font=("Arial", 50, "bold"), text_color="cyan")
        self.label.pack(pady=20)

        # Button Frame with Equal Size Buttons
        button_frame = ctk.CTkFrame(root)
        button_frame.pack(pady=10, padx=20, fill="x")

        # Configure grid layout for equal button sizing
        button_frame.columnconfigure((0, 1, 2), weight=1)

        # Start Button
        self.start_button = ctk.CTkButton(button_frame, text="Start", command=self.start, fg_color="green", hover_color="darkgreen")
        self.start_button.grid(row=0, column=0, padx=5, sticky="ew")

        # Pause Button
        self.pause_button = ctk.CTkButton(button_frame, text="Pause", command=self.pause, fg_color="orange", hover_color="darkorange")
        self.pause_button.grid(row=0, column=1, padx=5, sticky="ew")

        # Reset Button
        self.reset_button = ctk.CTkButton(button_frame, text="Reset", command=self.reset, fg_color="red", hover_color="darkred")
        self.reset_button.grid(row=0, column=2, padx=5, sticky="ew")

        # Update Timer Continuously
        self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time % 1) * 100)
            self.label.configure(text=f"{minutes:02}:{seconds:02}.{milliseconds:02}")
        self.root.after(10, self.update_timer)

    def start(self):
        if not self.running:
            self.start_time = time.time() - (self.start_time or 0)
            self.running = True

    def pause(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = None
        self.label.configure(text="00:00.00")

# Run the Application
root = ctk.CTk()
stopwatch = ModernStopwatch(root)
root.mainloop()
