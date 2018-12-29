#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qscintilla
Version  : 2.10.8
Release  : 6
URL      : https://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.10.8/QScintilla_gpl-2.10.8.tar.gz
Source0  : https://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.10.8/QScintilla_gpl-2.10.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 HPND
Requires: qscintilla-data = %{version}-%{release}
Requires: qscintilla-lib = %{version}-%{release}
Requires: qscintilla-license = %{version}-%{release}
Requires: qscintilla-python = %{version}-%{release}
Requires: qscintilla-python3 = %{version}-%{release}
BuildRequires : PyQt5
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : python3-dev
BuildRequires : qscintilla-dev
BuildRequires : sip
BuildRequires : sip-dev

%description
All the documentation for QScintilla for Qt v4 and Qt v5 (including
installation instructions) can be found in doc/html-Qt4Qt5/index.html.

%package data
Summary: data components for the qscintilla package.
Group: Data

%description data
data components for the qscintilla package.


%package dev
Summary: dev components for the qscintilla package.
Group: Development
Requires: qscintilla-lib = %{version}-%{release}
Requires: qscintilla-data = %{version}-%{release}
Provides: qscintilla-devel = %{version}-%{release}

%description dev
dev components for the qscintilla package.


%package lib
Summary: lib components for the qscintilla package.
Group: Libraries
Requires: qscintilla-data = %{version}-%{release}
Requires: qscintilla-license = %{version}-%{release}

%description lib
lib components for the qscintilla package.


%package license
Summary: license components for the qscintilla package.
Group: Default

%description license
license components for the qscintilla package.


%package python
Summary: python components for the qscintilla package.
Group: Default
Requires: qscintilla-python3 = %{version}-%{release}

%description python
python components for the qscintilla package.


%package python3
Summary: python3 components for the qscintilla package.
Group: Default
Requires: python3-core

%description python3
python3 components for the qscintilla package.


%prep
%setup -q -n QScintilla_gpl-2.10.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
pushd Qt4Qt5
%qmake qscintilla.pro INCLUDEPATH+=../Qt4Qt5 LIBS+=-L../Qt4Qt5
test -r config.log && cat config.log
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1545359610
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qscintilla
cp LICENSE %{buildroot}/usr/share/package-licenses/qscintilla/LICENSE
cp include/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/include_License.txt
cp lexers/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/lexers_License.txt
cp lexlib/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/lexlib_License.txt
cp src/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/src_License.txt
pushd Qt4Qt5
%make_install
popd
## install_append content
pushd Python
python3 configure.py --pyqt=PyQt5
make
%make_install
popd
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt5/qsci/api/python/Python-2.4.api
/usr/share/qt5/qsci/api/python/Python-2.5.api
/usr/share/qt5/qsci/api/python/Python-2.6.api
/usr/share/qt5/qsci/api/python/Python-2.7.api
/usr/share/qt5/qsci/api/python/Python-3.1.api
/usr/share/qt5/qsci/api/python/Python-3.2.api
/usr/share/qt5/qsci/api/python/Python-3.3.api
/usr/share/qt5/qsci/api/python/Python-3.4.api
/usr/share/qt5/qsci/api/python/Python-3.5.api
/usr/share/qt5/qsci/api/python/Python-3.6.api
/usr/share/qt5/qsci/api/python/Python-3.7.api
/usr/share/qt5/qsci/api/python/QScintilla2.api
/usr/share/qt5/translations/qscintilla_cs.qm
/usr/share/qt5/translations/qscintilla_de.qm
/usr/share/qt5/translations/qscintilla_es.qm
/usr/share/qt5/translations/qscintilla_fr.qm
/usr/share/qt5/translations/qscintilla_pt_br.qm
/usr/share/sip/PyQt5/Qsci/qsciabstractapis.sip
/usr/share/sip/PyQt5/Qsci/qsciapis.sip
/usr/share/sip/PyQt5/Qsci/qscicommand.sip
/usr/share/sip/PyQt5/Qsci/qscicommandset.sip
/usr/share/sip/PyQt5/Qsci/qscidocument.sip
/usr/share/sip/PyQt5/Qsci/qscilexer.sip
/usr/share/sip/PyQt5/Qsci/qscilexeravs.sip
/usr/share/sip/PyQt5/Qsci/qscilexerbash.sip
/usr/share/sip/PyQt5/Qsci/qscilexerbatch.sip
/usr/share/sip/PyQt5/Qsci/qscilexercmake.sip
/usr/share/sip/PyQt5/Qsci/qscilexercoffeescript.sip
/usr/share/sip/PyQt5/Qsci/qscilexercpp.sip
/usr/share/sip/PyQt5/Qsci/qscilexercsharp.sip
/usr/share/sip/PyQt5/Qsci/qscilexercss.sip
/usr/share/sip/PyQt5/Qsci/qscilexercustom.sip
/usr/share/sip/PyQt5/Qsci/qscilexerd.sip
/usr/share/sip/PyQt5/Qsci/qscilexerdiff.sip
/usr/share/sip/PyQt5/Qsci/qscilexeredifact.sip
/usr/share/sip/PyQt5/Qsci/qscilexerfortran.sip
/usr/share/sip/PyQt5/Qsci/qscilexerfortran77.sip
/usr/share/sip/PyQt5/Qsci/qscilexerhtml.sip
/usr/share/sip/PyQt5/Qsci/qscilexeridl.sip
/usr/share/sip/PyQt5/Qsci/qscilexerjava.sip
/usr/share/sip/PyQt5/Qsci/qscilexerjavascript.sip
/usr/share/sip/PyQt5/Qsci/qscilexerjson.sip
/usr/share/sip/PyQt5/Qsci/qscilexerlua.sip
/usr/share/sip/PyQt5/Qsci/qscilexermakefile.sip
/usr/share/sip/PyQt5/Qsci/qscilexermarkdown.sip
/usr/share/sip/PyQt5/Qsci/qscilexermatlab.sip
/usr/share/sip/PyQt5/Qsci/qscilexeroctave.sip
/usr/share/sip/PyQt5/Qsci/qscilexerpascal.sip
/usr/share/sip/PyQt5/Qsci/qscilexerperl.sip
/usr/share/sip/PyQt5/Qsci/qscilexerpo.sip
/usr/share/sip/PyQt5/Qsci/qscilexerpostscript.sip
/usr/share/sip/PyQt5/Qsci/qscilexerpov.sip
/usr/share/sip/PyQt5/Qsci/qscilexerproperties.sip
/usr/share/sip/PyQt5/Qsci/qscilexerpython.sip
/usr/share/sip/PyQt5/Qsci/qscilexerruby.sip
/usr/share/sip/PyQt5/Qsci/qscilexerspice.sip
/usr/share/sip/PyQt5/Qsci/qscilexersql.sip
/usr/share/sip/PyQt5/Qsci/qscilexertcl.sip
/usr/share/sip/PyQt5/Qsci/qscilexertex.sip
/usr/share/sip/PyQt5/Qsci/qscilexerverilog.sip
/usr/share/sip/PyQt5/Qsci/qscilexervhdl.sip
/usr/share/sip/PyQt5/Qsci/qscilexerxml.sip
/usr/share/sip/PyQt5/Qsci/qscilexeryaml.sip
/usr/share/sip/PyQt5/Qsci/qscimacro.sip
/usr/share/sip/PyQt5/Qsci/qscimod4.sip
/usr/share/sip/PyQt5/Qsci/qscimod5.sip
/usr/share/sip/PyQt5/Qsci/qscimodcommon.sip
/usr/share/sip/PyQt5/Qsci/qsciprinter.sip
/usr/share/sip/PyQt5/Qsci/qsciscintilla.sip
/usr/share/sip/PyQt5/Qsci/qsciscintillabase.sip
/usr/share/sip/PyQt5/Qsci/qscistyle.sip
/usr/share/sip/PyQt5/Qsci/qscistyledtext.sip

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/Qsci/qsciabstractapis.h
/usr/include/qt5/Qsci/qsciapis.h
/usr/include/qt5/Qsci/qscicommand.h
/usr/include/qt5/Qsci/qscicommandset.h
/usr/include/qt5/Qsci/qscidocument.h
/usr/include/qt5/Qsci/qsciglobal.h
/usr/include/qt5/Qsci/qscilexer.h
/usr/include/qt5/Qsci/qscilexeravs.h
/usr/include/qt5/Qsci/qscilexerbash.h
/usr/include/qt5/Qsci/qscilexerbatch.h
/usr/include/qt5/Qsci/qscilexercmake.h
/usr/include/qt5/Qsci/qscilexercoffeescript.h
/usr/include/qt5/Qsci/qscilexercpp.h
/usr/include/qt5/Qsci/qscilexercsharp.h
/usr/include/qt5/Qsci/qscilexercss.h
/usr/include/qt5/Qsci/qscilexercustom.h
/usr/include/qt5/Qsci/qscilexerd.h
/usr/include/qt5/Qsci/qscilexerdiff.h
/usr/include/qt5/Qsci/qscilexeredifact.h
/usr/include/qt5/Qsci/qscilexerfortran.h
/usr/include/qt5/Qsci/qscilexerfortran77.h
/usr/include/qt5/Qsci/qscilexerhtml.h
/usr/include/qt5/Qsci/qscilexeridl.h
/usr/include/qt5/Qsci/qscilexerjava.h
/usr/include/qt5/Qsci/qscilexerjavascript.h
/usr/include/qt5/Qsci/qscilexerjson.h
/usr/include/qt5/Qsci/qscilexerlua.h
/usr/include/qt5/Qsci/qscilexermakefile.h
/usr/include/qt5/Qsci/qscilexermarkdown.h
/usr/include/qt5/Qsci/qscilexermatlab.h
/usr/include/qt5/Qsci/qscilexeroctave.h
/usr/include/qt5/Qsci/qscilexerpascal.h
/usr/include/qt5/Qsci/qscilexerperl.h
/usr/include/qt5/Qsci/qscilexerpo.h
/usr/include/qt5/Qsci/qscilexerpostscript.h
/usr/include/qt5/Qsci/qscilexerpov.h
/usr/include/qt5/Qsci/qscilexerproperties.h
/usr/include/qt5/Qsci/qscilexerpython.h
/usr/include/qt5/Qsci/qscilexerruby.h
/usr/include/qt5/Qsci/qscilexerspice.h
/usr/include/qt5/Qsci/qscilexersql.h
/usr/include/qt5/Qsci/qscilexertcl.h
/usr/include/qt5/Qsci/qscilexertex.h
/usr/include/qt5/Qsci/qscilexerverilog.h
/usr/include/qt5/Qsci/qscilexervhdl.h
/usr/include/qt5/Qsci/qscilexerxml.h
/usr/include/qt5/Qsci/qscilexeryaml.h
/usr/include/qt5/Qsci/qscimacro.h
/usr/include/qt5/Qsci/qsciprinter.h
/usr/include/qt5/Qsci/qsciscintilla.h
/usr/include/qt5/Qsci/qsciscintillabase.h
/usr/include/qt5/Qsci/qscistyle.h
/usr/include/qt5/Qsci/qscistyledtext.h
/usr/lib64/libqscintilla2_qt5.so
/usr/lib64/qt5/mkspecs/features/qscintilla2.prf

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqscintilla2_qt5.so.13
/usr/lib64/libqscintilla2_qt5.so.13.2
/usr/lib64/libqscintilla2_qt5.so.13.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qscintilla/LICENSE
/usr/share/package-licenses/qscintilla/include_License.txt
/usr/share/package-licenses/qscintilla/lexers_License.txt
/usr/share/package-licenses/qscintilla/lexlib_License.txt
/usr/share/package-licenses/qscintilla/src_License.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
