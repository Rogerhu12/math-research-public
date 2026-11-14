# R39. 小 Hecke 对应的实际垂直修正仅支撑于有限自同源集合

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 对满足 R33 小次数条件的真实 Hecke 对应，本文控制先前未知的实际对角拉回多度数 $\nu_i$：在没有相应自同源的超奇异分量上，$e_i\nu_i$ 为同一个常数。由此，R30、R33 的最终垂直修正向量除一个明确有限集合外完全相同。对 $T_2$ 与恒等对应的任意 trace-zero 整数组合，全部修正至多有 **4 个值**，与层素数无关；当 $p\equiv1,9,25\pmod {56}$ 时，它在整个光滑开集已平凡。对应 $gT_2-\operatorname{Tr}(T_2)\mathrm{id}$ 对全部 $p>37$ 非零。

这里的有限值结论针对已经构造的实际积分 Poincaré 线丛及其规范泛纤维截面。它没有自动识别某个尚未指定的解析 QC 高度，也没有排除全局有理点。

## 1. 模型与最终要控制的量

沿用 R28、R30、R33。令 $p\ge17$，$R=\mathbb Z_p^{\rm ur}$，$K=\operatorname{Frac}(R)$，$k=\overline{\mathbb F}_p$；也可完备化。设
$$\sigma:\mathcal Y\longrightarrow\mathcal X$$
为 Edixhoven–Parent 的正规交叉模型到最小正则模型的收缩。$\mathcal X_k=\sum_iC_i$ 约化，$U=\mathcal X^{\rm sm}$，各 $C_i$ 按超奇异 $j_i$ 标记。令 $e_i=1,2,3$ 分别对应一般 $j_i$、$j_i=1728$、$j_i=0$；只有实际超奇异的例外值才出现。

设 $D$ 为全部尖点，$d=(p-1)/2$。已证明
$$M_{ij}=C_i\cdot C_j
=-\frac{p-1}{e_i}\mathbf1_{i=j}+\frac{12}{e_ie_j},
\qquad D_{\mathcal X}\cdot C_i=\frac6{e_i}.\tag{1.1}$$
令
$$\rho=\operatorname{ord}_{\mathfrak m_P}(p)
=\frac{p-\left(\frac{-3}{p}\right)}6,$$
其中 $P$ 是约化纤维的共同奇点。对素数 $\ell\ne p$，本文的小次数条件是
$$\ell+1<\rho.\tag{1.2}$$

令 $\mathscr B_\ell$ 为实际 Hecke 对应在 $\mathcal X\times_RU$ 中的纯水平闭包所定义的线丛。R33 在参数分量的泛点 DVR 上证明该闭包有限平坦，并由 (1.2) 排除目标特化到 $P$。所以其第一变量多度数恰为
$$H_{ij}(\ell)=\#\{G\subset E_j:\ |G|=\ell,\ E_j/G\simeq E_i\},\tag{1.3}$$
且尖点范数的全部垂直缺陷为零。此处按子群计数，$E_i/k$ 是 $j_i$ 对应的超奇异椭圆曲线。

实际对角拉回从 $U$ 唯一延拓为 $\mathcal X$ 上的线丛 $K_{\mathscr B_\ell}$，记
$$\nu_i(\ell)=\deg(K_{\mathscr B_\ell}|_{C_i}).$$
对实际整数虚对应
$$F=a_0\mathrm{id}+\sum_{\ell\in S}a_\ell T_\ell,
\qquad \operatorname{Tr}(F|H^0(X,\Omega^1))=0,\tag{1.4}$$
所有用到的 $\ell$ 都满足 (1.2)，负系数解释为线丛的对偶张量幂。设双次数为
$$n=a_0+\sum_{\ell\in S}a_\ell(\ell+1).$$
R33 的最终系数精确为
$$k_i(F)=6n+d\,e_i\bigl(H_{ii}(F)-\nu_i(F)\bigr).\tag{1.5}$$
全 $U$ 上有一个积分处处非零平凡化，当且仅当全部 $k_i(F)$ 相同。本文将确定此向量的非恒定支集，而不把 $\nu_i$ 换成 Brandt 对角元。

## 2. 总拉回的共同部分与局部部分

用 R28 的正规交叉树记号：中央分量为 $A$。一般超奇异支链为 $A-D_i$，$D_i$ 再邻接 $E_i,F_i$。超奇异 $j=0$ 支链同形；超奇异 $j=1728$ 的保留分量 $F_i$ 直接邻接 $A$。若 $j=0$ 普通，还有 $A-B-C$。最终保留的恰为所有 $F_i$。

定义不依赖于 $i$ 的垂直除子
$$V=6A+\sum_{j:e_j=1}(12D_j+6E_j)
+\begin{cases}
4D_0+2E_0,&j=0\text{ 超奇异},\\
4B+2C,&j=0\text{ 普通}.
\end{cases}\tag{2.1}$$
再定义有理垂直除子
$$R_i=\begin{cases}
F_i+2D_i+E_i,&e_i=1,\\
F_i,&e_i=2,\\
F_i+\frac23D_i+\frac13E_i,&e_i=3.
\end{cases}\tag{2.2}$$
每个 $R_i$ 的全部支集都位于遗忘映射 $j:\mathcal Y\to\mathbb P^1_R$ 的特殊值 $j_i$ 上。

**引理 1。** 有真正的总拉回恒等式
$$\boxed{\quad\sigma^*C_i=\frac1{e_i}V+R_i.\quad}\tag{2.3}$$
右侧整体为整数 Cartier 除子，尽管两个加数分别可以有有理系数。

**证明。** R30 已算出 $A$ 在 $\sigma^*C_i$ 中的系数 $c_A=6/e_i$。总拉回在保留分量 $F_j$ 上的系数是 $\mathbf1_{i=j}$，并与每个被收缩分量交数零，这唯一决定其余系数。

对一般支链，$D_j^2=-1$、$E_j^2=-2$，正交方程是
$$c_{E_j}=c_{D_j}/2,\qquad
-c_{D_j}+c_A+c_{E_j}+\mathbf1_{i=j}=0.$$
故
$$c_{D_j}=2c_A+2\mathbf1_{i=j},\qquad
c_{E_j}=c_A+\mathbf1_{i=j}.$$
对超奇异 $j=0$ 支链，$D_0^2=E_0^2=-2$，得到
$$c_{D_0}=\frac23(c_A+\mathbf1_{i=0}),\qquad
c_{E_0}=\frac13(c_A+\mathbf1_{i=0}).$$
对普通 $j=0$ 链，$B^2=C^2=-2$，得到 $c_B=2c_A/3$、$c_C=c_A/3$。逐项代入 $c_A=6/e_i$ 即是 (2.3)。这些系数是整个 Cartier 除子的总拉回系数；直接检查各个可能的 $e_i$ 也可见整体为整数。证毕。

这里保留 $R_i$ 与 $1/e_i$ 的不同含义；$R_i$ 是支撑在单个超奇异支链上的有理除子，不是尖点交数。

## 3. 非自同源分量上的实际对角拉回

定义有限的自同源支集
$$S_\ell=\{i:H_{ii}(\ell)>0\}.\tag{3.1}$$
令 $Q_\ell$ 为泛纤维上 $Z_\ell$ 与对角线的交除子，$\overline Q_\ell$ 为其在 $\mathcal X$ 中的水平闭包，$Q_{\ell,\mathcal Y}$ 为其在 $\mathcal Y$ 中的严格变换。对角线不是 $Z_\ell$ 的泛纤维分量：一般椭圆曲线没有素数次数的自同源；也可直接由 §5 中非零的 $\Phi_\ell(T,T)$ 看出。

对角拉回规范截面的除子写成
$$K_{\mathscr B_\ell}\simeq
\mathcal O_{\mathcal X}\left(\overline Q_\ell+
\sum_t\lambda_{\ell,t}C_t\right),\qquad\lambda_{\ell,t}\ge0.\tag{3.2}$$
非负性来自规范截面在 $U$ 上正则；$\mathcal X\setminus U$ 为有限闭点，不产生新的 codimension-one 极点。

**引理 2。** 若 $i\notin S_\ell$，则
$$\lambda_{\ell,i}=0,
\qquad Q_{\ell,\mathcal Y}\cdot R_i=0.\tag{3.3}$$

**证明。** 在参数分量 $U_i$ 的泛点 DVR 上，R33 的实际闭包有限平坦。其目标纤维与 $C_i$ 的交数为 $H_{ii}(\ell)=0$。这是有效有限除子的非负长度，所以它没有落在 $C_i$ 的特殊点，尤其不含泛点对角图的特殊点。拉回规范截面在该 DVR 是单位，故 $\lambda_{\ell,i}=0$。

再考察 $Q_{\ell,\mathcal Y}$ 的任一几何水平分支。若其泛点为尖点，R30 证明其特化只在中央 $A$ 的 $j=\infty$ 点，不遇 $R_i$。若其泛点不是尖点，它对应一个椭圆曲线 $E$ 和一个次数 $\ell$ 的自同源：把 Hecke 商与原粗模点的同构复合即可得到该自同源。

假设这个分支遇到 $R_i$。因为 $j$ 在 $\mathcal Y$ 上正则，$j(E)$ 整且约化等于 $j_i$。椭圆曲线的潜在好约化判据于是给出一个有限扩张，在其上 $E$ 有好约化，特殊纤维同构于 $E_i$。次数素于 $p$ 的自同源延拓到好约化模型；其有限 étale 核专门化后仍有阶 $\ell$，商和专门化相容。因此得到 $E_i$ 上的次数 $\ell$ 自同源，即 $H_{ii}(\ell)>0$，矛盾。支集不相交，故交数为零。证毕。

此论证不需要确定 CM 点在超奇异支链上究竟落于 $D_i,E_i,F_i$ 中哪一条，也没有把未知分歧轨道位置作为前提。

**定理 3。** 存在一个有理数 $c_\ell$，使
$$\boxed{\quad e_i\nu_i(\ell)=c_\ell
\qquad(i\notin S_\ell).\quad}\tag{3.4}$$
可以取
$$c_\ell=Q_{\ell,\mathcal Y}\cdot V+
12\sum_t\frac{\lambda_{\ell,t}}{e_t}.\tag{3.5}$$
若补集非空，$c_\ell$ 自动为整数。

**证明。** 对 $i\notin S_\ell$，投影公式、引理 1 与引理 2 给
$$\overline Q_\ell\cdot C_i
=Q_{\ell,\mathcal Y}\cdot\sigma^*C_i
=\frac{Q_{\ell,\mathcal Y}\cdot V}{e_i}.$$
在 (3.2) 中取 $C_i$ 的次数，再由 $\lambda_{\ell,i}=0$ 和 (1.1) 的非对角项，得到
$$\nu_i(\ell)
=\frac{Q_{\ell,\mathcal Y}\cdot V}{e_i}
+\sum_{t\ne i}\lambda_{\ell,t}\frac{12}{e_ie_t}.$$
乘以 $e_i$ 即为 (3.4)–(3.5)。证毕。

这是对实际固定点除子和实际水平 Hecke 闭包的结论；交矩阵只在这些几何事实证明之后用于计算。

## 4. 恒等对应的精确多度数

恒等对应的对角拉回为 $\omega_{\mathcal X/R}^{-1}$。

**引理 4。**
$$\boxed{\quad
\nu_i(\mathrm{id})=
\begin{cases}
9-p,&e_i=1,\\
(11-p)/2,&e_i=2,\\
(11-p)/3,&e_i=3.
\end{cases}\quad}\tag{4.1}$$
因此
$$e_i\bigl(1-\nu_i(\mathrm{id})\bigr)
=p-8-\mathbf1_{j_i=1728}.\tag{4.2}$$

**证明。** 在正规交叉模型中，各分量均为光滑有理曲线，故相对典范除子与一条分量 $G$ 的交数是 $-2-G^2$。一次 $(-1)$ 曲线 $E$ 收缩为正则点时，若另一条严格变换为 $G$，则
$$K_{\rm new}\cdot G'=K_{\rm old}\cdot G-G\cdot E.\tag{4.3}$$
这来自 $\sigma^*G'=G+(G\cdot E)E$ 和 $K_{\rm old}\cdot E=-1$。

使用 R33 的实际收缩顺序：先一般支链的全部 $D_j,E_j$，再 $A$，最后普通 $j=0$ 的 $B,C$ 或超奇异 $j=0$ 的 $D_0,E_0$。

- 一般 $F_i$ 起初的典范次数为 $p-1$。相应 $D_i,E_i$ 收缩各减 $1$，收缩 $A$ 减 $2$，最后两次各减 $2$，得到 $p-9$。
- $j=1728$ 的 $F_i$ 起初为 $(p-5)/2$；收缩 $A$ 及最后两次各减 $1$，得到 $(p-11)/2$。
- 超奇异 $j=0$ 的 $F_0$ 起初为 $(p-5)/3$；它在 $A$ 被收缩时尚不邻接 $A$，最后 $D_0,E_0$ 两次各减 $1$，得到 $(p-11)/3$。

取相反数即为 (4.1)，然后直接计算得到 (4.2)。证毕。

作为附带检验，伴随公式与 (1.1) 给出 $p_a(C_i)=3$（$e_i=1$）和 $p_a(C_i)=0$（$e_i=2,3$）。虽然所有保留分量的正规化都是 $\mathbb P^1$，一般 $C_i$ 自身在共同点可奇异；不能误把其算术亏格一律当作零。

## 5. 与层素数无关的支集大小界

令 $\Phi_\ell(X,Y)\in\mathbb Z[X,Y]$ 为经典模多项式，按 $Y$ 首一归一化。自同源必要地给出
$$\Phi_\ell(j_i,j_i)=0.$$

**引理 5。** $P_\ell(T)=\Phi_\ell(T,T)$ 是次数 $2\ell$、首项系数 $-1$ 的整数多项式。因此对所有 $p\ne\ell$，
$$|S_\ell|\le2\ell.\tag{5.1}$$

**证明。** 在复 Tate 参数 $q$ 下，$j(q)=q^{-1}+744+O(q)$。以 $j(q)$ 为第一变量时，模多项式的 $\ell+1$ 个根为
$$j(q^\ell),\qquad j(\zeta_\ell^a q^{1/\ell})\quad(0\le a<\ell).$$
在第二变量也代入 $j(q)$。第一个因子主项为 $-q^{-\ell}$，其余 $\ell$ 个因子的主项各为 $q^{-1}$；故
$$P_\ell(j(q))=-q^{-2\ell}+\text{更高 }q\text{ 次数项}.$$
对一个多项式代入 $j(q)=q^{-1}+O(1)$，最低 Laurent 次数恰为其次数的相反数，系数恰为首项系数。因此 $\deg P_\ell=2\ell$ 且首项为 $-T^{2\ell}$。在任何特征约化后该多项式仍非零，根数至多 $2\ell$。每个 $i\in S_\ell$ 给出一个不同的超奇异根，得到 (5.1)。证毕。

**定理 6（有限支撑的实际修正）。** 对 (1.4) 的实际 trace-zero 整数组合，令
$$S_F=\bigcup_{\ell:a_\ell\ne0}S_\ell
\ \cup\ \{i:j_i=1728,\ a_0\ne0\}.$$
那么所有 $i\notin S_F$ 的 $k_i(F)$ 完全相同。特别地
$$|S_F|\le1+2\sum_{\ell:a_\ell\ne0}\ell,\qquad
\#\{k_i(F):i\}\le2+2\sum_{\ell:a_\ell\ne0}\ell.\tag{5.2}$$
对使用同一有限素数集合的任意多条这样的对应，其**联合修正向量**在此共同例外集合的补集上也是一个值；联合取值数满足同一个界，而不需要将各条的取值数相乘。

**证明。** 在补集上 $H_{ii}(\ell)=0$，定理 3 和引理 4 给
$$e_i(H_{ii}(F)-\nu_i(F))
=a_0(p-8)-\sum_\ell a_\ell c_\ell,$$
与 $i$ 无关。代入真正的 (1.5) 即得。对共同集合外的每个坐标同理；根数界给 (5.2)。证毕。

这是固定有限 Hecke 素数集合时与 $p$ 无关的结论；它不声称这些小素数生成全部 Hecke 代数，也不改变 R33 对完整 Hecke 格的独立秩论证。

## 6. 一个非零的显式方向：$T_2$

对 $p>19$，有 $\rho>3$，所以 $\ell=2$ 满足 (1.2)。经典模多项式的直接整数恒等式为
$$\boxed{\quad
\Phi_2(T,T)=-(T-1728)(T-8000)(T+3375)^2.
\quad}\tag{6.1}$$
例如将 Sutherland 数据库给出的
$$\begin{aligned}
\Phi_2(X,Y)={}&X^3+Y^3-X^2Y^2+1488XY(X+Y)\\
&-162000(X^2+Y^2)+40773375XY\\
&+8748000000(X+Y)-157464000000000
\end{aligned}$$
代入 $X=Y=T$ 后展开即可得到；没有依赖有限层数值实验。

所以所有例外分量都包含在
$$\{j_i=1728,\ 8000,\ -3375\}\cap\{\text{超奇异 }j_i\}.$$
恒等对应唯一额外值 $j_i=1728$ 已在同一个集合中。因而对
$$F_2=gT_2-\operatorname{Tr}(T_2|H^0(X,\Omega^1))\mathrm{id},\tag{6.2}$$
或者任意由 $T_2,\mathrm{id}$ 形成的 trace-zero 整数组合，有
$$\boxed{\quad\#\{k_i(F_2):i\}\le4.\quad}\tag{6.3}$$

**定理 7（明确的全分量积分平凡化）。** 若
$$p>19,\qquad p\equiv1,9,25\pmod {56},\tag{6.4}$$
则 (6.2) 对应的实际线丛
$$\mathscr L_{F_2}=(u_D,2h_{F_2}u_D)^*\mathcal P^{\rm ext}$$
在整个 $U$ 上平凡；R33 的规范泛纤维截面只须乘以一个共同的 $p$ 次幂即可成为积分处处非零截面。

**证明。** 三个整数 $j=1728,8000,-3375$ 分别有 CM 域 $\mathbb Q(i)$、$\mathbb Q(\sqrt{-2})$、$\mathbb Q(\sqrt{-7})$。R9 的显式模型判别式分别是 $2^6,2^9,-7^3$，所以对这里的 $p$ 都有好约化。R9 §2 的 CM 环作用和经典惯性定理证明：当 $p$ 在相应 CM 域分裂时，该模型普通约化。这个证明对当前三个模型只要求 $p\ne2,7$，不需要 R9 为十三项统一使用的 $p>163$。

条件 (6.4) 使 $p\equiv1\pmod8$，故 $(-1/p)=(-2/p)=1$；同时 $p\bmod7$ 为 $1,2,4$，故 $(-7/p)=(p/7)=1$。于是三个可能例外值全部普通，没有任何例外超奇异分量。定理 6 给 $k_i$ 为常向量，R28 的全 $U$ 判据完成证明。证毕。

## 7. 这个 trace-zero 方向对所有 $p>37$ 确实非零

不能只把 (6.2) 写出就默认它非零。以下用已发表的 gonality 下界解决，不需要估计 Hecke 固定点重数或迹。

**引理 8。** 设正亏格光滑射影复曲线 $X$ 上有一个对称有效对应 $Z$，两个投影都有限、次数均为 $m$，且 $Z$ 不含对角线。若其 Jacobian 作用是一个有理标量 $a\,\mathrm{id}$，则 $a\in\mathbb Z$、$|a|\le m$，并且
$$\operatorname{gon}_{\mathbb C}(X)\le m+|a|\le2m.\tag{7.1}$$

**证明。** 该作用保持 $H^1(X,\mathbb Z)$，故有理特征值 $a$ 是代数整数，即 $a\in\mathbb Z$。将对应正规化，记两投影为 $r,s$。在全纯微分的 $L^2$ 范数下，次数 $m$ 的拉回算子范数为 $\sqrt m$；迹算子是另一个投影拉回的伴随，范数同样为 $\sqrt m$。因此 $s_*r^*$ 的范数不超过 $m$，得 $|a|\le m$。若对应可约，使用其正规化各分量的直和，拉回范数平方仍按总次数相加，论证不变。

取足够一般的 $x,y\in X(\mathbb C)$，使 $x,y,Z(x),Z(y)$ 的相关有限支集互不相遇；$x$ 不属于 $Z(x)$、$y$ 不属于 $Z(y)$ 可由对角线不是分量保证。Jacobian 作用假设给出
$$Z(x)-Z(y)-a(x-y)\sim0.$$
此除子非零：其 $Z(x)$ 支集没有被其他项抵消。其正部次数不超过 $m+|a|$，负部同度数，所以表示它的非恒定有理函数给次数至多 $m+|a|$ 的态射到 $\mathbb P^1$。证毕。

**定理 9。** 对所有素数 $p>37$，$F_2$ 是一个非零的有理定义、Rosati 对称、trace-zero 整数 Hecke 同态。

**证明。** $T_2$ 是双次数 $3$ 的对称有效对应，且一般非 CM 椭圆曲线没有次数 $2$ 自同源，故不含对角线。若 (6.2) 为零，则 $T_2=a\,\mathrm{id}$，$a=\operatorname{Tr}(T_2)/g\in\mathbb Q$。在特征零中，Jacobians 的同态由其微分决定；因此在微分空间上的标量等式也给 Jacobian 上的标量等式。

引理 8 给 $\operatorname{gon}_{\mathbb C}(X)\le6$。另一方面，Abramovich (1996), Theorem 0.1 给出
$$\operatorname{gon}_{\mathbb C}(X)\ge
\frac7{800}[\operatorname{PSL}_2(\mathbb Z):\Gamma_{\rm ns}^+(p)]
=\frac7{1600}p(p-1).\tag{7.2}$$
最后的指数是 $p(p-1)/2$：$\operatorname{PSL}_2(\mathbb F_p)$ 的阶为 $p(p^2-1)/2$，非分裂 Cartan 正规化子与 $\operatorname{SL}_2$ 相交后再模中心的阶为 $p+1$。对所有素数 $p>37$，(7.2) 严格大于 $6$，矛盾。非零性得证；其余性质由 (6.2) 及 Hecke 对称性直接得到。证毕。

故 (6.4) 的无限剩余类中，除去 $p\le37$ 后，定理 7 给出了一个明确非零 Hecke 方向的真正全 $U$ 积分平凡化，而不是零算子的形式例子。

## 8. 得到的接口与仍然缺少的输入

R33 的小次数范数计算已经消去 $\tau_i$；本文进一步控制真正的 $\nu_i$，使固定有限 Hecke 集合的全部非恒定修正只发生在统一有限个分量上。对 $T_2$，所有层的潜在特殊值仅为 $1728,8000,-3375$，且一个明确无限素数集合上连这些修正也全部消失。

本文没有计算这至多三个例外分量上的具体数值。要给出它们，仍须计算实际固定点水平分支和对角垂直消失阶；不能仅从 $\Phi_2(T,T)$ 的根重数读出这些算术交数。更进一步，解析 QC 函数中的局部高度、全局 Mordell–Weil 格与二阶迭代积分仍须独立识别、计算和控制。积分修正支集的统一界不等于统一有理点排除。

## 9. 原始来源及使用范围

- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058, DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)；[期刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.4 的正规交叉树与 Corollary 3.2 的收缩是 §2、§4 的输入；本文写出总拉回和典范次数的完整计算。
- D. Abramovich, **A linear lower bound on the gonality of modular curves**, *International Mathematics Research Notices* **1996**, no. 20, 1005–1011, DOI [10.1155/S1073792896000621](https://doi.org/10.1155/S1073792896000621)；[作者版本](https://arxiv.org/abs/alg-geom/9609012)。Theorem 0.1 的已证明常数是 $7/800$；本文没有使用 Selberg 猜想下的改善常数。
- R. Bröker, K. Lauter and A. V. Sutherland, **Modular polynomials via isogeny volcanoes**, *Mathematics of Computation* **81** (2012), 1201–1231, DOI [10.1090/S0025-5718-2011-02508-1](https://doi.org/10.1090/S0025-5718-2011-02508-1)；[作者版本](https://arxiv.org/abs/1001.0402)。[Sutherland 的经典模多项式数据库](https://math.mit.edu/~drew/ClassicalModPolys.html) 直接列出 $\Phi_2$ 全部系数；本文只使用这个可逐项展开验证的整数多项式，不使用算法复杂度中的 GRH 假设。
- J. H. Silverman, **The Arithmetic of Elliptic Curves**, 2nd ed. (2009), VII §5（潜在好约化与 $j$ 整性）、III §4 和 VII §3（同源、好约化与素于剩余特征的挠群）。引理 2 只用这些标准事实，且已明确所需的有限扩张和素于 $p$ 的次数条件。
- 仓库 R9 §1–2：三个 CM 模型、CM 环作用和普通约化判据的证明。R28：交矩阵与全 $U$ 垂直向量判据。R30：尖点支集和乘二后的实际 Poincaré 积分线丛。R33：实际 Hecke 闭包的 codimension-one 有限平坦性、Brandt 多度数、范数单位性和最终系数公式。
