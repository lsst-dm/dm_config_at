#!/bin/bash
if [ -z ${DM_CONFIG_AT_RELEASE} ]; then
	echo "environment variable DM_CONFIG_AT_RELEASE has to be set"
	exit 1
fi
if [ -z ${DM_CONFIG_AT_DIR} ]; then
	echo "environment variable DM_CONFIG_AT_DIR has to be set"
	exit 1
fi
HERE=$PWD
PID=$$
echo $PID
mkdir -p /tmp/build.$PID
cd /tmp/build.$PID
mkdir -p BUILD BUILDROOT RPMS SOURCES SPECS  SRPMS
cp $DM_CONFIG_AT_DIR/etc/specs/dm_config_at.spec SPECS
cd SOURCES
wget https://github.com/lsst-dm/dm_config_at/archive/${DM_CONFIG_AT_RELEASE}.zip
cd ..
rpmbuild --define "_topdir `pwd`" --target noarch -bb SPECS/*spec
cd $HERE
