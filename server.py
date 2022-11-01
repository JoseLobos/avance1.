from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

#importar las librerias necesarias
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

port = 3000



class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="Progra-III-2022-Parcial_II_A1/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    #def do_POST(self):
        #lenc = int(self.headers["Content-Length"])
        #data = self.rfile.read(lenc)
        #data = data.decode()
        #data = float(parse.unquote(data))

        #probar nuestra IA
        #resp = modelo.predict([data])

        #self.send_response(200)
        #self.end_headers()
        #self.wfile.write( str(resp[0][0]).encode() )

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()