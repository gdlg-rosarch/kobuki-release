# Script generated with Bloom
pkgdesc="ROS - Random walker app for Kobuki"
url='http://ros.org/wiki/kobuki_random_walker'

pkgname='ros-kinetic-kobuki-random-walker'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-yocs-controllers'
)

depends=('ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-yocs-cmd-vel-mux'
'ros-kinetic-yocs-controllers'
)

conflicts=()
replaces=()

_dir=kobuki_random_walker
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_random_walker $srcdir/kobuki_random_walker
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

