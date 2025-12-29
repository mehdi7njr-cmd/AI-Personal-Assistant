import edge_tts
import pygame
import asyncio
import os
from colorama import Fore, init

init(autoreset=True)

VOICE = "fa-IR-DilaraNeural"

async def generate_audio(text, output_file="speech.mp3"):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

def speak(text):
    if not text: return
    print(f"🔊 جارویس: {text}")
    filename = "temp_speech.mp3"

    try:
        asyncio.run(generate_audio(text, filename))
    except Exception as e:
        print(Fore.RED + f"❌ خطای تولید صدا: {e}")
        return
    
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        pygame.mixer.quit()

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print(Fore.RED + f"❌ خطای پخش: {e}")

if __name__ == "__main__":
    speak("سلام قربان. سیستم‌های من آماده است")