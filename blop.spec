%define debug_package	%{nil}

Name:		blop
Version:	0.2.8
Release:	10
Summary:	Bandlimited LADSPA Oscillator Plugins
License:	GPLv2+
Group:		Sound
URL:		http://blop.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
#Patch0:	blop-0.2.7-compile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ladspa-devel
Requires:	ladspa

%description
BLOP comprises a set of LADSPA plugins that generate bandlimited
sawtooth, square, variable pulse and slope-variable triangle waves,
for use in LADSPA hosts, principally for use with one of the many
modular software synthesisers available.

They are wavetable based, and are designed to produce output with
harmonic content as high as possible over a wide pitch range.

%prep
%setup -q
#%patch0 -p1
perl -p -i -e 's/\/lib\//\/%{_lib}\//g' src/wavedata.c

%build
%configure2_5x --with-ladspa-plugin-dir=%{_libdir}/ladspa
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf
%{makeinstall_std}

# install the rdf description
install -m0644 doc/blop.rdf $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf
# we don't want to package makefiles in the doc
#rm -f doc/Makefile*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO doc/{about.txt,blop.rdf,plugins_list.txt}
%{_libdir}/ladspa/*.so
%{_libdir}/ladspa/blop_files
%{_datadir}/ladspa/rdf/*.rdf




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.8-9mdv2011.0
+ Revision: 610079
- rebuild

* Wed Feb 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.8-8mdv2010.1
+ Revision: 503995
- clean spec, fix rpmlint's warning on spec

* Tue Jun 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.2.8-7mdv2010.0
+ Revision: 386384
- fix license tag

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.8-6mdv2009.0
+ Revision: 243354
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.2.8-4mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 08 2007 Stefan van der Eijk <stefan@mandriva.org> 0.2.8-4mdv2007.0
+ Revision: 118174
- rebuild
- Import blop

* Fri Dec 30 2005 Austin Acton <austin@mandriva.org> 0.2.8-3mdk
- don't own files you shouldn't

* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 0.2.8-2mdk
- fix libdir on x86_64

* Thu Jul 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.8-1mdk
- 0.2.8
- add translations
- drop P0 (fixed upstream)
- drop some docs we really don't need
- make package short-circuitable
- cosmetics

