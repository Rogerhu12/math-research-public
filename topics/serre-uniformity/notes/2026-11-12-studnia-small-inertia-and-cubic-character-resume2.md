# Studnia 的小惯性接口、已发表非消失及实际分母条件

日期：2026-11-12。状态：**文献接口核验及独立推导的边界记录；不据此宣布主问题完成。**

## 1. 必须修正的适用范围理解

Studnia 的 [arXiv:2507.20801v2](https://arxiv.org/html/2507.20801v2) 研究模 $p$ 表示为完整非分裂 Cartan 正规化子、且 $p$ 处惯性严格小于 Cartan 的曲线。其 Theorems B/C/D 不要求参考曲线预先固定，也不要求参考曲线有 CM。

因此，对本题的一条实际异常曲线 $E$，若满足这一小惯性条件，可以在论文的同余问题中直接取 **$F=E$**。以前对固定好约化 CM 曲线 $A$ 检查出 $I_p=C$，只说明那一固定参考分支不适用；不能扩大成对所有实际异常曲线不适用。

出版状态另须保留：核验当日，作者的[论文主页](https://pub.math.leidenuniv.nl/~studniae/publications.html) 仍把该文列为 **submitted**。本仓库没有重证 B/D 的整体几何及 Euler system 论证，所以它们只保留为未发表接口，不作为无条件结果的外部输入。

## 2. B/C/D 的准确逻辑链

用 $C\simeq\mathbb F_{p^2}^{\times}$，取阶恰为 $3$ 的复字符 $\vartheta$。小惯性条件等价于此处的 $I_p=C^3$，且 $p\equiv2,5\pmod9$。令
$$\eta=\vartheta\circ\lambda:G_K\longrightarrow\mu_3,
\qquad r=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\eta.$$
$r$ 的像为 $S_3$，有一个权 $1$ 二面体新形式 $g$，其水平为 $r$ 的 Artin 导子 $M$，且 $(M,p)=1$。

| 原文位置 | 输入 | 输出与限制 |
|---|---|---|
| Theorem B | 水平 $p$、权 $2$ 的某个新形式轨道 $\omega$ 中，$L(f,g,1)\ne0$ | 扭曲 Jacobian 的相应 $2|\omega|$ 维商有有限有理点群；这是该 submitted 论文的结论 |
| Theorem C | 判别式 $-M$ 的环类多项式模 $p$ 不是立方；$p>M$ 是其充分条件 | 存在所需的非零中心值 |
| Theorem D | B 所给商的有理点群有限 | 任一同余曲线的 $j$ 分母素数 $\ell$ 必 exceptional for $p$，并有 $\ell\equiv\pm1\pmod p$ |

这里不能把 C 的充分条件当成对所有实际曲线成立，也不能从 D 删去 exceptional 的例外集。

## 3. $p>M$ 范围其实有已发表的非消失输入

Feigon–Whitehouse，*Averages of central L-values of Hilbert modular forms with an application to subconvexity*，Duke Math. J. **149** (2009), 347–410，DOI [10.1215/00127094-2009-041](https://doi.org/10.1215/00127094-2009-041)，[作者稿](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[机构存档](https://ueaeprints.uea.ac.uk/id/eprint/18579/)，可覆盖本题的**分歧**三次反圆分字符，不限于普通理想类群字符。

具体取其基域 $F=\mathbb Q$、CM 扩张为 $K$、平方自由水平 $N=p$、权 $2$、有限阶字符 $\Omega=\eta$。其 §1.1 假设逐项成立：$p$ 在 $K$ 惰性且不分歧；$\eta$ 在 $p$ 不分歧；$\eta$ 在 $\mathbb A_{\mathbb Q}^{\times}$ 平凡；无穷权为 $0<1$。

最直接可核查的组合是 Lemma 3.6、Proposition 3.9、Corollary 4.22：阶 $3$ 字符使 residual 项为零，$p>D_K^{\rm abs}\,N\mathfrak f(\eta)=M$ 使 regular 几何项消失，剩余主项非零。因此
$$p>M\quad\Longrightarrow\quad
\exists f\in\mathcal S_2(\Gamma_0(p)):
L\!\left(\tfrac12,\pi_{f,K}\otimes\eta\right)\ne0.
\tag{3.1}$$
Theorem 6.10 的非范数字符分支也给同一非消失。其权 $2$ 情形不能错误地排除：只在引言的简化 Theorem 1.1 中加了 $k>1$，完整公式由上述 residual 项处理 $k=1$。

采用 (3.1) 的酉自守归一化可避免两个文本的 $s$ 记法混淆。若用椭圆曲线 Frobenius 根与有限像 $r$ 定义算术 Rankin $L$ 函数，则
$$L(s,V_f\otimes r)=L(s-\tfrac12,\pi_{f,K}\otimes\eta),$$
故 (3.1) 对应 Studnia 使用的算术中心 $s=1$。FW 作者稿的 classical reformulation 把其 Rankin 变量写在 $k+|m|+\tfrac12$；不能把那里的 $s=3/2$ 与 Studnia 的 $s=1$ 原样等同。

另一个文本核查点：accepted manuscript 的 Theorem 6.1 印有 “unramified outside of N”，但 §1.1、§6.2 和其证明使用的是在水平 **above $N$** 不分歧。这里应用上列三个已逐项核验的中间公式，而不将该孤立措辞用成反向的分歧条件。

这只使 $p>M$ 子范围的**非消失**成为已发表输入。B/D 的有限商与分母结论仍不能因而改记为已发表定理。

## 4. 导子和类数一的实际信息

本轮独立证明见 [R66](../results/R66-cubic-conductor-nonvanishing-and-tate-primes.md)。其导子具有精确形状
$$M=Df^2,\qquad f=3^aR,\qquad D=|D_K|,$$
其中 $R$ 平方自由、$(R,3Dp)=1$，每个 $q\mid R$ 满足
$$3\mid q-\chi_K(q).$$
若 $3\nmid D$，$a\in\{0,2\}$；若 $3\mid D$，$a\in\{0,1,2\}$。特别地，$2\mid D$ 时应保留 $v_2(M)=v_2(D)$，不能把所有二次分歧的导子指数都写成 $1$。

若 $h_K=1$，$\eta$ 非平凡强迫 $f>1$，所以必有 $p$ 以外的三次分歧。$\eta$ 实际经过导子 $f$ 的环类群，且 $3\mid h(\mathcal O_f)$。对 $K=\mathbb Q(\sqrt{-3})$，还得到单位造成的精确必要条件
$$a+\sum_{q\mid R}v_3\bigl(q-\chi_K(q)\bigr)\ge2.$$

这给出可检查的非消失范围 $D3^{2a}R^2<p$。但 $R$ 来自潜在好约化的三次惯性素数；它不是 $j$ 的分母根基。后者在 $M$ 中完全不出现。类数一及 $p$ 不分歧本身允许导子任意增大的三次环类字符，故尚不能从实际 Tate 分母条件推出 $p>M$。

## 5. Exceptional 的准确算术内容

取非平方 $z\in\mathbb F_p^\times$，$Q_3=\mathbb F_{p^2}^{\times}/\mathbb F_{p^2}^{\times3}$，并令
$$u_t=\sum_{\substack{b\in\mathbb F_p\\1+b\sqrt z\in t}}\zeta_p^b,
\qquad I_{z,p}=(u_t:t\in Q_3)\subset\mathbb Z[\zeta_p].$$
原文 Definition 3.1.1 的 exceptional 意味着
$$\ell\mid N(I_{z,p}),$$
即存在 $\mathfrak l\mid\ell$ 使三个 $u_t$ 同时为零模 $\mathfrak l$；不是只要求其中一个指数和的范数被 $\ell$ 整除。三个和之和为零，但共同消失仍是两个独立的剩余条件。

若 $\ell\ne p$，令 $P_t(X)=\sum_{1+b\sqrt z\in t}X^b$。这一条件等价于某个特征 $\ell$ 的域中存在阶恰为 $p$ 的 $\xi$，使所有 $P_t(\xi)=0$。当 $\ell\equiv1$ 或 $-1\pmod p$ 时，所需 $\xi$ 分别位于 $\mathbb F_\ell$ 或 $\mathbb F_{\ell^2}$。这给有限域判定，不给统一不可能性。

作者 Remark 3.1.2 报告了 $p\le10000$ 的无 exceptional 计算，并明确把一般不存在视作猜想。该有限计算不能覆盖任意大 $p$。

## 6. 与本题 Tate 条件的比较

R66 独立证明：若 $\ell$ 真是 $j(E)$ 的分母素数，则
$$\ell\nmid M,\qquad p\mid-v_\ell(j(E)),\qquad \ell\equiv\pm1\pmod p.$$
令 $L/K$ 为 $\eta$ 的三次扩张，每个 $\ell$ 上方的 $K$ 素理想都在 $L/K$ 完全分裂。更精确地，$\ell\equiv1\pmod p$ 时 $\ell$ 在 $L/\mathbb Q$ 完全分裂；$\ell\equiv-1\pmod p$ 时其 $S_3$ Frobenius 为换位。

这组条件尚不排除 exceptional。有限域定义只涉及 $p,\ell$；上述三次域随实际曲线变化。对每个 $\ell\equiv\pm1\pmod p$，局部 Tate 曲线参数 $t=\ell^p$ 已实现相应的模 $p$ 正规化子表示和分母赋值。因此，**仅凭该 Tate 表示与该同余类**不能证明 exceptional 不相容；还需要新的全局输入。这里没有把这个局部构造冒充一条全局实际异常曲线。

## 7. 小挠点的全局联系不能误认成同一三次域

R66 还独立证明小惯性分支中
$$L\cap K(E[2])=K.$$
原因是 $L/K$ 在 $p$ 不分歧，而 $E[2]$ 在 $p$ 有阶 $3$ 的惯性。此分支不在 R41 的固定/四次 CM 参考族范围内；R41 那两族在 $p$ 的惯性完整。

在 $3$ 处，$\eta$ 分歧等价于 $\mathbb Q_3(E[2])$ 有野三次分歧；在 $2$ 处，$2\mid R$ 等价于 $\mathbb Q_2(E[3])$ 的分歧指数被 $3$ 整除。这些是真实局部检测式，但它们不把两个全局三次对象识别起来，也不使 $f$ 有统一上界。

仍未解决的是：统一控制 $f$ 或排除剩余 exceptional/Tate 分母，并在整性之后处理变化参考/变化导子的全局同余刚性。本笔记没有将任何一个条件性接口标为主问题解答。


## 后续独立证明更新（12:35）

[R69](../results/R69-forgetful-maps-and-unconditional-rank-zero-quotient.md) 已从实际忘线映射的配对矩阵和 Galois 下降重建所需 Jacobian 商，并以已发表 Bertolini–Darmon 1997 Theorem B 及 Gross 周期共轭性证明 $p>M$ 时该商有理点群有限。所以上文 B 的几何/有限群结论现有独立证明，不把 submitted 论文当作定理输入。D 的整性、尖点处的实际整格和 exceptional 共同非零仍未建立；R69 不提供这些结论。
