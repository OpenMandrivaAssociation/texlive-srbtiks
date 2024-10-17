Name:		texlive-srbtiks
Version:	63308
Release:	2
Summary:	Font STIX2 for Serbian and Macedonian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/srbtiks
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbtiks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbtiks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The srbtiks package is the extension of the stix2-type1 package
that enables usage of the STIX2 font in LaTeX for the Serbian
and Macedonian languages (therefore, it is required to have the
stix2-type1 package installed).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/srbtiks
%{_texmfdistdir}/fonts/vf/public/srbtiks
%{_texmfdistdir}/fonts/tfm/public/srbtiks
%{_texmfdistdir}/fonts/map/dvips/srbtiks
%{_texmfdistdir}/fonts/enc/dvips/srbtiks
%doc %{_texmfdistdir}/doc/fonts/srbtiks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
