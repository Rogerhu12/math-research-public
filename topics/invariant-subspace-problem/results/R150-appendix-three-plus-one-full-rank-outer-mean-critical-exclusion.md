# R150 附录：完整低梯度排除满秩外均值的三重加单点支撑

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 在 mean 的 $4\times3$ Hankel 矩阵秩三、非零 $T_3$ 本质空间 $W$ 三维、$y\notin W$ 且 $H$ 秩四的原完整立方临界截面中，共同长度四支撑**不可能为 $3s+t$，其中 $s\ne t$，允许任一点为无穷远**。证明先使用原三次曲线的半权条件，再代入原完整 $y$ 梯度、最高梯度及两个 $H$ jet 梯度，迫三重支点的整个三维 jet 空间全等向；原六模式核不存在这样的三重 jet 空间，故矛盾。

这是完整梯度的原支撑排除。剩余满秩重支撑仍有 $2+2$、$2+1+1$；$H$ 降秩、secant mean 及本质维数四至六未由本文处理。

## 1. 只用原收缩关系作可逆归一

沿用[四 jets 归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)与[非约化中心三次分类](R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)。若支撑为 $3s+t$，按原 $\lambda$ 归一后有
$$
\mathcal A=\mathbb C[\varepsilon]/(\varepsilon^3)\oplus\mathbb C,\qquad
\tau(1)=1,\qquad
y(r)=\tau(X),\quad H(r,r)=\tfrac14\tau(X^2),\quad V(r,r,r)=\tfrac18\tau(X^3).
\tag{1.1}
$$
$H$ 满秩使 $\tau(\varepsilon^2)\ne0$，且单点权非零。前稿已经由原最高梯度及有理物理像证明，单点权必须为 $1/2$；三重块总权亦为 $1/2$。

设原归一后的 $\tau(\varepsilon)=\alpha$、$\tau(\varepsilon^2)=\beta\ne0$。选择
$$
a^2\beta=1,\qquad b=-a\alpha/\beta,\qquad
\phi(\varepsilon)=a\varepsilon+b\varepsilon^2.
$$
这是局部代数自同构。以 $\tau\circ\phi$ 为新泛函、以逆参数变换改变 jet 基，(1.1) 的所有张量保持不变，而新泛函满足
$$
\boxed{\tau(1_{3s})=\tfrac12,\quad\tau(\varepsilon)=0,\quad
\tau(\varepsilon^2)=1,\quad\tau(1_t)=\tfrac12.}
\tag{1.2}
$$
所有权都是复数；选择非零平方根与可逆参数不使用正性。

记新基为 $u_0,u_1,u_2,w$，前三个是同一三重支点的可逆归一、重参数化 jets，$w$ 是单点曲线向量的非零倍数。原曲线满足 $\nu(z)^{\mathsf T}K\nu(z)=0$，故低三阶对角系数仍满足
$$
u_0Ku_0=u_0Ku_1=0,\qquad 2u_0Ku_2+u_1Ku_1=0,\qquad wKw=0.
$$
因此原 $K$ 在此基的限制必为
$$
\boxed{
\overline K=
\begin{pmatrix}
0&0&c&f\\
0&-2c&d&g\\
c&d&e&h\\
f&g&h&0
\end{pmatrix}.}
\tag{1.3}
$$
没有假定 $\overline K$ 可逆。矩向量和二阶矩的准确坐标为
$$
2y=(1,0,2,1)^{\mathsf T},\qquad
8H=
\begin{pmatrix}
1&0&2&0\\
0&2&0&0\\
2&0&0&0\\
0&0&0&1
\end{pmatrix}.
\tag{1.4}
$$
当 $i,j,k<3$ 时，三阶张量满足 $8V_{ijk}=\tau(\varepsilon^{i+j+k})$；混合两个支撑块的条目为零，而 $V_{333}=1/16$。这些确定后续计算中的所有常数。

## 2. 使用的完整原梯度

置 $p=\overline Ky$、$F=y^{\mathsf T}\overline Ky/2$、$b=p^{\mathsf T}Hp$、
$\tau_2=\operatorname{tr}(\overline KH)^2$，并记
$$
T_2=yy^{\mathsf T}-2H,\qquad
T_3=y^{\otimes3}-2\operatorname{Sym}_{3}(y\otimes H)+4V.
$$
这里 $\operatorname{Sym}_{3}$ 是三个位置之和；作为多项式，
$T_3(r)=(yr)^3-6(yr)H(r,r)+4V(r,r,r)$。

[完整低梯度稿](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)中的 $y$ 梯度除去原可逆 $3K$ 后为
$$
\begin{aligned}
G={}&(F^2-2b+2\tau_2)y-4FHp+8H\overline KHp\\
 &+4V(p,p)-8V:\overline KH\overline K.
\end{aligned}
\tag{2.1}
$$
完整临界点必有 $G=0$。全部张量支撑在 $E$ 中，所以原六维向量条件在基 $u_0,u_1,u_2,w$ 上准确给这四个坐标条件。

$H$ 梯度对应原物理二次关系
$$
N=(T_3)_p-FT_2+4H\overline KH,\qquad
\nu(z)^{\mathsf T}KNK\nu(z)\equiv0.
\tag{2.2}
$$
沿三重支点的归一局部曲线，前三级系数可用
$\rho(z)=(1,z,z^2,0)^{\mathsf T}$ 计算；高于二阶的原曲线项不影响这里的系数。因此 (2.2) 特别给
$$
(\overline KN\overline K)_{00}=0,\qquad
2(\overline KN\overline K)_{02}+(\overline KN\overline K)_{11}=0.
\tag{2.3}
$$
最高梯度同理给
$$
[z^0]\,T_3(\overline K\rho(z))=0,\qquad
[z^1]\,T_3(\overline K\rho(z))=0.
\tag{2.4}
$$

## 3. 八个精确多项式条件

直接将 (1.3)–(1.4) 及原 $V$ 代入 (2.1)，四个 $G$ 坐标依次是 $16E_0,-32E_1,32E_2,16E_3$ 的 $1/128$ 倍，其中
$$
\begin{aligned}
E_0={}&-4eh+2ef-3e^2+4dg+6d^2+2cf+6ce-3c^2,\\
E_1={}&(e+c)g+2d(h-f+e),\\
E_2={}&2eh-2ef+e^2-2dg-2d^2-2ch-4ce+3c^2,\\
E_3={}&(e-c)^2-2d^2.
\end{aligned}
\tag{3.1}
$$
从 (2.4) 去掉非零数值常数，得到
$$
\boxed{c^2(3f+2c)=0,\qquad
c(2df+cg+2cd)=0.}
\tag{3.2}
$$
从 (2.3) 的第一个条件得到
$$
\boxed{c(2ef+2ch-cf+2ce-2c^2)=0.}
\tag{3.3}
$$
第二个条件在 $c=0$ 时准确为
$$
\boxed{2e^2f+2deg+2d^2h-3d^2f+2d^2e=0.}
\tag{3.4}
$$
(3.4) 只在下一节的 $c=0$ 分支使用。

[整数多项式重构器](../notes/2026-11-13-three-plus-one-critical-exclusion-verify.js)从 (1.3)、$\tau$ 的全部张量条目和 (2.1)–(2.4) 重建完整四个 $G$、四个 $H$ jet 条件及四个最高 jet 条件，逐项核验上述系数，并核验下面两分支消元所用的恒等式。[完整输出](../notes/2026-11-13-three-plus-one-critical-exclusion-certificate.json)保留全部系数。程序对每次整数运算检查安全整数范围，实际执行结果为 all_pass: true；它还从原六阶 $K$ 重算 §5 的接触多项式。以下给出全复数域的消元证明。

## 4. 完整消元迫三重 jet 块全等向

### 4.1 若 $c\ne0$，立即矛盾

由 (3.2) 和 (3.3) 顺次得到
$$
f=-\tfrac23c,\qquad
g=-\tfrac23d,\qquad
h=\tfrac13(2c-e).
\tag{4.1}
$$
代入 (3.1)，准确有
$$
E_0=-\tfrac43c(e+2c)-\tfrac53E_3,\qquad
E_1=\tfrac23d(e+3c).
\tag{4.2}
$$
因 $E_0=E_3=0$ 且 $c\ne0$，第一式迫 $e=-2c$。第二式遂迫 $d=0$。但
$$
E_3=(-2c-c)^2-2d^2=9c^2\ne0,
$$
矛盾。因此必有 $c=0$。

### 4.2 若 $c=0$，必有 $d=e=0$

$E_3=0$ 给 $e^2=2d^2$，而精确恒等式
$$
E_0+2E_2+E_3=-2ef
\tag{4.3}
$$
给 $ef=0$。若 $d\ne0$，则 $e\ne0$，从而 $f=0$。$E_2=0$ 再给 $dg=eh$，而 $E_1=0$ 给
$$
eg+2d(h+e)=0.
$$
使用 $e^2=2d^2$，得到
$$
h=-\tfrac12e,\qquad g=-d.
\tag{4.4}
$$
将 (4.4)、$f=0$ 代入 (3.4)，左边变成 $-d^2e\ne0$，再次矛盾。因此 $d=0$，随后 $e^2=2d^2$ 迫 $e=0$。

两分支合起来给出
$$
\boxed{c=d=e=0.}
\tag{4.5}
$$
由 (1.3)，这准确意味着
$$
K|_{\operatorname{span}(u_0,u_1,u_2)}=0.
\tag{4.6}
$$
这是整个三重 jet 空间全等向的条件。

## 5. 原六模式核不存在全等向的三重 jet 空间

可逆归一与参数变换不改变该三维支撑空间，所以可回到原物理曲线 $v(s)=(1,s,\ldots,s^5)$，使用
$$
u_0=v(s),\qquad u_1=v'(s),\qquad u_2=\tfrac12v''(s).
$$
由原固定 $K$ 直接得到
$$
\begin{aligned}
c_{\rm orig}(s)&=u_0^{\mathsf T}Ku_2=s^2(s-2)(s+6),\\
d_{\rm orig}(s)&=u_1^{\mathsf T}Ku_2=-2s(s^2+3s-6),\\
e_{\rm orig}(s)&=u_2^{\mathsf T}Ku_2=54-24s-12s^2.
\end{aligned}
\tag{5.1}
$$
若有限三重 jet 空间全等向，第一式迫 $s=0,2,-6$。但
$$
e_{\rm orig}(0)=54,\qquad d_{\rm orig}(2)=-16,\qquad
d_{\rm orig}(-6)=144
$$
各自非零。无穷远使用齐次坐标
$v_{\rm hom}(a,1)=(a^5,a^4,a^3,a^2,a,1)$，前三个 jets 为 $e_5,e_4,e_3$，而 $e_3^{\mathsf T}Ke_3=-8\ne0$。全部有限和无穷远支点均已覆盖，与 (4.6) 矛盾。$\square$

## 6. 剩余任务与边界

本条删除了原满秩外 mean、本质三维、非 secant 截面的全部 $3+1$ 支撑。配合[四重支点排除](R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md)，非约化支撑现在只剩 $2+2$ 与 $2+1+1$，且必须满足[中心三次分类](R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)中的节点或二次像条件。四个不同支点的无基点五次投影仍须处理。

本条不声称全临界簇只剩 $W_\pm$。$H$ 降秩、secant mean、本质维数四至六以及全局自然幂的 Jacobian 成员关系尚未全部闭合；实际 Bell 算子逆和普通复 Hilbert 空间 ISP 的完成标准尚未达到。

终端中断说明：本证明及证书在执行环境失联期间由代码模式中的精确整数运算完成，通过仓库小文本后备写入。API 写入与规则读取不记作真实 git pull；恢复终端后仍须实际同步。
