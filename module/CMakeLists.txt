#===============================================================================
#                       1. VERIFY LLVM INSTALLATION DIR
#===============================================================================
set(LLVM_INSTALL_DIR "/usr/lib/llvm-18" CACHE PATH "LLVM installation directory")

# 1.1 Check the "include" directory
set(LLVM_INCLUDE_DIR ${LLVM_INSTALL_DIR}/include/llvm)
if(NOT EXISTS ${LLVM_INCLUDE_DIR})
message(FATAL_ERROR
  " LLVM_INSTALL_DIR (${LLVM_INCLUDE_DIR}) is invalid.")
endif()

# 1.2 Check that the LLVMConfig.cmake file exists (the location depends on the OS)
set(VALID_INSTALLATION FALSE)

# Ubuntu + Darwin
if(EXISTS "${LLVM_INSTALL_DIR}/lib/cmake/llvm/LLVMConfig.cmake")
  set(VALID_INSTALLATION TRUE)
endif()

# Fedora
if(EXISTS "${LLVM_INSTALL_DIR}/lib64/cmake/llvm/LLVMConfig.cmake")
  set(VALID_INSTALLATION TRUE)
endif()

if(NOT ${VALID_INSTALLATION})
  message(FATAL_ERROR
    "LLVM installation directory, (${LLVM_INSTALL_DIR}), is invalid. Couldn't
    find LLVMConfig.cmake.")
endif()

#===============================================================================
# 2. LOAD LLVM CONFIGURATION
#    For more: http://llvm.org/docs/CMake.html#embedding-llvm-in-your-project
#===============================================================================
# Add the location of LLVMConfig.cmake to CMake search paths (so that
# find_package can locate it)
# Note: On Fedora, when using the pre-compiled binaries installed with `dnf`,
# LLVMConfig.cmake is located in "/usr/lib64/cmake/llvm". But this path is
# among other paths that will be checked by default when using
# `find_package(llvm)`. So there's no need to add it here.
list(APPEND CMAKE_PREFIX_PATH ${LLVM_INSTALL_DIR}/lib/cmake/llvm/)

# The way LLVMConfigVersion.cmake is set up, it will only match MAJOR.MINOR
# exactly, even if we do not specify "REQUIRED" in the statement below.
# So we accept any version and do the proper ranged check below.
find_package(LLVM REQUIRED CONFIG)

# We defer the version checking to this statement
if("${LLVM_VERSION_MAJOR}" VERSION_LESS 18)
  message(FATAL_ERROR "Found LLVM ${LLVM_VERSION_MAJOR}, but need LLVM 18 or above")
endif()

message(STATUS "Found LLVM ${LLVM_PACKAGE_VERSION}")
message(STATUS "Using LLVMConfig.cmake in: ${LLVM_INSTALL_DIR}")

message("LLVM STATUS:
  Definitions ${LLVM_DEFINITIONS}
  Includes    ${LLVM_INCLUDE_DIRS}
  Libraries   ${LLVM_LIBRARY_DIRS}
  Targets     ${LLVM_TARGETS_TO_BUILD}"
)

# Set the LLVM header and library paths
include_directories(SYSTEM ${LLVM_INCLUDE_DIRS})
link_directories(${LLVM_LIBRARY_DIRS})
add_definitions(${LLVM_DEFINITIONS})

#===============================================================================
# 3. LLVM BUILD CONFIGURATION
#===============================================================================

# Build type
if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug CACHE
      STRING "Build type (default Debug):" FORCE)
endif()

# Compiler flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall\
  -fdiagnostics-color=always")

# LLVM is normally built without RTTI. Be consistent with that.
if(NOT LLVM_ENABLE_RTTI)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-rtti")
endif()

# -fvisibility-inlines-hidden is set when building LLVM and on Darwin warnings
# are triggered if llvm-tutor is built without this flag (though otherwise it
# builds fine). For consistency, add it here too.
include(CheckCXXCompilerFlag)
check_cxx_compiler_flag("-fvisibility-inlines-hidden" SUPPORTS_FVISIBILITY_INLINES_HIDDEN_FLAG)
if (${SUPPORTS_FVISIBILITY_INLINES_HIDDEN_FLAG} EQUAL "1")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility-inlines-hidden")
endif()

# Set the build directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)

set(INCL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)


# =============================================================================== 
#  ADD SUB-TARGETS
# =============================================================================== 

# Exclusion for pre-build
add_subdirectory(src/Util)

# =============================================================================== 
#  ADD Executable
# =============================================================================== 
add_subdirectory(src/Core EXCLUDE_FROM_ALL)
add_executable(detector EXCLUDE_FROM_ALL src/main.cc)

target_include_directories(detector PRIVATE 
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(detector PRIVATE
  Core
)
