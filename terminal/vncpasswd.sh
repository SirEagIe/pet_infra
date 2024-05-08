#!/usr/bin/expect

set pass [lindex $argv 0];

spawn /usr/bin/vncpasswd
expect "Password:"
send "$pass\r"
expect "Verify:"
send "$pass\r"
expect "Would you like to enter a view-only password (y/n)?"
send "n\r"

set timeout -1
expect eof