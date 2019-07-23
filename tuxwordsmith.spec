%define name	tuxwordsmith
%define version	0.7.13
%define release	3

Summary:        Multilanguage scrabble game
Name:           %{name}
Version:        %{version}
Release:	1
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-0.7.13-fix-path.patch
URL:            http://www.schoolforge.net/education-software/educational-games/tuxwordsmith
License:        GPLv2+ 
Group:          Games/Boards
BuildRequires:  imagemagick
Requires:   python-pygame
Requires:   wxPythonGTK
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}
 
%description
With TuxWordSmith you get Scrabble in English, French, German, Italian, Greek,
Latin , Dutch, Swahili, Spanish, Russian, Ukranian, Swedish, Icelandic,
Norwegian, Finnish, Brazillian-Portuguese, Arabic, Hindi, Turkish, Czech,
Kurdish, Hungarian and more, all in one application!

%prep
%setup -q -n %name-%version
%patch0 -p0

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}
cp -pr Font %{buildroot}%{_gamesdatadir}/%{name}
cp -pr xdxf %{buildroot}%{_gamesdatadir}/%{name}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}/lib
cp -pr TuxWordSmith %{buildroot}%{_gamesdatadir}/%{name}/lib
cp .tws_config_master  %{buildroot}%{_gamesdatadir}/%{name}

install -d -m 755 %{buildroot}%{_gamesbindir}
install -m 755 %{name}.py %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 48x48 tws.ico %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 32x32 tws.ico %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 16x16 tws.ico %{buildroot}%{_miconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=TuxWordSmith
Comment=Multilanguage scrabble game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-admin.desktop << EOF
[Desktop Entry]
Name=TuxWordSmith Admin
Comment=Multilanguage scrabble game with administration mode enabled
Exec=%{_gamesbindir}/%{name} -wx
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README CHANGES
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}*.desktop 
%{_iconsdir}/*



%changelog
* Sun Apr 17 2011 Angelo Naselli <anaselli@mandriva.org> 0.7.13-1mdv2011.0
+ Revision: 654799
- import tuxwordsmith

