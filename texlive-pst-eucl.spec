# revision 31006
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-eucl
# catalog-date 2013-06-27 22:54:23 +0200
# catalog-license lppl
# catalog-version 1.48
Name:		texlive-pst-eucl
Version:	1.48
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
%{_texmfdistdir}/dvips/pst-eucl/pst-eucl.pro
%{_texmfdistdir}/tex/generic/pst-eucl/pst-eucl.tex
%{_texmfdistdir}/tex/latex/pst-eucl/pst-eucl.sty
%doc %{_texmfdistdir}/doc/generic/pst-eucl/Changes
%doc %{_texmfdistdir}/doc/generic/pst-eucl/README
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/abscur.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/abscur_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/angle.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/angle_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/arc.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/arc_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/astro.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/astro_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/bissec.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/bissec_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/ccirc.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/ccirc_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cercle.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cercle_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cinscex.pdf
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cinscex.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cinscex_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/curvetype.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/curvetype_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cyclo.pdf
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cyclo.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cycloO.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/cyclo_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/delto.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/droite.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/droite_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/envcardi.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/envcardi_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/envellipse.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/envellipse_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/euler.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/euler_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/fracthom.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/fracthom_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gal_biss.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gal_biss_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gauss.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gauss_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gencur.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/gencur_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/geohyper.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/geohyper_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/geonode.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/geonode_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/german_ra.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/german_ra_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/grav.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/grav_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/homothetie.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/homothetie_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/hyperbole.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/hyperbole_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/hypocyclo.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interCC.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interCC_bis_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interCC_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interDC.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interDC_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interDD.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interDD_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFC.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFC_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFF.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFF_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFL.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/interFL_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/mediator.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/mediator_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/milieu.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/milieu_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/oij.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/oij_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/orthocentre.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/orthocentre_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/orthoethyper.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/orthoethyper_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/parabole.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/parabole_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/projection.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/projection_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/ptfermat.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/ptfermat_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/remarq.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/remarq_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/rotation.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/rotation_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/segmentmark.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/segmentmark_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/symcentrale.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/symcentrale_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/symorthogonale.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/symorthogonale_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/tg1c.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/tg1c_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/tg2c.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/tg2c_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/translation.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/translation_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/triangle.ps
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/triangle.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/Examples/triangle_in.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/euclide-english.tex
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/euclide.sty
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/euclide_english.ist
%doc %{_texmfdistdir}/doc/generic/pst-eucl/doc/euclide_macros.ist
%doc %{_texmfdistdir}/doc/generic/pst-eucl/pst-eucl-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
