# R268：居中高低微包的完整 sine-four 面积仍严格非零

日期：2026-11-15。**独立纸面证明；没有执行 profile 求积、扫描、消元、人工测试或几何计算。**

本稿接 [R256 六能量分支](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)、[R262 有序 pure 障碍](R262-ordered-primitive-obstruction-for-the-multiwidth-energy-branch.md)及 [R265 伴随方向支付](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md)。它确定一个在 pure 标量之外的真实剩余项：对于这些**居中 cell 次序**，完整 Gaussian $A_{1,-3}$ 在 $\theta=\pi/2$ 的第零外矩严格非零。伴随母包的符号改变和正四次幅度混合都不改变这个号。

结论只作用于这个准确的正宽隐函数分支及其规定排列，不排所有多宽度、其他真实次序或所有合法 profile 圆。它同时说明 R265 已付一个 pure 必要标量与本稿的完整 sine-four 失败并不矛盾。

主要原式：[R257 真实 primitive](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)及 [R259 完整 self/cross 接口](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)。

## 1. 固定槽、真实系数和完整外矩

记

$$
P=\Phi_{r_0},\qquad Y=\Phi_{p_2},\qquad
P(u,v)=J(u''v''),\quad JF(x)=\int_x^rF.
$$

本稿研究准确量

$$
S_{04}(f,g)
=2I_0\{g,[P,Y](g;f\odot f-g\odot g)\}.
\tag{1}
$$

它是完整 $\theta=\pi/2$ 的外/内三槽表达，不用 pure diagonal 代替。在 R259 的四个角单项式中，它正是这个 pair 的 $\sin^4\theta$ 系数。

共振 germ $\varepsilon=\kappa^2/4$ 的原 Gaussian 方向为

$$
B_1=\zeta Y,\quad \zeta=-\kappa h_e,\qquad
B_{-3}=cP,\quad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}.
\tag{2}
$$

故原 Gaussian 第零矩等于 $-\zeta c\,S_{04}/2$，且

$$
\zeta c=\frac{\kappa^2(41\kappa^4+27)}{216h_e^2}>0
\quad(\kappa\ne0).
\tag{3}
$$

这里是 $A_{1,-3}$，不是 $A_{-1,-3}$。
后一个 pair 的原 $d=6\kappa^3/h_e$、
$e=-\kappa(15\kappa^2+1)/(4h_e)$
只参与其另外的 local 门；支付那些 $d/e$ 条件不会令 (3) 消失。所有原 Gaussian 因子均按原 germ 保留。

## 2. 单个不合法微包的 self：必须保住左端边项

对实紧微包 $u$，写 $v=u'$、$\rho=u''$、$\mathcal A=J(\rho^2)$。这个 $\mathcal A$ 一般有非零左常尾，不能当紧 profile。直接使用原同锚二次式，或 R259 的 local adjoint，得到

$$
2I_0\{u,[P,Y](u;u\odot u)\}
=-D\mathcal F_Y(u)[\mathcal A],
\tag{4}
$$

其中

$$
\mathcal F_Y(u)=\int\left(
xu\rho^2-\frac32x^2v\rho^2+\frac13x^3\rho^3-\frac13v^3
\right).
$$

式 (4) 不需要假设 $\mathcal A$ 紧：$\mathcal A$ 在左 collar 为常数，$u+t\mathcal A$ 的正阶导数仍有零 collar，$\mathcal F_Y$ 的原分部积分仍适用；$D\mathcal F_P(u)[Y(u,u)]=0$ 则直接来自 $\mathcal F_P=-2[(u'')^3]/3$ 的边界式在紧 $u$ 处的一阶导数为零。两条 quadratic cross 配对按原对称积分相消，不重置任何原函数。

R257 的同一完整变分在这里保留

$$
D\mathcal F_Y(u)[\mathcal A]
=\frac12\int\mathcal A^2
-\frac12[x\mathcal A^2]_\ell^r
+\int\left(x^2\rho^4-\frac83xv\rho^3+
\frac43u\rho^3+v^2\rho^2\right).
\tag{5}
$$

若 $m=\int\rho^2$，端项是 $+\ell m^2/2$，不能省略。

对一个 I0 归一 even 母包
$\eta_{w,\xi}=w^{3/2}u((x-\xi)/w)$，
沿用 R262 的母包常数 $m,C,\mathcal L,\Delta$。原积分恒等

$$
\int\mathcal A^2+\ell m^2
=m^2\xi-\frac{w\Delta}{2}
$$

来自 $\min(x,y)=(x+y-|x-y|)/2$。于是准确 self 为

$$
\boxed{
\mathbf S_{P,Y,0}(\eta_{w,\xi})
=-\left[
\frac{m^2\xi}{2}+\frac{C\xi^2}{w}
+w\left(\mathcal L-\frac\Delta4\right)
\right].
}
\tag{6}
$$

R259 的准确有序跨核为

$$
\Gamma_{P,Y,0}(\mathbf m_i,\mathbf m_j)
=-m_{i,1}m_{j,0}=-m^2\xi_i
\quad(i<j).
\tag{7}
$$

这两个式子一起消费；不得只取 (6) 的局部 quartic 项。

## 3. 居中 cell 的原物理数据

令 $n=2^{11}$、低组为 $64n$ 个包，沿用

$$
q_0=\frac1{16(1-\alpha)^2},\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
a=q_0(1-\alpha)>0,\quad\frac13\le\alpha\le\frac12.
$$

低包 $(a_i^2,b_i^2)=(\alpha q_0,q_0)$，
高包 $(a_i^2,b_i^2)=(\beta,1)$。记
$R_i=a_i^2-b_i^2$，则低包 $R_i=-a$，高包 $R_i=64a$。

shape 坐标的第 $k$ 个 cell 内，低中心为

$$
x_{k,l}=64A(k-(n-1)/2)+A(l-31.5),
\quad0\le l\le63;
$$

高中心为 $B(k-(n-1)/2)$，在低中心31与32之间。真实小偏移不用置零。高低宽度为 $1,q_0$，它们的方差差按原三矩严格为
$V_L-V_H=\nu(1-q_0^2)$。

在 $\theta=\pi/2$，R259 的外因子为 $b_i^2$、内因子为 $R_j$。因此微包内 $g$ 的符号、Thue–Morse 符号及 R265 伴随符号均不会改变 (1)。

## 4. 完整有序部分的每 cell 准确和

将 (6)、(7) 的 $\xi$ 项写为 $-m^2J$，其中

$$
J=\sum_i b_i^2\xi_i\left(\frac{R_i}{2}
+\sum_{j>i}R_j\right).
\tag{8}
$$

每个 cell 的内层总质量 $\sum R_j=0$，所以未来其他 cell 对 (8) 没有贡献。这只使用该分量的 inner 零次矩，不称每个 cell 的全部三矩或 canonical forcing 已紧。

高包的括号为 $32a-32a=0$。低包的括号在前32项为 $a(l+1/2)$，在后32项为 $a(l-63.5)$。常中心因两组系数和相反而消掉，于是

$$
\begin{aligned}
J_{\rm cell}
&=2q_0aA\sum_{l=0}^{31}(l-31.5)(l+1/2)\\
&=-10928\,q_0aA.
\end{aligned}
\tag{9}
$$

高包的真实小偏移没有进入结果，不是因为被近似删掉，而是因为它的括号准确为零。因此完整 ordered/self 线性坐标部分为

$$
10928\,nm^2q_0aA>0.
\tag{10}
$$

## 5. 局部余项与准确正号

其余两项由原幅度及方差约束准确给

$$
-\sum_i b_i^2R_i
\left[\frac{C\xi_i^2}{w_i}
+w_i\left(\mathcal L-\frac\Delta4\right)\right]
=
64na(1-q_0^2)\left(C\nu-\mathcal L+\frac\Delta4\right).
\tag{11}
$$

例如 $\sum b_i^2R_i/w_i=0$、其一次中心矩为零，而二次中心矩为
$64na(V_H-V_L)=-64na\nu(1-q_0^2)$；
另有 $\sum b_i^2R_iw_i=64na(1-q_0^2)$。
这里没有另用一个未约束的中心参数。

R256 的母包简单根及主宽分支由 R262 已严格付清

$$
C\nu-\mathcal L+\Delta/4>0:
$$

先固定足够小正母宽 $h$，其根为 $s_h=1+O(h^2)$；
再取正主宽 $\delta$，以根分支连续性保号。
因此沿**实际有限正宽能量零点分支**，

$$
\boxed{
S_{04}^{\rm shape}
=10928\,nm^2q_0aA
+64na(1-q_0^2)
\left(C\nu-\mathcal L+\frac\Delta4\right)>0.
}
\tag{12}
$$

主物理宽度只同乘正 $\delta$。共同物理中心的常数与一次项已经在 (8)、(11) 的完整矩恒等中消掉；未将只在 leading 根成立的符号代替真实分支。

这个号也保留在中央母包另乘
$\gamma=1+O(h^2)$ 的相邻幅度/宽度构造中。准确地，

$$
C\nu-\mathcal L
=\frac{2L^2C_v}{h}
\left[\frac{\gamma^4/s+2}{\gamma^2+2}-1\right]+O(h)=O(h),
$$

$$
\Delta=4Lm_v^2(\gamma^2+1)
+h(\gamma^4s+2)\Delta_v.
\tag{13}
$$

故同样先定小正 $h$、再定正 $\delta$，括号仍趋于
$2Lm_v^2>0$。支付额外 local 母形状门不能在这个相邻分支中改变 (12)。

## 6. 完整复制、伴随方向和正幅组合均保持

R265 的伴随母包在最小子包上只改变 $g$ 的符号。在 $\theta=\pi/2$，所有 outer、inner 因子都只用平方，所以 (1) 完整不变，不只是局部能量不变。

每个完整 block 已三矩合法。不同完整 block 之间的 R259 跨核对 inner 三矩线性，全部为零。八复制、十二复制及后续任意正幅组合因此按正四次权相加。在最后位置分别支付原能量 IFT 的每个 block，(12) 都严格为正；它们的正幅组合仍严格为正。

尤其 R265 的
$\mathscr Q_-<0<\mathscr Q_+$
能按正四次权配成 $\mathscr Q=0$，但两个 block 的 (1) 都为正，不能同时由这一次混合清掉 (1)。pure 四次谐波为零后，完整角多项式仍可留一个 $\sin^2\theta$ 层；本稿在 $\theta=\pi/2$ 正是读取其实际值。

由 (2)、(3)，原 Gaussian 的对应第零矩严格非零。这个失败发生在完整 $\theta$ ruling 的已识别 necessary area，不是尚未打印的诊断，更不是声称数值误差无法降低。

## 7. 窄结论与建设性后继位置

本稿只排居中高低 cell、所述母包简单根附近及其正幅完整复制。它不把这一实质量排列推广为任意 profile 圆的普遍障碍。

R265 主要改变 imaginary primitive，故可以调 pure 的实部差，却不改变 (1) 的平方因子。要处理本稿的额外完整 even 门，必须改变实际高低 real 质量的次序、位置分配或方向平方权，同时重新准确支付三矩与能量 IFT。只在原 cell 内改变符号或继续扩大同一幅度组合不够。

这种新次序可以独立作为一个实际参数化设计，但不能在一个已经求得的固定 $\delta$ 圆上任意移动高包、删去交叉尾，或据保持零次矩就宣布三矩保持。下一构造应显式给真实不交次序、二次中心补偿和全部复制后的正幅向量关系。

本稿没有运行任何新研究或重复旧计算。
