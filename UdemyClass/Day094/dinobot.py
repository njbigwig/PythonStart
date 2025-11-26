# import pyautogui
# from PIL import ImageGrab, ImageTk, Image
# from pynput import mouse
# from PIL import ImageDraw
# import time
# import tkinter as tk
# import threading

# pip install pyautogui
# pip install pillow
# pip install pynput
# pip install numpy



import time
import sys
import threading
from PIL import Image, ImageTk
import pyautogui
import numpy as np
import tkinter as tk

# ---------- CONFIG (tweak if needed) ----------
JUMP_KEY = 'space'         # or 'up'
SCAN_INTERVAL = 0.02       # seconds between checks
DARK_PIXEL = 120           # pixel value <= this counts as obstacle (0-255)
TRIGGER_RATIO = 0.02       # fraction of dark pixels that triggers a jump
COOLDOWN = 0.45            # seconds after a jump before next jump
KERNEL_SIZE = 1            # dilation kernel radius (1 disables)
PREVIEW_SCALE = 3          # scale preview window to see region
# ------------------------------------------------

state = {
    'region': None,
    'running': False,
    'last_jump': 0,
    'stop': False,
    'debug': True
}

def grab_region_img(region):
    left, top, w, h = region
    return pyautogui.screenshot(region=(left, top, w, h))

def to_gray_array(pil_img):
    return np.asarray(pil_img.convert('L'))

def detect_obstacle(arr_gray):
    dark_mask = arr_gray <= DARK_PIXEL
    dark_count = dark_mask.sum()
    total = dark_mask.size
    ratio = dark_count / total
    return ratio, dark_count, total, dark_mask

def jump():
    pyautogui.keyDown(JUMP_KEY)
    time.sleep(0.06)
    pyautogui.keyUp(JUMP_KEY)

def bot_loop():
    while not state['stop']:
        if not state['region'] or not state['running']:
            time.sleep(0.05)
            continue
        img = grab_region_img(state['region'])
        arr = to_gray_array(img)
        ratio, dark_count, total, mask = detect_obstacle(arr)
        now = time.time()
        print(f"\rratio={ratio:.4f} dark={dark_count}/{total}", end='', flush=True)
        if ratio >= TRIGGER_RATIO and (now - state['last_jump']) > COOLDOWN:
            state['last_jump'] = now
            jump()
        time.sleep(SCAN_INTERVAL)
    print("\nBot loop exiting.")

# ---------- Simple keyboard-based calibration UI ----------
def start_tk():
    root = tk.Tk()
    root.title("T‑Rex Bot — Calibration / Preview (Press Enter in terminal)")

    tk.Label(root, text="Calibration: Move your mouse to TOP-LEFT and press Enter in the terminal.\nThen move to BOTTOM-RIGHT and press Enter.\nUse Start to run the bot. Close window to exit.").pack(padx=8, pady=6)

    canvas = tk.Canvas(root, width=400, height=200, bg='black')
    canvas.pack(padx=8, pady=4)

    status_var = tk.StringVar(value="No region set")
    tk.Label(root, textvariable=status_var).pack()

    def update_preview():
        canvas.delete("all")
        if not state['region']:
            return
        left, top, w, h = state['region']
        try:
            img = grab_region_img(state['region'])
            sw, sh = max(1, w*PREVIEW_SCALE), max(1, h*PREVIEW_SCALE)
            display = img.resize((sw, sh))
            tk_img = ImageTk.PhotoImage(display)
            canvas.image = tk_img
            canvas.create_image(0,0, anchor='nw', image=tk_img)
            arr = to_gray_array(img)
            ratio, dark_count, total, mask = detect_obstacle(arr)
            canvas.create_text(8,8, anchor='nw', fill='lime', text=f"ratio={ratio:.4f} dark={dark_count}/{total}")
        except Exception as e:
            canvas.create_text(10,10, anchor='nw', fill='red', text=f"Preview error: {e}")

    def on_start():
        if not state['region']:
            status_var.set("Set region first using Enter calibration.")
            return
        # short countdown so you can focus the browser window
        status_var.set("Starting in 3...")
        root.update()
        time.sleep(1)
        status_var.set("Starting in 2...")
        root.update()
        time.sleep(1)
        status_var.set("Starting in 1...")
        root.update()
        time.sleep(1)
        state['running'] = True
        status_var.set("Running — bot active. Close window to stop.")

    def on_stop():
        state['running'] = False
        status_var.set("Stopped")

    def on_reset():
        state['region'] = None
        state['running'] = False
        status_var.set("Reset — use Enter calibration again.")
        update_preview()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=6)
    tk.Button(btn_frame, text="Start", command=on_start).pack(side='left', padx=4)
    tk.Button(btn_frame, text="Stop", command=on_stop).pack(side='left', padx=4)
    tk.Button(btn_frame, text="Reset", command=on_reset).pack(side='left', padx=4)
    tk.Button(btn_frame, text="Update Preview", command=update_preview).pack(side='left', padx=4)

    def periodic():
        if state['region'] and state['debug']:
            update_preview()
        if not state['stop']:
            root.after(300, periodic)
        else:
            root.quit()

    root.after(300, periodic)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    state['stop'] = True

def calibrate_via_enter():
    print("\nCalibration via keyboard:")
    print("  1) Move mouse to TOP-LEFT of detection box, then press Enter in this terminal.")
    input("Press Enter when mouse is at TOP-LEFT...")
    x1, y1 = pyautogui.position()
    print(f"Top-left: {x1},{y1}")
    print("  2) Move mouse to BOTTOM-RIGHT of detection box, then press Enter.")
    input("Press Enter when mouse is at BOTTOM-RIGHT...")
    x2, y2 = pyautogui.position()
    left = min(x1, x2); top = min(y1, y2)
    w = abs(x2 - x1); h = abs(y2 - y1)
    state['region'] = (left, top, w, h)
    print(f"Region set to: {state['region']}")

def main():
    print("T‑Rex bot (fixed). Make sure Chrome is visible with the game.")
    print("If you see permission errors on macOS, grant Screen Recording and Accessibility to your terminal/IDE.")
    t = threading.Thread(target=bot_loop, daemon=True)
    t.start()

    # Calibration step
    calibrate_via_enter()
    # Launch preview/control window
    try:
        start_tk()
    except Exception as e:
        print("GUI failed:", e)
    state['stop'] = True
    t.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        state['stop'] = True
        print("\nExiting.")
        sys.exit(0)
