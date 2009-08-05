Summary:	Data recovery tool
Summary(pl.UTF-8):	Narzędzie do odzyskiwania danych
Name:		safecopy
Version:	1.5
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/safecopy/%{name}-%{version}.tar.gz
# Source0-md5:	8b007de8d17c054593cdc0ade4516f08
URL:		http://safecopy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
safecopy is a data recovery tool which tries to extract as much data
as possible from a seekable but problematic (i.e., damaged sectors)
source like floppy drives, hard disk partitions, CDs, etc.

%description -l pl.UTF-8
safecopy jest narzędziem do odzyskiwania danych, które próbuje
wydobyć tak dużo danych, jak to możliwe z przeszukiwalnych lecz
problematycznych (np. z uszkodzonymi sektorami) źródeł, takich jak
dyskietki, partycje dysków, płyty CD itp.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README specification.txt
%attr(755,root,root) %{_bindir}/safecopy
%{_mandir}/man1/safecopy.1*
