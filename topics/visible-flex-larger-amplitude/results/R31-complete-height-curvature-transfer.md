# R31：完整高度两 jet 的全角主曲率转移界

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

状态：**已证明，条件几何工具**。给出从同一个实际等距高度函数的完整 $H/P/Q$ 到主曲率的连续门，包括完整均值、角向全部频率和径向区间。它不能把有限 ODE 的源右端、保存曲线的二阶导数或单 cut 修正混为同一个函数，也不把样本最大曲率当作全域证书。

## 1. 实际高度与主曲率的精确恒等式

设 $F$ 是 $C^2$ 等距浸入，其度量为

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad E(r)>0,\quad r>0.
$$

令 $h=e_z\cdot F$、$P=h_r$、$Q=h_{rr}$，并取正交标架
$e_1=E^{-1/2}\partial_r,e_2=r^{-1}\partial_\theta$。记

$$
\nu^2:=1-\frac{P^2}{E}-\frac{h_\theta^2}{r^2}>0.
\tag{31.1}
$$

选择竖直分量为正的单位法向，则 $n_z=\nu$，且

$$
\mathcal H:=\operatorname{Hess}_g h=
\begin{pmatrix}
(Q-E'P/(2E))/E&
(P_\theta-h_\theta/r)/(r\sqrt E)\\
(P_\theta-h_\theta/r)/(r\sqrt E)&
(h_{\theta\theta}+rP/E)/r^2
\end{pmatrix}.
\tag{31.2}
$$

全部主曲率是 $\mathcal H/\nu$ 的特征值。因此

$$
\boxed{\max_i|\kappa_i|=\frac{\|\mathcal H\|_{\rm op}}{\nu}.}
\tag{31.3}
$$

**证明。** 在任意切向量场上，$D_XdF(Y)=dF(\nabla_XY)+\mathrm{II}(X,Y)n$。与固定 $e_z$ 作内积，得到 $\operatorname{Hess}_g h=n_z\mathrm{II}$。水平投影的正交 Gram 矩阵为 $I-\nabla_gh\,\nabla_gh^T$，故单位法向竖直分量平方等于 (31.1)。由 $g$ 的 Christoffel 符号 $\Gamma^r_{rr}=E'/(2E)$、$\Gamma^r_{\theta\theta}=-r/E$、$\Gamma^\theta_{r\theta}=1/r$ 得 (31.2)。在正交标架中第二基本形式矩阵就是形算子矩阵，所以 (31.3) 成立。$\,\square$

这是主曲率公式。它不同于 [R21](R21-flat-cap-markers-without-reach-loss.md) 的水平图 Hessian，其界一般更大；[R25](R25-entire-graph-curvature-and-reach.md) 使用的正是本节主曲率。

## 2. 相对背景的点态全角门

选择一个实际径向参考高度 $h_0(r)$，写 $w=h_0'$、$w_r=h_0''$、$v=h-h_0$。令

$$
p=P-w,\quad q=Q-w_r,\quad u=\frac{h_\theta}{r},\quad
\beta=1-\frac{w^2}{E}>0.
\tag{31.4}
$$

不先假设浮点字段满足 $E=1+w^2$；一般恒等式也允许使用相同度量 $E$ 上的任意径向参考函数。其参考矩阵为

$$
\mathcal H_0=
\begin{pmatrix}
(w_r-E'w/(2E))/E&0\\
0&w/(Er)
\end{pmatrix},
\qquad
K_0=\frac{\|\mathcal H_0\|_{\rm op}}{\sqrt\beta}.
\tag{31.5}
$$

若参考径向函数与 $E$ 不满足旋转曲面的精确关系，$K_0$ 只表示这个参考矩阵的大小，不把它称作一个已经实现的旋转背景曲率。

对某个固定 $r$ 的整个角圆，设已有

$$
\|p\|_\infty\le d,\qquad \|u\|_\infty\le e,\qquad
\varepsilon:=\frac{(2|w|d+d^2)/E+e^2}{\beta}<1,
\tag{31.6}
$$

以及

$$
\begin{aligned}
A&\ge \frac{\|q-E'p/(2E)\|_\infty}{E},\\
B&\ge \frac{\|P_\theta-h_\theta/r\|_\infty}{r\sqrt E},\\
C&\ge \frac{\|h_{\theta\theta}/r+p/E\|_\infty}{r}.
\end{aligned}
\tag{31.7}
$$

取

$$
\Lambda(A,B,C)=
\frac{A+C}{2}+\sqrt{\frac{(A-C)^2}{4}+B^2}.
\tag{31.8}
$$

则完整角圆满足

$$
\nu^2\ge\beta(1-\varepsilon)>0,\qquad
\boxed{
\max_{\theta,i}|\kappa_i|
\le\frac{K_0+\Lambda(A,B,C)/\sqrt\beta}
          {\sqrt{1-\varepsilon}}.}
\tag{31.9}
$$

可用更简单的有理矩阵上界 $\max(A,C)+B$ 代替 $\Lambda$。

**证明。** 展开 (31.1)，

$$
\nu^2=\beta-\frac{2wp+p^2}{E}-u^2
\ge\beta(1-\varepsilon).
$$

矩阵 $\mathcal H-\mathcal H_0$ 的三个独立条目分别由 $A,B,C$ 控制。对单位向量 $z$，

$$
|z^T(\mathcal H-\mathcal H_0)z|
\le A|z_1|^2+2B|z_1z_2|+C|z_2|^2
\le\Lambda(A,B,C).
$$

三角不等式与 (31.3) 即给 (31.9)。$\,\square$

给定目标 $K_*>0$，一个明确的预算门就是

$$
\boxed{
\Lambda(A,B,C)
\le\sqrt\beta\bigl(K_*\sqrt{1-\varepsilon}-K_0\bigr),
\quad K_*\sqrt{1-\varepsilon}\ge K_0.}
\tag{31.10}
$$

本课题可取 $K_*=33/4$，或者取已严格得到的直径上界 $\overline D$ 所允许的 $K_*\le100/(3\overline D)$。直径点云的下界不能代入后者充作允许预算。

### 2.1 真正旋转背景的简化

若在实数函数层面确有

$$
E=1+w^2,\qquad E'=2ww_r,
\tag{31.11}
$$

则 $\beta=1/E$，并且

$$
K_0=\max\left\{\frac{|w_r|}{E^{3/2}},
                     \frac{|w|}{r\sqrt E}\right\},\qquad
\varepsilon=2|w|d+d^2+Ee^2.
\tag{31.12}
$$

因此 (31.9) 变成

$$
|\kappa|\le\frac{K_0+\sqrt E\,\Lambda(A,B,C)}
                         {\sqrt{1-\varepsilon}}.
\tag{31.13}
$$

不能因为配置文件有某个 curvatureBound 字段就认定 $K_0$ 已通过同名界；必须验证实际背景的两个表达式。保存的 $E,w,E',w_r$ 若不精确满足 (31.11)，应使用一般门或把差值纳入区间，不能静默替换算术对象。

## 3. 完整 Fourier 输入和径向连续性

例如实偶数据写为

$$
\begin{aligned}
h&=h_0+c_0+\sum_{m>0}H_m\cos(m\theta),\\
P&=w+p_0+\sum_{m>0}P_m\cos(m\theta),\\
Q&=w_r+q_0+\sum_{m>0}Q_m\cos(m\theta).
\end{aligned}
\tag{31.14}
$$

全部系数可依赖 $r$，并要求这些是同一高度函数的导数，因此 $p_0=c_0'$、$q_0=c_0''$，非均值系数也满足实际径向微分关系。不能只保留 nonmean 分支。

固定 $r$ 时，下列输入对**全部实角**成立：

$$
\begin{aligned}
d&=|p_0|+\sum_m|P_m|,&
e&=\frac1r\sum_m m|H_m|,\\
A&=\frac1E\left(
\left|q_0-\frac{E'}{2E}p_0\right|
+\sum_m\left|Q_m-\frac{E'}{2E}P_m\right|\right),\\
B&=\frac1{r\sqrt E}\sum_m m\left|P_m-\frac{H_m}{r}\right|,\\
C&=\frac1r\left(
\frac{|p_0|}{E}
+\sum_m\left|\frac{P_m}{E}-\frac{m^2H_m}{r}\right|\right).
\end{aligned}
\tag{31.15}
$$

这里先组合同一频率再取绝对值，保留有用的线性抵消；把每个量各自取最大值后相加仍然有效，但可能浪费曲率预算。实 sine/cosine 混合谱可把每个正频率的绝对值换为对应二维系数的欧氏范数，或直接使用完整复 Fourier 的 $\ell^1$ 范数。

若有未表示的尾或真解与近似的误差，必须把它对 $p,u$ 及 (31.7) 三个**组合量**的连续上界加进去。证明存在高频余项不等于余项为零。

要覆盖一个径向区间 $I$，须对每个 $r\in I$ 核销上述门。一个保守的统一实现是给出

$$
\beta\ge\beta_*>0,\quad
\varepsilon\le\varepsilon_*<1,\quad K_0\le K_{0,*},
\quad A\le A_*,\ B\le B_*,\ C\le C_*,
$$

于是整个 $I\times S^1$ 满足

$$
|\kappa|\le
\frac{K_{0,*}+\Lambda(A_*,B_*,C_*)/\sqrt{\beta_*}}
     {\sqrt{1-\varepsilon_*}}.
\tag{31.16}
$$

这些输入可以由实源 profile 与系数函数的区间包围取得。对 Fourier 数据必须采用逐模径向 supremum 之后再求和，或者直接包围组合 Fourier 系数；只有层端点的值、只采径向中点或源 ODE 右端的最大值都不够。若区间界过宽，可以细分同一背景下的径向区间；分区本身不改变 $g$。

## 4. R23 的深尾小球自动支付一个曲率门

在 [R23](R23-warped-head-complete-nonlinear-source-budget.md) 的完整全频、真实 mean 分支上，使用其相对变量

$$
\mathsf P=\frac{h_\theta}{rw},\qquad
K=\frac{P-w}{w},\qquad
R=\|\mathsf P\|_{\tau,1}+\|K_\perp\|_{\tau,1},
$$

并假设

$$
0<w\le2^{-12},\qquad R\le2^{-16},\qquad
K_0\le8,\qquad E=1+w^2.
\tag{31.17}
$$

这里还使用 R23 已证明的完整 mean 与全频方程结论

$$
\|K\|_{\tau,1}+\|\mathsf P\|_{\tau,1}\le2R,
\qquad
Q-w_r=-w_r(K+\mathsf P_\theta)+w\mathscr H,
$$

$$
\|\mathscr H\|_\tau\le16(1/r+|w_r/w|)R^2.
\tag{31.18}
$$

则对所有实角有

$$
\boxed{\nu^2>0.99999994,\qquad
|\kappa|<\frac{8001}{1000}=8.001<\frac{33}4.}
\tag{31.19}
$$

这对实际无限频谱成立，不依赖一个截断阶数。R23 的强胞元小球 (1.5) 已推出整个胞元的 $R\le2^{-16}$；所以只要真实背景 $K_0\le8$ 同时得到支付，其强球给出的尾部不再需要另做角向曲率网格。

**证明。** 置 $\sigma=2^{-24}$、$R_*=2^{-16}$。由 (31.18)，

$$
\varepsilon\le
\varepsilon_*:=\sigma\bigl(4R_*+4(2+\sigma)R_*^2\bigr).
\tag{31.20}
$$

将 (31.18) 代入 (31.7)，用背景两个主曲率均不超过 $K_0$，得到

$$
\begin{aligned}
\sqrt E A/K_0
&\le2(1+2\sigma)R+16(2+\sigma)R^2,\\
\sqrt E B/K_0&\le2\sqrt{1+\sigma}\,R,\\
\sqrt E C/K_0&\le2(1+\sigma)R.
\end{aligned}
\tag{31.21}
$$

例如第一式使用
$|w_r|/\sqrt E=E\,|w_r|/E^{3/2}\le E K_0$，以及
$|w|/(r\sqrt E)\le K_0$；两种背景贡献分别保留，所以没有漏掉 $\mathscr H$ 中的 $|w_r/w|$。

第一行上界不小于第三行上界。由
$\sqrt{1+\sigma}\le1+\sigma/2$ 和矩阵绝对行和界，

$$
\frac{\sqrt E\,\|\mathcal H-\mathcal H_0\|_{\rm op}}{K_0}
\le L_*:=(4+5\sigma)R_*+16(2+\sigma)R_*^2.
\tag{31.22}
$$

最后用 $\sqrt{1-\varepsilon_*}\ge1-\varepsilon_*$，有

$$
|\kappa|\le\frac{8(1+L_*)}{1-\varepsilon_*}
<\frac{8001}{1000},
\qquad
\nu^2\ge\frac{1-\varepsilon_*}{1+\sigma}
>\frac{99999994}{10^8}.
\tag{31.23}
$$

最后两项均是明确的有理数比较，见配套账本。$\,\square$

此推论不声称当前强幅 finite Robin 轨道已经进入 R23 的真实强球。特别是 raw node 的小值不能证明胞元内部的 (1.4) 强范数；有限 shooting $\Pi$ 也不能直接当成 R23 的 canonical $\Xi$。

### 4.1 对内 cuff 的平二阶极限

在 (31.18) 的真实解上，若 $r\downarrow r_c>0$ 时 $w,w_r\to0$，且 $R$ 一直有上述统一界，则

$$
P,\ h_\theta,\ P_\theta,\ h_{\theta\theta},\ Q\longrightarrow0
\quad\text{一致于角度}.
\tag{31.24}
$$

前四项直接由相对范数界得到。最后一项使用

$$
|w\mathscr H|
\le16\bigl(|w|/r+|w_r|\bigr)R^2\longrightarrow0.
$$

所以 $\nu\to1$、$\nabla_gh\to0$、$\operatorname{Hess}_gh\to0$。在已经建立的真实水平图坐标中，R21 的精确转换使 $\nabla_{xy}f,D^2_{xy}f\to0$。由于 $P$ 在有限径向区间有界，高度有一致极限；又 $h_\theta\to0$，该极限为同一常数。

因此若内 cuff 的水平边界还已证明为合法的 $C^2$ 边界，这些界支付 R27 平盘填充所需的高度/梯度/Hessian 极限。它们不单独证明全局图拓扑、内边界存在或浅头与真实深尾匹配。

### 4.2 当前 R26 新实背景的全尾 $K_0\le8$ 已支付

这一小节只处理 [R26](R26-real-head-source-interval-and-port-coordinates.md) 的**同一个真实旋转背景**，不处理尚未证明存在的非轴轨道。所有浅源参数、global warp alpha 和 factory 捕获的 oldCut 固定；$n\ge160$ 采用 $65/64$。指数、对数与半径积分都指对应实函数，不把保存 profile 的浮点样本当成证明。

固定参数满足

$$
d_0=\frac{3458764513820541}{576460752303423488},\qquad
c_0=\frac{3602879701896397}{72057594037927936},\qquad
c_\eta=\frac{c_0}{\sqrt{d_0}}>\frac12,
$$

$$
\frac3{64}<r_c<\frac1{16},\qquad
\alpha_{\rm warp}>2,\qquad E=1+w^2.
\tag{31.25}
$$

最后的 $c_\eta$ 比较可直接平方为 $4c_0^2>d_0$。全部浅源参数范围已由 R22 的 paid-source 账本核销。

**第 12 至 158 胞元。** 该区 cap 不起作用，保护权 $\chi=1$，实际半径满足

$$
r_x=\frac{|w_x|}{8(1+w^2)^{3/2}}+
\alpha_{\rm warp}\frac{(r_o)_x}{1+w^2}.
\tag{31.26}
$$

因此

$$
\frac{|w_r|}{(1+w^2)^{3/2}}\le8.
$$

由 R22 的 $w<2^{-12}$、$r\ge r_c>3/64$，环向曲率还满足

$$
\frac{w}{r\sqrt{1+w^2}}<\frac1{192}.
\tag{31.27}
$$

**第 159 胞元及以后。** 在受保护的内 collar，$r_x\ge(r_o)_x$；因为非曲率部分是 $(1-\chi)(r_o)_x+\chi\alpha_{\rm warp}(r_o)_x/E$，其中 $\alpha_{\rm warp}/E>1$。在 $n\ge160$，$r=r_o$。故此处只需控制未 warp 的真实导数。

设某转接的 log 跳量为 $b$、长度为 $\ell$。R22 给

$$
w\le2^{21}\delta_n^{7/4},\quad |b|\le5(n+9),\quad
\ell\ge\frac12\delta_n^{3/2},\quad
S'(x)\le\frac{15}{8},\quad \sqrt{12}<\frac72.
$$

平台只会有更小的界。对 $w=\mu_n p_*/r_o^7$ 直接求导，得到

$$
\left|\frac{dw}{dr_o}\right|
<
\frac{2^{27}}3\left[
\frac{525}{8}(n+9)\delta_n^{1/4}
+7\delta_n^{7/4}\right].
\tag{31.28}
$$

在 $n=159$，$\delta_n<2^{-166}<2^{-164}$，故右端小于

$$
\frac{3675}{16384}+2^{-258}<\frac9{40}.
\tag{31.29}
$$

首项相邻比至多 $(169/168)(27/32)<1$，第二项也递减，因此同一界覆盖所有 $n\ge159$，并且两项均趋零。由 $r_x\ge(r_o)_x$，实际 $w_r\to0$；$w\to0$ 已由 (31.28) 前的上界得到。这同时支付第 4.1 节背景所需的平二阶极限。该区径向曲率小于 $9/40$，环向仍小于 $1/192$。

**外侧第 0 至 11 胞元的斜率。** 普通 cap 的导数在 log 转接中为 $1-S_7\in[0,1]$；其值在两端接原 log slope 与 cap log level，所以 cap 输出不超过当地 cap。相邻 cap 的 log 插值仍不超过两端最大值。第 0 胞元普通 cap 最大为保存 binary64 的 $0.4$，第 1 至 11 胞元为保存 binary64 的 $0.02$。valley control 不改变这个 cap 上界。

仅须另查第 0 胞元的末两段。第 7 段令 $S=S(x)$、$c=\log(0.02_{\rm binary})$，原 log slope 写为

$$
\ell_{\rm raw}=A+BS-\frac{7\ell x}{\sqrt{12}},\qquad B<0.
$$

cut-preserving blend 为 $S\ell_{\rm raw}+(1-S)\ell_{\rm cap}$，且 $\ell_{\rm cap}\le c$，于是

$$
\ell_{\rm blend}
\le c+(A-c)S+BS^2
\le c-\frac{(A-c)^2}{4B}.
\tag{31.30}
$$

这对整个 $0\le x\le1$ 成立，不采样转接。准确参数的 192-bit Arb 计算给

$$
\exp\!\left(c-\frac{(A-c)^2}{4B}\right)
<0.103740139967422856<0.12.
$$

第 8 段为严格递减的原 slope，其左端上界为

$$
w<0.080048512125582782<0.081.
\tag{31.31}
$$

所以整个第 0 胞元仍有 $w\le0.4_{\rm binary}$。

**外侧的径向曲率。** 除第 0 胞元第 8 段外，$\chi=1$，且 warp weight 严格为正。因此实际 $r_x$ 含有完整 $|w_x|/(8E^{3/2})$ 项，立即给径向曲率 $\le8$，包括 cap、valley 和第 7 段 blend 的真实导数。

第 0 胞元第 8 段令

$$
\chi=1-S,\qquad
j_0=1+\left(\frac{r_{\rm Cut}}{\mathrm{oldCut}}-1\right)S,\qquad
T=\frac{7w}{8r_oE^{3/2}}.
$$

oldCut 是 factory 捕获的那个二进制参数，不是真实 $R_{\rm out}$。准确参数给 $r_{\rm Cut}/\mathrm{oldCut}>5$，而由 (31.31) 与 $r_o\ge r_c$ 有 $T<1.5$、$E<2$。实际半径公式准确满足

$$
\frac{r_x}{(r_o)_x}-T
=S(j_0-T)+\frac{\alpha_{\rm warp}(1-S)}E.
\tag{31.32}
$$

若 $S\le1/2$，首项大于 $-1/4$，第二项大于或等于一个严格大于 $1/2$ 的数；若 $S\ge1/2$，则 $j_0>3>T$，两项均非负。故 $r_x\ge T(r_o)_x=|w_x|/(8E^{3/2})$，该段径向曲率也 $\le8$。

**外侧的环向曲率。** 不能把略小于 $0.05$ 的 binary $r_c$ 与略大于 $0.4$ 的 binary cap 直接相除后仍称 $\le8$。第 0 胞元的所有半径严格大于 R26 的 node12 半径；其已认证下端为

$$
r_{12}\ge
1256145971708405051267622360403103502687023912083750456337
\cdot2^{-194}
>0.05002.
\tag{31.33}
$$

因此第 0 胞元环向曲率小于
$0.4_{\rm binary}/0.05002<7.997<8$。
第 1 至 11 胞元则小于 $0.02_{\rm binary}/r_c<0.401<8$。这不需要重新积分外 12 层，也不借用名义外半径。

合并各区得到同一个 R26 实背景的结论

$$
\boxed{\text{全部 }n\ge0\text{ 的 }K_0\le8,\qquad
w,w_r\longrightarrow0\quad(r\downarrow r_c).}
\tag{31.34}
$$

上述检查的恢复版本是
[tail_real_background_curvature.py](../computations/tail_real_background_curvature.py)
及 [recovered-background-ledger.json](../notes/2026-11-12-tail-r31-recovered-background-ledger.json)。
它只构造第 0 胞元的解析端点数据并作少量 Arb 运算；不构造 RealHead、不重新执行径向积分，也不启动尾部求解。所有依赖保存文件及脚本的 hash 均记入账本。

非轴实际高度的连续强范数仍须另付；(31.34) 不把第 4 节的条件非线性曲率界宣称为当前 finite Robin 尾的结论。

## 5. 实际有限强 H 头部需要提供什么

应用第 3 节于实际强幅解，应按原固定 $g$ 提供以下完整数据：

1. 每个真实径向区间上的 $r,E,E',w,w_r$ 包络及所用实数定义；不能只引用配置字段或混用 split 与 direct 算术层。
2. 同一高度函数的完整 $H/P/Q$ Fourier 系数或函数包络，特别包括 $p_0,q_0$，以及未表示频率、真实 mean 根和径向近似误差的界。
3. (31.7) 三个组合量在整个区间的上界，以及 $\beta,\varepsilon$；接缝必须与该同一函数的两 jet 相容。
4. 若使用 R23 深球推论，必须给逐模全胞元强范数和真实 $\Xi$，以及该背景的连续 $K_0\le8$。

这些输入支付的是曲率和正投影。仍需 R21/R30 的全局图/精确切口、真实内 cuff 与 R27 辅助外延，才能调用 R25；与其余闭面部分的点对继续使用 R11/R16/R24。第 4 节的 $8.001$ 不是当前完整强幅曲面的已测或已证总曲率。

若实际相位族的高度只按物理角 $\theta$ 平移，完整复 Fourier 系数只乘单位复数，上述组合范数及主曲率上界同时适用于所有相位。这里的角必须是物理 $\theta$；不能用前缀参考图的计算角 $\eta$ 直接替换。

## 6. 准确有理账本与已支付的切口实例

[tail_curvature_transfer_bounds.py](../computations/tail_curvature_transfer_bounds.py)
及其输出
[curvature-transfer-ledger.json](../notes/2026-11-12-tail-r31-curvature-transfer-ledger.json)
以准确分数验证 (31.23)，得到

$$
\frac{8(1+L_*)}{1-\varepsilon_*}
<8.000488340921,\qquad
\frac{1-\varepsilon_*}{1+\sigma}>0.9999999403917.
\tag{31.35}
$$

这支付第 4 节条件蕴含中的常数比较，仍未声明当前轨道的强球已经支付。当前 R26 新实背景的全部层曲率另由第 4.2 节及其恢复账本支付；两个账本的数学对象与输入哈希分别保留。

同一工具读取 R30 的 M16 邻近 exact cut、完整 mean 根区间及完整 $Q$ 修正界，使用未改动的直接保存 $E,E'$ 和一般门 (31.9)。包括 mean 和未表示修正之后，得到

$$
\boxed{|\kappa_{\rm corrected\ cut}|<1.850621954020<1.851.}
\tag{31.36}
$$

它与 R30 的辅助外环界 $1.960186488$ 是两个不同位置的界。此切口实例既没有使用 $E=1+w^2$ 的静默替换，也没有引用未通过的 $\log2$ 解析条带门；输出保留了直接算术层的背景恒等式差值。

复算：

    python computations/tail_curvature_transfer_bounds.py \
      --cut-response notes/2026-11-12-root-vu032-q085-actual-resumable-m16-tail-response_0003.json.gz \
      --cartesian-enclosure notes/2026-11-12-tail-r30-actual-m16-cartesian-enclosure.json \
      --out notes/2026-11-12-tail-r31-curvature-transfer-ledger.json

真实有限头仍需第 5 节列出的全径向输入。只对已存 shooting 状态评估 (31.9) 的诊断即使有正余量，也仅能定位哪一个胞元需要优先包围，不能省去该胞元内部、源实积分、同一高度函数两 jet 和全频误差。
