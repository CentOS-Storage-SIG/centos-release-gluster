%global altarch 0
%if ( 0%{?centos} >= 7 )
%ifnarch x86_64
# altarch is only available for CentOS-7, non c86_64
%global altarch 1
%endif
%endif

Summary: Gluster 4.1 (Long Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster41
Version: 0.9
# The .centos dist extension seems to be missing from the CBS rpm macros?
Release: 1%{?dist}.centos
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-4.1.repo

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-gluster = 4.1

# Obsoletes: for 4.0 only, 4.0 is EOL when 4.1 is released
Obsoletes: centos-release-gluster40
# No Conflicts:, possibly older repositories contain additional tools and those
# are still expected to be working.

%description
yum configuration for Gluster 4.1 packages from the CentOS Storage SIG.
Gluster 4.1 is a Long Term Stable release and will receive updates for
approximately 12 months. For more details about the Long Term Stable and Short
Term Stable release schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.1.repo
%if %{altarch}
sed -i -e "s,@BASEURL@,http://mirror.centos.org/altarch," %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.1.repo
%else
sed -i -e "s,@BASEURL@,http://mirror.centos.org/centos," %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.1.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.1.repo

%changelog
* Sat Jun 2 2018 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster40
- Only the centos-gluster41-test repo is enabled during Beta

* Thu Mar 15 2018 Niels de Vos <ndevos@redhat.com> - 1.0-3
- Fix altarch detection for .el6/i686

* Thu Mar 15 2018 Niels de Vos <ndevos@redhat.com> - 1.0-2
- Correct the repository URL

* Wed Mar 7 2018 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Disable centos-gluster40-test, enable centos-gluster40 repo

* Fri Jan 12 2018 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster313
- Only the centos-gluster40-test repo is enabled during Beta
