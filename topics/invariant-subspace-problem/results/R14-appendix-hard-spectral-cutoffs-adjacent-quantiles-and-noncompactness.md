# R14 附录：FJKP 硬谱截断的全指数非紧性与实际量化

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d；normal_resume_1cf 独立核对原文阈值、归一化和两条序列的全部极限。
状态：已证明。排除下述精确的 FJKP 2005 强收敛入口；不排除该文的所有方法，也不解决普通 Hilbert ISP。

## 1. 原文条件与本稿的准确对象

一手来源为 C. Foiaş、I. B. Jung、E. Ko、C. Pearcy，
*On quasinilpotent operators. III*，J. Operator Theory **54:2** (2005), 401–414，
[期刊正式全文](https://jot.theta.ro/jot/archive/2005-054-002/2005-054-002-013.pdf)。

本文核对其 §2（pp.402–404）的谱阈值和 Lemma 2.4，
以及 Theorem 3.1 / Corollary 3.2（p.405）。
该入口沿相邻阈值比趋零的子列构造两个非零弱极限；
其中任一向量序列有强收敛子列，就可得到超不变子空间。
以下对实际 Haar 算子独立计算这两个序列，并证明所需强收敛不发生。

保持仓库的实际算子
$$
H=L^2(\mathbb Z_2,\mu),\qquad A=M_wU,\qquad (Uf)(y)=f(y-1),
$$
以及 [R14](R14-backward-minimal-images-all-exponents.md) 的原权。
令
$$
W_n(y)=\prod_{j=0}^{n-1}w(y-j),\qquad
A^nA^{*n}=M_{W_n^2}.
$$
固定任意 $\|f\|=1$ 和 $0<\theta<1$。定义
$$
\lambda_n=\inf\{t\ge0:\|\mathbf1_{\{W_n^2\le t\}}f\|>\theta\}>0,
\tag{1.1}
$$
$$
P_n=\mathbf1_{\{W_n^2\le\lambda_n\}},\qquad
R_n=\mathbf1_{\{W_n^2<\lambda_n\}},
$$
$$
s_n=(I-R_n)f,\qquad t_n=A^*P_{n+1}f.
\tag{1.2}
$$
这里 $P_n,R_n$ 是指标乘法投影。

阈值两端必须分开。由单调性和谱测度的左右连续性质，
$$
\|R_nf\|^2\le\theta^2,\qquad
\|P_nf\|^2\ge\theta^2,\qquad
\|s_n\|\ge\sqrt{1-\theta^2}.
\tag{1.3}
$$
不要求闭端的第二个不等式严格。

原文把算子归一化为 $T=A/\|A\|$。
其阈值满足
$$
\lambda_n(T)=\|A\|^{-2n}\lambda_n(A).
$$
故相邻比趋零的条件不变，$s_n$ 完全相同，$t_n$ 只差一个固定非零标量倍。
以下直接用原 $A$。

## 2. 全指数的稀层与阈值下界

记
$$
E(n,Q)=\{y:y\bmod Q\in\{0,\ldots,n-1\}\},\qquad n<Q,\quad Q=2^a.
$$
[R14 §2.2](R14-backward-minimal-images-all-exponents.md) 给对每个固定 $g\in L^1(\mu)$
$$
\int_{E(n,Q)}g\,d\mu-\frac nQ\int g\,d\mu\longrightarrow0
\quad(Q\to\infty).
\tag{2.1}
$$
这个结论允许 $n/Q$ 不收敛；对固定平移后的事件也成立。
其证明只需在低位柱函数上数余类，再作 $L^1$ 逼近。

令
$$
r=\left\lceil\log_2\frac{16}{\theta^2}\right\rceil,\qquad
p_\theta=2^{-r-2}>0.
$$
当 $2^k\le n<2^{k+1}$ 时，置
$$
m_n=k+r-1,\qquad
G_n=E(n,2^{m_n+1})^c,
$$
$$
L_n=e^{-1400\,16^{m_n}},\qquad
\mathcal E_n=E(n,2^{m_n+3}),\qquad
U_n=e^{-4096\,16^{m_n}}.
\tag{2.2}
$$
R14 §§3–4 的真实权计数给
$$
W_n\ge L_n\text{ 于 }G_n,\qquad
W_n\le U_n<L_n\text{ 于 }\mathcal E_n,
\tag{2.3}
$$
$$
\int_{G_n^c}|f|^2\,d\mu\le\frac{\theta^2}{4}
\quad(n\text{ 充分大}),\qquad
p_\theta\le\mu(\mathcal E_n)<2p_\theta.
\tag{2.4}
$$
这些估计来自实际 $-\log w$ 的 $16^j$ 界，保留所有整数指数。

若 $t<L_n^2$，则 $\{W_n^2\le t\}\subseteq G_n^c$。
(2.4) 与 (1.1) 因而给
$$
\boxed{\lambda_n\ge L_n^2.}
\tag{2.5}
$$
由 (2.3)，$\mathcal E_n$ 严格落在 $\{W_n^2<\lambda_n\}$ 内，
不受阈值原子影响。因此
$$
\boxed{\mathbf1_{\mathcal E_n}s_n=0,\qquad
\mathbf1_{\mathcal E_n}P_nf=\mathbf1_{\mathcal E_n}f.}
\tag{2.6}
$$

## 3. 第一条硬谱截断序列：所有指数均无强子列

对任意固定 $s\in H$，(2.1)、(2.4)、(2.6) 给
$$
\liminf_{n\to\infty}\|s_n-s\|
\ge\liminf_n\|\mathbf1_{\mathcal E_n}s\|
\ge\sqrt{p_\theta}\|s\|.
\tag{3.1}
$$
再用 (1.3)，
$$
\liminf_n\|s_n-s\|\ge\sqrt{1-\theta^2}-\|s\|.
$$
两界合并：
$$
\boxed{
\liminf_n\|s_n-s\|
\ge
\frac{\sqrt{p_\theta}\sqrt{1-\theta^2}}{1+\sqrt{p_\theta}}>0
\quad(s\in H).
}
\tag{3.2}
$$
所以 $(s_n)$ 在全部整数指数中没有强收敛子列。
此结论不需要相邻阈值比条件。

## 4. 相邻比趋零时，低闭谱质量逼近准确阈值

以下取任意 $n_\nu\to\infty$，满足
$$
\frac{\lambda_{n_\nu+1}}{\lambda_{n_\nu}}\longrightarrow0.
\tag{4.1}
$$
置
$$
b_\nu=\|P_{n_\nu+1}f\|^2.
$$

**引理。**
$$
\boxed{b_\nu\longrightarrow\theta^2.}
\tag{4.2}
$$

证明：给任意 $\varepsilon>0$。
因为 $w>0$ 几乎处处，$\mu\{w<\delta\}\to0$。
Haar 平移保测度和 $|f|^2$ 积分的绝对连续性，使我们可以选择固定 $\delta>0$，满足
$$
\sup_{n\ge1}
\int_{\{w(y-n)<\delta\}}|f(y)|^2\,d\mu(y)<\varepsilon.
\tag{4.3}
$$
这里的统一性来自所有这些集合有同一测度，而非假定 $f$ 平移不变。

对足够大 $\nu$，(4.1) 给
$\lambda_{n_\nu+1}/\lambda_{n_\nu}<\delta^2$。
若 $b_\nu>\theta^2+\varepsilon$，则集合
$$
\{W_{n_\nu+1}^2\le\lambda_{n_\nu+1}\}
\cap\{w(y-n_\nu)\ge\delta\}
$$
的 $|f|^2$ 质量严格超过 $\theta^2$。
而
$$
W_{n+1}(y)=W_n(y)w(y-n)
$$
使该集合上
$$
W_{n_\nu}^2\le\lambda_{n_\nu+1}/\delta^2.
$$
由 (1.1)，
$$
\lambda_{n_\nu}\le\lambda_{n_\nu+1}/\delta^2,
$$
与所选比值矛盾。
故最终 $b_\nu\le\theta^2+\varepsilon$。
结合 (1.3) 的 $b_\nu\ge\theta^2$，证明 (4.2)。

引理不把阈值闭端的质量预先等同于 $\theta^2$；
准确等号只是沿 (4.1) 的极限结论。

## 5. 第二条序列：全部允许子列也有统一强距离

记 $a=A^*f$。
从 (2.6) 及 $A^*=U^*M_w$，在平移事件
$$
\widetilde{\mathcal E}_n=\{y:y+1\in\mathcal E_{n+1}\}
$$
上有准确等式
$$
\mathbf1_{\widetilde{\mathcal E}_n}t_n
=\mathbf1_{\widetilde{\mathcal E}_n}a.
\tag{5.1}
$$
因此，对任意固定 $t\in H$，沿 (4.1)，
$$
\liminf_\nu\|t_{n_\nu}-t\|
\ge\sqrt{p_\theta}\|a-t\|.
\tag{5.2}
$$

还须排除候选极限 $a$ 本身。
选固定 $\delta_0>0$ 使
$$
\int_{\{w<\delta_0\}}|f|^2\,d\mu
<\frac{1-\theta^2}{2}.
$$
由 (4.2)，
$$
\begin{aligned}
\liminf_\nu\|t_{n_\nu}-a\|^2
&=\liminf_\nu\|A^*(I-P_{n_\nu+1})f\|^2\\
&=\liminf_\nu\int w^2(1-P_{n_\nu+1})|f|^2\,d\mu\\
&\ge\delta_0^2\,\frac{1-\theta^2}{2}
=:d^2>0.
\end{aligned}
\tag{5.3}
$$
这里第二行利用 $U^*$ 酉，不把 $A^*$ 当成有界下界算子。

三角不等式另给
$$
\liminf_\nu\|t_{n_\nu}-t\|\ge d-\|a-t\|.
$$
与 (5.2) 合并，得到
$$
\boxed{
\liminf_\nu\|t_{n_\nu}-t\|
\ge\frac{d\sqrt{p_\theta}}{1+\sqrt{p_\theta}}>0
\quad(t\in H).
}
\tag{5.4}
$$
所以第二条序列在每个满足 (4.1) 的子列上也没有任何强收敛子列。

不能删除 (4.1)：
本稿只对第一条序列给出无条件的全指数非紧性；
第二条使用了由该比值迫出的 (4.2)。

## 6. 原文入口的确切结论与继续开放的范围

FJKP Lemma 2.4 所用子列满足 (4.1)，
所以其 Theorem 3.1 的两条可能强收敛序列在本算子上都被 §§3、5 排除。
相应两族谱投影也不可能沿这些子列强收敛：
一族强收敛会使 $s_n$ 强收敛，另一族会使 $A^*P_{n+1}f$ 强收敛。
因此 Corollary 3.2 的单调子列入口同样不成立。

这是硬谱截断的直接论证。
R14 原稿的软 resolvent 型极小像非紧性本身不能不加说明代替它。
这里没有使用原文的其他充分条件，也没有声称已经核完 JKP 2019 的未取得正文。

本稿不排除逃逸目标、退化阈值、其他归一化或不要求强紧性的方案。
一般正常见证、实际边界 $N=M$ 与普通复 Hilbert ISP 仍未完成。
