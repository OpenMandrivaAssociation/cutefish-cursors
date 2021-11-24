%define  _name  cutefish
Name:           cutefish-cursors
Version:        @SERVICE@
Release:        0
Summary:        Cutefish Desktop Cursors Theme
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/cutefishos/cursor-themes
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
#equires:       gtk3-tools
BuildArch:      noarch

%description
Dark and Light cursors for Cutefish Desktop

%prep
%autosetup

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/icons/
cp -a %{_name}-light %{buildroot}%{_datadir}/icons/
cp -a %{_name}-dark %{buildroot}%{_datadir}/icons/
find %{buildroot}%{_datadir}/icons -type f -exec chmod 0644 {} \;
find -L %{buildroot}%{_datadir}/icons -type l -delete -print

%fdupes -s %{buildroot}%{_datadir}/icons/

%files
%doc README.md
%{_datadir}/icons/%{_name}*/
#%%license LICENSE
