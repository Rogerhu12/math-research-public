# 固定 CM sigma 级数、严格高度及惰性素数的首个分母

后续 [R38](../results/R38-exact-inert-sigma-size-and-jet-budget.md) 已把这里的惰性上界加强为准确半径和 size，并给出无限分母列及完整 jet 渐近。

**可信度：本文各命题已证明；最后的跨素数高度输入仍缺。** 日期：2026-11-12。固定
$$
E:y^2=x^3-17x,\qquad \omega=\frac{dx}{2y},\quad
t=-x/y,\quad D=d/\omega.
$$

本笔记把 R35 的严格 MW 线放入实际的普通高度公式。所有普通分裂素数的 Mazur–Tate sigma 函数确实是同一有理形式级数；但相应高度的求值点及严格方向系数仍随 $p$ 改变。还给出该固定级数在每个惰性好素数处第一个非整系数，故不能把形式群高度二直接当成该 sigma 图像的可求和整性。

## 1. 全部普通分裂素数共有一个 sigma 级数

存在唯一奇级数 $\Sigma(t)\in t+t^2\mathbb Q[[t]]$ 满足
$$
D^2\log\Sigma=-x.
\tag{1.1}
$$
这里 $D\log\Sigma=D\Sigma/\Sigma$，不需要赋予 $\log t$ 形式常数。唯一性可在 $z=\log_E(t)$ 中看出：若 $x(z)=z^{-2}+O(z^2)$，则 (1.1) 唯一给出
$$
\Sigma(t(z))
=z\exp\left(-\int_0^z\int_0^u
\bigl(x(v)-v^{-2}\bigr)\,dv\,du\right).
\tag{1.2}
$$
奇性排除积分产生的一次项，规定 (1.1) 排除二次项，首项规定乘法常数；全部系数有理。

**命题 1。** 对每个好素数 $p\ge5$、$p\equiv1\pmod4$，
$$
\boxed{\quad \sigma_p(t)=\Sigma(t)\in t\mathbb Z_p[[t]].\quad}
\tag{1.3}
$$

**证明。** Mazur–Tate 唯一性定理给一个奇级数 $\sigma_p=t+\cdots\in\mathbb Z_p[[t]]$，使
$$
D^2\log\sigma_p=-x+c_p,\qquad c_p\in\mathbb Z_p.
$$
准确的已出版陈述见 Blakestad–Grant，Theorem 8、Remark 11、Theorem 30。

由于 $i\in\mathbb Z_p$ 且 $[i](x,y)=(-x,iy)$，有
$$
[i]^*t=it,\quad [i]^*x=-x,\quad[i]^*\omega=i\omega.
$$
因此 $\widetilde\sigma(t)=\sigma_p(it)/i$ 也奇、整、首项为 $t$，且
$$
D^2\log\widetilde\sigma
=i^2[i]^*(D^2\log\sigma_p)=-x-c_p.
$$
唯一性迫使 $\widetilde\sigma=\sigma_p$，故 $c_p=-c_p=0$。再由 (1.1) 的特征零唯一性得到 (1.3)。证毕。

同时
$$
\Sigma(it)=i\Sigma(t),\qquad
\Sigma(t)=t\left(1+\sum_{n\ge1}b_nt^{4n}\right).
\tag{1.4}
$$
在 Harvey §2.1 的规范中，常数为 $(a_1^2+4a_2-E_2)/12$；对本模型亦得到 $E_2(E,\omega)=0$。这与 universal-extension-log-determinants 笔记的固定单位根补空间 $\mathbb Q_p[x\omega]$ 相容。

## 2. 一个完全有理的递推及每处正收敛半径

由曲线方程直接得到
$$
x(t)=\frac{1+\sqrt{1+68t^4}}{2t^2},\qquad
\omega=w(t)\,dt,\qquad
w(t)=(1+68t^4)^{-1/2}=\sum_{n\ge0}w_nt^{4n},
$$
$$
w_n=(-1)^n\binom{2n}{n}17^n\in\mathbb Z.
\tag{2.1}
$$
尤其 $xw=(1+w)/(2t^2)$。将 (1.1) 积分一次，奇性给
$$
D\log\Sigma
=\frac1t-\frac12\sum_{n\ge1}\frac{w_n}{4n-1}t^{4n-1}.
\tag{2.2}
$$
令 $\log(\Sigma/t)=\sum_{n\ge1}c_nt^{4n}$，再乘 $w$ 并积分，得到
$$
\boxed{\quad
c_n=\frac1{4n}\left(w_n-\frac12\sum_{j=1}^n
\frac{w_{n-j}w_j}{4j-1}\right),\qquad
b_0=1,\quad nb_n=\sum_{j=1}^n j c_jb_{n-j}.
\quad}
\tag{2.3}
$$
例如
$$
\Sigma(t)=t-\frac{85}{12}t^5
+\frac{407779}{2016}t^9
-\frac{907897835}{114048}t^{13}+O(t^{17}).
$$

每个固定有限素数 $p$ 都有
$$
v_p(c_n)\ge-v_p(8n)-\max_{1\le j\le n}v_p(4j-1)
\ge-O(\log n).
\tag{2.4}
$$
故 $\sum c_nt^{4n}$ 在每个 $p$-进开单位圆盘上收敛；充分缩小圆盘后，其值落入指数函数的收敛域。因此 $\Sigma$ 在每个 $p$ 处具有正收敛半径。这里不把正半径等同于整系数或 adelic 大小条件。

## 3. 惰性素数的首个坏系数准确在次数 p+2

**命题 2。** 设 $p\ge7$、$p\equiv3\pmod4$，$r=(p+1)/4$。则
$$
b_0,\ldots,b_{r-1}\in\mathbb Z_p,\qquad
v_p(b_r)=-1,\qquad
\boxed{\quad p b_r\equiv-\frac{w_r}{2}\pmod p.\quad}
\tag{3.1}
$$
由于 $4r+1=p+2$，这是 $\Sigma$ 第一个非整系数。

**证明。** 对 $n<r$，(2.3) 中的 $4n$、$4j-1$ 全不被 $p$ 整除，故 $c_n$ 为 $p$ 整数。因为 $r<p$，指数展开中涉及的阶乘也都是 $p$ 单位，得 $b_n\in\mathbb Z_p$。

在 $n=r$ 时，唯一分母含 $p$ 的项是 $j=r$，其中 $4r-1=p$。由 $2r=(p+1)/2<p$，$w_r$ 为 $p$ 单位。因此
$$
p c_r\equiv-\frac{w_r}{2(4r)}
\equiv-\frac{w_r}{2}\pmod p.
$$
展开指数时 $b_r-c_r$ 是先前 $c_1,\ldots,c_{r-1}$ 的 $p$ 整多项式，因为相关阶乘指标至多 $r<p$。这证明 (3.1)。证毕。

### 3.1 这是实际图像 size 的上界

令 $\widehat C$ 为 $E\times\mathbb A^1$ 在 $(O,0)$ 处的图像 $Y=\Sigma(t)$。在好素数处 $t$ 给出沿 $O$ 的整 étale 坐标。Bost–Chambert-Loir Theorem 3.1 的 étale 不变性和 Proposition 3.5(2) 给
$$
S_p(\widehat C)=
\min\left(1,
\inf_{n\ge1}|b_n|_p^{-1/(4n)}\right),
\tag{3.2}
$$
其中忽略 $b_n=0$ 的项；所需 $\Sigma'(0)=1$ 和正半径已证。由 (3.1)，
$$
\boxed{\quad
S_p(\widehat C)\le p^{-1/(p+1)}
\quad(p\equiv3\pmod4,\ p\ge7).
\quad}
\tag{3.3}
$$
普通处 (1.3) 给 $S_p=1$；惰性处的损失已经不可能统一换成 $O(\log p/p^2)$。事实上
$$
\sum_{p\equiv3\ (4)}\log S_p^{-1}
\ge\sum_{p\equiv3\ (4),\ p\ge7}\frac{\log p}{p+1}
=\infty,
$$
最后用该固定算术级数中的素数定理。因此这个固定 sigma 图像不是 $A$-analytic。不能从普通处全整及形式群高度二推断其已经满足 Bost 的 adelic 输入。

## 4. 实际普通高度确实能用同一 Σ 计算

以下采用 Harvey 的高度规范；它等于 Mazur–Stein–Tate 文中规范的 $2p$ 倍。设 $C$ 是本曲线全部 Tamagawa 数的最小公倍数，取
$$
N_p=\operatorname{lcm}(\#E(\mathbb F_p),C).
$$
对任一非挠 $R\in E(\mathbb Q)$，$[N_p]R$ 在 $p$ 处约化为 $O$，在所有坏素数处属于恒等分支。以
$$
x([N_p]R)=a_R/d_R^2,\qquad
y([N_p]R)=b_R/d_R^3,\qquad d_R>0
$$
表示互素坐标。Harvey 已发表版本 §2.2、式 (2) 和二次齐次性给
$$
\boxed{\quad
h_p(R)=\frac{2}{N_p^2}
\log_p\frac{\Sigma(t([N_p]R))}{d_R}.
\quad}
\tag{4.1}
$$
$\log_p$ 取 Iwasawa 分支。公式中没有未知的 $E_2$ 或额外 sigma 归一化常数。

设 $s_{R,p}=\log_p(\Sigma(t([N_p]R))/d_R)$，令 $\ell_P=\log_E(P)$、$\ell_Q=\log_E(Q)$，以及 $v_p=\ell_QP-\ell_PQ$。把 $h_p$ 极化为对称双线性配对后，直接计算得到
$$
\boxed{\quad
h_p(v_p)=\frac{2}{N_p^2}\left[
(\ell_Q^2+\ell_P\ell_Q)s_{P,p}
+(\ell_P^2+\ell_P\ell_Q)s_{Q,p}
-\ell_P\ell_Qs_{P+Q,p}\right].
\quad}
\tag{4.2}
$$
因此它确实成为**三个 sigma 对数的线性组合**，但没有成为 Baker–Brumer 所需的代数系数形式。

准确地，置 $r_p=\ell_Q/\ell_P$，由 Bertrand-height-and-completed-strict-line 笔记已证 $r_p$ 超越。去掉公共因子后，(4.2) 的系数为
$$
(r_p^2+r_p,\ 1+r_p,\ -r_p).
\tag{4.3}
$$
不存在非零 $c\in\mathbb C_p$ 使这三个系数同时落入 $\overline{\mathbb Q}$：前两个非零系数之比正好是 $r_p$，与其超越性矛盾。因此仅乘一个归一化因子不能使 (4.2) 变成代数系数线性形式。此外，(4.1) 中的 sigma 值首先是解析值，这里没有证明它们是代数数。

固定 $\Sigma$ 也不固定求值点：$N_p$、$[N_p]P$、$[N_p]Q$、$[N_p](P+Q)$ 均随 $p$ 改变。Néron–Tate 实高度的正定性没有给出这些不同局部取值的代数共同值。若要用全局高度或超越性补足 R36 的 $G_p(p)$ 非零，仍需一个新的比较或非零定理；(1.3) 与 (4.2) 本身不提供它。

## 来源

- C. Blakestad、D. Grant，*On the universal p-adic sigma and Weierstrass zeta functions*，J. Number Theory **249** (2023)，348–376，Theorem 8、Remark 11、Theorem 30，[作者全文](https://euclid.colorado.edu/~grant/publications/P_adic_sigma_function-published)，[DOI](https://doi.org/10.1016/j.jnt.2023.01.013)。仅将其 sigma 存在唯一性作为外部输入；CM 固定性和惰性首个分母为本文计算。
- D. Harvey，*Efficient computation of p-adic heights*，LMS J. Comput. Math. **11** (2008)，40–59，§2.1–§2.2，出版式 (1)–(2)，[DOI及原文](https://doi.org/10.1112/S1461157000000528)。[作者预印本](https://arxiv.org/pdf/0708.3404) 的同一高度式编号为 (3)，勿混用。
- J.-B. Bost、A. Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，Theorem 3.1、Proposition 3.5(2)、Definition 3.7，[作者全文](https://arxiv.org/pdf/math/0702593)。
- B. Mazur、W. Stein、J. Tate，*Computation of p-adic heights and log convergence*，Doc. Math. Extra Volume (2006)，577–614，[DOI](https://doi.org/10.4171/DMS/4/17)。高度公式的准确常数在本笔记按 Harvey 的出版版本使用。
