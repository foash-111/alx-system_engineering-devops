#install nginx and add_header directive for servers in /sites-enabled/default

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/etc/nginx/sites-enabled/default ':
  ensure  => file,
  content => "
 server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        add_header X-Served-By ${HOSTNAME};
       location /redirect_me
       {
       return 301 https://www.youtube.come
       }

       error_page 404 /eror_page.html;

  }
 "
}
