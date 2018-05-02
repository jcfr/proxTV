cmake_minimum_required(VERSION 2.8.12)
#To avoid OpenMP warning: https://gitlab.kitware.com/cmake/cmake/issues/17292
if(POLICY CMP0054)
      cmake_policy(SET CMP0054 NEW)
endif()

project(proxTV
        DESCRIPTION "Toolbox for fast Total Variation proximity operators"
        LANGUAGES C CXX
        )

# Set VERSION
# Since cmake v3.0 we can just give an option to project(proxTV VERSION 3.2.1 LANGUAGES C CXX)
set(proxTV_VERSION_MAJOR 3)
set(proxTV_VERSION_MINOR 2)
set(proxTV_VERSION_PATCH 1)
# set(proxTV_VERSION_TWEAK 0)
set(proxTV_VERSION "${proxTV_VERSION_MAJOR}.${proxTV_VERSION_MINOR}.${proxTV_VERSION_PATCH}")
message(STATUS "proxTV version: ${proxTV_VERSION}")

# External Dependencies: {{{
# Use FindLAPACKE from local cmake folder
# FindLAPACK, FindOpenMP are already included in cmake installation.
# Threads is for pthreads flags.
# Append local module directory to the find_package search:
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

find_package(LAPACKE REQUIRED)
message(STATUS "Lapacke libraries: ${LAPACKE_LIBRARIES}")

find_package(LAPACK REQUIRED)
message(STATUS "Lapack libraries: ${LAPACK_LIBRARIES}")

find_package(Threads)

find_package(OpenMP)
message(STATUS "OpenMP found?: ${OpenMP_FOUND}")

add_subdirectory(src)

# Test
option(ENABLE_TESTING "Compile tests" OFF)
if(${ENABLE_TESTING})
    enable_testing()
    add_subdirectory(test)
endif()
