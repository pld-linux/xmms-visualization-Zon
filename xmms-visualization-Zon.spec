Summary:	GL && GLUT Visualization Plugin
Summary(pl):	Plugin Wizualizacji GL && GLU
Name:		xmms-visualization-Zon
Version:	0.04
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://choronzon.net/Code/Zon/Zon-%{version}.tar.gz
URL:		http://choronzon.net/Code/Zon/
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Visualization plugin which uses GL && GLUT.

%description -l pl
Plugin wizualizacji u¿ywaj±cy GL && GLUT.

%prep
%setup -q -n Zon-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags} \
	`glib-config --cflags` \
	`%{_bindir}/gtk-config --cflags` \
	`%{_bindir}/xmms-config --cflags` \
	-DUNIX -fPIC -fname-mangling-version-0 -DVERSION=\"%{version}\" -g "

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/ \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/ \
	XMMS_DATADIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

gzip -9nf Change* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
