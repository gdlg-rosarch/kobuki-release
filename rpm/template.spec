Name:           ros-indigo-kobuki-capabilities
Version:        0.6.8
Release:        0%{?dist}
Summary:        ROS kobuki_capabilities package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_capabilities
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-kobuki-node
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-rocon-app-manager
Requires:       ros-indigo-rocon-apps
Requires:       ros-indigo-std-capabilities
BuildRequires:  ros-indigo-catkin

%description
Kobuki's capabilities

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 09 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.6.8-0
- Autogenerated by Bloom

* Sat Aug 13 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.6.7-0
- Autogenerated by Bloom

* Wed May 27 2015 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.6.6-0
- Autogenerated by Bloom

