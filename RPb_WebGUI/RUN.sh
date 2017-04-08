#!/bin/sh
SCRIPT="$(readlink --canonicalize-existing "$0")"
SCRIPTPATH="$(dirname "$SCRIPT")"
echo $SCRIPTPATH 
xinit $SCRIPTPATH/MAX_GUI
