# 原 Heegner 二阶矩、Darmon 四阶项与完整 Selmer 导出高度

日期：2026-11-13。状态：§1–§3、§5 的比较和限制已证明；
§4 是对已发表标准猜想的精确条件化解释，不是该猜想的证明。
本笔记没有得到原曲线在无穷多个 $p$ 的 Sha 初级有限性。

本文保持 R150、R153、R156、R230、R232 的原输入
$(E,F,p,\ell,L,Q)$，特别保持
$$
 E=389\mathrm a1,\qquad
 Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell],\qquad
 \ell+1=pu,\quad p\nmid ua_\ell(E).
$$
不把原 $\ell$ 换成 Kolyvagin 观测素数。记
$$
 R=\mathbb Z_p[\Gamma],\quad \Gamma=\langle\tau\rangle\simeq C_p,
 \quad \bar R=\mathbb F_p[T]/(T^p),\quad T=\tau-1,
$$
$$
 B=E(L)\otimes\mathbb Z_p,\qquad
 \Delta=\tau+\tau^{-1}-2=\frac{T^2}{1+T}.
$$
除去 R230 的固定有限例外后，负号 Selmer 群是一维，由固定的
$p$ 原始点 $P_-\in E(F)^-$ 的 Kummer 类生成。本文先研究
R232 的**奇数 $a$ 分支**，因此已经有真实格分解
$$
 B=RX\oplus B_0^+,\qquad cX=-X,\quad NX=P_-,\qquad
 Q=\Delta f(\Delta)X,
\tag{1}
$$
以及 $a=1+2v_\Delta(f)$、$\lambda_Q=f(0)\bmod p$。

## 1. 单侧二阶矩对应 Darmon 的四阶张量项

令 $\bar B=B/pB$，定义保留完整轨道的 resolvent
$$
 \mathscr R(Y)=\sum_{j=0}^{p-1}\overline{\tau^{-j}Y}\otimes\tau^j
       \in\bar B\otimes_{\mathbb F_p}\bar R.
\tag{2}
$$
直接换指标可得 $\mathscr R(rY)=r\mathscr R(Y)$，右端 $r$
作用在群环因子。其增广为 $\overline{NY}$，故
$$
 \mathscr R(Q)=\Delta f(\Delta)\mathscr R(X),\qquad
 \mathscr R(X)\bmod T=\bar P_-\ne0.
\tag{3}
$$
这里 $\bar P_-\ne0$ 也在 $\bar B$ 中成立：若一个实际点
$P_-\in E(F)$ 在 $E(L)$ 中可被 $p$ 整除，则除点在任意
$\Gamma$ 元素下的差为 $p$ 挠点；$E(L)[p]=0$ 强迫除点
已在 $F$，与 $P_-$ 在 $E(F)$ 中原始矛盾。

特别，$a=1$ 时有准确的首项
$$
 \mathscr R(Q)=\lambda_Q\bar P_-T^2\pmod{T^3}.
\tag{4}
$$
定义张量积 resolvent
$$
 \Theta_Q=\mathscr R(Q)\odot\mathscr R(Q)^*
       \in\bar B^{\otimes2}\otimes\bar R,
\tag{5}
$$
其中 $*$ 只将第二份的群环变量变为逆元，$\odot$ 将两个
$\bar B$ 因子保留并相乘群环因子。于是
$$
 \boxed{\quad
 \Theta_Q=\lambda_Q^2(\bar P_-\otimes\bar P_-)T^4
                     \pmod{T^5}.\quad}
\tag{6}
$$
$T^*=-T/(1+T)$，所以偶数二阶项的符号为正。
$p\ge7$ 时 $T^4$ 尚未被截断；一个非零向量的张量平方
在域上的张量积中非零。因此 (6) 非零当且仅当 $a=1$。

更一般地，写 $f=\Delta^k v$、$v$ 为单位，则
$a+1=2k+2$，(3) 的准确 $T$ 阶为 $a+1$。
原高度构造给 $a\le(p-3)/2$，所以
$2(a+1)\le p-1$，平方也没有被截断，且
$$
 \operatorname{ord}_T\Theta_Q=2(a+1).
\tag{7}
$$

这与 Darmon [D92] 的原对象直接相接。该文 §2.1 的
$\theta'(E,S)$ 是两个正则化 Heegner resolvent 的张量积，
不是一个单侧 resolvent。对于 $S=\ell$、$\ell$ 惰性，
正则化点分别是 $\alpha_1-\alpha_\ell$ 和
$\alpha_1+\alpha_\ell$。取与本课题相同的完整类群迹，
再乘 $t_0$ 后，底层 Heegner 迹由原构造的挠点消去，
这两个点分别成为 $-Q$、$Q$。
因此在同一群环方向约定下，原 $\theta'$ 的模 $p$ 像是
$-t_0^{-2}\Theta_Q$；改变群环方向只改变可逆因子或 $*$。
这里 $p\nmid t_0$，没有丢弃一个非单位。

所以 O4 奇分支的目标确实是该标准对象的**四阶**领先项
非零；直接援用 $r(E/F)-1=2$ 的二阶 Mazur–Tate 预测
会错过真实的额外消失。

## 2. 第一导出高度在完整 Selmer 群上为零

设
$$
 S=\operatorname{Sel}_p(E/F),\qquad
 S^- =\mathbb F_p s_-,\quad s_-=\operatorname{Kum}(P_-).
\tag{8}
$$
正号部分 $S^+$ 未被假定等于 Mordell–Weil 部分。
R146 已支付所有局部范数满射，且满剩余像、好 $p$、
$p$ 不整除固定分量群等条件满足 [BD94] §2.3。
其 Lemma 2.19 因而给
$S\simeq\operatorname{Sel}_p(E/L)^\Gamma$。

[BD94] §3.5 定义完整 Selmer 过滤
$$
 S^{(1)}=S,\qquad
 S^{(k)}=\{s\in S:\ \exists\widetilde s\in
       \operatorname{Sel}_p(E/L),\ T^{k-1}\widetilde s=s\},
       \quad 2\le k\le p.
\tag{9}
$$
等式中使用上面的实际限制同构。因为
$N=T^{p-1}$ 于 $\bar R$，$S^{(p)}$ 正是从 $L$ 的
Selmer 群取范数所得的子空间。

由 (1)，$s_-=N\operatorname{Kum}(\bar X)$，故
$$
             0\ne s_-\in S^{(p)}\subset S^{(k)}
                    \quad(1\le k\le p).
\tag{10}
$$
$X$ 虽在完备点格中，但其模 $p$ 像是实际
$E(L)/pE(L)$ 元素，足以给出这条 Kummer 等式。

[BD94] Theorem 3.18 构造
$$
 h_k:S^{(k)}\times S^{(k)}\longrightarrow I^k/I^{k+1},
\tag{11}
$$
满足
$$
 h_k(x,y)=(-1)^{k+1}h_k(y,x),\qquad
 \operatorname{rad}(h_k)=S^{(k+1)}.
\tag{12}
$$
这些是**完整 Selmer 群的导出高度**。由其 Galois 等变
构造，以及 $c$ 在 $I^k/I^{k+1}$ 上作用为 $(-1)^k$，有
$$
                    h_k(cx,cy)=(-1)^k h_k(x,y).
\tag{13}
$$
对 $k=1$，(13) 使同号配对为零；(10) 使唯一负号线
与任何正号元素的配对也为零。因此无须假设正号 Sha 消失，
就有
$$
             \boxed{\quad h_1=0\text{ 于整个 }S,\qquad
                              S^{(2)}=S.\quad}
\tag{14}
$$

第二高度 $h_2$ 是交替形式。由 (13)，它的正负混合项
为零；负号一维线本身也为零。因此所有可能非零信息
都位于**完整的** $S^+$ 上，并且
$S^{(3)}=\mathbb F_p s_-\oplus\operatorname{rad}(h_2|_{S^+})$。

## 3. 已知两个点上的非退化不能排除额外 Sha 方向

令 $U\subset S^+$ 是两个已知独立有理点的模 $p$ Kummer
张成空间，删去其在固定秩二子格中可能的有限原始性例外。
即便证明 $h_2|_U$ 非退化，也只能推出
$$
              S^+=U\oplus U^{\perp,h_2}.
\tag{15}
$$
它没有令第二个直和因子消失。有限 Kummer 列仍然是
$$
 0\longrightarrow E(\mathbb Q)/pE(\mathbb Q)
 \longrightarrow S^+
 \longrightarrow\Sha(E/\mathbb Q)[p]\longrightarrow0.
\tag{16}
$$

下面是明确的线性代数模型，说明即便第二高度在整个
正号商上非退化，额外两个方向也完全相容。取 $p\ge11$，
$$
 S^+=\langle e_1,e_2,f_1,f_2\rangle,\qquad
 S^-=\langle z\rangle,
$$
令 $h_1=0$，$h_2(e_1,e_2)=h_2(f_1,f_2)=T^2$，其余
基向量配对由交替性给出或为零。令
$$
 S^{(1)}=S^{(2)}=S,\qquad
 S^{(3)}=\cdots=S^{(p)}=\langle z\rangle,
$$
且后续配对为零。它满足 (10)–(14) 的全部过滤、符号和
根基条件；$U=\langle e_1,e_2\rangle$ 上的高度已非退化，
但 $\langle f_1,f_2\rangle$ 仍可作为 (16) 中未被控制的
两个正号方向。若计算 [BD94] 的修正阶数，则
$$
 \rho'_p=\sum_{k=1}^{p-1}(\dim S^{(k)}-1)=4+4=8,
\tag{17}
$$
而非目标所需的 $4$。
本例只是逻辑模型，不声称存在具有这组实际 Sha 数据的曲线。

## 4. 与 Bertolini–Darmon 标准猜想的准确连接

[BD94] §4.3.2, Assumption 4.16 **先假设**
$\Sha(E/F)[p]=0$ 和 $\operatorname{rank}E(L)>
\operatorname{rank}E(F)$。其 Conjecture 4.20 随后预测，
在非零且未截断的情形，原 Heegner 轨道的模 $p$ 维数为
$$
       \dim\overline{R Q}=p-\frac12\rho'_p.
\tag{18}
$$
另一方面，(1) 中 $RX$ 确实自由，故本课题无条件已有
$$
                   \dim\overline{R Q}=p-(a+1).
\tag{19}
$$
因此，**在该猜想的假设和其结论都成立时**，
$$
                         2(a+1)=\rho'_p.
\tag{20}
$$
这给出一个精确的标准猜想接口。

进一步，若已经知道 $\dim S^+=2$（例如秩恰二并且
$\Sha(E/F)[p]=0$），则 $S$ 维数为三。(14) 给头两层
的贡献 $2+2$；(10) 给后续各层至少一维。因此
$$
 \rho'_p=4
 \Longleftrightarrow S^{(3)}=\mathbb F_p s_-
 \Longleftrightarrow h_2|_{S^+}\text{ 非退化}.
\tag{21}
$$
在这些假设及 Conjecture 4.20 下，(20)–(21) 才给
$a=1\Longleftrightarrow h_2|_{S^+}$ 非退化。

这不是一个无条件的 Sha 判据：用 (18) 来证明
$\Sha(E/F)[p]=0$ 会把 Assumption 4.16 中的同一结论
当作输入。也不能把二维 MW 空间 $U$ 偷换成 $S^+$。
Darmon [D92] Theorem 2.4 的消失下界和 Theorem 2.5
的单向消失结论均没有给出 (18) 的逆向非零性。

## 5. 自由选原 $\ell$ 时，通常 Kummer Frobenius 为什么无信息

这是对原 $\ell$ 的计算，不是对 R232 的观测 $q$。
设 $v$ 为 $F$ 上唯一的 $\ell$ 位，$A$ 为有理
$\ell$-Frobenius 在 $E[p]$ 上的作用。因 $\ell$ 惰性，
$v$-Frobenius 是 $A^2$，剩余域大小为 $q_v=\ell^2$。
有
$$
 \det(1-A^2)=(\ell+1)^2-a_\ell(E)^2
                   \equiv-a_\ell(E)^2\not\equiv0\pmod p.
\tag{22}
$$
同时 $q_v\equiv1\pmod p$。
好约化使表示不分歧。不分歧上同调部分为
$E[p]/(A^2-1)E[p]=0$；惯性部分的 $H^1$ 由
$E[p](-1)^{\mathrm{Fr}_v=1}$ 给出，也因 (22) 为零。
故
$$
                   \boxed{\quad H^1(F_v,E[p])=0.\quad}
\tag{23}
$$
同样，(22) 在每个 $\mathbb Z/p^n$ 层仍为单位，而
$A^2-q_v$ 的模 $p$ 化仍无核，所以
$H^1(F_v,E[p^n])=0$ 对所有 $n\ge1$ 成立。
全部固定点的通常局部 Kummer 类在原 $v$ 因而自动为零。

还能直接看到 Frobenius 共轭类的限制。把有限多个固定点
的 $p^n$-除点塔的平移模记为 $V_n^d$；其表示可写入
$V_n^d\rtimes G_n$。固定线性作用 $B=A^2$ 后，平移
共轭作用为
$$
             (z,B)\longmapsto(z+(1-B)u,B).
\tag{24}
$$
$1-B$ 可逆，故在完整平移半直积中所有 $z$ 都共轭于零。
特别，在满 Kummer 平移像的情况下，给原 $\ell$ 添加
这种通常除点域的 Frobenius 共轭条件，不能区分某个
固定点的非零二阶高度或原 $\lambda_Q$。若平移像是较小
的稳定子模，仍有局部 Kummer 类为零的 (23)，但不在
未经证明时断言较小像中的所有提升也彼此共轭。

这不排除所有 Chebotarev 方法。它指出必须另构造并比较
一个真正携带二阶信息的扩张，或者完整 Selmer 除法数据。
[BD94] 的定义实际要求先在
$\operatorname{Sel}_p(E/L)$ 中解 $T\widetilde s=s$，
再用满足全部局部条件的提升作配对；$L$ 本身随
$\ell$ 改变。没有已证的固定有限域把这些二阶数据化为
一个普通 Kummer Frobenius 值。

作为新的可检查方向，二步非交换扩张的中心确实可能避开
(24)。若 $V=E[p]$ 带 Weil 交替形式 $e$，令
$H(V)=V\times\mathbb F_p(1)$，群律为
$$
 (x,z)(y,t)=(x+y,z+t+\tfrac12e(x,y)).
$$
当 $B\in\mathrm{SL}(V)$ 且 $1-B$ 可逆时，
$H(V)\rtimes\langle B\rangle$ 中的线性平移 $x$ 可被
共轭消去，但留下中心量
$$
       z-\frac12e((1-B)^{-1}x,x).
\tag{25}
$$
证明是用 $u=-(1-B)^{-1}x$ 共轭：新线性项为零，
新中心项为 $z+\tfrac12e(u,Bu)$，即 (25)。
在原 $v$，$\det B=\ell^2\equiv1$，故这是正确的
局部线性代数类型。

(25) 只说明普通 Kummer 的共轭消去并不自动消去二步
中心。尚须构造具有所需像和局部条件的**实际**算术扩张，
把其中心与本课题的完整 Selmer 第二高度或 $\lambda_Q$
作准确比较，并消除 §3 的额外 Sha 方向。没有这三项证明，
不能把一个抽象 Heisenberg 群当作原点的非零证书。

### 5.1 从 $\mathbb Q$ 下降的二步扩张还受平方 Frobenius 限制

对于仅由有理正号点及有理 Poincaré 纤维提升构成、并且
确实给出上述半直积类型的固定扩张，不能任意选取 (25)
中的中心值。原因是 $F$ 上的原 Frobenius 是一个有理
Frobenius 的**平方**。

准确地说，设 $A\in\mathrm{GL}(V)$ 满足
$$
                   \det A=-1,\qquad 1-A^2\text{ 可逆}.
$$
它在 $H(V)$ 的中心作用为 $\det A=-1$。
若 $g=(x,z;A)$，用 $h=(u,v)\in H(V)$ 共轭，则
$$
 x'=x+(1-A)u,
$$
$$
 z'=z+(1-\det A)v+
       \tfrac12\bigl(e(u,x)-e(u,Au)-e(x,Au)\bigr).
\tag{26}
$$
$1-A^2$ 可逆使 $1-A$ 可逆。先唯一选
$u=-(1-A)^{-1}x$ 消去 $x'$，再用
$1-\det A=2$ 可逆选 $v$ 消去 $z'$。所以整个
$H(V)\rtimes A$ coset 在 $H(V)$ 共轭下只有一个类，
每个 $g$ 都共轭于 $(0,0;A)$。于是 $g^2$ 共轭于
$(0,0;A^2)$，其 (25) 中心不变量必为零。

原 $\ell$ 的有理 Frobenius 正满足这些条件：
$\det A=\ell\equiv-1\pmod p$，而 (22) 给第二个条件。
因此一个从 $\mathbb Q$ 下降的这种二步扩张，不能仅凭
在 $F$ 上看到 $\det(A^2)=1$，就宣称 Chebotarev 可选到
非零 (25)。有理 Frobenius 平方只落在中心零的子集。

混入负号点或一个不从 $\mathbb Q$ 下降的环面纤维提升，
会改变这条中心符号计算，故 (26) 不排除一切更高扩张。
但这样的新输入必须另付与原 $\lambda_Q$ 的规范比较；
任意更改环面提升所得的非零数，不能替代固定原点的系数。

### 5.2 自由 Lie 四次层的首个可能观察线不是固定 Tate 商

若进一步考虑生成空间为二维 $V$ 的自由 Lie 代数，前四个
齐次层有自然同构
$$
 L_1=V,\qquad L_2=\det V,\qquad
 L_3=V\otimes\det V,\qquad
 L_4=\operatorname{Sym}^2V\otimes\det V.
\tag{27}
$$
最后一个同构可直接由
$vw\otimes(x\wedge y)\mapsto[v,[w,[x,y]]]$ 给出：
Jacobi 恒等式和 $\wedge^2V$ 一维使其在 $v,w$ 中对称，
三个标准括号构成四次层的基。

当 $A$ 的特征值为 $\lambda,\mu$、$\lambda\mu=-1$，
且 $1-A^2$ 可逆时，前三层都没有 $A$ 不动向量；
第四层的特征值却是
$$
             -\lambda^2,\quad 1,\quad-\mu^2.
\tag{28}
$$
若另排除 $a_\ell^2+4\equiv0\pmod p$，中间的不动线
是一维。写 $D_4=-\operatorname{Sym}^2A$，它的准确投影为
$$
 \Pi_A=\frac{D_4^2+(a_\ell^2+2)D_4+1}{a_\ell^2+4}.
\tag{29}
$$
分子在另外两个特征值上为零，在 $1$ 上为分母。
这里 $a_\ell^2+4\not\equiv0\pmod p$ 仅是这条投影公式的
附加条件。本文没有证明它在 R149–156 同一联合无穷
$(p,\ell)$ 集合中仍留下无穷输入；也没有把固定 $p$ 后的
单独 Chebotarev 选择与原大素因子、$u^2=o(p)$、小高度
同时成立的耦合集合相交。

但是这条线依赖 $A$，并非一个固定的
$\mathrm{GL}_2$-等变 $\det^2$ 商。事实上
$$
 \operatorname{Hom}_{\mathrm{GL}_2}
   (\operatorname{Sym}^2V\otimes\det V,\det^2V)=0.
\tag{30}
$$
直接证明：对角矩阵的权强迫一个候选映射消去
$x^2\otimes(x\wedge y)$、$y^2\otimes(x\wedge y)$；
再用 $y\mapsto y+x$，其平方中的 $2xy$ 项也必须被消去。
因为 $p\ge7$，权可以区分且 $2$ 可逆，映射只能为零。

所以 (29) 给出了比二步中心更高的一个具体候选观察量，
却没有构造它与 (6) 的算术同构。穿孔椭圆曲线的非阿贝尔
Kummer 类首先是某些固定点的路径类；不能只因其四次
Lie 层有 (28)，就认作原环类域 Heegner resolvent 的四次项，
也不能由该路径类的非零性控制 (16) 的全部 Sha 方向。

## 主来源及本课题依赖

- H. Darmon, *A refined conjecture of Mazur–Tate type for Heegner
  points*, Invent. Math. **110** (1992), 123–146，特别 §2.1、
  Conjecture 2.3、Theorems 2.4–2.6。
  [发表版作者存档](https://www.math.mcgill.ca/darmon/pub/Articles/Research/05.Refined-conjecture/pub5.pdf)。
- M. Bertolini and H. Darmon, *Derived heights and generalized
  Mazur–Tate regulators*, Duke Math. J. **76** (1994), 75–111，
  DOI [10.1215/S0012-7094-94-07604-7](https://doi.org/10.1215/S0012-7094-94-07604-7)。
  [作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/11.Derived-heights/paper.pdf)；
  本笔记定理编号按该作者全文：§2.3、Lemma 2.19、
  §3.5、Theorem 3.18、Proposition 3.20、§4.3.2、
  Assumption 4.16、Conjecture 4.20。
- 本仓库 R146、R150、R153、R156：同一原曲线、原扩张、
  完整 Heegner 点、局部条件及 $a$ 的范围。
- 本仓库 R230、R232、R237：负号秩一和 Sha 消去，
  实际 regular 格与规范范数，完整观测群环比较。

两个文献对象的阶数、完整 Selmer 定义和 Sha 假设已经分别
核对；这里没有从“某个高阶系统非零”推出指定二阶节点非零。
