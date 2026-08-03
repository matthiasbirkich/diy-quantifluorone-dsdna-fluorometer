"""Filesystem mode for QuantiFluorONE logging.

With a USB data host connected, CIRCUITPY remains writable by the computer and
read-only to the firmware. With a charger or power bank, the firmware can save
blank state and CSV rows.
"""

import storage

try:
    import supervisor

    usb_connected = supervisor.runtime.usb_connected
except Exception:
    usb_connected = False

storage.remount("/", readonly=bool(usb_connected))
