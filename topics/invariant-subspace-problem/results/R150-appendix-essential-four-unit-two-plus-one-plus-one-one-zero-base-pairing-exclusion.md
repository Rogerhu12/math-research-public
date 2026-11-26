# R150 附录：单位 2+1+1 与孤立零点的一条基点配对为零支路为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条范围已证明。** 本条保留同一原 Frobenius 代数、原 mean、原最高梯度与原第二梯度，以及同一原物理曲线和 jets。结合[两条基点配对同时为零的附录](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-pairings-exclusion.md)，单位 $2+1+1$ 的剩余支路必须满足两条基点配对都非零。本结论不是整个 essential-four 分支、Bell 全局根式成员性或 Hilbert 不变子空间问题的结论。

## 1. 原对象与无除法的必要相容式

沿用[essential-four 外均值长度五代数](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)的全部假设。原长度五除子为
$$
D=2A+B+C+Z,
$$
四个支撑点两两不同，$L$ 在活跃的 $2A+B+C$ 上为单位，在约化点 $Z$ 上为零。以同一 $L$ 归一活跃坐标并归一双点最高 Frobenius 系数，得
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad \tau(x)=a x_0+x_1+b x_2+c x_3,
\quad a=1-b-c,\quad bc\ne0.
$$
允许 $a=0$。原活跃 Gram 及零点配对为
$$
K_B=\begin{pmatrix}
0&0&p&q\\0&A_1&r&s\\p&r&0&t\\q&s&t&0
\end{pmatrix},\qquad
U=(u_0,u_1,u_B,u_C)^T,\qquad m=\tau(U).
$$
这里矩阵条目 $A_1$ 不代表物理点 $A$。本条先处理 $p\ne 0,q=0$，由全部原方程的共同齐次性令 $p=1$；交换两个单位单点同时覆盖 $p=0,q\ne 0$。完整五维 Gram 为
$$
\widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix},\qquad
\operatorname{rank}\widehat K\ge4.                 \tag{1.1}
$$
原长度五 jets 独立，其五维张成空间在原六维非退化形式下的根空间维数至多一，故得此秩下界。

乘法为
$$
x y=(x_0y_0,x_0y_1+x_1y_0,x_2y_2,x_3y_3),\quad 1=(1,0,1,1).
$$
写 $k_i$ 为 $K_B$ 的行，定义
$$
(D_Kx)_i=\tau(k_i x),\quad d=D_K1,\quad f=\tfrac12\tau(d),
$$
$$
E=e-2D_Kd-2d^2+4fd=0,
\quad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2).  \tag{1.2}
$$
原最高式与原第二梯度分别为 $P+R³$、$N+mR²$，其中
$$
P(x)=\tfrac12\tau((x-\tau(x)1)^3),
$$
$$
N(x)=\tfrac12\tau((d-f1)x^2)-\tau(x)\tau(dx)
       +f\tau(x)^2+\tfrac14\tau(xD_Kx).                  \tag{1.3}
$$
设 $P_0,P_1,P_B,P_C$ 为 $P$ 在双点的值、一阶 jet、两个单点的值；$N_0,N_1,N_B,N_C$ 同义。原物理最高式、第二梯度的值和 jet 给
$$
P_0=-u_0^3,\ P_1=-3u_0^2u_1,\ P_B=-u_B^3,\ P_C=-u_C^3,
$$
$$
N_0=-mu_0^2,\ N_1=-2mu_0u_1,\ N_B=-mu_B^2,\ N_C=-mu_C^2. \tag{1.4}
$$
因此下列多项式都必须为零，不要求任何 $P_i,N_i,u_i,m$ 非零：
$$
c_0=3P_0N_1-2N_0P_1,
$$
$$
\mu=3N_0N_BN_C-(3aP_0+P_1)N_BN_C
                  -3bP_BN_0N_C-3cP_CN_0N_B,           \tag{1.5}
$$
$$
\chi_{ij}=N_i^3P_j^2-N_j^3P_i^2,\qquad i,j\in\{0,B,C\}.
$$
例如 $\mu $ 直接代入等于
$$
-3m^2u_0^2u_B^2u_C^2(m-a u_0-u_1-bu_B-cu_C)=0.
$$
后文只将这些式子用作必要条件；不由范数相容性断言物理临界点存在。

## 2. 原物理约化点不能成为完整 Gram 的零行

需要一个保留原物理曲线的简单事实。若 $S$ 是长度五除子 $D$ 的约化支撑点，而其在完整 Gram 中的行全部为零，则原五次极线
$$
\ell_S(z)=v(S)^TKv(z)
$$
在 $D$ 上全为零。另一方面，原恒等式 $v(z)^TKv(z)=0$ 的一阶导数使 $\ell _S$ 在 $S$ 至少二重零。由于 $S$ 在 $D$ 中只有一次，$\ell _S$ 至少有 $D+S$ 这六重零；齐次二元五次式只能恒等于零。原曲线张成六维空间且原 $K$ 非退化，矛盾。

这个论证对无穷远点也成立：所有次数与重数都在射影直线上理解。允许的单位归一和局部 jet 可逆变换不改变原除子上的消失阶。特别地，若活跃单点 $C$ 的 $K_B$ 行为零，则 $P_C=0$ 迫 $u_C=0$，从而完整 Gram 的这一行也为零，已经矛盾。

## 3. 不先除以边界因子的完整 mean 坐标

记
$$
x=d_B=a+r+ct,\qquad y=d_C=s+bt.
$$
解出
$$
r=x-a-ct,\quad s=y-bt,\quad A_1=2f-2bx-2cy+2bct.
$$
由于 $b\ne 0$，原 $E_0=0$ 给
$$
f=\tfrac12x+\tfrac12b-\tfrac14.
$$
设置
$$
\delta=1-2b,\quad h=t-1,\quad z=2(y-b)-h,\quad v=x-b.
$$
这仅为可逆仿射换元。余下 mean 恰为
$$
E_B=-chz-\delta v,                                      \tag{3.1}
$$
$$
2E_C=-\delta h^2+2\delta hv-\delta h+\delta z
                        -2hz+2vz-z^2-2z,               \tag{3.2}
$$
$$
\begin{aligned}
-2E_1={}&c\delta h^2+2c\delta hv+c\delta hz-c\delta h+c\delta z
 +chz+2cvz+cz^2-2cz\\
 &+\delta^2v-\delta^2-4\delta v^2+3\delta v.             \tag{3.3}
\end{aligned}
$$
下节先处理全部后续分母可能为零的情形。

## 4. 所有边界

### 4.1 $\delta =0$

由 (3.1)，$hz=0$。若 $z\ne 0$，则 $h=0$；(3.2) 给 $2v=z+2$，(3.3) 给 $2v+z=2$，相减迫 $z=0$，矛盾。因此 $z=0$，原 Gram 恰为
$$
b=\tfrac12,\quad A_1=s=0,\qquad
K_B=\begin{pmatrix}0&0&1&0\\0&0&r&0\\1&r&0&t\\0&0&t&0\end{pmatrix}. \tag{4.1}
$$
原 $P_0=P_C=0$ 给 $u_0=u_C=0$。还必须使用完整原物理 germ，而不能让相容式中消掉的 $u_1$ 成为自由变量。

在双点基极坐标 $e_B=(0,0,1,0)$，$\tau (e_B)=1/2$，且
$$
(e_B-\tfrac121)^2=\tfrac141.
$$
所以 $P(e_B)=0$ 且 $DP(e_B)=0$。原物理极坐标 germ 为
$$
k(\epsilon)=e_B+\epsilon r e_B+O(\epsilon^2).
$$
由三次齐次性及上述奇点条件，$P(k(\epsilon ))=O(\epsilon ⁴)$。零点极坐标为 $R(\epsilon )=u_1\epsilon +O(\epsilon ²)$，完整最高恒等式 $P(k(\epsilon ))+R(\epsilon )³=0$ 的三阶项因此迫 $u_1=0$。

于是 $U=(0,0,u_B,0)=u_BK_Be_0$ 且 $e_0^TK_Be_0=0$。完整 Gram 合同于 $K_B⊕0$，秩为二，违反 (1.1)。这排除了整个半权支，不曾除以 $r,t,a$。

以下 $\delta \ne 0$，并且 $b\ne 0$ 给 $\delta \ne 1$。

### 4.2 $t=0$

在原 $x,y$ 坐标下，两个单点 mean 是
$$
E_B=-\delta(x-b)+c(\delta+2y),\qquad
E_C=y(2x-2y-1).                                        \tag{4.2}
$$
若 $y=0$，前式给 $x=b+c$，从而 $s=t=0$；单点 $C$ 的活跃 Gram 行为零，由第 2 节直接排除。

若 $y\ne 0$，则 $x=y+1/2$，前式为
$$
(2y+\delta)(c-\delta/2)=0.
$$
当 $c=\delta /2$ 时，$A_1=0,r=s=y$，原相容式精确为
$$
c_0=-\frac{3}{32}\delta^2y^2(\delta-1)^2\ne0,
$$
矛盾。当 $c\ne \delta /2$ 时，必须 $y=-\delta /2,x=b$；原 $E_1=-\delta (2c-\delta )/2$ 非零，也矛盾。

### 4.3 $h=0$

由 (3.1) 得 $v=0$；(3.2) 给 $z(z+2-\delta )=0$。$z=0$ 时 (3.3) 给 $E_1=\delta ²/2\ne 0$。因此
$$
z=\delta-2,\quad \delta\ne2,\qquad
c=\frac{\delta^2}{2(\delta-2)^2}.
$$
原参数为
$$
b=\frac{1-\delta}{2},\quad r=-\delta,\quad s=\frac{\delta-2}{2},
\quad t=1,\quad A_1=\frac{\delta^2(1-\delta)}{2(\delta-2)}.
$$
直接由 (1.3)–(1.5) 得
$$
c_0=-\frac{3\delta^3(\delta-1)^2(3\delta^2-4\delta-2)}{128(\delta-2)},
$$
$$
\chi_{0B}=\frac{\delta^5(\delta-1)^2(3\delta+1)^2
 (19\delta^3+33\delta^2+11\delta+1)}{131072}.
$$
这两个分子的 $\mathbb Q[\delta ]$ 首一最大公因子恰为 $\delta ³(\delta −1)²$，全是已排除值，所以本支为空。

### 4.4 其余分母

现在 $\delta  h t\ne 0$。若 $z=0$，则 (3.1) 给 $v=0$，(3.2) 给 $\delta h(h+1)=0$，即已排除的 $t=0$。故 $z\ne 0$。

置 $D_0=z+\delta h$。若 $D_0=0$，(3.2) 中 $v$ 项消失，留下
$$
2E_C=-\delta(\delta-1)h(h+1),
$$
与 $\delta \ne 0,1$、$h\ne 0$、$t\ne 0$ 矛盾。故 $D_0\ne 0$。现在才合法地解出
$$
v=\frac{\delta(h^2+h-z)+z(2h+z+2)}{2D_0},
\qquad c=-\frac{\delta v}{hz}.                           \tag{4.3}
$$
$c\ne 0$ 又给 $v\ne 0$。

## 5. 完整一般 mean 图恰落在两个面上

把 (4.3) 代入原 (3.3)，精确得到
$$
E_1=\frac{\delta(h+1)F_1F_2}{2hzD_0^2},                 \tag{5.1}
$$
$$
F_1=\delta h^2+2hz+z^2,
$$
$$
F_2=\delta^2h^2+\delta h^2z+2\delta hz-\delta z^2+2hz^2+z^3+2z^2.
$$
所有显示的前因子与分母都已经证明非零，所以 $F_1=0$ 或 $F_2=0$。相交部分同时落入任一后续排除，不需另作假设。

### 5.1 第一面 $F_1=0$

令 $k=z/h$。从 (4.3) 直接得到
$$
\delta=-k(k+2),\quad v=-k/2,\quad
b=(k+1)^2/2,\quad c=-\frac{k(k+2)}{2h^2},
$$
$$
r=\frac{k((2k+3)h+k+2)}{2h},\quad
s=-\frac{hk(k+1)}2,\quad t=h+1,
\quad A_1=-\frac{k^2(k+1)(k+2)(h+1)}{2h}.                \tag{5.2}
$$
先验 $hk(k+1)(k+2)\ne 0$。原相容式为
$$
c_0=\frac{3k^4(k+1)^5(k+2)^2}{128h}
       \bigl((k^2-3)h+k^2+k-2\bigr).                   \tag{5.3}
$$
若 $k²=3$，括号中余项为 $k+1\ne 0$，不可能；因此
$$
h=\frac{(k+2)(k-1)}{3-k^2}.                            \tag{5.4}
$$
将 (5.2)、(5.4) 代入**同一原** $\mu ,\chi _{0B},\chi _{0C},\chi _{BC}$，分别在 $\mathbb Q(k)$ 中约去有理分式自身的公因子后取分子。四个分子的首一最大公因子精确为
$$
\boxed{k^3(k+1)^7(k+2)^2.}                              \tag{5.5}
$$
配套源码从 (1.2)、(1.3) 重新构造全部值和 jet，并执行精确有理欧几里得算法验证此等式。因为 (5.5) 仅含已证明非零因子，没有共同根。第一面全部排除。

### 5.2 第二面 $F_2=0$ 的完整参数

令 $w=\delta h/z$。此时 $w\ne 0$，且 $D_0=z(w+1)$ 给 $w\ne −1$。写
$$
W=h(w+2)+w^2+2w+2.
$$
方程 $F_2=0$ 正好是
$$
(w-h)z=hW.                                             \tag{5.6}
$$
若 $w=h$，右端成为 $2h(h+1)²$，与 $ht\ne 0$ 矛盾。因此 $w−h\ne 0$，而 (5.6) 与 $hz\ne 0$ 给 $W\ne 0$。全部原参数为
$$
b=-\frac{(h+w)(w+1)^2}{2(w-h)},\qquad c=\frac{w^2}{2h^2},
$$
$$
A_1=-\frac{w^2(h+1)(h+w)(w+1)W}{2h(w-h)^2},
$$
$$
r=-\frac{w(2h^2w+3h^2+2hw^2+4hw+4h+w^2)}{2h(w-h)},
$$
$$
s=\frac{h(w+1)W}{2(w-h)},\qquad t=h+1.                 \tag{5.7}
$$
$b\ne 0$ 还给 $h+w\ne 0$。因此
$$
hw(w+1)(h+w)(w-h)W\ne0.                                \tag{5.8}
$$
原相容式是
$$
c_0=\frac{3w^3(h+w)^2(w+1)^5W^3}{128h(w-h)^6}C(h,w),
$$
$$
C(h,w)=(w^2-4w+1)h^2+(w^3-w^2-6w)h+w^3-w^2.           \tag{5.9}
$$
所以 $C=0$，没有删除任何可能为零的前因子。

### 5.3 第二面的精确消元与全部例外纤维

令 $M,X_B,X_C$ 分别为将 (5.7) 代入原 $\mu ,\chi _{0B},\chi _{0C}$ 后，在 $\mathbb Q(h,w)$ 中化简所得分子。其 $(h,w)$ 次数分别为 $(12,26),(15,39),(18,39)$。不需要打印大系数数组：这些多项式已由 (1.3)–(1.5)、(5.7) 唯一、完整地定义，配套源直接生成。

在 $\mathbb Q[w]$ 中计算
$$
R_M=\operatorname{Res}_h(C,M),\quad
R_B=\operatorname{Res}_h(C,X_B),\quad
R_C=\operatorname{Res}_h(C,X_C).
$$
它们的次数分别为 $69,96,105$。精确首一最大公因子为
$$
\boxed{w^{18}(w-3)(w-1)^2(w+1)^{20}
          (w^4-w^3-2w^2-6w-2)^2.}                      \tag{5.10}
$$
这是特征零有理运算，不是模素数证据。结果式只作为共同有限根的必要条件使用，故首项系数降次产生的额外根仍在下一步原方程纤维中检查。

$w=0,−1$ 已由 (5.8) 排除。对于 $w=1$ 和 $w=3$，分别把该值代回 $C,M,X_B,X_C$；在 $\mathbb Q[h]$ 中的共同首一因子均恰为 $h+3$。

- $w=1,h=−3$：原 $P_0=0$、$P_1=−1/4$。前者由 (1.4) 强制 $u_0=0$，后者应为 $−3u_0²u_1=0$，矛盾。
- $w=3,h=−3$：原 $b=0$，违反 Frobenius 单点权非零。

最后令
$$
G(w)=w^4-w^3-2w^2-6w-2.
$$
对由 $G,C,M,X_B,X_C$ 生成的 $\mathbb Q[h,w]$ 理想，按 $h>w$ 字典序做精确有理消元，所得约化 Gröbner 基恰为
$$
\left\{\ h+\frac{-w^3+3w^2+9w+14}{13},\quad G(w)\ \right\}. \tag{5.11}
$$
把 $W=h(w+2)+w²+2w+2$ 对 (5.11) 取余，余数是零。因而这一完整四次纤维必须 $W=0$，违反 (5.8)。源码逐项核对 (5.11) 并验证这个理想约化，未选择某个代数共轭根。

至此 (5.10) 的所有因子和所有分母零例外均被原式或同一原物理几何排除，第二面全部为空。

## 6. 结论与执行记录

$p\ne 0,q=0$ 的全体支路已排除；交换两个单位单点同样排除 $p=0,q\ne 0$。连同已登记的 $p=q=0$，本单位 $2+1+1$、孤立零点、$rank H=4$ 分支若有完整原临界点，则必须 $pq\ne 0$。

配套源为 [2026-11-26-unit-two-plus-one-plus-one-one-zero-347c.py](../notes/2026-11-26-unit-two-plus-one-plus-one-one-zero-347c.py)。它只用 SymPy 1.14.0 的精确有理运算，重建原 Frobenius 乘法、完整 active mean、原最高式和第二梯度，验证全部显示参数化、边界、相容式及两个一般图消元。第 2 节物理次数论证和第 4.1 节完整最高 germ 的三阶项论证由正文证明，并未以自由 Gram 矩阵取代原曲线。

本地命令 `python 2026-11-26-unit-two-plus-one-plus-one-one-zero-347c.py` 完整 exit0，源内9.863867秒、峰值63852 KiB；Python3.12.14、SymPy1.14.0，无额外PYTHONPATH。源码SHA-256为 0ca6f3084ddf37365939534598df77aa8cfa3ba618c6a4fd1d5b7991149a54a4，完整stdout SHA-256为 e67a5241039f645b27dd331953f952dc27f641c81e824c6be7bcb7d002365039；[实际小执行记录](../notes/2026-11-26-unit-two-plus-one-plus-one-one-zero-execution-347c.json)保命令、参数和身份。本条不保存计算数组，不将已排除的几何临界支转换成未给出的全局多项式幂来源。接续问题仍是 $pq\ne 0$ 的一般单位 $2+1+1$ 分支，以及其他尚未关闭的原分支。
