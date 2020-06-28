# *********************************************************************
# ACME-A
# *********************************************************************
cmake_minimum_required(VERSION 3.9.0 FATAL_ERROR)

project(acme-a CXX)

include(CMakePackageConfigHelpers)
include(CTest)

add_library(
    acme-a
    ${CMAKE_CURRENT_SOURCE_DIR}/include/acme/a.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/a.cpp)
set_target_properties(acme-a PROPERTIES OUTPUT_NAME "acme-a")

# Mandate the use of at least C++17 by everything that uses this
target_compile_features(acme-a PUBLIC cxx_std_17)

target_include_directories(
    acme-a
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
           $<INSTALL_INTERFACE:include>
    PRIVATE src)

# *********************************************************************
# Package / Install Stuff
# *********************************************************************

install(DIRECTORY include/ DESTINATION include)

install(
    TARGETS acme-a
    EXPORT acme-a-targets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    INCLUDES
    DESTINATION include)

add_library(ACME::a ALIAS acme-a)
install(
    EXPORT acme-a-targets
    FILE acme-a-targets.cmake
    NAMESPACE ACME::
    DESTINATION lib/cmake/acme-a)

file(
    WRITE "${PROJECT_BINARY_DIR}/acme-aConfig.cmake"
    "
include(CMakeFindDependencyMacro)
include(\"\${CMAKE_CURRENT_LIST_DIR}/acme-a-targets.cmake\")
")

write_basic_package_version_file(
    "${PROJECT_BINARY_DIR}/acme-aConfigVersion.cmake"
    VERSION 1.0.1
    COMPATIBILITY AnyNewerVersion)

install(FILES "${PROJECT_BINARY_DIR}/acme-aConfig.cmake"
              "${PROJECT_BINARY_DIR}/acme-aConfigVersion.cmake"
        DESTINATION lib/cmake/acme-a)
