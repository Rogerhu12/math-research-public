# R57：有限多变量指数多项式与原临界算子的全部广义核分离

日期：2026-11-12。会话：Astra-ISP-0c017065，子任务 `l2_moments`。

**状态：已证明的中间结论。** 本文处理原来的真实算子 $D=I-Q$，不替换为无进位模型。允许任意有限个复平方可和 Rademacher 级数、任意代数关系、有限多变量指数多项式及有限前缀柱函数系数。所得向量不可能非零地属于任何 $\ker D^q$，$q\ge1$。证明通过一个有限维广义核阶梯完成，不要求多变量评价映射单射，也不要求各级数系数相对于 $\delta_j$ 有任何额外衰减率。

这不决定整个 $\ker D$，不证明这些向量各自循环，不解决一般两端多变量矩分离，也不解决完整 Hilbert 不变子空间问题。

依赖：R9/R12 的高位矩阵单位近似与有限链；R11 的 $1$ 循环性；R24 的复双线性对称性；R43 的原临界算子与 $\ker D^q=\ker L^q$；R44 的有限链归一化幂截断估计。新的有限维翻译公式、误差控制、测试升级和广义核阶梯全部在下文证明。

## 1. 向量类及主定理

沿用 $H=L^2(\mathbb Z_2,\mu)$，$\chi_j(y)=(-1)^{b_j(y)}$，以及

$$
(Af)(y)=w(y)f(y-1),\qquad w(0)=0,\qquad w(y)=a_{v_2(y)}\quad(y\ne0),
$$

$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$

原临界算子为

$$
N_j=\frac{A^{2^j}}{\|A^{2^j}\|},\qquad
\eta_j=\frac{a_{j+1}}{a_j},\qquad
\delta_j=\frac{2}{(j+2)^2+1},\qquad r_j=1-\delta_j,
$$

$$
V_j=(I+r_jN_j)(I+N_j)^{-1},\qquad
Q=\prod_{j\ge0}V_j,\qquad D=I-Q.
\tag{1.1}
$$

取有限整数 $s\ge1$、$m_0\ge0$，以及任意复级数

$$
X_\ell=x_{\ell,*}+\sum_{j\ge m_0}x_{\ell j}\chi_j,
\qquad (x_{\ell j})_{j\ge m_0}\in\ell^2,
\qquad 1\le\ell\le s.
\tag{1.2}
$$

写 $X=(X_1,\ldots,X_s)$，$\mathscr C_{m_0}$ 为低 $m_0$ 位的柱函数空间。令

$$
F(z)=\sum_{\lambda\in\Lambda}P_\lambda(z)e^{\lambda\cdot z},
\qquad \Lambda\subset\mathbb C^s\text{ 有限},
\qquad P_\lambda\in\mathscr C_{m_0}[z_1,\ldots,z_s].
\tag{1.3}
$$

这里 $\lambda\cdot z=\sum_\ell\lambda_\ell z_\ell$，不取共轭。允许各个 $X_\ell$ 线性相关乃至满足任意其他关系；允许形式非零的 $F$ 代入后为零。

**定理 1.1。** 对所有 (1.2)–(1.3)，$F(X)\in H$，且

$$
\boxed{D^qF(X)=0\text{ 对某个有限 }q\ge1
\quad\Longrightarrow\quad F(X)=0.}
\tag{1.4}
$$

由于 $D=L\Psi(L)$，其中 $\Psi(L)$ 可逆且与 $L$ 交换，同一结论对 $L^q$ 成立。

令 $\mathscr E_{\mathrm{fin}}$ 为所有上述向量的并集。这个类是线性空间：两种表达式的级数合并为一个有限向量，并把有限低位项吸收进共同的柱系数即可。它包含任意有限个不同标量 Rademacher 级数的指数多项式之和、任意有限多变量多项式及其与有限多个指数的组合。结论为

$$
\mathscr E_{\mathrm{fin}}\cap\bigcup_{q\ge1}\ker D^q=\{0\}.
\tag{1.5}
$$

## 2. 评价空间：有限维，但不假设单射

所有复 Rademacher 级数 (1.2) 有任意有限阶绝对矩。对任意 $\lambda\in\mathbb C^s$，$\operatorname{Re}(\lambda\cdot X)$ 是常数加实平方可和 Rademacher 级数，且有限和满足

$$
\mathbb E\exp\left(t\sum_jc_j\chi_j\right)
=\prod_j\cosh(tc_j)
\le\exp\left(\frac{t^2}{2}\sum_jc_j^2\right).
\tag{2.1}
$$

Fatou 引理给极限的全部实指数矩。由矩估计和 Hölder 不等式，$X^\alpha e^{\lambda\cdot X}\in L^p$ 对每个有限 $p$ 成立。这同时保证下文所有导数代入合法。有限和的代入在有限 $L^p$ 中收敛，可由多项式差分、

$$
|e^u-e^v|\le |u-v|\bigl(e^{\operatorname{Re}u}+e^{\operatorname{Re}v}\bigr)
$$

及 (2.1) 的一致指数矩直接得到。

固定一个表达式 (1.3)。对每个 $\lambda$ 选取 $d_\lambda\ge\deg P_\lambda$，令有限维形式空间

$$
V=\operatorname{span}\{h z^\alpha e^{\lambda\cdot z}:
h\in\mathscr C_{m_0},\ \lambda\in\Lambda,\ |\alpha|\le d_\lambda\}.
\tag{2.2}
$$

可把 $V$ 看作形式系数空间，或看作实际整函数空间；两种处理均可。每个 $\partial_\ell=\partial/\partial z_\ell$ 是 $V$ 上的有限矩阵，彼此交换。柱函数系数不参与求导。

固定 $V$ 的任意范数。评价映射

$$
\mathcal E:V\longrightarrow H,\qquad \xi\longmapsto\xi(X)
\tag{2.3}
$$

由上述可积性有界，令 $U=\mathcal E(V)$。**整个证明始终在 $V$ 上定义导数和翻译，不把它们擅自传到 $U$。** 特别地，不假设 $\ker\mathcal E$ 在导数下不变。

对 $j\ge m_0$ 置

$$
Z_j=\sum_{\ell=1}^s x_{\ell j}\partial_\ell.
\tag{2.4}
$$

$\|Z_j\|\to0$，而 $e^{Z_j}\xi(z)=\xi(z+x_j)$ 是精确的有限维翻译恒等式。对充分大的 $j$，$\cosh Z_j$ 可逆，并定义

$$
C_j=\frac12e^{Z_j}(\cosh Z_j)^{-1}
=\frac12(I+\tanh Z_j).
\tag{2.5}
$$

于是 $C_j\to I_V/2$，$C_j^2\to I_V/4$，各矩阵最终一致有界。

## 3. 真实 Q 的单高位近似

令 $E_j=e_{10}$ 只作用第 $j$ 位的物理基，满足 $E_j^2=0$、$E_j1=(1-\chi_j)/2$。已证估计为

$$
\|N_j\|\le1,\quad \|N_j^2\|\le\eta_j,\quad
\|N_j-E_j\|=\eta_j,
\tag{3.1}
$$

且 $N_i$ 不作用任何低于 $i$ 的位。$A_j$ 为只作用低 $j$ 位的有限链，

$$
\|A-A_j\|=a_j,\qquad \|A^n-A_j^n\|\le n a_j.
\tag{3.2}
$$

对 $i<j$ 置 $N_i^{[j]}=A_j^{2^i}/\|A^{2^i}\|$。R44 给

$$
\|N_i-N_i^{[j]}\|=\frac{a_j}{a_i},\qquad
\|N_i^{[j]}\|\le1,\qquad
\|(N_i^{[j]})^2\|\le\eta_i.
\tag{3.3}
$$

记 $V_i(T)=(I+r_iT)(I+T)^{-1}$。对本段出现的 $T$，因 $\eta_i\le\eta_0<1/4$，

$$
\|(I+T)^{-1}\|
\le\frac{2}{1-\eta_0}\le\frac83.
$$

由 $V_i(T)=r_iI+\delta_i(I+T)^{-1}$ 及预解式恒等式，

$$
\|V_i(T)\|\le1+\frac83\delta_i,\qquad
\|V_i(T)-V_i(S)\|\le\frac{64}{9}\delta_i\|T-S\|.
\tag{3.4}
$$

令 $K=\exp((8/3)\sum_i\delta_i)<\infty$。所有原因子或截断因子的连续乘积范数都不超过 $K$。望远镜展开及 (3.3) 给

$$
\left\|\prod_{i<j}V_i(N_i)-\prod_{i<j}V_i(N_i^{[j]})\right\|
\le\frac{64}{9}K^2\sum_{i<j}\delta_i\frac{a_j}{a_i}
\le C\eta_{j-1}.
\tag{3.5}
$$

最后一步使用 $a_i\ge a_{j-1}$。此外，(3.4) 对 $S=E_j$ 给

$$
\|V_j-(I-\delta_jE_j)\|\le C\delta_j\eta_j.
\tag{3.6}
$$

定义

$$
S_j=\left(\prod_{i<j}V_i(N_i^{[j]})\right)
\left(\prod_{i>j}V_i(N_i)\right),\qquad
\widetilde Q_j=S_j(I-\delta_jE_j).
\tag{3.7}
$$

前一个括号只作用低于 $j$ 的位，后一个只作用高于 $j$ 的位。因此 $S_j$ 在第 $j$ 位为恒等，且与 $E_j$、$A_j$ 交换；$\sup_j\|S_j\|<\infty$。原 $V_i$ 彼此交换，故 (3.5)–(3.6) 的乘积差估计给

$$
\boxed{\|Q-\widetilde Q_j\|\le C\eta_{j-1}.}
\tag{3.8}
$$

这里只使用范数望远镜差，不需要原算子与截断算子彼此交换。

因为 $E_j^2=0$，对每个固定整数 $k\ge0$，

$$
\widetilde Q_j^{\,k}=S_j^k(I-k\delta_jE_j),\qquad
\|Q^k-\widetilde Q_j^{\,k}\|\le C_k\eta_{j-1}.
\tag{3.9}
$$

从而对固定 $n,k\ge0$，

$$
\begin{split}
\|A^nQ^k1-A_j^n\widetilde Q_j^{\,k}1\|&\le C_{n,k}\eta_{j-1},\\
\|N_jA^nQ^k1-E_jA_j^n\widetilde Q_j^{\,k}1\|&\le C_{n,k}\eta_{j-1}.
\end{split}
\tag{3.10}
$$

这里使用 $a_j\le\eta_{j-1}$、$\eta_j\le\eta_{j-1}$。常数允许依赖固定 $n,k$，不依赖 $j$。

## 4. 精确单比特矩阵公式

使用 R24 的复双线性型

$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
\tag{4.1}
$$

反射 $y\mapsto-1-y$ 逐位取补。记 $X^{(j)}=X-x_j\chi_j$，它不依赖第 $j$ 位。令 $\mathcal E_j^0\xi=\xi(X^{(j)})$ 为去掉该位的评价。它有界且最终一致有界：若 $P_j$ 是对第 $j$ 位取条件平均，则

$$
P_j\mathcal E=\mathcal E_j^0\cosh Z_j,
\qquad
\mathcal E_j^0=P_j\mathcal E(\cosh Z_j)^{-1}.
\tag{4.2}
$$

对固定 $k$，充分大的 $j$ 还保证 $I-k\delta_jC_j$ 可逆。定义

$$
R_{j,k}=C_j(I-k\delta_jC_j)^{-1}.
\tag{4.3}
$$

在有限维矩阵范数中，

$$
\boxed{R_{j,k}=C_j+k\delta_jC_j^2+O_k(\delta_j^2).}
\tag{4.4}
$$

余项常数与大 $j$ 无关，因为 $C_j$ 一致有界。尤其这里没有对 $C_j-I/2$ 作任何以 $\delta_j$ 为尺度的估计。

**引理 4.1。** 若 $t\in H$ 不依赖第 $j$ 位，则对所有 $\xi\in V$ 有精确恒等式

$$
B(E_j(I-k\delta_jE_j)t,\mathcal E\xi)
=B((I-k\delta_jE_j)t,\mathcal E R_{j,k}\xi).
\tag{4.5}
$$

**证明。** 第 $j$ 位按物理基 $(b_j=0,b_j=1)$，$t$ 的局部向量为 $(t,t)$，

$$
(I-k\delta_jE_j)t=(t,(1-k\delta_j)t),\qquad
E_j(I-k\delta_jE_j)t=(0,t).
$$

把其余位上的双线性积分记为 $\Gamma_t$，其中去位评价 $\mathcal E_j^0$ 及其余位反射已包含在内。逐位取补给

$$
B((I-k\delta_jE_j)t,\mathcal E\zeta)
=\Gamma_t\left(\frac{e^{-Z_j}+(1-k\delta_j)e^{Z_j}}2\right)\zeta
=\Gamma_t\cosh Z_j(I-k\delta_jC_j)\zeta,
$$

而

$$
B((0,t),\mathcal E\xi)=\frac12\Gamma_t e^{Z_j}\xi.
$$

所有矩阵都是 $Z_j$ 的函数，彼此交换。令 $\zeta=R_{j,k}\xi$，由 (2.5)、(4.3) 两式右边相等。上述计算不需要任何评价映射单射。证毕。

在 (4.5) 中取 $t=A_j^nS_j^k1$。它不依赖第 $j$ 位。由 (3.9)–(3.10)、$\mathcal E$ 有界及 $R_{j,k}$ 一致有界，得到真实算子的测试公式

$$
\boxed{
B(N_jA^nQ^k1,\mathcal E\xi)
=B(A^nQ^k1,\mathcal E R_{j,k}\xi)
+O_{n,k,V}(\eta_{j-1})\|\xi\|_V.
}
\tag{4.6}
$$

$Q$ 与 $A$ 交换且对 $B$ 对称，故 (4.4) 进一步给

$$
\begin{split}
B(N_jA^nQ^k1,\mathcal E\xi)
={}&B(A^n1,Q^k\mathcal E C_j\xi)\\
&+k\delta_j B(A^n1,Q^k\mathcal E C_j^2\xi)
+O_{n,k,V}(\delta_j^2+\eta_{j-1})\|\xi\|_V.
\end{split}
\tag{4.7}
$$

## 5. 有限维矩测试升级为向量估计

**引理 5.1。** 对每个有限维子空间 $W\subset H$，存在有限指标 $n_1,\ldots,n_t\ge0$ 及常数 $K_W<\infty$，使

$$
\|w\|\le K_W\max_{1\le\nu\le t}|B(A^{n_\nu}1,w)|\qquad(w\in W).
\tag{5.1}
$$

**证明。** 若 $B(A^n1,w)=0$ 对全部 $n$，由 $1$ 对 $A$ 循环及 $B$ 非退化，$w=0$。因 $W$ 有限维，线性泛函族的共同核为零蕴含已有有限子族共同核为零：从 $W$ 开始，只要当前共同核非零就选一个使其维数下降的泛函，至多 $\dim W$ 步停止。由有限维范数等价得到 (5.1)。证毕。

**引理 5.2（广义核阶梯的单步）。** 对每个整数 $p\ge0$，

$$
\boxed{v\in U\cap\ker D^{p+1}\quad\Longrightarrow\quad D^pv\in D^{p+1}U.}
\tag{5.2}
$$

**证明。** 写 $v=\mathcal E\xi$。不需要以任何特殊方式选原像 $\xi$，只在整个证明中固定它。$N_j,A,D$ 彼此交换且对 $B$ 对称，所以

$$
0=B(N_jA^nD^{p+1}1,v)
=\sum_{k=0}^{p+1}(-1)^k\binom{p+1}{k}B(N_jA^nQ^k1,v).
\tag{5.3}
$$

将 (4.7) 代入，并使用

$$
\sum_{k=0}^{p+1}(-1)^k\binom{p+1}{k}Q^k=D^{p+1},
$$

$$
\sum_{k=0}^{p+1}(-1)^k\binom{p+1}{k}kQ^k=-(p+1)QD^p,
$$

可得对每个固定 $n$，

$$
|B(A^n1,w_j)|\le C_{n,p,V}(\delta_j^2+\eta_{j-1})\|\xi\|_V,
\tag{5.4}
$$

其中

$$
w_j=D^{p+1}\mathcal E C_j\xi
-(p+1)\delta_j QD^p\mathcal E C_j^2\xi.
\tag{5.5}
$$

这些 $w_j$ 全部属于固定有限维空间

$$
W_p=D^{p+1}U+QD^pU.
\tag{5.6}
$$

对 $W_p$ 使用引理 5.1，只需有限多个固定 $n$ 的 (5.4)，便得到

$$
\|w_j\|\le C_{p,V}(\delta_j^2+\eta_{j-1})\|\xi\|_V.
\tag{5.7}
$$

现在取 $H$ 对闭子空间 $D^{p+1}U$ 的商。第一项 $D^{p+1}\mathcal E C_j\xi$ 精确落在被模掉的空间里，无需估计它与 $(1/2)D^{p+1}v$ 的差。除以正数 $\delta_j$，(5.7) 给

$$
\operatorname{dist}\left((p+1)QD^p\mathcal E C_j^2\xi,D^{p+1}U\right)
\le C_{p,V}\left(\delta_j+\frac{\eta_{j-1}}{\delta_j}\right)\|\xi\|_V.
\tag{5.8}
$$

本模型有 $\delta_j\to0$ 和 $\eta_{j-1}/\delta_j\to0$，而 $C_j^2\xi\to\xi/4$。$D^{p+1}U$ 有限维而闭，因此取极限得

$$
QD^pv\in D^{p+1}U.
$$

由于 $D^{p+1}v=0$，$QD^pv=(I-D)D^pv=D^pv$，即 (5.2)。证毕。

上述取商步骤是证明的关键：若过早把 $C_j$ 换成 $I/2$，会引入 $O(\|Z_j\|)$ 的误差，再除以 $\delta_j$ 未必趋零。本证明完全避免这一错误。

## 6. 有限维空间不能容纳无限长的原像阶梯

假设 $0\ne v\in U\cap\ker D^q$。取最小的 $r\ge1$ 使 $D^rv=0$，令

$$
w=D^{r-1}v\ne0,
\qquad Dw=0.
$$

先置 $u_{r-1}=v\in U$，故

$$
D^{r-1}u_{r-1}=w,\qquad D^ru_{r-1}=0.
$$

假定已构造 $u_p\in U$ 满足 $D^pu_p=w$、$D^{p+1}u_p=0$。引理 5.2 给

$$
w=D^pu_p\in D^{p+1}U.
$$

于是可选 $u_{p+1}\in U$ 使 $D^{p+1}u_{p+1}=w$；自动有 $D^{p+2}u_{p+1}=Dw=0$。因此可对所有 $p\ge r-1$ 继续。

每个 $u_p$ 都属于

$$
U\cap\ker D^{p+1}\quad\text{但不属于}\quad U\cap\ker D^p,
$$

因为 $D^pu_p=w\ne0$。所以 $U\cap\ker D^p$ 从某一级开始每步严格增大，与 $\dim U<\infty$ 矛盾。这证明 (1.4)–(1.5)。注意此段并未要求 $w\in U$，只要求每个原像 $u_p\in U$。

## 7. 原临界向量的矩分离推论与适用边界

令 $f_*=D1$。由交换及 $B$-对称性，

$$
B(A^nf_*,u)=B(A^n1,Du).
$$

因此 $1$ 的循环性给

$$
B(A^nf_*,u)=0\quad(n\ge0)\quad\Longleftrightarrow\quad Du=0.
$$

定理 1.1 遂推出

$$
\boxed{u\in\mathscr E_{\mathrm{fin}},\quad
B(A^nf_*,u)=0\ (n\ge0)\quad\Longrightarrow\quad u=0.}
\tag{7.1}
$$

更一般地，对每个有限 $q\ge1$，$f_q=D^q1$ 也分离整个 $\mathscr E_{\mathrm{fin}}$：

$$
B(A^nf_q,u)=0\quad(n\ge0),\quad u\in\mathscr E_{\mathrm{fin}}
\quad\Longrightarrow\quad u=0.
\tag{7.2}
$$

反射共轭 $Cu(y)=\overline{u(-1-y)}$ 保持该向量类：它把每个级数系数变成 $-\overline{x_{\ell j}}$、常数变成 $\overline{x_{\ell,*}}$，并把柱系数和形式表达式作相应共轭。因此 (7.1)–(7.2) 也有通常复内积版本。

本结果允许例如

$$
u=P(X_1,X_2)e^{X_1}+R(X_2,X_3)e^{2X_2-X_3}
$$

的任意非零成员，其中三个复平方可和级数可以完全不同，可以不连续，可以有代数关系。它们不属于任意有限阶广义核。此前的单标量指数多项式排除不能直接处理这些一般多变量表达式。

但这里没有证明任意非零 $f,g\in\mathscr E_{\mathrm{fin}}$ 都互相矩分离；(7.1) 的一端必须是指定的 $D1$，(7.2) 的一端是 $D^q1$。也不能由该类含稠密柱函数核心推出 $D$ 在整个 $H$ 上单射。一般 $L^2$ 核向量仍未排除。

## 8. 抽象机制的精确条件

证明实际上只使用如下条件：

1. $1$ 对 $A$ 循环，相关算子对非退化连续双线性型 $B$ 对称并与 $A$ 交换；按第 $j$ 位分解时，$B$ 的局部配对为 $\tfrac12(u_0v_1+u_1v_0)$，其余位上保留相应双线性积分。
2. 存在高位 $E_j$ 及不作用第 $j$ 位的 $S_j$，使 $Q$ 与 $S_j(I-\delta_jE_j)$ 的误差为 $\varepsilon_j$，并且固定幂与固定矩测试的替换误差仍为 $O_{n,k}(\varepsilon_j)$。
3. $\delta_j\to0$ 且 $\varepsilon_j/|\delta_j|\to0$。
4. 存在有限维形式空间 $V$、有界评价 $\mathcal E$ 以及平移矩阵 $Z_j\to0$，使第 $j$ 位评价精确为 $e^{\pm Z_j}$ 的两个分支。

在这些条件下，$C_j=\tfrac12 e^{Z_j}(\cosh Z_j)^{-1}$ 的局部公式、有限测试升级、取商和广义核阶梯照样成立。原模型中 $\varepsilon_j=O(\eta_{j-1})$，已在 §3 严格验证。因此结果不依赖无原子性、单变量整函数零点性质或多变量零集孤立性，也不使用任何无定量的稠密性闭包步骤。
