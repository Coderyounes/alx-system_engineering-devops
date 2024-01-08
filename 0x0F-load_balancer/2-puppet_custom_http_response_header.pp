# Add a Custome Header to Nginx Configuration Using Puppet

exec {'update':
  provider => shell,
  command => 'sudo apt-get -y update',
}

exec {'Nginx Install':
  provider => shell,
  command => 'sudo apt-get -y install nginx',
}

exec {'add_header':
  provider => shell,
  command => 'sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/&\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
}

exec {'restart':
  provider => shell,
  command => 'sudo service nginx restart',
  }