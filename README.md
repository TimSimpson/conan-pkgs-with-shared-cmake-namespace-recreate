# Cona Pkgs with Shared CMake Namespace Recreate

This models a use case where multiple C++ packages export CMake targets which share a namespace. An example would be the vcpkg's for SDL2 and SDL2-image, which both export CMake targets starting with "SDL2::".

Here all the projects use the namespace `ACME::[name]`. To make things more confusing, you include them from CMake by calling `find_package(acme-[name])`. This models real life where everyone likes to make things as inconsistent as possible when naming things.

