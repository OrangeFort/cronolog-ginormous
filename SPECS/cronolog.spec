# No debugging packages, please!
%global  debug_package %{nil}
# Provide the upstream name for filesystem consistency
%define  _name         cronolog

Name:            cronolog-ginormous
Version:         1.6.2
Release:         1%{?repo}%{?dist}
Summary:         Web log rotation program for Apache, with 100% more Ginormous patch

Group:           Applications/System
License:         GPL 2
URL:             http://cronolog.org/
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Conflicts:       cronolog

Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

Source0:         http://cronolog.org/download/%{_name}-%{version}.tar.gz
Patch1:          cronolog-ginormous.patch

%description
cronolog is a simple filter program that reads log file entries from
standard input and writes each entry to the output file specified
by a filename template and the current date and time. When the
expanded filename changes, the current file is closed and a new one
opened. cronolog is intended to be used in conjunction with a Web server,
such as Apache, to split the access log into daily or monthly logs.

This build of cronolog has had the ginormous patch applied, which provides
added functionality like largefile support, changing umask, ownership, etc.

%prep
%setup -q -n %{_name}-%{version}
%patch1 -p1

%build
%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
sed -i 's|/www/sbin|/usr/sbin|g' %{buildroot}/%{_mandir}/man1/*
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{_sbindir}/cronosplit %{buildroot}/%{_bindir}
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{_name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/%{_name}.info %{_infodir}/dir || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%changelog
* Mon Sep 15 2014 Ryan McKern <ryan@orangefort.com> - 1.6.2-1
- Initial release
