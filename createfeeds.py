#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Skript um die einzelnen keys der data.json-Datei und der meta.json-Datei in RSS und XSPF umwandeln
# data.json - Datenbank von openscreencast.de
# meta.json - Metadaten
# Author: info@openscreencast.de
# License: MIT (https://github.com/openscreencast/openscreencast_scripts/blob/master/LICENSE)


import simplejson
import datetime
import html2text
import codecs

# 1 - Ja - Datei erstellen, 0 - Nein - Datei nicht erstellen 

OGG_XSPF = 1
MKV_XSPF = 1
MP4_XSPF = 1
WEBM_XSPF = 1

OGG_RSS = 1
MKV_RSS = 1
MP4_RSS = 1
WEBM_RSS = 1


# Datei data.json einlesen - json laden und in eine Variable stecken
json_file_content = open('data.json').read()
json_data = simplejson.loads(json_file_content)

# Datei meta.json einlesen - json laden und in eine Variable stecken
json_file_meta = open('meta.json').read()
json_meta = simplejson.loads(json_file_meta)

# Alles Keys nach der Zeit (pubDate) sortieren
keydict = {}
for key in json_data:
	keydict[json_data[key]['pubDate']] = key
keylist = keydict.keys()
keylist.sort()
keylist.reverse()

if OGG_XSPF == 1:
        f = codecs.open('ogg.xspf', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
	f.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">' + '\n')
	f.write('<trackList>' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('ogg_file'):
			f.write("<track>" + '\n')
            		f.write("\t<location>" +  json_data[key]['ogg_file'] + "</location>" + '\n')
            		f.write("\t<creator>" + json_data[key]['creator'] + "</creator>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<album>" + json_data[key]['album'] + "</album>" + '\n')
            		f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
            		f.write("\t<annotation>" + json_data[key]['description'] + "</annotation>" + '\n')
            		f.write("\t<duration>" + json_data[key]['duration'] + "</duration>" + '\n')
			if (json_data[key].has_key('image') == True):
            			f.write("\t<image>" + json_data[key]['image'] + "</image>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<info>" + json_data[key]['album'] + "</info>" + '\n')
	    		f.write("\t<license>" + json_data[key]['license'] + "</license>" + '\n')	
        		f.write("</track>" + '\n')	

        f.write('</trackList>' + '\n')
        f.write('</playlist>' + '\n')
        f.close()

if MKV_XSPF == 1:
	f = codecs.open('mkv.xspf', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
	f.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">' + '\n')
	f.write('<trackList>' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('mkv_file'):
			f.write("<track>" + '\n')
            		f.write("\t<location>" +  json_data[key]['mkv_file'] + "</location>" + '\n')
            		f.write("\t<creator>" + json_data[key]['creator'] + "</creator>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<album>" + json_data[key]['album'] + "</album>" + '\n')
            		f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
            		f.write("\t<annotation>" + json_data[key]['description'] + "</annotation>" + '\n')
            		f.write("\t<duration>" + json_data[key]['duration'] + "</duration>" + '\n')
			if (json_data[key].has_key('image') == True):
            			f.write("\t<image>" + json_data[key]['image'] + "</image>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<info>" + json_data[key]['album'] + "</info>" + '\n')
	    		f.write("\t<license>" + json_data[key]['license'] + "</license>" + '\n')	
        		f.write("</track>" + '\n')	

	f.write('</trackList>' + '\n')
	f.write('</playlist>' + '\n')
	f.close()

if MP4_XSPF == 1:
	f = codecs.open('mp4.xspf', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
	f.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">' + '\n')
	f.write('<trackList>' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('mp4_file'):
			f.write("<track>" + '\n')
            		f.write("\t<location>" +  json_data[key]['mp4_file'] + "</location>" + '\n')
            		f.write("\t<creator>" + json_data[key]['creator'] + "</creator>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<album>" + json_data[key]['album'] + "</album>" + '\n')
            		f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
            		f.write("\t<annotation>" + json_data[key]['description'] + "</annotation>" + '\n')
            		f.write("\t<duration>" + json_data[key]['duration'] + "</duration>" + '\n')
			if (json_data[key].has_key('image') == True):
            			f.write("\t<image>" + json_data[key]['image'] + "</image>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<info>" + json_data[key]['album'] + "</info>" + '\n')
	    		f.write("\t<license>" + json_data[key]['license'] + "</license>" + '\n')	
        		f.write("</track>" + '\n')	

	f.write('</trackList>' + '\n')
	f.write('</playlist>' + '\n')
	f.close()

if WEBM_XSPF == 1:
	f = codecs.open('webm.xspf', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
	f.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">' + '\n')
	f.write('<trackList>' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('webm_file'):
			f.write("<track>" + '\n')
            		f.write("\t<location>" +  json_data[key]['webm_file'] + "</location>" + '\n')
            		f.write("\t<creator>" + json_data[key]['creator'] + "</creator>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<album>" + json_data[key]['album'] + "</album>" + '\n')
            		f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
            		f.write("\t<annotation>" + json_data[key]['description'] + "</annotation>" + '\n')
            		f.write("\t<duration>" + json_data[key]['duration'] + "</duration>" + '\n')
			if (json_data[key].has_key('image') == True):
            			f.write("\t<image>" + json_data[key]['image'] + "</image>" + '\n')
			if (json_data[key].has_key('album') == True):
            			f.write("\t<info>" + json_data[key]['album'] + "</info>" + '\n')
	    		f.write("\t<license>" + json_data[key]['license'] + "</license>" + '\n')	
        		f.write("</track>" + '\n')	

	f.write('</trackList>' + '\n')
	f.write('</playlist>' + '\n')
	f.close()

if OGG_RSS == 1:
	f = codecs.open('ogg-rss.xml', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n')
 	f.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n')
 
  	f.write("<channel>" + '\n')
    	f.write("<title>" + json_meta['title'] + "</title>" + '\n')
    	f.write("<link>" + json_meta['domain'] + "</link>" + '\n')
    	f.write("<description>" + json_meta['description'] + "</description>" + '\n')
    	f.write("<lastBuildDate>" + datetime.datetime.fromtimestamp(int(json_meta['lastBuildDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</lastBuildDate>" + '\n')
    	f.write("<language>" + json_meta['language'] + "</language>" + '\n')
    	f.write("<managingEditor>" + json_meta['email'] + " (Heiko)</managingEditor>" + '\n')
    	f.write("<webMaster>" + json_meta['email'] + " (Heiko)</webMaster>" + '\n')
    	f.write("<ttl>1440</ttl>" + '\n')
    	f.write("<image>" + '\n')
	f.write("\t<url>" + json_meta['logo'] + "</url>" + '\n')
	f.write("\t<title>" + json_meta['title'] + "</title>" + '\n')
	f.write("\t<link>" + json_meta['domain'] + "</link>" + '\n')
	f.write("\t<width>144</width>" + '\n')
	f.write("\t<height>144</height>" + '\n')
   	f.write("</image>" + '\n')
   	f.write('<atom:link href="http://www.openscreencast.de/ogg-rss.xml" rel="self" type="application/rss+xml" />' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('ogg_file'):
			f.write("<item>" + '\n')
      			f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
      			f.write("\t<link>" + json_meta['domain'] + json_meta['path']  + json_data[key]['path'] + ".html</link>" + '\n')	
			f.write("\t<description><![CDATA[" + '\n')
			if json_data[key].has_key('ogg_file'):
				f.write('Ogg-Datei: <a href="' + json_data[key]['ogg_file'] + '">' + json_data[key]['ogg_file'] + '</a>\n' + '\n')
			if json_data[key].has_key('youtube'):
				f.write('Youtube-Link: <a href="http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '">http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '</a>\n' + '\n')
			f.write(json_data[key]['content'] + "]]></description>" + '\n')
			f.write("\t<pubDate>" + datetime.datetime.fromtimestamp(int(json_data[key]['pubDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</pubDate>" + '\n')	
			f.write("\t<dc:creator>" + json_data[key]['creator'] + "</dc:creator>" + '\n')
			for i in json_data[key]['category'].split(','):
		      		f.write("\t<category><![CDATA[" + i.strip() + "]]></category>" + '\n')
				f.write('\t<guid isPermaLink="false">' + json_meta['domain'] + json_meta['path'] + json_data[key]['path'] + ".html</guid>" + '\n')
			if json_data[key].has_key('ogg_file'): 
				f.write('<enclosure url="' + json_data[key]['ogg_file'] + '" type="video/ogv" />' + '\n')
			f.write("</item>" + '\n')

	f.write('</channel>' + '\n')
	f.write('</rss>' + '\n')
	f.close()

if WEBM_RSS == 1:
	f = codecs.open('webm-rss.xml', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n')
 	f.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n')
 
  	f.write("<channel>" + '\n')
    	f.write("<title>" + json_meta['title'] + "</title>" + '\n')
    	f.write("<link>" + json_meta['domain'] + "</link>" + '\n')
    	f.write("<description>" + json_meta['description'] + "</description>" + '\n')
    	f.write("<lastBuildDate>" + datetime.datetime.fromtimestamp(int(json_meta['lastBuildDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</lastBuildDate>" + '\n')
    	f.write("<language>" + json_meta['language'] + "</language>" + '\n')
    	f.write("<managingEditor>" + json_meta['email'] + " (Heiko)</managingEditor>" + '\n')
    	f.write("<webMaster>" + json_meta['email'] + " (Heiko)</webMaster>" + '\n')
    	f.write("<ttl>1440</ttl>" + '\n')
    	f.write("<image>" + '\n')
	f.write("\t<url>" + json_meta['logo'] + "</url>" + '\n')
	f.write("\t<title>" + json_meta['title'] + "</title>" + '\n')
	f.write("\t<link>" + json_meta['domain'] + "</link>" + '\n')
	f.write("\t<width>144</width>" + '\n')
	f.write("\t<height>144</height>" + '\n')
   	f.write("</image>" + '\n')
   	f.write('<atom:link href="http://www.openscreencast.de/webm-rss.xml" rel="self" type="application/rss+xml" />' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('webm_file'):
			f.write("<item>" + '\n')
      			f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
      			f.write("\t<link>" + json_meta['domain'] + json_meta['path']  + json_data[key]['path'] + ".html</link>" + '\n')	
			f.write("\t<description><![CDATA[" + '\n')
			if json_data[key].has_key('webm_file'):
				f.write('Webm-Datei: <a href="' + json_data[key]['webm_file'] + '">' + json_data[key]['webm_file'] + '</a>\n' + '\n')
			if json_data[key].has_key('youtube'):
				f.write('Youtube-Link: <a href="http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '">http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '</a>\n' + '\n')
			f.write(json_data[key]['content'] + "]]></description>" + '\n')
			f.write("\t<pubDate>" + datetime.datetime.fromtimestamp(int(json_data[key]['pubDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</pubDate>" + '\n')	
			f.write("\t<dc:creator>" + json_data[key]['creator'] + "</dc:creator>" + '\n')
			for i in json_data[key]['category'].split(','):
		      		f.write("\t<category><![CDATA[" + i.strip() + "]]></category>" + '\n')
				f.write('\t<guid isPermaLink="false">' + json_meta['domain'] + json_meta['path'] + json_data[key]['path'] + ".html</guid>" + '\n')
			if json_data[key].has_key('webm_file'): 
				f.write('<enclosure url="' + json_data[key]['webm_file'] + '" type="video/webm" />' + '\n')
			f.write("</item>" + '\n')

	f.write('</channel>' + '\n')
	f.write('</rss>' + '\n')
	f.close()

if MP4_RSS == 1:
	f = codecs.open('mp4-rss.xml', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n')
 	f.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n')
 
  	f.write("<channel>" + '\n')
    	f.write("<title>" + json_meta['title'] + "</title>" + '\n')
    	f.write("<link>" + json_meta['domain'] + "</link>" + '\n')
    	f.write("<description>" + json_meta['description'] + "</description>" + '\n')
    	f.write("<lastBuildDate>" + datetime.datetime.fromtimestamp(int(json_meta['lastBuildDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</lastBuildDate>" + '\n')
    	f.write("<language>" + json_meta['language'] + "</language>" + '\n')
    	f.write("<managingEditor>" + json_meta['email'] + " (Heiko)</managingEditor>" + '\n')
    	f.write("<webMaster>" + json_meta['email'] + " (Heiko)</webMaster>" + '\n')
    	f.write("<ttl>1440</ttl>" + '\n')
    	f.write("<image>" + '\n')
	f.write("\t<url>" + json_meta['logo'] + "</url>" + '\n')
	f.write("\t<title>" + json_meta['title'] + "</title>" + '\n')
	f.write("\t<link>" + json_meta['domain'] + "</link>" + '\n')
	f.write("\t<width>144</width>" + '\n')
	f.write("\t<height>144</height>" + '\n')
   	f.write("</image>" + '\n')
   	f.write('<atom:link href="http://www.openscreencast.de/mp4-rss.xml" rel="self" type="application/rss+xml" />' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('mp4_file'):
			f.write("<item>" + '\n')
      			f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
      			f.write("\t<link>" + json_meta['domain'] + json_meta['path']  + json_data[key]['path'] + ".html</link>" + '\n')	
			f.write("\t<description><![CDATA[" + '\n')
			if json_data[key].has_key('mp4_file'):
				f.write('Mp4-Datei: <a href="' + json_data[key]['mp4_file'] + '">' + json_data[key]['mp4_file'] + '</a>\n' + '\n')
			if json_data[key].has_key('youtube'):
				f.write('Youtube-Link: <a href="http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '">http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '</a>\n' + '\n')
			f.write(json_data[key]['content'] + "]]></description>" + '\n')
			f.write("\t<pubDate>" + datetime.datetime.fromtimestamp(int(json_data[key]['pubDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</pubDate>" + '\n')	
			f.write("\t<dc:creator>" + json_data[key]['creator'] + "</dc:creator>" + '\n')
			for i in json_data[key]['category'].split(','):
		      		f.write("\t<category><![CDATA[" + i.strip() + "]]></category>" + '\n')
				f.write('\t<guid isPermaLink="false">' + json_meta['domain'] + json_meta['path'] + json_data[key]['path'] + ".html</guid>" + '\n')
			if json_data[key].has_key('mp4_file'): 
				f.write('<enclosure url="' + json_data[key]['mp4_file'] + '" type="video/mp4" />' + '\n')
			f.write("</item>" + '\n')

	f.write('</channel>' + '\n')
	f.write('</rss>' + '\n')
	f.close()

if MKV_RSS == 1:
	f = codecs.open('mkv-rss.xml', 'w', 'utf-8')
	f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n')
 	f.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n')
 
  	f.write("<channel>" + '\n')
    	f.write("<title>" + json_meta['title'] + "</title>" + '\n')
    	f.write("<link>" + json_meta['domain'] + "</link>" + '\n')
    	f.write("<description>" + json_meta['description'] + "</description>" + '\n')
    	f.write("<lastBuildDate>" + datetime.datetime.fromtimestamp(int(json_meta['lastBuildDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</lastBuildDate>" + '\n')
    	f.write("<language>" + json_meta['language'] + "</language>" + '\n')
    	f.write("<managingEditor>" + json_meta['email'] + " (Heiko)</managingEditor>" + '\n')
    	f.write("<webMaster>" + json_meta['email'] + " (Heiko)</webMaster>" + '\n')
    	f.write("<ttl>1440</ttl>" + '\n')
    	f.write("<image>" + '\n')
	f.write("\t<url>" + json_meta['logo'] + "</url>" + '\n')
	f.write("\t<title>" + json_meta['title'] + "</title>" + '\n')
	f.write("\t<link>" + json_meta['domain'] + "</link>" + '\n')
	f.write("\t<width>144</width>" + '\n')
	f.write("\t<height>144</height>" + '\n')
   	f.write("</image>" + '\n')
   	f.write('<atom:link href="http://www.openscreencast.de/mkv-rss.xml" rel="self" type="application/rss+xml" />' + '\n')

	for k in keylist:
	       	key = keydict[k]
		json_data[key]['key'] = key
		if json_data[key].has_key('mkv_file'):
			f.write("<item>" + '\n')
      			f.write("\t<title>" + json_data[key]['title'] + "</title>" + '\n')
      			f.write("\t<link>" + json_meta['domain'] + json_meta['path']  + json_data[key]['path'] + ".html</link>" + '\n')	
			f.write("\t<description><![CDATA[" + '\n')
			if json_data[key].has_key('mkv_file'):
				f.write('mkv-Datei: <a href="' + json_data[key]['mkv_file'] + '">' + json_data[key]['mkv_file'] + '</a>\n' + '\n')
			if json_data[key].has_key('youtube'):
				f.write('Youtube-Link: <a href="http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '">http://www.youtube-nocookie.com/embed/' + json_data[key]['youtube'] + '</a>\n' + '\n')
			f.write(json_data[key]['content'] + "]]></description>" + '\n')
			f.write("\t<pubDate>" + datetime.datetime.fromtimestamp(int(json_data[key]['pubDate'])).strftime("%a, %d %b %Y %H:%M:%S +0100") + "</pubDate>" + '\n')	
			f.write("\t<dc:creator>" + json_data[key]['creator'] + "</dc:creator>" + '\n')
			for i in json_data[key]['category'].split(','):
		      		f.write("\t<category><![CDATA[" + i.strip() + "]]></category>" + '\n')
				f.write('\t<guid isPermaLink="false">' + json_meta['domain'] + json_meta['path'] + json_data[key]['path'] + ".html</guid>" + '\n')
			if json_data[key].has_key('mkv_file'): 
				f.write('<enclosure url="' + json_data[key]['mkv_file'] + '" type="video/mkv" />' + '\n')
			f.write("</item>" + '\n')

	f.write('</channel>' + '\n')
	f.write('</rss>' + '\n')
	f.close()

