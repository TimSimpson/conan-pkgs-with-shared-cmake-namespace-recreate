cmake_minimum_required(VERSION 3.5)
project(test_package)

set(CMAKE_CXX_STANDARD 17)

find_package(acme-a REQUIRED)

add_executable(a_test ${CMAKE_CURRENT_SOURCE_DIR}/a_test.cpp)
target_link_libraries(a_test PUBLIC ACME::a)
