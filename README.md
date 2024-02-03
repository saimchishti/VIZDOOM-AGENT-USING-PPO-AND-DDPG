Prerequisites:
Python (>=3.6):
Download and install Python from the official website.
OpenAI Gym:
Install OpenAI Gym:
Open a command prompt and run the following command:

pip install gym
VizDoom:
Install VizDoom Dependencies:

Download and install the following dependencies:
CMake
Visual Studio Build Tools
7-Zip
Download VizDoom Source Code:

Download the VizDoom source code zip file from the VizDoom GitHub Repository.
Extract and Build VizDoom:

Extract the downloaded zip file using 7-Zip or a similar tool.
Open a command prompt and navigate to the extracted folder.
Run the following commands:

mkdir build
cd build
cmake ..
cmake --build . --config Release
Install VizDoom:

Copy the generated vizdoom.dll from the bin folder to a location included in your system's PATH environment variable.
Running the Project:
