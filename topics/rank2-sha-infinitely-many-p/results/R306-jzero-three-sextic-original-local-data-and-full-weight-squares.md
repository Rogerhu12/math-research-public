# R306：三条原 sextic source 的共同局部数据与全权实平方

日期：2026-11-13。**状态：三条实际 Hecke 角色、共同 Hermitian 类、原 Schwartz 向量及其范数、全部合法权的完整 Yang 平方常数和 CM13 相位均已证明。本文不将非零中央质量替换成未知的中央导数。**

本篇把 R290 的实际来源扩展到同一个固定三元组
$$
\mathcal E_k:y^2=x^3+17^k,\qquad k\in\{1,3,5\}.
\tag{1}
$$
即 $D=17,4913,1419857$。仍固定
$$
K=\mathbb Q(\delta),\quad\delta=\sqrt{-3}=1+2\omega,
\quad\omega=e^{2\pi i/3},\quad\operatorname{Im}\delta>0,
$$
以及 R290 的 Yang 极化 $X=\mathbb Q\delta$ 和加性角色。三条来源从一开始共用 $\alpha=17$；不会先取不同 Gaussian 再隐含地识别它们。

## 1. 实际六次扭曲角色与两个小坏位

记 $\psi_k$ 为 (1) 的解析微分 CM type Hecke 角色，$\psi_0$ 为 $y^2=x^3+1$ 的基角色，并置 $\chi_k=\psi_k|\cdot|_K^{-1/2}$。Silverman–Stange 的已发表六次剩余公式给
$$
\psi_k(\mathfrak p)
=-\left(\frac{4\cdot17^k}{\mathfrak p}\right)_6^{-1}\pi,
\quad\pi\equiv2\pmod3,\qquad
\frac{\psi_k}{\psi_0}
=\left(\frac{17}{\cdot}\right)_6^{-k}.
\tag{2}
$$
这里负幂是理想角色的方向；主 idèle 的本地单位分量取其逆，和 R290 完全一致。

在 $2$ 处，$17\equiv1\pmod8$ 是 $\mathbb Q_2$ 的平方；单位群上的三次幂是自同构，故 $17$ 是六次幂。因此所有三条曲线的二处分量和基角色相同。

在 $3$ 处，$-17\equiv1\pmod9$，而三次幂将 $1+3\mathbb Z_3$ 同构到 $1+9\mathbb Z_3$，故 $17$ 是 $\mathbb Q_3$ 的三次幂。它的平方根给未分歧二次扩张，因为 $17\equiv-1\pmod3$。在 $K_3$ 上仍是未分歧二次扩张。所以 (2) 的三处扭曲恰是未分歧二次角色的 $k$ 次幂；三个 $k$ 都为奇数，得到同一个角色。特别，不能把它换成 R302 基参考的 $+i$ uniformizer 值。

原坏点表格准确为

| 地方 | 单位上的 $\chi_{k,v}$ | 指定 uniformizer 的值 |
|---|---|---|
| $2$ | $\operatorname{Teich}_{\mu_3}(u\bmod2)$ | $\chi_{k,2}(2)=-1$ |
| $3$ | $u\bmod\delta\in\{\pm1\}$ | $\chi_{k,3}(\delta)=-i$ |
| $17$ | $(u\bmod17)^{48k}\in\mu_6$ | $\chi_{k,17}(17)=-1$ |

十七处的 uniformizer 值也可由主 idèle $17$ 的积关系直接算出：二处为一，三处单位值为 $-1$，无穷处为一，故十七处必须为 $-1$。三个十七处单位角色均非平凡，故都具有 conductor 一。于是
$$
\mathfrak f_{\psi_k}=(2\delta\cdot17),\qquad
\operatorname N\mathfrak f_{\psi_k}=3468,\qquad
N_{\mathcal E_k}=10404.
\tag{3}
$$

在 R290 同一个 $\omega\bmod\mathfrak p=2$ 的范数七素理想上，(2) 给 $a_7(\mathcal E_1),a_7(\mathcal E_3),a_7(\mathcal E_5)=(-5,4,1)$；证书同时用原三条方程计点核定此方向。它不是按目标素数扫描出的推断。

## 2. 三条曲线具有同一个原 Hermitian 类

Yang 的条件仍是
$$
\epsilon\left(\tfrac12,\chi_{k,v},\tfrac12\psi_{K,v}\right)
\chi_{k,v}(\delta)
=\epsilon_{K_v/\mathbb Q_v}(\alpha).
\tag{4}
$$
二、三处角色已相同，所以 R290 的完整 Gauss 计算原样适用，左边分别为 $+1,-1$。以下直接支付十七处，而不只引用角色阶。

在 $\mathbb F_{289}=\mathbb F_{17}[\delta]$ 中令 $\vartheta_k(z)=z^{48k}$。它在 $\mathbb F_{17}^\times$ 上平凡，在 $\delta$ 上为 $-1$，且在 $\mathbb F_{289}^\times$ 上非平凡。写 $z=x+y\delta$。零 trace 纤维的和为
$$
\sum_{y\ne0}\vartheta_k(y\delta)^{-1}=-16.
$$
每个非零 $x$ 纤维的和相同；全部非零元素的角色和为零，故每个这样的纤维准确为一。对 R290 的同一负有限加性角色，有
$$
\sum_{z\ne0}\vartheta_k(z)^{-1}
e^{-2\pi i\operatorname{Tr}(z)/(2\cdot17)}=-17.
\tag{5}
$$
Tate 的本地式中 $\chi_{k,17}(17)=-1$，所以 epsilon 因子为 $+1$，再乘 $\chi_{k,17}(\delta)=-1$ 得 (4) 左边为 $-1$。无穷处仍为 $+1$，其余有限点为 $+1$。

因此与 R290 相同的
$$
\boxed{\alpha=17,\qquad \kappa=|\delta^3\alpha|=51\sqrt3}
\tag{6}
$$
满足全部局部条件。三条来源在同一个原嵌入
$$
\iota_{17}(x+y\delta)=
\begin{pmatrix}x&153y\\-y/51&x\end{pmatrix}
\tag{7}
$$
内实现。虽然 $17^k/17$ 也是一个全局范数，本篇并没有用这个事实来省掉一次隐含换框；(6) 直接由每条原角色的 (4) 得到。

## 3. 十七处三个实际有限 Weil 向量

仍使用 R290 的奇 conductor 模型
$$
e_a=\mathbf1_{a/17+\mathbb Z_{17}},\qquad a\in\mathbb F_{17}.
$$
写 $g=z/\bar z=z^{-16}$，则原 Hilbert 90 角色为 $\eta_k(g)=g^{-3k}$。Yang Proposition 1.2(3) 的 splitting 差必须保留缺失二次角色 $\eta_0(g)=g^9$。所以真正不变向量在有限 $\mu_4$ 模型中的角色是
$$
\tau_k=\eta_0\eta_k^{-1}=g^{9+3k}.
\tag{8}
$$
取 R290 同一个 $g_0=2+4\delta$，其阶为十八，$g_0^6=\omega$。准确表格为

| $k$ | 十七处单位角色 | 原有限 $\tau_k$ | $\tau_k(g_0)$ |
|---:|---|---|---|
| $1$ | $z^{48}$ | $g^{12}$ | $\omega^2$ |
| $3$ | $z^{144}$ | $1$ | $1$ |
| $5$ | $z^{240}$ | $g^6$ | $\omega$ |

三个角色均不是缺失的 $g^9$，且都具有重数一。

令 $\zeta=e^{2\pi i/17}$，$s=\sqrt{17}>0$。共同有限算子是
$$
W(x+y\delta)_{ab}
=-\frac{(y/17)}s\,
\zeta^{\frac3{2y}(x(a^2+b^2)-2ab)}\quad(y\ne0),
\quad W(-1)e_a=e_{-a},\quad W(1)=1.
\tag{9}
$$
定义原正交投影和规范向量
$$
\Pi_k=\frac1{18}\sum_{j=0}^{17}\tau_k(g_0)^{-j}W(g_0^j),
\qquad f_k=9s\,\Pi_ke_0.
\tag{10}
$$
不需要另取一个未经定标的 eigenvector。其全部坐标可由八项公式读取：写 $g_0^j=x_j+y_j\delta$，则
$$
f_k(a)=s\mathbf1_{a=0}
-\sum_{j=1}^{8}\left(\frac{y_j}{17}\right)
\tau_k(g_0)^{-j}\zeta^{c_ja^2},
\qquad c_j=\frac{3x_j}{2y_j}\in\mathbb F_{17}.
\tag{11}
$$
对应数据为
$$
\left(\left(\frac{y_j}{17}\right)\right)_{j=1}^8
=(1,1,1,-1,-1,1,1,1),\qquad
(c_j)_{j=1}^8=(5,15,10,6,11,7,2,12).
\tag{12}
$$
直接配对 (12) 中互为负数的指数，得到 $f_k(-a)=f_k(a)=\overline{f_k(a)}$。在零坐标上，平凡 $\tau_3$ 的符号和为四，另外两条的带权和为一。因此
$$
f_1(0)=f_5(0)=s-1,\qquad f_3(0)=s-4.
\tag{13}
$$
$W$ 是原单位表示，故 $\Pi_k$ 为正交投影。由 (10)，
$$
\|f_k\|^2=(9s)^2\langle\Pi_ke_0,e_0\rangle=9s f_k(0).
$$
于是原十七处范数准确为
$$
\boxed{\quad
n_1=n_5=9(17-\sqrt{17}),\qquad
n_3=9(17-4\sqrt{17})>0.
\quad}
\tag{14}
$$
自对偶测度取 $\operatorname{vol}(\mathbb Z_{17})=1$，所以 $\phi_{k,17}=\sum_a f_k(a)e_a$ 的 Schwartz 范数正是 (14)。

## 4. 共同小坏位、实际来源及全部权

由于 $2/3$ 角色和 (7) 均与 R290 相同，整套真实 Schrödinger splitting 相同，而不只是有限向量看起来相同。故
$$
\begin{aligned}
\phi_{k,2}&=e_0-e_2+t(e_1+e_3),
&e_a&=\mathbf1_{a/2+2\mathbb Z_2},
&t&=(1+\sqrt3)/\sqrt2,\\
\phi_{k,3}&=\mathbf1_{3^{-1}\mathbb Z_3},
&\|\phi_{k,2}\|^2&=3+\sqrt3,
&\|\phi_{k,3}\|^2&=3.
\end{aligned}
\tag{15}
$$
这包含 R290 对整个 $K_2^1$ 的生成元与支撑检验；三处仍用同一个奇、偶 conductor 转模。所有其他有限地点为原标准球。

原有理支撑是 $x=n/102$，共同 dyadic 系数 $v_2=(1,t,-1,t)$。定义
$$
\begin{aligned}
a_{k,n}&=v_2(n\bmod4)f_k(3n\bmod17),\\
b_{k,m}&=\sum_{n\in\mathbb Z}a_{k,n}
H_m\left(\frac{\sqrt\kappa}{102}n\right)
\exp\left(-\frac{\pi\sqrt3}{204}n^2\right),\\
\sum_{m\ge0}H_m(x)\frac{T^m}{m!}
&=\exp(xT-T^2/(8\pi)).
\end{aligned}
\tag{16}
$$
这些是全部原 Hermite 来源，不是有限阶拟合。它们实且偶；对有理三次单位 $\omega$ 的全局 Weil 不变性，和 R290 同样给
$$
\mathcal B_k(T)=\sum_{m\ge0}b_{k,m}T^m/m!\in\mathbb R[[T^6]].
\tag{17}
$$

全权角色为
$$
\chi_{k,m}=\psi_k^{2m+1}|\cdot|_K^{-m-1/2}
=\chi_k^{2m+1}.
\tag{18}
$$
二处单位角色要求 $3\mid m$，三处 $(-i)^{2m+1}$ 要求 $m$ 偶，故共同准确周期为 $6\mid m$。在这些权上十七处三个单位角色及 uniformizer 都保持不变。好分裂处的未分歧参数仍变化，但 Yang Corollary 2.14 的实际标准球保持；不能误称完整 Hecke 角色处处不变。三条来源均使用 (16) 同一个有限函数和第 $m$ Hermite 向量，且 (6) 的局部 dichotomy 保持。

## 5. 全权 Yang 平方及其全部常数

由 (14)–(16)，第 $m$ 权的原全局范数为
$$
\mathcal N_{k,m}
=\frac{3(3+\sqrt3)n_k}{\sqrt{102\sqrt3}}
\frac{m!}{(4\pi)^m}.
\tag{19}
$$
Yang Theorem 1.11 的 $S_1$ 对三条角色都是 $\{2,17\}$，没有坏分裂处，故
$$
c(0)=(1+2^{-1})^{-1}(1+17^{-1})^{-1}=17/27.
$$
共同 $K$ 的类数为一，原紧子群体积积与商体积之比为 $|\mu_6|=6$；因此 R290 的实际 theta 积分仍为 $b_{k,m}$ 除以 $\sqrt{\mathcal N_{k,m}}$ 乘同一商体积。带入 Yang 的规范平方，得
$$
\boxed{\quad
L(\psi_k^{2m+1},m+1)
=C_k\frac{(4\pi)^m}{m!}\,b_{k,m}^{2},
\quad
C_k=\frac{\pi\sqrt{102\sqrt3}}
{17\sqrt3(3+\sqrt3)n_k},
\quad 6\mid m.
\quad}
\tag{20}
$$
这是单个真实实来源的平方。常数之间准确有
$$
\boxed{C_5=C_1,\qquad C_3=(13+3\sqrt{17})C_1.}
\tag{21}
$$
这里 $C_1$ 正是 R290 的 $C_{17}^{(0)}$，所以 (20) 同时核回已发表的原 $k=1$ 规范。

若之后把三条来源各自写入原方程的微分 $dx/(2y)$，实周期的同构尺度必须另保留。对 (1) 原方程的相同实周期选择，有
$$
\Omega_k=17^{-(k-1)/6}\Omega_1,
\qquad
\Omega_k^{-(2m+1)}
=17^{(k-1)(2m+1)/6}\Omega_1^{-(2m+1)}.
\tag{22}
$$
(22) 来自 $x\mapsto17^{-(k-1)/3}x$、$y\mapsto17^{-(k-1)/2}y$ 到 $\mathcal E_1:y^2=x^3+17$ 的真实同构及微分拉回。它是原方程的尺度，不擅换成某个最小方程的周期。相应 $p$-adic Mellin 全权单位及其导数中的 $\log\langle17\rangle$ 不能删掉。

## 6. 与 R297 的实际 CM13 三线一一对应

令 $\gamma=4+\omega$、$\operatorname N\gamma=13$，并使用 R297 已证明的真正算子 $M_{13}=[\gamma]_*[\bar\gamma]^*$。在同一个 (6)、(7)、(15) 框架中，其十七处 torus 元素为
$$
\gamma/\bar\gamma\equiv g_0^{14}\pmod{17}.
$$
实际 theta pull/trace 与共同有限 Weil 算子实现同一个 Heisenberg 自同构；不可约性给一个对整块统一的标量。三条向量的二、三处分量相同，因此该标量不随 $k$ 改变。用 R297 已定标的 $M_{13}S_1=-\gamma S_1$，得到
$$
\frac{\lambda_k}{\lambda_1}
=\frac{\tau_k(g_0^{14})}{\tau_1(g_0^{14})}
=\omega^{k-1}.
$$
所以实际标定为
$$
\boxed{\quad
k=1:\lambda_1=-\gamma,\qquad
k=3:\lambda_3=-\gamma\omega^2,\qquad
k=5:\lambda_5=-\gamma\omega.
\quad}
\tag{23}
$$
不是只识别多项式 $X^3+\gamma^3$ 的无序根集合。共同 degree-$34$ 原截面、后续多项式和中央质量可据 (23) 使用准确 CM 身份。本文不以它们的 eigenvalue 代替完整 Mellin 交换公式，也不令任何 rank-zero 参考的中央导数为零。

## 证书与来源

- [check-jzero-three-sextic-original-local-data.py](../scripts/check-jzero-three-sextic-original-local-data.py) 及同名 JSON：在 $\mathbb Q(\zeta_{51})$ 中核三条真实 eigenline、全部 trace-fibre Gauss、向量实性和范数、全权周期、CM13 相位及全局测度常数；不存大稠密矩阵。
- R290 的全部原二处 Schrödinger 生成元/支撑、三处转模和全局测度；R297 的真实 CM13 Heisenberg 比较与 $k=1$ 定标；R302 的基参考及 $+i$ 与 $-i$ 角色区别。
- J. H. Silverman and K. E. Stange, *Amicable Pairs and Aliquot Cycles for Elliptic Curves*, Experimental Math. **20** (2011), 329–357，§6，Theorem 19 证明中的六次角色公式；[作者全文](https://arxiv.org/pdf/0912.1831)，DOI 10.1080/10586458.2011.565253。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*, Compositio Math. **117** (1999), 337–359，Proposition 1.2、Corollary 1.4、Proposition 1.5、Appendix (A1)–(A11)；[作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
- T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math. **485** (1997), 25–53，Theorem 1.11、Corollary 2.14、Theorems 2.6、2.15；[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
