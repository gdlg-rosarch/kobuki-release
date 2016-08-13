Name:           ros-kinetic-kobuki
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS kobuki package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-kobuki-auto-docking
Requires:       ros-kinetic-kobuki-bumper2pc
Requires:       ros-kinetic-kobuki-capabilities
Requires:       ros-kinetic-kobuki-controller-tutorial
Requires:       ros-kinetic-kobuki-description
Requires:       ros-kinetic-kobuki-keyop
Requires:       ros-kinetic-kobuki-node
Requires:       ros-kinetic-kobuki-random-walker
Requires:       ros-kinetic-kobuki-rapps
Requires:       ros-kinetic-kobuki-safety-controller
Requires:       ros-kinetic-kobuki-testsuite
BuildRequires:  ros-kinetic-catkin

%description
Software for Kobuki, Yujin Robot's mobile research base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Aug 13 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.7.1-0
- Autogenerated by Bloom

* Tue Jun 21 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.7.0-0
- Autogenerated by Bloom

