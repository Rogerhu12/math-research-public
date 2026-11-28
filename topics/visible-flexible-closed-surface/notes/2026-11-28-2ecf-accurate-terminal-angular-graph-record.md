# Accurate Γ95 terminal ring as a single-valued graph in the ellipse-flow chart

**Numerical evidence.**

Directed 96-bit dyadic intervals over 1024 closed native-angle cells for the actual R232/R233 coast output. All Γ95 Fourier modes were retained. The entrance section argument is the actual R225 arc interval and the accurate scale ratio from R233. Each angle interval is enclosed by a trigonometric Taylor expansion with a rigorous second-derivative remainder; Frenet data, the signed R137 ratio k, the exact physical outlet and exit unit tangent are subsequently evaluated by outward interval arithmetic.
Actual strict lower bounds: transverse determinant >.68781573, height >.18030692, height above central port >.07874442, material exit angular derivative >.96570256. The directional inequality covers the entire terminal circle. With the whole-domain oriented local chart in R256 and the boundary degree argument in the accompanying result this proves that the accurate upper prefix, its central section and reflection together are embedded. The return receipt is natural zero in 20.90994 seconds, peak RSS 27988 KiB. No nonlocal normal radius is asserted.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-accurate-exit-angular-graph.py --scripts $S --ramp $W/gap105-prefix-ramp-master.npz --coast $W/gap105-prefix-coast-master.npz --cells 1024 --output $W/polar-accurate-exit-angular-graph-1024.json
```

## Scientific SHA-256

- `2ecf-polar-accurate-exit-angular-graph.py`  `b94affda5c6b6afe0c76224bf31662569846f26b0078669a2ec49b9da50ed8af`.
- `polar-accurate-exit-angular-graph-1024.json`  `3f7c39bf060996d3d9c101880050d9cab5cc0ad843790cd262fd1ea95112366a`.
