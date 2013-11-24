%define		php_name	php%{?php_suffix}
%define		modname	KTagLib
%define		modname2	ktaglib
%define		status		beta
Summary:	library to edit audio properties and tags on MPEG and OGG files
Summary(pl.UTF-8):	biblioteka do edycji informacji w plikach MPEG i OGG
Name:		%{php_name}-pecl-%{modname2}
Version:	0.2.0
Release:	7
License:	Modified BSD
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	8c363e8c96eedd21ea652b280369d59b
URL:		http://pecl.php.net/package/KTaglib/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.650
BuildRequires:	taglib-devel >= 1.5
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTaglib is a PHP binding for the KDE taglib, which reads and writes
tags for various audio files.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
KTaglib to dowiązania PHP do biblioteki KDE, pozwalającej na odczyt i
zapis metadanych w róznych plikach audio.

To rozszerzenie ma w PECL status: %{status}.

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
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname2}.ini
; Enable %{modname2} extension module
extension=%{modname2}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname2}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname2}.so
