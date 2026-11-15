# 原 Koszul 外支撑扭子模、所选子式与最高系数检验

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

## 1. 对象、已付身份和本稿范围

固定本课题同一自然参数 $u=1/s$、同一原始权齐次化以及同一原行集 $I$、原来源列集 $J$。原矩阵与所选方阵分别为

$$
A(u)\in R^{4367\times6188},\qquad
B(u)=A(u)[I,J]\in R^{4354\times4354},
$$

其中本稿分别取 $R=\mathbf Q[[u]]$ 和 $R=\mathbf F_{31}[[u]]$。两种域中原矩阵的泛秩均为 $n=4354$，且同一个 $B$ 在分式域上可逆。常数所选矩阵在两种域中均秩 $4318$。这些对象使用原式的常数单位重标；不把有限域预基的系数解释成有理系数。

令 $\Phi(u):R^{1632}\to R^{6188}$ 是原十七式的标准 Koszul 来源族：全部 $136$ 个 $F_j e_i-F_i e_j$，各乘 $1,m_0,\ldots,m_{10}$。这里仅使用这 $1632$ 列，不宣称它们生成整个 Koszul 模。其自然权齐次化满足

$$
A(u)\Phi(u)=0.
$$

已经证明并实际核对：$\Phi(0)$ 在上述两种域中均满列秩 $1632$；投影到 $J^c$ 的常数矩阵秩均为 $1603$。因此定义

$$
O(u)=\operatorname{pr}_{J^c}\Phi(u)
       \in R^{1834\times1632}
$$

后，它恰有 $29$ 个正 Smith 指数。下文记为
$\alpha_1,\ldots,\alpha_{29}$，并记

$$
\sigma=\sum_{i=1}^{29}\alpha_i,\qquad
a=\max_i\alpha_i.
$$

这些指数在两种域中应分别计算；本稿不把有限域的指数直接当成特征零指数。

本稿使用的原身份和已付边界可追溯至：

- [原低 Koszul 来源的自然权齐次头](R150-appendix-infinity-weighted-heads-of-paid-low-koszul-sources.md)；
- [固定二十九条曲线的一阶外支撑](R150-appendix-fixed-koszul-curve-first-outside-rank29-and-no-constant-second-support.md)；
- 当前会话的 [二十九个完整原来源及第二配对回执](../notes/r150-infinity-remote-session-789f/43702348535-same-source-koszul29-second-pairing.json)；
- 同一 $I,J$ 的 [自然参数完整有限域 Schur 重建回执](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-u-minimal-rebuild32.json)。

后一回执实际付清 $\mathbf F_{31}$ 上所选 $B$ 的全部 $36$ 个正指数：总和 $243$、最大值 $21$。这是同一原子式的数值，不是全矩阵无穷远 torsion 总长。

## 2. 两个保持原来源的注入

设

$$
K=\ker_R A,\qquad
\Psi=\operatorname{pr}_{J^c}|_K:K\longrightarrow R^{1834}.
$$

因为 $R$ 是离散赋值环，$K$ 是 $R^{6188}$ 的饱和自由子模，秩为 $1834$。若 $k\in K$ 且其 $J^c$ 坐标为零，则 $B\,k_J=0$；$B$ 在分式域上可逆，故 $k=0$。所以 $\Psi$ 单射且在分式域上为同构。

$\Phi(0)$ 满列秩意味着 $\operatorname{im}\Phi$ 是 $R^{6188}$ 的一个原始直和因子。因此 $K/\operatorname{im}\Phi$ 无扭，且 $O=\Psi\Phi$ 在分式域上满列秩 $1632$。

自然商映射给出

$$
0\longrightarrow K/\operatorname{im}\Phi
 \longrightarrow \operatorname{coker}O
 \longrightarrow \operatorname{coker}\Psi
 \longrightarrow0.
$$

第一项无扭，所以限制到扭子模后得到单射

$$
\operatorname{tors}(\operatorname{coker}O)
 \hookrightarrow\operatorname{coker}\Psi.
\tag{2.1}
$$

也可直接检查：若扭子类由 $v=\Psi b$ 表示，且
$u^k v=Oa=\Psi\Phi a$，则 $\Psi$ 单射迫使
$u^k b=\Phi a$；$\operatorname{im}\Phi$ 的原始性再迫使
$b\in\operatorname{im}\Phi$，故该扭子类本来就是零。

第二个单射保留同一所选原输出。定义

$$
\theta:R^{J^c}\longrightarrow\operatorname{coker}B,
\qquad z\longmapsto[A_{I,J^c}z].
$$

显然 $\Psi K\subset\ker\theta$。反之，若 $\theta(z)=0$，存在 $x_J$ 使
$A_{I,J}x_J+A_{I,J^c}z=0$。由于 $A$ 泛秩为 $n$ 且 $A_{I,J}$ 泛可逆，
投影到 $I$ 在 $\operatorname{im}_{\operatorname{Frac}R}A$ 上单射；
因此完整原输出也为零，$(x_J,z)\in K$。故
$\ker\theta=\Psi K$，得到

$$
\operatorname{coker}\Psi
 \hookrightarrow\operatorname{coker}B.
\tag{2.2}
$$

合并为

$$
\boxed{\;
\operatorname{tors}(\operatorname{coker}O)
 \hookrightarrow\operatorname{coker}\Psi
 \hookrightarrow\operatorname{coker}B.
\;}
\tag{2.3}
$$

这不是对外支撑矩阵的任意截断；全部 $1834$ 个外来源坐标均保留。

## 3. 有限域筛选的严格截止与特征零边界

由 (2.3)，任何域上均有

$$
\sigma\le v_u\det B,\qquad
a\le a_{\max}(B).
\tag{3.1}
$$

因此已经付清的同一 $B_{\mathbf F_{31}}$ 数据严格给出

$$
\sigma_{31}\le243,\qquad a_{31}\le21.
\tag{3.2}
$$

所以对 $O_{\mathbf F_{31}}$ 作完整常数单位消去后，只需把真实
$231\times29$ Schur 系列算至 $u^{21}$，即可付清其全部正 Smith 指数。
这里“至 $u^{21}$”包含该次系数，即系列精度为 $22$。
若某实现到此仍有未定正指数，须检查输入、原参数或算法；不能用 (3.2)
代替缺失的原系列身份。

这给出一个较小的真实筛选任务，而不是一次新的 $4354$ 阶常矩阵消元。
它仍须核对原 $\Phi$、同一 $J$、实际 $1603$ 阶单位块和全部外来源行。

整系数模型的非零有限域最大子式还给出

$$
\sigma_{\mathbf Q}\le\sigma_{31}.
\tag{3.3}
$$

理由是取实现 $\sigma_{31}$ 的某个原最大子式；其 $u^{\sigma_{31}}$
系数模 $31$ 非零，所以该同一整数子式在 $\mathbf Q$ 上的消失阶至多
$\sigma_{31}$。对全部最大子式取最小值得 (3.3)。

(3.2) 不给出 $a_{\mathbf Q}\le21$。目前同一 $B$ 的
$\mathbf Q$ 最大指数可由已付特征零 cofactor 下界 $125$ 与
$v_u\det B\le243$ 得到上界 $118$；若后继另付 cofactor 下界
$127$，该上界才随之变成 $116$。这种上界与有限域截止必须分开。

## 4. 外支撑 Smith 权给出的同一子式界

在当前域上取 $A$ 的 Smith 分解，写成

$$
A=P
\begin{bmatrix}
\operatorname{diag}(u^{a_1},\ldots,u^{a_n})&0\\
0&0
\end{bmatrix}
V,
$$

其中两端矩阵可逆且系数在 $R$ 中。令 $E$ 为 $V$ 的前 $n$ 行。
则 $K=\ker E$。用 $O$ 的右侧可逆变换取得 $29$ 条真曲线
$\kappa_i=\Phi t_i$，使

$$
\operatorname{pr}_{J^c}\kappa_i\in u^{\alpha_i}R^{1834}.
$$

由于 $\Phi(0)$ 满列秩且这 $29$ 列在 $O(0)$ 的核中，其
$\kappa_i(0)_J$ 线性独立。把 $\kappa_i|_J$ 补成
$U_J\in\operatorname{GL}_n(R)$，由 $E\kappa_i=0$ 得

$$
E_J U_J
 =Y\operatorname{diag}
   (u^{\alpha_1},\ldots,u^{\alpha_{29}},1,\ldots,1)
\tag{4.1}
$$

，其中 $Y$ 的系数仍在 $R$。因此 $E_J$ 的全部 $n$ 阶子式至少含
$u^\sigma$，全部 $(n-1)$ 阶子式至少含 $u^{\sigma-a}$。
这是关于子式理想的陈述；右乘可逆矩阵不改变该理想。

记 $\delta_k(A)$ 为原 $A$ 的全部 $k$ 阶子式的最小消失阶。
由 Cauchy–Binet 逐项相乘，得到

$$
\boxed{v_u\det B\ge\delta_n(A)+\sigma.}
\tag{4.2}
$$

对所选 $B$ 的任意 cofactor，同样得到

$$
\boxed{v_u(\text{cofactor})\ge
       \delta_{n-1}(A)+\sigma-a.}
\tag{4.3}
$$

把 $B$ 的任一来源列换成原 $A$ 的另一来源列时，活动来源因子的新列
仍正则；沿该列展开，只使用 $E_J$ 的 $(n-1)$ 阶子式。因此每一个这样的
原来源换列子式满足

$$
\boxed{v_u(\text{原来源换列子式})\ge
       \delta_n(A)+\sigma-a.}
\tag{4.4}
$$

任意解析目标列只可直接用 (4.3) 的 cofactor 界，不能自动使用
(4.4) 的原来源列界。上述论证也没有要求 $\kappa_i(u)$ 的所有高次项
仍支撑于 $J$；外支撑的整除阶正是公式所保留的信息。

## 5. 最高系数为 $31$ 单位的可执行判据

设原所选多项式子式为 $D(s)$，其自然总权为 $H=8770$，于是

$$
\det B(u)=u^{8770}D(1/u).
$$

已付有限域长度 $243$ 给出

$$
\deg\overline D=8770-243=8527,\qquad
v_u\det B_{\mathbf Q}\le243.
\tag{5.1}
$$

如果后继在特征零真正付清一个完整原矩阵界 $L\le\delta_n(A_{\mathbf Q})$
以及本稿同一 $O_{\mathbf Q}$ 的长度 $\sigma_{\mathbf Q}$，并满足

$$
L+\sigma_{\mathbf Q}\ge243,
\tag{5.2}
$$

则 (4.2) 与 (5.1) 夹逼得到

$$
v_u\det B_{\mathbf Q}=243,\qquad
\deg D=8527.
$$

同一 $u^{243}$ 系数已经模 $31$ 非零，故 $D$ 的最高系数是
$\mathbf Z_{(31)}$ 中的单位。这里付清的是同一 $D$ 的最高系数；
泛秩相同本身不能给出这一结论。

先算 $\sigma_{31}$ 的作用是决定较小特征零外支撑任务是否值得继续。
例如若固定已付下界 $L$ 满足 $L+\sigma_{31}<243$，则仅用这个 $L$
和 (4.2) 尚不足以闭合最高系数条件；这不否定真实
$\delta_n(A_{\mathbf Q})$ 更大，也不否定最高系数实际为单位。
反之，$L+\sigma_{31}\ge243$ 只是继续真 $\mathbf Q$ 计算的筛选信号，
并不替代 (5.2)。

本稿没有执行新的 $O(u)$ 数值计算，没有产生新的完整 $\mathbf Q[s]$
目标成员性结论，也不把已完成的一次模 $31^6$ 原身份升级成全精度结论。
