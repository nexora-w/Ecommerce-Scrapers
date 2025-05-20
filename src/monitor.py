import threading
import time
from pynput import mouse, keyboard
from signals import Signals

class InactivityMonitor:
    def __init__(self, timeout=60):
        self.timeout = timeout
        self.last_activity = time.time()
        self.is_running = True
        self.signals = Signals()
        
        self.mouse_listener = mouse.Listener(on_move=self.on_activity, 
                                           on_click=self.on_activity, 
                                           on_scroll=self.on_activity)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_activity, 
                                                 on_release=self.on_activity)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        
        self.monitor_thread = threading.Thread(target=self.monitor_activity, daemon=True)
        self.monitor_thread.start()
    
    def on_activity(self, *args, **kwargs):
        self.last_activity = time.time()
    
    def monitor_activity(self):
        while self.is_running:
            current_time = time.time()
            if current_time - self.last_activity > self.timeout:
                self.signals.inactivity_detected.emit()
                self.last_activity = time.time()
            time.sleep(3)
    
    def stop(self):
        self.is_running = False
        self.mouse_listener.stop()
        self.keyboard_listener.stop()