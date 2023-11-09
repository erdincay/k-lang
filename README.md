# k-lang

GTK4 application using Conan/Meson

- steps to build this project:
    - create the build directory in the project root
        - `mkdir build`
    - change into the folder and install the dependencies
        - `cd build`
        - `conan install ..`
    - build the application in the build directory 
        - `conan build ..`
    - execute the application (Linux Shell)
        - `./k-lang`
