%define upstream_name    Calendar-Simple
%define upstream_version v2.1.0

Name:		perl-%{upstream_name}
Version:	2.1.0
Release:	1

Summary:	Perl extension to create simple calendars
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/davorg-cpan/calendar-simple
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/Calendar-Simple-v2.1.0.tar.gz

BuildRequires:	make
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

