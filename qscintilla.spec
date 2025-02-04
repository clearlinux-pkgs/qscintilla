#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: qmake
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : qscintilla
Version  : 2.14.1
Release  : 57
URL      : https://www.riverbankcomputing.com/static/Downloads/QScintilla/2.14.1/QScintilla_src-2.14.1.tar.gz
Source0  : https://www.riverbankcomputing.com/static/Downloads/QScintilla/2.14.1/QScintilla_src-2.14.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 HPND
Requires: qscintilla-data = %{version}-%{release}
Requires: qscintilla-lib = %{version}-%{release}
Requires: qscintilla-license = %{version}-%{release}
Requires: qscintilla-python = %{version}-%{release}
Requires: qscintilla-python3 = %{version}-%{release}
BuildRequires : PyQt6
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt6Designer)
BuildRequires : pkgconfig(Qt6PrintSupport)
BuildRequires : pkgconfig(Qt6Widgets)
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
Requires: PyQt6

%description python3
python3 components for the qscintilla package.


%prep
%setup -q -n QScintilla_src-2.14.1
cd %{_builddir}/QScintilla_src-2.14.1
pushd ..
cp -a QScintilla_src-2.14.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd src
export QMAKE_CFLAGS="$CFLAGS"
export QMAKE_CXXFLAGS="$CXXFLAGS"
export QMAKE_LFLAGS="$LDFLAGS"
export QMAKE_LIBDIR=/usr/lib64
export QMAKE_CFLAGS_RELEASE=
export QMAKE_CXXFLAGS_RELEASE=
export PATH=/usr/lib64/qt6/bin:$PATH
qmake6 QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto  qscintilla.pro INCLUDEPATH+=../Qt4Qt5 LIBS+=-L../Qt4Qt5
test -r config.log && cat config.log
make  %{?_smp_mflags}
popd
pushd ../buildavx2/src
qmake6 'QT_CPU_FEATURES.x86_64 += avx avx2 bmi bmi2 f16c fma lzcnt popcnt'\
    QMAKE_CFLAGS+="-march=x86-64-v3 -Wl,-z,x86-64-v3" QMAKE_CXXFLAGS+="-march=x86-64-v3 -Wl,-z,x86-64-v3" \
    QMAKE_LFLAGS+="-march=x86-64-v3" QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto  qscintilla.pro INCLUDEPATH+=../Qt4Qt5 LIBS+=-L../Qt4Qt5
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738690498
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qscintilla
cp %{_builddir}/QScintilla_src-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qscintilla/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/include/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/lexers/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/lexlib/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
cp %{_builddir}/QScintilla_src-%{version}/scintilla/src/License.txt %{buildroot}/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/src
%make_install_v3
popd
pushd src
GOAMD64=v2
%make_install
popd
## install_append content
# Install the Python bindings
export PATH=/usr/lib64/qt6/bin:$PATH
pushd Python
cp -p pyproject-qt6.toml pyproject.toml
sip-build --no-make --qsci-include-dir %{buildroot}/usr/include --qmake-setting 'INCLUDEPATH+=/usr/include/QtWidgets' --qmake-setting 'INCLUDEPATH+=/usr/include/QtPrintSupport' --verbose
make %{?_smp_mflags} -C build
make -C build install INSTALL_ROOT=%{buildroot}
popd
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt6/qsci/api/python/Python-2.4.api
/usr/share/qt6/qsci/api/python/Python-2.5.api
/usr/share/qt6/qsci/api/python/Python-2.6.api
/usr/share/qt6/qsci/api/python/Python-2.7.api
/usr/share/qt6/qsci/api/python/Python-3.1.api
/usr/share/qt6/qsci/api/python/Python-3.10.api
/usr/share/qt6/qsci/api/python/Python-3.11.api
/usr/share/qt6/qsci/api/python/Python-3.2.api
/usr/share/qt6/qsci/api/python/Python-3.3.api
/usr/share/qt6/qsci/api/python/Python-3.4.api
/usr/share/qt6/qsci/api/python/Python-3.5.api
/usr/share/qt6/qsci/api/python/Python-3.6.api
/usr/share/qt6/qsci/api/python/Python-3.7.api
/usr/share/qt6/qsci/api/python/Python-3.8.api
/usr/share/qt6/qsci/api/python/Python-3.9.api
/usr/share/qt6/translations/qscintilla_cs.qm
/usr/share/qt6/translations/qscintilla_de.qm
/usr/share/qt6/translations/qscintilla_es.qm
/usr/share/qt6/translations/qscintilla_fr.qm
/usr/share/qt6/translations/qscintilla_pt_br.qm

%files dev
%defattr(-,root,root,-)
/usr/include/Qsci/qsciabstractapis.h
/usr/include/Qsci/qsciapis.h
/usr/include/Qsci/qscicommand.h
/usr/include/Qsci/qscicommandset.h
/usr/include/Qsci/qscidocument.h
/usr/include/Qsci/qsciglobal.h
/usr/include/Qsci/qscilexer.h
/usr/include/Qsci/qscilexerasm.h
/usr/include/Qsci/qscilexeravs.h
/usr/include/Qsci/qscilexerbash.h
/usr/include/Qsci/qscilexerbatch.h
/usr/include/Qsci/qscilexercmake.h
/usr/include/Qsci/qscilexercoffeescript.h
/usr/include/Qsci/qscilexercpp.h
/usr/include/Qsci/qscilexercsharp.h
/usr/include/Qsci/qscilexercss.h
/usr/include/Qsci/qscilexercustom.h
/usr/include/Qsci/qscilexerd.h
/usr/include/Qsci/qscilexerdiff.h
/usr/include/Qsci/qscilexeredifact.h
/usr/include/Qsci/qscilexerfortran.h
/usr/include/Qsci/qscilexerfortran77.h
/usr/include/Qsci/qscilexerhex.h
/usr/include/Qsci/qscilexerhtml.h
/usr/include/Qsci/qscilexeridl.h
/usr/include/Qsci/qscilexerintelhex.h
/usr/include/Qsci/qscilexerjava.h
/usr/include/Qsci/qscilexerjavascript.h
/usr/include/Qsci/qscilexerjson.h
/usr/include/Qsci/qscilexerlua.h
/usr/include/Qsci/qscilexermakefile.h
/usr/include/Qsci/qscilexermarkdown.h
/usr/include/Qsci/qscilexermasm.h
/usr/include/Qsci/qscilexermatlab.h
/usr/include/Qsci/qscilexernasm.h
/usr/include/Qsci/qscilexeroctave.h
/usr/include/Qsci/qscilexerpascal.h
/usr/include/Qsci/qscilexerperl.h
/usr/include/Qsci/qscilexerpo.h
/usr/include/Qsci/qscilexerpostscript.h
/usr/include/Qsci/qscilexerpov.h
/usr/include/Qsci/qscilexerproperties.h
/usr/include/Qsci/qscilexerpython.h
/usr/include/Qsci/qscilexerruby.h
/usr/include/Qsci/qscilexerspice.h
/usr/include/Qsci/qscilexersql.h
/usr/include/Qsci/qscilexersrec.h
/usr/include/Qsci/qscilexertcl.h
/usr/include/Qsci/qscilexertekhex.h
/usr/include/Qsci/qscilexertex.h
/usr/include/Qsci/qscilexerverilog.h
/usr/include/Qsci/qscilexervhdl.h
/usr/include/Qsci/qscilexerxml.h
/usr/include/Qsci/qscilexeryaml.h
/usr/include/Qsci/qscimacro.h
/usr/include/Qsci/qsciprinter.h
/usr/include/Qsci/qsciscintilla.h
/usr/include/Qsci/qsciscintillabase.h
/usr/include/Qsci/qscistyle.h
/usr/include/Qsci/qscistyledtext.h
/usr/lib64/libqscintilla2_qt6.so
/usr/lib64/qt6/mkspecs/features/qscintilla2.prf

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libqscintilla2_qt6.so.15.2.1
/usr/lib64/libqscintilla2_qt6.so.15
/usr/lib64/libqscintilla2_qt6.so.15.2
/usr/lib64/libqscintilla2_qt6.so.15.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qscintilla/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qscintilla/f06de8b018290a99ff91fa2f136ad3b859ae8543

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
