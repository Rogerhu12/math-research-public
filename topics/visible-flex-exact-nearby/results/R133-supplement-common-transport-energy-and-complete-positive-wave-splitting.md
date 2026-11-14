# R133：共同输运的精确能量抵消与完整正区波分解

2026-11-14，visible-exact-astra-0df9。

**状态：已证明。** 本文给同一完整 moving Codazzi 线性算子的代数、
能量和 Fourier 支持恒等式。只在严格 $K>0$ 的径向区间使用正区
归一化；不要求所用连续修补背景已经满足非线性方程。
本文没有新的数值计算，也不宣称全低高 Schur 或帽端逆已经闭合。

与 [实际 M32 交叉费用](R133-supplement-actual-M32-body-cross-weighted-Green.md)
及 [完整帽边界](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md)
使用同一背景、物理角和均值。下述完整生成元也正是
[regular-cut interval model](../scripts/fourfold_codazzi_regular_cut_interval_model.py)
中 raw_generator 在有限正交基上的压缩；该源码 SHA256 为
b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183。

## 1. 完整向量场与真实均值列

圆周测度归一为 $d\phi/(2\pi)$，Fourier 频率为 $k=4j$。
$\Pi$ 表示均值，$P=1-\Pi$。$I=\partial_\phi^{-1}P$ 是零均值
primitive，因此 $I^*=-I$、$\partial_\phi I=P$，
且 $\|I\|_{L^2\to L^2}\le1/4$。

背景 $Q=(u,v)^{\mathsf T}$ 满足原反射类：$u$ odd，$v$ even。
固定 intrinsic 参数，记
$$
m=\Pi v,\quad S=u^2+Kv^2,\quad
d=-\beta I S,\quad
J_K=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
W=(u,Kv)^{\mathsf T}.
$$
$\beta,\gamma,K,m$ 都只依赖 $r$。完整向量场为
$$
 {\cal F}(Q)
 =dQ_\phi+\gamma mJ_KQ_\phi+
       \beta\operatorname{diag}(-1,1)Q-\beta SQ.
 \tag{V.1}
$$
对任意完整 $h=(h_1,h_2)$，$h_1$ odd、$h_2$ even，设
$z=\Pi h_2$。逐项求导得到
$$
\begin{split}
 {\cal A}h=D{\cal F}(Q)h
 ={}&d h_\phi+\gamma mJ_Kh_\phi\\
 &+\beta\{\operatorname{diag}(-1,1)-S I_2-2QW^{\mathsf T}\}h\\
 &-2\beta Q_\phi I(W^{\mathsf T}h)
       +\gamma zJ_KQ_\phi .
\end{split}
 \tag{V.2}
$$
这里 $I_2$ 是二阶单位矩阵，与 primitive $I$ 区别。
第二行是完整乘法矩阵；第三行是完整 primitive 与独立均值列。
证明只用 $\delta S=2W^{\mathsf T}h$、
$\delta d=-2\beta I(W^{\mathsf T}h)$ 和 $\delta m=z$。
没有从 $h_2$ 中删去均值。intrinsic 或其他参数方向的完整额外项
进入实际源 $f$，不被 (V.2) 视为零。

## 2. 共同输运的斜伴随恒等式

对每个固定 $r$，背景和参数先取实值。定义
$$
 {\cal T}=d\partial_\phi+\tfrac12d_\phi .
 \tag{V.3}
$$
周期积分分部直接给出
$$
 \langle a,{\cal T}b\rangle=-\langle{\cal T}a,b\rangle .
 \tag{V.4}
$$
此式先对 $H^1$ 测试函数成立。当前平滑圆周系数的流 $\Phi_t$
还给出酉群
$U_t f=\sqrt{\Phi_t'}\,f\circ\Phi_t$；
换元证明其保 $L^2$ 范数，在光滑函数上的生成元就是 (V.3)。
所以相应闭生成元斜自伴。本篇的频率结论只需 (V.4)。

若 $d_q$ 为真实 Fourier 系数，直接计算得
$$
 {\cal T}_{k\ell}=\frac i2(k+\ell)d_{k-\ell},
 \qquad {\cal T}_{k\ell}=-\overline{{\cal T}_{\ell k}}.
 \tag{V.5}
$$
令 $P_L,P_H$ 为互补正交 Fourier 投影，则
$$
 {\cal T}_{LH}=-{\cal T}_{HL}^*,\qquad
 \Re\langle y_L,{\cal T}y_H\rangle+
 \Re\langle y_H,{\cal T}y_L\rangle=0.
 \tag{V.6}
$$
两个分量分别成立。因而在同一 $L^2$ 能量中，输运头尾交叉
可以精确保留为相消的一对。把两个方向先分别绝对值放大
会丢掉这一恒等式；各自已有 upper 仍是合法 upper。

(V.6) 只涉及输运部分。完整 $\mathcal A_{LH}$ 与
$\mathcal A_{HL}$ 还有 (V.2) 的乘法、primitive 和均值项，
它们没有被声明为互为负伴随。

## 3. 正区的径向归一化及完整零阶部分

在一个严格正区间令
$$
 \kappa=\sqrt K>0,\qquad \eta=-\gamma m>0,\qquad a=\eta\kappa,
 \quad D_\kappa=\operatorname{diag}(\kappa,1),
 \quad y=D_\kappa^{-1}h,\quad
 q=(u,\kappa v)^{\mathsf T},
 \quad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
对 $h_r={\cal A}h+f$，准确代入 (V.2) 得
$$
 y_r={\cal T}y-aJ y_\phi+{\cal B}_\kappa y+D_\kappa^{-1}f,
 \tag{V.7}
$$
其中
$$
\begin{split}
 {\cal B}_\kappa y={}&
 \left[
 \beta\{\operatorname{diag}(-1,1)
       -\tfrac12(S+\Pi S)I_2-2qq^{\mathsf T}\}
       -\operatorname{diag}(\kappa_r/\kappa,0)
 \right]y\\
 &-2\beta q_\phi I(q^{\mathsf T}y)
       +\gamma(\Pi y_2)Jq_\phi .
\end{split}
 \tag{V.8}
$$
这是完整恒等式，不是主符号近似。

为核对各项，首先
$D_\kappa^{-1}J_KD_\kappa=\kappa J$，
$D_\kappa^{-1}QW^{\mathsf T}D_\kappa=qq^{\mathsf T}$。
其次，primitive 项内外的径向 $\kappa$ 因子准确抵消：
$$
 D_\kappa^{-1}Q_\phi I(W^{\mathsf T}D_\kappa y)
     =q_\phi I(q^{\mathsf T}y).
$$
均值列变为 $\gamma(\Pi y_2)Jq_\phi$。
径向换变量给 $-\operatorname{diag}(\kappa_r/\kappa,0)$，
不能把它忘掉。最后
$d_\phi=-\beta(S-\Pi S)$，故
$-\beta S I_2-\tfrac12d_\phi I_2
=-\tfrac12\beta(S+\Pi S)I_2$，得到 (V.8)。

对实背景，$S=|q|^2$。设
$q_\infty=\|q\|_{L^\infty}$、
$q_{\phi,\infty}=\|q_\phi\|_{L^\infty}$、
$q_{\phi,2}=\|q_\phi\|_{L^2}$，其中点态向量范数为 Euclidean。
完整零阶算子满足
$$
 \|{\cal B}_\kappa\|_{L^2\to L^2}
 \le |\beta|(1+3q_\infty^2)
      +|\kappa_r/\kappa|
      +\tfrac12|\beta|q_{\phi,\infty}q_\infty
      +|\gamma|q_{\phi,2}.
 \tag{V.9}
$$
乘法部分用 $\Pi S\le q_\infty^2$ 和
$\|qq^{\mathsf T}\|\le q_\infty^2$；primitive 部分用
$\|I\|\le1/4$；均值列用 $|\Pi y_2|\le\|y\|_2$。
此证明保完整均值，不引入角导数损失，也不假设背景是解。

尤其 (V.8) 的大乘法项仍可以保留其真实符号，而无需先用 (V.9)
的绝对值。对复测试函数和实背景，
$$
\begin{split}
 \Re\langle y,{\cal B}_{\kappa,\mathrm{mult}}y\rangle
 ={}&\beta(\|y_2\|_2^2-\|y_1\|_2^2)
 -\tfrac{\beta}{2}\int(S+\Pi S)|y|^2\\
 &-2\beta\|q^{\mathsf T}y\|_2^2
 -(\kappa_r/\kappa)\|y_1\|_2^2 .
\end{split}
 \tag{V.10}
$$
primitive 与均值两项继续完整加入能量式。
因此 (V.7) 的共同输运对
$\tfrac12\partial_r\|y\|_2^2$ 恰为零。
本文没有假定 $\beta$ 在所有径向区间同号。

## 4. 两个正区波及其准确范数

定义圆周算子
$$
 {\cal J}e^{ik\phi}=i\,\operatorname{sgn}(k)e^{ik\phi},
 \quad {\cal J}1=0,\qquad
 |D|=-{\cal J}\partial_\phi .
$$
$\mathcal J^2=-P$，且 $\mathcal J$ 在非均值空间上等距。
记 $x=Ph_2$，并定义
$$
 s=\tfrac12(x-{\cal J}h_1/\kappa),\qquad
 t=\tfrac12(x+{\cal J}h_1/\kappa),\qquad
 \zeta=t-s .
 \tag{V.11}
$$
这里 $t$ 是波变量，不是非线性族参数。反变换为
$$
 h_1=-\kappa{\cal J}\zeta,\qquad h_2=s+t+z,\qquad
 \kappa^{-2}\|h_1\|_2^2+\|h_2\|_2^2
 =2\|s\|_2^2+2\|t\|_2^2+|z|^2.
 \tag{V.12}
$$
所以 $y\mapsto(\sqrt2s,\sqrt2t,z)$ 是完整反射类上的酉坐标变换。
独立 even mean 是第三个坐标，绝不被归入波零模后丢弃。

令 $\mathfrak r$ 是 (V.2) 后两行作用于 $h$ 后再加完整 $f$，
即 $h_r=d h_\phi+\gamma mJ_Kh_\phi+\mathfrak r$。
设
$$
 {\cal C}=P[{\cal J},d]|D|.
 \tag{V.13}
$$
完整两波方程是
$$
\begin{split}
 s_r={}&P d\,\partial_\phi s-a|D|s
       -\tfrac12{\cal C}\zeta
       +\frac{\kappa_r}{2\kappa}\zeta
       +\tfrac12(P\mathfrak r_2-\kappa^{-1}{\cal J}\mathfrak r_1),\\
 t_r={}&P d\,\partial_\phi t+a|D|t
       +\tfrac12{\cal C}\zeta
       -\frac{\kappa_r}{2\kappa}\zeta
       +\tfrac12(P\mathfrak r_2+\kappa^{-1}{\cal J}\mathfrak r_1).
\end{split}
 \tag{V.14}
$$
证明可直接用
$$
\begin{split}
 x_r&=P d\,x_\phi+a|D|\zeta+P\mathfrak r_2,\\
 \zeta_r&=P d\,\zeta_\phi+{\cal C}\zeta+a|D|x
       -(\kappa_r/\kappa)\zeta+\kappa^{-1}{\cal J}\mathfrak r_1 .
\end{split}
$$
这里 $\mathcal J|D|=\partial_\phi$，故
$\mathcal Jd|D|=d\partial_\phi+[{\cal J},d]|D|$；
最后必须施加 $P$，以保真实均值投影。

对 $w=s,t$，
$$
 P d\,\partial_\phi w=P{\cal T}P w-\tfrac12P(d_\phi w).
 \tag{V.15}
$$
因此两个波具有共同的斜伴随输运和对角的
$-a|D|,+a|D|$；余下全部是 (V.9)、(V.13) 和已写出的
径向换变量项控制的零阶作用。
将 (V.14) 与 (V.8) 结合时，零阶项只能计一次。

## 5. Hilbert 交换子的完整界与有限带支持

对非零物理频率 $k,\ell$，
$$
 {\cal C}_{k\ell}
   =i\{\operatorname{sgn}(k)-\operatorname{sgn}(\ell)\}
        |\ell|d_{k-\ell}.
 \tag{V.16}
$$
若同号，此条目精确为零。若异号，则
$|\ell|\le|k-\ell|$。Young 卷积不等式因此给
$$
 \|{\cal C}\|_{L^2\to L^2}
 \le2\sum_q|q||d_q|
 =2\|d_\phi\|_{\mathcal A^0}.
 \tag{V.17}
$$
这是真完整算子界，不要求把输出截断。
若 $d$ 不是有限 Fourier 多项式，只要右端有限，结论仍成立。

若 $d$ 在指标 $j$ 上的带宽为 $b$，(V.16) 的非零条目还必须满足
$$
 k=4j,\quad \ell=4n,\quad
 jn<0,\quad |j|+|n|\le b .
 \tag{V.18}
$$
输入或输出为零时 (V.13) 已使该条目为零。

对固定修补 M32 背景 $\delta=0$，$u,v$ 带宽 32，
故 $S$、$d$ 带宽至多 64。于是 $\mathcal C$ 的输入和输出都只可能
位于 $1\le|j|\le63$。特别对原 $P_H=P_{|j|\ge97}$，
$$
 {\cal C}P_H=P_H{\cal C}=0\qquad(\delta=0).
 \tag{V.19}
$$
共同输运 $\mathcal T$ 本身并非块对角；其跨越 96/97 的条目
仍位于原 $33\ldots96\leftrightarrow97\ldots160$ 频带。
它们由 (V.6) 保精确相关，而非被 (V.19) 删去。

对显式全族 $Q_\delta=Q_0+\delta Z$，完整 $Z$ 带宽 96，
$S_\delta,d_\delta$ 带宽至多 192。因此
$$
 P_H{\cal C}_\delta P_H=0,
 \tag{V.20}
$$
因为两个异号高指标之和至少为 194。
此时高低交换子条目可以存在，不能把 (V.19) 的两向消失
免费授给非零 $\delta$。
此外
$$
 \|{\cal C}_\delta-{\cal C}_0\|
 \le2\|(d_\delta-d_0)_\phi\|_{\mathcal A^0}.
$$
在 intrinsic 系数与 $\delta$ 无关的本正区，
$(d_\delta-d_0)_\phi$ 准确等于
$$
-\beta P\{2\delta(u_0Z_u+Kv_0Z_v)
                  +\delta^2(Z_u^2+KZ_v^2)\}.
$$
所有 full mean 均在这些乘积中。
实际非线性修正背景通常不再有限带；它必须另付 (V.17) 的真实费用，
不能沿用 (V.19)–(V.20) 的有限带断言。

## 6. 真实均值方程与非解中心

直接对 (V.1) 第二分量取均值，用
$\Pi(dv_\phi)=-\Pi(d_\phi v)$，得
$$
 \Pi{\cal F}_2(Q)=\beta(1-\Pi S)m.
$$
再线性化，$h_r={\cal A}h+f$ 的完整均值行是
$$
 z_r=\beta(1-\Pi S)z
        -2\beta m\,\Pi(uh_1+Kvh_2)+\Pi f_2.
 \tag{V.21}
$$
等价地，写 $v=m+v^\perp$、$h_2=x+z$：
$$
 z_r=\beta(1-\Pi S-2Km^2)z
       -2\beta m\,\Pi(uh_1+Kv^\perp x)+\Pi f_2.
 \tag{V.22}
$$
(V.14) 的 $P$ 与 (V.21) 一起才是完整系统；
$Pd\partial_\phi$ 不能被解释为“该输运没有真实均值输出”。

修补中心一般有非零残差
$R_*=Q_r-{\cal F}(Q)$。故背景自己的 mean 满足
$$
 m_r=\beta(1-\Pi S)m+\Pi(R_*)_2 .
$$
只有中心确实是解时才可去掉最后一项。
前述 (V.2)、(V.7)、(V.14)、(V.21) 均未用该错误的无残差替换。
这也说明输运的斜伴随性质不能消去
[完整共轭残差 Hessian](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)。

## 7. 真实端口、源与使用范围

本变换在 $K>0$ 的闭区间内逐点可逆，所有端点数据按 (V.12)
准确转换。真实接口跳 $[h]=g$ 给
$[y]=D_\kappa^{-1}g$，mean 跳为 $\Pi g_2$；
同一 $s,t,z$ 线性变换作用于全部跳。没有人为建立新物理接缝。

普通源变为 $D_\kappa^{-1}f$。若实际源含 $\partial_r H$，
必须使用
$$
 D_\kappa^{-1}\partial_rH
 =\partial_r(D_\kappa^{-1}H)-(D_\kappa^{-1})_rH,
$$
并保留 total-flux 端口；$\partial_\phi$ weak 源因 $D_\kappa$
仅径向而与其交换。本文不把 weak 源自动换成普通 $L^2$ 源，
也不由主体 $L^2$ 范数控制独立切口迹。

以原有限系统的 $x=R h$、
$R=\operatorname{diag}(I_{96},\rho I_{97})$ 表示同一能量时，
其准确度量为
$\operatorname{diag}(\kappa^{-2}I_{96},\rho^{-2}I_{97})$。
更一般的非酉 QR/frame、角向 Sobolev 权或帽共轭必须携带
相应拉回度量及其变化；在未经转换的 Euclidean 范数中，
不能继续直接套用 (V.6)。径向 frame 导数和角向交换子都要付清。

最后，忽略所有零阶项而保留正区主部时，稳定代数关系为
$h_1=\kappa{\cal J}Ph_2$，即帽行形式主项 $E_0=-\kappa{\cal J}$。
这只是 (V.14) 在 $t=0$ 的主部关系。完整帽图的
$E-E_0$ 平滑阶、真实常数、高低块或伴随关系并未由本文证明；
完整 P1–19 帽行、独立 mean 和全部 Poisson 列仍须使用。

本文可直接用于保留共同输运的 signed 交叉、构造同度量的全矩阵
能量以及完整正区高频系统。真正的两端可解性、参数 Schur、
强返回及非线性状态球仍需各自完成，不能从这些恒等式单独宣布
全无限维逆成立。
