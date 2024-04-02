cmake_minimum_required(VERSION 3.15...3.26)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(hello_cython)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)
find_package(PCL REQUIRED)

add_subdirectory(pypcl)
