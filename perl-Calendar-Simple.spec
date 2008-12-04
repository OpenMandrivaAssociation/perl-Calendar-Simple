Summary:	Perl extension to create simple calendars
Name:		perl-Calendar-Simple
Version:	1.20
Release:	%mkrel 1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Calendar-Simple/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Calendar-Simple-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Required by the tests
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Perl extension to create simple calendars.

%prep

%setup -q -n Calendar-Simple-%{version}

chmod -x lib/*/Simple.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/pcal
%{perl_vendorlib}/Calendar
%{_mandir}/man3/*

