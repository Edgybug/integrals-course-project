# Integrals Course Project

A practical introduction to definite integrals and double integrals, combining mathematical explanations, analytical solutions, numerical approximations, Python visualizations, and real-world applications.

## Overview

This project explores the concept of integration, starting with the geometric interpretation of definite integrals and gradually extending to applications in physics, probability, and geometry.

The project also introduces double integrals and demonstrates their practical use in estimating excavation volumes from terrain elevation data.

## Topics Covered

1. **Introduction to Integration** – Understanding accumulation and the area under a curve.
2. **Riemann Sums** – Approximating definite integrals using rectangles.
3. **Definite Integrals** – Connecting numerical approximations with analytical solutions.
4. **Velocity and Distance** – Calculating distance from a velocity function.
5. **Variable Force and Work** – Applying integration to calculate mechanical work.
6. **Probability Density Functions** – Using integration to calculate probabilities.
7. **Extending Integration to Two Dimensions** – Introducing functions of two variables and double integrals.
8. **Calculating Volume with Double Integrals** – Comparing analytical and numerical volume calculations.
9. **Estimating Excavation Volume** – Applying numerical integration to synthetic terrain and real elevation data.

## Technologies and Libraries

- **Python** – Main programming language.
- **NumPy** – Numerical calculations and array operations.
- **Pandas** - Minor usage for displaying data in a better way
- **Matplotlib** – 2D and 3D visualizations.
- **SymPy** – Symbolic mathematics and analytical integration.
- **Rasterio** – Reading and processing geospatial raster data.
- **Jupyter Notebook** – Interactive development and presentation.

## Real-World Application

The final chapter uses the Copernicus DEM GLO-30 elevation dataset to demonstrate how double integration can be applied to estimate excavation volume.

The example includes:
- Loading and inspecting raster elevation data.
- Understanding raster resolution and coordinate systems.
- Defining an excavation target elevation.
- Calculating excavation depth and volume.
- Estimating loose material volume, truck trips, and illustrative costs.

The real-world example is educational. Its assumptions and results are not intended to replace a professional engineering survey or construction estimate.

## Requirements

Python 3 and the libraries listed in `requirements.txt` are required.

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Download or clone the repository.
2. Install the required Python dependencies.
3. Ensure that `terrain_clip.tif` and all supporting Python modules are in the expected locations.
4. Open `course_project.ipynb` in Jupyter Notebook or JupyterLab.
5. Run the notebook cells from beginning to end.

## Project Files

| File | Description |
|---|---|
| `course_project.ipynb` | Main project notebook |
| `terrain_clip.tif` | Clipped Copernicus DEM elevation raster |
| `draw_rectangles.py` | Visualization helper functions |
| `draw_3d.py` | 3D visualization helper functions |
| `plot_functions.py` | Plotting helper functions |
| `solve_integrals.py` | Integration helper functions |
| `requirements.txt` | Python dependencies |

## Data Source

The real elevation data comes from the Copernicus DEM GLO-30 dataset.

European Space Agency (ESA). (n.d.). *Copernicus DEM: Global and European Digital Elevation Model*. https://doi.org/10.5270/ESA-c5d3d65

See the main notebook for the full dataset attribution and additional references.

## Author

Created as a course project exploring the mathematical foundations and practical applications of integration.