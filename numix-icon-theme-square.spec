%global commit 307e74299ea5cdb373db069d569c0caec19f5068
%global gittag 18.08.29

%global gitdate %(date -d %(echo %{gittag} | tr -d '.') +%Y%m%d)
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           numix-icon-theme-square
Version:        0.1.0
Release:        2.%{gitdate}.git%{shortcommit}%{?dist}
Summary:        Numix Project square icon theme
License:        GPLv3

URL:            https://github.com/numixproject/numix-icon-theme-square
Source:         https://github.com/numixproject/numix-icon-theme-square/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch
Requires:       numix-icon-theme

%description
Numix Square is a modern icon theme for Linux from the Numix project.

%prep
%autosetup -n %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -pr Numix-Square %{buildroot}%{_datadir}/icons/Numix-Square
cp -pr Numix-Square-Light %{buildroot}%{_datadir}/icons/Numix-Square-Light

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
* Wed Aug 29 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-2.20180829.git307e742
- Update to release 18.08.29

* Sun Jul 22 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-2.20180717.git9fc27a9
- Accept new git tag date format

* Mon Jan 01 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-1.20171225.git084e0ae
- Initial packaging
