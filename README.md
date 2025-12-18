# Calculus of Variations Project
This repository contains a numerical solver for the Brachistochrone problem. Instead of solving the Euler-Lagrange differential equation, the code in this repository minimizes the time integral directly using `scipy.optimize`.

**Contents:**
- `brachistochrone_basic.py`: Solves for the path between two fixed points.
- `brachistochrone_full_arch.py`: Solves the full cycloid arch using symmetry.
- `Theory/`: A folder containing my handwritten notes and derivations on the subject, used to verify the code analytically.

**References:**
- Differential Equations with Applications and Historical Notes, George F. Simmons.
