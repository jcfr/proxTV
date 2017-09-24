
set(headers
    condat_fast_tv.h
    general.h
    johnsonRyanTV.h
    LPopt.h
    TVmacros.h
    TVopt.h
    utils.h
    )

# Install rule for headers
if(proxTV_INSTALL_DEVELOPMENT)
    install(FILES ${headers}
        DESTINATION ${proxTV_INSTALL_INCLUDE_DIR}
        COMPONENT Development
        )
endif()

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

#------------------------------------------------------------------------------
add_library(proxTV ${sources})

target_compile_definitions(proxTV PUBLIC NOMATLAB)

target_include_directories(proxTV
    PUBLIC
        $<BUILD_INTERFACE:${proxTV_SOURCE_DIR}/src>
        $<INSTALL_INTERFACE:${proxTV_INSTALL_INCLUDE_DIR}>
        ${LAPACKE_INCLUDE_DIRS} # Required to support older version of Lapacke not providing a config file
    )

# Link libraries
target_link_libraries(proxTV
    PUBLIC
        ${LAPACKE_LIBRARIES}
    )
if(Threads_FOUND)
    target_link_libraries(proxTV PUBLIC Threads::Threads)
endif()
if(OpenMP_FOUND)
    target_compile_options(proxTV PUBLIC ${OpenMP_CXX_FLAGS})
    target_link_libraries(proxTV PUBLIC ${OpenMP_CXX_LIBRARIES})
endif()

# Install proxTV target
if(proxTV_INSTALL_DEVELOPMENT OR BUILD_SHARED_LIBS)
  install(TARGETS proxTV EXPORT proxTVTargets
      ARCHIVE DESTINATION ${proxTV_INSTALL_LIB_DIR} COMPONENT Development
      LIBRARY DESTINATION ${proxTV_INSTALL_LIB_DIR} COMPONENT RuntimeLibraries
      RUNTIME DESTINATION ${proxTV_INSTALL_BIN_DIR} COMPONENT RuntimeLibraries
      )
endif()

