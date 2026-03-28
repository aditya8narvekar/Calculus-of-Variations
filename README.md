# Calculus of Variations Project
This repository contains a numerical solver for the Brachistochrone problem.
Instead of solving the Euler-Lagrange differential equation, the code in this repository minimizes the time integral directly using `scipy.optimize`.
The same code is then used to find numerical solutions for the hanging chain (catenary) problem and the shortest distance problem.

**Contents:**
- `brachistochrone_basic.py`: Solves for the quickest path for a bead sliding down under gravity.
- `brachistochrone_full_arch.py`: Solves the full cycloid arch using symmetry.
- `catenary_derived.py`: Solves for the path taken by a chain hanging between two fixed points.
- `shortest_distance_derived.py`: Solves for the shortest path between two fixed points.
- `Theory/`: A folder containing my handwritten notes and derivations on the subject, used to verify the code analytically.

**References:**
- Calculus of Variations, I. M. Gelfand and S. V. Fomin.
- Differential Equations with Applications and Historical Notes, George F. Simmons.
