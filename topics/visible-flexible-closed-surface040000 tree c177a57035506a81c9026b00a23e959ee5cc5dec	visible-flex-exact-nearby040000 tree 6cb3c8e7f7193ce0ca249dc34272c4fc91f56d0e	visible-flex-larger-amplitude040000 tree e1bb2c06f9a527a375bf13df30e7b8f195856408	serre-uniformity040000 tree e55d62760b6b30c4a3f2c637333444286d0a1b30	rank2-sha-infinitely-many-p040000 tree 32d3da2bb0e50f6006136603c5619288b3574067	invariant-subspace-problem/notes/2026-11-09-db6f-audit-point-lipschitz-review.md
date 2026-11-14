# 单点背景修包的独立审查

审查者：`/root/independent_geometry`，2026-11-09。未参与前缀或尾的数值优化。

结论：**所冻结引理、实现及本次 736 行重放 PASS。** 此结论只改进同一冻结背景的值区间表示，不宣称完整 metric 误差下降，更不支付 G5。

## 1. 被审对象

全文审读 `2026-11-09-db6f-tail-background-point-lipschitz.md`，SHA256 为 `074b8a146559b8cddd29ebf2196fffd69a81c43a5a44b3279f99675d3a63d81e`；逐行审读 `db6f-tail-background-point-lipschitz.py`，SHA256 为 `ccd59bc42f6685e38229b5425e52c18d08437a43ddbd5073e55e93561a6a0bef`。

依赖是已经独审的完整 depth4 primitive、stable source、精确径向网格定义和背景导数界。它们仍然是证明输入；本审查没有把数值近似 inverse 当成精确反解。原 raw2 包与新包的背景定义、manifest、primitive 和数据 hash 均已绑定。

## 2. 证明核查

任意合法 source 点的严格半径包为 $R_*=[r_-,r_+]$，斜率包为 $W_*$。对于待证的精确物理区间 $J=[a,b]$，矩形上 $|r-s|$ 的最大值由四个角点取得。因此

$$
d=\max_{r\in\{a,b\},\ s\in\{r_-,r_+\}}|r-s|
$$

控制真实选点到整个区间的距离。在连接线段上有 $|w_r|\le K$ 时，$W_*+[-Kd,Kd]$ 包含整个 $w(J)$。只要求连续且分片 $C^1$，不要求跨 source、cap 或绝对值界面的高阶光滑性。

内侧 $K=601/100$ 的选择同时检查 $J$ 和真实选点半径包的右端都不超过已证 raw0 内端下界；由此覆盖完整连接线段。审查器以 Fraction 独立核查

$$
36(1+49^{-2})^3 < (601/100)^2.
$$

外侧用已审全域界 $K=24$。当前所有选点及待证盒都位于正的 cuff 半径之外，连接只穿过有限段，逐段微积分基本定理足够。

## 3. 独立重放和有理数包含检查

按原稿命令重跑到 `2026-11-09-db6f-audit-raw2-point-replay.json/.npz`，进程实际退出码为 0。随后运行独立脚本 `db6f-audit-point-lipschitz-check.py`，完整结果为同名日期前缀 JSON。

检查结果如下：

- 736 行所有输出数组与作者输出逐项相同。
- 正好四个 $w$ 行改变；其余 $w$ 行、全部 $w_r$ 系数与余项、半径分割、source 及 radial-residual 辅助列均逐位未变。
- 对四个改动行，重新取对应 primitive 点值与 stable source 点值，独立以 Fraction 计算四角最大距离，核查新常数区间确实包含 $[w_- -Kd,w_+ +Kd]$。
- 每个新多项式的高次系数精确为零，余项精确为零；新常数区间本身支付整个物理小盒，而不是仅支付选点。
- 内侧连接阈值和导数有理常数逐项核验通过。

输出中原 producer 的未达工作容差计数没有被冒充为新的完整判断。`unmet_tolerance_rows=null` 与单独记录的剩余 $w$ 工作宽度语义正确。

## 4. 六个原宽盒的 M12 uniform 误差预算

这一步使用已经完成的 **M12 uniform 有限图**高度导数界；不挪用于两个 adaptive 有限图。对于新包每个盒，以精确物理端点选择全部相交的 M12 区间。旧报告的浮点端点先向外扩一 ulp，因此只会多选，不会漏掉实际重叠。

取

$$
\delta w = \mathrm{remainder}+\frac12\sum_k(\mathrm{hi}_k-\mathrm{lo}_k),
\qquad
W=2\|Z_r\|+\|Z_\theta\|/r_{\min}.
$$

由已审度量公式，背景区间宽度对相对算子界的可分离预算不超过 $\delta w\,W$。六个原未达工作宽度盒的新预算最大为 $8.791420072086598\cdot10^{-12}$，全部严格小于 $2\cdot10^{-10}$。因此原 span 3129 与 3246 的两个小宽盒，在这一 uniform 背景精度预算下无需再细分。

这是一个充分误差预算，既不是实际残差下界，也不是完整 metric 认证。完整残差仍包含有限曲面系数、目标中心多项式与区间算术；它需要 metric-only 或完整后端实际运行。对于同一 manifest，既有曲率证书可作为单独证明输入保留，但必须单独绑定其背景包与运行记录。

## 5. 重放命令

```bash
python scripts/db6f-tail-background-point-lipschitz.py \
  --packet notes/2026-11-09-db6f-tail-background-lowmetric-raw2.json \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --primitive notes/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out-prefix notes/2026-11-09-db6f-audit-raw2-point-replay \
  --minimum-width 1e-6
python scripts/db6f-audit-point-lipschitz-check.py
```
