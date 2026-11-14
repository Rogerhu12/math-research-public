# R392：不增加固定极阶的第三精度模型与完整配对的规范协变

日期：2026-11-14。**状态：已证明。** R388 的真实低轴修正可以吸收到 R385 已允许的 $H_1$ 整提升下一位，保持原 $3p^2-3$ 二挠极预算、原测试零和 $x=0$ 零。由此整个第三精度矩阵不需额外的全局 $H_2$ 极。与此同时，完整原中央聚合和真正 $d_2$ 的“基准加修正”组合不变；单独的低轴或 Pascal 边界向量不是规范不变量，不能据其非零宣布主目标完成。

## 1. 固定原提升和第二商

保留 R385/R388 的
$$
p=6s-1>83,\quad b=17,\quad t=-b/x^3,\quad
M_1=3(p^2-1)/2,
$$
$$
G_2,\ F_1^\sharp,\ H_1^\sharp,\ \widetilde H_1^\sharp,\quad
Q_3,\ K_2,\ J_2=I_Z(\bar Q_3),\quad
H_2=I_Z(J_2+\bar K_2).
$$
所有无条函数和系数按各自定义在 $k$ 或 $\mathcal O$ 中读取。
R385 允许的整提升满足
$$
\widetilde H_1^\sharp
=\frac{\mathscr B_p(-t)\widetilde N_1(t)}{(1-t)^{M_1}},
\qquad
\widetilde H_1^\sharp(0)=0,\quad
\deg(\mathscr B_p(-t)\widetilde N_1)\le M_1-1.
\tag{1}
$$
它在所有真实 lifted 测试点精确为零，在 $x=0$ 至少三阶零，
只在原非零二挠点有极。

原径向模型 $g^\sharp$、确定低轴和完整 forcing 为
$$
A_0^\sharp=[\,p^{-2}\log(g_\kappa/g^\sharp)\,]_{<s},
\qquad
\bar A_0^\sharp=34H_2\bmod t^s,
$$
$$
\mathcal R=\frac{34}{6x}(\bar Q_3+D\bar K_2),\qquad
\mathscr L=\frac{D^2}{6x}
=6t^2(1-t)\partial_t^2+t(5-8t)\partial_t.
\tag{2}
$$
$H_2$ 在 $O$、$x=0$ 和原测试点的零及全部极界已由 R388 支付。

## 2. 指定全局 H2 的完整 p-jet

**引理1。**
$$
\boxed{\mathcal R=34\mathscr L H_2\pmod{t^p}.}
\tag{3}
$$
这是指定有理函数的 $p$-jet；不把原形式 $A^{\rm for}$ 的已付
$2s$ 窗擅自扩到 $p$。

**证明。** 置
$$
C_Q=D^{p-1}\bar Q_3,\qquad
C_H=D^{p-1}(J_2+\bar K_2).
$$
R388 给 $C_Q=O(z^{6p})$。
后一个 forcing 正规、型负一，所以 $C_H=O(z^{5p})$；
两者都是 $p$ 次幂。
有限求导身份准确给
$$
D^2H_2
=\bar Q_3+D\bar K_2
 +Z^{p-1}C_Q-Z^{p-2}C_H.
\tag{4}
$$
最后一步使用 $D C_H=0$ 和 $p-1=-1$ 于 $k$，未删全局附加项。
除以 $6x$ 后，两个附加项的原点阶分别至少为
$$
z^{7p+1}=w^{7s-1},\qquad z^{6p}=w^p.
$$
因 $7s-1>p$，得到 (3)。$\square$

## 3. 原极预算内的相容插值

R388 的 $H_2$ 在 $t=0$ 正规且常数为零。取它按 R388
真实因子和次数约束的任一个整提升 $\widetilde H_2$。
令
$$
\boxed{
P(t)=
 \left[\widetilde H_2(t)\,
       \frac{(1-t)^{M_1}}{\mathscr B_p(-t)}\right]_{<p},
\qquad
C(t)=\frac{\mathscr B_p(-t)P(t)}{(1-t)^{M_1}}.
}
\tag{5}
$$
$\mathscr B_p(0)=1$，故 (5) 是单位分母的有限整运算，
$P(0)=0$、$\deg P\le p-1$，且
$$
\bar C=H_2\pmod{t^p}.
\tag{6}
$$

更关键的是，此构造仍在原 (1) 的预算内：
$$
\deg(\mathscr B_pP)\le(3s-1)+(p-1)=9s-3<M_1-1.
\tag{7}
$$
因此 $C$ 在原点为零，在原所有 lifted 测试点为零，
在 $x=0$ 至少三阶零，二挠极阶至多 $2M_1=3p^2-3$；
没有增加任何移动极或新的固定坏点。

现在作允许的整提升变更
$$
\boxed{
\widetilde H_1^{\rm new}
=\widetilde H_1^\sharp+pC.
}
\tag{8}
$$
其约化、原点常数和 (1) 的全部真实条件不变。
$G_2,F_1^\sharp$ 及第一 Cartier 幂不变；
改变的只是原来已允许任意选择的下一位整系数。

## 4. 整个第三精度不需新的极

把 (8) 代入 R385 同一个准确归一的有限指数，记新模型为 $g^{\rm new}$。
原点常数 $c_*$ 不变；在所需普通窗口有
$$
\boxed{
g^{\rm new}/g^\sharp
\equiv1+34p^2C\pmod{p^3,w^{3s}}.
}
\tag{9}
$$
确实，原指数自变量是 $34(\widetilde H_\kappa+p\widetilde H_1)$，
所以增加的是 $34p^2C$。
有限 $E_{p-1}$ 与完整指数的尾在 $w^{3s}$ 前仍被 $p^3$ 整除，
按 R385 的 $r-j-v_p(r!)$ 下界即可直接核定。
平方误差至少含 $p^4$。

由 (2)、(6)，(9) 的低块消去原 $A_0^\sharp\bmod p$；
中、高块继续保持原普通模 $p^2$。所以
$$
\boxed{
A_0^{\rm new}\equiv0\pmod p,\qquad
g^{\rm new}\equiv g_\kappa\pmod{p^3\Gamma_T},
\quad T\le3s.
}
\tag{10}
$$
坐标仍用原 R382 的 $\epsilon^{[3]}$；不能把 $C_0$ 一并删去。
对全部真实 charge $N=n+40$，原角多项式 $F_{n,j}$ 不变，
$$
\left(\frac{g^{\rm new}}{1+8t}\right)^N
 F_{n,j}(t)e_2(Na_\kappa\epsilon^{[3]})
$$
逐项给同一个原矩阵模 $p^3$。
$P_{134}/U_0$、十三行、所有混合次数和完整首次提升像均保持。

(10) 是有限精度代表的改进，不声称 $g^{\rm new}$ 的全权 Mellin 函数
就是原函数。原完整中央判据仍从 R382 的已付尾界读取。

## 5. 真实 forcing 的规范变换

R388 的 $Q_3$ 不含 $\widetilde H_1^\sharp$，故 (8) 后不变。
其 $\widetilde\Xi_H$ 只由固定 $F_1^\sharp\bmod p$ 决定，也不变。
由 R388 的准确整商定义，得到特征零等式
$$
\boxed{K_2^{\rm new}=K_2-DC.}
\tag{11}
$$
因而
$$
\boxed{
\mathcal R^{\rm new}
=\mathcal R-34\mathscr L\bar C.
}
\tag{12}
$$
结合 (3)、(6)，
$$
\boxed{\mathcal R^{\rm new}=0\pmod{t^p}.}
\tag{13}
$$
所以这个允许的真实整提升可使全部前 $p-1$ 个 forcing 系数为零。

这没有让其全局函数恒零，也没有删除二挠高极。
R390 的完整 Pascal 运输中，所有可见行只是在本规范下变为零；
其唯一不可见的 Frobenius 方向仍按原式保留。
由于 (8) 同时改变基准模型，(13) 不能成为原中央或整个 $d_2$ 为零的证明。

## 6. 原中央第三聚合的完整协变

对任意允许的 $C$，不必先取 (5)，记
$$
\widehat S^\sharp=g^\sharp a_{\rm ang}(t)/(7b),\qquad
c_j^\sharp=[w^{js}]\widehat S^\sharp ,
$$
其中原 $a_{\rm ang}=t(t-1)(16t^2+4t+7)$ 从 $w$ 起。
R385 的实际中央表达为
$$
\mathfrak C=
a_\kappa^2c_1^\sharp-pa_\kappa c_2^\sharp+2p^2c_3^\sharp
+p^2a_\kappa^2[w^s](A_0^\sharp\widehat S^\sharp)
\pmod{p^3}.
\tag{14}
$$
由 (9)，基准前三项的变化准确为
$$
34p^2a_\kappa^2[w^s](C\widehat S^\sharp).
\tag{15}
$$
另由实际低轴定义，
$$
\bar A_0^{\rm new}
=\bar A_0^\sharp-34[\bar C]_{<s}.
$$
原 $\widehat S^\sharp(0)=0$，所以修正项的变化恰是 (15) 的负数。
于是
$$
\boxed{\mathfrak C^{\rm new}=\mathfrak C\pmod{p^3}.}
\tag{16}
$$
在 (5) 的规范下，原 $A_0$ 的全部贡献已经搬入新的基准前三项；
它没有消失于原中央函数。

## 7. 原第二障碍的完整协变

使用同一整个物理矩阵规范，令 $\mathcal E_{\rm tot}=\mathcal E+40$。
设 $M^\sharp$ 为未加低轴修正的基准模型，
$P_2$ 为同一个真正模 $p^2$ 核向量，$\lambda_2$ 为同一可提升整左核。
这些核和原 $\beta_1$ 像在 (8) 前后相同，因为基准矩阵只改变 $p^2$。

按每个真实 charge 展开 (9)，在完整原目标中
$$
\boxed{
M^{\rm new}P-M^\sharp P
=34p^2\bar C\,
 \bar M^{\rm orig}(\mathcal E_{\rm tot}\bar P)
 \pmod{p^3}.
}
\tag{17}
$$
因此基准第二障碍的配对变化是
$$
34\lambda_0\!\left(
 \bar C\,\bar M^{\rm orig}(\mathcal E_{\rm tot}\bar P)\right).
\tag{18}
$$
完整低轴修正项因 $A_0\mapsto A_0-34C$ 给出其准确负数。
相加后，固定模 $p^2$ 提升的 $C_1$ 类、再商去全部 $\beta_1(K_1)$
所得真正 $C_2$ 类都不变。

(17) 没有要求 Euler 保持 $K_1$ 或 $K_2$。
在同一个原 $m_{13}J$ 规范中，R390 的全部末行和角权继续原样参与。
所得结论是完整原第二障碍的协变恒等式，
不是可以把 (18) 单独赋零的理由。

## 8. 后续必须比较的对象

R388/R390 的低轴递推和固定二挠转置都是有效的确定计算。
本篇进一步确定其精确使用方式：
必须将该修正与同一规范下的中央基准项、第二障碍基准项一起比较。
仅证明某个有理 forcing、某条 Cartier 行或其 Pascal 边界向量非零，
没有给原完整中央非零；(5)–(13) 是保持全部原局部条件的具体检验。

另一方面，(8)–(10) 提供了不增加原 $H_1$ 固定极阶的全矩阵第三精度代表。
可以在这个规范中直接研究原基准矩阵与基准中央，
也可保持旧规范使用 R390 的完整基准加修正式；
两种选择读取同一个原问题。

固定曲线、无穷多个不同素数以及整个 Sha 的完成标准不变，主目标未完成。

## 依赖

R377/R385 的真实 $H_1$ 整提升自由度、强普通窗和有限指数界；
R382 的第三坐标与完整中央尾；
R388 的两个全局整商、$H_2$、首共振；
R390 的原 $P_2,\lambda_2$ 与完整固定边界转置。

全篇为参数证明，不扫描目标素数，不增加原来源。
环境不可用期间按根规则用小文本 API 发表；API 同步不冒称实际 git pull。
