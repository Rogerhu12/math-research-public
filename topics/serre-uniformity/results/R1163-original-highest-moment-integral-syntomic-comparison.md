# R1163 — 原全部矩系数与指定 primitive 的整 syntomic 比较

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇对同一原 good elliptic fibre 的有限系数，
用实际椭圆曲线乘积及整 projector，把已刊的 scalar log-syntomic
比较准确转成原对称幂系数的比较。所得范围足以运输原两条
abelian cochains、它们的最高 ordered cup，以及
R1158–1160 已指定的最高中央 primitive 的完整 gauge 类。
§§8–10 进一步以实际 paired projectors 和 Poincaré coevaluation，
支付全部三个中央槽、常数补项及原完整四十三格的同一比较。

这里的新输入是**有限整 syntomic complex 与原 étale complex
之间的实际比较**，不只是 rational associatedness。
本篇没有把所得类的一份未知整代表当作已经算出的 PD 矩阵；
R1155 §16、R1162 所需的原 normal coefficients 仍须由同源代表读取。

## 1. 固定原 fibre、系数与小权范围

设 \(p>37\)，\(L/\mathbb Q_p\) 为有限扩张，
\(\mathcal E/\mathcal O_L\) 为原 good elliptic curve，
\(E=\mathcal E_L\)，\(k\) 为 residue field。对最终原
Fontaine–Laffaille 格的应用仍取未分歧底 \(F\)；
这里为了覆盖实际标记域，先允许 \(L\) 分歧。

记
\[
H_n=E[p^n],\qquad
T_{d,t,n}=\operatorname{Sym}^d H_n(t).
\tag{1163.1}
\]
所需 pairs 为
\[
(d,t)=(4,1),(8,1),(12,2),(8,4),(4,6),(0,5).
\tag{1163.2}
\]
其 \(d+t\) 依次为 \(5,9,14,12,10,5\)，都严格小于
\(p-2\)。所有 \(2^d d!\) 都为 \(p\)-单位。
本篇不为任何一条系数线另换 Tate generator 或 Weil 标记。

\(\mathcal X_d=\mathcal E^d\) 带由特殊纤维定义的 log structure，
\(\mathcal Y_d=\mathcal X_d\otimes k\)。
它是 \(\operatorname{Spec}\mathcal O_L\) 带原 vertical log
structure 上的 proper、smooth、fs log scheme。
\(d=0\) 时取底本身。

令 \(\mathcal S_n(r)\) 为 Tsuji 的 log-syntomic complex。
其已刊 Theorem 5.1 和 §2 的实际 period map 给
\[
\alpha_{r,n}:\mathcal S_n(r)_{\mathcal X_d}
 \longrightarrow
 i^*Rj_*\mathbb Z/p^n(r),\qquad
\mathcal S_n(r)_{\mathcal X_d}
 \simeq\tau_{\le r}i^*Rj_*\mathbb Z/p^n(r)
\quad(0\le r\le p-2).
\tag{1163.3}
\]
这里 \(j:E^d\hookrightarrow\mathcal X_d\)、\(i:\mathcal Y_d
\hookrightarrow\mathcal X_d\)，原底的 vertical log 不能删。
尤其 (1163.3) 是精确的整比较，并非仅由某个 \(p^N\)
杀掉 kernel/cokernel 的比较。

## 2. 实际椭圆乘积上的整 signed projector

在 \(\mathcal X_d\) 上，以 \(\iota_a\) 表示第 \(a\) 个因子的
\([-1]\)，以 \(\sigma\in S_d\) 表示实际因子置换。定义
\[
o_d=\prod_{a=1}^d\frac{1-\iota_a^*}{2},\qquad
s_d=\frac1{d!}\sum_{\sigma\in S_d}
             \operatorname{sgn}(\sigma)\sigma^*,\qquad
\epsilon_d=s_do_d .
\tag{1163.4}
\]
\(o_d\) 与所有置换相交换；两者均为 idempotents，故
\(\epsilon_d\) 为整 idempotent。它作用于实际 syntomic、
nearby-cycle 及 étale complexes，(1163.3) 与之相容。

先在 \(\bar L\) 上检查此 projector。
\([-1]^*\) 在 \(H^0(E_{\bar L})\)、\(H^2(E_{\bar L})\)
上为 \(+1\)，在 \(H^1(E_{\bar L})\) 上为 \(-1\)。
因此 \(o_d\) 只留下总 fibre degree \(d\) 的
\(H^1(E_{\bar L})^{\otimes d}\)。

在这一 Künneth summand 上，几何置换 \(\sigma^*\) 自带
degree-one 因子的 Koszul 符号 \(\operatorname{sgn}(\sigma)\)。
所以 (1163.4) 的第二个相同符号准确消去它，
留下通常的 symmetric projector。不能去掉这一个
\(\operatorname{sgn}(\sigma)\)，否则得到的是另一个表示。

用原主极化的 Weil pairing 固定
\[
H_n\xrightarrow{\sim}H^1_{\mathrm{et}}(E_{\bar L},
                    \mathbb Z/p^n)(1).
\tag{1163.5}
\]
具体采用 \(v\mapsto(w\mapsto\langle v,w\rangle)\)，
使第一槽、原固定 Weil frame 与 R1147 (1147.15) 一致。
所有因子都使用这同一 convention。
于是
\[
\boxed{\quad
\epsilon_d R\Gamma_{\mathrm{et}}(E_{\bar L}^{\,d},
                      \mathbb Z/p^n(d+t))
 \simeq T_{d,t,n}[-d].
\quad}
\tag{1163.6}
\]
这是 derived complex 的等式：projector 后只有显示的一项
cohomology，故其 canonical truncation 给 (1163.6)。
不需要选一个未经证明的 integral formality splitting。
有限 étale cohomology 的 Künneth 在这里没有 Tor 余项，
因为椭圆曲线的三个整 cohomology groups 都是自由
\(\mathbb Z_p\) 模；约模 \(p^n\) 后仍与这一计算相容。

(1163.4) 对所有 \(n\) 使用同一整系数，故 (1163.6)
严格与层约化相容，不另选有限标签的 \(T_pE\) lift。

## 3. 截断后的精确系数比较

定义实际 syntomic coefficient complex
\[
C_{d,t,n}^{\mathrm{syn}}
 :=\epsilon_dR\Gamma_{\mathrm{et}}
       (\mathcal Y_d,\mathcal S_n(d+t)_{\mathcal X_d})[d].
\tag{1163.7}
\]
对 (1163.3) 取原 special-fibre étale cohomology，
再用 proper base change 与算术 Hochschild–Serre，
得到自然 map
\[
\boxed{\quad
A_{d,t,n}:C_{d,t,n}^{\mathrm{syn}}
 \longrightarrow R\Gamma(G_L,T_{d,t,n}).
\quad}
\tag{1163.8}
\]

这里说明算术基的使用，以免将 geometric 与 arithmetic
cohomology 混同。在严格 henselian 基变换上，
proper nearby-cycle 比较给
\[
R\Gamma(\mathcal Y_{d,\bar k},
          i^*Rj_*\mathbb Z/p^n(d+t))
 \simeq
 R\Gamma(I_L,R\Gamma(E_{\bar L}^{\,d},
                           \mathbb Z/p^n(d+t))).
\]
再对 \(G_k=G_L/I_L\) 取 continuous cohomology，
由 Hochschild–Serre 得到完整 \(G_L\) cohomology。
随后使用 (1163.6)；没有只在 geometric fibre 取 invariants
而漏掉 residue-field Frobenius。

(1163.3) 的 cone 位于 sheaf degrees \(\ge d+t+1\)。
\(R\Gamma(\mathcal Y_d,-)\) 不会把这个下界降低，
整 projector 也不会降低它；最后的 shift \([d]\)
把下界准确改成 \(t+1\)。故
\[
\boxed{\qquad
H^q(A_{d,t,n})\text{ 是同构，对每个 }q\le t.
\qquad}
\tag{1163.9}
\]
顶端 \(q=t\) 包含在内。由 cone 的长正合序列，
它同时给 \(H^{t+1}\) 的单射；本篇不需要也不宣称更高次数满射。

原输入的有效范围如下：

| 原系数 | \(d+t\) | 本篇精确覆盖的非负 cohomology degrees |
|---|---:|---|
| \(\operatorname{Sym}^4H_n(1)\) | 5 | \(0,1\) |
| \(\operatorname{Sym}^8H_n(1)\) | 9 | \(0,1\) |
| \(\operatorname{Sym}^{12}H_n(2)\) | 14 | \(0,1,2\) |
| \(\operatorname{Sym}^{8}H_n(4)\) | 12 | \(0,1,2,3,4\) |
| \(\operatorname{Sym}^{4}H_n(6)\) | 10 | \(0,1,\ldots,6\) |
| \(\mathbb Z/p^n(5)\) | 5 | \(0,1,\ldots,5\) |

特别，原最高中央 cup 的 obstruction degree 二没有超出
比较范围。此结论直接来自真正 scalar small-weight theorem，
不借一个未刊的 relative-coefficient essential-surjectivity 命题。

## 4. 原最高 ordered cup 的全部乘法尺度

Tsuji §2 (2.5) 的 product 和 (2.8) 的 period morphism
相容。对两个实际 projections
\(\mathcal E^{12}\to\mathcal E^4,\mathcal E^8\)，
先拉回、再取 product、最后施 \(\epsilon_{12}\)，得到
\[
C_{4,1,n}^{\mathrm{syn}}
 \mathbin{\otimes^{\mathbf L}}
C_{8,1,n}^{\mathrm{syn}}
 \longrightarrow C_{12,2,n}^{\mathrm{syn}}.
\tag{1163.10}
\]
syntomic weights 相加为 \(5+9=14<p-2\)。
degree shifts \(4,8\) 都为偶数，故这里没有额外的 shift 负号。

检查 (1163.10) 在原 fibre coefficients 上的归一。
把 ordinary symmetric power 识别为 tensors 中
\((1/d!)\sum_{\sigma}\sigma\) 的像；
\(\epsilon_{12}\) 施于已对前四和后八因子分别对称化的
tensor，正是对全部十二因子对称化。
在 symmetric coinvariants 中它仍映到同一个单项式。
因此其 coefficient map 准确是
\[
\Pi_0:\operatorname{Sym}^4H_n(1)
 \otimes\operatorname{Sym}^8H_n(1)
 \longrightarrow\operatorname{Sym}^{12}H_n(2),\qquad
v^4\otimes w^8\longmapsto v^4w^8.
\tag{1163.11}
\]
它就是 R1144 (1144.21)、R1147 (1147.11) 的原
\(\Pi_0\)，没有多一个 \(\binom{12}{4}\)、\(12!\) 或 \(1/2\)。

整个比较 diagram 与此 bilinear map 相容，
所以同一 syntomic representatives \(a,b\) 的
ordered cup \(a\cup b\) 被送到原 ordered étale cup。
本篇未将它改成反对称 bracket，也未删除有序群律中的交叉项。
此处只需最高 product，不以一个尚未在原规范中校准的
Gysin contraction 代替低两个 \(\Pi_2,\Pi_4\)。

## 5. 固定原 primitive 的 integral syntomic gauge 类

固定 \(n\)，令 \(a_{\mathrm{et}},b_{\mathrm{et}}\) 是
R1147、R1158–1160 的同一原两条 actual cochains，
\(h_{\mathrm{et}}\) 是原最高中央 cochain，满足
\[
da_{\mathrm{et}}=db_{\mathrm{et}}=0,\qquad
dh_{\mathrm{et}}=-\Pi_0(a_{\mathrm{et}}\cup b_{\mathrm{et}}).
\tag{1163.12}
\]
包括原平滑、真正 crossed correction、算术未平滑和同根
gauge 在内，均固定为原文的选择。不是另取一个任意 cup primitive。

以 (1163.9) 的 \(H^1\) 同构提升两条 abelian classes，
取 syntomic cocycles \(a,b\)。
它们的 cup 在 étale \(H^2\) 中由 (1163.12) 为零。
(1163.9) 对最高中心给 \(H^2\) 单射，故 syntomic cup
本身为边界；可以取 \(h\) 满足
\[
dh=-\Pi_0(a\cup b).
\tag{1163.13}
\]

先取到一个 \(h\) 还没有识别原 \(h_{\mathrm{et}}\)。
对固定 \(a,b\)，所有 (1163.13) 的 solutions
模中央零次 gauge 构成 \(H^1(C_{12,2,n}^{\mathrm{syn}})\)
的 torsor；其 automorphisms 为
\(H^0(C_{12,2,n}^{\mathrm{syn}})\)。
étale 侧同样成立。
由 (1163.9) 的 \(H^1\) 与 \(H^0\) 同构，
原 \(h_{\mathrm{et}}\) 的**整个 gauge 类有唯一的
syntomic gauge 类原像**，且原 morphisms 同时被恢复。

也可在实际 complexes 上逐式验证这个 argument。
选择与 product 相容的 resolutions；
对于 degree-one \(a,b,h\) 满足 \(dh=-a b\)，
degree-zero \(r,s,t\) 的 ordered gauge 是
\[
\boxed{\quad
a'=a+dr,\qquad b'=b+ds,\qquad
h'=h+a s-r b+dt-r\,ds.
\quad}
\tag{1163.14}
\]
乘法在第三槽使用 (1163.11)。
直接微分得 \(dh'=-(a+dr)(b+ds)\)。
这也是上三角矩阵
\(M' =g^{-1}Mg+g^{-1}dg\) 的第三槽。
因此两侧 abelian representatives 的 exact 差可以用同一个
ordered gauge 对齐，之后才用中央 \(H^1\) 同构选择所需差。
所有 \(a s,r b,r\,ds\) 都保留。

这一描述严格区分：

- 固定 étale primitive 的 syntomic **gauge 类**唯一；
- 不同 cochain representatives 本身并不因此相等；
- \(H^0\) 同构控制全部 gauge automorphisms，
  不擅自假设分歧标记域上的有限 \(H^0\) 为零。

更形式化地，固定 quotient 后的 primitive groupoids
之间，(1163.8) 诱导一个等价。
固定原 étale object 连同其 identification 后的 homotopy fibre
是 contractible；这正是“唯一到相容同构”的准确含义。

## 6. 全部 p-power 层、同根运算与原未平滑对象

(1163.3) 的 maps、(1163.4) 的 projectors 及 (1163.10)
的 products 均与 \(\mathbb Z/p^{n+1}\to\mathbb Z/p^n\)
相容。原 actual cochains 本来组成 R1147 §§17–20
及 R1160 §8 的兼容整塔。

因此可对这些 groupoid equivalences 取 homotopy inverse limit，
得到同一原塔的兼容 syntomic object。
这不是每层另挑一个不相容的 primitive：
连同其指定 étale identification 的 lift groupoid
逐层 contractible，过渡 maps 与所有 cocycle identities
从原塔一并运输。有限层 \(H^0\) 可能非零不破坏该论证，
因为其 maps 也由比较完整控制。

具体应用时，原 \(1-p^d\)、\(d!\)、\(i!j!\)、
\(\lambda_\infty\)、\(J_n\)、\(B_n\) 与 \(v_n^{-1}\)
仍按各原定义作用；本篇不把它们换成 cohomology 上的
一个未经上链校准的 scalar。
尤其原 \(h_0=(h_V+B_n)/v_n\) 是被运输的同一 object，
不是看到 scalar eigenvalue 后另行解 cup 方程所得的 arbitrary lift。

若某个 root change、chord identity 或 actual norm transition
已在原 étale 塔中给出同构，则 groupoid equivalence
将该**已给同构**带到 syntomic 侧。
反过来，本篇不从 object 的存在捏造一份 raw roots
或 four-line formula 的逐槽 compatibility。
R1162 所要求的实际系数输入仍须在原源中建立。

## 7. 与原 FL 格、rational dilogarithm 以及 PD 窗口的关系

回到未分歧底 \(F\)。
R1147 §§14–15、R1149–1150 已把原 compatible tower
识别为指定 \(43\) 格及其相对 realization。
本篇 (1163.8) 的 étale side 正是同一格的最高 quotient，
所以它没有留下另一条 \(p\)-power index 未知的 stable lattice
供任意选择。

另一方面，R1155 §15 对每个原 raw primitive 给出同一路径的
rational \(B_{\mathrm{st}}\) comparison。
本篇只是将该原 étale primitive 的 integral syntomic
gauge 类另行固定；两种实际同源比较必须沿原
étale identification 连接，不能先将一个 rational
class 的任意坐标逐项约模 \(p\)。

后续还需执行的具体步骤是：

1. 以原 theta roots、Miller coefficient source 和
   已给的 ordered homotopies 写出此 syntomic object 的实际代表；
2. 将这个代表写到 R1147 的同一 adapted integral frame；
3. 用 R1155 (1155.102) 或 R1162 (1162.12) 读取真正的
   normal coefficients，并作原 Cartan projection 和 global subtraction。

本篇支付的是步骤前的**精确有限整比较及原 primitive 类的识别**。
它没有把 cohomological existence 说成已列出了这些
normal coefficients，也不把 raw Frobenius 矩阵再施一次
Frobenius。当原整 representative 给定时，
R1155–1162 的全尾与有限 block 界可直接使用。

## Primary 与证明范围

使用并亲读的已刊 primary 为：

T. Tsuji, *On p-adic nearby cycles of log smooth families*,
Bulletin de la Société Mathématique de France **128** (2000),
529–575，
[正式全文](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
Theorem 5.1 给 (1163.3)；
§2 (2.5)、(2.8) 和其构造给 functorial product compatibility；
Proposition 2.11 保持实际 Kummer symbol convention。
原 log base、分歧允许范围和 \(r\le p-2\) 均在本文明确满足。

signed projector、Tate shift、cohomology cutoff、
最高 \(\Pi_0\) 的全部尺度，以及 primitive groupoid
的比较由本文逐式证明。
没有使用 ordinary 假设、未刊系数比较或一个有 \(p\)-分母的
averaging projector。全部为纸面证明，无数学程序执行。


## 8. 全三个中央槽在同一十二因子模型中的整实现

原低两个 contraction 可以保留在同一
\(\mathcal E^{12}\)、syntomic weight \(14\) 中实现。
这样无需先把一个高 degree 的整 Gysin map 当作已知输入。

在十二因子的 odd summand 上，定义 ordinary permutation
\[
\widetilde\sigma=\operatorname{sgn}(\sigma)\sigma^* .
\tag{1163.15}
\]
它在 \(H^1(E)^{\otimes12}\) 上就是不带 Koszul 号的
通常 tensor permutation。以下全部 projector 都以这个
\(\widetilde\sigma\) 构造，连同原 \(o_{12}\) 作用于 actual complexes。

对 \(r=0,2,4\)，置 \(m=12-2r\)。
先排列十二个位置，使前 \(2r\) 个按序成为 \(r\) 对，
其余 \(m\) 个为剩余位置。定义
\[
P_r=
 \left(\prod_{a=1}^{r}
       \frac{1-\widetilde{(2a-1,\;2a)}}2\right)
 \left(\frac1{m!}
       \sum_{\sigma\in S_{\{2r+1,\ldots,12\}}}
               \widetilde\sigma\right)o_{12}.
\tag{1163.16}
\]
这些因子作用于互不相交的位置，故 \(P_r\) 为整 idempotent。
\(r=0\) 时就是 \(\epsilon_{12}\)。

其 geometric cohomology 仍只在 degree \(12\)，且为
\[
(\bigwedge^2 H^1(E))^{\otimes r}
       \otimes\operatorname{Sym}^{m}H^1(E).
\]
加总 Tate twist \(14\)，再用原 Weil pairing，
准确得到
\[
(\bigwedge^2H_n)^{\otimes r}
       \otimes\operatorname{Sym}^{m}H_n(2)
 \simeq \operatorname{Sym}^{12-2r}H_n(r+2)=:Z_{r,n}.
\tag{1163.17}
\]
定义
\[
C_{Z_r,n}^{\mathrm{syn}}
 :=P_rR\Gamma(\mathcal Y_{12},\mathcal S_n(14))[12].
\tag{1163.18}
\]
由 §3 的同一 cone 论证，
\[
\boxed{\quad
H^q(C_{Z_r,n}^{\mathrm{syn}})
 \xrightarrow{\sim}H^q(G_L,Z_{r,n})
 \quad(q=0,1,2),\qquad r=0,2,4.
\quad}
\tag{1163.19}
\]
这里 \(r=2,4\) 的模型与 (1163.7) 的较少因子模型不同；
本节只使用它已经准确覆盖的 degrees \(0,1,2\)。
不需要宣称这两个不同 integral complexes 在全部 degrees 上相同。

对原 \(\operatorname{Sym}^4H_n\otimes
\operatorname{Sym}^8H_n\)，先作 §4 的 external product；
将第一块的前 \(r\) 个位置与第二块的前 \(r\) 个位置
依序交叉配对，使用 (1163.15) 的 actual signed permutation
送到 (1163.16) 的 pair positions，最后施 \(P_r\)。
在 pure powers \(v^4\otimes w^8\) 上，每个 pair 的投影是
\[
\frac{v\otimes w-w\otimes v}{2}.
\]
由 normalized alternating-tensor 与 exterior-power 的同构，
它正对应 \(v\wedge w\)，不是 \((v\wedge w)/2\)。
其余位置的 normalized symmetrization 对应
\(v^{4-r}w^{8-r}\)。因此得到的 coefficient map 为
\[
\boxed{\quad
v^4\otimes w^8\longmapsto
 \langle v,w\rangle^r\,v^{4-r}w^{8-r},
\quad}
\tag{1163.20}
\]
恰为原 \(\Pi_r\)，三个 \(r=0,2,4\) 同时成立。
因 pure powers 的 polarization 所需 factorial 都是单位，
这在整个原 tensor coefficient 上确定同一个 map。
没有再乘选取 cross-pairs 的组合数，也没有将原
normalized polarization 换成未归一的 transvectant。

## 9. 常数槽的真实 Poincaré coevaluation 及负二分之一

还需实现原
\[
\lambda_\infty x\otimes t',
\qquad
\lambda_\infty=\frac{21}{11}(1+p^4),
\]
从 \(\operatorname{Sym}^4H_n(1)\otimes\mathbb Z/p^n(5)\)
到 \(Z_{4,n}=\operatorname{Sym}^4H_n(6)\) 的项。
为了把它也放进 (1163.18)，使用实际整 Poincaré line bundle
\[
\mathcal P=
\mathcal O_{\mathcal E\times\mathcal E}
       (\Delta-\mathcal E\times O-O\times\mathcal E),
\tag{1163.21}
\]
连同两坐标轴上的原 rigidifications。

Tsuji (2.6) 的 symbol map 施于此 line bundle 的实际
transition units，给其整 syntomic Chern class
\[
c_{1,\mathrm{syn}}(\mathcal P)
 \in H^2(\mathcal Y_2,\mathcal S_n(1)).
\tag{1163.22}
\]
具体地，取将 \(\mathcal P\) 平凡化的整 open cover；
其 transition units 是 Čech degree 一的数据，
symbol map 将它们送到 internal degree 一，所得 total
degree 二的类就是 (1163.22)。
三重交上的乘法恒等与 symbol 的加法结构保证它闭合，
改变 trivializations 只给同一个实际 coboundary。
Proposition 2.11 使其 period image 等于原 étale Chern class。
这里不要求一个任意 ramified raw rational function 本身为整单位。

令
\[
Q_\wedge=\frac{1+\operatorname{swap}^*}{2}\,o_2,\qquad
\eta=-\frac12Q_\wedge\,c_{1,\mathrm{syn}}(\mathcal P).
\tag{1163.23}
\]
几何 swap 在两个 degree-one factors 上是 ordinary swap 的负号，
故 \(Q_\wedge\) 选的正是 \(\bigwedge^2H^1(E)\)。
下面校准 (1163.23) 的完整符号和 \(2\)。

取 \(a,b\in H^1(E_{\bar L},\mathbb Z/p^n)\)，使原
cup–trace 满足 \(\operatorname{tr}(a\cup b)=1\)。
mixed part 的 diagonal class 为
\[
c_1(\mathcal P)=b\otimes a-a\otimes b.
\tag{1163.24}
\]
这可直接用 diagonal correspondence 的 identity action 验证；
也可不选基核准系数：
\(\Delta^*\mathcal O(\Delta)\) 是 \(T_{\mathcal E/\mathcal O_L}\)，
其 fibre degree 为零；两坐标轴各在 diagonal 上切出 \(O\)。
所以
\[
\deg\Delta^*\mathcal P=-2.
\]
由此，diagonal cup 后的 trace 在 (1163.24) 上为 \(-2\)。
故 (1163.23) 的 étale image 正为
\[
\frac{a\otimes b-b\otimes a}{2},
\]
其 exterior/cup contraction 是 \(+1\)。

沿 (1163.5) 的原 first-slot Weil identification，
这一 unit 正是
\[
\mathbb Z/p^n
 \xrightarrow{\ \eta_{\mathrm{et}}\ }
 \bigwedge^2H^1(E)(1),
\tag{1163.25}
\]
即原 Weil coevaluation；没有任意 CM period。
若写 \(u\mapsto b\otimes\tau_1\)、
\(v\mapsto-a\otimes\tau_1\)，
\(\langle u,v\rangle=\tau_1\)，可再逐基核出同一个正号。

取四份 (1163.23) 的 external product，占据
(1163.16) 的前八个 pair positions；
把原 \(x\) 的四个 factor 放在最后四位。
再与原 Tate-five complex 的 element 相乘，得到
\[
C_{4,1,n}^{\mathrm{syn}}
 \mathbin{\otimes^{\mathbf L}}C_{0,5,n}^{\mathrm{syn}}
 \longrightarrow C_{Z_4,n}^{\mathrm{syn}}.
\tag{1163.26}
\]
四份 Chern classes 总 cohomological degree 为八、
总 syntomic weight 为四；
与原两项的 weights \(5,5\) 相加恰为 \(14\)，
degree shifts \(4,0,8\) 相加恰为十二。
每个 pair 的 contraction 为 \(+1\)，所以 (1163.26)
的 coefficient map 精确为 \(x\otimes t\mapsto x t\)。
最后乘原 \(\lambda_\infty\)，得到原 bilinear law 的最后一项。
特别负号只在必要的 \(-1/2\) coevaluation 中出现四次，
没有为此修改原 \(\lambda_\infty\)、\(\gamma_5\) 或 Tate frame。

(1163.22) 的 Chern class 位于 degree 二、weight 一，
超出 (1163.9) 在零因子时的一阶满射范围；
本节没有据该满射制造它。
它由实际 line bundle 和实际 integral symbol map直接构造，
比较只用于识别其既有 étale image。


## 10. 原完整四十三格的同一 finite integral primitive 比较

现在取三个**分开的目标 complexes**
\[
C_{Z,n}^{\mathrm{syn}}=
 C_{Z_0,n}^{\mathrm{syn}}\oplus
 C_{Z_2,n}^{\mathrm{syn}}\oplus
 C_{Z_4,n}^{\mathrm{syn}},
\]
以及
\[
C_{V,n}^{\mathrm{syn}}=
 C_{4,1,n}^{\mathrm{syn}}\oplus
 C_{8,1,n}^{\mathrm{syn}}\oplus
 C_{0,5,n}^{\mathrm{syn}}.
\tag{1163.27}
\]
三个 \(P_r\) 不必在同一个十二因子 cohomology 中互相正交；
(1163.27) 是各个实际 direct summands 的外部 direct sum，
不是未经证明的一个 projector 分解。

(1163.20)、(1163.26) 给原全部 bilinear map
\[
\mathfrak b((x,y,t),(x',y',t'))=
\left(\Pi_0(x,y'),\Pi_2(x,y'),
      \Pi_4(x,y')+\lambda_\infty x t'\right)
\tag{1163.28}
\]
的 integral syntomic realization。
period maps 与其完全相容，三项与原 R1147 的 Tate twists、
normalization 和 order 都相同。

对原 actual cochains \(a,b,c\) 及中央 \(h_0,h_2,h_4\)，
方程为
\[
dh_0=-\Pi_0(ab),\qquad
dh_2=-\Pi_2(ab),\qquad
dh_4=-\Pi_4(ab)-\lambda_\infty ac.
\tag{1163.29}
\]
\(a,b,c\) 都闭合。对零次 gauge \(r,s,u\)，三交换槽
变成 \(a+dr,b+ds,c+du\)；中央的完整变换为
\[
\begin{aligned}
h_j'&=h_j+\Pi_j(as-rb-r\,ds)+dt_j,
                  &&j=0,2,\\
h_4'&=h_4+\Pi_4(as-rb-r\,ds)
             +\lambda_\infty(au-rc-r\,du)+dt_4.
\end{aligned}
\tag{1163.30}
\]
微分逐项给原 (1163.29) 的 transformed equations。
这里既没有删除 constant Tate-five 槽，也没有只保 highest bracket。

三个交换系数的 \(H^0,H^1\) 比较同构，三个中心的
\(H^0,H^1,H^2\) 比较同构。因此 §5 的同一 obstruction、
difference 和 automorphism 论证适用于 (1163.28)：
\[
\boxed{\quad
\text{原完整 finite Heisenberg primitive groupoid
与其上述 integral syntomic realization 相等价。}
\quad}
\tag{1163.31}
\]
固定 R1147、R1158–1160 的原整塔及指定 étale identification 后，
其 homotopy fibre contractible。
全部 \(\eta\)、projectors、period maps 和 bilinear maps
来自同一整构造，故 (1163.31) 与所有 \(p^n\) reductions 相容。
由 §6 得原全 tower 的同一结论。

经 R1147 (1147.46) 的 faithful affine representation，
这正是秩 \(1+15+27=43\) 的原 flagged object 的
finite integral syntomic 比较。回未分歧底时，其 étale
lattice 正是先前恢复的原 Fontaine–Laffaille 格；
没有使用分歧底上的虚假未分歧 FL 等价。

至此，§4 当时只处理最高 product 的范围已由 §§8–10
扩大到原 \(\Pi_2,\Pi_4,\lambda_\infty\) 全部项。
尚未替代的输入仍是 §7 的实际 theta/Miller representative、
同根/中央 homotopies 在原 adapted frame 中的矩阵，
以及 R1155–1162 的 finite normal coefficients。
(1163.31) 不把这些未知系数设为零或设为单位。

本节新增的 scalar source 只有实际 Poincaré line bundle；
它的 syntomic Chern class由已亲读的 Tsuji (2.6) 和
Proposition 2.11 构造并校准。所有 projector、coevaluation
的 \(-1/2\)、三中心尺度及 ordered gauge 公式均在上文自证。
全部为纸面证明，无数学程序执行。
