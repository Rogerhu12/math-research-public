# R66：小惯性三次商的精确导子、非消失范围与 Tate 分母

日期：2026-11-12。状态：**已证明的结构与必要条件；主问题未完成。**

本文独立推导实际小惯性分支的三次商导子与分母分裂条件，再接上 Feigon–Whitehouse 已发表的中心值平均公式。Studnia 的 submitted 论文 B/D 不作为本文证明输入；其准确条件单独保留在[接口笔记](../notes/2026-11-12-studnia-small-inertia-and-cubic-character-resume2.md)。

## 1. 设置与主结论

设 $E/\mathbb Q$ 无 CM，$p>37$ 为异常素数，采用 R1、R5 的完整实际像
$$\rho_{E,p}(G_{\mathbb Q})=N=C\rtimes\langle c\rangle,
\qquad C\simeq\mathbb F_{p^2}^{\times}.$$
商域 $K$ 虚二次，$p$ 在 $K$ 不分歧且惰性。令
$$\lambda:G_K\twoheadrightarrow\mathbb F_{p^2}^{\times},
\qquad \chi_K:G_{\mathbb Q}\longrightarrow\{\pm1\},
\qquad D=|D_K|.$$

本文假设
$$\rho_{E,p}(I_p)\subsetneq C.\tag{1.1}$$
第 2 节仅用 R21 和已发表的椭圆曲线局部理论证明
$$p\equiv2,5\pmod9,\qquad \rho_{E,p}(I_p)=C^3.\tag{1.2}$$
选阶恰为 $3$ 的复字符 $\vartheta:C\to\mu_3$，并定义
$$\eta=\vartheta\circ\lambda,
\qquad r=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\eta,
\qquad L=\overline{\mathbb Q}^{\ker r}.$$
这里 $\eta$ 是本文的**三次商字符**；不是 R21 中比较两个椭圆曲线特征所得的差字符，也不是 R58 的平方字符。$L/\mathbb Q$ 的群为 $S_3$，其二次子域为 $K$，$L/K$ 为循环三次扩张。

**定理 A：精确导子及类数一限制。** 设 $M$ 为 $r$ 的 Artin 导子。存在唯一正整数 $f$，使
$$\boxed{\quad\mathfrak f(\eta)=f\mathcal O_K,
\qquad M=Df^2,\qquad f=3^aR.\quad}\tag{1.3}$$
其中 $R$ 平方自由、$(R,3Dp)=1$，并且
$$\boxed{\quad
q\mid R\ \Longrightarrow\ 3\mid q-\chi_K(q),
\qquad
a\in\begin{cases}\{0,2\},&3\nmid D,\\\{0,1,2\},&3\mid D.
\end{cases}\quad}\tag{1.4}$$
$\eta$ 是序 $\mathcal O_f=\mathbb Z+f\mathcal O_K$ 的原始三次环类字符。若 $h_K=1$，则
$$f>1,\qquad 3\mid h(\mathcal O_f).\tag{1.5}$$
特别对 $K=\mathbb Q(\sqrt{-3})$，有额外的精确单位限制
$$\boxed{a+\sum_{q\mid R}v_3\bigl(q-\chi_K(q)\bigr)\ge2.}\tag{1.6}$$

**定理 B：已发表的非消失子范围。** 若
$$\boxed{D3^{2a}R^2<p,}\tag{1.7}$$
则存在水平 $p$、权 $2$、平凡 nebentype 的新形式 $g_2$，满足
$$\boxed{L\!\left(\tfrac12,\pi_{g_2,K}\otimes\eta\right)\ne0.}\tag{1.8}$$
这里使用酉自守归一化。该结论允许 $K$、$f$ 和 $\eta$ 随 $E,p$ 变化；不要求 $\eta$ 为普通类群字符。

**定理 C：实际三次商与二除法域不交。** 令 $H=\mathbb Q(E[2])$。则
$$\boxed{L\cap KH=K.}\tag{1.9}$$
若 $\operatorname{Gal}(H/\mathbb Q)=S_3$，记其二次子域为 $K_2$，还精确有
$$L\cap H=\begin{cases}K,&K_2=K,\\\mathbb Q,&K_2\ne K.\end{cases}\tag{1.10}$$
若 $\operatorname{Gal}(H/\mathbb Q)=C_3$，则 $L\cap H=\mathbb Q$。小惯性条件会排除 mod $2$ 像更小的情形。

**定理 D：分母素数在三次扩张中的分裂。** 若 $v_\ell(j(E))<0$，则
$$\boxed{\ell\nmid M,\quad p\mid-v_\ell(j(E)),\quad
\ell\equiv\pm1\pmod p.}\tag{1.11}$$
每个 $\ell$ 上方的 $K$ 素理想都在 $L/K$ 完全分裂。具体而言：

| $\ell\bmod p$ | $K/\mathbb Q$ 的行为 | $L/\mathbb Q$ 的 Frobenius |
|---|---|---|
| $1$ | 分裂 | 单位元，$\ell$ 完全分裂 |
| $-1$ | 惰性 | 换位 |

这使 $M$ 的分歧支集与 $j$ 分母支集严格不交，却没有给前者统一上界，也没有排除 Studnia 定义的 exceptional 素数。

## 2. 从 R21 独立识别小惯性，不用未发表分类

在 $p>3$，潜在好超奇异约化的有限惯性商阶为
$$e\in\{1,2,3,4,6\}.$$
R21 §§2–4 已证明：选择第二层基本特征 $\omega_2$ 的一个取向后，在取得好约化的惯性子群上 $\lambda=\omega_2$。因此
$$\lambda=\omega_2\delta\quad\text{在 }I_p\text{ 上},\qquad
\delta^e=1.$$
行列式给 $\delta^{p+1}=1$。设 $s$ 是 $\delta$ 的阶，则
$$s\mid\gcd(e,p+1),\qquad s\in\{1,2,3,4,6\}.$$
这些字符都是温和的，且取值于 $\mathbb F_{p^2}^{\times}$。写 $T=p^2-1$，可表示为
$$\lambda=\omega_2^b,\qquad b=1+kT/s$$
（$s=1$ 时按平凡字符解释）。$\lambda(I_p)$ 在 $C$ 中的指数为 $\gcd(b,T)$。

若素数 $u\mid\gcd(b,T)$，则 $u\mid s$：否则 $u\mid T/s$ 与 $b\equiv1\pmod u$ 矛盾。又因 $8\mid T$、$s\mid12$，$T/s$ 总为偶数，所以 $b$ 为奇数，$u\ne2$。故唯一可能的真指数来自 $3\mid s$，从而 $3\mid e$，$e=3$ 或 $6$，且 $3\mid p+1$。

若 $9\mid T$，则 $3\mid T/s$，又得 $b\equiv1\pmod3$，指数仍为 $1$。所以真指数要求 $v_3(T)=1$；结合 $3\mid p+1$，恰有 $p\equiv2,5\pmod9$。此时真指数只能为 $3$，得到 (1.2)。

因 $p\equiv-1\pmod3$，复共轭作用为
$$\eta^c=\eta^{-1}.$$
$\lambda$ 满射使 $\eta$ 恰为阶 $3$，所以其诱导表示的核给群 $C_3\rtimes C_2=S_3$。而 $C^3=\ker\vartheta$，故 $r(I_p)=1$，即
$$p\nmid M.\tag{2.1}$$

上述论证也明确给出 $e=3$ 或 $6$；后面二除法域的证明会用这一实际约化信息。

## 3. 三次反圆分字符的局部导子

用全局类域论把 $\eta$ 视为有限阶 Hecke 字符 $\Omega$。由于 $\eta^c=\eta^{-1}$，对任意 $x\in\mathbb A_{\mathbb Q}^{\times}$，有
$$\Omega(x)=\Omega(x)^ {-1}.$$
再用 $\Omega^3=1$，得到
$$\Omega|_{\mathbb A_{\mathbb Q}^{\times}}=1.\tag{3.1}$$
其无穷分量平凡，因为 $\mathbb C^{\times}$ 连通而字符像有限。

### 3.1 $q\ne3$ 且 $q$ 在 $K$ 不分歧

局部主单位群为 pro-$q$ 群，任意阶 $3$ 字符都在该群平凡。因此非零导子指数只能为 $1$。

若 $q$ 分裂，两个局部字符互逆，同有导子指数 $0$ 或 $1$；非平凡惯性字符要求 $3\mid q-1$。

若 $q$ 惰性，剩余域为 $\mathbb F_{q^2}$，复共轭在其中为 $x\mapsto x^q$。对一个非平凡三次惯性字符，反圆分关系要求 $q\equiv-1\pmod3$。

所以这些分歧素数恰可写入一个平方自由整数 $R$，且
$$q\mid R\Longrightarrow q\nmid D,
\qquad 3\mid q-\chi_K(q).\tag{3.2}$$
这也涵盖 $q=2$：只有 $2$ 在 $K$ 惰性时才可能出现在 $R$ 中。

### 3.2 $q\ne3$ 且 $q$ 在 $K$ 分歧

阶 $3$ 字符仍杀死 pro-$q$ 主单位群；二次共轭在剩余域上作用平凡。对剩余单位字符，反圆分关系使其平方平凡，与阶整除 $3$ 合起来使其平凡。因此 $\eta$ 在 $q$ 上方不分歧。

这里不意味着 $r$ 在 $q$ 不分歧：诱导表示仍包含二次域自身的分歧。特别在 $q=2$，最后的 Artin 导子指数必须是 $v_2(D)$，可能为 $2$ 或 $3$。

### 3.3 $3$ 在 $K$ 不分歧

分别在 $\mathbb Q_3$ 或其不分歧二次扩张中考察局部单位。剩余单位群阶素于 $3$；对 $U_n=1+3^n\mathcal O$，$3$ 进对数给
$$U_1^3=U_2.$$
因此一个阶 $3$ 字符在 $U_2$ 平凡；若分歧，它必在 $U_1$ 非平凡，导子指数恰为 $2$。分裂时两处指数相等，故此处理想导子为 $1$ 或 $9\mathcal O_K$。

### 3.4 $3$ 在 $K$ 分歧

在局部二次扩张中可取 $\pi^2=3u$，$u\in\mathbb Z_3^{\times}$；令 $U_n=1+\pi^n\mathcal O$。对数在 $U_2$ 上为同构，并有
$$U_2^3=U_4.$$
故导子指数至多 $4$。指数 $1$ 被剩余单位群阶为 $2$ 排除。对于每个 $m\ge1$，
$$U_{2m}=(1+3^m\mathbb Z_3)U_{2m+1}.$$
由 (3.1)，若字符在 $U_{2m+1}$ 平凡，它也在 $U_{2m}$ 平凡。因此导子指数不能为奇数，剩下 $0,2,4$。

由于 $(3)=\mathfrak p_3^2$，这恰对应理想导子 $1,3\mathcal O_K,9\mathcal O_K$。

合并四种情形及 (2.1)，得到
$$\mathfrak f(\eta)=3^aR\mathcal O_K=f\mathcal O_K$$
以及 (1.4)。Artin 导子的诱导公式给
$$\mathfrak f_{\mathbb Q}(\operatorname{Ind}_K^{\mathbb Q}\eta)
=D\,N_{K/\mathbb Q}\mathfrak f(\eta)=Df^2,$$
证明 (1.3)。所用公式是标准的 Artin 导子诱导公式，见 Serre，*Corps locaux / Local Fields*，Chapter VI §3；这里每个局部指数已由上文确定，不从未发表论文的导子表直接代入。

## 4. 环类群、类数一以及变化导子的真正范围

对 $q\mid f$，序的局部单位满足
$$\mathcal O_{f,q}^{\times}
=\mathbb Z_q^{\times}(1+f\mathcal O_{K,q}).$$
由 (3.1) 和导子定义，$\Omega$ 在这个群平凡；$q\nmid f$ 时它在全部 $\mathcal O_{K,q}^{\times}$ 平凡。因此 $\eta$ 经过 $\operatorname{Pic}(\mathcal O_f)$。若它经过更小导子的序，其 Hecke 导子也会更小，故这是原始环类字符。

若 $h_K=1$ 且 $f=1$，该字符经过平凡普通类群，与阶恰为 $3$ 矛盾。因此 $f>1$，且其满射到 $\mu_3$ 给 $3\mid h(\mathcal O_f)$。

序的标准理想类群正合列为
$$\mathcal O_K^{\times}\longrightarrow
(\mathcal O_K/f\mathcal O_K)^{\times}/(\mathbb Z/f\mathbb Z)^{\times}
\longrightarrow\operatorname{Pic}(\mathcal O_f)
\longrightarrow\operatorname{Cl}(K)\longrightarrow1.$$
逐素数计数，得到
$$h(\mathcal O_f)=
\frac{h_Kf}{[\mathcal O_K^{\times}:\mathcal O_f^{\times}]}
\prod_{q\mid f}\left(1-\frac{\chi_K(q)}q\right).\tag{4.1}$$

在 $K=\mathbb Q(\sqrt{-3})$、$f>1$ 时，单位指数为 $3$。代入 $f=3^aR$，(4.1) 的 $3$ 进赋值为
$$v_3h(\mathcal O_f)=
\begin{cases}
\displaystyle\sum_{q\mid R}v_3(q-\chi_K(q))-1,&a=0,\\[2mm]
\displaystyle a-1+\sum_{q\mid R}v_3(q-\chi_K(q)),&a>0.
\end{cases}$$
要求该值至少为 $1$，两种情形都化为 (1.6)。例如只有一个 $q\ne3$ 分歧且 $a=0$ 时，必须有 $9\mid q-\chi_K(q)$；只有 $3$ 分歧时必须有 $a=2$。这不是只看局部是否容许阶 $3$ 就能省略的全局单位条件。

同时，类数一并不给 $f$ 上界。固定一个类数一虚二次域 $K$ 和 $p$，取任意大的素数
$$q\equiv1\pmod{9D},\qquad q\ne p.$$
Dirichlet 定理给无穷多个这样的 $q$。它们在 $K$ 分裂，且由上述正合列，$\operatorname{Pic}(\mathcal O_q)$ 为阶 $(q-1)/u$ 的循环群，其中 $u=[\mathcal O_K^{\times}:\mathcal O_q^{\times}]\in\{1,2,3\}$。其阶被 $3$ 整除，故存在阶 $3$ 字符；$h_K=1$ 保证其导子恰为 $q$。这些字符在 $p$ 不分歧，但 $Dq^2$ 无界。

这个构造是实际类域字符的构造。它**不**声称每个字符均来自本题的一条椭圆曲线；它精确说明不能仅凭“类数一、三次、反圆分、$p$ 不分歧”删除变化的 $f$。

## 5. 与实际约化及 $E[2],E[3]$ 的局部对应

$\vartheta$ 杀死标量和 $C$ 的全部素于 $3$ 的部分；由 $v_3(p^2-1)=1$，它在 $C$ 的三次子群上忠实。因此 $q\ne p$ 处 $\eta$ 分歧恰好表示实际惯性像具有非平凡三次部分。

潜在乘法时，R2 给惯性像在 $\{\pm I\}$ 中，所以不会贡献 $f$。潜在好约化时，有限惯性在素于剩余特征的 Tate 模上忠实，模 $p$ 约化也忠实：$1+pM_2(\mathbb Z_p)$ 没有有限阶非单位元。特别地，R2 的潜在乘法条件 $q\equiv\pm1\pmod p$ 排除了本题在 $q=2,3$ 的潜在乘法；这两个位置必为潜在好约化。

于是有以下实际检测式。

1. 对 $q\ge5$、$q\ne p$，若 $E$ 潜在好约化，则
   $$q\mid R\quad\Longleftrightarrow\quad3\nmid v_q(\Delta_{\min}).\tag{5.1}$$
   这是温和惯性阶 $12/\gcd(12,v_q\Delta_{\min})$ 的三次部分；潜在乘法情形不在 (5.1) 内。
2. 在 $q=2$，使用 $T_3(E)$。其有限惯性模 $3$ 约化仍忠实，因为 $1+3M_2(\mathbb Z_3)$ 无扭。故
   $$2\mid R\quad\Longleftrightarrow\quad
   3\mid e\bigl(\mathbb Q_2(E[3])/\mathbb Q_2\bigr).\tag{5.2}$$
   这里使用上一段已经确认的潜在好约化，不能将该检测式无条件用于任意 Tate 曲线的 $3$ 除法域。
3. 在 $q=3$，野惯性是 pro-$3$ 群，其像若非平凡，必为 $C$ 中的阶 $3$ 子群。$T_2(E)$ 到 $E[2]$ 的核是 pro-$2$，不能杀死这个三次部分。因此
   $$a>0\quad\Longleftrightarrow\quad
   \mathbb Q_3(E[2])/\mathbb Q_3\text{ 有野分歧}.\tag{5.3}$$

在 (5.3) 的非平凡情形，$r$ 与 $E$ 的 Tate 模在每个非平凡野惯性子群上的不变量都为零，且两者的 tame conductor contribution 都为 $2$；所以其 $3$ 进导子指数相等。这还给出
$$v_3(N_E)=
\begin{cases}
4,&3\nmid D,\ a>0,\\
1+2a\in\{3,5\},&3\mid D,\ a>0.
\end{cases}\tag{5.4}$$

这些式子保留了真实小挠点分歧信息，但不意味着不同素数上的三次部分组成同一个全局三次扩张。下一节给本情形中恰相反的全局结论。

## 6. $p$ 处三次分歧强迫二除法域不交

第 2 节证明 $E$ 在 $p$ 的有限惯性阶为 $e=3$ 或 $6$。在 $T_2(E)$ 中，该有限循环群的阶 $3$ 部分模 $2$ 不会消失，因为约化核为 pro-$2$；其至多阶 $2$ 的部分在 $\operatorname{GL}_2(\mathbb F_2)$ 中与阶 $3$ 子群交换，只能平凡。故
$$\rho_{E,2}(I_p)=C_3.\tag{6.1}$$
因此 $\operatorname{Gal}(H/\mathbb Q)$ 只能为 $C_3$ 或 $S_3$。

另一方面，$L/\mathbb Q$ 在 $p$ 不分歧。分情况证明 (1.9)。

- 若 $H/\mathbb Q$ 的群为 $C_3$，则 $KH/K$ 为循环三次，且在 $p$ 分歧。它不可能等于不分歧的 $L/K$，故交为 $K$。
- 若 $H/\mathbb Q$ 的群为 $S_3$ 且其二次子域 $K_2=K$，同样 $H/K$ 为在 $p$ 分歧的循环三次，所以 $H\cap L=K$。
- 若 $K_2\ne K$，则 $H\cap K=\mathbb Q$，$\operatorname{Gal}(KH/K)=S_3$。若 $L\subset KH$，将产生 $S_3$ 的阶 $3$ 商，与 $S_3^{\rm ab}=C_2$ 矛盾。因为 $[L:K]=3$，交域只能为 $K$。

这证明定理 C。对 (1.10)，还可直接使用 $S_3$ 的正规子群分类：$L\cap H$ 若非平凡且不是整个 $H$，只能是双方相同的二次子域；整个 $H$ 的情形已被 (6.1) 排除。

**与 R41 的边界。** R41 只讨论固定 $A:y^2=x^3-x$ 及特定归一化四次 CM 参考族；那些族在 $p$ 的惯性完整。本文 (1.1) 不在该范围内，所以 (1.9) 不是 R41 的直接特例。本文也没有把 (1.9) 扩大成 $H$ 与整个 $p$ 幂除法塔总不交：当 $K_2=K$ 时已经存在共同二次域。

## 7. Feigon–Whitehouse 的已发表非消失如何逐项适用

引用 Feigon–Whitehouse (2009)，Duke Math. J. **149** (2), 347–410，DOI [10.1215/00127094-2009-041](https://doi.org/10.1215/00127094-2009-041)，[作者原文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)。为避免引言简化式及 classical 变量的歧义，使用其 Lemma 3.6、Proposition 3.9、Corollary 4.22；Theorem 6.10 的非范数分支也记录相同结论。

在其记号中，取
$$F=\mathbb Q,\quad E_{\rm FW}=K,\quad N=p,\quad k=1,
\quad m=0,\quad\Omega=\eta.$$
水平是一个惰性且不分歧的素数，满足其奇偶条件；$\Omega$ 在 $p$ 不分歧；(3.1) 给其中心字符条件；$0<1$ 给无穷权条件。字符的导子范数为
$$c(\Omega)=N\mathfrak f(\eta)=f^2.$$

取辅助 Hecke 函数为单位元。由 Proposition 3.9，谱侧是一个非零公共常数乘
$$\sum_{\pi\in\mathcal F(p,2)}
\frac{L(1/2,\pi_K\otimes\eta)}{L(1,\pi,\operatorname{Ad})}$$
加 residual 项。Lemma 3.6 表明 residual 项只可能来自阶至多 $2$ 的范数型字符；$\eta$ 的阶为 $3$，故该项严格为零。这正是权 $2$ 时不能漏掉的检查。

若 $p>Df^2$，Corollary 4.22 给稳定几何侧：regular 项消失，剩余项是非零局部常数与 $L(1,\chi_K)$ 及其删有限 Euler 因子版本的乘积，因而非零。两侧相等使上述谱和非零，至少有一个分子不为零。这证明 (1.8)，无需假设每一项都非零。

若 $V_{g_2}$ 采用椭圆曲线的算术 Frobenius 归一化，$r$ 为有限像 Artin 表示，则
$$L(s,V_{g_2}\otimes r)
=L(s-\tfrac12,\pi_{g_2,K}\otimes\eta).\tag{7.1}$$
所以本文的酉中心 $1/2$ 对应算术中心 $1$。这与 Studnia 的变量相合；不可把 FW classical reformulation 中另写的 $3/2$ 原样代入 Studnia 的 $L$ 函数。

本节只证明非消失。它没有证明任何 Jacobian 商的有理点有限，也没有调用 Studnia B/D 来排除分母。

## 8. Tate 分母的精确三次 Frobenius

令 $v_\ell(j(E))<0$。R15 的 $p$ 处潜在超奇异结论先给 $\ell\ne p$。局部 $E$ 为一个 Tate 曲线的至多二次扭曲。去掉标量二次字符后，模 $p$ 表示是
$$\begin{pmatrix}\chi_p&*\\0&1\end{pmatrix}.$$
实际像阶素于 $p$，所以相应有限像表示半单；惯性中的单幂元被排除。Tate 参数 $t$ 的 Kummer 类于是给
$$p\mid v_\ell(t)=-v_\ell(j(E)).\tag{8.1}$$
惯性像只余标量 $\pm I$，从而 $r(I_\ell)=1$，$\ell\nmid M$。

Frobenius 半单化的两个本征值，除去共同符号，为 $\ell$ 和 $1$。若它在 $C$ 中且在 $\mathbb F_p$ 有本征值，则必须为标量，故 $\ell\equiv1\pmod p$。否则它在 $N\setminus C$，迹为零，故 $\ell\equiv-1\pmod p$。这重证 (1.11) 中所需的同余，而不使用任何 formal immersion 输入。

当 $\ell\equiv1\pmod p$，Frobenius 是标量，$\vartheta$ 在标量群平凡，故 $r(\operatorname{Frob}_\ell)=1$。

当 $\ell\equiv-1\pmod p$，Frobenius 的像在 $N/C$ 非平凡，其在 $N/C^3\simeq S_3$ 中为一个换位。此时 $\ell$ 在 $K$ 惰性，而 $K$ 上 Frobenius 是该换位的平方，因而也为单位元。

这证明定理 D 中全部分裂陈述，尤其
$$\eta(\operatorname{Frob}_{\mathfrak l})=1
\quad\text{对每个 }\mathfrak l\mid\ell\text{ 成立}.\tag{8.2}$$

## 9. 为什么这些 Tate 条件尚不排除 exceptional

先给一个可独立检查的局部实现事实。对任意素数 $\ell\ne p$、$\ell\equiv\pm1\pmod p$，取 $\mathbb Q_\ell$ 上参数
$$t=\ell^p$$
的 Tate 曲线。$t$ 已是 $p$ 次幂，所以其模 $p$ 表示分裂为
$$\chi_p\oplus1.$$
该表示不分歧。若 $\ell\equiv1$，像为单位元；若 $\ell\equiv-1$，像由一个本征值 $1,-1$ 的反射生成，适当共轭后在非分裂 Cartan 正规化子中。其 $j$ 的赋值为 $-p$。因此 (8.1)、(8.2) 及相应商二次局部型都实际可实现。

Studnia 的 exceptional 条件是某三个特定的 $p$ 次圆分整数同时消失于一个 $\ell$ 上方素理想。它仅由 $p,\ell$ 定义；没有因 (8.1) 的 Tate 参数为 $p$ 次幂而自动失败。上述构造只说明**局部表示与同余类相容**，不声称提供了全局异常曲线，也不声称 exceptional 素数确实存在。

若再采用 Studnia submitted 的 B/D，并在 (1.7) 范围使用定理 B，则实际分母会被限制到 exceptional 集与定理 D 所述三次分裂集合的交。但要证明这个交对所有实际曲线为空，仍缺少新的证明。

## 10. 已推进的量词与保留的缺口

已发表非消失现在可由真实约化数据检查：令 $R$ 是实际三次惯性素数的乘积，确定 $a$ 后，$R<3^{-a}\sqrt{p/D}$ 即足够。对类数一 $K$，$D\le163$，一个较粗的充分条件是 $13203R^2<p$；这只是将 $3^{2a}\le81$ 代入。

但 $R$ 与分母支集不交，故不能用分母素数都大于 $p$ 来使 $M$ 变小。类数一强迫存在三次分歧，却不限制分歧素数大小或个数。二除法域与三次商的实际不交进一步排除了把它们误认成同一个全局对象的捷径。

因此本文没有无条件整性结论，没有绝对异常素数界，也没有解决主课题。它把小惯性分支中的三个独立问题分清并给出可用接口：精确的 $Df^2$、已发表的 $p>Df^2$ 非消失，以及与之支集不交的 Tate 分母分裂条件。

## 11. 输入与可核查来源

- [R1](R1-exact-remaining-image.md)、[R5](R5-quadratic-self-twist-and-inertness.md)：完整实际正规化子像、商虚二次域及 $p$ 惰性。
- [R2](R2-exact-tate-local-criterion.md) 的 Tate 局部论证；[R21](R21-twelfth-power-signature-and-cm-twists.md) §§2–5 的 Raynaud 端点型及潜在好约化惯性。
- J.-P. Serre，*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*，Invent. Math. **15** (1972), 259–331，§5.6：上述温和/野惯性及潜在好约化的标准局部输入。R21 已记录所需 Raynaud 原始来源。
- J.-P. Serre，*Corps locaux / Local Fields*，Chapter VI §3 的 Artin 导子诱导公式；局部类域论把字符导子与单位过滤对应。本文在 §§3–4 展开了本情形的所有指数和环类群计数。
- B. Feigon and D. Whitehouse，Duke Math. J. **149** (2009), 347–410，[DOI](https://doi.org/10.1215/00127094-2009-041)，[作者全文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)：§1.1；Lemma 3.6、Proposition 3.9、Corollary 4.22；Theorem 6.10 非范数分支。本文只将这些已发表公式用于定理 B。
- [R41](R41-two-and-p-power-division-field-independence.md)：对照其明确受限的固定/四次参考范围，避免把此次 (1.9) 与整个除法塔不交混同。

Studnia，arXiv:2507.20801v2，并非本文定理 A–D 的证明输入。其出版状态、B/C/D 条件及 exceptional 定义见上列独立接口笔记。


**后续（R69）：** 已通过忘线映射独立证明实际秩零商的存在与有理点群有限，使用已发表 BD1997；本文件 §6 的“只证明非消失”仍是本节范围，不再表示整个项目缺少有限商证明。尖点整性与 exceptional 的排除依旧开放，见 [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)。
