#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
#
%define		module	cssselect
Summary:	Python module for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł Pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Name:		python3-%{module}
Version:	1.3.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/cssselect/
Source0:	https://files.pythonhosted.org/packages/source/c/cssselect/%{module}-%{version}.tar.gz
# Source0-md5:	e0148abb13430399cbdbc173c3fa1c80
URL:		http://packages.python.org/cssselect/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-lxml
%endif
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document. This
module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%description -l pl.UTF-8
cssselect interpretuje selektory CSS3 i tłumaczy je na wyrażenia XPath
1.0. Owe wyreażenia mogą być później użyte w lxml lub w innym kodzie
XPath do znajdywania pasujących elementów w dokumentach XML lub HTML.
Ten moduł był częścią lxml jako lxml.cssselect zanim został wydzielony
jako osobny projekt.

%package apidocs
Summary:	API documentation for Python cssselect module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cssselect
Group:		Documentation

%description apidocs
API documentation for Python cssselect module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cssselect.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
# no Makefile...
cd docs
PYTHONPATH=$(pwd)/.. \
sphinx-build -b html . _build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py3_sitescriptdir}/cssselect
%{py3_sitescriptdir}/cssselect-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
