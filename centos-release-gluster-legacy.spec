Summary: Disable unmaintained Gluster repositories from the CentOS Storage SIG
Name: centos-release-gluster-legacy
Version: 4.0
Release: 3%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
BuildArch: noarch
Source0: README.warn

# WARN: only have a single Provides: to work around rhbz#1657753
Provides: centos-release-gluster = 4.0
Obsoletes: centos-release-gluster40
Conflicts: centos-release-gluster40

# only deprecate LTM releases, STM should get upgraded with the next LTM
#Provides: centos-release-gluster = 3.12
Obsoletes: centos-release-gluster312
Conflicts: centos-release-gluster312

#Provides: centos-release-gluster = 3.10
Obsoletes: centos-release-gluster310
Conflicts: centos-release-gluster310

#Provides: centos-release-gluster = 3.8
Obsoletes: centos-release-gluster38
Conflicts: centos-release-gluster38

#Provides: centos-release-gluster = 3.7
Obsoletes: centos-release-gluster37
Conflicts: centos-release-gluster37

#Provides: centos-release-gluster = 3.6
Obsoletes: centos-release-gluster36
Conflicts: centos-release-gluster36


%description
When this package is installed, an unmaintained Gluster version was available
on this system. In order to prevent problems when the YUM repository
disappears, this package removed the old .repo files.

It is recommended to deploy Gluster environments with planning for timely
upgrades to keep using a maintained version. For more details about the
maintenance and release schedule, see
https://www.gluster.org/community/release-schedule

%build
cp %{SOURCE0} README

%files
%doc README

%changelog
* Fri Feb 22 2019 Niels de Vos <ndevos@redhat.com> - 4.0-3
- Place README in the correct package doc directory

* Mon Dec 10 2018 Niels de Vos <ndevos@redhat.com> - 4.0-2
- Drop unneeded Provides: to work around YUM bug (rhbz#1657753)

* Wed Dec 5 2018 Niels de Vos <ndevos@redhat.com> - 4.0-1
- Deprecate centos-release-gluster40

* Fri Nov 2 2018 Niels de Vos <ndevos@redhat.com> - 3.12-1
- Deprecate centos-release-gluster312

* Mon Jun 25 2018 Niels de Vos <ndevos@redhat.com> - 3.10-1
- Remove unmaintained centos-release-gluster* <= 3.10 versions
