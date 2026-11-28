# R149 ASQ20. Recovering the low coordinates of all original physical columns

Let \(U\) denote the map from the 96 ordered original trial coefficients to their true physical target, including the correction from the regular equation. Write \(T=\Theta|_{E_{96}^a}\) in the true orthonormal target coordinates. Let \(X\) be the dyadic trial inverse from the actual UACT record, and \(\widehat T\) its original exact dyadic square. For any finite-dyadic matrix \(D\) and verified \(e\) with \(\|\Theta U-D\|_{2\to2}\le e\), the exact matrix \(XD\) obeys
\[
 \|T^{-1}\Theta U-XD\|_{2\to2}
 \le (1347/500)e+(17/100)\min\{\|D\|_{\rm HS},
             \sqrt{\|D\|_1\|D\|_\infty}\}.                  \tag{ASQ20.1}
\]
All components in this formula use unweighted orthonormal real Euclidean coordinate spaces. The signs and order of the 96 input columns and of the 96 original \(\Theta\) rows are fixed by CFC and UACT respectively.

Indeed [ASQ18.1 and its finite application](R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md) give \(\|X\|<2.523\), \(\|I-X\widehat T\|<10^{-15}\) and \(\|T-\widehat T\|<1/40\). Hence \(\|I-XT\|<r=10^{-15}+2.523/40<1\). The Neumann series gives \(\|T^{-1}\|<2.523/(1-r)<1347/500\) and
\(\|T^{-1}-X\|=\|(I-XT)T^{-1}\|<2.523r/(1-r)<17/100\). Now use the exact identity
\[
 T^{-1}\Theta U-XD=T^{-1}(\Theta U-D)+(T^{-1}-X)D.
\]
The full Schur row/column norm bound and the Hilbert--Schmidt bound on \(D\) are evaluated separately on all entries. No assumptions about the individual signs or orthogonality of the 96 true column errors enter this argument.

For the original CFC scientific target the finite matrix \(D\) is the complete binary64 signed centre of the DCP pairings on the 96 physical columns. For each original column \(j\), CFC's original forward residual gives the norm error \(d_j\) of the full target, including its infinite tail. In the original formula for the true \(\Theta\) row error, use \((\|\widehat\Theta\|+13/50)d_j\), by the global part of ASQ18. The complete leakage head and tail, original \(\alpha\) product, true phase and inverse-coordinate fees in the finite action remain in its original \(e_j\). The joint fee \(e=(\sum_{j=1}^{96}e_j^2)^{1/2}+e_{\rm round}\) charges the full change to the exact dyadic centre, including sign and centring roundoff. It supplies precisely the hypothesis in (ASQ20.1).

The ASQ20 receiver forms the actual ordered dyadic product. The original IR trial is generated from the original complete 4096-point grid with its retained immutable binary64 solver and all entries are verified against its original whole SHA. The required square can be obtained without calculating the other 2144 OT output modes. In the original notation let \(z_{j,n}\) be the positive IR coefficient, \(1\le n\le192\), \(u_{j,n}=z_{j,n}/(4n)\), and use the original complete real \(\widehat\alpha\) with \(\widehat\alpha_0=0\). For \(1\le k\le96\) the original DT coefficient is exactly
\[
 v_{j,k}=u_{j,k}+(4ik)^{-1}\sum_{n=1}^{192}\widehat\alpha_{k-n}u_{j,n}.
\]
This is the finite same-sign Toeplitz action. Its negative coefficient indices use exact conjugation of the original positive \(\widehat\alpha\). Each retained sum has the original increasing \(n\) order. The original formal DT readback, true low source phase \(2kb+\pi/4\), low multiplier one, normalized real pairing and original formal OT readback produce the binary64 square
\(\widehat T_{jk}=\operatorname{mid}_{64}[\sqrt2(\operatorname{Re}v_{j,k}\cos(2kb+\pi/4)-\operatorname{Im}v_{j,k}\sin(2kb+\pi/4))]\),
with both formal readbacks performed before their original dependent use. The full 73,728-byte square must match the original UACT SHA beginning 59407fb83861. Its complete 73,728-byte inverse proposal must match the original SHA beginning 982b6c5fe1d9. Both full SHA values and the original IR, grid and \(\alpha\) identities are enforced before using the finite factors. This restores the necessary dyadic witnesses without re-evaluating any old residual, norm or certified scientific target.

Both exact dyadic factors are scaled by a common power of two per factor. Integer multiplication and addition give all 9216 signed product numerators and their common binary exponent. The complete product is privately saved and read back, with its whole-file identity and both signed factor identities available to the next consumer. The physical mean, phase, height, independent world/parameter columns and all high-to-low and low-to-high responses retain their separate slots. Formula (ASQ20.1) supplies a complete finite recovery on the physical target columns once the outstanding original public CFC parent groups have succeeded. No CFC numerical conclusion or complete bordered inverse is asserted here.
