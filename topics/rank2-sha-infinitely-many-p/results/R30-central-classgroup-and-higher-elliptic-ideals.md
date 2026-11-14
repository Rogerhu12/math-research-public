# R30：中心类群生成元数与高阶 Fitting 理想的精确判据

**可信度：已证明。** 沿用 R4、R7、R12、R27 的曲线和素数范围
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
p\equiv1\pmod4,\quad p\ge13,\quad p\ne17.
$$
本文把 R27 的中心矩阵核转到同一塔的**处处无分歧类群模**，给出中心生成元数与第二个 Fitting 理想的准确判据。该判据只要求某个中心值非零，允许非零有限 $\Sha[p^\infty]$。它比先前强求初级部分为零的条件宽，但尚未证明相应素数无穷。

## 1. 记号和主结论

固定 $p=\pi\bar\pi$，其中 $\pi=\psi_E(\mathfrak p)$。记
$$
K_n=K(E[\pi^n]),\quad K_\infty=\bigcup_{n\ge1}K_n,
\quad \operatorname{Gal}(K_\infty/K)=\Delta\times\Gamma.
$$
这里 $\Delta\simeq\mathbb F_p^\times$，$\Gamma\simeq\mathbb Z_p$。在 $E[\pi]$ 上的作用字符记为 $\chi$，其 Teichmüller 提升记为 $\widetilde\chi$。取 $\gamma\in\Gamma$ 使 $\rho_E(\gamma)=1+p$，并置
$$
\Lambda=\mathbb Z_p[[T]],\qquad T=\gamma-1,
\qquad \mathfrak P=(T-p),\quad\mathfrak m=(p,T).
$$
所有上标 $\widetilde\chi$ 均表示 **$\Delta$ 通过 $\widetilde\chi$ 作用的分量**，不取逆字符。

令 $X_\infty$ 为 $K_\infty$ 上仅允许在 $\mathfrak p$ 处分歧的最大交换 pro-$p$ 扩张的 Galois 群，令
$$
M_p=X_\infty^{\widetilde\chi},\qquad
\mathcal A_p=
\left(\varprojlim_n\operatorname{Cl}(K_n)\otimes\mathbb Z_p\right)^{\widetilde\chi},
$$
后一个极限用理想范数。定义
$$
q_p=\dim_{\mathbb Q_p}
\left(\mathcal A_p/(T-p)\mathcal A_p\right)\otimes_{\mathbb Z_p}\mathbb Q_p.
\tag{1.1}
$$
这是中心**几何生成元数**，不是特征级数在 $T=p$ 的消失重数。

记 $s_{\infty,p}=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$。则
$$
\boxed{\quad q_p\ge1,\qquad
s_{\infty,p}=2\left\lceil\frac{q_p}{2}\right\rceil.\quad}
\tag{1.2}
$$
因此
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad q_p\in\{1,2\}.
\quad}\tag{1.3}
$$

等价地，令 $\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)$ 为第二个高阶 Fitting 理想，则
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)
\not\subset\mathfrak P.
\quad}\tag{1.4}
$$
右端表示存在 $F_p(T)\in\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)$ 满足 $F_p(p)\ne0$。允许 $v_p(F_p(p))$ 任意大，**不要求它为单位**。

## 2. 从类域论得到相差至多一的精确不等式

用 Rubin §§11.2–11.3 的记号，$U_\infty$ 为在 $\mathfrak p$ 处局部单位的范数极限，$E_\infty$ 为全局单位的 $p$-完备化范数极限。Rubin §11.2，式 (13)，由类域论给出
$$
0\longrightarrow U_\infty/E_\infty
\longrightarrow X_\infty
\longrightarrow A_\infty\longrightarrow0.
\tag{2.1}
$$
其中 $A_\infty$ 是处处无分歧模，而非另一个仅在某处无分歧的替代模。对 (2.1) 取 $\widetilde\chi$ 分量是正合的，因为 $p\nmid|\Delta|$。

R20、R24 已证明 $U_\infty^{\widetilde\chi}$ 为自由秩一 $\Lambda$-模。故
$$
B_p=(U_\infty/E_\infty)^{\widetilde\chi}
$$
是一个循环 $\Lambda$-模，并有正合列
$$
0\longrightarrow B_p\longrightarrow M_p
\longrightarrow\mathcal A_p\longrightarrow0.
\tag{2.2}
$$
在 $\mathfrak P$ 处局部化。局部环
$$
R=\Lambda_{\mathfrak P}
$$
是离散赋值环，极大理想由 $T-p$ 生成，剩余域为 $\mathbb Q_p$。商去 $\mathfrak P$ 后的右正合列为
$$
(B_p)_{\mathfrak P}/\mathfrak P(B_p)_{\mathfrak P}
\longrightarrow (M_p)_{\mathfrak P}/\mathfrak P(M_p)_{\mathfrak P}
\longrightarrow (\mathcal A_p)_{\mathfrak P}/\mathfrak P(\mathcal A_p)_{\mathfrak P}
\longrightarrow0.
\tag{2.3}
$$
左端是循环 $R$-模的剩余空间，维数至多一。右端维数是 $q_p$。由 R27，中央维数恰为 $s_{\infty,p}$。因此
$$
q_p\le s_{\infty,p}\le q_p+1.
\tag{2.4}
$$
这里无需断言 (2.3) 左端映射单射；可能出现的 Tor 正是不能任意选定两种维数之一的原因，而上下界始终成立。

R4 给秩恰为二，R7 的 $p$-parity 给 $s_{\infty,p}$ 为偶数，均不预设 $\Sha[p^\infty]$ 有限。两个相邻整数 $q_p,q_p+1$ 中唯一的偶数为 $2\lceil q_p/2\rceil$。若 $q_p=0$，(2.4) 会给偶数 $s_{\infty,p}=0$，与秩二下界矛盾。因此 $q_p\ge1$，得到 (1.2)。初级群有限等价于 $s_{\infty,p}=2$，再得 (1.3)。

## 3. 与首层相对类群维数以及有限 Sha 商的关系

令 $c_p$ 是 R7、R12 的相对类群维数。R12 给
$$
c_p=\dim_{\mathbb F_p}\operatorname{Cl}(K_1)[p]^\chi.
$$
Rubin Lemma 11.1 的准确范数控制给
$$
\mathcal A_p/T\mathcal A_p
\simeq\bigl(\operatorname{Cl}(K_1)\otimes\mathbb Z_p\bigr)^{\widetilde\chi}.
\tag{3.1}
$$
有限交换 $p$-群的 $p$-挠与模 $p$ 商有相同维数，故
$$
c_p=\dim_{\mathbb F_p}\mathcal A_p/\mathfrak m\mathcal A_p.
\tag{3.2}
$$

R25 证明 $M_p$ 是有限秩自由 $\mathbb Z_p$-模，故它的商 $\mathcal A_p$ 是有限生成 $\mathbb Z_p$-模。令 $D_p=\mathcal A_p/(T-p)\mathcal A_p$。则
$$
q_p=\operatorname{rank}_{\mathbb Z_p}D_p
\le\dim_{\mathbb F_p}D_p/pD_p
=c_p,
\tag{3.3}
$$
最后一步使用 $(p,T-p)=(p,T)$。

于是有限层和无限层的两个准确公式并列为
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=2\left\lceil\frac{c_p}{2}\right\rceil,
\qquad
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
=2\left\lceil\frac{q_p}{2}\right\rceil.
\tag{3.4}
$$
设 $\Sha_p^{\mathrm{fin}}$ 表示 $\Sha(E/\mathbb Q)[p^\infty]$ 商去最大可除子群后的有限商。由 R27 的结构结论，或由可除子群在交换群中可裂这一事实，得到
$$
\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]
=2\left\lceil\frac{q_p}{2}\right\rceil-2,
\tag{3.5}
$$
以及
$$
\dim_{\mathbb F_p}\Sha_p^{\mathrm{fin}}[p]
=2\left(
\left\lceil\frac{c_p}{2}\right\rceil-
\left\lceil\frac{q_p}{2}\right\rceil\right).
\tag{3.6}
$$
(3.6) 只给有限商的 $p$-秩；其元素阶和各循环因子仍由 R27 的 Smith 分解决定。这里没有声称 Mordell–Weil 嵌入附带一个规范直和分解。

因此 $q_p\le2$ 保留了任务只求初级有限的宽度。它不强迫 $c_p\le2$；后一个条件等价于初级群为零。

## 4. 中心处的高 Fitting 理想

对于有限生成模 $N$，采用 $\operatorname{Fitt}_{R,i}(N)$ 为某个有限呈现矩阵的余阶 $i$ 子式生成的理想这一通常约定。因此在局部环上
$$
\operatorname{Fitt}_{R,i}(N)=R
\quad\Longleftrightarrow\quad
N\text{ 可由至多 }i\text{ 个元素生成}.
\tag{4.1}
$$
本处也可直接验证：在 DVR $R=\Lambda_{\mathfrak P}$ 上写
$$
(\mathcal A_p)_{\mathfrak P}
\simeq\bigoplus_{j=1}^{q_p}R/(T-p)^{e_j},\qquad e_j\ge1.
\tag{4.2}
$$
则 $q_p$ 是最小生成元数。对角呈现的子式说明 Fitting 理想等于单位理想恰在 $i\ge q_p$ 时发生。因此
$$
q_p\le2
\quad\Longleftrightarrow\quad
\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)
\not\subset\mathfrak P.
\tag{4.3}
$$

这与只知道特征理想不同。后者仅给 (4.2) 的总长度 $\sum_j e_j$，而 (4.3) 控制直和项数。例如 $R/(T-p)^m$ 的长度可任意大，生成元数始终为一。故中心消失阶大本身不使 (4.3) 失效。

结合 (4.3) 与 (1.3) 即得 (1.4)。评价 $F(T)\mapsto F(p)$ 的核恰为 $(T-p)$：评价收敛，而整幂级数除以首一线性多项式的余项就是 $F(p)$。

作为对照，局部环 $\Lambda$ 上的生成元数判据及 (3.2) 给
$$
c_p\le2
\iff \operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)=\Lambda
\iff \Sha(E/\mathbb Q)[p^\infty]=0.
\tag{4.4}
$$
因此“理想不包含于中心素理想”和“理想等于整个环”分别对应本题的有限目标与更强的零目标。

## 5. Euler 系统实现与尚未完成的跨素数步骤

将本结果的高阶 Fitting 理想写成椭圆单位或 Rubin–Stark 元素的显式理想，有望提供可研究的算术输入。Ohshita II 的相应陈述及字符条件已在
[来源审计笔记](../notes/2026-11-12-higher-elliptic-ideals-source-audit.md)
中逐项记录；该笔记清楚分离了已经核查的适用条件与尚需补足的来源或证明。本文的 (1.2)–(1.4)、(3.3)–(3.6) 不依赖那项额外比较。

当前无条件得到的准确开放目标是
$$
\#\{p:q_p\le2\}=\infty,
$$
也就是对无穷多个 $p$，存在第二个 Fitting 理想中的元素在 $T=p$ 非零。它不要求同一素数处的类群最小生成元数 $c_p\le2$，也不要求任一特征级数的中心消失阶最多二。本文没有证明这个跨素数非零性，因而主问题仍未完成。

## 来源

- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，SWC 讲义，§11.2 式 (13)、Lemma 11.1、Propositions 11.2–11.5：[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- 本仓库 R4、R7、R12、R20、R24、R25、R27：秩二、有限层与无限层 parity、字符方向、局部单位自由性及准确 Selmer 控制。
