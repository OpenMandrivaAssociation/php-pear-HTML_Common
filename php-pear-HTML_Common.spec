%define	_class		HTML
%define	_subclass	Common
%define	modname	%{_class}_%{_subclass}

Summary:	Base class for other HTML classes
Name:		php-pear-%{modname}
Version:	1.2.5
Release:	7
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTML_Common/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
The PEAR::HTML_Common package provides methods for HTML code display
and attributes handling:
- Methods to set, remove, update HTML attributes.
- Handles comments in HTML code.
- Handles layout and tabs for nicer HTML code.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

