import speech_recognition as sr
from colorama import Fore, init

init(autoreset=True)

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300 
    r.pause_threshold = 0.8 

    try:
        with sr.Microphone() as source:
            print(Fore.CYAN + "🎧 کالیبره کردن نویز... (۱ ثانیه ساکت)")
            r.adjust_for_ambient_noise(source, duration=1)
            
            print(Fore.GREEN + "🎤 گوش می‌دهم... (فارسی حرف بزنید)")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            print(Fore.YELLOW + "⏳ پردازش...")
            text = r.recognize_google(audio, language="fa-IR")
            
            print(Fore.WHITE + f"🗣️ گفتید: {text}")
            return text.lower()
            
    except sr.WaitTimeoutError:
        print(Fore.RED + "❌ تایم‌اوت (صدایی نیامد).")
        return None
    except sr.UnknownValueError:
        print(Fore.RED + "❌ نامفهوم بود.")
        return None
    except sr.RequestError:
        print(Fore.RED + "❌ خطای اینترنت.")
        return None
    except Exception as e:
        print(Fore.RED + f"❌ ارور ناشناخته: {e}")
        return None

if __name__ == "__main__":
    while True:
        res = listen()
        if res and "exit" in res:
            break