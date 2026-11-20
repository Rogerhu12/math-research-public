# R150 附录：第三累积量为零的本质四维重节点临界支全部排除

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 在原完整六模式立方临界系统中，第三累积量 $V=0$ 时，第三普通矩 $T_3$ 的本质维数不可能为四。本稿完成此前保留的全部非约化长度四支撑：
$$
4,\qquad 3+1,\qquad 2+2,\qquad 2+1+1.
$$
证明包括原无穷远点，使用原最高、均值和二阶矩梯度。与 [四不同点排除](R150-appendix-zero-third-cumulant-reduced-essential-four-section-is-empty.md) 合并后，整个 $V=0,\ \operatorname{essdim}T_3=4$ 分支为空。

这一结论不宣布一般完整临界集为空；$V\ne0$、本质五/六维以及原全局匹配 Bell 幂归属仍未由本稿关闭。

## 1. 原梯度、准确支撑和已付物理几何

沿用原 $K$、物理正规列 $v_{\rm hom}$ 和
$$
F_0(x)=\tfrac12x^{\mathsf T}Kx.
$$
在 $V=0$ 时，普通矩泛函为
$$
\Lambda[f]=\left.e^{-H(\partial,\partial)}f(x)\right|_{x=y}.
\tag{1.1}
$$
因此 Gaussian 协方差的代数记号是 $-2H$，不使用正性。在本质维数四时 $y\ne0$，原最高式可准确约去一次极线，得到
$$
(y^{\mathsf T}Kv(z))^2
=6v(z)^{\mathsf T}KHKv(z).
\tag{1.2}
$$
另两组必须保留的完整梯度是
$$
\Lambda[xF_0(x)^2]=0,\qquad
\Lambda[F_0(x)(v(z)^{\mathsf T}Kx)^2]=0.
\tag{1.3}
$$
来源为 [原 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 和 [原完整低阶梯度稿](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)。

[秩三外值域排除](R150-appendix-zero-third-cumulant-rank-three-outer-range-exclusion.md) 与 [独立双二次及单基点归约](R150-appendix-zero-third-cumulant-essential-four-independent-quadrics-and-basepoint-reduction.md) 已从原完整梯度给出：
$$
\operatorname{rank}H=4,\quad y\in E=\operatorname{Ran}H=E_D,
\tag{1.4}
$$
其中 $D$ 是唯一准确长度四物理 jet divisor。$E_D$ 的物理投影有唯一简单基点 $r$，并且 $r$ 属于 $D$ 的支撑。若取该点正规列 $u_r$，则
$$
u_r^{\mathsf T}K E_D=0.
\tag{1.5}
$$
所以 $u_r$ 是四维支撑上限制双线性型的根向量。

以下只复用四项已经完整核验、包括射影边界的原几何事实：

1. [长度三全等向 jet 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)：原长度三全等向 jet 空间只有 $W_\pm$，它们分别是三个不同有限根 $P_\pm$ 的支撑，没有重节点类型。
2. [三个不同物理点稿](R150-appendix-three-distinct-physical-support-complete-critical-classification.md) §2.2：原核
   $$
   k(s,t)=-(s-t)^2q(s,t)
   $$
   的任一非零齐次三次极线 $q(s,\cdot)$ 都不是一个一次式的三次幂。
3. 同稿 §2.3：在两个不同射影点处，$q,q_s,q_t$ 不会同时为零。
4. [任意长度四单基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md) §§2–4：两个不同物理点的五次极线最大公因子次数至多三。

在任一点选择局部参数并写正规物理列
$$
u(t)=u_0+u_1t+u_2t^2+\cdots .
\tag{1.6}
$$
于是 $u_1$ 是一阶 jet，$u_2$ 是二阶导数除以 $2$，依此类推。对长度 $m$ 的局部 $H$，准确表示为
$$
H_{\rm loc}=\sum_{i+j<m}h_{i+j}u_i u_j^{\mathsf T},
\qquad h_{m-1}\ne0.
\tag{1.7}
$$
最后的非零性来自原 $H$ 的准确长度和秩四。其他不同支撑点没有交叉累积量。以下的 Gaussian 坐标都由这些独立 jet 列定义；在坐标中写出的 $H$ 系数指 (1.7) 的系数矩阵，而非对物理列再作一次 $H$ 配对。

## 2. 一个保留根方向相关性的完整梯度引理

设四维物理支撑的独立列为
$$
u_r,\ u_X,\ u_Y,\ u_Z,
$$
且 $u_r$ 是 $K$ 的根方向。记对应坐标为 $R,X,Y,Z$，极线为 $p_r,p_X,p_Y,p_Z$。假设在活跃三坐标中
$$
H_{\{X,Y,Z\}}=\operatorname{diag}(h,0,k),
\qquad h k\ne0,
\tag{2.1}
$$
而根坐标与 $Y$ 的系数
$$
H_{RY}=t\ne0.
\tag{2.2}
$$
允许 $H_{RR},H_{RX},H_{RZ}$ 任意。假设限制二次式为
$$
F_0=\varepsilon XZ+uXY+vYZ+\frac{\kappa}{2}Y^2,
\qquad \varepsilon\ne0.
\tag{2.3}
$$
设均值为 $(a_0,a,d,b)$，并定义
$$
A=a+\frac{v}{\varepsilon}d,\qquad
B=b+\frac{u}{\varepsilon}d.
\tag{2.4}
$$
若原最高式已经给出
$$
A^2=6h,\qquad B^2=6k,
\tag{2.5}
$$
则完整三组梯度 (1.2)–(1.3) 不可能同时成立。

**证明。** 对只含活跃变量的多项式，$Y$ 的所有二阶系数均为零，故其矩作用准确等于把 $Y$ 代为均值 $d$。这一步只用于不含 $R$ 的多项式，不删除 (2.2)。

置
$$
\widetilde X=X+(v/\varepsilon)Y,\quad
\widetilde Z=Z+(u/\varepsilon)Y,\quad
\ell=\kappa/2-uv/\varepsilon.
$$
活跃边际矩仍有独立的二阶系数 $h,k$，且
$$
F_0=\varepsilon\widetilde X\widetilde Z+\ell Y^2.
$$
由 (2.5)，
$$
\Lambda[\widetilde X^2]=\tfrac23A^2,\quad
\Lambda[\widetilde Z^2]=\tfrac23B^2,\quad
\Lambda[\widetilde X^3]=\Lambda[\widetilde Z^3]=0.
\tag{2.6}
$$
若 $d\ne0$，完整均值梯度的 $Y$ 分量迫 $Q_2=\Lambda[F_0^2]=0$。置 $c=\ell d^2$，则
$$
Q_2=\tfrac49\varepsilon^2A^2B^2+2\varepsilon cAB+c^2.
\tag{2.7}
$$
完整均值梯度的 $\widetilde X$ 分量又给
$$
0=cA\left(\tfrac43\varepsilon AB+c\right).
\tag{2.8}
$$
这里 $A,B\ne0$。若 $c=0$，(2.7) 非零；若
$c=-4\varepsilon AB/3$，(2.7) 等于
$-4\varepsilon^2A^2B^2/9$，仍非零。因此
$$
d=0,\quad a^2=6h,\quad b^2=6k,\quad ab\ne0.
\tag{2.9}
$$

写原最高物理二次关系为 $\mathcal C=0$，原二阶梯度物理二次关系为 $\mathcal G=0$：
$$
\mathcal C=(y^{\mathsf T}Kv)^2-6v^{\mathsf T}KHKv,\qquad
\mathcal G=\Lambda[F_0(p_rR+p_XX+p_YY+p_ZZ)^2].
$$
在 (2.9) 下，所有不含 $p_r$ 的平方项相消，故准确有
$$
\mathcal C=p_rL_C+2ab\,p_Xp_Z.
\tag{2.10}
$$
其中 $L_C$ 是四条物理极线的线性组合，它的 $p_Y$ 系数为
$$
[p_Y]L_C=-12t.
\tag{2.11}
$$
同样，只看不含 $R$ 的边际，$Y=0$，而 $X,Z$ 的三阶普通矩为零，所以
$$
\mathcal G=p_rL_G+\frac89\varepsilon a^2b^2\,p_Xp_Z.
\tag{2.12}
$$
现在必须保留根方向相关性。Gaussian 分部积分给
$$
\Lambda[RYF_0]=-2t\,\Lambda[F_0]
=-2t\varepsilon ab,
$$
因为 $F_0$ 与 $R$ 无关，而 $Y$ 只与 $R$ 有二阶相关。因此
$$
[p_Y]L_G=-4t\varepsilon ab.
\tag{2.13}
$$
将 (2.12) 减去 $4\varepsilon ab/9$ 倍的 (2.10)，物理恒等式成为
$$
p_r\left(L_G-\frac49\varepsilon abL_C\right)=0.
\tag{2.14}
$$
$p_r\ne0$，而括号中 $p_Y$ 的系数为
$$
-4t\varepsilon ab+\frac{16}{3}t\varepsilon ab
=\frac43t\varepsilon ab\ne0.
$$
四条极线独立，故括号不可能为零多项式。矛盾。 $\square$

## 3. 型 $2s+t+u$：基点是双点 $s$

取
$$
u_r=v(s),\quad u_Y=v'(s),\quad u_X=v(t),\quad u_Z=v(u),
$$
使用各点的正规射影列。由 (1.7)，
$$
H=h_0R^2+2h_1RY+h_tX^2+h_uZ^2,
\qquad h_1h_th_u\ne0.
\tag{3.1}
$$
这里 $H$ 写成坐标二次符号以显示其系数矩阵。根方向身份给
$$
F_0=\varepsilon XZ+\gamma YX+\delta YZ+\frac{\kappa}{2}Y^2,
\tag{3.2}
$$
其中 $\varepsilon=v(t)^{\mathsf T}Kv(u)$。

若 $\varepsilon\ne0$，在物理点 $t,u$ 评价原最高式，依次得到
$$
\left(b+\frac{\gamma}{\varepsilon}d\right)^2=6h_u,
\qquad
\left(a+\frac{\delta}{\varepsilon}d\right)^2=6h_t.
$$
因此 §2 引理直接适用，矛盾。

若 $\varepsilon=0$，三个不同点 $s,t,u$ 全等向，故其空间是 $W_\pm$。$u_Y$ 不能同时与这三个列正交，否则由 $W_\pm=W_\pm^{\perp_K}$ 得 $u_Y\in W_\pm$，违反长度四 jets 独立性。所以 $\gamma,\delta$ 至少一个非零。最高式在 $t,u$ 的评价给 $d\gamma=d\delta=0$，因而 $d=0$：
$$
y\in W_\pm.
\tag{3.3}
$$
令 $P=P_\pm$。三条根点极线 $p_r,p_X,p_Z$ 被 $P$ 整除，而 $y$ 的极线也被 $P$ 整除。由 $h_1\ne0$，原最高式于是迫
$$
P\mid (p_r/P)p_Y.
\tag{3.4}
$$
不同极线的 gcd 次数界说明 $(p_r/P)(t)\ne0$ 及 $(p_r/P)(u)\ne0$：否则 $p_r$ 和相应自极线共享 $P$ 以及另一个同点因子，总次数至少四。因此 $p_Y(t)=p_Y(u)=0$。物理对角恒等式还给 $p_Y(s)=0$。所以 $P\mid p_Y$。

$W_\pm$ 的三维极线空间恰是 $P S_2$，而 $K$ 可逆，故 $P\mid p_Y$ 再次迫 $u_Y\in W_\pm$，矛盾。双点基点的全部 $2+1+1$ 型已排。

## 4. 型 $2s+t+u$：基点是简单点 $t$

取根列 $u_r=v(t)$，活跃列
$$
u_X=v(s),\quad u_Y=v'(s),\quad u_U=v(u).
$$
原累积量系数为
$$
H=h_tR^2+h_0X^2+2h_1XY+h_uU^2,\qquad h_1h_u\ne0.
\tag{4.1}
$$
记
$$
\lambda=u_Y^{\mathsf T}Ku_Y,\quad
\kappa=u_X^{\mathsf T}Ku_U,\quad
\gamma=u_Y^{\mathsf T}Ku_U.
$$
原物理对角恒等式给 $u_X^{\mathsf T}Ku_Y=0$，所以
$$
F_0=\frac{\lambda}{2}Y^2+(\kappa X+\gamma Y)U.
\tag{4.2}
$$

首先 $\lambda\ne0$。否则 $u_r,u_X,u_Y$ 是全等向的长度三 $t+2s$ 支撑，违反旧分类。其次 $\kappa\ne0$。若 $\kappa=0$，三个简单底点 $s,t,u$ 全等向，必给 $W_\pm$。根列 $u_r$ 与 $v'(s)$ 正交，所以它的极线在 $s$ 至少二重；$v(s)$ 的自极线在 $s$ 也至少二重。二者都被 $P_\pm$ 整除，因此 gcd 次数至少四，仍违反旧界。

记 $Y,U$ 的均值为 $d,b$。最高式在 $s$ 的评价给
$$
b^2=6h_u,\qquad b\ne0.
\tag{4.3}
$$
在 $s$ 的原局部参数中对最高式作一阶导数。根极线及 $u_X$ 的极线在该点的一阶导数均为零；$u_Y$ 极线的一阶导数为 $\lambda$，$u_U$ 极线的一阶导数为 $\gamma$。(4.3) 消去共同项后，准确得到
$$
2b\kappa d\lambda=0.
$$
所以 $d=0$。

置
$$
L=\kappa X+\gamma Y,\quad
A=\Lambda[L],\quad
\tau=H_{LY}=\kappa h_1\ne0,\quad
h=H_{LL}=\kappa^2h_0+2\kappa\gamma h_1.
\tag{4.4}
$$
这里 $H_{LY},H_{LL}$ 是 (4.1) 经此线性坐标变化后的二阶系数。最高式在物理点 $u$ 评价给
$$
A^2=6h.
\tag{4.5}
$$
且 $Y$ 的均值和自身二阶系数都为零；它只与 $L$ 有二阶相关 $\tau$，而 $U$ 与 $L,Y$ 独立。

完整均值梯度的 $Y$ 分量，按同一 Gaussian 分部积分，给
$$
\begin{aligned}
0=\Lambda[YF_0^2]
&=-4\tau\,\Lambda[UF_0]\\
&=-4\tau A(b^2-2h_u)
=-\frac83\tau A b^2.
\end{aligned}
\tag{4.6}
$$
所以 $A=0$，再由 (4.5) 得 $h=0$。现在 $L,Y$ 都是零均值、自身二阶系数为零的两个变量，交叉系数为 $\tau\ne0$。准确 Wick 矩为
$$
\Lambda[L^3]=0,\qquad
\Lambda[L^2Y^2]=8\tau^2,\qquad
\Lambda[LY^4]=0.
\tag{4.7}
$$
因此完整均值梯度的 $L$ 分量却为
$$
\begin{aligned}
\Lambda[LF_0^2]
&=\Lambda[L^3]\Lambda[U^2]
+\lambda\Lambda[L^2Y^2]\Lambda[U]
+\frac{\lambda^2}{4}\Lambda[LY^4]\\
&=8\lambda\tau^2b\ne0.
\end{aligned}
\tag{4.8}
$$
矛盾。所有简单基点的 $2+1+1$ 型也已排除。

## 5. 型 $3s+t$

若唯一基点为简单点 $t$，它的五次极线在不同点 $s$ 至少三重。除去非零的离对角平方因子，齐次三次 $q(t,\cdot)$ 就必须是一个一次式的三次幂，违反 §1 的旧事实。故基点只能为三重点 $s$。

取
$$
u_r=u_0,\quad u_X=u_1,\quad u_Y=u_2,\quad u_Z=v(t)
$$
和局部 Taylor jets (1.6)。累积量准确为
$$
H=h_0R^2+2h_1RX+h_2(2RY+X^2)+h_tZ^2,
\qquad h_2h_t\ne0.
\tag{5.1}
$$
因为 $u_r$ 是根方向，$u_0^{\mathsf T}Ku_2=0$。物理对角恒等式在局部二阶的系数为
$2u_0^{\mathsf T}Ku_2+u_1^{\mathsf T}Ku_1=0$，故
$$
u_X^{\mathsf T}Ku_X=0.
\tag{5.2}
$$
令
$$
\varepsilon=u_X^{\mathsf T}Ku_Z.
$$
若 $\varepsilon=0$，则 $u_0,u_1,v(t)$ 是全等向长度三重节点支撑，违反旧分类。因此 $\varepsilon\ne0$。写
$$
F_0=\varepsilon XZ+\alpha XY+\beta YZ+\frac{\kappa}{2}Y^2.
\tag{5.3}
$$
在物理点 $t$ 评价最高式，得到
$$
\left(a+\frac{\beta}{\varepsilon}d\right)^2=6h_2.
\tag{5.4}
$$
在三重点 $s$ 的局部展开中，各极线在常数项都为零；根极线和 $X$ 极线的一阶项也为零，而 $Y,Z$ 极线的一阶系数依次为 $\alpha,\varepsilon$。比较最高式的二阶系数，得到
$$
\left(b+\frac{\alpha}{\varepsilon}d\right)^2=6h_t.
\tag{5.5}
$$
这里 (5.1) 中所有含根极线的项至少四阶，$X$ 极线平方至少四阶；只有 $h_t$ 项贡献所比较的二阶系数。

现在 (5.1)–(5.5) 完整满足 §2 引理，其中
$$
h=h_2,\quad k=h_t,\quad H_{RY}=h_2\ne0.
$$
所以三重点基点也不可能。整个 $3+1$ 型排除。

## 6. 型 $2s+2t$

可设基点为 $s$。取
$$
u_r=v(s),\quad u_Y=v'(s),\quad
u_T=v(t),\quad u_U=v'(t).
$$
原累积量为
$$
H=h_0R^2+2h_1RY+k_0T^2+2k_1TU,
\qquad h_1k_1\ne0.
\tag{6.1}
$$
根身份给 $k(s,t)=\partial_tk(s,t)=0$。不同点处的旧核光滑性于是给
$$
\gamma=u_Y^{\mathsf T}Ku_T\ne0.
\tag{6.2}
$$
此外
$$
\lambda=u_U^{\mathsf T}Ku_U\ne0;
\tag{6.3}
$$
否则 $u_r,u_T,u_U$ 是全等向的长度三 $s+2t$ 支撑。

物理对角恒等式给 $u_T^{\mathsf T}Ku_T=
u_T^{\mathsf T}Ku_U=0$，所以
$$
F_0=\frac{\kappa}{2}Y^2+\gamma YT+\delta YU
+\frac{\lambda}{2}U^2.
\tag{6.4}
$$
在 $t$ 评价最高式，只有 $Y$ 极线非零，且原 $H$ 在这一评价的全部项均零。由 (6.2)，
$$
\Lambda[Y]=0.
\tag{6.5}
$$
在不含根变量的边际中，$Y$ 的全部二阶系数为零；$U$ 的自身二阶系数也为零。因此若 $b=\Lambda[U]$，完整均值梯度的 $U$ 分量为
$$
0=\Lambda[UF_0^2]=\frac{\lambda^2}{4}b^5.
$$
由 (6.3)，$b=0$。

现在一次极线只剩 $p_r,p_T$ 的线性组合，它们在 $t$ 都至少二重，故最高式左侧至少四阶。另一方面，根极线 $p_r=k(s,\cdot)$ 在 $t$ **恰二重**：如果至少三重，则离对角三次极线 $q(s,\cdot)$ 是纯三次幂，违反旧事实。在 $t$，$p_Y$ 的常数项为 $\gamma\ne0$。因此原最高式右端中
$$
2h_1p_rp_Y
\tag{6.6}
$$
恰为二阶且系数非零。其余项 $h_0p_r^2,k_0p_T^2$ 至少四阶，$2k_1p_Tp_U$ 至少三阶，无法抵消 (6.6)。矛盾。

论证使用各点的局部参数，包含双点之一为原无穷远的情况。

## 7. 型 $4s$：原两处四阶自极线的奇阶矛盾

基点只能是 $s$，所以 $k(s,\cdot)$ 在自身点至少四重。由原核
$$
q(s,s)=-s^2(s-2)(s+6)
$$
以及原无穷远正规列，自极线的阶数准确为：一般点二阶，$s=2,-6$ 时三阶，$s=0,\infty$ 时四阶。因此这里只需处理 $0,\infty$。

取局部 Taylor jets $u_0,u_1,u_2,u_3$，其中 $u_0$ 是根。原准确累积量为
$$
H=h_0u_0^2+h_1(u_0u_1^{\mathsf T}+u_1u_0^{\mathsf T})
+h_2(u_0u_2^{\mathsf T}+u_2u_0^{\mathsf T}+u_1^2)
$$
$$
\hspace{8mm}
+h_3(u_0u_3^{\mathsf T}+u_3u_0^{\mathsf T}
+u_1u_2^{\mathsf T}+u_2u_1^{\mathsf T}),
\qquad h_3\ne0.
\tag{7.1}
$$
记 $p_i=u_i^{\mathsf T}Ku(w)$。直接由原 $K$ 的相应四行，极线最低项为

| 点与局部参数 | $p_0$ | $p_1$ | $p_2$ | $p_3$ |
|---|---|---|---|---|
| $s=0,\ w=z$ | $5w^4+O(w^5)$ | $-32w^3+O(w^4)$ | $54w^2+O(w^3)$ | $-32w+O(w^2)$ |
| $s=\infty,\ u(w)=(w^5,w^4,w^3,w^2,w,1)^{\mathsf T}$ | $-w^4+O(w^5)$ | $5w^3+O(w^4)$ | $-8w^2+O(w^3)$ | $5w+O(w^2)$ |

所以
$$
v(w)^{\mathsf T}KHKv(w)
=2h_3(p_0p_3+p_1p_2)+O(w^6)
$$
的最低项分别为
$$
-3776h_3w^5,\qquad -90h_3w^5.
\tag{7.2}
$$
两者都非零，恰为奇数五阶。原最高式左端是一个非零或零物理多项式的平方，无法具有这一奇数最低阶。因此 $4s$ 型也不可能。

## 8. 合并后的准确范围

长度四非约化 divisor 的全部重数型已逐一排除，且在各型中覆盖了基点可能落入的每一个支撑点。与 [四不同点排除](R150-appendix-zero-third-cumulant-reduced-essential-four-section-is-empty.md) 合并，得到
$$
\boxed{\ V=0\text{ 且原点完整临界}
\quad\Longrightarrow\quad
\operatorname{essdim}T_3\ne4.\ }
\tag{8.1}
$$

已有本质维数至多三的完整匹配 Bell 结论继续适用；本稿没有替代或重做它。尚未覆盖的包括 $V\ne0$ 的内均值本质四维支、相关高本质维数支和全局自然幂归属。这里的空性结论准确针对已证明的 $V=0,\ \operatorname{essdim}T_3=4$ 层，不将最终目标改成“所有临界点都不存在”。
