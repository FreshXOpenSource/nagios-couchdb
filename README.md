nagios-couchdb
==============

CouchDB Nagios and Centreon check plugin

check_couchdb - simple couchdb monitoring

INSTALL

on RedHat EL6, SL6 or CentOS 6 : use wallaby repo and do a yum install

wget http://wallaby.freshx.de/repo/binary/Linux/RPM/wallaby.repo -O /etc/yum.repos.d/wallaby.repo
yum install nagios-plugins-couchdb

or get all the RPM files from the website manually

OTHER

get and install the backend drivers with git

https://github.com/FreshXOpenSource/wallaby-backend-couchdb
https://github.com/FreshXOpenSource/wallaby-backend-http

get the check_couchdb file from the download (see top)

TODO:

- Full IPv6 support (does not correctly look up v6 Adresses at the moment)
- add more performance data points
- add support for warning and critical checks

Feel free to get back to us for feedback at support@freshx.de
