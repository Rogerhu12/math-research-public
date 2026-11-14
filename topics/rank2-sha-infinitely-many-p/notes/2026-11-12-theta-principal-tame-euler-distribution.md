# Theta 主 tame 分量的精确单 Euler 分布关系

日期：2026-11-12。状态：以下测度恒等式、逐权单 Euler 因子及正式群迹关系已证明。它们没有证明中心斜率非零。

本笔记从已证明的中央分支平方及精确 Katz 插值反推一个单因子的分布关系。证明不需要把另一个 CM 域的平方根插值定理套到 $\mathbb Q(i)$，也不需要在每个权重重新选择平方根符号。

## 1. 固定对象与结论

采用 [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)
及 [实结构笔记](2026-11-12-theta-real-structure-and-mellin-square.md)
的同一规范。固定

$$
 p\ge13,\quad p\equiv1\pmod4,\quad p\ne17,\qquad
 \pi=\psi(\mathfrak p),\quad v_p(\pi)=1,\quad \pi\bar\pi=p.
$$

设 $\nu=\nu_p$ 是固定截面 $S$ 的有界 Amice 测度，
$M_m=\int_{\mathbb Z_p}x^m\,d\nu$，$G=G_p$ 是其单位部分的 principal
Mellin 变换。已有

$$
 \nu(\mathbb Z_p)=S(0)=0,\qquad G(0)=0,\qquad G\not\equiv0.
                                                               \tag{1}
$$

对 $u\in\mathbb Z_p$，$[u]_*\alpha$ 表示乘法 $x\mapsto ux$
对测度的推前。令

$$
 \nu^{(0)}
   =\frac1{p-1}\sum_{\epsilon\in\mu_{p-1}}[\epsilon]_*\nu,
 \quad
 \mu=\nu^{(0)}|_{\mathbb Z_p^\times},
 \quad
 a=\frac{\pi}{\bar\pi}\in p\mathbb Z_p^\times,\quad
 c=\bar\pi^{-1}\in\mathbb Z_p^\times .
                                                               \tag{2}
$$

上标 $(0)$ 表示取平凡 tame 字符，不能省略。
平均不改变 $G$；因此 $\mu\ne0$。

**定理。** 作为作用于 $C(\mathbb Z_p,\mathbb C_p)$ 的有界测度，

$$
 \boxed{\quad
 \nu^{(0)}|_{p\mathbb Z_p}
        =c[a]_*\nu^{(0)},\qquad
 \mu=\nu^{(0)}-c[a]_*\nu^{(0)} .
 \quad}                                                       \tag{3}
$$

所以对每个非负整数 $m\equiv0\pmod{p-1}$，

$$
 \boxed{\quad
 G((1+p)^m-1)=
     \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)M_m .
 \quad}                                                       \tag{4}
$$

式 (4) 的平方根符号已统一为正号；没有依赖 $m$ 的未定符号。

## 2. 先得到乘法卷积的平方恒等式

记

$$
 q=\varpi/\bar\varpi,\qquad
 b=f^2/d,
$$

其中 $q$、$f$、$d$ 与实结构笔记相同。该笔记给

$$
 \bar s_m=q^{-m}s_m,\qquad
 F_p^{\Theta,-}(T)
   =\kappa f\Omega_p(1+T)^{\log_p\langle b/q\rangle/
                                  \log_p(1+p)}G(T)^2.
                                                               \tag{5}
$$

而 R46 的精确插值式给，对正整数 $(p-1)\mid m$，

$$
 F_p^{\Theta,-}((1+p)^m-1)
  =\kappa f\Omega_p(b/q)^m
       (1-ca^m)^2M_m^2 .                                    \tag{6}
$$

$b/q$ 在当前位为单位；$m$ 是 $p-1$ 的倍数，所以 (5) 在同一点的
principal-unit 幂正好是 $(b/q)^m$。消去共同非零因子，得

$$
 \left(\int x^m\,d\mu\right)^2
       =\bigl((1-ca^m)M_m\bigr)^2 .                          \tag{7}
$$

置

$$
 \delta=\nu^{(0)}-c[a]_*\nu^{(0)} .
$$

对 $(p-1)\mid m$，$\delta$ 的第 $m$ 矩正是 $(1-ca^m)M_m$。
对其他正整数 $m$，两边测度的第 $m$ 矩都为零，因为它们
$\mu_{p-1}$-不变。对于 $m=0$，(1) 给
$\delta(\mathbb Z_p)=\mu(\mathbb Z_p)=0$。

对有界测度定义乘法卷积

$$
 (\alpha*\beta)(h)=
       \int_{\mathbb Z_p}\int_{\mathbb Z_p}
                      h(xy)\,d\alpha(x)\,d\beta(y).
                                                               \tag{8}
$$

内层积分是连续函数；用局部常值函数的一致逼近可验证交换次序、
交换律及结合律。其第 $m$ 矩是两测度第 $m$ 矩的乘积。
由 (7) 及其余矩的比较，$\mu*\mu$ 与 $\delta*\delta$ 的所有非负整数矩相等。
多项式在 $C(\mathbb Z_p,\mathbb C_p)$ 中稠密，因此

$$
                       \mu*\mu=\delta*\delta .              \tag{9}
$$

此处没有直接从每个数值的平方相等挑选正号。

## 3. 去掉原点后，乘法测度环嵌入一个整域

本节把消去平方根符号需要的代数事实单独证明。
所有测度都假设 $\mu_{p-1}$-不变。对 $k\ge0$，定义

$$
 \mathscr L_k(\alpha)(T)
  =\int_{p^k\mathbb Z_p^\times}
      (1+T)^{\log_p\langle p^{-k}x\rangle/\log_p(1+p)}
                      \,d\alpha(x)\in\mathbb C_p[[T]],
                                                               \tag{10}
$$

并令

$$
 \mathscr R(\alpha)
       =\sum_{k\ge0}\mathscr L_k(\alpha)(T)X^k
       \in\mathbb C_p[[T]][[X]].                             \tag{11}
$$

每个系数都是一个有界 Amice 变换。因为 tame 不变性，
$\mathscr L_k(\alpha)$ 完全确定 $\alpha$ 在第 $k$ 个环带上的限制：
分解
$p^k\mathbb Z_p^\times\simeq\mu_{p-1}\times(1+p\mathbb Z_p)$
后，第一因子上必须是均匀平均，第二因子由 Amice 单射恢复。

乘法把第 $i,j$ 环带送入第 $i+j$ 环带。因此对每个固定 $k$，
只出现有限个 $i+j=k$，从而

$$
 \mathscr R(\alpha*\beta)
                   =\mathscr R(\alpha)\mathscr R(\beta).
                                                               \tag{12}
$$

目标环 $\mathbb C_p[[T]][[X]]$ 是整域。

### 核恰为 $\mathbb C_p\delta_0$

若 $\mathscr R(\alpha)=0$，则 $\alpha$ 在每个环带上的限制为零。
设 $h$ 为连续函数且 $h(0)=0$。给定 $\varepsilon>0$，取 $N$ 使
$|h(x)|_p<\varepsilon$ 对所有 $x\in p^N\mathbb Z_p$ 成立。
函数 $h{\bf1}_{\mathbb Z_p\setminus p^N\mathbb Z_p}$ 支撑于有限个环带，
其积分为零；余项的积分绝对值至多
$\|\alpha\|\varepsilon$。令 $\varepsilon\to0$，得 $\alpha(h)=0$。
对任意连续 $h$，遂有

$$
 \alpha(h)=h(0)\alpha(1).
$$

故 $\alpha=\alpha(1)\delta_0$。反向显然。
这个证明只用有界测度对连续函数的作用，未使用未定义的单点质量，
也未假设可数可加性。

## 4. 由单位环带固定符号，再用总质量去掉原点

对 (9) 应用 $\mathscr R$。由整域性质，

$$
 \mathscr R(\delta)=\mathscr R(\mu)
       \quad\text{或}\quad
 \mathscr R(\delta)=-\mathscr R(\mu).
$$

由于 $v_p(a)=1$，$[a]_*\nu^{(0)}$ 支撑在 $p\mathbb Z_p$，
所以 $\delta|_{\mathbb Z_p^\times}=\mu$。两边 (11) 的 $X^0$ 系数均为
$G(T)\ne0$。特征为零，故负号不可能。于是

$$
 \mathscr R(\delta-\mu)=0,\qquad
 \delta-\mu=C\delta_0
$$

对某个 $C\in\mathbb C_p$ 成立。由 (1)，
$\delta(1)=\mu(1)=0$，所以 $C=0$。这证明 (3)。
积分 $x^m$ 后即得 (4)，包括两边均为零的 $m=0$。

## 5. Amice 形式及正式群的准确迹公式

令 $A^{(0)}(Z)$ 是 $\nu^{(0)}$ 的 Amice 变换。有限 Fourier 投影给

$$
 \boxed{\quad
 \frac1p\sum_{\zeta^p=1}A^{(0)}(\zeta(1+Z)-1)
       =c\,A^{(0)}((1+Z)^a-1).
 \quad}                                                       \tag{13}
$$

所有翻译点均位于开单位圆盘；有界 Amice 级数在那里收敛。
式 (13) 是 (3) 的变换，不是把 $p$-挠点的正式对数代入零。

在 $\widehat E$ 坐标中，写

$$
 \mathscr S_p^{(0)}(t)
   =\frac1{p-1}\sum_{\epsilon\in\mu_{p-1}}
              S(\log_E([\epsilon]t)).
                                                               \tag{14}
$$

每项按 $R(x([\epsilon]t))\Sigma([\epsilon]t)^d$ 的整正式级数解释。
$[\epsilon]$ 是正式群的 $\mathbb Z_p$ 作用，不声称它总来自
全局椭圆曲线的代数自同态。因此 (14) 仍是依赖 $p$ 的 tame 平均。

式 (13) 等价于

$$
 \boxed{\quad
 \sum_{Q\in E[\pi]}\mathscr S_p^{(0)}(P+Q)
        =\pi\,\mathscr S_p^{(0)}([\pi][\bar\pi]^{-1}P).
 \quad}                                                       \tag{15}
$$

这里 $P$ 位于正式群圆盘，$[\bar\pi]$ 在该圆盘是自同构。
系数确为 $pc=\pi$，而不是 $p$ 或 $\bar\pi$。

式 (15) 给出所需主 tame 分量的单 Euler 分布。
它没有断言未平均的固定截面 $S$ 满足同样公式。

## 6. 所有环带由单位分量恢复，但斜率仍留在该分量中

设

$$
 h_p=\frac{\log_p\langle\bar\pi^{-2}\rangle}{\log_p(1+p)}
                    \in\mathbb Z_p .
$$

因为 $a/p=\bar\pi^{-2}$，(3) 与 (10) 给

$$
 \mathscr L_k(\nu^{(0)})(T)
      =c^k(1+T)^{kh_p}G(T),\qquad
 \boxed{\quad
 \mathscr R(\nu^{(0)})
      =\frac{G(T)}{1-cX(1+T)^{h_p}} .
 \quad}                                                       \tag{16}
$$

这是在记录 $p$-进赋值环带的变量 $X$ 上的有理式。
它没有把未知 $G(T)$ 变成 $T$ 的有理函数，
也不能据此给 $G$ 的中心零点阶设上界。

下面给出分布关系本身仍容许任意零阶的准确模型。
固定任意 $r\ge1$，在单位群上取 tame 不变测度

$$
 \mu_r=\left(\frac1{p-1}\sum_{\epsilon\in\mu_{p-1}}\delta_\epsilon\right)
          *(\delta_{1+p}-\delta_1)^{*r}.
$$

其总质量为零，principal Mellin 变换恰为 $T^r$。
对连续函数 $f$ 定义

$$
 \nu_r(f)=\sum_{k\ge0}c^k\int f(a^kx)\,d\mu_r(x).             \tag{17}
$$

由于 $\mu_r(1)=0$，每项可改写成
$c^k\int(f(a^kx)-f(0))\,d\mu_r(x)$。
一致连续性说明这些项趋于零，故非阿基米德级数收敛，
且 $|\nu_r(f)|_p\le\|\mu_r\|\|f\|_\infty$。
因此 (17) 确实定义有界测度。移位求和即得

$$
 \nu_r|_{p\mathbb Z_p}=c[a]_*\nu_r,\qquad
 \nu_r|_{\mathbb Z_p^\times}=\mu_r,\qquad \nu_r(1)=0.
$$

它满足 (3) 的全部分布要求，却有 Mellin 零阶 $r$。
这不是原截面的反例；它精确说明单 Euler 分布与有界性本身
没有排除 $r\ge2$。本题仍需要利用原固定 theta 截面的额外算术，
证明 $G_p'(0)\ne0$ 在无穷多个 $p$ 成立。
