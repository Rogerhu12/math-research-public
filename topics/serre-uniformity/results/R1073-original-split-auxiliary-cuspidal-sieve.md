# R1073：原 split 辅助素的完整同点 cuspidal 标签算法

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：方法与全部来源、相位、覆盖范围已证明；本文未执行数学程序，也未声称已排除任何候选。** 本文把 R1064、R1068、R1069、R1070、R1071 的同一个原 Kummer 标签，变成在 $\ell\equiv1\pmod p$ 处可直接复核的完整有限点比较。随后明确 $p=47,\ell=283,c=5,\delta=5$ 的全部模型和 Frobenius 输入。

## 1. 原对象与正确的比较目标

固定
$$
X=X_{\rm ns}^+(p),\qquad p>37,\qquad
m=(p-1)/2,\qquad F=\mathbf Q(\zeta_p)^+,
\qquad G=\mathbf F_p^\times/\{\pm1\}.
$$
保 R1062 的实际 $V=C_\Sigma[p]$，以及 R1069 中已经付清唯一全局标签的 good 子模块 $W\subset V$。本文的函数评价对全部实际 $V$ 成立；把原 $p$-local 坐标称为唯一全局候选，只在 $W$ 上进行。

对每个实际非零角色 $\chi=\omega^R$，R1070 §10 已证明 $\chi^2\ne1$。取正奇整数 $c$，满足 $(c,6p\ell)=1$，且 $c\bmod p$ primitive。于是
$$
\kappa_\chi=c^2-\chi(c^2)\in\mathbf F_p^\times.
\tag{A1}
$$
选原整数指数 $n_h$，满足
$$
n_h\equiv m^{-1}\chi(h)^{-1}\pmod p,\qquad \sum_{h\in G}n_h=0.
\tag{A2}
$$
R1070 给同一个原单位基 $u_\chi\in V_\chi$ 和实际函数
$$
M_\chi(E,\mathcal C)
 =\prod_{v\in\mathbf F_{p^2}^\times/\{\pm1\}}
       \psi_c(P_v)^{-n_{[Nv]}},
\qquad
\Phi_y(u_\chi)=\frac m{\kappa_\chi}[M_\chi(y)].
\tag{A3}
$$
这里保持全部原 leading-coefficient 归一化；没有引入未知 cusp 常数，也没有把原 Kummer 类取 $p$ 次幂以消相位。

R1071 的 $p$-local 多项式给一个候选 $(C_\chi)_{\chi\subset W}$，其全局意义为
$$
\phi(u_\chi)=C_\chi\,\beta_\chi,\qquad
\beta_\chi=e_\chi[\eta_c]\in F^\times/F^{\times p},
\qquad
\eta_c=\zeta_p^{(1-c)/2}\frac{1-\zeta_p^c}{1-\zeta_p}.
\tag{A4}
$$
要在辅助素通过，必须存在**同一个** $y\in X(\mathbf F_\ell)$，使所有角色同时满足
$$
\operatorname{loc}_\ell\phi(u_\chi)
 =\operatorname{loc}_\ell\Phi_y(u_\chi).
\tag{A5}
$$
不能逐角色换用不同的 $y$，也不能把不同 $p$-local 圆盘的坐标混成一个候选。

## 2. 任意实际 full basis 与全部 necklaces

本节取素数 $\ell\equiv1\pmod p$；所以 $\mu_p\subset\mathbf F_\ell$。固定原 nonsquare $\delta\in\mathbf F_p^\times$，并使用
$$
\mathbf F_{p^2}=\mathbf F_p(s),\quad s^2=\delta,\quad
N(v_0+v_1s)=v_0^2-\delta v_1^2.
$$
对一个实际模型 $E/\mathbf F_\ell$，取真实 $E[p]$ 的基 $(P,Q_0)$，记 arithmetic Frobenius 的矩阵为 $A$。由 Weil pairing，$\det A=\ell\bmod p=1$。

所有 nonsplit necklaces 与下列矩阵的 $\pm$ 商一一对应：
$$
J=\begin{pmatrix}a&b\\d&-a\end{pmatrix},
\qquad a^2+bd=\delta,\qquad J\sim-J.
\tag{A6}
$$
因为 $\delta$ 非平方，$d=0$ 不可能。对每个 $a\in\mathbf F_p$ 和 $d\in\mathbf F_p^\times$，$b=(\delta-a^2)/d$ 唯一；故总数为 $p(p-1)/2$。

解释是：$\mathbf F_p[J]$ 是实际 nonsplit Cartan 代数；在每一个这样的代数内，满足 trace zero、square $\delta$ 的两个生成元恰为 $\pm J$。反向由该代数的共轭 eigenline 对得到 R1068 的同一 necklace。原固定条件准确为
$$
AJA^{-1}=J\quad\hbox{或}\quad AJA^{-1}=-J.
\tag{A7}
$$
没有仅凭 trace 相同而合并不同 necklaces。

该 necklace 使用的实际 Cartan basis 是
$$
(P,JP),\qquad
\begin{pmatrix}P&JP\end{pmatrix}
 =\begin{pmatrix}P&Q_0\end{pmatrix}
  \begin{pmatrix}1&a\\0&d\end{pmatrix}.
\tag{A8}
$$
因此若 $\zeta_{\rm nat}=e_p(P,Q_0)$，其真实 cyclotomic embedding 为
$$
\zeta_J=e_p(P,JP)=\zeta_{\rm nat}^{\,d}.
\tag{A9}
$$
它是 $\mathbf F_\ell$ 中的 primitive $p$-th root。$\zeta_{\rm nat}$ 必须由真实 Weil pairing 计算；只知道它是某个 primitive root 不能替代 (A9)。

## 3. 全部 norm 纤维的实际 base-field 乘积

先缓存 native 半点
$$
P_{u,w}=uP+wQ_0,\qquad
(u,w)\in(\mathbf F_p^2\setminus\{0\})/\{\pm1\}.
$$
共有 $(p^2-1)/2$ 个。对 (A6) 的一个 $J$，其 Cartan 坐标准确是
$$
v_1=w/d,\qquad v_0=u-aw/d.
\tag{A10}
$$
定义
$$
S_h(J)=
\prod_{\substack{(u,w)/\pm\\
 [\, (u-aw/d)^2-\delta(w/d)^2\,]=h}}
       \psi_c(P_{u,w}),
\qquad h\in G.
\tag{A11}
$$
每个纤维有 $p+1$ 个半点。$\psi_c$ 在这些点无零无极：其零点是非零 $c$-torsion，而 $(c,p)=1$；所有点又不为原点。因为 $c$ 为奇数，$\psi_c(-P)=\psi_c(P)$，故半点代表不影响乘积。

**每个 $S_h(J)$ 本身严格属于 $\mathbf F_\ell^\times$。** 为证明这一点，将 Frobenius 写在 (A8) 的 Cartan basis 中。若它与 $J$ 交换，则是乘某个 $\alpha\in\mathbf F_{p^2}^\times$，且 $N\alpha=\det A=1$。若它反交换，则是 $\alpha$ 乘共轭，且
$$
1=\det A=-N\alpha,\qquad N\alpha=-1.
$$
两种情况下 Norm 只乘 $1$ 或 $-1$，所以恰保持 (A11) 的 $G=\mathbf F_p^\times/\pm$ 标签。Frobenius 对每组半点作置换，且 $\psi_c$ 在 $\mathbf F_\ell$ 定义，遂逐组固定该乘积。

这正是必须按 $\pm$ Norm 分组的原因。若只按一个非商的 $N(v)=h$ 分组，反射情形下不能断言乘积在 base field。

由 (A3)，
$$
M_\chi=\prod_{h\in G}S_h^{-n_h}.
\tag{A12}
$$
原 $\sum n_h=0$ 同时消掉改变 Weierstrass differential/model 时的公共 scaling。改变指数的 $p$ 倍只使 (A12) 乘一个实际单位的 $p$ 次幂；没有删掉任何未知常数。

## 4. 同一 Weil root 下的完整有限行

对 $\zeta\in\mu_p(\mathbf F_\ell)$ primitive，定义
$$
\operatorname{KLog}_{\zeta}(x)
 =k\in\mathbf F_p
 \quad\Longleftrightarrow\quad
 x^{(\ell-1)/p}=\zeta^k,
 \qquad x\in\mathbf F_\ell^\times.
\tag{A13}
$$
这是实际 residue Kummer quotient 的固定坐标，不是对任意单位作 $p$-adic log。

对每个 $J$ 必须取 $\zeta=\zeta_J$。将 (A2) 代入 (A12)，原 $m$ 准确相消，得到
$$
D_\chi(J):=
\operatorname{KLog}_{\zeta_J}\Phi_y(u_\chi)
 =-\kappa_\chi^{-1}
   \sum_{h\in G}\chi(h)^{-1}
      \operatorname{KLog}_{\zeta_J}(S_h(J)).
\tag{A14}
$$
另一方面，用同一 root 评价原 circle class：
$$
B_\chi(\zeta_J)=
\frac1m\sum_{h\in G}\chi(h)^{-1}
 \operatorname{KLog}_{\zeta_J}
 \left(
 \zeta_J^{h(1-c)/2}
 \frac{1-\zeta_J^{ch}}{1-\zeta_J^h}
 \right).
\tag{A15}
$$
偶角色和 $\eta_c(\zeta^{-h})=\eta_c(\zeta^h)$ 使 $h$ 的 $\pm$ 代表无影响。原 (A5) 于是准确为
$$
\boxed{\quad
C_\chi B_\chi(\zeta_J)=D_\chi(J)
\qquad\hbox{对所有 }\chi\subset W.
\quad}
\tag{A16}
$$
若某个 $B_\chi(\zeta_J)=0$，必须保留条件 $D_\chi(J)=0$。不能除这个零读数，也不能由它断言该角色没有辅助约束。

若所有 $p$-torsion 在 $K=\mathbf F_{\ell^f}$ 中计算，(A11) 必须先核 $S_h^\ell=S_h$，再按 (A13) 读取。若改用 $K$ 的指数 $(\ell^f-1)/p$，则对 base-field 元素读数准确乘 $f\bmod p$，因为
$$
1+\ell+\cdots+\ell^{f-1}\equiv f\pmod p.
\tag{A17}
$$
在 $p\nmid f$ 时可以明确除 $f$，或者把两边统一用同一扩大域读数；不能漏掉这个因子。本文的指定 $p=47$ native nonsplit 输入有 $f\mid48$，所以 $p\nmid f$。

## 5. 换基、不同模型与相位的一致性

设固定 Cartan 内把第一向量换成 $\alpha P$，$N\alpha=b\in\mathbf F_p^\times$。新的 Norm 纤维满足
$S'_h=S_{bh}$，Weil root 变为 $\zeta'=\zeta^b$。重指标 (A14) 后
$$
D'_\chi=b^{R-1}D_\chi,\qquad
B_\chi(\zeta^b)=b^{R-1}B_\chi(\zeta).
\tag{A18}
$$
后一式也可直接在 (A15) 中以 $h\mapsto bh$ 核准。$J\mapsto-J$ 时 $b=-1$ 的相同读数规则使两边同时反号。故 (A16) 不依赖这些 Cartan basis 选择。

任意 native full-basis 更换只会重标同一个实际 $J$/necklace 集合。使用 (A8)–(A9) 的真实 Weil root 后，仍得到 (A18) 的同一点条件。几何 isomorphism 运输下原全部 $\psi_c$ 的 model scaling 由 (A2) 消去，原函数下降由 R1070 付款。因此不同 twists 若给同一 coarse 点，其 (A16) 定义同一个候选条件。

实际实现可以直接取所有模型、所有固定 necklaces 的条件并集；重复表示不改变这个并集。若要报告实际点数，则必须再按完整几何 automorphisms 取商，不能把模型行数当作点数。也不应把不同 $\zeta_J$ 下的原始 $D_\chi$ 数字直接当成同一固定坐标的标签；(A16) 或明确 (A18) 运输才是正确比较。

## 6. 所有 rational cusps 的完整行

因为 $\ell\equiv1\pmod p$，原 $m$ 个 cusps 全在 $\mathbf F_\ell$。不能只枚举 affine elliptic models。

固定任意一个实际 primitive root $\zeta\in\mathbf F_\ell$，并对每个 $h\in G$ 使用 R1064 的原 cusp $c_h$。其规范值是
$$
\Phi_{c_h}(u_\chi)
 =\frac m2\,\chi(h)\chi(-\delta)^{-1}
    e_{\chi^2}[\varpi_1],
\qquad
\varpi_1=(1-\zeta_p)(1-\zeta_p^{-1}).
\tag{A19}
$$
由原 circle identity
$$
(\chi(c)^2-1)e_{\chi^2}[\varpi_1]
 =2e_{\chi^2}[\eta_c],
$$
得到相同 Kummer 坐标中的完整 cusp 行
$$
\boxed{
D_{\chi,h}^{\rm cusp}(\zeta)
 =\frac{m\,\chi(h)\chi(-\delta)^{-1}}
        {\chi(c)^2-1}\,B_{\chi^2}(\zeta).
}
\tag{A20}
$$
这里 $\chi^2\ne1$、$c$ primitive 保分母非零。即使 $\chi^2$ 不属于实际 $V$，也必须计算右侧指定的 circle-unit 投影；它是 $F^\times/F^{\times p}$ 的真实分量，不能因不在 $V$ 删除。该局部 circle 读数仍可能为零。

每个 cusp 对候选的条件为所有角色同时
$$
C_\chi B_\chi(\zeta)=D_{\chi,h}^{\rm cusp}(\zeta).
\tag{A21}
$$
只允许同一个 $h$。换 $\zeta\mapsto\zeta^a$ 时，左侧按 $a^{R-1}$ 运输，右侧的 circle 平方角色按 $a^{2R-1}$ 运输；把全部 cusp 索引改为 $h/a$ 后，两边匹配。故完整 cusp 条件集合不依赖所选 primitive root。

## 7. $p=47,\ell=283$ 的全部实际输入

本节固定 $c=5,\delta=5$。$5$ 是模 $47$ primitive，且是 nonsquare。$\ell-1=282=6p$，所以 (A13) 就是 $x^6$ 的真实 $\mu_{47}$ 离散对数。

对所有 $j\in\mathbf F_{283}$ 取完整模型：
- $j\ne0,1728$：取一个 short Weierstrass representative。其另一 quadratic twist 给相同 projective Frobenius 和同一 coarse necklace 点集；一个代表足够。
- $j=0$：取全部六个 sextic twists。因为 $283\equiv1\pmod6$，这确为全部 $\mathbf F_{283}$-isomorphism classes。
- $j=1728$：取全部两个 quartic twists，因为 $\gcd(4,282)=2$。

这是 R1068 twisted-Burnside/实际 twist descent 的同一完整点源。一般 $j$ 的 geometric automorphisms 只有 $\{\pm1\}$，所以 quadratic twist 不新增 coarse 点。特殊 $j$ 则必须保全部 twists；不能只选一个模型的 fixed necklaces。

对任一个上述模型，真实 Frobenius 的 trace 满足 $|t|\le33$。R1068 的 endomorphism degree 论证适用，因为
$$
283<47^2/4.
$$
因此其 $47$-torsion 上不可能 scalar。若 $t^2-4\cdot283$ 模 $47$ 为零，则是非 scalar unipotent，没有 fixed necklace。若非零且 split，也没有 fixed necklace，除非 projective involution；本输入中 projective involution 等价 $t=0$，而此时 $-1$ 是模 $47$ nonsquare。因此所有有贡献的模型均有 irreducible Frobenius polynomial：
$$
t=0,\quad\hbox{或}\quad
t\ne0,\quad\left(\frac{t^2-4}{47}\right)=-1.
\tag{A22}
$$
任取非零 $P\in E[47]$，$(P,\pi P)$ 因而自动独立，可取
$$
Q_0=\pi P,\qquad
A=\begin{pmatrix}0&-1\\1&t\end{pmatrix}.
\tag{A23}
$$
$t\ne0$ 时恰有一个 fixed necklace。$t=0$ 时 $A^2=-I$，恰有
$$
(47+3)/2=25
$$
个 fixed necklaces，完整由 (A6)–(A7) 列出。所有这些矩阵在 nonsplit Cartan 内 determinant 一，故原 full Frobenius 的阶 $f$ 整除 $48$，真实 $47$-torsion 已在 $\mathbf F_{283^f}$ 定义。

这里每个 $J$ 的 $23$ 个纤维各含 $48$ 个半点；native cache 总共有 $1104$ 个半点。每个原 $M_\chi$ 都用这整套点，未把某个 Frobenius 相似类或一个代表点代替函数值。

$j=0$ 在 characteristic $283$ 是 ordinary。其六个 twists 的 Frobenius 位于原 $\mathbf Q(\sqrt{-3})$ Cartan；该 CM 域在 $47$ inert。其非标量 Frobenius 判别式是 $-3a^2$，且 $a\not\equiv0\bmod47$（Hasse 界与 $283<47^2/4$ 已排 scalar）。于是它们都给同一唯一 CM necklace/coarse 点。六个读数因此可以作为跨模型相位一致性核查，不能算成六个不同 coarse 点。

$j=1728$ 的两个 quartic twists 均 trace zero，各给 $25$ 个 fixed-necklace 表示。必须按几何 automorphisms 识别它们，或直接取其条件并集；不能把 $50$ 行称为 $50$ 个不同点。

最后加入 (A20) 的全部 $23$ 个 rational cusp 行。

## 8. 结果能说明什么

对 R1071 的每个完整原候选向量，逐个原辅助行测试 (A16)，并加入全部 (A21)。存在一行通过是必要条件；所有行都失败，才真正排除这个候选作为原 $X(\mathbf Q)$ 点的标签。

本方法不假设 circular-unit residue 非零，不把不同角色的辅助像作直积，不把同 trace 当同标签，不以固定 CM 代表替全部 twists，也不把通过一个辅助素的候选称作有理点。它可与另外的有效辅助素继续使用**同一个**候选向量作交集。

本文没有新数学运行或任何辅助排除的数值结论。

### 来源

- R1064，尤其 §§1–4、6–8：原统一 étale torsor、规范 cusp fibre、真实 Galois 角色和同标签条件。
- R1067：所有 $\ell\ne p$ 的原好模型、规范标签的 $p$-only 支撑。
- R1068 §§1–3：原 moduli/necklace 对象、twisted Burnside、全部 twist 覆盖、fixed-count 与 scalar degree 排除；其 primary 来源为 Rebolledo–Wuthrich, *A moduli interpretation for the non-split Cartan modular curve*, Glasgow Math. J. 60 (2018), 411–434，DOI 10.1017/S0017089517000180。
- R1069：Bernoulli-good 角色上的原全局标签唯一性。
- R1070，尤其 §§3–8、10：完整实际 $V$ 的原 division-polynomial 函数、实下降、全部 normalization 和可逆 $\kappa_\chi$。
- R1071：原全部 $p$-local 圆盘的候选坐标、同一 Weil pairing 相位与有限 source 算法。

global_route 逐项推导；root 对 norm 纤维方案、native basis、角色尺度与固定输入 coverage 作独立纸面核查。完整方法未经数学程序执行。

root 已逐式独核 (A1)–(A23)，包括原负指数、全部 m/2 因子、Norm/± 的严格 base-field 下降、换 Weil root 的 a^(R−1) 运输、zero-circle mask、全部 cusp 同一 h，以及指定 283 的实际 twist/Frobenius 覆盖。o2 独立纸核主要角色尺度与 cusp 式。后继数值 sieve 尚未执行。


## 9. 完整 Frobenius 半轨道乘积与固定-root 的规范标签

本节给原算法的精确压缩；只改变有限乘积的顺序和读数坐标，不删除任何点、角色或相位。

### 9.1 必须使用 half-orbit 的长度

令
$$
\mathcal T=(\mathbf F_p^2\setminus\{0\})/\{\pm1\}
$$
为 native 半点集合，$A$ 在其上作用。对每条完整轨道 $O$，取代表 $v_O$，令 $r_O=|O|$。实际点满足
$$
\pi^{r_O}P_{v_O}=\epsilon_O P_{v_O},
\qquad \epsilon_O\in\{1,-1\}.
$$
因为奇 $c$ 的 $\psi_c$ 是偶函数，
$$
\theta_O:=\psi_c(P_{v_O}),\qquad
\theta_O^{\ell^{r_O}}=\theta_O.
$$
因此准确的 orbit product 是
$$
W_O=\prod_{i=0}^{r_O-1}\theta_O^{\ell^i}
    =\prod_{v\in O}\psi_c(P_v)
    \in\mathbf F_\ell^\times.
\tag{A24}
$$
改变轨道起点只对右侧作循环重排。即使 $\theta_O$ 定义在一个更小的子域，仍必须用 $r_O$ 个因子；轨道中可能相等的数值有其真实重数。

若计算采用 $K=\mathbf F_{\ell^f}$，不能把 (A24) 直接换成 $N_{K/\mathbf F_\ell}(\theta_O)$。当 $r_O\mid f$ 时，后者是
$$
N_{K/\mathbf F_\ell}(\theta_O)=W_O^{\,f/r_O}.
\tag{A25}
$$
特别本题 trace-zero native Frobenius 满足 $A^2=-I$，full torsion field 的阶为 $f=4$，但所有非零 half-orbits 的长度是 $2$。此时错误使用 ambient norm 会把原 $W_O$ 平方。

对一般 irreducible semisimple $A$，所有非零 half-orbit 的长度都等于
$$
\min\{r\ge1:A^r=\pm I\}.
\tag{A26}
$$
事实上，若 $A^rv=\pm v$ 对某个非零 $v\in\mathbf F_p^2$ 成立，则在 $A$ 的 nonsplit Cartan 中相应乘子为 $\pm1$，故 $A^r=\pm I$。不要求先选一个特殊 torsion 点。

### 9.2 每个 stable necklace 的分组完全在 base field 完成

对一个满足 (A7) 的 $J$，§3 已证明 Norm/± 标签在完整 Frobenius half-orbit 上不变。记该标签为 $h_J(O)$。于是原乘积准确为
$$
S_h(J)=\prod_{\substack{O\subset\mathcal T\\h_J(O)=h}}W_O.
\tag{A27}
$$
因此每个 orbit 只须一次真正的 $\psi_c$ 求值；随后按真实 Frobenius 幂形成 (A24)。全部 $J$ 的后续分组都只需在 $\mathbf F_\ell^\times$ 内乘法。

必须同时核完整覆盖计数
$$
\sum_O r_O=(p^2-1)/2,\qquad
\sum_{O:h_J(O)=h}r_O=p+1
\quad\text{对每个 }J,h.
\tag{A28}
$$
$p=47$ 时两式右侧分别为 $1104$ 和 $48$。此外逐个核 $W_O^\ell=W_O$。这些检查与 (A27) 的证明共同保证没有只取一个 orbit 代表便漏掉它的重数，也没有把一个非闭合列表冒充 Norm。

所有这些式子是有限域中的严格身份，无近似截断或误差项；唯一潜在的次数混淆已在 (A25) 明确支付。

### 9.3 固定 primitive root 下的完整原标签

固定 $\zeta_0\in\mu_p(\mathbf F_\ell)$ primitive。实现时可以取 prime-field 标准整数表示中最小的 primitive $p$-th root，这只是可复核的确定性选择。

每个 $J$ 的原真实 root 已由 (A9) 计算。唯一地写
$$
\zeta_J=\zeta_0^{\,a_J},\qquad a_J\in\mathbf F_p^\times.
\tag{A29}
$$
先完整计算 (A14)–(A15) 的实际读数，再定义
$$
D_\chi^0(J)=a_J^{\,1-R}D_\chi(J),\qquad
B_\chi^0=a_J^{\,1-R}B_\chi(\zeta_J).
\tag{A30}
$$
由 (A18)，第二式严格等于
$$
B_\chi^0=B_\chi(\zeta_0)
\tag{A31}
$$
并且与模型、native basis 和 $J$ 无关。这可以逐行核查。

第一式也确是原标签在固定 embedding/root 下的读数，而不只是任意坐标缩放：Norm 映射
$\mathbf F_{p^2}^\times\to\mathbf F_p^\times$ 满射，故可把 Cartan basis 乘一个 Norm 为 $a_J^{-1}$ 的元素，使其 Weil root 准确成为 $\zeta_0$。按 (A18)，真实标签的变化正为 $a_J^{1-R}$。实际计算不必构造这个换基元素；(A30) 已支付其全部作用。

所以同一个原候选的完整固定辅助向量可以只构造一次：
$$
\mathcal C_\ell(C)=
  \bigl(C_\chi B_\chi(\zeta_0)\bigr)_{\chi\subset W}.
\tag{A32}
$$
对每个原 affine 点，只需比较
$$
\mathcal C_\ell(C)
 =\bigl(D_\chi^0(J)\bigr)_{\chi\subset W}.
\tag{A33}
$$
$B_\chi(\zeta_0)=0$ 的坐标依然保留为零，并要求右侧相应坐标为零；没有除零。

cusp 行直接在 $\zeta_0$ 下使用 (A20)。若先在 $\zeta_J=\zeta_0^a$ 下计算，则乘 $a^{1-R}$ 后得到固定-root 下索引 $ah$ 的 cusp 行；因为平方角色的 $a^{2R-1}$ 和外侧 $\chi(h)$ 正好给这个同步重标。因此仍是同一套完整 $m$ 个 cusp 行。

### 9.4 可复核的输出与范围

在声明的模型、全部 fixed $J$ 和全部 cusps 上，收集固定-root 向量并去重，可以给出排序后的真实辅助标签像及其 hash。不同 finite-field 模型、native torsion basis 或 orbit 代表只会重排原点表示，不改变这个固定 $\zeta_0$、固定角色顺序的标签集合。

不同原点可能有相同标签；去重所得数目是标签像大小，不是原曲线点数。重复 twists 给同一 coarse 点，也不会改变这个像。全部候选必须用 (A32) 的同一组 global coordinates 比较该像。若两个候选在某个辅助素因 $B_\chi=0$ 等原因合并，也不能错误地把它们当成同一个 $p$-local 圆盘。

本节只证明 exact finite-field 操作及来源，无数学程序执行。后继真正排除仍须由已授权公开 CI 的实际完整输出或独立纸面证明给出。

root 独核 §9：half-orbit 的真实重数、ambient norm 的 f/r 因子、整 Norm/± 纤维的 1104/48 覆盖，以及固定 root 的 a^(1−R) 与 cusp 同步重标均一致；仍未执行辅助数学。
