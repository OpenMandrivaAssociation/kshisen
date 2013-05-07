Name:		kshisen
Version:	4.10.3
Release:	1
Epoch:		1
Summary:	Patience game where you take away all pieces
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kshisen
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkmahjongg-devel
Requires:	libkdegames-common
Requires:	kmahjongglib

%description
KShisen is a solitaire-like game played using the standard set of Mahjong
tiles. Unlike Mahjong however, KShisen has only one layer of scrambled tiles.

%files
%{_kde_bindir}/kshisen
%{_kde_applicationsdir}/kshisen.desktop
%{_kde_appsdir}/kshisen
%{_kde_datadir}/sounds/kshisen
%{_kde_datadir}/config.kcfg/kshisen.kcfg
%{_kde_iconsdir}/hicolor/*/apps/kshisen*
%{_kde_docdir}/*/*/kshisen

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

