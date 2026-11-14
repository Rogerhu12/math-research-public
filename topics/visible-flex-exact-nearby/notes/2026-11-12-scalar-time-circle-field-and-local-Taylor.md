# 实际时间圆场包与局部角 Taylor 表

2026-11-12，root。本次两个计算均已真正完成。

## 完整时间圆场包

`scripts/fourfold_phase_time_circle_field_package.py` 读取同一个准确 δ₅、
419 段、主 germ、负分支的 R3 与 R6 已付域。R67 的准确端点门已经
证明实际整个实时间段只在该 germ 中；R6 报告同样只列这一准确跨度。
代码逐项比较对象、根、descriptor、参数、端点、分支和物理角带，
不把较大的时间域误用到不同的径向解析输入半径。

取 $N_\theta=4096,K=1800,N_t=40,m=35,\rho=5/4,Q=1024$，320 bits。
利用实共轭对称，只计算时间圆上的21个独立节点；原始实际 primitive
及复均值误差全部保留。时间 DFT 给 $g_i=f_i+\sum_{l\ge1}f_{i+lN_t}\rho^{lN_t}$。
对两真圆 $(R_j,M_j)$，在共同物理角带 $S_o=1/64$ 上使用

$$
 |f_i|\le\min_j M_jR_j^{-i},\qquad
 |g_i-f_i|\le M_6R_6^{-i}
    \frac{(\rho/R_6)^{N_t}}{1-(\rho/R_6)^{N_t}}=:A_i.
$$

角重构用解析模界 $|f_i|+A_i$；节点和 DFT 球误差另付，最后再将
$A_i$ 的完整角 Wiener 费用加回。时间圆 alias 不是角白噪声。
完整省略时间尾取两个合法 Cauchy 界的较小值。这给同一实际全实段、
$|\operatorname{Im}\theta|\le81/10000$ 的完整安全界：

| 真实场误差 | 严格上界 |
|---|---:|
| $f-P$ | $1.239\times10^{-21}$ |
| $f_\theta-P_\theta$ | $9.063\times10^{-18}$ |
| $f_{\theta\theta}-P_{\theta\theta}$ | $6.649\times10^{-14}$ |

准确 dyadic 系数保存并全部重新读回。另与独立时间 jet 得到的旧准确
$P$ 做全部时间/Fourier 系数的有向 Wiener 差比较，三项差均小于两份
真实场误差的和。新包 CPU 26.0801s，wall 115.057s；完整报告是
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_time_circle_field.json`。
它还不是参考复合或完整返回图证书。


## 同一准确 P 的两域改进预算

新 `fourfold_saved_circle_field_multidomain_budget.py` 已对上面保存的同一 P
完成九个 time/strip 组合的有向重预算，不重新选择有限系数。它分别使用
R70 的 $(R_3,S_3)=(3,1/48)$ 与真实 $(R_6,S_6)=(6,1/64)$，并逐项核对
准确对象、根、端点和唯一主 germ。较宽角门的场模上界来自
$(|M|+\sqrt{|K|}|W|)/|D|$，对两个已固定平方根的速度符号均成立。

设 $\Pi_{N,K}$ 表示实角等间距 DFT 后只保留 $|k|\le K<N/2$。对任意
解析周期函数 $v$ 及 $j=0,1,2$，有准确系数关系

$$
 (\Pi_{N,K}v)_k=\sum_{l\in\mathbb Z}v_{k+lN},\qquad
 \|\partial_\theta^j\Pi_{N,K}v\|_{A_s}
 \le\|\partial_\theta^jv\|_{A_s}.
$$

这是因为每个所选剩余类只出现一次，而且
$|k|\le|k+lN|$，故 $|4k|^je^{4|k|s}\le|4(k+lN)|^je^{4|k+lN|s}$。
因此可把真实角重构与时间 alias 准确分开：

$$
 f_i-\Pi_{N,K}g_i=(f_i-\Pi_{N,K}f_i)-\Pi_{N,K}(g_i-f_i).
$$

第一项用较宽角域支付完整角 alias 与尾；第二项只付其在自己较窄角域
上的完整 Wiener 范数，无需、也不允许将 R6 时间 alias 转授给 R3 的
更宽角带。节点算术误差仍单列。完整时间尾可取两个合法域费用中的
较小者；没有把两个 bidisc 的外半径交叉组成一个不存在的域。

在 $|u|\le1$、物理角带 $81/10000$，同一个 P 的 $f-P$ 新上界为
$2.974\times10^{-24}$；角带 $1/256$ 与 $1/512$ 分别小于
$1.910\times10^{-24}$、$1.638\times10^{-24}$。在复时间圆所需
$|u|\le5/4$ 上，这三项分别小于
$3.924\times10^{-21}$、$2.520\times10^{-21}$、$2.161\times10^{-21}$。
零、一、二阶角导数的完整费用及各项拆分均保存在
`notes/2026-11-12-saved-circle-field-multidomain-budgets.json`。
这些新域仍只属于同一个419段，参考 Y 的像包含和完整返回继续另付。

## 原生 FFT 局部角 Taylor 表

固定复时间后，全部有限场为 $P(\theta)=\sum_{|k|\le K}a_ke^{4ik\theta}$。
令准确系数中点为 $b_k$，非均匀角中点为 $c_j$。输入球费用沿用
scalar-time-circle-and-native-composition 笔记的完整公式，全部有限模
都保留。对 $M$ 个准确实锚点 $\alpha_l=\pi l/(2M)$，用原生 DFT 形成

$$
 B_{r,l}=\sum_{|k|\le K}b_k\frac{(4ikA)^r}{r!}
                   e^{2\pi i kl/M}.
$$

形成原频率的导数后才按 $k\bmod M$ 求和，所以即使 $M<2K+1$，
这里也是准确折叠全部有限模，并没有丢模。每个点选一个锚点，使用
有向球验证 $q=\max_j|(c_j-\alpha_{l(j)})/A|<1$，再作原生标量 Horner。
浮点数只帮助选择整数锚点，不承担准确距离判定。

有限多项式在任意锚点复圆上的真模界是

$$
 M_A=\sum_{|k|\le K}|b_k|e^{4|k|A};
 \qquad |\mathrm{tail}_{r\ge m}|\le M_A q^m/(1-q).
$$

因此 Taylor 半径不受真实场解析域限制；但真实 $f-P$ 费用仍只在
已经证明的真实域上有效。这两个域没有混用。所有 DFT、表系数、
锚点距离和 Horner 算术球继续保留，再加完整输入费与 Taylor 尾。

实际运行：原 R67 的 $K=1800$ 准确 $P$，$u=1/2+i/8$；δ₅ 的准确
$H(x)/4$ 在标签带 $1/512$ 上8192个点；$M=512,A=1/64$。
自动选出34项，$q<.111802$，$M_A<1.409003$。完整有限评价误差
小于 $7.042\times10^{-33}$，其中算术半径小于 $2.161\times10^{-95}$。
CPU .3253s，wall .9391s。四个独立完整 Laurent 求和均与返回球相交。
源码和全部预算另经 reproduce_newton 逐式审阅。

该输入是实际有限 $H/4$，不是419段轨迹 $Y$；没有把8192点改称连续圆。
完整轨迹重建、复像、商 $h$、时间/标签重构余项和两腿汇总继续计算。

原 scalar 非均匀 benchmark 的 JSON 一直正确：其约 $4.38\times10^{-24}$
来自算术球，舍弃模仅约 $2.303\times10^{-43}$。旧笔记的文字误归因已在
本批改正，旧数值报告不变；新 Taylor 方法不依赖那个误归因。

复现入口（在本题目录）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_time_circle_field_package.py \
  --angles 4096 --degree 1800 --primitive-nodes 1024 --time-nodes 40 \
  --terms 35 --radius 5/4 --bits 320 \
  --polynomial-dir /tmp/visible-time-circle-field-replay \
  --out /tmp/visible-time-circle-field-replay.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_fourier_local_taylor.py --nodes 8192 --anchors 512 \
  --out /tmp/visible-angular-Taylor-replay.json
```
