# 原辅助 c-扭点相关和与整 Manin 关系

日期：2026-11-28（Asia/Taipei）  
会话：Astra-serre-24b8836b-20261126  
状态：完整纸证；无新数学程序执行。一般 $p$ 主目标仍为 OPEN。

## 1. 本文付出的具体输入

固定 $p>37$。在原 full-level 通用椭圆曲线的函数域中，
取奇整数 $c\ge3$、$(c,p)=1$，使用原除法多项式规范
$h_c=\psi_c^{-1}$。本文构造
$$
\Psi_c(P,Q)=
c^2\{h_c(P),h_c(Q)\}
-\sum_{t\in E[c]_{\rm cl}}
\operatorname{Cor}_{k(t)/k}
 \{h_c(P+t),h_c(Q-t)\}.
\tag{C.1}
$$
其中 $P,Q\in E[p](k)\setminus\{0\}$，
求和按 $E[c]$ 的全部 closed points，包含 $t=0$。
这个实际 $K_2$ 类满足整的 Manin 三项关系。证明只用原
$K_3$ 符号的全部残数，没有将 level-$p$ theta 取 $12p$ 次幂，
也没有除以 $p$ 或 $p^2$。

式 (C.1) 中的第二项是同一个 $t$ 在两槽中反向平移的相关和。
它不能被替换成两个独立范数的符号。
特别是，从这个实际来源得到的首系数是 $c^2$；
本文没有证明一个仅由同时 $(P,Q)\mapsto(cP,cQ)$ 给出的
$c^4-[c,c]$ 算子，也不把该算子作为既有输入。

## 2. 原函数、闭点及完整 multiplicity

令 $k$ 为特征零域，$E/k$ 为一个固定 Weierstrass 模型，
并假设原 $E[p]$ 标记均定义于 $k$。
应用时取 $k=K(X(p))$，$K=\mathbf Q(\zeta_p)$；
需要时先在该实际函数域上选 Weierstrass 模型。
沿用 R1070/R1133 的除法多项式，取
$$
h_c(T)=\psi_c(T)^{-1}.
$$
$c$ 为奇数，故 $h_c(-T)=h_c(T)$ 严格成立。
其完整 divisor 是
$$
\operatorname{div}(h_c)
=c^2[O]-\sum_{t\in E[c]}[t].
\tag{C.2}
$$
因此在 $O$ 的阶是 $c^2-1$，其余 $c$-扭点的阶为 $-1$。
这里的和是有限 étale divisor，度恰为 $c^2$。

对非零 $P\in E[p]$ 和任意 $t\in E[c]$，
$P+t$ 既不为 $O$，也不属于 $E[c]$；
否则乘以 $c$ 会给 $cP=0$，与 $(c,p)=1$ 矛盾。
所以 (C.1) 中每个值都存在且非零。
在模曲线非退化开部的每个局部无零 Hodge 标架中，这些值都是单位。
个别 $h_c(P+t)$ 仍有 Hodge 权，不能把任意有理 Weierstrass 标架
下的内点零极直接当成 cusp。换局部标架时，它们乘同一个与
$P,t$ 无关的权常数；§4 的全局 $H_{\chi,c}(t)$ 因 augmentation
恰为零才下降为真正权零的 modular unit，其零极仅在 cusp。

闭点写法保留原 residue field。若先在 splitting field 中
写全部 $c^2$ 个几何点，下降时仍须恢复 (C.1) 的完整
corestriction，而不是只取一个代表或另除以 $c^2$。
以下证明直接在 $k$ 上用 closed-point residue，因此不需要
预先对 splitting field 的次数做任何除法。

## 3. 从一个实际 K3 符号逐槽取残数

取互异 $A,B,C\in E[p](k)$，令
$$
u=A-B,\qquad v=B-C,\qquad w=C-A.
$$
于是 $u,v,w$ 均非零，且 $u+v+w=0$。
在 $k(E)$ 中取实际符号
$$
\Xi_c(A,B,C)=
\{h_c(z-A),h_c(z-B),h_c(z-C)\}\in K_3^M(k(E)).
\tag{C.3}
$$
三个 divisor 支持 $A+E[c],B+E[c],C+E[c]$ 两两不交。
例如交点会使 $A-B\in E[p]\cap E[c]=\{0\}$。
所以每个支持点只有一个槽有非零 valuation，
没有两个非单位槽导致的额外 $-1$ 修正。

写 $d_t=c^2\mathbf1_{t=0}-1$。
在 $z=A+t$ 的完整残数为
$$
d_t\{h_c(A-B+t),h_c(A-C+t)\}
=d_t\{h_c(u+t),h_c(w-t)\}.
\tag{C.4}
$$
第二步用 $h_c$ 的严格偶性。对该 coset 的所有 closed points
作 corestriction 求和，正是 $\Psi_c(u,w)$。

在 $z=B+t$，中间槽移到第一槽产生负号：
$$
-d_t\{h_c(B-A+t),h_c(B-C+t)\}
=d_t\{h_c(v+t),h_c(u-t)\}.
\tag{C.5}
$$
这一组准确给 $\Psi_c(v,u)$。
在 $z=C+t$ 的第三组则为
$$
d_t\{h_c(w+t),h_c(v-t)\},
\tag{C.6}
$$
给 $\Psi_c(w,v)$。没有其他零极点。

原 Milnor $K_3\to K_2$ 的 proper-curve reciprocity 是整等式：
所引原稿 Theorem 2.2.2 最后一句明确包含 $n=3$ 的 integral 版本。
也可将 (C.3) 送入 Quillen $K_3$，由曲线 localization 的边界、
闭点 pushforward 与 proper pushforward 的复合为零读取。
因此得到
$$
\boxed{\quad
\Psi_c(u,w)+\Psi_c(w,v)+\Psi_c(v,u)=0
\quad(u+v+w=0).
\quad}
\tag{C.7}
$$
这是整 $K_2^M(k)=K_2(k)$ 中的等式，不只是张量 $\mathbf Q$ 后成立。
特别要保留 $t=0$：首项 $c^2$ 减去求和中的那一项，
才恰是原 divisor 的 $c^2-1$。

由 $t\mapsto-t$ 以及 field $K_2$ 的反对称性，
$$
\Psi_c(Q,P)=-\Psi_c(P,Q),\qquad
\Psi_c(-P,-Q)=\Psi_c(P,Q).
\tag{C.8}
$$
故 (C.7) 也等价于通常顺序
$\Psi_c(u,v)+\Psi_c(v,w)+\Psi_c(w,u)=0$。
退化值 $\Psi_c(u,-u)$ 至多为 $2$-torsion；
在本文使用的 $p$-local 群中为零，可相容地把零槽值定义为零。
这里不把一个 arbitrary pair 的 $\Psi_c$ 值宣称为零。

## 4. 共同模型常数及原加权函数

若改变 Weierstrass 模型或使用同源的 theta 平滑函数，
$h_c$ 会乘上同一个 base 常数 $\lambda\in k^\times$。
不能逐个槽位删除这个常数。

先注意实际函数
$$
\prod_{t\in E[c]}h_c(z+t)
$$
的 divisor 为零，因此它是某个固定 $\nu_c\in k^\times$。
用 projection formula 展开 (C.1)，得到准确变换
$$
\Psi_c^{\,\lambda h}(P,Q)-\Psi_c^{\,h}(P,Q)
=c^2\{\lambda,h_c(Q)/h_c(P)\}.
\tag{C.9}
$$
右侧在三项循环中望远镜相消。因此 (C.7) 的实际规范不依赖
未说明的模型常数；但单个 $\Psi_c(P,Q)$ 仍须按已选模型读取。

现在回到原 R1064/R1070 的全部标记。对两个实际非零角色
$\chi,\psi$，保原整数权
$$
n_{\chi,[Nz]}\equiv
m^{-1}\chi([Nz])^{-1}\pmod p,\qquad
\sum_h n_{\chi,h}=0,
$$
并保 $\psi$ 的同一规范。记
$$
H_{\chi,c}(t)=
\prod_{z\in\mathbf F_{p^2}^{\times}}
 h_c(P_z+t)^{n_{\chi,[Nz]}}.
\tag{C.10}
$$
这是 **all-vector** 乘积，不是 half-vector 乘积。尤其
$$
H_{\chi,c}(0)
=\prod_{z\ne0}\psi_c(P_z)^{-n_{\chi,[Nz]}}
=M_{c,\chi}^{\mathrm{all}}.
\tag{C.11}
$$
$\sum_{z\ne0}n_{\chi,[Nz]}=2(p+1)\sum_hn_{\chi,h}=0$，
故每个 $H_{\chi,c}(t)$ 内的同一个 $\lambda$ 都准确消失，
没有剩余未知常数或另一个 half/all 因子。

对 (C.1) 作完整双权重求和，双线性与 projection formula 给
$$
\begin{aligned}
\mathcal P_{\chi,\psi,c}
&:=\sum_{z,z'\ne0}
 n_{\chi,[Nz]}n_{\psi,[Nz']}
 \Psi_c(P_z,P_{z'})\\
&=
c^2\{M_{c,\chi}^{\mathrm{all}},M_{c,\psi}^{\mathrm{all}}\}\\
&\quad-\sum_{t\in E[c]_{\rm cl}}
\operatorname{Cor}_{k(t)/k}
 \{H_{\chi,c}(t),H_{\psi,c}(-t)\}.
\end{aligned}
\tag{C.12}
$$
这是保留全部 shifted products、closed-point fields 和
corestriction 的实际恒等式。
(C.7) 说该 pair-symbol 具有真 Manin 关系；
它**不**说 (C.12) 的任意 rectangular 双权重和自动等于零。

## 5. 与原 normalized Kummer 类的精确接口

R1070 §9/R1133 §4 已付的是函数域类本身：
$$
[M_{c,\chi}^{\mathrm{all}}]
=\frac{2\kappa_\chi(c)}m[F_\chi],
\qquad
\kappa_\chi(c)=c^2-\chi(c^2).
\tag{C.13}
$$
所以在原 $K_2/p$ 中，(C.12) 的首项严格是
$$
\frac{4c^2\kappa_\chi(c)\kappa_\psi(c)}{m^2}
 \{F_\chi,F_\psi\}.
\tag{C.14}
$$
这里的 $F_\chi$ 是原 $u^m/A(u)$ 规范，
不是任意重标的 modular unit。余下相关和必须完整保留。

可选一个同时适用两角色的奇整数 $3\le c<p$。
确实，每个实际角色满足
$\chi(t^2)=t^{k_\chi}$，
$k_\chi$ 为偶数且 $4\le k_\chi\le p-3$。
$\kappa_\chi(c)=0$ 的剩余类集合是
$$
\{c\in\mathbf F_p^\times:c^{k_\chi-2}=1\},
\tag{C.15}
$$
一个 proper subgroup。两个 proper subgroups 不可能覆盖
$\mathbf F_p^\times$。选定并集外的剩余类，再在 $\pm c$ 中
取 $1,\ldots,p-1$ 的奇代表；两种 $\kappa$ 都不改变。
它不是 $1$，故满足所述范围，且 (C.14) 的系数为 $p$ 单位。

对这一范围的 $c$，还可明确保辅助 full division field 的
prime-to-$p$ 性：对每个素因子 $\ell\mid c$，
$$
|\operatorname{GL}_2(\mathbf Z/\ell^e)|
=\ell^{4e-3}(\ell-1)^2(\ell+1)
$$
不被 $p$ 整除。因为 $\ell<p$，而 $\ell+1=p$ 会要求
$\ell=p-1$，与 $p>3$ 时 $\ell$ 为素数矛盾。
因此 $k(E[c])/k$ 的次数为 $p$ 单位。
这提供需要时 restriction–corestriction 的整下降入口；
(C.3)–(C.7) 的 closed-point 证明本身不依赖这种除法。

## 6. 已付款的范围及真实下一门

本笔记无条件付出：

1. 原 $\psi_c$ 上一个实际 $K_3$ 符号和它的全部有限点残数。
2. 无 $p$ 分母的整 Manin 关系 (C.7)，包含 $t=0$ 的准确阶。
3. 原 all-vector 函数与 $F_\chi$ 的准确尺度 (C.12)–(C.14)。
4. 对任何两个实际角色可同选 $c<p$ 使该尺度为单位。

下一步仍需对指定原 Manin/Hecke 线性组合读取
(C.12) 的完整 anti-diagonal $c$-torsion correlation。
不能以 $\Psi_c$ 有三项关系，推断每个单独原
$\{F_\chi,F_\psi\}$ 为有理零、模 $p$ 零或存在全局单位 norm witness。
也不能把一条完整 prime-to-$p$ 辅助覆盖的 corestriction
缩成若干已选几何点。

本笔记没有用 R1132 的 normalized integral torsion 消失
来替代任意 $K_2/p$ 类的消失；没有得到原 coarse 曲线的四阶覆盖，
没有关闭一般 $p$ 的同点排除问题，也没有重开固定 $p=47$ 的计算。

## 来源与独立审核

- [R1070](../results/R1070-original-cuspidal-labels-by-division-polynomial-values.md)
  §§9–10：实际 $\psi_c$、all-vector 规范、共同模型常数、
  完整角色范围及原 $\kappa$。
- [R1133](../results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)
  §§1–8：原 full-level/Cartan/norm 范围及必须保留的 crossed terms。
- Milnor $K_3$ 在 proper smooth curve 上的 residue/corestriction
  reciprocity。本文逐点算 (C.4)–(C.6)，没有引用仅张量 $\mathbf Q$
  的 Manin 关系作为整结论。
- Busuioc–Park–Patashnick–Stevens,
  *Modular Symbols with Values in Beilinson-Kato Distributions*,
  作者稿 2025-10-13，§3.2 提供比较：
  https://discovery.ucl.ac.uk/id/eprint/10222921/1/Kato-Milnor-Siegel_2025Aug.pdf 。
  已亲读 Theorem 2.2.2 的 $n=3$ 整 reciprocity，以及
  Lemma 3.2.1/Proposition 3.2.3 的 $N^2(12N^2)^3$ 尺度。
  该稿的主构造在 rational $K$ 群中；本文没有在 $N=p$ 时
  除去其 $p$ 因子，而是另用实际 $c$-torsion divisor 得到
  上述保留 correlation 的整等式。

global_route 推导。o2_high_coefficient 已独立纸核三 coset、
$t=0$ 的阶、中槽负号、偶性、完整 closed Cor，以及
原全向量双乘积和共同常数消去。全文候选交根线程复核。


root 对精确候选78d638a逐式独立审核，并亲读所引作者稿 Theorem 2.2.2 的 n=3 整版本及 §3.2 的有理尺度；三组互不交支持、残数符号、模型常数、全向量权及双κ单位门均通过。按共同审核收紧个别h_c的Hodge标架措辞：真正的全局权零单位是augmentation后的Hχ,c；未改函数域K₃或任何Cor项。
