all:
	@echo -e "Valid targets :"
	@echo -e "\tinstall\t(Install myself either to /usr/lib/nagios/plugins"
	@echo -e "\t\t/usr/lib64/nagios/plugins or /usr/local/lib/nagios/plugins)"
	@echo -e "\traw-req \(requires pip and git\)"

install:
	@if [ -d /usr/lib/nagios/plugins ]; then cp check_couchdb /usr/lib/nagios/plugins; echo Installed.; fi
	@if [ -d /usr/lib64/nagios/plugins ]; then cp check_couchdb /usr/lib64/nagios/plugins;echo Installed.; fi
	@if [ -d /usr/local/lib/nagios/plugins ]; then cp check_couchdb /usr/local/lib/nagios/plugins; echo Installed.; fi

raw-req:
	pip install twisted
	git clone https://github.com/FreshXOpenSource/wallaby-backend-http || echo 'skip'
	(cd wallaby-backend-http; python setup.py install)
	rm -rf wallaby-backend-http
	git clone https://github.com/FreshXOpenSource/wallaby-backend-couchdb || echo 'skip'
	(cd wallaby-backend-couchdb; python setup.py install)
	rm -rf wallaby-backend-couchdb
