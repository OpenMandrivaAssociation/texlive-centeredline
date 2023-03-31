Name:		texlive-centeredline
Version:	64672
Release:	2
Summary:	A macro for centering lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/centeredline
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/centeredline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/centeredline.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a macro \centeredline{...} which allows
to conveniently center a line inside a paragraph while allowing
usage therein of \verb or other macros changing catcodes. It
works nicely in list environments, and material whose natural
width exceeds the current linewidth will get properly centered
too.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/centeredline
%doc %{_texmfdistdir}/doc/latex/centeredline

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
