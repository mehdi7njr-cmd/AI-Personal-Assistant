import pvporcupine
from pvrecorder import PvRecorder
import os

ACCESS_KEY = "YOUR_API_KEY_HERE"

def wait_for_keyword(manual_check_callback=None):
    """
    manual_check_callback: تابعی که اگر True برگرداند، یعنی دکمه فشرده شده
    """
    if not ACCESS_KEY or "YOUR_ACCESS_KEY" in ACCESS_KEY:
        print("Error: No Access Key")
        return False

    porcupine = None
    recorder = None
    
    try:
        porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=["jarvis"])
        recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
        recorder.start()
        
        while True:
            if manual_check_callback and manual_check_callback():
                return True

            pcm = recorder.read()
            result = porcupine.process(pcm)
            
            if result >= 0:
                return True
                
    except Exception as e:
        print(f"Wakeword Error: {e}")
        return False
        
    finally:
        if recorder is not None:
            recorder.stop()
            recorder.delete()
        if porcupine is not None:
            porcupine.delete()