%global tl_name srbtiks
%global tl_revision 63308

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Font STIX2 for Serbian and Macedonian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/srbtiks
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srbtiks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srbtiks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The srbtiks package is the extension of the stix2-type1 package that
enables usage of the STIX2 font in LaTeX for the Serbian and Macedonian
languages (therefore, it is required to have the stix2-type1 package
installed).

