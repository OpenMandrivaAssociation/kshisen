Name:		kshisen
Version:	15.12.3
Release:	1
Epoch:		1
Summary:	Patience game where you take away all pieces
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kshisen
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkmahjongg-devel
Requires:	libkdegames-common
Requires:	kmahjongglib
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:  cmake(KF5CoreAddons)                                                                   
BuildRequires:  cmake(KF5XmlGui)                                                                       
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5KIO)                                                                          
BuildRequires:  cmake(KF5DNSSD)                                                                        
BuildRequires:  cmake(KF5NewStuff)                                                                     
BuildRequires:  cmake(KF5Declarative)                                                                  
BuildRequires:  cmake(KF5DocTools)
BuildRequires:	cmake(KF5KMahjongglib)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Phonon4Qt5)



%description
KShisen is a solitaire-like game played using the standard set of Mahjong
tiles. Unlike Mahjong however, KShisen has only one layer of scrambled tiles.

%files
%{_bindir}/kshisen                                                                                     
%{_datadir}/applications/org.kde.kshisen.desktop                                                          
%{_datadir}/sounds/kshisen   
%{_datadir}/kxmlgui5/kshisen/kshisenui.rc
%{_datadir}/config.kcfg/kshisen.kcfg                                                                   
%{_iconsdir}/hicolor/*/apps/kshisen*                                                                   
%doc %{_docdir}/*/*/kshisen
%_kde5_datadir/appdata/org.kde.kshisen.appdata.xml
   

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

