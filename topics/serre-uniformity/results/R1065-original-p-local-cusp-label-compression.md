# R1065：原完整非分裂曲线的模 p 圆盘标签与 regular 全局候选压缩

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对每个 $p>37$，R1062/R1064 的完整原曲线
$X=X_{\rm ns}^+(p)$ 的规范 cuspidal Kummer 标签，在每个原
$\mathbf Q_p$ 模 $p$ 圆盘上恒定。其全部实际局部像至多有
$p\,n(p)\le p(p+13)/12$ 个元素。这里覆盖全部 $p\bmod12$，
不限制为旧的 $j=0$ CM 分支或 $p\equiv11\bmod12$。

对 regular $p$，forced 模块的全局标签向 $p$ 处的核恰有
$p^{\kappa_p}$ 个元素，其中 $\kappa_p$ 完整保留 $2,3$ 的角色贡献。
因此 R1064 中真正可能有 $\mathbf Q_p$ 点的全局 twists 数至多为
$p\,n(p)\,p^{\kappa_p}$，不再把全部 ambient 全局标签逐个当候选。
这仍不是非 CM 点排除，也不声称各局部标签均已确定为 CM 标签。
本文全为纸面证明，无数学程序执行。

## 1. 固定原对象与主张

沿用 R1062/R1064：
$$
m=(p-1)/2,\qquad F=\mathbf Q(\zeta_p)^+,\qquad
G=\operatorname{Gal}(F/\mathbf Q),\qquad
K=F_{\mathfrak p}=\mathbf Q_p(\zeta_p)^+.
\tag{1065.1}
$$
$\mathfrak p$ 是唯一 $p$ 位，$e(K/\mathbf Q_p)=m$。
$V=U_p/pU$ 是原 cuspidal $p$-torsion 模块，$V^G=0$；
取原全部 $m$ 个 cusps 的整参数后，
$$
\Phi_x([u])=
 \left[\frac{u(x)^m}{A(u)}\right],\qquad
 A(u)=\prod_{c\in\Sigma}\operatorname{lc}_c(u).
\tag{1065.2}
$$
R1062 证明常数缩放、参数变化和 $p$ 次幂全部抵消，
所以它是实际 $G$-equivariant 线性标签。
对 $x\in X(\mathbf Q_p)$，(1065.2) 取值于
$K^\times/K^{\times p}$；cusps 的定义域在 $p$ 处次数为 $m>1$，
故 $X(\mathbf Q_p)$ 本身没有 cusp。

写 $p=12k+i$，$i\in\{1,5,7,11\}$，置
$$
n(p)=
\begin{cases}
k&i=1,\\
k+1&i=5,7,\\
k+2&i=11.
\end{cases}
\tag{1065.3}
$$
这是几何 supersingular $j$-invariants 的数目。
下面证明存在规范有限映射
$$
\bar\Phi_p:\mathcal M^{\rm sm}(\mathbf F_p)
 \longrightarrow
 \operatorname{Hom}_{\mathbf F_p[G]}
       (V,K^\times/K^{\times p})
\tag{1065.4}
$$
使 $\Phi_x=\bar\Phi_p(\bar x)$；$\mathcal M/\mathbf Z_p$
是原曲线的最小正则模型。每个 $\bar x$ 都可 Hensel 提升，
所以 (1065.4) 的像准确等于 $\Phi_p(X(\mathbf Q_p))$，
而不只是包含它的形式集合。

## 2. 全部四种 p mod 12 的真实模型与 cusp 位置

使用已发表 Edixhoven–Parent [EP]：
Theorem 3.4（印刷 1038 页，PDF 第 21 页）、
Figure 6（1039 页，PDF 第 22 页）、
Corollary 3.2（1042 页，PDF 第 25 页）及其证明
（1043–1044 页，PDF 第 26–27 页）。
这里 PDF 页从 0 起编号；读者界面通常显示页码再加一。

在原最小 normal-crossing 正则模型上，中央 Igusa $j$-线
$A$ 的重数为 $m$。每个普通 supersingular $j$ 的支链有一个
重数 $p+1$ 的 Drinfeld $\mathbf P^1$、一个重数 $(p+1)/2$
的 $\mathbf P^1$，及一个唯一的重数 $1$ 外端 $F_s$。
特殊自同构点的处理如下，均属于同一个原模型：

| $p\bmod12$ | $j=0$ | $j=1728$ | 保留下来的重数 $1$ 外端数 |
| --- | --- | --- | --- |
| $1$ | ordinary 的额外链，重数 $(p-1)/3,(p-1)/6$ | ordinary | $k$ |
| $5$ | supersingular 链，重数 $(p+1)/3,(p+1)/6,1$ | ordinary | $k+1$ |
| $7$ | 同第一行的 ordinary 额外链 | supersingular 特殊分量本身重数 $1$ | $k+1$ |
| $11$ | 同第二行的 supersingular 链 | 同第三行的重数 $1$ 分量 | $k+2$ |

[EP, Corollary 3.2] 的收缩只留下这些 $F_s$；
中央 $A$、上述全部其它分量组成的连通树收缩到一个共同点 $z$。
Figure 6 中每个 $F_s$ 只在一个点接这棵树。
故收缩在该点之外是同构，且
$$
(\mathcal M_{\overline{\mathbf F}_p})^{\rm sm}
 =\coprod_{s\ {\rm supersingular}}\mathbf A^1_s.
\tag{1065.5}
$$
这里没有从一般“rational normalization”偷推单分支：
只删一个点，是原外端与被缩树的实际接合方式。
共同点可能高度奇异，各 $F_s$ 在那里也可能不再光滑；
(1065.5) 不把该点包括进来。

为核 cusp 闭包，先在收缩前保留原 $j$-态射。
[EP, §2, Theorem 2.1] 从 Katz–Mazur compactification 出发，
经基变换、blow-ups、Galois 商及解消得到所用模型。
忘掉 level 的 $j$-映射在 compactification 上为到
$\mathbf P^1_{\mathbf Z_p}$ 的态射；这些操作均保留此态射：
blow-ups/解消作复合，商上因 $j$ 不变而下降。
每个 $F_s$ 来自有限 supersingular $j=s$ 上的支链，
所以原 $j$ 在 $F_s$ 上恒为有限的 $s$。
收缩在 $\mathcal M\setminus\{z\}$ 是同构，故这个开集仍有原
$j$-态射，special fiber 的值全有限。cusp 的 $j$ 值为 $\infty$，
其闭包不能穿过该开集。因此
$$
\overline\Sigma\cap\mathcal M_{\overline{\mathbf F}_p}
 \subset\{z\}.
\tag{1065.6}
$$
这一步使用实际模型，不由 $j(x)\in\mathbf Z_p$
直接猜一个未分歧 formal chart。

原曲线定义在 $\mathbf Q_p$，且 $p>37$ 时 genus 大于一。
最小正则模型的唯一性给上述模型的未分歧下降；
也可从 $\mathbf Z_p$ 上最小正则模型作未分歧基变换来识别它。
Frobenius 按原 supersingular $j$ 运输这些外端。
若一个分量被 Frobenius 固定，其 normalization 是
$\mathbf P^1$ 的 $\mathbf F_p$-形式，且唯一被删的点被固定，
所以它是带一个 $\mathbf F_p$ 点的 genus-zero 曲线，
即 $\mathbf P^1_{\mathbf F_p}$。其余开集为 $\mathbf A^1_{\mathbf F_p}$，
恰有 $p$ 个点。不固定的分量在共同点以外没有 $\mathbf F_p$ 点。
记 $n_{\mathbf Q_p}(p)$ 为属于 $\mathbf F_p$ 的 supersingular $j$ 数目。
上述实际 Frobenius 运输还给准确计数
$\#\mathcal M^{\rm sm}(\mathbf F_p)=p\,n_{\mathbf Q_p}(p)$；从而
$
\#\mathcal M^{\rm sm}(\mathbf F_p)\le p\,n(p)
 \le\frac{p(p+13)}{12}.
\tag{1065.7}
$$

## 3. 每个 Qp 点确实落在 smooth 圆盘

Properness 使每个 $x\in X(\mathbf Q_p)$ 延伸为
$\operatorname{Spec}\mathbf Z_p\to\mathcal M$。
设其闭点为 $z_x$，令 $R_x=\mathcal O_{\mathcal M,z_x}$。
这是 dimension-two regular local ring。
若 special fiber 在 $z_x$ 不光滑，因为 residue field 是完美的
$\mathbf F_p$，正则参数判据给 $p\in\mathfrak m_x^2$。
局部 section 把 $\mathfrak m_x$ 送到 $p\mathbf Z_p$，
就会把 $p$ 送入 $p^2\mathbf Z_p$，矛盾。
所以 $z_x\in\mathcal M^{\rm sm}(\mathbf F_p)$。

反之 smoothness 与 completeness 给每个
$z_0\in\mathcal M^{\rm sm}(\mathbf F_p)$ 一个 $\mathbf Z_p$ lift。
选择一个该 lift 作原点，可写完成局部环
$$
\widehat{\mathcal O}_{\mathcal M,z_0}=\mathbf Z_p[[t]].
\tag{1065.8}
$$
同一原 $\mathbf Q_p$ 圆盘内的点满足 $t(x)\in p\mathbf Z_p$。
到 $\mathcal O_K$ 的基变换仍 smooth，完成环恰为
$\mathcal O_K[[t]]$。不能用任意 $K$ 点的 $t\in\mathfrak p_K$
替代这里的真实 $t\in p\mathbf Z_p$。

## 4. 同一原模 p 圆盘内全部 Kummer 标签恒定

取 $u\in U_p$ 的实际有理函数代表。
由 (1065.6)，这个完成邻域没有任何水平 cusp divisor；
$\operatorname{div}(u)$ 的水平部分又只在 cusps 上。
故在 $R=\mathcal O_K[[t]]$ 中其 Weil divisor 只支撑在
唯一 vertical height-one prime $(\pi)$，其中 $\pi$ 是 $K$ 的
uniformizer。$R$ 是正则 factorial local ring，于是
$$
u=\pi^a v(t),\qquad a\in\mathbf Z,\quad v(t)\in R^\times.
\tag{1065.9}
$$
具体地，去掉 $(\pi)$ 上的 order 后，所得函数在每个 height-one
prime 上 order 都为零。Krull-domain 交集描述使它和它的倒数均在
$R$ 中，故为 unit。这也支付了负 order 及 completion 后的所有分支。

若 $x,y$ 在同一原模 $p$ 圆盘，
$t(x)-t(y)\in p\mathbf Z_p$，(1065.9) 给
$$
\frac{u(x)}{u(y)}\in1+p\mathcal O_K.
\tag{1065.10}
$$
令 $U_i=1+\pi^i\mathcal O_K$。
因 $e(K/\mathbf Q_p)=m<p-1$，$p$-adic log/exp 在 $U_1$
与 $\pi\mathcal O_K$ 上互逆，所以
$$
U_1^p=U_{m+1},\qquad 1+p\mathcal O_K=U_m.
\tag{1065.11}
$$
取 $\pi=(1-\zeta_p)(1-\zeta_p^{-1})$ 乘一个 unit 也可。
$\sigma_a$ 在 $\pi\mathcal O_K/\pi^2\mathcal O_K$ 上的作用为
$\omega(a)^2$，故在
$$
U_m/U_{m+1}\simeq\pi^m\mathcal O_K/\pi^{m+1}\mathcal O_K
$$
上为 $\omega(a)^{2m}=1$。
因此 $U_m$ 在 $K^\times/K^{\times p}$ 中的像是 trivial
$G$ 子模。

(1065.2) 中 $A(u)$ 在 $x,y$ 之比里准确抵消；
(1065.10) 又对每个 $u$ 成立，所以
$\Phi_x-\Phi_y$ 的全部值都在这个 trivial 子模中。
该差仍是实际 $G$-equivariant $\mathbf F_p$-linear map。
$p\nmid|G|$ 且 $V^G=0$，Maschke 分解给
$\operatorname{Hom}_G(V,\mathbf F_p)=0$。
于是
$$
\boxed{\Phi_x=\Phi_y
\quad\text{当 }\bar x=\bar y
       \text{ 在原 }\mathcal M^{\rm sm}(\mathbf F_p)\text{ 中}.}
\tag{1065.12}
$$
这证明 (1065.4)，并结合 (1065.7) 给
$$
\boxed{\#\Phi_p(X(\mathbf Q_p))\le p\,n(p).}
\tag{1065.13}
$$
此结论完全不需要 regularity，且作用于完整 $V$，不只是 forced 子模块。

## 5. Regular p 的 class-group 与 S-unit 精确维数

现在假设 $p$ regular，含义与 R1062 相同：
$B_2,B_4,\ldots,B_{p-3}$ 的分子均不被 $p$ 整除。
Kummer criterion 把此条件等价为
$p\nmid h(\mathbf Q(\zeta_p))$；
本文实际核读的已发表 primary 陈述是 [Y, Theorem 1]，
印刷第31页（PDF第1页，从0起）。

这里不把 real class-group 项静默删除。
对 $F\subset F'=\mathbf Q(\zeta_p)$，
extension 与 norm 在 $\operatorname{Cl}(F)[p]$ 上的复合为乘 $2$。
由于 $p>2$，extension 在此群上单射。
所以
$$
\operatorname{Cl}(F)[p]=0,\qquad
\operatorname{Cl}(\mathcal O_{F,S})[p]=0,
\quad S=\{\mathfrak q:\mathfrak q\mid6p\}.
\tag{1065.14}
$$
后一 class group 是前者的 quotient，故阶仍 prime to $p$。
这不是 Vandiver 假设；它只在已经假定 regular 的此节使用。

记 $E=\mathcal O_F^\times,\ E_S=\mathcal O_{F,S}^\times$。
完整 valuation exact sequence 为
$$
0\to E\to E_S\to\bigoplus_{\mathfrak q\in S}\mathbf Z[\mathfrak q]
 \to\operatorname{Cl}(F)\to\operatorname{Cl}(\mathcal O_{F,S})\to0.
\tag{1065.15}
$$
张量 $\mathbf Z_p$（它在 $\mathbf Z$ 上 flat）并用 (1065.14)，得
$$
0\to E\otimes\mathbf Z_p\to E_S\otimes\mathbf Z_p
 \to\bigoplus_{\mathfrak q\in S}\mathbf Z_p[\mathfrak q]\to0.
\tag{1065.16}
$$
右侧为 free $\mathbf Z_p$ 模；按角色分解后仍 free，
所以再模 $p$ 不引入 Tor 项。

Dirichlet 的实对数嵌入给
$E\otimes\mathbf R\simeq\mathbf R[G]_0$ 的实表示；
$\mathbf Z_p[G]$ 的每个 Teichmüller character idempotent 都整，
故每个非 trivial 偶角色 $\chi$ 的 $E\otimes\mathbf Z_p$ 部分
为 rank-one free $\mathbf Z_p$ 模。
$p$ 位的 prime module 为 trivial；
$\ell=2,3$ 上的 prime module 为
$\mathbf Z_p[G/\langle\sigma_\ell\rangle]$，
其 $\chi$ 重数为 $1$ 当且仅当 $\chi(\ell)=1$。
R1062 的 exact sequence 再用 (1065.14)，给
$$
\dim_{\mathbf F_p}F(S,p)_\chi
 =1+\mathbf 1_{\chi(2)=1}+\mathbf 1_{\chi(3)=1}
\quad(\chi\ne1).
\tag{1065.17}
$$
R1062 §9 的真实 circular-unit log 计算证明：
在 regular 情形，每个 $\chi\ne1$ 的原 global-unit 部分
向唯一一维的 $(K^\times/K^{\times p})_\chi$ 非零，故同构。
因此 (1065.17) 的完整 localization 的秩为 $1$，核维数准确为
$$
\mathbf 1_{\chi(2)=1}+\mathbf 1_{\chi(3)=1}.
\tag{1065.18}
$$
没有把 $2,3$ 删去，也没有把 $u_a=\eta_a/a$ 当 global unit。

## 6. 原 forced twists 的实际候选数

令
$$
r=\lfloor p/4\rfloor-1,\qquad
W_{\rm forced}=\bigoplus_{j=1}^r V_{\chi_j},
\qquad\chi_j=\omega^{-2j}.
$$
R1062 的每个 $V_{\chi_j}$ 恰为一维。
令
$$
\mathscr L_W=\operatorname{Hom}_G(W_{\rm forced},F(S,p)),\qquad
\kappa_p=\sum_{j=1}^r
 \left(\mathbf1_{2^{2j}\equiv1\bmod p}
       +\mathbf1_{3^{2j}\equiv1\bmod p}\right).
\tag{1065.19}
$$
由 (1065.18)，
$$
\mathscr L_W\longrightarrow
 \operatorname{Hom}_G(W_{\rm forced},K^\times/K^{\times p})
$$
满射，且每个 fiber 恰有 $p^{\kappa_p}$ 个元素。
R1064 已把这些标签变为实际 $\mathbf Q$-torsor twists。
一个 twist $Y_\phi$ 有 $\mathbf Q_p$ 点，当且仅当存在
$x_p\in X(\mathbf Q_p)$ 满足 $\phi_{\mathfrak p}=\Phi_{x_p}|_W$：
这是同一个实际 torsor 的 fiber Kummer class 为零的充要条件。
所以
$$
\boxed{
 \#\{\phi\in\mathscr L_W:Y_\phi(\mathbf Q_p)\ne\varnothing\}
 \le p\,n(p)\,p^{\kappa_p}.}
\tag{1065.20}
$$
该集合是明确的有限集合：对每个原 smooth $\mathbf F_p$ 点选任意
Hensel lift，算一次 (1065.2)，再取完整 global localization fiber；
(1065.12) 保证不依赖 lift。

若 $\delta_\ell$ 是 $\ell$ 在
$G=\mathbf F_p^\times/\{\pm1\}$ 中的阶，则准确有
$$
\kappa_p=\left\lfloor\frac r{\delta_2}\right\rfloor+
          \left\lfloor\frac r{\delta_3}\right\rfloor.
\tag{1065.21}
$$
由 $\ell^{\delta_\ell}\equiv\pm1\bmod p$，
有 $\ell^{\delta_\ell}\ge p-1$，从而
$\kappa_p\le r\log6/\log(p-1)$。
特别若 $m=(p-1)/2$ 为奇素数，则 $2,3\not\equiv\pm1\bmod p$，
故 $\delta_2=\delta_3=m>r$、$\kappa_p=0$：
对 regular 的这类 $p$，至多 $p\,n(p)$ 个实际 global twists
能够有 $\mathbf Q_p$ 点。

此计数不声称有无限多个 regular 的该类素数；
也不把它外推到不满足 regular 的素数。
对一般 $p$，(1065.13) 仍无条件成立，但全局 lift fiber
必须继续保留 R1062 的 class-group 与完整 unit-localization 核。

## 7. 和 R1062 满射边界的准确关系

R1062 §9 说每个允许的单独 $p$-local 标签均来自某个 ambient
全局标签，所以那个比较不排除任何 $x_p$。
本篇取的是相反方向：全局 twists 要有 $p$ 点，
其标签必须落入 (1065.4) 的**实际点像**。
后者至多 $p\,n(p)$，而允许的整个 local vector space
在 forced 部分有 $p^r$ 个元素。
两个结论没有冲突，且不把“local class 可提升”当作 twist 一定有点。

本篇尚未：
- 算出所有 $\bar\Phi_p(\bar x)$ 的 circular-unit 坐标；
- 证明这些实际标签只来自 CM 点；
- 证明它们与 R1064 辅助 $\ell$ 处同一标签条件不相容；
- 排除 irregular $p$ 的全部 global class-group 自由度。

后继必须对这些同一实际标签施加辅助条件或其它全局约束；
仅本篇有限候选数不完成 O0，更不完成 Serre uniformity。

## 8. 核读来源

- [EP] B. Edixhoven and P. Parent,
  *Regular models of modular curves in prime level over*
  $\mathbf Z_p^{\rm ur}$, Doc. Math. **29** (2024), 1017–1058,
  [DOI](https://doi.org/10.4171/DM/974)，
  [已刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。
  使用 Theorem 2.1、Theorem 3.4、Figure 6、
  Corollary 3.2、Figure 7 及收缩证明；§2 明确补齐
  $\mathbf F_p$ 下降、smooth locus 与 cusp 闭包接口。
- [Y] R. I. Yager,
  *A Kummer criterion for imaginary quadratic fields*,
  Compositio Math. **47** (1982), 31–42，
  [已刊全文](https://www.numdam.org/article/CM_1982__47_1_31_0.pdf)。
  仅用其印刷第31页 Theorem 1 所准确陈述的经典 Kummer criterion，
  不用该文关于 imaginary quadratic fields 的后继定理。
- R1062：原模块、无基点 normalization、全部 $S$-class group、
  actual $G$ 作用及 regular circular-unit local isomorphism。
- R1064：原连通 $\mathbf Q$-cover、twist 分类及好素同标签条件。

2026 年 Love–Studnia–Vonk 预印本的模型描述提供了检索线索；
本篇没有引用其尚未在仓库重证的定理。

本篇由global_route推导，root实读所引已刊模型、四行图和最终收缩证明，逐项核cusp闭包、section必落smooth locus、完成环的unit分解及$U_m$角色；另独核全部class-group、$2,3$自由度和实际twist点像计数。原模型是已知输入，本篇新增的是其规范Kummer标签和完整global候选的接口；无数学执行。


## 9. 实际有理 supersingular 分量的精确类数计数

前面 §2、(1065.7) 已准确识别
$\#\mathcal M^{\rm sm}(\mathbf F_p)=p\,n_{\mathbf Q_p}(p)$。
这里的 $n_{\mathbf Q_p}(p)$ 是 $\mathbf F_p$ 内 supersingular
$j$ 值数；它不是全部几何 supersingular 值数 $n(p)$。
Delfs–Galbraith 原文第2页式 (1) 给出
$$
n_{\mathbf Q_p}(p)=
\begin{cases}
\frac12h(-4p),&p\equiv1\pmod4,\\
h(-p),&p\equiv7\pmod8,\\
2h(-p),&p\equiv3\pmod8,
\end{cases}
\tag{1065.22}
$$
其中 $h(D)$ 为判别式 $D$ 的虚二次域类数；此处三个 $D$
均为相应域的基本判别式。该文同页给
$h(D)\le\sqrt{|D|}\log|D|/\pi$。
因而三个分支的 $p\,n_{\mathbf Q_p}(p)$ 分别不超过
$$
\frac{p^{3/2}\log(4p)}{\pi},\qquad
\frac{p^{3/2}\log p}{\pi},\qquad
\frac{2p^{3/2}\log p}{\pi}.
$$
故原实际标签的无条件界可准确收紧为
$$
\boxed{
 \#\Phi_p(X(\mathbf Q_p))
 \le p\,n_{\mathbf Q_p}(p)
 \le\frac{2p^{3/2}\log(4p)}{\pi}.}
\tag{1065.23}
$$
在 §6 的 regular 条件下，同一 global-twist 候选数相应满足
$$
\boxed{
 \#\{\phi\in\mathscr L_W:Y_\phi(\mathbf Q_p)\ne\varnothing\}
 \le p\,n_{\mathbf Q_p}(p)\,p^{\kappa_p}.}
\tag{1065.24}
$$
全部 $2,3$ 角色、class-group 条件和实际 localization fiber
均保持 §5–6 的定义；没有把 supersingular reduction
称为 $\mathbf Q$-有理 CM 点，也没有据此排除任何候选。

本节核读来源：C. Delfs and S. D. Galbraith,
*Computing isogenies between supersingular elliptic curves over*
$\mathbf F_p$，[作者原文](https://arxiv.org/pdf/1310.7789)，
第2页式 (1) 及其下一段的类数界。
global_route 与 root 分别亲读该页并核对三个同余分支。
这里只消费已知精确计数，新增的是它对原规范标签及同一 global
twists 的直接界；无数学执行。


## 10. 后继的实际 CM 代表接口

[R1066](R1066-original-p-local-disks-and-bounded-CM-representatives.md)
已证明原每个 $\mathbf Q_p$ 模 $p$ 圆盘均含一个 canonical CM 点，
完整 CM 判别式 $D'\le4p^{3/2}/\sqrt3$，p 惰性且不除 conductor。
因此本篇有限局部标签像可由这些实际 CM 点及其指定
$\mathbf Q_p$ embeddings 完整读取。
这些点通常不是 $\mathbf Q$-有理点；这项进展没有证明
带这些标签的 $\mathbf Q$ 点为 CM，也没有支付同一 global twist
的辅助共同像条件。


## 11. 后继删去原 $2,3$ 全局自由度

[R1067](R1067-original-cuspidal-labels-supported-only-at-p.md)
已严格证明原规范标签仅在 $p$ 支撑。regular $p$ 下，
该精确允许全局空间到全部非平凡角色的 $p$-local 空间是同构。
所以本篇实际局部像中的每个标签恰有一个全局候选，
(1065.24) 的保守上界可收紧为 $p\,n_{\mathbf Q_p}(p)$，
不再带 $p^{\kappa_p}$。本篇对原较大 $S$-unit 空间的核维数计算仍成立；
R1067 的加强来自实际点标签落在严格较小的全局空间。
irregular class-group 项与同一候选的辅助共同像排除仍开。
