cmake_minimum_required(VERSION 3.10)


#set project name
project(qsort_test)

# specify the C++ standard
#set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the executable
add_executable(qsort main.cpp)

#target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

#target_include_directories(Tutorial PUBLIC 
#                            "${PROJECT_BINARY_DIR}"
#                             ${EXTRA_INCLUDES}
#                            )