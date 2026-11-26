# R150 附录：单位 2+1+1 的相等非零基点配对与零总单点权重支路为空

作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条范围已证明。** 在原 essential-four 外均值、rank $H=4$、单位 $2+1+1$ 加孤立零点分支中，若两条基点配对相等且非零，而两个单位单点的 Frobenius 权重之和为零，则不存在原临界点。证明保留原物理有理正规曲线和完整最高式的二阶 germ；只满足 Gram 抽象相容式的点不足以通过该条件。其余非零配对支路、原全局 Bell 来源及普通 Hilbert ISP 均未由本条关闭。

## 1. 原代数与本条覆盖

沿用[外均值长度五原代数](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)及[一条零基配对附录](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)的原记号。除子为
$$
D=2A+B+C+Z,
$$
其中四个支撑点两两不同，活跃代数与同一 Frobenius 泛函为
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\qquad \tau(z)=a z_0+z_1+bz_B+cz_C,
\qquad a+b+c=1,\quad bc\ne0.
$$
本条假设 $p=q\ne0$、$b+c=0$。共同齐次规范给 $p=q=1$，于是 $a=1,c=-b,b\ne0$，原活跃 Gram 为
$$
K_B=\begin{pmatrix}
0&0&1&1\\
0&A_1&r&s\\
1&r&0&t\\
1&s&t&0
\end{pmatrix}.
\tag{1.1}
$$
记零点配对列为 $U=(u_0,u_1,u_B,u_C)^T$，$m=\tau(U)$。所有变量仍来自同一个原五点 jet Gram；没有独立选择抽象 Gram 后丢掉物理曲线。

在 $\mathcal B$ 中，$z w=(z_0w_0,z_0w_1+z_1w_0,z_Bw_B,z_Cw_C)$，$1=(1,0,1,1)$。写 $k_i$ 为 (1.1) 的行，令
$$
(D_Kz)_i=\tau(k_i z),\quad d=D_K1,\quad f=\tfrac12\tau(d),
$$
$$
e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2),
\qquad E=e-2D_Kd-2d^2+4fd=0.
\tag{1.2}
$$
原最高梯度在物理曲线上为 $P+R^3=0$，其中
$$
P(z)=\tfrac12\tau\bigl((z-\tau(z)1)^3\bigr),
\qquad P_0=-u_0^3,\quad P_1=-3u_0^2u_1.
\tag{1.3}
$$
下文使用 (1.2) 与完整曲线恒等式 (1.3) 的必要条件即可排除本支，不要求仅由有限相容式推出充分性。

## 2. 原 mean 与首阶最高式迫使特殊 Gram

设 $x=d_B,y=d_C$。可逆换元为
$$
r=x-1+bt,\quad s=y-1-bt,\quad
A_1=2f-2b(x-y)-2b^2t.
\tag{2.1}
$$
直接按原乘法展开，得到
$$
E_0=-2b(x-y).
$$
因 $b\ne0$，故 $x=y$。原基点行 $k_0=(0,0,1,1)$ 满足 $P_0=0$，于是 $u_0=0$。在 $x=y$ 后，完整首阶最高式给
$$
P_1=3b^2t=-3u_0^2u_1=0,
$$
所以 $t=0$。此时原 $E_1$ 精确为 $8f^2$，故 $f=0$。代回 (2.1)，
$$
\boxed{A_1=0,\qquad r=s=x-1,\qquad t=0,\qquad u_0=0.}
\tag{2.2}
$$
特别地，$k_1=rk_0$。余下 mean 还给 $-2x^2+2x-1=0$，但本条不必再除以或求解该式；下一节的物理条件已经矛盾。

## 3. 双点的四个物理位置与不能省略的二阶 germ

原非退化六维形式和曲线为
$$
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix},\qquad
v(z)=(1,z,z^2,z^3,z^4,z^5)^T,
\quad v(\infty)=e_5.
\tag{3.1}
$$
有 $\det K=-25600$、$v(z)^TKv(z)=0$。有限双点 $A=\alpha$ 的规范 jets 为 $\lambda v(\alpha)$、$\mu v'(\alpha)+\nu v(\alpha)$，其中 $\lambda\mu\ne0$。由于 $v^TKv=v^TKv'=0$，条件 $A_1=0$ 等价于
$$
0=v'(\alpha)^TKv'(\alpha)=-2\alpha^2(\alpha-2)(\alpha+6).
$$
无穷远局部曲线为 $(\epsilon^5,\epsilon^4,\epsilon^3,\epsilon^2,\epsilon,1)$，其一阶 jet 的自配对亦为零。故
$$
A\in\{0,2,-6,\infty\}.
\tag{3.2}
$$

现在使用完整最高式的二阶 germ。任意允许的物理局部坐标及单位规范下，活跃极线列具有
$$
k(\epsilon)=k_0+\epsilon k_1+\epsilon^2Z+O(\epsilon^3)
=(1+r\epsilon)k_0+\epsilon^2Z+O(\epsilon^3).
$$
此处 $Z$ 是二阶列系数，不是孤立零点的名称。因为 $\tau(k_0)=\tau(k_0^2)=0$、$k_0^2=k_0$，精确微分给
$$
DP(k_0)[Z]=\tfrac32\tau(k_0^2 Z)
=\tfrac{3b}{2}(Z_B-Z_C).
\tag{3.3}
$$
又 $P(k_0)=0$，因此平行一阶项不会产生二阶贡献。零点极线有 $R(0)=u_0=0$，从而 $R(\epsilon)^3$ 的二阶系数为零。由原最高恒等式及 $b\ne0$，
$$
\boxed{Z_B=Z_C.}
\tag{3.4}
$$
结合 $p=q=1$ 与 $r=s$，两个已按基点配对归一的单点极线在 $A$ 的零、一、二阶 jets 全部相等。允许的局部单位和坐标变换保留极线差至少三阶消失，因此可以在 (3.1) 的规范坐标中检验此条件。

## 4. 全部有限单点的精确有理排除

设物理单点 $B=z,C=w$ 均有限，$z\ne w$，且二者不同于 $A$。令
$$
k(a,z)=v(a)^TKv(z),\qquad
q(z,w)=-\frac{k(z,w)}{(z-w)^2}\in\mathbb Q[z,w].
\tag{4.1}
$$
由于 $t=0$、$z\ne w$，必有 $q(z,w)=0$。

对有限 $A=a$，定义
$$
f_j(z)=\frac1{j!}\partial_a^j k(a,z)\big|_{a=A},\qquad j=0,1,2.
$$
对 $A=\infty$，依次取 $K$ 的第 $5,4,3$ 行与 $v(z)$ 的配对，作为 $f_0,f_1,f_2$。两条非零基点配对保证 $f_0(z)f_0(w)\ne0$。前节必要条件为
$$
f_j(z)f_0(w)-f_j(w)f_0(z)=0,\qquad j=1,2.
$$
每个左端均被 $z-w$ 整除，记商为 $L_j(z,w)$。于是原点必同时满足 $q=L_1=L_2=0$。取完整有理结式
$$
R_j(z)=\operatorname{Res}_w(q,L_j),\qquad j=1,2.
\tag{4.2}
$$
任何有限共同根都使两结式为零；此必要性不需要除掉首项，也包含所有降次纤维。

附带自足源码从 (3.1) 和原 (1.2)–(1.3) 直接构造，得到以下准确结果。gcd 均取 $\mathbb Q[z]$ 的首一形式。

| $A$ | $(\deg R_1,\deg R_2)$ | $\gcd(R_1,R_2)$ | $f_0(z)$ |
|---|---|---|---|
| $0$ | $(22,24)$ | $z^{13}(z-5)^3$ | $-z^4(z-5)$ |
| $2$ | $(24,24)$ | $(z-2)^8(3z^2-17z+6)^2/9$ | $-(z-2)^3(3z^2-17z+6)$ |
| $-6$ | $(24,24)$ | $(z+6)^8(5z^2+65z+66)^2/25$ | $(z+6)^3(5z^2+65z+66)$ |
| $\infty$ | $(5,9)$ | $z+1$ | $-(z+1)$ |

每一行的 gcd 的所有复根都是原 $f_0$ 的零点；源码以准确 square-free 因子整除回乘检查这一点。因此任何候选 $z$ 都使原基点配对为零，与 $p=1$ 矛盾。全部有限 $B,C$ 已排除。

## 5. 单点在无穷远的全部边界

若 $A=\infty$，两个不同单点都必须有限，已由上一节覆盖。否则 $A\in\{0,2,-6\}$。由交换 $B,C$ 的对称性，只须设 $B=\infty$。条件 $t=0$ 给
$$
0=e_5^TKv(C)=-(1+C),\qquad C=-1.
$$
取 $f_j(\infty)$ 为上述二元五次极线在无穷远的值，即有限多项式的 $z^5$ 系数。第一阶归一条件的交叉乘积为
$$
f_1(-1)f_0(\infty)-f_1(\infty)f_0(-1)
=-(A+1)^2(15A^2+62A+32).
$$
在 $A=0,2,-6$ 分别等于
$$
-32,\qquad -1944,\qquad -5000.
$$
均非零，而三个位置的 $f_0(\infty)f_0(-1)$ 都非零。于是连一阶必要条件都不成立。两单点同时为无穷远违反不同支撑点假设。所有射影情形均已穷尽，定理得证。

## 6. 精确源与实际执行身份

- 自足源码：[2026-11-26-unit-two-plus-one-plus-one-equal-zero-weight-347c.py](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-zero-weight-347c.py)。SHA-256：`1a63e7f16608385a425387f77319b23c199451c2b7c7a3eccf38b7f76a10c9ec`。
- 实际执行：CPython 3.12.14、SymPy 1.14.0；无 `PYTHONPATH` 覆盖；exit $0$，源码计时 $0.506024$ 秒，峰值 RSS $51064$ KiB。仅构造原多项式和完整 QQ 结式，没有有限域存在性提升。
- [紧凑执行回执](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-zero-weight-execution-347c.json)保留原 mean/最高首阶、物理二阶 germ、四个完整 gcd、全部无穷远门和原输出身份；未保存可重算结式数组。

本条只关闭 $p=q\ne0,b+c=0$；$p=q\ne0,b+c\ne0$ 及其它非零配对继续开放。
