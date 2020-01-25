%define		_status		alpha
%define		_pearname	Validate_ES
Summary:	%{_pearname} - Validation class for ES
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Hiszpanii
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2092a7370b04d99e1b1b578436e8fcde
URL:		http://pear.php.net/package/Validate_ES/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for ES such as:
- DNI

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa do sprawdzania poprawności dla Hiszpanii danych takich jak:
- DNI

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/ES.php
