# R1099：原 level47 曲线在2处的 CM–Hecke 交数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明。** 本文处理原 $X_{\rm ns}^{+}(47)$ 的 wild dyadic coarse 重数。
没有沿用旧 level41 的有效稳定子2，也没有删除 Gaussian 或 anti-Gaussian 端态。

## 1. 原对象与完整公式

沿用 [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md) 的
原 rational canonical-Cartan CM 点 $y_4,y_{16}$，
$j$ 分别为1728、287496。
对奇数 $n$ 且 $47\nmid n$，定义原好模型上的交数
$$
G_2(n)=(\overline y_4\cdot\overline{T_ny_{16}})_2.
$$
取 Hurwitz 最大序
$$
R_2=\left\{\frac{a+bi+cj+dk}{2}:
 a,b,c,d\in\mathbf Z,\ 
 a\equiv b\equiv c\equiv d\pmod2\right\},
$$
$$
i^2=j^2=-1,\quad k=ij=-ji,\qquad
N(\beta)=\frac{a^2+b^2+c^2+d^2}{4}.
\tag{1}
$$
原47 canonical Cartan 为 $C_i=\mathbf F_{47}[i]^\times$。
置
$$
S_2(n)=\#\{\beta\in R_2:
  N(\beta)=n,\ \beta\bmod47\in N(C_i)\}.
\tag{2}
$$
这里 $N(C_i)$ 指 $\mathrm{GL}_2(\mathbf F_{47})$ 中的正规化子；
因 $47\nmid n$，每个元素都可逆。则
$$
\boxed{\quad G_2(n)=S_2(n)/8.\quad}
\tag{3}
$$

令 $r_2(t)$ 为二平方表示数，并约定 $r_2(0)=1$。
原 normalizer 筛选化成两个互不相交的整数进程后，(3)等价于
$$
\boxed{\quad
G_2(n)=\frac14\left\{
 \sum_{\substack{s\ge0\\2209s\le n}}
    r_2(s)r_2(n-2209s)
 +\sum_{\substack{0<2209s<4n\\s\equiv2\pmod4}}
    r_2(s)r_2(4n-2209s)
 \right\}.\quad}
\tag{4}
$$
第二和来自 Hurwitz 序的真正半整数坐标，不可省。
第一和的 $s=0$ 项保留 Gaussian 和 anti-Gaussian 来源。
特别地
$$
G_2(1)=1.
\tag{5}
$$

取 $q=4513$，$D_a=(q+1-T_q)(23y_a-C_\infty)$。
对奇 $n$ 且 $(n,47q)=1$，完整局部 Néron 交数为
$$
\boxed{\quad
I_2(D_4,T_nD_{16})
=23^2\left((q^2+3q+1)G_2(n)-2(q+1)G_2(nq)+G_2(nq^2)\right).
\quad}
\tag{6}
$$
它是 [R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
第一全局高度公式所需的2处真实输入。

## 2. 两个原点的 marked supersingular reduction

在2处所有 supersingular 椭圆曲线在代数闭域上同构。
原 $E_4$ 的三个 degree2 核都专化到唯一的 $\alpha_2$ 核；
canonical Gaussian 同源 $1+i$ 给其中一个 lift，
其余两个 lift 正是原 $T_2y_4=y_4+2y_{16}$ 中的两个 $y_{16}$ 副本。

选择 special isomorphism，使专化后的 degree2 同源是 $1+i$。
它与 $i$ 交换，故正规化原 $C_i$。
因此 $y_{16}$ 和 $y_4$ 在2的 **marked** special 点相同。
这里比较的是原47 necklace，不只是 underlying $j=0$。

degree 奇数的 Hecke 同源在2的形式群上可逆，
保留 endomorphism 序的2-local completion。
所以全部 $T_ny_{16}$ 的 characteristic-zero 目标
在2仍带
$$
\mathcal O_1=\mathbf Z_2+2\mathbf Z_2[i],
\tag{7}
$$
而 $y_4$ 带最大序 $\mathcal O=\mathbf Z_2[i]$。
它们 generic 支撑不相交，因而没有 self-intersection 或 tangent 项。
在其它奇素数处 conductor 可以变化，不影响(7)。

## 3. 真实 marked automorphism 群是 Q8

$\operatorname{Aut}(\overline E_4)$ 是 Hurwitz 序的24个 norm1单位。
8个坐标轴单位
$$
\pm1,\ \pm i,\ \pm j,\ \pm k
$$
都正规化 $C_i$，组成 $Q_8$。

其余16个单位为 $(\pm1\pm i\pm j\pm k)/2$。
在 $R_2/47R_2=M_2(\mathbf F_{47})$ 中，
normalizer 的两个分支为
$$
\mathbf F_{47}[i]^\times
\quad\hbox{和}\quad
\mathbf F_{47}[i]^\times j.
$$
16个半整数单位的两个 Gaussian 分量均非零，
故一个也不落在这两个分支。
所以实际 special marked automorphism 群恰为 $Q_8$。
中心 $\{\pm1\}$ 在整个 necklace deformation 上作用平凡，
有效作用群
$$
H=Q_8/\{\pm1\}\simeq(\mathbf Z/2)^2
\tag{8}
$$
的阶为4。

这一步正是与旧
[R193](R193-two-adic-local-heights.md) level41 的区别；
旧有效 $C_2$ 或旧20条固定 necklace 不能用于原47。

## 4. wild coarse 商仍可精确计长

令 $W_0$ 为未分歧底环， residue field 代数闭。
把 prime-to-2 level 刚性化后，marked supersingular 椭圆曲线的
fine universal deformation ring 为 $R=W_0[[t]]$。
原粗曲线在2有好光滑模型，
其此处 completed ring 为 $A=R^H$，也是二维正则局部环。
有限商 $R/A$ 的 generic degree 为4；
$R$ Cohen–Macaulay 而 $A$ 正则，故有限平坦、秩4。

原 $y_4$ 的 generic marked automorphism 群为 $\mu_4$，
除中心后的有效稳定子阶2。
所以它在 fine 盘上有两个 geometric canonical branches $a_1,a_2$，
各 generic ramification index 为2。
在足够的整底扩张后，原 coarse Cartier section 的方程 $z_4$
满足
$$
z_4(t)=u(t)(t-a_1)^2(t-a_2)^2,\qquad u(t)\in R^\times.
\tag{9}
$$
没有遗漏2的垂直因子：
$A/2A\longrightarrow R/2R$ 是单射；
若 invariant $a=2r$，则 $2g(r)=2r$，
无2-torsion迫 $r$ 也 invariant。
故一个非零 coarse special 参数不能整个拉回为2的倍数。
结合 generic divisor 的两支及总degree4，
regular ring 的 divisor 分解给(9)的单位精确性。
这里未使用 wild quotient 可按群阶平均的错误操作。

Gross 的 canonical/quasi-canonical lifting 理论适用于 residual characteristic2。
取 $K=\mathbf Q_2(i)$，$\pi=1+i$，
$W$ 为 $K$ 的最大未分歧扩张的整数环。
canonical modulus 在 $\pi W$ 中，因而
$$
v_2(a_\nu)\ge\frac12.
\tag{10}
$$
对 conductor $\mathcal O_s=\mathbf Z_2+2^s\mathcal O$ 的 quasi-canonical lift，
Gross Proposition 5.3 表明其 modulus 是
对应扩张 $M_s/W$ 的 uniformizer。
ramified quadratic 情形 $[M_s:W]=2^s$。
本处全部目标由(7)为 $s=1$，故任一 fine branch $b$ 满足
$$
v_2(b)=\frac14.
\tag{11}
$$
不同的原 formal embedding 或 fine framing 只作整参数变换；
constant 项为 canonical modulus，赋值至少 $1/2$，
不改变(11)这个严格较小的赋值。
因此
$$
v_2(b-a_1)=v_2(b-a_2)=\frac14.
$$
将目标代入(9)，得到 **每一个约化到同一 marked special 点的 Hecke 核**
在原 coarse 曲线上的交数
$$
2\cdot\frac14+2\cdot\frac14=1.
\tag{12}
$$
若目标 residue point 不同，交数为0。
对于分歧定义域，各 geometric conjugate 按原有效 cycle 的重数相加；
以上统一取 $v_2(2)=1$，已经是 base-normalized 交数。
不再额外除以 generic automorphism、quasi 分支数或 wild 群阶。

作为尺度核对，无level的 special 有效群阶12，
同样代入六个 canonical branches 各重2得到 $12/4=3$；
恰为 $v_2(287496-1728)=3$。
原 marked 曲线上(12)为1，不能用这个无level的3代替。

## 5. 从同一个 marked special 点到 norm n 枚举

给 $T_ny_{16}$ 的一个 geometric 核，
其 quotient marked special point 若与 $(\overline E_4,C_i)$ 同构，
到该固定点的 marked isomorphism 有
$|\operatorname{Aut}(\overline E_4,C_i)|=8$ 种。

第2节的固定 special identification 将此同源写成
$R_2$ 中 norm $n$ 的一个端态 $\beta$。
标记兼容恰为 $\beta\bmod47\in N(C_i)$。
反过来每个这样的 $\beta$ 给一个且仅一个核及一个 marked isomorphism。
即使 $n$ 非平方自由，这仍是原 degree $n$ Hecke 的全部子群；
没有删除非循环核，也没有添加 cyclic 条件。
所以
$$
\#\{\text{matching 原 Hecke 核}\}=S_2(n)/8.
$$
合(12)得到(3)。

特别地，$\beta$ 落在 Gaussian 或 anti-Gaussian 子空间
只描述 special endomorphism；
它不意味着 char0 的 conductor2目标等于 conductor1点。
这些元素必须保留。这与 good odd prime 通过 $2n$ 同源剔除
Gaussian 二核的 [R1097](R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)
是不同的实际枚举，不能混用。

## 6. 准确的两个稀疏二平方和

写 $A=a^2+b^2,\ B=c^2+d^2$。
因47在 $\mathbf Z[i]$ 惰性，
$$
\beta\bmod47\in N(C_i)
\Longleftrightarrow
47\mid a,b\ \text{或}\ 47\mid c,d
\Longleftrightarrow
2209\mid A\ \text{或}\ 2209\mid B.
\tag{13}
$$
两分支不相交，因为 $A+B=4n$ 且 $47\nmid n$；
它们交换 $(a,b)$、$(c,d)$ 后完全对称。

若四个坐标全偶，令 $\beta=x+yi+zj+wk$，则
$x^2+y^2+z^2+w^2=n$。
第一分支的贡献为
$$
\sum_{2209s\le n}r_2(2209s)r_2(n-2209s)
=\sum_{2209s\le n}r_2(s)r_2(n-2209s).
\tag{14}
$$
这里 $s=0$ 留下两坐标轴的真实项。
等式用 $r_2(47^2s)=r_2(s)$，由惰性可直接对表示同时除以47。

若四坐标全奇，则 $A,B\equiv2\pmod4$，
$A+B=4n$，第一分支为 $A=2209s,\ s\equiv2\pmod4$。
这时任一二平方表示的两个坐标自动均奇；
若范数模8不是2，$r_2$ 自己为0。
其贡献为
$$
\sum_{\substack{0<2209s<4n\\s\equiv2\pmod4}}
r_2(s)r_2(4n-2209s).
\tag{15}
$$
将(14)、(15)各乘两个 normalizer 分支，再除8，得到(4)。
$n=1$ 时仅(14)的 $s=0$ 保留，$r_2(1)=4$，所以(5)成立。

## 7. 完整 Bq 高度与剩余工作

对2处完整 admissible Néron symbol 作 Hecke 自伴移槽，
方法和 [R1098 §5](R1098-original-bad47-CM-intersections-and-exact-vertical-correction.md)
相同。这里原模型光滑，degree-zero 除子无非平凡垂直修正。
CM 目标具有 good reduction，尖点不与之相交；
$B_q$ 消去整个 $C_\infty$。
故
$$
I_2(D_4,T_nD_{16})
=23^2(y_4\cdot T_nB_q^2y_{16})_2,
$$
再用 $B_q^2=(q^2+3q+1)-2(q+1)T_q+T_{q^2}$ 得(6)。

至此2处、所有奇好素数和坏47的原交数公式都有精确来源。
后继将消费这些公式计算第一全局高度；
本文未宣称实际高度非零、整高度矩阵可逆、八盘内部分类或 Serre 主目标完成。

## 文献

- Benedict H. Gross，*On canonical and quasi-canonical liftings*，
  Inventiones Mathematicae 84 (1986)，§§2–5，
  特别是 wild2 也适用的 Proposition 3.3、4.3 与
  Proposition 5.3 的 quasi modulus uniformizer。
  [原扫描](https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf)，
  PDF末尾六页；本处 ramified degree $[M_s:W]=2^s$ 保留在(10)–(11)。
- 原 integral modular curve、full-level rigidification 和 good reduction
  沿用 R1094 的原 $X_{\rm ns}^{+}(47)$ 来源。
  coarse wild 重数由本文第3–4节直接计算。
- [旧R193的even-degree审计](../notes/2026-11-13-r193-quasi-canonical-even-degree-audit.md)
  只作 Gross 原端态/quasi 层出处；旧level41的 $C_2$、20necklaces、
  对角项和特定高度值均未移用。
