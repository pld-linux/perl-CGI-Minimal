#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Minimal
Summary:	CGI::Minimal - a lightweight CGI form processing package
Summary(pl.UTF-8):	CGI::Minimal - lekki pakiet do przetwarzania formularzy CGI
Name:		perl-CGI-Minimal
Version:	1.29
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76c659dc5f32018d2158d2427d549f35
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a micro-weight alternative to the CPAN CGI.pm
module. Rather than attempt to address every possible need of a CGI
programmer, it provides the _minimum_ functions needed for CGI such as
form decoding (including file upload forms), URL encoding and
decoding, HTTP usable date generation (RFC1123 compliant dates) and
_basic_ escaping and unescaping of HTMLized text.

The form decoding interface is somewhat compatible with the CGI.pm
module. No provision is made for generating HTTP or HTML on your
behalf - you are expected to be conversant with how to put together
any HTML or HTTP you need.

%description -l pl.UTF-8
Ten pakiet dostarcza bardzo lekką alternatywę dla modułu CPAN CGI.pm.
Zamiast próbować sprostać wszelkim możliwym potrzebom programisty CGI,
ten moduł dostarcza _minimalne_ funkcje potrzebne dla CGI, takie jak
dekodowanie formularzy (włącznie z przysyłaniem plików), kodowanie i
dekodowanie URL-i, generowanie użytecznego w HTTP formatu daty
(zgodnego z RFC1123) oraz _podstawowe_ traktowanie znaków specjalnych
(escape/unescape) w tekście HTML.

Interfejs do dekodowania formularzy jest częściowo kompatybilny z
modułem CGI.pm. Natomiast nie ma generowania HTTP czy HTML za
programistę - to on ma wiedzieć, jak umieścić potrzebny mu HTML czy
HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/CGI/Minimal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/CGI/Minimal.pm
%{perl_vendorlib}/CGI/Minimal
%{_mandir}/man3/*
