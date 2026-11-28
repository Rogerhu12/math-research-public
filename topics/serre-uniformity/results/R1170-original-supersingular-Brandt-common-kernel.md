# R1170：原同源归一的超奇异 Brandt 格与三个中央算子族的共同核

日期：2026-11-28  
会话：Astra-serre-24b8836b-20261126  
状态：§§1–8 的前两个有限格定理及 §10 的最低槽扩展、整 Hecke 单位理想已证明。原候选中央差的仿射有限化另见 R1171；实际右端与辅助族仍须按其来源使用。本文没有执行数学计算。

## 1. 结论与准确范围

设 $p>37$，$\mathscr S_p$ 是 $\overline{\mathbb F}_p$ 上椭圆曲线的超奇异同构类集合。对 $d=12,8$，取完整系数空间
$$
\overline{\mathcal B}_d=
\bigoplus_{[E]\in\mathscr S_p}
\bigl(\operatorname{Sym}^d H^1_{\mathrm{dR}}(E/\overline{\mathbb F}_p)\bigr)^{\operatorname{Aut}(E)}.
\tag{1170.1}
$$
这里是完整秩二 de Rham 空间的对称幂，不是单一 Hodge 分次。原定向的素数次同源为
$$
\phi_C:E\longrightarrow E/C,\qquad
\psi_C^{-1}=\ell^{-1}\phi_C^*.
\tag{1170.2}
$$
第二式沿用 [R1159 §5](R1159-original-correlation-to-Hecke-cochain-comparison.md) 的 pointed coefficient 运输。定义
$$
T_\ell^{(d)}f(E)=
\sum_{\substack{C\subset E[\ell]\\ |C|=\ell}}
\operatorname{Sym}^d(\psi_C^{-1})f(E/C)
\qquad(\ell\ne p).
\tag{1170.3}
$$
各商同构回代表元时由自同构不变量消除选择；每个循环子群计一次。

**定理。** 对任意有限素数集合 $\Sigma$，$p\in\Sigma$，有
$$
\bigcap_{\ell\notin\Sigma}
\ker\bigl((\ell^4+\ell^{-11})-\ell^2T_\ell^{(12)}\bigr)=0,
\tag{1170.4}
$$
以及
$$
\bigcap_{\ell\notin\Sigma}
\ker\bigl((\ell^4+\ell^{-11})-T_\ell^{(8)}\bigr)=0.
\tag{1170.5}
$$
所有负幂均在 $\mathbb Z_p^\times$ 或其剩余域内解释。更强地，在下文真实有限自由格的 Hecke 整序中，相应算子生成单位理想；因此存在只用有限多个 $\ell\notin\Sigma$ 的 Hecke 线性组合等于恒等算子。

(1170.4) 精确对应原最高 $\Pi_0$ 中央运输；(1170.5) 对应保留两次 Weil 收缩后的 $\Pi_2$ 运输。定理不声称这些有限多个素数可以都取 $\ell<p$，也不声称只用 $2,5$ 已足够。

## 2. 实际有限自由格，不假定模 $p$ 特征系统可提升

取有限域 $k/\mathbb F_p$，使所有代表 $E_i$ 及它们两两之间的全部几何同态都定义在 $k$ 上。这样的 $k$ 存在：代表只有有限个，每个 $\operatorname{Hom}(E_i,E_j)$ 是有限生成的 $\mathbb Z$-模，只须同时定义有限组生成元。必要时扩大 $k$。令
$$
W=W(k),\qquad D_i=H^1_{\mathrm{crys}}(E_i/W),\qquad
\mathcal B_d=\bigoplus_i(\operatorname{Sym}^d D_i)^{\operatorname{Aut}(E_i)}.
\tag{1170.6}
$$
$D_i$ 是秩二自由 $W$-模。$p>3$ 时自同构群的阶只含 $2,3$，故平均投影是整的，$\mathcal B_d$ 有限自由，而且取不变量与模 $p$ 约化交换。晶体—de Rham 比较给
$$
(\mathcal B_d/p)\otimes_k\overline{\mathbb F}_p
\simeq\overline{\mathcal B}_d.
\tag{1170.7}
$$

定义真实整算子
$$
B_\ell f(E)=\sum_{|C|=\ell}\operatorname{Sym}^d(\phi_C^*)f(E/C).
\tag{1170.8}
$$
由 $\widehat\phi_C\phi_C=[\ell]$，$\phi_C^*$ 在 $D_i$ 上是整同构。式 (1170.2) 逐项给出
$$
B_\ell=\ell^d T_\ell^{(d)}.
\tag{1170.9}
$$
没有除以 $\ell+1$，没有额外的自同构平均，也没有把 $\phi^*$ 与其倒向混用。

以下证明提升的是这个具体格的 Hecke 整序的特征系统。它不要求 $\mathcal B_d/p$ 半单，也不从一个抽象残余伪特征先假定存在特征零模形式。

## 3. 标准 Brandt 归一与经典权

Deuring 对应把 $\mathscr S_p$ 及其同态范畴送到判别式为 $p$ 的定四元数代数的极大整序理想类。所用精确来源是 Voight《Quaternion Algebras》第 42 章：定理 42.1.9、引理 42.1.11、定理 42.3.2、推论 42.3.7，以及 42.3.13 的子群计数描述。[来源 1]

还必须核系数方向。固定一个超奇异曲线 $E_*$，令 $B=\operatorname{End}^0(E_*)$。拉回给出右作用
$$
v\cdot b=b^*v.
\tag{1170.10}
$$
由于 $(bc)^*=c^*b^*$，这是右作用而非未经修正的左标准作用。在一个分裂域中，二维忠实反表示与
$$
b\longmapsto\operatorname{adj}(\iota(b))
\tag{1170.11}
$$
共轭：先用四元数标准反自同构把反表示变成表示，再用分裂矩阵代数的内自同构性。因而 $\operatorname{Sym}^dD_*$ 的右作用恰是 Dembélé–Voight §7 的
$$
P(X,Y)\cdot b=P\bigl((X,Y)\operatorname{adj}(\iota(b))\bigr).
\tag{1170.12}
$$
在底域 $\mathbb Q$、经典权 $d+2$ 的情形，其式 (7.3) 的额外行列式扭转指数为零。标量 $a$ 在两边都作用为 $a^d$。

把各代表通过实际同源识别到理想类后，(1170.8) 的每个拉回就是该右系数作用的相应理想邻接项。Dembélé–Voight 的 (7.14)–(7.15) 在函数变量中使用逆陪集，(7.20)–(7.22) 把它运输为右系数作用；其 (7.27) 正是各理想类稳定子的系数不变量。故 (1170.8) 是通常、未除 $\ell+1$ 的 Brandt 算子，而非它再扭一次行列式的版本。[来源 2]

这里 $d>0$，定四元数模形式的 Eisenstein 部分为零。由该文定理 7.28，
$$
\mathcal B_d[1/p]
\quad\text{的 Hecke 特征系统全部来自}\quad
S_{d+2}(\Gamma_0(p))^{p\text{-new}}.
\tag{1170.13}
$$
可先扩大系数域再比较；不变量格的整结构仍取 (1170.6)。这些经典新形式有平凡 nebentype，标准 Galois 规范是
$$
\operatorname{tr}\rho_f(\operatorname{Frob}_\ell)=a_\ell(f),
\qquad
\det\rho_f(\operatorname{Frob}_\ell)=\ell^{d+1}.
\tag{1170.14}
$$
本文用算术 Frobenius，$\omega(\operatorname{Frob}_\ell)=\ell\bmod p$。若从采用几何 Frobenius 的上同调表示出发，取其对偶即得到 (1170.14)；后面的惯性权也在同一对偶规范中使用。

## 4. 有限整序中的残余提升引理

令
$$
\mathbb T_{d,\Sigma}
=W[B_\ell:\ell\notin\Sigma]
\subset\operatorname{End}_W(\mathcal B_d).
\tag{1170.15}
$$
它是有限无挠 $W$-代数：作为有限自由模的自同态代数的 $W$-子模，它有限生成；$p$ 非零因子。其特征零谱由 (1170.13) 中实际出现的特征系统组成。

设 $\mathfrak m$ 是 $\mathbb T_{d,\Sigma}$ 的极大理想。有限整扩张使 $\mathfrak m\cap W=(p)$。取包含于 $\mathfrak m$ 的极小素理想 $\mathfrak q$。因为 $p$ 非零因子，$\mathfrak q$ 不含 $p$；所以 $\mathfrak q$ 给出特征零分支，而不是仅在特殊纤维出现的分支。归一化该分支并在 $\mathfrak m$ 之上取素理想，得到一个实际出现的新形式 $f$ 和系数素理想 $\mathfrak p\mid p$，其 Hecke 特征约化为 $\mathbb T_{d,\Sigma}/\mathfrak m$ 的指定特征。

这一步只用具体有限无挠 Hecke 整序。即使原模 $p$ 作用有非平凡 Jordan 块，结论仍成立。

若一个算子理想不是单位理想，它包含于某个这样的 $\mathfrak m$。于是只须证明指定残余特征不能出现在 (1170.13) 的任何新形式上。

## 5. 同一素数处的半稳定惯性界

权 $d+2$、级别 $p$ 的 $p$-new 形式在 $p$ 处是未分歧扭转的 Steinberg。Saito 的 $p$-进局部—整体相容性给出其 Galois 表示的潜在半稳定性及相同的 Weil–Deligne 参数；该参数的惯性平凡，因此表示已在 $\mathbb Q_p$ 上半稳定，不须先进入有分歧基域。[来源 3]

在 (1170.14) 的对偶规范中，Hodge–Tate 权为 $0,d+1$，即 Caruso 所用的非负权规范。Caruso 的定理 1.0.3–1.0.5 给出：若 $r<p-1$，$\mathbb Q_p$ 上权在 $[0,r]$ 的半稳定表示的任意稳定整格，其模 $p$ 剩余表示的半单惯性权都在
$$
0\le a\le r.
\tag{1170.16}
$$
此处绝对分歧指数是基域 $\mathbb Q_p$ 的 $1$，不是新形式系数域的分歧指数。[来源 4]

若系数整数环在 $p$ 处分歧，先把稳定格限制标量为 $\mathbb Z_p$-格，再应用该定理；模系数极大理想的表示是模 $p$ 表示的子商。Caruso 的精确性及子商封闭性保留同一界。因此不能借系数域分歧绕过 (1170.16)。

对本稿两个权，分别取
$$
(d,r)=(12,13),\qquad (8,9),
\tag{1170.17}
$$
均满足 $r<p-1$。下文出现的剩余角色都是一级基本字符 $\omega$ 的幂；其惯性权采用 $0,\ldots,p-2$ 的代表。

## 6. 最高中央算子：权 14 的矛盾

由 (1170.9)，最高算子是
$$
V_{\ell,0}
=(\ell^4+\ell^{-11})-\ell^2T_\ell^{(12)}
=\ell^{-10}\bigl(\ell^{14}+\ell^{-1}-B_\ell\bigr).
\tag{1170.18}
$$
若所有 $V_{\ell,0}$ 生成的理想真包含于 $\mathfrak m$，§4 给出实际权 14、级别 $p$ 的新形式，使
$$
a_\ell(f)\equiv\ell^{14}+\ell^{-1}\pmod{\mathfrak p}
\quad(\ell\notin\Sigma).
\tag{1170.19}
$$
行列式为 $\omega^{13}$。Chebotarev 及二维剩余特征多项式的唯一性给
$$
\overline\rho_f^{\,\mathrm{ss}}
\simeq\omega^{14}\oplus\omega^{-1}.
\tag{1170.20}
$$
删去任意固定有限素数集合不影响此结论。因 $p>37$，两个惯性权的标准代表是 $14,p-2$，均超出半稳定权 14 形式所允许的 $[0,13]$。这与 (1170.16) 矛盾。

故
$$
(V_{\ell,0}:\ell\notin\Sigma)=\mathbb T_{12,\Sigma}.
\tag{1170.21}
$$
存在有限个 $\ell_i\notin\Sigma$ 和 $A_i\in\mathbb T_{12,\Sigma}$ 满足 $\sum_iA_iV_{\ell_i,0}=1$。约化及扩域后即得 (1170.4)。

## 7. 两次 Weil 收缩：权 10 的矛盾

这一步保留 [R1169](R1169-original-second-central-correlation-and-Frobenius.md) 已付的真实原群及 Tate 尺度。对 $\ell$ 次同源，$\psi_C^{-1}=\ell^{-1}\phi_C^*$ 使每次 Weil 配对乘 $\ell^{-1}$。$\Pi_2$ 含两次配对，因此其中央传递为
$$
\ell^{-2}\operatorname{Sym}^8(\psi_C^{-1});
\tag{1170.22}
$$
原中央外部 Tate 因子未再次变换。原功能方程外部的 $\ell^2$ 与 (1170.22) 抵消，所以其正确算子恰为 (1170.5)，不是最高算子的 $\ell^2T_\ell^{(8)}$。

归一后
$$
V_{\ell,2}
=(\ell^4+\ell^{-11})-T_\ell^{(8)}
=\ell^{-8}\bigl(\ell^{12}+\ell^{-3}-B_\ell\bigr).
\tag{1170.23}
$$
若该族不生成单位理想，同样提升到权 10、级别 $p$ 的实际新形式，得到
$$
\overline\rho_f^{\,\mathrm{ss}}
\simeq\omega^{12}\oplus\omega^{-3},
\qquad
\det\overline\rho_f=\omega^9.
\tag{1170.24}
$$
两个惯性权为 $12,p-4$，均超出允许的 $[0,9]$。故
$$
(V_{\ell,2}:\ell\notin\Sigma)=\mathbb T_{8,\Sigma},
\tag{1170.25}
$$
从而 (1170.5) 成立。此段给出所写 $\Pi_2$ 系数算子族的格定理；不以它替代该槽实际原余链的构造或数值读取。

## 8. 如何接原功能方程，以及尚未付款的两处接口

[R1159 §5](R1159-original-correlation-to-Hecke-cochain-comparison.md) 给出的最高真实恒等式是
$$
Z_{\mathrm{corr},n}(E)
=(n^4+n^{-11})Z_0(E)
-n^2\sum_C\operatorname{Sym}^{12}(\psi_C^{-1})Z_0(E/C).
\tag{1170.26}
$$
[R1168](R1168-original-unramified-PD-contraction-and-CM-moment-readout.md) 已给原相关项所需的实际双线性读数。这些等式与本文有限格之间，还需以下两个独立输入。

第一，必须把待解量真正化成 (1170.1) 的元素。不能直接把原 $Z_0$ 宣称为只依赖超奇异约化的函数。[R1149 §14、式 (1149.38)–(1149.40)](R1149-original-relative-Hodge-section-and-central-connection.md) 的实际 $F_t=F_0\Delta(t)$ 已显示一般提升的依赖；其相对前提由该文 §16 接 R1150 支付。若 $A_*B_*\ne0$，同一整基中最高 $\nu^{12}$ 系数满足
$$
[\nu^{12}]\Delta Z_0=\frac{\lambda^2A_*B_*}{70}s^{14},
\qquad
[\nu^{12}]\Delta Z_0^{\mathrm{BCH}}
=\frac{\lambda^2A_*B_*}{315}s^{14}.
\tag{1170.27}
$$
第一式直接积分 $(v^5/5)v^8$；第二式再减 $\tfrac12(s^5/5)(s^9/9)$。参考 $F_0$ 的 cross 项次数至多九，不能消掉十四次项；$14<p$。因此绝对的约化不变性在该一般分支确实不成立，不能把它列为一个可直接假定的输入。

真正可能使用本文的对象是固定同一原 abelian 数据后的中央差，或选择参考提升并把完整 $\Delta(t)$ 与 cross 项加入右端所得到的有限常数向量。这仍须分别证明跨全部实际同源的系数、$\sigma$、参考点和 affine 平移相容；本文没有把这一改写冒称已经完成。某个 CM 提升上的 $F_0$ 可定义、点上 Fontaine–Laffaille 格存在，均不能单独替代这个步骤。

第二，本文的单位理想使用一个余有限的素数族。R1157–R1158 的原 raw 源先在 $3<n<p$ 建立，$n=2$ 另行付清；不能由这些有限小素数自动推得 (1170.21)。若要用任意 $\ell\ne p$，须另证实际 Norm 群图、同根运输和相应功能方程在 $\ell\ge p$ 也成立，或给出一个已实际构造且生成单位理想的有限素数集。尤其不能在辅助分裂域次数含 $p$ 时沿用反除该次数的旧 raw 步骤。仅有 $n=2,5$ 的原方程不被本文宣称足够。

一旦待解中央差或相应参考常数向量的有限格实现、以及所需素数族都已证明，两个满足同一右端方程的完整有限系数函数之差落在本文共同核，因而必相等。这提供真实的唯一性／重建入口。方程是非齐次的，故即使两输入完成，也不是令 $Z_0=0$。本文不计算尚未读取的一般算术 Frobenius 共轭路径，不把共同核定理升级为原盘排除或一般 $p$ 的主目标完成。

## 9. 已亲读的 primary 与精确使用位置

1. John Voight, *Quaternion Algebras*, GTM 288, Springer, 2021，第 42 章，页 783–797。本文使用定理 42.1.9、引理 42.1.11、定理 42.3.2、推论 42.3.7、42.3.13。  
   [作者著作的出版社开放章节](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)，DOI 10.1007/978-3-030-56694-4_42。已读章节正文；没有把超出网页读取限制的整本 PDF 冒称读完。

2. Lassina Dembélé and John Voight, *Explicit methods for Hilbert modular forms*, 2013 年书章；使用作者更新稿 §7 的 (7.3)、(7.14)–(7.15)、(7.20)–(7.22)、(7.27)、定理 7.28，以及权大于 2 时定四元数 Eisenstein 部为零的段落。当前作者 PDF 的相应位置为第 35–43 页。  
   [作者 PDF](https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf)，[arXiv:1010.5727](https://arxiv.org/abs/1010.5727)。已亲读上述系数作用、陪集方向及定理，未只凭“Brandt”名称指定归一。

3. Takeshi Saito, *Modular forms and p-adic Hodge theory*, Invent. Math. 129 (1997), 607–620，DOI [10.1007/s002220050175](https://doi.org/10.1007/s002220050175)。本文实际亲读的是作者在 *Galois representations in arithmetic geometry* §2c、定理 3（作者 PDF 第 9 页）对其原文 [S7] 的重述及其前后潜在半稳定性说明，并结合 §2a 的权。  
   [作者该文 PDF](https://www.ms.u-tokyo.ac.jp/~t-saito/pp/suams.pdf)，[作者出版目录](https://www.ms.u-tokyo.ac.jp/~t-saito/publ.html)。1997 年出版社全文本次受访问限制，未声称重新全文读取；所用相容性结论在上述作者原文中完整显示。

4. Xavier Caruso, *Représentations semi-stables de torsion dans le cas $er<p-1$*, J. reine angew. Math. 594 (2006), 35–92，DOI 10.1515/CRELLE.2006.035。使用定理 1.0.3 的惯性权、1.0.4 的精确性及子商封闭、1.0.5 的所有稳定格接口。  
   [作者完整原文 PDF](https://xavier.caruso.ovh/papers/publis/smaller.pdf)，[作者出版页](https://xavier.caruso.ovh/papers/publis/galois.html)。三个定理在该作者稿 PDF 第 3–4 页，已逐项亲读。本文基域始终 $\mathbb Q_p$，故使用 $e=1$，没有把系数域分歧指数代入。

本结果的新增部分是：原倒向同源的精确 $\ell^{12}$／$\ell^8$ 归一、实际整序的残余提升，以及两个目标算子族的无条件单位理想。其应用范围以 §8 为准。


## 10. 最低中央槽的原系数算子也生成单位理想

[R1172](R1172-original-lowest-central-Tate-correlation-and-unsmoothing.md) 已支付原最低槽的完整 Tate 运输。四次 Weil 收缩要求中心 map 为
$$
\ell^{-4}\operatorname{Sym}^4(\psi_C^{-1});
$$
原 product 的外部 $\ell^2$ 因此留下 $\ell^{-2}$。相应有限格算子为
$$
V_{\ell,4}=(\ell^4+\ell^{-11})-\ell^{-2}T_\ell^{(4)}.
\tag{1170.28}
$$
取 (1170.6) 的同一个实际晶体构造、令 $d=4$，得到 $\mathcal B_4$；其 $\bmod p$ 扩域仍为完整 $\operatorname{Sym}^4H^1_{\rm dR}$ 的自同构不变量。§3 的实际 coefficient 方向给
$$
B_\ell=\ell^4T_\ell^{(4)},\qquad
V_{\ell,4}=\ell^{-6}
  \bigl(\ell^{10}+\ell^{-5}-B_\ell\bigr).
\tag{1170.29}
$$
因此它的特征零系统来自权 $6$、级别 $p$ 的 $p$-new 形式，标准 Galois 行列式为 $\chi^5$。

对任意含 $p$ 的有限素数集 $\Sigma$，令
$$
\mathbb T_{4,\Sigma}=W[B_\ell:\ell\notin\Sigma].
$$
若 $(V_{\ell,4}:\ell\notin\Sigma)$ 不为单位理想，§4 在这一具体有限无挠整序中给实际新形式和系数素理想，使
$$
a_\ell\equiv\ell^{10}+\ell^{-5}\pmod{\mathfrak p}
\qquad(\ell\notin\Sigma).
$$
由 Chebotarev 和相同的行列式，
$$
\overline\rho^{\,\rm ss}\simeq\omega^{10}\oplus\omega^{-5}.
$$
Saito 的同一相容性给 $\mathbb Q_p$ 上半稳定；Caruso 取 $r=5<p-1$，要求半单惯性权在 $[0,5]$。上述两角色的标准权为 $10,p-6$，在 $p>37$ 时均超界。故
$$
\boxed{\quad
(V_{\ell,4}:\ell\notin\Sigma)=\mathbb T_{4,\Sigma},\qquad
\bigcap_{\ell\notin\Sigma}\ker V_{\ell,4}=0
\quad\text{于 }\overline{\mathcal B}_4.
\quad}
\tag{1170.30}
$$
模 $p$ 作用不必半单，系数域也不必未分歧；§§4–5 的稳定格与子商论证原样适用。

至此三个有限算子族均有单位理想，分别对应实际 $\Pi_0,\Pi_2,\Pi_4$ 的归一。最低相关项还含 R1172 的真实 Tate-five 修正，不能把它改成裸 $\Pi_4$ raw 源。本文的有限格结论也没有把足够多素数的相关项局部值、所有一般 SS 参考点的 abelian 输入或真实 affine 右端认作已经读取；这些是继续使用本式所需的独立输入。

本节仅延长本文已核原来源与 R1172 的实际系数式，没有新增数学程序或数值窗口。
