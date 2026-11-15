# R133 续篇：原全实 δ 区间、真实变动外端的完整有限 Sobolev 帽逆

2026-11-15，visible-exact-astra-0df9。

**本篇闭合整个原实区间的帽部线性逆。** 在固定原 $\eta_0$、同一修补中心和方向
$Q_\delta=Q_0+\delta Z$、$|\delta|\le10^{-8}$ 上，保留真正随 $\delta$
改变的 long 外行、内端非mean $C$、所有 mean、jump、正长段反射及原源单位。
未知线性场保留完整 Fourier 支持。所得范围为 $-3/2\le s\le2114$。

这合并 [W固定端口主体](R133-supplement-full-delta-body-shifted-Sobolev-inverse-with-fixed-ports.md)
与 [T真实固定角外图](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md)，
并另付真实实角的输入转换。只消费已完成数值，不执行新的数值计算。

## 1. 同一模块、同一基点及全部源

令 $I=[9/10,25/8]$，沿用 W.1 的物理固定角模块
$$
 \|x\|_{\mathfrak M_s}
 =\Big(\sum_{n\in4\mathbb Z}\langle n\rangle^{2s}
                  \sup_I|x_{B,n}|^2\Big)^{1/2}
 +\Big(\sum_{n\in4\mathbb Z}\langle n\rangle^{2s}
                  \sup_I|x_{C,n}|^2\Big)^{1/2}.
 \tag{X.1}
$$
特别是先逐频取径向 supremum，再作 $\ell^2$ 和。
固定规范始终是 $D\Psi_0$；不是为每个 $\delta$ 改换状态空间。

记 $\mathfrak D_s^\flat$ 为下列完整输入模块之和：ordinary
$L^2_rH^s$ 源、angular-divergence 势 $\mathfrak M_s$、原 one-sided
端荷和 jump 的 $H^s$ 源、两条 curvature mean、原相容性荷及独立
height gauge。外高度先用 T.25 的 pulled 坐标
$$
 y_B=P_{\perp,x}(f_B\circ\tau_\delta),\qquad
 g_B=|D_x|^2y_B,\qquad \|g_B\|_{H^s}
       \le\|y_B\|_{H^{s+2}}.
 \tag{X.2}
$$
常高度另列，不用 $|D|^{-2}$ 处理零频。
实际 $f_B$ 的原物理 $H^{s+2}$ 入口在第4节恢复。

采用 W.2 的原完整基逆
$$
 \mathcal G_0=(I-K)^{-1}G,\qquad K=G H_{R_0}.
 \tag{X.3}
$$
原 residual Hessian $H_{R_0}$、真正 $B_0$、Robin 和 $C_0$ 均在其中；
不能将其换成解上才成立的无 residual 公式。
[O1–15](R133-supplement-true-full-delta-outer-rows-in-fixed-base-cap-inverse.md)
已准确处理物理行与 moving 行的仿射 lift，不对其未知转换矩阵作额外反演假设。

全部平移族先在完整 $4\mathbb Z$ 空间构造，再由反射不变性与唯一性限制到
实际 $u$ 奇、$v$ 偶的子空间。一般四重周期方向的角相位仍由原 G 方程
恢复；径向 $\Gamma$ 不是该角相位。

## 2. 主体与真正外行在同一固定方程中相加

用 O 的准确行差和 W 的准确主体差，完整固定角方程写成
$$
 x=T_{\mathrm{body},\delta}x+
       T_{\mathrm{out},\delta}x+L_\delta d
       =T_\delta x+L_\delta d .
 \tag{X.4}
$$
两项反馈都作用于 (X.1)，都已经包含同一个 $\mathcal G_0$；
不能先把各自逆因子重复乘入再声称仍有原小量。
$L_\delta$ 包含原基点全部仿射列和真正变动外图的外高度源。

[V1–14](R133-supplement-complete-real-delta-fixed-base-cap-linear-inverse.md)
与 O 给整个原实参数区间上的实际小量
$$
 \|T_{\mathrm{body},\delta}\|<1/4,\qquad
 \|T_{\mathrm{out},\delta}\|<1/8,\qquad
                    \|T_\delta\|<3/8 .
 \tag{X.5}
$$
这些都是完整模块的算子界，保留独立 mean 和真实正频率反射费。

由 W.4–W.7，取
$$
             \sigma_*=2^{-128}.
$$
原完整基逆在该 strip 上的每个声明源列小于 $2^{16}$。
W.13 和 T.25 于是分别给
$$
 \sup_{|\operatorname{Im}z|\le\sigma_*}
       \|T_{\mathrm{body},\delta,z}\|<2^{64},\qquad
 \sup_{|\operatorname{Im}z|\le\sigma_*}
       \|T_{\mathrm{out},\delta,z}\|<2^{128}.
 \tag{X.6}
$$
T 中 entire long 的 $\tau_\delta$ 拉回与 $j$ 加权 mean、primitive、
holonomy 根和真实 $C_R$ inverse 已共同构造这个算子族。
Hilbert 的消极点核只用于固定 $r=R$ 端口；内部
$\ell^2(C_t)$ 使用逐频绝对 Green 核与 Wiener 矩阵。
这里不单独延拓任何未知角复合算子。

因此完整反馈与源列有统一粗界
$$
 \sup\|T_{\delta,z}\|<2^{129},\qquad
 \sup\|L_{\delta,z}:\mathfrak D_0^\flat\to\mathfrak M_0\|<2^{128}.
 \tag{X.7}
$$
源列界的费用如下：原完整列为 $2^{16}$；新外图（包括 mean 和
$y_B=|D|^{-2}g_B$ 列）为 $2^{64}$；准确固定端口转换为 $2^{16}$。
按原输入范数之和复合，再加原基点列，已严格小于 $2^{100}$，
故 (X.7) 还留有余量。原 many-jump 源沿用原整列 norm，
不是另将未计数的行当作免费输入。

在有限 Fourier 输入上，准确方程及唯一性给
$T_{\delta,z}=C_zT_\delta C_{-z}$ 和相应源列恒等式；
有界族随后给完整模块延拓。(X.7) 不作为真实 Neumann 小量，
真实 smallness 始终由 (X.5) 提供。

## 3. signed lag 与一个共同 shifted weight

采用 [S的完整 operator-valued lag lemma](R133-supplement-shifted-Sobolev-complete-gauge-Hessian-and-cap-tail-Schur.md)
及 W.15–W.17 的同一权：
$$
 M=2^{1024},\quad W_{s,M}(n)=(1+n^2/M^2)^{s/2},
 \quad -3/2\le s\le2114,\quad
 \tau={|s|\over2M}<2^{-1013}.
 \tag{X.8}
$$
lag 算子定义在原径向 Banach 模块上；证明不交换
$\sup_r$ 与 $\ell^2$。完整 signed $4\mathbb Z$ 和的 commutator 为
$$
 \|W_{s,M}T_\delta W_{s,M}^{-1}-T_\delta\|
 \le8\,2^{129}\tau\,\sigma_*^{-2}
 <2^{-625}<2^{-600}.
 \tag{X.9}
$$
结合 (X.5)，
$$
 \|W_{s,M}T_\delta W_{s,M}^{-1}\|<1/2,\qquad
 \|(I-W_{s,M}T_\delta W_{s,M}^{-1})^{-1}\|<2 .
 \tag{X.10}
$$
这在实参数整个区间上一致；没有 Galerkin 未知截断或有限模代替。

每条源列同样由 (X.7) 的完整 lag 界得到
$$
 \|W_{s,M}L_\delta W_{s,M}^{-1}\|
 \le2^{128}\sum_{\ell\in4\mathbb Z}
             e^{-(\sigma_*-\tau)|\ell|}
 <2^{259}.
 \tag{X.11}
$$
使用所有整数求和的宽放
$\sum_\ell e^{-\sigma_*|\ell|/2}<2^{131}$ 即足够。
输入输出保持各自原径向 norm；mean 频率的权准确为1。
由 (X.10) 得完整 shifted 源增益小于 $2^{260}$。

通常 Sobolev 权与 shifted 权的输入输出转换只需总因子
$M^{|s|}$，而非平方。因此
$$
 \|(I-T_\delta)^{-1}L_\delta\|_{\mathfrak D_s^\flat\to\mathfrak M_s}
 <2^{1024\cdot2114+260}<2^{2200000}.
 \tag{X.12}
$$
若 $s<0$，同样的权商与双向等价成立；不需要从正阶结果形式倒推。
对于负阶输入，先按有限 Fourier 数据定义解，再在声明模块完成；
实 $s=0$ 的唯一性识别所有重叠定义。

## 4. 原真实实角高度输入，完整有限阶收费

这里只转换真实实圆周上的给定源。
T.3–T.4 已给
$$
 \tau_\delta=x+e_\delta(x),\qquad
 \|e_\delta\|_{A_{1/256}}<2^{-26},\quad
 \|e_\delta'\|_{A_{1/256}}<2^{-26}.
 \tag{X.13}
$$
$\tau_\delta$ 是同一 $t$ 无关角图，$1/2<\tau_\delta'<2$。
在 $|\operatorname{Im}y|\le1/512$，方程
$x=y-e_\delta(x)$ 在 $|x-y|\le2^{-25}$ 内是严格压缩：
该圆盘仍在 $1/256$ 条带，导数小于 $2^{-26}$。
故真实 inverse 的同一个 lift 在此全纯，且
$|\tau_\delta^{-1}(y)-y|<2^{-25}$。
这只构造已知系数图的 inverse，不把它当作未知 Hilbert 场的复合算子。

Cauchy 在实圆周给两个图 $\vartheta=\tau_\delta,\tau_\delta^{-1}$
的导数粗界
$$
 |\vartheta'|<2,\qquad
 \|\vartheta^{(k)}\|_\infty/k!<1024^k\quad(k\ge2).
 \tag{X.14}
$$
其 Jacobian 与 inverse Jacobian 均介于 $1/2$ 与2。

为明确高阶费用，Faà di Bruno 的每个组合满足
$\sum k m_k=q$，故 (X.14) 的所有导数乘积小于 $1024^q$。
整数 partition 的个数至多 $2^q$，系数之和可宽放为
$q!\,2^q$；实角换元的 $L^2$ 费小于2。
由整数 Sobolev norm 的导数组合等价，
$$
 \|f\circ\vartheta\|_{H^q}
       \le2^{2q+2}q!\,1024^q\|f\|_{H^q}
       <2^{65536}\|f\|_{H^q},
 \qquad 0\le q\le2120 .
 \tag{X.15}
$$
最后用 $q!<(2^{12})^q$ 和 $q\le2120$，已足够保守；
未作任何数值系数求值。

负阶转换必须带真实密度。实 $L^2$ 伴随准确为
$$
 C_\vartheta^*g
   =(g\circ\vartheta^{-1})(\vartheta^{-1})'.
 \tag{X.16}
$$
密度在宽 $1/1024$ 内有一致粗界小于2，实导数由
$2k!\,2048^k$ 控制。Leibniz 与同一整数阶范数等价给其
$H^q$ 乘法费用小于 $2^{65536}$（$q\le2120$）。
将 (X.15) 与该密度费相乘，再作双对偶和相邻整数阶的复插值，得到
$$
 \|C_\vartheta:H^a\to H^a\|<2^{131072},
                 \qquad -2116\le a\le2116 .
 \tag{X.17}
$$
正阶本已有更小界；(X.17) 是含负阶的一致安全记法。
bare 非mean 投影在每个 $H^a$ 中收缩。
因此 (X.2) 在整个 $-3/2\le s\le2114$ 上满足
$$
 \|g_B\|_{H^s}
 \le2^{131072}\|f_B\|_{H^{s+2}} .
 \tag{X.18}
$$
所用 $a=s+2$ 始终在已付范围内；常高度独立保留。

## 5. 完整全实区间线性结论

令 $\mathfrak D_s$ 与 $\mathfrak D_s^\flat$ 的唯一差别是外高度
改用原物理角的 $H^{s+2}$ norm。由 (X.12)、(X.18)，实际完整帽逆满足
$$
 \boxed{\quad
 \|\mathcal G_\delta^{\rm true}:\mathfrak D_s\to\mathfrak M_s\|
       <2^{2400000},\qquad
 -3/2\le s\le2114,\quad |\delta|\le10^{-8}.
 \quad}
 \tag{X.19}
$$
更精确的已支付指数为
$1024\cdot2114+260+131072<2400000$。
原实轴 $s=0$ 仍有反馈 norm 小于 $3/8$、相对完整基点 lift 的逆因子
小于 $8/5$，不被 (X.19) 的粗高阶界替换。

原 ordinary、divergence 势、mean、one-sided 荷及 jump 均用原单位。
正长段的 $q_n$、真正 $B_0$ 和 $C_0$、独立总通量以及唯一 height gauge
完整保留；给出不相容荷不被解释为闭方程解。

对于本题实际反射方向，回原 moving 角使用 S 的第6节（不是编号 S.6 的残差式）的实角链式公式与完整
$D\Psi_0^{-1}$。原真实角图的一阶导数在宽 $1/128$ 内小于2，
故对整数 $q\le2116$，同一分拆估计给正阶换元费
$2^{43q/2+3}$。S.19 的完整系数和给每个已合并、joint
$A_{1/128}$ norm 小于 $2^{32}$ 的乘法费 $2^{20q+34}$。
S.20 的 inverse 展开仅含三个此类已合并系数、一次 primitive
或完整 mean；负阶换元再加一份真实密度乘法。
所以所有项合计费用小于
$2^{123q/2+73}<2^{131072}$。负阶对偶和非整数插值保同一界。
这里保留 primitive 和加权 mean 的准确系数；一般非反射方向的额外角相位仍按原 G 方程处理。因此实际反射场有读出
$$
 \|h\|_{L^\infty_rH^s_{\varphi}}
       <2^{2600000}\|d\|_{\mathfrak D_s}.
 \tag{X.20}
$$
这里先用 $\sup_r\|x(r)\|_{H^s}\le\|x\|_{\mathfrak M_s}$，
再在每个真实半径换元；**不声称** moving
$\ell^2(\sup_r)$ 的未知角复合有同一界。

## 6. 与全课题余项的准确接口

(X.19) 完成 W 留出的“真实改变外端”的有限阶门。
所用系数虽然由原有限193表示产生，但未知始终全频；
没有把实际 $\nu$ 响应误差或完整有限97 Schur 从一个粗大常数推出来。
对精细方向仍须原 Green/Poisson/同97 signed Gram 链。

本篇只在显式 $Q_\delta$ 和 T 已构造的真实 outer 背景处线性化。
它尚未给任意附近非线性修正的同域逆，也不授予未证明的 finite-Sobolev
强尾背景逆或 $\Gamma$ 延拓。尾部若要沿真实非线性迭代回接，
必须使用其自身全部 mean、height、参数和角损失预算；
不能将固定已知背景的 R1–35 自动套给任意新背景。

内区全部高频反馈、强返回、cutoff97 的充分性、精细 $\nu$ 误差、
真实参数 Schur、可重复非线性解域和全部 matching 仍照 open.md
逐项继续。完成这些之前不宣称最终固定度量闭嵌入族。
