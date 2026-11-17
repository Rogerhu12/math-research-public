# Future inward port and finite linear DN

Numerical evidence; no strong cut. Parent ends at .997; its scalar reference at
$s=1.845715907539644$: $(r,a',a'',w,w_r)=(.941878892351088,-.8,-.9,.75,2.9296875)$.
Use reflected height $h=-z$; future actual jets must satisfy
$h_r=-z_s/a'$ and $h_{rr}=-(z_{ss}-z_sa''/a')/(a')^2$.
Then $\widetilde P=h_\phi/(rw)$, $K=h_r/w-1$ use actual fixed $\rho$.

Fixed: orientation +1, R=prefixR=64, zero valleys, curvature parameter5, pulse caps(.4,.1), native width .39999997814693256, .01 cubic-logw bridge. It preserves cut w/wr and targets reference cuff .5318789142041555. 2404 raw rows deduplicate to2369 nodes:2304 native cells+64 bridge cells. GL8/16 height .07738734822431065/.07738734822431063, length .350285308464154/.35028530846415395. Sampled meridian curvature reaches6.31029; parameter5 is not a continuous bound. Infinite retirement, actual height and reach remain unpaid.

## Actual finite DN

Below the depth4 port use the same native source's far32/steps512 homogeneous columns. On the declared Hermite portion integrate
$C_r=V,\ V_r=(\log w)_r(m^2C/r-V)$ per cell with column renormalization. Deep row $pP+kK=0$ becomes $-mpC/r+kV=0$; only at the cut normalize $P=-mC/(rw)=1$.
For m=2,4,...,16, K/P is
`[-1.69368083755,-2.22492223712,-2.34474151699,-2.34608017502,-2.30611965289,-2.25058038824,-2.19010248945,-2.12957016814]`.
RK4 subdivisions8→16 change DN by at most7.587e-10. Unit-Pcut m2 has sampled max|K|6.74706e8 and max|h_r|198.790: this g strongly amplifies m2. Finite linear diagnostics only; no nonlinear acceptance or infinite-DN bound. A future physical-phi trace requires its rho-weighted angular eigenproblem, not diagonal material m rows.

## Reproduction and identities

Sources: [dynamic-tail-first](2026-11-17-parallel-numerical-dynamic-tail-first.md). S is this topic's scripts path, B=`parallel-inward-apm08-compact-background.json`, C=`parallel-inward-apm08-compact-columns.json`.

```sh
export PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S"
python "$S/parallel_20261117_inward_tail_background.py" --parent parallel-inward0997-m112.json.gz --primitive-background parallel-tail-d4-s64.json --source parallel-tail-source --out "$B"
node "$S/../notes/2026-11-17-parallel-model-calibrate-tail.mjs" --source parallel-tail-source --input "$B" --depth 4 --far 32 --steps 512 --passes 0 --modes '[2,4,6,8,10,12,14,16]' --out "$C"
python "$S/parallel_20261117_inward_linear_dn.py" --background "$B" --columns "$C" --substeps 16 --out parallel-inward-apm08-compact-dn-s16.json
```

SHA256 (raw outputs remain scratch):

- producer `4d075500558c392e7ce4713fd8edfe5230eb47a1f878590684d4c950649fbeab`; DN `cbcf34e98a6595e04d9f6efb3dd36e8c68fd17100106fecaf256948836fa450b`.
- parent `11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`; primitive `b24084c47f03ab87af2f22edeb641d9f50b8a8bbce01d7e9578b2796c5298a3d`.
- B `84fa6bd749e98009f52b69c03f49e9dea1ef489fa693bffd98cbb6b0b2613011`; C `6b55812a755d74af75179ee65da16547234ca755d3c16aef2c05404f47d0e95f`.
- DN8 `7c8c1c0b82ff99c61cac374dc06962a40aeaf7fb75fc035fbe60fb33f22150b7`; DN16 `a9553975d7fe216682314b4a7edb589bb1eb2ad361bcf91c26058d56bdd4fe5c`.
