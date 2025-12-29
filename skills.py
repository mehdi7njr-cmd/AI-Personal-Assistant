import pyautogui
import psutil
import pywhatkit
import datetime
import requests
import mouth

CITY_URL = "Kashan"
CITY_NAME = "کاشان"

def get_time():
    now = datetime.datetime.now().strftime("%H:%M")
    mouth.speak(f"{now} است")

def get_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    mouth.speak("امروز یک روز خوب است")

def system_stats():
    battery = psutil.sensors_battery()
    percentage = battery.percent

    cpu = psutil.cpu_percent(interval=1)

    mouth.speak(f"شارژ باتری {percent} درصد است. مصرف CPU {percent} درصد است.")

    if percentage < 20 and not battery.power_plugged:
        mouth.speak("اخطار. باتری کم است. به شارژ بزنید.")

def take_screenshot():
    mouth.speak("اسکرین‌شات گرفتم.")
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    pyautogui.screenshot(f"screenshot_{timestamp}.png")

def play_youtube(topic):
    mouth.speak(f"در حال پخش {topic} در یوتیوب")
    pywhatkit.playonyt(topic)

def get_weather():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        url = f"https://wttr.in/{CITY_URL}?format=%t"
        res = requests.get(url, headers=headers)
        
        if res.status_code == 200:
            temp = res.text.strip()
            temp = temp.replace("+", "مثبت ")
            mouth.speak(f"دمای هوای {CITY_NAME}، {temp} است")
        else:
            mouth.speak("متاسفانه نتوانستم اطلاعات هوا را بگیرم")
            
    except Exception as e:
        print(e)
        mouth.speak("خطا در اتصال به سرور آب و هوا")

def control_volume(command):
    if "قطع صدا" in command or "ساکت" in command:
        pyautogui.press("volumemute")
        mouth.speak("صدا قطع شد")
    elif "زیاد" in command:
        for _ in range(5): pyautogui.press("volumeup")
        mouth.speak("صدا زیاد شد")
    elif "کم" in command:
        for _ in range(5): pyautogui.press("volumedown")
        mouth.speak("صدا کم شد")

def minimize_windows():
    pyautogui.hotkey('win', 'd')
    mouth.speak("دسکتاپ نمایش داده شد")

def execute_command_logic(command):
    if "پلی کن" in command or "آهنگ" in command:
        topic = command.replace("پلی کن", "").replace("آهنگ", "").strip()
        play_youtube(topic)
        return True
    
    elif "باتری" in command or "سیستم" in command:
        system_stats()
        return True
    
    elif "عکس" in command or "شات" in command:
        take_screenshot()
        return True
    
    elif "هوا" in command or "دما" in command:
        get_weather()
        return True
        
    elif "صدا" in command:
        control_volume(command)
        return True
        
    elif "پنهان" in command or "خلوت" in command:
        minimize_windows()
        return True
        
    elif "ساعت" in command or "زمان" in command:
        get_time()
        return True
        
    return False
