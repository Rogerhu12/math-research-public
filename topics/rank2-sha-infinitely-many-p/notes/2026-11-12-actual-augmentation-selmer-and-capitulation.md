# 实际增广类的 Selmer 部分与 Sha 消失核

日期：2026-11-12。状态：本文的正合列与局部比较均已证明。
它们把当前单素数 Heegner 类剩余的全局条件写在实际点群中，
没有证明所指定的 Heegner 类非零。

取 R103–R106 的固定
$$
E:y^2=x^3-17x,\qquad F=\mathbb Q(\sqrt{-15}),
$$
以及合法的 $M_\ell=1$ 辅助素数。写 $L=L_p$，
$\Gamma=\operatorname{Gal}(L/F)=\langle\tau\rangle\simeq C_p$。
在 $\lambda\mid\ell$ 处，$L/F$ 全分歧，剩余域不变，
$E$ 好约化且 $\ell\ne p$。全局有 $E(L)[p]=0$。
取
$$
N=1+\tau+\cdots+\tau^{p-1},\qquad
\Delta=\tau-1,\qquad
D=\sum_{j=1}^{p-1}j\tau^j,
$$
$$
\mathcal M=\ker(N:E(L)\longrightarrow E(F)),\qquad
B=\mathcal M/\Delta\mathcal M.
\tag{1}
$$
实际点是 $Q_{\ell,p}=\operatorname{Tr}_{F[\ell]/L}P[\ell]$。
这里完整保留 prime-to-$p$ 的迹；本文不把原始点 $P[\ell]$ 或
R105 的类数二求和点 $X_\ell$ 换成 $Q_{\ell,p}$。

## 1. 唯一下降与真实 Selmer 子群

R104 已证明一个单射
$$
\iota:B\lhook\joinrel\longrightarrow H^1(F,E[p]),
\qquad [Q]\longmapsto[c_Q],
\tag{2}
$$
其限制到 $L$ 是 $DQ$ 的 Kummer 类。
为了固定所有符号，若 $pZ=DQ$，$g\in G_F$ 在 $\Gamma$ 中的像是
$\tau^k$，则
$$
c_Q(g)=gZ-Z-\sum_{j=0}^{k-1}\tau^jQ.
\tag{3}
$$
在 Weil–Châtelet 群中的像准确为 $-\operatorname{inf}[Q]$。
定义实际子群
$$
B_{\mathrm{Sel}}=
\iota^{-1}\bigl(\operatorname{Sel}_p(E/F)\bigr),
\qquad
\operatorname{Cap}_{L/F}(E)[p]
=\ker\bigl(\Sha(E/F)[p]\longrightarrow\Sha(E/L)[p]\bigr).
\tag{4}
$$
这里 $\operatorname{Cap}$ 是 Sha 类在这个指定循环扩张中的消失核，
不是全局类群，也没有被假定为零。

**命题 1。** 存在准确短正合列
$$
0\longrightarrow\frac{NE(L)}{pE(F)}
\xrightarrow{\ j\ }B_{\mathrm{Sel}}
\xrightarrow{\ -\operatorname{inf}\ }
\operatorname{Cap}_{L/F}(E)[p]\longrightarrow0,
\qquad j([NZ])=[\Delta Z].
\tag{5}
$$
左端经 $\iota$ 映为 $-\delta_p(NE(L))$。

证明：R104 的整数点正合列是
$$
0\longrightarrow NE(L)/pE(F)\longrightarrow B
\longrightarrow H^1(\Gamma,E(L))\longrightarrow0.
$$
Inflation–restriction 将最后一项单射到 $H^1(F,E)$，
像恰为限制到 $L$ 后消失的类。这个群被 $p$ 杀掉。
其一个像属于 Sha，当且仅当其在所有 $F_v$ 上为零。
对任意提升 $c_Q\in H^1(F,E[p])$，局部 Kummer 正合列说明，
这恰好等价于 $c_Q$ 满足全部通常 Selmer 局部条件。
因此把 R104 正合列限制到 Sha 的逆像便得到 (5)，包括右端满射。
左端公式是
$D\Delta Z=pZ-NZ$ 在 (3) 中的直接计算。证毕。

此证明没有要求 $\Sha(E/F)$ 有限，也没有要求 $\Sha(E/L)$ 有限。
特别地，$\operatorname{Cap}[p]$ 可以包含未知可除部分的 $p$ 挠点；
不能在本题中先将其删除。

## 2. 全部这些 Selmer 类在辅助素数处自动为零

**命题 2。** 对每个 $b\in B_{\mathrm{Sel}}$，
$$
\operatorname{loc}_{\lambda}(\iota(b))=0
\quad\text{于 }H^1(F_\lambda,E[p]).
\tag{6}
$$

证明：取 $b=[Q]$，并将 $Q$ 约化到 $L_\lambda$ 的剩余域。
全分歧使全部 $\tau^j$ 在剩余域上作用相同。因此
$$
0=\overline{NQ}=p\bar Q,
\qquad
\overline{DQ}=\frac{p(p-1)}2\bar Q=0.
\tag{7}
$$
因为 $p$ 为奇数，第二式由第一式确实成立。
所以 $DQ$ 落在好约化的形式群中。
乘 $p$ 在 residue characteristic 为 $\ell\ne p$ 的形式群上是同构，
故 $DQ\in pE(L_\lambda)$。
由 (2)，$c_Q$ 的局部类限制到 $L_\lambda$ 后为零。

另一方面，$c_Q$ 是 Selmer 类，其局部像来自 $E(F_\lambda)/p$。
光滑约化和形式群上的乘 $p$ 同构，给出交换方块的两条同构
$$
E(F_\lambda)/pE(F_\lambda)
\simeq\widetilde E(k_\lambda)/p\widetilde E(k_\lambda)
\simeq E(L_\lambda)/pE(L_\lambda).
\tag{8}
$$
两边使用同一个剩余域，所以 Kummer 有限局部条件上的限制是单射。
局部类既在这个子空间中、限制后又为零，故本身为零。证毕。

这里不能把局部等式 $pR=pS$ 直接约去 $p$：
本题辅助位确有非零 $E(F_\lambda)[p]$。
(7)–(8) 是完整的替代证明，没有假定局部无 $p$ 挠点。

同一证明也适用于 R104 的一般奇数 $n=p^M$：
把 $p,D$ 分别换成 $n,D_n$，用
$\overline{D_nQ}=n(n-1)\bar Q/2=0$ 即可。
本文后续只用已经固定的 $M=1$ 情形。

## 3. 与全部 strict Selmer 类的准确差别

置
$$
\mathcal S^{\mathrm{cap}}
=\{\kappa\in\operatorname{Sel}_p(E/F):
\text{其 Sha 像属于 }\operatorname{Cap}_{L/F}(E)[p]\},
$$
$$
\mathcal S^{\mathrm{cap},0}_{\lambda}
=\ker\bigl(\operatorname{loc}_\lambda:
\mathcal S^{\mathrm{cap}}\to H^1(F_\lambda,E[p])\bigr),
$$
$$
V_\lambda
=\ker\bigl(E(F)/pE(F)\longrightarrow E(F_\lambda)/pE(F_\lambda)\bigr),
\qquad
\mathcal N=NE(L)/pE(F).
\tag{9}
$$
由 R106 的实际局部范数公式，$\mathcal N\subseteq V_\lambda$。
命题 1、2 给出
$$
\mathcal S^{\mathrm{cap},0}_{\lambda}
=\iota(B_{\mathrm{Sel}})+\delta_p(V_\lambda),
\qquad
\iota(B_{\mathrm{Sel}})\cap\delta_p(V_\lambda)
=\delta_p(\mathcal N).
\tag{10}
$$
因而
$$
\frac{\mathcal S^{\mathrm{cap},0}_{\lambda}}
     {\iota(B_{\mathrm{Sel}})}
\simeq\frac{V_\lambda}{\mathcal N}.
\tag{11}
$$
证明 (10) 只需取一个任意 strict 类，
用 (5) 选一个具有相同 Sha 像的 $c_Q$。
二者之差是基域点的 Kummer 类；命题 2 使这个基域点属于
$V_\lambda$。交集由 (5) 的左端准确给出。

现在取 R106 的复共轭正特征。
中间的增广商必须按 R106 的反号约定取负特征；准确为
$$
0\longrightarrow\mathcal N^+
\longrightarrow B_{\mathrm{Sel}}^-
\longrightarrow\operatorname{Cap}_{L/F}(E)[p]^+
\longrightarrow0.
\tag{12}
$$
这里 $B^-_{\mathrm{Sel}}$ 的符号指实际点上的复共轭作用，
其下降 $\iota(B^-_{\mathrm{Sel}})$ 是 cohomology 的正特征。
若 R106 的约化映射
$$
\rho_\ell:E(\mathbb Q)/pE(\mathbb Q)
\longrightarrow E(\mathbb F_\ell)/pE(\mathbb F_\ell)
$$
非零，则 $V_\lambda^+=\ker\rho_\ell$ 恰为一维，
而 $\dim_{\mathbb F_p}\mathcal N^+$ 只能是 $0$ 或 $1$。
于是 (11) 的正特征商维数恰为
$$
1-\dim_{\mathbb F_p}\mathcal N^+.
\tag{13}
$$
这是实际范数像与全部 strict 消失核类的差别，
不是从已知上界线推断范数像一定非零。

还应区分一个更大的群：由全部 $\operatorname{Sel}_p(E/\mathbb Q)$
而非 $\mathcal S^{\mathrm{cap}}$ 定义的 strict Selmer 群。
只要 $\rho_\ell$ 非零，任意 Sha 类的一个 Selmer 提升都可加一个
基域点的 Kummer 类来消去它在 $\ell$ 处的值。因此准确有
$$
0\longrightarrow\ker\rho_\ell
\longrightarrow\operatorname{Sel}_p^{\ell=0}(E/\mathbb Q)
\longrightarrow\Sha(E/\mathbb Q)[p]\longrightarrow0.
\tag{14}
$$
故指定局部核线不会自动消掉 Sha 商。
(12) 保留的只是其中在所选 $L/F$ 消失的实际部分。

## 4. 已核的 Cassels–Tate 对偶关系提供什么

Morgan–Smith（2024），Corollary 4.9(2)，对正确运输的 Selmer
局部条件证明 restriction 与 corestriction 的伴随性。
通常椭圆曲线条件满足这些运输假设，因为 Kummer 映射分别与
点的基变换和范数相容。因而对
$\alpha\in\operatorname{Cap}_{L/F}(E)[p]$、$\beta\in\Sha(E/L)$，
得到的关系是
$$
\langle\alpha,\operatorname{cor}_{L/F}\beta\rangle_F
=\langle\operatorname{res}_{L/F}\alpha,\beta\rangle_L=0.
\tag{15}
$$
它给消失核对 corestriction 像的正交性。
它没有给这个像的满射性，也不单独证明消失核为零。
本题亦没有先证明可除的 Sha 部分消失，
所以不能把 (15) 当作一个已经非退化的有限群配对来约去未知类。

## 5. 对实际 Heegner 点的剩余条件

R100 已证明实际 $[Q_{\ell,p}]$ 属于 (12) 的中项。
本文加强了其定位：所有同类 Selmer 增广元素在 $\ell$ 处均为零；
整个中项恰由基域范数点部分和实际 Sha 消失核组成。
成功仍要求这个指定点的类不为零。

R105、R107、R109 对真实整数 Heegner 轨道给出的高度原始性和
较长增广长度，尚未证明 prime-to-$p$ 迹后的指定类在 (12) 中非零。
R106 可以选择 $\ker\rho_\ell$，但其可指定性只控制 (12) 左端的
容许位置。要让这条比较证明指定的单素数 Kolyvagin 类非零，
必须证明由这个实际 $[Q_{\ell,p}]$ 对应得到的范数部分非零，
或证明这个指定类在 Sha 消失核中的像非零。
任意另一个非零范数点或非零消失核类，只能证明
$B_{\mathrm{Sel}}\ne0$，不能代替指定 Heegner 类的非零性。

## 来源

- R104、R106：实际整数增广商、无全局 $p$ 挠点、下降 cocycle、
  复共轭反号与局部范数等式；本文 §1–3 由这些输入给出完整证明。
- A. Morgan、A. Smith（2024），
  *Field change for the Cassels–Tate pairing and applications to class groups*，
  Research in Number Theory **10**, Article 61，
  [正式全文](https://link.springer.com/article/10.1007/s40993-024-00545-2)，
  Corollary 4.9，特别是 (2)；Remark 4.10 说明椭圆曲线版本及来源。
  本文只使用实际伴随等式，不把它升级为未证明的满射或有限性。
