# 固定 cuff 的真实 tail 长度约束与 cut .4 的严格粗界

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

**状态。** 第 1 节为任意实际等距尾的必要条件。第 2–4 节为指定正径向背景构造的解析粗界，使用已有无限深 source 的校准括号，不使用有限 quadrature 值作为严格上界。此文不证明当前候选的非线性尾存在，不证明新目标的精确 warp 归一化为正，也不证明完整强活动核。

## 1. 必须由实际材料路径支付的高度与 Fourier 约束

设目标 tail 度量为

$$g=ds^2+a(s)^2du^2,\qquad s_c\le s\le s_f,\quad
L_{tail}=s_f-s_c,$$

且实际 C¹ 图 F 在 cuff 满足 $F_z(s_f,u)=Z$，其中 Z 与 u 无关。若 F 对 g 准确等距，则每条固定材料 u 的路径长均为 $L_{tail}$。由欧氏距离不大于路径长度，

$$|F(s_c,u)-F(s_f,u)|\le L_{tail},\qquad
\boxed{|H_{cut}(u)-Z|\le L_{tail}.} \tag{1}$$

这不要求该路径在实际空间中是直线或测地线，也不要求其高度单调。
若只知道实际拉回度量 h 满足二次型意义的 $h\le(1+\epsilon)g$，则同样积分给

$$|H_{cut}(u)-Z|\le\sqrt{1+\epsilon}\,L_{tail}. \tag{2}$$

对正整数 k，以真实材料角定义实 cosine 系数

$$h_k=\frac1\pi\int_0^{2\pi}H_{cut}(u)\cos(ku)\,du.$$

常数 Z 的系数为零；由 $\int_0^{2\pi}|\cos(ku)|du=4$，

$$\boxed{|h_k|\le\frac4\pi L_{tail}} \tag{3}$$

在 (2) 的近似度量条件下右边乘 $\sqrt{1+\epsilon}$。同一结论适用于 sine 系数及任意固定相位的实 harmonic 系数。若使用复 Fourier 的 $1/(2\pi)$ 归一化，数值常数必须相应改变，不能混用。
非线性计算角 φ 或随 s 改变的 chart 不是这里的材料 u；转换后才可应用 (3)。

如果 cuff 的完整材料对应点已固定，(1) 还给出真实 cut 空间曲线到其对应 cuff 圆点的同一距离界。这可作为实际几何筛选条件，但此文没有将任何尚未闭合的 BVP 状态当作满足 cuff 对应关系的曲面。

## 2. 当前目标的原始有限值及其作用范围

输入为 `2026-11-12-fd2d-ellipse-cuff032-cut04-config.json`，
实际定义入口为 `scripts/closing_weighted_tail.mjs` / `closing_recalibrated_tail.mjs`。
关键参数为 cut=.4、cuff=.32、wCut=.1、width=.08、K=7、protectCell=160、
δ0=.006、c0=.05、source 指数 11/4、R=64；cell 0 的 cap levels 为
$.004,.08,.02,.004,.004$，其余 finite cell 的 cap 为 .004。
最外两个 source 段 j=7,8 使用 cut-preserving 恢复，positive warp 权重不改变 w 的值。

原端口数值报告 `2026-11-12-fd2d-ellipse-cuff032-cut04-port.json` 给

$$L_{tail}\simeq .08005605867123879,\qquad
4L_{tail}/\pi\simeq .10193053969585955.$$

这些是有限 quadrature 数值，未以其最后显示位声称严格上界。下面重新给一个略宽、但不依赖该 quadrature 的解析界。

## 3. 全 source 的 slope 严格粗界

### 3.1 capped 段

程序的 cap 以 $c=\log C$、$t\in[0,1]$ 给出
$\log w_{new}=c-L+2L I(t)$。其中
$J(t)=\int_0^t S_7(x)dx\ge0$，$S_7$ 是单调的七次 smoothstep，

$$I(t)=\begin{cases}t-J(t),&t\le1/2,\\1/2-J(1-t),&t\ge1/2.\end{cases}$$

因此 $I\le1/2$，整个 cap 满足 $w_{new}\le C$。端部恒等/常值区也满足此不等式。变化的 local cap 是相邻 cap levels 的几何插值，故不超过两者较大值。
于是除 j=7,8 的 cut 恢复以外，所有有限被改段均有 $w\le.081$；这里用 .081 为所有输入 binary cap 留出严格余量。

### 3.2 恢复 cut 两 jet 的两个段

设 $w_c$ 为实际 wCut，$C$ 为末端 cap=.004，$d=\delta_0$、$c_0=\eta_0/d$。
source 的最外 port j=8 长度为 $c_0d/\sqrt{12}$（log-radius 坐标），且在 source cut 为 $w_c$。
因此整个 j=8 有

$$w\le w_c\exp\left(\frac{7c_0d}{\sqrt{12}}\right). \tag{4}$$

对前一 transition j=7，令 $t=S_5(x)\in[0,1]$。source 的两个 log-P 端值为 0 与
$\log d+(11/4)\log2$。故其原始 slope 满足

$$\log w_{raw}\le\log w_c+(1-t)B+e,
\quad B=\log\frac1{d2^{11/4}},\quad
e=\frac{14c_0d}{\sqrt{12}}.$$ 

cut-preserving 程序准确采用
$\log w=(1-t)\log w_{capped}+t\log w_{raw}$。
由于此段 local cap 的两个端值都等于 C，且

$$d2^{11/4}>C/w_c,$$

即 $B<\log(w_c/C)=A$，因此

$$\begin{aligned}
\log w&\le(1-t)\log C+t\{\log w_c+(1-t)B+e\}\\
&=\log w_c+(1-t)(tB-A)+te
\le\log w_c+e.
\end{aligned}$$

这里 $B>0$；若 B 非正，最后不等式同样成立。所需 $d2^{11/4}>C/w_c$ 可不用 transcendental 计算验证：对正数两边四次方，比较
$2^{11}(dw_c/C)^4>1$ 即可。准确十进制情形该左边为 1.0368；脚本实际比较输入 binary rationals，仍严格大于 1。
合并 (4)，整个 cut 恢复满足

$$w\le w_c e^{14c_0d/\sqrt{12}}<.100122. \tag{5}$$

最后一个有理粗比较使用 $\sqrt{12}>433/125$、$e^x\le1/(1-x)$（$0\le x<1$），脚本给出完整分子/分母。valleyControls 只作用于 j=3,4,5，所以不会改变本节 raw 计算。

### 3.3 无限未改深 source

沿用 [R15 §2.2](../results/R15-weighted-inner-background-and-collar-bounds.md) 已用的准确深校准括号 $\alpha_n\in[1/2,2]$（$n\ge80$）。选根只依赖 δn、cn、R 及 source 指数，不依赖 cuff 半径或 wCut。
具体 source 及其原证明参数见 [N160 背景证明](2026-11-09-closing-deep-background-n160.md) 和 [半径缩放证明](2026-11-09-closing-deep-radius-family.md)。

本题 $d\in[1/200,1/160]$、$c_0\in[1/25,1/16]$、$w_c\le1/2$，所以同一 raw 估计仍给

$$0<w\le1280\,2^{-7n/4},\qquad n\ge160. \tag{6}$$

为明确没有误用旧 cuff 的常数：原归一化为
$\varepsilon_{src}=w_c(r_f e^{Y/\sqrt{12}})^7/(2d)^{11/4}$，
raw slope 是 $\varepsilon_{src}\delta_n^{7/4}p/r^7$。
校准括号给全部平台 $p\le64$；$r\ge r_f$，所以 r_f 的七次方准确约去。
$Y<1/20$、$e^{7Y/\sqrt{12}}<6/5$、$2^{11/4}>6$ 和上述 d 下界直接给 (6)。
新 wCut=.1 只进一步减小这个上界。因此无限深部的 w 远小于 .004，也被 (5) 覆盖。
这里没有把 R15 的 K=6 或原 finite cap 数值直接移植到新 K=7 目标；仅使用其同一深源校准括号并重算 raw slope 上界。

## 4. 严格长度和材料实系数上界

对这个背景构造的任意正精确 warp 归一化，r 严格单调从 cuff 到 cut，目标经线长度为

$$L_{tail}=\int_{r_f}^{r_c}\sqrt{1+w(r)^2}\,dr.$$

因此上面的全 source bound 给

$$L_{tail}<(r_c-r_f)\sqrt{1+.100122^2}<\boxed{.0804}. \tag{7}$$

脚本按 assembler 的实际 binary64 endpoint 约定取 $r_f=r_c-\texttt{width}$，以准确分数验证
$r_c-r_f\le.0800000000000001$ 及 (7) 的平方不等式。故这里没有将 binary .4−.32 强行视为准确 .08。

结合 (3)，准确等距真实尾必满足

$$\boxed{|h_k|<.102369\quad(k\ge1).} \tag{8}$$

近似 metric 则 (7)–(8) 的右边乘 $\sqrt{1+\epsilon}$。
π 下界用 Machin 恒等式及 atan 交错级数的准确有理截断，粗比较足以给 .102369。

复现：

```sh
python scripts/fd2d_tail_length_rational.py --out notes/tail-length-rational-reproduction.json
```

实际报告为 `2026-11-12-fd2d-tail-length-rational-01.json`。`passed=true` 只说明以上有理比较成立；报告明确保留 `warp_normalization_certified=false`、`nonlinear_tail_certified=false` 和 `full_core_geometry_certified=false`。这不是新增独审或冻结门，而是所证命题本身的准确作用范围。

## 5. 对大幅 branch 的正确使用

p148 的单位中央 f0 线性高度 gain 为 $.32859844773793095$。简单乘以约 $.455$ 得 $.14951229372075858$，超过当前尾的 (8)。这说明把该一阶轨道一直线性外推到那一大幅度不符合真实 tail 的必要条件。
它不排除非线性 continuation：真实分支可弯离一阶切线，且全部非线性模态、均值和中央幅度关系都会改变。尚未得到的真实尾不能因这项比较被宣告不存在。
若后续选择更宽径向尾，例如保持 cuff=.32 而 cut 改为 .45 或 .50，必须另名定义完整物理 g 和新的真实 tail/DN；旧 .4 cut 的端口不自动沿用。
