%define nspr_version 4.6
%define nss_version 3.11

Summary:          Secure PIN handling using NSS crypto
Name:             svrcore
Version:          __VERSION__
Release:          1%{?dist}
License:          MPL2.0
URL:              https://pagure.io/svrcore
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         nspr >= %{nspr_version}
Requires:         nss >= %{nss_version}
BuildRequires:    nspr-devel >= %{nspr_version}
BuildRequires:    nss-devel >= %{nss_version}
BuildRequires:    pkgconfig

Source0:            http://www.port389.org/binaries/%{name}-%{version}.tar.bz2

%description
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

%package devel
Summary: Development files for secure PIN handling using NSS crypto
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: nspr-devel >= %{nspr_version}
Requires: nss-devel >= %{nss_version}
Requires: pkgconfig

%description devel
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

This package contains header files and symlinks to develop programs which will
use the libsvrcore library.  You should install this package if you need to
develop programs which will use the svrcore library.

%prep
%setup -q

%build

%configure --with-systemd
make

%install
%{__rm} -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.la

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README NEWS
%{_libdir}/libsvrcore.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libsvrcore.so
%{_includedir}/svrcore.h

%changelog
* Thu Apr 21 2016 Noriko Hosoi <nhosoi@redhat.com> - 4.1.2
- Code quality improvements

* Thu Apr 14 2016 William Brown <wibrown@redhat.com> - 4.1.1
- Code quality and stability improvements
- Improvements to rpm tooling and features

* Fri Apr 8 2016 William Brown <wibrown@redhat.com> - 4.1.0
- Added systemd ask password support

* Tue Mar 13 2007 Rich Megginson <richm@stanfordalumni.org> - 4.0.4-1
- Removed some autoconf generated files which were GPL only - all
- code needs to be tri-licensed
- updated version to 4.0.4
- added empty COPYING file - do not use the one generated by autoreconf
- use bz2 for source tarball instead of gz

* Wed Dec 13 2006 Rich Megginson <richm@stanfordalumni.org> - 4.0.3.01-0
- Fixed support for windows build by moving old makefile to src/Makefile.win
- and updating instructions - I could not get configure/libtool to work
- with cygwin and the msvc compiler
- Added support for --with-nspr and --with-nss and finding nspr/nss
- "in-tree" when building with other mozilla components
- Use PK11_TokenKeyGenWithFlags instead of PK11_KeyGen

* Fri Dec 08 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 4.0.2.02-0
- Test build based on an second experimental autotools version of svrcore.

* Thu Dec 07 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 4.0.2.01-0
- Test build based on an experimental autotools version of svrcore.

* Thu Jul 13 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-3
- Bump spec rev to 3
- Remove unneeded buildrequires perl, gawk, sed
- Remove leading / from path macros
- Remove provides for package name - done automatically
- Move pkgconfig file stuff under install
- Added LICENSE and README under docs

* Mon Jun 26 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-2
- Bump spec rev to 2 due to change of spec file name from svrcore
- to svrcore-devel to comply with fedora packaging guidelines

* Thu Jun 22 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-1
- Bump rev to 4.0.2; now using HEAD of mozilla/security/coreconf
- which includes the coreconf-location.patch, so got rid of patch

* Tue Apr 18 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.1-3
- Use pkg-config --variable=includedir to get include dirs

* Wed Feb  1 2006 Rich <rmeggins@redhat.com> - 4.0.1-2
- Requires nss version was wrong

* Wed Jan 11 2006 Rich Megginson <rmeggins@redhat.com> - 4.01-1
- Removed svrcore-config - use pkg-config instead

* Mon Dec 19 2005 Rich Megginson <rmeggins@redhat.com> - 4.01-1
- Initial revision
