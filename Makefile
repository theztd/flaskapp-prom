
deb:
	@echo "Build deb package"
	cp -a src flaskapp/opt/flaskapp
	dpkg-deb -b flaskapp
	
check:
	@echo "Check builded package"
	dpkg --install flaskapp.deb

