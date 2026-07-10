%global tl_name centeredline
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A macro for centering lines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/centeredline
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/centeredline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/centeredline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a macro \centeredline{...} which allows to
conveniently center a line inside a paragraph while allowing usage
therein of \verb or other macros changing catcodes. It works nicely in
list environments, and material whose natural width exceeds the current
linewidth will get properly centered too.

