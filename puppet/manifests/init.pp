
Exec {
  path => ['/usr/bin', '/bin', '/sbin'],
}

package {'default-jdk':
  ensure => present,
}

class { 'elasticsearch':
  require => Package['default-jdk'],
}

