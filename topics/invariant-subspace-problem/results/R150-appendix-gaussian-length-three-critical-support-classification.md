# R150 附录：六模式立方在总长度至多三的二阶矩 jet 支撑上的完整临界分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 本稿对原完整六模式立方的一个明确支撑类证明：在一次矩、第三累积量均为零时，总长度至多三的非退化曲线 jet 二阶矩是临界点，当且仅当其整个支撑平面对原 $K$ 全等向。由已证曲线 jet 平面分类，可进一步列尽这一类别的全部临界支撑。

这里先定义并保留 jet 矩表示；没有把任意 Hankel 矩阵自动假定成这种表示，也没有覆盖更高秩、非零一次矩或一般完整临界点。

## 1. 同一完整临界方程的二阶矩截面

沿[完整第三矩 Schur 消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)，保留原 $K,J_3,R_3(y,H)$、$V$ 和 $B_r$。取
$$
y=0,\qquad V=0,\qquad H=(H_{i+j})_{0\le i,j\le5}.
\tag{1.1}
$$
此时 $\ell=0$，完整第三矩梯度为零；一次梯度由 $y$ 的偶性为零。剩下的完整梯度准确为
$$
\partial_{H_m}R_3=-24\sum_{i+j=m}(KHKHK)_{ij}.
$$
因此 (1.1) 为完整临界点的充要条件是
$$
\boxed{\mathcal P_H(z):=v(z)^{\mathsf T}KHKHKv(z)\equiv0,}
\qquad v(z)=(1,z,\ldots,z^5)^{\mathsf T}.
\tag{1.2}
$$
其临界值自动为零：$R_3(0,H)=-8\operatorname{tr}((KH)^3)$ 对 $H$ 为齐次三次式，全部 $H$ 偏导零后由 Euler 恒等式即得目标值零。原较高显示累积量对 $F_0^3$ 的梯度已经在完整消元稿中准确消失，没有在此另删方程。

一般而言，(1.2) 不能直接替成 $HKH=0$。下面在所定义支撑类别内证明这个加强，而不是把它当作假设。

## 2. 总长度至多三的非退化 jet 矩

有限点 $s$ 使用正规曲线列 $u(\zeta)=v(\zeta)$；无穷远点使用 $u(\zeta)=(\zeta^5,\zeta^4,\ldots,1)^{\mathsf T}$ 在 $\zeta=0$ 的列。取不同支撑点，每个点的长度为 $r_\nu\ge1$，并令
$$
R=\sum_\nu r_\nu\le3.
$$
在每个支撑点取复系数 $c_{\nu,0},\ldots,c_{\nu,r_\nu-1}$，要求最高系数非零。定义
$$
\boxed{
H=\sum_\nu\sum_{j=0}^{r_\nu-1}
c_{\nu,j}
\left.\frac{d^j}{d\zeta^j}
\big(u_\nu(\zeta)u_\nu(\zeta)^{\mathsf T}\big)
\right|_{\zeta=s_\nu}.
}
\tag{2.1}
$$
无穷远项的局部基点按上述约定为零。这些都是原 Hankel 二阶矩：有限项的每个矩阵元只依赖 $i+j$，无穷远项则只占相应最高反对角线。没有实性或正性要求。

把支撑点的 jets 排成 $6\times R$ 列矩阵 $U$。由 Leibniz 公式，(2.1) 准确写成
$$
H=U C U^{\mathsf T},
$$
其中 $C$ 按支撑点分块；长度一、二、三的块分别是
$$
(a),\qquad
\begin{pmatrix}a&b\\b&0\end{pmatrix},\qquad
\begin{pmatrix}a&b&c\\b&2c&0\\c&0&0\end{pmatrix}.
\tag{2.2}
$$
最高系数非零使每个块可逆。长度至多三的曲线 jets 线性独立，故 $\operatorname{rank}H=R$，且 $\operatorname{Ran}H=\operatorname{Ran}U$。

置
$$
G=U^{\mathsf T}KU,\qquad p(z)=U^{\mathsf T}Kv(z).
$$
则完整临界多项式恰为
$$
\boxed{\mathcal P_H(z)=p(z)^{\mathsf T}C G C p(z).}
\tag{2.3}
$$
由于 $U$ 满列秩、$C$ 可逆且 $K$ 非退化，
$$
HKH=0\quad\Longleftrightarrow\quad G=0.
\tag{2.4}
$$
此外，$p(z)$ 的各分量线性独立：任何常系数关系都使 $KU\alpha$ 与全部 $v(z)$ 双线性正交；这些 $v(z)$ 张成 $\mathbb C^6$，故 $KU\alpha=0$，继而 $\alpha=0$。下面反复使用这一准确独立性。

## 3. 不同单点支撑的临界条件

先取 $H=\sum_{i=1}^R c_i u_i u_i^{\mathsf T}$，点均不同且 $c_i\ne0$。记
$$
k_{ij}=u_i^{\mathsf T}Ku_j,\qquad p_i(z)=u_i^{\mathsf T}Kv(z).
$$
曲线全在原二次零锥上，所以 $k_{ii}=0$。

长度一时 (2.3) 恒为零，且 $G=0$。
长度二时
$$
\mathcal P_H=2c_1c_2k_{12}p_1p_2.
$$
每个 $p_i$ 非零，因此临界等价于 $k_{12}=0$，亦即 $G=0$。

长度三时，在第 $i$ 个支撑点代入 (2.3)，只有另两个指标贡献，得到
$$
\mathcal P_H(z_i)=2c_jc_k\,k_{12}k_{13}k_{23}.
\tag{3.1}
$$
若点为无穷远，(3.1) 是对应齐次十次式在该点的取值，等价于原仿射多项式最高系数的取值。因此它同样由 (1.2) 控制。

所有系数非零，(3.1) 迫至少一个配对为零。不妨 $k_{12}=0$，则
$$
\mathcal P_H=2c_3p_3(c_1k_{13}p_1+c_2k_{23}p_2).
$$
由 $p_3\ne0$ 及 $p_1,p_2$ 的线性独立性，必有 $k_{13}=k_{23}=0$。故三个不同点的完整临界条件也准确等价于 $G=0$。

## 4. 一个二重点

令 $u=u(s)$、$u'=u'(s)$。曲线恒等式 $u(\zeta)^{\mathsf T}Ku(\zeta)=0$ 给
$$
u^{\mathsf T}Ku=u^{\mathsf T}Ku'=0.
$$
置 $g=(u')^{\mathsf T}Ku'$。对长度二块 (2.2)，准确有
$$
G=\begin{pmatrix}0&0\\0&g\end{pmatrix},\qquad
\mathcal P_H=b^2g\,p_0^2.
$$
因为 $b\ne0$、$p_0\ne0$，临界等价于 $g=0$，也就是整个二阶 jet 平面全等向。

## 5. 二重点加另一个单点

现在 $U=(u,u',w)$，二重点与单点不同，且
$$
C=\begin{pmatrix}a&b&0\\b&0&0\\0&0&c\end{pmatrix},\qquad bc\ne0.
$$
记
$$
g=(u')^{\mathsf T}Ku',\quad k=u^{\mathsf T}Kw,\quad l=(u')^{\mathsf T}Kw.
$$
于是
$$
G=\begin{pmatrix}0&0&k\\0&g&l\\k&l&0\end{pmatrix},
$$
$$
\mathcal P_H=b^2g p_0^2+2c(ak+bl)p_0p_2+2bck p_1p_2.
\tag{5.1}
$$
在二重点的局部坐标下，
$$
p_0(s)=p_0'(s)=p_1(s)=0,\quad
p_1'(s)=g,\quad p_2(s)=k.
$$
因此 (1.2) 的一次导数准确给
$$
0=\mathcal P_H'(s)=2bc\,g k^2.
\tag{5.2}
$$

若 $k=0$，则 (5.1) 为 $bp_0(bg p_0+2clp_2)$。独立性迫 $g=l=0$。
若 $k\ne0$，(5.2) 先给 $g=0$；此时 (5.1) 为
$$
2cp_2((ak+bl)p_0+bk p_1),
$$
与 $p_0,p_1$ 的独立性及 $bk\ne0$ 矛盾。
所以临界必有 $k=g=l=0$，亦即 $G=0$。这个推导只用正规曲线的局部导数，二重点或单点在无穷远时同样成立。

## 6. 一个三重点

令 $U=(u,u',u'')$，并取 (2.2) 的长度三块，$c\ne0$。置
$$
g=(u')^{\mathsf T}Ku',\qquad h=(u')^{\mathsf T}Ku'',\qquad j=(u'')^{\mathsf T}Ku''.
$$
两次求导曲线零式给 $u^{\mathsf T}Ku''=-g$，所以
$$
G=\begin{pmatrix}0&0&-g\\0&g&h\\-g&h&j\end{pmatrix}.
\tag{6.1}
$$
在支撑点，$p,p',p''$ 的列分别为
$$
(0,0,-g)^{\mathsf T},\qquad
(0,g,h)^{\mathsf T},\qquad
(-g,h,j)^{\mathsf T}.
$$
直接对 (2.3) 求二阶导数，得到
$$
\boxed{\mathcal P_H''(s)=6c^2g^3.}
\tag{6.2}
$$
所以完整临界条件先迫 $g=0$。此时准确简化为
$$
\mathcal P_H=(2bch+c^2j)p_0^2+4c^2h p_0p_1.
$$
由独立性及 $c\ne0$，得到 $h=j=0$。因此这个类型也必须 $G=0$。

所有长度至多三的型均已处理。反方向 $G=0\Rightarrow\mathcal P_H=0$ 直接来自 (2.3)，故得到完整等价
$$
\boxed{(y,H,V)=(0,H,0)\text{ 是完整临界点}
\quad\Longleftrightarrow\quad HKH=0}
\tag{6.3}
$$
对且只对本稿定义的总长度至多三、最高 jet 系数非零的支撑类别成立。

## 7. 该类别内全部支撑的明确清单

空支撑 $H=0$ 也显然为临界点。对非零支撑，应用[长度三全等向曲线 jet 的完全分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)，(6.3) 给出下列清单。

| 总长度 | 完整临界支撑 |
|---|---|
| 一 | 任意一个曲线点，包括无穷远点 |
| 二，不同点 | 任意满足 $k(s,t)=0$ 的一对；有限不同点等价于 $q(s,t)=0$；含无穷远时另一点只能为 $-1$ |
| 二，二重点 | 有限点 $0,2,-6$ 的一阶 jet，或无穷远的一阶 jet |
| 三 | 只有 $P_+$ 或 $P_-$ 的三个不同根；无重复点及无穷远类型 |

二重点清单使用 $g=2q(s,s)=-2s^2(s-2)(s+6)$；无穷远的 $g=e_4^{\mathsf T}Ke_4=0$。总长度三的全部重根和无穷远类型则已由前稿严格排除。每个允许支撑上的系数只须保持各最高 jet 系数非零；无需正权。

## 8. 剩余范围

本稿已经在上述低长度二阶矩类中证明了全等向性，而非仅在预设全等向平面上验证临界条件。它没有给任意 Hankel 二阶矩的低长度表示，没有覆盖总长度四及以上，也没有处理非零 $y$ 的一般完整临界点。

在本截面每个 $B_r$ 的点值都为零，但理想的局部厚化仍须另付；例如已证的 $W_+$ 二阶矩点需要区分第三与第五自然幂。不能从本稿的临界点分类直接推出任何新的全局幂归属、实际算子逆或普通 ISP 结论。
