cmake_minimum_required(VERSION 3.10)

# set the project name
project(executor)

file(GLOB SOURCES
    headers/*.h
    source/*.cpp
)

add_executable(executor ${SOURCES})                      )

# add the executable
add_executable(executor.cpp)