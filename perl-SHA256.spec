%define upstream_name    SHA256
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    A module that implements the NIST SHA-256/384/512 hash
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}b.tar.gz
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The *sha256* module allows you to use the NIST SHA 256/384/512 hash
algorithm.

A new sha256 context object is created with the *new* operation followed by
a digest size which may be either 256, 384, or 512 bits. Multiple
simultaneous digest context can be maintained if desired. The context is
updated with the *add* operation which adds the strings contained in the
_LIST_ parameter.

The final message digest value is returned by the *digest* operation as a
32-, 48-, or 64-byte binary string. This operation delivers the result of
operations since the last *new* or *reset* operation. Once the operation
has been performed, the context must be *reset* before being used to
calculate another digest value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 556143
- rebuild for perl 5.12

* Sun Jan 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 486070
- import perl-SHA256


* Sun Jan 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.0-1mdv2010.1
- initial mdv release, generated with cpan2dist
