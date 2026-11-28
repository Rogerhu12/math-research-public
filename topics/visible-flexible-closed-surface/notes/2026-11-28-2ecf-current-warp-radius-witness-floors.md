# Current fixed-field witnesses for the sharp warp-radius floor

**Numerical evidence.** For the same position field at its stored worst relative-metric sample, minimize the spectral error analytically over *all* positive target radii, even allowing the radius to depend on the angle. The formula is in the accompanying sharp pointwise warp-radius lemma. With the old target radius $a_0$, the stored components are $e=E-1$, $f=F/a_0$, $g=G/a_0^2-1$. Thus $F^2/G=f^2/(1+g)$, with no finite-difference reconstruction.

| saved field and grid | s | observed | lower bound for arbitrary warp |
|---|---:|---:|---:|
| polar-G10s-fast-step14-step01-state.json | 0.1037166394 | 0.218494335084 | 0.218494335084 |
| polar-G10s-fast-step14-G11.json | 0.1039428934 | 0.212742187555 | 0.212045410544 |
| polar-design-G10s-fast-step17-step01-state.json | 0.1037166394 | 0.154289511718 | 0.154289511718 |
| polar-design-G10s-fast-step17-G11.json | 0.1039428934 | 0.149375935435 | 0.148950353803 |
| polar-frozen-alpha10-step04-step01-state.json | 0.1037166394 | 0.160846177732 | 0.160846177732 |
| polar-frozen-alpha10-step04-G11.json | 0.1039428934 | 0.15557970003 | 0.155159218548 |
| polar-frozen-alpha10-M32-step01-step01-state.json | 0.1037166394 | 0.159878718638 | 0.159878718638 |
| polar-frozen-alpha10-M32-accepted-G11.json | 0.1039428934 | 0.153905863451 | 0.153422246748 |

At all four G10 worst witnesses, angular-radius redesign alone has no visible room at the stated precision. At the four independent G11 witnesses the most it can improve the uniform metric error is respectively 0.000697, 0.000426, 0.000421 and 0.000484. A reduction from order 0.15 to the required precision therefore needs a position-field change within this meridional gauge. This neither certifies a continuous maximum nor excludes simultaneous changes in the position field and the warp.

## Reproduction

The G10/G11 source recipes and accepted steps are in the original 7–14, design 9–17, frozen 1–4 and M32 refinement notes. Put the sources and regenerated states in W.

```sh
python3 -u $W/2ecf-polar-radius-optimal-witness.py --output $W/polar-radius-witness.json $W/polar-G10s-fast-step14-step01-state.json $W/polar-G10s-fast-step14-G11.json $W/polar-design-G10s-fast-step17-step01-state.json $W/polar-design-G10s-fast-step17-G11.json $W/polar-frozen-alpha10-step04-step01-state.json $W/polar-frozen-alpha10-step04-G11.json $W/polar-frozen-alpha10-M32-step01-step01-state.json $W/polar-frozen-alpha10-M32-accepted-G11.json
```

Script SHA-256 `5f8e1b03ddd965798ee655e9645d7e4ea57dc0c242cd2b1ea710701b4e57adff`. Output `779a394b2f74b498d6fc47b223417fb82e1a2a1619330462b529b0fc9b10e407`. Natural exit 0 in 0.20911 seconds.

Input SHA-256 values:

- polar-G10s-fast-step14-step01-state.json `c66ae970d4e6fa2ab1886c18a22a9bcf77eccb5d4f0c719eb82336829a5f3c15`.
- polar-G10s-fast-step14-G11.json `2da9fa323982f9796e8ff4213bab9b6c711f0df1b74370365a665468c8d0f40a`.
- polar-design-G10s-fast-step17-step01-state.json `0b74a5755c8bfc46b7024f9feeec057465a1d9252bc4a5de4b2a22cb801594b2`.
- polar-design-G10s-fast-step17-G11.json `1c8e35bdbc291e0d7b35a03f76a50f04fc7fc81bc5f574e8419c50c144b17971`.
- polar-frozen-alpha10-step04-step01-state.json `10fee0325bba32ab5eb1f58b84c8be1b87ca14efab9474adb27011f66063707f`.
- polar-frozen-alpha10-step04-G11.json `ddf167ab8552db6b26ce2458ad467b7230243878db4123a0d472af82f8507a14`.
- polar-frozen-alpha10-M32-step01-step01-state.json `a8a4d2231af9b89ce25317d8e93f2a8541eb5fd384a588f72bfcf1f3bd9e0d09`.
- polar-frozen-alpha10-M32-accepted-G11.json `01e26eb439b0744848e652f8010e695e4fe3280790876c30e3cb5fa9057521ac`.
