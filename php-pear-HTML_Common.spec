%define		_class		HTML
%define		_subclass	Common
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.5
Release:	7
Summary:	Base class for other HTML classes
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Common/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::HTML_Common package provides methods for HTML code display
and attributes handling:
- Methods to set, remove, update HTML attributes.
- Handles comments in HTML code.
- Handles layout and tabs for nicer HTML code.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-4mdv2011.0
+ Revision: 667500
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-3mdv2011.0
+ Revision: 607101
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.5-2mdv2010.1
+ Revision: 477860
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.5-1mdv2010.0
+ Revision: 383549
- update to new version 1.2.5

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-4mdv2009.1
+ Revision: 321815
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2009.0
+ Revision: 224735
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-2mdv2008.1
+ Revision: 171037
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2008.0
+ Revision: 28894
- 1.2.4

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdv2008.0
+ Revision: 15537
- 1.2.3


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdv2007.0
+ Revision: 81093
- Import php-pear-HTML_Common

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- 1.2.2

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-10mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-9mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-8mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-7mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdk
- fix deps

* Fri Jun 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-5mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.2.1-4mdk
- fix pre/post

* Sun Jan 04 2004 Pascal Terjan <pterjan@mandrake.org> 1.2.1-3mdk
-  Register into pear

* Thu Jan 01 2004 Pascal Terjan <pterjan@mandrake.org> 1.2.1-2mdk
- Fix dir ownership

* Mon Dec 29 2003 Pascal Terjan <pterjan@mandrake.org> 1.2.1-1mdk
- First mdk package

