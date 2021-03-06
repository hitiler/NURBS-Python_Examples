#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl import tessellate
from geomdl.visualization import VisVTK as vis
from geomdl.shapes import analytic


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("../ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set surface tessellation component
surf.tessellator = tessellate.TrimTessellate()

# Set visualization component
visconf = vis.VisConfig(ctrlpts=False, legend=False, trims=False)
surf.vis = vis.VisSurface(config=visconf)

# Generate circular trim curves with different sense
tcrv1 = analytic.Circle(origin=(0.5, 0.0), radius=0.2)
tcrv1.opt = ['sense', 0]
tcrv2 = analytic.Circle(origin=(0.0, 0.5), radius=0.2)
tcrv2.opt = ['sense', 0]
tcrv3 = analytic.Circle(origin=(1.0, 0.5), radius=0.2)
tcrv3.opt = ['sense', 0]
trim_curves = [tcrv1, tcrv2, tcrv3]
# trim_curves = [tcrv3]

# Set trim curves (as a list)
surf.trims = trim_curves

# Set sample size
surf.sample_size = 50

# Visualize surface
surf.render()

# # Save as Wavefront OBJ file
# exchange.export_obj(surf, "trim_multi_sense3.obj")

# Good to have something here to put a breakpoint
pass
