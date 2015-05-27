Name:           ros-indigo-kobuki-description
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS kobuki_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
Description of the Kobuki model. Provides the model description of Kobuki for
simulation and visualisation. The files in this package are parsed and used by a
variety of other components. Most users will not interact directly with this
package. WARNING: This package is disabled because it cannot be catkinized by
now, as xacro dependency is not catkin still. In the interim we use a unary pre-
catkin stack named kobuki_description.

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
* Wed May 27 2015 Younghun Ju <yhju@yujinrobot.com> - 0.6.6-0
- Autogenerated by Bloom

