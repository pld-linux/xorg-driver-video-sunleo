Summary:	X.org video driver for Sun Leo (ZX) video cards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Sun Leo (ZX)
Name:		xorg-driver-video-sunleo
Version:	1.2.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-sunleo-%{version}.tar.xz
# Source0-md5:	4d6f74b562f06c95f0067013012bb5de
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sunleo_drv.so
%{_mandir}/man4/sunleo.4*
