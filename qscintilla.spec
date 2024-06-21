#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: qmake
# autospec version: v2
# autospec commit: f032afc
#
Name     : qscintilla
Version  : 2.14.0
Release  : 43
URL      : https://www.riverbankcomputing.com/static/Downloads/QScintilla/2.14.0/QScintilla_src-2.14.0.tar.gz
Source0  : https://www.riverbankcomputing.com/static/Downloads/QScintilla/2.14.0/QScintilla_src-2.14.0.tar.gz
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
BuildRequires : pypi-pyqt_builder-python3
BuildRequires : python3-dev
BuildRequires : sip
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
QScintilla - Python Bindings for the QScintilla Programmers Editor Widget
=========================================================================

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
Requires: qscintilla = %{version}-%{release}

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
%setup -q -n QScintilla_src-2.14.0
cd %{_builddir}/QScintilla_src-2.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd src
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto  qscintilla.pro INCLUDEPATH+=../Qt4Qt5 LIBS+=-L../Qt4Qt5
test -r config.log && cat config.log
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697564586
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qscintilla
cp %{_builddir}/QScintilla_src-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qscintilla/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/include/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/lexers/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/lexlib/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/src/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
pushd src
%make_install
popd
## install_append content
# Install the Python bindings
pushd Python
cp -p pyproject-qt5.toml pyproject.toml
sip-build --no-make --qsci-include-dir %{buildroot}/usr/include/qt5 --qmake-setting 'INCLUDEPATH+=/usr/include/qt5/QtWidgets' --qmake-setting 'INCLUDEPATH+=/usr/include/qt5/QtPrintSupport' --verbose
make %{?_smp_mflags} -C build
make -C build install INSTALL_ROOT=%{buildroot}
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
/usr/share/qt5/qsci/api/python/Python-3.10.api
/usr/share/qt5/qsci/api/python/Python-3.11.api
/usr/share/qt5/qsci/api/python/Python-3.2.api
/usr/share/qt5/qsci/api/python/Python-3.3.api
/usr/share/qt5/qsci/api/python/Python-3.4.api
/usr/share/qt5/qsci/api/python/Python-3.5.api
/usr/share/qt5/qsci/api/python/Python-3.6.api
/usr/share/qt5/qsci/api/python/Python-3.7.api
/usr/share/qt5/qsci/api/python/Python-3.8.api
/usr/share/qt5/qsci/api/python/Python-3.9.api
/usr/share/qt5/translations/qscintilla_cs.qm
/usr/share/qt5/translations/qscintilla_de.qm
/usr/share/qt5/translations/qscintilla_es.qm
/usr/share/qt5/translations/qscintilla_fr.qm
/usr/share/qt5/translations/qscintilla_pt_br.qm

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/Qsci/qsciabstractapis.h
/usr/include/qt5/Qsci/qsciapis.h
/usr/include/qt5/Qsci/qscicommand.h
/usr/include/qt5/Qsci/qscicommandset.h
/usr/include/qt5/Qsci/qscidocument.h
/usr/include/qt5/Qsci/qsciglobal.h
/usr/include/qt5/Qsci/qscilexer.h
/usr/include/qt5/Qsci/qscilexerasm.h
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
/usr/include/qt5/Qsci/qscilexerhex.h
/usr/include/qt5/Qsci/qscilexerhtml.h
/usr/include/qt5/Qsci/qscilexeridl.h
/usr/include/qt5/Qsci/qscilexerintelhex.h
/usr/include/qt5/Qsci/qscilexerjava.h
/usr/include/qt5/Qsci/qscilexerjavascript.h
/usr/include/qt5/Qsci/qscilexerjson.h
/usr/include/qt5/Qsci/qscilexerlua.h
/usr/include/qt5/Qsci/qscilexermakefile.h
/usr/include/qt5/Qsci/qscilexermarkdown.h
/usr/include/qt5/Qsci/qscilexermasm.h
/usr/include/qt5/Qsci/qscilexermatlab.h
/usr/include/qt5/Qsci/qscilexernasm.h
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
/usr/include/qt5/Qsci/qscilexersrec.h
/usr/include/qt5/Qsci/qscilexertcl.h
/usr/include/qt5/Qsci/qscilexertekhex.h
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
/usr/lib64/libqscintilla2_qt5.so.15
/usr/lib64/libqscintilla2_qt5.so.15.2
/usr/lib64/libqscintilla2_qt5.so.15.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qscintilla/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
