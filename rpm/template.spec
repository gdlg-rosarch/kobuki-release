Name:           ros-indigo-kobuki-bumper2pc
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS kobuki_bumper2pc package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_bumper2pc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-kobuki-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-kobuki-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
Bumper/cliff to pointcloud nodelet: Publish bumpers and cliff sensors events as
points in a pointcloud, so navistack can use them for poor-man navigation.
Implemented as a nodelet intended to run together with kobuki_node.

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
* Sat Aug 13 2016 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.7-0
- Autogenerated by Bloom

* Wed May 27 2015 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.6-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.4-1
- Autogenerated by Bloom

* Tue Aug 26 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.3-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.1-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.6.0-0
- Autogenerated by Bloom

