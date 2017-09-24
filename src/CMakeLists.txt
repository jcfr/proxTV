cmake_minimum_required(VERSION 2.8.12)
#To avoid OpenMP warning: https://gitlab.kitware.com/cmake/cmake/issues/17292
if(POLICY CMP0054)
      cmake_policy(SET CMP0054 NEW)
endif()

project(proxTV)
set(headers
    condat_fast_tv.h
    general.h
    johnsonRyanTV.h
    LPopt.h
    TVmacros.h
    TVopt.h
    utils.h
    )

set(sources
    condat_fast_tv.cpp
    johnsonRyanTV.cpp
    LPopt.cpp
    TV2Dopt.cpp
    TV2DWopt.cpp
    TVgenopt.cpp
    TVL1opt.cpp
    TVL1opt_hybridtautstring.cpp
    TVL1opt_kolmogorov.cpp
    TVL1opt_tautstring.cpp
    TVL1Wopt.cpp
    TVL2opt.cpp
    TVLPopt.cpp
    TVNDopt.cpp
    utils.cpp
    )

# External Dependencies:

find_package (Threads)
find_package(LAPACKE REQUIRED)
message(STATUS "Lapacke found?: ${LAPACKE_FOUND}")
message(STATUS "Lapacke libraries: ${LAPACKE_LIBRARIES}")
find_package(LAPACK REQUIRED)
message(STATUS "Lapack found?: ${LAPACKE_FOUND}")
message(STATUS "Lapack libraries: ${LAPACK_LIBRARIES}")

find_package(OpenMP)
message(STATUS "OpenMP found?: ${OpenMP_FOUND}")
# No way to do it via targets, do it old way.
if(${OpenMP_FOUND})
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

add_library(proxTV ${sources})

target_compile_definitions(proxTV PUBLIC
    NOMATLAB
    )

# Create directory with headers at build and install time.
file(COPY ${headers}
    DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/include")
install(FILES ${headers}
    DESTINATION include)

target_include_directories(proxTV PUBLIC
    $<BUILD_INTERFACE:${proxTV_BINARY_DIR}/include>
    $<INSTALL_INTERFACE:include>
    ${LAPACKE_INCLUDE_DIRS}
    )

target_link_libraries(proxTV PUBLIC
    ${LAPACKE_LIBRARIES}
    ${LAPACK_LIBRARIES}
    ${CMAKE_THREAD_LIBS_INIT}
    )

install(TARGETS proxTV EXPORT proxTVTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )
install(EXPORT proxTVTargets
    FILE proxTVTargets.cmake
    NAMESPACE proxTV::
    DESTINATION lib/cmake/proxTV
    )

# Test
option(ENABLE_TESTING "Compile tests" OFF)
if(${ENABLE_TESTING})
    enable_testing()
    add_executable(test_tv1_2d "./test/test_tv1_2d.cpp")
    target_include_directories(test_tv1_2d PUBLIC
        $<BUILD_INTERFACE:${proxTV_BINARY_DIR}/include>)
    target_compile_definitions(test_tv1_2d PUBLIC NOMATLAB)
    target_link_libraries(test_tv1_2d
        PUBLIC
        proxTV)
    add_test(NAME tv1_2d COMMAND test_tv1_2d)
endif()

