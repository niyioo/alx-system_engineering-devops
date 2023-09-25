#!/usr/bin/env bash
# Puppet manifest to configure SSH client

file { 'ect/ssh/ssh-config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
