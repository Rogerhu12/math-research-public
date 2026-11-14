# R32：固定辅助素数的 Rubin–Stark 有限层证书

**可信度：已证明。** 沿用 R30 的固定曲线、素数和字符：
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p\equiv1\pmod4,\quad p\ge13,\quad p\ne17.
$$
本文只使用已出版的 Bley 与 Burns–Kurihara–Sano 定理，不使用 Ohshita II 的高阶椭圆单位比较。通过一个对所有 $p$ 都适用的辅助素理想 $(67)$，获得完整类群模的高阶 Fitting 理想的 Rubin–Stark 表达式，并将 R30 的中心非零条件变成有限层证书。尚未证明有无穷多个 $p$ 存在这种证书。

## 1. 记号及主结论

固定 $\pi=\psi_E(\mathfrak p)$，记
$$
K_n=K(E[\pi^n]),\quad
G_n=\operatorname{Gal}(K_n/K)=\Delta\times\Gamma_n,
\quad |\Gamma_n|=p^{n-1}.
$$
$\widetilde\chi:\Delta\to\mathbb Z_p^\times$ 是 $E[\pi]$ 作用字符的 Teichmüller 提升。取 $\gamma$ 满足 $\rho_E(\gamma)=1+p$，令
$$
\Lambda=\mathbb Z_p[[T]],\quad T=\gamma-1,\quad
\omega_n(T)=(1+T)^{p^{n-1}}-1,
\quad R_n=\Lambda/(\omega_n)=\mathbb Z_p[\Gamma_n].
$$
本文的字符分量为 $\Delta$ **通过 $\widetilde\chi$ 作用**的分量，不取逆字符。置
$$
A_n=(\operatorname{Cl}(K_n)\otimes\mathbb Z_p)^{\widetilde\chi},
\qquad \mathcal A=\varprojlim_n A_n.
$$

固定
$$
\mathfrak l=(67),\qquad \mathcal T=\{\mathfrak l\}.
\tag{1.1}
$$
对每个 $n$，取 $S_n=S_\infty(K)\cup S_{\rm ram}(K_n/K)$，$V=\{\infty\}$ 为 $K$ 唯一的复位。第 4 节以这些数据定义 $R_n$ 中的 Rubin–Stark 值理想 $\Theta^{\rm RS}_{i,n}$。则
$$
\boxed{\Theta^{\rm RS}_{i,n}
=\operatorname{Fitt}_{R_n,i}(A_n)\quad(i\ge0,n\ge1).}
\tag{1.2}
$$
这是完整类群的普通高阶 Fitting 理想，不是转置 Selmer 模的相对 Fitting 理想。

有一个自然环同态
$$
e_n:R_n\longrightarrow\mathbb Z_p/p^n\mathbb Z_p,
\qquad T\longmapsto p.
\tag{1.3}
$$
它的存在由 $v_p(\omega_n(p))=n$ 保证。主证书为
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff
\exists n\ge1:\ e_n(\Theta^{\rm RS}_{2,n})\ne0.
\quad}
\tag{1.4}
$$
等价地，存在一个有限层 $K_n$、两个在 $K_n/K$ 完全分裂的辅助素位，以及三个下文规定的 $R_n$-线性同态，使相应秩三 Rubin–Stark 元素的外积取值经 $e_n$ 后非零。这里不要求该值为单位；其估值可以为 $0,\ldots,n-1$ 中的任意值。

## 2. 塔的分歧和固定辅助素理想

### 2.1 BKS 的分歧条件

CM 理论给 $K_n/K$ 交换，以及
$$
K_n\subset K(\mathfrak f\pi^n),\qquad
\mathfrak f=(34(1+i)).
\tag{2.1}
$$
其中右侧为射线类域；本曲线的导子数据已在 R18–R19 使用。由于
$$
\mathfrak f\sim(1+i)^3\cdot17,
\qquad
|({\cal O}_K/\mathfrak f)^\times|
=(8-4)(17-1)^2=1024,
\tag{2.2}
$$
射线类域中位于 $2,17$ 上方的惯性群都是 $2$-群的商。它们映到 $G_n$ 后若非平凡，就不可能包含在 $p$-群 $\operatorname{Gal}(K_n/K_1)$ 中。因此任何这类在 $K_n/K$ 分歧的素位，在 $K_1/K$ 中已有非平凡惯性群。

在 $\mathfrak p$ 处，$K_n/K$ 全分歧，首层 tame 次数为 $p-1$；所以其首层分解群也非平凡。在 $\bar{\mathfrak p}$ 处，$[\pi]$ 的微分是单位，好约化下该同源为 étale，故 $K_n/K$ 在此未分歧。由 (2.1) 没有别的分歧素位。

因此，**每一个在 $K_n/K$ 分歧的有限素位，在最大素于 $p$ 子扩张 $K_1/K$ 中都不完全分裂**。这正是 BKS Theorem 8.1 的条件 $(*)$；因 $\widetilde\chi$ 忠实，它也等价于 BKS Corollary 1.7 所用的非平凡字符条件。

### 2.2 在 $(67)$ 处的准确 Frobenius

$67\equiv3\pmod4$，所以 $\mathfrak l=(67)$ 在 $K$ 中为惰性素理想，范数为 $4489$。它与 $\mathfrak f\pi$ 互素，故所有 $K_n/K$ 都在此未分歧。

对本曲线在 $\mathbb F_{67}$ 的点数，$x$ 与 $-x$ 的配对给
$$
\sum_{x\in\mathbb F_{67}}
\left(\frac{x^3-17x}{67}\right)=0,
$$
因为 $\left(\frac{-1}{67}\right)=-1$。因此 $a_{67}=0$，$67$ 次 Frobenius 的特征多项式为 $X^2+67$。于是对所有与 $67$ 互素的 Tate 模，$\mathfrak l$ 的算术 Frobenius 是其平方，作用为
$$
\rho_E(\sigma_{\mathfrak l})=-67.
\tag{2.3}
$$
特别地，在 $E[\pi]$ 上是 $-67\bmod p$。这也与 R31 的 Hecke 值 $\psi_E((67))=-67$ 一致。

### 2.3 $\mathcal T$-修正单位群无挠

$K_n$ 在 $67$ 上方的完备化是 $\mathbb Q_{67}$ 的未分歧扩张。其主单位群 $1+67\mathcal O$ 无挠：素于 $67$ 的根单位通过剩余域约化单射，而非平凡 $67$ 次根单位会产生分歧扩张。故任何在 $\mathfrak l$ 上方所有素位都约化为 $1$ 的根单位只能为 $1$。

这证明，对任意不含 $\mathfrak l$ 的有限集合 $S'$，群
$$
\mathcal O_{K_n,S',\mathcal T}^{\times}
=\{u\in\mathcal O_{K_n,S'}^\times:
 u\equiv1\pmod w\text{ 对所有 }w\mid\mathfrak l\}
$$
是无挠的。因而固定的 $\mathcal T$ 满足 BKS 的单位无挠条件，包括稍后增加完全分裂辅助素位的各个 $S'$。

## 3. 射线类群修正项在目标字符上消失

模 $\mathfrak l\mathcal O_{K_n}$ 的射线类群存在标准右正合列
$$
\mathcal O_{K_n}^{\times}
\longrightarrow
\prod_{w\mid\mathfrak l}\kappa(w)^\times
\longrightarrow
\operatorname{Cl}^{\mathcal T}(K_n)
\longrightarrow\operatorname{Cl}(K_n)\longrightarrow0.
\tag{3.1}
$$
令 $B_n$ 为中央剩余域乘法群的 $p$-部分。因为 $G_n$ 交换，$\sigma_{\mathfrak l}$ 固定每一个 $w\mid\mathfrak l$，并在每个剩余域上作用为 $x\mapsto x^{4489}$。按加法模记号，
$$
(\sigma_{\mathfrak l}-4489) B_n=0.
\tag{3.2}
$$

写 $\sigma_{\mathfrak l}=\delta\gamma_n^a$，$\delta\in\Delta$。在 $\widetilde\chi$ 分量，(3.2) 的算子是 $R_n$ 的元素
$$
\widetilde\chi(\delta)\gamma_n^a-4489.
$$
$R_n$ 为局部环，极大理想为 $(p,\gamma_n-1)$。这个元素在剩余域的值由 (2.3) 给出：
$$
-67-4489=-4556=-4\cdot17\cdot67\not\equiv0\pmod p.
\tag{3.3}
$$
所以它是 $R_n$ 的单位。单位消灭 $B_n^{\widetilde\chi}$ 只能发生在该模为零时。对 (3.1) 张量 $\mathbb Z_p$ 再取字符分量，得到准确同构
$$
\boxed{
(\operatorname{Cl}^{\mathcal T}(K_n)\otimes\mathbb Z_p)^{\widetilde\chi}
\simeq A_n.}
\tag{3.4}
$$

这也核对了 Euler 因子的方向。BKS 的 $\mathcal T$-修正因子为
$$
1-4489\sigma_{\mathfrak l}^{-1},
$$
它与 (3.2) 的算子相差单位 $\sigma_{\mathfrak l}$。在目标字符的 Iwasawa 环中，该因子是单位，且按 $T=p$ 评价时恰为
$$
1-\frac{4489}{-67}=68.
\tag{3.5}
$$
因此没有隐藏的逆字符、额外 $p$ 因子或需要逐 $p$ 重新选择的辅助素数。

## 4. 已出版的 Bley–BKS 输入及完整模比较

### 4.1 Bley 的范围

Bley，*On the Equivariant Tamagawa Number Conjecture for Abelian Extensions of a Quadratic Imaginary Field*，*Documenta Mathematica* **11** (2006), 73–118，Theorem 4.2 及 Corollary 4.3，证明：若 $p$ 为虚二次域 $k$ 中的奇分裂素数，且 $p\nmid h_k$，则对任意有限交换扩张 $L/k$ 及中间域，所述 $h^0(\operatorname{Spec}L)$ 的 $p$-部分 ETNC 成立。[出版原文](https://ftp.gwdg.de/pub/EMIS/journals/DMJDMV/vol-11/04.pdf)

这里 $k=K=\mathbb Q(i)$，$h_K=1$，$L=K_n$，所以没有额外字符限制。BKS Remark 3.2、Proposition 3.4 与 Conjecture 3.6 后的说明，明确把这一 ETNC 与其 leading-term conjecture $\operatorname{LTC}(K_n/K)$ 识别，并说明它独立于允许的 $S,\mathcal T$。故以下所用 $p$-部分 LTC 是无条件输入。

### 4.2 Rubin–Stark 值理想的准确对象

使用 Burns–Kurihara–Sano，*On zeta elements for $\mathbb G_m$*，*Documenta Mathematica* **21** (2016), 555–626，Corollary 1.7 及其详细版本 Theorem 8.1。[出版原文](https://ems.press/content/serial-article-files/26320?nt=1)

令 $\mathcal V_{i,n}$ 为满足以下条件的集合 $W$ 的全体：

- $W$ 恰含 $i$ 个有限素位；
- 每个素位在 $K_n/K$ 完全分裂；
- $W\cap(S_n\cup\mathcal T)=\varnothing$。

对 $W\in\mathcal V_{i,n}$，置
$$
U_{n,W}=
(\mathcal O_{K_n,S_n\cup W,\mathcal T}^{\times}
\otimes\mathbb Z_p)^{\widetilde\chi},
\qquad H_{n,W}=\operatorname{Hom}_{R_n}(U_{n,W},R_n).
$$
取 BKS §5.1 定义的秩 $1+i$ Rubin–Stark 元素的字符分量
$$
\epsilon_{n,W}^{\widetilde\chi}
\in\bigcap_{R_n}^{1+i}U_{n,W},
\qquad
\bigcap_R^d U:=
\operatorname{Hom}_R\!\left(\bigwedge_R^d\operatorname{Hom}_R(U,R),R\right).
$$
其复 regulator 定义使用 $V\cup W$，其中 $V=\{\infty\}$。Bley 的 ETNC 和 BKS 的定理同时保证所需整性。因此任意
$$
\Phi\in\bigwedge_{R_n}^{1+i}H_{n,W}
$$
都能取整值 $\Phi(\epsilon_{n,W}^{\widetilde\chi})\in R_n$。定义
$$
\Theta^{\rm RS}_{i,n}
=\left\langle
\Phi(\epsilon_{n,W}^{\widetilde\chi}):
W\in\mathcal V_{i,n},\quad
\Phi\in\bigwedge_{R_n}^{1+i}H_{n,W}
\right\rangle_{R_n}.
\tag{4.1}
$$

所有条件已逐项核对：$K_n/K$ 有限交换；$\widetilde\chi$ 非平凡且忠实于素于 $p$ 部分 $\Delta$；第 2.1 节验证全部分歧素位的首层条件；$S_n$ 恰为复位和分歧位；$V$ 是所有完全分裂的复位且 $|V|=1$；$\mathcal T$ 与 $S_n$ 不交且第 2.3 节给单位无挠；第 4.1 节给所需字符的 LTC。

因此 BKS Theorem 8.1 直接给
$$
\Theta^{\rm RS}_{i,n}
=\operatorname{Fitt}_{R_n,i}
\bigl((\operatorname{Cl}^{\mathcal T}(K_n)\otimes\mathbb Z_p)^{\widetilde\chi}\bigr).
\tag{4.2}
$$
再用 (3.4)，便得 (1.2)。

为明确没有把别的模误当成类群，BKS 的证明先从转置 Selmer 模出发，但在这里位于有限分歧素位上方的置换模的字符分量全为零，复位部分则是自由秩一 $R_n$-模。因此其 Theorem 8.1 的最终左端就是 (4.2) 的**完整射线类群**。本证明引用的是这个已完成修正的定理；没有自行删除相对 Fitting 下标或假定转置操作不影响理想。BKS 使用的张量字符分量也正是本文的 $\widetilde\chi$，其公式没有再取 involution。

## 5. 范数控制、Fitting 基变换与逆极限

本塔在 $\mathfrak p$ 处只有一个素位且全分歧；$K_n/K_1$ 在其他素位未分歧。Rubin Lemma 11.1 的范数控制，已在 R30 使用，给所有 $n\ge1$ 的准确同构
$$
\mathcal A/\omega_n\mathcal A\simeq A_n.
\tag{5.1}
$$
这里仍是完整理想类群，而不是先商掉 $\mathfrak p$ 类的模。

令
$$
I_i=\operatorname{Fitt}_{\Lambda,i}(\mathcal A).
$$
有限呈现矩阵的子式与任意基变换相容，故 (5.1) 和 (1.2) 给
$$
\Theta^{\rm RS}_{i,n}
=(I_i+(\omega_n))/(\omega_n).
\tag{5.2}
$$
于是有限层值理想自动按 $R_{n+1}\to R_n$ 相容。定义
$$
\Theta^{\rm RS}_{i,\infty}
=\{F\in\Lambda:F\bmod\omega_n\in\Theta^{\rm RS}_{i,n}
\text{ 对所有 }n\}.
$$
则
$$
\boxed{\Theta^{\rm RS}_{i,\infty}=I_i.}
\tag{5.3}
$$

证明这个等式不需要为每个层的 Rubin–Stark 元素及同态先选出相容提升。事实上，(5.2) 给左端为 $\bigcap_n(I_i+(\omega_n))$。记 $\mathfrak m=(p,T)$；由 $\omega_1=T$ 及
$$
\omega_{n+1}=(1+\omega_n)^p-1
$$
归纳得到 $\omega_n\in\mathfrak m^n$。而有限生成 $\Lambda$-模 $\Lambda/I_i$ 是 $\mathfrak m$-进分离的，故
$$
\bigcap_n(I_i+(\omega_n))
\subset\bigcap_n(I_i+\mathfrak m^n)=I_i.
$$
反向包含显然。这也表明 (5.3) 是准确理想等式，没有伪零或高度二误差。

## 6. 中心评价的有限精度及有限层证书

提升指数公式给
$$
v_p\big((1+p)^{p^{n-1}}-1\big)=n.
\tag{6.1}
$$
因此 $\omega_n(p)=0$ 在 $\mathbb Z_p/p^n$ 中成立，(1.3) 的 $e_n$ 是良定义环同态。对 $R_n$ 的元素选不同 $\Lambda$ 提升，其 $T=p$ 值的差都是 $p^n$ 的倍数。

记 $\operatorname{ev}_p:\Lambda\to\mathbb Z_p$ 为 $T\mapsto p$。由 (5.2)，
$$
e_n(\Theta^{\rm RS}_{i,n})
=\bigl(\operatorname{ev}_p(I_i)+p^n\mathbb Z_p\bigr)
/p^n\mathbb Z_p.
\tag{6.2}
$$
若 $\operatorname{ev}_p(I_i)=(p^{b_i})$，其中 $b_i\in\mathbb Z_{\ge0}\cup\{\infty\}$，则
$$
e_n(\Theta^{\rm RS}_{i,n})
=p^{\min(b_i,n)}\mathbb Z_p/p^n\mathbb Z_p.
\tag{6.3}
$$
所以
$$
I_i\not\subset(T-p)
\iff b_i<\infty
\iff \exists n:\ e_n(\Theta^{\rm RS}_{i,n})\ne0.
\tag{6.4}
$$
取 $i=2$，再用 R30，得到 (1.4)。

此外，因为 (4.1) 是由具体外积取值生成的理想，若其像非零，就至少有一个生成值像非零。每个外积又是纯外积的有限和，所以可取三个实际同态 $\phi_0,\phi_1,\phi_2\in H_{n,W}$，使
$$
\boxed{
 e_n\bigl((\phi_0\wedge\phi_1\wedge\phi_2)
 (\epsilon_{n,W}^{\widetilde\chi})\bigr)\ne0
 \quad\text{于 }\mathbb Z_p/p^n.
}
\tag{6.5}
$$
反过来，任何这样的有限数据都给出 $I_2$ 中一个中心值非零的提升，因此证明 $\Sha[p^\infty]$ 有限。这里只使用**理想元素**的提升；未断言所选三个同态、两个辅助素位或 Rubin–Stark 元素本身在塔中有相容提升。

当 $n=1$ 时，证书要求一个模 $p$ 的非零值，等价于 $I_2=\Lambda$，于是 R30 给更强的 $\Sha[p^\infty]=0$。允许任意 $n$ 恰好保留了有限非零初级群的可能性。

## 7. 固定的修正素数与必须变化的分裂素数

固定 $\mathcal T=\{(67)\}$ 消除了射线类群修正，并不是预先固定了 (6.5) 中的两个完全分裂素位。后者一般必须随 $p,n$ 变化。

具体地，若预先固定一个不在 $2,17$ 上方的素理想 $\mathfrak q$，则对 $p$ 不等于其剩余特征，$\mathfrak q$ 在 $K_1/K$ 完全分裂必有
$$
\psi_E(\mathfrak q)\equiv1\pmod\pi,
\qquad
p\mid N_{K/\mathbb Q}(\psi_E(\mathfrak q)-1).
\tag{7.1}
$$
右端是固定非零整数，因为 $|\psi_E(\mathfrak q)|^2=N\mathfrak q>1$。因此一个预先固定的有限素理想集合只能为有限多个目标 $p$ 提供所需完全分裂素位。这不妨碍按 Chebotarev 逐 $p,n$ 选择无限多个候选；但候选存在不保证 (6.5) 的评价非零。

同样，复 regulator 所定义的 Rubin–Stark 元素在有限阶字符处非零，不能直接推出 (6.5)：$T=p$ 并不是 $R_n\otimes\mathbb Q_p$ 的一个特征值，只有模 $p^n$ 的评价才良定义。其有限层非零性需要精度控制。

因而本文完成的是一个无条件、来源闭合、可用有限数据验证的算术接口。要完成课题，仍须对无穷多个 $p$ 构造至少一个满足 (6.5) 的有限证书，或以其他论证保证其存在。

## 来源

- W. Bley，*On the Equivariant Tamagawa Number Conjecture for Abelian Extensions of a Quadratic Imaginary Field*，Doc. Math. **11** (2006), 73–118，Theorem 4.2、Corollary 4.3；[出版原文](https://ftp.gwdg.de/pub/EMIS/journals/DMJDMV/vol-11/04.pdf)，[DOI](https://doi.org/10.4171/DM/205)。
- D. Burns、M. Kurihara、T. Sano，*On zeta elements for $\mathbb G_m$*，Doc. Math. **21** (2016), 555–626，Corollary 1.7、Remark 3.2、Proposition 3.4、§5.1、Theorem 8.1；[出版原文](https://ems.press/content/serial-article-files/26320?nt=1)，[DOI](https://doi.org/10.4171/DM/540)。
- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，CM reciprocity 及 Lemma 11.1；[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- 本仓库 R18–R19、R27、R30–R31：本曲线导子与字符约定、准确 Selmer 控制、中心类群判据及辅助 $(67)$ 的一致规范。
