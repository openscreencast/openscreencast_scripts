#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Skript um die einzelnen keys der data.json-Datei zu zählen
# data.json - Datenbank von openscreencast.de
# Author: info@openscreencast.de
# License: MIT

"""
count_data.py ist ein Skript um die Datei data.json (Datenbank) von openscreencast.de
auszuwerten. Die Daten werden in eine Statistik gegossen.

Beispiel:

python ./count_data.py

Datei data.json muss im gleichen Verzeichnis sein.
"""

import simplejson

# --- mit OOP ---
class data_statistik(object):
    """
    Ein Objekt der Klasse data_statistik nimmt die json-Daten als Dictionary und bietet
    die 2 Funktionen count_data und count_data_short an.
    """
    
    def __init__(self, json_data):
        """
        Beim Erstellen eines Objekts der Klasse data_statistik wird ein Dictionary von data.json genommen.
        """

        self.json_data = json_data

    def count_data(self):
        """
        Mit count_data werden alle vorhandenen Schlüssel und deren Anzahl ausgegeben.

        Beispiel:

        a = data_statistik(json_data)
        a.count_data()
        """
        
        self.count_data = {}

        for key in self.json_data:
            for key_next in self.json_data[key]:
                if self.count_data.has_key(key_next):
                    self.count_data[key_next] += 1
                else:
                    self.count_data[key_next] = 1

        for key in self.count_data:
            print key, ": ", self.count_data[key]
#        print "Anzahl der Einträge:", len(self.json_data.keys())

    def count_data_short(self):
        """
        Mit count_data_short wird eine kurze Statistik ausgegeben.

        Beispiel:

        a = data_statistik(json_data)
        a.count_data_short()
        """

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
        for key in self.json_data:
            count_data['all'] += 1
            if (self.json_data[key].has_key('ogg_file') != False) or (self.json_data[key].has_key('youtube') != False) or (self.json_data[key].has_key('vimeo') != False) or (self.json_data[key].has_key('webm_file') != False) or (self.json_data[key].has_key('mp4_file') != False) or (self.json_data[key].has_key('mkv_file') != False):
                count_data['video'] += 1
            else:
                count_data['article'] += 1

            if (self.json_data[key].has_key("youtube") == True):
                count_data["youtube"] += 1
	        if (self.json_data[key].has_key('vimeo') == True):
		        count_data['vimeo'] += 1
	        if (self.json_data[key].has_key('ogg_file') == True):
		        count_data['ogg'] += 1
	        if (self.json_data[key].has_key('webm_file') == True):
		        count_data['webm'] += 1
	        if (self.json_data[key].has_key('mp4_file') == True):
		        count_data['mp4'] += 1
	        if (self.json_data[key].has_key('mkv_file') == True):
		        count_data['mkv'] += 1
	        if (self.json_data[key].has_key('srt_file') == True):
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
#        for key in count_data:
#            print key, ": ", count_data[key]




# Datei data.json einlesen
json_file_content = open('data.json').read()

# json laden und in eine Variable (Dictionary) stecken
json_data = simplejson.loads(json_file_content)



# --- ohne OOP ---
#
# ohne OOP - Mit count_data_short wird eine kurze Statistik ausgegeben.
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

# ohne OOP - Mit count_data werden alle vorhandenen Schlüssel und deren Anzahl ausgegeben.
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


# --- ohne OOP ---
#count_data_short(json_data)
#count_data(json_data)

# --- mit OOP ---
stat = data_statistik(json_data)
stat.count_data_short()
#stat.count_data()



