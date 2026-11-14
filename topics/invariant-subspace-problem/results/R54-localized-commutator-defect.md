# R54：原临界核的柱乘子局部化缺陷

日期：2026-11-12（UTC+8）。分工：`critical_kernel`。

**状态：已完成证明的局部化路线约束；实际核仍未决定。** 沿用 R53 的 $K=\ker L$、$B$、$\delta_j$、$E_j$、$\eta_j$；本条使用 [R53](R53-critical-kernel-isotropy-and-parity-graph.md) 的实际尾模型近似与实系数核性质，给出全部新的局部化计算。

## 1. 柱乘子局部化：额外项的实际渐近值

设 $\varphi$ 为固定有限柱函数。若能进一步构造实际交换子强极限 $[Y_m,L]\to M_\varphi$，则对 $v,w\in K$ 的同一论证会给出 $B(M_\varphi v,w)=0$。对所有柱函数都得到此结论，将足以迫使 $K=0$；下文同时说明朴素尾乘子及正规重选权为何没有实现它。

固定 $v,w\in K$，记

$$
b_j=B([M_\varphi,L]M_{\chi_j}v,w).
$$

**命题 1.1。**

$$
\boxed{\frac{b_j}{\delta_j}\longrightarrow B(M_\varphi v,w).}
\tag{1.1}
$$

**证明。** 对足够大的 $j$，R50/R53 的 $T_j$ 头部不作用第 $j$ 位，其尾部只有 $\delta_jE_j$ 不与 $M_{\chi_j}$ 交换。因而

$$
\|[M_{\chi_j},L]+2\delta_jE_j\|
\le44\eta_{j-1}.
\tag{1.2}
$$

因为 $v,w\in K$ 且 $L$ 对 $B$ 对称，任意有界 $X$ 都满足 $B([X,L]v,w)=0$。取 $X=M_\varphi M_{\chi_j}$ 并展开，得到

$$
b_j=2\delta_jB(M_\varphi E_jv,w)
   +O(\|\varphi\|_\infty\eta_{j-1}\|v\|\|w\|).
$$

$E_j\to I/2$ 于 WOT：在固定柱函数对上由高位独立性直接成立，再用一致范数界与密度推广。又 $\eta_{j-1}/\delta_j\to0$，故上式除以 $\delta_j$ 后即得 (1.1)。证毕。

现在取任意有限支集复权 $\beta_{m,j}$，满足

$$
\min\{j:\beta_{m,j}\ne0\}\to\infty,\qquad
\sum_j\beta_{m,j}=1,\qquad
\sup_m\sum_j|\beta_{m,j}|<\infty.
\tag{1.3}
$$

置 $\alpha_{m,j}=\beta_{m,j}/\delta_j$、$G_m=\sum_j\alpha_{m,j}M_{\chi_j}$。由 (1.1) 和 (1.3)，

$$
\boxed{
B([M_\varphi,L]G_mv,w)
=\sum_j\beta_{m,j}\frac{b_j}{\delta_j}
\longrightarrow B(M_\varphi v,w).
}
\tag{1.4}
$$

所以当 $[G_m,L]\to-I$ 的尾平均方案成功时，

$$
[M_\varphi G_m,L]
=M_\varphi[G_m,L]+[M_\varphi,L]G_m
$$

中的额外项在核对上的配对恰好抵消所期待的 $-M_\varphi$ 配对。它不因为改变满足 (1.3) 的正规权而自动消失；若证明它消失，就已经证明了需要的新局部等向性。

允许 $\sum|\beta_{m,j}|$ 无界也不能不加估计地保留纯尾平均的强算子收敛。事实上，对任何有限复权，

$$
\left\|\sum_j\beta_jE_j\right\|
\ge\frac12\sum_j|\beta_j|.
\tag{1.5}
$$

证明只需在所选有限位上取单位产品向量，使每个 $E_j$ 的数值期望相位与 $\beta_j$ 相反、绝对值为 $1/2$；其余位取 Haar 参考向量。对应矩阵元就是右侧。故纯平均若强收敛，其算子范数一致有界，从 (1.5) 必得到有界总变差。此处没有排除加入全新的算子修正；只指出标量尾平均本身的确切限制。

最后核实“全部柱局部化足以结束”的说法。若 $B(M_\varphi v,w)=0$ 对所有柱函数及所有 $v,w\in K$ 成立，则柱函数分离 $L^1$，故

$$v(y)w(-1-y)=0\quad\text{几乎处处，所有 }v,w\in K.$$

若 $0\ne v\in K$，取 $w=A^n\overline v\in K$，$n\ge0$。所有有限权积几乎处处严格正，因此 $E=\{v\ne0\}$ 与 $-1-n-E$ 的交都必须为零测。加一变换的遍历性保证正测度集合 $-1-E$ 的所有非负整数平移之并为满测度，从而它们不可能全部与正测度的 $E$ 零交，矛盾。

当前缺的正是这一**全部柱局部化**，而 (1.1)–(1.4) 表明旧尾乘子方案的额外项没有被解决。
