#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : packaging
Version  : 17.1
Release  : 15
URL      : https://pypi.debian.net/packaging/packaging-17.1.tar.gz
Source0  : https://pypi.debian.net/packaging/packaging-17.1.tar.gz
Summary  : Core utilities for Python packages
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: packaging-python3
Requires: packaging-python
Requires: pyparsing
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
=========
        
        Core utilities for Python packages
        
        
        Documentation
        -------------
        
        `documentation`_
        
        
        Discussion
        ----------
        
        If you run into bugs, you can file them in our `issue tracker`_.
        
        You can also join ``#pypa`` on Freenode to ask questions or get involved.

%package python
Summary: python components for the packaging package.
Group: Default
Requires: packaging-python3

%description python
python components for the packaging package.


%package python3
Summary: python3 components for the packaging package.
Group: Default
Requires: python3-core

%description python3
python3 components for the packaging package.


%prep
%setup -q -n packaging-17.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523293264
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
