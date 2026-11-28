# 原 Walsh 循环块全部平方根分支的同源 Sylvester 发散

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

依赖 [原 Walsh 全块表示](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md) 的全部实际定义。本附录将其中主根的线性结论推广到每个有限循环块的所有平方根分支；没有对分支作枚举或数值筛查。

## 1. 任意分支的每个 Fourier 系数都付有统一下界

在第 $m$ 块，令 $N=2^m$，原 $D_m$ 满足 $D_m^N=-p_mI$、$p_m=r_m^N>0$，且具有 $N$ 个互异特征值。任意矩阵平方根 $R_m^2=D_m$ 自动与 $D_m$ 交换，故唯一写成

$$
R_m=\sum_{\ell=0}^{N-1}a_{\ell,N}\,r_m^{1/2-\ell}D_m^\ell.
\tag{1.1}
$$

取 $\zeta=e^{\pi i/(2N)}$。在特征值 $r_m\zeta^{2(2j+1)}$ 上，平方根值为
$\sqrt{r_m}\,\varepsilon_j\zeta^{2j+1}$，$\varepsilon_j\in\{-1,1\}$。因此

$$
a_{\ell,N}
=\frac{\zeta^{1-2\ell}}{N}
P_\varepsilon\!\left(\zeta^{2(1-2\ell)}\right),
\qquad
P_\varepsilon(t)=\sum_{j=0}^{N-1}\varepsilon_jt^j.
\tag{1.2}
$$

因 $N$ 是 $2$ 的幂，$\zeta^{2(1-2\ell)}$ 是 primitive $2N$ 次单位根，其最小多项式为 $t^N+1$。$P_\varepsilon$ 次数小于 $N$ 且非零，故 (1.2) 从不为零。

其代数范数是非零整数；全部 $N$ 个共轭的绝对值都不超过 $N$。于是

$$
\boxed{\quad N^{-N}\le |a_{\ell,N}|\le1
\qquad(0\le\ell<N).\quad}
\tag{1.3}
$$

这一下界与任意 $2^N$ 种符号选择无关。$N=1$ 同样成立。

## 2. 全部分支仍有真正闭稳定块根和双侧迹类来源

任取每块的一个平方根，并在常数块取 $\pm\sqrt{\mu_0}$，组成与前文相同实际平方和定义域的直和 $R$。前文 (4.2)–(4.3) 的闭性、稳定性和 $R^2=D$ 证明逐字适用。

在平衡坐标中每个分支都是 $\sqrt{r_m}$ 乘一个酉矩阵，所以

$$
\|R_m\|\le r_m^{3/2}/\mu_m
$$

仍与分支无关。故原 $K=C-D$ 仍满足

$$
KH\subset\mathcal D(R),\qquad
RK\in\mathfrak S_1,\qquad
KR|_{\mathcal D(R)}\text{ 有全域迹类延拓},
\tag{2.1}
$$

并保留前文 (4.7) 的共同上界。

所有这样的直和根都无界：真实末/首矩阵元满足

$$
|\langle R_mu_m,v_m\rangle|
=|a_{N-1,N}|\frac{r_m^{3/2}}{\mu_m}
\ge N^{-N}\frac{r_m^{3/2}}{\mu_m}\longrightarrow\infty,
\tag{2.2}
$$

因为 $N\log N=O(m2^m)$，而前文 (3.3) 给右端对数的正主项为 $(280/3)16^{m_0}16^m$。

## 3. 对所有分支，原相邻 carry 的线性修正都无界

仍取 $n\ge2$、$N=2^n$、$m=n+1$、$M=2N$，并置
$\rho=r_m/r_n$、$q=\rho^N$。实际原均值给

$$
q^2=\frac{p_m}{p_n^2}
=\frac{a_n\mu_{n+1}}{\mu_n^2}
=1-\left(\frac{\delta_n}{\mu_n}\right)^2\in(0,1),
\tag{3.1}
$$

以及准确的尺度

$$
-\log q=700\,16^{m_0}16^n+O_{m_0}(8^n).
\tag{3.2}
$$

尤其 $r_m<r_n$。两块平方根的特征值模分别为 $\sqrt{r_m}$ 和 $\sqrt{r_n}$，故无论怎样选符号，$R_mX+XR_n=K_{mn}$ 的有限 Sylvester 解总是唯一；这里不再需要主根的开右半平面性质。

记本次任意分支系数
$c_j^{(s)}=a_{j,2^s}r_s^{1/2-j}$。前文完整望远镜仅用了平方关系，故同一个实际极端元仍为

$$
x_n=
\frac{(\delta_m/\sqrt2)\beta_m\beta_n}{p_m+p_n^2}
\left(c_{N-1}^{(n)}-c_{N-1}^{(m)}
+p_n c_{M-1}^{(m)}\right).
\tag{3.3}
$$

令最后一项为主项。由 (1.3)，其余两项与它的绝对值比之和不超过

$$
M^M\left(q+\rho^{M-3/2}\right)\le 2M^M q.
\tag{3.4}
$$

这里 $M-3/2\ge N$，而 $\rho<1$。由 (3.2)，$2M^Mq\to0$，且该收敛完全不依赖本次任意分支。对充分大的 $n$，三项式的绝对值至少为最后一项的一半；$\delta_m/\mu_m\ge1/2$，$1+q^2\le2$，因此

$$
\boxed{\quad
|x_n|\ge
\frac1{8\sqrt2}\,
M^{-M}\frac{r_{n+1}^{3/2}}{\mu_n}
\longrightarrow\infty.
\quad}
\tag{3.5}
$$

最后极限来自

$$
\log\!\left(M^{-M}\frac{r_{n+1}^{3/2}}{\mu_n}\right)
=
\frac{280}{3}16^{m_0}16^n
-O_{m_0}(8^n+n2^n)\longrightarrow+\infty.
$$

于是对任何整套循环块根分支，原方程 $RX+XR=K$ 的形式有限块解已经没有有界拼接。该结论对所有分支统一成立，不只是未找到一个方便的分支。

## 4. 原范围

已付 (2.1) 是原实际 carry 的正向定义域结论。已否定的是以任一块对角根为基点、对同一 $K$ 求有界线性 Sylvester 修正。

完整非线性式 $RX+XR+X^2=K$ 的额外同源抵消、改换块分解、非块对角闭域或任意实际旗商上的闭稳定根，都没有被 (3.5) 排除。本附录不以线性化失败代替原根问题或普通 ISP 的结论。
