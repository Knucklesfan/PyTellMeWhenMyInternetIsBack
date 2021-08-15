import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time

import simpleaudio as sa

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) != 0



print("Making request...")
time.sleep(1.0)
keepCalling = True

while True:

    keepCalling = (ping("google.com"))
    if keepCalling:
        print("No response... Trying again in 5 seconds.")
        time.sleep(5.0)
    else:
        print("Response gotten!!!")
        filename = 'vineboom.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
