# Script generated with Bloom
pkgdesc="ROS - Software for Kobuki, Yujin Robot's mobile research base."
url='http://ros.org/wiki/kobuki'

pkgname='ros-kinetic-kobuki'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-kobuki-auto-docking'
'ros-kinetic-kobuki-bumper2pc'
'ros-kinetic-kobuki-capabilities'
'ros-kinetic-kobuki-controller-tutorial'
'ros-kinetic-kobuki-description'
'ros-kinetic-kobuki-keyop'
'ros-kinetic-kobuki-node'
'ros-kinetic-kobuki-random-walker'
'ros-kinetic-kobuki-rapps'
'ros-kinetic-kobuki-safety-controller'
'ros-kinetic-kobuki-testsuite'
)

conflicts=()
replaces=()

_dir=kobuki
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki $srcdir/kobuki
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

