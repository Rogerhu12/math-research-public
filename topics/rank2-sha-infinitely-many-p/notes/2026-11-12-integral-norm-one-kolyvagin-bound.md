# 实际范数一 Heegner 系统的整增广比较与定量界

日期：2026-11-12。**已证明**。本篇在真实范数一格上证明
$\operatorname{length}_{\mathcal O}\Sha(A/F)[p^\infty]\le2a$。
有限层下降只用原始类的局部消失等价，不将局部 Frobenius
矩阵冒充全局 Galois 模自同态。这个界没有证明 $a=0$。

沿用 R119 的实际 $E,F,\ell,L,\Gamma,Q,A,B$：
$$
E:y^2=x^3-17x,\quad F=\mathbb Q(\sqrt{-15}),\quad
\Gamma=\operatorname{Gal}(L/F)=\langle\sigma\rangle\simeq C_p,
$$
$$
B=\operatorname{Res}_{L/F}E,\qquad
A=\ker(N:B\to E),\qquad N_\Gamma Q=0.
$$
本篇允许任何 $p\ge7$、$p\ne17$；不要求 $p$ 在 $F$ 或
$\mathbb Q(i)$ 分裂。$\ell$ 仍在这两域惰性，
$v_p(\ell+1)=1$，而 $L/F$ 是环类域中的次数 $p$ 子域。
为讨论有限指数，假设实际 $Q$ 非扭；R119 的证明在本范围同样成立。

写
$$
R=\mathbb Z_p[\Gamma],\quad
\mathcal O=\mathbb Z_p[\zeta_p],\quad \delta=\zeta_p-1,
\quad W=A(F)\otimes\mathbb Z_p=\mathcal O w,
\quad Q=\delta^a\varepsilon w.                        \tag{1}
$$
其中 $\varepsilon\in\mathcal O^\times$。与平衡一致化元
$\sigma^{(p-1)/2}(\sigma-1)$ 的指数相同。

## 1. 未除群阶的角色和准确只带一个额外 δ

在
$$
W\otimes_{\mathbb Z_p}\mathcal O
 \simeq\mathcal O[X]/(\Phi_p(X))\,w
$$
中，$X$ 表示第一因子的 $\sigma$。固定 $\chi(\sigma)=\zeta_p$，
令
$$
g_\chi(X)=\frac{\Phi_p(X)}{X-\zeta_p}.
$$
因 $g_\chi$ 首一，乘 $X-\zeta_p$ 的核恰为自由秩一格
$\mathcal O g_\chi$。另一方面，严格的多项式恒等式为
$$
e_\chi(X)=\sum_{j=0}^{p-1}\zeta_p^{-j}X^j
 =\zeta_p(X-1)g_\chi(X).
$$
在本征格上 $X$ 等于 $\zeta_p$，故
$$
e_\chi Q
 =\zeta_p\delta^{a+1}\varepsilon(\zeta_p)g_\chi w.
                                                               \tag{2}
$$
因此 $e_\chi Q$ 在真实整本征格内的指数是 $a+1$。
这个格在整个 $W\otimes\mathcal O$ 中饱和，所以按整个
Mordell--Weil 格衡量的可除指数也为 $a+1$。

另一个不同的映射是把 $X$ 直接代入 $\zeta_p$。它将生成元送到
$$
g_\chi(\zeta_p)=\Phi_p'(\zeta_p)
 =\frac{p\zeta_p^{p-1}}{\zeta_p-1},
\qquad v_\delta(g_\chi(\zeta_p))=p-2.                \tag{3}
$$
(3) 是 different 的代价；不能把它误算成 (2) 的可除指数。

## 2. 实际 Tate 格与两个整数映射

令 $I=(\sigma-1)R$。在 $\overline F$ 上取 $B=E^p$ 的坐标，
范数为坐标和，则
$$
T_pB\simeq T_pE\otimes R,\qquad
T_pA\simeq T_pE\otimes I.                            \tag{4}
$$
乘 $\sigma-1$ 给出严格的整数同构
$$
R/(N_\Gamma)\xrightarrow{\sim} I.
$$
它来自真正的阿贝尔簇同构
$$
B/E_{\rm diag}\xrightarrow{\sim}A,
\qquad \overline P\longmapsto(\sigma-1)P.             \tag{5}
$$
因为 $\ker(\sigma-1:B\to B)=E_{\rm diag}$，像为 $A$；
商后的核为零，故是同构。

以 $(\sigma-1)\mapsto1$ 将 $I$ 识别为 $\mathcal O$，
$T=T_pA$ 是自由秩二的 $\mathcal O$ 模，并成为实际的扭曲表示
$$
T\simeq T_pE\otimes\mathcal O(\chi^{-1}).             \tag{6}
$$
逆角色来自 R113 的坐标约定：$g|_L=\sigma^j$ 时，
Galois 作用把坐标 $k$ 送到 $k-j$。同时改变所有坐标方向只将
$\chi$ 换成 $\chi^{-1}$。

重要的是，商映射 $R\to\mathcal O$ 在点上对应 (5) 之前的
$B\to A$，所以把 $Q\in B(F)=E(L)$ 送到
$(\sigma-1)Q\in A(F)$。因此直接做整数特化的 leading class
是 $\delta Q$，而不是 $Q$。

## 3. 原辅助位的实际 Néron 组件

令 $K=F_\lambda$，$\lambda\mid\ell$，$K'=L_\lambda$。
这是次数 $p$ 的全分歧扩张，且 $p\ne\ell$。
$E/K$ 好约化。其良好 Néron 模型的 Weil restriction
$$
\mathscr B=\operatorname{Res}_{\mathcal O_{K'}/\mathcal O_K}
              \mathscr E_{\mathcal O_{K'}}
$$
是 $B$ 的 Néron 模型：光滑测试概形上的延拓性质可通过
Weil restriction 的伴随性直接验证。

特殊纤维的约化映射 $\mathscr B_k\to\widetilde E$ 的核是
连通 unipotent 群。可沿 $\mathcal O_{K'}/\ell$ 的幂零理想
逐层过滤；每个相邻核是 $\operatorname{Lie}(\widetilde E)$ 的
加法群。因此 $\mathscr B_k$ 连通，$\Phi_B=0$。

范数 $\mathscr B\to\mathscr E$ 的微分是 trace。因为
$\operatorname{Tr}_{K'/K}(1)=p\in\mathcal O_K^\times$，该映射
光滑；其核就是 $A$ 的 Néron 模型，延拓性质仍由泛纤维的
范数为零和目标的分离性验证。特殊纤维上的范数等于
$[p]\circ\operatorname{red}$：unipotent 群到椭圆曲线的
群同态为零，而 $p$ 个 Galois 共轭的剩余值相同。于是
$$
\Phi_A(\overline k)\simeq\widetilde E[p](\overline k),
\qquad \delta\Phi_A=0.                               \tag{7}
$$
最后一式因为 $\sigma$ 在剩余域及上述椭圆商上为恒等。
在这里 $\operatorname{Frob}_{\ell^2}=[-\ell]$，且
$\ell\equiv-1\pmod p$，故这 $p^2$ 个组件均在 $k$ 上定义。

这一区别不能省略：$B$ 在 $\lambda$ 的组件群为零；
$A$ 的组件群有 $p^2$ 个元素，却只被一个 $\delta$ 杀掉。
在其他位，$B$ 的 $p$-初级组件均为零：在好约化处这是
好约化及不分歧 Weil restriction；在 $2,17$ 处，原曲线
潜在好约化的几何组件仅含 $2,3$ 因子，且 $L/F$ 不分歧。

## 4. 不要求普通性的残余与局部检查

以下是对 Howard H.0--H.5 的实际输入核查，而不是使用
该论文介绍部分的满 $\mathrm{GL}_2$ 假设。

### 4.1 全局不可约性与 Sah 消去

$T/\delta T\simeq E[p]$。在 $p$ 分裂于 $\mathbb Q(i)$ 时，
局部 CM 普通惯性给两个不同的对角特征，且分别提供
$\operatorname{diag}(u,1)$ 和其共轭。由于
$\mathbb Q(i)\not\subset L$，还有交换两条 CM 线的元素。
这些元素生成全部二阶矩阵代数，故残余表示在 $G_F$、
$G_L$ 上绝对不可约。

在 $p$ 惰性于 $\mathbb Q(i)$ 时，同一论证使用高度二 CM
形式群的两个基本特征 $\omega_2,\omega_2^p$。未分歧 CM
二次域上的 Lubin--Tate 惯性像包含完整 Cartan；在代数闭
剩余域上其两条不同特征仍被 $G_F$ 中的非 CM 元素交换。
所以绝对不可约性仍成立。

两种情形中，CM 局部惯性都提供作用为 $-1$ 的标量。
$L/F$ 在 $p$ 不分歧，所以它在 $\chi$ 上为 $1$。
因此在 $F(E[p^\infty],L)/F$ 的表示像中有中央元素
$(-I,1)$。Sah 引理用它的 $-2$ 杀掉所需 $H^1$，给出
Howard H.2；没有依赖 $p$ 的分母。这个域在 $\mathbb Q$
上 Galois，且已经包含全部 $p$-幂单位根。

另由 R107，所有环类辅助域 $F[n]\subset F^{\rm ab}$ 均满足
$$
E(F[n])[p]=0,\qquad A(F[n])[\delta]=0.                \tag{8}
$$
后式使用实际 $A[\delta]\simeq E[p]$。

### 4.2 局部条件与对偶

在 $V=T\otimes_{\mathcal O}\operatorname{Frac}(\mathcal O)$
上取通常的 Bloch--Kato／Kummer 局部条件，再向 $T$ 及有限
商传播。它就是实际 $A$ 的局部 Kummer 条件。
$H^1(F_v,T)/H^1_f(F_v,T)$ 无 $\mathcal O$ 挠；
Mazur--Rubin Lemma 3.7.1、Howard Theorem 1.6.5 及
Proposition 2.1.3 的证明给这些条件在所有有限商上的
Cartesian 性。此断言在 $\lambda$ 也包括 (7) 的组件，
不把它们删成一个所谓无分歧条件。

下面给出包括原 $\lambda$ 在内的直接有限层 pullback 证明，
避免仅由“饱和”一词略过组件。令 $K=F_v$、
$C_k=A[\delta^k]$。对 $i\le k$，真实包含
$\iota:C_i\hookrightarrow C_k$ 对应于
$T/\delta^iT\xrightarrow{\delta^{k-i}}T/\delta^kT$。
两条完整 Kummer 正合列为
$$
0\to A(K)/\delta^jA(K)\to H^1(K,C_j)
 \to H^1(K,A)[\delta^j]\to0\qquad(j=i,k).
$$
它们的比较图右边是 $H^1(K,A)$ 中子群的真实包含。
所以 $\iota(c)$ 属于 $k$ 层 Kummer 像，当且仅当 $c$
属于 $i$ 层 Kummer 像。这正是 Cartesian 的 pullback 条件。
左边的箭头是 $P\mapsto\delta^{k-i}P$，它可能因局部
$\delta$ 挠点而有核；论证不要求局部 $H^1(\iota)$ 单射，
也没有删去这部分核。任意 Quot$(T)$ 中的单射是上述
包含再乘一个 $\mathcal O$ 单位，而单位保持 Kummer 条件。
对商映射，Kummer 像上的箭头则是
$A(K)/\delta^kA(K)\twoheadrightarrow A(K)/\delta^iA(K)$。

最后，局部点群的 $\delta$ 进完成为
$H^1_f(K,T)$：对上述 Kummer 列取逆极限，所得商是
$T_\delta H^1(K,A)$，没有 $\delta$ 挠点；这与从 $V$
传播的定义相同。各 $A(K)/\delta^kA(K)$ 有限且过渡满，
故完成到每个有限商满射，有限层传播正是完整 Kummer 像。
因此 (7) 的组件贡献在所有这些图中均被保留。Howard
出版版印页 1455 的 H.3 核查使用相同的传播性质；本段给出
本题实际 $\delta$-同源的具体实现。

取 $E$ 的 Weil 配对 $e$，在 (6) 中定义
$$
\langle x\otimes a,y\otimes b\rangle=ab\,e(x,cy).      \tag{9}
$$
这是完美、对称、$\mathcal O$-双线性的共轭对偶配对；
$\chi(g)\chi(cgc)=1$ 验证其 Galois 等变性。
Bloch--Kato 局部对偶及传播给 Howard H.4 的准确正交关系。
该构造不要求给 $A$ 选择主极化。

残余表示可延拓到 $G_{\mathbb Q}$，复共轭有两个一维
$\pm1$ 空间。R113 的局部比较在这里仍适用：
$v\ne\lambda$ 时 $L_v/F_v$ 不分歧或分裂，局部范数满射，
所以 $\delta$-条件等于 $E[p]$ 的通常条件；
$\lambda$ 处为 $L_\lambda/F_\lambda$ 的 transverse 条件。
两类条件对复共轭稳定。因此 H.5 也成立。

为明确 $p$ 处没有隐藏异常：$F_v/\mathbb Q_p$ 的次数至多
$2$。普通时 $a_p(E)$ 为偶数，Hasse 界及 $p\ge7$ 排除
$a_p\equiv\pm1\pmod p$；惰性 CM 时 $a_p=0$。
故 $E(F_v)[p]=0$。这里没有将超奇异局部条件替换成普通条件。

## 5. 实际有限诱导类与保留标签的局部比较

先固定任意整数 $K\ge1$，取 $m$ 使
$m(p-1)\ge2K$。选择辅助素数 $q$ 的集合，使其在
$F(E[p^m],L)/\mathbb Q$ 中的 Frobenius 类为复共轭。
因而 $q$ 在 $F,\mathbb Q(i)$ 均惰性，
$a_q(E)=0$，$p^m\mid q+1$，且 $F$ 中 $q$ 上方的素位在
$L/F$ 完全分裂。可以另外排除任意固定有限素数集合。

令 $n$ 为这些辅助素数的平方自由乘积，并取
$$
Y_n=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n]
       \in B(F[n])=E(LF[n]).                          \tag{10}
$$
新素数的 Heegner 范数关系与 $a_\ell(E)=0$ 给
$$
N_\Gamma Y_n=0,\qquad
\operatorname{Tr}_{F[nq]/F[n]}Y_{nq}=a_q(E)Y_n.        \tag{11}
$$
在辅助 $q$ 处还有原始 Heegner 的 Frobenius 约化同余。
两式都由原曲线的点关系取实际迹得到，无未定的 $p$ 因子。
在 $n=1$ 后再取 $F[1]/F$ 的迹，所得点准确为 $Q$。

### 5.1 原始导数类及全部 augmentation 为零

沿 Howard §1.7、§2.2.1 的有限诱导定义取
$D_q=\sum_{j=1}^{q}j\sigma_q^j$、$D_n=\prod_{q\mid n}D_q$，
再对环类群的类数部分取 coset 和。恒等式
$(\sigma_q-1)D_q=q+1-N_q$ 及 (11) 使对应 Kummer 类模
$p^m$ 不变。由 (8)，inflation--restriction 给唯一的下降
$$
c_n^B\in H^1(F,T_pB/p^m),\qquad
c_1^B=\operatorname{Kum}_B(Q).                        \tag{12}
$$
Shapiro 将这里的系数识别为 $T_pE\otimes R$。这些是
未经 comparison correction 的原始类。

为区分原始 Heegner 点与 Kolyvagin 导出整点，固定上述
coset 代表系，明确记
$$
\widetilde\kappa_n=\sum_s sD_nY_n.
$$
它是定义 $c_n^B$ 的实际整点；以下局部公式中的
$\overline{\widetilde\kappa_n}$ 指它在所选剩余域的约化。
不能将其替换为未经 $D_n$ 和 coset 和处理的 $Y_n$。

在非辅助位，类在一个不分歧扩张后变成局部 Kummer 类；
其在 $H^1(F_v,B)$ 的误差属于不分歧 $H^1$。
Néron 组件描述
$H^1_{\rm ur}(F_v,B)\simeq H^1(k_v,\Phi_B)$
及第 3 节使其 $p$-部分为零。这包括原 $\lambda$ 和 $v\mid p$。
在辅助 $q$ 处，Howard Lemma 1.7.3 的计算逐坐标适用：
$D_q$ 在不分歧类上的作用是 $q(q+1)/2=0\pmod{p^m}$，
故得到 transverse 条件。因此 (12) 满足所有实际局部条件。

augmentation 类限制到 $F[n]$ 是
$\operatorname{Kum}(D_nN_\Gamma Y_n)=0$。再次用 (8) 的
下降单射，得到严格的全系统等式
$$
\operatorname{aug}(c_n^B)=0\qquad\text{对每个 }n.     \tag{13}
$$

### 5.2 局部 Frobenius 只作用在 E 因子

在辅助 $q$ 选择一个 $L$ 上方素位，并将其他素位以
$\Gamma$ 标记。令 $\varphi_q$ 为 $\widetilde E$ 上的
算术 $q$-Frobenius。原点约化同余在所有坐标中都是
$$
Y_{nq,j}\equiv\varphi_qY_{n,j}.
$$
说明这个式子不会丢失标签：若选定素位为 $w$，则在
$\sigma^{-j}w$ 的 Frobenius 是
$\sigma^{-j}\operatorname{Fr}_w\sigma^j$；先在那里应用
原点同余、再施加 $\sigma^j$，恰得到选定剩余域中对
$\sigma^jY_n$ 施加 $\varphi_q$。所以所用局部算子为
$\varphi_q\otimes1_R$，而不是另加一次 $\Gamma$ 标签反演
的全局复共轭。又 $q\nmid n$ 时，$q$ 在 $F[n]/F$ 完全
分裂，因为其对应理想 $(q)$ 在该环类群中为主理想；
所以这里各坐标的剩余点都在 $\mathbb F_{q^2}$ 上。

以 Frobenius evaluation 识别有限局部类、以所选惯性
生成元识别奇异局部类，Howard Proposition 1.7.4 的原始
Kummer 计算是
$$
\begin{aligned}
c_n^B(\operatorname{Fr}_{q^2})
 &=\frac{\varphi_q^2-1}{p^m}\,\overline{\widetilde\kappa_n},\\
c_{nq}^B(\sigma_q)
 &=\frac{a_q-(q+1)\varphi_q}{p^m}\,\overline{\widetilde\kappa_n}.
\end{aligned}                                       \tag{14}
$$
右边按该命题的约化和除点定义；不要求
$\widetilde\kappa_n$ 本身是全局可除点。特征多项式恒等式给
$$
a_q-(q+1)\varphi_q=-q\varphi_q^{-1}(\varphi_q^2-1).
$$
所以两种局部值之间有实际的 $R/p^m$-线性自同构
$$
\Psi_q=-q\varphi_q^{-1}\otimes1_R.                   \tag{15}
$$
本题 $a_q=0$，故 $\Psi_q=\varphi_q\otimes1_R$。
它只需作为局部自同构；本文不声称它定义一个全局
$H^1(F,T_pB/p^m)$ 自同态。因为 (15) 在 $R$ 因子为恒等，
它严格与 augmentation 及 $R\to\mathcal O$ 交换。
这就是所需的真实有限--奇异比较，而不需要全局 correction。

### 5.3 有限下降只需要局部消失等价

Howard Lemma 1.6.4 的证明对下述较弱类族原样成立：
各类满足对应的有限／transverse Selmer 条件，在精度间相容，
而对每个边 $n\leftrightarrow nq$，有限和奇异局部值由
一个保持精度的局部线性同构相连。

理由如下。其 first case 只用从 $2k-1$ 向 $k$ 的提升、
Cartesian 性和低精度归纳。其余两种 case 用 Chebotarev
选择一个局部值非零的素数，再用 Proposition 1.5.9 使
相邻 stub 的局部值为零，最后由边关系推出矛盾。
整个证明不需要把局部同构延拓到全局，也不需要比较两条
不同路径的全局 correction。因此 (15) 足以保留该证明的
全部步骤。以下采用这一有限下降版本。

这里的结论是完整的 stub 包含关系，而不仅是模 $\delta$
的非零性。为便于逐式核查，列出出版版的准确位置：

1. **印页 1454，Lemma 1.6.4 的第一段。** 当
   $S^{(k)}(n)\ne0$ 时令 $i=\lambda^{(k)}(n)<k$。
   对精度的归纳先给 $\kappa_n^{(i)}\in S^{(i)}(n)=0$；
   Lemma 1.3.3 把它转换成 $\delta^{k-i}\kappa_n^{(k)}=0$。
   同页 Lemma 1.6.3 说明从 $2k-1$ 层向 $k$ 层的提升像
   是自由秩一的 $\mathcal O/\delta^k$ 模，因而该等式
   强迫 $\kappa_n^{(k)}$ 被 $\delta^i$ 整除。这一段完全
   没有使用边比较。
2. **同页 Case i。** 两个复共轭符号的剩余 Selmer 空间
   均非零。取 $\kappa_n^{(k)}$ 的一个非零
   $\delta$-torsion 多重 $d$，用 Lemma 1.6.2 选辅助素数
   使 $d$ 和相反符号的一类定位均非零。相邻顶点的
   剩余维数降二；对该维数的归纳及 Proposition 1.5.9
   给出相邻类定位为零。唯一所用边关系是“相邻类定位
   为零推出本类定位为零”，故局部可逆比较已经足够。
3. **同页 Case ii。** 一个剩余符号空间为零。选择非零
   $\delta$-torsion 多重并定位非零后，相邻顶点有两个
   非零符号空间，且总维数不变。Case i 与 Proposition
   1.5.9 令相邻类定位为零；边的非零性等价给出矛盾。
   同样没有使用两边的字面相等。
4. **印页 1455，Theorem 1.6.1 证明末段。** 对所有足够
   大 $k$ 的 stub 包含关系及紧 Selmer 到有限层的单射，
   才给出 $\kappa_1\in\delta^\lambda H^1_{\mathcal F}(F,T)$。
   量化的 $\lambda$ 正是第一段的低精度归纳与提升像给出。

此外，(15) 是同一个局部 Tate 模自同构在所有精度的
约化，而不是每层临时选择的单位。对每个辅助 $q$ 固定
一次惯性生成元后，它与所有 $\delta^b$、精度商和
$R\to\mathcal O$ 严格交换。因此上述双重归纳以及下一节
的除法均使用相容的局部关系；不要求不存在的全局
correction，亦不需要额外的路径兼容性。

## 6. 逐精度除 δ 不再损失整性

将 (12) 经 (5) 特化到 $T$。leading 为 $\delta Q$。
由于 $\mathcal O\to\mathbb F_p$ 与
$R\xrightarrow{\rm aug}\mathbb Z_p\to\mathbb F_p$ 相同，
所有类模 $\delta$ 均为零。

对任意目标精度 $k$，先选源精度至少 $k+1$，并把辅助
素数的 Frobenius 同余也选到这一精度。正合列
$$
0\to T/\delta^kT\xrightarrow{\delta}
T/\delta^{k+1}T\to T/\delta T\to0
$$
及全局 $H^0(F,T/\delta T)=0$ 给
$$
0\to H^1(F,T/\delta^kT)\xrightarrow{\delta}
H^1(F,T/\delta^{k+1}T)
\to H^1(F,T/\delta T).                              \tag{16}
$$
故每个特化类有唯一的“除 $\delta$”前像。

在任一非辅助位，Cartesian 性说这个前像仍满足局部条件；
这里不要求局部 $H^1$ 的箭头单射。在辅助 $q$ 处则确有
$$
H^1_f(F_q,T/\delta^kT)\simeq(\mathcal O/\delta^k)^2,
\qquad H^1_s(F_q,T/\delta^kT)\simeq(\mathcal O/\delta^k)^2,
$$
且在所选高同余下，(16) 的局部有限、奇异箭头均为
通常的乘 $\delta$ 注入。(15) 与 $\delta$ 交换，故有限--奇异关系中的
$\delta$ 可以消去。关系所带的辅助循环群在该精度也为
自由秩一，故张量后不引入新的核。

所得 leading 准确为 $\operatorname{Kum}_A(Q)$，由 (16)
的唯一性验证。不同精度的前像相容。Howard Lemma 1.6.4
在目标精度 $k$ 只需要一直到 $2k-1$ 的提升；原系统取到
$2k$ 即够。其 Chebotarev 引理允许任意更高的 Tate 同余：
H.2 的域已包含全部 Tate 层，残余 Kummer 类的限制仍单射。
所以这里不需要宣称一个固定有限理想上的类可无代价除法。

第 5.3 节的有限层下降于是给出
$$
\boxed{
S=\Sha(A/F)[p^\infty]\simeq M\oplus M,\qquad
\operatorname{length}_{\mathcal O}M\le a.}            \tag{17}
$$
为看清最后一个指数，取 $k$ 大于有限 $S$ 的指数和 $a$。
通常 Selmer 模是一个自由 $\mathcal O/\delta^k$ 因子加
$S$；实际点 $Q$ 在该自由因子恰有指数 $a$。
Howard 的 stub 包含关系将 leading 放进
$\delta^{\operatorname{length}M}$ 倍的 Selmer 模，所以得到
(17)。不使用 $E\otimes\mathbb Q_p$ 的 logarithm 单射。

若不做本节的除法，同一比较直接只给
$\operatorname{length}M\le a+1$；(13) 与多一层精度支付了
进一步消去这个 $1$ 的步骤。

## 7. 与原 Nekovář 界和主问题的关系

在 Nekovář §7.6.4 的原始整角色证明中，本题的
$C_4=1$、$C_5=p-1$，而第 1 节给 $C_0=a+1$。
潜在好约化组件、CM 惯性标量及完整矩阵代数分别给
$C_1=C_2=C_3=0$；排除一个固定极化／同源整数的素因子
后 $C_6=0$。因此原式只能直接读成
$\delta^{4a+2p+7}$ 的统一消去界。第 5–6 节的目的，正是
用真实范数一格支付并去掉这部分群阶损失。

即使使用 (17)，也不能从 $a<p-1$ 推出 $a=0$。
例如有限 Sha 的允许偶长度层仍可与 $a=2$ 共存。
对 R121 的 $r_+=1$ 选择，把 (17) 与实际 Cassels--Tate
分层限制联立，可以给原曲线额外 Selmer 维数与 $a$ 的
数量关系；不能将这一数量关系改写为已经证明原始性。

## 原始来源与本篇新增范围

- B. Howard, *The Heegner point Kolyvagin system*,
  Compositio Math. **140** (2004), 1439–1472；
  [出版全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)，
  [作者预印本](https://arxiv.org/pdf/1202.6340)。
  本文使用 H.0--H.5、Lemmas 1.6.2--1.6.4、Theorem 1.6.1；
  §5 将 §§1.7、2.3 的原始局部比较在实际有限诱导格中逐式
  写出，并说明只用局部消失等价即可完成所需下降。
- J. Nekovář, *The Euler system method for CM points on Shimura curves*,
  LMS Lecture Note Series **320** (2007), 471–547；
  [作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)。
  原定量常数见 §§5.11、6.1–6.2、7.2、7.6.4。
- R113、R119：实际范数一簇、Kummer 识别、整角色秩及完整 Sha 有限性。
