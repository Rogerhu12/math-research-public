# R150 附录：满秩外均值的两个双支点全部排除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 在原 mean 的 $4\times3$ Hankel 矩阵秩三、非零 $T_3$ 本质空间三维、mean 在该空间之外且 $H$ 秩四的完整立方临界截面中，共同支撑不可能为 $2s+2t$，其中 $s\ne t$，允许无穷远。二次像分支由基点数排除；普通权值的节点三次分支由两个互素的一元兼容多项式排除；剩余退化分支只可能落在原支点对 $\{0,\infty\}$，又由二阶接触与三阶余项不相容排除。

结合[四重支点](R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md)与[三重加单点](R150-appendix-three-plus-one-full-rank-outer-mean-critical-exclusion.md)的结果，本文截面的非约化支撑只剩 $2+1+1$。四个不同点的无基点情形与其他秩层仍未在本文闭合。

## 1. 原矩的规范式及完整梯度

由[非约化中心三次分类](R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)，按同一原 $\lambda$ 归一各支撑点，再分别可逆缩放局部参数，可取
$$
\mathcal A=\mathbb C[\varepsilon]/(\varepsilon^2)\oplus
\mathbb C[\eta]/(\eta^2),\qquad
\tau(1_s)=\mu,\quad\tau(\varepsilon)=1,\quad
\tau(1_t)=1-\mu,\quad\tau(\eta)=1.
\tag{1.1}
$$
这里 $\mu$ 是复数，暂允许 $0,1,1/2$。$H$ 满秩只要求两块的最高 nilpotent 权非零，故归一没有删掉总权为零的块。原张量准确为
$$
y(r)=\tau(X),\qquad H(r,r)=\tfrac14\tau(X^2),\qquad
V(r,r,r)=\tfrac18\tau(X^3).
\tag{1.2}
$$
以两块的第零、第一 jet 为基 $u_0,u_1,w_0,w_1$，原对角恒等式给
$$
\overline K=
\begin{pmatrix}
0&0&c&d\\
0&a&e&f\\
c&e&0&0\\
d&f&0&b
\end{pmatrix}.
\tag{1.3}
$$
全部必要梯度条件关于 $\overline K$ 齐次，因此在证明 $c\ne0$ 后可在这些代数条件中除以 $c$，取 $c=1$。这不更改原物理核，而是齐次方程的归一。

使用[三重加单点稿](R150-appendix-three-plus-one-full-rank-outer-mean-critical-exclusion.md) §2 的原完整公式
$$
G=(F^2-2pHp+2\operatorname{tr}(\overline KH)^2)y-4FHp
 +8H\overline KHp+4V(p,p)-8V:\overline KH\overline K,
$$
$$
p=\overline Ky,\quad F=y^{\mathsf T}\overline Ky/2,\quad
N=(T_3)_p-F(yy^{\mathsf T}-2H)+4H\overline KH.
\tag{1.4}
$$
完整临界点满足 $G=0$、原物理二次恒等式以及最高三次恒等式。记
$$
\mathcal G=128G,\qquad
\mathcal H_0=32(\overline KN\overline K)_{00},\qquad
\mathcal V_j=8[z^j]T_3\bigl(\overline K(1,z,0,0)^{\mathsf T}\bigr).
\tag{1.5}
$$
另一个支撑块使用交换两块后的同样记号。所有这些量都必须为零。

[精确重构器](../notes/2026-11-13-two-plus-two-critical-exclusion-verify.js)从 (1.1)–(1.5) 重建全部原张量及相关多项式，核验下文使用的恒等式、有限域 Bézout 见证与原核接触数据。[完整输出](../notes/2026-11-13-two-plus-two-critical-exclusion-certificate.json)的实际结果为 all_pass: true。下文给出包括全部例外值的代数证明。

## 2. 零交叉值与半权分支均不可能

若 $c=0$，两支点的最高梯度常数项分别为
$$
8T_3(\overline Ku_0)=8d^3,\qquad
8T_3(\overline Kw_0)=8e^3.
$$
故 $d=e=0$。此时 (1.3) 的第零行和第二行都为零，意味着两个不同物理支点 $s,t$ 都是整个四维投影的基点。这违反[任意长度四物理投影至多一个简单基点](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)。因此
$$
\boxed{c\ne0.}
\tag{2.1}
$$

若 $\mu=1/2$，[中心三次分类](R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)证明原三维物理像必须是光滑二次曲线。而[原光滑二次中心定理](R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md)证明，在本文满秩截面中无基点的四维投影只能给三次像。因此四维投影必须有基点。

上述基点定理还证明每个基点属于共同支撑 $g$，所以这里只能是 $s$ 或 $t$。任一个成为基点都会使 $c=0$，与 (2.1) 矛盾。故
$$
\boxed{\mu\ne\tfrac12.}
\tag{2.2}
$$
以后在齐次必要条件中固定 $c=1$。

## 3. 直接排除总权零的两个例外值

先取 $\mu=0$。最高梯度常数项给 $\mathcal V_0=8d^3$，故 $d=0$；随后第一 jet 梯度给 $\mathcal V_1=12a$，故 $a=0$。在 $\mu=0,a=d=0,c=1$ 上，完整梯度准确给
$$
32[z]\,\rho(z)^{\mathsf T}\overline KN\overline K\rho(z)=-16bf,
$$
$$
\mathcal G_2=-32b(b+2f),\qquad
\mathcal G_3=32b^2+128bf+128f^2-64be,
\quad \rho(z)=(1,z,0,0)^{\mathsf T}.
$$
第一式迫 $bf=0$，第二式遂迫 $b=0$，第三式再迫 $f=0$。最后两个 $y$ 梯度化为
$$
\mathcal G_0=64e(1-e),\qquad
\mathcal G_1=32(1-4e+2e^2).
$$
前式使 $e^2=e$，后式遂使 $e=1/2$，矛盾。交换两支撑块即排除 $\mu=1$。因此只须处理
$$
\boxed{\mu\notin\{0,\tfrac12,1\}.}
\tag{3.1}
$$

## 4. 两端 jet 梯度的三个短恒等式

令
$$
\theta=2\mu-1,\qquad A=1+\theta=2\mu,\qquad
B=1-\theta=2(1-\mu).
$$
在 $c=1$ 上，最高梯度的常数项准确为
$$
P(d)=\mathcal V_0
 =8d^3-12A d^2+6A\theta d+\theta-\theta^3.
\tag{4.1}
$$
记 $P_d$ 为对 $d$ 的导数，并置
$$
R_1=4d^2-4\theta d+\theta^2-\theta,\qquad
R_2=4d^2-4(\theta+2)d+(\theta+1)(\theta+2).
\tag{4.2}
$$
从原张量直接展开可得三个完整多项式恒等式：
$$
\boxed{\begin{aligned}
\mathcal V_1&=P_d(f-de)+3eP+6R_1a,\\
dP_d&=3AR_1+3P,\\
3\mathcal H_0-6AP-4\mathcal V_1&=12(R_2b-R_1a).
\end{aligned}}
\tag{4.3}
$$
这三条在整个六变量空间成立，没有先除掉可能为零的变量。精确证书逐系数重构它们；另一支点的恒等式由
$$
(\mu,a,b,d,e)\longleftrightarrow(1-\mu,b,a,e,d)
$$
取得。

引入
$$
r=2d-A,\qquad s=2e-B.
$$
两个常数项恒等式化为
$$
r^3=A(3r+2),\qquad s^3=B(3s+2),\qquad A+B=2.
\tag{4.4}
$$
由 (3.1)，$r,s$ 均不为 $0,-1,-2$；例如这些三个值依次迫 $A=0,1,2$。$3r+2$、$3s+2$ 也不能为零。于是
$$
d=\frac{r(r+1)(r+2)}{2(3r+2)}\ne0,\qquad
R_1=\frac{2(r+1)^2(r+2)}{3r+2}\ne0,
\tag{4.5}
$$
另一个支点的对应量亦非零。

置 $\Delta=de-f$。因 $P=\mathcal V_1=0$，前两条 (4.3) 给
$$
\boxed{ad=\mu\Delta,\qquad be=(1-\mu)\Delta.}
\tag{4.6}
$$
第三条给 $R_2b=R_1a$，以及其交换版本。下面分别处理 $\Delta\ne0$ 与 $\Delta=0$。

## 5. 非退化交叉块：两个一元多项式互素

若 $\Delta\ne0$，由 (3.1)、(4.5)–(4.6) 可合法消去 $a,b,d,e,R_1$。代入
$$
R_2=\frac{2r(r^2-2r-2)}{3r+2}
$$
后，$R_2b=R_1a$ 准确化为
$$
e=(1-\mu)\frac{r^2-2r-2}{r(r+1)}.
$$
结合 $B=2(1-\mu)=2-r^3/(3r+2)$，得到
$$
\boxed{s=T(r),\qquad r=T(s),\qquad
T(x)=\frac{x^3-6x-4}{x(x+1)}.}
\tag{5.1}
$$
所有分母在 (3.1) 下已经逐一排除为零。

令
$$
N(x)=x^3-6x-4,\qquad L(x)=x(x+1).
$$
从 $s=N(r)/L(r)$ 和第二个三次关系 (4.4)，除去已知非零的 $N(r)$，得到
$$
Q(r)=0,\qquad
Q=(3r+2)N^2+3NL^2+2L^3.
$$
从 $r=T(s)$ 得到
$$
J(r)=0,\qquad
J=N^3-6NL^2-4L^3-rNL(N+L).
$$
完整展开是
$$
\begin{aligned}
Q={}&6r^7+10r^6-45r^5-90r^4+52r^3+204r^2+144r+32,\\
J={}&-2r^8-14r^7-3r^6+114r^5+158r^4-148r^3\\
&\hspace{14mm}-424r^2-288r-64.
\end{aligned}
\tag{5.2}
$$
两个最高系数 $6,-2$ 模 $103$ 均非零，故完整次数保持。按常数项在前，取
$$
U=(93,90,11,92,76,4,23,59),\qquad
W=(32,33,86,69,24,52,74).
$$
逐系数有
$$
\boxed{U\overline Q+W\overline J=1
\quad\text{于 }\mathbb F_{103}[r].}
\tag{5.3}
$$
完整次数保持与 Gauss 引理遂给 $Q,J$ 在 $\mathbb Q[r]$、亦在 $\mathbb C[r]$ 中互素。因此不存在同时满足 (5.2) 的复数 $r$，整个 $\Delta\ne0$ 分支排除。

## 6. 退化交叉块只剩原支点对 $\{0,\infty\}$

若 $\Delta=0$，(4.6) 及 $d,e\ne0$ 给
$$
a=b=0,\qquad f=de.
\tag{6.1}
$$
第一 jet 向量在原曲线归一和重参数化后只变为 $v'(s)$ 的非零倍数加 $v(s)$ 的倍数。原 $vKv=vKv'=0$，所以 $a=0$ 准确迫原切向量零长。有限支点有
$$
v'(s)^{\mathsf T}Kv'(s)=-2s^2(s-2)(s+6).
$$
无穷远的原第一 jet 是 $e_4$，同样零长。因此两个支点只能从
$$
\{0,2,-6,\infty\}
$$
中选取。

$f=de$ 又使两块交叉配对矩阵的行列式为零；这个零值在两个块的可逆三角 jet 变换及整体缩放下保持。直接从原 $K$ 计算，六对不同支点的交叉行列式为：

| 支点对 | $\det\begin{pmatrix}v(s)Kv(t)&v(s)Kv'(t)\\v'(s)Kv(t)&v'(s)Kv'(t)\end{pmatrix}$ |
|---|---:|
| $0,2$ | $2048$ |
| $0,-6$ | $25380864$ |
| $0,\infty$ | $0$ |
| $2,-6$ | $536870912$ |
| $2,\infty$ | $-40$ |
| $-6,\infty$ | $-120$ |

无穷远列使用其齐次第零、第一 jets $e_5,e_4$。所以唯一剩余支点对是 $\{0,\infty\}$。

## 7. 原两端极线的二阶接触给最终矛盾

交换两块后可令第一块在 $0$，第二块在 $\infty$。原物理极线分别为
$$
\begin{aligned}
P_0(z)&=5z^4-z^5,&
P_1(z)&=-32z^3+5z^4-z^5,\\
Q_0(z)&=-1-z,&
Q_1(z)&=5+5z+5z^2.
\end{aligned}
\tag{7.1}
$$
任何允许的归一、重参数化后，第一块两个物理坐标 $U_0,U_1$ 的消失阶仍分别为四、三；第二块坐标必形如
$$
W_0=\gamma Q_0,\qquad
W_1=\alpha Q_1+\beta Q_0,\qquad \alpha\gamma\ne0.
$$
由于准确恒等式 $Q_1+5Q_0=5z^2$，
$$
\frac{W_1}{W_0}
=\frac\beta\gamma-\frac{5\alpha}{\gamma}
-\frac{5\alpha}{\gamma}\frac{z^2}{1+z}.
\tag{7.2}
$$
该比值与其 $z=0$ 值之差，消失阶准确为二。

把完整 $T_3$ 写成不含第一块坐标的二元三次式 $C_R(W_0,W_1)$，加上至少含一个 $U_0$ 或 $U_1$ 的项。后一组项消失阶至少三。前一组在 $z=0$ 为零，但其对应的单变量根是简单根：其原常数项正是 (4.1)，在 $r=2d-A$ 下为
$$
r^3-3Ar-2A.
$$
若此式与导数同时为零，则 $r^2=A$，进而 $A(r+1)=0$，只可能 $A=0$ 或 $A=1$，即 $\mu=0$ 或 $\mu=1/2$，都已排除。因此该二元三次式在当前比值处的导数非零。

现在 $W_0(0)\ne0$，由 (7.2) 得
$$
\operatorname{ord}_{z=0} C_R(W_0(z),W_1(z))=2.
$$
所有含第一块坐标的项的阶至少为三，无法抵消这个非零二阶项。这违反完整最高梯度恒等式 $T_3(Kv(z))\equiv0$。故 $\Delta=0$ 的最后支点对也排除。$\square$

## 8. 已完成的范围

本文覆盖 $c=0$、$\mu=1/2$、$\mu=0,1$、普通权值的 $\Delta\ne0$ 与 $\Delta=0$，以及所有有限或无穷远支点。因此没有遗漏两个双点类型中的权退化或坐标边界。

满秩外 mean、非 secant、$T_3$ 本质三维的非约化支撑现在仅剩 $2+1+1$。原全临界簇、其他本质维数、全局自然幂成员关系和实际算子逆尚未全部解决，普通复 Hilbert 空间 ISP 仍未达到完成标准。

执行环境失联期间，本文通过代码模式中的精确整数运算完成并使用仓库小文本后备保存。API 同步不记作真实 git pull，恢复终端后仍须实际同步。
