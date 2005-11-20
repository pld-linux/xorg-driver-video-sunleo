Summary:	X.org video driver for Sun Leo (ZX) video cards
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Sun Leo (ZX)
Name:		xorg-driver-video-sunleo
Version:	1.0.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-sunleo-%{version}.tar.bz2
# Source0-md5:	2736c74a272ffa431d754ec2a128fd29
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
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

%description -l pl
Sterownik obrazu X.org dla kart graficznych Sun Leo (ZX). Obs³uguje
wszystkie stacje robocze Suna zawieraj±ce uk³ad Leo (znany tak¿e jako
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sunleo_drv.so
%{_mandir}/man4/sunleo.4x*
