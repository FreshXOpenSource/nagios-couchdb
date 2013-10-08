Name:           nagios-plugins-couchdb
Version:        0.9
Vendor:		FreshX Labs
Release:        5.fx%{?dist}
Summary:        A nagios plugin to monitor couchdb databases
Group:          Development/Languages
License:        BSD
URL:            https://github.com/FreshXOpenSource/nagios-couchdb
Source0:        http://wallaby.freshx.de/repo/binary/Linux/RPM/source/nagios-plugins-couchdb-%{version}.tar.gz
BuildArch:      noarch
Requires:  	python-wallaby-backend-couchdb, twisted >= 11.0

%description
This package provides a couchdb monitoring plugin. The plugin can connect to remote hosts via https or http, anonymous or using username and password and can produce basic performance data. This plugin also demonstrates the asynchroneuous couchdb Python driver. All packages are found as RPM and SRPM at http://wallaby.freshx.de/repo/binary/Linux/RPM, the sources are at https://github.com/FreshXOpenSource/nagios-couchdb

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/nagios/plugins/
cp check_couchdb $RPM_BUILD_ROOT/%{_libdir}/nagios/plugins/check_couchdb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/nagios/plugins/check_couchdb

%changelog
* Tue Oct 08 2013 Kai Mosebach
- check for empty couchStat values before converting to int
* Sat May 25 2013 Kai Mosebach
- Ready for nagios exchange and github
* Fri May 24 2013 Kai Mosebach
- Initial RPM of Version 0.93
