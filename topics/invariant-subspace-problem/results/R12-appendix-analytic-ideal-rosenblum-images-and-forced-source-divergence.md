# 原 Haar 模型的解析理想像、同一循环闭包与强制来源发散

日期：2026-11-27（Asia/Taipei）。
作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：§§1–4 的数学结论有以下完整证明。§5 是新取得 Rosenblum II 正文后的适用性核查。没有构造非循环向量，没有证明普通 ISP、边界 $N=M$ 或任何未知闭根的域包含。**

本稿中的 $A$ 始终是原 Haar 算子，作用于
$\mathcal H=L^2(\mathbb Z_2)$；它不是 R271 的负整数边界 $B$。
已发布的
[任意奇数剩余类收缩强*密度](R12-appendix-contractive-strong-star-density-in-every-odd-residue-class.md)
特别给出：对每个整数 $k\ge0$，有多项式 $q_n$ 满足
$$
z^k\mid q_n,\qquad \|q_n(A)\|\le1,\qquad
q_n(A)\longrightarrow I\quad\text{强*}.                 \tag{0.1}
$$
这里只用 $p=1$ 的结论。原 $A$ 单射且范数拟幂零；这些均是已有结论，不重新登记。

## 1. 任意拟幂零算子的准确解析流形像

设 $Q$ 是复 Hilbert 空间上的有界拟幂零算子，$g\ne0$，$\mu\ne0$。写
$$
\mathcal C_Q(g)=\overline{\operatorname{span}\{Q^ng:n\ge0\}}.
$$
令 $\mathscr L$ 是单位圆盘上全纯函数的一个非零线性流形，并且
$z\mathscr L\subset\mathscr L$。不要求 $\mathscr L$ 已闭，也不要求它是整个函数代数的理想。定义
$$
k=\min\{\operatorname{ord}_0 f:0\ne f\in\mathscr L\}.
                                                               \tag{1.1}
$$
这个最小值是某个有限非负整数，并由某个非零 $f_0\in\mathscr L$ 达到。

所有 $f(\mu Q)$ 都可以按原 Taylor 系数定义为范数收敛级数。确切地，若 $f$ 在 $|z|<\rho$ 全纯，则系数在每个更小圆周满足几何上界；而
$\|Q^n\|^{1/n}\to0$，故
$\sum |f_n||\mu|^n\|Q^n\|<\infty$。
同一理由也允许使用任意在 $0$ 附近全纯的函数，而不要求 $\|\mu Q\|<1$。

**定理 1.1。** 准确有
$$
\boxed{
\overline{\{f(\mu Q)g:f\in\mathscr L\}}
=\overline{Q^k\mathcal C_Q(g)}.
}                                                        \tag{1.2}
$$

**证明。** 每个 $f\in\mathscr L$ 都有 $f(z)=z^k u_f(z)$，其中 $u_f$ 在圆盘上全纯。因此
$$
f(\mu Q)g=\mu^k Q^k u_f(\mu Q)g
\in Q^k\mathcal C_Q(g).
$$
这里 $u_f(\mu Q)$ 的范数收敛多项式逼近保持
$\mathcal C_Q(g)$，给出 (1.2) 的一个包含。

对达到最小值的 $f_0$，写
$f_0(z)=z^k u(z)$、$u(0)\ne0$。
$1/u$ 在 $0$ 的某邻域全纯，以上范数级数给
$u(\mu Q)^{-1}=(1/u)(\mu Q)$。
这两个算子都保持 $\mathcal C_Q(g)$，故
$$
u(\mu Q)\mathcal C_Q(g)=\mathcal C_Q(g).                  \tag{1.3}
$$
又因 $z^n f_0\in\mathscr L$，左侧闭包含有
$\mathcal C_Q(f_0(\mu Q)g)$。连续性和交换性给
$$
\begin{aligned}
\mathcal C_Q(f_0(\mu Q)g)
&=\overline{f_0(\mu Q)\mathcal C_Q(g)}\\
&=\overline{Q^k u(\mu Q)\mathcal C_Q(g)}
=\overline{Q^k\mathcal C_Q(g)}.
\end{aligned}
$$
因此反向包含也成立。证毕。

这里明确保留 $\overline{Q^k\mathcal C_Q(g)}$；对一般拟幂零 $Q$，不能把它改成 $\mathcal C_Q(g)$。

## 2. 原 Haar 算子：所有非零解析流形都给同一循环闭包

**推论 2.1。** 对原 Haar $A$、同一个 $g\ne0$、任意 $\mu\ne0$ 和上述任意非零 $\mathscr L$，
$$
\boxed{
\overline{\{f(\mu A)g:f\in\mathscr L\}}=\mathcal C_A(g).
}                                                        \tag{2.1}
$$
更一般，对任意闭 $A$-不变子空间 $\mathcal M$ 和任意非零、在 $0$ 附近全纯的 $f$，
$$
\overline{f(\mu A)\mathcal M}=\mathcal M.                 \tag{2.2}
$$

**证明。** 对 $x\in\mathcal M$，(0.1) 给
$q_n(A)x\in A^k\mathcal M$ 且 $q_n(A)x\to x$。
所以
$$
\overline{A^k\mathcal M}=\mathcal M\qquad(k\ge0).         \tag{2.3}
$$
再将 $f(z)=z^k u(z)$ 分解，并用
$u(\mu A)\mathcal M=\mathcal M$，得到 (2.2)。
取 $\mathcal M=\mathcal C_A(g)$ 并使用定理 1.1，即得 (2.1)。证毕。

这一步使用的是原 Haar 空间上已经支付的实际强单位，不是把全空间的稠密像自动限制到未知 $\mathcal M$。同一实际多项式保持 $\mathcal M$，所以 (2.3) 的限制是合法的。

还可保持乘积的普通算子范数。对每个非零全纯 $f(z)=z^k u(z)$，存在多项式 $p_n$，使
$$
\boxed{
\|p_n(A)f(\mu A)\|\le1,\qquad
p_n(A)f(\mu A)\longrightarrow I\quad\text{强*}.
}                                                        \tag{2.4}
$$
**证明。** 写 $q_n(z)=z^k r_n(z)$，取 $\varepsilon_n\downarrow0$。
用 $u(\mu A)^{-1}$ 的范数收敛 Taylor 多项式选 $t_n$，使
$$
\|t_n(A)u(\mu A)-I\|\le\varepsilon_n.
$$
置
$$
p_n(z)=\frac{\mu^{-k}r_n(z)t_n(z)}{1+\varepsilon_n}.
$$
则
$$
p_n(A)f(\mu A)
=\frac{q_n(A)t_n(A)u(\mu A)}{1+\varepsilon_n}.
$$
其范数至多 $1$，且与 $q_n(A)$ 的范数差至多
$2\varepsilon_n/(1+\varepsilon_n)$，得到强*收敛。证毕。
(2.4) 只控制乘积，没有控制 $\|p_n(A)\|$ 或 $p_n$ 在外部来源空间中的范数。

## 3. 同一 $g$ 的真实 Sobolev--Rosenblum 来源

令 $\mathcal R=R(\mathbb D)$ 为 Sobolev disk Hilbert 空间，使用正交归一基
$$
e_n(z)=\beta_n z^n,\qquad
\beta_n=
\left(\frac{n+1}{\pi(3n^4-n^2+2n+1)}\right)^{1/2}.
                                                               \tag{3.1}
$$
因此
$$
\left\|\sum c_nz^n\right\|_{\mathcal R}^2
=\sum_{n\ge0}\frac{|c_n|^2}{\beta_n^2}.
$$
固定同一 $g\ne0$ 和 $\mu\ne0$，定义
$$
\Phi_g:\mathcal R\longrightarrow\mathcal H,\qquad
\Phi_g(f)=f(\mu A)g.                                      \tag{3.2}
$$
这是外部解析来源映射，不是 R271 的 $G_0^*$ 或其规范形式来源。

**定理 3.1。** $\Phi_g$ 是紧单射；事实上它有范数绝对收敛的秩一展开
$$
\Phi_g=\sum_{n\ge0}
\bigl[\beta_n(\mu A)^ng\bigr]\otimes e_n.                 \tag{3.3}
$$

**证明。** 因 $\sup_n\beta_n<\infty$ 且 $r(A)=0$，
$$
\sum_{n\ge0}\beta_n\|(\mu A)^ng\|<\infty.
$$
所以 (3.3) 按算子范数绝对收敛，有限秩部分和范数逼近
$\Phi_g$；在基向量上的作用正是 (3.2)。这证明有界性和紧性。

若 $0\ne f\in\mathcal R$，写 $f(z)=z^k u(z)$、$u(0)\ne0$。
于是 $u(\mu A)$ 可逆，且 $A^k$ 单射，故
$f(\mu A)$ 单射。因此 $\Phi_g(f)=f(\mu A)g\ne0$。
这证明 $\Phi_g$ 的单射性。证毕。

取任意酉识别 $U:\mathcal H\to\mathcal R$。以 $\mu UAU^*$ 和 $Ug$ 构造正文的 $K_{Ug,\mathbf1}$，准确有
$
K_{Ug,\mathbf1}=\pi U\Phi_g,
\qquad \|\mathbf1\|_{\mathcal R}^2=\pi.
$
以下统一用 (3.2)，避免把这个归一化常数混入来源预算。

**定理 3.2（同源的闭包/实际像严格差与强制来源发散）。**
若 $\mathscr I\subset\mathcal R$ 是任意非零真闭理想，则
$$
\boxed{
\overline{\Phi_g(\mathscr I)}=\mathcal C_A(g),
\qquad
g\notin\Phi_g(\mathscr I).
}                                                        \tag{3.4}
$$
特别，$\Phi_g(\mathscr I)$ 不是闭子空间。对每个有限 $R\ge0$，
$$
\boxed{
\delta_{\mathscr I,g}(R):=
\inf_{\substack{f\in\mathscr I\\\|f\|_{\mathcal R}\le R}}
\|\Phi_g(f)-g\|>0,
\qquad
\delta_{\mathscr I,g}(R)\longrightarrow0
\quad(R\to\infty).
}                                                        \tag{3.5}
$$
因此任何真实来源列 $f_n\in\mathscr I$ 若满足
$\Phi_g(f_n)\to g$，必有
$$
\boxed{\|f_n\|_{\mathcal R}\longrightarrow\infty.}         \tag{3.6}
$$

**证明。** 理想 $\mathscr I$ 非零且对 $M_z$ 不变，
所以 (2.1) 给 (3.4) 的闭包等式。
若 $\Phi_g(f)=g=\Phi_g(1)$，紧单射的单射部分给 $f=1$。
真理想不含 $1$，于是实际像严格缺少 $g$。

固定有限 $R$。$\mathscr I$ 的闭 $R$ 球在 Hilbert 空间
$\mathcal R$ 中弱紧，且紧算子 $\Phi_g$ 把它送成范数紧集。
若其到 $g$ 的距离为零，则 $g$ 属于该紧像，与上段矛盾。
故 (3.5) 的严格正性成立；距离趋零由 (3.4) 得到。

最后，若 (3.6) 失败，就有某个有限 $R$ 和一个子列的来源范数都不超过
$R$，而其输出仍趋于 $g$，直接违反 (3.5)。证毕。

这里没有假设 $\mathcal C_A(g)=\mathcal H$，也没有构造任何
$\mathcal C_A(g)\ne\mathcal H$ 的向量。紧性只用于真实有限来源球的正距离；
闭包等式与实际像差均保留同一个 $g$、同一个理想和原 Hilbert 来源范数。

## 4. 对当前接口的准确含义

给原 Haar 空间选定任意酉识别 $U:\mathcal H\to\mathcal R$。
把正文的零点判据用于 $\widetilde A=UAU^*$ 时，
对于任意非零 $M_z$-不变流形 $\mathscr L$，其所考察的闭子空间准确是
$$
U\mathcal C_A(g)
=\overline{\{f(\mu\widetilde A)Ug:f\in\mathscr L\}}.
                                                               \tag{4.1}
$$
所以改变这个解析流形，不会改变同一 $g$ 的输出闭包。
若满足零点判据，确实能证明该闭包为真；但本稿没有提供零点见证，
没有把“可以选择一个理想”当成非循环向量的构造。
(3.5)--(3.6) 还表明，闭包返回 $g$ 的能力不提供统一有界的实际
Sobolev 来源。

对负整数边界 $B$，定理 1.1 仍适用，但 (0.1) 不能搬过去。
其准确输出是 $\overline{B^k\mathcal C_B(g)}$。
若 $g\in M=\ker T$ 且 $k\ge1$，这个输出包含于
$N=\overline{BM}$；这不证明 $N=M$。若 $k=0$，输出为
$\mathcal C_B(g)\subset M$，也没有取得新的稳定范围身份。

同样，$G_0^*$ 是实际非全域、非闭值域的除法算子；
不能把 (3.2) 的有界全域解析来源当成它的图域。
目前的 $R:F\to Y$ 和 $X=\{v+Zv:v\in F\}$ 亦未证明是不变分块。
这些不同的实际来源不能相互替换。

## 5. Rosenblum II 正文核查的新记录

来源：Junsheng Fang, Bingzhe Hou, Chunlan Jiang, Yuanhang Zhang,
*The invariant subspace problem and Rosenblum operators II*,
arXiv:2610.11202v1, 2026-10-08，
[本轮取得的作者 HTML 全文](https://arxiv.org/html/2610.11202v1)。
这更新 [2026-11-14 核查](../notes/2026-11-14-literature-789f.md) 中“正文未取得”的状态；
本轮实际读了 §2 Theorem A、§3 Definition 3.1/Theorem 3.3/Propositions 3.5–3.6，
以及 §5 的真实逆与不变分块接口。

Theorem A 要求同一来源的零点见证。Proposition 3.6 在已有 ideal property
之后运输到指定 SOT 闭包；原 Haar 的多项式强密度不提供其先决见证。
§5 Proposition 5.8/Corollary 5.9/Theorem D 的逆接口要求有界全域逆及真实不变分块；
它们没有给予当前 $G_0^*$、未知闭根或 $X/Y$ 的这些条件。

以下两个核查点是直接反例/修复，不是否定 Theorem A 的结论：

1. §2 proof Step 3 中“$\mathcal R$ 范数与 sup 范数等价”的文字过强。
   由 (3.1)，$\|z^n\|_{\mathcal R}=\beta_n^{-1}\asymp n^{3/2}$，
   而 $\|z^n\|_\infty=1$。实际所需的单向嵌入成立：
   $$
   \|f\|_\infty
   \le\sum|c_n|
   \le\left(\sum\beta_n^2\right)^{1/2}\|f\|_{\mathcal R}.
   $$
   因此有零点的函数不可能在 $\mathcal R$ 中趋于 $1$；
   其零点可以随函数变化，仍不影响此证明。

2. Remark 2.2 中所写的同一个 $K_{g,\mathbf1}(\mathscr L)$
   未必非零。取 $T=0$、$g\ne0$、$\mathscr L=z\mathcal R$，
   则全部 $f(T)g=0$。这不影响 Theorem A 的结论：
   像为零的分支改由有限维循环子空间/特征值处理即可。
   本稿原 Haar 情形因定理 3.1 的单射性，明确排除了该零像分支。

有理矩生成函数在原 Haar 上只能为零的限制已经登记在
[2026-11-12 centered 文献稿 §3](../notes/2026-11-12-centered-literature-e2.md)，
本轮不重复证明或登记。
