# R104 supplement: cutoff-dependent gauge with the complete finite head

2026-11-13, phase-inverse continuation.

**Status.** This is a proved improvement of the R104 operator interface. It
replaces the fixed high Sobolev multiplier cost by a multiplier cost that
depends on the actual cutoff. It keeps every low-to-high and high-to-low
entry in the exact finite-head Schur problem. It does not supply the missing
identification of the actual complete feedback coefficient, the complete
returned strong remainder, or a certified inverse of that Schur problem.
In particular no numerical phase sample is used as an operator certificate.

## 1. The same complete operator and a different gauge

Use the R104 positive-frequency notation and fixed weight
\(W_j=e^{\rho\varpi(|j|)}\), where \(\varpi\) is increasing and subadditive.
Suppose the actual complete operator has already been proved to satisfy

\[
 A=I+U(I+iT_bD^{-1})+R,\qquad
 \langle b\rangle=\beta,\qquad
 \|R:H^s_\rho\longrightarrow H^{s+4/3}_\rho\|\le R_*
 \quad (|s|\le S).
 \tag{G1}
\]

Here \(De_j=je_j\), \(Ue_j=e^{ij\omega}e_j\), and \(T_b\) is the full
positive-cone Toeplitz compression. Assume the same already paid divisors

\[
 |1-e^{-il\omega}|>{2\over5|l|}\quad(l\ne0),\qquad
 |1+e^{ij\omega}(1+i\beta/j)|>{c\over j}\quad(j\ge1).
 \tag{G2}
\]

For the actual R104 arithmetic one can use \(c=7/110\). Solve the same
cohomological equation, without averaging away its nonconstant input:

\[
 a_l=-{b_l\over1-e^{-il\omega}}\quad(l\ne0),\qquad a_0=0,
 \qquad a-a(\mathord\cdot-\omega)=\beta-b.
 \tag{G3}
\]

Fix an integer \(N\ge1\), put \(P=1_{j\ge N}\), \(Q=I-P\), and now use
the **two-sided** high compression

\[
 C_N=PT_aP D^{-1}P,\qquad T_N=I+iC_N.
 \tag{G4}
\]

Unlike an input-only compression, this gauge commutes with \(P\) and is
exactly the identity on the finite head. The discarded output rows are
retained in the full conjugacy error in (G9), not declared to be zero.

For \(r=0,1\) define complete Fourier sums

\[
 A_r(N)=\sum_{l\in\mathbb Z}
 W_l(1+|l|/N)^S |l|^r|a_l|,\qquad
 B_r(N)=\sum_{l\in\mathbb Z}
 W_l(1+|l|/N)^S |l|^r|b_l|.
 \tag{G5}
\]

Use \(0^0=1\). These sums include every actual coefficient and every
infinite tail. Set

\[
 q_0={A_0(N)\over N},\qquad
 q_1={A_0(N)+A_1(N)/N\over N}.
 \tag{G6}
\]

All conclusions below require \(q_1<1\), and hence also \(q_0<1\).

## 2. Complete high-block multiplier and gauge bounds

For \(j,k\ge N\) and \(l=j-k\), the triangle inequality in
\(\mathbb R^2\) gives

\[
 {\langle j\rangle\over\langle k\rangle}
 \le 1+{|l|\over\langle k\rangle}\le1+{|l|\over N},
 \qquad
 {\langle k\rangle\over\langle j\rangle}\le1+{|l|\over N}.
\]

Consequently, for every \(|s|\le S\), Young's inequality gives the true
infinite-matrix bound

\[
 \|PT_vP:H^s_\rho\to H^s_\rho\|
 \le\sum_l W_l(1+|l|/N)^S|v_l|.
 \tag{G7}
\]

This argument requires both input and output frequencies to be high. It is
not valid for a low output of a high input in a negative Sobolev norm; those
entries remain in the finite-head wiring below.

The exact matrix commutator is
\(DT_a-T_aD=T_{Da}\), with \((Da)_l=la_l\). Thus

\[
 \|C_N\|_s\le q_0,\qquad
 \|DC_ND^{-1}\|_s\le q_1,
\]
\[
 \|T_N\|_s\le1+q_0,\quad
 \|T_N^{-1}\|_s\le(1-q_0)^{-1},\quad
 \|DT_N^{-1}D^{-1}\|_s\le(1-q_1)^{-1}.
 \tag{G8}
\]

These are convergent Neumann inverses on the entire infinite high space.
The last formula follows by conjugating the convergent series, or directly
by inverting \(I+iDC_ND^{-1}\). It avoids asking for a separate unproved
\(s+1\) window of the actual remainder.

## 3. Exact full identity and its high compression

Write
\(\mathcal D=I+U(I+i\beta D^{-1})\). Expanding products gives

\[
 AT_N-T_N\mathcal D=F_N+E_N+RT_N,
\]
\[
 F_N=iU\{T_{b-\beta}D^{-1}Q
                 +QT_{b-\beta}D^{-1}P\},\qquad
 E_N=-UT_bD^{-1}C_N+\beta C_NUD^{-1}.
 \tag{G9}
\]

For the first-order terms, use
\(C_N-U^{-1}C_NU=PT_{\beta-b}PD^{-1}P\). The two terms in \(F_N\)
are respectively finite input rank and finite output rank. Each can have
infinitely many nonzero matrix entries. Both are kept exactly; the only
vanishing assertion is \(PF_NP=0\).

Let \(A_H=PAP\), \(T_H=PT_NP\), and \(\mathcal D_H=P\mathcal DP\).
On the high space, (G9) is therefore

\[
 A_HT_H=T_H\mathcal D_H+E_H+R_HT_H,
\]
\[
 E_H=-U(PT_bP)D^{-1}(PT_aP)D^{-1}
          +\beta(PT_aP)D^{-1}UD^{-1},\qquad R_H=PRP.
 \tag{G10}
\]

All intermediate frequencies in these two displayed products are high.
No Toeplitz product has been replaced by multiplication of its symbols.

The exact commutator in §2 gives

\[
 \|DE_H\|_s\le
 {A_0(N)[B_0(N)+B_1(N)/N]
       +|\beta|[A_0(N)+A_1(N)/N]\over N}
 =:\mathcal E_N.
 \tag{G11}
\]

For example
\(D(PT_bP)D^{-1}=PT_bP+PT_{Db}PD^{-1}\); this is the first
factor in the first term. The second term is handled identically. This
calculation pays the actual ordering of both inverse derivatives.

The complete strong remainder satisfies

\[
 \|DR_HT_H:H^s_\rho\to H^s_\rho\|
 \le {R_*(1+q_0)\over\langle N\rangle^{1/3}}.
 \tag{G12}
\]

Indeed \(j/\langle j\rangle^{4/3}\le\langle N\rangle^{-1/3}\)
on its high output. This uses the full strong matrix norm in (G1), including
all intermediate frequencies of the actual remainder, rather than a
columnwise asymptotic.

## 4. A cutoff-dependent high inverse with one derivative loss

Define

\[
 \boxed{\displaystyle
 \kappa_N={1\over c(1-q_1)}
 \left\{\mathcal E_N+
 {R_*(1+q_0)\over\langle N\rangle^{1/3}}\right\}.}
 \tag{G13}
\]

If \(q_1<1\) and \(\kappa_N<1\), then every right-hand side in
\(PH^{s+1}_\rho\) has exactly one solution in \(PH^s_\rho\), with

\[
 \boxed{\displaystyle
 \|A_H^{-1}:PH^{s+1}_\rho\to PH^s_\rho\|
 \le {1+q_0\over c(1-q_1)(1-\kappa_N)}
 \quad(|s|\le S).}
 \tag{G14}
\]

To see this without commuting the gauge with the diagonal model, put

\[
 K_H=\mathcal D_H^{-1}T_H^{-1}(E_H+R_HT_H).
\]

The multiplier \(\mathcal D_H^{-1}D^{-1}\) has norm at most \(1/c\).
Use the exact factorization

\[
 \mathcal D_H^{-1}T_H^{-1}
 =(\mathcal D_H^{-1}D^{-1})(DT_H^{-1}D^{-1})D.
 \tag{G15}
\]

Equations (G8), (G11), and (G12) give \(\|K_H\|_s\le\kappa_N\).
Equation (G10) becomes
\(A_HT_H=T_H\mathcal D_H(I+K_H)\). The inverse of \(I+K_H\)
is its convergent Neumann series. The same factorization (G15), now applied
to an \(H^{s+1}_\rho\) input, yields (G14).

This proof uses only the same \(|s|\le S\) window of \(R\) as R104.
There is no hidden application of \(R\) at \(s+1\) or \(s+2\).

## 5. All low rows, columns, and ordinary sources remain

With the exact block decomposition \(P+Q=I\), form

\[
 S_L=A_{LL}-A_{LH}A_H^{-1}A_{HL}.
 \tag{G16}
\]

It acts on the actual finite head, but its second term includes the
infinite output of every low column and the infinite input of every low
row. If and only if this complete finite-head matrix has the required
inverse, the full solution is given by

\[
 u_L=S_L^{-1}(f_L-A_{LH}A_H^{-1}f_H),\qquad
 u_H=A_H^{-1}(f_H-A_{HL}u_L).
 \tag{G17}
\]

An ordinary source already wired into \(f\) follows these same formulas.
A weak divergence load, a contact source, or an unconnected PDE port does
not become an ordinary \(f\) merely by writing (G17).

For the complete R104 setting, apply this construction to the direct sum
of all diagonal principal cones and amplitude branches, with the maximum
of their corresponding \(A_r,B_r,q_r\) and the **full block** \(R_*\).
All cross-cone and cross-amplitude entries must already belong to that
paid remainder. Add the actual mean and finite augmentation coordinates
to the head in (G16). This is a bookkeeping extension of the block proof,
not an authorization to delete those entries.

## 6. How actual Fourier certificates enter

An actual finite coefficient enclosure is useful here only together with
its full tail. If \(|b_l|\le M e^{-\sigma|l|}\) and
\(W_l\le e^{\rho|l|}\), \(\rho<\sigma\), then (G2) gives the valid tail
bound \(|a_l|\le(5/2)|l|M e^{-\sigma|l|}\). For integer \(S\), the
tail of each sum (G5) reduces after a binomial expansion to finitely many
positive sums \(\sum_{l>L}l^q e^{-(\sigma-\rho)l}\). These have exact
rational expressions in \(e^{-(\sigma-\rho)}\), or directed upper bounds
from the existing power-tail/Stirling recurrence. For retained modes one
may use the actual certified divisor in (G3) rather than the uniform
\((5/2)|l|\) estimate.

As \(N\) increases, the Sobolev factor in (G5) decreases to one. This is
why the large factor \(\langle l\rangle^{S+3}\) from the fixed global
Peetre estimate need not be paid in the high inverse. It does not remove
the true size of the complete Fourier sums, the \(R_*N^{-1/3}\) cost, or
the need to invert the exact head (G16).

No actual \(b_l\), full \(R_*\), or numerical cutoff is asserted in this
supplement. The full geometric phase diagnostic and the separate strict
R46 bounds are not substitutes for those three complete-return inputs.
