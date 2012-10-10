#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	cssselect
Summary:	Python moudle for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
# Name must match the python module/package name (as in 'import' statement)
######		/home/users/matkor/rpm/packages/../rpm-build-tools/rpm.groups: no such file
Name:		python-%{module}
Version:	0.7.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c6c5e9a2e7ca226ce03f6f67a771379c
URL:		http://packages.python.org/cssselect/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# remove BR: python-devel for 'noarch' packages.
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
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

%prep
%setup -q -n %{module}-%{version}

# fix #!%{_bindir}/env python -> #!%{_bindir}/python:
# %{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}.py

%build
# CC/CFLAGS is only for arch packages - remove on noarch packages
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
# %{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
# %{py_sitescriptdir}/%{name}-%{version}
%{py_sitescriptdir}/%{module}
