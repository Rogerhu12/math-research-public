# R188：带真实41项链标记的CM–Hecke正常水平交数

**状态：已证明并实算。** 本文完成R186全部54个实际对应在
$\ell\nmid2\cdot41\cdot n$处的**互异水平分量交数**。它不是完整的
$h(B,S B)$：共有CM分量和尖点的切向自交、$\ell\mid n$处的准典范提升、
2处以及41处的模型修正仍须保留。

计算使用整数四元数及$\mathbb F_{41}$上的20个真实项链，未构造庞大的41挠点数域，
也未用未带标记的$j$ resultant替代本曲线的交数。
全部54行共核验68256个正常端态，得到538个非零$(n,\ell,I)$项；其中26项在47，
其余512项属于R186尚需的非47输入。所有正项的素数不超过347。

## 1. 除子与待算的交数

令$X=X_{\rm ns}^+(41)$，$Z=Z_{-4}$为R112的真实20次CM迹。
在本节的特征零算术模型中取

$$E:y^2=x^3-x,\qquad \mathcal O=\mathbb Z[i].$$

R112在47处使用的$y^2=x^3+x$是其几何同构模型；本文的项链条件在换基下不变，
不将两套模型的局部截面坐标混用。

设$S_n$是R186的一个实际有效对应。除$n=4$外，其指标均为平方自由整数，
$S_n=T_n$；$S_4=C_4=T_2^2-3\Delta$只取循环四核，度为6。
在所有情形中$41\nmid n$，且$n\le91$。
定义$S_nZ$中所有特征零底层椭圆曲线仍与$E$同构的子循环为$Z_n^{\rm ret}$，并置

$$D_n=S_nZ-Z_n^{\rm ret}.$$

对平方自由$n$，

$$Z_n^{\rm ret}=r_K(n)Z,\qquad
r_K(n)=\tfrac14\#\{\alpha\in\mathbb Z[i]:N\alpha=n\}.$$

理由是每个这样的核是一个高斯理想，$[\alpha]$在41项链上给一个置换；四个单位给同一核。
循环四情形中唯一范数4理想是$(2)$，其核$E[2]$非循环，所以$Z_4^{\rm ret}=0$。
于是$D_n$与$Z$在特征零没有共有支撑。
记

$$I_\ell^{\rm prop}(n)=(\overline Z\cdot\overline D_n)_\ell,$$

其中先在严格未分歧基变换上逐个几何截面计算，再按整个有理迹相加。
这个和已经包含剩余次数；不再因$[K:\mathbb Q]=2$额外除二。

## 2. 两个分裂反射固定的非分裂项链

以下有限群引理独立于交数公式。
取$p\equiv1\pmod4$，在$\mathbb F_p^2$中令
$i=\operatorname{diag}(s,-s)$，$s^2=-1$。
把一个无向非分裂项链看作一个非分裂Cartan正规化子，等价地看作其Cartan内唯一的
射影二阶元。所有被$i$固定的项链准确为

$$\nu_t=\begin{pmatrix}0&t\\1&0\end{pmatrix},
\qquad t\in\mathbb F_p^\times\text{ 为非平方}.$$

所以共有$(p-1)/2$个。
确实，$i$是分裂射影反射，不能属于非分裂Cartan；固定项链等价于
$i\nu=-\nu i$。迹零矩阵的这条等式迫对角元为零，非分裂条件恰为$t$非平方。

对另一分裂反射$i'$，它与$i$共同固定的项链数为：

1. $i'=i$射影成立时，为$(p-1)/2$；
2. $ii'$是正则非分裂元时，为1；
3. 其余非恒等情形，包括正则分裂元和非平凡幺幂元，为0。

证明是两个反射之积属于它们共同的Cartan。非标量非分裂矩阵生成唯一的二次域子代数，
所以Cartan唯一；反之$i$把该积共轭到其逆，因此正规化这个Cartan。
即使该积射影阶为二，其在$\mathrm{GL}_2$中生成的二次域仍唯一，结论不变。

设$\beta=a+bj$，$a,b\in\mathbb Q(i)$，$j^2=-\ell$且$ji=-ij$，
记$A=N(a)$、$B=\ell N(b)$、$n=A+B$。
在$p\nmid n\ell$时直接乘矩阵给

$$\operatorname{tr}(i\beta i\beta^{-1})=\frac{2(B-A)}n,
\qquad \operatorname{disc}(i\beta i\beta^{-1})=-\frac{16AB}{n^2}.$$

故所需标记权重$w_p(\beta)$为

$$
w_p(\beta)=
\begin{cases}
(p-1)/2,&\beta\text{ 正规化分裂子域},\\
1,&\left(\frac{-AB}{p}\right)=-1,\\
0,&\text{其他情形}.
\end{cases}
\tag{188.1}
$$

当$A$或$B$模$p$为零，但相应向量本身非零时，不能套第一行；此时非平凡幺幂情形给0。

在本题$p=41$，取$s=9$。写

$$\beta=(a+bi+cj+dij)/2.$$

忽略不影响项链的标量$1/2$，其实际41挠点矩阵可取

$$M_\beta=
\begin{pmatrix}
a+9b&-\ell(c+9d)\\c-9d&a-9b
\end{pmatrix}
=\begin{pmatrix}A_0&B_0\\C_0&D_0\end{pmatrix}.$$

行列式为$4n$。直接将$M_\beta^{-1}iM_\beta$与$\nu_t$反交换，得到

$$\boxed{B_0D_0-tA_0C_0=0\pmod{41}.}\tag{188.2}$$

程序对每一个端态逐一检查全部20个非平方$t$，并与(188.1)独立比较。
在当前范数界下所有整数坐标绝对值小于41，故正规化分裂子域的例外恰为
$(a,b)=(0,0)$或$(c,d)=(0,0)$，没有未处理的模41零向量。

## 3. 实际超奇异端环及完整范数枚举

设$\ell\equiv3\pmod4$为奇素数，$j$取$E/\mathbb F_\ell$的Frobenius。
则$j^2=-\ell$且$ji=-ij$。
$E$的全部二挠点在$\mathbb F_\ell$有理，所以$1+j$杀$E[2]$，
$(1+j)/2$是实际端态。因此

$$R_\ell=\mathbb Z[i,(1+j)/2]\subseteq
\operatorname{End}_{\overline{\mathbb F}_\ell}(E).$$

基$1,i,(1+j)/2,(i+ij)/2$的约化迹判别式绝对值为$\ell^2$，
故其约化判别式为$\ell$，已经是该四元数代数的极大序；包含关系遂为等式。
准确整性与范数条件为

$$a\equiv c\pmod2,\qquad b\equiv d\pmod2,\qquad
a^2+b^2+\ell(c^2+d^2)=4n.\tag{188.3}$$

程序在(188.3)给出的有界整数盒中完整枚举。
除$n=4$外，$n$平方自由，因此所有度$n$核自动循环。
范数4时，核非循环当且仅当$\beta\in2R_\ell$；准确判据是四坐标均偶，且
$a/2\equiv c/2$、$b/2\equiv d/2\pmod2$。这些项从$C_4$中剔除。

对一个非CM端态$(c,d)\ne(0,0)$，(188.3)立即给$\ell\le4n$。
所以枚举上界不是经验截断。
若$\ell\equiv1\pmod4$且$\ell\nmid41n$，约化普通。
端态在典范提升上全部提升；一个相交的同源核只能返回原CM曲线，已经在$Z_n^{\rm ret}$中。
故这种分裂素数的正常交数为零。

## 4. 精确提升长度

现在仍设$\ell$惰性且$\ell\nmid2\cdot41\cdot n$。
令$W=W(\overline{\mathbb F}_\ell)$。
$E/W$具有未分歧二次CM作用，是其形式群的典范提升。
写$\beta_-=((c+di)/2)j$。未分歧典范提升的端态提升判据为

$$\beta\text{ 提升到 }W/\ell^k
\quad\Longleftrightarrow\quad
v_\ell(N\beta_-)\ge2k-1.\tag{188.4}$$

这正是Gross–Zagier III §7 Proposition 7.3的局部端环公式：在本处二次判别式$-4$是单位，
且$N(\ell)=\ell^2$。其证明只用未分歧二次CM形式群的典范提升及Serre–Tate定理，
与他们全局主定理的奇判别式假设无关；这里不调用该全局定理来覆盖$-4$。
也可在局部写成
$\operatorname{End}_{W/\ell^k}(E)\otimes\mathbb Z_\ell
=\mathcal O_{K,\ell}+\ell^{k-1}R_\ell\otimes\mathbb Z_\ell$，
得到相同条件。

因$\ell$在$\mathbb Z[i]$惰性，

$$v_\ell(N\beta_-)=1+2\min(v_\ell(c),v_\ell(d)).$$

于是每个非CM端态贡献的准确长度为

$$\boxed{L_\ell(\beta)=1+\min(v_\ell(c),v_\ell(d)).}\tag{188.5}$$

41层结构为étale，已经成立的模$\ell$标记等式唯一提升到任何$W/\ell^k$；
故项链筛选不再改变(188.5)。程序中的实际长度为1、2或3，未一律替换成1。

## 5. 素数3处必须删除整个返回核类

对$\ell\ge7$，$R_\ell^\times=\{\pm1,\pm i\}$。
返回原CM曲线的度$n$核在约化端环中的所有表示就是范数$n$的高斯整数。
但在$\ell=3$，$R_3^\times$有12个元素。
一个在特征零由高斯整数$\alpha$给出的同一个核，在特殊纤维还可以表示为
$u\alpha$，$u\in R_3^\times$；其中某些$u\alpha$已经不在$\mathbb Q(i)$中。
把它们误留在正常部分，会把共有CM分量的自交混入本题。

因此所有奇惰性素数统一使用集合

$$\mathcal R_{n,\ell}=R_\ell^\times
\{\alpha\in\mathbb Z[i]:N\alpha=n,\ \ker\alpha\text{ 满足对应的循环条件}\}.
\tag{188.6}$$

将(188.6)整个删除。它准确对应返回核：若两个可分同源有同一核，
它们之间恰差目标曲线的一个自同构；反向亦然。
程序在四元数序内精确相乘，并核验范数恒等式，没有按整数坐标猜测核类。

还需确认20个CM截面本身在3处不互相合并。
射影自同构群为$S_3$，固定的$i$是一个换位。
含有这个换位的稳定子只能是$C_2$或$S_3$；相应$S_3$轨道内都恰有一个$i$固定点。
故20个$i$固定项链属于20个不同的自同构轨道。

这些点在粗模型上也正则。可用完整二层结构的Legendre参数$\lambda$在
$\lambda=-1\pmod3$附近作验证。换位$λ\mapsto1/\lambda$的不变量环为
$W[[(\lambda+1)^2/\lambda]]$，因为2为单位。
整个$S_3$的不变量环是$j$直线的完备局部环，其中

$$j=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.$$

后一断言在$\mathbb Z[1/2]$上成立：Legendre环在$j$环上有限整，
泛纤维不变量域为$\mathbb Q(j)$，而$j$环整闭；不需要除3。
由于41层结构为étale，对给定项链取稳定子的不变量即得这两种正则局部环。
$\ell\ge7$时只有素于$\ell$的二阶稳定子，同样正则。

## 6. 粗模交数的准确因子

固定一个源截面及一个度$n$核。因$\ell\nmid n$，该核唯一提升为étale子群，
从而给$S_nZ$中的一个带准确对应重数的目标截面。
对正常目标，特征零的自同构群为$\{\pm1\}$；其CM序的导子大于1。
若它与$Z$中的一个目标相交，模$\ell^k$的同构等价于对应的标记端态$\beta$提升。

在粗曲线上，相交截面的长度为

$$\frac12\sum_{k\ge1}
\#\operatorname{Isom}_{W/\ell^k}(\text{两个带41标记的对象}).\tag{188.7}$$

(188.7)可将两个截面拉回一个素于$\ell$的完整辅助层$M>3$来证明：
在刚性模问题上，交数恰是可提升同构的次数；再用有限映射的投影公式求和，
仅有泛纤维的$\pm1$重复。特殊纤维中额外自同构保留在该和式内，不能额外除4或12。
这就是Gross–Zagier III §6的局部证明；上节已经核实本曲线所需的非尖点正则性。
同一个源的不同核若在粗曲线上给同一点，仍按Hecke循环的重数累加，
与R165中$T_2Z=Z+2Z_{-16}$的因子2一致。

依次对全部核、20个源项链和20个目标项链求和，用(188.2)、(188.5)、(188.6)，得到

$$\boxed{
I_\ell^{\rm prop}(n)=\frac12
\sum_{\substack{\beta\in R_\ell,\ N\beta=n\\
\ker\beta\text{ 满足循环条件}\\
\beta\notin\mathcal R_{n,\ell}}}
L_\ell(\beta)w_{41}(\beta).
}\tag{188.8}$$

集合外的每个端态都非CM，因此和有限且提升长度有定义。
式(188.8)在所有$\ell\nmid2\cdot41\cdot n$给完整的正常水平交数。

## 7. 完整计算与独立小指标检验

生成器直接读取R186已发布格式的54个对应标签及其输入SHA。
它对每个可能的惰性素数$\ell\le4n$：

- 完整枚举(188.3)，逐项保留或删除循环核；
- 构造整个返回核类(188.6)，包括3处的12个真实单位；
- 逐项计算实际矩阵(188.2)与二次特征(188.1)，二者必须一致；
- 按(188.5)保留全部长度并求(188.8)，检验结果为整数。

前几行的非零项如下；表中只包括本条已经处理的素数。

| 对应 | 非零$(\ell,I_\ell^{\rm prop})$ |
|---|---|
| $T_1$ | 无 |
| $T_2$ | $(3,12),(7,4)$ |
| $T_3$ | $(7,8),(11,4)$ |
| $T_5$ | $(3,16),(11,4),(19,4)$ |
| $T_6$ | $(7,16),(11,8),(19,8)$ |
| $T_7$ | $(3,36),(19,4)$ |
| $T_{10}$ | $(3,64),(7,16),(11,8),(19,8),(23,8)$ |

对$n=2$，3处有24个正常端态，各权1、长度1；返回核类共有12个表示，
其中8个不是高斯整数。若只删高斯整数，就会错误得到16而不是12。
7处有8个正常端态，各权1、长度1，得到4。
结合实际循环恒等式$T_2Z=Z+2Z_{-16}$，得到

$$(Z\cdot Z_{-16})_3=6,\qquad(Z\cdot Z_{-16})_7=2.$$

这与独立已知的两个$j$值的精确差

$$287496-1728=2^3\cdot3^6\cdot7^2$$

吻合。程序同时保留标记分布：3处三种源标签$t=7,13,38$各有8个端态，
7处只有$t=34$有8个。上述吻合只是检查，不被当作一般带层交数的证明。

证书保存全部54行、每个候选素数的零值、被删核类数量、长度/权重直方图，
以及每一个正贡献端态的四个整数坐标和实际20项链中的匹配标签。
全部算术只用Python标准库。复算：

```sh
python notes/verify_r188_cartan_intersections.py \
  --basis scripts/data/p41_hecke_height_basis47_certificate.json.gz \
  --output notes/r188_cartan_intersections_certificate.json.gz --check
```

完整源码、输入及证书SHA见同日R188稳定清单。

## 8. 对R186的准确贡献及剩余工作

R186的全局右端为$h(B,S_nB)$，其中$B=[Z-D]$。
本条计算的是它在各好处的一个确定组成部分$\overline Z\cdot\overline D_n$。
还须处理：共有CM循环$r_K(n)Z$的真实切向自交、尖点循环的自交和对应切向单位；
所有$\ell\mid2n$的额外项；41处正确正则模型上的分量修正。
只有这些与47处同一个实际范数元匹配后，才能代入R186式(186.8)。

证书中的47项也不进入非47和式。它们说明某些实际Hecke像与CM支撑在辅助处发生剩余碰撞，
供第三类微分的对数极点消去和实际支撑选择使用；不能据此把它们再从47局部高度中扣一次。

## 来源

- B. H. Gross and D. B. Zagier, *Heegner points and derivatives of L-series*,
  Invent. Math. **84** (1986), 225–320，[作者全文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01388809/fulltext.pdf)。
  本文只使用III §§5–7的étale核提升、粗模交数及未分歧典范提升的局部证明；
  不调用其要求奇判别式的全局主定理。III §8说明共有分量和同源度素因子处为何必须另保留修正。
- B. H. Gross, *On canonical and quasi-canonical liftings*, Invent. Math.
  **84** (1986), 321–326，[作者出版目录](https://abel.math.harvard.edu/~gross/publications.html)。
  所需未分歧局部端环式已经在上一个来源III Proposition 7.3中精确列出并解释。
- [R112](R112-actual-cm-minus4-class-in-local-makdisi-model.md)、
  [R165](R165-actual-t2-on-cm4-cm16-divisor-and-principal-transport.md)：真实20次CM迹和循环二对应的粗模重数。
- [R186](R186-prime-to47-hecke-basis-for-global-height-calibration.md)：54个实际对应、循环四的准确含义及非47高度项的规范。
