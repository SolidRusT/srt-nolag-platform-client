import mysql.connector
from mysql.connector import Error
import os
import subprocess

# Read configuration values from MySQL database
def read_config_values():
    try:
        # Read MySQL connection parameters from config file
        with open("config.ini", "r") as f:
          config = f.read()
        mysql_config = dict(line.split("=") for line in config.split("\n") if line)
        if "port" in mysql_config:
          mysql_config["port"] = int(mysql_config["port"])
        mysql_conn = mysql.connector.connect(**mysql_config)
        
        # Read configuration values for this server
        server_name = os.environ["SERVER_NAME"]
        cursor = mysql_conn.cursor()
        cursor.execute(f"SELECT key_name, value FROM config_values WHERE server_name='{server_name}'")
        rows = cursor.fetchall()
        
        # Set configuration values as environment variables
        for row in rows:
            os.environ[row[0]] = row[1]
            
        cursor.close()
        mysql_conn.close()
        
    except Error as e:
        print(e)
        exit(1)
        
# Launch RustDedicated with configuration values from MySQL database
def start_rust():
    # Read configuration values
    read_config_values()
    
    # Construct RustDedicated command
    rust_cmd = ["./RustDedicated", "-batchmode", "-nographics", "-silent-crashes", "-logfile", os.environ["SERVER_LOGS"],
                "+server.ip", "0.0.0.0", "+server.port", os.environ["RUST_SERVER_PORT"], "+rcon.ip", "0.0.0.0",
                "+rcon.port", os.environ["RUST_RCON_PORT"], "+app.publicip", os.environ["SERVER_IP"],
                "+app.port", os.environ["RUST_APP_PORT"], "+rcon.web", "1", "+rcon.password", os.environ["RUST_RCON_ADMIN"],
                "+server.gamemode", "vanilla", "+server.identity", os.environ["RUST_IDENTITY"],
                "+server.logoimage", os.environ["RUST_AVATAR"]]
    
    # Launch game server
    subprocess.Popen(rust_cmd)
