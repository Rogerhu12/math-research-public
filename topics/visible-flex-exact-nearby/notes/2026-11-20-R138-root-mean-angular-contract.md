# R138 minimal full-circle mean denominator

The new source is fourfold_codazzi_root_mean_angular.py. It has only been statically
parsed, with no local scientific evaluation. It is for the repository's
public Actions child. Its sole new mathematical target is a complete
enclosure of the actual root mean denominator D in W.15 and the resulting
nonzero/positive comparison, if the saved enclosing ball supports it.

The source consumes:

1. The already pinned exact definition helper
   fourfold_codazzi_root_axis_support.py, SHA-256
   d152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79.
   It imports that module, calls only its input reader, candidate loader,
   and private original root coefficient definition. It never calls its
   axis target, nor consumes or recomputes q/s.
2. The original root germ
   notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz,
   SHA-256 397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864.
3. The original candidate index and all five sibling lossless shards.
   Index SHA-256 is
   ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.

The essential new mathematical proof pin is
R138-supplement-actual-root-angular-comparison-and-mean-readout.md;
its W.1 and W.16 give the actual periodic-frame transfer. The original
root contract U retains the full mean, high-stable domain, physical angle
and interpretation of the local fixed vector ell=X(root,0).

The whole 65-coefficient definition is private memory. No new array,
matrix, Fourier coefficient packet, or trajectory is published.
Interrupted partial integral scalars and counts are preserved, but no
resume is declared without the private nominal frame. The new source is
designed for one short public child.

## Fixed whole-domain integration

There are N=8192 actual closed angular cells

    I_j = [2*pi*j/N, 2*pi*(j+1)/N].

Every original mode, the repaired mean, the complete true root interval,
all interval coefficient uncertainty and the full cell are used in each
trigonometric evaluation. No scalar target, residual, intrinsic primitive
or old geometry ODE is reevaluated.

On a cell the exact ideal frame obeys O'=O Omega, with a real skew
connection. Let Omega_c be the exact Arb midpoint of the three connection
coefficient balls. If d_j is the Euclidean norm of their complete radii,
then ||Omega-Omega_c||_op <= d_j throughout that cell.

The private nominal point matrix M is propagated by the exact constant
rotation exp(t Omega_c), enclosed by the 3-by-3 Rodrigues identity.
If ||O(left)-M||_op <= E, variation of constants against the orthogonal
constant propagator gives, for every 0 <= t <= h,

    ||O(left+t)-M exp(t Omega_c)||_op <= E + h*d_j.

No orthogonality of the nominal rounded matrix M is assumed. The forcing
in this identity uses the exact orthogonal O, so the bound has no
spurious multiplicative growth factor.

At the right endpoint, the entire Arb arithmetic radius of the matrix
product is bounded in Frobenius norm and added to E. The new private M
is the exact midpoint matrix. Thus all earlier rounding remains paid.

For the integral, exp([0,h] Omega_c) is enclosed on the whole time
interval. Each entry is widened by E+h*d_j before inserting X_z,Y_z into

    g_m dot ell = (a/m) * (A0 X_z + B0 Y_z),
    q0 = -I(v-m)/m,
    A0 = 1/v - q0*v_phi/v^2,
    B0 = -u*A0 - q0*u_phi/v.

The normalized whole-cell integral lies in this complete interval divided
by N, since h/(2*pi)=1/N exactly. Adding the 8192 entire cells encloses
the full ideal denominator; it is not a quadrature of midpoint values.
The same cells bound the coefficient integral

    chi_m = average |a/m| sqrt(A0^2+B0^2).

The actual periodic-frame denominator is contained in

    ideal_D + [-(11/10^7)*chi_m, +(11/10^7)*chi_m].

This is W.16. The ideal full-circle ODE need not close its endpoint.
Neither a periodicity constraint nor an unproved C1 transfer is imposed
on it.

## Scalar publication and scope

The denominator and coefficient integral are published as exact decimal
integer midpoint/radius/exponent balls via mid_rad_10exp(70), and their
entire outward readback is checked. The actual-frame fee is formed from
these saved complete enclosures. The final sign uses the complete saved
actual denominator ball, not a hidden narrower value.

The result is complete even if that entire ball is not separated from
zero: then both nonzero and positive claims are false. This is an
enclosure result, never a declaration of singularity. The full root
energy, body residual absorption, inverse and final topic theorem all
retain their separate false/unpaid scopes.

## Entry

    python fourfold_codazzi_root_mean_angular.py \
      --definition-source <pinned-axis-source.py> \
      --germ <accepted-root-germ-native.json.gz> \
      --candidate <original-candidate-index.json> \
      --output <new-root-mean-result.json>

The scientific runtime needs python-flint and numpy; Arb precision
is fixed at 320 bits. Only exact input restoration and static inspection
are allowed outside the public child.
