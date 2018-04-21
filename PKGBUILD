# Script generated with Bloom
pkgdesc="ROS - Description of the Kobuki model. Provides the model description of Kobuki for simulation and visualisation. The files in this package are parsed and used by a variety of other components. Most users will not interact directly with this package. WARNING: This package is disabled because it cannot be catkinized by now, as xacro dependency is not catkin still. In the interim we use a unary pre-catkin stack named kobuki_description."
url='http://ros.org/wiki/kobuki_description'

pkgname='ros-kinetic-kobuki-description'
pkgver='0.7.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-urdf'
'ros-kinetic-xacro'
)

depends=('ros-kinetic-urdf'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=kobuki_description
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_description $srcdir/kobuki_description
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

