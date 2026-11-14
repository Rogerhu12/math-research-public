# R133 续篇：保留衰减的 signed Riccati 正 Green 与完整界面源

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇给[分片 regular projector 与跳项 Green](R133-supplement-piecewise-regular-projectors-and-complete-jump-Green.md)
可消费的一个替代标量比较定理。它保留每片的真实 signed rate、
全部左右边界及所有界面负荷。是否有实际有限 Riccati 包络、各个界面
分母是否为正以及最外标量门是否通过，仍须由同一实际连续问题给出；
本文没有把已保存的浮点 projector proposal 当作这些门的证书。

## 1. 数据和所需的明确条件

取有限分点 $0=t_0<t_1<\cdots<t_N=L$。每个开片上
$\mu,\nu$ 为实 $L^1$ 函数，$c,e\ge0$ 为 $L^1$ 函数。
未知的两个非负大小函数满足几乎处处的比较不等式

$$
p'\le\mu p+cq+f,\qquad
-q'\le\nu q+ep+g,
\qquad f,g\ge0.
\tag{R.1}
$$

它们在每片绝对连续，保留各分点的两侧迹。
两端数据为

$$
p(0)\le D_0q(0)+b_0,\qquad
q(L)\le D_Lp(L)+b_L,
\quad D_0,D_L,b_0,b_L\ge0.
\tag{R.2}
$$

每个内界面使用已经从实际框架证明的四个非负系数
$A_k,B_k,C_k,D_k$ 和两个非负界面源 $a_k,b_k$：

$$
p_k^+\le A_kp_k^-+B_kq_k^++a_k,\qquad
q_k^-\le C_kp_k^-+D_kq_k^++b_k.
\tag{R.3}
$$

这里的 $D_k$ 仅为界面系数；不与右端的 $D_L$ 混同。
不预设 $A_k=D_k=1$。特别，投影夹角本身不能免费授予这种对角归一化。

从右端向左解 Riccati 方程

$$
\rho'=-e-(\mu+\nu)\rho-c\rho^2,\qquad \rho(L)=D_L.
\tag{R.4}
$$

在每个界面由右迹定义

$$
d_k=1-B_k\rho_k^+,\qquad
\rho_k^-=C_k+\frac{D_kA_k\rho_k^+}{d_k}.
\tag{R.5}
$$

所需的三个条件准确是：

$$
\rho\ge0\ \hbox{在全部片上有限},\qquad
d_k>0\ \hbox{对每个实际界面},\qquad
1-D_0\rho(0)>0 .
\tag{R.6}
$$

有限性包括每个闭片上的有限两侧值；于是出现的乘积和积分都有限。
若某个条件尚未核实，后面的结论只是一条待消费的定理，不是实际
边值问题已经可逆的断言。

## 2. 先构造等式的正逆

先将 (R.1)–(R.3) 全部换成等式，未知记为 $P,Q$。
允许一般实源以证明线性和唯一性；正性在源非负时断言。
设

$$
Z=Q-\rho P.
\tag{R.7}
$$

将等式和 (R.4) 准确代入，而不是操作不等式，得到三角系统

$$
Z'=-(\nu+c\rho)Z-g-\rho f,\qquad
P'=(\mu+c\rho)P+cZ+f .
\tag{R.8}
$$

右端条件准确为 $Z(L)=b_L$。在每个界面，先消去 $P_k^+$：

$$
\boxed{\quad
P_k^+=\frac{A_k}{d_k}P_k^-
      +\frac{B_k}{d_k}Z_k^+
      +\frac{a_k}{d_k},
\qquad
Z_k^-=\frac{D_k}{d_k}Z_k^+
      +\frac{D_k\rho_k^+}{d_k}a_k+b_k .
\quad}
\tag{R.9}
$$

这里 (R.5) 正是消掉 $P_k^-$ 系数所需的 Riccati jump。
全部界面源都保留了真实系数；尤其左侧 $Z$ 方程含
$D_k\rho_k^+a_k/d_k$，不能只留下 $b_k$。

因此先从 $L$ 到0依次求解第一条 (R.8) 和第二条 (R.9)，唯一得到
$Z$。再用左端

$$
P(0)=\frac{D_0Z(0)+b_0}{1-D_0\rho(0)}
\tag{R.10}
$$

向右求解第二条 (R.8) 和第一条 (R.9)，唯一得到 $P$；最后令
$Q=\rho P+Z$。这构造了完整边值等式的双侧逆。
齐次数据给 $Z=0$，继而 $P=Q=0$，所以不存在隐藏的齐次自由度。

若全部六类源 $f,g,b_0,b_L,(a_k),(b_k)$ 非负，
则 $Z$ 的逆向积分与每个跳式都非负。例如没有内界面的一个片上

$$
Z(t)=
\exp\!\left(\int_t^s(\nu+c\rho)\right)Z(s)
+\int_t^s
\exp\!\left(\int_t^\tau(\nu+c\rho)\right)
 [g(\tau)+\rho(\tau)f(\tau)]\,d\tau,\qquad t\le s.
\tag{R.11}
$$

即使 $\nu+c\rho$ 为负，此指数仍为正，并准确保留衰减。
由 (R.10)，$P(0)\ge0$；$P$ 的正向变常数公式以及 (R.9)
接着给 $P\ge0$。由于 $\rho\ge0$，也有 $Q\ge0$。
所以所构造的**完整 Green 逆为正算子**。

连续核是上述两个真实积分因子的有序乘积，界面核是
$D_k/d_k$、$A_k/d_k$ 以及 (R.9) 中的非负源系数。
这提供一个可直接累计的正核，不需要先分别取两个方向传播的
全区间 supremum 再相乘。

## 3. 用非负 slack 比较原不等式

不能直接对原不等式中的 $q-\rho p$ 求导后照搬 (R.8)：
减去 $\rho p'$ 时，$p'$ 的上界不能给所需的上界方向。
正确论证消费刚才已经构造的正逆。

对原 $p,q$ 定义片内缺量

$$
\sigma_f=f-p'+\mu p+cq\ge0,\qquad
\sigma_g=g+q'+\nu q+ep\ge0,
\tag{R.12}
$$

两端缺量

$$
\sigma_0=b_0-p(0)+D_0q(0)\ge0,\qquad
\sigma_L=b_L-q(L)+D_Lp(L)\ge0,
\tag{R.13}
$$

以及全部界面缺量

$$
\sigma_{a,k}=a_k-p_k^++A_kp_k^-+B_kq_k^+\ge0,\qquad
\sigma_{b,k}=b_k-q_k^-+C_kp_k^-+D_kq_k^+\ge0 .
\tag{R.14}
$$

于是 $p,q$ 正好解等式系统，其数据是原数据逐项减去这些缺量。
等式解唯一且依赖数据线性，故

$$
(P,Q)-(p,q)
 =\mathcal G_+\bigl(\sigma_f,\sigma_g,\sigma_0,\sigma_L,
                         (\sigma_{a,k}),(\sigma_{b,k})\bigr)\ge0,
\tag{R.15}
$$

其中 $\mathcal G_+$ 是第2节的正逆。于是 $p\le P,\ q\le Q$；
没有假设原不等式本身在某个方向是等式，也没有丢任一 jump 源。

## 4. 真正正交 projector 的角费用

若一个界面的两侧使用同秩正交投影 $\mathsf P_-,\mathsf P_+$，
且

$$
\delta=\|\mathsf P_+-\mathsf P_-\|<1,\qquad
r=\sqrt{1-\delta^2},\qquad \tau=\delta/r,
\tag{R.16}
$$

令 $p^\pm=\|\mathsf P_\pm u\|$、
$q^\pm=\|(I-\mathsf P_\pm)u\|$，则准确有

$$
rp^+\le p^-+\delta q^+,\qquad
rq^-\le q^++\delta p^- .
\tag{R.17}
$$

第一式来自
$\|\mathsf P_-\mathsf P_+u\|\ge r\|\mathsf P_+u\|$ 和
$\|\mathsf P_-(I-\mathsf P_+)u\|\le\delta\|(I-\mathsf P_+)u\|$；
第二式对两个补空间作同一论证。它们对任意向量成立，未要求它已经
落在某个 cone 中。

因此 (R.3) 的合法共同门是

$$
A=D=r^{-1},\qquad B=C=\tau,
\tag{R.18}
$$

并非 $A=D=1,\ B=C=\delta$。由 $r^{-2}=1+\tau^2$，
无源 Riccati jump 精确化为

$$
\boxed{\quad
\rho^-=\frac{\tau+\rho^+}{1-\tau\rho^+},\qquad
d=1-\tau\rho^+>0 .
\quad}
\tag{R.19}
$$

相应的 $P^-$ 到 $P^+$ 和 $Z^+$ 到 $Z^-$ 的传播系数均为
$1/[r(1-\tau\rho^+)]$，并仍按 (R.9) 保留非齐次源。
若只保存了 nonorthonormal frame $X$，必须用
$\mathsf P=X(X^*X)^{-1}X^*$ 的真实投影及已证 Gram 下界；
未经证明不能把 $XX^*$ 代入 (R.16)。
另一合法选择是直接从完整两侧 frame block 取得实际
$A,B,C,D$，然后使用通式 (R.5)。

## 5. 范数、零点与实际数据的权限

应用于连续向量方程时，不必假设未知的范数在每一点可微。
若向量解和实际 projector 在每片绝对连续，其投影向量及范数也
绝对连续，因而几乎处处导数和 (R.12) 足够。
例如对
$u'=H_{11}u+H_{12}v+F$，若
$\operatorname{Re}\langle u,H_{11}u\rangle\le\mu\|u\|^2$、
$\|H_{12}\|\le c$，可先对
$p_\varepsilon=(\|u\|^2+\varepsilon^2)^{1/2}$ 求导，得到

$$
p_\varepsilon'\le\mu p_\varepsilon+c\|v\|+\|F\|
                              +|\mu|\varepsilon .
\tag{R.20}
$$

积分后令 $\varepsilon\downarrow0$ 即得 (R.1)，包括 $u=0$ 的点。
负向 $q$ 行同理。真实 signed rate $\mu,\nu$ 的负号没有被
$|\mu|,|\nu|$ 取代；绝对值仅乘最终趋于0的正则化项。
投影导数、全源和背景误差须先真实进入这些四个系数及 $f,g$；
本文不免费提供该前置验证。

本篇为纯解析恒等式和比较证明，没有新的数值运行。
实际有限连续逆仍必须核实同一背景上的全部 Riccati 覆盖、
所有正分母、$D_0\rho(0)<1$、真两侧边界、完整 high 反馈和全部源。
满足这组门后，才可用上述正核替换过粗的两个全区间 supremum 乘积。
