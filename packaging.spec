#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6E3CBCE93372DCFA (donald@stufft.io)
#
Name     : packaging
Version  : 16.8
Release  : 8
URL      : https://pypi.debian.net/packaging/packaging-16.8.tar.gz
Source0  : https://pypi.debian.net/packaging/packaging-16.8.tar.gz
Source99 : https://pypi.debian.net/packaging/packaging-16.8.tar.gz.asc
Summary  : Core utilities for Python packages
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: packaging-legacypython
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

%package legacypython
Summary: legacypython components for the packaging package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the packaging package.


%package python
Summary: python components for the packaging package.
Group: Default
Requires: packaging-legacypython
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
%setup -q -n packaging-16.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507163469
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507163469
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
