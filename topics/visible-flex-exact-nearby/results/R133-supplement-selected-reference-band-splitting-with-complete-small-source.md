# R133 续篇：保留 selected 源抵消的32模主背景分带

2026-11-15，visible-exact / tail_connector。

**已证明的解析拆分，供独立核对。** 本篇与 [DB](R133-supplement-degree32-reference-band-cancellation-and-finite-receivers.md) 使用同一个真实状态、同一组正 collar 系数、同一 canonical 连续方向和同一 Fourier 投影。它把 DB 的 degree32 主线性带消去直接用于 selected 未知量，因而可以继续消费已成 [NR](R133-supplement-actual-saved-nonmean-restrictions-and-three-band-trace-budgets.md) / [WA](R133-supplement-actual-wide-collar-mean-and-six-ordinary-half-trace-tables.md) 的小源，而不先将已知 $\delta Z_{\rm can}$ 作为粗 body norm 加回未知 shell。

没有新数值运行。所有原成功源积分、MA 五例、Green 和参考系数原样保留。本文不宣称新增 shell receiver 的未知范数已付。

## 1. 一直使用同一个 selected 未知

沿用 DB.1--3：
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\quad
 W_0=PQ_0,\quad e=\delta PZ_{\rm can},\quad
 W_\delta=W_0+e,\quad z=P(Q-Q_\delta).
 \tag{SB.1}
$$
$Q_0$ 的完整角支撑止于32，$Z_{\rm can}$ 止于96，mean 均保。
$P(r)=\operatorname{diag}(K^{-1/4},K^{1/4})$ 是同一个径向矩阵。
实际状态 $Q$、其 ordinary 残差 $f$、真 mean、实际 principal $a,d$ 不改变。
这里固定 R.16--22 已明确避开 intrinsic $\nu$ bump 的同一正 collar，故 $P,\alpha,b,g$ 是共同径向系数；本篇不将有 intrinsic 系数变化的其他区间并入这个恒等式。

取真界
$$
 |W_0|\le M_0,\quad |W_{0,\phi}|\le M_1,\quad
 |e|\le E_0,\quad |e_\phi|\le E_1,\quad |z|\le\eta_\delta.
 \tag{SB.2}
$$
例如可用同窗 $E_0\le19p_+|\delta|$、$E_1\le83p_+|\delta|$，
以及 $\eta_\delta\le p_+\rho_w$。这些是 selected 球的真实单位。
没有把 $\eta_\delta$ 改成关于 $Q_0$ 的球，也没有增加 $\delta Z_{\rm can}$ 的未知 body 输入。

## 2. 完整 reference 差的精确式

对任意已知背景 $W$，定义 E.13 的 reference 部分
$$
 {\cal A}^{\rm ref}(W)u=
 \alpha Du-b\{|W|^2u+2W(W\cdot u)\}
 -2bW_\phi I_\phi(W\cdot u)
 +g\langle u_2\rangle J_0W_\phi .
 \tag{SB.3}
$$
全部 mean/rank 项保留在定义中。令
${\cal A}_*={\cal A}^{\rm ref}(W_0)$。直接展开得到
$$
 \begin{aligned}
 \Delta_{\rm ref}{\cal A}\,u
 :={}&[{\cal A}^{\rm ref}(W_\delta)-{\cal A}_*]u\\
 ={}&-b\{(2W_0\cdot e+|e|^2)u
       +2W_0(e\cdot u)+2e(W_0\cdot u)+2e(e\cdot u)\}\\
 &-2b\{W_{0,\phi}I(e\cdot u)
                +e_\phi I(W_0\cdot u)+e_\phi I(e\cdot u)\}\\
 &+g\langle u_2\rangle J_0e_\phi .
 \end{aligned}\tag{SB.4}
$$
因此完整 $L^2$ 算子界可以取
$$
 A_{\rm ref,\delta}
 =b_+(6M_0E_0+3E_0^2)
 +\frac{b_+}{2}(M_1E_0+M_0E_1+E_0E_1)+g_+E_1 .
 \tag{SB.5}
$$
其每一项均为非负已知系数。primitive 先作用于完整乘积，使用
$I:L^2\to L^2$ 的 $1/4$；没有将 mean-containing 乘积改成逐点除频率。

对 $H_J$、$J\ge96$，(SB.4) 末项的输出准确止于96，故可以去掉
(SB.5) 的 $g_+E_1$，记所得较尖界为 $A_{\rm ref,\delta}^{>J}$。
这只删除这个已显式识别的高输出零项；$u_2$ 的 mean 在前三种乘积中仍全部保留。

实际非线性差以 $W_\delta$ 为背景，按 E.13 精确为
$$
 \begin{aligned}
 \Delta_{\rm nl}{\cal A}\,u
 ={}&-b\{(2W_\delta\cdot z+|z|^2)u+W_\delta(z\cdot u)\}\\
 &-bW_{\delta,\phi}I(z\cdot u).
 \end{aligned}\tag{SB.6}
$$
置 $M_\delta=M_0+E_0$、$M_{\delta,1}=M_1+E_1$，则
$$
 A_{\rm nl}
 =b_+\eta_\delta(3M_\delta+\eta_\delta+M_{\delta,1}/4),
 \qquad
 \|H_J(\Delta_{\rm ref}{\cal A}+\Delta_{\rm nl}{\cal A})u\|_2
 \le(A_{\rm ref,\delta}^{>J}+A_{\rm nl})\|u\|_2 .
 \tag{SB.7}
$$
也可以直接使用已付更宽 $M_\delta,M_{\delta,1}$；不得把原无关 full-state norm 减成一个新小量。

令 $d_0=-bI|W_0|^2$。实际 drift 差准确分为
$$
 d-d_0=-bI(2W_0\cdot e+|e|^2)
        -bI(2W_\delta\cdot z+|z|^2).
 \tag{SB.8}
$$
完整 sawtooth primitive 费用给
$$
 D_{\rm ref,\delta}=\frac{\pi b_+}{8}E_0(2M_0+E_0),\qquad
 D_{\rm nl}=\frac{\pi b_+}{8}\eta_\delta(2M_\delta+\eta_\delta),
 \quad \|d-d_0\|_\infty\le D_{\rm ref,\delta}+D_{\rm nl}.
 \tag{SB.9}
$$
这里仍使用同一个实际 principal $a,d$ 和同态 $a_-,L,c_p,c_r$，不是对另一个解重套能量。

## 3. selected ordinary 源和32模主带同时保留

对 $J\ge96$，定义
$$
 z_L=\Pi_Jz,\quad z_S=(\Pi_J-\Pi_{J-64})z,\quad z_H=H_Jz,
 \quad Z_L=\|z_L\|_2,\ Z_S=\|z_S\|_2,\ Z_H=\|z_H\|_2.
 \tag{SB.10}
$$
这些都是 selected 差的完整 ordinary $L^2(dr\,d\phi)$ 范数。
DB.11 对 ${\cal A}_*$ 和 $d_0$ 原样适用。

记 $f_\delta=Q_{\delta,r}-{\cal F}(Q_\delta)$。
用 PE 的 projected principal 后，准确高方程为
$$
 \begin{aligned}
 {\cal L}_{H_J}H_Jz={}&H_J{\cal A}_*(z_S+z_H)
 +H_J(\Delta_{\rm ref}{\cal A}+\Delta_{\rm nl}{\cal A})z\\
 &+H_Jd_0\partial_\phi z_S
 +H_J(d-d_0)\partial_\phi z_L
 +H_JP(f-f_\delta).
 \end{aligned}\tag{SB.11}
$$
所有 $\delta Z_{\rm can}$ 的已知高 residual 都留在最后一项，不被一个
$\delta\|PZ_{\rm can}\|_{\rm body}$ 的大 triangle 代替。

对同一 triangular cutoff，$C_{\chi,J}=\|\chi'H_Jz\|_2$，
一个完整正向能量 budget 为
$$
 \begin{aligned}
 E_J^{\rm sel}={}&\|H_JP(f-f_\delta)\|_2
 +(A_*+4Jd_{0,+})Z_S+(A_*+L)Z_H+C_{\chi,J}\\
 &+(A_{\rm ref,\delta}^{>J}+A_{\rm nl})(Z_L+Z_H)
 +4J(D_{\rm ref,\delta}+D_{\rm nl})Z_L .
 \end{aligned}\tag{SB.12}
$$
$A_*$ 是 DB.9 的完整 operator bound；没有再加 PE 已经准确消去的 self-commutator。
在宽 $[.85,.95]$ 窗上可以用 $C_{\chi,J}\le20Z_H$。

真解 $f=0$ 时：
$$
 \|H_{96}P(f-f_\delta)\|_2=\|H_{96}Pf_\delta\|_2
                    \le F_{96}^{\rm NR/WC},\qquad
 H_{288}P(f-f_\delta)=0 .
 \tag{SB.13}
$$
第二个等式是完整 selected reference 支撑止于288的结论，
包括 $f_0$、canonical response、两个非线性 Taylor 项及 raw mean。

更具体地，正确 source identity 始终是
$$
 f_\delta=f_0-\delta b_0+\delta r_0e_2-\delta^2T_2-\delta^3T_3.
 \tag{SB.14}
$$
当前已经成功的 NR/WC 对 $H_{96}$ 支付这个完整 source。
$+\delta r_0e_2$ 仅在当前高投影中准确消去；没有撤销 MC/MA 的完整 mean 修正，
没有将 mean-completed $q^\sharp$ 当 canonical $Z_{\rm can}$。

对近似态，(SB.13) 不能使用 $f=0$，必须改用
$$
 \|H_{96}P(f-f_\delta)\|_2\le\|H_{96}Pf\|_2+F_{96}^{\rm NR/WC},
 \qquad
 \|H_{288}P(f-f_\delta)\|_2=\|H_{288}Pf\|_2.
 \tag{SB.15}
$$
其 residual mean 也继续进入实际 principal 速度的径向变化条件。

## 4. 去掉 radial diagonal 的另一精确选择

如另有已付同窗
$$
 \overline W_0=\langle W_0\rangle,\quad
 \|\overline W_0\|\le M_{\rm av},\quad
 \|W_0-\overline W_0\|_\infty\le N_0,\quad
 \|W_{0,\phi}\|_\infty\le N_1,
 \tag{SB.16}
$$
则 ${\cal A}^{\rm ref}(\overline W_0)$ 是径向 Fourier-diagonal 乘子，
所以 $H_J{\cal A}^{\rm ref}(\overline W_0)\Pi_J=0$。
又因 reference rank 输出止于32，主低输入列可以使用
$$
 A_{\rm mix}
 =b_+(6M_{\rm av}N_0+3N_0^2)
       +\frac{b_+}{2}N_1(M_{\rm av}+N_0),
 \qquad
 \|H_J{\cal A}_*z_S\|_2\le A_{\rm mix}\|z_S\|_2.
 \tag{SB.17}
$$
证明直接将 (SB.3) 的背景拆成径向 mean 加 nonmean，并在最后一次
$H_J$ 后取消 reference rank；mean 本身没有从原方程中删除。

同理
$$
 d_{0,+}\le\frac{\pi b_+}{8}(2M_{\rm av}N_0+N_0^2).
 \tag{SB.18}
$$
若 (SB.16) 的 actual narrow/wide 字段尚未支付，则不准使用这些较尖系数；
原 (SB.12) 仍保持完整有效。尤其不能由 full-state norm 和 mean norm
分别取上界后相减来制造 $N_0$。$A_*$ 对 high 输入的费不因 (SB.17) 而删去。

## 5. 同一 cut、高正则与实际 receiver

将 (SB.12) 代入 DB.17 的相同 half-trace 输出，再用 MA.7 的 selected
$H^{8193}$，得到 DB.19 同一个三带 cut 界，且全部 $Z_L,Z_S,Z_H$ 都是
selected 差。主要有限 shell 为33--96；far 的线性 shell 为225--288。
full finite193 cut 仍含 mean。

因此新 left receiver 可以直接消费原 Green 的 selected moving 未知 $h$，
而不再为该 shell 另加 DB.22 的 $\delta PZ_{\rm can}$ body triangle。
DB.22 本身没有错误：它是选择 $z_0$ 为未知时的准确转换。本篇选择的是
另一个等价但保留已知 source 抵消的方程。

新 receiver 的局部 signed Gram 仍须真实构造。当前 active Green 没有保存
该局部 $F(r)$ 系数，不能从旧三类 input-side Gram 截输出频带。
右半同态 cap、225--288真 high 部分、未知 ordinary residual、两侧真实接口、
independent narrow MA 球及全部 mean/cut 数据仍独立保留。

(SB.12) 或 (SB.17) 的系数可以由后继公共 read-only scalar 消费原已成字段；
本文不运行这些新数，不更改任何旧 source、norm、verdict 或存在性结论。
