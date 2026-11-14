# R595 recovery erratum: the last factor in (595.10)

This corrects a transcription in the recovered proof whose pre-correction
SHA256 is `5f5f7253010dc94b1050b4ceef189e811b973bcf2cc772f9309a24c73e0a67cc`.
It does not change the recovered rational kernel, coefficient records, or any
torsion-orbit computation.

With $R=N/\Delta$ and $V=N'\Delta-N\Delta'$, the old displayed formula was

$$
4(x^3-1)(V'\Delta-2V\Delta')+6x^2V\Delta'=2A_2.
$$

The last $\Delta'$ must be $\Delta$. The correct formula is

$$
\boxed{4(x^3-1)(V'\Delta-2V\Delta')+6x^2V\Delta=2A_2.}
$$

Indeed $D=2y\,d/dx$, $y^2=x^3-1$, and $Dy=3x^2$, so

$$
D^2R=4(x^3-1)R''+6x^2R'
=\frac{4(x^3-1)(V'\Delta-2V\Delta')+6x^2V\Delta}{\Delta^3}.
$$

The coefficient of $E^2$ in the actual saved kernel is
$A_2/(2\Delta^3)=D^2R/4$, giving the boxed identity.

The recovered constructor `R595-exact-H2-kernel.recovered.js` computes the
kernel by the full rational eighteen-point trace. It contains neither version
of this displayed differentiation identity and has no such transcription.
The historical identity-checker source was lost, so its exact original line
is not asserted here. The saved $A_2$ coefficients were independently
substituted into the boxed identity in the new, short
`R605_rational_kernel_reduction.py`: the full integer polynomial is zero,
whereas the old displayed expression is nonzero. This short new symbolic
check was actually executed; no old torsion orbit, $269$ computation, or prime
grid was repeated.

The new check also proves the rational integration-by-parts identity in the
R605 working record. Its data are saved as
`R605_rational_kernel_reduction.json`, SHA256
`702be8ed8987d53122a8dba3937b597ce0b997a2dde2947324276b2bd18fbb88`.

The frozen recovered proof is left intact for the root publisher to apply this
explicit correction and record the changed publication hash.
