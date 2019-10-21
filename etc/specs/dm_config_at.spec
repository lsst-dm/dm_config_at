%define lsstpath /opt/lsst/dm_config_at
%define gitrelease %{getenv:DM_CONFIG_AT_RELEASE}
%define user ARC

Name:		dm_config_at
Version:	1.0.0
Release:	1%{?dist}
Summary:	configuration for dm_ATArchiver CSC

Group:		LSST
License:	GPL
URL:		http://www.lsst.org
Source0:	https://github.com/lsst/dm_config_at/archive/%{gitrelease}.zip

%description
Configuration information used by the salobj csc classes for dm_ATArchiver


%prep
%setup -q -n dm_config_at-%{gitrelease}


%build


%install
install -d %{buildroot}%{lsstpath}/ATArchiver %{buildroot}%{lsstpath}/ATArchiver/v1
install -m 755 -D ATArchiver/v1/normal.yaml %{buildroot}%{lsstpath}/ATArchiver/v1


%files
%defattr(755, %{user}, %{user}, 755)
%lsstpath/ATArchiver/v1/*

%doc



%changelog

