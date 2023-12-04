#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-URI-Find
Version  : 20160806
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/URI-Find-20160806.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/URI-Find-20160806.tar.gz
Summary  : 'Find URIs in arbitrary text'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-URI-Find-bin = %{version}-%{release}
Requires: perl-URI-Find-license = %{version}-%{release}
Requires: perl-URI-Find-man = %{version}-%{release}
Requires: perl-URI-Find-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
URI::Find - Find URIs in arbitrary text
SYNOPSIS
require URI::Find;

my $finder = URI::Find->new(\&callback);

$how_many_found = $finder->find(\$text);

%package bin
Summary: bin components for the perl-URI-Find package.
Group: Binaries
Requires: perl-URI-Find-license = %{version}-%{release}

%description bin
bin components for the perl-URI-Find package.


%package dev
Summary: dev components for the perl-URI-Find package.
Group: Development
Requires: perl-URI-Find-bin = %{version}-%{release}
Provides: perl-URI-Find-devel = %{version}-%{release}
Requires: perl-URI-Find = %{version}-%{release}

%description dev
dev components for the perl-URI-Find package.


%package license
Summary: license components for the perl-URI-Find package.
Group: Default

%description license
license components for the perl-URI-Find package.


%package man
Summary: man components for the perl-URI-Find package.
Group: Default

%description man
man components for the perl-URI-Find package.


%package perl
Summary: perl components for the perl-URI-Find package.
Group: Default
Requires: perl-URI-Find = %{version}-%{release}

%description perl
perl components for the perl-URI-Find package.


%prep
%setup -q -n URI-Find-20160806
cd %{_builddir}/URI-Find-20160806

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-URI-Find
cp %{_builddir}/URI-Find-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-URI-Find/33588c7e464ec9e25c0a768a4ca6381bc8e7e530 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/urifind

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI::Find.3
/usr/share/man/man3/URI::Find::Schemeless.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-URI-Find/33588c7e464ec9e25c0a768a4ca6381bc8e7e530

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/urifind.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
