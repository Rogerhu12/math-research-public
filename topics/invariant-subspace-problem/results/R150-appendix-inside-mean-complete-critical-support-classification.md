# R150 附录：非割线内均值、本质三维的完整临界支撑分类

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 对原六模式立方的完整临界点，若均值的 $4\times3$ Hankel 秩为三、普通第三矩的本质支撑 $W$ 为三维，且 $y\in W$，则必有 $W=W_+$ 或 $W=W_-$。本稿排除了此前保留的全部两点三次曲线余类，包括奇点位于坐标轴上的情形；没有留下“只在一般位置成立”的例外。

## 1. 定理与已经支付的归约

仍用原 $\mathcal Q_3(y,H,V)$、原非退化对称矩阵 $K$、物理曲线 $v(z)=(1,z,\ldots,z^5)$，以及
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)H(r,r)+4V(r,r,r).
$$
本稿证明
$$
\boxed{
\nabla\mathcal Q_3=0,\quad
\operatorname{rank}(y_{j+k})_{0\le j\le3,\,0\le k\le2}=3,\quad
\operatorname{ess}(T_3)=W,\quad \dim W=3,\quad y\in W
\ \Longrightarrow\ W\in\{W_+,W_-\}.
}
\tag{1.1}
$$
$W_\pm$ 是原全等向物理三点平面，其支撑多项式分别为
$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
$$

[全等向归约](R150-appendix-inside-mean-critical-support-is-isotropic.md)已经证明，除 $W_\pm$ 外，唯一可能是 $W=W^{\perp_K}$、$W\cap v(\mathbb P^1)$ 为准确长度二的除子，且 $H,V$ 的最小并支撑就是该除子，$y$ 在其外。其物理投影是双有理不可约平面三次曲线。

[双 jet 排除](R150-appendix-inside-mean-double-jet-residual-exclusion.md)与[两点极线限制](R150-appendix-inside-mean-reduced-support-and-simple-polars.md)进一步把余类准确限制为
$$
D=s+t,\qquad s\ne t,\qquad s,t\notin\{0,2,-6,\infty\},
\qquad k(s,t)=0,
\tag{1.2}
$$
$$
H=h_s v(s)^2+h_t v(t)^2,\qquad
V=v_s v(s)^3+v_t v(t)^3,\qquad
(h_i,v_i)\ne(0,0)\quad(i=s,t).
\tag{1.3}
$$
令 $G(z)=(z-s)(z-t)$，并把
$$
A=\frac{k(s,z)}{G(z)},\qquad B=\frac{k(t,z)}{G(z)},\qquad
P=\frac{y^{\mathsf T}Kv(z)}{G(z)}
$$
齐次化为二元三次式。它们无共同零点，定义上述双有理三次参数化，其不可约方程为
$$
\mathcal C(Y,X,Z)=Y^3-6Y(h_sX^2+h_tZ^2)+4(v_sX^3+v_tZ^3)=0.
\tag{1.4}
$$
已知 $A,B$ 互素且各自无重根。三次曲线有理，因而有奇点。[内点节点排除](R150-appendix-inside-mean-interior-node-exclusion.md)已经排除奇点三个坐标同时非零的全部情况。下面将剩余零坐标情形全部排除。

## 2. 零坐标奇点的准确归一化

先设奇点满足 $Y=0$。若 $XZ\ne0$，两个支持坐标的一阶方程给 $v_s=v_t=0$，使 (1.4) 含因子 $Y$，违背不可约性。若 $X=0,Z\ne0$，则 $\mathcal C_Y=\mathcal C_Z=0$ 给 $h_t=v_t=0$，违背 (1.3)；交换两点后同理。因此每个剩余奇点都有 $Y\ne0$。

由已经排除的内点情形，该奇点必有 $X=0$ 或 $Z=0$；二者不能同时为零，因为这时 $\mathcal C_Y=3Y^2\ne0$。交换两个物理支持点后，只须处理 $X=0$。非零缩放 $Y,Z$，可将奇点归一为 $[1:0:1]$。一阶方程准确给出 $h_t=v_t=1/2$。于是同一三次式成为
$$
\mathcal C=(Y-Z)^2(Y+2Z)-6hYX^2+4\eta X^3,
\qquad (h,\eta)\ne(0,0).
\tag{2.1}
$$
这里没有假设 $h\ne0$：下面的计算同时包含可能的尖点退化。

在图 $Z=1$ 中，以通过奇点的直线 $[Y-1:X]=[r:u]$ 求第三个交点，得到
$$
\begin{aligned}
Y&=-2r^3+4\eta u^3,\\
X&=6hu^3-3r^2u,\\
Z&=r^3-6hru^2+4\eta u^3.
\end{aligned}
\tag{2.2}
$$
其有理逆是 $[Y-Z:X]=[r:u]$。该参数化无基点：若三式同时为零，则 $u\ne0$，并有
$$
(r/u)^2=2h,\qquad \eta=h(r/u).
$$
若 $h=0$，这迫 $\eta=0$，违背 (2.1)。否则令 $c=r/u$；直接代入 (2.1) 可见 $Y-Z-cX$ 是一个线性因子，因为 $c^2=2h,\eta=hc$。这也与不可约性冲突。因此原参数化 $(P,A,B)$ 与 (2.2) 只差共同 $\mathrm{PGL}_2$ 参数变换及三个坐标各自的非零缩放。

## 3. 轴奇点强制的两个不变量

对于升幂系数为 $(a_0,a_1,a_2,a_3)$、$(b_0,b_1,b_2,b_3)$ 的二元三次式，记
$$
J(A,B)=3a_0b_3-a_1b_2+a_2b_1-3a_3b_0,
$$
$$
C_{ij}(A,B)=[\lambda^i\mu^j]\operatorname{disc}(\lambda A+\mu B),\qquad i+j=4.
\tag{3.1}
$$
共同 $M\in\mathrm{GL}_2$ 参数变换分别使 $J,C_{ij}$ 乘以 $\det(M)^3,\det(M)^6$；分别缩放 $A,B$ 时，$C_{22}$ 与 $J^2$ 同乘以两个缩放量的平方乘积。因此下面两个身份的零性在原参数化与 (2.2) 之间保持不变。

在 (2.2) 中，$X,Z$ 的升幂系数为
$$
X=(6h,0,-3,0),\qquad Z=(4\eta,-6h,0,1).
$$
直接展开得到
$$
J(X,Z)=36h,
$$
$$
\operatorname{disc}(\lambda X+\mu Z)
=648h\lambda^4+432\eta\lambda^3\mu+1296h^2\lambda^2\mu^2
 +(864h^3-432\eta^2)\mu^4.
$$
故原物理极线必有
$$
\boxed{C_{22}(A,B)-J(A,B)^2=0,\qquad C_{13}(A,B)=0.}
\tag{3.2}
$$
这是同一两条物理极线的必要条件，没有把它们改成任意无重三次式。它也没有排除 $h=0$ 后才成立的限制。

## 4. 原极线的整数消去

原核写成 $k(s,t)=-(s-t)^2q(s,t)$，其中
$$
q=s^3t+st^3-3s^2t^2+s^3+t^3-3s^2t-3st^2-5s^2-5t^2+22st.
\tag{4.1}
$$
在 $q(s,t)=0$ 上，令
$$
\alpha=s+1,\quad\beta=-3s^2-3s-5,\quad\gamma=s^3-3s^2+22s,
$$
则 $A=-(z-s)q(s,z)/(z-t)$ 的升幂系数准确为
$$
\begin{aligned}
a_0&=s(\gamma+\beta t+\alpha t^2),\\
a_1&=s(\beta+\alpha t)-(\gamma+\beta t+\alpha t^2),\\
a_2&=s\alpha-(\beta+\alpha t),\qquad a_3=-\alpha.
\end{aligned}
\tag{4.2}
$$
$B$ 由交换 $s,t$ 得到。用 (4.2) 定义 $E=C_{22}-J^2$ 与 $L=C_{13}$ 为原整数二元多项式。普通三次判别式在此取约定
$$
\operatorname{disc}(az^3+bz^2u+czu^2+du^3)
=b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd.
$$

先假设 $s\ne-1$。在 $\mathbb Q(s)[t]$ 中作以 $t$ 为变量的余式，定义
$$
R(s,t)=\frac{(s+1)^4}{6}\operatorname{rem}_t(E,q),\qquad
F(s,t)=\frac{(s+1)^6}{2}\operatorname{rem}_t(L,q).
\tag{4.3}
$$
这两个式事实上属于 $\mathbb Z[s,t]$，且各自的 $t$ 次数至多二。其全部整数系数列在[随稿验证器](../notes/2026-11-13-inside-mean-axis-singularity-exclusion-verify.py)的 R_rows、F_rows；该程序还直接从 (4.2) 重建 $E,L$ 并核对两个伪余式为零。因而任何 $q=E=L=0$ 且 $s\ne-1$ 的点都有 $R=F=0$。

两个原 Sylvester 行列式准确分解为
$$
\operatorname{Res}_t(q,R)=-s^4(s+1)^8P_{28}(s),
$$
$$
\operatorname{Res}_t(q,F)=s^4(s+1)^{12}(s-5)^3Q_{22}(s).
\tag{4.4}
$$
这里 $P_{28},Q_{22}$ 的下标是准确次数，它们在验证器及[完整回执](../notes/2026-11-13-inside-mean-axis-singularity-exclusion-verification.json)中列出全部整数系数；最高系数分别为 $12150,360848$。以下是排除公共根所需的全部数值身份：
$$
P_{28}(5)=111771310667503789670400000\ne0,
\tag{4.5}
$$
$$
12150\equiv99,\quad360848\equiv39\pmod{103},\qquad
\operatorname{Res}(P_{28},Q_{22})\equiv97\pmod{103}.
\tag{4.6}
$$
次数在模 $103$ 后完整保持，因此 (4.6) 说明原整数结果式非零，$P_{28},Q_{22}$ 在 $\mathbb C$ 上互素。为使这个非零断言还可逐系数检查，下面列出一组 Bézout 系数。若 $U,V$ 的升幂系数分别为
$$
\begin{aligned}
U: (&38,-12,50,24,-32,-23,-36,13,-51,-2,18,-6,\\
&-48,3,-20,49,41,-19,-46,-4,-41,-7),\\
V: (&18,6,23,33,-44,46,26,17,49,-5,15,-39,43,-39,\\
&-8,28,9,12,-46,44,-24,35,42,1,-45,24,-36,-6),
\end{aligned}
$$
则
$$
UP_{28}+VQ_{22}\equiv1\pmod{103}.
\tag{4.7}
$$

由 (1.2) 已知 $s\ne0$。在目前的 $s\ne-1$ 图中，(4.4) 迫 $P_{28}(s)=0$ 及 $(s-5)^3Q_{22}(s)=0$；(4.5) 排除 $s=5$，从而迫 $P_{28},Q_{22}$ 有公共根，与 (4.6) 矛盾。

最后单独处理被 (4.3) 的除法排除的图 $s=-1$。回到未经余式化的原多项式，直接有
$$
q(-1,t)=-5t^2-26t-6,
$$
$$
\operatorname{rem}_t(E(-1,t),q(-1,t))
=\frac{384}{125}(1338022t+291267),
$$
$$
\operatorname{Res}_t\bigl(q(-1,t),E(-1,t)\bigr)
=30471386056704000\ne0.
\tag{4.8}
$$
所以这个图上连 $q=E=0$ 都不可能。有限 $s$ 全部处理完毕；无穷远已在 (1.2) 中由原物理接触计算排除。

随稿程序使用整数二元多项式、精确伪除法、两个 $5\times5$ 多项式 Sylvester 行列式及有限域 Bézout 身份，核对 (4.3)–(4.8) 的全部身份；固定图 (4.8) 使用有理数行消元。它不以有限域无解代替复数域无解，复数域结论来自完整次数保持的非零整数结果式。

## 5. 完整分类与原匹配 Bell 值

§§2–4 排除全部带零坐标的奇点；内点奇点已由前稿排除。有理不可约三次曲线必有奇点，故 (1.2)–(1.4) 的整个两点余类不存在。结合长度三、全等向、双 jet 的已证归约，得到 (1.1)。

此时原前三累积量均支持于 $W_+$ 或 $W_-$。按[两平面的完整矩判据](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)，完整临界性恰对应于该物理二次曲线方程 $Q_\pm$ 整除 $T_3|_{W_\pm}$。因此原三个匹配 first Bell 方向在本稿整个内均值类上的普通第三矩均为零：它们满足已付的两个方程 $q_+(r)=q_-(r)=0$，而 $T_3|_{W_\pm}=Q_\pm L$。

本稿的范围准确限于非割线均值、本质三维、$y\in W$。外均值、均值 Hankel 秩降至二以下、第三矩本质维数四至六，以及全局 Jacobian 自然幂和实际 Bell 逆仍须另外处理；这些未解项不影响本稿已经完成的支撑分类。
