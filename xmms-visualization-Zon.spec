Summary:	GL && GLUT Visualization Plugin
Summary(pl):	Wtyczka wizualizacji dla XMMS-a u¿ywaj±ca GL i GLU
Name:		xmms-visualization-Zon
Version:	0.04
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://choronzon.net/Code/Zon/Zon-%{version}.tar.gz
# Source0-md5:	a09cd9d3dfea64eab451dfdc10eee9eb
URL:		http://choronzon.net/Code/Zon/
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	glut-devel
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visualization plugin which uses GL && GLUT.

%description -l pl
Wtyczka wizualizacji dla XMMS-a u¿ywaj±ca GL i GLUT.

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
install -d $RPM_BUILD_ROOT{%{xmms_visualization_plugindir},%{xmms_datadir}}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{xmms_datadir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
%{xmms_datadir}/*
