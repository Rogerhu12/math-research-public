# R150：八个常数真除源仍排七目标的全部标准预算

作者：normal_annihilator / root / 789f。2026-11-14 UTC。AI-assisted，GPT-6 Astra Pro。

状态：由已成原七关系及 pair run43632271378 的真实完整商数据得到的特征零固定来源族排除。没有执行新数值，没有把模幂证书写成特征零原式。后继七个增广第二方向已在run43634830833完成九个原模幂身份；它属于另一来源范围，不改变本固定族排除。

## 1. 固定八常数族与模31单射

沿用[七常数单位列族](2026-11-14-r150-seven-fixed-unit-family-and-all-budget-obstruction-789f.md)的全部字典。令 $p=31$，$D=\mathbf Z_{(31)}$，$k=\mathbf F_{31}$，$A$ 为原17式的完整整数多项式来源映射。

$\mathcal S$ 是原3333预基来源的全部参数单项式，以及原2195剩余来源中被完整模31核基判为标准的全部来源单项式。它们满足

$$
\{\bar A e:e\in\mathcal S\}
\text{ 是 }\operatorname{im}\bar A\text{ 的 }k\text{ 向量空间基}.
$$

保留七个原真实除源

$$
b_i=A\kappa_i/p^{e_i},\qquad
(e_i)_{i=1}^7=(1,1,2,2,2,2,2),
$$

再加入实际关系7003的原来源

$$
b_8=A\kappa_8/p^3,\qquad
\kappa_8=K_{3,3},\qquad \operatorname{cost}\kappa_8=87.
$$

这里 $\kappa_8$ 是已经完整保存并对原17式乘回的同一个标准整数代表。不能用一个只有相同模31商类的任意来源代替。

实际完整315商计算证明八类 $u_i=[\bar b_i]$ 线性独立，张成 $s$ 不变八维空间 $U_8$。原完整商记为

$$
Q=k[s]^{4367}/\operatorname{im}\bar A.
$$

定义只允许有限支撑的 $D$ 线性来源族

$$
P_{8,\infty}:D^{(\mathcal S)}\oplus D^8\longrightarrow D[s]^{4367},
\qquad
P_{8,\infty}(a,c)=\sum_{e\in\mathcal S}a_eAe+\sum_{i=1}^8c_i b_i .
\tag{1.1}
$$

后八列只配 $D$ 中的常数。没有加入任意 $s^j b_i$；整数像也未被证明是 $D[s]$ 子模。

上述独立性直接给

$$
\bar P_{8,\infty}\text{ 单射},\qquad
\operatorname{coker}\bar P_{8,\infty}=Q/U_8.
\tag{1.2}
$$

等式包括完整自由部分，并非只取torsion后才成立。每个有限列集于是有一个模31非零的最大列阶子式；因而其有理表示系数自动属于 $D$。这不需要假定原全部有限 $A_B$ 的秩已经等于模秩加八。

特别，对 $B\ge87$，固定族 $P_{8,B}$ 的确切列秩为

$$
4354(B+1)-157070+8.
$$

在 $B=87$ 时是226090。此计数只属于固定单位列族；它不宣称原 $A_{87}$ 的全部有理秩已由这个下界穷尽。

## 2. 两位近似与真实原来源 carry

记目标 $b_j=h_0t_j$。旧已成原来源 $Z_j$ 满足

$$
AZ_j\equiv p b_j\pmod {p^3}.
$$

[七常数族稿的完整来源身份](2026-11-14-r150-seven-fixed-unit-family-and-all-budget-obstruction-789f.md)第4节已经给出同一个有限两位系数

$$
y_j^{(2)}=(x_{0,j}+p z_j,\ pC_j,\ 0)
\in D^{(\mathcal S)}\oplus D^7\oplus D,
$$

以及真实原来源 $\eta_j$，使

$$
b_j-P_{8,\infty}y_j^{(2)}\in p^2D[s]^{4367},
$$

$$
r_j^{\rm raw}:=\frac{p b_j-AZ_j}{p^3}
\equiv
\frac{b_j-P_{8,\infty}y_j^{(2)}}{p^2}+A\eta_j
\pmod p.
\tag{2.1}
$$

因此当前原 raw 在 $Q/U_8$ 中的类，就是这个固定八常数族的准确下一位障碍。式 (2.1) 支付了保存 $Z$ 时取标准模代表的 carry；并未把保存来源直接等同于未取模的组合。

## 3. 七个目标的任意预算特征零排除

[pair 的实际八维矩阵回执](r150-seven-compatible-pair-actions-789f/43632271378-1/saved-matrix-analysis__eighth-and-raw-annihilators-receipt.json)与[实际总回执](r150-seven-compatible-pair-actions-789f/43632271378-1/seven-compatible-pair-pipeline-receipt.json)给出：

$$
[r_j^{\rm raw}]\ne0\text{ in }Q/U_8
\quad\Longleftrightarrow\quad
j\in\{2,3,4,5,7,8,10\}.
\tag{3.1}
$$

这七个非零类共同张成一维空间，最小ann均为 $s-2$；$j=6,9$ 的类为零。全部九列此前均已核505自由观察及完整315重建。

对 (3.1) 的每个负目标，

$$
\boxed{b_j\notin\operatorname{im}_{\mathbf Q}P_{8,\infty}.}
\tag{3.2}
$$

证明：假设存在有限有理表示 $b_j=P_{8,\infty}y$。第1节的单位子式先迫 $y$ 的全部系数在 $D$。将其支撑和 $y_j^{(2)}$ 的支撑合并成一个有限列集。由 (1.2) 的模 $p$ 单射，连续两次除 $p$ 得

$$
y-y_j^{(2)}\in p^2D^{(\mathcal S)\oplus8}.
$$

所以 (2.1) 进入 $Q/U_8$ 后必须为零，矛盾。该论证与来源次数、费用和选取多少个标准列无关，因此排除了整个无限标准族，而不只是某个有限 $P_{8,B}$。

对 $j=6,9$，本条不作成员资格结论：下一位类为零不能证明特征零属于该族。实际 pair 只证明这两列的原 $ph_0$ 模 $p^4$ 身份，不能据此越界。

## 4. 条件性正解仍只需一层31分母

如果某个目标确有 $P_{8,\infty}$ 的特征零表示，以上逐位唯一性不仅给所有 $c_i\in pD$，还给更强的

$$
c_8\in p^2D.
\tag{4.1}
$$

因为旧两位近似的第八列系数恰为零，而精确表示与它相差 $p^2$ 倍有限系数。前七列则满足 $c_i\equiv p(C_j)_i\pmod {p^2}$。

于是从该表示还原的原来源

$$
x=\sum_{e\in\mathcal S}a_e e
+\sum_{i=1}^7\frac{c_i}{p^{e_i}}\kappa_i
+\frac{c_8}{p^3}\kappa_8
$$

满足

$$
Ax=b_j,\qquad x\in p^{-1}D[s]^{6188}.
\tag{4.2}
$$

所以新增 $b_8$ 虽由 $p^3$ 整除产生，在这个固定族与这个目标的两位初值下仍不会强迫两层31分母。若表示已在 $P_{8,B}$ 中，原来源成本仍不超过同一 $B$。

原完整第一 Bockstein 已逐目标排除了原 $D[s]$ 的模 $p^2$ 来源，因此若这种特征零表示真的存在，则其一层31分母同时必要。当前只有 $j=6,9$ 尚未被 (3.2) 排除；并未证明它们满足这个条件。

这也说明应区别三种范围：固定八常数族的任意预算有理表示；允许所有参数多项式乘子及初值变化的 $A^+$；以及全部原有理来源。已完成的七个增广第二方向计算处理第二种范围。其[正向原 $p^2h_0$ 模 $p^5$ 证书](2026-11-14-r150-all-nine-original31squaredh0-mod31five-and-complete-related-second-789f.md)已经给出真实有限来源，但本身不证明任一固定族中的特征零成员资格。
