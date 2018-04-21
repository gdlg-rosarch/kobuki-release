# Script generated with Bloom
pkgdesc="ROS - ROS nodelet for Kobuki: ROS wrapper for the Kobuki driver."
url='http://ros.org/wiki/kobuki_node'

pkgname='ros-kinetic-kobuki-node'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-streams'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-driver'
'ros-kinetic-kobuki-ftdi'
'ros-kinetic-kobuki-keyop'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-kobuki-safety-controller'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-angles'
'ros-kinetic-capabilities'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-streams'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-driver'
'ros-kinetic-kobuki-ftdi'
'ros-kinetic-kobuki-keyop'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-kobuki-rapps'
'ros-kinetic-kobuki-safety-controller'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=kobuki_node
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_node $srcdir/kobuki_node
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

