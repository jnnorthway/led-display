#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $REPO_DIR/.env

echo DISPLAY_HOME=$REPO_DIR > $REPO_DIR/.env
echo PRIMARY_USER=$(who am i | awk '{print $1}') >> $REPO_DIR/.env

if [ -f /etc/systemd/system/led-display.service ]; then
    systemctl stop led-display.service
    systemctl disable led-display.service
    rm /etc/systemd/system/led-display.service
fi
cp $REPO_DIR/led-display.service /etc/systemd/system/
sed -i "s#{REPLACE_ME}#$REPO_DIR/.env#g" /etc/systemd/system/led-display.service

systemctl daemon-reload
if [ -f /usr/lib/python3.*/EXTERNALLY-MANAGED ]; then
    while true; do
        read -p "Remove /usr/lib/python3.*/EXTERNALLY-MANAGED? (y/n) " rsp
        case $rsp in
            [yY] )
                rm /usr/lib/python3.*/EXTERNALLY-MANAGED
                break;;
            [nN] )
                echo "This may cause issues on startup"
                break;;
            * )
                echo invalid response;;
        esac
    done
fi

question="YouTube channel id? "
if [[ -n "$CHANNEL_ID" ]]; then
    question="$question($CHANNEL_ID) "
fi
while true; do
read -p "$question" rsp
    if [[ -z $rsp ]] && [[ -z "$CHANNEL_ID" ]]; then
        echo invalid response
    elif [[ -z $rsp ]] && [[ -n "$CHANNEL_ID" ]]; then
        echo CHANNEL_ID="$CHANNEL_ID" >> $REPO_DIR/.env
        break
    else
        echo CHANNEL_ID="$rsp" >> $REPO_DIR/.env
        break
    fi
done

question="YouTube api key? "
if [[ -n "$API_KEY" ]]; then
    question="$question($API_KEY) "
fi
while true; do
read -p "$question" rsp
    if [[ -z $rsp ]] && [[ -z "$API_KEY" ]]; then
        echo invalid response
    elif [[ -z $rsp ]] && [[ -n "$API_KEY" ]]; then
        echo API_KEY="$API_KEY" >> $REPO_DIR/.env
        break
    else
        echo API_KEY="$rsp" >> $REPO_DIR/.env
        break
    fi
done

while true; do
    read -p "Update on startup? (y/n) " rsp
    case $rsp in
        [yY] )
            echo UPDATE_ON_START="true" >> $REPO_DIR/.env
            break;;
        [nN] )
            echo UPDATE_ON_START="false" >> $REPO_DIR/.env
            break;;
        * )
            echo invalid response;;
    esac
done

while true; do
    read -p "Force update? (y/n) " rsp
    case $rsp in
        [yY] )
            echo FORCE_UPDATE="true" >> $REPO_DIR/.env
            break;;
        [nN] )
            echo FORCE_UPDATE="false" >> $REPO_DIR/.env
            break;;
        * )
            echo invalid response;;
    esac
done

read -p "Tracking branch? (default: main) " rsp
if [[ -z $rsp ]]; then
    echo TRACKING_BRANCH="main" >> $REPO_DIR/.env
else
    echo TRACKING_BRANCH="$rsp" >> $REPO_DIR/.env
fi

while true; do
    read -p "Enable led-display.service on startup? (y/n) " rsp
    case $rsp in
        [yY] )
            systemctl enable led-display.service
            break;;
        [nN] )
            break;;
        * )
            echo invalid response;;
    esac
done

while true; do
    read -p "Start led-display.service now? (y/n) " rsp
    case $rsp in
        [yY] )
            systemctl start led-display.service
            break;;
        [nN] )
            break;;
        * )
            echo invalid response;;
    esac
done
