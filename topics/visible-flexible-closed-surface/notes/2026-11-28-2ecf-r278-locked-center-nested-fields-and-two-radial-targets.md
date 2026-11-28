# R278 双锁实际中央的固定目标加密与双径向目标实验

[R278](../results/R278-R262-true-convex-central-support-and-noncircular-width-continuation.md) 的 η=1/256 双锁状态同时固定方向支撑差和半宽差。第一、二行沿用其整个中央支撑函数和动量场的实际两端。第三、四行把 Minkowski 幅度升到 η=1/32，自由支撑系数取原 η=1/256 向量的 1/2，因此保存新的中央形状；两个方向约束仍由每个基向量严格满足。两个大幅状态使用同一中央。

| η、目标及空间 | 接受步 | 第一观察峰 | 独立移位峰 | 移位最大绝对主曲率 |
|---|---:|---:|---:|---:|
| 1/256，原 R262 度量，48 段、整角至 21 | 2 个纯位置 | .000228872464 | .000228865009 | 6.181515 |
| 1/256，双径向目标，24 段、整角至 15 | 1 个位置与度量联合步 | .000234514574 | .000234527322 | 6.303089 |
| 1/32，双径向目标，径速初始正偏 | 13 个联合步 | .002100162171 | .002093912074 | 7.184482 |
| 1/32，双径向目标，径速初始负偏 | 14 个联合步 | .002119266368 | .002115066280 | 7.382911 |

原目标实验用 Boehm 插结嵌入前一完整 XYZ 系数，仅释放位置，前一场独立移位峰为 .00023502612。两组新观察的径角节点数分别为 347×258、335×287。其余三次在同一 12 段两端平二阶的五次基内设置独立对数径速与对数角半径，即 $e^{2A(s)}ds^2+r(s)^2e^{2B(s)}du^2$。每个联合终点分别冻结，后续纯位置搜索中接受数均为零。三组用 284×241 和 270×257 观察，后两行移位网格的 $(\|A\|_\infty,\|B\|_\infty)$ 分别约为 (.374957,.068883)、(.408464,.065487)。原双锁端口的 R278 连续凸性可直接用于前两行。大幅端口的连续凸性、全闭嵌入及强指标仍待证明。

第一次从 η=1/256 升到 1/32 时同时将所有自由支撑系数乘 8。两个径速偏置在中央物理反演前同样触发选定的采样曲率半径下限 .02，未产生可用状态。改取系数因子 .5 后才产生表中两个大幅状态。该门限是本次有限求值器的选取。

使用原 [R278 源再生说明](2026-11-28-2ecf-r262-noncircular-minkowski-true-central-and-bulk-steps.md) 的 `S`、`W`、`a`、单线程环境及双锁父文件执行下列 Bash。

```bash
p="$W/g12-mink-width-eta1over256.json"
python "$S/2ecf-r262-fixed-actual-central-shape-refine.py" "${a[@]}" --parent "$p" --steps 2 --output "$W/g12-mink-width-eta1over256-frozen48.json"
python "$S/2ecf-r262-two-radial-targets-full-shape.py" "${a[@]}" --parent "$p" --output "$W/g12-mink-new-g-width-eta1over256.json"
for n in 1 -1; do
  if test "$n" = 1; then b=.02; k=13; else b=-.02; k=14; fi
  python "$S/2ecf-r262-two-radial-targets-admissible-support.py" "${a[@]}" --parent "$p" --eta .03125 --support-scale .5 --radial-bias "$b" --steps "$k" --output "$W/g12-mink-new-g-admissible-eta1over32-bias$n.json"
done
```

| 源码或完整产物 | SHA-256 |
|---|---|
| `2ecf-r262-fixed-actual-central-shape-refine.py` | `0dc2dd443287d07707c3c072cb1cfbcffc60646cb2beabdf23e906da8556a2b0` |
| `2ecf-r262-two-radial-targets-full-shape.py` | `4e60fe83e62ab3b025c0592f4244ce2e76ae9f311e664d37ea8cb7c3cc341009` |
| `2ecf-r262-two-radial-targets-admissible-support.py` | `53381f8c268aee79b7fedc69dc5e3befb7afe5a7dd14d3dbd8cd18763dfa4e3f` |
| `g12-mink-width-eta1over256-frozen48.json` | `08099249d5f21e637778e70aa6c1ed5fc547fdee9d96388c6ad0e9b46f220b84` |
| `g12-mink-new-g-width-eta1over256.json` | `4ff4a78cbd62e1d25ec2cddf2b1a71a93ed6196abcb8893490e4f3ee7100ccb6` |
| `g12-mink-new-g-admissible-eta1over32-bias1.json` | `e20ea1d9edea4ca4f0489c40d87ec738ecf973c11fdd194555b07e0500b668fe` |
| `g12-mink-new-g-admissible-eta1over32-bias-1.json` | `9ec7a49c725396cf1084fc9fd7c71b4d6d376371a5c801a9d719b1bf3b5ac500` |
