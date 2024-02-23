# increase the fie descriptors
exec { 'change_nginx_config':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
  notify  => Exec['restart_nginx_service'],
}

exec { 'restart_nginx_service':
  command     => '/usr/bin/env service nginx restart',
  refreshonly => true,
}
