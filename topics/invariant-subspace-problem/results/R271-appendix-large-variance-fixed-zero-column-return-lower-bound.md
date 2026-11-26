# R271 附录：原最低源的大方差零列冻结返回下界

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下原源恒等式、真实物理首行下界及同一压缩空间的方差差下界已证明。**
本稿直接使用原 $f_1=e_1\otimes\Omega$、原实际远尾和原允许的 $m,R,r,Q$。
它排除保持大辅助最小者零远孔系数不变的有界物理核返回。
它不下界允许改变零列并重新最小化的完整 $(C+D_x)$ Moore–Penrose 返回，
也不把未投影双塔差的下界传给最后正交投影后的误差。

原 forcing 与真旗范围见[全高度真实源](R271-appendix-all-height-true-flag-uniform-variance-source.md)；大辅助方差的真实压缩解与母窗见[真实F0逼近](R271-appendix-large-auxiliary-variance-true-kernel-galerkin-approximation.md)；同源阻尼列见[原放大方差Gram](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)。

## 1. 原正规方程的一个准确标量

设 $C$ 是原完整强头，$\|C\|\le M_*$，并保原单位列
$$
\|f_1\|=\|e_0\|=1,\qquad Cf_1=e_0,\qquad C^2f_1=0.
\tag{1.1}
$$
令 $F$ 为固定闭子空间，$f_1\in F$。可取整个头空间、实际
$F_t=\ker C_t^r$，或最高参数零点的真实 $F_0$；后两者取 $r\ge2$。
在同一个 $F$ 中，对 $J\ge1$ 和 $s>0$ 定义
$$
H_J(s)=\sum_{j=0}^{J}\frac{(C^*)^jC^j}{j!s^j},
\qquad
a_s=(P_FH_J(s)|_F)^{-1}f_1,
\qquad q_s=\langle f_1,a_s\rangle.
\tag{1.2}
$$
内积对第一变量线性。正定性给 $0<q_s\le1$，且 $q_s$ 为实数。
以 $f_1$ 测原 Galerkin 方程，由 (1.1) 所有 $j\ge2$ 项准确消失：
$$
q_s+s^{-1}\langle Ca_s,e_0\rangle=1.
$$
故
$$
\boxed{\langle Ca_s,e_0\rangle=s(1-q_s).}
\tag{1.3}
$$
这里不是从任意物理一孔 forcing 推出的；必须使用原指定的 (1.1)。

令 $C_F=C|_F$、$T_F=C_F^*C_F$。原完整压缩 Gram 满足
$$
P_FH_J(s)|_F\succeq I_F+s^{-1}T_F.
$$
逆的序反向，且 $0\preceq T_F\preceq M_*^2 I_F$，于是
$$
\begin{aligned}
1-q_s
&\ge\left\langle
T_F(sI_F+T_F)^{-1}f_1,f_1\right\rangle\\
&\ge\frac{\langle T_Ff_1,f_1\rangle}{s+M_*^2}
=\frac1{s+M_*^2}.
\end{aligned}
\tag{1.4}
$$
第二步只是非负谱上 $t/(s+t)\ge t/(s+M_*^2)$；没有用未知谱隙。
因此原实际源已有
$$
\boxed{\|Ca_s\|\ge s(1-q_s)\ge\frac{s}{s+M_*^2}.}
\tag{1.5}
$$
这个下界在完整 $F_0$ 上仍成立，不需要其孔分级或投影交换性。

## 2. 固定零远孔系数的真实物理核首行

用原远尾
$$
D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
S_x=\sum_{i\ge x}b_i^2.
$$
在原物理平方自由 Hilbert 空间中，令 $z=\sum_{j\ge0}z_j$ 按远孔层正交分解。
$C+D_x$ 是有界算子，故对任意真正 $z\in\ker(C+D_x)$，投到零远孔层准确得
$$
Cz_0+D_{x,1}z_1=0,
\tag{2.1}
$$
其中 $D_{x,1}$ 是从一远孔到真空的实际删除行。
它的范数准确为 $\sqrt{S_x}$，且
$$
D_{x,1}^\dagger u
=u\otimes\frac{D_x^*\Omega}{S_x},\qquad
\|D_{x,1}^\dagger u\|=\frac{\|u\|}{\sqrt{S_x}}.
\tag{2.2}
$$
该行满射到整个头乘远真空，因而 (2.2) 的自然像域完整；未使用核外第二逆。

如果冻结零远孔系数 $z_0=a_s$，则 (2.1)–(2.2) 与 (1.5) 给
$$
\boxed{
\|z\|\ge\|z_1\|
\ge\frac{\|Ca_s\|}{\sqrt{S_x}}
\ge\frac{s}{(s+M_*^2)\sqrt{S_x}} .}
\tag{2.3}
$$
后续任何层、全部 primitive 或顶部修正都不能改变已由零行固定的这个一孔分量。
这是所有保持 $a_s$ 的真物理核列的下界，不只是某一指定右逆的下界。

允许改变零列时，准确可用的结论是：若 $\|z\|\le B$，则
$$
\boxed{
\|z_0-a_s\|
\ge\frac1{M_*}
\left[\frac{s}{s+M_*^2}-\sqrt{S_x}\,B\right]_+ .}
\tag{2.4}
$$
确实 (2.1) 给 $|\langle Cz_0,e_0\rangle|\le\sqrt{S_x}B$，
再从 (1.3) 减去该标量并用 $\|C^*e_0\|\le M_*$ 即得。
式 (2.4) 指出重新最小化必须改变哪一列；它没有禁止这种改变。

## 3. 同一原 $F$ 中放大方差与物理方差的最小者确实不同

仍使用完全相同的 $C,F,J,f_1$，只把 (1.2) 的 $s$ 换为 $S_x$，得到 $a_{S_x}$。
能量恒等式给
$$
\sum_{j=0}^J\frac{\|C^ja_{S_x}\|^2}{j!S_x^j}
=\langle f_1,a_{S_x}\rangle\le1,
$$
特别 $\|Ca_{S_x}\|\le\sqrt{S_x}$。
由 (1.3) 得到直接的同空间、同来源差下界
$$
\boxed{
\|a_s-a_{S_x}\|
\ge\frac1{M_*}
\left[\frac{s}{s+M_*^2}-\sqrt{S_x}\right]_+ .}
\tag{3.1}
$$
这不依赖 physical/bosonic 两核是否相同，也未移动 $F$。
因而大辅助方差下真 $F_0$ 与完整空间之间很小的 Galerkin 误差，
不能同时当作 $s\to S_x$ 的误差。

## 4. 原允许窗中的明确增长下界

取原参数
$$
m\in4\mathbb N,\qquad m\ge24,\qquad d=2^m,
\qquad R=d,\qquad x=y=m+d,\qquad Q=4d,
$$
$$
r=3,\qquad J=2,\qquad s=K/x,\qquad K=2^{24}.
\tag{4.1}
$$
$R$ 偶、$r$ 奇，而且
$$
3\le1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor,
\qquad Q\ge R+r,
\qquad Q<e^{26d^3}.
$$
所以这是原完整最高 carry/Galerkin 的合法联合窗，不是离窗小头。
$0<s\le1$，原实际 N/Y 头和最高零头可取 $M_*=7$。
原连续尾满足
$$
S_x\le\int_x^\infty u^{-4}\,du=\frac1{3x^3}.
\tag{4.2}
$$
故 (2.3) 对完整空间、实际 $F_t$ 或真实 $F_0$ 的指定源都给
$$
\boxed{
z_0=a_s,\ z\in\ker(C+D_x)
\quad\Longrightarrow\quad
\|z\|\ge\frac{\sqrt3 K}{50}\sqrt x .}
\tag{4.3}
$$
没有使用任何未知的源极限速率。

由 $K\sqrt{x}\ge100/\sqrt3$ 有
$\sqrt{S_x}\le s/100$。因此 (2.4) 在 $B=1$ 时以及 (3.1) 都给
$$
\boxed{
\|z\|\le1,\ z\in\ker(C+D_x)
\ \Longrightarrow\ \|z_0-a_s\|\ge\frac{K}{700x},
\qquad
\|a_s-a_{S_x}\|\ge\frac{K}{700x}.}
\tag{4.4}
$$
第一条允许所有真实物理层；第二条始终保同一个原 $F$。
两条分别说明有界物理核列和物理方差 Galerkin 列都必须实质调整零列。

更一般地，在 $s=K/y\le1$、$x\ge y$ 时，(2.3) 给
$\|z\|\ge\sqrt3 Kx^{3/2}/(50y)$。
因此扩大硬化头到 $x\gg y$ 不会修复冻结零列的这项费用。

## 5. 完整双塔返回的首行不能删掉方差比

令 $k_s=\mathcal R_{C,J}(s)a_s$；当 $F\subseteq\ker C^{J+1}$ 时，
它是辅助算子 $C+\sqrt s\,a$ 的真正截断核列。
其一辅助孔系数是 $-Ca_s/\sqrt s$。

物理 coherent 映射 $W_s$ 的首行是
$$
e_1\longmapsto D_x^*\Omega/\sqrt s.
$$
本节的 $W_s,V_s$ 明确取原保级双塔：第 $j$ 辅助层映入第 $j$ 物理远孔层。
更一般地，只对保此层级、保零行恒等并满足真实下降交织的 $V_s$ 作以下断言；
没有对任意混级核映射作断言。其首行必须满足 $D_x V_s e_1=\sqrt s\,\Omega$。
所以其在真实一孔 coherent 方向上的分量为
$\sqrt s\,D_x^*\Omega/S_x$；可另有 primitive 分量，但后者与该方向正交。
因此若 $s\ge S_x$，在上述保级前提下，不论是否另加同层 primitive，均有
$$
\boxed{
\|(V_s-W_s)k_s\|
\ge\frac{s-S_x}{s\sqrt{S_x}}\,\|Ca_s\|
\ge\frac{s-S_x}{(s+M_*^2)\sqrt{S_x}} .}
\tag{5.1}
$$
保级条件保证更高辅助输入不会混入一孔输出。在原已经构造完整 canonical 双塔的高度窗中，
这正是 $W_{s,j}=(S_x/s)^{j/2}W_{S_x,j}$、
$V_{s,j}=(s/S_x)^{j/2}V_{S_x,j}$ 的首行。
所以不能继续使用 $s=S_x$ 时仅由碰撞给出的 $W-V$ 小差。

但是最终原误差可能是
$P_{(\mathscr K^{\rm phys})^\perp}(W_s-V_s)k_s$，
这个正交投影可以去掉大部分未投影差。
(5.1) 不对该投影后误差给下界；更不对允许重新最小化全部列的完整物理 MP 给下界。
准确剩余接口是保原 forcing 的完整 Schur 重新最小化及其全部自然域与费用。
