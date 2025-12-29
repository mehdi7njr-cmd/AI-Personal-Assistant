import wakeword
import ears
import brain
import mouth
import skills
import ui
import time
import winsound

def play_wake_sound():
    try:
        winsound.Beep(1000, 200)
    except:
        pass

def main():
    ui.startup_banner()
    mouth.speak("سیستم آنلاین شد.")
    
    while True:
        ui.print_status("[zzz] منتظر کلمه بیدارباش...", style="dim white")
        
        is_waked = False
        try:
            is_waked = wakeword.wait_for_keyword()
        except:
            pass

        if is_waked:
            play_wake_sound()
            ui.print_status("!بیدار شدم", style="bold cyan")
            mouth.speak("[جانم؟]")
            
            while True:
                ui.print_status("گوش می‌دهم...", style="yellow")
                user_text = ears.listen()
                
                if user_text:
                    ui.print_user_input(user_text)
                    
                    if "خداحافظ" in user_text or "بخواب" in user_text:
                        mouth.speak("فعلا خداحافظ.")
                        break
                    
                    if skills.execute_command_logic(user_text):
                        continue 
                    
                    ui.print_status("در حال فکر کردن...", style="magenta")
                    ai_response = brain.think(user_text)
                    ui.print_ai_response(ai_response)
                    mouth.speak(ai_response)
                        
                else:
                    ui.print_status("سکوت تشخیص داده شد. بازگشت به خواب.", style="dim red")
                    break 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped.")