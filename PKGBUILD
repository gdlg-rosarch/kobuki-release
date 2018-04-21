# Script generated with Bloom
pkgdesc="ROS - Keyboard teleoperation for Kobuki: relays commands from a keyboard to Kobuki."
url='http://ros.org/wiki/kobuki_keyop'

pkgname='ros-kinetic-kobuki-keyop'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-threads'
'ros-kinetic-ecl-time'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
)

depends=('ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-threads'
'ros-kinetic-ecl-time'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-yocs-cmd-vel-mux'
'ros-kinetic-yocs-velocity-smoother'
)

conflicts=()
replaces=()

_dir=kobuki_keyop
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_keyop $srcdir/kobuki_keyop
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

