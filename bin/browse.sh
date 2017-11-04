#!/bin/bash

#
# Wrapper script for playing videos or browsing links
# - Default X11 DISPLAY to :0
# - Force fullscreen
#

DISPLAY=:0 chromium-browser -kiosk -fullscreen $*

