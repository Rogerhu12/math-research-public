# 原弯向开发尾的所选 Z=.52 输入及两个真实位置步

**数值证据。**

在 15 项原弯向 R205 真端口的完整选择后，固定选定高度 .52 与原弯幅。将 gap 23/25 自身第 2 态的完整 5292 W 纳入新底图，再以 5292 个初值为零的真实位置系数重新开始；同一目标、完整原两网格及 4291840 行保留。含新帽的目标度量保持，因为这次原喉与帽整片刚体平移。新源保留真端口的数据 SHA，逐次重算全六 jets。自身 0 时 G10 R²=.0818625018319668、G11 metric .2023424235、κ19.55502796、held .6422178391。

| 新真实步 | 原G10 R² | G11 metric / κ / held |
|---:|---:|---|
| 1 | 0.073596118965 | 0.31937905079 / 22.194313462 / 0.63407957887 |
| 2 | 0.069269202016 | 0.26385567904 / 15.802908792 / 0.63345346934 |

两个步均降低自身原成本。独立第二态 κ15.80291，held 未达 .64，且 metric .26385568 高于初态。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-gap092-selected-tail-position-source.py" --mode prepare --scripts "$S" --parent polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --donor polar-new-gap-092-fixed-step02-step01-state.json --selection polar-gap092-full-tail-AZ-select.json --output polar-gap092-Z52-prepared.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-gap092-selected-tail-position-source.py" --prepared polar-gap092-Z52-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --zero --initial-damping .015 --steps 2 --prefix polar-gap092-Z52-xyz-own1
python3 -u "$S/2ecf-polar-gap092-selected-tail-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-Z52-prepared.json --state polar-gap092-Z52-xyz-own1-step01-state.json --output polar-gap092-Z52-xyz-own1-G11.json
python3 -u "$S/2ecf-polar-gap092-selected-tail-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-Z52-prepared.json --state polar-gap092-Z52-xyz-own1-step02-state.json --output polar-gap092-Z52-xyz-own2-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-gap092-selected-tail-position-source.py | dc61c1d6e154d325bc33fa072d64a313eb35efaa355b1b54e0a4a9ebca3e8cd7 |
| polar-gap092-Z52-prepared.json | b6bb99c0fe6c7a3c10b297798ba97f33b0c8a61afc5cb9ec77b357cb4c9a537a |
| polar-gap092-Z52-xyz-own1-initial.json | dd40c10bd6da67ca2a629154de525f57a6355f123c6ec7c2bcc41a334e1c028d |
| polar-gap092-Z52-xyz-own1-actual-derivative-check.json | 10b548a82a7cdbb9bb60b106e8fb9fe51cc8fe746062d1b6be33d254fd32ea9e |
| polar-gap092-Z52-xyz-own1-report.json | c2ddb7a6513f3d2ba472d4b8efeca6b659467def64d34b9a341759fcd2bc2544 |
| polar-gap092-Z52-xyz-own1-step01-state.json | cdf15e49480cdc42051822f91c24603991956a4e6d1d243f848d97f28b045f0e |
| polar-gap092-Z52-xyz-own1-G11.json | 99060fdd699faae59d582ddd82156daaf5d3c0604af8dccc6f98beb37ac0a6cb |
| polar-gap092-Z52-xyz-own1-step02-state.json | ffd7dabe897d9b424abc5124299066e7878d0be33620bb7fb78a3a1b8843521c |
| polar-gap092-Z52-xyz-own2-G11.json | 68c92df3187dab39207056bdb7f9b01824429c0ba7c885c79527d972e31fb4ad |
| polar-gap092-Z52-compose-exit.json | 96eb027c81a07274e4ab9282fc6744e98479db42e639aed791f19a0bcae08958 |
| polar-gap092-Z52-compose.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-gap092-Z52-xyz-own1-exit.json | 1f56a2859d73e24d2f060cd4cac1de09e077849840e363d4379101412de8b467 |
| polar-gap092-Z52-xyz-own1.log | 069395b9a453d441588263a982c3c7c62421981537d8de9326f02a7ef1e31b54 |
| polar-gap092-Z52-xyz-own1-G11-exit.json | 37f4e23c0fdcd7ce0d5d2d376c9c5082f639c9cbb643ad7969887c3e789bd821 |
| polar-gap092-Z52-xyz-own1-G11.log | 21c2c2411f35015a276e737a1236f2bbe3284dd2af0a94832321c6816ff8e9ee |
| polar-gap092-Z52-xyz-own2-G11-exit.json | 1e3046da18592e675928197bdb2cc43bca1f5549c3dbe75c98b985aea6908a60 |
| polar-gap092-Z52-xyz-own2-G11.log | c9cf022ae9e360614db2224995ee04341379db116ce7ec70d98eb4fb8e0f6bbc |
