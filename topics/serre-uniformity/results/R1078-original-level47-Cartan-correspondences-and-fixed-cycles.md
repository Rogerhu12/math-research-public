# R1078. 原层 47 的全部 Cartan 角对应与完整 fixed cycles

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：已证明，纯纸面。**
本篇在原完整曲线
$$
X=X_{\rm ns}^+(47),\qquad J=\operatorname{Jac}(X)
$$
上给出全部非恒等、只改变 Cartan 的双陪集对应。
证明包含几何支、粗模自同构重数、全部二十三个 cusps、
完整 fixed divisor 和每个对应在 $H^0(X,\Omega^1)$ 上的准确 trace。
结果是实际后继高度计算的输入，不宣称这些对应已经给出
Mordell–Weil 非饱和块或盘内非零高度。

令 $y_4=c_{1728}$、$y_3=c_0$ 为 canonical CM Cartan 的两个有理点，
令 $D_\infty$ 是全部二十三个 cusps 之和。
以下 $R_C$ 中的下标满足 $C\sim-C$；
特别 $C=0$ 只计一次。

## 1. 原双陪集的完整分类

因 $-1$ 在 $\mathbf F_{47}$ 非平方，每个非分裂 Cartan 子代数
恰含一对迹零元 $\{\pm x\}$ 满足
$$
x^2=-I.
\tag{1078.1}
$$
反过来，该对生成该 Cartan。因此原无定向 necklace 就是这一对，
不增加一个带向或带 Weil root 的 level 结构。
这与 R1073 的 $J_5^2=5I$ 坐标相容：$x=13J_5$ 满足 (1078.1)；
此处仅使用 intrinsic Cartan，未替换原曲线或其有理下降。

给定 $\pm x$、$\pm x'$，定义角
$$
C=-\frac12\operatorname{tr}(xx')\pmod{\pm1}.
\tag{1078.2}
$$
选取 $C$ 的代表，可唯一写
$$
x'=Cx+w,\qquad xw=-wx,\qquad w^2=C^2-1.
\tag{1078.3}
$$
anti-commuting 空间是 $\mathbf F_{47^2}$ 上的一维模；
其中平方是某固定非零 scalar 乘二次范数。
Cartan 的共轭作用将 $w$ 乘以 $r/\bar r$，
这些乘子恰遍历范数一的四十八元群。

若 $C=\pm1$，范数为零迫 $w=0$，于是 $\pm x'=\pm x$。
这是唯一恒等双陪集。
若 $C\ne\pm1$，非零范数纤维有四十八个元素，
Cartan 共轭在其上可迁。
当 $C\ne0$ 时取 $\pm x'$ 不使固定 $C$ 的纤维进一步减半；
当 $C=0$ 时 $w$ 与 $-w$ 代表同一 necklace，故减半。

所以全部非恒等双陪集准确为
$$
R_C,\qquad
C\in\mathbf F_{47}/\{\pm1\},\quad C\ne\pm1,
\tag{1078.4}
$$
共二十三个，其中
$$
d_C:=\deg R_C=
 \begin{cases}24&C=0,\\48&C\ne0.\end{cases}
\tag{1078.5}
$$
泛纤维检查为 $1+24+22\cdot48=1081$，
等于原 necklaces 的总数 $47\cdot46/2$。

$R_C$ 把 $(E,\pm x)$ 送到同一个 $E$ 上角为 $C$ 的全部 $\pm x'$。
Galois 在 $E[47]$ 上的 conjugation 保持 (1078.2)，
故这些对应定义于 $\mathbf Q$。
$\operatorname{tr}(xx')=\operatorname{tr}(x'x)$ 说明每个对应对称；
其紧化是实际有限 correspondence，泛纤维的各项带重数一。
所有 $R_C$ 都不含 diagonal component。

## 2. 两个 CM 角映射

以下符号 $\mathcal F_i^*R_C$ 表示若干原 $R_A$ 的**和**，
每个角类 $A\sim-A$ 只计一次：
$$
\mathcal F_4^*R_C
 =\sum_{\substack{A\in\mathbf F_{47}/\pm,\ A\ne\pm1\\
                  2A^2-1=\pm C}}R_A,
\tag{1078.6}
$$
$$
\mathcal F_3^*R_C
 =\sum_{\substack{A\in\mathbf F_{47}/\pm,\ A\ne\pm1\\
                 (3A^2-1)/2=\pm C}}R_A.
\tag{1078.7}
$$
恒等角不进入这两个和。
在 (1078.6) 中 $A=0$ 的 image 是恒等角，所以不会出现；
在 (1078.7) 中 $A=0$ 可出现，其 degree 必须使用 $24$。
因 $(-1/3\,/\,47)=-1$，(1078.7) 的 image 为恒等角时也只有
已删去的 $A=\pm1$。

### 2.1 $j=1728$：一条 fixed branch 与二倍粗模拉回

在 $E$ 上取 $i^2=-1$，其 canonical Cartan 是 $x_0=i$。
对 $x=Ax_0+w$，共轭给
$$
ixi^{-1}=Ax_0-w.
$$
由 $w^2=A^2-1$ 得 $x$ 与 $ixi^{-1}$ 的相对角
$$
-\frac12\operatorname{tr}\bigl(x\,ixi^{-1}\bigr)=2A^2-1.
\tag{1078.8}
$$
若 $A=0$ 或 $A=\pm1$，共轭已经固定 $\pm x$，
没有非恒等 $R_C$ fixed branch。
其它情形中 $\operatorname{Aut}(E)/\{\pm1\}=C_2$
在该 Cartan 轨道上自由作用。
在 fine deformation 参数 $s$ 上，其非恒等元为 $s\mapsto-s$；
固定分支与 diagonal 交长为一。

另一方面，$R_A(y_4)$ 的 specialization
在每个这样的 coarse 目标点上有重数二：
源的有效稳定子为 $C_2$，目标稳定子平凡，
对应模问题的粗模拉回长度就是二。
所以这一部分 fixed cycle 准确是
$$
\frac12(\mathcal F_4^*R_C)(y_4).
\tag{1078.9}
$$
分母二不是删去某个几何支，而是准确除去粗模拉回重数。

### 2.2 $j=0$：两条 fixed branches 与三倍粗模拉回

取 $\omega^2+\omega+1=0$。
因 $3$ 在 $\mathbf F_{47}$ 为平方，令
$$
x_0=(2\omega+1)/\sqrt3,\qquad x_0^2=-1;
$$
换 $\sqrt3$ 的符号不改原 Cartan。
写 $x=Ax_0+w$。
$\omega$ 的共轭在 anti-commuting 平面上乘一个非平凡三次单位，
直接乘法给相对角
$$
-\frac12\operatorname{tr}\bigl(x\,\omega x\omega^{-1}\bigr)
 =\frac{3A^2-1}{2}.
\tag{1078.10}
$$
$\omega^2$ 给同一个角。
除 canonical Cartan $A=\pm1$ 外，
有效 $C_3$ 在 Cartans 上自由作用。
$\omega$ 和 $\omega^2$ 给两条不同分支，
在 fine 参数上分别为 $s\mapsto\zeta_3s$ 和
$s\mapsto\zeta_3^{-1}s$；
二者与 diagonal 的交长各为一。

$R_A(y_3)$ 的相同 coarse 目标点则有拉回重数三。
因此 fixed cycle 的这一部分为
$$
\frac23(\mathcal F_3^*R_C)(y_3).
\tag{1078.11}
$$
该论证也包含 $A=0$ 的二十四度轨道；
它分成八个实际 coarse 点，每点重数三。
没有把两条 fixed branches 合并成一条。

## 3. 全部 cusps 的 fixed branches

原每个 cusp 的 width 为 $47$。
在原 Tate full-level 参数上，取
$$
u=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
x=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad
a^2+bc=-1.
$$
这里 $c\ne0$，否则 $-1$ 是平方。
同一 cusp 的非恒等 branches 为
$u^n x u^{-n}$，$n\in\mathbf F_{47}^{\times}$。
它们两两给不同的 Cartans：
若两项相差符号，lower-left entry 已迫符号为正；
剩下的等式会使一个非平凡 $47$ 阶 unipotent
正规化非分裂 Cartan，这是不可能的。

矩阵乘法给
$$
\operatorname{tr}(x u^n x u^{-n})=-2-n^2c^2.
$$
故定义
$$
n_C=
\#\{\,m\in\mathbf F_{47}^{\times}:\ 1+m^2/2=\pm C\,\},
\tag{1078.12}
$$
便是 $R_C$ 在每个原 cusp 的 fixed-branch 数。
$C=0$ 时两个符号是同一个条件，绝不能重复计数。
每个分支在参数 $q^{1/47}$ 上乘 $\zeta_{47}^{\,n}$，
特征零中与 diagonal 的交长为一。
因此完整 cusp cycle 是
$$
n_C D_\infty.
\tag{1078.13}
$$
本段“交长一”只指这个泛纤维 fixed divisor；
不把它挪成坏 $47$ 整模型中的交数断言。

## 4. 完整 fixed divisor 和 trace

一般 elliptic curve 的有效自同构群平凡，
故非恒等 Cartan correspondence 在 $j\notin\{0,1728,\infty\}$
处没有 fixed points。
结合 §§2–3，得到**原粗模除子**等式
$$
\boxed{\quad
\operatorname{Fix}R_C
 =\frac12(\mathcal F_4^*R_C)(y_4)
  +\frac23(\mathcal F_3^*R_C)(y_3)
  +n_C D_\infty.
\quad}
\tag{1078.14}
$$
虽然以分数书写，右边是整数有效 cycle，
其整数性已由全部 source/target 稳定子和各支交长逐点证明。

令 $E_i(C)=\deg(\mathcal F_i^*R_C)$。
对称有限对应的 Lefschetz 交数公式是
$$
\deg\operatorname{Fix}R_C
 =2d_C-\operatorname{Tr}(R_C\mid H^1_{\rm dR}(X))
 =2d_C-2\operatorname{Tr}(R_C\mid H^0(X,\Omega^1)).
$$
第二个等号用对称对应的 Hodge 两半共轭迹相同。
于是
$$
\boxed{\quad
\operatorname{Tr}(R_C\mid H^0(X,\Omega^1))
 =d_C-\frac{E_4(C)}4-\frac{E_3(C)}3-\frac{23\,n_C}{2}.
\quad}
\tag{1078.15}
$$

这已经给出所有二十三个 trace 的完整闭式。
为便于原有限算法直接读取，
令 $\epsilon$ 是 $\mathbf F_{47}$ 的 quadratic character，
并固定 $\epsilon(0)=0$。
当 $C\ne0,\pm1$ 时，
$$
E_4(C)=24\left(
 2+\epsilon\!\left(\frac{1+C}{2}\right)
  +\epsilon\!\left(\frac{1-C}{2}\right)\right),
\tag{1078.16}
$$
$$
E_3(C)=24\left(
 2+\epsilon\!\left(\frac{1+2C}{3}\right)
  +\epsilon\!\left(\frac{1-2C}{3}\right)\right),
\tag{1078.17}
$$
$$
n_C=2+\epsilon\bigl(2(C-1)\bigr)
       +\epsilon\bigl(-2(C+1)\bigr).
\tag{1078.18}
$$
每个非零平方根对 $\{\pm A\}$ 给一个四十八度对应。
若 (1078.17) 的某个 radicand 为零，它给一个 $A=0$，
其二十四度正好由 $\epsilon(0)=0$ 的那一项保留。
这是不用执行表格即可读取所有特殊角的精确规则。

$C=0$ 必须单列：
$$
E_4(0)=E_3(0)=48,\qquad n_0=0.
\tag{1078.19}
$$
因为 $1/2$、$1/3$ 在 $\mathbf F_{47}$ 都是平方，
而 $-2$ 非平方。
以上每个式子都在 $C\mapsto-C$ 下不变，未依赖任取的 sign 代表。

## 5. 一个明确的 trace-zero 原 cycle

由 (1078.6)–(1078.7)，直接纸算有
$$
\mathcal F_4^*R_0=R_{20},\qquad
\mathcal F_3^*R_0=R_4,\qquad
\deg\operatorname{Fix}R_0=56,
$$
所以
$$
\operatorname{Tr}R_0=24-28=-4.
\tag{1078.20}
$$
对 $C=2$，$A^2=3/2=25$ 给 $R_5$，
另一个 $-1/2=23$ 非平方；
两个 cubic radicands $5/3=33$、$-1$ 都非平方。
又 $2$ 是平方、$-6$ 非平方，因此
$$
\mathcal F_4^*R_2=R_5,\qquad
\mathcal F_3^*R_2=0,\qquad n_2=2,
$$
$$
\deg\operatorname{Fix}R_2=24+46=70,\qquad
\operatorname{Tr}R_2=48-35=13.
\tag{1078.21}
$$
于是实际对称、无 diagonal 的 cycle
$$
Z=13R_0+4R_2
\tag{1078.22}
$$
满足
$$
\deg Z=504,\qquad \deg\operatorname{Fix}Z=1008,\qquad
\operatorname{Tr}Z=0,
$$
以及完整等式
$$
\operatorname{Fix}Z
 =\left(\frac{13}{2}R_{20}+2R_5\right)y_4
   +\frac{26}{3}R_4 y_3+8D_\infty.
\tag{1078.23}
$$

本篇仅将 (1078.22) 作为准确的 trace-zero **cycle**。
没有证明其在 $J$ 上的 endomorphism 非零，
没有证明某个 good-prime degree-one Hecke character $\theta$ 满足
$\theta(Z)=0$，也没有计算相应全局高度的首项。
特别这种 $\theta$ 是指定局部 Hecke 块的残余 eigencharacter，
不能与 Chow–Heegner 平移类混为一物。

## 6. 原八个 CM 圆盘与后继高度的准确接口

[R1074 §9](R1074-certified-original-p47-eight-CM-disks.md)
已经在原八个 $\mathbf C_{47}$ tubes 上证明 $j$ 单射且 étale，
并支付所有非恒等 Cartan 支的几何支撑避让。
本篇的每个 $R_C$ 正是那里允许的实际对应。
因此，对同一 tube 中定义于有限 $L/\mathbf Q_{47}$ 的
$x,y$，以及任意 trace-zero 整组合 $Z'$，
$$
h_{47}\bigl(x-y,\operatorname{Fix}Z'-Z'(x)-Z'(y)\bigr)=0.
\tag{1078.24}
$$
(1078.14) 同时把其全局 fixed divisor 准确压成
$y_3,y_4$ 的**真实 Cartan-correspondence images**及全部 cusps。
不能将 $R_A y_i$ 替换成一个未付的 scalar 倍；
这正是后继需要原 Hodge/Hecke 矩阵的地方。

尚未完成的 good-prime 输入包括：
实际整微分格与局部 Hecke 分裂、指定 Mordell–Weil 对数或高度、
需要的 unit/非饱和读数以及最终深盘排除。
本篇不以有限 double-coset 分类替代其中任一项，
也不把固定 $47$ 的结果外推成 Serre 一致性完成标准。

## 7. 完整 association composition 与实际 trace pairing

本节同样是纸面证明，未执行二十三角的数值线性代数。
它把后继非零性检验化成完整、已识别的有限和，
不依赖另一个模曲线的微分模型。

### 7.1 原 genus 的独立付款

原 $j$-map degree 为 $1081$。
$j=1728$ 上有效 involution 稳定的 Cartans
为 canonical 那一个，以及与其反交换的二十四个，故 $e_2=25$。
$j=0$ 上有效三阶单位仅稳定 canonical Cartan，故 $e_3=1$。
全部 cusps 为二十三个，width 均为四十七。
因此 Riemann–Hurwitz 给
$$
g=1+\frac{1081}{12}-\frac{25}{4}-\frac13-\frac{23}{2}=73.
\tag{1078.25}
$$
此处的 $e_2,e_3$ 是原 coarse elliptic points，
不把全部 $j=1728,0$ fibers 的点数误作这两个数。

### 7.2 每一个 composition coefficient

在三维 $\mathbf F_{47}$ 空间 $\mathfrak{sl}_2$ 上取
$$
B(x,y)=-\frac12\operatorname{tr}(xy).
$$
相对于标准坐标 $(a,b,c)$，$B(x,x)=-a^2-bc$，
Gram determinant 为 $1/4$，是平方。
原 oriented generators 恰满足 $B(x,x)=1$。

固定两个不同 necklaces，并选 representatives $x,z$，
写 $D=B(x,z)\ne\pm1$。
对定向中间元 $y$ 加上
$$
B(y,y)=1,\qquad B(x,y)=A,\qquad B(y,z)=B.
$$
$\langle x,z\rangle$ 的 Gram determinant 是 $1-D^2\ne0$。
线性约束唯一确定其在这平面上的投影 $y_0$，且
$$
1-B(y_0,y_0)
 =\frac{\Delta(A,B,D)}{1-D^2},\qquad
\Delta(A,B,D)=1+2ABD-A^2-B^2-D^2.
$$
正交补直线的 norm 有 squareclass $1-D^2$，
因为整个三维 Gram determinant 是平方。
所以定向解数准确为 $1+\epsilon(\Delta)$。

下降到 $y\sim-y$ 时必须保所有符号。
对 $A,B,D$ 都是 (1078.4) 的角类，令
$n_{A,B}^{D}$ 为 $R_AR_B$ 在 $R_D$ 上的 coefficient。
若 $A,B\ne0$，四组符号约束按 $y\mapsto-y$ 除以二，给
$$
n_{A,B}^{D}
 =2+\epsilon(1+2ABD-A^2-B^2-D^2)
    +\epsilon(1-2ABD-A^2-B^2-D^2).
\tag{1078.26}
$$
若恰一个角为零，则
$$
n_{A,B}^{D}=1+\epsilon(1-A^2-B^2-D^2).
\tag{1078.27}
$$
若两个角均为零，则只剩一组约束，给
$$
n_{0,0}^{D}=\frac{1+\epsilon(1-D^2)}2.
\tag{1078.28}
$$
$D$ 已经代表一个固定的目标 necklace；
即使 $D=0$，也不在这些 coefficient 上另除二。

端点是同一个 necklace 时，两个邻接角必须相同，
中间 necklaces 数为 $d_A$。所以完整实际对应恒等式为
$$
\boxed{\quad
R_AR_B=\mathbf1_{A=B}d_A\,\operatorname{id}
       +\sum_{D\in\mathbf F_{47}/\pm,\ D\ne\pm1}
            n_{A,B}^{D}R_D.
\quad}
\tag{1078.29}
$$
这里 $A=B$ 是角类相同，不是预选 representatives 同号。
因为两个输入都非恒等，中间元不可能误等于任一端点。
(1078.26)–(1078.28) 在各 sign 选择下不变，
并在 $A,B$ 间对称，故这些实际对应组成交换代数。

恒等式先在 generic finite level fiber 中逐点成立；
各 composition 是有限 correspondence 的 cycle，
故紧化后由 generic multiplicities 唯一决定。
椭圆点和 cusps 的 specialization 仍保原拉回长度，
不能把重合后的 coarse 点重新按一计算。

### 7.3 实际 Rosati 非零性证书的准确有限靶

记 $\tau_C$ 为 (1078.15) 的完整 trace。
由 (1078.29)，全部实际 trace pairing 给为
$$
\operatorname{Tr}(R_AR_B\mid H^0(X,\Omega^1))
 =73\,\mathbf1_{A=B}d_A+\sum_D n_{A,B}^{D}\tau_D.
\tag{1078.30}
$$
另有原 finite-fiber 恒等式
$\operatorname{id}+\sum_CR_C=j^*j_*$。
它经 genus-zero $X(1)$ 因子，在 $J$ 上为零，故
$$
73+\sum_C\tau_C=0.
\tag{1078.31}
$$
这是后继完整角表必须满足的来源检查。

每个 $R_C$ 对称，所以其 Jacobian endomorphism 对 Rosati 自伴。
对任意有理整组合 $F$，在复 Hodge 空间上其 eigenvalues 为实数，
因此 $\operatorname{Tr}(F^2)\ge0$；
等号成立当且仅当 $F$ 在 Hodge 空间为零，
也当且仅当其实际 Jacobian endomorphism 为零。
因此 (1078.30) 的有理 rank 正是原角代数在 $J$ 上 image 的维数。
这不是以抽象 permutation representation 的 rank 替代实际 Jacobian rank。

特别对 (1078.22)，
$$
\operatorname{Tr}(Z^2)
 =73\cdot4824+\sum_D b_D\tau_D,
\tag{1078.32}
$$
其中
$$
\begin{aligned}
b_D={}&\frac{169}{2}(1+\epsilon(1-D^2))
       +104(1+\epsilon(-3-D^2))\\
     &+16\bigl(2+\epsilon(-7-D^2+8D)
                  +\epsilon(-7-D^2-8D)\bigr).
\end{aligned}
$$
这里 identity coefficient 为 $169\cdot24+16\cdot48=4824$。
本文只给完整可核有限式，尚不登记其数值或非零结论；
任何程序核验必须按根规矩在审查后的公开 CI 执行。

## 8. 来源与审查

- R94 §1 已自足构造原 necklace 的中央非分裂对合与真正 incidence；
  本篇使用同一个 moduli 对象，新增完整角分类和全部 fixed cycles。
- M. Rebolledo–C. Wuthrich,
  *A moduli interpretation for the non-split Cartan modular curve*,
  Glasgow Math. J. **60** (2018), §§2–4：
  [作者全文](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。
  原 full-level / Cartan 模解释及 cusp width 沿用其已发表来源。
  本篇所有角轨道数、CM 支、粗模重数和 cusp fixed-branch 数均在正文重证。
- R43 §4 支付规范 QC 局部高度与真实 Néron pairing 的已发表比较；
  R1074 §9 支付此处全部原坏 $47$ 圆盘及 raw 支撑。
- M. Jaswal 2026 年 $X_{\rm ns}^+(121)$ 预印本 §4
  提供只改变 Cartan 的构造线索。
  本篇**不引用其未发表命题作为证明输入**，
  而在原 prime-$47$ 曲线上完整证明 (1078.1)–(1078.24)，
  不带入其 level-$121$ 数值、rank 或高度结论。

o2_high_coefficient 已对 §§1–4 的三类局部 fixed-cycle
逐式独立纸审，特别核准二倍/三倍粗模长度、
两条 cubic 分支、$C=0$ 不重计与泛纤维交长范围。
本篇未运行数学程序。
