Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.6.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0: 	http://sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(x11)
Recommends: 	lxappearance-obconf

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%package devel
Summary:	%{name} developement files
Group:		Graphical desktop/Other
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q

%build
autoreconf --install
%configure --enable-dbus --enable-gtk3
%make_build

%install
%make_install

%find_lang %{name}

desktop-file-install --vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/lxappearance.*

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc
