cmake_minimum_required(VERSION 3.10)


include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_cython_target(_pointcloud CXX)
add_library(_pointcloud MODULE _pointcloud pcd_reader.cpp)

target_link_libraries(_pointcloud ${PCL_LIBRARIES}  ${PYTHON_LIBRARIES} )
target_include_directories(_pointcloud PUBLIC ${PYTHON_INCLUDE_DIRS} ./)
target_compile_definitions(_pointcloud PUBLIC ${PCL_DEFINITIONS})

python_extension_module(_pointcloud)

install(TARGETS _pointcloud LIBRARY DESTINATION pointclouds)
