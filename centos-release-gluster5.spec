Summary: Gluster 5 packages from the CentOS Storage SIG repository
Name: centos-release-gluster5
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-5.repo
BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%endif
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-gluster = 5

%description
yum configuration for Gluster 5 packages from the CentOS Storage SIG.  Gluster
5 will receive updates for approximately 12 months. For more details about the
release and maintenance schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-5.repo
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-5.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-5.repo

%changelog
* Fri Oct 19 2018 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Use mirrorlist.c.o for the main repository
- Disable centos-gluster5-test, enable centos-gluster5 repository

* Mon Sep 17 2018 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster41
- Only the centos-gluster5-test repo is enabled during pre-release
