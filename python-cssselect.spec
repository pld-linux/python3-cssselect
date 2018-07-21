#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests [tests missing in archive as of 1.0.3]
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
#
%define 	module	cssselect
Summary:	Python moudle for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Name:		python-%{module}
Version:	1.0.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/cssselect/
Source0:	https://files.pythonhosted.org/packages/source/c/cssselect/%{module}-%{version}.tar.gz
# Source0-md5:	50422c9ec04b74cd60c571f74ddc1a80
URL:		http://packages.python.org/cssselect/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-lxml
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-lxml
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
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

%package -n python3-%{module}
Summary:	Python moudle for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document. This
module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
# no Makefile...
cd docs
PYTHONPATH=$(pwd)/.. \
sphinx-build -b html . _build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py_sitescriptdir}/cssselect
%{py_sitescriptdir}/cssselect-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py3_sitescriptdir}/cssselect
%{py3_sitescriptdir}/cssselect-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
