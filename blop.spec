Name:		blop
Version:	0.2.8
Release:	%mkrel 9
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


