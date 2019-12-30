from fonAPI.fonAPI import FonApi

#My token : f36fc5968a418f32aca94157b7898c2cf296f189bcefa8de

#Features avalaibles
""" 
DeviceName
Brand
technology
2g_bands
gprs
edge
announced
status
dimensions
weight
sim
type (display type)
size
resolution
card_slot
phonebook
call_records
camera_c (camera availablity)
alert_types
loudspeaker_
3_5mm_jack_
sound_c (Sound Quality)
wlan
bluetooth
gps
infrared_port
radio
usb
messaging
browser
clock
alarm
games
languages
java
features_c (additional features sperated by "-")
battery_c (battery information)
stand_by (standby time)
talk_time (standby time)
colors (available colors)
sensors
cpu
internal (memory + RAM)
os
body_c (body features seperated by "-")
keyboard
primary_ (primary camera)
video
secondary (secondary camera)
3g_bands
speed
network_c
chipset
features (additional features seperated by "-")
music_play
protection
gpu
multitouch
loudspeaker
audio_quality
nfc
camera
display
battery_life
4g_bands
"""

def getData(name_device):
    """
    Get data for devices 
    """
    fon = FonApi('f36fc5968a418f32aca94157b7898c2cf296f189bcefa8de')
    phones = fon.getdevice(name_device)

    return phones

