# Conditional build:
%bcond_without  doc             # don't build doc
%bcond_without  tests   # do not perform "make test"
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
#
%define 	module	cssselect
Summary:	Python moudle for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Name:		python-%{module}
Version:	0.9.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c74f45966277dc7a0f768b9b0f3522ac
URL:		http://packages.python.org/cssselect/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%if %{with tests}
BuildRequires:	python-lxml
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%if %{with tests}
BuildRequires:	python3-lxml
%endif
%endif
Requires:	python-modules
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
1.0. Owe wyreażenia mogą być późnije użyte w lxml lub w innym kodzie
XPath do znajdywania pasujących elementów w dokumentach XML lub HTML.
Ten moduł był częścią lxml jako lxml.cssselct zanim został wydzielony
jako osobny projekt.

%package -n python3-%{module}
Summary:	Python moudle for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document. This
module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%description -n python3-%{module} -l pl.UTF-8
cssselect interpretuje selektory CSS3 i tłumaczy je na wyrażenia XPath
1.0. Owe wyreażenia mogą być późnije użyte w lxml lub w innym kodzie
XPath do znajdywania pasujących elementów w dokumentach XML lub HTML.
Ten moduł był częścią lxml jako lxml.cssselct zanim został wydzielony
jako osobny projekt.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
%{py_sitescriptdir}/%{module}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
