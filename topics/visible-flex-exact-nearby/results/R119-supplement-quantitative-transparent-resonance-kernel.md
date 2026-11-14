# R119 supplement: a quantitative separation of the actual transparent-resonance kernel

2026-11-14, visible-exact / root. **Proved; 43 new exact rational gates passed.**

The phase-preserving control theorem proved that the actual resonant
Wronskian kernel is not in the span of the two phase kernels. This
supplement gives a frequency-uniform quantitative lower bound for that
distance, in the same actual radial problem and with its true normalized
wave state. The complex growth has order \(|m|\), with the small
factor \(\delta_j^{3/4}\), rather than order \(m^2\).

This is a bound for the complete radial kernel. A norm-controlled
compact control, its actual compensated Wronskian derivative, the
coupled nonradial middle network and the full nonlinear tail equation
remain further contracts. In particular a layer-dependent constant
below cannot be charged to the original low-frequency source weight
without a separately proved frequency-window conversion.

## 1. Actual inputs, normalization and conclusion

Use precisely the actual local problem and fixed real Robin lines of
[the phase-preserving finite Schur theorem](R119-supplement-phase-preserving-actual-finite-Schur-controls.md),
Git blob \(\mathtt{5214cfffb5d16f3aebb0105af8aab14b2b5188b1}\).
For \(j\ge8193\), put
\[
 \delta=\frac2{25}2^{-j},\quad
 a=\frac{\eta_j}{\sqrt{12}}=\frac{\delta^{3/2}}{8\sqrt6},
 \quad j/2<\Delta<3(j+4),\quad B=\Delta/a.
 \tag{Q.1}
\]
On the genuinely unused subinterval of the descending ramp,
\[
 J=[7/16,15/32],\quad c=29/64,\quad l=1/64,\quad
 Q(x)=7+30B x^2(1-x)^2,\quad t=t_d+ax .
 \tag{Q.2}
\]
The existing two bumps are outside this interval. Thus (Q.2) is the
actual polynomial there, not an approximate radial coefficient.

Fix a nonzero physical fourfold mode \(m\), let \(\lambda=m^2\ge16\),
and take the true nonzero real resonant solution
\[
 h_{tt}-(1+Q)h_t+\lambda Qh=0,\qquad
 \mu_t/\mu=-1-Q .
 \tag{Q.3}
\]
Normalize its left wave state to Euclidean norm one, with
\[
 u=\sqrt\mu\,h,\quad k=\sqrt{7m^2-16},\quad
 Y=(\sqrt k\,u,u_t/\sqrt k).
\]
The complete real Cauchy bound supplied by the input theorem is
\[
 \|U(t,s)\|\le K_j:=2^{6000}(j+5)^8\delta^{-16}
 \tag{Q.4}
\]
in these fixed wave units, for both directions throughout the actual
window. Consequently \(K_j^{-1}\le|Y(c)|\le K_j\).
No value of a numerical shooting determinant is supplied as an input.

Define the complete true kernel
\[
 {\cal K}(x)=\mu(h_t^2-2\lambda hh_t+\lambda h^2).
 \tag{Q.5}
\]
Let \(\phi_S,\phi_\beta\) be the original two phase kernels, with the
original \(dt\) measure and derivatives. Set
\[
 \chi=1+|m|\sqrt{a(1+\Delta)},\qquad T=1+\Delta+\chi .
\]
Then
\[
\boxed{\ 
 \operatorname{dist}_{L^\infty(J)}
  ({\cal K},\operatorname{span}_{\mathbb R}\{\phi_S,\phi_\beta\})
 \ \ge\
 2^{-32768}a^{382}B^{-1472}\lambda^{-383}K_j^{-510}
                     \exp(-2^{67}T) .\ }
 \tag{Q.6}
\]
Every quantity on the right is explicit and strictly positive.
No frequency cutoff occurs in the proof.

A convenient coarser consequence, writing \(J_0=j+5\), is
\[
\boxed{\ 
 \operatorname{dist}_{L^\infty(J)}
  ({\cal K},\operatorname{span}\{\phi_S,\phi_\beta\})
 \ \ge\
 2^{-2^{22}}\delta^{10941}J_0^{-5552}|m|^{-766}
 \exp\{-2^{69}J_0-2^{66}|m|\delta^{3/4}\sqrt{J_0}\} .
 \ }
 \tag{Q.7}
\]
The large factor depending only on the layer is explicitly present.
It has not been absorbed into \(\delta^{131}\), another existing
radial weight, or an unproved whole-frequency inverse.

## 2. Both actual phase kernels have a fixed polynomial numerator

Write \(Q_x=dQ/dx\). The exact kernels in P.20–P.21 give
\[
 \phi_S=-\frac{Q_x}{4aQ^{3/2}},
\]
\[
\begin{split}
 256Q^{9/2}\phi_\beta={}&
 a^{-1}(12Q^4-8Q^3+12Q^2)Q_x\\
 &+a^{-3}(40QQ_xQ_{xx}-35Q_x^3-8Q^2Q_{xxx}).
\end{split}                                                     \tag{Q.8}
\]
The \(S\) numerator in the same units is \(-64a^{-1}Q^3Q_x\).
Thus every real linear combination of the two actual kernels has
the form
\[
                         P(x)/Q(x)^{9/2},\qquad \deg P\le19.
 \tag{Q.9}
\]
The scalar factor 256 is absorbed into \(P\).
The proof below allows every complex polynomial of degree at most
19; this is a larger comparison space than the two real phase kernels.

The positive square root in (Q.9) is used only on \(J\).
No square root is continued around a complex branch point.

## 3. A fixed-disk interpolation inequality

If an entire function \(F\) has
\[
 \sup_{|z-c|\le1024}|F(z)|\le M_F,\qquad
 \sup_{x\in J}|F(x)|\le\epsilon_F ,
\]
then
\[
                  \sup_{|z-c|\le2}|F(z)|
                       \le3\sqrt{M_F\epsilon_F}.        \tag{Q.10}
\]
For \(\epsilon_F=0\), this follows from the identity theorem.
Otherwise choose the \(N+1\) Chebyshev roots in \(J\).
The sum of the absolute Lagrange basis functions on the radius-2
disk is at most \(A^N\), where
\[
 A=2(2+l)/l=258 .
\]
Indeed the numerator of each degree-\(N\) basis function is at
most \((2+l)^N\), and its denominator is at least
\((N+1)l^N/2^N\).
The contour interpolation remainder on the radius-1024 circle
is at most
\[
 2M_F q^{N+1},\qquad q=(2+l)/(1024-l)=129/65535<1/A .
\]
Take \(N=\lfloor\log(M_F/\epsilon_F)/(2\log A)\rfloor\).
The interpolation polynomial is bounded by \(\sqrt{M_F\epsilon_F}\)
and the remainder by \(2\sqrt{M_F\epsilon_F}\), proving (Q.10).

All radii here are fixed. In particular the propagation exponent
does not deteriorate when two complex roots of \(Q\) approach one
another as \(B\) increases.

## 4. The actual quartic roots and a finite Hermite bound

The four roots solve
\[
 x(1-x)=\pm i\tau,\qquad \tau=\sqrt{7/(30B)}.
\]
For \(B\ge1\), the square roots \(\sqrt{1\pm4i\tau}\) have modulus
less than \(3/2\). Hence every root \(r_i\) satisfies
\[
 |r_i-c|<3/4+3/64<1 .
\]
Their mutual distances obey
\[
                         |r_i-r_j|\ge d:=1/(4\sqrt B).
 \tag{Q.11}
\]
For conjugate roots close to 0 or 1, write
\(\sqrt{1+4i\tau}=\alpha+i\beta\).
Then \(\alpha<3/2\), \(\alpha\beta=2\tau\), and their distance
is \(|\beta|>4\tau/3>d\).
The other pairwise distances are at least \(\alpha\ge1\).
Thus the roots are all simple, with the displayed quantitative
separation.

Let \(P\) have degree at most 19. If its first five normalized
Taylor coefficients at every \(r_i\) have magnitude at most \(D\),
then
\[
                        \|P\|_{L^\infty(J)}
                              \le2^{80}B^{10}D .        \tag{Q.12}
\]
Here is an explicit interpolation bound.
Put
\(L_i(z)=\prod_{j\ne i}((z-r_j)/(r_i-r_j))^5\).
The coefficients through order four of \(1/L_i(r_i+w)\)
are bounded by \(\binom{14+k}{k}d^{-k}\le3060d^{-k}\).
The corresponding truncated coefficients of \(P/L_i\)
are at most \(15300Dd^{-4}\).
On \(J\), \(|z-r_i|<2\), so the complete Hermite formula gives
\[
 \|P\|_J
 \le4(2/d)^{15}\,5(16)(15300)Dd^{-4}
 <2^{40}d^{-19}D<2^{80}B^{10}D .
\]
There are exactly four roots times five jets, the full dimension
20 of the permitted polynomial space.

## 5. Entire-kernel separation with an explicit exponent

Suppose \({\cal K}\) is entire and
\[
 \|{\cal K}\|_{|z-c|\le1024}\le M,\qquad
 \|{\cal K}\|_J\ge\kappa>0 .
\]
For every polynomial \(P\) of degree at most 19,
\[
 \left\|{\cal K}-P/Q^{9/2}\right\|_J
       \ge2^{-28352}B^{-960}\kappa^{64}M^{-63}.
 \tag{Q.13}
\]

To prove this, let the left norm be \(\epsilon\).
If \(\epsilon\ge M\), the result already follows from
\(\kappa\le M\); if \(\epsilon=0\), the same argument below or
the identity theorem yields a contradiction.
Thus assume \(0<\epsilon<M\).
On \(J\), \(B<Q<9B\), and therefore
\(\|P\|_J<2^{16}B^5M\).
Degree-19 Chebyshev interpolation to the fixed radius-1024
disk gives
\[
                 \|P\|_{|z-c|\le1024}\le M_P:=2^{358}B^5M .
\]
Indeed \(2(1024+l)/l=131074<2^{18}\).

Use the genuinely entire function
\[
                         F=Q^9{\cal K}^2-P^2 .         \tag{Q.14}
\]
On the large disk \(|Q|<2^{46}B\), whence
\[
 \|F\|_{1024}<2^{717}B^{10}M^2 .
\]
On \(J\), factor the difference of squares to obtain
\[
 \|F\|_J<2^{31}B^9M\epsilon .
\]
Equation (Q.10) consequently gives
\[
 \|F\|_2
 <D_F:=2^{376}B^{10}M^{3/2}\epsilon^{1/2}.              \tag{Q.15}
\]

At each simple root \(r_i\), the first nine coefficients of
\(Q^9{\cal K}^2\) vanish. The coefficients of \(P^2\) through
order eight therefore have absolute value at most \(D_F\):
use the radius-one Cauchy circle centered at \(r_i\), which
lies strictly inside the radius-two disk.

Let \(c_n\) be the coefficients of \(P\) at one root.
All satisfy \(|c_n|\le M_P\).
Set \(e=D_F/M_P^2=2^{-340}(\epsilon/M)^{1/2}<1\).
For \(j=0,\ldots,4\), the coefficient of degree \(2j\) in \(P^2\)
gives
\[
 |c_j/M_P|^2
 \le e+2j\max_{i<j}|c_i/M_P|.
\]
Successive constants \(1,2,3,5,7\) prove
\[
 |c_j|\le C_jM_P e^{\,1/2^{j+1}},
 \qquad
 \max_{0\le j\le4}|c_j|
       <2^{361}B^5M^{63/64}\epsilon^{1/64}.             \tag{Q.16}
\]
This is an inequality for the complete coefficients, not a
division by a potentially small value of \(P\).

Insert (Q.16) into the complete Hermite estimate (Q.12).
Since \(Q>1\) on \(J\),
\[
 \kappa
 \le\epsilon+\|P/Q^{9/2}\|_J
 <2^{443}B^{15}M^{63/64}\epsilon^{1/64}.
\]
Raising to the 64th power proves (Q.13).
Only a fixed exponent 64 was lost. No \(B\)-dependent number of
analytic-continuation steps or untracked branch choice occurs.

## 6. The actual resonant kernel has a quantitative real size

Let \(V=\mu h^2\), \(H=\mu hh_t\), and \(Z=\mu h_t^2\).
The exact symmetric-square identity from the input theorem is
\[
 {\cal K}_{tt}=A{\cal K}
           +2\lambda(\lambda-1)Q_t V,\quad
 A=Q^2+(2-4\lambda)Q+1+Q_t .
\]
Its first derivative also gives exactly
\[
 Z=\frac{(Q-1){\cal K}-{\cal K}_t}{2(\lambda-1)}
                                      +\lambda QV .
\]
Thus the positive energy \({\cal E}=Z+\lambda QV\) equals
\[
 {\cal E}=
 \frac{(Q-1){\cal K}-{\cal K}_t}{2(\lambda-1)}
 +\frac{Q}{(\lambda-1)Q_t}
                         ({\cal K}_{tt}-A{\cal K}).    \tag{Q.17}
\]
All quantities are evaluated on the actual real interval.
Since \(Q_x>7B/8\), its denominators are separated.

At \(c\), the elementary change from the wave state gives
\[
 |Y(c)|^2\le128B^2\lambda{\cal E}(c).
\]
For example
\(u_t^2\le2\mu h_t^2+(1+Q)^2u^2/2\),
\(2\sqrt\lambda<k<3\sqrt\lambda\), and \(1+Q<10B\)
give this conservative constant directly.
Using (Q.4),
\[
                  {\cal E}(c)\ge(128B^2\lambda K_j^2)^{-1}.
\]

Convert (Q.17) to \(x\) derivatives.
With \(0<a<1\), \(B\ge1\), \(\lambda\ge16\), \(Q<9B\),
\(7B/8<Q_x<60B\), its total coefficient norm is bounded by
\[
                         2^{14}B^2\lambda/a .
\]
For explicit accounting, a sufficient sum before this rounding is
\[
 1329B/\lambda+23/(a\lambda)
       +1782aB^2/\lambda+990aB+22a/\lambda ;
\]
after division by \(B^2\lambda/a\), it is at most
\(1329+23+1782+990+22<2^{14}\).
Consequently
\[
 \max(|{\cal K}(c)|,|{\cal K}_x(c)|,|{\cal K}_{xx}(c)|)
       \ge 2^{-21}aB^{-4}\lambda^{-2}K_j^{-2}.          \tag{Q.18}
\]

Apply (Q.10) to \({\cal K}\), then take the radius-one Cauchy
estimates at \(c\). The maximum in (Q.18) is at most
\(6\sqrt{M\|{\cal K}\|_J}\).
It follows that one may use the explicit lower size
\[
              \kappa=
        2^{-48}a^2B^{-8}\lambda^{-4}K_j^{-4}M^{-1}
             \le\|{\cal K}\|_J                         \tag{Q.19}
\]
in the abstract separation theorem. This argument does not assume
that \(h\) has no zero, or that \({\cal K}(c)\) itself is nonzero.

## 7. Full complex growth has the correct frequency scale

The polynomial extension in this proof is the unique entire
continuation of the *local* actual solution from its real Cauchy
values at \(c\). It does not assert that the rest of the globally
piecewise profile is this polynomial.

Normalize \(\widetilde\mu(c)=1\) by
\(\widetilde\mu=\mu/\mu(c)\), \(\widetilde h=\sqrt{\mu(c)}h\).
This preserves \({\cal K}\). In the \(x\) coordinate,
\[
 \widetilde h_{xx}-(8a+\Delta S'(x))\widetilde h_x
            +\lambda a(7a+\Delta S'(x))\widetilde h=0,
 \quad S'(x)=30x^2(1-x)^2 .
 \tag{Q.20}
\]
For \(X=(\chi\widetilde h,\widetilde h_x)\), its exact generator is
\[
 \begin{pmatrix}
 0&\chi\\
 -\lambda a(7a+\Delta S')/\chi&8a+\Delta S'
 \end{pmatrix}.
\]
On \(|x-c|\le1024\), \(|S'|<2^{45}\).
Because \(\chi^2\ge\lambda a(1+\Delta)\), the generator norm is
at most \(2^{47}T\). At \(c\), the true wave normalization and
\(a(1+Q(c))<10\Delta\) give \(|X(c)|<10TK_j\).
Complex straight-segment Gronwall therefore gives
\[
                         |X|<10TK_j\exp(2^{57}T).
\]
The exact entire density obeys
\[
 \widetilde\mu(x)
   =\exp[-8a(x-c)-\Delta(S(x)-S(c))],
 \qquad |\widetilde\mu|<\exp(2^{56}T).
\]
Since \(h_t=a^{-1}h_x\), combining these bounds in (Q.5) yields
\[
       \|{\cal K}\|_{1024}\le
       M:=2^{10}\lambda a^{-2}K_j^2\exp(2^{60}T).       \tag{Q.21}
\]
For clarity the direct polynomial prefactor is at most
\(400\lambda a^{-2}K_j^2T^2\); its exponential coefficient is at
most \(5\cdot2^{56}\), and \(T^2\le e^{2T}\).
This accounts for the harmless larger constants in (Q.21).

The scale in (Q.21) is
\(1+\Delta+|m|\sqrt{a(1+\Delta)}\).
It is not the much larger \(\lambda\)-scale from estimating the
unbalanced raw first-order system.

## 8. Assemble the explicit lower bounds and retain their permissions

Substitute (Q.19) into (Q.13):
\[
 \operatorname{dist}\ge
 2^{-31424}a^{128}B^{-1472}\lambda^{-256}K_j^{-256}M^{-127}.
\]
Inserting (Q.21), using
\(31424+1270<32768\) and \(127\cdot2^{60}<2^{67}\),
proves (Q.6).

For (Q.7), use
\[
 a>\delta^{3/2}/32,\quad
 a<\delta^{3/2}/16,\quad B=\Delta/a,\quad
 \Delta<3J_0,\quad 1+\Delta<4J_0 .
\]
Then
\[
 T<4J_0+\tfrac12|m|\delta^{3/4}\sqrt{J_0}.
\]
The polynomial powers are exactly
\[
 382+1472=1854,\quad
 (3/2)(1854)+16(510)=10941,\quad
 1472+8(510)=5552,\quad 2(383)=766 .
\]
The remaining fixed binary exponent is less than
\[
 32768+6000(510)+5(1854)+2(1472)
                  =3104982<2^{22},
\]
which proves the displayed coarser formula.

The result concerns the real radial profile, its actual local
diagonal Robin Schur and its complete kernel.
To obtain a usable control theorem one must still produce a real
compact \(\psi\), bound its required \(C_x^4\) norm, enforce both
phase integrals exactly, and account for the true Wronskian
normalization and the two compensating bumps.
A bound for this scalar radial kernel does not invert the
nonradial coupled middle matrix.

Likewise the layer term \(\exp(-2^{69}J_0)\) in (Q.7) is a large
radial cost. A subsequent argument may convert it to a per-frequency
angular-width cost on a separately verified moving-middle window.
It cannot simply be multiplied into the original low-frequency
source space or declared smaller than every fixed radial power.
All ordinary/weak sources, both physical traces, the independent
mean and height, and the true positive DN cross terms retain the
contracts of the input theorem.

## 9. Executed source

Source:
[scripts/fourfold_transparent_kernel_quantitative_separation.mjs](../scripts/fourfold_transparent_kernel_quantitative_separation.mjs).

Complete actual report:
[notes/2026-11-14-R119-transparent-kernel-quantitative-separation.json](../notes/2026-11-14-R119-transparent-kernel-quantitative-separation.json).

The complete arithmetic function ran in the available V8 runtime;
all 43 normalized BigInt gates passed. They cover the fixed complex
disk, all quartic roots, interpolation constants, Hermite and
square-root jet bounds, actual wave/energy conversion, the balanced
ODE growth and every displayed exponent.
The analytic proof above supplies the infinite-frequency statement;
no finite-frequency sample, lost native array or numerical shooting
determinant is used.
