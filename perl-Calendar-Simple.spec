%define upstream_name    Calendar-Simple
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension to create simple calendars
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Calendar-Simple/
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(ExtUtils::MakeMaker)
# Required by the tests
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
