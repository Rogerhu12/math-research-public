# R23：实际 warped 浅头的完整非线性源项与均值预算

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**状态：已证明的条件全频源项引理。** 在 R22 的实际浅头参数范围内，本文给出完整均值分支上的全 Fourier 非线性源项、二次 Lipschitz 常数和均值高度增量的显式界。它可用于真正实源方程的残差和强迫校正；不是从保存的浮点端点推导出来的整段界，也不单独断言浅头流、全 Dirichlet DN 或当前大幅闭曲面已存在。

## 1. 对象、范数和结论

使用 [R22](R22-wide-strip-linear-head-envelope.md) §1 的固定新实背景及其全部有限源参数假设。有限浅源的保存参数 $\alpha_n\in[1/2,2]$ 现已由实际 depth12/far225 worker 参数表逐项核销，范围及完整检查见 R22 §1 的 paid-source 账本；$n\ge160$ 的新有理深源则已明定为 $\alpha_n=65/64$。这仍不把浮点 profile 求值称为真实积分包络。令

$$
a=11/4,\quad \delta_n=d_0 2^{-n},\quad
\mu_n=\epsilon_{\rm norm}r_c^7\delta_n^a,
\qquad n\ge12.
\tag{1.1}
$$

用 $r_o$ 表示未 warp 的源半径，$r$ 表示实际半径，$p_*$ 表示九段源 profile 的正层值插值。它们是实函数，不是两个不同数值求积输出的混用。由 R22，

$$
w=\frac{\mu_n p_*}{r_o^7},\qquad
r_c\le r_o\le r<\frac{257}{256}r_c,\qquad
0<w<2^{-12}.
\tag{1.2}
$$

高度扰动的非均值部分为 $v_\perp$。对非零偶 Fourier 频率，使用物理 canonical 坐标

$$
Q_m=\frac{C_m}{r^4},\qquad
\Xi_m=\frac{r^7w}{\mu_n}
\frac{C_m'/r^3-m^2Q_m}{\sqrt{12}}.
\tag{1.3}
$$

这里 $C_m$ 可用复 Fourier 系数，也可用常规 cosine 系数；两种表示对应的完整对称 $\ell^1$ 范数相同。$\Xi$ 不是数值 shooting checkpoint 所保存的非线性 connection momentum $\Pi$，使用实际输出时必须先按完整 root 转换。

对任意 $\tau\ge0$，记

$$
\|f\|_{\tau,k}=\sum_{m\in2\mathbb Z}(1+|m|)^k
e^{\tau|m|}|\widehat f_m|.
$$

输入采用真正的强时空范数

$$
\boxed{
X_n(Z)=\sum_{m\ne0}(1+|m|)^3e^{\tau|m|}
\sup_{r\in I_n}|Q_m(r)|
+\sum_{m\ne0}(1+|m|)e^{\tau|m|}
\sup_{r\in I_n}|\Xi_m(r)|.
}
\tag{1.4}
$$

它的顺序是先逐模取胞元 supremum，再求和。下面不把它替换为较小的 $\sup_r\sum_m$，也不从两端点范数推出 (1.4)。

在非均值变量上取真实的完整角 holonomy 小根来决定均值 slope。若

$$
\boxed{X_n(Z)\le\mathfrak r_n
:=2^{-23}\epsilon_{\rm norm}r_c^{-3}\delta_n^{19/4},}
\tag{1.5}
$$

则完整全频向量场的非线性部分 $\mathcal N=(0,\mathcal N_\Xi)$ 满足

$$
\boxed{
\int_{I_n}\|\mathcal N_\Xi(Z;r)\|_{\tau,0}\,dr
\le B_n X_n(Z)^2,
\qquad
B_n=2^{12}\frac{r_c^3}{\epsilon_{\rm norm}\delta_n^{19/4}}.
}
\tag{1.6}
$$

对同一背景上均满足 (1.5) 的两个路径，令 $X_n(Z-\widetilde Z)$ 按非均值坐标差定义，则

$$
\boxed{
\int_{I_n}\|\mathcal N_\Xi(Z;r)-\mathcal N_\Xi(\widetilde Z;r)\|_{\tau,0}\,dr
\le 2B_n\bigl(X_n(Z)+X_n(\widetilde Z)\bigr)
X_n(Z-\widetilde Z).
}
\tag{1.7}
$$

同一个完整均值根还满足

$$
\boxed{
\int_{I_n}|(v_0)_r|\,dr
\le H_n X_n(Z)^2,
\qquad
H_n=2^8\frac{r_c^7}{\epsilon_{\rm norm}\delta_n^{23/4}}.
}
\tag{1.8}
$$

这些不等式在复 Wiener 球成立，常数不依赖绝对 strip 宽度 $\tau$ 或频率截断。它们是 $L^1_r\mathcal W_\tau$ 源项预算；没有声称已得到不带径向积分的强时空源范数，也没有自动支付返回 (1.4) 所需的线性 Green 算子。

## 2. 完整均值及实际半径下的精确二次恒等式

记物理一阶扰动及相对变量为

$$
p=\frac{v_\theta}{r},\qquad \kappa=v_r,\qquad
\mathsf P=\frac p w,\qquad K=\frac\kappa w,
\qquad \lambda=\frac{w_r}{w}.
$$

取 $K=K_\perp+K_0$，其中 $K_0$ 是完整角平均条件的小根。设

$$
L=K+\mathsf P_\theta,\quad U=K_\theta-\mathsf P,
\quad E=1+w^2,\quad A=1+K+E\mathsf P_\theta.
$$

固定 source Q §2 的全频方程把压缩投影取为恒等后，leading factor 和 density 的乘法逆消去，得到实际 $r$ 坐标下的精确恒等式

$$
\kappa_r=-\lambda(\kappa+p_\theta)+w\mathscr H,
\tag{2.1}
$$
$$
\boxed{
\mathscr H=A^{-1}\left[
\frac E r U^2+\lambda L^2
+\lambda w^2(2K\mathsf P_\theta+\mathsf P_\theta^2-\mathsf P^2)
\right].
}
\tag{2.2}
$$

这适用于实际 warped 半径，因为这里只把源的任意径向参数改写成 $r$；$\lambda$ 是实际 $w_r/w$，不是未 warp 坐标的导数。有限 Galerkin 的压缩逆一般不等于先作 (2.2) 的点态倒数再截断；本文没有对有限 Galerkin 作这个替换。

记

$$R=\|\mathsf P\|_{\tau,1}+\|K_\perp\|_{\tau,1}.$$

source L §2.1 和 R17 §4 的完整复 mean 引理，在非均值输入范数至多 $10^{-4}$ 时给出全纯小根

$$|K_0|\le40R^2.\tag{2.3}$$

为了明确此处使用的域：原 mean 引理的输入 norm 是
$\|K_\perp\|_{\tau,0}+\|\mathsf P\|_{\tau,1}$，它不超过这里的 $R$。其 normalized holonomy 在 $w=0$ 也解析；这项估计没有额外 $w^{-1}$ 奇性。若 $R\le r_*:=2^{-16}$，则

$$
\|K\|_{\tau,1}+\|\mathsf P\|_{\tau,1}
\le R+40R^2\le2R.
\tag{2.4}
$$

于是 $\|A-1\|_\tau\le4R<1/2$，$\|A^{-1}\|_\tau\le2$。其他根号也处于同一个正分支的复邻域：

$$
S_0=1-w^2\mathsf P^2,\quad
D=1-w^2(2K+K^2+E\mathsf P^2),
$$

$$
\|S_0-1\|_\tau\le2^{-56},\qquad
\|D-1\|_\tau\le5\,2^{-40}<2^{-37}.
\tag{2.5}
$$

特别地，实数据下的实际两条正性条件都严格成立。

由 (2.4)，$\|U\|_\tau,\|L\|_\tau\le2R$；同时

$$
\|2K\mathsf P_\theta+\mathsf P_\theta^2-\mathsf P^2\|_\tau
\le6R^2.
$$

因 $E<2$、$w^2<2^{-24}$，(2.2) 的方括号范数不超过
$8(1/r+|\lambda|)R^2$。因此

$$
\boxed{\|\mathscr H\|_\tau
\le16(1/r+|\lambda|)R^2.}
\tag{2.6}
$$

## 3. 完整均值的导数和源项 Lipschitz 常数

在相对非均值 Banach 变量 $z$ 上，把 mean lift 记为 $M(z)$。对于 $\|z\|\le r_*$，以 $\|z\|$ 为半径的复 Cauchy 圆盘落在 $2r_*<10^{-4}$ 的原 mean 球中。(2.3) 直接给

$$\|DM(z)\|\le160\|z\|,\tag{3.1}$$

在 $z=0$ 则由二次性给导数0。沿两点之间的线段积分，得到完整相对场差不超过非均值输入差的2倍。

对两个相对输入，记其半径为 $R,\widetilde R\le r_*$、非均值差范数为 $R_d$。于是

$$
\|A-\widetilde A\|_\tau\le4R_d,
\qquad
\|A^{-1}-\widetilde A^{-1}\|_\tau\le16R_d.
\tag{3.2}
$$

令 $a_r=1/r+|\lambda|$，$J$ 为 (2.2) 的方括号。逐项差分给

$$
\|J-\widetilde J\|_\tau
\le8a_r(R+\widetilde R)R_d,
\qquad
\|\widetilde J\|_\tau\le8a_r\widetilde R^2.
$$

例如 $U^2$ 的差至多 $4(R+\widetilde R)R_d$，乘 $E<2$ 后是上述 $8/r$ 项；$L^2$ 的差至多 $4(R+\widetilde R)R_d$，最后三项的差可统一放宽到 $8(R+\widetilde R)R_d$，再乘 $w^2<2^{-24}$，仍有 $4+8\,2^{-24}<8$。

故完整源满足

$$
\begin{aligned}
\|\mathscr H-\widetilde{\mathscr H}\|_\tau
&\le16a_r(R+\widetilde R)R_d+128a_r\widetilde R^2R_d\\
&\le32a_r(R+\widetilde R)R_d.
\end{aligned}
\tag{3.3}
$$

最后一步仅用了 $16+128r_*<32$。因此没有把 mean 根对输入的依赖漏出 Lipschitz 常数。

## 4. 从 physical canonical 输入到相对球

由 (1.3)，逐模恒有

$$
\mathsf P_m=\frac{imr^3}{w}Q_m,
\qquad
(K_\perp)_m=\frac{m^2r^3}{w}Q_m
+\frac{\sqrt{12}\mu_n}{r^4w^2}\Xi_m.
\tag{4.1}
$$

所以在整个胞元每一点，

$$
R(r)\le\left(\frac{2r^3}{w}
+\frac{4\mu_n}{r^4w^2}\right)X_n.
\tag{4.2}
$$

profile 的最小层值满足 $p_*\ge\delta_n/2$。又
$(r_o/r_c)^7<2$，故

$$w\ge\frac{\epsilon_{\rm norm}}4\delta_n^{a+1}.$$

由 $r^3<2r_c^3$、$r\ge r_c$、$\delta_n<1$ 得

$$
\boxed{
R(r)\le2^7\frac{r_c^3}{\epsilon_{\rm norm}\delta_n^{a+2}}X_n.
}
\tag{4.3}
$$

因此 (1.5) 确实保证 $R(r)\le2^{-16}$，对每个真实胞元内部点都适用。此处没有用某个端口的 profile 值代替 valley 的最小值。

## 5. 实材料积分，不作两个不相容的最大值相乘

下一步保留 (4.2) 中 $w$ 的实际位置，避免把谷底的相对范数最大值与峰顶的 $w^2$ 最大值粗乘。所需准确的材料积分是

$$
I_n=\int_{I_n}(1+p_*^{-2})
\left(\frac{dr}{r}+|d\log w|\right).
\tag{5.1}
$$

R22 已证明实际胞元宽度 $L_n/r_c\le1/256$ 和源半径增量
$\Delta r_o/r_c\le\delta_n$。首先

$$
\int(1+p_*^{-2})\frac{dr}{r}
\le\frac5{256}\delta_n^{-2}.
\tag{5.2}
$$

profile 的五层值依次是 $1,R_n/\delta_n,\delta_n/\alpha_n,1/\delta_n,\rho$，其中 $\rho=2^{11/4}>1$。四个 log 转接均单调；平台不贡献 profile 变差。对每个单调转接，

$$
\int p_*^{-2}|d\log p_*|
=\frac12|p_{*,\rm end}^{-2}-p_{*,\rm start}^{-2}|.
$$

加四段后，使用 $\alpha_n\le2$，得到

$$
\int p_*^{-2}|d\log p_*|
\le\alpha_n^2\delta_n^{-2}+\frac{1+\rho^{-2}}2
\le5\delta_n^{-2}.
\tag{5.3}
$$

另一方面 R22 的 log 变差界给

$$
\int|d\log p_*|\le5(n+9)\le\delta_n^{-2}
\quad(n\ge12).
\tag{5.4}
$$

后一比较在 $n=12$ 用 $105<2^{38}<\delta_{12}^{-2}$；之后左侧相邻比小于4，右侧恰乘4。

由于 $w=\mu_n p_*/r_o^7$，

$$|d\log w|\le|d\log p_*|+7d\log r_o.$$

额外半径项至多

$$
7\int(1+p_*^{-2})d\log r_o
\le35\delta_n^{-1}
<\frac1{256}\delta_n^{-2},
\tag{5.5}
$$

这里用的是 $\delta_n<2^{-19}$。合并 (5.2)–(5.5)，得到实际 warped 源也可使用的严格界

$$
\boxed{I_n\le(6+6/256)\delta_n^{-2}
<8\delta_n^{-2}.}
\tag{5.6}
$$

该证明没有用 $w_r$ 的采样最大值、未认证的 quadrature 误差或有限角网格。

## 6. canonical 源项积分和差分

由 (1.3) 和 (2.1)，$Q$ 的方程没有非线性强迫；对 $\Xi$ 则准确有

$$
\boxed{\mathcal N_{\Xi,m}
=\frac{r^4w^2}{\sqrt{12}\mu_n}\mathscr H_m.}
\tag{6.1}
$$

这是常规 cosine 或复 Fourier 归一化。若数值实现用 $\sqrt2\cos(m\theta)$ 的正交基，须先转换系数；不可再凭空保留一个额外的 $\sqrt2$。

由 (4.2)，

$$
R(r)^2\le
\left(\frac{8r^6}{w^2}
+\frac{32\mu_n^2}{r^8w^4}\right)X_n^2.
$$

将它和 (2.6) 代入 (6.1)，可取

$$
\|\mathcal N_\Xi\|_\tau
\le2^8(1/r+|\lambda|)
\left(\frac{r^{10}}{\mu_n}
+\frac{\mu_n}{r^4w^2}\right)X_n^2.
\tag{6.2}
$$

因为 $r_o\le r$，第二项满足

$$
\frac{\mu_n}{r^4w^2}
=\frac{r_o^{14}}{r^4\mu_n p_*^2}
\le\frac{r^{10}}{\mu_n p_*^2}.
$$

再用 $(257/256)^{10}<2$，积分 (6.2) 给

$$
\int\|\mathcal N_\Xi\|_\tau dr
\le2^9\frac{r_c^3}{\epsilon_{\rm norm}\delta_n^a}
I_nX_n^2
\le2^{12}\frac{r_c^3}{\epsilon_{\rm norm}\delta_n^{a+2}}X_n^2.
$$

这就是 (1.6)。采用 (3.3)，同一个计算仅把前面的16换成32，故给出 (1.7) 的 $2^{13}$。

输入 (1.4) 控制每一点的 $R$，输出则是准确的 $L^1_r$ 范数。非负项的 Tonelli 定理允许把输出写成

$$
\int\sum_m e^{\tau|m|}|\mathcal N_m(r)|dr
=\sum_m e^{\tau|m|}\int|\mathcal N_m(r)|dr.
$$

这里没有把输出擅自换成 $\sum_m\sup_r|\mathcal N_m(r)|$。在一个后续 Green 算子给定了从该 $L^1_r$ 源空间到所需状态空间的范数时，(1.6)–(1.7) 才可直接乘以该范数。

## 7. 完整均值的物理高度增量

由 (2.3) 和 (4.2)，

$$
|(v_0)_r|=w|K_0|
\le\left(\frac{320r^6}{w}
+\frac{1280\mu_n^2}{r^8w^3}\right)X_n^2.
$$

使用 $w=\mu_np_*/r_o^7$、$r_o\le r$，再用
$(257/256)^{13}<2$，得

$$
|(v_0)_r|
\le2^{12}\frac{r_c^6}{\epsilon_{\rm norm}\delta_n^a}
(p_*^{-1}+p_*^{-3})X_n^2.
\tag{7.1}
$$

由于 $p_*\ge\delta_n/2$，括号至多 $10\delta_n^{-3}$。所以还有点态界

$$
|(v_0)_r|\le2^{16}\frac{r_c^6}
{\epsilon_{\rm norm}\delta_n^{23/4}}X_n^2.
\tag{7.2}
$$

而 $L_n\le r_c/256$ 给

$$
\int|(v_0)_r|dr
\le\frac{10\,2^{12}}{256}
\frac{r_c^7}{\epsilon_{\rm norm}\delta_n^{23/4}}X_n^2
\le H_nX_n^2,
$$

即 (1.8)。均值高度必须从一个统一 gauge 积分，不能在每个胞元两端分别重置。以上预算支付的是这个真实 mean root 的 slope 和高度变化；完整二阶径向 jet 仍由实际方程 (2.1) 决定。

## 8. 当前 dyadic 参数下可直接使用的尺度

R17 已用存数的精确分数证明

$$
2^{14}<\epsilon_{\rm norm}<2^{15},\quad
r_c<2^{-4},\quad
2^{-8}<d_0<2^{-7}.
$$

所以可以采用以下纯二进制预算：

$$
\mathfrak r_n>2^{-19n/4-35},\qquad
B_n<2^{19n/4+24},\qquad
H_n<2^{23n/4+12}.
\tag{8.1}
$$

例如在第12胞元，保守的输入球为 $X_{12}\le2^{-92}$，而
$B_{12},H_{12}<2^{81}$。如果今后的真实全胞元包络实际证明
$X_{12}\le2^{-140}$，则该胞元非线性源和均值高度增量各小于
$2^{-199}$。这里的 $2^{-140}$ 是一个可检验的预算示例，**不是已从 q003 的端点数值证明的界**。

附属脚本
`computations/closure_head_forcing_ledger.py`
把所有分数范围、整数常数和 (8.1) 的代表胞元做精确比较。非整数四分之一次幂的比较通过两边取四次方完成，没有浮点幂作为认证依据。输出为
`notes/2026-11-12-closure-head-forcing-ledger.json`。

## 9. 已支付的接口及本结果的准确边界

R22 控制真实深尾的高模端迹经过精确线性头的像。本文另外支付在实际 warped 实源上、完整 mean 分支中的全频非线性源项及其 Lipschitz 常数，且保留了正确的 canonical 坐标、材料积分和物理均值尺度。

把两项接入实际浅头问题时，仍要以同一个真实路径的全胞元包络核销 (1.5)，并使用与 (1.6) 源空间相配的线性/线性化 Green 界。本文没有从 endpoint 小量直接跳过这一步。有限 Galerkin、有限径向积分和源实积分的误差也不能由 profile fingerprint 自动支付。

最终高频 cut 高度依旧是完整解的输出，须由前缀联解吸收；这里没有固定高于46模的全部浅端 Dirichlet 数据。所有这些量词与 R18 的46参数真尾接口一致。

引用的方程和 mean 引理来自固定提交
`869436630c99aa5a68afb55bd8877c826034d117` 的 Q/L 文件，精确路径与 hash 见 R17 §2。本文使用并补全该接口的实际 warped 系数，没有把旧 source 的纯数值输出用作证明。
