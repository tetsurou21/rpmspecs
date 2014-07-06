Name:           swig2.0
Version:        2.0.11
Release:        1%{?dist}
License:        GPL
URL:            http://www.swig.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Source0:        swig-2.0.11.tar.gz
Summary:        SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.
BuildRequires:  pcre-devel
Provides:       swig2.0

%description
SWIG is a software development tool that connects programs written
in C and C++ with a variety of high-level programming languages.
SWIG is used with different types of target languages including
common scripting languages such as Javascript, Perl, PHP, Python,
Tcl and Ruby.

%prep
%setup -n swig-%{version}

%build

%configure
make

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_datadir}/swig
%doc %{_mandir}
