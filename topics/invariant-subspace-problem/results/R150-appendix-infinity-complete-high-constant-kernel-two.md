# Original infinity: the complete high constant kernel has dimension two

Date: 2026-11-15 UTC. Author: Astra-ISP-789f / root, normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Status: complete original characteristic-zero constant-block result from an actual fixed-prime lower bound and two exact rational kernel columns. This note does not assign the sixth connection a rank.

## 1. Original operator and complete high block

Use the same natural chart $u=1/s$, reversal of the physical $K$, ordinary co-moving moment coordinates, and original seventeen equations as in [the completed original projection calculation](R150-appendix-infinity-original-projection-exact-length61-and-full-length-gap-five.md). These are the established unit transports relative to the already defined naturally weighted original matrix; no additional power of $u$ is divided out.

Write $A(u)$ for the original $4367\times6188$ coefficient matrix. Its transpose acts on target functionals. Let $S_r$ denote all original source coordinates whose multiplier has normal degree $r$, and $V_r$ all target coordinates of normal degree $r$. In the fixed actual dictionaries,

$$
(\dim S_0,\dim S_1,\dim S_2,\dim S_3)
=(170,918,2295,2805),
$$

$$
(\dim V_0,\ldots,\dim V_5)
=(20,135,450,990,1485,1287).
$$

The matrix in this calculation is exactly

$$
H=
\left.A_0^{\mathsf T}\right|_{
(S_2\oplus S_3)\times(V_3\oplus V_4\oplus V_5)}
\in\mathbb Q^{5100\times3762}.
\tag{1}
$$

All $5100$ source rows and all $3762$ target columns are retained. In particular, (1) includes both the $S_2,V_4$ and $S_3,V_4$ cross blocks. No previously computed rank of a single diagonal block is substituted for this complete matrix.

The actual six block nonzero counts, before rational row normalization, are

| Source rows | $V_3$ | $V_4$ | $V_5$ |
|---|---:|---:|---:|
| $S_2$ | 33480 | 66285 | 0 |
| $S_3$ | 0 | 40920 | 81015 |

Thus the original rational matrix contains $221700$ nonzero entries.

## 2. Two genuine rational kernel columns

The completed original fifth-stage high cache contains two homogeneous columns $Z_3\in\mathbb Q^{990\times2}$. They are the first two columns of the actual $999\times11$ high-lift kernel, with all nine final head coordinates equal to zero. In the original cubic target dictionary, their coordinates numbered $164$ and $494$ form $I_2$. Both columns are therefore independent over $\mathbb Q$.

Embed them as

$$
Z=\begin{pmatrix}Z_3\\0_{1485\times2}\\0_{1287\times2}\end{pmatrix}.
\tag{2}
$$

The new execution checks $HZ=0$ on every original row. It verifies all $5100\cdot2=10200$ rational product coordinates, rather than relying on only the old $2295$-row high identity. The source file and canonical matrix hashes are

- old high-lift file: `d8dff9e38bad4a0a41a21679e5654609f36b7da36dbb84f996a0778bfa73eb50`;
- actual $990\times2$ rational matrix: `c10632a05ab35246f09f7595d090c54d533d010c5fbded2c23f5958dbe523464`.

Consequently,

$$
\operatorname{rank}_{\mathbb Q}H\le3760.
\tag{3}
$$

## 3. One actual field lower bound

Each complete rational row of (1) is multiplied by its single exact denominator/content scale. The execution checks all $5100$ row-scaling identities. In this instance every scale is a $31$-adic unit: no row denominator or cleared common content is divisible by $31$. This statement concerns this constant matrix only.

The prescribed field is $\mathbb F_{31}$. The resulting full matrix has rank

$$
\operatorname{rank}_{\mathbb F_{31}}\overline H=3760.
\tag{4}
$$

All $1340$ dependent original rows reduce to zero. The original pivot minor is independently checked. The native implementation also verifies all $961$ field-addition identities, all $30$ nonzero inverses, and padding of the retained bit planes. Its actual row-addition count is $5787134$.

A nonzero $3760$-minor modulo $31$ is a nonzero rational minor of the original matrix, since the exact row scales are nonzero. Therefore (4) gives the reverse inequality to (3). We conclude

$$
\boxed{\operatorname{rank}_{\mathbb Q}H=3760,\qquad
\ker_{\mathbb Q}H=\operatorname{im}_{\mathbb Q}Z.}
\tag{5}
$$

In particular, every rational high constant correction satisfying all original high equations has its normal-degree-four and normal-degree-five coordinates equal to zero. Its cubic coordinates are a unique rational combination of the two columns in (2).

No field kernel is being lifted or identified with a rational kernel on the basis of its dimension alone. The rational kernel columns and all their products precede the field computation.

## 4. Integral constant-block scope

Let $D=\mathbb Z_{(31)}$. All original coefficients and row scales of this calculation are $D$-defined and the actual rank minor is a $D$-unit. Elimination of this minor over $D$ gives a rank-two $D$-integral kernel graph in the free coordinates of that minor. Its reduction is the full two-dimensional field kernel.

The rational span of this integral graph equals the span in (2). We do not infer that an arbitrary separately normalized rational basis, including one normalized at different free coordinates, is integral solely from its displayed $I_2$ minor. Integrality of that particular basis would require its entries or its coordinate transition to be checked. The sixth-stage calculation needs the exact rational kernel (5), which is already complete.

This conclusion does not assert flatness of any higher parameter jet, equality of the full characteristic-zero and field Smith spectra, or a unit leading coefficient of the chosen large polynomial minor. It is a complete result for the single original constant block (1).

## 5. Why this is the needed sixth-stage interface

The actual full and projected first five connection ranks are both

$$
(4,0,1,3,1).
$$

Their leading spaces agree, because the projected cochains are genuine full cochains and have the full dimensions at every one of these stages. An induction, subtracting a projected chain with the same head and then dividing their difference by $u$, shows that every full fifth-stage chain has each coefficient in the pure/one-normal target sectors.

Its sixth forcing therefore has zero coordinates on all $5100$ original rows $S_2\oplus S_3$. A last correction of normal degree at most two also has zero coordinates there, since the actual original $F_0$ has zero pure part. Thus the high component of the last correction must lie in (5), and this condition is also sufficient to satisfy all the high equations.

It remains to solve the low $1088$ rows with the two columns $Z_3$, all nine prior incoming directions, and the two actual exponent-six projection failures. The resulting $1088\times598$ rational system retains the complete original sixth-stage problem. This note does not report its rank or claim that either failure lifts.

## 6. Actual execution and reproducibility

The completed run is

- Actions run `43740928483`;
- step `infinity-complete-normal345-high-field31`;
- execution source `30fc39c2ba04bb9ecfcca58362ec3a8cebb8de02`;
- total mathematical time $3.976483646$ seconds, including the native field calculation of $1.976728848$ seconds;
- actual semantic binding `be780095c27b5cdc6729a5736c7b42d84dc4d0a11bec67ca2997f592dc7dea05`.

The small execution record is

`notes/r150-source-kernel-session-789f/43740928483-infinity-complete-normal345-high-field31.json`,

$12776$ bytes, SHA256

`0f6cbe9bb23601be632d0045f35839b922e16e4d893aca6b9d4e2f849cbd9141`.

The underlying complete raw receipt has $7567$ bytes and SHA256

`7ceb39a4c6cf66265c842c8ab5f3d0d6f53def762f9bad780028ed49eccf562b`.

Reproducible sources are

- `notes/2026-11-15-r150-infinity-complete-normal345-high-field31-789f.py`, SHA256 `1a578441929247d114b7f39e9824b243dbc0433de781dd2ffce4d4e11dea4122`;
- its `-native-789f.cpp` companion, SHA256 `cee59e862dc22bd5ade469177ce9e4541d2a6b4743ab811684a5e387a4402ba4`;
- the matching input manifest and interface.

The original rational row stream has SHA256 `348d9b675aedc1a5cc2baec2b80bb6b40261f51e7dbb07ccf29302f64ff40cc9`; the primitive integer row stream has SHA256 `f809182df6b304b41daf2045c9189e59717781349adc85a808f553ef11543887`. All large reconstructible matrices, pivot rows, and row-operation arrays remain temporary job data.
