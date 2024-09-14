#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.6
%define		qtver	5.15.2
%define		kfname	knewstuff

Summary:	Framework for downloading and sharing additional application data
Name:		kf6-%{kfname}
Version:	6.6.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	9ae981d2f24dd04a46d56da68146f22a
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf6-attica-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-karchive-devel >= %{version}
BuildRequires:	kf6-kcompletion-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kiconthemes-devel >= %{version}
BuildRequires:	kf6-kio-devel >= %{version}
BuildRequires:	kf6-kitemviews-devel >= %{version}
BuildRequires:	kf6-kpackage-devel >= %{version}
BuildRequires:	kf6-kservice-devel >= %{version}
BuildRequires:	kf6-ktextwidgets-devel >= %{version}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf6-kxmlgui-devel >= %{version}
BuildRequires:	kf6-syndication-devel >= %{version}
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Qml >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
Requires:	kf6-attica >= %{version}
Requires:	kf6-dirs
Requires:	kf6-karchive >= %{version}
Requires:	kf6-kcompletion >= %{version}
Requires:	kf6-kconfig >= %{version}
Requires:	kf6-kcoreaddons >= %{version}
Requires:	kf6-ki18n >= %{version}
Requires:	kf6-kiconthemes >= %{version}
Requires:	kf6-kio >= %{version}
Requires:	kf6-kitemviews >= %{version}
Requires:	kf6-kpackage >= %{version}
Requires:	kf6-kservice >= %{version}
Requires:	kf6-ktextwidgets >= %{version}
Requires:	kf6-kwidgetsaddons >= %{version}
Requires:	kf6-kxmlgui >= %{version}
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration
Services specification.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Widgets-devel >= %{qtver}
Requires:	Qt6Xml-devel >= %{qtver}
Requires:	cmake >= 3.16
Requires:	kf6-attica-devel >= %{version}
Requires:	kf6-kservice-devel >= %{version}
Requires:	kf6-kxmlgui-devel >= %{version}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF6NewStuffCore.so.6
%attr(755,root,root) %{_libdir}/libKF6NewStuffCore.so.*.*
%ghost %{_libdir}/libKF6NewStuffWidgets.so.6
%attr(755,root,root) %{_libdir}/libKF6NewStuffWidgets.so.*.*
%{_datadir}/qlogging-categories6/knewstuff.categories
%{_libdir}/qt6/qml/org/kde/newstuff/libnewstuffqmlplugin.so
%dir %{_libdir}/qt6/qml/org/kde/newstuff
%{_libdir}/qt6/qml/org/kde/newstuff/Action.qml
%{_libdir}/qt6/qml/org/kde/newstuff/Button.qml
%{_libdir}/qt6/qml/org/kde/newstuff/Dialog.qml
%{_libdir}/qt6/qml/org/kde/newstuff/DialogContent.qml
%{_libdir}/qt6/qml/org/kde/newstuff/DownloadItemsSheet.qml
%{_libdir}/qt6/qml/org/kde/newstuff/EntryDetails.qml
%{_libdir}/qt6/qml/org/kde/newstuff/Page.qml
%{_libdir}/qt6/qml/org/kde/newstuff/QuestionAsker.qml
%{_libdir}/qt6/qml/org/kde/newstuff/UploadPage.qml
%dir %{_libdir}/qt6/qml/org/kde/newstuff/private
%{_libdir}/qt6/qml/org/kde/newstuff/private/ConditionalLoader.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/EntryCommentDelegate.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/EntryCommentsPage.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/EntryScreenshots.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/ErrorDisplayer.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/GridTileDelegate.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/Rating.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/Shadow.qml
%dir %{_libdir}/qt6/qml/org/kde/newstuff/private/entrygriddelegates
%{_libdir}/qt6/qml/org/kde/newstuff/private/entrygriddelegates/BigPreviewDelegate.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/entrygriddelegates/FeedbackOverlay.qml
%{_libdir}/qt6/qml/org/kde/newstuff/private/entrygriddelegates/TileDelegate.qml
%{_libdir}/qt6/qml/org/kde/newstuff/qmldir
%{_datadir}/qlogging-categories6/knewstuff.renamecategories
%attr(755,root,root) %{_bindir}/knewstuff-dialog6
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/knewstuff6widgets.so
%{_libdir}/qt6/qml/org/kde/newstuff/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/newstuff/newstuffqmlplugin.qmltypes
%{_desktopdir}/org.kde.knewstuff-dialog6.desktop
%{_libdir}/qt6/qml/org/kde/newstuff/private/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/newstuff/private/libnewstuffqmlpluginprivate.so
%{_libdir}/qt6/qml/org/kde/newstuff/private/newstuffqmlpluginprivate.qmltypes
%{_libdir}/qt6/qml/org/kde/newstuff/private/qmldir


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KNewStuff
%{_includedir}/KF6/KNewStuffCore
%{_includedir}/KF6/KNewStuffWidgets
%{_libdir}/cmake/KF6NewStuff
%{_libdir}/cmake/KF6NewStuffCore
%{_libdir}/libKF6NewStuffCore.so
%{_libdir}/libKF6NewStuffWidgets.so
