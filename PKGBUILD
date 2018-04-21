# Script generated with Bloom
pkgdesc="ROS - Automatic docking for Kobuki: Users owning a docking station for Kobuki can use this tool to let Kobuki find its nest autonomously."
url='http://ros.org/wiki/kobuki_auto_docking'

pkgname='ros-kinetic-kobuki-auto-docking'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kobuki-dock-drive'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kobuki-dock-drive'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-yocs-cmd-vel-mux'
)

conflicts=()
replaces=()

_dir=kobuki_auto_docking
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_auto_docking $srcdir/kobuki_auto_docking
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

