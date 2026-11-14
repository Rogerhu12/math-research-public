# 原全局单位的 CM5 范数、中心差分与全部平移中心

日期：2026-11-13。**状态：下列原函数范数、全局单位差分及有限群环商公式已证明；尚未给出新的跨 $p$ 原始性。**

本记录继续 O6 的原单位 $\Phi$。它支付几何 CM5 对应在这个单位上的真实 Artin 作用，再准确分解一个在 $T=p$ 为零的 CM 差分。这里的算子不同于整单位工作记录 §8 中中心非零的 Robert smoothing 因子。本文不把 theta 截面上的 CM5 特征值直接当作全局单位的作用。

## 1. 固定原函数及实际 CM5 特征

取
$$
E:y^2=x^3-17x,\qquad K=\mathbf Q(i),\qquad
a=2+i,\quad \bar a=2-i.
$$
原函数仍是 R18–R19 的
$$
\Phi(t)=\frac{N_{M/K}(1+\alpha t)}{N_{M/K}(1-\alpha t)},
\qquad t=-x/y,
$$
并有
$$
\operatorname{div}\Phi=D_+-D_-,\quad
\Phi(O)=1,\quad \Phi(-P)=\Phi(P)^{-1}.
\tag{1}
$$
$D_+$ 是原 $\mathfrak f$ 挠点的完整 $K$-Galois 轨道，$D_-=[-1]D_+$，其中 $\mathfrak f=(34(1+i))$。

直接在 $\mathbf F_5$ 上计数，$x^3-17x$ 在 $x=0,1,2,3,4$ 处分别为 $0,4,4,1,1$，故 $\#E(\mathbf F_5)=10$、$a_5=-4$。沿用本课题的 Hecke 规范，$\psi_E((a))$ 是属于理想 $(a)$、范数五且迹为 $-4$ 的 CM 整数，因而
$$
\psi_E((a))=-a,\qquad
\psi_E((\bar a))=-\bar a.
\tag{2}
$$
CM 互反律使 $[-a]$、$[-\bar a]$ 分别置换 $D_+$ 和 $D_-$。所以原始乘法 $[a]$、$[\bar a]$ 都交换这两个除子。

## 2. 函数范数没有额外常数

用有限平坦函数范数
$$
(N_{[a]}f)(Z)=\prod_{[a]W=Z}f(W)
$$
固定输出变量。其除子是 $[a]_*\operatorname{div}f$。由 (1)–(2)，$N_{[a]}\Phi$ 与 $\Phi^{-1}$ 除子相同。

在 $Z=O$ 处，$E[a]$ 的四个非零点分成两对 $T,-T$，每对的 $\Phi$ 值之积为一；$O$ 的因子也为一。所有值有限非零，因为 $5$ 与 $N\mathfrak f$ 互素。由此固定常数，得到
$$
\boxed{\quad N_{[a]}\Phi=\Phi^{-1},\qquad
N_{[\bar a]}\Phi=\Phi^{-1}.\quad}
\tag{3}
$$

令 $\mathscr C_a=[a]_*[\bar a]^*$ 表示对乘法函数先拉回、再取上述范数。$[\bar a]$ 在 $E[a]$ 上为自同构，故逐纤维换指标得到
$$
\boxed{\quad
\mathscr C_a\Phi(Z)
=N_{[a]}(\Phi\circ[\bar a])(Z)
=\Phi([\bar a]Z)^{-1}.
\quad}\tag{4}
$$
这里是一个五点有限 étale 代数的范数，不把它称为某个未指定的五次域扩张范数。

### 2.1 对数导数的缩放也须保留

写 $\ell=\log\Phi$，在 $O$ 取常数零的 germ，并令 R19 的 $S$ 满足 $\partial\ell=2S$。对加法函数定义
$$
(\mathscr C_a^{\rm add}h)(Z)
=\sum_{[a]W=Z}h([\bar a]W).
$$
对 (4) 求不变导数时，每个分支的链式因子为 $\bar a/a$。因此
$$
\frac{\bar a}{a}\,\mathscr C_a^{\rm add}S
=-\bar a\,S\circ[\bar a],
$$
即
$$
\boxed{\quad
\mathscr C_a^{\rm add}S=-a\,S\circ[\bar a].
\quad}\tag{5}
$$
这是有理函数恒等式，不依赖对数分支。取实际 $p$-adic 单位对数时，(4) 本身也给准确的对数等式；若用复 germs，可令 $T,-T$ 两项的常数互相抵消来固定同一等式。

## 3. 在原单位塔上恰为共轭素理想的 Artin 作用

固定目标 split 素数 $p\ge13$、$p\ne17$，选 $\mathfrak p\mid p$，并取原塔
$$
K_n=K(E[\pi^n]),\quad \pi=\psi_E(\mathfrak p),\qquad
P_n\in E[\pi^n],\quad
z_n=e_{\widetilde\chi}\Phi(P_n).
$$
单位模用加法记号。设 $\sigma_{(\bar a)}$ 是素理想 $(\bar a)$ 在 $K_n/K$ 中的算术 Artin 元。由 (2)，它在 $P_n$ 上的作用为 $[-\bar a]$。因为 $\Phi$ 在 $K$ 上定义，(4) 给
$$
\mathscr C_a\Phi(P_n)
=\Phi([\bar a]P_n)^{-1}
=\Phi([-\bar a]P_n)
=\sigma_{(\bar a)}\Phi(P_n).
$$
因此全部有限层以及范数极限都满足
$$
\boxed{\quad
\mathscr C_a z_n=\sigma_{(\bar a)}z_n,
\qquad \mathscr C_a z_\infty=\sigma_{(\bar a)}z_\infty.
\quad}\tag{6}
$$
此处右边是原全局单位格上的真实 Galois 作用。左边总乘积的全局单位性直接由 (4) 给出；不需要先对每个单独的纤维值作单位性断言。

令
$$
u=1+p,\quad \rho_E(\gamma)=u,\quad T=\gamma-1,
\quad \theta=T-p,\quad \Lambda=\mathbf Z_p[[T]],
\quad \lambda=\iota_{\mathfrak p}(-\bar a)\in\mathbf Z_p^\times.
$$
在直接 $\widetilde\chi$ 分量上，(6) 的中心值是 $\lambda=-\bar a$，不是 $-a$。若人为加入已明说的标量 $a/\bar a$，则
$$
\boxed{\quad
\frac a{\bar a}\,\mathscr C_a+a
=\frac a{\bar a}\bigl(\sigma_{(\bar a)}-\lambda\bigr)
\quad\text{在原单位系统上}.
\quad}\tag{7}
$$
式 (7) 是中心零的实际单位差分。它不声称这个标量补偿已经等于 theta 线丛中的全部 Gaussian 补偿；将两种实现相互比较仍须支付所用变换。

## 4. 中心零差分的完整 Iwasawa 分解

写
$$
\lambda=\omega(\lambda)\langle\lambda\rangle,
\qquad s=\frac{\log_p\langle\lambda\rangle}{\log_pu}\in\mathbf Z_p.
$$
$s\ne0$：否则单位 $\lambda$ 的 $p$-adic 对数为零，故为单位根；但作为代数数 $-2+i$ 的复绝对值为 $\sqrt5$。置
$$
e=v_p(s)=v_p(\lambda^{p-1}-1)-1\ge0.
\tag{8}
$$
在直接字符块内，真实 Artin 差分是
$$
D_a(T):=\sigma_{(\bar a)}-\lambda
=\omega(\lambda)\bigl((1+T)^s-u^s\bigr).
\tag{9}
$$

**分解。** 存在 $V_a(T)\in\Lambda^\times$，使
$$
\boxed{\quad
D_a(T)=V_a(T)\,\theta\,C_e(T),\qquad
C_e(T)=\frac{(1+T)^{p^e}-u^{p^e}}{T-p}.
\quad}\tag{10}
$$
当 $e=0$ 时 $C_e=1$。一般 $C_e$ 为次数 $p^e-1$ 的首一 distinguished 多项式，并且
$$
C_e(p)=p^e u^{p^e-1},\qquad
C_e(T)\equiv T^{p^e-1}\pmod p.
\tag{11}
$$

证明：写 $s=p^e r$，$r\in\mathbf Z_p^\times$，令 $X=(1+T)^{p^e}$、$b=u^{p^e}$。则
$$
\frac{X^r-b^r}{X-b}
=b^{r-1}\sum_{k\ge1}\binom rk
\left(\frac{X-b}{b}\right)^{k-1}
$$
属于 $\Lambda$，其模 $(p,T)$ 的值为 $r$，所以是单位。再乘 $\omega(\lambda)$，即得 (10)。式 (11) 由几何级数与模 $p$ 的 Frobenius 恒等式直接给出。

若在包含 $p^e$ 次单位根的域上分解，$C_e$ 的根准确为
$$
T=u\zeta-1,\qquad \zeta^{p^e}=1,\quad \zeta\ne1.
\tag{12}
$$
所以 $D_a/\theta$ 在高度一局部环 $\Lambda_{(\theta)}$ 中总可逆，但它在完整 $\Lambda$ 中可逆当且仅当 $e=0$。这些额外的平移中心不能由“中心导数非零”删去。

准确的中心一次系数为
$$
\left.\frac{D_a(T)}{\theta}\right|_{T=p}
=\frac{\lambda s}{u}\ne0.
\tag{13}
$$

## 5. 所有有限层的额外商及 Smith 因子

置
$$
R_n=\Lambda/(\omega_n),\qquad
\omega_n=(1+T)^{p^{n-1}}-1,\qquad d=p^{n-1}.
$$
下式是完整有限群环商的准确整数结构：
$$
\boxed{
R_n/C_eR_n\simeq
\begin{cases}
\mathbf Z_p/p^{e+1-n}\ \oplus\
(\mathbf Z_p/p^{e+1})^{d-1},& n\le e+1,\\[2mm]
(\mathbf Z_p/p^n)^{p^e-1},& n\ge e+1.
\end{cases}}
\tag{14}
$$
指数为零的循环因子指零模；两式在 $n=e+1$ 完全一致。

证明：若 $n\ge e+1$，在首一多项式 $C_e$ 的商中有 $(1+T)^{p^e}=u^{p^e}$，因而 $\omega_n=u^d-1$。该商为秩 $p^e-1$ 的自由 $\mathbf Z_p$-模，而 $v_p(u^d-1)=n$，得到第二式。

若 $n\le e+1$，则 $(1+T)^{p^e}=1$ 在 $R_n$ 中成立，所以
$$
\theta C_e=1-u^{p^e}.
$$
右端是 $p^{e+1}$ 乘一个单位。乘 $\theta$ 的 Smith 因子为 $1$（$d-1$ 次）及 $p^n$，因为 $R_n/\theta R_n\simeq\mathbf Z_p/p^n$。在 $\mathbf Q_p\otimes R_n$ 中取逆再乘上述标量，便得到第一式的所有 Smith 因子。这也证明没有漏掉有限群环的非最大整环格。

特别地，若 $e>0$ 固定，随 $n$ 增长，(14) 的余长度为 $n(p^e-1)$。所以一般不能用一个与 $n$ 无关的 $p$ 次幂清除 $D_a/\theta$ 的逆在全部有限层上的分母。

## 6. 对已构造的全局除点的准确作用

整单位工作记录已证明
$$
w_\infty=z_\infty/\theta\in E_\infty^{\widetilde\chi}.
$$
因此当 $e=0$ 时，(10) 确实构造一个新的写法下的原全局单位差分原像：
$$
\boxed{\quad
v_\infty=V_a(T)^{-1}w_\infty
\in E_\infty^{\widetilde\chi},\qquad
(\sigma_{(\bar a)}-\lambda)v_\infty=z_\infty.
\quad}\tag{15}
$$
它范数相容，且在每个有限层属于原全局单位的 $p$-完备化；没有将一个局部 Coleman 原像直接称为全局单位。

若 $e>0$，先在每层的 $\mathbf Q_p\otimes U_{0,n}$ 中取 $D_a^{-1}z_n$；$D_a$ 在那里可逆，因为有限阶 Galois 特征值不等于非单位根 $\lambda$。这些唯一的有理原像仍范数相容，记为 $v_\infty$。它成为整单位系统的准确额外要求为
$$
v_\infty\in E_\infty^{\widetilde\chi}
\quad\Longleftrightarrow\quad
w_\infty\in C_e(T)E_\infty^{\widetilde\chi}.
\tag{16}
$$
这是由 (10) 及 $V_a\in\Lambda^\times$ 得到的实际单位格条件。已知的 $w_\infty\in E_\infty$ 本身不给 (16)。作为明确检验，$p=13$ 的两个 $i$ 的模 $13^2$ 提升为 $70,99$，相应 $\lambda^{12}$ 模 $169$ 为 $27,157$，两处都给 $e=0$；这里没有将这个有限检验当作跨 $p$ 结论。

式 (15) 只把已经存在的一次中心除法实现成一个真实 CM5 Artin 差分的原像，不是新的第二次中心除法。若写原局部系数 $F_p=\theta^2G_p$，其局部坐标仍为 $F_p/D_a$，故一次中心系数只是原 $G_p(p)$ 乘 $u/(\lambda s)$，没有新增非零来源。

最后保留 O6 的原中心核。对辅助 $w$，若 $I=\operatorname{Ann}_{R_n}(c_w)$，其中心核中的项仍是
$$
\frac{I\cap\theta^2R_n}{\theta I}.
\tag{17}
$$
(14) 计算的是 CM5 差商的额外商，既不将 (17) 置零，也不把两者认作同一个模。两条原 MW Artin 关系及一辅助 MRS 给出 (15) 所需的 $w_\infty$；更高的原始性仍须新的实际输入。

## 整数核对

[脚本](../scripts/check-original-unit-cm5-translated-centres.py) 对 $p=3,5$、$n=1,2,3$、$e=0,1,2$ 的全部十八个有限群环直接构造循环矩阵，并分别检查乘法恒等式和整数 Smith 形的 $p$ 初级因子；它另核 $a_5=-4$ 和两处 $p=13$ 的上述 Fermat 余数。[输出](../scripts/check-original-unit-cm5-translated-centres.json) 共 **38 项精确检查通过**。小素数 $3,5$ 在这里只检验一般群环代数公式，不被列入 E17 的目标素数集。

## 依赖

- R18–R19：原 $\Phi$、完整 $D_\pm$、奇性、全局单位及 Hecke 规范。
- R24、R36：直接字符、$\rho_E(\gamma)=1+p$、有限层中心商和 $\theta$ 非零因子。
- [原单位范数塔记录](2026-11-12-phi-coleman-tower.md)：规范范数及理想群的全局单位论证。
- [O6 整单位记录](2026-11-13-o6-integral-unit-division-and-one-prime-mrs-descent.md)：$z_\infty/\theta$ 的全局整性及 (17) 的中心核。
