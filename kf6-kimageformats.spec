%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240217

#                 Attention! Achtung! Uwaga! Attenzione!                  #
###########################################################################
#   When updating kf6-kimageformats remember to also update its twin in	  #
# 	 restricted repository - kf6-kimageformats-restricted, 		  #
# 		which has the heif codec enabled.               	  #
###########################################################################

Name: kf6-kimageformats
Version: 6.19.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kimageformats/-/archive/master/kimageformats-master.tar.bz2#/kimageformats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kimageformats-%{version}.tar.xz
%endif
Source10: imageformat-package
Summary: Plugins to allow QImage to support extra file formats.
URL: https://invent.kde.org/frameworks/kimageformats
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(OpenEXR) >= 3.0.0
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: jxrlib-devel
BuildRequires: cmake(KF6Archive)
Suggests: %{name}-ani = %{EVRD}
Suggests: %{name}-avif = %{EVRD}
Suggests: %{name}-dds = %{EVRD}
Suggests: %{name}-eps = %{EVRD}
Suggests: %{name}-exr = %{EVRD}
Suggests: %{name}-hdr = %{EVRD}
Suggests: %{name}-iff = %{EVRD}
Suggests: %{name}-jxl = %{EVRD}
Suggests: %{name}-jxr = %{EVRD}
Suggests: %{name}-kra = %{EVRD}
Suggests: %{name}-pcx = %{EVRD}
Suggests: %{name}-pfm = %{EVRD}
Suggests: %{name}-pic = %{EVRD}
Suggests: %{name}-psd = %{EVRD}
Suggests: %{name}-pxr = %{EVRD}
Suggests: %{name}-ora = %{EVRD}
Suggests: %{name}-qoi = %{EVRD}
Suggests: %{name}-ras = %{EVRD}
Suggests: %{name}-raw = %{EVRD}
Suggests: %{name}-rgb = %{EVRD}
Suggests: %{name}-sct = %{EVRD}
Suggests: %{name}-tga = %{EVRD}
Suggests: %{name}-xcf = %{EVRD}
BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DKIMAGEFORMATS_JXL:BOOL=ON
BuildOption: -DKIMAGEFORMATS_JXR:BOOL=ON
# HEIF has patent issues, and is therefore in restricted
BuildOption: -DKIMAGEFORMATS_HEIF:BOOL=OFF

%description
Plugins to allow QImage to support extra file formats.

%package devel
Summary:	Development files for %{name}
Group:		Development/C and C++

%description devel
Development files for %{name}

%{expand:%(sh %{SOURCE10} ani)}
%{expand:%(sh %{SOURCE10} avif)}
%{expand:%(sh %{SOURCE10} dds)}
%{expand:%(sh %{SOURCE10} eps)}
%{expand:%(sh %{SOURCE10} exr)}
%{expand:%(sh %{SOURCE10} hdr)}
%{expand:%(sh %{SOURCE10} iff)}
%{expand:%(sh %{SOURCE10} jp2)}
%{expand:%(sh %{SOURCE10} jxl)}
%{expand:%(sh %{SOURCE10} jxr)}
%{expand:%(sh %{SOURCE10} kra)}
%{expand:%(sh %{SOURCE10} pcx)}
%{expand:%(sh %{SOURCE10} pfm)}
%{expand:%(sh %{SOURCE10} pic)}
%{expand:%(sh %{SOURCE10} psd)}
%{expand:%(sh %{SOURCE10} pxr)}
%{expand:%(sh %{SOURCE10} ora)}
%{expand:%(sh %{SOURCE10} qoi)}
%{expand:%(sh %{SOURCE10} ras)}
%{expand:%(sh %{SOURCE10} raw)}
%{expand:%(sh %{SOURCE10} rgb)}
%{expand:%(sh %{SOURCE10} sct)}
%{expand:%(sh %{SOURCE10} tga)}
%{expand:%(sh %{SOURCE10} xcf)}

%files

%files devel
%{_libdir}/cmake/KF6ImageFormats
