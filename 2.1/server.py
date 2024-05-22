import socketserver
from http.server import SimpleHTTPRequestHandler
from dataprovider import DataProvider


class ServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.dataprovider = DataProvider('C:/Users/HP Pavilion Gaming/Desktop/Programming_2/2.1/dSST.csv')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if not self.path.startswith("/data"):
            self.send_error(404)
            return
        
        path_parts = [part for part in self.path.split("/") if part]
        try:
            if path_parts[1] == "all":
                json_data = self.dataprovider.get_weather_data()
            else:
                year_1 = int(path_parts[1])
                if len(path_parts) == 3:
                    year_2 = int(path_parts[2])
                    json_data = self.dataprovider.get_weather_data((year_1, year_2))
                else:
                    json_data = self.dataprovider.get_weather_data(year_1)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode("UTF-8"))
            

        except (ValueError, IndexError):
            self.send_error(400)

if __name__ == "__main__":  
    port = 8080
    with socketserver.TCPServer(("localhost", port), ServerHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()
