%global pypi_name execnet
%bcond_without python2

Name:           python-%{pypi_name}
Version:	1.9.0
Release:	2
Group:          Development/Python
Summary:        Execnet provides a tested means to interact with interpreters across version, platform and network barriers. 

License:        MIT
URL:            https://codespeak.net/execnet/
Source0:	https://files.pythonhosted.org/packages/source/e/execnet/execnet-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-setuptools_scm
 
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
%endif # if with python2

%description
Execnet provides carefully tested means to ad-hoc interact with Python 
interpreters across version, platform and network barriers. It provides 
a minimal and fast API targetting the following uses: To distribute tasks to 
local or remote processes, write and deploy hybrid multi-process applications 
and to write scripts to administer multiple hosts


%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Execnet provides a tested means to interact with interpreters across version, platform and network barriers. 

%description -n python2-%{pypi_name}
Execnet provides carefully tested means to ad-hoc interact with Python.
interpreters across version, platform and network barriers. It provides.
a minimal and fast API targetting the following uses: To distribute tasks to.
local or remote processes, write and deploy hybrid multi-process applications.
and to write scripts to administer multiple hosts

%endif # with python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with python2


%build
%{__python} setup.py build

%if %{with python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with python2


%install

%if %{with python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc ISSUES.txt README.rst CHANGELOG.rst LICENSE
%{python_sitelib}/execnet
%{python_sitelib}/*.egg-info*


%if %{with python2}
%files -n python2-%{pypi_name}
%doc  ISSUES.txt README.rst CHANGELOG.rst LICENSE
%{python2_sitelib}/execnet
%{python2_sitelib}/*.egg-info*
%endif # with python2
