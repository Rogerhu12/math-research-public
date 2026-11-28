# 真实新帽 432 场的整闭直径与两项强形变

**已证明。** [R296](../results/R296-actual-432-higher-cap-strong-distances-and-sharper-diameter.md) 用 24,969,217 个真闭盒覆盖新 432 场的全部位置、两真实出口与新开平环，给 |y|<.889603、|P|<1.580408、对两见证距离>.652115。将 R293 两顶实际平移凸帽的球包收至 1.5822，真实喉及 R267 原中央均容于此球。故整闭材料像 D≤3.1644、δheld/D>.20607856、δE/D>.05255245。全核高度还满足 R293 给半径 .096 gluing 所需的额外限制。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-exact-full-shape-enclosure.py" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --correction polar-released40-genuine-floor-R293.json --quarter-cells 3072 --depth 4 --output polar-raised-065-newcap-continuous-shape.json
python3 -u "$S/2ecf-polar-released-432-complete-geometric-certificates.py" --mode shape --field polar-released-cut-flat40-enriched.npz --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --cap-source "$S/2ecf-higher-bottom-cap-exact-budget.py" --prefix polar-gap092-entire-prefix-reach.json --output polar-R293-432-final-shape.json --shape polar-raised-065-newcap-continuous-shape.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-432-complete-geometric-certificates.py | cbf0edde2ce3b74b6b189d830afeff3ea51cbeb70c11daecc03d5a8160d4e82b |
| polar-raised-065-newcap-continuous-shape.json | d3f07841f9e0944655887894a1f67d83d89fd6930c0ea49b48921a6d8878eeb3 |
| polar-R293-432-final-shape.json | 69418b3f93fe2826036cb630a6f1d1a6806840f3a1ec43e5ac26ac396247aa49 |
| polar-raised-065-newcap-continuous-shape-exit.json | 6f8ea67c6a05fe82979590b6abde55ecab932a08785ddf9a465182ed87da147e |
| polar-raised-065-newcap-continuous-shape.log | a3614a413935d9366c2a8d127d1580fd341e1f3b13a13d1d983c2b9a3b3eeb31 |
| polar-R293-432-final-shape-exit.json | 7aea9d213b13aa18b3e9d58f75292363122efab73cfa67eb52865580cf540045 |
| polar-R293-432-final-shape.log | 3c908d71a4b2007d35daabbd4f4fabe59ab6a4ed582255509b7d4f3ccfd56924 |
