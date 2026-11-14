# R111：族 II 立方分母的唯一参考，由五阶点域的完整局部迹确定

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明，含从零重算的精确有限证书。** 在 R106 的实际族 II 中，三阶点域给出的共同好约化条件留下两个参考扭曲。本文改用一个五阶点域中剩余域为 $\mathbb F_2$ 的分支，计算整个分解群的一个非零迹，将参考唯一确定。结果不排除尚存的全局参数，也不将局部必要条件当作全局同构的充分条件。

## 1. 实际输入与结论

沿用 [R106](R106-cube-family-II-level1536-and-dyadic-exclusion.md) 的全部实际假设：
$$
p>37,\quad p\equiv3\pmod4,\quad a,b>0\text{ 奇},\quad
(a,b)=1,\quad3\nmid a,
$$
$$
h=(a^2-3b^2)/2,\qquad a^4-3h^2=-2Y^p,
\qquad |Y|>1,\quad(Y,6p)=1.
\tag{111.1}
$$
令
$$
K=\mathbb Q(r),\quad r^2=3,\quad
B(a,h):y^2=x^3+4ax^2+2(a^2+rh)x,
$$
$$
B_1:y^2=x^3+4x^2+2(1-r)x.
$$
它们来自 R19 的族 II、$Z=Y^3$，并满足 R106 的原始曲线与 $A:y^2=x^3-x$ 的实际模 $p$ 同构条件。两个 $W$ 符号均包括。R106 已证明
$$
Y\equiv1\pmod8,\qquad a^2\equiv b^2\pmod{16},
\tag{111.2}
$$
以及
$$
B(a,h)[p]\simeq B_1^{(d)}[p]\quad(G_K),\qquad
d\in\{\eta,-2\eta\},\qquad \eta=\left(\frac a3\right).
\tag{111.3}
$$
二次扭曲约定仍为
$[0,A,0,C,0]^{(d)}=[0,dA,0,d^2C,0]$。

**定理 111.1。** 每个实际 (111.1)–(111.3) 中的 $d$ 唯一，并满足
$$
\boxed{d=\left(\frac a3\right)(-2)^e,
\qquad e\in\{0,1\},\qquad
(-1)^e=\left(\frac6a\right).}
\tag{111.4}
$$
这里右端是对正奇数 $a$ 的 Jacobi 符号；$3\nmid a$。显式表为

| $a\bmod24$ | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 唯一 $d$ | 1 | $-1$ | $-2$ | 2 | $-2$ | 2 | 1 | $-1$ |

因而 R106 的两候选归约已经闭合成唯一参考。本表的每一列仍有一个参考；它本身不是删除某列参数的结果。

## 2. 奇有理单位在 $K_{\mathfrak p_2}$ 上的扭曲

写 $k=\mathbb Q_2(\sqrt3)$。有理奇单位的 $\mathbb Q_2$ 平方类由其模 $8$ 决定。在 $k$ 上，$3$ 已是平方。因此
$$
v\in\mathbb Z_2^\times:\qquad
v\equiv1,3\pmod8\Longrightarrow v\in k^{\times2},
$$
$$
v\equiv5,7\pmod8\Longrightarrow
k(\sqrt v)/k\text{ 是非平凡的未分歧二次扩张}.
\tag{111.5}
$$
第二行使用 $\mathbb Q_2(\sqrt5)/\mathbb Q_2$ 未分歧，而 $k/\mathbb Q_2$ 全分歧；两者线性不交。特别地，$-1\equiv7\pmod8$ 在 $k$ 上给出非平凡未分歧角色。

对正奇 $a$，其二次角色在算术 Frobenius 上的值为
$$
\chi_a(\operatorname{Frob}_k)=
\begin{cases}1&a\equiv1,3\pmod8,\\-1&a\equiv5,7\pmod8\end{cases}
=\left(\frac{-2}{a}\right).
\tag{111.6}
$$
这一步没有把所有奇单位说成平方：非平凡未分歧扭曲恰是本文所需区分的部分。

置
$$
H=h/a^2=\frac{1-3(b/a)^2}{2}.
$$
由 (111.2) 得 $H\equiv-1\pmod8$。依照上述扭曲约定，有定义方程层面的精确恒等关系
$$
B(a,h)=B(1,H)^{(a)}.
\tag{111.7}
$$
故只要算出 $B(1,H)$ 的完整局部迹，乘 (111.6) 即得到实际 $B(a,h)$ 的迹。

## 3. 五阶点域及精确的局部分支

令 $\psi_5$ 为 $B_1$ 的五阶除法多项式，首项为 $5X^{12}$。令
$$
P_5(Z)=5^{11}\psi_5(Z/5)\in\mathcal O_K[Z].
$$
它是首一十二次多项式。取根 $z$，记
$$
H_5=K(z),\qquad x_5=z/5,\qquad
f_5=x_5^3+4x_5^2+2(1-r)x_5,
$$
$$
L_5=H_5(w),\qquad w^2=625f_5.
\tag{111.8}
$$
于是 $P=(x_5,w/25)$ 是 $B_1$ 上的五阶点。程序在带嵌入的精确数域中验证 $P$ 在曲线上、$y(P)\ne0$ 和 $[5]P=O$；并验证两个定义多项式均不可约。

实际计算结果为
$$
[H_5:\mathbb Q]=24,\qquad
\operatorname{disc}(H_5)=2^{66}3^{12}5^{22},
$$
$$
[L_5:\mathbb Q]=48,\qquad
\operatorname{disc}(L_5)=2^{174}3^{24}5^{46}.
\tag{111.9}
$$
在 $2$ 处的全部绝对 $(e,f)$ 分解为

| 域 | 全部 $(e,f)$ |
|---|---|
| $H_5$ | $(8,1),(8,2)$ |
| $L_5$ | $(16,1),(16,2)$ |

取 $L_5$ 中唯一剩余次数为 $1$ 的素理想 $\mathfrak P$，令
$$
\mathscr L=(L_5)_{\mathfrak P}.
$$
它包含已指定嵌入的 $k$，且
$$
e(\mathscr L/k)=8,\qquad f(\mathscr L/k)=1,
\qquad\kappa(\mathscr L)=\mathbb F_2.
\tag{111.10}
$$
没有从全局次数 $48$ 直接假定局部次数；表格逐个分解了 $2$ 以上的素理想。

在同一个 $\mathfrak P$ 上，精确局部平方检验为
$$
\begin{array}{c|rrrr}
v&2&-2&-1&5\\\hline
v\in\mathscr L^{\times2}&1&0&0&0
\end{array}
\tag{111.11}
$$
因此 $B_1^{(2)}$ 与 $B_1$ 在 $\mathscr L$ 上同构，而 $-1$ 的扭曲在 $\mathscr L$ 上仍是非平凡的未分歧扭曲：后者也直接由 (111.5) 和剩余次数 $1$ 得到。

证书的局部平方检验使用 `nfislocalpower`；它判定的是完成域中的精确平方性。没有把有限精度的近似根当作平方，也没有将局部平方误写成 $L_5$ 内的全局平方。

## 4. 所有允许 $H$ 在同一域上的好约化及迹

以 $v_{\mathscr L}(2)=16$ 归一化赋值。两个模 $16$ 代表 $H_*=-1,7$ 的 Tate 最小模型计算为

| $H_*$ | 导子指数 | $v(\Delta_{\min})$ | $(v(U),v(R),v(S),v(T))$ | $(v(a'_1),v(a'_2),v(a'_3),v(a'_4),v(a'_6))$ | $a_{\mathbb F_2}$ |
|---:|---:|---:|---|---|---:|
| $-1$ | 0 | 0 | $(14,12,6,26)$ | $(8,0,0,1,1)$ | $-2$ |
| 7 | 0 | 0 | $(14,12,6,26)$ | $(8,0,0,1,1)$ | $-2$ |

因为剩余域是 $\mathbb F_2$，表中各单位都约化为 $1$。两行的约化方程均为
$$
\widetilde B:y^2+y=x^3+x^2.
\tag{111.12}
$$
当 $x=0,1$ 时右边都为 $0$，分别有两个 $y$，再加无穷远点；故 $\#\widetilde B(\mathbb F_2)=5$，迹等于 $3-5=-2$。程序同时独立调用好最小模型的 `ellap` 作交叉核验。

这也与 $\mathscr L$ 上非零五阶点在好约化后仍有五阶相容。这里好约化首先由最小模型证明，未反过来仅由点的存在假定好约化。

现在令 $H=H_*+16t$，$t\in\mathbb Z_2$。原始模型只改变
$$
a_4\text{，改变量 }\eta=2r(H-H_*),\qquad v(\eta)\ge80.
$$
使用代表行的**同一个**换元 $[U,R,S,T]$，变化量为
$$
\delta a'_4=\eta/U^4,\qquad
\delta a'_6=R\eta/U^6.
$$
两者赋值分别至少为
$$
80-4\cdot14=24,\qquad
80+12-6\cdot14=8.
\tag{111.13}
$$
其余系数不变。因此新模型整且保持逐项相同的约化 (111.12)。它的判别式仍是单位；也可由 $H$ 为奇数时 $v_k(1\pm rH)=1$ 核出原始判别式赋值恒为 $168$，同一 $U^{12}$ 正好除去全部赋值。

由此得到完整的、无参数大小限制的结论
$$
\boxed{H\equiv-1\pmod8
\Longrightarrow B(1,H)/\mathscr L\text{ 好约化，且 }a_{\mathscr L}(B(1,H))=-2.}
\tag{111.14}
$$
这不是将两次样本计算外推到无穷参数；(111.13) 给出两类内部的严格稳定界。

## 5. 比较模 $p$ 表示的完整 Frobenius 迹

由 (111.7)、(111.6)、$f(\mathscr L/k)=1$ 及 (111.14)，实际曲线在 $\mathscr L$ 上好约化，且
$$
a_{\mathscr L}(B(a,h))=-2\left(\frac{-2}{a}\right).
\tag{111.15}
$$
另一方面，在 $\mathscr L$ 上，$2$ 已是平方，$-1$ 给非平凡未分歧二次角色。所以对 $d\in\{1,-1,2,-2\}$，
$$
a_{\mathscr L}(B_1^{(d)})=-2\,\operatorname{sgn}(d).
\tag{111.16}
$$
将实际的 (111.3) 限制到 $G_{\mathscr L}$，得到这两个整数迹模 $p$ 同余。它们均属于 $\{2,-2\}$；$p>37$，故同余必为整数相等。因此
$$
\operatorname{sgn}(d)=\left(\frac{-2}{a}\right).
\tag{111.17}
$$
此处使用的是剩余特征 $2\ne p$ 的好约化 Frobenius，不涉及在特征 $p$ 处未经证明的迹同余。

R106 已从 $\mathfrak p_3$ 的好约化迹给出
$d\equiv a\pmod3$，即 $d=\eta(-2)^e$。将其代入 (111.17)，得
$$
(-1)^e=\eta\left(\frac{-2}{a}\right).
$$
对正奇数 $a$，二次互反律给
$\eta=(a/3)=(-3/a)$，所以右端为 $(6/a)$，即 (111.4)。定理得证。

这里完整比较了一个非零的分解群迹。仅知道两条曲线在同一域上好约化，不能推出 (111.17)；R106 使用的三阶点域中相应好约化迹为 $0$，正是它保留两个候选的原因。

## 6. 证书、复验及全局边界

- [标准库 Python 与内嵌 GP 程序](../notes/verify_r111_cube_ii_unique_twist.py)。
- [精确证书](../notes/r111_cube_ii_unique_twist_certificate.json)。

~~~sh
python3 -B topics/serre-uniformity/notes/verify_r111_cube_ii_unique_twist.py \
  --gp /tmp/pari-2.19.0/gp --check
~~~

`--write` 从除法多项式开始重新构造带嵌入数域；`--residue-table-only` 仅用 Python 标准库重算最后的八列符号。程序不依赖预先保存的大型数域对象，证书只保存定义多项式、判别式、素理想分解、局部平方判定和两个最小模型的估值及迹。域计算不调用类群算法，亦不使用 GRH。

所用接口及含义由 [PARI 官方数域文档](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html) 的 `nfislocalpower`、`idealprimedec`、`nfinit`，及[官方椭圆曲线文档](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html) 的 `elldivpol`、`elllocalred`、`ellap` 给出。无界参数的延伸由 (111.13) 自含证明。

结合 R103、R108，立方分母四次参数化的所有未排除分支现在都有由参数准确指定的单一非 CM 参考。仍需排除实际 $|Y|>1$ 的全局模 $p$ 同构；对这个困难，本文没有给出统一解。R106 的平凡 $Y=1$、$a=b=1$ 点在本表中对应 $d=1$，仍解释同一种奇素数有限筛为何必有参考点存活。对非立方 $Z$ 的完整高指标方程，本结果也未作额外结论。
