# led-display

This repo is used for displaying a YouTube subscriber counter on an WS2812B led matrix.

## Installation

For hardware, follow the overview on https://www.youtube.com/@CoastTimesDayOff

For software setup, install an OS such as Rasbian Lite to your Raspberry Pi.

Then run the setup script

```bash
sudo ./setup.sh
```

This setup script will install the led-display as a systemd service and will allow it to automatically start on boot.

(Optionally can also pull latest repo changes on startup.)

This will ask a number of question,

<b>YouTube channel id:</b> Find this in the url for your YouTube channel page.

For example, https://www.youtube.com/channel/UCxQf0pX4ocxBEWNVfVqE8FA the channel id is <i>UCxQf0pX4ocxBEWNVfVqE8FA</i>

<b>YouTube api key:</b> Set up a google developer account
following a tutorial such as <a href=https://blog.hubspot.com/website/how-to-get-youtube-api-key>this one.<a>

Other questions should be self explanitory.

To start/restart/stop the service you can use,

```bash
sudo systemctl <action> led-display.service
```

Check status with,

```bash
sudo systemctl status led-display.service
```

Get logs with,

```bash
sudo journalctl -u led-display
```

And uninstall with,

```bash
systemctl stop led-display.service
systemctl disable led-display.service
rm /etc/systemd/system/led-display.service
```
