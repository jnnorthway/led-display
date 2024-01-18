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
    channel_id = os.environ.get("CHANNEL_ID")
    api_key = os.environ.get("API_KEY")
    old_subs = 0
    while True:
        try:
            sub_count = int(
                youtube.get_sub_count(
                    channel_id,
                    api_key,
                )
            )
            if sub_count and old_subs != sub_count:
                print(f"New sub count: {sub_count}")
                if old_subs < sub_count:
                    wipe_color = WC
                else:
                    wipe_color = RC
                display.wipe(wipe_color)
                time.sleep(0.4)
                display.wipe(DC, brightness=0)
                time.sleep(0.4)
                display.wipe(wipe_color)
                time.sleep(0.4)
                display.wipe(DC, brightness=0)
                old_subs = sub_count
                num_array = number_array.get_number_array(sub_count, WC, DC, MAX_DIGITS)
                display.pack_subs(LOGO, num_array)
            time.sleep(10)
        except KeyboardInterrupt:
            display.wipe(DC, brightness=0)
            exit(0)
