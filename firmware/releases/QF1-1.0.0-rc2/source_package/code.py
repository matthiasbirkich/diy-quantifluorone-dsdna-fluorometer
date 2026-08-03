import gc
import sys
import time
import board
import displayio
import terminalio
from adafruit_display_text import label

STAGE = "boot"


def _splash():
    for path in ("/splashscreen.bmp", "/assets/splashscreen.bmp", "/images/splashscreen.bmp"):
        file_obj = None
        try:
            file_obj = open(path, "rb")
            bitmap = displayio.OnDiskBitmap(file_obj)
            tile = displayio.TileGrid(
                bitmap,
                pixel_shader=bitmap.pixel_shader,
                x=(board.DISPLAY.width - bitmap.width) // 2,
                y=(board.DISPLAY.height - bitmap.height) // 2,
            )
            group = displayio.Group()
            group.append(tile)
            board.DISPLAY.root_group = group
            time.sleep(2.0)
            board.DISPLAY.root_group = None
            file_obj.close()
            return
        except Exception:
            try:
                if file_obj is not None:
                    file_obj.close()
            except Exception:
                pass


def _fatal(error):
    try:
        gc.collect()
        bitmap = displayio.Bitmap(1, 1, 1)
        palette = displayio.Palette(1)
        palette[0] = 0x000000
        bg = displayio.Group(scale=max(board.DISPLAY.width, board.DISPLAY.height))
        bg.append(displayio.TileGrid(bitmap, pixel_shader=palette))
        group = displayio.Group()
        group.append(bg)
        free = gc.mem_free() if hasattr(gc, "mem_free") else -1
        text = str(error)
        lines = (
            "QuantiFluorONE ERROR",
            type(error).__name__,
            "stage=" + STAGE,
            "free=" + str(free) + " B",
            text[:25],
            text[25:50],
            "See serial traceback",
        )
        for i, value in enumerate(lines):
            group.append(label.Label(
                terminalio.FONT,
                text=value,
                color=0xFFFFFF if i == 0 else 0xFF7777,
                x=4,
                y=10 + i * 17,
            ))
        board.DISPLAY.root_group = group
    except Exception:
        pass
    try:
        sys.print_exception(error)
    except Exception:
        print(repr(error))
    while True:
        time.sleep(1)


try:
    STAGE = "splash"
    _splash()
    board.DISPLAY.root_group = None
    del _splash
    gc.collect()

    STAGE = "import app"
    from quantifluorone_app import QuantiFluorOneApp
    gc.collect()

    STAGE = "app init"
    app = QuantiFluorOneApp()
    gc.collect()

    STAGE = "run"
    app.run()
except Exception as exc:
    _fatal(exc)
