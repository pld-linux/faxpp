#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Fast XML Pull Parser
Summary(pl.UTF-8):	Fast XML Pull Parser - szybki analizator XML-a
Name:		faxpp
Version:	0.4
Release:	2
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/faxpp/%{name}-%{version}.tar.gz
# Source0-md5:	cf9a8f4301699710fd93eb0c854fc420
URL:		http://faxpp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faxpp is a small, fast and conformant XML pull parser written in C
with an API that can return strings in any encoding including UTF-8
and UTF-16. Faxpp is written by John Snelson, and is released under
the terms of the Apache Licence v2.

%description -l pl.UTF-8
Faxpp to mały, szybki i zgodny ze standardem analizator XML-a napisany
w C z API mogącym zwracać łańcuchy znaków w dowolnym kodowaniu,
włącznie z UTF-8 i UTF-16. Faxpp został napisany przez Johna Snelsona
i wydany na warunkach licencji Apache v2.

%package devel
Summary:	Header files for faxpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki faxpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for faxpp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki faxpp.

%package static
Summary:	Static faxpp library
Summary(pl.UTF-8):	Statyczna biblioteka faxpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static faxpp library.

%description static -l pl.UTF-8
Statyczna biblioteka faxpp.

%package apidocs
Summary:	faxpp API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki faxpp
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for faxpp library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki faxpp.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_libdir}/libfaxpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfaxpp.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfaxpp.so
%{_libdir}/libfaxpp.la
%{_includedir}/faxpp

%files static
%defattr(644,root,root,755)
%{_libdir}/libfaxpp.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/{api,header.html}
%endif
