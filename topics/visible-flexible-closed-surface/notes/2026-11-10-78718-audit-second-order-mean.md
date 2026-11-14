# 二阶平均兼容条件消去稿：完整未参与者独立审查

**结论：接受作者稿全部八节的准确数学范围，无阻断修改。**

审者：`independent_audit`，会话 Astra-visible-flex-78718bd0，2026-11-10。
审者未参与原作者推导、R58 的构造或本轮新数值候选的构造/调参。
本次逐节重推全部所需公式，而非抽查、转述既有审稿或只核文本哈希。
没有运行 ODE/PDE/BVP，没有生成或读取数值候选数组；没有新增闭面证书。

## 1. 本次实际读取的冻结文本与审查边界

主稿：

- `notes/2026-11-10-db6f-root-second-order-mean-compatibility-v1.md`，
  10,659 字节，SHA256
  `7a5147c433e7ce7ba190729bf8319798891dbdbc0d8c48a930c9b7219e94de3b`。
- 依赖 `results/R58-radial-cap-linear-matching-conditions.md`，
  23,680 字节，SHA256
  `cddbe456b36e643c07932940f9514511ae9243411f96f0f48a4f390600fdf972`。
- R58 的作者原文
  `notes/2026-11-10-db6f-radial-cylinder-cap-linear-matching-v1.md`，
  22,996 字节，SHA256
  `a93f8a74f2a23726dd93310d41c85b27499311ed8634c57b37453e48907c9c62`。

主稿八节、正式 R58 全文均实际阅读。本审查重新验证主稿所需的
Gauss–Codazzi、线性化、轴高变元和球心模态；不把本次工作称为对 R58
所有其它结论（例如高频解析障碍、端口拼接）的重新完整独审。

准确结论是条件性的：固定一个具有开单位柱入口、正轴向速度和球心开核心的
旋转基态，对其**已经给定的全盘光滑线性第二形式解**，二阶零角模态的
积分兼容条件自动成立。没有构造一阶解，更没有构造非线性帽族。
主稿未调用尚待审查的无限共振模态稿，故不依赖该稿是否最终成立。

## 2. 原方程、两阶展开和平均必要条件（对应作者 §§1–2）

用共同材料度量

$$
g=dr^2+a(r)^2du^2,
\qquad F_0=(a\cos u,a\sin u,Z),
\qquad Z_r=b=(1-a_r^2)^{1/2}>0
$$

和定向法向 $N_0=-b e_{\rm rad}+a_r e_z$，直接计算得到

$$
M_0=0,\qquad C_0=ab,\qquad L_0=-a_{rr}/b.
$$

Gauss–Codazzi 的符号为

$$
LC-M^2=-aa_{rr},\qquad
M_r=L_u-(a_r/a)M,\qquad
C_r=M_u+(a_r/a)C+aa_rL.
$$

以无阶乘的系数展开 $L=L_0+\tau\ell+\tau^2\ell_2+\cdots$，
$M=\tau m+\tau^2m_2+\cdots$，$C=ab+\tau c+\tau^2c_2+\cdots$，有

$$
ab\ell-(a_{rr}/b)c=0,
$$

$$
ab\ell_2-(a_{rr}/b)c_2+\ell c=m^2.
$$

故

$$
\ell=\frac{a_{rr}c}{ab^2},\qquad
\ell_2=\frac{a_{rr}c_2}{ab^2}+S,
\qquad
S=\frac{m^2}{ab}-\frac{a_{rr}c^2}{a^2b^3}.
$$

由 $b_r/b=-a_ra_{rr}/b^2$，对 $x=am$、$\zeta=bc/a$ 求导时，
所有零阶线性项抵消，得

$$
x_r=P\zeta_u,\qquad \zeta_r=Rx_u,
\qquad P=\frac{aa_{rr}}{b^3},\quad R=\frac b{a^2}.
$$

二阶代入相同线性消元时，来自 $S$ 的项分别是 $aS_u$ 和 $ba_rS$：

$$
(x_2)_r=P(\zeta_2)_u+aS_u,\qquad
(\zeta_2)_r=R(x_2)_u+ba_rS.
$$

没有遗漏阶乘、符号或第二个非齐次项。
角平均后第一式右端为零，第二式给
$\langle\zeta_2\rangle_r=ba_r\langle S\rangle$。
共同单位速率平面凸柱边的总曲率为 $2\pi$，故其二阶平均曲率系数为零；
共同垂直 conormal 给 $M_\tau(0,u)=0$。
真实中心正则给 $\zeta_2\to0$。因此作者式 (7) 确是这一几何范围内的
二阶平均必要条件。本定理随后只用线性解即证明它成立，无循环假设非线性族。

## 3. 轴高变元、模态方程与低模排除（对应作者 §3）

去中心域内 $dZ/dr=b>0$，故 $A(Z)=a(r(Z))$ 合法，而且

$$
A_Z=a_r/b,\qquad
A_{ZZ}=a_{rr}/b^4.
$$

后一式的独立计算是

$$
\frac1b\left(\frac{a_r}{b}\right)_r
=\frac{a_{rr}b-a_rb_r}{b^3}
=\frac{a_{rr}(b^2+a_r^2)}{b^4}
=\frac{a_{rr}}{b^4}.
$$

Fourier 第 $n\ne0$ 模给

$$
x_n=\frac{A^2}{in}(\zeta_n)_Z,
\qquad
\bigl(A^2(\zeta_n)_Z\bigr)_Z+n^2AA_{ZZ}\zeta_n=0.
$$

取 $y_n=A\zeta_n$ 后，

$$
\bigl(A^2(\zeta_n)_Z\bigr)_Z
=A(y_n)_{ZZ}-A_{ZZ}y_n,
$$

所以

$$
(y_n)_{ZZ}+(n^2-1)(A_{ZZ}/A)y_n=0.
$$

开柱入口 $A=1$、$A_Z=0$ 和 $m(0,u)=0$ 给 $(y_n)_Z(0)=0$。
全盘光滑 Cartesian 张量给一致的 $m=O(a)$、$c=O(a^2)$；在球核心
$b=a/\sigma$，故 $x=O(a^2)$、$\zeta=O(a^2)$。

- $n=0$：$x_0$ 和 $\zeta_0$ 均为常数，中心极限迫使它们为零。
- $n=\pm1$：$y_{ZZ}=0$，入口零导数使 $y$ 常数，而中心
  $y=A\zeta\to0$ 使其为零。
- $|n|\ge2$：球核心中令 $t=\tan(\rho/(2\sigma))$，
  则 $d\log t/d\rho=1/a$。原一阶系统或二阶 ODE 的两支恰为
  $t^{|n|}$ 与 $t^{-|n|}$。后者与真实中心有界性矛盾，因此仅剩
  $\zeta_n=d_n t^{|n|}$。

作者没有用“极坐标系数有界”替代 Cartesian 光滑，也没有从逐模正则推断
一个未经控制的无穷级数光滑。本定理一开始就给定真实光滑张量。

## 4. 全段边界原函数的逐项验证（对应作者 §4）

以下撇号均指 $d/dZ$。固定 $|n|\ge2$，置 $\lambda=n^2-1$、
$q=A''/A$，并按作者定义

$$
\mathcal B=AA'\operatorname{Re}(\overline\zeta\zeta')
-\tfrac12(AA''-(A')^2)|\zeta|^2,
\quad
\mathcal E=|y'|^2+\lambda q|y|^2.
$$

直接求导时，$\operatorname{Re}(\bar\zeta\zeta')$ 的系数先化为
$2(A')^2$；再用
$\zeta''=-2(A'/A)\zeta'-n^2(A''/A)\zeta$，该项精确抵消，留下

$$
\mathcal B'
=AA'|\zeta'|^2-n^2A'A''|\zeta|^2
-\tfrac12(AA'''-A'A'')|\zeta|^2.
$$

由 $y''=-\lambda qy$、$q$ 为实函数，能量交叉项也精确抵消：

$$
\mathcal E'=\lambda q'|y|^2.
$$

而 $AA'''-A'A''=A^2q'$、$|y|^2=A^2|\zeta|^2$，故

$$
\frac1{n^2}\left(\mathcal B+
\frac{\mathcal E}{2(n^2-1)}\right)'
=A'\left(\frac A{n^2}|\zeta'|^2-A''|\zeta|^2\right).
$$

本式没有除以 $q$、$a_{rr}$ 或它们的导数，对改变曲率符号、平坦区和
任意阶光滑转折均合法。$\mathcal E$ 无须非负，证明没有误用正能量论证。

## 5. 入口、球心和可积性（对应作者 §5）

入口开柱给 $A'=A''=q=y'=0$，因此 $\mathcal B(0)=\mathcal E(0)=0$。
球心设 $h=H-Z$，真实球面给 $A\asymp h^{1/2}$，
$A'=O(h^{-1/2})$、$A''=O(h^{-3/2})$、$q=O(h^{-2})$。
第 $N=|n|\ge2$ 稳定模满足

$$
\zeta=O(h^{N/2}),\quad \zeta'=O(h^{N/2-1}),\quad
y=O(h^{(N+1)/2}),\quad y'=O(h^{(N-1)/2}).
$$

$\mathcal B$ 和 $\mathcal E$ 的每一项均为 $O(h^{N-1})$，故中心极限为零。
原函数恒等式左侧每一项则为 $O(h^{N-2})$，含最坏的 $N=2$ 仍可积。
因此每个模态的全段积分确实为零，极限过程没有丢失端点通量。
同理，$q'|y|^2=O(h^{N-2})$ 可积，且 $\mathcal E$ 两端为零，
所以作者附带的 $\int q'|y|^2\,dZ=0$ 也成立。

## 6. 无限模的严格合并（对应作者 §6）

从原变量直接代入 $m=x/a$、$c=a\zeta/b$、$dr=dZ/b$：

$$
ba_rS\,dr
=A'\left(\frac{x^2}{A^3}-A''\zeta^2\right)dZ.
$$

实值性和给定 Fourier 归一化给
$\langle x^2\rangle=\sum_n|x_n|^2$，
$\langle\zeta^2\rangle=\sum_n|\zeta_n|^2$。
代入 $|x_n|^2=A^4|(\zeta_n)'|^2/n^2$，第 $n$ 项正是上一节已证零积分。
不存在遗漏负频率或额外因子 $2$ 的问题。

交换积分与无限求和必须控制绝对值，作者给的控制充分。
由实际全盘光滑性，中心附近

$$
\langle x^2\rangle+\langle\zeta^2\rangle=O(A^4).
$$

结合 $|A'|=O(A^{-1})$、$|A''|=O(A^{-3})$，得

$$
|A'|\left(A^{-3}\langle x^2\rangle
+|A''|\langle\zeta^2\rangle\right)=O(1).
$$

每个有限 Fourier 截断的平方和均不超过完整平方和，故这个关于 $Z$ 可积的
函数统一控制各截断的两项绝对值。中心以外的紧区间上则由光滑性控制。
支配收敛因而适用，并严格推出

$$
\int_0^Tba_r\langle S\rangle\,dr=0.
$$

这完成主定理，不需要模态支集有限、谱密度、解析边数据或非线性存在性。

## 7. 实际平均方程和球心解析例（对应作者 §7）

设

$$
\langle x_2\rangle=0,\qquad
\langle\zeta_2(r)\rangle=\int_0^rba_r\langle S\rangle\,ds.
$$

已证积分消去使它等于 $-\int_r^Tba_r\langle S\rangle\,ds$。
中心 $S=O(1)$、$ba_r=O(\rho)$，故 $\langle\zeta_2\rangle=O(\rho^2)$，
继而 $\langle c_2\rangle=O(\rho^2)$，$\langle\ell_2\rangle=O(1)$。
作者准确地只把一般情形称为平均径向方程的解和必要中心阶数，没有据此宣称
整个二阶张量 Cartesian 光滑。

对单一实稳定球心模式 $\zeta=d t^n\cos(nu)$，独立计算为

$$
x=-\sigma d t^n\sin(nu),\qquad c=\sigma d t^n\cos(nu),
\qquad a=\frac{2\sigma t}{1+t^2}.
$$

此时球核心内两项平方的角依赖精确相消，实际上 $S$ 本身就是径向函数：

$$
S=\frac{\sigma^3d^2t^{2n}}{a^4}
=\frac{d^2}{16\sigma}t^{2n-4}(1+t^2)^4.
$$

又

$$
ba_r=-\frac{2t(1-t^2)}{(1+t^2)^2},\qquad
\frac{dr}{dt}=-\frac{2\sigma}{1+t^2}.
$$

因此 $d\langle\zeta_2\rangle/dt=(d^2/4)(t^{2n-3}-t^{2n+1})$，
中心零初值积分得到作者式 (22)，所有常数和符号均正确。

写 $\alpha=\langle\ell_2\rangle$、
$\beta=\langle c_2\rangle/a^2$。
在 $n=2$ 时二者的中心极限均为 $d^2/(32\sigma)$；在 $n>2$ 时均为零。
$\alpha$、$\beta$ 都是 $t^2$ 的解析函数，且
$\alpha-\beta=t^2$ 乘一个 $t^2$ 解析函数。
在真实材料 Cartesian 图 $X=\rho\cos u,Y=\rho\sin u$ 中还须计入
$a/\rho$，但 $(a/\rho)^2=1+O(\rho^2)$ 本身为 $\rho^2$ 的解析函数。
于是

$$
\alpha\,d\rho^2+\beta a^2du^2
=\beta(a/\rho)^2(dX^2+dY^2)
+\frac{\alpha-\beta(a/\rho)^2}{\rho^2}(X\,dX+Y\,dY)^2
$$

的两个系数均在中心解析。这补明了作者单模平均张量的 Cartesian 解析结论。

非阻断的阅读澄清：单模球心核心内的 $S$ 恰为零角模；作者末句提及的
$\pm2n$ 模问题应理解为完整帽域上的二阶边值系统，它们可在非球形桥段出现。
无论这一局部抵消如何，作者从未宣称已经解了完整域的非零模。

## 8. 全文结论及不能从中取得的事项（对应作者 §8）

接受主稿所有八节。可正式登记为“已证明：指定共同径向旋转基态上，
每个给定的真实光滑、两端匹配的一阶解，其二阶平均积分兼容自动成立”。
该结论修正一种可能误判：不能把 $ba_rS$ 的零模直接当作新的独立平均障碍。

仍未支付且本次独审不支付：非零二阶模态的边值兼容、任意高阶可积性、
稀疏共振支集上的固定开弧数据、实际非线性帽族、与强环带接合、闭面、
全时间 reach 与幅度、flat17 的 G5、网格或原种子完整独立重跑。

本审者本轮保持未参与新数值候选优化；本次纯数学独审不改变该独立身份。
