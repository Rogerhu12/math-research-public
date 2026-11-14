# 实际 Euler 原函数的全余类 Stokes 分解

日期：2026-11-12。状态：本文全部解析等价、余类分解、精确半径及
实际非中央单位均已证明。没有由某个非中央 Stokes 常数非零推断
目标中央导数非零。

## 1. 固定原函数与各素数处的规范

在 $E_0:y^2=x^3-x$ 上使用已经认证的同一实际截面

$$
A(z)=\theta(z)^{17}q(x(z)^{-2})=z^4+O(z^8)
       =\sum_{m\ge0}\beta_mz^m,
\qquad 4\mid m\ \text{才可能有 }\beta_m\ne0.
$$

定义不随素数变化的 Euler 原函数

$$
\mathscr H(z)=\int_0^z\frac{A(w)}w\,dw
             =\sum_{m\ge1}\frac{\beta_m}{m}z^m.
\tag{1.1}
$$

以下固定惰性素数 $p\ge7$，令

$$
d=p+1,\quad a=17c,\quad v_p(c)=-1,\quad
\rho=p^{-1/(2p)},\quad
S=p^{-p/(p^2-1)}<\rho.
\tag{1.2}
$$

$c$ 是 R54 的首坏 sigma 系数。采用 $v_p(p)=1$。
[R54](../results/R54-inert-analytic-half-factor-and-central-slope.md)
已经证明正式分解

$$
A=e^{az^d}G,\qquad G\in\mathbb Q_p\langle z/\rho\rangle,
\qquad \|G\|_\rho\le\rho^4.
\tag{1.3}
$$

并且同次数参考 $f_0(z)=\theta((4-i)z)$ 满足

$$
f_0=e^{az^d}G_0,\qquad
G_0,G_0^{-1}\in\mathbb Q_p(i)\langle z/\rho\rangle,
\quad G_0(0)=1.
\tag{1.4}
$$

这里的指数分解首先在正式级数中进行，不要求两个因子分别收敛到
半径 $\rho$。令

$$
\mathscr H=e^{az^d}K,
\quad G=\sum_{j\in\mathcal I}z^j\sum_{h\ge0}g_{j,h}z^{dh},
\quad K=\sum_{j\in\mathcal I}z^j\sum_{h\ge0}k_{j,h}z^{dh},
$$

$$
\mathcal I=\{0,4,8,\ldots,d-4\}.
\tag{1.5}
$$

指数与 $A$ 都只含四的倍数次幂，所以只需这些余类。
记 $P_j$ 为选取次数 $j\bmod d$ 的正式投影；它是固定 $p$ 后的投影，
并非一个独立于 $p$ 的全局算子。

## 2. 明确区分 shifted 变换与对参数求导

对每个 $j\in\mathcal I$，定义

$$
\mathcal J_{p,j}(u)
   =\sum_{h\ge0}a^{-h}g_{j,h}\,(u)_{\underline h},
\qquad
(u)_{\underline h}=u(u-1)\cdots(u-h+1).
\tag{2.1}
$$

下标 $j$ 表示所选 Taylor 余类，不表示对 $u$ 的 $j$ 次导数。
$\mathcal J_{p,0}$ 正是 R54 的实际半因子 $J_{A,p}$。
在非负整数 $k$，(1.3) 的卷积给

$$
\mathcal J_{p,j}(k)=k!a^{-k}[z^{dk+j}]A.
\tag{2.2}
$$

从 (1.3) 得

$$
v_p(a^{-h}g_{j,h})\ge
 \left\lceil\frac{h(p-1)+4-j}{2p}\right\rceil.
\tag{2.3}
$$

因此 (2.1) 在 $u\in\mathbb Z_p$ 一致收敛，且在包含该盘的某个更大
开盘解析。对本文的每个 $0<j<d$，都有 $j\le d-4$；于是 $h\ge1$
的右边至少为 $1$。这也证明随后使用的 Stokes 和式是真正收敛的。

定义中央常数

$$
\mathcal S_0:=-\mathcal J_{p,0}'(0)
 =\sum_{h\ge1}(-1)^h(h-1)!a^{-h}g_{0,h}.
\tag{2.4}
$$

对 $0<j\in\mathcal I$，置 $x_j=j/d\in\mathbb Z_p^\times$，并定义

$$
\mathcal S_j:=\mathcal J_{p,j}(-x_j)
 =\sum_{h\ge0}(-1)^h(x_j)_{\overline h}\,a^{-h}g_{j,h},
$$

$$
(x)_{\overline h}=x(x+1)\cdots(x+h-1).
\tag{2.5}
$$

这里从下降阶乘变为上升阶乘，用的是
$(-x)_{\underline h}=(-1)^h(x)_{\overline h}$；两者不能混同。
由于 $x_j$ 为 $p$ 整，上升阶乘均 $p$ 整，(2.3) 保证收敛。

## 3. Euler 方程逐余类的准确解

由 $z\mathscr H'=A$ 和 (1.3)，有

$$
zK'+ad z^dK=G.
$$

在余类 $j$ 中，它等价于

$$
(h+x_j)k_{j,h}+a k_{j,h-1}=g_{j,h}/d,
\qquad k_{j,-1}=0.
\tag{3.1}
$$

中央余类取 $x_0=0$，另有规范 $k_{0,0}=0$。对 $h\ge1$，递推给

$$
k_{0,h}=\frac{(-a)^h}{d\,h!}
  \sum_{l=1}^h(-1)^l(l-1)!a^{-l}g_{0,l}.
\tag{3.2}
$$

对 $j>0$，包括 $h=0$ 在内，递推给

$$
k_{j,h}=\frac{(-a)^h}{d(x_j)_{\overline{h+1}}}
  \sum_{l=0}^h(-1)^l(x_j)_{\overline l}a^{-l}g_{j,l}.
\tag{3.3}
$$

例如 $h=0$ 时，右边为 $g_{j,0}/(dx_j)=\beta_j/j$，与 (1.1) 相符。
所有分母都非零，因为 $x_j$ 是正有理数。

定义显式模型

$$
E_{p,0}(z)=e^{-az^d},\qquad
E_{p,j}(z)=z^j\sum_{h\ge0}
             \frac{(-a)^hz^{dh}}{(x_j)_{\overline{h+1}}}
                    \quad(j>0).
\tag{3.4}
$$

将 (3.2)、(3.3) 中的有限和补到无穷和，得到完整分解

$$
\boxed{\qquad
K(z)=\frac1d\sum_{j\in\mathcal I}\mathcal S_jE_{p,j}(z)
      +\mathcal R_p(z),
\qquad
\mathcal R_p\in\mathbb Q_p\langle z/\rho\rangle,
\quad\|\mathcal R_p\|_\rho\le\rho^{p+3}.
\qquad}
\tag{3.5}
$$

**余项界的完整证明。** 写 $\mathcal R_p=\sum_jz^j\sum_h r_{j,h}z^{dh}$。
当 $j>0$ 时，

$$
r_{j,h}=-\frac{(-a)^h}{d(x_j)_{\overline{h+1}}}
    \sum_{l>h}(-1)^l(x_j)_{\overline l}a^{-l}g_{j,l}.
\tag{3.6}
$$

对 $l\ge h+1$，商
$ (x_j)_{\overline l}/(x_j)_{\overline{h+1}}$
是整因子的乘积，空乘积为 $1$。由 (1.3)，每项赋值至少为

$$
-h+l+\frac{4-dl-j}{2p}.
$$

它随 $l$ 严格增加；$l=h+1$ 时是

$$
\frac{p+3-dh-j}{2p}.
\tag{3.7}
$$

对中央余类，同一个公式成立，只需将上升阶乘的商替换为
$(l-1)!/h!\in\mathbb Z$；$h=0$ 的余项定义为
$-\mathcal S_0/d$，同一个尾和证明覆盖它。
所以每个加权系数的赋值至少 $(p+3)/(2p)$，给出 Gauss 界。

还须证明闭盘上的系数趋零，不能只给有界性。
由 $G\in\mathbb Q_p\langle z/\rho\rangle$，其加权系数
$v_p(g_{j,l})+(dl+j)/(2p)$ 随 $l\to\infty$ 趋于 $+\infty$。
在 (3.6) 的 $l>h$ 范围，它们的下确界也随 $h\to\infty$ 趋于
$+\infty$；再结合 (3.7) 的同一估计，得到所需的趋零性。
有限个余类求和不会改变结论。$\square$

## 4. 每个模型的精确半径与闭边界行为

$E_{p,0}$ 的收敛半径是 $S$，因为 $v_p(a)=-1$，而 $p$ 进指数的
半径是 $p^{-1/(p-1)}$。这给
$|a z^d|<p^{-1/(p-1)}$，即 $|z|<S$。

对 $j>0$，有

$$
v_p((x_j)_{\overline{h+1}})
   =\sum_{k=0}^h v_p(j+dk)
   =\frac{h+1}{p-1}+O_p(\log(h+2)).
\tag{4.1}
$$

这里分母 $d^{h+1}$ 为单位。对每个 $p^e$，算术级数 $j+dk$
在一个长度 $h+1$ 区间里被 $p^e$ 整除的次数与 $(h+1)/p^e$
相差至多 $1$；只有 $e=O_p(\log(h+2))$ 能贡献。求和即得 (4.1)。
所以由 Cauchy–Hadamard 公式，每个 $E_{p,j}$ 的半径也准确等于 $S$。

更精确地，取 $h=p^n$、$n\ge1$。对 $e\le n$，
$j+dk$ 在 $0\le k\le p^n$ 中的零剩余类不是 $k=0$，因此恰出现
$p^{n-e}$ 次。对 $e=n+1$，唯一可能的正倍数是 $p^{n+1}$；
但它模 $d=p+1$ 为 $(-1)^{n+1}$，而
$j\in\{4,8,\ldots,d-4\}$ 不等于 $1$ 或 $d-1$。
更高的 $p$ 次幂大于区间中全部正整数。因此

$$
v_p((x_j)_{\overline{p^n+1}})
  =\frac{p^n-1}{p-1}=v_p((p^n)!).
\tag{4.2}
$$

在半径 $S$ 处，$E_{p,j}$ 的这条系数子序列的加权赋值恒为

$$
\frac1{p-1}+\frac{jp}{p^2-1}\quad(j>0),
\qquad \frac1{p-1}\quad(j=0).
\tag{4.3}
$$

所以这些级数均不属于闭 $S$ 盘的 Tate 代数。
如果乘上非零 $\mathcal S_j$，只在 (4.3) 上增加固定的
$v_p(\mathcal S_j)$。而 (3.5) 中的余项在更大的闭 $\rho$ 盘解析，
其在 $S$ 上的加权系数趋零，不可能抵消这条子序列。

不同 $j$ 的模型支撑在互不相同的 $d$ 余类，彼此也不能抵消。

## 5. 中央导数的准确 Stokes 等价

由 (2.4)、(3.5)、(4.3)，得到

$$
\boxed{\quad
J_{A,p}'(0)=0
\iff P_0K\in\mathbb Q_p\langle z/\rho\rangle
\iff \|P_0K\|_\rho\le\rho^{p+3}.
\quad}
\tag{5.1}
$$

第二个等价的反向使用精确半径：若 $\mathcal S_0\ne0$，
$P_0K$ 的半径准确为 $S<\rho$，因而不能在闭 $\rho$ 盘有有限 Gauss 范数。
并且这时 $P_0K$ 连闭 $S$ 盘的 Tate 条件也不满足；
沿 $h=p^n$ 的加权赋值最终准确为
$v_p(J_{A,p}'(0))+1/(p-1)$。

这严格识别了真实中央导数为实际 Euler 方程的中央 Stokes 常数，
没有用裸 $d\log$ 或另一个 theta 模型替换输入。
若将 (5.1) 用于本课题，仍需对无穷多个 $p$ 证明该中央常数非零；
已证的 Selmer 接口给其非零是初级有限的充分条件。

## 6. 实际非中央块 $j=4$ 永远不消失

对每个 $0<j\in\mathcal I$，(2.3) 说明 (2.5) 中 $h\ge1$ 的项
全被 $p$ 整除，又 $g_{j,0}=[z^j]A=\beta_j$。因此

$$
\mathcal S_j\equiv\beta_j\pmod p.
\tag{6.1}
$$

特别地，$d\ge8$，故 $j=4$ 总在 $\mathcal I$ 中，且实际首项给

$$
\boxed{\qquad \mathcal S_4\equiv1\pmod p.\qquad}
\tag{6.2}
$$

这是所有目标惰性素数的定理，不是有限样例。
由 §4 的互不抵消性，整个 $K$ 的半径因此总是准确等于 $S$，
且不满足闭 $S$ 盘的 Tate 条件。再由 (1.4)，

$$
\boxed{\qquad
\frac{\mathscr H}{f_0}=\frac K{G_0}
\text{ 的收敛半径对每个惰性 }p\ge7
\text{ 都准确等于 }p^{-p/(p^2-1)}.
\qquad}
\tag{6.3}
$$

理由是 $G_0$ 及其逆在更大闭盘 $\rho$ 上解析：若商的半径更大，
乘回 $G_0$ 就使 $K$ 的半径更大，与 §4 矛盾。闭 $S$ Tate 失败也同样
由可逆乘法保持。

因此，中央条件 $J_{A,p}'(0)=0$ 即使成立，也只改善 $P_0K$；
它不会改善整个固定原函数除去参考后的半径。
实际 $j=4$ 的单位正是一个不能略去的阻碍。
关于[保留参考的切向范数](2026-11-12-short-cycle-miller-and-theta-tangent-norm.md)，
其方向 $R=A/f_0$ 的 trace 本征关系没有消去这个明确存在的块。
要走跨素数代数化，必须保留 $p$ 依赖的中央投影或找到另一种真正消去
所有非中央 Stokes 项的固定结构；不能把 (5.1) 擅自升级为整个
$\mathscr H/f_0$ 的半径改善。

## 7. 固定切向范数在各 Stokes 块上的真实作用

这里进一步检查前文的范数是否把各余类联系起来。
固定 $b=69$；本节只排除 $p\mid b$，在前述范数稿的
$p\equiv35,67\pmod {68}$ 短周期素数中无需另加例外。
由于 $bP=P$，同一个 Miller 除子证明给
$\sum_{Q\in E[b]}R(Z+Q)=bR([b]Z)$。
所以常数项一的代数 theta 切向范数准确为

$$
\mathscr N_b(f_0+\tau A)=f_0(bz)+\tau bA(bz).
\tag{7.1}
$$

先使用这个函数层等式，再取线性的 shifted 变换；没有将乘积的
Mellin 变换误写为各变换的乘积。
新截面的次数为 $17b^2$，故相应首坏指数取 $a_b=b^2a$。
对非负整数 $k$，直接取系数给

$$
k!a_b^{-k}[z^{dk+j}]\{bA(bz)\}
  =b^{j+1}\bigl(b^{p-1}\bigr)^k\mathcal J_{p,j}(k).
$$

由于 $b^{p-1}\in1+p\mathbb Z_p$，右边有唯一的解析延拓。
左边的 residual 同样满足所需半径：

$$
e^{-a_bz^d}bA(bz)
 =b\exp\bigl(a(b^d-b^2)z^d\bigr)G(bz),
$$

其中额外指数的系数为整。因此恒等定理给

$$
\boxed{\quad
\mathcal J^{[a_b]}_{bA(bz),j}(u)
 =b^{j+1}\bigl(b^{p-1}\bigr)^u\mathcal J_{p,j}(u).
\quad}
\tag{7.2}
$$

方括号标注首坏指数的参数，不表示求导。
参考行相应变为
$\mathcal J^{[a_b]}_{f_0(bz),0}(u)
=(b^{p-1})^u\mathcal J^{[a]}_{f_0,0}(u)$。
所以先除去真实参考，再取切向中心导数，只把原值乘以 $b$。
候选的 $\log_p(b^{p-1})$ 项乘上 $J_{A,p}(0)=0$，准确消失。

同样，(2.4)–(2.5) 中的常数变为

$$
\mathcal S_{0,b}=b\mathcal S_0,\qquad
\mathcal S_{j,b}
  =b^{j+1}(b^{p-1})^{-j/d}\mathcal S_j\quad(j>0).
\tag{7.3}
$$

各乘子均为 $p$ 进单位。这个合法的固定范数比较在 Stokes 向量上
是对角作用：它保留各块原来的消失或非消失，没有把中央块和
实际单位块 $j=4$ 联系成同一个条件。
这精确解释了为何 (6.2) 与中央消失仍可同时成立；目前这些范数
恒等式不能把已知的非中央单位移到目标中央导数。
