import customtkinter as ctk
import time
import threading

class StopwatchApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch")
        self.geometry("500x600")
        self.resizable(True, True)  # Make window resizable
        
        # Set dark theme as default
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#1a1a1a")
        
        # Initialize variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.laps = []
        self.theme_mode = "dark"
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = ctk.CTkLabel(
            self,
            text="Stopwatch",
            font=("Arial", 32, "bold"),
            text_color="#FFFFFF"
        )
        title_label.grid(row=0, column=0, pady=(30, 20))
        
        # Theme toggle button
        self.theme_button = ctk.CTkButton(
            self,
            text="☀️",
            width=50,
            height=35,
            font=("Arial", 18),
            command=self.toggle_theme
        )
        self.theme_button.place(relx=0.95, rely=0.05, anchor="ne")
        
        # Time display frame
        time_frame = ctk.CTkFrame(self, fg_color="transparent")
        time_frame.grid(row=1, column=0, pady=20, sticky="ew")
        time_frame.grid_columnconfigure(0, weight=1)
        
        # Time display
        self.time_label = ctk.CTkLabel(
            time_frame,
            text="00:00:00.000",
            font=("Arial", 48, "bold"),
            text_color="#00FF00"  # Green color for time
        )
        self.time_label.grid(row=0, column=0, pady=20)
        
        # Control buttons frame
        controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        controls_frame.grid(row=2, column=0, pady=20, sticky="ew")
        controls_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # Start/Pause button
        self.start_button = ctk.CTkButton(
            controls_frame,
            text="Start",
            font=("Arial", 16, "bold"),
            width=100,
            height=40,
            command=self.start_stop,
            fg_color="#28a745",  # Green
            hover_color="#218838"
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Reset button
        self.reset_button = ctk.CTkButton(
            controls_frame,
            text="Reset",
            font=("Arial", 16, "bold"),
            width=100,
            height=40,
            command=self.reset,
            fg_color="#dc3545",  # Red
            hover_color="#c82333"
        )
        self.reset_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Lap button
        self.lap_button = ctk.CTkButton(
            controls_frame,
            text="Lap",
            font=("Arial", 16, "bold"),
            width=100,
            height=40,
            command=self.add_lap,
            fg_color="#007bff",  # Blue
            hover_color="#0056b3"
        )
        self.lap_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Clear Laps button
        self.clear_laps_button = ctk.CTkButton(
            controls_frame,
            text="Clear",
            font=("Arial", 16, "bold"),
            width=100,
            height=40,
            command=self.clear_laps,
            fg_color="#6c757d",  # Gray
            hover_color="#545b62"
        )
        self.clear_laps_button.grid(row=0, column=3, padx=10, pady=10)
        
        # Laps frame
        laps_frame = ctk.CTkFrame(self)
        laps_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        laps_frame.grid_columnconfigure(0, weight=1)
        laps_frame.grid_rowconfigure(1, weight=1)
        
        # Laps title
        laps_title = ctk.CTkLabel(
            laps_frame,
            text="Laps",
            font=("Arial", 20, "bold"),
            text_color="#FFFFFF"
        )
        laps_title.grid(row=0, column=0, pady=(15, 10))
        
        # Laps scrollable frame
        self.laps_scrollable = ctk.CTkScrollableFrame(
            laps_frame,
            width=400,
            height=200
        )
        self.laps_scrollable.grid(row=1, column=0, padx=10, pady=(0, 15), sticky="nsew")
        
        # Start the update loop
        self.update_time()
        
    def start_stop(self):
        if not self.running:
            # Start the stopwatch
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.configure(text="Pause", fg_color="#ffc107", hover_color="#e0a800")  # Yellow
        else:
            # Pause the stopwatch
            self.running = False
            self.elapsed_time = time.time() - self.start_time
            self.start_button.configure(text="Start", fg_color="#28a745", hover_color="#218838")  # Green
            
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.start_button.configure(text="Start", fg_color="#28a745", hover_color="#218838")
        self.time_label.configure(text="00:00:00.000")
        
    def add_lap(self):
        if self.running or self.elapsed_time > 0:
            current_time = self.get_current_time()
            lap_number = len(self.laps) + 1
            
            # Calculate lap time
            if self.laps:
                lap_time = current_time - self.laps[-1]["total_time"]
            else:
                lap_time = current_time
                
            lap_info = {
                "lap_number": lap_number,
                "lap_time": lap_time,
                "total_time": current_time
            }
            
            self.laps.append(lap_info)
            self.update_laps_display()
            
    def clear_laps(self):
        self.laps.clear()
        self.update_laps_display()
        
    def get_current_time(self):
        if self.running:
            return time.time() - self.start_time
        else:
            return self.elapsed_time
            
    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = seconds % 60
        milliseconds = int((seconds % 1) * 1000)
        seconds = int(seconds)
        
        return f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
        
    def update_time(self):
        if self.running:
            current_time = self.get_current_time()
            self.time_label.configure(text=self.format_time(current_time))
            
        # Schedule next update
        self.after(10, self.update_time)  # Update every 10ms for smooth milliseconds
        
    def update_laps_display(self):
        # Clear existing lap widgets
        for widget in self.laps_scrollable.winfo_children():
            widget.destroy()
            
        # Add lap widgets
        for lap in self.laps:
            lap_frame = ctk.CTkFrame(self.laps_scrollable)
            lap_frame.pack(fill="x", padx=5, pady=2)
            
            # Lap number
            lap_number_label = ctk.CTkLabel(
                lap_frame,
                text=f"Lap {lap['lap_number']}",
                font=("Arial", 12, "bold"),
                width=80
            )
            lap_number_label.pack(side="left", padx=10, pady=5)
            
            # Lap time
            lap_time_label = ctk.CTkLabel(
                lap_frame,
                text=self.format_time(lap['lap_time']),
                font=("Arial", 12),
                width=120
            )
            lap_time_label.pack(side="left", padx=10, pady=5)
            
            # Total time
            total_time_label = ctk.CTkLabel(
                lap_frame,
                text=self.format_time(lap['total_time']),
                font=("Arial", 12),
                width=120
            )
            total_time_label.pack(side="left", padx=10, pady=5)
            
    def toggle_theme(self):
        if self.theme_mode == "dark":
            self.theme_mode = "light"
            self.theme_button.configure(text="🌙")
            ctk.set_appearance_mode("light")
            self.configure(fg_color="#f8f9fa")
            # Update title color
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "Stopwatch":
                    widget.configure(text_color="#000000")
        else:
            self.theme_mode = "dark"
            self.theme_button.configure(text="☀️")
            ctk.set_appearance_mode("dark")
            self.configure(fg_color="#1a1a1a")
            # Update title color
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "Stopwatch":
                    widget.configure(text_color="#FFFFFF")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = StopwatchApp()
    app.protocol("WM_DELETE_WINDOW", app.quit)
    app.mainloop() 
