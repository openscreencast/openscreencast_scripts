#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Skript um die einzelnen keys der data.json-Datei zu zählen
# data.json - Datenbank von openscreencast.de
# Author: info@openscreencast.de
# License: MIT

import simplejson


# Datei data.json einlesen
json_file_content = open('data.json').read()

# json laden und in eine Variable (Dictionary) stecken
json_data = simplejson.loads(json_file_content)

def count_data_short(json_data):
    # Variable (Dictionary) um die Einträge zu zählen
    count_data = {
            "all": 0,
            "video": 0,
            "article": 0,
            "ogg": 0,
            "webm": 0,
            "mp4": 0,
            "mkv": 0,
            "srt": 0,
            "youtube": 0,
            "vimeo": 0
            } 

    # Alle Keys in einer Schleife durchgehen
    for key in json_data:
        count_data['all'] += 1
        if (json_data[key].has_key('ogg_file') != False) or (json_data[key].has_key('youtube') != False) or (json_data[key].has_key('vimeo') != False) or (json_data[key].has_key('webm_file') != False) or (json_data[key].has_key('mp4_file') != False) or (json_data[key].has_key('mkv_file') != False):
            count_data['video'] += 1
        else:
            count_data['article'] += 1

        if (json_data[key].has_key("youtube") == True):
            count_data["youtube"] += 1
	    if (json_data[key].has_key('vimeo') == True):
		    count_data['vimeo'] += 1
	    if (json_data[key].has_key('ogg_file') == True):
		    count_data['ogg'] += 1
	    if (json_data[key].has_key('webm_file') == True):
		    count_data['webm'] += 1
	    if (json_data[key].has_key('mp4_file') == True):
		    count_data['mp4'] += 1
	    if (json_data[key].has_key('mkv_file') == True):
		    count_data['mkv'] += 1
	    if (json_data[key].has_key('srt_file') == True):
		    count_data['srt'] += 1

    print ""
    print ""
    print "data.json - Statistik"
    print "====================="
    print ""
    print "Einträge:", count_data["all"], "( Videos:", count_data["video"], "Artikel:", count_data["article"], ")"
    print ""
    print "Youtube:", count_data["youtube"], "Vimeo:", count_data["vimeo"]
    print ""
    print "ogg:", count_data["ogg"], "mp4:", count_data["mp4"], "webm:", count_data["webm"], "mkv:", count_data["mkv"]
    print ""
    print "srt:", count_data["srt"]   
    print ""
    print ""  
#    for key in count_data:
#        print key, ": ", count_data[key]


def count_data(json_data):
    count_data = {}

    for key in json_data:
        for key_next in json_data[key]:
            if count_data.has_key(key_next):
                count_data[key_next] += 1
            else:
                count_data[key_next] = 1

    for key in count_data:
        print key, ": ", count_data[key]
#    print "Anzahl der Einträge:", len(json_data.keys())


count_data_short(json_data)

count_data(json_data)

