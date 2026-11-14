# Theta 单因子的中心斜率：有限挠值对数和与严格误差

日期：2026-11-12。状态：本文的有限层公式、误差界及逐素数充要证书已证明。没有证明这些证书对无穷多个素数成功。

采用 [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md) 的固定截面，并采用 [实结构笔记](2026-11-12-theta-real-structure-and-mellin-square.md) 的一次固定相位规范：

$$
 S(z)=R(x(z))\sigma_E(z)^d,\qquad R=P(x^2),\qquad
 E:y^2=x^3-17x .
$$

在每个目标普通素数 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$ 处，
记其有界 Amice 测度为 $\nu_p$，principal Mellin 分支为 $G_p(T)$。
实结构已经证明

$$
 G_p(0)=0,\qquad
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
       \iff G_p'(0)\ne0.                                      \tag{1}
$$

本笔记把 (1) 的实际斜率写成有限个**代数挠值乘有理数的
$p$-进对数**的极限，并给出每一层的确定精度。因此它比仅说
“斜率是一个对数矩”更具体；但它也准确保留了需要无限塔的部分。

## 1. 一个由固定截面给出的测度界

设

$$
 P(X)=\sum_j r_jX^j,\qquad
 B_p=\max\bigl(0,\lceil-\min_{r_j\ne0}v_p(r_j)\rceil\bigr).
                                                               \tag{2}
$$

这里固定代数系数域在 $\mathbb C_p$ 中的嵌入与前文一致，
$v_p(p)=1$。除固定有限个素数之外，$B_p=0$。

沿用 $\Sigma(t)=\sigma_E(\log_Et)$。普通处
$\Sigma(t)\in t\mathbb Z_p[[t]]$，且 $x(t)\in t^{-2}\mathbb Z_p[[t]]$。
因为 $\deg P\le d/4-1$，每一项
$r_jx(t)^{2j}\Sigma(t)^d$ 均至少有 $t^4$ 的因子。因此

$$
 R(x(t))\Sigma(t)^d\in
       p^{-B_p}t^4\mathcal O_{\mathbb C_p}[[t]].                 \tag{3}
$$

与整的高度一正式群同构
$\widehat{\mathbb G}_m\longrightarrow\widehat E$ 复合，得到 Amice
变换 $A_p(Z)$，其系数仍属于
$p^{-B_p}\mathcal O_{\mathbb C_p}$。Amice 对应遂给出

$$
 p^{B_p}\nu_p\text{ 是整测度}.                                \tag{4}
$$

这里的界只使用固定多项式的系数，没有把未知 Mellin 斜率的赋值用作输入。

## 2. 所有有限 $\pi$-除法层的 sigma 值都是代数数

固定 $\pi=\psi(\mathfrak p)$，$v_p(\pi)=1$，
$\pi\bar\pi=p$。对 $n\ge1$，取

$$
 e_n=\operatorname{ord}_{(\mathcal O_K/\pi^n)^\times}(\bar\pi),
 \qquad a_n=\bar\pi^{\,e_n},\qquad N(a_n)=p^{e_n}.
$$

由于 $\bar\pi$ 是模 $\pi^n$ 的单位，$e_n$ 存在，
并且

$$
 a_n\equiv1\pmod{\pi^n},\qquad
 E[a_n]\cap E[\pi^n]=\{O\}.                                  \tag{5}
$$

对任意奇范数 CM 乘子 $a$，使用
[挠值笔记](2026-11-12-theta-factor-center-torsion-trace.md)
已完整规范的 division 函数

$$
 \Psi_a(P)=a\prod_{T\in(E[a]\setminus\{O\})/\{\pm1\}}
                 (x(P)-x(T))
$$

及精确恒等式

$$
 \Sigma([a]t)=\Sigma(t)^{N(a)}\Psi_a(t).                       \tag{6}
$$

若 $0\ne Q\in E[\pi^n]$，则 $Q$ 位于正式群圆盘中。
$E[a_n]$ 在所选位是 étale 子群，其非零点的 $x$ 坐标整；
故 (6) 的两边都可在 $t(Q)$ 处求值。由 $[a_n]Q=Q$，

$$
 \boxed{\quad
 \Sigma(t(Q))^{p^{e_n}-1}
          =\Psi_{a_n}(Q)^{-1}\in\overline{\mathbb Q}^{\,\times}.
 \quad}                                                       \tag{7}
$$

这证明 $\Sigma(t(Q))$ 是代数数，并完整固定其分支：它是满足

$$
 \frac{\Sigma(t(Q))}{t(Q)}\in1+\mathfrak m_{\mathbb C_p}
                                                               \tag{8}
$$

的唯一根。具体地，
$(\Sigma(t(Q))/t(Q))^{p^{e_n}-1}
=[\Psi_{a_n}(Q)t(Q)^{p^{e_n}-1}]^{-1}\in1+\mathfrak m$，
而指数 $p^{e_n}-1$ 是 $p$-单位，故在 principal-unit 群上取该次根是双射。
这与第一除法层的证明完全相同，未增加一个未指定的根单位。

定义

$$
 V_p(Q)=R(x(Q))\Sigma(t(Q))^d\quad(Q\ne O),\qquad
 V_p(O)=S(0)=0.                                               \tag{9}
$$

每个 $V_p(Q)$ 都是代数数；允许 $R(x(Q))=0$。
这里没有声称所有 $n$ 的值同属一个固定数域。

## 3. 每个剩余类的测度质量都是有限代数 Fourier 和

取本原 $p^n$ 次单位根 $\zeta_n$，并在固定正式群同构下令
$Q_n$ 对应 $\zeta_n-1$。于是 $Q_n$ 生成循环群 $E[\pi^n]$，
且 $\zeta_n^j-1$ 对应 $[j]Q_n$。

对 $a\in\mathbb Z/p^n\mathbb Z$ 定义

$$
 \begin{aligned}
 M_{a,n}
   &=\nu_p(a+p^n\mathbb Z_p)\\
   &=\frac1{p^n}\sum_{j=0}^{p^n-1}
                    \zeta_n^{-aj}V_p([j]Q_n).
 \end{aligned}                                                \tag{10}
$$

**证明。** 有限字符正交性给

$$
 {\bf1}_{a+p^n\mathbb Z_p}(x)
     =\frac1{p^n}\sum_{j=0}^{p^n-1}\zeta_n^{j(x-a)}.
$$

对有界测度积分，使用
$\int\zeta_n^{jx}\,d\nu_p=A_p(\zeta_n^j-1)$ 以及 (9)，即得 (10)。
这只是有限求和，不涉及在挠点把正式对数直接代成零。$\square$

由 (7)–(10)，所有 $M_{a,n}\in\overline{\mathbb Q}$。同时 (4)
给 $v_p(M_{a,n})\ge-B_p$；不能从式 (10) 的外部 $p^{-n}$
因子反向低估这个整性。

## 4. 斜率的有限对数和及准确误差

对每个单位剩余类，选唯一整数代表 $1\le a<p^n$。令

$$
 J_{p,n}=
 \sum_{\substack{1\le a<p^n\\p\nmid a}}M_{a,n}\log_p a ,
 \qquad \log_p p=0.                                          \tag{11}
$$

这是一个有限的代数系数对数线性形式。
实际斜率满足

$$
 \log_p(1+p)\,G_p'(0)
       =\int_{\mathbb Z_p^\times}\log_p x\,d\nu_p(x).          \tag{12}
$$

当 $x\in a+p^n\mathbb Z_p$ 时，$x/a\in1+p^n\mathbb Z_p$，所以

$$
 v_p(\log_p x-\log_p a)\ge n.
$$

把这一一致误差用 (4) 积分，立即得到

$$
 \boxed{\quad
 v_p\!\left(\log_p(1+p)G_p'(0)-J_{p,n}\right)
                     \ge n-B_p .
 \quad}                                                       \tag{13}
$$

特别地，

$$
 G_p'(0)=\lim_{n\to\infty}\frac{J_{p,n}}{\log_p(1+p)},
 \quad
 v_p\!\left(G_p'(0)-\frac{J_{p,n}}{\log_p(1+p)}\right)
                     \ge n-1-B_p .                          \tag{14}
$$

这里 $v_p(\log_p(1+p))=1$。误差界趋于无穷，故已同时证明收敛，
而非只给一个固定精度的同余。

### 逐素数的有限证书

结合 (1)、(13)，

$$
 \boxed{\quad
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
  \iff \exists n\ge1:\quad v_p(J_{p,n})<n-B_p .
 \quad}                                                       \tag{15}
$$

充分性是非阿基米德三角不等式。必要性也严格成立：
若 $G_p'(0)\ne0$，取
$n-B_p>v_p(\log_p(1+p)G_p'(0))$，则 (13) 强迫
$v_p(J_{p,n})$ 等于该固定有限赋值。

除固定有限素数之外，(15) 的门槛就是 $v_p(J_{p,n})<n$。
第一层不能靠一般整性自动成功：
$M_{a,1}$ 整且 $\log_p a\in p\mathbb Z_p$，
所以 $v_p(J_{p,1})\ge1$。

## 5. 每层 Baker–Brumer 能断言什么

把 $a$ 按有理素数分解，则

$$
 J_{p,n}=\sum_{\substack{\ell<p^n\\\ell\ {\rm prime},\ell\ne p}}
             b_{\ell,n}\log_p\ell,\qquad
 b_{\ell,n}=
 \sum_{\substack{1\le a<p^n\\p\nmid a}}
             v_\ell(a)\,M_{a,n}\in\overline{\mathbb Q}.        \tag{16}
$$

这一有限组 $\log_p\ell$ 在 $\mathbb Q$ 上线性无关。
确实，整数关系会给
$\log_p\prod_\ell\ell^{m_\ell}=0$；该乘积是正有理 $p$-单位，
故只能为 $1$，而有理数的素因子分解迫使所有 $m_\ell=0$。
这里使用对数在 $\mathbb Q_p^\times$ 上的核是
$p^\mathbb Z\mu_{p-1}$，且正有理数与 $\mu_{p-1}$ 的交只有 $1$。

Baker–Brumer 定理随后给出精确的有限层等价：

$$
 \boxed{\quad J_{p,n}=0\iff
               b_{\ell,n}=0\text{ 对所有上述 }\ell .\quad}    \tag{17}
$$

所用定理的准确形式及来源已在
[有限层单位非零性笔记 §4](2026-11-12-unit-character-nonvanishing.md)
核对：代数 $p$-进单位的对数若在 $\mathbb Q$ 上线性无关，
就在代数数系数上保持线性无关。可先把各 $\ell$ 提到
$(p-1)$ 次方，使其全部位于对数收敛的 principal-unit 群。

(17) 不替代 (15) 的赋值门槛。即使对每个 $n$ 都证明
$J_{p,n}\ne0$，仍容许

$$
 v_p(J_{p,n})\ge n-B_p\qquad\text{对所有 }n,                  \tag{18}
$$

这正与 $G_p'(0)=0$ 相容。有限层的代数系数及其所属数域随 $n$
变化，不能把所有这些对数和当作一个固定的有限 Baker 线性形式。
要从这条路线得到无穷多个素数，仍须给出对无穷多个 $p$
实际违反 (18) 的算术论证。

## 6. 正式群同构的选择不会改变所需斜率

若把正式群同构改成与 $[u]$ 复合，$u\in\mathbb Z_p^\times$，
则测度变为乘 $u$ 的推前，故

$$
 G_{p,u}(T)=(1+T)^{\log_p\langle u\rangle/\log_p(1+p)}G_p(T).
$$

由已经证明的 $G_p(0)=0$，

$$
 G_{p,u}'(0)=G_p'(0).                                        \tag{19}
$$

因此用于 (10) 的 Tate 模生成元选择不会改变极限斜率。
在任意固定选择下，(10)–(15) 都给同样的非零性判据。
这没有把 $p$-进周期本身宣布为代数数；代数性来自每个有限层的
division 方程 (7)，而不是来自周期的代数性。
