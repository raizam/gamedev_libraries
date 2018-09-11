# junkyard_gfx

A Collection of small C/C++ libraries for game development

![header](https://raw.githubusercontent.com/raizam/junkyard_gfx/master/header.jpg)

* [General purpose](#general-purpose)
* [Math](#math)
* [Meshes / geometry](#meshes-geometry)
* [Texture Backing](#texture-baking)
* [Scenegraphs](#scenegraphs-ecs)
* [Animation](#animation)
* [Threading](#threading)
* [Physics and Collision](#physics-and-collision)
* [Renderers](#renderers)
* [Networking](#networking)

## General purpose

- [bkaradzic/bx](https://github.com/bkaradzic/bx) - Base library
- [septag/sx](https://github.com/septag/sx) - Portable base library for C programmers, tailored for performance and simplicity
- [rhoot/sp](https://github.com/rhoot/sp) - Public domain string formatting micro-library for C++, based on python-style format strings
- [nothings/stb](https://github.com/nothings/stb) - stb single-file public domain libraries for C/C++
- [RandyGaul/cute_headers](https://github.com/RandyGaul/cute_headers) - One-file C/C++ libraries with no dependencies, primarily used for games 
- [vurtun/mmx](https://github.com/vurtun/mmx) - single header libraries for C/C++ 
- [zpl-c/zpl](https://github.com/zpl-c/zpl) - Your C99 Powerkit 
- [rmitton/rjm](https://github.com/rmitton/rjm) - Various single-file C libraries. 

## Math

- [g-truc/glm](https://github.com/g-truc/glm) - OpenGL Mathematics (GLM)
- [recp/cglm](https://github.com/recp/cglm) - Optimized OpenGL/Graphics Math (glm) for C
- [google/mathfu](https://github.com/google/mathfu) - C++ math library developed primarily for games focused on simplicity and efficiency.
- [ferreiradaselva/mathc](https://github.com/ferreiradaselva/mathc) - Pure C math library for 2D and 3D programming
- [demianmnave/CML](https://github.com/demianmnave/CML) The Configurable Math Library http://cmldev.net
- [sce_vectormath](https://github.com/erwincoumans/sce_vectormath) - Vector math library
- [Imath](https://github.com/openexr/openexr/tree/develop/IlmBase/Imath) - Imath
- [Handmade-Math](https://github.com/HandmadeMath/Handmade-Math) - A simple math library for games and computer graphics.

## Meshes / Geometry

- [libigl](https://github.com/libigl/libigl) - Simple C++ geometry processing library
- [MathGeoLib](https://github.com/juj/MathGeoLib) - library for linear algebra and geometry manipulation for computer graphics
- [sseculling](https://github.com/nsf/sseculling) - SSE Frustum Culling Demo
- [Cullminator9000](https://github.com/Alan-FGR/Cullminator9000) - The fastest culler ever
- [SeamAwareDecimater](https://github.com/songrun/SeamAwareDecimater) - Mesh simplification with UV's boundary preserved
- [zeux/meshoptimizer](https://github.com/zeux/meshoptimizer) - Mesh optimization library that makes indexed meshes more GPU-friendly

## Assets Importers/Exporters
- [assimp](https://github.com/assimp/assimp) - Official Open Asset Import Library Repository. Loads 40+ 3D file formats into one unified and clean data structure
- [nem0/OpenFBX](https://github.com/nem0/OpenFBX) - Lightweight open source FBX importer 
- [syoyo/tinyobjloader](https://github.com/syoyo/tinyobjloader) - Tiny but powerful single file wavefront obj loader 
- [syoyo/tinygltfloader](https://github.com/syoyo/tinygltfloader) - Header only C++ Tiny glTF loader. 

## Texture Baking

- [caosdoar/Fornos](https://github.com/caosdoar/Fornos) - GPU Texture Baking Tool. A fast and simple tool to bake your high-poly mesh details to textures.
- [kmkolasinski/AwesomeBump](https://github.com/kmkolasinski/AwesomeBump) - AwesomeBump generate normal, height, specular or ambient occlusion textures from a single image
- [dariomanesku/cmft](https://github.com/dariomanesku/cmft), [dariomanesku/cmftStudio](https://github.com/dariomanesku/cmftStudio) - Cross-platform open-source command-line cubemap filtering tool

## Scenegraphs / ECS

- [buserror/libc3](https://github.com/buserror/libc3) - Lightweight C Scene Graph Library
- [skypjack/entt](https://github.com/skypjack/entt) - A fast and reliable entity-component system (ECS) and much more
- [redxdev/ECS](https://github.com/redxdev/ECS) - C++ single-header entity component system library
- [alecthomas/entityx](https://github.com/alecthomas/entityx) - EntityX - A fast, type-safe C++ Entity-Component system

## Animation

- [guillaumeblanc/ozz-animation](https://github.com/guillaumeblanc/ozz-animation) - Open source c++ skeletal animation library and toolset

## Threading

- [rhoot/sc](https://github.com/rhoot/sc) - Cross platform co-routine library exposed through a minimal C API
- [deboost.context](https://github.com/septag/deboost.context) - "Deboostified" version of boost.context (coroutines), Plain and simple C API for context switching. Easy build on multiple platforms.
- [SergeyMakeev/TaskScheduler](https://github.com/SergeyMakeev/TaskScheduler) - Multithreaded task scheduler experiments
- [dougbinks/enkiTS](https://github.com/dougbinks/enkiTS) - C++ and C multithreading task scheduler

## Physics and Collision

- [gjk.c](https://github.com/kroitor/gjk.c) - Gilbert-Johnson-Keerthi (GJK) collision detection algorithm
- [nudge](https://github.com/rasmusbarr/nudge) - A small data-oriented and SIMD-optimized 3D rigid body physics library.
- [gpu sph fluids](https://github.com/erwincoumans/fluids_v3) - GPU SPH fluids 
- [phyx](https://github.com/zeux/phyx) - 2D physics engine with SoA/SIMD optimizations
- [ParticleSolver](https://github.com/ebirenbaum/ParticleSolver) - CPU and GPU implementations of a particle-based physics
- [PlayRho](https://github.com/louis-langholtz/PlayRho) - Real-time oriented physics engine and library that's currently best suited for 2D games
- [Chipmunk2D](https://github.com/slembcke/Chipmunk2D) - A fast and lightweight 2D game physics library.
- [PositionBasedDynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) PositionBasedDynamics is a library for the physically-based simulation of rigid bodies, deformable solids and fluids

## Renderers

- [bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) - Cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library.
- [Kode/Kore](https://github.com/Kode/Kore) - Modern low level game library and hardware abstraction
- [floooh/sokol](https://github.com/floooh/sokol) - minimal cross-platform standalone C headers
- [floooh/oryol](https://github.com/floooh/oryol) - A small, portable and extensible C++ 3D coding framework
- [pplux/px](https://github.com/pplux/px) - Single header C++ Libraries for Thread Scheduling, Rendering
- [google/filament](https://github.com/google/filament) - Filament is a real-time physically based rendering engine for Android, Windows, Linux and macOS
- [fastuidraw](https://github.com/intel/fastuidraw) - library that provides a higher performance Canvas interface


## Texture Packing

- [Cheetah-Texture-Packer](https://github.com/scriptum/Cheetah-Texture-Packer) - High efficient and fast 2D bin packing tool
- [thekla_atlas](https://github.com/Thekla/thekla_atlas) - Atlas Generation Tool

## Sound

- [openal-soft](https://github.com/kcat/openal-soft) - software implementation of the OpenAL 3D audio API
- [soloud](https://github.com/jarikomppa/soloud) - Free, easy, portable audio engine for games

## UI
- [ocornut/imgui](https://github.com/ocornut/imgui) - Dear ImGui: Bloat-free Immediate Mode Graphical User interface for C++ with minimal dependencies
- [vurtun/nuklear](https://github.com/vurtun/nuklear) - A single-header ANSI C gui library

## Pathfinding and Navigation

- [jps](https://github.com/fgenesis/jps) - Jump Point Search, public domain, single .h (Super fast pathfinding on uniform grids)
- [astar-algorithm-cpp](https://github.com/justinhj/astar-algorithm-cpp) - Implementations of the A* algorithm in C++ and C#
- [MicroPather](https://github.com/leethomason/MicroPather) - A* solver (astar or a-star) written in platform independent C++
- [recastnavigation](https://github.com/recastnavigation/recastnavigation) - Navigation-mesh Toolset for Games

## Input

- [SDL](https://github.com/SDL-mirror/SDL) - Simple DirectMedia Layer
- [glfw](https://github.com/glfw/glfw) - A multi-platform library
- [gainput](https://github.com/jkuhlmann/gainput) - C++ input library for games

## Networking

- [librg](https://github.com/librg/librg) - Pure C99 game networking library
- [bkaradzic/bnet](https://github.com/bkaradzic/bnet#bnet---message-oriented-networking-library) - Message oriented networking library using TCP transport
- [zeromq/libzmq](https://github.com/zeromq/libzmq) - ZeroMQ core engine in C++, implements ZMTP/3.1 http://www.zeromq.org


## Misc

- [easy_profiler](https://github.com/yse/easy_profiler) - Lightweight profiler library for c++
- [spdlog](https://github.com/gabime/spdlog) - Fast C++ logging library.
- [color](https://github.com/dmilos/color) - C++ library thats implemets class color
- [libmorton](https://github.com/Forceflow/libmorton) - C++ header-only library with methods to efficiently encode/decode Morton codes
- [pugixml](https://github.com/zeux/pugixml) - Light-weight, simple and fast XML parser for C++ with XPath support
- [opengex](http://opengex.org/) - Scene format specification















