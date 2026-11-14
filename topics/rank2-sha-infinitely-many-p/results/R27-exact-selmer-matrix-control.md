# R27：非异常 CM 塔的准确 Selmer 控制与 Smith 矩阵公式

**可信度：已证明。** 固定 $E:y^2=x^3-17x$、$K=\mathbb Q(i)$，设
$$
p\ge13,\qquad p\equiv1\pmod4,\qquad p\ne17.
$$
使用 R24–R26 的
$$
\pi=\psi(\mathfrak p),\quad
L_\infty=K(E[\mathfrak p^\infty]),\quad
G_\infty=\Delta\times\Gamma,\quad
\rho_E(\gamma)=1+p,
$$
$$
\mathcal A=\mathbb Z_p[[T]],\quad T=\gamma-1,\quad
\chi=\rho_E|_\Delta,\quad
M=X_\infty^\chi.
$$
R25 已证明 $M$ 是秩 $\ell=\lambda_p^{\mathrm{Iw}}$ 的自由 $\mathbb Z_p$-模。选一组 $\mathbb Z_p$ 基，记 $T$ 的作用矩阵为 $A\in M_\ell(\mathbb Z_p)$。本文的 $A$ 是 Iwasawa 作用矩阵，不是 R24 中模 $p$ 的 Hasse 标量。

## 0. 结论

在本题全部所列非异常素数处，usual 与 extended $\mathfrak p^\infty$-Selmer 群完全相同，并有
$$
\operatorname{Sel}_{\mathfrak p^\infty}(E/K)
\simeq
\operatorname{Hom}_{\mathrm{cont}}
\bigl(M/(T-p)M,E[\mathfrak p^\infty]\bigr).
\tag{0.1}
$$
特别地，
$$
\boxed{\quad
s_p^{\mathrm{fin}}
:={\dim}_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=\dim_{\mathbb F_p}M/(p,T)M
=\ell-\operatorname{rank}_{\mathbb F_p}(A\bmod p),
\quad}\tag{0.2}
$$
$$
\boxed{\quad
s_p^\infty
:=\operatorname{corank}_{\mathbb Z_p}
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
=\operatorname{nullity}_{\mathbb Q_p}(A-pI_\ell).
\quad}\tag{0.3}
$$
所以初级有限的准确条件是 (0.3) 右边等于 $2$；初级部分为零的准确条件是 (0.2) 右边等于 $2$。

Smith 分解还确定 $\Sha[p^\infty]$ 商去最大可除子群后的有限部分。若已知初级部分有限，它确定其完整群结构与阶，而无须选定 Mordell–Weil 子群的非典范直和补。

## 1. 局部条件的核恰是中心理想

令 $W=E[\mathfrak p^\infty]$，固定相容扭点给出的 $T_{\mathfrak p}E$ 基 $x$。R24 显式构造了 $U_\infty^\chi$ 的基
$$
u_\infty=e_\chi\bigl(\beta-X(P_{\pi^n})\bigr)_n,
\qquad \beta^{p-1}=1-\pi,
$$
其中 $X(t)\in t\mathbb Z_p[[t]]$ 是严格 LT 坐标，$X'(0)=1$。该基的一阶 Coates–Wiles 矩为
$$
\operatorname{CW}_1(u_\infty)=-\beta^{-1}\in\mathbb Z_p^\times.
\tag{1.1}
$$
R24 的连续等变性包括权 $1$，给出
$$
\operatorname{CW}_1(F(T)u_\infty)
=F(p)\operatorname{CW}_1(u_\infty)
\qquad(F\in\mathcal A).
\tag{1.2}
$$

Rubin Theorem 12.3 的 Wiles 显式互反律将局部映射
$\delta_\infty:U_\infty\to T_{\mathfrak p}E$ 写为
$$
\delta_\infty(v)
=(\pi-1)\operatorname{CW}_1(v)x.
\tag{1.3}
$$
这里 $\delta t(O)=1$，所以 $\operatorname{CW}_1(v)$ 就是该定理中的 Coleman 级数 $f_v'(0)/f_v(0)$。$\pi-1$ 是单位。由 (1.1)–(1.3)，$\delta_\infty$ 在 $\chi$ 分量上是评价映射 $F(T)\mapsto F(p)$ 乘以一个固定单位。因此
$$
\boxed{\quad
(\ker\delta_\infty)^\chi
=(T-p)U_\infty^\chi.
\quad}\tag{1.4}
$$
评价核为 $(T-p)$ 可直接由首一一次多项式的 Weierstrass 除法得到。

## 2. usual 与 extended Selmer 完全相同

Rubin Proposition 12.2(i) 给出
$$
\operatorname{Sel}'_{\mathfrak p^\infty}(E/K)
=\operatorname{Hom}_{\mathrm{cont}}(M,W)^\Gamma.
\tag{2.1}
$$
其 (ii) 说明 usual Selmer 是其中那些在局部 Artin 映射的
$\ker\delta_\infty$ 像上取零的同态。

设 $\varphi\in\operatorname{Hom}_{\mathrm{cont}}(M,W)^\Gamma$。目标 $W$ 上 $\gamma$ 的作用为 $1+p$，所以
$$
\varphi((T-p)m)
=\bigl((\rho_E(\gamma)-1)-p\bigr)\varphi(m)=0
\qquad(m\in M).
\tag{2.2}
$$
局部 Artin 映射是 $\mathcal A$-线性的；由 (1.4)，$\varphi$ 因而自动消去所需的 $\chi$ 局部核。其他字符分量的像也被消去，因为将 $\varphi$ 经 $e_\chi$ 延伸到 $X_\infty$ 后，它在所有非 $\chi$ 分量上为零。于是通常 Selmer 的局部条件在 (2.1) 中自动成立：
$$
\operatorname{Sel}_{\mathfrak p^\infty}(E/K)
=\operatorname{Sel}'_{\mathfrak p^\infty}(E/K).
\tag{2.3}
$$
式 (2.2) 同时说明 (2.1) 恰好是
$$
\operatorname{Hom}_{\mathrm{cont}}(M/(T-p)M,W),
$$
证明 (0.1)。这里关键使用了非异常情形的局部自由基和 (1.4)；不把这个结论外推到局部模可能不自由的异常素数。

## 3. 有限 Selmer 也得到准确同构

令
$$
D=E(K)\otimes_{\mathcal O_K}(K_{\mathfrak p}/\mathcal O_{K,\mathfrak p})
\simeq(\mathbb Q_p/\mathbb Z_p)^2.
$$
R4、R7 已证明这里的 $\mathcal O_K$-秩为二，且 $E(K)[\mathfrak p^\infty]=0$。有限 Kummer 列为
$$
0\longrightarrow E(K)/\pi E(K)
\longrightarrow\operatorname{Sel}_\pi(E/K)
\longrightarrow\Sha(E/K)[\pi]\longrightarrow0.
\tag{3.1}
$$
无穷 Kummer 列为
$$
0\longrightarrow D
\longrightarrow\operatorname{Sel}_{\mathfrak p^\infty}(E/K)
\longrightarrow\Sha(E/K)[\mathfrak p^\infty]\longrightarrow0.
\tag{3.2}
$$
因为 $D$ 可除，对 (3.2) 取 $[\pi]$ 仍在右端满射。自然映射
$E(K)/\pi E(K)\to D[\pi]$ 是同构：在 $\mathfrak p$-局部化的自由秩二 Mordell–Weil 模上，它是 $P\mapsto P\otimes\pi^{-1}$；有限挠部分不贡献 $\mathfrak p$ 分量。右侧的映射也是恒等同构
$\Sha(E/K)[\pi]=\Sha(E/K)[\mathfrak p^\infty][\pi]$。

两条正合列的相容 Kummer 图因此给出
$$
\boxed{\quad
\operatorname{Sel}_\pi(E/K)
\simeq\operatorname{Sel}_{\mathfrak p^\infty}(E/K)[\pi].
\quad}\tag{3.3}
$$
R25 已从 $E(K)[\mathfrak p^\infty]=0$ 及限制映射的 $\Delta$ 字符检查了此自然映射没有全局核；上面的两个 Kummer 列同时证明其满射性。

现在将 (0.1) 代入 (3.3)。记 $C=M/(T-p)M$。因为在 $W$ 上 $[\pi]$ 与 $[p]$ 只差一个 $\mathbb Z_p$ 单位，
$$
\operatorname{Sel}_\pi(E/K)
\simeq\operatorname{Hom}_{\mathbb F_p}(C/pC,E[\pi])
=\operatorname{Hom}_{\mathbb F_p}(M/(p,T)M,E[\pi]).
\tag{3.4}
$$
R7 的有限层同构 $\operatorname{Sel}_p(E/\mathbb Q)\simeq\operatorname{Sel}_\pi(E/K)$ 于是给出 (0.2)。同一基变换比较在无穷层也成立，而
$$
C=M/(A-pI_\ell)M
$$
的 $\mathbb Z_p$ 秩为 $\operatorname{nullity}_{\mathbb Q_p}(A-pI_\ell)$。对它取 Pontryagin 对偶，得到 (0.3)。

## 4. Smith 分解给出的有限部分

令
$$
r=\operatorname{nullity}_{\mathbb Q_p}(A-pI_\ell),
\qquad d=\ell-r.
$$
在 $\mathbb Z_p$ 上对 $A-pI_\ell$ 作 Smith 分解，可以写成
$$
\operatorname{diag}(p^{e_1},\ldots,p^{e_d},0,\ldots,0),
\qquad 0\le e_1\le\cdots\le e_d.
\tag{4.1}
$$
单位因子已吸收到左右可逆基变换中。因此
$$
C\simeq\mathbb Z_p^r\oplus
\bigoplus_{i=1}^{d}\mathbb Z_p/p^{e_i}\mathbb Z_p,
\tag{4.2}
$$
其中 $e_i=0$ 的项是零群。式 (0.1) 给出抽象群同构
$$
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
\simeq(\mathbb Q_p/\mathbb Z_p)^r\oplus
\bigoplus_{i=1}^{d}\mathbb Z/p^{e_i}\mathbb Z.
\tag{4.3}
$$
本文不把这个直和分解称为典范。

有限商却可以典范描述。$C$ 的挠子群 $C_{\rm tors}$ 是典范的；限制同态给出
$$
\frac{\operatorname{Hom}(C,W)}{\operatorname{Div}\operatorname{Hom}(C,W)}
\xrightarrow{\ \sim\ }\operatorname{Hom}(C_{\rm tors},W).
\tag{4.4}
$$
证明如下：其核为 $\operatorname{Hom}(C/C_{\rm tors},W)$，是余秩 $r$ 的可除群；其商有限，故该核正是最大可除子群。右侧满射性也可由 $C/C_{\rm tors}$ 自由得到。

Mordell–Weil 项 $(\mathbb Q_p/\mathbb Z_p)^2$ 本身可除，必包含于 Selmer 的最大可除子群中。将 (3.2) 商掉此项后，最大可除子群的余秩减少二，而有限商保持不变。因此
$$
\operatorname{Div}\Sha(E/\mathbb Q)[p^\infty]
\simeq(\mathbb Q_p/\mathbb Z_p)^{r-2},
\tag{4.5}
$$
并有有限商的自然同构
$$
\boxed{\quad
\frac{\Sha(E/\mathbb Q)[p^\infty]}
{\operatorname{Div}\Sha(E/\mathbb Q)[p^\infty]}
\simeq\operatorname{Hom}(C_{\rm tors},W).
\quad}\tag{4.6}
$$
这里同构利用 R7 固定的限制/CRT 比较；再将 $W$ 选基识别为 $\mathbb Q_p/\mathbb Z_p$ 时，有限群的不变量不随基变化。

抽象地，可以非典范地写
$$
\Sha(E/\mathbb Q)[p^\infty]
\simeq(\mathbb Q_p/\mathbb Z_p)^{r-2}
\oplus\bigoplus_{i=1}^{d}\mathbb Z/p^{e_i}\mathbb Z.
\tag{4.7}
$$
这没有指定 Mordell–Weil 在 (4.3) 的某个坐标子空间内：任何可除秩二子群都包含于最大可除部分，其商的余秩为 $r-2$，而 (4.4) 的有限商与这种选择无关。

### 4.1 当初级部分有限时

若 $r=2$，Selmer 的最大可除子群恰好等于 Mordell–Weil 项：两者余秩同为二，其可除商余秩为零，故为零。于是
$$
\Sha(E/\mathbb Q)[p^\infty]
\simeq\bigoplus_{i=1}^{\ell-2}\mathbb Z/p^{e_i}\mathbb Z,
\qquad
\#\Sha(E/\mathbb Q)[p^\infty]=p^{\sum_i e_i}.
\tag{4.8}
$$
等价地，$\sum_i e_i$ 是 $A-pI$ 的全部 $(\ell-2)\times(\ell-2)$ 子式生成的非零理想的 $p$-赋值。当 $\ell=2$ 时取空子式为一，所得群为零。

在所有情形，R7 使用的奇偶性及有限商上的 Cassels–Tate 配对还强迫 $r-2$ 为偶数，并且 (4.6) 的非零循环因子按相同阶成对出现。无须先假设 $r=2$ 才能使用这个有限商配对。

## 5. 两个准确矩阵判据

由以上公式，
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\Longleftrightarrow
\operatorname{rank}_{\mathbb Q_p}(A-pI_\ell)=\ell-2,
\quad}\tag{5.1}
$$
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]=0
\Longleftrightarrow
\operatorname{rank}_{\mathbb F_p}(A\bmod p)=\ell-2.
\quad}\tag{5.2}
$$
前者检测几何特征空间的维数；$H_p$ 中 $T-p$ 的重数检测代数重数，两者不能互换。后者检测有限 Selmer，而非只看其余秩。

一个形式例子说明即使完整知道特征级数，也不能替代这些矩阵数据。令
$$
B_e=\begin{pmatrix}p&p^e\\0&p\end{pmatrix},\qquad
A_e=B_e\oplus B_e\qquad(e\ge0).
$$
所有这些矩阵都拓扑幂零，给出的 $\mathbb Z_p$ 自由 Iwasawa 模都无有限子模，且
$$
\det(TI_4-A_e)=(T-p)^4.
$$
但是
$$
\operatorname{coker}(A_e-pI_4)
\simeq\mathbb Z_p^2\oplus(\mathbb Z/p^e\mathbb Z)^2.
$$
所以同一个特征级数允许不同的有限商阶。再取 $A=pI_4$，特征级数仍是 $(T-p)^4$，而余核变成 $\mathbb Z_p^4$，其几何特征空间维数也不同。这些仅是满足相应代数条件的模块例子，不声称它们由本椭圆曲线实现。

## 6. 本结果尚未提供什么

R26 的极大理想阶、R25 的 $\lambda$ 与 R24 的有限权条件都是准确的充分上界。本结果将它们背后的有限 Selmer 商及整个 $p^\infty$-Selmer 群写成同一个矩阵的明确余核，且把有限 $\Sha$ 的阶与 Smith 不变量连接起来。

但 $M$ 的 $\mathbb Z_p$ 基及 $A$ 随 $p$ 改变，现有证明没有把这些矩阵实现成一个固定的有理相容系，也没有证明 (5.1) 对无穷多个 $p$ 成立。不能把矩阵表示本身当成新的跨素数比较。主要目标仍然开放。

## 引用与依赖

- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*：Proposition 12.2 的 extended/usual Selmer 比较、Theorem 12.3 的 Wiles 显式互反律；[讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- J. Coates, A. Wiles, *On p-adic L-functions and elliptic units*, J. Austral. Math. Soc. Ser. A **26** (1978), 1–25：Theorem 4 的显式局部基、§4 的 Coates–Wiles 同态；[DOI](https://doi.org/10.1017/S1446788700011459)。
- 本仓库 R4、R7：秩、无 $p$ 挠、有限和无穷层的基变换与奇偶性；R24：严格 LT 基及连续全权等变性；R25：实际 $\mathbb Z_p$ 自由性；R26：$\det(TI-A)$ 的特征理想表示。
