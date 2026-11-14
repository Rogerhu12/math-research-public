# R43 supplement: a sharp complete two-row shifted-Airy frame change

For the unchanged actual old family, every parameter in the original
interval, every Fourier mode including zero, and every
\(0\le\xi\le L=1/4000\), the exact change between the original R39 Airy
frame and the constant-\(5050\) shifted frame satisfies

\[
 \boxed{\|F_0(\xi)^{-1}F_{5050}(\xi)\|,\ 
        \|F_{5050}(\xi)^{-1}F_0(\xi)\|<4.203925521.}
 \tag{J.1}
\]

The matrices contain both height and momentum rows. The same bound holds
on every scaled or unscaled Sobolev amplitude space because this change is
Fourier diagonal. It includes the independent mean matrix; the nonzero
bound alone is smaller, \(3.570544818\).

This replaces the coarse \(1100.925158\) bound in the full-root operator
supplement, without changing its equation, height, density, first phase,
or sources. In that supplement's homogeneous estimate the two frame
factors improve by more than \(68581\); in its ordinary-source estimate
the one output factor improves by more than \(261.88\). These are
improvements of the specified factors. They do not by themselves certify
a new full returned remainder or a finite-head inverse.

## 1. The exact real matrix behind both nonzero Cauchy rows

Write \(v=5050\), \(\lambda=q|n|\), and

\[
 x=\lambda^{2/3}\xi,\qquad s=v\lambda^{-4/3},\qquad
 A(x)=
 \begin{pmatrix}
  \operatorname{Bi}(-x)&\operatorname{Ai}(-x)\\
  \operatorname{Bi}'(-x)&\operatorname{Ai}'(-x)
 \end{pmatrix}.
 \tag{J.2}
\]

The complete actual frequency is still

\[
 38.883851605869<q<38.883851623093.
\]

The primes in (J.2) are derivatives of the Airy argument. Let

\[
 C=\begin{pmatrix}1&1\\i&-i\end{pmatrix},\qquad
 U=C/\sqrt2.
\]

Then \(U\) is unitary. For the unchanged normalization
\(c^2=\operatorname{Ai}(0)/[-\operatorname{Ai}'(0)]\), the two frames are
exactly

\[
 F_0=c\,\operatorname{diag}(\lambda^{-1/3},-\lambda^{1/3})
                A(x)C,\qquad
 F_v=c\,\operatorname{diag}(\lambda^{-1/3},-\lambda^{1/3})
                A(x+s)C.
 \tag{J.3}
\]

Consequently their change is unitarily similar to
\(A(x)^{-1}A(x+s)\). All frequency powers and the common height constant
cancel in this identity, rather than being estimated independently.
The Wronskian gives \(\det A(x)=-1/\pi\), so the real change matrix has
determinant one. For a real \(2\times2\) determinant-one matrix its two
singular values are reciprocal; hence

\[
 \|A(x)^{-1}A(x+s)\|
 =\|A(x+s)^{-1}A(x)\|.
 \tag{J.4}
\]

This pays the inverse direction exactly. It does not invoke only a
one-sided bound on a general infinite-dimensional operator.

The physical relation between \(x,s\) is essential:

\[
 x^2s=v\xi^2\le h:=vL^2=.000315625,\qquad
 0<s\le vq_-^{-4/3}<38.335312576.
 \tag{J.5}
\]

## 2. A complete compact real Airy cover

For \(0\le x\le1\), (J.5) places \(x+s\) in \([0,40]\).
The native consumer evaluates every closed interval of length \(1/128\)
in \([0,40]\) with Arb Airy functions. It does not sample just their
centers. For each real matrix it encloses its exact largest singular value
using

\[
 \|A\|^2
 =\frac{f^2+\sqrt{f^4-4(\det A)^2}}2,\qquad
 f^2=\sum_{i,j}|A_{ij}|^2,
 \tag{J.6}
\]

with an upper enclosure of \(f^2\) and the exact determinant \(1/\pi\)
in absolute value. The complete closed cover gives

\[
 \sup_{0\le x\le1}\|A(x)\|<.781456455,\qquad
 \sup_{0\le y\le40}\|A(y)\|<1.454386496.
\]

Since \(\|A(x)^{-1}\|=\pi\|A(x)\|\), it follows that

\[
 \|A(x)^{-1}A(x+s)\|<3.570544818
       \qquad(0\le x\le1).
 \tag{J.7}
\]

Every mode whose \(x\) is in this range is covered, without retaining a
finite list of frequencies.

## 3. The whole unbounded range by an exact Sonin identity

For a solution of \(u_{xx}+xu=0\), set

\[
 Z=(x^{1/4}u,x^{-1/4}u_x)^t,\qquad
 e(x)=\frac1{4x^{3/2}},\qquad S(x)=I+e(x)\sigma_1 .
\]

On \(x\ge1\), \(Z_x=MZ\), where

\[
 M=\begin{pmatrix}1/(4x)&\sqrt{x}\\-\sqrt{x}&-1/(4x)\end{pmatrix},
 \qquad M^*S+SM=0.
 \tag{J.8}
\]

Thus \((Z^*SZ)'=Z^*S'Z\), and

\[
 \frac{d}{dx}\log(Z^*SZ)\le\frac{|e'(x)|}{1-e(x)}.
\]

The exact integral from \(1\) to \(x\) is
\(\log[(1-e(x))/(1-e(1))]\). Dividing by the final lower eigenvalue
\(1-e(x)\) cancels that factor, yielding

\[
 \|Z(x)\|^2\le\frac{1+e(1)}{1-e(1)}\|Z(1)\|^2
             =\frac53\|Z(1)\|^2.
 \tag{J.9}
\]

This holds for every complex linear combination of the two Airy
solutions. Changing the sign of the derivative row is an isometry, so
(J.9) implies

\[
 \|\operatorname{diag}(x^{1/4},x^{-1/4})A(x)\|
 \le C_1:=\sqrt{5/3}\,\|A(1)\|<.802608000.
\]

In particular \(\|A(x)\|\le C_1x^{1/4}\) and
\(\|A(x)^{-1}\|\le\pi C_1x^{1/4}\). The argument-derivative convention
in (J.2) gives \(A'(t)=B(t)A(t)\) with
\(B(t)=\left(\begin{smallmatrix}0&-1\\t&0\end{smallmatrix}\right)\);
for \(t\ge1\), \(\|B(t)\|=t\). Therefore

\[
\begin{aligned}
 \|A(x)^{-1}A(x+s)-I\|
 &\le \pi C_1^2 x^{1/4}(x+s)^{5/4}s\\
 &\le \pi C_1^2 h(1+h)^{5/4}
 <.000638998078 .
\end{aligned}
 \tag{J.10}
\]

The second inequality uses \(s\le h/x^2\) and \(x\ge1\). This proves
the entire remaining half-line, with no frequency cutoff and no
frequency derivative loss. Equations (J.7) and (J.10), followed by
(J.4), give the claimed complete nonzero bound.

## 4. The independent mean cannot be replaced by a nonzero limit

The unchanged original mean columns are
\(c(1\pm i\xi/\pi)\), and the shifted mean columns are

\[
 c\left(\cos(k\xi)\pm i\frac{\sin(k\xi)}{\pi k}\right),
 \qquad k=\sqrt{5050}.
\]

After the same constant unitary column change, their exact comparison is

\[
 M_0(t)=
 \begin{pmatrix}
 \cos(kt)+tk\sin(kt)&[\sin(kt)/k-t\cos(kt)]/\pi\\
 -\pi k\sin(kt)&\cos(kt)
 \end{pmatrix},\qquad 0\le t\le L.
 \tag{J.11}
\]

Its determinant is one. The complete 512-cell closed interval cover,
using (J.6) with determinant one, proves

\[
 \sup_{0\le t\le L}\|M_0(t)\|
 =\sup_{0\le t\le L}\|M_0(t)^{-1}\|
 <4.203925521.
 \tag{J.12}
\]

The mean is the largest of the three estimates here. Removing it would
give a false bound for the full specified frame.

## 5. Exact scope of consumption

Let \(C_v(t,s)\) and \(Z_v f\) be any already proved complete propagation
and source in the exact shifted frame. If \(M=F_0^{-1}F_v\), then

\[
 C_0(t,s)=M(t)C_v(t,s)M(s)^{-1},\qquad
 Z_0f=M(t)Z_vf.
 \tag{J.13}
\]

Thus a homogeneous bound uses two factors from (J.1), and a source bound
uses one. These identities retain both Cauchy rows, all modes and every
intermediate path through the finite head. No projection is moved through
a multiplication or evolution. They hold on every full \(E_N^s\) and
unscaled \(E^s\), because \(M(t)\) is Fourier diagonal and its modewise
norm is uniformly bounded. The independent physical regular ports,
grounded conormal height shear, and ordinary-source Piola law of the
earlier consumers remain unchanged.

The original R43 first phase \(B_{\rm original}\) is still computed from
the actual \(V\). The present comparison does not replace it with the
constant reference phase. It does not claim that the full returned
remainder has already been recomputed, that a finite head is inverted,
or that the nearby-surface theorem follows.

## 6. Actual calculation

The new producer is
scripts/fourfold_actual_root_sharp_Airy_frames.py.
Its complete report is
notes/2026-11-13-actual-root-sharp-Airy-frames.json.
The report binds the existing complete actual domain, producer,
dependencies and whole family identity, and stores all 40 unit-range
cover bounds and the exact full-axis inequalities.

Reproduce from the topic directory with a fresh output:

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_root_sharp_Airy_frames.py \
  --out /tmp/actual-root-sharp-Airy-frames.json
~~~

The actual directed run took about 1.17 seconds. No large geometric or
seven-field native cache was rerun for this conclusion.

