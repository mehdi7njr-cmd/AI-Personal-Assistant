from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import datetime

console = Console()

def startup_banner():
    """چاپ لوگوی شروع"""
    console.clear()
    logo = """
       ██  █████  ██████  ██    ██ ██ ███████ 
       ██ ██   ██ ██   ██ ██    ██ ██ ██      
       ██ ███████ ██████  ██    ██ ██ ███████ 
  ██   ██ ██   ██ ██   ██  ██  ██  ██      ██ 
   █████  ██   ██ ██   ██   ████   ██ ███████ 
    """
    console.print(Panel(Align.center(logo, vertical="middle"),
                        title="[bold cyan]AI ASSISTANT SYSTEM[/bold cyan]",
                        subtitle="[green]Online[/green]",
                        border_style="cyan"))
def print_status(text, style="white"):
    """چاپ وضعیت سیستم (مثل: گوش می‌دهم...)"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    console.print(f"[{timestamp}] {text}", style=style)

def print_ai_response(text):
    """چاپ جواب جارویس در کادر بنفش"""
    console.print(Panel(text, title="[bold magenta]JARVIS[/bold magenta]", border_style="magenta"))

def print_user_input(text):
    """چاپ حرف کاربر در کادر سبز"""
    console.print(Panel(text, title="[bold green]USER[/bold green]", border_style="green", expand=False))