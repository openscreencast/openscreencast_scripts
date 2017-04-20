#!/usr/bin/env bash
# by openscreencast.de
# License: https://creativecommons.org/publicdomain/zero/1.0/

OPENSCREENCAST_ICON=$(curl -s "http://www.openscreencast.de/favicon.ico" | base64 -w 0)
LISTE=$(curl -s "http://www.openscreencast.de/data/gnome_shell_extension_argos_openscreencast_screencasts.csv")
STATISTIK=$(curl -s "http://www.openscreencast.de/data/gnome_shell_extension_argos_openscreencast_statistik.csv")

echo "openscreencast"
echo "---"
echo "openscreencast | image='$OPENSCREENCAST_ICON' imageWidth=25 href='http://www.openscreencast.de/'"
echo "---"
echo "Die letzten 5 Screencasts: "
echo "--- | dropdown=true"
while IFS= read line
do
    TITLE=$(echo $line | cut -f 1 -d ',' | cut -c-30)
    LINK=$(echo $line | cut -f 2 -d ',')
    THUMBNAIL_LINK=$(echo $line | cut -f 3 -d ',')
    THUMBNAIL=$(curl -s $THUMBNAIL_LINK | base64 -w 0)
    echo "-- $TITLE ... | href='$LINK'"
    echo "-- | image='$THUMBNAIL' imageWidth=180 imageHeight=100 | href='$LINK'"
done <<< "$LISTE"
echo "Statistik: "
echo "--- | dropdown=true"
echo "-- Videos: $STATISTIK"
echo "Links: "
echo "--- | dropdown=true"
echo "-- Youtube | href='https://www.youtube.com/user/openscreencast'"
echo "-- Vimeo | href='https://www.vimeo.com/openscreencast'"
echo "-- Tumblr | href='http://openscreencast.tumblr.com/'"
echo "-- Twitter | href='https://twitter.com/openscreencast'"
echo "-- Diaspora | href='https://pod.geraspora.de/u/openscreencast'"
echo "-- GnuSocial | href='https://gnusocial.de/openscreencast'"
echo "-- GitHub | href='https://github.com/openscreencast'"


