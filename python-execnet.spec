Name:		python-execnet
Version:	2.1.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/e/execnet/execnet-%{version}.tar.gz
Summary:	execnet: rapid multi-Python deployment
URL:		https://pypi.org/project/execnet/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch
# Not really, but we have to get rid of py2 cruft on updates...
Obsoletes:	python2-execnet

%description
execnet: rapid multi-Python deployment

%prep
%autosetup -p1 -n execnet-%{version}

%files
%{py_sitedir}/execnet
%{py_sitedir}/execnet-*.*-info
