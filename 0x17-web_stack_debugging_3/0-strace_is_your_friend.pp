# Puppet script Fix a Typographique issue in wp-setting.php "phpp" to "php"

exec{'fix-wp-setting':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
    path    => '/usr/local/bin/:/bin/'
}
