worker_processes 1;

user nobody nogroup;
pid /tmp/nginx.pid;

events {
    worker_connections 1024;
    accept_mutex off;
}

http {
    include mime.types;
    default_type application/octet-stream;
    sendfile on;

    error_log /var/log/nginx.error.log;
    access_log /var/log/nginx.access.log;


    server {
    	listen 80;
    	server_name example.org;
    	access_log  /var/log/nginx/example.log;

    	location / {
        	proxy_pass http://127.0.0.1:8000;
        	proxy_set_header Host $host;
        	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    	}
    }
}