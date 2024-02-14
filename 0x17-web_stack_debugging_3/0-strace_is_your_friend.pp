# Puppet script Fix a Typographique issue in wp-setting.php "phpp" to "php"

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
