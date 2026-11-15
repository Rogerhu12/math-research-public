# 第一 wild tame 平均的真实二阶 Brandt 式与同步匹配

日期：2026-11-15。**状态：下述原有限 incidence 恒等式、对角 Brandt 部分、原指定 norm fibre 的正主项、实际二位匹配及全 Haar 二阶平均已证明。没有给原固定 CM 基点的严格正下界。局部示例只排除从径向树关系直接推该下界，不是原固定全局向量的反例。**

沿用 R716 及
[第一 wild/Rubin 注](2026-11-15-original-first-wild-rubin-factor-and-central-order.md)
中的同一 rational quaternionic test vector $f$。坏位及原 CM 嵌入固定；好惯性 $p>3$ 处为球向量，Hecke 特征值 $a_p(f)=0$。在原 $p^2$ CM 轨道上写
$$
G_2=\Delta\times\Gamma_1,\qquad
|\Delta|=h=(p+1)/3,\qquad
\Gamma_1=\langle\gamma\rangle\simeq\mathbf F_p.
$$
不作新的 $p$-stabilization。令
$$
A_t=\sum_{\tau\in\Delta}f(x_2(\tau\gamma^t)),
\qquad t\in\mathbf F_p.
\tag{1}
$$
原第一 wild 周期零当且仅当 $A_t$ 全相等。下面所有公式保实际投影碰撞和基点。

## 1. 原有限二阶矩

令 $X$ 为固定 quaternionic level 的有限 Shimura 集，并定义非负整数矩阵
$$
C_{t,x}=
 \#\{\tau\in\Delta:x_2(\tau\gamma^t)=x\}.
\tag{2}
$$
不要求 CM 点投影到 $X$ 单射。把 $f$ 写成其实际值列，则
$$
\boxed{\quad
\sum_t A_t^2=f^{\rm t}C^{\rm t}Cf.
\quad}
\tag{3}
$$
同一个式子还可写成
$$
\sum_t A_t^2
 =\sum_{\delta\in\Delta}\sum_{g\in G_2}
                f(x_2(g))f(x_2(\delta g)).
\tag{4}
$$
每个 $\delta$ 的完整碰撞矩阵是
$$
N_{p,\delta}(x,y)=
 \#\{g\in G_2:x_2(g)=x,\ x_2(\delta g)=y\}.
\tag{5}
$$
因而 $C^{\rm t}C=\sum_\delta N_{p,\delta}$；
$N_{p,\delta}^{\rm t}=N_{p,\delta^{-1}}$。
这些是原轨道上精确有限矩阵，不是自由选择的相关函数。

## 2. 对角部分确由原 Brandt 算子读取

在局部 Bruhat–Tits 树上，惯性非分裂环面作用传递于半径二球面，其大小为 $p(p+1)$。原全局 $\mu_6$ 在投影后给一个自由的三元作用，所以 $G_2$ 是这个球面的三元商。原 $f$ 在该商上确实下降；这一步只用于原 CM 基点 $x_0$。

令 $B_p$ 为带全部边重数的未归一 $p$-邻接 Brandt 算子。半径二不回溯算子为
$$
S_{p,2}=B_p^2-(p+1)I.
$$
因此 (4) 中 $\delta=1$ 的对角部分严格为
$$
\boxed{\quad
D_p:=\sum_{g\in G_2}f(x_2(g))^2
 =\frac13 S_{p,2}(f^2)(x_0).
\quad}
\tag{6}
$$
$B_p$ 的边重数和 (2) 的所有全局碰撞均保留，不能改成互异终点数。

若用标准的 Brandt 谱分解及权二 Ramanujan 界，设
$\Pi_{\rm norm}$ 为固定层上全部 reduced-norm 字符组成的子空间投影，则
$$
D_p=\frac{p(p+1)}3\,
            (\Pi_{\rm norm}f^2)(x_0)+O_{f,X}(p).
\tag{7}
$$
理由是 norm 字符的 $B_p$ 特征值为 $\pm(p+1)$，
而 cuspidal 特征值模不超过 $2\sqrt p$；
固定有限集上的逐点评值常数不依 $p$。
$\Pi_{\rm norm}f^2$ 是相应 norm fibre 的带正确稳定子权重的平均。
它非负；严格正需要 $f$ 在该 fibre 不恒零，
不能由 $f$ 在整个 $X$ 非零推断任意 fibre 正。

原基点关系另外给
$$
\sum_t A_t
 =\frac13 S_{p,2}f(x_0)
 =-\frac{p+1}{3}f(x_0).
\tag{8}
$$
在原未扭 toric 基点 $f(x_0)=0$ 的规范下，
总和为零，因此 $A_t$ 全相等等价于 $A_t$ 全为零。
(8) 本身不控制 (3) 的正性。

## 3. 交叉项不是径向距离四核

对不同 $\tau,\sigma\in\Delta$，
$x_2(\tau\gamma^t)$ 与 $x_2(\sigma\gamma^u)$ 的局部提升位于不同第一分支，树距均为四。可是 (3) 只保 $u=t$ 的 $p$ 个配对，并非这两分支的全部 $p^2$ 个配对。

所以在原树球面上，同步核
$$
\mathbf1_{t=u}
$$
不是距离的函数：同为距离四的两对，可以分别属于和不属于此核。
因此没有一个只由局部径向 Hecke/距离算子给出的**普适**替换，
把 (5) 的实际同步交叉项改成完整距离四和。

这没有证明投影到某个具体有限 $X$ 后不可能出现额外恒等式。
若原固定 $f$ 或实际 $N_{p,\delta}$ 还有特殊全局关系，仍可使用；
但该关系须另外证明。

## 4. 同步匹配中的真实 Fermat 修正

取 $K_p=\mathbf Q_p(\delta)$、$\delta^2=-3$，
用 line $1+x\delta$ 的 slope $x\in\mathbf Z/p^2$ 描述有限第一分支；
无穷分支另用倒数坐标。

主单位 $\gamma_t=1+p\delta t$ 的实际作用为
$$
x\longmapsto\frac{x+pt}{1-3pxt}
 \equiv x+pt(1+3x^2)\pmod{p^2}.
\tag{9}
$$
$p$ 惰性保证 $1+3a^2\ne0\bmod p$ 对每个 $a\in\mathbf F_p$ 成立。

令
$$
\vartheta(x)=\frac{1+x\delta}{1-x\delta}.
$$
tame Teichmüller 截面在分支 $a$ 上为
$\widetilde x(a)=a+p\kappa_p(a)$，由
$\vartheta(\widetilde x(a))^{p+1}=1\bmod p^2$
确定。展开一次，得到准确式
$$
\boxed{\quad
\kappa_p(a)=
 -\frac{1+3a^2}{2\delta}\,
    \frac{\vartheta(a)^{p+1}-1}{p}\pmod p.
\quad}
\tag{10}
$$
右侧属于 $\mathbf F_p$：括号内商的共轭为其负数。
所以原同 $t$ 集合的实际坐标是
$$
\boxed{\quad
x(a,t)=a+p\{\kappa_p(a)+(1+3a^2)t\}\pmod{p^2}.
\quad}
\tag{11}
$$
无穷分支的倒数坐标为 $-3pt$。
最后再取原 $\mu_3$ 商，不删除任何二位信息。

(10)–(11) 正是 R724 的实际 anti-Fermat 条件在树边坐标中的形式。
它不是任选的第二位；仅知道 $a\bmod p$ 或所有端点距离为四，不能恢复它。

## 5. 完整 Haar 平均确为正，但原固定基点不含此平均

在整个 automorphic quotient 上取原 Haar 内积。
选定 (1) 每个点的实际局部代表 $g_{\tau,t}$；它们把根送到所选半径二顶点。
对任意两不同分支且同 $t$ 的代表，
$g_{\sigma,t}^{-1}g_{\tau,t}$ 的 Cartan 距离为四。

原局部球函数 $\varphi_p$ 满足
$$
\varphi_p(0)=1,\quad
\varphi_p(1)=\frac{a_p}{p+1}=0,\quad
p\varphi_p(n+1)+\varphi_p(n-1)=a_p\varphi_p(n).
$$
因此
$$
\varphi_p(2)=-p^{-1},\qquad
\varphi_p(4)=p^{-2}.
\tag{12}
$$
用原纯球向量的矩阵系数，而非独立点值假设，得到
$$
\boxed{\quad
\int\sum_{t\in\mathbf F_p}
   \left|\sum_{\tau\in\Delta}f(xg_{\tau,t})\right|^2dx
 =
 \left(hp+\frac{h(h-1)}p\right)\|f\|_2^2>0.
\quad}
\tag{13}
$$
对角共有 $hp$ 项；异分支同 $t$ 的有序对共有 $h(h-1)p$ 项，每项的全内积是 $p^{-2}\|f\|^2$。

(13) 的积分含原固定 CM 基点所没有的全部紧方向。
它不能改成 (3) 在 $x=x_0$ 的值，
也不能将“存在某个 $x$ 的非零”改成原固定嵌入的非零。
原 $\mu_3$ 商只在 CM 基点使用；(13) 对已选出的代表作全 Haar 平均，不额外假定商关系对所有 $x$ 成立。

## 6. 局部谱值与行和不足以控制同步交叉项

这个限制可在原无限树上直接看见。
取任意非零实函数 $F:\mathbf F_p\to\mathbf R$，满足 $\sum_tF(t)=0$。
在两个不同的 $\Delta$ 分支放 $F(t)$、$-F(t)$，
其余分支放零；在原三元单位轨道内复制相同值。
令根和第一层全部为零。于是：

- 每个第一分支的第二层子和都为零；
- 根和第一层的邻接特征值方程 $B_pf=0$ 成立；
- 半径二对角平方和严格正；
- 每个同步列和 $A_t$ 都严格为零。

这些局部数据还能扩为整棵树上的有界 $0$-本征函数：
在任意已赋值顶点，令其所有 $p$ 个向外子顶点均取
$-\text{该顶点的父值}/p$。
这样每个顶点的邻接和为零，赋值保持有界并保持三元单位对称。

这个例子没有固定有限 Shimura 集，也不是原 automorphic $f$。
它准确说明：仅由原局部特征值 $a_p=0$、允许的 Ramanujan 谱值、分支行和以及径向距离信息，不能推出 (3) 在指定基点严格正。

实际剩余输入是 (5) 的原同步碰撞矩阵与原全局 $f$ 之间的关系，
或等价地 R724 中非实 anti-Fermat 和的严格单边估计。
全 Haar 正性和原 Fourier 自对偶都不能代替该输入。

## 来源

- R716：原 Hecke 角色与固定 quaternionic/theta 族的相同零判据。
- R724：同一个第一 wild 理想角色及实际 anti-Fermat 核。
- 第一 wild/Rubin 注 §6：实际 $G_2=\Delta\times\Gamma_1$ 与 rational tame 平均。
- Burungale–He–Kobayashi–Ota，
  [*Hecke L-values, definite Shimura sets and Mod ℓ non-vanishing*](https://arxiv.org/html/2408.13932v3)，
  §3、§5，原固定 test vector、Shimura 集及 CM 点。本文没有借其固定 $p$ 的深层满射取代第一层同步矩阵。

本注无数值计算，也不提出新的中央零假设。


## 7. 在原轨道上确实可用的 norm-fibre 平均

这里把第2节的对角式扩成一个完整、但量词有限的双点式。

固定 $\alpha\in K^\times$，先排除其分子、分母及原层的有限坏素数。原 CM 基点写为 $x_0=[g_0]$，并在原嵌入下记 $a=\iota(\alpha)\in B^\times(\mathbf Q)$。令
$$
s_\alpha=g_{0,f}^{-1}a_f^{-1}g_{0,f}.
\tag{14}
$$
在本篇好 $p$ 处，$a_p$ 为极大紧子群中的元素；右乘其分量不改变球向量。故在以下公式中，也可将 $s_\alpha$ 的 $p$ 分量改为一。无穷分量因原 quaternionic 权二对应的无穷表示平凡而不产生额外因子。原所有坏位分量则完整保留。

取固定细化层
$$
U_\alpha=U\cap s_\alpha U s_\alpha^{-1},
\qquad
F_\alpha(x)=f(x)f(xs_\alpha).
\tag{15}
$$
这是该细化层有限 Shimura 集上的真实函数。除已经排除的有限素数外，$(U_\alpha,F_\alpha)$ 与 $p$ 无关。没有将坏位矩阵系数改为一。

记 $[\alpha]_p$ 为 $\alpha$ 在
$$
\mathcal O_{K,p}^{\times}/
 \bigl(\mathbf Z_p^\times(1+p^2\mathcal O_{K,p})\mu_6\bigr)
 \simeq G_2
$$
中的类。它属于原 tame 因子 $\Delta$ 当且仅当
$$
\ell_p(\alpha)=0,
\tag{16}
$$
这里 $\ell_p$ 是 R724 的完整 ideal anti-Fermat 角色。条件 (16) 含实际第二位，不能用固定模数同余代替。

若 (16) 成立，令 $\delta=[\alpha]_p$。全局 $a^{-1}$ 的左乘及环面的交换性给出逐点的准确恒等
$$
f(x_2(\delta g))=f(x_2(g)s_\alpha)
\qquad(g\in G_2).
\tag{17}
$$
例如用 $x_2(g)=[\iota(g)_p g_0 a_{p,2}]$ 表示原点，左乘 $a^{-1}$ 在 $p$ 处准确消去 $\iota(\alpha)_p$，在其余有限处留下 (14)。在 $p^2$ 稳定子和全局单位商中的选择不会改变两端。

由于 $s_\alpha$ 与原 CM 单位在相应嵌入下交换，原三元单位商对 (15) 仍成立。故同一个半径二球面式给
$$
\boxed{
\sum_{g\in G_2}f(x_2(g))f(x_2(\delta g))
=
\frac13\{B_{p,\alpha}^2-(p+1)I\}F_\alpha(x_{0,\alpha}).
}
\tag{18}
$$
$x_{0,\alpha}$ 是原基点在细化层中的指定提升；$B_{p,\alpha}$ 是该层真正带重数的 Brandt 邻接算子。这不是对另一个基点求平均，也没有添加 $K_p$ 积分。

因此固定 $\alpha$ 后，真实 norm-fibre 谱分解确实给出
$$
\boxed{
\sum_g f(x_2(g))f(x_2(\delta g))
=
\frac{p(p+1)}3
  (\Pi_{{\rm norm},\alpha}F_\alpha)(x_{0,\alpha})
+O_{\alpha,f,U}(p).
}
\tag{19}
$$
这里的投影是细化层的全部 reduced-norm 字符投影，必须取原指定 fibre。证明与 (7) 相同：norm 字符在半径二算子上的特征值为 $p(p+1)$，其余特征值为 $a_p^2-(p+1)=O(p)$；固定层上的点评值常数不依 $p$。

更一般地，对任何固定层上的固定函数 $F$，实际单点 CM 轨道就有
$$
\frac1{|G_2|}\sum_g F(x_2(g))
=
(\Pi_{\rm norm}F)(x_0)+O_F(p^{-1}).
\tag{20}
$$
所以原 norm-fibre 平均的确能从原环类轨道得到。对同步双点，(18)–(19) 说明何时能把它严格化为这样的单点函数；所需固定 away-$p$ 来源不能省略。

### 7.1 与完整 Haar 矩阵系数的区别

若 $\alpha$ 还满足足够强的固定坏位同余，则 (14) 在所有原坏位固定 $f$。在好位把 $\alpha$ 的有理公因子约去后，其非中心分量只在分裂素数出现。全 Haar 平均可准确写成
$$
\int F_\alpha
=\|f\|_2^2
 \prod_{\ell\mid N(\alpha)}
       \varphi_{\pi_\ell}(d_\ell),
\tag{21}
$$
其中 $d_\ell$ 是真实 Cartan 距离；球系数保持
$$
\varphi_\ell(0)=1,\quad
\varphi_\ell(1)=\frac{a_\ell(f)}{\ell+1},\quad
\ell\varphi_\ell(n+1)+\varphi_\ell(n-1)
 =a_\ell(f)\varphi_\ell(n).
$$
无该坏位同余时，在 (21) 中保留实际坏位矩阵系数。

(21) 不自动等于 (19) 的指定 norm-fibre 值。后者要保完整 $\Pi_{{\rm norm},\alpha}$；特别不能将所有 norm 分量的平均替代原 CM 分量。

### 7.2 这一式子尚不覆盖全部同步交叉和

对一个固定有限集合的 $\alpha$，(19) 的误差可统一；只对其中满足原 (16) 的素数使用对应行。如果不同固定 $\alpha$ 的商不属于 $\mathbf Q^\times\mu_6$，则除有限个 $p$ 外它们在 $G_2$ 中的类不同：类相同会迫一个固定非零虚部代数整数被 $p^2$ 整除。

但在完整 $\Delta$ 中，余下的 $\delta$ 通常必须取随 $p$ 变化的全局代表。此时 (15) 的层、函数和点评值常数也可能随 $p$ 变化，不能仍写成统一 $O(p)$。此外，某个固定非实 $\alpha$ 是否满足 (16)，正是实际 anti-Fermat 条件，不由原固定 ray 决定。

因此 (18) 是原同步矩阵中一个真正可计算的固定来源子族；它没有把整个 $C^{\rm t}C$ 变成径向 Brandt 多项式，也没有证明原 $\sum_t A_t^2>0$。原相消若发生，仍须由其余真实同步项补足 (19) 已确定的这些项。


## 7.3 原指定 norm fibre 的对角主项严格为正

本小节只补齐 (7) 的正系数，不将它升级为 (3) 的正性。沿用同一个原有理向量 $f$，并写其固定 quaternionic 层为 $U=\widehat R^\times$。原模形式 conductor 是
$$
N_0=36\cdot17^2,\qquad v_3(N_0)=2>v_3(D_K)=1.
$$
BHKO 的 Lemma 3.11 因而直接适用，给
$$
\operatorname{nrd}(U)
  =N_{K/\mathbf Q}(\widehat{\mathcal O}_K^\times).
\tag{22}
$$
这里保持原 $2,3,17$ 局部向量；Definition 3.10 的原 universal 向量在所有好惯性素数都相同。固定有理归一只乘一个非零常数，不改变本小节结论。

令 $c$ 为 reduced-norm 映射。因为 $K=\mathbf Q(\omega)$ 类数一，任意有限 $K$-idele 可写成 $\alpha u$，其中 $\alpha\in K^\times$、$u\in\widehat{\mathcal O}_K^\times$。于是
$$
N(\widehat K^\times)
 \subset\mathbf Q_{>0}^{\times}\operatorname{nrd}(U).
\tag{23}
$$
因此 BHKO 的 $X_U^+$ 是**一个** norm fibre，而非若干未知 fibre 的并。原 $x_0$ 在这个分量：其固定 CM 矩阵 $\varsigma^{(0)}$ 的 reduced norm 属于 $\mathbf Q_{>0}^\times N(\widehat K^\times)$，如该文 Proposition 5.8 证明所明示；在本曲线的 $2,3,17$ 均不分裂规范中，好惯性处的零深矩阵还具有行列式一。故
$$
X_U^+=c^{-1}(c(x_0)).
\tag{24}
$$

原 $\psi_{17}$ 的根号为 $+1$。BHKO Proposition 5.12 对这个原 universal 向量给
$$
f|_{X_U^+}\ne0,\qquad f|_{X_U^-}=0.
\tag{25}
$$
这是固定向量的分量定理，不是关于随 $p$ 变化的第一层周期的非消失断言。它也可由固定辅助惯性素数的深偶层非零推出：primitive 角色消去 stabilization 的旧层项，而类数一及偶深度保持 (24) 的原 norm fibre。无需将深度阈值对变化的 $p$ 一致化。

用本篇 (7) 的正确稳定子权重，设
$$
c_f=
\frac{\displaystyle\sum_{x\in X_U^+}w_x^{-1}f(x)^2}
     {\displaystyle\sum_{x\in X_U^+}w_x^{-1}},
\qquad
w_x=[B^\times\cap xUx^{-1}:\mathbf Z^\times].
\tag{26}
$$
$f$ 是实有理向量，所有 $w_x^{-1}>0$；由 (25) 得
$$
\boxed{c_f=(\Pi_{\rm norm}f^2)(x_0)>0.}
\tag{27}
$$
所以对所有充分大的原好惯性 $p$，
$$
\boxed{
D_p=\frac{c_f}{3}p(p+1)+O_{f,U}(p)>0.
}
\tag{28}
$$
这里的阈值和误差常数固定，不依第一 wild 角色或其第二位。

保留实际异分支同步和
$$
E_p=\sum_{\substack{\delta\in\Delta\\\delta\ne1}}
       \sum_{g\in G_2}f(x_2(g))f(x_2(\delta g)).
$$
则原第一层全零仍准确等价于
$$
D_p+E_p=0.
\tag{29}
$$
在该情形，(28) 只迫
$$
E_p=-\frac{c_f}{3}p(p+1)+O_{f,U}(p).
\tag{30}
$$
它没有排除这个真实、随 $p$ 变化的同步补偿。§7.2 的固定 $\alpha$ 子族仍不足以估计全部 $E_p$；§5 的全 Haar 平均亦不能替换它。

本小节的外部输入只用 BHKO 同一
[原文](https://arxiv.org/html/2408.13932v3)
的 Lemma 3.11、Definition 3.10、Proposition 5.8 中的原 CM 基点规范以及 Proposition 5.12；类数一到单一 norm fibre、(26)–(30) 是上面的完整推导。没有新增计算或中央零条件。


## 7.4 固定代数同步项的指定平均与原局部系数

在本篇原向量上，§7.1 的 norm-fibre 与全内积之间还可准确比较；这一步不是对任意局部测试向量的断言。

$s_\alpha$ 与原共轭嵌入的 $\widehat{\mathcal O}_K^\times$ 交换。故
$$
g_{0,f}^{-1}\iota(\widehat{\mathcal O}_K^\times)g_{0,f}
 \subset U_\alpha\subset U.
$$
取 reduced norm 并用 (22)，上下包含迫
$$
\operatorname{nrd}(U_\alpha)
 =\operatorname{nrd}(U)
 =N(\widehat{\mathcal O}_K^\times).
\tag{31}
$$
所以细化层的原 plus norm fibre 正是 $X_U^+$ 的完整逆像，没有新增 norm 分量。又 $\operatorname{nrd}(s_\alpha)$ 是 $K$-范数，右移保持这个分量。由 (25)，$f$、$R(s_\alpha)f$ 及 $F_\alpha$ 全部支撑于同一个原 plus fibre。

在共同 adelic quotient 上用同一 Haar 测度；将它推至两个有限层时，自动带各自正确的稳定子权重。原 plus fibre 的 Haar 质量不随层细化改变。因此
$$
\boxed{
(\Pi_{{\rm norm},\alpha}F_\alpha)(x_{0,\alpha})
 =c_f\,\mathcal K_f(\alpha),\qquad
\mathcal K_f(\alpha)=
 \frac{\langle f,R(s_\alpha)f\rangle}{\langle f,f\rangle}.
}
\tag{32}
$$
这付清的是原指定 fibre，而不是把一个任意 CM 点换成 Haar 随机点。代回 (19)，对固定 $\alpha$ 且满足完整 $\ell_p(\alpha)=0$ 的 $p$，
$$
\sum_g f(x_2(g))f(x_2([\alpha]_p g))
 =
 \frac{c_f}{3}p(p+1)\mathcal K_f(\alpha)
 +O_{\alpha,f,U}(p).
\tag{33}
$$

本曲线的原坏素数 $2,3,17$ 全不分裂，且在 conductor 中都属于 BHKO Definition 3.4(b) 的部分。因此原 quaternionic test vector 在这些地点**由定义**固定于相应共轭 $K_\ell^\times$；局部矩阵系数确为一，并非把原 $\psi_{17}$ 的坏位角色任意删掉。好惯性地点的 $K_\ell^\times$ 是中心与 $\mathcal O_{K,\ell}^\times$ 的乘积，亦固定球向量。无穷表示平凡。于是只有分裂素数有非平凡因子。

对 $\ell=\mathfrak l\bar{\mathfrak l}$，置
$$
e_\ell(\alpha)=
 |v_{\mathfrak l}(\alpha)-v_{\bar{\mathfrak l}}(\alpha)|.
$$
原纯张量矩阵系数给
$$
\boxed{
\mathcal K_f(\alpha)=
 \prod_{\ell\ {\rm split}}\Phi_\ell(e_\ell(\alpha)),
}
\tag{34}
$$
其中仅有限因子不为一，而且
$$
\Phi_\ell(0)=1,\qquad
\Phi_\ell(1)=\frac{a_\ell(E_{17})}{\ell+1},\qquad
\ell\Phi_\ell(e+1)+\Phi_\ell(e-1)
 =a_\ell(E_{17})\Phi_\ell(e)\quad(e\ge1).
\tag{35}
$$
(34) 的 $a_\ell$ 是原曲线的真实 Hecke 特征值，包含其固定 $17$-local 算术；不能换成 $E_1$ 的特征值。$\alpha$ 或其逆给相同 Cartan 距离，故 (14) 的逆号不改变 (34)。

最后，取固定 ramified 元素 $\delta=\sqrt{-3}$。其类 $d_0=[\delta]_p$ 对 $p>3$ 是 $\Delta$ 中的非平凡二阶元，且 $\ell_p(\delta)=0$。因 $\delta$ 只有 ramified/nonsplit 非中心分量，上述原局部不变性直接给
$$
R(s_\delta)f=f.
$$
所以这一个同步项不只是有主项，而是全量准确等于对角项：
$$
\boxed{
f(x_2(d_0g))=f(x_2(g)),\qquad
\sum_g f(x_2(g))f(x_2(d_0g))=D_p.
}
\tag{36}
$$
这也是原 $\Delta^{\rm alg}$ 的二阶作用，和 BHKO (5.5) 一致。因此原全第一层零会迫更精确的剩余补偿
$$
\boxed{
\sum_{\delta'\in\Delta\setminus\{1,d_0\}}
 \sum_g f(x_2(g))f(x_2(\delta' g))
 =-2D_p.
}
\tag{37}
$$
本节没有估计 (37) 的左端。对随 $p$ 增长的其余全局代表，细化层误差仍不能从 (33) 冒作统一常数；固定 $\alpha$ 的可读性和全部同步和的控制依然不同。
