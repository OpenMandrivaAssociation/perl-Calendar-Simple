%define upstream_name    Calendar-Simple
%define upstream_version 1.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension to create simple calendars
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/Calendar-Simple/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
# Required by the tests
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
Perl extension to create simple calendars.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod -x lib/*/Simple.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%files
%doc Changes README
%{_bindir}/pcal
%{perl_vendorlib}/Calendar
%{_mandir}/man3/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.210.0-2mdv2011.0
+ Revision: 680713
- mass rebuild

* Thu Jul 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 563186
- update to new version 1.21

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 402987
- rebuild using %%perl_convert_version

* Thu Dec 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.20-1mdv2009.1
+ Revision: 309992
- import perl-Calendar-Simple


* Thu Dec 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.20-1mdv2009.0
- initial Mandriva package (fedora import)

* Tue Jul 08 2008 Ralf Corsépius <rc040203@freenet.de> - 1.20-1
- Upstream update.

* Tue Mar 11 2008 Ralf Corsépius <rc040203@freenet.de> - 1.19-1
- Upstream update.
- Reflect upstream having dropped "COPYING".

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.17-3
Rebuild for new perl

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.17-2
- Update license tag.
- Reflect perl package split.

* Thu Oct 19 2006 Ralf Corsépius <rc040203@freenet.de> - 1.17-1
- Upstream update.

* Sat Oct 07 2006 Ralf Corsépius <rc040203@freenet.de> - 1.14-2
- chmod -x files with broken permissions.

* Mon Sep 18 2006 Ralf Corsépius <rc040203@freenet.de> - 1.14-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-4
- Mass rebuild.

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-3
- Fix indentation.

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-2
- Fix Source0.

* Thu Jun 22 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-1
- FE submission.
