# Exceptional 的有限域算术：共同 Fourier 零点、实多项式与已排除的捷径

日期：2026-11-12。状态：**精确代数归约与方法核验；尚未证明 exceptional 集为空。** 本文不把有限计算推广到所有 $p$，不把 Maschke 半单性当成具体矩阵系数的非消失。

## 1. 固定的实际问题

设 $p>37$、$p\equiv2\pmod3$，取非平方 $z\in\mathbb F_p^\times$、$\tau^2=z$，并令 $\chi:\mathbb F_{p^2}^{\times}\to\mu_3$ 为一个阶三字符。写
$$B_j=\{b\in\mathbb F_p:\chi(1+b\tau)=\zeta_3^j\},
\qquad P_j(X)=\sum_{b\in B_j}X^b,\qquad 0\le j\le2.$$
指数采用 $0,\ldots,p-1$ 的代表。Studnia Definition 3.1.1 的理想是
$$I=(P_0(\zeta_p),P_1(\zeta_p),P_2(\zeta_p))
\subset\mathbb Z[\zeta_p].$$
实际 Tate 分母只需考察 $\ell\equiv\pm1\pmod p$。对这样的素数，$\ell>p+1$ 且 $\ell\nmid p(p^2-1)$，所以有限群平均合法；问题仍是三个具体和是否能在同一个素理想同时消失。

定义来源为 Studnia，[arXiv:2507.20801v2, §3.1](https://arxiv.org/html/2507.20801v2)。作者的 [论文状态页](https://pub.math.leidenuniv.nl/~studniae/publications.html) 在本次核查时将该文列为 submitted；本文只使用其显式定义及可独立检查的有限和，不把其未发表的全局结论当作输入。

下文均在 $\ell\ne2,3,p$ 进行；这个限制对实际 Tate 分母自动成立。

## 2. 颜色的精确对称和大小

$\chi$ 在 $\mathbb F_p^\times$ 平凡，因为 $3\nmid p-1$。又因 $\tau^2\in\mathbb F_p^\times$，$\chi(\tau)=1$。于是
$$\chi(1-b\tau)=\chi(1+b\tau)^{-1},\qquad
B_0=-B_0,\quad B_2=-B_1.\tag{2.1}$$

设 $U=\{u\in\mathbb F_{p^2}^{\times}:u^{p+1}=1\}$。Cayley 映射
$$b\longmapsto \frac{1-b\tau}{1+b\tau}$$
给 $\mathbb F_p\simeq U\setminus\{-1\}$；选取 $\chi$ 的一个取向后，
$$\chi(1+b\tau)
=\left(\frac{1-b\tau}{1+b\tau}\right)^{(p+1)/3}.$$
右边的三次根通过固定识别送到复三次根。$-1$ 位于立方类中，所以若 $m=(p+1)/3$，则
$$|B_0|=m-1,\qquad |B_1|=|B_2|=m.\tag{2.2}$$
此外
$$P_0+P_1+P_2=\Phi_p(X).\tag{2.3}$$
特别在 $X=1$，三个值为 $m-1,m,m$，永远不同时为零。这也直接证明 $p$ 不是 exceptional：$\mathbb Z[\zeta_p]$ 中唯一 $p$ 上方素理想将 $\zeta_p$ 送到 $1$。

## 3. 两个相反频率的精确等价

在特征 $\ell$ 的代数闭域中取阶恰为 $p$ 的 $\xi$、阶恰为 $3$ 的 $\omega$。对 $a\in\mathbb F_p^\times$ 定义
$$S(a)=\sum_{b\in\mathbb F_p}\omega^{j(b)}\xi^{ab},
\qquad j(b)=j\quad(b\in B_j).$$
由 (2.1)，
$$S(-a)=\sum_b\omega^{-j(b)}\xi^{ab}.$$
记 $u_j=P_j(\xi^a)$。则
$$\begin{aligned}
u_0+u_1+u_2&=0,\\
S(a)&=u_0+\omega u_1+\omega^2u_2,\\
S(-a)&=u_0+\omega^2u_1+\omega u_2.
\end{aligned}$$
三阶 Fourier 变换在 $\ell\ne3$ 时可逆，因此
$$\boxed{u_0=u_1=u_2=0
\quad\Longleftrightarrow\quad S(a)=S(-a)=0.}\tag{3.1}$$

要证明无 exceptional，必须为每个非零频率排除这一对同时为零，不能只引用某个较弱的单一 Fourier 结论。

## 4. 联合线性复杂度与反演对称给出的缺维

在 $\mathbb F_\ell[X]$ 中定义
$$G_{p,\ell}(X)=\gcd\bigl(\Phi_p,P_0,P_1,P_2\bigr)
=\gcd(\Phi_p,P_0,P_1).\tag{4.1}$$
由于 $\ell\ne p$，$\Phi_p$ 无重根。故
$$\ell\text{ exceptional for }p\quad\Longleftrightarrow\quad
\deg G_{p,\ell}>0.\tag{4.2}$$

将三条 $p$ 周期的 $0/1$ 指示序列同时考虑，最短共同线性递推的阶为
$$\boxed{\mathcal L_{p,\ell}=p-\deg G_{p,\ell}.}\tag{4.3}$$
证明可直接在 $\overline{\mathbb F}_\ell[C_p]$ 中对平移对角化：每个频率贡献一维，且只有三个 Fourier 系数都为零的频率才不出现在联合平移张成空间中。频率 $0$ 由 (2.2) 保证存在，故共同 gcd 不含 $X-1$。

由 (2.1)，$G_{p,\ell}$ 的根集在 $\xi\mapsto\xi^{-1}$ 下稳定。非平凡 $p$ 次根没有反演不动点，因此
$$\deg G_{p,\ell}\text{ 是偶数}.$$
从而一个真正可用的复杂度定理只要证明
$$\mathcal L_{p,\ell}\ge p-1$$
就足以排除 exceptional；但目前并没有得到这个界。

另有一个简单的无例外范围：若
$$\langle\ell,-1\rangle=\mathbb F_p^\times,$$
一个共同零点经过 Frobenius 与反演将给出全部非平凡 $p$ 次根，于是 $\Phi_p\mid P_j$，与 $P_j$ 的 $0/1$ 系数及非恒定性矛盾。所以该群生成条件排除 exceptional。它包含 $\ell$ 模 $p$ 为本原根的情形，却不包含本题的 $\ell\equiv\pm1\pmod p$：后者生成的群只有两个元素。

## 5. 实际分母对应三个整系数实多项式的共同根

令 $n=(p-1)/2$。定义 $C_0(T)=2,C_1(T)=T$、
$$C_{r+1}=TC_r-C_{r-1},$$
以及 $V_0(T)=1,V_1(T)=T$、
$$V_{r+1}=TV_r-V_{r-1}.$$
于是对 $T=\xi+\xi^{-1}$，
$$C_r(T)=\xi^r+\xi^{-r},\qquad
V_{r-1}(T)=\frac{\xi^r-\xi^{-r}}{\xi-\xi^{-1}}.$$

令
$$\begin{aligned}
A_p(T)&=1+\sum_{\substack{1\le b\le n\\b\in B_0}}C_b(T),\\
B_p(T)&=\sum_{b=1}^{n}
\bigl(\mathbf1_{b\in B_1}-\mathbf1_{b\in B_2}\bigr)V_{b-1}(T).
\end{aligned}\tag{5.1}$$
则
$$u_0=A_p(T),\qquad
u_1-u_2=(\xi-\xi^{-1})B_p(T).$$
令 $\Psi_p(T)$ 为 $\zeta_p+\zeta_p^{-1}$ 的最小多项式，亦即
$$\Phi_p(X)=X^n\Psi_p(X+X^{-1}).$$

当 $\ell\equiv\pm1\pmod p$ 时，$\Psi_p$ 在 $\mathbb F_\ell$ 完全分裂。由于 $\ell\ne2,p$，$\xi-\xi^{-1}\ne0$；结合 (2.3)，有精确等价
$$\boxed{\ell\text{ exceptional for }p
\Longleftrightarrow
\exists T\in\mathbb F_\ell:
\Psi_p(T)=A_p(T)=B_p(T)=0.}\tag{5.2}$$
这把所需排除转成显式共同根问题，不需要在 $\mathbb F_{\ell^2}$ 中运行三个指数和。一个足够但不必要的可核查整数证书是
$$\gcd\bigl(\operatorname{Res}(\Psi_p,A_p),
\operatorname{Res}(\Psi_p,B_p)\bigr)=1;$$
但本文没有证明这个证书对所有 $p$ 成立，也没有将它当作已经求出的统一公式。

也不能直接把 $\Psi_p$ 从问题中删掉，声称 $A_p,B_p$ 在所有素于群阶的特征均无共同根。用 §7 的 $p=41,z=3$ 颜色，(5.1) 给次数分别为 $20,18$ 的两个整多项式，精确 resultant 为
$$\operatorname{Res}(A_{41},B_{41})=44315068748179.$$
这个素数不整除 $41(41^2-1)$，且模 $41$ 为 $18$。因此二元 Bézout 常数只含群阶素因子的更强路线不成立；本题仍须保留 $\Psi_p$ 和 $\ell\equiv\pm1\pmod p$ 的限制。该计算仅否证这个捷径，没有给出 exceptional 素数。

## 6. 实圆分域中的内容条件

回到特征零，令
$$\mathcal R=\mathbb Q(\zeta_{3p})^+,
\qquad \mathcal R_0=\mathbb Q(\zeta_p)^+,
\qquad W=S(1).$$
由 (2.1)，复共轭固定 $W$，所以 $W\in\mathcal O_{\mathcal R}$。$\mathcal R/\mathcal R_0$ 的非平凡自同构 $\sigma$ 满足 $\sigma(W)=S(-1)$。直接相乘得
$$\operatorname{Tr}_{\mathcal R/\mathcal R_0}(W)=3u_0,
\qquad
N_{\mathcal R/\mathcal R_0}(W)=3(u_0^2-u_1u_2).\tag{6.1}$$

若 $\ell\equiv\pm1\pmod p$，则 $\ell$ 在 $\mathcal R_0$ 完全分裂。对 $\ell\ne3,p$，共同消失等价于某个 $\mathfrak q\mid\ell$ 同时使 $W$ 和 $\sigma(W)$ 的剩余值为零，即
$$W\in\mathfrak q\mathcal O_{\mathcal R}.$$
这里若 $\mathfrak q$ 分裂，要求其上方两支都整除 $W$；若惰性，则唯一一支整除 $W$。由于扩张在 $\ell$ 不分歧，两种情形都给
$$\boxed{\ell^2\mid N_{\mathcal R/\mathbb Q}(W).}\tag{6.2}$$
因此该整数在 $\ell$ 处平方自由即可排除该 $\ell$。反向不成立：范数的平方因子可能来自同一个素理想的高赋值，或来自不同的 $\mathfrak q$，不一定表示相同基素理想的内容。

若把 $\ell\bmod p$ 和 $\ell\bmod3$ 各写成 $\pm1$，两符号相同则 $\mathfrak q$ 在 $\mathcal R/\mathcal R_0$ 分裂，符号不同则惰性。这只是 Frobenius 在
$$(\mathbb Z/p\mathbb Z)^\times\times(\mathbb Z/3\mathbb Z)^\times/
\langle(-1,-1)\rangle$$
中的直接计算。它没有自动排除任一种情况。

## 7. 精确反例：半单性不保证单个颜色和为单位

取
$$p=41,\qquad z=3,\qquad \ell=19433\equiv-1\pmod{123}.$$
$19433$ 为素数，$3$ 是其二次非剩余。对某个三次字符取向，三个颜色为
$$\begin{aligned}
B_0={}&\{0,1,4,13,14,17,20,21,24,27,28,37,40\},\\
B_1={}&\{2,6,7,8,9,12,15,16,18,19,30,31,36,38\},\\
B_2={}&\{3,5,10,11,22,23,25,26,29,32,33,34,35,39\}.
\end{aligned}$$
在 $\mathbb F_{19433}[s]/(s^2-3)$ 中，令
$$\xi=10669+4716s.$$
直接模乘法给 $\xi^{41}=1$、$\xi\ne1$，且
$$P_0(\xi)=0,\qquad
P_1(\xi)=11182s,\qquad
P_2(\xi)=8251s=-11182s.\tag{7.1}$$
这不是 exceptional 反例；它反驳的是“在所需同余类且群阶可逆时，每一个颜色和都不消失”的过强捷径。此处 $\xi+\xi^{-1}=1905$，相应实多项式值为
$$A_{41}(1905)=0,\qquad B_{41}(1905)=2961\ne0\pmod{19433}.$$

下面的纯整数代码可重算 (7.1)，没有数值精度假设。

~~~python
def mul(a, b, ell):
    return ((a[0]*b[0] + 3*a[1]*b[1]) % ell,
            (a[0]*b[1] + a[1]*b[0]) % ell)

def power(a, k, ell):
    r = (1, 0)
    while k:
        if k & 1:
            r = mul(r, a, ell)
        a = mul(a, a, ell)
        k //= 2
    return r

B0 = [0,1,4,13,14,17,20,21,24,27,28,37,40]
B1 = [2,6,7,8,9,12,15,16,18,19,30,31,36,38]
B2 = sorted(set(range(41)) - set(B0) - set(B1))
ell, xi = 19433, (10669, 4716)
assert power(xi, 41, ell) == (1, 0) and xi != (1, 0)
values = []
for cell in [B0, B1, B2]:
    terms = [power(xi, b, ell) for b in cell]
    values.append(tuple(sum(t[j] for t in terms) % ell for j in [0, 1]))
assert values == [(0, 0), (0, 11182), (0, 8251)]
~~~

## 8. 纯 Gauss 和与现有 SLCE 定理的准确边界

这里确实有一个简单的纯 Gauss 和。取 $\psi(x)=\zeta_p^x$，则
$$G(\chi)=\sum_{x\in\mathbb F_{p^2}}\chi(x)\psi(\operatorname{Tr}x)=p.$$
可直接证明：迹零直线上非零元素为 $a\tau$，其字符均为 $1$，贡献 $p-1$。每条非零迹直线的无扭加权和相同；所有字符和为零使该和为 $-1$。再用 $\sum_{a\ne0}\psi(a)=-1$，便得 $G(\chi)=p$。

但 $S(a)$ 在迹固定的直线上还有一个非恒定加法权重，不是这个完整二维 Gauss 和。将迹条件展开再使用 $G(\chi)=p$，只返回
$$S(a)=S_{\chi^{-1}}(-a),$$
即 (2.1) 已有的对称；没有得到 $S(a)S(-a)$ 是 $p$ 的幂或一个单位。

已核查的最接近原始文献接口如下。

- Ş. Alaca、G. Millar，*Character values of the Sidelnikov–Lempel–Cohn–Eastman sequences*，Cryptography and Communications **9** (2017), 665–682，DOI [10.1007/s12095-016-0208-3](https://doi.org/10.1007/s12095-016-0208-3)，[作者稿](https://arxiv.org/pdf/1602.05888)：Theorem 3.1 把他们的二元、乘法指数、周期 $q-1$ 序列的某个因子判定写成 Jacobi 和的同余。其因子条件发生在特征 $2$，不能把本文的加法指数 $b$ 和特征 $\ell$ 直接替换进去。纯和 $K(\chi)=p$ 也不是本文的 $S(a)$。
- U. K. Anandavardhanan、A. Jana，*Orthogonality of invariant vectors*，J. Algebra **604** (2022), 496–532，DOI [10.1016/j.jalgebra.2022.03.037](https://doi.org/10.1016/j.jalgebra.2022.03.037)，[作者稿](https://arxiv.org/pdf/2106.01929)：Theorem 1.1 控制 split-torus 与 non-split-torus 的不变向量相关系数，所用模约化是群定义特征 $p$。本文需在不同特征 $\ell$ 控制非平凡 $U$-特征线与 $C^3$ 的二维不变空间；两对空间与模特征都不同，故该定理不给 (3.1) 的排除。

没有找到适用于本文准确参数、能给 $\mathcal L_{p,\ell}\ge p-1$ 或 (5.2) 无共同根的已发表定理。以上不是对所有文献“不存在结果”的断言；它记录了已检查的具体接口为何不足。

## 9. 留给后续的准确目标

需要的有限域输入现在可以等价写成 (3.1)、(4.3) 或 (5.2) 的排除。实多项式版本将 $\ell\equiv\pm1\pmod p$ 的剩余次数限制完全吸收，(6.2) 给一个可检查的范数必要条件，但二者尚未变成所有 $p$ 的统一证明。

本笔记初写时，接到 R69 实际秩零商的 Hecke 因子整格及尖点微分仍未处理；后续 [R72](../results/R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md) 已通过最优商、Raynaud–Mazur 饱和及全部尖点除子独立补齐该接口。此处有限域共同非零仍是准确的剩余输入。忘线 Gram 标量 $(p^2-1)/2$ 和群平均分母在 $\ell$ 可逆，本身仍不能代替 R72 的证明或消掉任意 Hecke 幂等元的分母。

本文保留作者无 exceptional 的猜想为猜想，不把该猜想、已知有限范围或“半单”改写成无条件整性。
