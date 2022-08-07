# A change to version_tag must also be applied to Source0
%global version_tag r2_0
%global version_num 2.0

Name:		xrescat
Version:	%{version_num}
Release:	1%{?dist}
Summary:	Prints the value of an X resource

License:	MIT
URL:		https://github.com/regolith-linux/xrescat
Source0:	https://github.com/regolith-linux/xrescat/archive/refs/tags/r2_0.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libX11-devel
Requires:	libX11

%description
`xrescat` is a simple utility which prints the value of an X resource.  It is [based on `xgetres`](https://github.com/tamirzb/xgetres) but does not add a linefeed, like `cat`.  `xrescat` will also trim enveloping double-quotes from values.

%prep
%setup -n xrescat-%{version_tag}

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc %{_mandir}/man1/xrescat.1.gz
%{_bindir}/xrescat

