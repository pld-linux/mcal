Summary:	libmcal powered cal replacement
Summary(pl):	Oparty o libmcal zamiennik programu cal
Name:		mcal
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/libmcal/%{name}-%{version}.tar.gz
# Source0-md5:	06e7a54ce84752194ce4b6f93fca67d6
Patch0:		%{name}-segv.patch
URL:		http://mcal.chek.com/
BuildRequires:	libmcal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmcal powered cal replacement.

%description -l pl
Oparty o libmcal zamiennik programu cal.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} \
	INCLUDE="%{rpmcflags} -I/usr/include/mcal" \
	LIBDIR=/usr/lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mcal $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
