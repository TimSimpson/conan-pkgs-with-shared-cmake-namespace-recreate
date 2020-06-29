import conans

class TestPackage(conans.ConanFile):

    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        cmake = conans.CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(f"{self.build_folder}/b_test", run_environment=True)
