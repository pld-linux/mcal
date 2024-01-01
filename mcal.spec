Summary:	libmcal powered cal replacement
Summary(pl.UTF-8):	Oparty o libmcal zamiennik programu cal
Name:		mcal
Version:	0.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://downloads.sourceforge.net/libmcal/%{name}-%{version}.tar.gz
# Source0-md5:	06e7a54ce84752194ce4b6f93fca67d6
Patch0:		%{name}-segv.patch
URL:		https://libmcal.sourceforge.net/
BuildRequires:	libmcal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmcal powered cal replacement.

%description -l pl.UTF-8
Oparty o libmcal zamiennik programu cal.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	INCLUDE="%{rpmcflags} %{rpmcppflags} -I/usr/include/mcal" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mcal $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mcal
