cmake_minimum_required(VERSION 3.5)
project(test_package)

set(CMAKE_CXX_STANDARD 17)

find_package(acme-c REQUIRED)

add_executable(c_test ${CMAKE_CURRENT_SOURCE_DIR}/c_test.cpp)
target_link_libraries(c_test PUBLIC ACME::c)
