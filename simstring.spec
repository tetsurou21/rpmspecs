Name:           simstring
Version:        1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.chokkan.org/software/simstring/index.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Source0:        simstring-1.0.tar.gz
Summary:        A fast and simple algorithm for approximate string matching/retrieval
Provides:       simstring

%description
SimString is a simple library for fast approximate string retrieval.
Approximate string retrieval finds strings in a database whose similarity
with a query string is no smaller than a threshold. Finding not only
identical but similar strings, approximate string retrieval has various
applications including spelling correction, flexible dictionary matching,
duplicate detection, and record linkage.

%prep
%setup -n simstring-%{version}

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
%{_includedir}
%doc %{_docdir}
