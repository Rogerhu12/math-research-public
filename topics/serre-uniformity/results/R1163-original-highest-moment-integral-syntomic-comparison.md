# R1163 — 原最高矩与指定 primitive 的整 syntomic 比较

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇对同一原 good elliptic fibre 的有限系数，
用实际椭圆曲线乘积及整 projector，把已刊的 scalar log-syntomic
比较准确转成原对称幂系数的比较。所得范围足以运输原两条
abelian cochains、它们的最高 ordered cup，以及
R1158–1160 已指定的最高中央 primitive 的完整 gauge 类。

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
