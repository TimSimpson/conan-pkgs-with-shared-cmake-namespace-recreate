cmake_minimum_required(VERSION 3.5)
project(test_package)

set(CMAKE_CXX_STANDARD 17)

find_package(acme-b REQUIRED)

add_executable(b_test ${CMAKE_CURRENT_SOURCE_DIR}/b_test.cpp)
target_link_libraries(b_test PUBLIC ACME::b)
