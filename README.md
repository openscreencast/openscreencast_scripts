Skripte von openscreencast.de

## Tools

### json2md.py

Skript um die einzelnen keys der data.json-Datei in md-Dateien umzuwandeln    
data.json - Datenbank von openscreencast.de    
md-Dateien sind für die Software pelican

Beispiel:

```
pip install simplejson
./json2md.py
```

### count_data.py

Skript um die einzelnen keys der data.json-Datei zu zählen    
data.json - Datenbank von openscreencast.de

Beispiel:

```
pip install simplejson
./count_data.py
```

### createfeeds.py

Skript um die RSS-Feeds und XSPF-Dateien zu erstellen (für OGG, MP4, WEBM, MKV)    
data.json - Datenbank von openscreencast.de    
meta.json - Metadaten

Beispiel:

```
pip install simplejson
./createfeeds.py
```

## Lizenz

[MIT](https://github.com/openscreencast/openscreencast_scripts/blob/master/LICENSE)
