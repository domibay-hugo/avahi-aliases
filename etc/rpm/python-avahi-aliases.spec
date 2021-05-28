#
# spec file for package python-avahi-aliases
#



%define project_name avahi-aliases

Name:           python-%{project_name}
Version:        0.0.10
Release:        4+beta
Summary:        Simple python application that manages the announcement of multiple avahi aliases
URL:            http://github.com/airtonix/avahi-aliases
License:        BSD (see LICENSE)
Group:          System Environment/Networking
Source:         %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch

Requires:       avahi dbus
Requires:       python-avahi python-daemon


%description
Simple python application that manages the announcement of multiple avahi aliases

For usage instructions see README


%prep
%setup -q -n %{project_name}


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_exec_prefix}/local/bin/
mkdir -p %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_docdir}/%{name}

mv README %{buildroot}%{_docdir}/%{name}/
mv LICENSE %{buildroot}%{_docdir}/%{name}/
mv setup.py %{buildroot}%{_docdir}/%{name}/

mv avahi_aliases/etc/avahi %{buildroot}/etc/
mv avahi_aliases/etc/init %{buildroot}/etc/
mv avahi_aliases/bin/* %{buildroot}%{_exec_prefix}/local/bin/

cp etc/%{project_name}.service %{buildroot}%{_unitdir}/%{project_name}.service

rm -f %{buildroot}%{_docdir}/%{name}/*.pyc
rm -f %{buildroot}%{_docdir}/%{name}/*.pyo


%clean
rm -rf $RPM_BUILD_ROOT


%post
%systemd_post %{project_name}.service

%preun
%systemd_preun %{project_name}.service

%postun
%systemd_postun_with_restart %{project_name}.service


%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/setup.py*
%{_exec_prefix}/local/bin/avahi-alias
%{buildroot}%{_unitdir}/%{project_name}.service
%{_sysconfdir}/init/%{project_name}.conf
%config(noreplace) %{_sysconfdir}/avahi/aliases
%config(noreplace) %{_sysconfdir}/avahi/aliases.d
