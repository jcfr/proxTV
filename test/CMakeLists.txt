
set(KIT "${PROJECT_NAME}")

# To add more tests: append a name to test_names, and add_executable/add_test with that name
# Tests can be run with `ctest` in the build directory,
# it accepts regex, and different verbosity: ctest -R tv1 -VV

create_test_sourcelist(Tests ${KIT}CxxTests.cxx
  test_tv1_2d.cpp
  )

add_executable(${KIT}CxxTests ${Tests})
target_link_libraries(${KIT}CxxTests PUBLIC proxTV)

add_test(
    NAME test_tv1_2d
    COMMAND $<TARGET_FILE:${KIT}CxxTests> test_tv1_2d
    )
