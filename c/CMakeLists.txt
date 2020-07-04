# *********************************************************************
# ACME-A
# *********************************************************************
cmake_minimum_required(VERSION 3.9.0 FATAL_ERROR)

project(acme-c CXX)

include(CMakePackageConfigHelpers)
include(CTest)

find_package(acme-a REQUIRED)
find_package(acme-b REQUIRED)


add_library(
    acme-c
    ${CMAKE_CURRENT_SOURCE_DIR}/include/acme/c.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/c.cpp)
set_target_properties(acme-c PROPERTIES OUTPUT_NAME "acme-c")

# Mandate the use of at least C++17 by everything that uses this
target_compile_features(acme-c PUBLIC cxx_std_17)

target_include_directories(
    acme-c
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
           $<INSTALL_INTERFACE:include>
    PRIVATE src)

target_link_libraries(acme-c ACME::a ACME::b)

# *********************************************************************
# Package / Install Stuff
# *********************************************************************

install(DIRECTORY include/ DESTINATION include)

install(
    TARGETS acme-c
    EXPORT acme-c-targets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    INCLUDES
    DESTINATION include)

add_library(ACME::c ALIAS acme-c)
install(
    EXPORT acme-c-targets
    FILE acme-c-targets.cmake
    NAMESPACE ACME::
    DESTINATION lib/cmake/acme-c)

file(
    WRITE "${PROJECT_BINARY_DIR}/acme-cConfig.cmake"
    "
include(CMakeFindDependencyMacro)
include(\"\${CMAKE_CURRENT_LIST_DIR}/acme-c-targets.cmake\")
")

write_basic_package_version_file(
    "${PROJECT_BINARY_DIR}/acme-cConfigVersion.cmake"
    VERSION 1.0.1
    COMPATIBILITY AnyNewerVersion)

install(FILES "${PROJECT_BINARY_DIR}/acme-cConfig.cmake"
              "${PROJECT_BINARY_DIR}/acme-cConfigVersion.cmake"
        DESTINATION lib/cmake/acme-c)
