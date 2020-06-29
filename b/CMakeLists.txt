# *********************************************************************
# ACME-A
# *********************************************************************
cmake_minimum_required(VERSION 3.9.0 FATAL_ERROR)

project(acme-b CXX)

include(CMakePackageConfigHelpers)
include(CTest)

find_package(acme-a REQUIRED)

add_library(
    acme-b
    ${CMAKE_CURRENT_SOURCE_DIR}/include/acme/b.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/b.cpp)
set_target_properties(acme-b PROPERTIES OUTPUT_NAME "acme-b")

# Mandate the use of at least C++17 by everything that uses this
target_compile_features(acme-b PUBLIC cxx_std_17)

target_include_directories(
    acme-b
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
           $<INSTALL_INTERFACE:include>
    PRIVATE src)

target_link_libraries(acme-b ACME::a)

# *********************************************************************
# Package / Install Stuff
# *********************************************************************

install(DIRECTORY include/ DESTINATION include)

install(
    TARGETS acme-b
    EXPORT acme-b-targets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    INCLUDES
    DESTINATION include)

add_library(ACME::b ALIAS acme-b)
install(
    EXPORT acme-b-targets
    FILE acme-b-targets.cmake
    NAMESPACE ACME::
    DESTINATION lib/cmake/acme-b)

file(
    WRITE "${PROJECT_BINARY_DIR}/acme-bConfig.cmake"
    "
include(CMakeFindDependencyMacro)
include(\"\${CMAKE_CURRENT_LIST_DIR}/acme-b-targets.cmake\")
")

write_basic_package_version_file(
    "${PROJECT_BINARY_DIR}/acme-bConfigVersion.cmake"
    VERSION 1.0.1
    COMPATIBILITY AnyNewerVersion)

install(FILES "${PROJECT_BINARY_DIR}/acme-bConfig.cmake"
              "${PROJECT_BINARY_DIR}/acme-bConfigVersion.cmake"
        DESTINATION lib/cmake/acme-b)
