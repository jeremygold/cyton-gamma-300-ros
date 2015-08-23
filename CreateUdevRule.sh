#!/bin/bash

rules_file=/etc/udev/rules.d/50-cyton-gamma-300.rules
cyton_serial_number="A9U5XBR7"

if [ "$(id -u)" != "0" ]; then
    echo "ERROR: This script must be run as root"
    exit 1
fi

if [ ! -f $rules_file ]; then
    echo "Updating udev rule for Cyton Gamma 300"
    echo 'SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="0000", ATTRS{serial}=="'$cyton_serial_number'", SYMLINK+="cyton_gamma_300", MODE="0666"' > $rules_file
else
    echo "Cyton Gamma 300 udev rule already there"
fi
