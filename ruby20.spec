%define rubyxver       2.0 
%define rubyver        2.0.0
%define _patchlevel p481

Name:           ruby20
Version:        %{rubyxver}.%{_patchlevel}
Release:        1%{?dist}
License:        Ruby or BSD 
URL:            https://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

BuildRequires:  ncurses-devel gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  gcc unzip openssl-devel byacc
BuildRequires:  readline-devel

Source0:        ruby-%{rubyver}-%{_patchlevel}.tar.gz
Summary:        A dynamic, open source programming language with a focus on simplicity and productivity.

Group:          Development/Languages

%description
A dynamic, open source programming language with a focus on simplicity and 
productivity. It has an elegant syntax that is natural to read and easy to
write.

%prep
%setup -n ruby-%{rubyver}-%{_patchlevel}

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
%{_datadir}
%{_libdir}
