# R149 BW：由完整 alpha 得到首次 signed target w 载体

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**已证明的首次载体与完整误差公式；尚未执行新数值。**
原 [NWA](R133-supplement-actual-cohomological-normalizer-windows-and-global-sign-correction.md)
的成功 source `fourfold_codazzi_cohomological_normalizer_windows_sign.py`
由完整导数球形成 series norm budgets、两个窗口及 affine 常数，并未
形成 signed $w_n$。这里不重跑 NWA 或原 cohomological solve，而从
整个 [ASR](R149-supplement-original-alpha-full-source192-and-ended-first-attempt.md)
成功结果及其原 signed witnesses 得到尚缺的目标系数载体。

## BW1. 同一个 w，两个真实 reflection phases

保持 [WBN.1--7](R133-supplement-exact-two-sided-reflected-waist-first-coefficient-normalization.md)
的同一个 selected member、真实 $\mathcal H$、归一测度和频率 $4n$。

$$
 a=2\mathcal H(0),\quad b=a+\Omega,\quad
 c_i=-\mu/2+v_i,\quad
 \alpha=v_i-w,\quad
 R_b\alpha=-\alpha,\quad R_aw=-w.
 \tag{BW.1}
$$

三个非均值函数的常数均为零；两 physical means 与 first-coefficient
mean $-\mu/2$ 保持原有独立地位。$w$ 是
[WBP](R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md)
中的 target coefficient，目标是 $\mathcal B=Id+\mathcal T_wI$。
它既不是 source $\alpha$，也不是另一个 individual principal coefficient。
本条没有重新设置 $a,b$、重选 $\Omega$ 或改变原 cohomology。

ASR 整 actual 给同一 exact-dyadic $\widehat\alpha$、两个完整误差
$e_{\alpha,\infty},e_{\alpha,2}$、四个完整 $e_q^H$、整个 $T_\sigma$、
$E_H,G_1,m>0$，以及完整 raw192/grid/alpha witnesses 的原 SHA。
所有这些量只读，不重算任何一个已完成的 ASR norm/error 目标。

## BW2. 原积分恢复一次，保全部两符号和真正均值

从原完整 ASR input closure，按原 runtime 只恢复必要有限载体。
调用原 OT 的 `restore_AS` 路径时，其原 2048 次 `WholeQuadrature.next`
可增加只读记录包装：调用原 `next` 一次，将返回的完整复球以原
90-digit 格式写到 private 文件，然后**原样返回同一球**。不改变
任何算术、相位、mean 或返回值；完成后仍核整个原 raw、grid 和
alpha SHA。包装不调用旧 source/error/tail/cohomology targets。
其全部2048个自然积分球在原 alpha carrier 的同一次必要恢复中
取得，不需要再跑第二遍 quadrature。

原 AS.5 的同一换元等式是

$$
 (v_i)_n=\frac1\ell\int_0^\ell
 t(y)e^{-4in\mathcal H(y)}\,dy,\qquad n\ne0,
 \quad t=V_++\chi_\perp/\sqrt{r_*}-\mu/2.
 \tag{BW.2}
$$

raw 常数在积分前保留；不能因为新 trial 的零频为零而预先删除它。
令 $z_n$ 是已恢复的原完整 directed quadrature 球，取 exact-dyadic
midpoint $\widehat v_n$，负频取 exact conjugate，$\widehat v_0=0$。
固定 $K=2048,L=8192,\sigma=1/128$；不为试不同 K 重做已成模式。

## BW3. 首次 vi trial 的完整 head 与 tail

用 ASR 已保存的完整原 inputs，令

$$
 s_n=\min_{0\le q\le3}\frac{e_q^H}{(4n)^q},\qquad
 A_n=\frac{2T_\sigma e^{4nG_1\sigma}e^{-4\sigma L}}
                         {1-e^{-4\sigma L}},\qquad
 M_n=4nE_HT_\sigma e^{-4nm\sigma}.
 \tag{BW.3}
$$

AS 的 contour、完整 alias 几何级数和四列 source argument 原样适用。
因此新的完整 $v_i$ coefficient 误差为

$$
 d_n\ge\sup_{z\in z_n}|z-\widehat v_n|+s_n+A_n+M_n,
 \qquad |(v_i)_n-\widehat v_n|\le d_n.
 \tag{BW.4}
$$

这里没有除以 cohomological divisor，也不计算旧 alpha coefficient
error；对象是首次 $v_i$ finite trial error。所有2048个完整 records
先保存、读回，才进入新的 head 累加器。

令 $q=e^{-4m\sigma}<1$。解析部分的全 $|n|>K$ Wiener tail 为
$2T_\sigma q^{K+1}/(1-q)$。真实 source error 的第三导数已由整个
$e_3^H$ 支付；对其全部两符号，Cauchy--Schwarz 和
$\sum_{n>K}n^{-6}\le1/(5K^5)$ 给

$$
 V_{an}=\frac{2T_\sigma q^{K+1}}{1-q},\quad
 V_\infty=V_{an}+\frac{e_3^H}{64}\sqrt{\frac2{5K^5}},\quad
 V_2=V_{an}+\frac{e_3^H}{[4(K+1)]^3}.
 \tag{BW.5}
$$

中间 source error 实际为 $P U_{\mathcal H^{-1}}(t-\widehat t)$；
$P$ 在 $L^2$ 是收缩且与导数交换，所以同一原四列仍合法。这里
没有为真实误差假设 analytic，也没有把丢失的 Fourier 尾设为零。

head 与 tail Fourier 支集正交，因此

$$
 e_{v,\infty}=2\sum_{n=1}^K d_n+V_\infty,\qquad
 e_{v,2}=\sqrt{2\sum_{n=1}^K d_n^2+V_2^2}
 \tag{BW.6}
$$

分别为整个 $v_i-\widehat v$ 的 $L^\infty$ 与 $L^2$ bound。

## BW4. exact signed w trial 与两个完整误差

先恢复并核原整个 $\widehat\alpha$ carrier，再定义

$$
 \widehat w_n=\widehat v_n-\widehat\alpha_n\quad(1\le n\le K),
 \quad \widehat w_{-n}=\overline{\widehat w_n},\quad\widehat w_0=0.
 \tag{BW.7}
$$

两个已保存 dyadic fractions 逐坐标作**精确有理数减法**，不再取
一次浮点 midpoint；其新的完整 carrier 有独立 bytes/recipe/SHA。
若后继用有限精度读取该精确 rational，必须使用包含它的有向球。
它一般不严格满足未知真实 $a$ 的反射奇性；真实 $w$ 的该性质由
原定理保留，而 trial 的全部偏差由本条整误差支付。

由 (BW.1)、(BW.6--7) 的完整三角不等式，

$$
 \boxed{e_{w,\infty}=e_{v,\infty}+e_{\alpha,\infty}},\qquad
 \boxed{e_{w,2}=e_{v,2}+e_{\alpha,2}}.
 \tag{BW.8}
$$

不假定两个误差正交，也不从某个旧 norm upper 减去 trial norm。
四个新固定 targets 为两个 vi error 和两个 w error；原 alpha 两球
及全 global/source 数据作为 copied records 保留，不计作新目标。

## BW5. 消费边界

纯公式源为
[fourfold_codazzi_target_w_signed_carrier_math.py](../scripts/fourfold_codazzi_target_w_signed_carrier_math.py)。
实际输入必须是整个 ASR 成功 actual/execution/manifest，而非零 mode
失败或某个 prefix。将来以该 carrier 形成原 same-sign $\mathcal T_w$
时，必须保完整正负支集和 original projection order；它不能被
$PM_wP$ 替代。原 $\mathcal B$ 的两个窗口、mean extension 和 full
physical Schur 身份保持，不用本次误差假装有限矩阵已可逆。

本条仅补原 target coordinate 所缺的实际 signed 输入。必要原 carrier
恢复和新 arithmetic 只在公开 Actions；大数组与逐 mode 数据留在
runner，公开小结论保整 SHA，不上传 artifact/Release。
