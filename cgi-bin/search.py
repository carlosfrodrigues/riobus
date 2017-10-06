#!/usr/bin/python
import cgi   
import json
import requests
url = 'http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterTodasPosicoes'
data = requests.get(url).content
output = json.loads(data)
n = len(output['DATA'])
lista =[]
form = cgi.FieldStorage()   
valor = form.getfirst("number", "0")
valor = float(valor)
print "Content-type:text/html\r\n\r\n"
#print "<h1>%i</h1>"% valor 
#print "<br>"
for i in range(0, n):
    if valor == output['DATA'][i][2]:
#	print """<li><a href="http://www.google.com/maps/place/%f,%f">%s</a></li>"""% (output['DATA'][i][3],output['DATA'][i][4],output['DATA'][i])
	lista.append([output['DATA'][i][3],output['DATA'][i][4]])

z = len(lista)
print """\
<html>
  <head>
<title>BusRio</title>
	<link href="/static/style.css" rel="stylesheet">
		<meta name="robots" content="noindex,follow" />
</head>
<body>
	<ul class="nav">
		<li id="settings">
			<img src="/static/settings2.png"/>
		</li>
		<li>
			<a href="#">RioBus</a>
		</li>
		<li>
			<a href="#">Sobre</a>
		</li>
		<li id="search">
			<form action="" method="get">
				<input id="search_text" maxlength="4" size="4" value="" name="number" placeholder="Digite aqui o n&uacute;mero do &ocirc;nibus"/>
				<input type="button" name="search_button" id="search_button" type="submit"></a>
			</form>
		</li>	
	</ul>
	
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      #map {
        height: 100%;
      }

      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -22.9053516, lng: -43.1956282},
          zoom: 11
        });"""
for i in range(0, z):     
	print"""      var marker = new google.maps.Marker({
	    		position: new google.maps.LatLng(%f,%f),
	    		map: map,
	    		title: ""
	      });"""% (lista[i][0],lista[i][1])
print"""      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key= AIzaSyAN69JFgFynsUNnSR3kryVDKzzDLvbkfy0 &callback=initMap"
    async defer></script>
  </body>
</html>

"""

