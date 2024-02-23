# Replace Holberton with foo
exec { 'update_limits_conf':
  command     => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}