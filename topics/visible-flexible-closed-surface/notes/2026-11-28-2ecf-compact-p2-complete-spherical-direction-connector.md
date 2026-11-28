# A full spherical-direction connector from 49 real quadrant meridians (V54)

Keep the original p2 512-angle Cauchy prefix, the original V40 frozen metric, and the same R314 real shell and caps. On [.24,.8] change the generating variables for the actual surface. At 49 true material angles in the fundamental quadrant solve clamped spherical directions with eight angular Hermite spans in normalized meridional length. True left/right position, tangent and curvature come from both physical ports. Compute each Cartesian meridian by integrating its unit direction over the common physical length .85372. The generator keeps both pole azimuths and radial curvature jets clamped, and includes physical width, height, held ball and curvature penalties. The real prefix target arclength is approximately .853719. Small integrated endpoint residuals are removed with a quintic that exactly preserves both boundary two-jets; the maximum physical repair is .000699595. Encode differences from the exact two-sided Hermite port extension with 56 genuine radial quintics and 40 true angular indices per Cartesian coordinate. The residual PVA is exactly zero at both joins, including endpoint angular derivatives. The full center and exterior keep their own mathematical definitions.

The long meridian endpoints close before the final repair to about 1.3e−6 with sampled physical curve curvature 9.576. At the last reflected short meridian the preliminary 80-point direction fit gives curve curvature 20.15. The unreleased per-angle fitting leaves steep angular dependence near the short axis.

| Full physical observation | spectral metric defect | max principal curvature | minimum area ratio | held | half-width |
|---|---:|---:|---:|---:|---:|
| G10a | 132.72265 | 24790.083 | 0.025766936 | 0.65068645 | 0.91680771 |
| G10b | 132.72265 | 24790.083 | 0.025766936 | 0.65408874 | 0.91426667 |
| G11 | 112.50551 | 779971.82 | 0.0024728134 | 0.65194495 | 0.92009007 |

The G11 worst metric (t,u)=(.538771738,4.722623700) has large circumferential stretch. Its diagonal radial, off-diagonal, and diagonal angular component suprema over G11 are .697529, 4.102939, 112.500232. Finite held clears .65 on all three reported grids while the area, curvature, angular length, shear and width remain unsuitable. Successful individual direction fits do not imply compatibility of neighboring meridians. A joint angular fit and independently varied target remain open.

Run `2ecf-compact-p2-two-port-rays.mjs make STATE192 STATE540 P2F512 RAYFIELD`, then `observe STATE192 STATE540 P2F512 RAYFIELD` on the same inputs as V52. Generated field SHA256 with LF 02459e1f48d9e719faaa0ae412a208413c802f327c9898ecf3f007f45108a57b. Both full upper material grids and all original 14 rows were observed.
