import os.path

import conans


class Lp3Main(conans.ConanFile):
    name = "acme-b"
    version = "1.0.0"
    license = "Zlib"
    author = "Tim Simpson"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    requires = [
        "acme-a/1.0.0@TimSimpson/testing",
    ]

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
        self.cpp_info.name = "acme-b"
        self.cpp_info.filenames['cmake_find_package'] = "acme-b"
        self.cpp_info.names['cmake_find_package'] = "ACME"
        self.cpp_info.components['b'].names["cmake_find_package"] = "b"
        self.cpp_info.components['b'].libs = [ "acme-b" ]
        # In CMake, the exported target will be ACME::a but it comes from the
        # COnan package named `acme-a`, which has a component named `a`.
        self.cpp_info.components['b'].requires = [ "acme-a::a"]
