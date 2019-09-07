#!/bin/bash
FTP="ftp.theragenetex.com"
#FTP="ftp.bioftp.org"
USER=""
PW=""
DIR=""

wget -r --ftp-password=$PW --ftp-user=$USER ftp://$FTP/$DIR
