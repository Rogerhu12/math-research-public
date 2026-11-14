# 独立审查：N160 深背景在 cuff 半径变化下的缩放

2026-11-09，Astra-visible-flex-950f9f73 / independent_audit。
审查者未参与候选背景或权重优化。

**结论：PASS，限于未改的旋转深背景 $n\ge160$。**
前会话的 `2026-11-09-closing-deep-radius-family.md` 可按其原范围采用。
本次不是新的闭曲面构造，也不支付非旋转尾或有限 warp 的条件。

## 原陈述与实际构造的一致性

已审 R8 固定 $r_c=1/4$。新 weighted 候选固定
$r_{\rm cut}=3/5$、`orientation=1`、`width=9/20`，因而
$r_c=3/20$，不能直接保留 R8 的母线曲率 $1/50$ 常数。

实际 `closing_recalibrated_tail.mjs` 定义

$$r_{\rm old,cut}=r_c\exp(Y/\sqrt{12}),\qquad
\epsilon=\frac{w_{\rm cut}r_{\rm old,cut}^{7}}{(2\delta_0)^{11/4}}.$$

在 $w_{\rm cut}=1/2,\delta_0=3/500,R=64,a=11/4$ 和原过渡长度均不变时，
$Y$ 不依赖 $r_c$。因此 $\epsilon$ 精确按 $r_c^7$ 缩放，而原始源的
$r$ 按 $r_c$ 缩放；$w$ 及其对 cell 坐标的导数不变，$w_r$ 按
$r_c^{-1}$ 缩放。这也直接证明了所用的 $W_n$ 与 $r_c$ 无关，
$B_n$ 和圆周曲率上界均按 $r_c^{-1}$ 缩放，剩余径宽及高度界按
$r_c$ 缩放。

`closing_weighted_tail.mjs` 只重分配有限的 $n<160$ 块，而且其端口
权重固定为 1。它没有改变所引用的 $n\ge160$ 原始源；这保证缩放的
对象确实是候选将要接入的深背景。这里没有把有限块与深背景接缝的
数值误差当作已经认证为零。

## 独立有理复算

`scripts/950f-audit-deep-radius.py` 不导入构造脚本或前会话的证书程序，
从 R8 的符号主界重新用 `Fraction` 计算。它逐项与保存的候选分数
输出核对，全部相等。审查对象的 SHA256 保存在 JSON 中。

在 $n=160$，

$$W_{160}<\frac{80000}{81}\,2^{-280},\qquad
\eta_{160}=\frac3{10000}\,2^{-240},$$

$$B_{160}<
\frac72 W_{160}\frac{15}{8}\frac{241}{r_c\eta_{160}}
+\frac{7W_{160}}{r_c}.$$

代入 $r_c=3/20$ 得上界的浮点显示值约 $0.031570320204$，精确有理
比较证明它小于 $1/30$。R8 的单调包络比值仍小于 1，故同一个界
覆盖所有 $n\ge160$。其余结论为

$$|\kappa_\theta|<10^{-79},\qquad
\text{剩余高度}<10^{-131},\qquad w,w_r\longrightarrow0.$$

因而该旋转背景仍然 $C^2$ 接上半径 $3/20$ 的平圆盘。
对原候选表中的全部五个半径也独立复算通过；在
$1/10\le r_c\le7/20$ 上统一有 $|\kappa_{\rm mer}|<1/20$。

复现命令（输出路径须新建，不覆盖旧审查）：

```bash
python scripts/950f-audit-deep-radius.py --out notes/2026-11-09-950f-audit-deep-radius.json
```

## 尚未支付的条件

本结论没有证明有限浅层 warp 的连续曲率界、非轴对称高度的全频
非线性无限延拓、Cartesian 二阶接缝、全曲面的嵌入性或 reach。
它只能替换这些后续步骤中使用的**旋转深背景**常数。
