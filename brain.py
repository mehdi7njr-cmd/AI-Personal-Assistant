import google.generativeai as genai
from colorama import Fore, init

init(autoreset=True)

API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')
chat_session = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["تو جارویس هستی. یک دستیار هوشمند، شوخ‌طبع و بامزه. جواب‌هایت باید فارسی، کوتاه و با لحن صمیمی و دوستانه باشد. گاهی از ایموجی استفاده کن."]
    },
    {
        "role": "model",
        "parts": ["ای جان! مخلصیم. بگو چه خبر؟ 😉"]
    }
])


def think(user_text):
    try:
        print(Fore.MAGENTA + "🧠 ...")        
        response = chat_session.send_message(user_text)
        ai_text = response.text.strip()
        ai_text = ai_text.replace("*", "") 
        return ai_text
        
    except Exception as e:
        return "متاسفانه مشکلی در پردازش پیش آمد"

if __name__ == "__main__":
    while True:
        text = input("شما: ")
        if text == "exit": break
        think(text)