# R150 附录：长度四共同支撑上的完整低梯度与非零投影二次关系

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明的进一步必要条件。** 接[三维矩的共同长度四归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)，本文实际使用余下低阶梯度。一次矩在三次矩本质三空间之外时，完整一次梯度迫原平方的完整标量值为零；若原 $H$ 的秩为四，则完整二阶梯度还迫四维物理投影有一个非零二次关系。这两项均非仅从最高第三矩条件得来，仍不构成完整临界条件的充分性。

## 1. 已付的同一组参数与张量

使用原完整 $\mathcal Q_3(y,H,V)$、非退化对称 $K$、$F=\tfrac12y^{\mathsf T}Ky$，并记
$$
p=Ky,\quad b=p^{\mathsf T}Hp,\quad \tau_2=\operatorname{tr}((KH)^2),
$$
$$
T_2=yy^{\mathsf T}-2H,\qquad M=H-\tfrac14yy^{\mathsf T}.
$$
第三普通矩为对称三线性张量
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V,
\tag{1.1}
$$
其中 $\operatorname{Sym}_{\Sigma}$ 表示三个不同位置之和，所以 $T_3(r,r,r)=(yr)^3-6(yr)H(r,r)+4V(r,r,r)$。

本文假设已付前稿的情形：$T_3$ 的本质支撑 $W$ 三维，mean 的 $4\times3$ Hankel 秩为三，$y\notin W$。于是
$$
E=W\oplus\mathbb Cy,\quad \dim E=4,\quad
\operatorname{Ran}M\subset W,
$$
并有唯一 $\lambda\in E^*$ 满足 $\lambda|_W=0,\lambda(y)=1$。前稿已从原矩身份证明
$$
\boxed{H\lambda=\tfrac14y,\qquad T_2\lambda=\tfrac12y.}
\tag{1.2}
$$
这些都是同一原 $y,H,V$ 上的等式；任意延长 $\lambda$ 到六维对偶空间都给相同收缩。

原 Hankel 性还给
$$
\operatorname{tr}(KH)=0,\qquad
\operatorname{tr}(KM)=-F/2,
\qquad K:V=0.
\tag{1.3}
$$
最后一项是向量等式；它由 $K$ 每条反对角线系数和为零逐个剩余指标成立。

## 2. 六个原一次梯度的准确第三矩表达

直接对[完整未消元式](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)求 $y$ 梯度，先得到
$$
\frac13K^{-1}\nabla_y\mathcal Q_3
=(F^2-2b+2\tau_2)y-4FHp+8HKHp
 +4V(p,p,\cdot)-8V:(KHK).
\tag{2.1}
$$
记号 $V:B$ 表示在两个指标上与矩阵 $B$ 收缩，留下一个向量。式 (2.1) 中全部项来自原有限展开，没有替换或丢去 $V$。

用 (1.1) 逐项消去 $V$，再用
$$
\operatorname{tr}((KT_2)^2)=4F^2-4b+4\tau_2,
$$
准确化为
$$
\boxed{
\frac13K^{-1}\nabla_y\mathcal Q_3
=T_3:(KT_2K)-2F T_2p
 +\left(3F^2-\frac12\operatorname{tr}((KT_2)^2)\right)y.
}
\tag{2.2}
$$
例如代换可先核
$$
4V(p,p,\cdot)=T_3(p,p,\cdot)-4F^2y+2by+8FHp,
$$
$$
8V:(KHK)=2T_3:(KHK)-2by+4\tau_2y+8HKHp,
$$
两式代回 (2.1) 即给 (2.2)。这些身份对所有原 $y,H,V$ 成立，未使用临界性。

若当前点为完整临界点，将 (2.2) 与 $\lambda$ 配对。第一项由 $T_3\in\operatorname{Sym}^3W$ 消失；由 (1.2)，
$$
\lambda(T_2p)=\tfrac12y^{\mathsf T}p=F.
$$
因此
$$
0=F^2-\frac12\operatorname{tr}((KT_2)^2)
=-(F^2-2b+2\tau_2).
$$
也就是
$$
\boxed{\mathcal Q_{F_0^2}(y,H)=F^2-2p^{\mathsf T}Hp+2\operatorname{tr}((KH)^2)=0.}
\tag{2.3}
$$
这里只得到原平方完整多项式的值为零，没有说该点也满足原平方的全部梯度。

## 3. 十一个原二阶梯度给一个具体四维二次关系

对任意物理点 $v(z)$，直接二阶物理求导给
$$
-\frac16\sum_{m=0}^{10}z^m\partial_{H_m}\mathcal Q_3
=T_3(p,Kv(z),Kv(z))-F T_2(Kv(z),Kv(z))
 +4v(z)^{\mathsf T}KHKHKv(z).
$$
所以令对称矩阵
$$
N=T_{3,p}-F T_2+4HKH,
\tag{3.1}
$$
其中 $T_{3,p}(r,r)=T_3(p,r,r)$，完整临界性迫
$$
\boxed{v(z)^{\mathsf T}KNKv(z)\equiv0.}
\tag{3.2}
$$
$N$ 的全部列都在 $E$ 内。用 $H=M+yy^{\mathsf T}/4$ 展开，另有准确式
$$
\boxed{
N=T_{3,p}+2FM+4MKM
  +y(Mp)^{\mathsf T}+(Mp)y^{\mathsf T}.
}
\tag{3.3}
$$
后面两个跨项没有被删除。

## 4. 若原 H 秩四，该二次关系必非零

现在另假设
$$
\operatorname{rank}H=4.
\tag{4.1}
$$
在 $E=W\oplus\mathbb Cy$ 中，$H=M+yy^{\mathsf T}/4$ 分成一个三维块和一个非零一维块，因此 $M$ 在 $W$ 上的对称张量块可逆。

反设 $N=0$。式 (3.3) 中前三项属于 $\operatorname{Sym}^2W$，最后两项是 $y$ 与 $Mp\in W$ 的交叉块。由于 $y\notin W$，交叉块为零迫
$$
Mp=0.
\tag{4.2}
$$
$M$ 的三维块可逆，故 $p$ 湮灭整个 $W$，从而 $T_{3,p}=0$。于是 (3.3) 变成
$$
MKM=-F M/2.
\tag{4.3}
$$
取任一满列秩 $U$ 张成 $W$，写 $M=UCU^{\mathsf T}$、$C$ 可逆。式 (4.3) 给
$$
(U^{\mathsf T}KU)C=-F I_3/2,
$$
所以
$$
\operatorname{tr}(KM)=-3F/2.
$$
与 (1.3) 的 $\operatorname{tr}(KM)=-F/2$ 比较，得到 $F=0$。再由 $C$ 可逆，$U^{\mathsf T}KU=0$；(4.2) 给 $y^{\mathsf T}KU=0$；$F=0$ 给 $y^{\mathsf T}Ky=0$。因此整个四维 $E$ 都是 $K$ 全等向空间。

这与六维非退化双线性型矛盾：全等向 $E\subseteq E^{\perp_K}$，而 $\dim E^{\perp_K}=6-\dim E=2$。所以
$$
\boxed{\operatorname{rank}H=4\ \Longrightarrow\ N\ne0.}
\tag{4.4}
$$

由 (3.2)、(4.4)，原四维物理投影的像确实落在一个**非零二次曲面**上。若选 $E$ 的任一基矩阵 $E_4$，有唯一非零四阶对称矩阵 $C_N$ 使 $N=E_4C_NE_4^{\mathsf T}$，并且
$$
\boxed{
(E_4^{\mathsf T}Kv(z))^{\mathsf T}C_N
(E_4^{\mathsf T}Kv(z))\equiv0.}
\tag{4.5}
$$
四个投影多项式独立，故这不是零坐标关系。于是只要对某一候选长度四支撑证明其十个二次乘积线性无关，就已通过原二阶梯度排除了该候选的这类完整临界点。

## 5. 与四不同点参数和剩余条件的接口

前稿的四不同点表示中，若全部 $l_i=\lambda(u_i)\ne0$，则
$$
H=2\sum_{i=1}^4v_i l_i u_i u_i^{\mathsf T},\qquad v_i\ne0,
$$
四个 $u_i$ 独立，所以 $\operatorname{rank}H=4$ 自动成立。因此该子类现在同时必须满足：原平方值 (2.3) 为零、原四维投影有 (4.5) 的非零二次关系，以及前稿的中央三次半权分割。

这些条件全部来自同一原 $y,H,V$；没有自由改选第四或第五普通矩。含重 jets 的情形，只要原 $H$ 秩四，§§2–4 仍全部适用；若 $H$ 降秩，本文不声称 $N$ 必非零。

尚须分类真正具有二次关系的长度四投影，并同时支付余下的全部向量等式 (2.2)、二阶关系 (3.2) 与最高第三矩恒等式。本文不将其余标量必要条件当充分条件，也未给全局 Bell 幂或原算子的循环性。
