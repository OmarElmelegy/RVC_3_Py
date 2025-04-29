# Robotics, Vision and Control (RVC3) Code Examples

This repository contains Python implementations of algorithms and concepts from the book "Robotics, Vision and Control" (3rd Edition) by Peter Corke, Witold Jachimczyk, and Ron Reeve.

## Repository Structure

The repository is organized by parts and chapters following the book structure:

### Part I: Modeling and Control
- **Chapter 2: Representing Position and Orientation**
  - Poses in 3D
  - Quaternions
  - Rotations and Logarithms
  - Twists in 3D
  - Using Classes for Representation

- **Chapter 3: Time-Varying Position and Orientation**
  - Spatial Velocity
  - Incremental Rotation
  - Dynamics of Moving Bodies
  - Trajectories (One-Dimensional, Multi-Axis, Multi-Segment)
  - Cartesian Motion in 3D
  - Interpolation of Orientation in 3D
  - Inertial Sensor Fusion and Orientation Estimation
  - Complementary Filters

### Part II: Mobile Robots
- **Chapter 4: Mobile Robot Vehicles**
  - Car-Like Vehicle Models
  - Path Following and Configuration Control
  - Point-to-Point Navigation
  - Line Following
  - Quadrotor Control and Simulation

## Requirements

The code examples utilize several Python libraries including:

- NumPy
- Matplotlib
- SciPy
- SpatialMath (Peter Corke's spatial mathematics toolbox)
- BDSim (Block Diagram Simulation library)

## Usage

Each Python file corresponds to a specific concept or algorithm from the book. The file naming convention includes the section number from the book in parentheses, for example:

```
Quaternions(2.3.1.7).py
```

refers to the Quaternions concept explained in section 2.3.1.7 of the book.

To run any example:

```bash
python "Part I/Chapter 2/PoseIn3D(2.3.2).py"
```

Most examples include visualizations that will be displayed when the script is executed.

## About the Book

"Robotics, Vision and Control: Fundamental Algorithms in Python" (3rd Edition) is a comprehensive resource for understanding robotics concepts, computer vision, and control systems using Python. The book covers topics ranging from representing position and orientation to robot dynamics and control.

For more information about the book, visit [Peter Corke's website](https://petercorke.com/rvc/).

## License

Please refer to the book's license for usage rights of these example implementations.
