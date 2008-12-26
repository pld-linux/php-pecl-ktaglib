%define		_modname	KTagLib
%define		_modname2	ktaglib
%define		_status		beta
Summary:	library to edit audio properties and tags on MPEG and OGG files
Summary(pl.UTF-8):	biblioteka do edycji informacji w plikach MPEG i OGG
Name:		php-pecl-%{_modname2}
Version:	0.2.0
Release:	1
License:	Modified BSD
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	8c363e8c96eedd21ea652b280369d59b
URL:		http://pecl.php.net/package/KTaglib/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
BuildRequires:	taglib-devel
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTaglib is a PHP binding for the KDE taglib, which reads and writes
tags for various audio files.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
KTaglib to dowiązania PHP do biblioteki KDE, pozwalającej na odczyt i
zapis metadanych w róznych plikach audio.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
mv KTaglib-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	EXTENSION_DIR=%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname2}.ini
; Enable %{_modname2} extension module
extension=%{_modname2}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname2}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname2}.so
