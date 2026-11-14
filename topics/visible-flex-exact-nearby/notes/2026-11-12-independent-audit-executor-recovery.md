# Actual beta bulk recovery after executor reset

Status: development only. No full beta enclosure has been proved.

The executor changed while the child independent_audit was performing the
bulk integral. The previous execution sessions cannot be resumed. Explicit
shell `bash`, `login=false` works on the replacement executor; the former repo
checkout is absent. Do not confuse the remaining placeholder topic directory
with a git checkout.

## Frozen input and previously proved collar

Input: type_fixed_step02_analytic_smoothing_inputs.npz, SHA256
bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532.
The explicit symmetric infinite R33 primitive has even radius and beta,
odd gamma and exact integral height, and the full R37 ell zero order.

The previously completed collar package (parent independently checked):

- fourfold_phase_beta_interval.py, SHA256
  d23c4c5531e2d12deefb1bc93634b25d00417ecbf526e74298efae51e88ad277.
- 2026-11-12-beta-full-collar-enclosure.json, SHA256
  7f8dc9e5539e05554b05dbac10b6ea77e8188a9e0030178fdc3ad0ae05967015.
- 2026-11-12-directed-root-collar-finite-part.md, SHA256
  0887cc03efe281cf97ef89cef539c48182107764d897f6222ddd39972c1f5cb0.

The exact fixed cut is
b=1072423152036779/4503599627370496. The corrected infinite root satisfies
t in [.23836991573146337267349149754020302,
.23836991573146337267349149759843689]. The complete infinite collar finite
part is enclosed by [1305.4032588258,1305.4032592152]. The radial Taylor tail
is at most 1.94585255415198e-7 and the 2048-angle trapezoid fee is at most
9.56674067017e-14. This collar does not by itself certify beta.

## Bulk exact algebra

Use C=F_theta cross F_r, A2=C dot C, R2=F dot F, h=C dot F;
l,m,n=C dot (F_rr,F_rtheta,F_thetatheta). Set
a=-n/A2, b=m/A2, c=-l/A2, kgeom=(l*n-m*m)/A2^2,
omega=(kgeom-K0)/a, chat=(b^2+K0)/a.
These are the zeta^2-multiplied coefficients, not the unscaled R37 matrix.

With X=F_r, Y=F_theta, P=F dot X, Q=F dot Y,
d=(a*(X dot X-P^2/R2)+2*b*(X dot Y-P*Q/R2)
+c*(Y dot Y-Q^2/R2))/R2.

logz_r=(C_r dot F)/h-(C dot C_r)/A2-P/R2; likewise theta.
fr=K0'/(2*K0)-2*logz_r, ft=-2*logz_theta,
ell=Y_z/F_z-Q/R2.
The actual bulk density is
J=(d+omega*(ell^2+ell*ft)-(a*fr^2+2*b*fr*ft+chat*ft^2)/4)/sqrt(-K0).
For this symmetric object beta=(bulk positive-half integral+collar)/2.

## Exact spline cells, not floating midpoint selection

The positive half interval has 167 nonzero common knot cells before inserting
the waist cut 2^-20. Include every exact binary knot from both signs and
retain widths around 1e-16. Convert binary knots to Fraction. For each spline,
select the span with the exact rational midpoint and assert that both cell
endpoints lie in that same closed span. Build the full local polynomial with
Arb precision cap at least degree+1; calling NativeSpline.germ at cap4 before
seeding its cache can silently truncate its cached high coefficients.

One may continue that local polynomial beyond its physical span for complex
Cauchy estimates. This does not assert analyticity of the piecewise spline
across another knot. All actual real integrations are split at all knots.

## Directed fast kernel design and verified comparisons

New development files were fourfold_phase_beta_bulk_interval.py (about 23KB)
and fourfold_phase_beta_bulk_box.py (about 25KB). They used:

1. Arb exact-span scalar polynomial coefficients, enclosed into binary64
   endpoints by one outward nextafter after each conversion.
2. Complex boxes built from the existing directed real Box class. All
   arithmetic, pairwise sums, and radix-two FFT butterflies use outward
   binary64 elementary operations. Roots of unity come from Arb. No numpy
   floating FFT is used in a certificate.
3. Complex sine/cosine Taylor polynomial degree32 with entire remainder
   exp(R)*R^33/33!. Actual radial jets through order3 are then explicit.
4. One normalized Horner pass for all scalar jets at once. For derivative
   jets J0..J3, multiplication by z updates
   (zJ0+c,zJ1+J0,zJ2+2J1,zJ3+3J2).
5. The native quarter DFT primitive and parity rules, with true infinite
   Fourier/alias errors from R52. Field derivatives use Cauchy fees
   eps_i=i!*eps_F/Rout^i, Rout=.003, source angular strip .32.
6. Exact identities F_theta=a*T, F_rtheta=a'*T+a*T_r,
   F_thetatheta=a*T_theta. They avoid amplifying interval DFT errors by
   retained mode squared. Only F, F_r, F_rr use the primitive FFT.
7. The exact reflection gives F(-theta)=diag(1,-1,1)F(theta). Thus J is even.
   The full A-point trapezoid is evaluated as
   (J0+J_(A/2)+2*sum(J1..J_(A/2-1)))/A. The domain cover of the half circle
   reflects to the whole circle; the same full-A trapezoid error is paid.

At r=.1001 the independent native Arb evaluator gave
-2.7387295061040961348896 +/-4.51e-23. The directed box evaluator, after the
exact angular derivative identities, contained it with about 8.3e-12 radius.
This comparison is a development validation, not a proof of all source code.

## Sharper target E error budget

The finite primitive has Fourier coefficients F_(i,k) for radial derivative
i. Let B_i=max_component sum_k abs(F_(i,k,component)). The complex bilinear
mean is E=<F_r dot F_r>, never a Hermitian conjugate in complex r.
The actual infinite errors for E,E',E'' are bounded by

e0=3*(2*B1*eps1+eps1^2),
e1=6*(B1*eps2+B2*eps1+eps1*eps2),
e2=6*(2*B2*eps2+eps2^2+B1*eps3+B3*eps1+eps1*eps3).

With scalar radius a and jets ar,arr,arrr,
N=ar*E'-2*arr*E, N'=ar*E''-arr*E'-2*arrr*E,
K0=N/(2*a*E^2),
K0'=N'/(2*a*E^2)-K0*(ar/a+2*E'/E).
This sharper jet budget makes quarter grid256 potentially sufficient for
the deliberately broad first beta enclosure; the old coarse uniform E
Cauchy budget did not. Every final accepted integration cell must still
meet its actual error budget.

## Analytic integration and domain checks

The radial callback uses acb.integral on each exact polynomial cell with
outward complex-box enclosures, allowing automatic subdivision. For every
complex radial ball it proves Re(-K0)>0, Re(A2)>0, Re(R2)>0, Re(h)>0,
Re(a)>0, and Re(F_z)>0. Hence all quotients and sqrt(-K0) use actual analytic
branches. A failed gate returns nan so the validated integrator subdivides.
No failed gate is ignored.

Separately enclose all actual real r in the subcell and complex normalized
angle x=4theta, |Im x|<=sigma=.02. Each angular grid cell includes its real
half-gap pi/A. At real r, the real part of the vertical first variation is
zero: finite Fourier coefficient padding for mode k is
abs(k)*pi/A+cosh(abs(k)*sigma)-1 in real part, sinh(abs(k)*sigma) in imaginary
part. Add the full infinite tail at sigma+pi/A. Direct tangent fields use
exact complex trigonometry on the same angular rectangles.
If M bounds |J| on that complete strip, the angular mean fee is
2*M*exp(-sigma*A)/(1-exp(-sigma*A)). Multiply by cell length.

The small waist [0,2^-20] uses the exact odd identities F_z(0)=Y_z(0)=0:
F_z/r belongs to a box for (F_r)_z and Y_z/r belongs to a box for (F_rtheta)_z
on the whole small interval. This encloses ell without dividing by r.
The native and fast kernels both proved a waist integral radius below
7.4e-6 using continuous angular cells; no angular quadrature is used there.

The first smoke at quarter512/angles1024 accepted several strict subcells
in the first knot span, with subdivision depths 5..7. Its stopped partial
report must not be called a full certificate. The new quarter256 smoke
started and passed its waist bound, but the executor reset before a complete
bulk cell was recorded. The full bulk source and report need restoration.

## Important implementation cautions

- In complex-box FFT reshape operations, arrays are shared views. A cached
  `is_real` flag can become stale after a butterfly writes imaginary parts.
  The corrected implementation computes `is_real` dynamically from current
  interval arrays; do not restore the intermediate cached-flag version.
- Exact-zero Arb coordinates can transfer to exact binary64 zero. For real
  inputs, real trig outputs and known-real target E jets may be projected to
  real intervals; not for a complex radial quadrature ball.
- Tail scalar polynomial bounds must round all additions outwards. In
  particular beta-bound+gamma-bound is computed in Arb, not an unrounded
  numpy float addition.
- Keep physical support and target data of the same frozen infinite object.
  The nearby D5 object has a different beta, diagnostically about37.025921506;
  no original-object interval may be transferred to it.

## Next authorized work

Restore frozen dependencies and the two bulk files, rerun the partial
integration. Aim for per-original-cell absolute error .0002, so 167 cells
give less than .034 bulk error and less than .017 beta error, plus the small
waist/collar fees. Adaptive subcells receive tolerance proportional to exact
length, so their sum stays within the original cell budget. Preserve all
failed/development reports but label them as incomplete.
After complete exact endpoint coverage, add the collar and divide by2.
Apply the interval to the actual R34 dangerous grid; then run the full
calculation independently for the D5 exact-affine object.
