import webbrowser
import http.server
import socketserver


browser_name = "firefox"
browser_path = "C:\\Program Files\\Mozilla Firefox\\"
PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
    
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser_path + browser_name + ".exe"))
    webbrowser.get(browser_name).open_new_tab("http://127.0.0.1:" + str(PORT) + "/index.html")
    httpd.serve_forever()

print("end")
