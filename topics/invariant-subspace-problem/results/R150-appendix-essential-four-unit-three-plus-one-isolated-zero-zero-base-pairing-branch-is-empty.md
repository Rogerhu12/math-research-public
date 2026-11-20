# R150 附录：孤立零点加单位三重点、单点的零基点配对支路为空

作者：Astra-ISP-b2a9acde-20261120（root 与 r150_structure）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

## 1. 范围、同一原物理 jets 与原源

沿用[外均值 essential-four 的原长度五 Frobenius 约化](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)：
$$
 \operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\quad
 \dim\operatorname{ess}(T_3)=4,\quad y\notin\operatorname{ess}(T_3),\quad
 \operatorname{rank}H=4.
$$
$L$ 在一个长度三局部因子和一个约化点上为单位，在另一个约化点上为零。
归一单位因子后
$$
 B=\mathbb C[\epsilon]/(\epsilon^3)\oplus\mathbb C,\qquad
 \tau(x)=a x_0+x_2+b x_3,\qquad a+b=1,\quad b\ne0.
$$
允许 $a=0$。局部参数变换可令 $\tau\epsilon=0,\tau\epsilon^2=1$，
保持同一原曲线的物理 jets。

活跃物理基为 $u_0,u_1,u_2,v_0$，极坐标为 $(X,Y,Z,T)$；
零点极坐标记为 $R$。原矩及其三次式为
$$
 y=\tau X,\quad H=\tfrac14\tau X^2,\quad
 V=\tfrac18\tau X^3+\tfrac14R^3,\quad
 T_3=P+R^3,\quad P(x)=\tfrac12\tau(x-\tau(x)1)^3.
$$
原活跃 Gram 是
$$
 K_B=
 \begin{pmatrix}
 0&0&A&p\\
 0&-2A&B&q\\
 A&B&C&r\\
 p&q&r&0
 \end{pmatrix}.                                             \tag{1.1}
$$
$K_{11}=-2K_{02}$ 来自原曲线二阶 jet，不能删去。
本附录排除整个
$$
                         p=0                              \tag{1.2}
$$
支路，分别处理 $A\ne0$ 与 $A=0$。

写零点交叉列 $U=(u,v,w,z)^T$，则
$$
 m=a u+w+b z,\qquad
 \widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix},\qquad
 \operatorname{rank}\widehat K\ge4.                         \tag{1.3}
$$
秩下界来自原长度五 jets 独立及原六维 $K$ 非退化。

令 $D_Kx$ 的第 $i$ 分量为 $\tau((K_B)_{i,\bullet}x)$，
$d=D_K1,\ \phi=\tau d/2$。原 active mean 和低二次梯度为
$$
 e-2D_Kd-2d^2+4\phi d=0,
$$
$$
 e=(\tau k_0^2,\ 2\tau k_0k_1,\
       2\tau k_0k_2+\tau k_1^2,\ \tau k_3^2),               \tag{1.4}
$$
$$
 N=N_B+mR^2,\qquad
 N_B(x)=\tfrac12\tau((d-\phi)x^2)
 -(\tau x)\tau(dx)+\phi(\tau x)^2+\tfrac14\tau(xD_Kx).         \tag{1.5}
$$
原零点 mean 另给
$$
                         \tau U^2=2m^2.                   \tag{1.6}
$$
原 highest、$N$ 在整条原曲线上恒为零。

还使用已登记的
[全等向长度三原曲线 jets 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)：
原全等向长度三支撑只有两种约化三点，故不存在全等向的三重点，
也不存在全等向的 $2+1$ 支撑；该结论包括无穷远点。

## 2. $p=0,\ A\ne0$

利用所有 Gram 配对的共同齐次缩放令 $A=1$。
原 mean 的常数、一次系数先给
$$
 \phi=1,\qquad C=2b(1-r),\qquad B=bq(r-2).
$$
另外两系数为
$$
 q^2[1+2b(1-r)]+2r(1-r)=0,                                 \tag{2.1}
$$
$$
 2+bq^2-4b+6br-2br^2+b^2q^2(-4r^2+10r-6)=0.               \tag{2.2}
$$
在三重点基点，$K_Bu_0=(0,0,1,0)$，原式直接给
$$
 P(K_Bu_0)=1,\qquad N_B(K_Bu_0)=0.
$$
highest 迫 $u^3=-1$，故 $u\ne0$；原 $N$ 常数项遂迫 $m=0$。

同一原 $N_B$ 的一阶 jet 为
$$
                         (N_B)_1=bq(r-1).                 \tag{2.3}
$$
因 $b\ne0$，$N=0$ 给 $q=0$ 或 $r=1$。
若 $r=1$，(2.1) 给 $q=0$，但 (2.2) 给 $2=0$，矛盾。
故 $q=0$，继而 (2.1)、(2.2) 给
$$
 r=0,\qquad b=1/2,\qquad B=0,\qquad C=1.
$$
在唯一剩余候选上，
$$
 x_0=(0,0,1,0),\quad x_1=(0,-2,0,0),\quad x_2=(1,0,1,0),
$$
$$
 [t^2]\,N_B(x_0+t x_1+t^2x_2)
 =N_B(x_1)+\partial_{x_2}N_B(x_0)=-2-1=-3.
$$
零点补项 $mR^2$ 因 $m=0$ 消失，与原 $N=0$ 矛盾。
这包括 $q=0,r=0,r=1$ 的全部退化候选；没有除以这些量。

## 3. $A=p=0$：合法归一与完整 active mean 分类

此时 $K_Bu_0=0$，原 highest 在基点给 $u^3=0$，故 $u=0$。
因此 $u_0$ 已经是整个 $\widehat K$ 的核向量。

若 $q=0$，原子空间 $\langle u_0,u_1,v_0\rangle$ 全等向：
这是一阶双点加一个不同约化点的真实原 $2+1$ 支撑，违反第 1 节已付分类。
所以 $q\ne0$，可以把所有 Gram 配对同时除以 $q$，以下令 $q=1$。
若同时 $B=C=0$，原三重点空间 $\langle u_0,u_1,u_2\rangle$ 全等向，
也违反同一已付分类。

令
$$
 s=B+b,\qquad \phi=C/2+br.
$$
原一次 mean 为
$$
                         4\phi s-2br=0.                   \tag{3.1}
$$
若 $\phi=0$，因 $b\ne0$，有 $r=C=0$。
原单点 mean 给 $B=(1-2b)/2$，原二次 mean 随后给 $1-2b=0$，
于是 $B=C=0$，已排除。因此 $\phi\ne0$。

置
$$
 \kappa=2\phi/b\ne0.
$$
由 (3.1) 及 $\phi$ 的定义，
$$
 B=s-b,\qquad r=\kappa s,\qquad C=b\kappa(1-2s).             \tag{3.2}
$$
剩余两个原 mean 恰为
$$
 E_P=1-2s+2\kappa^2s(b-s)=0,                                \tag{3.3}
$$
$$
 E_2=b(1+2s)-4s^2+2b\kappa^2\{b(1-s)-s^2\}=0.              \tag{3.4}
$$
特别地 $s\ne0$。若 $B=s-b=0$，(3.3) 给 $s=b=1/2$，
(3.2) 又给 $C=0$，已排除；故 $B\ne0$。

不作任何除法，线性消去 $\kappa^2$：
$$
 s(b-s)E_2-b\{b(1-s)-s^2\}E_P
  =(b-2s^2)\{(4s-1)b-2s^2\}=0.                             \tag{3.5}
$$
若 $s=1/2$，(3.5) 给 $b=1/2$，又落入已排除的 $B=C=0$。
因此剩余 mean 穷尽为以下两族：

$$
 \mathrm I:\quad
 b=2s^2,\ B=s(1-2s),\ r^2=1/2,\ C=2rB,\quad s\ne0,1/2;     \tag{3.6}
$$
$$
 \mathrm {II}:\quad
 b=\frac{2s^2}{4s-1},\
 B=\frac{s(2s-1)}{4s-1},\
 r^2=\frac{1-4s}{2},\
 C=-2rB,\quad s(2s-1)(4s-1)\ne0.                            \tag{3.7}
$$
(3.6)、(3.7) 由 (3.3) 求 $\kappa^2$ 得出。
被除量 $b,s,B$ 均已证明非零；第二族中 $4s-1=0$
不可能满足 (3.5) 的第二因子，因为 $s\ne0$。
因此没有丢失参数或 Frobenius 零权例外。

## 4. 族 I：完整 Gram 多出一个核方向

在活跃约化点，
$$
 P(K_Bv_0)=-r,\qquad N_B(K_Bv_0)=-rs.
$$
由于 $r^2=1/2$，highest 给 $z^3=r\ne0$，而 $N$ 给
$$
 m z^2=rs,\qquad m=sz.
$$
因 $u=0$，零点 mean (1.6) 是
$$
 v^2+bz^2=2m^2.
$$
用 $b=2s^2,m=sz$，得 $v=0$。由 $m=w+bz$ 又得 $w=Bz$。

活跃 Gram 除 $u_0$ 外还杀向量
$$
                         -r u_1+u_2-Bv_0.
$$
与零点的配对为 $-rv+w-Bz=0$，所以它也是完整 $\widehat K$ 的核向量。
它与 $u_0$ 独立，故 $\operatorname{rank}\widehat K\le3$，违反 (1.3)。
此处只用了明确核向量；没有把“扩充列在像中”误当成一般秩不变规则。

## 5. 族 II：在真实原曲线 germ 中取消公共零因子

因为 $u_0$ 是完整 Gram 的核向量，所有活跃与零点极坐标在该原曲线基点都为零。
取产生 $u_0,u_1,u_2$ 的实际局部参数及实际单位缩放，
原曲线 germ 的极坐标展开从
$$
 t(K_Bu_1)+t^2(K_Bu_2)+O(t^3)
$$
开始，零点极坐标从 $tv+t^2w+O(t^3)$ 开始。
原 highest、$N$ 是整条原曲线上的恒等式，所以可在真实形式幂级数环中分别取消
$t^3,t^2$，再读取常数与一次系数。
**这不是在截断代数 $\mathbb C[\epsilon]/(\epsilon^3)$ 内除以 $\epsilon$。**

令
$$
 P_0=P(K_Bu_1),\quad P_1=\partial_{K_Bu_2}P(K_Bu_1),\quad
 N_0=N_B(K_Bu_1),\quad N_1=\partial_{K_Bu_2}N_B(K_Bu_1).
$$
由刚才合法取消后的原式，
$$
 P_0+v^3=P_1+3v^2w=N_0+mv^2=N_1+2mvw=0.
$$
因此无须除以 $m$ 或 $v$，仍有
$$
                         3P_0N_1-2N_0P_1=0.               \tag{5.1}
$$

设 $d_0=4s-1$。把真实族 II 的 (3.7) 代入原 (1.5)，得到
$$
 P_0=\frac{s^2(2s-1)^2}{d_0},\qquad
 N_0=-\frac{r s^2(2s-1)^2}{d_0^2},
$$
$$
 P_1=-\frac{3r s^2(2s-1)^2(2s+1)}{d_0^2},\qquad
 N_1=\frac{s^2(2s-1)^3}{d_0^2}.                             \tag{5.2}
$$
使用 $r^2=-d_0/2$，(5.2) 给出
$$
 3P_0N_1-2N_0P_1
   =\frac{12s^5(2s-1)^4}{(4s-1)^3}\ne0,                    \tag{5.3}
$$
因为全部分母与非零因子均已在 (3.7) 保留。这与 (5.1) 矛盾。

## 6. 结论与仍开范围

由第 2–5 节，外均值 essential-four 的
$$
 D=(3+1)_{\rm unit}+1_{\rm zero},\qquad
 p=K(u_0,v_0)=0
$$
整个支路为空，覆盖 $A\ne0$ 和 $A=0$、任意允许 Frobenius 权，
并包括无穷远原支撑（证明使用物理 jets 与原形式 germ，不依赖有限仿射点）。

配套[完整原 QQ 源](../notes/2026-11-20-essential-four-unit-three-plus-one-zero-base-pairing-verify.py)从(1.4)、(1.5)重建mean、各jet及(3.5)、(5.2)、(5.3)，只作展开、精确有理除法和二次关系取余。实际run44732550495/job136275725868，冻结提交35d0d768258a205cd0d78552fb7fbfa4018ec70a，全部通过，程序计时0.591秒。源码SHA256为b2394a711c80f4c8c08bdaba2104d79433074294879d4937c142437d82199535；[批次运行身份](../notes/2026-11-20-exact-source-run44732550495-b2a9.json)保完整日志、标准输出SHA和真实pull回执。先前失败仅为未化简矩阵的结构比较，修复为逐项精确化简后完整重核；全部数学定义不变，不保存计算数组。

$p\ne0$ 的单位 $3+1$ 支路仍开；本附录也不关闭其他单位补空间、
unit rank-five、inner-mean 或普通 Hilbert ISP 主结论。
