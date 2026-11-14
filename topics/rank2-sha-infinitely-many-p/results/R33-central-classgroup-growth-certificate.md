# R33：中心有限类群商的满阶循环因子证书

**可信度：已证明。** 日期：2026-11-12。沿用 R30–R32 的
$E:y^2=x^3-17x$、$K=\mathbb Q(i)$ 和分裂素数
$p\ge13,\ p\ne17$。

R32 将初级有限性化成某个有限层的 Rubin–Stark 值非零。
本结果给同样无条件、但无需先计算 Rubin–Stark 元素的有限群证书：
在一个明确的有限类群商中，阶**恰为 $p^n$** 的循环因子至多两个，
已经足以证明 $\Sha[p^\infty]$ 有限。
还给出这个检测首次成功的准确层数，以及它与 R32 所需精度的关系。
没有证明成功素数无穷。

## 1. 全部对象均由有限层定义

记
$$
K_n=K(E[\pi^n]),\qquad
A_n=(\operatorname{Cl}(K_n)\otimes\mathbb Z_p)^{\widetilde\chi},
$$
其中 $\widetilde\chi$ 和生成元 $\gamma$ 的约定与 R32 相同：
$\rho_E(\gamma)=1+p$，
$\Gamma_n=\langle\gamma_n\rangle$ 的阶为 $p^{n-1}$。
定义有限群
$$
\boxed{\quad
C_{p,n}=A_n/(\gamma_n-(1+p))A_n\quad(n\ge1).
\quad}
\tag{1}
$$
式中的整数 $1+p$ 按加法模的标量作用。
因此它不是把 $\gamma_n$ 直接当作一个在 $\mathbb Q_p$ 中的有限阶字符。
令 $C_{p,0}=0$，并置
$$
\ell_{p,n}=\log_p|C_{p,n}|,\qquad
d_{p,n}=\ell_{p,n}-\ell_{p,n-1}\quad(n\ge1).
\tag{2}
$$

**主结论。** 每个 $C_{p,n}$ 被 $p^n$ 杀死；由范数得到的自然映射
$C_{p,n}\to C_{p,n-1}$ 是满射，而且
$$
\boxed{\quad
d_{p,n}=\dim_{\mathbb F_p}p^{n-1}C_{p,n}.
\quad}
\tag{3}
$$
右端等于 $C_{p,n}$ 的初等因子分解中，循环因子
$\mathbb Z/p^n\mathbb Z$ 的个数。
数列 $d_{p,n}$ 单调不增，并且最终恒等于 R30 的 $q_p$。
特别地，
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff \exists n\ge1:\ d_{p,n}\le2.
\quad}
\tag{4}
$$

所以一个层 $K_n$ 的完整有限群数据便可给证书，
不必先知道这个数列已经稳定，也不必证明该初级群为零。

## 2. 有限商与中心模的准确关系

令
$$
\mathcal A_p=\varprojlim_n A_n,\qquad
C_p=\mathcal A_p/(T-p)\mathcal A_p,\qquad T=\gamma-1.
$$
R25、R30 证明 $\mathcal A_p$ 是有限生成 $\mathbb Z_p$-模的商，
所以 $C_p$ 是有限生成 $\mathbb Z_p$-模。
R32 的准确范数控制为
$$
\mathcal A_p/\omega_n(T)\mathcal A_p\simeq A_n,
\qquad
\omega_n(T)=(1+T)^{p^{n-1}}-1.
\tag{5}
$$
这里没有先商去某些分歧素位的类。
把 (5) 再商去 $T-p$ 得到
$$
C_{p,n}\simeq C_p/\omega_n(p)C_p.
$$
由提升指数公式，
$$
v_p(\omega_n(p))=
v_p\bigl((1+p)^{p^{n-1}}-1\bigr)=n.
$$
于是有自然同构
$$
\boxed{\quad C_{p,n}\simeq C_p/p^nC_p.\quad}
\tag{6}
$$
同构兼容范数：$n$ 到 $n-1$ 的映射对应自然约化。
这同时证明 (1) 的群被 $p^n$ 杀死，无须在其定义里额外加入 $p^n$ 关系。

注意 $C_p$ 是**处处无分歧类群模**的中心商；
它不同于 R27 中原始分歧 Galois 模 $M_p$ 的中心商。
本结果不把 $C_p$ 的有限挠子直接认作 Sha 的有限部分。
两者与 Selmer 的准确连接使用 R30 的
$s_{\infty,p}=2\lceil q_p/2\rceil$。

## 3. 增长公式与无需等待稳定的证书

写出 $\mathbb Z_p$-模结构
$$
C_p\simeq
\mathbb Z_p^{q_p}\oplus
\bigoplus_{j=1}^{t_p}\mathbb Z_p/p^{a_j}\mathbb Z_p,
\qquad
1\le a_1\le\cdots\le a_{t_p}.
\tag{7}
$$
式中的分解不要求规范；秩与指数多重集是规范不变量。
由 (6)，
$$
C_{p,n}\simeq
(\mathbb Z/p^n\mathbb Z)^{q_p}\oplus
\bigoplus_{j=1}^{t_p}
\mathbb Z/p^{\min(a_j,n)}\mathbb Z,
\tag{8}
$$
故
$$
\ell_{p,n}=q_pn+\sum_j\min(a_j,n),
\tag{9}
$$
以及
$$
\boxed{\quad
d_{p,n}=q_p+\#\{j:a_j\ge n\}.
\quad}
\tag{10}
$$
特别地 $d_{p,1}=q_p+t_p=c_p$，与 R30 的首层维数一致。
此外
$$
d_{p,n}-d_{p,n+1}=\#\{j:a_j=n\}\ge0.
\tag{11}
$$
所以 $d_{p,n}$ 单调不增，最终等于 $q_p$。
对 (8) 乘以 $p^{n-1}$，只有阶恰为 $p^n$ 的循环因子留下一个
$\mathbb F_p$ 维数，正是 (10)。这证明 (3)。
也可从约化映射的核
$p^{n-1}C_p/p^nC_p$ 直接得到。

R30 已证明 $q_p\ge1$，且初级有限当且仅当 $q_p\le2$。
若某个 $d_{p,n}\le2$，则 (10) 立即给 $q_p\le2$；
即便尚未知道后续数列，也已足够。
反过来，若 $q_p\le2$，取 $n>\max_j a_j$ 就有
$d_{p,n}=q_p\le2$。空的挠子和取 $n=1$。
由此证明 (4)。

另有较弱但有时方便的纯阶数证书：
$$
|C_{p,n}|<p^{3n}
\quad\Longrightarrow\quad
\Sha[p^\infty]\text{ 有限}.
\tag{12}
$$
这是因为 $q_p\ge3$ 会由 (9) 强迫
$\ell_{p,n}\ge3n$。
若初级有限，(12) 也会在足够大 $n$ 成立；
但在同一个层，它可能弱于 (3)–(4)。

## 4. 最早成功层与 Rubin–Stark 证书精度

假设 $q_p\le2$，令 $r=q_p+t_p=c_p$。
如果 $r\le2$，则 $d_{p,1}\le2$，最早成功层为一。
如果 $r>2$，则 $r-2\le t_p$，而 (10) 给
$$
\boxed{\quad
n_{\rm cyc}=1+a_{r-2}.
\quad}
\tag{13}
$$
证明如下：$d_{p,n}\le2$ 恰好表示至少 $r-2$ 个有限挠子指数小于 $n$；
按 (7) 的递增顺序，恰好是 $a_{r-2}<n$。
若 $q_p\ge3$，所有层都失败，把 $n_{\rm cyc}$ 记为 $\infty$。

再比较 R32。令
$$
I_2=\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p),
\qquad
\operatorname{ev}_p:\Lambda\to\mathbb Z_p,\quad T\mapsto p.
$$
Fitting 理想与任意基变换相容，所以
$$
\operatorname{ev}_p(I_2)
=\operatorname{Fitt}_{\mathbb Z_p,2}(C_p).
\tag{14}
$$
对 (7) 的对角呈现直接取余阶二子式：
若 $q_p\ge3$，所有相关子式为零；
若 $q_p\le2$，则
$$
\operatorname{ev}_p(I_2)=(p^{b_p}),\qquad
b_p=
\begin{cases}
0,&r\le2,\\
\displaystyle\sum_{j=1}^{r-2}a_j,&r>2.
\end{cases}
\tag{15}
$$
因此 R32 的值理想在模 $p^n$ 中首次非零的层是
$$
\boxed{\quad n_{\rm RS}=b_p+1.\quad}
\tag{16}
$$
由 (13)–(16) 得
$$
n_{\rm cyc}\le n_{\rm RS}.
\tag{17}
$$
两种证书都等价于初级有限；它们在给定层要求的精度不同。
这里没有断言 R32 外积值本身计算起来更难，也没有把有限群分解
当成免费可得的数据。

例如，仅为说明两种检测的代数差别，取
$$
C=\mathbb Z_p^2\oplus(\mathbb Z/p^N\mathbb Z)^2.
$$
则满阶循环因子证书在 $n=N+1$ 首次成功，而
$\operatorname{Fitt}_2(C)=(p^{2N})$ 的非零模值须到 $n=2N+1$ 才出现。
这是模论例子，不声称每个 $N$ 都由本曲线的算术实现。

## 5. 只用有限整矩阵核验证书

若已经准确给出
$$
A_n\simeq\bigoplus_{j=1}^{s}\mathbb Z/p^{b_j}\mathbb Z
$$
及 $\gamma_n$ 的作用矩阵 $G$，则 (1) 的一个整数呈现矩阵为
$$
\left[
\operatorname{diag}(p^{b_1},\ldots,p^{b_s})
\ \middle|\ G-(1+p)I_s
\right].
\tag{18}
$$
改变 $G$ 的整数提升不改变所呈现的商。
取 Smith 标准形后，全部非平凡初等因子是 $p^{e_j}$，
且 (6) 保证 $e_j\le n$。
只须数出其中 $e_j=n$ 的个数；若至多两个，就获得 (4) 的证书。
若不是，不能据此宣称初级无限，因为尚可能有很深但有限的挠子指数。

有限字符分量也只需有限精度：
若 $p^B A_n=0$，整幂等元
$$
e_{\widetilde\chi}
=\frac1{p-1}\sum_{\delta\in\Delta}
\widetilde\chi(\delta)^{-1}\delta
$$
可在 $\mathbb Z/p^B\mathbb Z$ 中准确计算。
因此 (18) 无须输入未确定精度的无限 $p$-进数。

当证书成功，R7 还给
$$
\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]
=2\left\lceil\frac{d_{p,1}}2\right\rceil-2,
\tag{19}
$$
因为此时整个初级群已有限。
式 (19) 只给 $p$-秩，不给其元素阶或群阶；
后者仍需 R27 的实际分歧模中心 Smith 数据或其他算术信息。

## 6. 尚需研究的跨素数输入

现在一个保留原任务宽度的完整开放命题是：
$$
\#\left\{p:\ \exists n\ge1,\
\dim_{\mathbb F_p}p^{n-1}
\frac{A_n}{(\gamma_n-(1+p))A_n}\le2\right\}=\infty.
$$
这与 R30 的 $q_p\le2$ 无穷性等价。
本文允许层数随 $p$ 变化，也不要求统一的初级群阶上界；
但尚未证明这种有限层证书对无穷多个 $p$ 存在。
固定首层维数本身不限制挠子指数，因此不能把某次有限层失败
或一个人为的层数截止作为无限性结论。

## 依赖与来源

- R25、R30：$\mathcal A_p$ 的有限生成性、$q_p$ 与初级有限的准确关系、
  $c_p$ 的首层维数及字符约定。
- R32 第 5–6 节：Rubin 范数控制的准确形式、Fitting 基变换及
  $v_p(\omega_n(p))=n$。
- K. Rubin，*Elliptic Curves with Complex Multiplication and the
  Conjecture of Birch and Swinnerton-Dyer*，1999，Lemma 11.1：
  [原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- 本文其余步骤均由有限生成 $\mathbb Z_p$-模结构和整数矩阵呈现逐项证明。
