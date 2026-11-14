# R240附录：有限一阶预解式乘积仍不能完成配对正则化

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：完整实际反例。使用 R207 指数次数尺度付清全部有限混合自然词、系数截断乘积的极限和测试成本。它统一加强单个一阶预解式反例，仍不涉及慢符号主理想的正湮灭者构造。

## 1. 固定向量及其实际矩增长

取
$$
J_p=[4p^2,4p^2+2p)\cap\mathbb N_0,\quad
c_p=2^{-p/4},\quad \varepsilon=1/16,
$$
$$
f=1+\varepsilon\sum_{p\ge1}c_p\chi_{J_p}.
\tag{1.1}
$$
这些块互不交，每块大小为 $2p$。[R240](R240-cyclic-positive-functional-without-fixed-vacuum-factor.md) 的实际反例证明：

- $f$ 连续、严格正且 $Cf=f$；
- $\varepsilon^2\sum c_p^2<\infty$，实际块 carry 差可和，故 R136 给 $f$ 对 $A$ 循环及其有限柱核心闭乘子 $X_f$；
- 对 $V_j=(I-N_j)(I+N_j)^{-1}$，
  $V_{J_p}1=\chi_{J_p}$，并且
  $$
  \operatorname{Re}\langle V_{J_p}f,f\rangle
  \ge\varepsilon^2\,2^{3p/2}+2\varepsilon c_p-o(1).
  \tag{1.2}
  $$

为使增长输入自含，纯 $D_j=I-2E_j$ 满足
$D_j1=\chi_j$、$D_j\chi_j=2\chi_j-1$。不同块正交给
$$
\langle D_{J_p}f,f\rangle
=2\varepsilon c_p+\varepsilon^2c_p^2\,2^{2p}.
$$
排序 telescoping 及明确 carry 包络给
$$
\|V_{J_p}-D_{J_p}\|
\le16p6^{2p-1}e^{-77016^{4p^2}}\to0,
$$
从而得到 (1.2)，同时支付 R136 所需的实际块差可和。

## 2. R207 尺度上的任意有限混合自然词

令 $\mathcal N$ 为原 Haar Walsh 次数算子，
$$
H_t=\operatorname{Dom}e^{t\mathcal N},\qquad
\|u\|_t=\|e^{t\mathcal N}u\|,\qquad 0\le t\le1.
$$
R207 指数次数附录引理A.1（取尾起点 $m=0$）给固定模型常数 $C$，对任意 $b\in\ell^2$、$0<\delta\le t\le1$，
$$
\left\|\sum_jb_jV_j:H_t\to H_{t-\delta}\right\|
\le C\|b\|_2\delta^{-1/2}.
\tag{2.1}
$$
这是实际闭一阶乘子的限制，已包含真实 carry；正指数尺度确实包含在其真实定义域中。

固定整数 $k\ge1$。对 $\nu=1,\ldots,k$，令
$$
F_\nu=\lambda_\nu I+X_{b^{(\nu)}}=
a_\nu I+\sum_jb_j^{(\nu)}V_j,
\qquad b^{(\nu)}\in\ell^2,
$$
其中 $a_\nu$ 吸收一阶常数项和 $\lambda_\nu$。
有限截断为
$$F_{\nu,n}=a_\nu I+\sum_{j=0}^n b_j^{(\nu)}V_j\in\mathcal A.$$

由 (2.1) 以及同一引理用于系数尾，
$$
\|F_\nu:H_t\to H_{t-\delta}\|,
\ \sup_n\|F_{\nu,n}:H_t\to H_{t-\delta}\|
\le |a_\nu|+C\|b^{(\nu)}\|_2\delta^{-1/2},
\tag{2.2}
$$
$$
\|F_{\nu,n}-F_\nu:H_t\to H_{t-\delta}\|
\le C\|b^{(\nu)}_{>n}\|_2\delta^{-1/2}\to0.
\tag{2.3}
$$

取任意 $0<t\le1$，将 $t\to0$ 分为 $k$ 个等步长 $\delta=t/k$。从右到左实际依次作用，定义自然词
$$P=F_1F_2\cdots F_k.$$
每个中间输出仍在正指数尺度中，直到最后一步才进入 $H_0$。所以 $H_t$ 中的每个向量都在这个自然复合域内；这不是由各因子域的交集作出的推断。

准确成本为
$$
\boxed{
\|P:H_t\to H\|
\le\prod_{\nu=1}^k
\left(|a_\nu|+C\|b^{(\nu)}\|_2\sqrt{k/t}\right).
}
\tag{2.4}
$$
同一界适用于有界截断乘积 $P_n=F_{1,n}\cdots F_{k,n}$。按固定顺序对乘积作有限 telescoping，每一项用 (2.3) 及其余因子的 (2.2)，得到
$$
\boxed{P_n\to P\quad\text{于 }B(H_t,H).}
\tag{2.5}
$$
中间尺度在每一项中都保留。有限截断因子两两交换，所以不同顺序的自然词在这些指数尺度上也有相同值；下面只需要一个固定顺序。

## 3. 固定向量与有限次数测试都在全部所需复合域内

由 (1.1) 的正交次数分解，
$$
\|e^{t\mathcal N}f\|^2
=1+\varepsilon^2\sum_{p\ge1}e^{4tp}2^{-p/2}<\infty
\quad\text{当 }0<t<\frac{\log2}{8}.
\tag{3.1}
$$
例如可固定 $t_0=(\log2)/16$。因此对任意固定有限词，
$$
f\in\operatorname{Dom}P,\qquad P_nf\to Pf
\tag{3.2}
$$
由 (2.5) 直接成立，已付清逐次图域和真实截断极限。

另一方面，若 $u$ 属于 Walsh 次数至多 $q$ 的空间，取
$$t=\frac1{q+1}$$
则 $\|u\|_t\le e\|u\|$。代入 (2.4)，得到
$$
\boxed{
\|Pu\|\le L_P(q+1)^{k/2}\|u\|,
\qquad
L_P=e\prod_{\nu=1}^k
\left(|a_\nu|+C\sqrt k\,\|b^{(\nu)}\|_2\right).
}
\tag{3.3}
$$
这支付整个有限次数层，位指标可以无限远。特别
$$
\|P\chi_{J_p}\|\le L_P(2p+1)^{k/2}.
\tag{3.4}
$$
固定 $p$ 时，(2.5) 也给 $P_n\chi_{J_p}\to P\chi_{J_p}$。

## 4. 任意有限预解乘积的反例

假设每个 $F_\nu$ 均有有界处处定义的逆 $R_\nu=F_\nu^{-1}$。由一阶的实际域交换，
$$R_\nu\in\mathfrak C.$$
因此这些有界预解式交换，记
$$R=R_k\cdots R_1.$$
允许重复因子，因而包括有限幂。对 $u\in\operatorname{Dom}P$，按定义顺序依次消去
$R_1F_1,R_2F_2,\ldots$，有
$$RPu=u.$$
每次消去时，其输入确在相应 $F_\nu$ 的真实域中；这里不作无界形式约分。由 (3.2)，
$$
\boxed{RP_nf\longrightarrow f.}
\tag{4.1}
$$

定义
$$\psi_R(F)=\langle RFf,f\rangle\qquad(F\in\mathfrak C).$$
该泛函通常不正；证明只用它是否具有下面的表示。

**定理 4.1。** 不存在 $h\in H$ 满足
$$
\boxed{\psi_R(F)=B(Fh,1)\quad(F\in\mathfrak C).}
\tag{4.2}
$$

**证明。** 假设存在。固定 $p$，使用有界实际测试
$$F_n=P_nV_{J_p}\in\mathcal A.$$
所有有界因子交换，故 (4.1) 给
$$
\psi_R(F_n)
=\langle V_{J_p}RP_nf,f\rangle
\longrightarrow\langle V_{J_p}f,f\rangle.
$$
另一方面，$F_n$ 为实际 $C$ 对称交换子，且 $V_{J_p}1=\chi_{J_p}$，所以
$$
B(F_nh,1)=B(h,F_n1)
=B(h,P_n\chi_{J_p})
\longrightarrow B(h,P\chi_{J_p}).
$$
因此
$$
\langle V_{J_p}f,f\rangle=B(h,P\chi_{J_p}).
\tag{4.3}
$$
右侧由 (3.4) 至多为 $\|h\|L_P(2p+1)^{k/2}$，而左侧的实部由 (1.2) 指数增长，矛盾。证毕。

极限次序是：先固定 $p$，让 $n\to\infty$；随后才令 $p\to\infty$。不要求 $h\in\operatorname{Dom}P$。$P$ 只作用在已支付自然域的 $\chi_{J_p}$ 上。

## 5. 配对域与全域正则化的同时排除

因为 $Cf=f$，若 $Rf\in\operatorname{Dom}X_f$，[R244](R244-paired-domain-regularizers-and-normal-annihilator-factorization.md) 的配对域引理会给
$$
\langle RFf,f\rangle
=B(FX_fRf,1)\qquad(F\in\mathfrak C),
$$
违反定理4.1。故
$$
\boxed{
Rf\notin\operatorname{Dom}X_f,\qquad
RH\not\subseteq\operatorname{Dom}X_f.
}
\tag{5.1}
$$

这排除任意有限个有界复杂 $\ell^2$ 一阶预解式的乘积，包括普通正一阶预解式、其有限幂以及任意有限混合组合。它同时说明：有界因子各自具有已知的强单位或图核心性质，并不能使有限组合自动涵盖任意闭乘子的配对域。

本稿不排除预解式的有限线性组合、真正无穷乘积或其他依赖于有限元组的 $\mathfrak C$ 算子。也不把该 $f$ 当作目标慢符号的湮灭者：$f$ 已知循环，目标 $S$ 全空间稠密像，故它不能给非零秩一主理想湮灭泛函。反例严格针对所述自动正则化命题。

## 6. 可复用的抽象检测式

同一论证可简述为一个已经支付域的检测准则。若对一个 $f\in H$ 有实际测试 $G_p\in\mathfrak C$，满足
$$
|\langle G_pf,f\rangle|/a_p\to\infty,
$$
而某个有限闭词 $P$ 及有界 $R\in\mathfrak C$ 具有有界截断 $P_n$，使
$$
RP_nf\to f,\qquad P_nG_p1\to PG_p1
\quad\text{（每个固定 }p\text{）},
$$
并且 $\|PG_p1\|\le Ca_p$，则 $\phi_f(R\,\cdot)$ 不可能有固定真空表示。

本例取 $G_p=V_{J_p}$、$a_p=(2p+1)^{k/2}$。此准则不要求 $RP=I$ 在全空间成立，只要求明确列出的向量极限；但任何应用都必须重新验证这些域和极限。

