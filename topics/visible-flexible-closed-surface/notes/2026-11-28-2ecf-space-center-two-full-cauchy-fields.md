# Two full-angular Cauchy fields from the actual R320 nonplanar strip (V56)

Freeze the original V40 target, both true material halves with R320's proper half-turn, the same physical R314 exterior, and the R320 h=.09 input. At the exact outgoing flat-strip boundary integrate the nonlinear Gauss–Codazzi, material frame and Cartesian positions using genuine initial n,m,T,B,N. Both spatial discretizations use all cosine and sine frequencies independently in all three coordinates.

The 256-angle/600-step run and the 512-angle/1200-step run use 40 native quintic spans up to t=.20 and all harmonics through 80 and 152 respectively in each coordinate. The physical field adds the full Fourier/quintic residual to the continuous R320-strip reference described in the code. From .20 to .70 the same actual last two-jet is lifted to the previous V48 exterior by the prescribed quintic. The exact strip is continued by its own formula below the port, and all true R314 layers and caps survive beyond the continuation.

| Input and row set | Prefix metric | Prefix curvature | Full metric | Full curvature | Full held | Full half-width |
|---|---:|---:|---:|---:|---:|---:|
| 256 G10a | 0.01342187 | 11.72582 | 0.93980710 | 113.01948 | 0.51126105 | 0.98715939 |
| 256 G10b | 0.01029590 | 11.72582 | 0.93980710 | 113.01948 | 0.51126105 | 0.98715939 |
| 256 G11 | 0.02002852 | 11.08590 | 0.93977173 | 112.73545 | 0.51138903 | 0.98709263 |
| 512 G10a | 0.003689171 | 12.80032 | 0.93979316 | 112.99650 | 0.51103167 | 0.98714700 |
| 512 G10b | 0.005411517 | 12.80032 | 0.93979316 | 112.99650 | 0.51103167 | 0.98714700 |
| 512 G11 | 0.006533476 | 14.17095 | 0.93975961 | 112.71331 | 0.51125204 | 0.98708156 |

All 958×(128+192)×14 prescribed and 668×256×14 independent rows were retained. The real full connector remains far from the physical and metric goals. The finite Cauchy trace itself has high curvature, and its two discretizations do not give continuous control. R320's exact central flat-strip geometry remains local to that input.

Use the R320 source `make256 STATE192 STATE540 TWIST256` and `make512 STATE192 STATE540 TWIST512`, then `observe STATE192 STATE540 TWIST256` and likewise for TWIST512. SHA256 of the generated JSON with final LF 237b5361be2b95338e96d8c4f13d4181c3f70f257a3a919b7cd8d7e74358bb5d and cec59f04aaf2553d67d7d93f47b3a9d410267360a14572ebef2cb2adcb2c5cce.
