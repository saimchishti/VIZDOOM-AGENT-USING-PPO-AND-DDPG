Prerequisites
Before running the project, make sure you have the following dependencies installed:

Python (>=3.6)
OpenAI Gym
VizDoom
Installation
1. Python
Make sure you have Python installed on your system. You can download Python from here.

2. OpenAI Gym
Install OpenAI Gym using the following command:

bash
Copy code
pip install gym
3. VizDoom
VizDoom is required for the project, and you can install it with the following steps:

3.1 Install Dependencies
Download and install the required dependencies from the following links:

CMake
Visual Studio Build Tools
7-Zip
3.2 Clone and Build VizDoom
3.2.1 Download the Source Code
Download the VizDoom source code zip file from the VizDoom GitHub repository.

3.2.2 Extract and Build
Extract the downloaded zip file using 7-Zip or a similar tool.
Open a command prompt and navigate to the extracted folder.
Run the following commands to build VizDoom:
bash
Copy code
mkdir build
cd build
cmake ..
cmake --build . --config Release
3.3 Install VizDoom
Copy the generated vizdoom.dll from the bin folder to a location included in your system's PATH environment variable.
