# Conan Pkgs with Shared CMake Namespace Recreate

This models a use case where multiple C++ packages export CMake targets which share a namespace. An example would be the vcpkg's for SDL2 and SDL2-image, which both export CMake targets starting with "SDL2::".

Here all the projects use the namespace `ACME::[name]`. To make things more confusing, you include them from CMake by calling `find_package(acme-[name])`. This models real life where everyone likes to make things as inconsistent as possible when naming things.

## Weird Requirements

This currently supports the use of an attribute `self.cpp.filenames['cmake_find_package']` which is not in Conan trunk. See [here](https://github.com/conan-io/conan/issues/7254).

## Usage


Run the Conan test package workflow on A, in the process exporting it to your local cache, then do it for B.

If you want something more specific of don't know the common Conan idioms like the back of your hand, I personally use [this repo](https://github.com/TimSimpson/ci-land) and then just run

```bash
git clone https://github.com/TimSimpson/ci-land
set PROFILE=clang-8-d-static
pushd a
../ci-land/cil conan package all
popd
pushd b
../ci-land/cil conan package all
```

