import time
import os
import common
import youtube
import number_array


if os.uname()[4].startswith("arm"):
    import led.display as display
else:
    import gui.display as display


MAX_DIGITS = 4
DC = "black"
RC = "red"
WC = "white"
LOGO = [
    [DC, RC, RC, RC, RC, RC, RC, RC, RC, DC, DC],
    [RC, RC, RC, RC, RC, RC, RC, RC, RC, RC, DC],
    [RC, RC, RC, RC, WC, RC, RC, RC, RC, RC, DC],
    [RC, RC, RC, RC, WC, WC, RC, RC, RC, RC, DC],
    [RC, RC, RC, RC, WC, WC, WC, RC, RC, RC, DC],
    [RC, RC, RC, RC, WC, WC, RC, RC, RC, RC, DC],
    [RC, RC, RC, RC, WC, RC, RC, RC, RC, RC, DC],
    [DC, RC, RC, RC, RC, RC, RC, RC, RC, DC, DC],
]


if __name__ == "__main__":
    config = common.load_config()
    old_subs = 0
    while True:
        sub_count = youtube.get_sub_count(
            config["youtube"]["channel_id"],
            config["youtube"]["api_key"],
        )
        if old_subs != sub_count:
            old_subs = sub_count
            num_array = number_array.get_number_array(sub_count, WC, DC, MAX_DIGITS)
            display.pack_subs(LOGO, num_array)
        time.sleep(10)
