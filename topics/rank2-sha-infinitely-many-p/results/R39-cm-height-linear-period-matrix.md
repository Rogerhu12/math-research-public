# R39：固定 CM 高度矩阵的一阶 period 表示与四个高度的线性独立

**可信度：已证明。** 日期：2026-11-12。

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
P=(-1,4),\quad Q=(9,24).
$$
R4 给出 $P,Q$ 的有理独立性；复共轭因而给出它们在
$\operatorname{End}^0(E)=K$ 上的独立性。
目标 $p$、素位 $\mathfrak p$、单 $\mathfrak p$ 高度
$h_{\mathfrak p}$、$h^\pm$ 的规范均与
[R37](R37-cm-period-reciprocity-nonvanishing.md) 相同。

R37 已证明一个原始 universal-extension 行列式和一个反对称高度非零。
本结果进一步把**实际的全部 rank-two cyclotomic 高度条目**放入
同一个固定半阿贝尔群的线性对数矩阵。
这种有限点处的 CM 线性化不等于说任意局部群上的 canonical 高度微分
已经变成代数定义的单个 Lie 泛函。

## 1. 精确结论

记
$$
H=\begin{pmatrix}H_{PP}&H_{PQ}\\H_{PQ}&H_{QQ}\end{pmatrix},
\qquad H_{UV}=h^+(U,V),\qquad j=h^-([i]P,Q).
$$

**定理。** 对每一个目标 $p$，有
$$
\boxed{\quad H_{PP},\ H_{PQ},\ H_{QQ},\ j
\quad\text{在 }\overline{\mathbb Q}\text{ 上线性独立}.\quad}
\tag{1}
$$
这里代数系数通过固定的 $p$-adic 嵌入读入 $\mathbb C_p$。

更具体地，存在固定五维半阿贝尔群
$$
0\longrightarrow\mathbb G_m^4\longrightarrow J
\longrightarrow E\longrightarrow0
\tag{2}
$$
和两个代数 invariant differentials $\vartheta_P,\vartheta_Q$，
使四个数是矩阵
$$
M_p=
\begin{pmatrix}
\vartheta_P(\log b'_P)&\vartheta_P(\log b'_Q)\\
\vartheta_Q(\log b'_P)&\vartheta_Q(\log b'_Q)
\end{pmatrix}
=\frac12
\begin{pmatrix}
H_{PP}&H_{PQ}-ij\\
H_{PQ}+ij&H_{QQ}
\end{pmatrix}
\tag{3}
$$
的固定代数线性组合。
除固定有限多个 $p$ 外，$b'_P,b'_Q$ 也可一次选为固定代数点。
小素数处对数分支的修正已由 R37 的紧性引理处理，
所以 (1) 并不只对一个未知的余有限子集成立。

式 (1) **只是线性独立**。本结果不推出
$$
\det H\ne0,
\qquad \det H-j^2\ne0,
\qquad \boldsymbol\ell^t\operatorname{adj}(H)\boldsymbol\ell\ne0.
\tag{4}
$$
下文将这三项仍然存在的非线性条件写清楚。

## 2. 同一个固定广义 Jacobian

取
$$
\mathfrak m=(O)+(P)+(Q)+([i]P)+([i]Q),\qquad
J=J_{\mathfrak m}.
\tag{5}
$$
四个 torus 扩张类为 $P,Q,[i]P,[i]Q$。
它们在 $\mathbb Z$ 上独立，故
$$
\operatorname{Hom}(J,\mathbb G_m)=0.
\tag{6}
$$
半阿贝尔群到 $\mathbb G_a$ 也无非零同态。

由 (6)，任何两个代数提升 $z_P,z_Q\in J(\overline{\mathbb Q})$
只要分别投影到 $P,Q$，其代数群包就是 $J^2$。
证明为 R37 §3 的完整论证：群包恒等分支投射满 $E^2$；
否则产生非零 CM 关系。商群被 torus 核满射，因而 affine；
(6) 及无加法商迫使商群为零。
这一步不要求代数提升本身满足某种“泛性”。

令
$$
\omega=\frac{dx}{2y},\qquad
\eta_U=\frac{y+y(U)}{x-x(U)}\omega
\qquad(U=P,Q,[i]P,[i]Q).
\tag{7}
$$
它们分别有留数除子 $(U)-(O)$。
由广义 Abel–Jacobi 理论，$\omega,\eta_P,\eta_Q,\eta_{[i]P},\eta_{[i]Q}$
唯一提升为 $J$ 上的一组代数 invariant differentials
$$
\omega^{\rm inv},\theta_P,\theta_Q,\theta_{[i]P},\theta_{[i]Q}.
\tag{8}
$$
按留数选 torus 坐标，则每个 $\theta_U$ 在 torus 上是相应坐标的
$d\log$，而 $\omega^{\rm inv}$ 在 torus 上为零。

取 R37 的固定不交支集代表
$$
R=2P+2Q,\qquad B_P=(R+P)-(R),\quad B_Q=(R+Q)-(R).
\tag{9}
$$
原始提升为 $b_V=[B_V]_{\mathfrak m}$。
Coleman 积分和群对数的准确比较给
$$
I_{U,V,p}:=\int_{B_V}\eta_U
=\theta_U(\log b_V),
\qquad \int_{B_V}\omega=\ell_{V,p}.
\tag{10}
$$
这里使用的是 Besser (2004), Proposition 2.3、Corollary 2.4，
以及 Zarhin (1996), §3；完整出处和两套积分一致性的接口见 R37 §2.2。

## 3. 远处交数、单 π 字符和提升的实际选择

单 $\mathfrak p$ 的 idele class character 为
$$
\begin{aligned}
\chi_{\mathfrak p,\mathfrak p}(x)
&=\log_p\iota_\mathfrak p(x)
-v_\mathfrak p(x)\log_p\iota_\mathfrak p(\pi),\\
\chi_{\mathfrak p,\mathfrak q}(x)
&=-v_\mathfrak q(x)\log_p\iota_\mathfrak p(\alpha_\mathfrak q)
\quad(\mathfrak q\ne\mathfrak p),
\end{aligned}
\tag{11}
$$
其中 $\mathfrak p=(\pi)$，$\mathfrak q=(\alpha_\mathfrak q)$。
类数为 $1$ 和单位群为 $\mu_4$ 保证其在主 idèle 上为零。
在 $\mathfrak p$ 所用对数分支杀掉 $\pi$；
$\bar{\mathfrak p}$ 处未分歧，须用交数项。

对每个 $U,V$，记远离分歧位 $\mathfrak p$ 的总项为
$$
C_{U,V,p}=\sum_\mathfrak q
r_{U,V,\mathfrak q}\log_p\iota_\mathfrak p(\alpha_\mathfrak q),
\qquad r_{U,V,\mathfrak q}\in\mathbb Q.
\tag{12}
$$
系数是带符号的有理交数，只有有限项非零。
所有曲线和除子固定，故在固定有限素数集外，这些系数和生成元都固定。
这里没有把 $\mathfrak p$ 处的积分或未分歧的
$\bar{\mathfrak p}$ 处误放入不合用的分歧公式。

选择代数根，令
$$
u_{U,V,p}=\prod_\mathfrak q
\alpha_\mathfrak q^{r_{U,V,\mathfrak q}}.
$$
把 $b_V$ 加上 torus 点 $(u_{U,V,p})_U$ 得到 $b'_V$。
因为所有 $\mathfrak q\ne\mathfrak p$，这些生成元在
$\mathfrak p$ 处是单位；标准对数与 (11) 的分支在它们上相同。
代数根的选择只乘根单位，不改变对数。
于是
$$
\mathcal B_{U,V,p}:=I_{U,V,p}+C_{U,V,p}
=\theta_U(\log b'_V),
\qquad \operatorname{pr}(b'_V)=V.
\tag{13}
$$

若 $b'_V$ 不在标准对数的 $J(\mathbb C_p)_f$ 中，
R37 §3.1 给出一个共同正整数 $N$ 和 torus 中的代数 $\pi$-有理次幂，
使修正后的两点进入紧子群、投影为 $NP,NQ$，
并且对数恰为 $N\log b'_P,N\log b'_Q$。
因此 AST 可合法应用，且非零结论不受影响。
固定有限集外不必作这一修正，(13) 的两个代数点可一次固定。

## 4. CM 组合已经消去整个正规化项

设 $\beta$ 如 R37，为 $x\omega$ 的固定有理倍数。
在 $\mathfrak p$ 处 ordinary unit-root 补空间为 $\mathbb Q_p\beta$。
写
$$
\Psi_p(\eta_U)=a_{U,p}\omega+\ell_{U,p}\beta.
\tag{14}
$$
直接计算 $[i](x,y)=(-x,iy)$ 给
$$
[i]^*\eta_{[i]U}=\eta_U,
\quad [i]^*\omega=i\omega,
\quad [i]^*\beta=-i\beta.
$$
因此
$$
a_{[i]U,p}=-i a_{U,p},\qquad
\ell_{[i]U,p}=i\ell_{U,p}.
\tag{15}
$$

现在定义**代数**第三类形式的线性组合
$$
\alpha_U:=\eta_U-i\eta_{[i]U},\qquad U=P,Q.
\tag{16}
$$
虽然它的留数允许 $K$ 系数，积分及 $\Psi$ 均按局部域线性延拓；
也可将下一式逐项理解为两个整数留数微分等式的线性组合。
由 (14)–(15)，
$$
\Psi_p(\alpha_U)
=(a_{U,p}-i(-i a_{U,p}))\omega
+(\ell_{U,p}-i(i\ell_{U,p}))\beta
=2\ell_{U,p}\beta.
\tag{17}
$$
故 $\alpha_U$ 已经满足 ordinary 高度的正规化条件。
这里使用的是两个实际 CM 点的组合，
不是把一个未知的 $p$-adic 系数 $a_{U,p}$ 当成代数数。

令
$$
\vartheta_U=\theta_U-i\theta_{[i]U}\in\Omega^1_{\rm inv}(J/K).
\tag{18}
$$
高度定义和 (13)、(17) 给
$$
\boxed{
\vartheta_U(\log b'_V)
=h_{\mathfrak p}(U,V)-i h_{\mathfrak p}([i]U,V).
}
\tag{19}
$$
这已是实际 canonical 高度的准确表示，所有远处项也在 (13) 中。

## 5. 四个值的代数线性独立

$\vartheta_P,\vartheta_Q$ 是代数 Lie 线性形式，并且相互独立。
可仅在 torus 上验证：在坐标顺序
$P,Q,[i]P,[i]Q$ 下，它们的系数向量分别为
$$
(1,0,-i,0),\qquad (0,1,0,-i).
\tag{20}
$$
所以任意非平凡代数组合仍非零。

若矩阵 (3) 的四个条目有代数线性关系
$$
c_{11}M_{11}+c_{12}M_{12}+c_{21}M_{21}+c_{22}M_{22}=0,
$$
则 $(\log b'_P,\log b'_Q)$ 被如下 Lie 线性形式杀掉：
$$
L(z_1,z_2)=
(c_{11}\vartheta_P+c_{21}\vartheta_Q)(z_1)
+(c_{12}\vartheta_P+c_{22}\vartheta_Q)(z_2).
\tag{21}
$$
由 (20)，只要四个 $c_{ij}$ 不全为零，$L$ 就非零。
而 §2 的群包为全 $J^2$，§3 的紧性修正保留满群包及关系 (21)。
Fuchs–Pham Theorem 2.2 因而使 (21) 不可能为零。
故 $M_{11},M_{12},M_{21},M_{22}$ 在
$\overline{\mathbb Q}$ 上线性独立。

注意此处没有新增的四个列点，也没有忽略列之间的 CM 关系：
只使用两个 CM 独立的列 $P,Q$，四个行留数类则在 $\mathbb Z$ 上独立。
这正是能直接证明满群包的原因。

## 6. 识别为 cyclotomic 和 anticyclotomic 高度

由 CM 自同构和 unit-root 补空间稳定性，
$$
h_{\mathfrak p}([i]U,[i]V)=h_{\mathfrak p}(U,V).
$$
结合对称性得
$$
h_{\mathfrak p}([i]U,U)=0,
\qquad h_{\mathfrak p}([i]P,Q)=-h_{\mathfrak p}([i]Q,P).
\tag{22}
$$
令
$$
a=h_{\mathfrak p}(P,P),\quad b=h_{\mathfrak p}(P,Q),\quad
d=h_{\mathfrak p}(Q,Q),\quad c=h_{\mathfrak p}([i]P,Q).
$$
则 (19) 的矩阵准确为
$$
M_p=\begin{pmatrix}a&b-ic\\b+ic&d\end{pmatrix}.
\tag{23}
$$
在有理点上，复共轭给 $h^+=2h_{\mathfrak p}$，
而 $j=2c$，故得到 (3)。
反向换元为
$$
H_{PP}=2M_{11},\quad H_{QQ}=2M_{22},\quad
H_{PQ}=M_{12}+M_{21},\quad j=i(M_{12}-M_{21}).
\tag{24}
$$
它是可逆的代数线性换元，故 §5 证明了 (1)。

特别地，若 $u,v\in\overline{\mathbb Q}$ 不全为零，则
$$
u^2H_{PP}+2uvH_{PQ}+v^2H_{QQ}\ne0.
\tag{25}
$$
这说明高度的零方向若存在，其斜率不能是代数数；
并没有说明 $\mathbb Q_p$ 中不存在这样的方向。

## 7. 剩余问题准确变成哪些非线性 period 条件

与较早的 $3\times3$ 表示相比，(3) 把 cyclotomic 高度行列式降成
四个实际线性 period 的二次式：
$$
\det H
=4M_{11}M_{22}-(M_{12}+M_{21})^2.
\tag{26}
$$
单 $\mathfrak p$ 两个 CM 分量的矩阵行列式为
$$
\boxed{\quad \det H-j^2=4\det M_p.\quad}
\tag{27}
$$
所以文献中额外假设的 $\det H-j^2\ne0$
也没有被条目的线性独立自动证明。
一个线性独立的四元组仍可能满足 (26) 或 (27) 的二次关系。
R37 能处理的是通过互易式恰好降成**线性** period 的那个特定行列式，
不能对这里的新二次式再次直接套 AST。

最后令 $\boldsymbol\ell=(\ell_P,\ell_Q)^t$。
strict Mordell–Weil 向量 $\xi=\ell_QP-\ell_PQ$ 的自高度仍为
$$
\begin{aligned}
h^+(\xi,\xi)
&=H_{PP}\ell_Q^2-2H_{PQ}\ell_P\ell_Q+H_{QQ}\ell_P^2\\
&=2M_{11}\ell_Q^2
-2(M_{12}+M_{21})\ell_P\ell_Q+2M_{22}\ell_P^2.
\end{aligned}
\tag{28}
$$
这是线性 period 的三次式。
$\ell_Q/\ell_P$ 超越，已由 AST 和 $P,Q$ 的 CM 独立性证明；
故不能把 (25) 用于 (28)。

本结果提供的是固定半阿贝尔对象、四个实际高度的全部代数线性独立，
以及剩余 determinant 和 strict 条件的准确次数。
它没有排除 $V_p\Sha$ 所给的额外 Selmer 空间，
仍未闭合主课题的无穷素数有限性。

## 来源和与已存笔记的关系

- Fuchs–Pham，*The $p$-adic analytic subgroup theorem revisited*，
  2015，Theorem 2.2，
  [原文](https://arxiv.org/pdf/1502.00768)。
- Zarhin，*P-adic abelian integrals and commutative Lie groups*，
  1996，§3，
  [原文](https://arxiv.org/pdf/alg-geom/9603006)。
- Besser，*The $p$-adic height pairings of Coleman–Gross and of Nekovář*，
  2004，Proposition 2.3、Corollary 2.4，
  [原文](https://arxiv.org/pdf/math/0209006)。
- Coleman，*Vectorial extensions of Jacobians*，1990，§1–§2；
  Besser，*p-adic heights and Vologodsky integration*，Theorem 3.7；
  Lie–de Rham 的固定代数识别及相容性已在 R37 §2.3 写出。
- Bianchi–Kaya–Müller，*Algorithms for p-adic Heights on Hyperelliptic Curves
  of Arbitrary Reduction*，2024，§2，
  [原文](https://antsmath.org/ANTSXVI/papers/BianchiKayaMuller.pdf)，
  给出包括 $p$ 上方未分歧位在内的统一局部定义。

[固定 Poincaré 笔记](../notes/2026-11-12-poincare-fixed-period-matrices.md)
给出一般的 $H=\mathcal B-\mathbf a\boldsymbol\ell^t$。
它明确没有排除在指定有限代数点上的另一种线性化；
本结果正利用新增的 $[i]P,[i]Q$ 行实现了这种 CM 线性化。
