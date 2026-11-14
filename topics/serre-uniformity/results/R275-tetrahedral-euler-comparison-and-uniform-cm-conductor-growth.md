# R275：实际三挠点的四面体提升与六次 CM 分支的统一导子增长

日期：2026-11-13。

**状态：已证明。** 保留 R258 的实际小惯性、$K=H=\mathbb Q(\sqrt{-3})$、$\sigma=1$ 和整 $j$ 假设，并假定 $E$ 无 CM。对每个 $\epsilon>0$，

$$\boxed{c\gg_\epsilon p^{25/507-\epsilon}.} \tag{275.1}$$

隐含常数只依赖 $\epsilon$，不依赖实际曲线、$p$ 或变化的六次 CM 参数。这是无条件且有显式指数的增长结论。**本文不声明隐含常数可有效计算**：所引用 Wu 次凸定理的证明使用 Siegel 下界；显式次凸指数不自动给出有效常数。

结果覆盖 R261、R263 留下的共同三次商域及共同二、三除法域情形，包括 R266 尚未排完的 $c=9$ 族。它证明，在这个完整分支中，任何预先固定的 $c$ 上界都只允许有界的 $p$；它不排除 $c$ 同时增长，因而不完成 Serre 一致性。

## 1. 实际对象与二择一的使用

取 R258 的同一个全局二次扭曲及正立方自由参数，记

$$
E_0[p]\simeq A[p],\qquad
A=A_d:\ y^2=x^3+d,\qquad
N(E_0)=N(A)=\kappa p^2c^2.
\tag{275.2}
$$

这里 $p>37$，$p\equiv2,5\pmod9$，$\kappa$ 属于 R258 的六个固定值，且

$$
d=2^u3^vp^m\prod_{\substack{q\mid c\\q\ge5}}q^{e_q},
\qquad u,v\in\{0,1,2\},\quad m,e_q\in\{1,2\}.
\tag{275.3}
$$

实际模 $p$ 像仍为完整 $N_{\rm ns}(p)$，在 $p$ 的像仍为 $C^3$。所有出现的三挠点表示均属于这同一对曲线 $E_0,A$。

写

$$
\mathcal L_3(B)=\overline{\mathbb Q}^{\ker(\rho_{B,3}\bmod Q_8)}
=H(\sqrt[3]{\Delta_B}),
\tag{275.4}
$$

其中 $Q_8\triangleleft\operatorname{GL}_2(\mathbb F_3)$ 为四元数正规子群，商为 $S_3$；等式见 R96、R261。两条曲线的这个商均满射到 $S_3$。对 $A$，这是因为 $v_p(\Delta_A)=2m$ 不被三整除；对 $E_0$，R258 的 $p$ 处好约化分歧指数为三或六，极小判别式赋值为 $4,8$ 或 $2,10$，同样不被三整除。

R261 已证明：若两个实际商域不同，则对任意 $\delta>0$，

$$c\gg_\delta p^{1/3-\delta}. \tag{275.5}$$

由于 $25/507<1/3$，这已蕴含 (275.1)。此后只需处理

$$\mathcal L_3(E_0)=\mathcal L_3(A). \tag{275.6}$$

该假设只比较实际 $S_3$ 商域，不把两个完整三挠点表示误认为相同。

## 2. 实际模三像必为完整 $\operatorname{GL}_2(\mathbb F_3)$

令 $G=\rho_{E_0,3}(G_{\mathbb Q})$，$U=G\cap Q_8$。因为 $G\to S_3$ 满射，$G$ 中存在元素以三循环置换 $Q_8$ 的三个阶四循环子群。$U$ 在该共轭作用下稳定。

若 $U$ 包含一个非中心元素，则包含它生成的阶四子群，进而包含其三循环共轭，故 $U=Q_8$。否则 $U\subset\{\pm I\}$。在后一情形，$S_3$ 的正规阶三子群在 $G$ 中的逆像是阶三或阶六群；若阶六，其阶二核为中心，所以该逆像为循环群。它的唯一阶三子群因而在 $G$ 中正规。

一个非平凡阶三子群作用在 $\mathbb F_3^2$ 上时由非平凡幺幂矩阵生成，具有唯一不变直线。该子群正规，使这条直线被整个 $G$ 保持。因此 $E_0$ 有有理三同源。

Lemos Theorem 1.1（已在 R8 使用）说明：无 CM 且有非平凡有理循环同源的椭圆曲线，对每个 $p>37$ 都具有满模 $p$ 像。这与 (275.2) 的坏像矛盾。所以 $U=Q_8$，从而

$$
G=\operatorname{GL}_2(\mathbb F_3),\qquad
\rho_{E_0,3}(G_H)=\operatorname{SL}_2(\mathbb F_3).
\tag{275.7}
$$

第二式使用 $\det\rho_{E_0,3}=\chi_{-3}$，其核恰为 $G_H$。

## 3. 复提升、角色与准确的复迹表

采用标准忠实提升

$$
\iota:\operatorname{GL}_2(\mathbb F_3)
\hookrightarrow
\operatorname{GL}_2(\mathbb Z[\sqrt{-2}])
\subset\operatorname{GL}_2(\mathbb C),
\tag{275.8}
$$

其在素理想 $(1+\sqrt{-2})$ 约化为恒等映射。Wiles 的已发表原文，第五章 Theorem 5.1 后、印刷页 541–542，明确给出此提升和约化归一化。

该提升的行列式取值于 $\mathbb Q(\sqrt{-2})$ 中的单位根，即 $\{\pm1\}$；约化恒等性说明它就是自然行列式。因此在 $\operatorname{SL}_2(\mathbb F_3)$ 上，复行列式恒为一。

以下表格由元素的准确阶数确定，不能把 $\mathbb F_3$ 的迹直接当作复数迹：

| $g\in\operatorname{SL}_2(\mathbb F_3)$ 的类型 | 是否属于 $Q_8$ | $\operatorname{tr}_{\mathbb F_3}(g)$ | $\operatorname{tr}_{\mathbb C}\iota(g)$ |
|---|---|---:|---:|
| $I$ | 是 | $2$ | $2$ |
| $-I$ | 是 | $1$ | $-2$ |
| $Q_8\setminus\{\pm I\}$，阶四 | 是 | $0$ | $0$ |
| 阶三 | 否 | $2$ | $-1$ |
| 阶六 | 否 | $1$ | $1$ |

确实，复提升忠实且行列式为一，故阶四、三、六元素的特征值分别为 $\{i,-i\}$、$\{\zeta_3,\zeta_3^{-1}\}$、$\{\zeta_6,\zeta_6^{-1}\}$。非平凡中心阶二元必须提升为 $-I$。自然二维特征三表示上的迹由各元素的特征多项式给出。$\operatorname{SL}_2(\mathbb F_3)$ 的元素除 $\pm I$ 和 $Q_8$ 的六个阶四元外，均为阶三或六，故表格穷尽全部情形。

设

$$\Sigma=\iota\circ\rho_{E_0,3}|_{G_H}. \tag{275.9}$$

它是忠实、不可约的复二维表示；若可约，则有限像可同时酉化并分解为两个一维角色，像应交换，与 (275.7) 矛盾。其 projective 像为

$$\operatorname{SL}_2(\mathbb F_3)/\{\pm I\}\simeq A_4,$$

所以是四面体型。

另一方面，$A$ 的三阶 CM 自同构在 $H$ 定义，在 $A[3]$ 上是非平凡幺幂元。它非平凡，因为对应自同构减恒等的核只有三阶，不能包含全部九个三挠点。其在 $\operatorname{GL}_2(\mathbb F_3)$ 中的中心化子是循环六阶群；$G_H$ 的像必须落在这个中心化子中。于是

$$
\iota\circ\rho_{A,3}|_{G_H}\simeq\eta\oplus\eta^{-1}
\tag{275.10}
$$

对某个有限阶 Hecke 角色 $\eta$ 成立，且 $\eta^6=1$。全局类域论在此只将实际一维 Galois 角色视作 Hecke 角色。

令

$$
\tau=\Sigma\otimes\eta^{-1},\qquad
\chi=\eta^{-2}.
\tag{275.11}
$$

因为 $A$ 的 $S_3$ 商在 $p$ 分歧，$\eta^2$ 非平凡且在 $p$ 分歧。因此 $\chi$ 恰为三阶角色。$\tau$ 仍不可约，projective 像仍为 $A_4$，行列式为 $\chi$。

Langlands 的四面体定理给出酉尖点表示 $\Pi$，满足

$$
L(s,\Pi)=L(s,\tau),\qquad \omega_\Pi=\chi,
\tag{275.12}
$$

而且每个地方的参数均与 $\tau$ 匹配。这里使用《Base change for GL(2)》§3 的完整结论：该节开头证明几乎处处匹配与全部地方匹配等价；随后 Theorem 3.3 的证明为任意数域上的四面体表示构造相应尖点表示。因此 (275.12) 包含坏 Euler 因子及 Artin 导子相等，不仅是去掉未控制的有限集合后的等式。不需要把 $H$ 误当作实二次域，也不需要对 $H$ 上的表示添加奇性条件。

## 4. 实际导子的两个不同上界

写 $c^{(6)}$ 为去掉 $c$ 的二、三因子后的部分。本节证明，绝对常数 $C_0$ 下，

$$
\boxed{
C(\Pi)\le C_0p^4c^2,\qquad
C(\chi)\le C_0p^2c^2.
}
\tag{275.13}
$$

这里 $C$ 为中心点的解析导子。因为底域 $H$ 固定，且所有 Artin 参数有限，阿基米德部分固定；只需控制有限 Artin 导子。

### 4.1 在 $q\ge5,\ q\ne p$ 处

若 $q\nmid c$，则 R258 保证 $E_0,A$ 都有好约化。因此三挠点及 (275.11) 全部不分歧。

若 $q\mid c$，则 $A$ 的有限惯性为循环三阶或六阶。实际同构 $E_0[p]\simeq A[p]$ 识别两边在惯性上的表示。由于 $p>37$，潜在好约化的有限惯性在模 $p$ 约化时忠实，故 $E_0$ 的有限惯性也为同一阶数。

对每个惯性元素，两条曲线的特征零 Tate 表示的迹均是 $\{-2,-1,0,1,2\}$ 中的整数；它们模 $p$ 相同，所以作为整数相同。这里的迹与辅助 Tate 素数无关：它是对应良约化特殊纤维自同构的特征多项式的迹。

模三约化也不杀掉任何非平凡有限惯性元。一个直接证明是：$1+3M_2(\mathbb Z_3)$ 无非平凡有限阶元。若 $M=1+3^rB$、$r\ge1$，且 $B$ 至少一项为三进单位，则

$$v_3(M^3-I)=r+1;$$

乘以任何素于三的正整数幂则仍为 $r$，所以任何有限正整数幂都不能成为恒等。

因此，第 3 节复提升在这些阶数为 $1,2,3,6$ 的惯性元上的迹恰为原特征零迹。得到

$$
\Sigma|_{I_{\mathfrak q}}
\simeq
(\eta\oplus\eta^{-1})|_{I_{\mathfrak q}}
$$

对 $H$ 的每个 $\mathfrak q\mid q$ 成立，进而

$$
\tau|_{I_{\mathfrak q}}\simeq1\oplus\chi|_{I_{\mathfrak q}}.
\tag{275.14}
$$

这里 $\chi|_{I_{\mathfrak q}}$ 为非平凡温和三次角色。所以 $\tau$ 与 $\chi$ 的局部导子指数都恰为一。即使不同素理想的两个特征交换，(275.14) 仍成立：无序特征集合相同已保证 $\eta$ 是其中一条。

因此所有这些地方贡献的导子范数都是 $(c^{(6)})^2$。

### 4.2 在表示素数 $p$ 处

$p\equiv2\pmod3$，所以在 $H$ 中惰性，唯一素理想范数为 $p^2$。$\tau$ 的有限像阶整除 $24\cdot6=144$，而 $p>37$，故它在 $p$ 的野惯性平凡。二维温和表示的 Artin 指数至多二。因此该处对 $C(\Pi)$ 的贡献至多 $p^4$。

$\chi$ 是在 $p$ 分歧的三次角色，其温和导子指数恰为一，故对 $C(\chi)$ 的贡献恰为 $p^2$。

此处没有从同一个表示素数上的模 $p$ 同构推断特征零有限惯性相同；所需上界只是准确的二维温和上界。

### 4.3 二、三处的绝对界

联合表示 $(\Sigma,\eta)$ 的像是阶 $24\cdot6=144$ 群的子群。对 $F=H_{\mathfrak q}$、$\mathfrak q\mid6$，取该联合表示切出的局部有限 Galois 扩张 $L/F$，其分歧指数 $e$ 整除 $144$。

设 $G_i$ 为低标号分歧群，$d_{L/F}$ 为不同指数。对任意维数至多二、被 $L$ 平凡化的表示 $V$，

$$
a_F(V)
=\frac1e\sum_{i\ge0}|G_i|\operatorname{codim}V^{G_i}
\le\frac4e\,d_{L/F}.
\tag{275.15}
$$

求和只需保留 $G_i\ne1$；对这些群有 $|G_i|\le2(|G_i|-1)$，而 $d_{L/F}=\sum_i(|G_i|-1)$。

令 $F'$ 为 $L/F$ 的最大不分歧子扩张。$L/F'$ 全分歧，均匀化元的 Eisenstein 最小多项式为 $f(X)$，次数为 $e$。$f'$ 的不同项在 $L$ 中的赋值具有不同的模 $e$ 余数，所以最低项不能抵消。特别

$$
d_{L/F}=v_L(f'(\varpi_L))
\le v_L(e\varpi_L^{e-1})
=e\,v_F(e)+e-1.
\tag{275.16}
$$

在二处，$H_2/\mathbb Q_2$ 不分歧且 $v_2(e)\le4$；在三处，$H_3/\mathbb Q_3$ 分歧指数为二且 $v_3(e)\le2$。故两处均有 $v_F(e)\le4$，由 (275.15)–(275.16) 得 $a_F(V)<20$（无分歧时为零）。

于是可以保守地对 $\tau,\chi$ 都使用二、三处指数至多二十。除固定的判别式和阿基米德因子外，

$$
N\mathfrak f_\tau\le4^{20}3^{20}p^4(c^{(6)})^2,\qquad
N\mathfrak f_\chi\le4^{20}3^{20}p^2(c^{(6)})^2.
$$

这证明 (275.13)。使用如此粗的固定常数是为了完整控制变化局部类型；它不改变任何增长指数。

## 5. 整数迹及共同商域强迫全部小 Euler 因子相同

令 $\mathcal B$ 为 $H$ 中所有位于有理素数 $q\mid6pc$ 上方的素理想，置

$$
F_-(s)=L^{\mathcal B}(s,\Pi),\qquad
F_+(s)=\zeta_H^{\mathcal B}(s)L^{\mathcal B}(s,\chi).
\tag{275.17}
$$

上标表示删除这些地方的全部局部因子。

若 $q\nmid6pc$ 且 $q<p^2/16$，实际模 $p$ 同构及 Hasse 界给

$$
a_q(E_0)\equiv a_q(A)\pmod p,\qquad
|a_q(E_0)-a_q(A)|\le4\sqrt q<p,
$$

所以

$$a_q(E_0)=a_q(A)\quad\text{作为整数}. \tag{275.18}$$

现在分两种分裂类型，逐项证明完整复 Euler 多项式相同。

**$q$ 在 $H$ 分裂。** 此时两条自然三挠点 Frobenius 都在 $\operatorname{SL}_2(\mathbb F_3)$。由 (275.6)，它们同时属于 $Q_8$ 或同时不属于 $Q_8$。

若它们属于 $Q_8$，则 $A$ 的 Frobenius 同时属于循环六阶中心化子，其与 $Q_8$ 的交为 $\{\pm I\}$。故 $A$ 的自然模三迹非零；(275.18) 使 $E_0$ 的模三迹相同，从表中可知 $E_0$ 的 Frobenius 必为同一个 $\pm I$。两条复迹相同。

若它们不属于 $Q_8$，则两边均为阶三或六元，且 (275.18) 的模三迹准确区分这两个阶数。由表格，两条复迹仍相同。

复行列式均为一。因此对每个 $\mathfrak q\mid q$，$\Sigma(\operatorname{Frob}_{\mathfrak q})$ 与 $(\eta\oplus\eta^{-1})(\operatorname{Frob}_{\mathfrak q})$ 的复特征多项式完全相同。乘以 $\eta(\mathfrak q)^{-1}$ 后，$\tau$ 的特征多项式正是

$$
(1-T)(1-\chi(\mathfrak q)T).
\tag{275.19}
$$

**$q$ 在 $H$ 惰性。** 对三次 CM 曲线 $A$ 有 $a_q(A)=0$。这也可直接数点：$q\equiv2\pmod3$ 时 $x\mapsto x^3$ 是 $\mathbb F_q$ 的置换，所以 $\sum_x(\frac{x^3+d}{q})=0$。由 (275.18)，$a_q(E_0)=0$。

两条自然模三 Frobenius 的迹为零、行列式为 $q\equiv-1\pmod3$，故由 Cayley–Hamilton 定理，其平方都是 $I$。$H$ 中唯一素理想的 Frobenius 正是有理 Frobenius 的平方，所以 $\Sigma$ 及 $\eta\oplus\eta^{-1}$ 在该 Frobenius 上都是恒等。因而两侧局部多项式都等于 $(1-T)^2$，仍与 (275.19) 一致。

取

$$X=p^2/32. \tag{275.20}$$

每个范数至多 $X$、且不在 $\mathcal B$ 中的素理想所对应有理素数都满足 $q<p^2/16$。因此 $F_-$、$F_+$ 对所有范数至多 $X$ 的理想都有完全相同的 Dirichlet 系数。这个断言包括素理想幂；只比较一次项是不够的，而 (275.19) 已比较完整二次多项式。

## 6. 保留中央角色的两个次凸指数

Wu 的 Theorem 1.1 与 Remark 1.3 对任意固定数域给

$$
|L(1/2,\pi)|
\ll_{H,u}
C(\pi)^{1/4+u}
\left(\frac{C(\pi)}{C(\omega_\pi)}\right)^{-\alpha}
C(\omega_\pi)^{-\beta},
\tag{275.21}
$$

其中使用无条件可取的 $\theta=7/64$、$A=5/4$、$\delta'=(1-2\theta)/8$，得到

$$
\alpha=\frac{1-2\theta}{80}=\frac5{512},\qquad
\beta=\frac{1-2\theta}{320}=\frac5{2048}.
\tag{275.22}
$$

(275.21) 中相邻各因子相乘。该公式也可无歧义地写成

$$
|L(1/2,\pi)|
\ll_{H,u}C(\pi)^{1/4-\alpha+u}
C(\omega_\pi)^{\alpha-\beta}.
\tag{275.23}
$$

这里 $\alpha-\beta>0$；故 (275.13) 的两个上界都可以代入。中央角色较小的 $p$ 指数必须保留，若仅以一个共同上界替换，会丢失本结论的一部分指数。

对 $\pi=\Pi\otimes|\cdot|^{it}$ 应用该定理。其中央角色为 $\chi|\cdot|^{2it}$。因为 $[H:\mathbb Q]=2$ 且原有限阶表示的无限型固定，

$$
C(\Pi\otimes|\cdot|^{it})\ll p^4c^2(1+|t|)^4,\qquad
C(\chi|\cdot|^{2it})\ll p^2c^2(1+|t|)^2.
$$

从而，在将任意小的 $u$ 重新命名后，

$$
|L(1/2+it,\Pi)|
\ll_u
p^{1-2\alpha-2\beta+u}
c^{1/2-2\beta+u}(1+|t|)^{1+u}.
\tag{275.24}
$$

我们只需 $0<u<1$。Wu 在 §4.1.2 及附录 §6.3 的 Eisenstein 项使用 Siegel 下界。因此这里只使用已证明的统一估计，不从该文标题或“显式指数”推出隐含常数的有效性。

对 $F_+$，R251 已使用的固定域 GL(1) Burgess 界及固定 $\zeta_H$ 的凸性界给

$$
|\zeta_H(1/2+it)L(1/2+it,\chi)|
\ll_u
(pc)^{3/8+u}(1+|t|)^{1+u}.
\tag{275.25}
$$

由于 $1-2\alpha-2\beta>3/8$ 且 $1/2-2\beta>3/8$，(275.24) 的导子部分同时控制 (275.25)。

## 7. 删除坏因子、非零留数和紧支撑移线

有

$$\prod_{\mathfrak q\in\mathcal B}N\mathfrak q\le(6pc)^2. \tag{275.26}$$

每个被删除的局部因子对应一个次数至多二、根的绝对值至多一的 Euler 多项式。因所有参数来自有限像 Artin 表示，这个界也包括分歧处不变量上的 Frobenius。

在 $\Re s\ge1/2$ 上，这些有限乘子的总绝对值为

$$
\ll_u(pc)^u.
\tag{275.27}
$$

证明如下：对足够大的范数 $n$，$(1+n^{-1/2})^2\le n^{u/2}$；固定底域只有有限个较小范数的素理想，它们给固定常数。再用 (275.26)。若需更小的总指数，只先把这里的 $u$ 缩小。

$F_-$ 整；$F_+$ 在 $s=1$ 有一个简单极点，留数

$$
\mathcal R=
\operatorname{Res}_{s=1}\zeta_H(s)\,L(1,\chi)
\prod_{\mathfrak q\in\mathcal B}
\left(1-\frac1{N\mathfrak q}\right)
\left(1-\frac{\chi(\mathfrak q)}{N\mathfrak q}\right).
\tag{275.28}
$$

在分歧处取 $\chi(\mathfrak q)=0$。该留数可能是复数，证明不要求其为正。$\chi$ 是非实三次角色，R251、R261 已证明的非实角色一处下界给

$$|L(1,\chi)|\gg_u C(\chi)^{-u}.$$

同时

$$
\left|\prod_{\mathfrak q\in\mathcal B}
\left(1-\frac1{N\mathfrak q}\right)
\left(1-\frac{\chi(\mathfrak q)}{N\mathfrak q}\right)\right|
\ge\prod_{\mathfrak q\in\mathcal B}
\left(1-\frac1{N\mathfrak q}\right)^2
\gg_u(pc)^{-u}.
$$

结合 (275.13)，重命名 $u$ 后得

$$|\mathcal R|\gg_u(pc)^{-u}. \tag{275.29}$$

选紧支撑权

$$
w(x)=(1-x)^8\quad(0\le x\le1),\qquad
\widehat w(s)=\frac{8!}{s(s+1)\cdots(s+8)},\quad
\widehat w(1)=\frac19.
$$

设 $S_\pm(X)$ 为 $F_\pm$ 的理想系数乘以 $w(N\mathfrak a/X)$ 后求和。第 5 节说明

$$S_-(X)=S_+(X),\qquad X=p^2/32. \tag{275.30}$$

从 $\Re s=2$ 移到 $\Re s=1/2$。由 (275.24)–(275.27)，$\widehat w(s)$ 的九次衰减充分吸收全部竖线增长；横边沿标准截断序列趋于零。得到

$$
S_-(X)
=O_u\!\left(
p^{1-2\alpha-2\beta+u}
c^{1/2-2\beta+u}X^{1/2}
\right),
$$

$$
S_+(X)
=\frac{\mathcal RX}{9}
+O_u\!\left(
p^{1-2\alpha-2\beta+u}
c^{1/2-2\beta+u}X^{1/2}
\right).
\tag{275.31}
$$

相减并取绝对值，使用 (275.29)–(275.30)，再适当扩大任意小的 $u$，可得

$$
p^{2\alpha+2\beta-u}
\ll_u c^{1/2-2\beta+u}.
\tag{275.32}
$$

这里主项为复数不造成困难：左侧使用的是非零留数的绝对值，没有把复系数当作正系数。

令 $u$ 趋向零，极限幂指数是

$$
\frac{2\alpha+2\beta}{1/2-2\beta}
=\frac{4(\alpha+\beta)}{1-4\beta}
=\frac{25}{507}.
\tag{275.33}
$$

准确地说，对任意给定 $\epsilon>0$，选足够小的正 $u$，(275.32) 蕴含 (275.1)。结合第 1 节的异域情形，定理在整个 $\sigma=1$、整 $j$、无 CM 分支成立。证毕。

## 8. 得到的范围与下一缺口

1. 对每个固定实数 $B>0$，该完整分支中所有 $c\le B$ 的坏像素数 $p$ 都有只依赖 $B$ 的上界。这一存在性推论不要求把共同三次曲线的全部有理点逐个求出。
2. 特别，R266 的 $c=9$ 同域族不能产生 $p\to\infty$ 序列；本篇未证明它在每个 $p>37$ 都无解。
3. R266 的 $c=6$ 有效排除与其精确小方程结论保留原有强度；本文不借助非有效估计改写那里的结论。
4. 尚缺与 (275.1) 相冲突的实际 $c$ 上界，或对变化的大 $c$ 的独立排除。本篇没有把固定底域 $H$ 偷换为固定 CM 曲线，也没有固定变化参数 $d$。

## 来源与产物

- R258：同一实际表示的六次 CM 下降、正立方自由标准形和全部坏素数支撑；R261：实际三挠点 $S_3$ 商域二择一；R251：固定域紧支撑 Euler 比较和非实三次角色的一处下界。
- P. Lemos，*Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*，Trans. Amer. Math. Soc. **371** (2019)，Theorem 1.1，DOI [10.1090/tran/7198](https://doi.org/10.1090/tran/7198)，[作者稿](https://arxiv.org/pdf/1702.01985)，第 2 页。
- A. Wiles，*Modular elliptic curves and Fermat's Last Theorem*，Ann. of Math. **141** (1995), 443–551，[原文 PDF](https://wstein.org/edu/2004/24g/flt.pdf)，第五章 Theorem 5.1 后，印刷页 541–542：$\operatorname{GL}_2(\mathbb F_3)$ 的忠实复提升及约化恒等归一化。
- R. P. Langlands，*Base change for GL(2)*，Annals of Mathematics Studies **96** (1980)，[作者电子版](https://publications.ias.edu/sites/default/files/base-change-for-gl2_rpl_2.pdf)，§3，电子排印页 15–18：该节开头的全部地方匹配、Lemma 3.2 后的结论及 Theorem 3.3 的构造。本文使用任意数域上的四面体尖点性，不使用仅有概括摘要的模性结论。
- H. Wu，*Explicit subconvexity for GL2*，Mathematika **68** (2022), 921–978，DOI [10.1112/mtk.12147](https://doi.org/10.1112/mtk.12147)，[作者稿 arXiv:1812.04391v5](https://arxiv.org/pdf/1812.04391)：Theorem 1.1、Remark 1.3 给 (275.21)–(275.22)；§4.1.2、§6.3 显示证明使用 Siegel 下界，因此本文不声明隐含常数有效。

本篇为纯证明产物，无外部数据、数值扫描或脚本依赖。局部野导子绝对界、模三与复迹的转换、全部小素理想 Euler 多项式、坏因子乘子、非零复留数及指数运算均在正文给出。
