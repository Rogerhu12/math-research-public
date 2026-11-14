# R172：尖点型中心值非零给实际秩零商

日期：2026-11-13。

**状态：已证明的条件性秩零接口；非零中心值仍是明确前提。** 本文补上 R166、R169 中“双方导子都含 $p^2$，不能直接使用旧 squarefree/prime-to-level 环类定理”的缺口。所用主要输入是 Kings–Loeffler–Zerbes 已发表的**一般新形式**定理 11.7.3；大像条件用已发表 Studnia (2026) Proposition 2.1 的直积定理及本题的真实反射逐项验证。

这里使用的是 Studnia 已发表于 *Research in Number Theory* **12** (2026), 59 的 Euler-system 论文，不是其 Serre-uniformity submitted 文稿。也没有将该论文只对椭圆曲线陈述的 Theorem B，或关于一般阿贝尔簇的展望性 Remarks，直接当作本题商的秩定理。一般系数的 Kummer 拼接在 §7 独立给出。

## 1. 实际结论与量词

保留 R166 的实际小惯性分支。对任意配对乘子 $\alpha$，令
$$X_\alpha=X_E^\alpha(p),\qquad p>37.$$
取 R166 中一个非 CM、平凡 nebentype、权二、水平 $p^2$ 新形式 $f$；其深度零尖点参数 $\theta$ 阶为 $d=(p+1)/3>4$。取
$$
\varphi=\theta\vartheta^{\pm1},\qquad
\Xi=\varphi\circ\lambda,
\qquad \rho=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Xi.
\tag{172.1}
$$
由 R166，$K$ 虚二次，$p$ 在 $K$ 惰性，$\Xi$ 阶为 $n=p+1$，在有理 idèle 上平凡。$\rho$ 是不可约奇 Artin 表示，行列式为 $\varepsilon_K$，其有限像是阶 $2n$ 的二面体群。其在 $p$ 的导子指数为二。

**定理 172.1。** 若
$$
\boxed{L\!\left(\tfrac12,\pi_{f,K}\otimes\Xi\right)\ne0,}
\tag{172.2}
$$
则对每个 $\alpha$，R166 中属于 $V_f\otimes\rho$ 完整有理兼容系统轨道的非零商，可以取为一个真实的 $\mathbb Q$ 阿贝尔簇商 $B_{\alpha,[f,\Xi]}$，并且
$$\boxed{B_{\alpha,[f,\Xi]}(\mathbb Q)\text{ 有限}.}\tag{172.3}$$

更准确地，任何实际 Jacobian 的 $\mathbb Q$-简单因子，只要其绝对不可约兼容系统中含有满足 (172.2) 的这个因子，就有有限的有理点群。经过同源或取连通核的最优商，有限性不变。

因此 R169 的指定尖点行判据现在可以在以下条件下直接用于分母排除：保留某个满足 (172.2) 的实际轨道，并使用它确实包含的 $\varphi,\varphi^{-1}$ 两条有限角色线。若要同时使用 R169 的四条线，则分别保留这些线所属的完整轨道，并对每个不同的简单轨道提供非零中心值。不能从一个中心值非零，未经轨道识别就声称另一不等价轨道的中心值也非零。

本文没有证明对每个实际 $E,p,K$ 总能找到满足 (172.2) 的因子，也没有证明 R169 指定行在所有实际分母素数处为单位。

## 2. 权一形式、反射与 inner-twist 场

### 2.1 真实二面体 Artin 因子

用复共轭 $c$ 作 $G_K$ 的陪集代表。因为 $c^2=1$ 且 $\Xi^c=\Xi^{-1}$，$\rho$ 可以写为
$$
\rho(G_K)=
\left\{\begin{pmatrix}\zeta&0\\0&\zeta^{-1}\end{pmatrix}:
\zeta\in\mu_n\right\},
\qquad
\rho(c)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{172.4}
$$
每个 $G_{\mathbb Q}\setminus G_K$ 元素的像都是阶二反射，特征值恰为 $1,-1$。表示自对偶，保留非退化对称配对
$$\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$
由有限阶虚二次 Hecke 字符的经典 theta 构造，$\rho$ 对应一个权一尖点新形式 $g$，nebentype 为 $\varepsilon_K$。这里不可约性来自 $\Xi\ne\Xi^{-1}$；不需要援引尚未证明的偶 Artin 模性。

### 2.2 $f$ 的 inner twists 只在 $p$ 上分歧

若 $f^\sigma=f\otimes\chi$ 是一个 inner twist，比较 nebentype 得 $\chi^2=1$。在每个 $q\ne p$，$f$ 及其系数共轭的表示都未分歧；若 $\chi$ 在 $q$ 分歧，则扭后的惯性为非平凡标量，矛盾。因此 $\chi$ 只可能是平凡角色或唯一在 $p$ 分歧的二次角色
$$\chi_{p^*},\qquad p^*=(-1)^{(p-1)/2}p.$$
这也直接是 Studnia 已刊 Lemma 1.3 的一个特例。

令 $H$ 为所有 inner twists 的核的固定域，则
$$
H=\mathbb Q\quad\text{或}\quad H=\mathbb Q(\sqrt{p^*}).
\tag{172.5}
$$
而 $p$ 在 $K$ 未分歧且惰性，所以
$$\boxed{K\not\subset H.}\tag{172.6}$$
从而 $\rho(G_H)$ 包含一个 (172.4) 中的真实反射。

此外，$[H:\mathbb Q]\le2$，故 $\rho(G_H)$ 在 $\rho(G_{\mathbb Q})$ 中的指数至多二。它包含阶至少 $n/2>2$ 的旋转及一个反射。因此在任何剩余特征不整除 $2n$ 的分裂系数域中，它的二维表示仍绝对不可约：旋转的两个特征值不同，反射交换两条特征线。

## 3. KLZ 的三个大像条件逐项成立

为避免符号混淆，本题模曲线水平仍记 $p$，Euler system 的**辅助系数素数**记 $\ell$。

固定一个包含 $f,g$ 系数及 $\rho$ 所有特征值的数域 $L$。令 $F_f$ 为 $f$ 的 inner-twist 固定系数域。Momose–Ribet 的大像定理，以 Studnia 已刊 Proposition 1.5 的准确形式，说明除有限多个系数素理想外，在 $H$ 上的像满足其所需满射。再由该文 Proposition 2.1，若 $\lambda|\ell$ 是好素理想，则
$$
\operatorname{im}\left(G_{H(\mu_{\ell^\infty})}
\longrightarrow
\operatorname{Aut}(T_{f,\lambda})\times\operatorname{Aut}(T_\rho)\right)
=\operatorname{SL}_2(\mathcal O_{F_f,\lambda})
\times\rho(G_H).
\tag{172.7}
$$
所谓好素理想包括 $\ell\nmid30N_fN_g$、$\ell$ 在系数域未分歧以及上述大像满射；除有限多个有理 $\ell$ 后，所有 $\lambda|\ell$ 均好。另排除 $\ell|2n$。

KLZ Hypothesis 11.1.2 的准确三项为：在 $G_{\mathbb Q(\mu_{\ell^\infty})}$ 上，残余张量不可约、存在自由秩一余核元素、存在作用为 $-1$ 的元素。以下在 (172.7) 的更小群中已全部实现。

1. **残余不可约。** 第一个因子的标准二维表示绝对不可约；§2.2 证明第二个因子的约化也绝对不可约。直积的外张量绝对不可约，故在更大的 $G_{\mathbb Q(\mu_{\ell^\infty})}$ 上亦然。
2. **自由秩一余核。** 由 (172.7) 可以同时取
   $$
   U=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
   R\sim\operatorname{diag}(1,-1).
   $$
   因 $2$ 为单位，反射的两条特征线可在整格上分开。$U\otimes R-1$ 的两个块为
   $$U-I=\begin{pmatrix}0&1\\0&0\end{pmatrix},
   \qquad -U-I=\begin{pmatrix}-2&-1\\0&-2\end{pmatrix}.$$
   第一块余核自由秩一，第二块可逆。因此
   $$\boxed{T/(\tau-1)T\simeq\mathcal O_\lambda.}\tag{172.8}$$
   这里不是只计算特征零核的维数；单位上三角项同时排除了整余核挠性。
3. **负单位元。** 在 (172.7) 中取 $(-I,I)$，张量作用即为 $-I$。

对偶表示或 KLZ 所用的等价格规范保留以上三项。在圆分核上，Tate 扭曲平凡；对偶只是将 $U$ 换成另一个有单位非对角项的幺幂块。

这给出了 KLZ 的完整 Hyp(BI)，而不只是一个“大像通常成立”的判断。它也解释了为何 Studnia 论文中一般导子相交时的反例不阻碍这里：那些反例可以让 Artin 的二次域落在 inner-twist 场内；(172.6) 明确排除了这一点。

## 4. 一个同时满足 ordinary 与 distinguished 的辅助素数

### 4.1 在惰性条件下选非零 $a_\ell(f)$

存在无穷多个在 $K$ 惰性的有理素数 $\ell$，使 $a_\ell(f)\ne0$。这里可不用任何关于普通素数密度的附加定理：固定另一个充分好的系数素数 $r$。非 CM 大像在有限扩张 $K$ 上仍包含一个开 $\operatorname{SL}_2$ 子群。任一惰性陪集上的迹函数不可能恒零，因为一个开 $\operatorname{SL}_2$ 子群 Zariski 稠密，而矩阵迹配对非退化。于是可以选一个有限 Galois 商中的非空共轭开集，同时保证 $\varepsilon_K=-1$ 和迹非零模某个 $r^m$。Chebotarev 给无穷多个这样的 $\ell$，其代数整数 $a_\ell(f)$ 必非零。

从中删除所有有限坏素数，包括
$$2,3,5,p,\quad \ell|N_g n,\quad
\ell\text{ 分歧于 }L,\quad
\text{§3 中任何系数素理想非好的有理素数}.$$

### 4.2 至少一个系数素理想普通

选这样的 $\ell>4$。若 $f$ 在每个 $\lambda|\ell$ 都非 ordinary，则 $a_\ell(f)$ 属于所有这些素理想。由于已经要求 $\ell$ 在 $L$ 未分歧，
$$a_\ell(f)\in\ell\mathcal O_L.$$
于是 $a_\ell(f)/\ell$ 是代数整数。Deligne 界在每个复嵌入下给
$$
\left|\sigma\!\left(a_\ell(f)/\ell\right)\right|
\le2/\sqrt\ell<1.
$$
非零代数整数的范数不可能绝对值小于一，所以 $a_\ell(f)=0$，矛盾。因此至少有一个 $\lambda|\ell$ 满足
$$\boxed{a_\ell(f)\in\mathcal O_\lambda^\times.}\tag{172.9}$$
这一步不要求 $\ell$ 在系数域完全分裂，但**确实要求未分歧**；不能将根理想整除直接当成 $\ell\mathcal O_L$ 整除。

### 4.3 权一侧及其余运行假设

因为 $\ell$ 在 $K$ 惰性且不分歧于 $\rho$，(172.4) 给
$$\rho(\operatorname{Frob}_\ell)\text{ 的特征值为 }1,-1.\tag{172.10}$$
故 $g$ 在每个 $\lambda|\ell$ 都 ordinary 且 distinguished。$f$ 在 (172.9) 的 $\lambda$ 普通，且权二、$\ell\ge5$、$\ell\nmid N_f$ 使两个残余局部字符的惯性分别为平凡角色与模 $\ell$ 圆分角色，所以 distinguished。

$f$ 的残余表示由大像绝对不可约，$g$ 的残余表示由 $\ell\nmid2n$ 的有限二面体表示绝对不可约；两者均 non-Eisenstein。权重为 $2,1$，不同时为一；$\ell\nmid N_fN_g$。这逐项核准 KLZ Hypothesis 11.1.1，而非只核普通性。

## 5. 真正中心值与 KLZ imprimitive 值

KLZ §2.7 的经典归一化函数为
$$
L^{\rm imp}(f,g,s)
=L^{(N_fN_g)}(\varepsilon_K,2s-1)
\sum_{m\ge1}a_m(f)a_m(g)m^{-s}.
\tag{172.11}
$$
其中心为 $s=1$；R166 使用的酉中心 $1/2$ 对应这里的 $1$。

在 $q\ne p$，$f$ 未分歧。若 $g$ 在 $q$ 的惯性不变量为零，则两种局部因子都是一；若其维数为一、Frobenius 值为 $\gamma$，则 (172.11) 的局部级数为
$$
\sum_{r\ge0}a_{q^r}(f)\gamma^r q^{-rs}
=\frac1{(1-\alpha_{f,q}\gamma q^{-s})
(1-\beta_{f,q}\gamma q^{-s})},
$$
即 $f\otimes\rho$ 的真实局部因子；两者都未分歧时是标准 Rankin Euler 恒等式。因此两种函数的差别只可能在 $p$。

在 $p$，$f$ 为导子指数二的深度零 supercuspidal，新形式有 $a_{p^r}(f)=0$（$r\ge1$）。$g$ 在 $p$ 也无惯性不变量，所以 (172.11) 的 $p$ 因子为一。真实四维张量则有二维惯性不变量；必须**先张量再取不变量**，不能将各自零维的不变量相乘。记真实局部因子为
$$L_p^{\rm true}(s)=\det(1-p^{-s}\operatorname{Frob}_p\mid
(V_f\otimes\rho)^{I_p})^{-1}.$$
该 Weil–Deligne 表示无 monodromy；$V_f$ 纯权一，$\rho$ 有限阶，故这里的 Frobenius 特征值在每个复嵌入下绝对值为 $\sqrt p$。因此 $L_p^{\rm true}(1)$ 有限且非零，得到
$$
\boxed{L^{\rm imp}(f,g,1)\ne0
\quad\Longleftrightarrow\quad
L\!\left(\tfrac12,\pi_{f,K}\otimes\Xi\right)\ne0.}
\tag{172.12}
$$

### 5.1 辅助 $\ell$ 处也无插值异常零

令 $\alpha_f$ 为普通根、$\beta_f=\ell/\alpha_f$，而 $g$ 的两根为 $\alpha_g,\beta_g=1,-1$。KLZ 的插值因子所需不等式为
$$
\beta_f\ne\alpha_f,\qquad \beta_f\ne\ell\alpha_f,
\qquad \alpha_f\notin\{\alpha_g^{-1},\beta_g^{-1}\},
\qquad \beta_f\notin\{\ell\alpha_g^{-1},\ell\beta_g^{-1}\}.
\tag{172.13}
$$
第一个由 $\lambda$ 赋值为 $0,1$；其余由所有复绝对值 $|\alpha_f|=|\beta_f|=\sqrt\ell$ 与 $|\alpha_g|=|\beta_g|=1$ 得到。KLZ Hyp(NEZ) 同样成立；权重 $2\ne1$ 本已使它自动成立。临界字符取平凡角色，即 $j=0$，恰在 $r'-1\le j\le r-2$ 的区间内。

## 6. 精确调用 KLZ 的一般形式定理

KLZ §11.1 固定
$$T=M_{\mathcal O}(f)^*\otimes M_{\mathcal O}(g)^*.$$
按其 Hypotheses 11.1.1、11.1.2、Proposition 11.7.2 和 Theorem 11.7.3，§3–5 的条件及 (172.12) 给相应 Bloch–Kato Selmer 复形的
$$\widetilde H^2(\mathbb Z[1/S],T;\Delta^{\rm BK})\text{ 有限}.\tag{172.14}$$
这里 $S$ 含 $\ell N_fN_g\infty$。

**原文记号校正。** Theorem 11.7.3 的陈述处将 $M_{\mathcal O}(f\otimes g)$ 漏印了星号；应按 §11.1 对 $T$ 的定义、前一 Proposition 11.7.2 和紧后 Theorem 11.7.4 的证明理解。Studnia 已刊论文 p.5 footnote 2 也指出同一处缺星号。本文不依靠该处孤立的误印选择 Tate 扭曲。

**协变 Tate 规范与一阶的直接证明。** Definition 2.8.1 将 $M_{L_\lambda}(f)^*$ 定义为 $H^1_{\acute et}(Y_1(N_f)_{\overline{\mathbb Q}},\mathbb Q_\ell(1))$ 的对偶 Hecke 商；权二时由 Kummer 同构 $H^1_{\acute et}(X,\mathbb Q_\ell(1))=V_\ell\operatorname{Pic}^0(X)$，它本身就是 $A_f$ 的协变 Tate 因子 $V_{f,\lambda}$，而不是还需再扭一次的普通 $H^1$。§7.6 将 $M_{L_\lambda}(g)^*$ 专门化为权一 Artin 表示；本题 $\rho\simeq\rho^*$，所以无论以该 Artin 实现还是其对偶表述，都有
$$
T\otimes_{\mathcal O_\lambda}L_\lambda
\simeq V_{f,\lambda}\otimes\rho
=:W_{f,\rho,\lambda},
$$
且**没有额外 Tate 扭曲**。紧后 Theorem 11.7.4 的证明亦明确将 $T^\vee(1)$ 识别为椭圆曲线挠点张量 Artin 对偶，和这一协变规范一致。

这里可以直接用一阶 Selmer 群，免去再由 (172.14) 作对偶转换：§5 已证明 $L_\ell(f,g,1)\ne0$，故 Theorem 11.6.6(ii) 给
$$\widetilde H^1(\mathbb Z[1/S],T;\Delta^{(f)})=0.$$
Proposition 11.7.2 对 $i=1$ 的自然映射有有限核余核，所以
$$\widetilde H^1(\mathbb Z[1/S],T;\Delta^{\rm BK})\otimes L_\lambda=0.$$
§11.2 的 Bloch–Kato 局部条件是 simple：它在 $H^0$ 上同构，在 $H^1$ 上给恰当的 Bloch–Kato 子群。因此 Selmer 复形的长正合列把这最后一群直接识别为通常的 $H_f^1(\mathbb Q,T\otimes L_\lambda)$，得到
$$\boxed{H_f^1(\mathbb Q,W_{f,\rho,\lambda})=0.}\tag{172.15}$$
(172.14) 是同一原文定理的二阶结论，保留作来源对照；本题 Mordell–Weil 秩零只需上述一阶直接链。等价地，在杀掉 $\rho$ 的有限扩张上，$A_f$ 的 $\rho$-等型 Kummer Selmer 群有理化为零。这里不声称所有系数素数的整数 Selmer 群都同时消失。

这里用的是 KLZ **一般 $f,g$** 的 Theorem 11.7.3。Studnia Theorem B 本身只对椭圆曲线陈述，本文没有把其展望性一般化备注当成定理。

## 7. 从一个系数因子到真实 $\mathbb Q$-简单商

需要说明为何 (172.15) 不是一个与实际商的 Mordell–Weil 群脱节的形式 Selmer 消失。

**引理 172.2。** 设 $D/\mathbb Q$ 是 $\mathbb Q$-简单阿贝尔簇。若对某个素数 $\ell$ 和有限系数扩张 $L_\lambda$，$V_\ell D\otimes L_\lambda$ 的一个绝对不可约因子 $W$ 满足
$$H_f^1(\mathbb Q,W)=0,$$
则 $D(\mathbb Q)$ 有限。

**证明。** 令 $\mathscr D=\operatorname{End}_{\mathbb Q}^0(D)$，这是除环。Mordell–Weil 向量空间
$$M=D(\mathbb Q)\otimes_\mathbb Z\mathbb Q$$
是有限维左 $\mathscr D$-模；若它非零，则是正秩自由 $\mathscr D$-模。Faltings 的半单性和 Tate 同态定理给
$$
\operatorname{End}_{G_{\mathbb Q}}(V_\ell D\otimes L_\lambda)
=\mathscr D\otimes_\mathbb Q L_\lambda.
$$
扩大 $L_\lambda$ 后，取该代数中的非零幂等元 $e$，投影到一份 $W$。若 $M\ne0$，则自由性给
$$e(M\otimes L_\lambda)\ne0.$$
Kummer 映射是 $\mathscr D$ 等变的注入
$$M\otimes L_\lambda\hookrightarrow
H_f^1(\mathbb Q,V_\ell D\otimes L_\lambda).$$
作用 $e$ 后，其右边为 $H_f^1(\mathbb Q,W)=0$，矛盾。故 $M=0$；Mordell–Weil 有限生成性给有理点群有限。证毕。

这也处理系数域分裂、可能的 Schur 指数和内自扭曲产生的端代数；没有假定实际商本身为椭圆曲线或 $\mathrm{GL}_2$ 型。

**完整有理轨道的中央域拼接。** 对整个实际不连通 Jacobian，令 $\mathcal A$ 为 R166 中实际 Hecke 代数与有限 $N$ 中心所生成的交换半单有理作用代数的像。有限中心的类和与实际下降交换，故确实是 $\mathbb Q$ 上的作用；它与 Hecke 作用交换。一个完整的 Hecke/有限角色配对轨道给 $\mathcal A$ 的原始有理幂等元 $e$，并有
$$F=e\mathcal A\text{ 为数域},\qquad B=e\mathscr J.$$
在与已核四维表示 $W=W_{f,\rho,\lambda}$ 对应的嵌入 $\iota:F\hookrightarrow\overline{\mathbb Q}_\ell$ 处，R166 的实际等变分解给
$$e_\iota\bigl(V_\ell B\otimes\overline{\mathbb Q}_\ell\bigr)
\simeq W^{\oplus m}$$
（扩大有限系数域即可；完整曲线上的 Dirichlet twist 取消按 R166 §5）。因此该中央分量的 $H_f^1$ 为零。另一方面，$M=B(\mathbb Q)\otimes\mathbb Q$ 是 $F$ 向量空间；若 $M\ne0$，则每个 $e_\iota(M\otimes\overline{\mathbb Q}_\ell)$ 都非零。$F$ 等变的 Kummer 注入在此分量上给矛盾，所以 $B(\mathbb Q)$ 有限。

若同一个兼容系统因 Dirichlet twist 重叠出现于数个配对轨道分量，对每个分量采用对应的嵌入作同一论证，再取有限乘积。此论证不需要声称不同系数素数上的全局共轭在同一个 $\ell$ 下共有绝对因子，也不把 Faltings 同态定理用于这种未说明的跨素数拼接。上面的引理 172.2 仍正确，但这里的整个有理轨道直接由其真实中央数域作用处理。

R166 中 $B_\alpha=e(J_\alpha)$ 是这个 $B$ 的实际 $\mathbb Q$ 子簇，故 $B_\alpha(\mathbb Q)$ 也有限；分支间 Hecke 循环论证保证每个 $B_\alpha$ 非零。最优化和同源不改变有理点群的秩，于是得到 (172.3)。对另一个尚未识别为此完整有理投影像的轨道，仍需另有一个满足 (172.2) 的代表。

## 8. 接回指定尖点行，及仍然开放的范围

一旦 (172.2) 对某个实际轨道成立，R169 中属于该轨道的 $\varphi,\varphi^{-1}$ 行就成为真正秩零商的整微分。任何实际分母素数必须使这些行在同一实际尖点、同一圆分剩余嵌入下全为零；任一单位行便排除该分母。

若同时存在 R69 的非零三次 Steinberg 中心值，则旧三色共同理想和这些新尖点型行理想必须一起消失。两种商的因子、导子及非零 $L$ 假设仍分别记录；不能将一方的非消失传给另一方。

因此 R172 将 R166 的一个准确缺口闭合为
$$
\text{所选实际尖点型中心值非零}
\Longrightarrow
\text{所选实际商的有理点群有限}.
$$
剩余主问题仍包括：随实际 $E,K,p$ 变化时至少一个可用中心值的非消失，以及固定实际频率的整行单位性。没有由正根数推出非消失，没有使用 GRH，也没有得到完成 uniformity 的全称排除。

## 9. 已核主来源与版本位置

1. G. Kings, D. Loeffler, S. L. Zerbes, *Rankin–Eisenstein classes and explicit reciprocity laws*, Cambridge J. Math. **5** (2017), 1–122，DOI [10.4310/CJM.2017.v5.n1.a1](https://doi.org/10.4310/CJM.2017.v5.n1.a1)。原刊 §11.1 的 Hypotheses 11.1.1–11.1.2 在 pp.96–97；Theorem 11.7.3 在 p.109，Theorem 11.7.4 及其 Kummer/对偶证明紧随。已逐行核 [作者接受稿](https://wrap.warwick.ac.uk/id/eprint/84343/7/WRAP_klz1b-arxiv_.pdf) 的 §§11.1、11.7（稿页53–54、60–61），并核对原刊索引中的同编号内容。另用 §2.7 的 imprimitive 归一化和 Theorem 2.7.4 插值因子；Definition 2.8.1、§7.6 核准协变 Tate/Artin 规范，Theorem 11.6.6(ii) 与 Proposition 11.7.2 的 $i=1$ 给本文直接使用的一阶消失。
2. E. Studnia, *On obstructions to the Euler system method for Rankin-Selberg convolutions*, Research in Number Theory **12** (2026), article 59，2026-06-01 正式发表，[官方全文](https://link.springer.com/article/10.1007/s40993-026-00718-1)、[官方 PDF](https://link.springer.com/content/pdf/10.1007/s40993-026-00718-1.pdf)。准确使用 Lemma 1.3（p.6）、Proposition 1.5（pp.7–8）、Proposition 2.1（p.9 起）的直积。Proposition 2.4、Corollary 2.8 给同一 Euler-adapted 结论；本文还独立写出了实际反射和整秩一余核。Corollary 2.9 及其证明、随后 Remark 在 pp.17–18，供插值/局部 Euler 对照；p.5 footnote 2 指明 KLZ 的缺星号。没有调用其 Introduction Remarks 中尚以 “can likely” 表述的一般阿贝尔簇推广。
3. K. A. Ribet, *On $l$-adic representations attached to modular forms. II*, Glasgow Math. J. **27** (1985), 185–194，Theorem 3.1，原刊 p.191：[作者保存原刊](https://math.berkeley.edu/~ribet/Articles/rankin.pdf)。大像的准确系数域形式亦见上一项 Proposition 1.5；本文用有限扩张后开 $\mathrm{SL}_2$ 构造惰性非零迹的 Chebotarev 开集。
4. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. **73** (1983), 349–366，§5，Sätze 3–4，p.360：[公开原刊扫描](https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)。用于引理 172.2 的半单性及端同态/Tate 同构；Kummer 注入和除环自由模论证在本文展开。

本文没有把任何预印本的秩零商定理当作已发表输入。
