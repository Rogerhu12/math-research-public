# R388：原第二整商的全局 forcing、低轴微分式与首共振

日期：2026-11-14。**状态：已证明。** R385 的确定低轴 $A_0^\sharp$ 有一个来自原第二整商的全局有理 forcing；两次整除均在同一个平坦整环中成立。本文给出保原测试零、没有新移动极的有限 primitive，并支付其完整固定极界。原 $t$ 轴上的二阶递推、首共振及 R382 坐标 $C_0$ 的单位 carry 同时保留。该单位 carry 是坐标补偿，不能用作新的中央非零输入。

## 1. 同一数据和整环

取 R385 的
$$
p=6s-1>83,\quad b=17,\quad
E_b:y^2=x^3+b,\quad t=-b/x^3,\quad D=D_z,
$$
$$
\mathcal A=\mathcal O[x,y,1/y]/(y^2-x^3-b),\qquad
a_E=x^2/y,\qquad f=-x.
$$
该 $\mathcal O$ 代数平坦，约化核恰为 $p\mathcal A$。
以下除以 $p$、$p^2$ 都先在这个整环中支付，不先把原点形式整性当全局整性。

仍用原 $\widetilde Z,Z,e,\mathfrak F_p,c_p$ 及有限 primitive
$\widetilde I,I_Z$。记
$$
\widetilde e=3\widetilde Za_E,\quad
\widetilde Z_1=\widetilde I(\widetilde e),\quad
\widetilde Z_2=\widetilde Z+p\widetilde Z_1,
$$
$$
G_2=G_\kappa^{(2),\sharp}
=\widetilde G_\kappa+pL,\qquad
L=(y/x)\widetilde r_1^\sharp\in\mathcal A.
\tag{1}
$$
这里 $L\bmod p=G_1+c_pZ^{p-1}Z_1$，$Z_1=I_Z(e)$。
所有提升都固定为 R385 允许的实际提升；本文公式随同一选择同步改变。

写
$$
u_\sigma=-[z^{p-1}]x,\qquad
u_\kappa=(p+1)a_\kappa/34=u_\sigma+p\delta_\kappa,
\quad \bar u_\kappa=-c_p.
\tag{2}
$$
原规范准确给
$$
D\zeta_\kappa=f-u_\kappa z^{p-1}.
$$
R385 的强普通比较使
$$
q_2=(\zeta_\kappa-G_2)/p^2
\tag{3}
$$
在所需有限 Laurent 窗口整；$G_2$ 的极部准确为 $1/z$，
所以 $q_2$ 在原点正规、型负一，从 $z^5$ 起。

## 2. 三个真实 Cartier 幂及保原点阶的提升

置
$$
C_e=D^{p-1}e,\qquad
C_F=D^{p-1}\mathfrak F_p.
$$
它们是原函数域中的 $p$ 次幂。R363、R385 已付
$$
C_e=O(z^{4p}),\qquad C_F=O(z^{6p}).
\tag{4}
$$
例如 $C_e$ 的原点型为二；R385 则准确消去了 $C_F$ 的常数。

取其唯一的 $p$ 次根
$$
B_e^p=C_e,\qquad B_F^p=C_F
$$
于原剩余函数域中。它们都在 $\bar{\mathcal A}$ 中；
$B_e$ 型负二，在 $O$ 至少四阶零，二挠极阶至多二。
由 R363 的 Cartier 公式，可以准确取
$$
B_e=-3b\lambda_p\,x/y^2,
\tag{5}
$$
其中 $\lambda_p$ 是该文的明确单位。
$B_F$ 型零，在 $O$ 至少六阶零，二挠极阶至多 $p+1$，
在 $x=0$ 正规。因此
$$
B_F=\frac{N_F(t)}{(1-t)^{(p+1)/2}},\quad
N_F(0)=0,\quad\deg N_F\le(p+1)/2.
\tag{6}
$$
这些界也直接来自 $\mathfrak F_p$ 的二挠极阶 $p^2+1$，
经 $p-1$ 次导数后取 $p$ 次根。

按 (5)、(6) 提升系数，得到
$\widetilde B_e,\widetilde B_F\in\mathcal A$，
同时保持型、原点零阶和全部极界。定义
$$
\boxed{
\widetilde\Xi_2=
 \widetilde Z^{p-1}\widetilde B_F^{\,p}
 +\widetilde c_p\widetilde Z^{2p-2}\widetilde B_e^{\,p}.
}
\tag{7}
$$
其约化是
$$
\Xi_2=Z^{p-1}C_F+c_pZ^{2p-2}C_e.
$$
(7) 在 $O$ 的两个项分别至少有 $7p-1$、$6p-2$ 阶零；
二挠极阶至多 $2p^2$。在所有原 $Z=0$ 测试点，它至少有 $p-1$ 阶零。
选择这种保阶提升，是为了稍后能合法除以 $p$ 后在原短窗略去它；
不能任取一个只模 $p$ 同余的低阶提升来代替。

## 3. 第二整商的全局 p² 整除

取原坐标幂的准确有限二项截断
$$
T_2=
\widetilde Z^{p-1}
+(p-1)p\widetilde Z^{p-2}\widetilde Z_1
+\binom{p-1}{2}p^2\widetilde Z^{p-3}\widetilde Z_1^2.
\tag{8}
$$
它属于 $\mathcal A$，并满足
$T_2\equiv\widetilde Z_2^{p-1}\bmod p^3\mathcal A$。
不用整个高次幂来隐含增加极界。

**定理1。** 下式是原整环中的实际元素：
$$
\boxed{
Q_2=\frac{\,f-u_\kappa T_2-DG_2+p\widetilde\Xi_2\,}{p^2}
\in\mathcal A.
}
\tag{9}
$$

**证明。** 模 $p$，
$DG_2=f+c_pZ^{p-1}$，而 $\bar u_\kappa=-c_p$，
所以 (9) 的前三项之和被 $p$ 整除。

为了核下一位，沿 R363 记
$$
\widetilde T_p=
 [\,D^{p-1}f/(p-1)!-u_\sigma\,]/p,
\qquad
\widetilde H_f=\sum_{i=0}^{p-2}
       (-1)^i\widetilde Z^iD^if/i!.
$$
准确特征零求导式给
$$
D\widetilde G_\sigma
=f-\widetilde Z^{p-1}(u_\sigma+p\widetilde T_p)
  -p\widetilde e\,\widetilde H_f.
$$
加上原 $-\delta_\kappa\widetilde Z^p+pL$，
再用 (8)，可直接读出
$$
\overline{\frac{f-u_\kappa T_2-DG_2}{p}}
=Z^{p-1}\tau_p+eH_f-D\bar L
                    -c_pZ^{p-2}Z_1.
\tag{10}
$$
这里 $u_\kappa-u_\sigma=p\delta_\kappa$ 的两项准确抵消；
没有丢 Gaussian 的下一位。

另一方面，R385 的指定 $\bar L=G_1+c_pZ^{p-1}Z_1$ 满足
$$
D\bar L=
Z^{p-1}\tau_p+eH_f-c_pZ^{p-2}Z_1
+Z^{p-1}C_F+c_pZ^{2p-2}C_e.
\tag{11}
$$
把 (11) 代入 (10)，右边恰为 $-\Xi_2$。
所以加上 (7) 后，先除以 $p$ 的商再次模 $p$ 为零。
平坦整环的约化核是 $p\mathcal A$，于是 (9) 全局可除以 $p^2$。
$\square$

(9) 在 $O$ 正规：$f$ 与 $DG_2$ 的双极准确相消，其余项在那里有零。
它型负二，故约化的首可能项为 $z^4$。
在 $x=0$，分子有真实 $x$ 因子；相应局部商对 $\mathcal O$ 平坦，
故除以 $p^2$ 后仍至少一阶零。
在每个真正 lifted 测试点 $\widetilde Z=0,\ x,y$ 为单位，
$T_2=0$、$DG_2=f$、$\widetilde\Xi_2=0$，所以
$$
\boxed{Q_2(\widetilde P)=0.}
\tag{12}
$$
二挠极阶有明确上界
$$
\operatorname{pole}Q_2\le3p^2-p-2.
\tag{13}
$$
其中最大项来自 (8) 的最后一项；
$DG_2$ 及 (7) 的界至多 $2p^2$。

## 4. 完整原坐标第三位

令 $C_0(t)$ 正是 R382/R385 的已付多项式：
$$
C_0(t)=\frac1{6p^2}
 [\,W(t)/\widetilde Z_2^6-1\,]_{<s},
\qquad W(t)=(-t/b)h(t)^6=z^6.
$$
由 R377 的准确线性系数
$$
[z]\widetilde Z_2=1-9p^2\lambda_{\rm lin}^2
$$
得到
$$
\bar C_0(0)=9.
\tag{14}
$$
实际第二坐标商 $z_2=(z-\widetilde Z_2)/p^2$ 在所需短窗整，
并且
$$
\bar z_2/Z=\bar C_0(t)+O(t^s).
\tag{15}
$$

定义使用第三坐标规范的 forcing
$$
\boxed{
Q_3=Q_2-u_\kappa(p-1)\widetilde Z^{p-1}C_0(t).
}
\tag{16}
$$
它仍属于 $\mathcal A$：虽然 $C_0$ 是 $t$ 多项式，
在 $x=0$ 新项的零阶至少
$(p-1)-3(s-1)=3s+1$，没有新 $x=0$ 极。
(12)、(13)、原点正规和型负二均保持。

由 (3)、(8)、(9) 的准确形式式，
$$
Dq_2=Q_2-\widetilde\Xi_2/p
      -u_\kappa(z^{p-1}-T_2)/p^2.
\tag{17}
$$
在原短窗，(7) 项为零，二项展开及 (15) 给
$$
\boxed{
D\bar q_2=\bar Q_3+O(z^{2p}).
}
\tag{18}
$$
这里显式略去的阶已在所读首共振之后。
因 $\bar q_2$ 真实整，(18) 也准确给
$[z^{p-1}]\bar Q_3=0$。
所以 $D^{p-1}\bar Q_3$ 在 $O$ 至少有 $6p$ 阶零；
不能把它的整个全局 $p$ 次幂设为零。

令
$$
J_2=I_Z(\bar Q_3).
\tag{19}
$$
它正规、型负一，在 $O$ 从 $z^5$ 起，
在每个原非原点测试点至少双零，在 $x=0$ 至少二阶零。
有限原函数的求导式及 (18) 给
$$
\bar q_2=J_2\pmod{z^p}.
\tag{20}
$$
唯一可能的更高 $z^p$ 常数不进入本文的低轴；
本文不声称已消去原第二整商的全部高共振。
二挠极阶至多 $4p^2-p-4$。

## 5. 原 theta 对数的下一整商

保持 R385 的 $F_1^\sharp,\widetilde H_1^\sharp$。
令
$$
C_H^{(1)}=D^{p-1}\overline{F_1^\sharp}=B_H^p.
$$
因为 $\overline{F_1^\sharp}$ 正规、型负一，
$C_H^{(1)}$ 在 $O$ 从 $z^{5p}$ 起；其根 $B_H$ 型负一，
在 $O$ 从 $z^5$ 起，在 $x=0$ 至少二阶零。
R385 的固定极界给 $B_H$ 的二挠极阶至多 $2p-1$：
先从 $2p^2-1$ 加 $p-1$ 后取 $p$ 次根，得到至多 $2p$；
再用奇型在固定二挠点的极阶必须为奇数。

因此准确可写
$$
B_H=a_E\,\frac{N_H(t)}{(1-t)^{p-1}},\qquad
N_H(0)=0,\quad\deg N_H\le p-1.
\tag{21}
$$
按这些条件提升为 $\widetilde B_H\in\mathcal A$，置
$$
\widetilde\Xi_H=
 \widetilde Z^{p-1}\widetilde B_H^{\,p}.
\tag{22}
$$
它在 $O$ 至少有 $6p-1$ 阶零，只有原二挠极，极阶至多 $3p^2-2p$。

**命题1。**
$$
\boxed{
K_2=\frac{F_1^\sharp-D\widetilde H_1^\sharp
                         +\widetilde\Xi_H}{p}
\in\mathcal A.
}
\tag{23}
$$
其约化在 $O$ 正规、型负一，在 $x=0$ 至少二阶零；
二挠极阶至多 $3p^2-2$。在真实测试点
$$
\boxed{
K_2(\widetilde P)
=\frac{4a_E(\widetilde P)
                   -D\widetilde H_1^\sharp(\widetilde P)}p
\in\mathcal O.
}
\tag{24}
$$

**证明。** 有限 primitive 的准确模 $p$ 求导式为
$$
DH_1^\sharp=\overline{F_1^\sharp}
                    +Z^{p-1}D^{p-1}\overline{F_1^\sharp}.
$$
所以 (23) 分子模 $p$ 为零；再由平坦性全局除以 $p$。
$F_1^\sharp$ 在 $O$ 的唯一可能一阶极系数属于
$p^{p-1}\mathcal O$，故再除以 $p$ 后约化为零。
其余两项在原点正规；型负一使约化首项从 $z^5$ 起。
$x=0$ 的真实 $x^2$ 因子在这个平坦局部商中保留。
固定极界由 $\widetilde H_1^\sharp$ 的 $3p^2-3$ 阶极再求一次导数得到。
在测试点，R385 给 $F_1^\sharp=4a_E$，而 (22) 为零，
所以得到 (24)。$\square$

(24) 一般不是零；它保留原已选 lift 的确切一阶误差。
不能把一个另外选取的 Hermite 提升当成当前 $A_0^\sharp$ 的免费性质。

定义
$$
\boxed{
H_2=I_Z(J_2+\bar K_2).
}
\tag{25}
$$
它型零，在 $O$ 常数为零，在 $x=0$ 至少三阶零，
在每个原非原点测试点值为零，且
$$
DH_2(P)=\bar K_2(P).
\tag{26}
$$
其二挠极阶至多
$$
5p^2-p-6.
\tag{27}
$$
所有断言都由 (19)、(23) 的局部阶及同一有限 primitive 直接得到；
每次有限 primitive 对极阶至多增加 $p^2-2$。

令 $M_2=(5p^2-p-6)/2$。于是
$$
\boxed{
H_2=\frac{N_2(t)}{(1-t)^{M_2}},\quad
N_2(0)=0,\quad\deg N_2\le M_2-1,\quad
B_p(-t)\mid N_2(t).
}
\tag{28}
$$
这给真实整测试因子和完整固定极预算，不需要另加移动极。

## 6. 同一个 A0 的指定全局代表

在 R385 的强普通窗中，定义实际形式级数
$$
A^{\rm for}(t)=p^{-2}\log\{g_\kappa(t)/g^\sharp(t)\}.
\tag{29}
$$
其常数为零，普通系数整至 $t^{5s-1}$ 之前：
R385 已给比值为一模 $p^2$，且所需有限对数分母小于 $p$。
低窗准确为 $A_0^\sharp=[A^{\rm for}]_{<s}$。

**定理2。**
$$
\boxed{\bar A_0^\sharp=34H_2\pmod{t^s}.}
\tag{30}
$$

**证明。** 用完整原 theta 对数求导，并保 (18)、(23) 的定义，准确得到
$$
D A^{\rm for}
=34\{q_2+K_2-\widetilde\Xi_H/p
                    -\widetilde\chi/p^2\}
+\mathcal E_{\exp}.
\tag{31}
$$
$\mathcal E_{\exp}$ 是把 R385 有限指数换成完整局部指数后的
已确定误差，原点规范常数的导数为零。
R385 的有限指数估计，在本文 $w^{2s}$ 之前仍使
$\mathcal E_{\exp}$ 模 $p$ 为零；这里已经把原 $p^2$ 除法计入。
同样，该窗内 $\widetilde\chi/p^2$ 的所有所读系数模 $p$ 为零。
(22) 的保阶提升则使 $\widetilde\Xi_H/p$ 在该窗没有项。
所以
$$
D\overline{A^{\rm for}}=34(\bar q_2+\bar K_2)
$$
于所需低窗。
再用 (20) 和 (25) 的有限求导式，
其附加项至少从 $z^{6p-1}$ 起。
积分低窗 $z^{6j}$、$1\le j<s$ 的分母 $6j$ 均为单位；
原点常数相同为零，得 (30)。$\square$

(30) 是原第二整商产生的代表，而不是为了消测试点而任意插值。
按 (28) 的真实 $\mathscr B_p$ 因子、零常数和次数条件取
$\widetilde H_2$，可用
$$
g^\sharp(1+34p^2\widetilde H_2)
\tag{32}
$$
代替 R385 的 $g^\sharp(1+p^2A_0^\sharp)$。
两者在原 $\Gamma_T$ 中相同模 $p^3$：
低块由 (30)，其余差均含 $p^2w^s$。
同步使用已付 $\epsilon^{[3]}$ 后，整个同一原矩阵模 $p^3$
及同 $P_2,\lambda_2$ 的完整 $d_2$ 不变。
(28) 同时保证 (32) 的新因子在真实测试点精确为一，
在 $x=0$ 不增加极；固定二挠极和全部原 Gaussian 仍保留。

## 7. 原 t 轴上的全局 forcing 与逐系数递推

定义指定有理函数
$$
\boxed{
\mathcal R(t)=\frac{34}{6x}\{\bar Q_3+D\bar K_2\}\in k(t).
}
\tag{33}
$$
它只可能在 $t=1$ 有极，在 $t=0$ 为零，在 $t=\infty$ 正规。
原因是 $Q_3$ 在 $x=0$ 至少一阶零，$K_2$ 至少二阶零；
除以 $x$ 不增加极。其型为零，二挠极阶至多 $3p^2-1$，
所以可取
$$
\mathcal R(t)=
 \frac{R(t)}{(1-t)^{(3p^2-1)/2}},
\quad R(0)=0,\quad
\deg R\le(3p^2-1)/2.
\tag{34}
$$
所有系数来自 (9)、(16)、(23) 的指定有限有理计算。

原参数准确满足
$$
Dt=-6ty/x,\quad
(Dt)^2=36t^2x(1-t),\quad
D^2t=6xt(5-8t).
$$
因此定义固定二阶算子
$$
\boxed{
\mathscr L=6t^2(1-t)\partial_t^2+t(5-8t)\partial_t
=6(1-t)(t\partial_t)^2-(1+2t)t\partial_t .
}
\tag{35}
$$
由 (18)、(31)，得到
$$
\boxed{
\mathscr L\,\overline{A^{\rm for}}=\mathcal R(t)
                       \pmod{t^{2s}}.
}
\tag{36}
$$
(18) 的 $z^{2p}$ 导数误差，在除以 $x$ 后从
$z^{2p+2}=w^{2s}$ 起，恰在 (36) 的窗外。

写 $\bar A_0^\sharp=\sum_{k=1}^{s-1}A_kt^k$、
$\mathcal R=\sum_{k\ge1}\mathcal R_kt^k$。
对全部 $1\le k<s$，(36) 给
$$
\boxed{
k(6k-1)A_k-2(k-1)(3k-2)A_{k-1}=\mathcal R_k,\qquad A_0=0.
}
\tag{37}
$$
显示对角项都是单位；因此最高低轴系数与较低系数的关系
由同一个固定 forcing 确定，不能把它们当作自由可调系数。
第一个非单位对角项准确在 $k=s$，因为 $6s-1=p$。

## 8. 完整首共振与坐标 carry

由于 (29) 的实际普通整性包括 $t^s$，(36) 在首共振给
$$
\mathcal R_s=-2(s-1)(3s-2)A_{s-1}.
\tag{38}
$$
把前面的递推一并转置，等价地得到完整一条行
$$
\boxed{
[t^s](1-t)^{-1/2}\mathcal R(t)=0.
}
\tag{39}
$$
具体证明如下：末系数取一，向前回代的左权是
$$
c_k=\prod_{j=k}^{s-1}\frac{j+1/3}{j-1/6}
=\frac{(1/2)_{s-k}}{(s-k)!}.
$$
这里模 $p$ 有 $s=1/6$，全部所用分母是单位。
将 (37)、(38) 乘 $c_k$ 后求和，邻项准确相消，
即得 (39)。这是一条带全部中项的共振关系，不是逐系数零。

为了明确原坐标代价，若先不使用 $C_0$，令
$$
\mathcal R^{[2]}(t)=\frac{34}{6x}(\bar Q_2+D\bar K_2).
$$
由 (14)、(16)，其与正确 forcing 的首差准确为
$$
\mathcal R^{[2]}-\mathcal R
=51c_p(-1/b)^s t^s+O(t^{s+1}).
$$
所以
$$
\boxed{
[t^s](1-t)^{-1/2}\mathcal R^{[2]}
=51c_p(-1/b)^s\in k^\times.
}
\tag{40}
$$
该单位不是新的算术非零。它恰来自
$[z](z-\widetilde Z_2)/p^2=9$ 的原坐标 carry，
并由已付第三坐标 $C_0(0)=9$ 准确抵消为 (39)。
省略 $C_0$ 后把 (40) 当成原中央反证，会比较两个不同规范。

## 9. 当前真实配对的范围

本文把原 $A_0^\sharp$ 的全部低系数固定为 (37)，
给出它的真实全局来源 (25)、(28)、(33)，并支付首共振 (39)。
这些函数只有原固定二挠极，全部非原点测试零保留。
原中央与完整第二障碍读取不同的有限转置，
可对同一个 $\mathcal R$ 逐项比较；尚不能仅由同一 forcing
或 (39) 一条行推出两种转置相同。

所有极界只是全局有理代表的明确成本，
没有把这些大次数函数添为原低次数 canonical 来源。
原整 $C_2$、首提升像、物理 Gaussian、$P_{134}/U_0$、十三行
及完整残数总和均不变。固定 rank 二曲线的无穷素数主目标仍待证明。

## 依赖与同步

- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：两个原 forcing、全局 Cartier 幂及平坦整环。
- [R377](R377-whole-original-theta-first-lift-and-integral-serre-model.md)：完整 theta 第一提升、真实坐标和全部测试因子。
- [R382](R382-original-third-central-aggregate-and-full-third-precision-model.md)：原第三坐标 $C_0$、全矩阵和中央第三聚合。
- [R385](R385-original-zero-resonance-and-strong-whole-theta-second-lift.md)：唯一零共振、普通模 $p^2$ 强窗及本文同一个提升选择。
- [R386](R386-original-second-harmonic-miller-iterate-and-two-torsion-interface.md)：同原 first-lift 的完整 fixed forcing 与相容规范。

全篇为参数证明，没有目标素数扫描。仅在执行环境不可用期间按根规则用小文本接口发表；没有把 API 同步称为 git pull。
