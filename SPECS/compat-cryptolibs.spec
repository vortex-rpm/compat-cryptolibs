%global		_boost_ver	1_48_0
%global		_db_ver		5.3.28
%global		_openssl_ver	1.0.1e

%global		_dest		/opt/cryptolibs

Name:           compat-cryptolibs
Version:        1.0
Release:        1.vortex%{?dist}
Summary:        Libs required for cryptocurrencies
Vendor:         Vortex RPM
Source0:	boost_%{_boost_ver}.tar.bz2
Source1:	db-%{_db_ver}.tar.gz
Source2:	openssl-%{_openssl_ver}.tar.gz

Group:          System Environment/Libraries
License:        GPL
URL:            http://localhost
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  python-devel, python-pip, python-nose, python-virtualenv

%description
Used to build cryptocurrencies.

%prep
tar xf %{SOURCE0}
tar xf %{SOURCE1}
tar xf %{SOURCE2}

%build
cd boost_%{_boost_ver}
./bootstrap.sh --prefix=%{_dest}
cd ..
cd db-%{_db_ver}/build_unix
../dist/configure --enable-cxx --prefix=%{_dest}
make
cd ../..
cd openssl-%{_openssl_ver}
./configure --prefix=%{_dest}
make
cd ..

%install
cd boost_%{_boost_ver}
./bjam install
cd ..
cd db-%{_db_ver}/build_unix
make install
cd ..
cd openssl-%{_openssl_ver}
make install
cd ..

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_dest}

%changelog
* Sat Dec 21 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.0-1.vortex
- Initial packaging.

