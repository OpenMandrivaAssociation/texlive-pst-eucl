%global tl_name pst-eucl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.77
Release:	%{tl_revision}.1
Summary:	Euclidean geometry with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-eucl
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the drawing of Euclidean geometric figures using TeX
pstricks macros for specifying mathematical constraints. It is thus
possible to build point using common transformations or intersections.
The use of coordinates is limited to points which controlled the figure.

