import os.path

import conans


class Lp3Main(conans.ConanFile):
    name = "acme-a"
    version = "1.0.0"
    license = "Zlib"
    author = "Tim Simpson"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    requires = tuple()

    build_requires = []

    generators = "cmake_find_package"

    exports_sources = (
        "src/*", "include/*", "demos/*", "tests/*", "CMakeLists.txt", "cmake/*",
    )

    def _configed_cmake(self):
        cmake = conans.CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configed_cmake()
        cmake.build()

    def package(self):
        cmake = self._configed_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.name = "acme-a"
        self.cpp_info.filenames['cmake_find_package'] = "acme-a"
        self.cpp_info.names['cmake_find_package'] = "ACME"
        self.cpp_info.components['a'].names["cmake_find_package"] = "a"
        self.cpp_info.components['a'].libs = [ "acme-a" ]


