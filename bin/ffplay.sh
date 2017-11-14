#!/bin/bash

#
# Wrapper script for playing videos with ffplay
# - Default X11 DISPLAY to :0
# - Buffer 10MB of input
# - Force fullscreen 1920x1080
# - Exit once finished
#

DISPLAY=:0 stdbuf -o 10MB ffplay -fs -x 1920 -y 1200 -autoexit -noborder - < $*

