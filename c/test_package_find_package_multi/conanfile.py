import conans

class TestPackage(conans.ConanFile):

    generators = "cmake_find_package_multi"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        cmake = conans.CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(f"{self.build_folder}/c_test", run_environment=True)
