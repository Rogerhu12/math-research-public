# R150 附录：非零一次矩、完整第三矩为零的全部立方临界点

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明的完整扇区分类。** 对原六模式完整立方，假设一次矩 $y\ne0$ 且整个第三普通矩张量 $T_3$ 为零。本文列尽这一范围的所有完整临界点。除两个不同曲线点的有限原子族及单点族外，还存在四个特定曲线点上的切向二阶矩族。没有假设原 $H$ 已有有限支撑，没有删去任何原低阶梯度，也不宣称所有临界点的 $T_3$ 都为零。

## 1. 原张量与结论

沿用[完整第三矩 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)的原可逆矩阵 $K$、$F_0(x)=\tfrac12x^{\mathsf T}Kx$、$v(s)=(1,s,\ldots,s^5)^{\mathsf T}$。二、三阶累积量张量为
$$
H_{ij}=H_{i+j},\qquad V_{ijk}=V_{i+j+k}.
$$
这里的 $H,V$ 不是第二、第三普通矩。真正第三普通矩是
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)(r^{\mathsf T}Hr)
       +4\sum_{i,j,k}V_{i+j+k}r_i r_j r_k.
\tag{1.1}
$$
假设 $T_3\equiv0$ 且 $y\ne0$。

**定理。** 该参数组为原完整 $\mathcal Q_{F_0^3}$ 的临界点，当且仅当属于以下清单。全部系数允许为复数，曲线支撑也包括射影点 $\infty$。

**A. 两个不同支撑点。** 取不同的 $s,t\in\mathbb P^1$、所选非零曲线代表 $u=v(s),w=v(t)$，及 $a,b\ne0$，有
$$
\boxed{
 y=au+bw,\quad
 H=\tfrac12a^2uu^{\mathsf T}+\tfrac12b^2ww^{\mathsf T},\quad
 V=\tfrac12a^3u^{\otimes3}+\tfrac12b^3w^{\otimes3}.}
\tag{1.2}
$$
在 $\infty$ 使用 $v(\infty)=e_5$；改变曲线代表只相应重标量 $a,b$。

**B. 一个支撑点及其切向。** 取 $s\in\mathbb P^1$，令 $u$ 为曲线代表、$w$ 为一个非零局部切向代表，并取 $a\ne0,c,d\in\mathbb C$。有
$$
\boxed{
\begin{aligned}
y&=au,\\
H&=c\,uu^{\mathsf T}+d(uw^{\mathsf T}+wu^{\mathsf T}),\\
V&=\frac{6ac-a^3}{4}\,u^{\otimes3}
 +ad\,(u\otimes u\otimes w+u\otimes w\otimes u+w\otimes u\otimes u),
\end{aligned}}
\tag{1.3}
$$
并且
$$
\boxed{d=0\quad\text{或}\quad s\in\{0,2,-6,\infty\}.}
\tag{1.4}
$$
有限点用 $w=v'(s)$；在 $\infty$ 用局部曲线 $(z^5,z^4,z^3,z^2,z,1)$ 的导数 $w=e_4$。在 (1.4) 的四点处可取任意 $d$。

清单中所有匹配第三 Bell 值均严格为零，因为它们就是 (1.1)。这仍是点值结论，不是全局统一自然幂或实际算子逆证书。

## 2. Hankel 二阶差分强迫一次矩只有二点支撑

将 $T_3$ 看作变量 $r_0,\ldots,r_5$ 的三次多项式。对 $0\le i,j\le4$，令
$$
\mathcal D_{ij}=\partial_{r_{i+1}}\partial_{r_j}
                -\partial_{r_i}\partial_{r_{j+1}}.
$$
Hankel 性使 $\mathcal D_{ij}$ 湮灭 $r^{\mathsf T}Hr$ 及三次 $V$ 多项式。由 $\mathcal D_{ij}T_3=0$ 比较剩余一次式，得到准确向量等式
$$
(y_{i+1}y_j-y_i y_{j+1})y
=2(y_{i+1}H_j+y_jH_{i+1}-y_iH_{j+1}-y_{j+1}H_i),
\tag{2.1}
$$
其中 $H_j$ 是原矩阵第 $j$ 行转置。

置
$$
M=H-\tfrac14yy^{\mathsf T},\quad
Y_0=(y_0,\ldots,y_4),\quad Y_1=(y_1,\ldots,y_5).
$$
对 $M$ 的每个固定列，将前、后五项分别记为 $M_0,M_1$。式 (2.1) 准确变成
$$
\boxed{Y_1\wedge M_0=Y_0\wedge M_1.}
\tag{2.2}
$$
注意 $M$ 本身一般不是 Hankel；这里只使用原 $H$ 的 Hankel 性。

先假设 $Y_0,Y_1$ 线性无关。将 (2.2) 分别再楔乘 $Y_0,Y_1$，可知 $M_0,M_1\in\operatorname{span}\{Y_0,Y_1\}$；再比较 $Y_0\wedge Y_1$ 的系数，有某些列相关标量 $\alpha,\beta,\gamma$ 使
$$
M_0=\alpha Y_0+\beta Y_1,\qquad
M_1=\gamma Y_0-\alpha Y_1.
\tag{2.3}
$$
两段的四个重叠项给
$$
\beta y_{j+2}+2\alpha y_{j+1}-\gamma y_j=0,
\qquad 0\le j\le3.
\tag{2.4}
$$

如果 $4\times3$ Hankel 矩阵
$$
\mathsf Y=(y_{j+k})_{0\le j\le3,\,0\le k\le2}
$$
的秩为三，则每列的 $\alpha,\beta,\gamma$ 都为零，从而 $M=0$。但这使 $H=yy^{\mathsf T}/4$ 是 Hankel，故 $y_{i+1}y_j=y_i y_{j+1}$ 对全部 $i,j$ 成立，与 $Y_0,Y_1$ 独立矛盾。因此
$$
\operatorname{rank}\mathsf Y\le2.
\tag{2.5}
$$

为同时保留退化首块和无穷远，使用一个有限的二元配对。定义 $\Lambda_y:\mathbb C[X_0,X_1]_5\to\mathbb C$，令
$$
\Lambda_y(X_0^{5-j}X_1^j)=y_j,
$$
并令 $I_k$ 是对全部次数 $5-k$ 乘子配对为零的 $k$ 次形式。记 $b_k=\dim S_k/I_k$。配对转置给 $b_k=b_{5-k}$。若 $I_k\ne0$，则
$$
\dim(X_0I_k+X_1I_k)\ge\dim I_k+1,
$$
所以从首次非零 $I_k$ 起，$b_k$ 不增。这个维数不等式可用各元素不同的最高单项式指数及集合 $A\cup(A+1)$ 直接证明。

当前 $Y_0,Y_1$ 独立给 $b_1=2$，而 (2.5) 给 $b_2\le2$。由 $b_4=b_1=2$ 及上述不增性，必有 $b_2=2$，故 $I_2$ 恰由一个非零二次式 $g$ 生成。$\Lambda_y$ 杀掉 $gS_3$；二维商 $S_5/gS_3$ 的有限除法与中国剩余定理说明，$y$ 有且只有以下两类长度二表示：

- 两个不同曲线点：$y=au+bw$，两个系数非零；
- 一个二重点：$y=au+bw$，其中 $w$ 是切向，$b\ne0$。

这不是无限矩延拓，也不要求实性、正性或首主块非退化。射影换元保留全部物理 Hankel 张量空间；可选择仿射图使二次式的全部根有限，以下暂在该图中计算。

## 3. 非曲线一次矩：只有两个不同点的原子族

在上一节的仿射图中，$g$ 的最高系数非零，且 (2.4) 的关系空间是一维。把 $y_6$ 按同一二阶递推延长一次。由 (2.3)、(2.4)，每列最后一项也满足
$$
M_5=\gamma y_4-\alpha y_5=\alpha y_5+\beta y_6.
$$
因此每个完整六项列都是 $y$ 及其移位的线性组合。这两列都在上述二点/二jet空间 $W$ 内，所以
$$
\operatorname{Ran}H\subseteq W.
\tag{3.1}
$$
对称性进一步给 $H=UCU^{\mathsf T}$，其中 $U=(u,w)$、$C$ 为二阶对称矩阵。

### 3.1 两个不同点

令 $u=v(s),w=v(t)$、$s\ne t$，并写 $X=u^{\mathsf T}r,Y=w^{\mathsf T}r$。$H_{02}=H_{11}$ 迫交叉系数乘 $(s-t)^2$ 为零，故
$$
r^{\mathsf T}Hr=cX^2+dY^2.
$$
由 $T_3=0$，三次 $V$ 多项式也仅依赖 $X,Y$。原 Hankel 差分 $\partial_{r_0}\partial_{r_2}-\partial_{r_1}^2$ 在这个二变量空间上就是 $(s-t)^2\partial_X\partial_Y$，故
$$
V(r,r,r)=eX^3+fY^3.
$$
比较 $T_3$ 的 $X^2Y$、$XY^2$ 系数，因 $a,b\ne0$，得到
$$
c=a^2/2,\qquad d=b^2/2.
$$
再比较两项纯立方，得到 $e=a^3/2,f=b^3/2$，正是 (1.2)。

### 3.2 一次矩本身含真正切向分量不可能

令 $u=v(s),w=v'(s)$，且 $y=au+bw$、$b\ne0$。同一 Hankel 条件迫
$$
r^{\mathsf T}Hr=cX^2+2dXY;
$$
因为 $w_0w_2-w_1^2=-1$，不能有 $Y^2$ 项。上述差分在 $X,Y$ 上变成 $-\partial_Y^2$，所以 $V$ 也只能有 $X^3,X^2Y$ 项。

于是 $T_3$ 的 $Y^3$ 系数恰为 $b^3\ne0$，与 $T_3=0$ 矛盾。二重点的一次矩类型全部被排除，包括射影换回后的无穷远二重点。

## 4. 曲线一次矩：全部二阶、三阶矩也被确定

若 $Y_0,Y_1$ 相关，则非零 $y$ 本身是曲线点的倍数，包括 $Y_0=0$ 给出的 $e_5$。可作射影换元使 $y=ae_0$、$a\ne0$。

在 (2.1) 中取 $i=0$、$1\le j\le4$，得到原 $H$ 的第 $2,3,4,5$ 行全部为零。Hankel 性因此迫
$$
H_2=H_3=\cdots=H_{10}=0.
$$
所以 $H$ 恰为 (1.3) 的形式。再由 $T_3=0$ 比较 $X^3$、$X^2Y$，唯一得到该式所列 $V$；更高物理 $V_n$ 均为零。射影换回即得到任意支撑点上的 (1.3)。至此仅使用 $T_3=0$，尚未使用其余低阶临界方程。

## 5. 保留全部低阶梯度后，准确留下四个切向点

记
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad T_2=yy^{\mathsf T}-2H.
$$
由完整 Schur 稿中未消去 $V$ 的公式逐项对 $H$ 求导，或直接对完整普通矩泛函求二阶物理导数，得到
$$
\boxed{
-\frac16\sum_{m=0}^{10}z^m\partial_{H_m}\mathcal Q_3
=T_3(p,Kv(z),Kv(z))-F\,T_2(Kv(z),Kv(z))
 +4v(z)^{\mathsf T}KHKHKv(z).
}
\tag{5.1}
$$
这里 $T_3(\cdot,\cdot,\cdot)$ 表示 (1.1) 的对称三线性极化。等式仍含原所有十一条 $H$ 梯度。

对 (1.3)，原曲线关系及其一阶导数给
$$
u^{\mathsf T}Ku=u^{\mathsf T}Kw=0,
\qquad F=0,
\qquad HKH=d^2g(s)\,uu^{\mathsf T},
\quad g(s)=w^{\mathsf T}Kw.
\tag{5.2}
$$
因 $K$ 可逆且曲线张成整个六维空间，$u^{\mathsf T}Kv(z)$ 不是零多项式。由 (5.1) 和 $T_3=0$，全部二阶梯度为零当且仅当
$$
d^2g(s)=0.
\tag{5.3}
$$

此条件也足以使所有剩余梯度为零。若 $d=0$，全部累积量支持全等向直线 $\mathbb Cu$。若 $g(s)=0$，则全部累积量支持全等向二平面 $W=\operatorname{span}\{u,w\}$。在两种情况下，$F_0|_W=0$；完整矩泛函仅由 $W$ 内的平移和常系数导数组成，故它湮灭所有限制到 $W$ 后恒为零的多项式。于是
$$
\partial_{y_i}\mathcal Q_3=3\Lambda[F_0(x)^2(Kx)_i]=0,
\qquad
\partial_{H}\mathcal Q_3=0,
$$
而全部十六条第三梯度已经由 $T_3=0$ 付清。更高累积量的导数恒等为零，完整性未丢失。

有限点处，原双点配对满足
$$
k(s,t)=v(s)^{\mathsf T}Kv(t)=-(s-t)^2q(s,t),
\quad q(s,s)=-s^2(s-2)(s+6).
$$
所以
$$
g(s)=v'(s)^{\mathsf T}Kv'(s)=2q(s,s)
=-2s^2(s-2)(s+6).
$$
在 $\infty$，$u=e_5,w=e_4$，$g(\infty)=K_{44}=0$。这准确给出 (1.4)，没有遗漏射影点。

最后，(1.2) 的全部临界条件由[有限原子普通矩族](R150-appendix-finite-atomic-ordinary-moment-critical-families.md)付清：完整矩生成函数可取 $(1+a\,u^{\mathsf T}t)(1+b\,w^{\mathsf T}t)$，次数大于二的全部普通矩均为零；原 $F_0^3$ 的非零物理导数所需矩次数至少三。因此它是完整临界族，无需 $u,w$ 相互 $K$ 正交。

## 6. 本结论解决的范围

本文从原 $T_3=0$ 本身导出二点支撑，没有另设 $H$ 的秩或支撑假设。它列尽了该范围内全部非零一次矩临界点，并给出了此前两原子图之外的四个切向支撑族；每个切向族在 $a\ne0$ 时允许独立参数 $a,c,d$。

$y=0$ 时，$T_3=0$ 只迫 $V=0$，一般 $H$ 仍须另外满足完整 Gaussian 临界条件；其秩至多三的范围见[已付分类](R150-appendix-all-rank-three-hankel-gaussian-critical-points.md)。$T_3\ne0$ 的非零一次矩临界点没有被本文排除，原三个方向的全局 Bell 自然幂归属及普通 ISP 仍未完成。
