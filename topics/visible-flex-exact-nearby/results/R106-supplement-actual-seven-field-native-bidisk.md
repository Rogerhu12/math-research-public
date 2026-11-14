# R106 supplement: the actual seven-field bidisk has been computed

2026-11-13, phase_inverse. **Status: proved, with completed native interval
computation.** This is a coefficient-domain result, not the full returned phase
or the completed PDE inverse.

## Statement

Keep the exact affine step5 object, real parameter

$$
p_5=-7789843107295549/4611686018427387904,\qquad
|p-p_5|\le 10^{-9},
$$

and its actual radial root $t(p)$. On the complete complex domain

$$
|\rho|\le 1/2500,\qquad |\operatorname{Im}\theta|\le1/64,
\qquad \rho=t(p)-r,
$$

the seven original-height functions defined in R106RF.1–3 are holomorphic,
with the following rigorous, outward-rounded uniform upper bounds:

| Field | Uniform upper bound |
|---|---:|
| $G=\rho^{5/2}D_{\rm red}$ | $39/1000$ |
| $q$ | $371$ |
| $k_*$ | $10009$ |
| $S_{\rm reg}$ | $714/100$ |
| $L_\theta$ | $154/100$ |
| $U_0$ | $267/1000$ |
| $U_1$ | $543/10$ |

The means are included. The scalar radial factor $Q$ uses the positive-real
square-root branch fixed by the actual interval calculation.

## Proof and complete computation

Use the proof of the integrated-ray/boundary-bidisk supplement §§2–3, now with
its previously unexecuted common domain actually certified. The producer
`scripts/fourfold_subprincipal_root_bidisk_boundary_v2.py` retains the exact
finite Fourier and Taylor coefficients, all infinite primitive tails and radial
Taylor remainders, and evaluates the upper complex angular boundary on 2048
closed cells. Its normalized Fourier mode $k$ is multiplied by $e^{-4kS}$;
physical angular derivatives include the rotating-frame connection.

The finite angular-cell enclosure is

$$
\sum_k \sup_{|\rho|\le R}|c_k(\rho)|\,e^{4|k|S}|k|\pi/N.
$$

It bounds the entire closed real cell, while the independent infinite-tail
bound uses imaginary width $4S$. Differentiated zero-padded finite modes now
carry the same declared Taylor precision as the nonzero differentiated modes;
these entries are exact zero polynomials, so this representation repair changes
no finite coefficient or analytic remainder.

The actual report shows, uniformly on the boundary and radial disk,

$$
\operatorname{Re}(C\cdot C)>181/100,\quad
\operatorname{Re}(F\cdot F)>118/100,\quad
\operatorname{Re}(C\cdot F)>121/100,
$$

$$
\operatorname{Re}F_z>268/1000,\qquad
\operatorname{Re}a_0>38/1000.
$$

These bounds follow by rounding the saved complete cell minima downward.
Schwarz conjugation gives the lower angular boundary with the same full radial
disk. The periodic-strip harmonic minimum principle first proves the positive
real denominator bounds throughout the interior, in the order specified by
the original boundary proof; reciprocals and the seven field formulas are
therefore holomorphic on that interior. The maximum modulus principle then
transfers the computed boundary moduli to the whole domain. The independent
radial deflation computation uses

$$
Q=\int_0^1K_{0,r}(t-z\rho)\,dz,\qquad
Q_\rho=-\int_0^1 z K_{0,rr}(t-z\rho)\,dz,
$$

so it does not divide an interval containing the actual root by $\rho$.
The coefficient $G$ is bounded through its exact $A+\rho B+\rho^2C_2$
formula and includes all original-height terms. No mean is substituted for a
nonconstant field.

The complete 2048-cell interval report is
`notes/2026-11-13-R106-seven-field-boundary-v2-native-2048.json.gz`;
its source, full input identities, exact domain, all individual fees and
all denominator gates are stored inside it. The execution command and SHA
are in `notes/2026-11-13-R106-seven-field-native-recovery.md`.
Every final printed rational bound is weaker than the corresponding saved
outward endpoint. This proves the statement. $\square$

## Use and remaining scope

The common angular width $1/64$ is now an actual domain and can replace the
previous provisional input for the seven-field Fourier-Taylor contract. The
complete aliases, omitted radial and angular modes, finite coefficients,
true-ray pullbacks, both root endpoints, bulk phase, final frame and strong
$4/3$ remainder still require their own payments. No R104 cutoff or closed
isometric family is inferred from this coefficient-domain theorem.
