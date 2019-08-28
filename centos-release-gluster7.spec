Summary: Gluster 7 packages from the CentOS Storage SIG repository
Name: centos-release-gluster7
Version: 0.1
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-7.repo
Source1: 75-gluster.preset
%if 0%{?centos} >= 7
BuildRequires: systemd
%endif
BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%systemd_requires
%endif
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-gluster = 7

%description
yum configuration for Gluster 7 packages from the CentOS Storage SIG. Gluster
7 will receive updates for approximately 12 months. For more details about the
release and maintenance schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-7.repo
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-7.repo
%endif
%if 0%{?centos} >= 7
install -D -m 644 %{SOURCE1} %{buildroot}%{_presetdir}/$(basename %{SOURCE1})
%endif

%if 0%{?centos} >= 7
%post
%systemd_post

%preun
%systemd_preun

%postun
%systemd_postun
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-7.repo
%if 0%{?centos} >= 7
%{_presetdir}/75-gluster.preset
%endif

%changelog
* Wed Aug 28 2019 Niels de Vos <ndevos@redhat.com> - 0.1-1
- Initial version based on centos-release-gluster6
- Only the centos-gluster7-test repo is enabled during pre-release
