# VizDoom with OpenAI Gym: Setup and Installation Guide

This guide provides step-by-step instructions to set up Python, OpenAI Gym, and VizDoom for running AI experiments in the VizDoom environment. Follow these steps to get started quickly.

## Prerequisites

Before proceeding, ensure you have the following installed:

1. **Python (>=3.6):** [Download Python](https://www.python.org/downloads/)
2. **OpenAI Gym:** Used for reinforcement learning environments.
3. **VizDoom Dependencies:** Including CMake, Visual Studio Build Tools, and 7-Zip.

## Installation Guide

### 1. Install Python
- Download and install Python (version 3.6 or higher) from the [official website](https://www.python.org/).
- Ensure you add Python to your system's PATH during the installation.

### 2. Install OpenAI Gym
- Open a command prompt (or terminal) and run:
  ```bash
  pip install gym
  ```

### 3. Install VizDoom Dependencies

#### a. Download and Install Required Tools
- **CMake:** [Download CMake](https://cmake.org/download/)
- **Visual Studio Build Tools:** [Download Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **7-Zip:** [Download 7-Zip](https://www.7-zip.org/download.html)

### 4. Download VizDoom Source Code
- Download the VizDoom source code from the [VizDoom GitHub repository](https://github.com/mwydmuch/ViZDoom).
- Extract the downloaded zip file using 7-Zip or another extraction tool.

### 5. Build VizDoom

1. Open a command prompt and navigate to the extracted VizDoom folder:
   ```bash
   cd path\to\vizdoom-folder
   ```
2. Create a build directory and navigate into it:
   ```bash
   mkdir build
   cd build
   ```
3. Run CMake to configure the build:
   ```bash
   cmake ..
   ```
4. Build VizDoom using the following command:
   ```bash
   cmake --build . --config Release
   ```

### 6. Install VizDoom

- After building, locate `vizdoom.dll` in the `bin` folder of the build directory.
- Copy `vizdoom.dll` to a location included in your system's PATH environment variable.

---

## Running the Project

Once the installation is complete, you're ready to run VizDoom environments with OpenAI Gym.

Make sure you have the required Python scripts and configurations in place to start your AI experiments.

For more details, check out the official [VizDoom documentation](https://vizdoom.cs.put.edu.pl/).

---

## Troubleshooting

If you encounter issues during installation or setup, consider the following:

- Verify your system's PATH includes Python, CMake, and `vizdoom.dll`.
- Ensure all dependencies (e.g., CMake, Visual Studio Build Tools) are installed correctly.
- For additional help, consult the [VizDoom GitHub Issues](https://github.com/mwydmuch/ViZDoom/issues).

Happy coding!
