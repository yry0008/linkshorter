# linkshorter
UIC的SDW2的期末作业


### Requirements

    Linux(Ubuntu 16.04 LTS+,Debian9+,CentOS7+)
    Python3 and pip support
    LNMP or BT-Panel

### Deployment

    mkdir -p /opt && cd /opt
    git clone https://github.com/yry0008/linkshorter.git
    cd linkshorter
    python3 -m pip install -r requirements.txt

Then edit the config.

    {
        "baseurl":"https://example.com",
        "debug":false,
        "db":"sqlite", //sqlite or mysql 
        "sqlite":{
            "file":"db.sqlite3"
        },
        "mysql": {
            "host": "",
            "port": 3306,
            "database": "",
            "user": "",
            "password": ""
        },
        "static_path": "/var/www/html/static"  //to storage css and js
    }

Then

    python3 manage.py migrate
    python3 manage.py collectstatic
    cp linkshorter.service /lib/systemd/system

The default server port is 9807

### Start The server

    systemctl enable linkshorter
    systemctl start linkshorter

You also can edit the linux systemd file to change the port

### Default Nginx reserved proxy config

    server
    {
        listen 80;
        server_name example.com;
        location /static {
            allow all;
            access_log off;
        }
        location /
        {
            proxy_pass http://127.0.0.1:9807;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header REMOTE-HOST $remote_addr;
            
            add_header X-Cache $upstream_cache_status;        
            add_header Cache-Control no-cache;
        }
    }

