#!/bin/bash

# Got root?
myWHOAMI=$(whoami)
if [ "$myWHOAMI" != "root" ]
  then
    echo "Need to run as root ..."
    exit
fi

/usr/bin/openssl req -nodes -x509 -sha512 -newkey rsa:4096 -keyout "nginx.key" -out "nginx.crt" -days 3650

