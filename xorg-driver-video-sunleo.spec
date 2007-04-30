Summary:	X.org video driver for Sun Leo (ZX) video cards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Sun Leo (ZX)
Name:		xorg-driver-video-sunleo
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sunleo-%{version}.tar.bz2
# Source0-md5:	0408d95795d754c92d12d6476b6932a1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-sunleo < 1:7.0.0
Obsoletes:	XFree86-driver-sunleo < 1:7.0.0
ExclusiveArch:	sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Sun Leo (ZX) video cards. It supports all Sun
stations that include a Leo (also known as ZX, TZX, TurboZX) chipset:
- Sun 4/15, 4/30, 4/75,
- SPARCstation 5, 10, 20
- Ultra 1, 1E, 2
and servers:
- SPARCserver 1000
- SPARCcenter 2000

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Sun Leo (ZX). Obsługuje
wszystkie stacje robocze Suna zawierające układ Leo (znany także jako
ZX, TZX, TurboZX):
- Sun 4/15, 4/30, 4/75,
- SPARCstation 5, 10, 20
- Ultra 1, 1E, 2
oraz serwery:
- SPARCserver 1000
- SPARCcenter 2000

%prep
%setup -q -n xf86-video-sunleo-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sunleo_drv.so
%{_mandir}/man4/sunleo.4*
