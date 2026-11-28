# 同时实现整闭材料像两项强比例的实际空间变换

**已证明。** [R286](../results/R286-actual-smooth-images-enforcing-both-strong-shape-ratios.md) 对任何接 R267 与 R273/R282 双真端口的周期 C² 连接图，在保持端口开域恒等的条件下，构造两种保向空间映射。上下连接、真实中央、所有开发盘/真喉及完整固定两帽已合入同一闭材料像；其 D≤3.2、held≥.65、δE≥.1609，两强归一比例分别≥.203125、.05028125。第一种还把原七个几何行在全连接上置于允许域，并把刚体商比例提高到 .05275。第二种使用 Euclidean 三维两排球，只移动真正靠近见证中心的点。两图的整核嵌入、reach 和度量精度尚未得到此结论的保证。

## 可移植重生

W 为运行目录，S 为课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 "$S/2ecf-polar-spatial-guard-global-rational-budgets.py" --plane "$S/2ecf-polar-material-global-spatial-guard-image.py" --sphere "$S/2ecf-polar-material-spatial-guard-true-spheres.py" --output polar-spatial-guard-rational.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-material-global-spatial-guard-image.py | d56daff25b6565feafd2d9ecd6598f7d644b5e222d18500e0bcbdc47ab5663f9 |
| 2ecf-polar-material-spatial-guard-true-spheres.py | 70b4268cc7ccf9579c987a93d089310b9ef2e85644610c189b8d925764d7df5c |
| 2ecf-polar-spatial-guard-global-rational-budgets.py | ee30e54dea13676ad67d548401c87cc90858fe67f93946dd0a583613aa1be71f |
| polar-spatial-guard-rational.json | 5d4b618912a96304280d3e56d5092b6db551c3174c7a018aceb62216149c5dd3 |
| polar-spatial-guard-rational-exit.json | 42433b71fdc06f03fa19cc30188bd77fda4fc004ec0a941da5a26a82c7293fb0 |
| polar-spatial-guard-rational.log | 290c7fe041a8280b6f8846ef328dee3678a7413ab188e35a485f152e191c4487 |
