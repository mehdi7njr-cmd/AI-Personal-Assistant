import customtkinter as ctk
import threading
import time
import winsound
import ears
import brain
import mouth
import skills
import wakeword

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class JarvisGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("JARVIS AI Assistant")
        self.geometry("400x700")
        self.resizable(False, False)
        
        self.manual_trigger = False
        self.was_manual_wake = False

        self.chat_frame = ctk.CTkScrollableFrame(self, width=380, height=530)
        self.chat_frame.pack(pady=10, padx=10)

        self.status_frame = ctk.CTkFrame(self, height=120, fg_color="transparent")
        self.status_frame.pack(fill="x", side="bottom", pady=10)

        self.mic_btn = ctk.CTkButton(
            self.status_frame,
            text="🎤",
            font=("Arial", 30),
            width=80,
            height=80,
            corner_radius=40,
            fg_color="#1f6aa5",
            hover_color="#154c79",
            command=self.on_mic_click
        )
        self.mic_btn.pack(pady=5)

        self.status_label = ctk.CTkLabel(self.status_frame, text="سیستم آنلاین. منتظر صدا زدن...", text_color="gray")
        self.status_label.pack()

        self.running = True
        threading.Thread(target=self.jarvis_logic, daemon=True).start()

    def on_mic_click(self):
        """وقتی دکمه زده شد"""
        if not self.manual_trigger:
            self.manual_trigger = True
            self.was_manual_wake = True 
            self.update_status("دکمه فشرده شد...", "#1f6aa5")

    def check_manual_wake(self):
        """چک کردن وضعیت دکمه توسط wakeword"""
        if self.manual_trigger:
            self.manual_trigger = False
            return True
        return False

    def add_message(self, text, sender="user"):
        if sender == "user":
            align = "e"
            color = "#2b2b2b"
            txt_color = "white"
        else:
            align = "w"
            color = "#004D40"
            txt_color = "cyan"

        msg_label = ctk.CTkLabel(
            self.chat_frame, 
            text=text, 
            font=("Arial", 14),
            fg_color=color,
            text_color=txt_color,
            corner_radius=10,
            wraplength=250,
            padx=10, pady=10
        )
        msg_label.pack(anchor=align, pady=5, padx=5)
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    def update_status(self, text, color="#1f6aa5"):
        self.status_label.configure(text=text)
        self.mic_btn.configure(fg_color=color)

    def play_system_beep(self):
        """پخش صدای بیپ کوتاه"""
        try:
            winsound.Beep(800, 150)
        except:
            pass

    def jarvis_logic(self):
        time.sleep(1)
        
        while self.running:
            try:
                self.update_status("منتظر کلمه Jarvis...", "#333333")
                
                try:
                    is_waked = wakeword.wait_for_keyword(manual_check_callback=self.check_manual_wake)
                except Exception as e:
                    print(f"Wake Error: {e}")
                    time.sleep(1)
                    continue

                if is_waked:
                    self.update_status("بیدار شدم! بگو...", "#c62828")
                    if self.was_manual_wake:
                        self.play_system_beep()
                        self.was_manual_wake = False
                    else:
                        mouth.speak("جانم")
                    user_text = ears.listen()
                    
                    if user_text:
                        self.add_message(user_text, "user")
                        self.update_status("در حال پردازش...", "#6a1b9a")
                        
                        if skills.execute_command_logic(user_text):
                            self.add_message("دستور اجرا شد.", "bot")
                        else:
                            ai_response = brain.think(user_text)
                            self.add_message(ai_response, "bot")
                            mouth.speak(ai_response)
                    else:
                        self.update_status("چیزی نشنیدم.", "#ff9800")
                    
                    time.sleep(1)
                    
            except Exception as e:
                print(f"Logic Error: {e}")
                time.sleep(1)

if __name__ == "__main__":
    app = JarvisGUI()
    app.mainloop()