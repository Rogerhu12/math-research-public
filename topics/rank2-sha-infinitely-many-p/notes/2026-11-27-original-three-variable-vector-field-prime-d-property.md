# 原三变量 Theta 向量场的全稳定素簇、截断 D-property 与小长度根理想

日期：2026-11-27 UTC。**状态：本文全部代数分类、截断相容和局部 Artin 引理已证明。尚未声称正特征的立方重数界，亦未据此排除原 canonical 坏条件。**

本文保持 R525/R526 的同一个实际 Theta 低轴，考察三变量多项式导子
$$
\begin{aligned}
V_0&=6t(1-t)\partial_t+
 \left((1+2t)X+\frac23t\right)\partial_X,\\
V&=V_0+6(1-t)XY\partial_Y.
\end{aligned}
\tag{1}
$$
其原点是 $(0,0,1)$，为真正奇点。这里 $X=t\theta'/\theta$、$Y=\theta$；不把 $(1)$ 当作已经给出一条特征 $p$ 的无限形式解。

主要结论是：在原好惰性特征中，$(1)$ 的非零稳定素理想均含有一个沿原截断弧消失阶不超过 $1$ 的元素。这个结论对**全部次数的素理想**成立。正特征中任意 $(f^p)$ 都可能稳定而其根理想不稳定，故素理想结论与非约化消元之间仍有独立费用；第6节给出长度严格小于 $p$ 时的准确补桥。

## 1. 原系数域与 R525 的全局可分障碍

设
$$
p=6s-1>83,\qquad \Bbbk\text{ 为完美特征 }p\text{ 域}.
$$
所有论证可先扩到 $\overline{\Bbbk}$；下列显示式本身均在原域上。

R525 §1(2)–(7) 已证明：
$$
F\in\Bbbk[t,X]\text{ 不可约},\quad \deg_XF>0
\quad\Longrightarrow\quad F\nmid V_0F.
\tag{2}
$$
该结论没有 $\deg_XF<p$ 的假设。为明确本次应用的范围，重述其短证明。

假设某个有限可分扩张 $L/\Bbbk(t)$ 中有解
$$
6t(1-t)\partial_t X=(1+2t)X+\frac23t.
$$
置
$$
H=t^s(1-t)^{3s-1},\qquad
f(t)=\frac1{9t^s(1-t)^{3s}}.
$$
由 $6s=1$ 在 $\Bbbk$ 中成立，
$$
\partial_t(X/H)=f(t).
\tag{3}
$$
$f(t)\,dt$ 在 $0$ 的留数是
$$
\frac19\binom{4s-2}{s-1}\ne0,
\tag{4}
$$
因为涉及的阶乘指标均小于 $p$。$\partial_t$ 唯一延拓到可分扩张 $L$，且 $\partial_t^p$ 作为导子在 $\Bbbk(t)$ 上为零，故在 $L$ 上也为零。但 $(4)$ 给 $\partial_t^{p-1}f$ 一个非零的 $t^{-p}$ 主项，与 $(3)$ 矛盾。

若不可约 $F$ 满足 $F_X\ne0$，$F\mid V_0F$ 会在其可分根域产生上面的解。若 $F_X=0$，该整除要求
$$
F\mid 6t(1-t)F_t.
$$
因 $\deg_XF>0$，可得 $F\mid F_t$；次数迫 $F_t=0$。完美性遂使 $F$ 为 $p$ 次幂，与不可约性矛盾。这证明 $(2)$，并保留了非可分情形。

因此 $\Bbbk[t,X]$ 的稳定素超曲面准确只有
$$
t=0,\qquad t=1.
\tag{5}
$$
纯 $t$ 不可约因子若稳定，须整除 $t(1-t)$；不存在第三个边界。

## 2. 一个完整的有理对数导数引理

令 $K=\Bbbk(t,X)$。对任意 $f\in K^\times$，若
$$
\frac{V_0f}{f}\in\Bbbk[t,X],
$$
则存在 $g\in K^\times$ 和整数 $a,b$，可取 $0\le a,b<p$，使
$$
\boxed{
f=g^p t^a(1-t)^b,\qquad
\frac{V_0f}{f}=6\{a(1-t)-bt\}.
}
\tag{6}
$$

证明：在唯一分解环 $\Bbbk[t,X]$ 中写
$$
f=c\prod_Q Q^{e_Q},\qquad e_Q\in\mathbf Z.
$$
若 $p\nmid e_Q$，则在素因子 $Q$ 处，$V_0f/f$ 的正规性要求 $Q\mid V_0Q$；其它因子的项在该处正规，不能抵消这个分母。由 $(2)$–$(5)$，这样的 $Q$ 只能是 $t$ 或 $1-t$。其余指数均为 $p$ 的倍数，常数也有 $p$ 次根；将两边界指数除以 $p$ 的整倍数吸收入 $g^p$，即得第一式。直接对 $t^a(1-t)^b$ 微分给第二式。

特别，
$$
\boxed{\ker(V_0:K\longrightarrow K)=K^p.}
\tag{7}
$$
因为 $(6)$ 的多项式为零先迫 $a=0$，再迫 $b=0$。更关键的是：$(6)$ 的右边**不含 $X$**，故对 $c\in\Bbbk^\times$，
$$
\frac{V_0f}{f}=c(1-t)X
\quad\text{无非零有理解}.
\tag{8}
$$
这不是把一个对数形式的留数条件当作充分条件，而是由所有原素因子的完整赋值逐项得到。

## 3. 三变量稳定素超曲面的全分类

**命题1。** $\Bbbk[t,X,Y]$ 中 $(1)$ 的稳定素超曲面准确为
$$
\boxed{t=0,\qquad t=1,\qquad Y=0.}
\tag{9}
$$
没有任何次数门。

证明：设 $P$ 不可约、$P\mid VP$。若 $\deg_YP=0$，由第1节直接得到前两个超曲面。以下令 $\deg_YP>0$，并写
$$
P=\sum_{i=0}^m P_i(t,X)Y^i.
$$
$V$ 不增加 $Y$ 次数。因此 $VP=AP$ 的多项式 cofactor 满足
$$
A\in\Bbbk[t,X],
\tag{10}
$$
包括 $VP=0$ 时取 $A=0$；不能在这里引入依赖 $Y$ 的 cofactor。

若 $P_0=0$，则 $Y\mid P$，不可约性迫 $P$ 为 $Y$ 的非零常数倍。故只须排除 $P\ne Y$ 且 $P_0\ne0$ 的情形。逐系数比较 $(10)$：
$$
V_0P_i+i\,6(1-t)XP_i=AP_i.
$$
对每个非零 $P_i$，取 $f_i=P_i/P_0\in K^\times$，得到
$$
\frac{V_0f_i}{f_i}=-i\,6(1-t)X.
\tag{11}
$$
第2节迫 $i=0$ 于 $\Bbbk$，即每个存活指标均被 $p$ 整除；随后 $(7)$ 又给
$$
P_i/P_0=g_i^p,\qquad g_i\in K.
$$
于是
$$
\frac P{P_0}
 =\left(\sum_{p\mid i}g_iY^{i/p}\right)^p
 \quad\text{在 }K[Y]\text{ 中}.
\tag{12}
$$
括号的 $Y$ 次数为正。原不可约 $P$ 关于 $Y$ 是 primitive，多项式 Gauss 引理使其在 $K[Y]$ 中仍不可约；$(12)$ 矛盾。

最后 $(9)$ 的三者确实稳定：
$$
Vt=6t(1-t),\quad V(t-1)=-6t(t-1),\quad
VY=6(1-t)XY.
$$
分类证毕。特别，正特征中两个存活 $Y$ 指数相差 $p$ 的可能性已由 $(12)$ 排除，不能只凭“指标不同”略过这一分支。

## 4. 更高余维的稳定素簇与常数1

**命题2。** 设 $\mathfrak p\ne(0)$ 为 $\Bbbk[t,X,Y]$ 的真稳定素理想。如果 $\operatorname{ht}\mathfrak p\ge2$，则
$$
\boxed{t\in\mathfrak p\quad\text{或}\quad t-1\in\mathfrak p.}
\tag{13}
$$

证明：令 $\mathfrak q=\mathfrak p\cap\Bbbk[t,X]$。它是 $V_0$ 稳定素理想。因 $\dim\Bbbk[t,X,Y]/\mathfrak p\le1$，若 $\mathfrak q=0$，商域将包含超越次数2的 $\Bbbk(t,X)$，矛盾。因此 $\mathfrak q\ne0$。

若 $\mathfrak q$ 高度1，由 $(5)$ 得到 $(13)$。若其高度2，剩余域是 $\Bbbk$ 的有限代数扩张；完美性使其可分，诱导的 $\Bbbk$-导子为零。故在该域中 $6t(1-t)=0$，仍得 $(13)$。这也覆盖三维的稳定闭点。

在原点 $(0,0,1)$ 经过的每一个非零真稳定素簇，因而都含 $t$。不经过该点者已有某个不消失的函数。沿任意以 $t$ 为第一坐标的弧、且 $X(0)=0,Y(0)=1$，
$$
\boxed{
\min_{f\in\mathfrak p}\operatorname{ord}_t f(t,X(t),Y(t))\le1.
}
\tag{14}
$$
具体而言，$(Y)$ 与 $(t-1)$ 已有阶0元素，包含 $(t)$ 的理想有阶1元素。

这里所谓素理想的 D-property 常数为 $1$，严格指 $(14)$；尚未把它扩成所有非约化稳定理想的同一阶界。

## 5. 原实际低轴的截断相容

现在只使用 R525(1)、R526 已付的真实低轴：
$$
\theta(0)=1,\qquad x=t\theta'/\theta,\qquad x(0)=0,
$$
$$
6t(1-t)x'-(1+2t)x-\frac23t=0\pmod{t^s}.
\tag{15}
$$
取
$$
\operatorname{ev}_s:\Bbbk[t,X,Y]\longrightarrow
 \Bbbk[t]/(t^s),\qquad
(t,X,Y)\longmapsto(t,x,\theta).
$$
链式法则准确给
$$
\boxed{
\operatorname{ev}_s(VF)
 =6t(1-t)\partial_t\operatorname{ev}_s(F)\pmod{t^s}
 \quad(F\in\Bbbk[t,X,Y]).
}
\tag{16}
$$
$Y$ 方程来自 $x=t\theta'/\theta$，原 $X$ 方程的全部误差在 $(t^s)$；没有使用该窗之后的任何系数。$t\partial_t$ 保理想 $(t^s)$，所以右边确实定义了截断环上的导子。

因此
$$
\boxed{
J_s:=\ker\operatorname{ev}_s\quad\text{满足}\quad VJ_s\subset J_s.
}
\tag{17}
$$
$\operatorname{ev}_s$ 满射，故
$$
\dim_\Bbbk\Bbbk[t,X,Y]/J_s=s,\qquad
\sqrt{J_s}=(t,X,Y-1).
\tag{18}
$$
对任一稳定素理想，定义其截断接触阶为所有非零可见评价阶的最小值，并把零评价的阶记为 $s$。第4节直接给这个截断接触阶不超过1。

还有一个可供后继截断 Rolle 论证使用的准确式。若
$$
1\le h=\operatorname{ord}_t\operatorname{ev}_s(F)<s,
$$
则 $h<p$，$(16)$ 的首系数乘 $6h\ne0$，所以
$$
\boxed{
\operatorname{ord}_t\operatorname{ev}_s(VF)=h.
}
\tag{19}
$$
若评价为零模 $t^s$，其导数评价仍为零。阶0时没有声称导数仍为阶0。

$(15)$ 在特征 $p$ 下不能被提升成一个没有障碍的无限形式解；第1节的同一非零留数正显示该做法不合法。后继任何重数估计必须真正以 $(16)$–$(19)$ 的有限环为输入。

## 6. 长度小于p时，稳定理想的根确实稳定

**引理3。** 设 $R$ 为特征 $p$ 的环，$D$ 为导子，$I$ 为 $D$ 稳定理想。令 $\mathfrak p$ 是 $I$ 的一个最小素理想，假设
$$
e=\operatorname{length}_{R_{\mathfrak p}}
 (R_{\mathfrak p}/I_{\mathfrak p})<p.
\tag{20}
$$
则 $D\mathfrak p\subset\mathfrak p$。

证明：导子按商法则延拓到 $R_{\mathfrak p}$，并保持 $I_{\mathfrak p}$，故作用于局部 Artin 环
$$
A=R_{\mathfrak p}/I_{\mathfrak p}.
$$
设 $\mathfrak m$ 为其极大理想。对 $a\in\mathfrak m$，取最小正整数 $m$ 使 $a^m=0$；局部长度给 $m\le e<p$。如果 $Da$ 在 $\mathfrak m$ 外，则它为单位，而
$$
0=D(a^m)=m a^{m-1}Da
$$
迫 $a^{m-1}=0$，矛盾。因此 $D\mathfrak m\subset\mathfrak m$。局部化后再收缩，得到 $D\mathfrak p\subset\mathfrak p$。

这同时说明严格不等号的必要性：在 $\Bbbk[u]$ 上取 $D=\partial_u$，$(u^p)$ 稳定，局部长度恰为 $p$，但其根 $(u)$ 不稳定。

引理只在显示的局部长度条件下使用；未称任意全局 primary 分解都逐项受导子保持。若后继消元森林给每个实际局部长度一个 Bézout 上界 $E$，则 $p>E$ 才能逐处使用本引理，接第4节的稳定素簇分类。

## 7. 已支付范围与尚待证明的立方重数门

本文给出了后继正特征重数论证所需的三个具体输入：

- 全次数稳定素簇分类 $(9)$、$(13)$，及原点接触常数1；
- 同一原低轴的稳定截断核 $(16)$–$(19)$，不造不存在的无限特征 $p$ 解；
- 小于 $p$ 的实际 primary 长度到稳定素理想的引理3。

还不能直接写出 $\operatorname{ord}P(t,x,\theta)\le C(D+A)^3$。其余必须支付的步骤是：对实际低次数 $P$ 构造次数受控的消元森林，证明其需要的求导次数、交数及 primary 长度均在已声明界内，并在 $(t^s)$ 中证明对应的截断重数比较。仅引用特征零复解析曲线定理，或仅用素理想分类替代所有非约化理想，均不足。

如果后继得到立方界，还须要求拟读取的接触长度严格在原 $s$ 窗内，再代入 R525 §4 的同一个完整 $M$ 必要投影。原 Gaussian、两次进位、固定 conductor 与完整来源核仍按原式保留。本文没有增加来源列、独立中央零、或多项式乘积闭性，也未执行任何新的数学计算。

主要原记录：

- [R525 — 原低轴的多权 Wronskian 零估计](../results/R525-original-multiweight-wronskian-and-growing-kernel-support.md)：实际全局障碍与 $(2)$ 对应其 §1(2)–(7)，真实截断与完整 $M$ 在其 §2、§4。
- [R526 — 原 Theta 对数方程与两权核排除](../results/R526-original-theta-logarithmic-zero-bound-and-two-weight-kernel-exclusion.md)。


## 8. 固定低次数的统一有限阶退出：不借特征零轨道

本节另付森林的低次数步骤。常数只取决于固定的原导子
$V$ 和一个固定整数 $d_0$；不随剩余特征、待测多项式系数或
待测素簇改变。后继可取 $d_0=864$，这里不宣称已经算出有效最小值。

令 $\mathbf z=(t,X,Y)$，给所有 $|\alpha|\le d_0$ 引入有限个独立参数
$a_\alpha$，并在
$$
R_{\rm univ}
 =\mathbf Z[1/6,\{a_\alpha\}_{|\alpha|\le d_0},t,X,Y],
\qquad
P_{\rm univ}=\sum_{|\alpha|\le d_0}a_\alpha\mathbf z^\alpha
$$
中延拓 $V$，规定 $Va_\alpha=0$。
参数个数虽大但有限，故 Hilbert 基定理使此环 Noetherian。
升链
$$
I_j=(P_{\rm univ},VP_{\rm univ},\ldots,V^jP_{\rm univ})
$$
于某个固定 $M$ 稳定。可增大 $M$ 使 $M\ge1$。
稳定等式 $I_M=I_{M+1}$ 是有限多项式线性组合的等式；
它不是一个需要假定平坦性的几何纤维结论。

因此对任一特征 $p>3$ 的代数闭域 $\Bbbk$，以及任一
非零 $P\in\Bbbk[t,X,Y]$、$\deg P\le d_0$，把 $a_\alpha$
专门化为 $P$ 的系数，准确得到
$$
J=(P,VP,\ldots,V^MP),\qquad VJ\subset J.
\tag{21}
$$
该专门化与导子相容；即使某些生成元或系数变零，有限线性
组合仍然成立。这里没有无限多个参数，也没有新增依赖 $p$
的分母。

因 $\deg V\le3$，保守地置
$$
L=d_0+3M .
$$
$(21)$ 的所有生成元的总次数至多 $L$。
若 $J\ne R$，令 $\mathfrak q$ 为其任一最小素理想，
$c=\operatorname{ht}\mathfrak q\le3$。在无穷域上可取
$c$ 个这些生成元的通用常系数线性组合 $G_1,\ldots,G_c$，
使 $\mathfrak q$ 在 $(G_1,\ldots,G_c)$ 中仍为一个孤立分量。
具体地，在正则局部环 $R_{\mathfrak q}$ 中逐次避开有限个
极小素理想，取得一个参数理想。其每个生成元的次数仍至多 $L$。
局部理想包含与该孤立分量的 Bézout 交数于是给
$$
\begin{aligned}
e_{\mathfrak q}
&:=\operatorname{length}_{R_{\mathfrak q}}
                  (R_{\mathfrak q}/JR_{\mathfrak q})\\
&\le
 \operatorname{length}_{R_{\mathfrak q}}
          (R_{\mathfrak q}/(G_1,\ldots,G_c)R_{\mathfrak q})
 \le L^c\le L^3 .
\end{aligned}
\tag{22}
$$
最后一步是 $c$ 个次数不超过 $L$ 的超曲面在一个余维 $c$
孤立分量上的交重数界；其正整数分量次数至少为1。
$(22)$ **只**讨论最小素分量，不对 embedded primary 长度
作未经证明的声称。

若
$$
p>L^3,
\tag{23}
$$
第6节的局部引理逐个使所有这些 $\mathfrak q$ 成为 $V$ 稳定
素理想。无需先声称任意正特征根理想自动稳定，再从中分解。

由此得到所需结论：

**命题4（固定低次数退出）。** 设 $(23)$ 成立，
$Z\subset\mathbf A^3_\Bbbk$ 为不可约真簇，并且 $Z$ 不包含于
任何非零真 $V$ 稳定素理想定义的簇。若
$0\ne P\in I(Z)$、$\deg P\le d_0$，则存在
$$
\boxed{1\le j\le M\quad\text{使}\quad V^jP\notin I(Z).}
\tag{24}
$$

若反之 $(21)$ 的所有生成元均在 $I(Z)$ 内，则 $J\subset I(Z)$。
取包含于 $I(Z)$ 的一个最小素理想 $\mathfrak q$；
因 $P\ne0$，$\mathfrak q\ne0$，且它是真理想。
$(22)$–$(23)$ 与第6节使 $\mathfrak q$ 稳定，故
$Z\subset V(\mathfrak q)$，直接矛盾。命题证毕。

这是一个固定的有限坏素数排除及统一有限阶存在结论。
没有在不存在的无限特征 $p$ 轨道上求 Taylor 展开，也没有把
未知 $M$ 写成已经计算的有效常数。高次数最小方程、三层实际
交循环和原 $s$ 窗内的截断重数比较仍须继续给出；本命题不独自
排除原完整 $M$ 的临界核。
