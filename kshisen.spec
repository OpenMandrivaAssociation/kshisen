#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		kshisen
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
Summary:	Patience game where you take away all pieces
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=kshisen
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kshisen/-/archive/%{gitbranch}/kshisen-%{gitbranchd}.tar.bz2#/kshisen-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kshisen-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:	cmake(KMahjongglib6)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(Phonon4Qt6)

%rename plasma6-kshisen

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KShisen is a solitaire-like game played using the standard set of Mahjong
tiles. Unlike Mahjongg however, KShisen has only one layer of scrambled tiles.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kshisen.categories
%{_bindir}/kshisen
%{_datadir}/applications/org.kde.kshisen.desktop
%{_datadir}/sounds/kshisen
%{_datadir}/config.kcfg/kshisen.kcfg
%{_iconsdir}/hicolor/*/apps/kshisen*
%{_datadir}/metainfo/org.kde.kshisen.appdata.xml
