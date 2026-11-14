# 完整 Gauss 点 Codazzi 有限离散的实际接口检查

状态：**实现检查，非解、非连续证书。**
根代理实现 `scripts/fd2d_gc_gauss_cell_codazzi.py::gauss_cell_codazzi`；
本代理只实现独立实际输入检查
`scripts/fd2d-metric-gauss-cell-codazzi-check.py` 及其流式版本
`scripts/fd2d-metric-gauss-cell-codazzi-stream-check.py`，未修改该 helper 或原 provider。

## 1. 输入与检查范围

使用已经关闭的 joint02 第 20 个 accepted 实体：
`notes/2026-11-12-fd2d-raw-bump-joint02-accepted-0020.npz`，
SHA `2bf2d98aaa6c57752a78aeabf96a4d5541528c998b669b59fc139556203f1a22`。
其原有限失败状态保留，本件不重新求解，也不积分实际 body。
物理参数、99 个实际节点、plateau seed、完整尾 lifting 和原角图册都不变。

新的两点 Gauss 规则只改变径向有限求积：

- `retained_residual` 是原前 $(N-1)d$ 条 Codazzi 行的新求积版本；
- `high_residual` 是同一 Gauss 平均的完整角补余；
- 原节点 Gauss、边界和 gap 行仍由原 provider 计算；
- 原节点/梯形 $F$ 单独保存，未被新残差覆盖或改名为已通过。

全部矩阵对原始独立节点字段及实际参数求导；中央边界消元由 caller 另组合。
检查器没有为了降低内存再构造一份原完整稀疏 Jacobian，只比较原 $F$ 和原场。

## 2. 三类非零方向和独立 P1 函数比较

实际检查覆盖独立 $(n,m,l)$ 节点、完整尾参数、物理 $\delta$ 三类方向。
每类分别检查 retained 与 high 两块，共六个应非零的导数。
使用中央差分步长 $4\cdot10^{-6}$ 和 $10^{-6}$；报告同时保存绝对误差、
除以 $\max(1,\|Jd\|_2)$ 的 scaled 误差，以及真正的相对误差，避免混用。

另外由独立 `RawBumpSeedNativeField` 在相同两点 Gauss 位置求
实际 P1 斜率和完整 lifting jets，再直接计算 $G,R_n,R_m$。
将其 $R_n,R_m$ 平均与 helper 的 `full_codazzi_cells` 比较；
将其 $G$ 与 helper 的 `point_gauss` 比较。
这条路径没有把 solver RHS 替代插值的真实径向导数。

还检查：完整平均投影恰好重现 retained 行，完整平均等于 retained 函数加
omitted 函数，原 $F$/场/mesh/chart 调用前后不变，所有源字节在运行期间不变。

## 3. 有限规则的解释

新旧残差的差是本次有意修改径向有限离散的结果，不表示改变了实际物理度量。
两个 Gauss 点还不是连续积分，节点 between-point 的 residual 也未被证成零。
真正的新求解、真实同 $g$ 加密、实际位置图和连续后验须另有各自结果。

## 4. 首次执行中断与等值流式消费

第一次实际执行 **45122 / a5f706 返回 137**，没有完整报告。
工具只报告退出状态，没有系统终止原因；不将其推断为数学失败。
helper 和 checker 原源分别保存于 `repro/fd2d-metric-gauss-cell-check01/`，
真实失败回执为 `...metric-gauss-cell-codazzi-check-01-failure.json`。

随后另名 stream checker 保持 helper、输入、规则、所有测试方向及容差不变，
只把独立原生点值比较分成每批 8 个原径向格，并加入阶段/RSS记录。
这样不用一次展开整张 Gauss 点的 seed 角函数数组；每个实际点仍全部消费。
该修改不删检查点，不变有限方程，也不修改 source field。

## 5. 流式实际执行成功

**75977 / 77b248 实际退出 0，76.262 秒，峰 RSS 366380 KiB。**
helper 源保持
`6be627488b06bfd6f5dd3f4f291432ccff326463b1af1fcf134e5179d08dc03f`，没有修源。

| 非零实际方向 | retained 真相对 $L^2$ 误差 | high 真相对 $L^2$ 误差 |
|---|---:|---:|
| 独立 $(n,m,l)$ 节点 | $1.416\cdot10^{-9}$ | $7.245\cdot10^{-9}$ |
| 完整尾参数 | $1.033\cdot10^{-9}$ | $8.415\cdot10^{-9}$ |
| 物理 $\delta$ | $3.588\cdot10^{-10}$ | $1.114\cdot10^{-8}$ |

上表步长为 $10^{-6}$。六块导数均实际非零。
独立 native 真 P1 残差的 Gauss 平均相差至多 $4.069\cdot10^{-14}$；
内部 $G$ 相差至多 $3.376\cdot10^{-14}$。
完整平均投影与 retained 差 $4.112\cdot10^{-14}$，
完整平均减 retained/omitted 重构差 $4.835\cdot10^{-14}$。
原节点 $F$、独立三场、未知 mesh 和原图册数组变化都逐位为零。

原梯形 retained 与新 Gauss retained 的最大差为 `.3046165394`，
表明这里确实采用了新的有限求积，未把旧行换名。
新矩阵为 retained $3038\times4691$（155846 非零）和 high
$50176\times4691$（2381260 非零）。这些数不是新解的收敛值。

复现应使用流式入口：

```bash
python3 scripts/fd2d-metric-gauss-cell-codazzi-stream-check.py \
  --field notes/2026-11-12-fd2d-raw-bump-joint02-accepted-0020.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --out notes/<fresh-check>.json
```

这项实现检查已经足够支撑新 driver 接入；不为同一失败状态再增加 body 或重复求解门。

