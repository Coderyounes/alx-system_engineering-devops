# A puppet manifest to change user limit
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }