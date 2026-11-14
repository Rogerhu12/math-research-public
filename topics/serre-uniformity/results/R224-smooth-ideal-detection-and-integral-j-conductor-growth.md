# R224：光滑理想检测与整 $j$ 四次支撑的 $2\sqrt e$ 次增长

日期：2026-11-13；会话：serre-uniformity-recovery。

**状态：已证明。** 本文把 R107 的有效必要条件
$Q_0\gg_\epsilon p^{2-\epsilon}$ 加强为
$Q_0\gg_\epsilon p^{2\sqrt e-\epsilon}$。这里 $Q_0$ 是同一实际曲线的四阶惯性支撑乘积，前提仍是 R107 的 $K=\mathbb Q(\sqrt{-3})$、$c=6$ 或 $9$、整 $j$ 分支。新输入是一个在固定虚二次域分裂、在变化二次域惰性的有效小素数定理。完整证明只用普通 Dirichlet Burgess、固定域的理想计数和已发表的无条件有效 Mertens 定理，不引用变化数域上的 Hecke Burgess 界。

本结果给导子向下增长的新约束，不给导子或 $p$ 的绝对上界。

## 1. 解析定理和实际曲线的推论

记
$$
\alpha=\frac1{2\sqrt e}=0.3032653298\ldots.
$$

**定理 224.1（固定虚二次域内的指定二次 Frobenius）。**
固定虚二次域 $K$，基本判别式为 $D_K<0$。令 $F\ne K$ 为任意二次域，基本判别式为 $D_F$，置 $Q=|D_F|$。给定 $\epsilon>0$ 和 $A>0$，存在有效常数 $C_{K,A,\epsilon}$，使对每个整数 $1\le B\le Q^A$，都有有理素数 $q$ 满足
$$
\boxed{
q\nmid 2D_KD_FB,\qquad
\chi_K(q)=1,\qquad \chi_F(q)=-1,\qquad
q\le C_{K,A,\epsilon}Q^{\alpha+\epsilon}.
}                                                        \tag{224.1}
$$
不需要 $F$ 为虚二次域，不需要 $B$ 固定，也没有使用变化域的 Siegel 下界。对无增长限制的任意 $B$，本文不作这个断言。

**推论 224.2（R107 实际分支的增强增长）。**
保持 R107 (107.1) 的全部实际条件：
$$
\begin{gathered}
E/\mathbb Q,\quad \rho_{E,p}(G_\mathbb Q)=N_{\rm ns}(p),\quad
K=\mathbb Q(\sqrt{-3}),\quad p>37,\quad p\equiv11\pmod{12},\\
\rho_{E,p}(I_p)=C^3,\quad c(\eta)\in\{6,9\},\quad
j(E)\in\mathbb Z,\quad j(E)\ne0.
\end{gathered}                                           \tag{224.2}
$$
令
$$
\mathcal S=\{q\ge5:q\ne p,\ e_q(E)=4\},\qquad
Q_0=\prod_{q\in\mathcal S}q,
$$
并假设 $\mathcal S\ne\varnothing$。令 $F$ 为 R104 的实际二除判别式域，$E'$ 为其规范化的同 $j$ 二次扭曲。对每个 $\epsilon>0$，存在有效正数 $c_\epsilon,c'_\epsilon$，与曲线、$p$、$F$ 和支撑素数个数无关，使
$$
\boxed{
Q_0\ge c_\epsilon p^{\,2\sqrt e-\epsilon},
\qquad |D_F|\ge3c_\epsilon p^{\,2\sqrt e-\epsilon},
}                                                        \tag{224.3}
$$
以及
$$
\boxed{
N_{E'}\ge c'_\epsilon p^{\,2+4\sqrt e-\epsilon}.
}                                                        \tag{224.4}
$$
其中
$$
2\sqrt e=3.2974425414\ldots,\qquad
2+4\sqrt e=8.5948850828\ldots.
$$
R107 的原下界指数分别为 $2$ 与 $6$。本文不去掉 (224.2) 或非空支撑前提。

## 2. 二次基变换与普通 Dirichlet Burgess

令 $\psi$ 为二次扩张 $KF/K$ 的原始二次 Hecke 特征，并在其导子不互素的理想上置零。因为 $F\ne K$，该特征非平凡。

设 $\chi_1=\chi_F$，$\chi_2$ 为 $\chi_K\chi_F$ 所诱导的**原始** Dirichlet 特征。二者都是非主二次特征，其导子满足
$$
f_1=Q,\qquad f_2\le |D_K|Q.
$$
双二次扩张的 Artin 诱导给精确等式
$$
L_K(s,\psi)=L(s,\chi_1)L(s,\chi_2).                       \tag{224.5}
$$
也可由
$\zeta_{KF}=\zeta\,L(\chi_K)L(\chi_1)L(\chi_2)$
和 $\zeta_{KF}=\zeta_KL_K(\psi)$ 相除证明。这个等式保留分歧取消处的正确 Euler 因子；不能在所有理想上把原始 $\psi$ 机械写成带零值的 $\chi_F(N\mathfrak a)$。

置
$$
a_r=\frac{r+1}{4r^2},\qquad
S_\psi(X)=\sum_{N\mathfrak a\le X}\psi(\mathfrak a).
$$
已发表的 Norton–Burgess 估计，按 Pollack [P17, Proposition 2.1] 的表述，对任意二次非主 Dirichlet 特征、任意整数 $r\ge2$ 和 $\eta_1>0$，给
$$
\left|\sum_{n\le Y}\chi_i(n)\right|
\ll_{K,r,\eta_1}Q^{a_r+\eta_1}Y^{1-1/r}.                \tag{224.6}
$$
其常数有效。该文的附加因子为
$$
R_k(m)^{1/r},\quad
R_k(m)=\min\{M(m)^{3/4},Q(k)^{9/8}\},
$$
其中 $Q(k)$ 是 $k$ 的素数幂次数至少为二的部分。这里 $k=2$，所以 $Q(k)=1$，附加因子恰为一。故即使基本判别式含二进制导子 $8$，任意 $r$ 的使用仍然合法。R107 的实际应用只有奇平方自由导子，原始 Burgess 的立方自由版本已经足够。

由 (224.5)，
$$
S_\psi(X)=\sum_{ab\le X}\chi_1(a)\chi_2(b).
$$
令 $Y=\lfloor\sqrt X\rfloor$，$C_i(t)=\sum_{n\le t}\chi_i(n)$。双曲线公式精确给出
$$
S_\psi(X)=
\sum_{a\le Y}\chi_1(a)C_2(X/a)
+\sum_{b\le Y}\chi_2(b)C_1(X/b)-C_1(Y)C_2(Y).
$$
第一项由 (224.6) 至多为
$$
\ll Q^{a_r+\eta_1}X^{1-1/r}
\sum_{a\le Y}a^{-1+1/r}
\ll_r Q^{a_r+\eta_1}X^{1-1/(2r)}.
$$
第二项同样。最后一项对一个因子用 (224.6)，另一个用 $|C_i(Y)|\le Y$，得到相同上界。因此
$$
\boxed{
|S_\psi(X)|
\ll_{K,r,\eta_1}Q^{a_r+\eta_1}X^{1-1/(2r)}.
}                                                        \tag{224.7}
$$
这里没有使用 Hecke 特征和的额外估计。

## 3. 把变化的坏素数填成正一，保留消去界

为了使用无筛除条件的光滑理想计数，令 $\mathcal T$ 为 $K$ 中位于有理素数 $2D_KD_FB$ 上方的全部素理想。它包含 $\psi$ 的所有分歧素理想，且
$$
\prod_{\mathfrak p\in\mathcal T}N\mathfrak p
\le (2|D_K|QB)^2
\le 4D_K^2Q^{2+2A}.                                    \tag{224.8}
$$
定义完全乘法的理想函数
$$
\widetilde\psi(\mathfrak p)=
\begin{cases}
1,&\mathfrak p\in\mathcal T,\\
\psi(\mathfrak p),&\mathfrak p\notin\mathcal T.
\end{cases}                                             \tag{224.9}
$$
它在每个非零整理想上均为 $\pm1$。

记理想上的 Dirichlet 卷积为 $*$。存在非负乘法函数 $g$，支撑于 $\mathcal T$ 的乘积，使
$$
\widetilde\psi=\psi*g.
$$
逐个局部因子即可证明：若 $z=(N\mathfrak p)^{-s}$，原值分别为 $0,-1,1$，修正因子分别为
$$
\frac1{1-z},\qquad \frac{1+z}{1-z},\qquad 1.
$$
这些幂级数系数非负。

设 $\sigma=1-1/(2r)>0$。由 (224.7)，
$$
\begin{aligned}
\left|\sum_{N\mathfrak a\le X}\widetilde\psi(\mathfrak a)\right|
&\le \sum_{N\mathfrak d\le X}
g(\mathfrak d)\left|S_\psi(X/N\mathfrak d)\right|\\
&\ll_{K,r,\eta_1}
Q^{a_r+\eta_1}X^\sigma
\prod_{\mathfrak p\in\mathcal T}
\frac{1+(N\mathfrak p)^{-\sigma}}
     {1-(N\mathfrak p)^{-\sigma}}.
\end{aligned}                                           \tag{224.10}
$$
对于每个 $\eta_2>0$，这个有限 Euler 乘积有有效上界
$$
\prod_{\mathfrak p\in\mathcal T}
\frac{1+(N\mathfrak p)^{-\sigma}}
     {1-(N\mathfrak p)^{-\sigma}}
\ll_{K,A,r,\eta_2}Q^{\eta_2}.                            \tag{224.11}
$$
确切证明如下。令 $\gamma=\eta_2/(2+2A)$。当整数 $n$ 大于一个有效阈值 $n_0(\sigma,\gamma)$ 时，
$$
\frac{1+n^{-\sigma}}{1-n^{-\sigma}}\le n^\gamma.
$$
范数小于该阈值的素理想有限，其全部贡献是只依赖 $K,\sigma,\gamma$ 的有效常数。其余项用 (224.8) 相乘即得 (224.11)。

因此
$$
\boxed{
\left|\sum_{N\mathfrak a\le X}\widetilde\psi(\mathfrak a)\right|
\ll_{K,A,r,\eta_1,\eta_2}
Q^{a_r+\eta_1+\eta_2}X^{1-1/(2r)}.
}                                                        \tag{224.12}
$$
这一步同时解决分歧素数、固定小素数和增长中排除集 $B$ 的问题。填入正一会改变函数，但对消去界只增加任意小的 $Q$ 次幂。

## 4. 固定虚二次域的光滑理想计数

令
$$
A_K(X)=\#\{\mathfrak a\subset\mathcal O_K:
\mathfrak a\ne0,\ N\mathfrak a\le X\}.
$$
固定虚二次域的平面格点计数给有效估计
$$
A_K(X)=\kappa_KX+O_K(\sqrt X),\qquad X\ge1,
\quad
\kappa_K=\frac{2\pi h_K}{w_K\sqrt{|D_K|}}>0.              \tag{224.13}
$$
为说明其有效性，可在每个理想类选一个固定整理想 $\mathfrak b$。相反类中的整理想恰为
$(z)\mathfrak b^{-1}$，其中 $0\ne z\in\mathfrak b$，按 $w_K$ 个单位取商。范数上界对应半径 $\sqrt{XN\mathfrak b}$ 的圆盘；格 $\mathfrak b$ 的余体积为
$\sqrt{|D_K|}N\mathfrak b/2$。圆盘面积给每类主项
$2\pi X/(w_K\sqrt{|D_K|})$，边界给 $O_{\mathfrak b}(\sqrt X)$。有限求和得 (224.13)，各类代表及格点常数可有效求出。

称理想 $\mathfrak a$ 为 $y$-光滑，若它的每个素理想因子 $\mathfrak p$ 都有 $N\mathfrak p\le y$。固定 $1<u<2$，令 $y=X^{1/u}$。则
$$
\boxed{
\Psi_K(X,y):=
\#\{\mathfrak a:N\mathfrak a\le X,\ \mathfrak a\text{ 为 }y\text{-光滑}\}
=\kappa_KX(1-\log u)+O_{K,u}\!\left(\frac X{\log X}\right).
}                                                        \tag{224.14}
$$
这里及以下取 $X$ 大于一个有效的固定阈值。

证明只需考虑至多一个大素理想。因为 $y^2>X$，任意不光滑的 $\mathfrak a$ 恰含一个范数大于 $y$ 的素理想因子，且其指数为一。于是
$$
\Psi_K(X,y)=A_K(X)
-\sum_{y<N\mathfrak p\le X}A_K(X/N\mathfrak p).           \tag{224.15}
$$
无条件有效 Mertens 定理 [GL22, Theorem 1, (B1)–(B2)] 给
$$
\sum_{N\mathfrak p\le t}\frac1{N\mathfrak p}
=\log\log t+M_K+O_K(1/\log t),
$$
故
$$
\sum_{y<N\mathfrak p\le X}\frac1{N\mathfrak p}
=\log u+O_{K,u}(1/\log X).                              \tag{224.16}
$$
这个文献结论的常数有效，不需要 GRH 或排除异常实零点。

由有理素数的有效 Chebyshev 上界，二次域中
$$
\pi_K(t):=\#\{\mathfrak p:N\mathfrak p\le t\}
\ll t/\log t.
$$
例如上界 $2\pi(t)+\pi(\sqrt t)+O_K(1)$ 足够。部分求和给
$$
\sum_{N\mathfrak p\le X}(N\mathfrak p)^{-1/2}
\ll_K \sqrt X/\log X.
$$
因此把 (224.13) 代入 (224.15) 时，累计边界误差至多
$$
\ll_K \sqrt X\sum_{N\mathfrak p\le X}(N\mathfrak p)^{-1/2}
\ll_K X/\log X.
$$
结合 (224.16)，即得 (224.14)。

## 5. Vinogradov 正质量矛盾与所有参数的选择

令
$$
1<u<\sqrt e.
$$
若不存在满足 (224.1) 前三个条件且 $q\le y$ 的素数，则
$$
N\mathfrak p\le y\quad\Longrightarrow\quad
\widetilde\psi(\mathfrak p)=1.                           \tag{224.17}
$$
逐类核查如下：

- $\mathfrak p\in\mathcal T$ 时由定义成立；
- 其下方有理素数 $q$ 在 $K$ 惰性时，$N\mathfrak p=q^2$，而非分歧基变换角色的值为 $\chi_F(q)^2=1$；
- 其下方 $q$ 在 $K$ 分裂时，$N\mathfrak p=q$ 且 $\psi(\mathfrak p)=\chi_F(q)$。若值为负一，就得到被假设排除的测试素数；
- $K$ 的分歧素数已经全部包含于 $\mathcal T$。

因 $\widetilde\psi$ 完全乘法，所有 $y$-光滑理想取值一；其他理想的值至少为负一。由 (224.13)–(224.14)，
$$
\begin{aligned}
\sum_{N\mathfrak a\le X}\widetilde\psi(\mathfrak a)
&\ge 2\Psi_K(X,y)-A_K(X)\\
&=\kappa_KX(1-2\log u)+O_{K,u}(X/\log X).
\end{aligned}                                           \tag{224.18}
$$
记 $\mu=1-2\log u>0$。对所有 $X\ge X_0(K,u)$，
$$
\sum_{N\mathfrak a\le X}\widetilde\psi(\mathfrak a)
\ge \tfrac12\kappa_K\mu X,                              \tag{224.19}
$$
且 $X_0$ 可有效选择。

给定定理中的 $\epsilon>0$，先有效选择 $\delta>0$ 和 $1<u<\sqrt e$，使
$$
\frac{1/2+\delta}{u}<\frac1{2\sqrt e}+\epsilon.
$$
再选整数 $r\ge2$、$r>1/(2\delta)$，并置
$$
\lambda=\frac{\delta}{2r}-\frac1{4r^2}>0,\qquad
\eta_1=\eta_2=\frac\lambda4,\qquad
X=LQ^{1/2+\delta}.
$$
式 (224.12) 的右端除以 $X$ 后至多为
$$
C\,L^{-1/(2r)}
Q^{a_r+\eta_1+\eta_2-(1/2+\delta)/(2r)}
=C\,L^{-1/(2r)}Q^{-\lambda/2}.                          \tag{224.20}
$$
有效选择固定 $L\ge1$，使同时有 $L3^{1/2+\delta}\ge X_0$ 和
$$
CL^{-1/(2r)}\le \tfrac14\kappa_K\mu.
$$
则对所有二次域的 $Q\ge3$，(224.20) 与 (224.19) 矛盾。故测试素数存在，且
$$
q\le y=X^{1/u}
=L^{1/u}Q^{(1/2+\delta)/u}
\le L^{1/u}Q^{\alpha+\epsilon}.
$$
这证明定理 224.1，并直接覆盖所有 $Q$；没有留下依赖未知最小素数的有限范围填补。

## 6. 应用于同一实际整 $j$ 曲线

在 (224.2) 下，R104 给
$$
d=\prod_{q\in\mathcal S}(-1)^{(q-1)/2}q,\qquad
D_F=-3d,\qquad |D_F|=3Q_0.
$$
由 $\mathcal S\ne\varnothing$，有 $Q_0>1$，所以 $F\ne K$。

用定理 224.1，取固定 $K=\mathbb Q(\sqrt{-3})$ 和 $B=1$。对任意 $\eta>0$，得到
$$
q\ge5,\qquad \chi_K(q)=1,\quad \chi_F(q)=-1,\qquad
q\ll_\eta Q_0^{\alpha+\eta}.                            \tag{224.21}
$$
这里自动有 $q\ne p$，因为 $p\equiv2\pmod3$ 在 $K$ 惰性，而 $q$ 在 $K$ 分裂。该素数不分歧于 $F$，因此不是实际四阶惯性支撑素数。

R107 定理 107.1 对**这个同一实际曲线的测试素数**给严格必要条件
$$
q>p/4.
$$
其证明使用同一个好约化局部二次扭曲的偶整数迹 $a$、真实二除 Frobenius 和有限四次差特征，得到
$0<|a^2-3m^2|<4q$ 且 $p\mid a^2-3m^2$。本文只使用已证明的这一必要条件，不把不同曲线或不同局部相位的整数迹拼合。

结合 (224.21)，
$$
p\ll_\eta Q_0^{\alpha+\eta}.
$$
给定 $0<\epsilon<2\sqrt e$，选择 $\eta>0$ 足够小，使
$$
\frac1{\alpha+\eta}\ge 2\sqrt e-\epsilon.
$$
整理即得 (224.3)，且常数有效；较大 $\epsilon$ 的结论由弱化得到。

最后 R104 的准确规范化公式为
$$
N_{E'}=12p^2D_F^2\quad(c=6),\qquad
N_{E'}=27p^2D_F^2\quad(c=9).
$$
在 (224.3) 使用 $\epsilon/2$，立即得到 (224.4)。

## 7. 对 O4 的含义和仍缺的约束

这个论证在 $K$ 固定时把“特定二次 Frobenius 首次出现得很晚”转成变化判别式的更强下界。排除集可以含任意 $B\le |D_F|^A$，所以它不要求先找到与变化导子互素的固定测试素数。

本题实际整 $j$ 分支仍允许 $Q_0$ 随 $p$ 更快增长。R220 的共同导子与二次扭曲导子关系也只把这种增长传递到真实曲线的导子。因此 (224.3)–(224.4) 不与已有上界矛盾。要完成绝对排除，仍需同一曲线的整 $j$、三次角色或全部 Frobenius 条件迫出的上方约束，或一个不依赖 $Q_0$ 大小的整体有理点论证。

定理 224.1 的常数依赖固定的 $K$；不能直接令 $K$ 随 $p$ 变化并把常数当绝对常数。

## 8. 文献与仓库依赖

- [R104](R104-variable-discriminant-field-and-actual-cubic-conductor.md)：实际二除判别式域、四阶惯性支撑和规范化导子的准确公式。
- [R107](R107-actual-quartic-trace-parity-and-discriminant-growth.md)：实际偶整数迹、指定分裂/惰性测试素数的严格 $q>p/4$ 条件，以及旧的 $Q_0\gg p^{2-\epsilon}$ 界。
- P. Pollack，*Bounds for the first several prime character nonresidues*，Proceedings of the American Mathematical Society **145** (2017), 2815–2826，**Proposition 2.1**。[正式 DOI](https://doi.org/10.1090/proc/13432)，[作者稿全文](https://arxiv.org/html/1508.05035v2)。本文只使用该处已发表的 Norton–Burgess 估计，平滑理想和 Euler 修正均在上文证明。
- S. R. Garcia、E. S. Lee，*Unconditional explicit Mertens' theorems for number fields and Dedekind zeta residue bounds*，The Ramanujan Journal **57** (2022), 1169–1191，**Theorem 1, (B1)–(B2)**。[正式 DOI](https://doi.org/10.1007/s11139-021-00435-6)，[对应作者稿 v4](https://arxiv.org/html/2007.10313v4)。使用的是其无条件版本，非同作者另一篇以 GRH 为前提的论文。
- D. A. Burgess，*On character sums and $L$-series, II*，Proceedings of the London Mathematical Society (3) **13** (1963), 524–536，[DOI](https://doi.org/10.1112/plms/s3-13.1.524)。实际 R107 分支的两个有理导子平方自由，该经典版本已足够。

