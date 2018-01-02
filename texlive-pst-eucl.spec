Name:		texlive-pst-eucl
Version:	1.56
Release:	1
Summary:	Euclidian geometry with pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-eucl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the drawing of Euclidean geometric figures
using TeX pstricks macros for specifying mathematical
constraints. It is thus possible to build point using common
transformations or intersections. The use of coordinates is
limited to points which controlled the figure.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-eucl
%{_texmfdistdir}/tex/generic/pst-eucl
%{_texmfdistdir}/tex/latex/pst-eucl
%doc %{_texmfdistdir}/doc/generic/pst-eucl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
