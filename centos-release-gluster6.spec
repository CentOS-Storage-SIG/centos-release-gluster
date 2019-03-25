Summary: Gluster 6 packages from the CentOS Storage SIG repository
Name: centos-release-gluster6
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-6.repo
BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%endif
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-gluster = 6

%description
yum configuration for Gluster 6 packages from the CentOS Storage SIG. Gluster
6 will receive updates for approximately 12 months. For more details about the
release and maintenance schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-6.repo
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-6.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-6.repo

%changelog
* Mon Mar 25 2019 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Gluster 6 has been released, reflect that in the ,repo file

* Fri Feb 22 2019 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster5
- Only the centos-gluster6-test repo is enabled during pre-release
