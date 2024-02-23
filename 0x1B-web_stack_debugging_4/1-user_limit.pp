# A puppet manifest to change user limit
exec { 'increase-user-limit' :
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}