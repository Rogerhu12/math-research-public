# A torqued p6 center, a polar connector and 72 real coupled position controls on the original material metric (V57)

Keep the original V40 radial target and its full central strip length 2·13/128. Use R320's exact rectifying strip with a different closed space curve. For x=sin²θ define F=A cosθ x⁶(x−d)/(1−d), A=.18, d=1001/1184, and T=(−sinθ, cosθ √(1−F²), cosθ F). Keep the material dv=ρdθ, ρ=1/5+32x²/15. In particular d is the exact ratio of the moments of ρ cos²θ x⁷ and ρ cos²θ x⁶. Thus the vertical component of γ_θ integrates to zero over π; the other components and full closure follow from their displayed parities. This upper field has a horizontal half-turn symmetry together with the R320 two-half reconstruction. At each point invert the material clock using a bracket-contraction iteration and an explicit inverse-residual check.

Integrate the full nonlinear Cartesian Cauchy field to t=.20 at 512 true angles and 1200 RK4 steps, using all cosine and sine harmonics through order 152 in each coordinate and 40 quintic radial spans. Generate a new two-port surface in genuine cylindrical polar coordinates on [.20,.80]. At both ends extract position and both radial jets at fixed physical polar angle, and separately match the material angle clock. For azimuth φ set w=z−.28r; a degree-16 Bernstein expression for w_t matches the two endpoint jets and the full endpoint difference. Use a degree-9 radius. Across the four interior radial Bernstein controls solve for radial and w changes with nine material Fourier factors in each, giving 72 real spatial variables. All changes keep the two true end jets. Fit on 49 radial positions and 64 native angles with 115 L-BFGS steps. Reconstruct the complete actual Cartesian field in 56 radial quintics with all angular orders through 104 in each component; the endpoint residual jets vanish exactly. Both true caps and the R314 exterior continue beyond the new connector.

| Whole observer | metric | physical curvature | held | half-width | minimum area ratio |
|---|---:|---:|---:|---:|---:|
| G10a | .629206369 | 15.622698 | .59408490 | .97412927 | .58688253 |
| G10b | .629206369 | 15.630181 | .59408490 | .97412927 | .58688253 |
| G11 | .628796467 | 15.638969 | .59421993 | .97413480 | .58687151 |

The independent prefix alone gives metric 1.0611105e−5 and physical curvature 7.3980504. The full upper annulus includes all 4,291,840 prescribed plus 2,394,112 independent scalar rows and retains all seven original geometric guides. This actual full field misses the strong metric, reach-curvature, held and width working bounds. R320's certified nonplanar strip is a different curve; its strict estimates are not transferred here.

With V40's STATE192 and V48's STATE540, run from this topic's scripts:

```sh
node 2ecf-compact-p6-steered-space-center.mjs make STATE192 STATE540 P6BASE .18 .1015625 512
node 2ecf-compact-p6-polar-space-connector.mjs fit STATE192 STATE540 P6BASE P6COEFF
node 2ecf-compact-p6-polar-space-connector.mjs field STATE192 STATE540 P6BASE P6COEFF P6FIELD
node 2ecf-compact-p6-polar-space-connector.mjs observe STATE192 STATE540 P6BASE P6FIELD
```

Generated JSON SHA256 including LF: P6BASE f85d8f40115cbd4ab264b4b1c2bd26ab6dcfbe3628172ac2c8e42ccba367e0cc; P6COEFF 2c4a439f99d91f8f7ae41df7b59c04a9c395baa412c7a9ab832aa50338127fe3; P6FIELD ba4c17df10a137e326790191b828d2013ee201d09f25b690a938a61e33f8037d. The complete observer exited zero using these three regenerated inputs.
