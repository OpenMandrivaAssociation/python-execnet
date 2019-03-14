# Created by pyp2rpm-2.0.0
%global pypi_name execnet
%global with_python2 1
%define version 1.5.0

Name:           python-%{pypi_name}
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        Execnet provides a tested means to interact with interpreters across version, platform and network barriers. 

License:        MIT
URL:            https://codespeak.net/execnet/
Source0:        https://files.pythonhosted.org/packages/ab/c0/9496c35092eac2523ee8993ca3690b2d0aa95ef56623035b9c890745ac55/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
Execnet provides carefully tested means to ad-hoc interact with Python interpreters across version, 
platform and network barriers. It provides a minimal and fast API targetting the following uses:
To distribute tasks to local or remote processes, write and deploy 
hybrid multi-process applications and to write scripts to administer multiple hosts


%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        Execnet provides a tested means to interact with interpreters across version, platform and network barriers. 

%description -n python2-%{pypi_name}
Execnet provides carefully tested means to ad-hoc interact with Python interpreters across version, 
platform and network barriers. It provides a minimal and fast API targetting the following uses:
To distribute tasks to local or remote processes, write and deploy 
hybrid multi-process applications and to write scripts to administer multiple hosts

%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  ISSUES.txt README.rst CHANGELOG.rst LICENSE
%{python_sitelib}/*/*
#%%{python_sitelib}/pep8.py


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  ISSUES.txt README.rst CHANGELOG.rst LICENSE
%{python2_sitelib}/*/*
#%%{python2_sitelib}/pep8.*
%endif # with_python2

