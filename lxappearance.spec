# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		655fd083a98e7b11d61119bdf0d97aae6c774780
	%global commitdate	20230917
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	A new feature-rich GTK+ theme switcher
Name:		lxappearance
Version:	0.6.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	https://github.com/lxde/lxappearance/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
#Patch0:		lxappearance-fix-man-patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(x11)
Recommends: 	lxappearance-obconf

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/lxappearance.*

#---------------------------------------------------------------------------

%package devel
Summary:	%{name} developement files
Group:		Graphical desktop/Other
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains header files needed when building applications based on
%{name}.

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-dbus \
	--enable-gtk3 \
	--enable-man \
	%{nil}
%make_build

%install
%make_install

# .desktop
desktop-file-install \
	--vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

# locales
%find_lang %{name}

