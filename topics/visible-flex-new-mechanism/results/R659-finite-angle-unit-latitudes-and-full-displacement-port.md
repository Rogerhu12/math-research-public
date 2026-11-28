# R659：有限倾角的单位纬圈切向、完整等距行与全位移端口

2026-11-28。**已证明**一套直接用实际三维像求固定有限倾角的圆环方程。完整几何从纬圈单位切向和两个径向中心函数构造。在反射空间中，闭合确实只剩一个标量函数；其余两个度量行给完整旋转度量条件。内外两圈的两阶 jets 硬约束于真实刚帽，实际倾角是输入，首个运行即使用 $\sin\vartheta=9/25$。还给出任意候选的精确有限倾斜端口及其真实度量缺陷修正。以下不把未解零点或线性余量称作有限等距根。

## 1. 整圈原函数与真实闭合

用 $\varphi$ 作材料经度。令 $e_r=(\cos\varphi,\sin\varphi,0)$、$e_\varphi=(-\sin\varphi,\cos\varphi,0)$。$u(r,\varphi),v(r,\varphi)$ 为角变量的奇周期函数。置
$$
T=\cos v(\sin u\,e_r+\cos u\,e_\varphi)+\sin v\,e_z,\quad
H=T-\langle T\rangle,\quad U=\partial_\varphi^{-1}H ,
$$
其中 $\langle\cdot\rangle$ 是整圈平均，$U$ 取零均值原函数。$|T|=1$。其笛卡尔 $x,z$ 分量奇，$y$ 分量偶；故 $\langle T\rangle=0$ 等价于唯一的实标量行
$$
\langle T_y\rangle=\langle\cos v\cos(\varphi-u)\rangle=0.        \tag{1}
$$
这里没有把径向或竖直的额外闭合分量留给后续。令 $Jx=e_y\times x$，$Q(r)=R_y(\omega(r))$，$C(r)=(C_x(r),0,C_z(r))$。真实位置和导数为
$$
F=C+rQU,\quad F_\varphi=rQH,\quad F_r=QD,
\quad D=Q^TC'+U+rU_r+r\omega' JU.                              \tag{2}
$$
对任意候选 $F$ 已经是周期函数，即使 (1) 尚未满足。闭合行衡量其周期导数与所指定单位切向是否相同。径向的 $Q$ 与角平均、角微分可交换；其径向导数已完整保留在 $D$ 中。$U$ 的笛卡尔 $x,z$ 分量偶、$y$ 分量奇，故 $F$ 的反射正是关于 $xz$ 面的环境反射。

由 (2) 实际的 $rr,r\varphi,\varphi\varphi$ 项分别为 $|D|^2,rD\cdot H,r^2|H|^2$。因此以下与全部旋转等距行等价：
$$
(1),\qquad D\cdot H=0,\qquad |D|^2-\langle|D|^2\rangle=0,
\qquad E(r)=\langle|D|^2\rangle>0.                              \tag{3}
$$
在任意解上，$g=E(r)dr^2+r^2d\varphi^2$，(1) 给 $|H|=1$。反向若 $g_{\varphi\varphi}=r^2$，取全圈平均得 $1=\langle|H|^2\rangle=1-|\langle T\rangle|^2$，所以必要闭合也是 (1)。实际求解还保留 $|H|^2-1$ 的全部行。若已冻结一个 $E_*$，则把第三行改为 $|D|^2-E_*=0$，以后不随更新的 $F$ 重新选择度量。

(1)–(4) 中的均值和原函数均以全周期连续积分定义。在奇数角网，实际求值先对 $T$ 作三角插值，只在该插值空间准确作零均值角积分。不同角数给不同的近似原函数，网间差异必须另行读出。二阶曲率读数使用同一个插值位置的角谱二阶导，还记录其与单位切向解析角导的差。冻结 513 点角均值时，冻结的是指定参数和 513 点插值所定义的一个关于连续 $r$ 的精确目标函数。它与全角积分目标的差需单独估计。

真实二阶 jets 在同一个 $Q$ 框架为
$$
Q^TF_{rr}=Q^TC''+2U_r+rU_{rr}+2\omega'J(U+rU_r)
                  +r\omega''JU+r(\omega')^2J^2U,
$$
$$
Q^TF_{r\varphi}=H+rH_r+r\omega'JH,\qquad
Q^TF_{\varphi\varphi}=rT_\varphi .                               \tag{4}
$$
这给实际第一、第二基本形式；在离根处也用真实第一基本形式求主曲率。

## 2. 有限倾角、两阶端 jets 和材料相位

设 $t=(r-a)/(b-a)$、$\omega=\vartheta(1-10t^3+15t^4-6t^5)$。$\omega(a)=\vartheta,\omega(b)=0$ 且两端一、二阶径向导数全零。要求 $u,v$ 及各自两阶径向导数在两端为零，$C(b)=0,C'=C''=0$ 于两端。于是两端 $T=e_\varphi,U=e_r,U_r=U_{rr}=0$。由 (2)、(4)，外端准确等于原平盘，内端准确等于 $C(a)+R_y(\vartheta)(r e_r)$，包括 $F_r,F_{rr},F_{r\varphi},F_{\varphi\varphi}$ 的全部匹配。完整内端平移由实际 $C(a)$ 给出。

五次夹持 B 样条节点重复度六，两端分别删去前三、后三个控制基函数，就得到 $u,v$ 所需的三个齐次迹。$C'$ 的基只删去前二、后二个，令 $C(r)=\int_b^r C'(s)ds$；背景竖直导数额外使用双端二阶零的多项式。标准 B 样条的端点 Taylor 阶数直接证明这些迹条件。角上使用全部 $1\le j\le K$ 正弦列，有非零均值作用的第一正弦列也保留。该有限空间有真实 $C^2$ 端点，与把尚未知的自然线当成已接平帽不同。

在外帽坐标，对基解作 $F_\alpha(r,\varphi)=R_z(\alpha)F(r,\varphi-\alpha)$，$0\le\alpha\le\pi$。外圈材料固定，内刚姿准确是 $R_z(\alpha)Q(a)R_z(-\alpha)$ 和 $R_z(\alpha)C(a)$。接 [R655](R655-offset-rigid-cap-and-thick-inner-hold.md) 的两个刚件，再按其内框冻结握柄。两次刚体作用保持度量；基相位的度量误差在其余相位只平移材料角，所以相对同一旋转 $g$ 的全相位最大误差等于基相位的全角最大误差。这条身份对离根场同样成立；采样的最大值仍不等于全角最大值。R655 的整像支撑差、管和包络使用实际 (2)–(4) 和真实 $C(a)$。

## 3. 全位移的准确有限倾角端口

以下采用 $h'=-w<0$ 的参考图 $X=r e_r+h e_z$，参考度量为 $E=1+w^2$。可在任一 $w>0$ 的紧区间使用，不要求端帽附近能安全数值除以 $w$。令 $V=F-X$ 是实际、完整的三维位移。取其第一余弦径向、第一正弦方位、第一余弦竖直系数分别为 $A_1,B_1,f_1$，记实际度量缺陷为 $e_{rr},e_{r\varphi},e_{\varphi\varphi}$。定义
$$
P=-[|V_r|^2]_1/2,\qquad Q_1=-[|V_\varphi|^2]_1/(2r),
\qquad S=-[V_r\cdot V_\varphi]_{\sin1},
$$
$$
P_e=[e_{rr}]_1/2,\qquad Q_e=[e_{\varphi\varphi}]_1/(2r),\qquad
S_e=[e_{r\varphi}]_{\sin1}.
$$
这里各 $[\cdot]_1$ 是真实余弦系数；方位基的角导数不能删掉。逐项展开 $g_F-g_X=2\operatorname{sym}(dX\cdot dV)+dV\cdot dV$，得到
$$
A_1'-wf_1'=P+P_e,\quad A_1+B_1=Q_1+Q_e,\quad
-A_1-B_1+wf_1+r B_1'=S+S_e .
$$
没有截断 $V$ 的阶数。对任意三行 $p,q,s$，定义
$$
\mathcal I_{[c,d]}(p,q,s)=
  [q/(wr)]_c^d+\int_c^d\left[\frac{qw'}{w^2r}
                   -\frac{s}{wr^2}-\frac{p}{wr}\right]dr .
$$
消去 $A_1,B_1$ 得 $w(r f'_1-f_1)=r(q)'-q-s-rp$。分部积分时 $q/(wr^2)$ 两项准确消去，故
$$
\boxed{[f_1/r]_c^d
  =\mathcal I_{[c,d]}(P,Q_1,S)+\mathcal I_{[c,d]}(P_e,Q_e,S_e).}       \tag{5}
$$
这条**有限角、离根也准确**的身份只用全位移一阶与 $w'$，从不微分度量误差。在任一已知 $w\ge w_0>0$ 的紧段，第二项绝对值由两个边界 $|Q_e|/(wr)$ 及被积三项的绝对值给出可直接包围的误差。全圈第一系数消费所有相邻 Fourier 差频以及零/一模作用，不限于 R657 的指定两模。全真帽的 $[f_1/r]_a^b=0-(-\sin\vartheta)=\sin\vartheta$；在数值上可把 (5) 两侧遗漏的端区差直接由实际 $F$ 的 $f_1/r$ 读取。若某真实候选 $E<1$，旋转度量系统 (1)–(4) 依然有定义，但不在该段假设一个实数 $w=\sqrt{E-1}$ 来报告 (5)。

## 4. 全部形状列的微分

写 $T_u,T_v$ 为 (1) 所用真实单位球坐标的两个导数，$T_{ur}=T_{uu}u_r+T_{uv}v_r$，$T_{vr}=T_{uv}u_r+T_{vv}v_r$。对任意方向
$$
\delta T=T_u\delta u+T_v\delta v,\quad
\delta T_r=T_{ur}\delta u+T_{vr}\delta v+T_u\delta u_r+T_v\delta v_r .
$$
设 $P_0$ 是零均值角原函数，$M_0$ 为减均值。则
$$
\delta H=M_0\delta T,\quad
\delta D=Q^T\delta C'+(I+r\omega'J)P_0\delta T+rP_0\delta T_r .
$$
三真实度量行分别使用 $2D\cdot\delta D$、$\delta D\cdot H+D\cdot\delta H$、$2H\cdot\delta H$。设计阶段为第一行减角平均；冻结后保留其全部均值。闭合微分 $\langle\delta T_y\rangle$ 也加入。在导数内沿一个角频分离径向基 $B_i$ 与 $B_i'$，即可组装每个真实径向列，平方范数及其右端不作谱截断。新公开求解见[实际有限输入](../notes/2026-11-28-r659-direct-finite-tilt-latitude-scope.md)。本稿证明系统与姿态、读出等价性；真实有限根及全点误差由求解和后续验证决定。
