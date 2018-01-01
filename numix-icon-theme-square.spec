%global commit 084e0ae8a956c4ad6e19af81e3ad3c5fa9e2198f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           numix-icon-theme-square
Version:        0.1.0
Release:        1.git%{shortcommit}%{?dist}
Summary:        Numix Project square icon theme
License:        GPLv3

URL:            https://github.com/numixproject/numix-icon-theme-square
Source:         https://github.com/numixproject/numix-icon-theme-square/archive/%{commit}.tar.gz#/numix-icon-theme-square-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       numix-icon-theme

%description
Numix Square is a modern icon theme for Linux from the Numix project.

%prep
%autosetup -n %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -r Numix-Square %{buildroot}%{_datadir}/icons/Numix-Square
cp -r Numix-Square-Light %{buildroot}%{_datadir}/icons/Numix-Square-Light

%post
touch -c %{_datadir}/icons/Numix-Square &>/dev/null || :
touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch -c %{_datadir}/icons/Numix-Square &>/dev/null
    touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Numix-Square
%{_datadir}/icons/Numix-Square-Light

%changelog
* Mon Jan 01 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-1.git
- Initial packaging


