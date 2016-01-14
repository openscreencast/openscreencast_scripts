#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Skript um die einzelnen keys der data.json-Datei in md-Dateien umzuwandeln
# data.json - Datenbank von openscreencast.de
# md-Dateien sind für die Software pelican
# Author: info@openscreencast.de
# License: MIT

import simplejson
import datetime
import html2text
import codecs

# Datei data.json einlesen
json_file_content = open('data.json').read()
# json laden und in eine Variable stecken
json_data = simplejson.loads(json_file_content)

# i = 0
# Alles Keys in einer Schleife durchgehen
for key in json_data:
	# UTF-8 md Dateien im Verzeichnis ./tmp erstellen
	f = codecs.open("./tmp/" + json_data[key]['path'] + ".md","w",'utf-8')
	#print str(i) + " " + json_data[key]['pubDate']
	f.write("Title: " + json_data[key]['title'] + "\n")
        f.write("Date: " + datetime.datetime.fromtimestamp(int(json_data[key]['pubDate'])).strftime('%Y-%m-%d %H:%M') + "\n")
	f.write("Author: " + json_data[key]['creator'] + "\n")	
	if (json_data[key].has_key('ogg_file') != False) or (json_data[key].has_key('youtube') != False) or (json_data[key].has_key('vimeo') != False) or (json_data[key].has_key('webm_file') != False) or (json_data[key].has_key('mp4_file') != False):
		f.write("Category: Video\n")
	else:
		f.write("Category: Artikel\n")	
	f.write("Tags: " + json_data[key]['category'] + "\n")
	f.write("Slug: " + json_data[key]['path'] + "\n")
	if (json_data[key].has_key('album') == True):
		f.write("Album: " + json_data[key]['album'] + "\n")
	if (json_data[key].has_key('duration') == True):
		f.write("Duration: " + json_data[key]['duration'] + "\n")
	if (json_data[key].has_key('license') == True):
		f.write("License: " + json_data[key]['license'] + "\n")
	if (json_data[key].has_key('license_om') == True):
		f.write("Licenseom: " + json_data[key]['license_om'] + "\n")
	if (json_data[key].has_key('youtube') == True):
		f.write("Youtube: " + json_data[key]['youtube'] + "\n")
	if (json_data[key].has_key('vimeo') == True):
		f.write("Vimeo: " + json_data[key]['vimeo'] + "\n")
	if (json_data[key].has_key('tumblr') == True):
		f.write("Tumblr: " + json_data[key]['tumblr'] + "\n")
	if (json_data[key].has_key('diaspora') == True):
		f.write("Diaspora: " + json_data[key]['diaspora'] + "\n")
	if (json_data[key].has_key('ogg_file') == True):
		f.write("Oggfile: " + json_data[key]['ogg_file'] + "\n")
	if (json_data[key].has_key('ogg_file_om') == True):
		f.write("Oggfileom: " + json_data[key]['ogg_file_om'] + "\n")
	if (json_data[key].has_key('webm_file') == True):
		f.write("Webmfile: " + json_data[key]['webm_file'] + "\n")
	if (json_data[key].has_key('mp4_file') == True):
		f.write("Mp4file: " + json_data[key]['mp4_file'] + "\n")
	if (json_data[key].has_key('mp4_file_om') == True):
		f.write("Mp4file_om: " + json_data[key]['mp4_file_om'] + "\n")
	if (json_data[key].has_key('mkv_file') == True):
		f.write("Mkvfile: " + json_data[key]['mkv_file'] + "\n")
	if (json_data[key].has_key('srt_file') == True):
		f.write("Srtfile: " + json_data[key]['srt_file'] + "\n")
	if (json_data[key].has_key('srt_file_om') == True):
		f.write("Srtfile_om: " + json_data[key]['srt_file_om'] + "\n")
	if (json_data[key].has_key('srt_file_eo') == True):
		f.write("Srtfileeo: " + json_data[key]['srt_file_eo'] + "\n")
	if (json_data[key].has_key('srt_file_om_eo') == True):
		f.write("Srtfileomeo: " + json_data[key]['srt_file_om_eo'] + "\n")
	if (json_data[key].has_key('srt_file_en') == True):
		f.write("Srtfileen: " + json_data[key]['srt_file_en'] + "\n")
	if (json_data[key].has_key('srt_file_om_en') == True):
		f.write("Srtfileomen: " + json_data[key]['srt_file_om_en'] + "\n")
	if (json_data[key].has_key('image') == True):
		f.write("Image: " + json_data[key]['image'] + "\n")
	f.write("\n")
	print html2text.html2text(json_data[key]['content'])
	f.write(html2text.html2text(json_data[key]['content']))	
	# i = i + 1
	f.close()
