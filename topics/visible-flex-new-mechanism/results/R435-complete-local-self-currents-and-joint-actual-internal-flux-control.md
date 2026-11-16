# R435：完整局部轨道的 self current 与同一实际联合零值下的内部支付

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、积分、符号程序、秩、人工测试或科学运行。**

[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 已在 R431 同一母库上给出
$$
J^+=(E,\mathcal A,\mathcal O),\qquad E=(\pi,\mathcal Q)
$$
的实际有限 $C^1$ 截面。其中 $\mathcal A$ 只含原实际母的共同 self 与所需 ordered 查询，$\mathcal O$ 是全部有序 $3+2$ 自然系数；**不是全部 self 自然函数**。

本稿继续内部 self 部分。原十一维局部响应轨道有一个完整、显式、保真实左常数的 current 生成式。它给出：

1. 每个真实简单 $A_f$ 点的单独 self 门都有非零的 $J^+$ 核响应；
2. 原 $u''\ne0$ 基点的至多十一个同形对应副本仍可同时支付；若 $u''=0$，另有至多六个对应副本的完整结论；
3. 这些支付可接入 **同一个** R433 实际截面；对已支付的消-self 行 $C$，必须按下文准确的联合接口保持；
4. 这组有限 self 门不能使原正字符 $\lambda_+$ 下降，因为有一个明确的 $\lambda_+=1$ 新联合核见证。

不将“每个点分别可控”写成全部点联合可控，不改变 R431 已冻结的母形、真实宽度、原副本或退化点。一般全包 self 像仍有精确余项。

直接来源：[R345](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md)、R395 §§1—3、R397 §§2—6、R401 §§2—5、[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)、R433。R395/R397/R401 在本文仅用原式及原真实实现方法，不把其较早、较小的实际观察集与当前 $J^+$ 混用。

## 1. 原轨道、同一点与全部真实基准

原响应为
$$
K_0=\frac13\mathcal B_P[P,S],\qquad K_n=\delta^nK_0,
\qquad 0\le n\le10 .
\tag{1}
$$
R345 已证明其完整 universal 成本空间
$$
\mathscr K=\operatorname{span}(K_0,\ldots,K_{10})\simeq V_{10},
$$
$$
NK_n=n(n-11)K_{n-1},\qquad K_{11}=0,
\qquad \mathscr K\subset\mathcal R\cap\ker E.
\tag{2}
$$
这里 $\delta$ 是对输出和全部输入的原代数导子，不是允许自由改变实际几何的非仿射变换。

R344/R352 的完整自然函数杀全部 $\mathcal R$。因而
$$
\boxed{\mathscr K\subset\ker J^+.}
\tag{3}
$$
(3)含 $\mathcal A$ 的真实 ordered 系数及 R433 新增的整个 $\mathcal O$，不是只含一个裸 self 积分。

取 R431 同一最终圆
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
\qquad R_i=a_i^2-b_i^2,\quad T_i=a_ib_i ,
\tag{4}
$$
各最细 $u_i$ 的值支撑严格不交。实际幅度、宽度、中心及八/十二/五块都保留。以下 $u$ 可以已经包含任意一个固定的真实宽度；不同宽度不在没有证明时并成同一对应点组。

R345 的完整局部身份是
$$
K_n(f^2,\phi)
=-\frac13\sum_i a_i^2(a_i^2-c_i^2)
P_n(x,u_i,u_i',u_i''),
\qquad \phi=\sum_i c_i u_i.
\tag{5}
$$
这里无跨包余项，所有外 collar 上的输出及其导数都准确为零。
这来自原三响应项和原有限代数轨道，不能推广为一般成本输出左紧。

## 2. 完整 self current 的有限生成式

令
$$
p=u',\quad r=u'',\quad t=u''',\qquad
w=1-zx,\qquad
A_z=w^2r+2zwp+2z^2u .
\tag{6}
$$
$z$ 只是原有限多项式的形式参数。R345(4)给
$$
U_z:=\sum_{n=0}^{10}\frac{z^n}{n!}K_n(u^2,0)
=-\frac13w^2A_z^4.
\tag{7}
$$
最重要的真实 $x$ 导数是
$$
D_xA_z=w^2t.
\tag{8}
$$
因此
$$
\int_\ell^x tU_z
=-\frac13\int_\ell^x A_z^4D_xA_z
=-\frac1{15}A_z(x)^5 .
\tag{9}
$$
$\ell$ 是该实际包的左零 collar。那里 $u=p=r=0$，故 $A_z(\ell)=0$；(9)没有丢掉一个可以任选的积分常数。

两次真实分部积分现在给
$$
\boxed{
\mathcal F_z(x;u)
:=\int_\ell^x p\,U_z''
=pU_z'-rU_z-\frac1{15}A_z^5 .
}
\tag{10}
$$
先保一般点，代(7)—(8)可写为
$$
\mathcal F_z
=\frac4{15}A_z^5
-\frac23z^2uA_z^4
-\frac43p\,w^4A_z^3t .
\tag{11}
$$
这些是完整 self 的 partial，既非 principal，也非只模全导数。

在真实退化点
$$
A_u(x):=6pt-2r^2=0
$$
处，$pt=r^2/3$，所以
$$
\boxed{
\mathcal F_z\big|_{A_u=0}
=\frac{A_z^3}{15}
\left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right).
}
\tag{12}
$$
该式次数至多十，对每个实际根适用，不需要除以 $p$。

定义
$$
\mathcal F_x(K_n;u)=
\int_\ell^x u'[K_n(u^2,0)]''.
$$
由(12)取普通系数再乘 $n!$，准确得到这十一个值。特别
$$
\boxed{
\mathcal F_x(K_0;u)=-\frac8{45}r^5,\qquad
\mathcal F_x(K_1;u)=-10x\,\mathcal F_x(K_0;u).
}
\tag{13}
$$
第二式中的 $x$ 是实际全局坐标，不是临时重置的母坐标。

### 2.1 以前不需要处理的 r 零边界

R431 的所有内部 $A_u$ 根简单，原 $p$ 的零也简单，故在 $A_u=0$ 点必有 $p\ne0$。
否则 $A_u=0$ 会给 $r=0$，与 $p$ 的简单零矛盾。

若 $r\ne0$，(13)已经给非零响应。
若 $r=0$，则 $t=0$，而
$$
A_z=2pz+2(u-xp)z^2.
$$
代入(12)，最低项为
$$
\mathcal F_z=\frac{128}{15}p^5z^5+O(z^6).
$$
所以
$$
\boxed{
\mathcal F_x(K_n;u)=0\ (0\le n<5),\qquad
\mathcal F_x(K_5;u)=1024p^5\ne0 .
}
\tag{14}
$$
每个真实简单 $A_u$ 点因此都被同一个 $\mathscr K$ 看见。
这只是单行非零性，不意味着任意多行同时独立。

## 3. 对原两条 period 通道的准确作用

先在全部 U 上使用原 raw 线性读出
$$
\mathsf V_d=V(f^2,g),\qquad
\mathsf V_e=\frac12\partial_\theta
V(f^2,f\cos\theta+g\sin\theta)\big|_{\theta=0}.
$$
对实际包 i 和其中退化点 x，令
$$
H_d(V)=\int_{\ell_i}^{x}f'\mathsf V_d'',\qquad
H_e(V)=\int_{\ell_i}^{x}f'\mathsf V_e'',
\qquad C(V)=R_iH_e(V)+T_iH_d(V).
\tag{15}
$$
如需 R345 的一般平台规范，使用
$$
\widehat H_d(V)=H_d(V)
-\{f(x)-f(\ell_i)\}\mathsf V_d''(\ell_i).
\tag{16}
$$
一般 V 的平台项保留。对(5)它严格为零；在最终 $E=0$ 的原真实 period 范围中，原二次平台也已为零。

直接从(5)作真实相位半导数，得到
$$
\boxed{
H_d(K_n)=a_i^3R_i\,\mathcal F_x(K_n;u_i),\qquad
H_e(K_n)=-a_i^3T_i\,\mathcal F_x(K_n;u_i).
}
\tag{17}
$$
因此
$$
\boxed{C(K_n)=0}
\tag{18}
$$
对整个当前圆、全部包、全部根同时成立；不是只在下面选中的点成立。
所有 $n$ 和实际 $a_i,b_i$ 均保，g 的整块翻号不会被误并到第五次幅度里。

(18)是后继三角联调的关键：这些响应可以改变剩余 self 通道，而不改变任何已列消-self 行。它不允许在一条冻结实际几何上免费加入 signed 成本；真实 prototype 基准仍按第5节支付。

## 4. 两种准确的对应副本范围

固定一个已经存在的真实基点 $x_*$，不移动或重新求根。
选相同最终母、相同真实宽度的不同完整副本：
$$
f=\rho_j a\,u(x-t_j),\qquad
g=\rho_j\epsilon_jb\,u(x-t_j),
\quad \epsilon_j=\pm1,\quad \rho_j\ne0,\quad t_i\ne t_j .
\tag{19}
$$
其中 $a\ne0$、$R=a^2-b^2\ne0$，实际点为 $x_j=x_*+t_j$。
原完整复制库保留这样的副本；它们不是另外自由安置的假想查询。

记基点 raw 值
$$
c_n=\widehat H_{d,*}(K_n)
=a^3R\,\mathcal F_{x_*}(K_n;u).
$$
令
$$
q=\begin{cases}0,&r(x_*)\ne0,\\5,&r(x_*)=0.\end{cases}
$$
由(13)—(14)，$c_n=0$ 对 $n<q$ 成立，且 $c_q\ne0$。
真实平移和(2)给
$$
p_n(t)=\widehat H_{d,*}(e^{tN}K_n),\qquad
\widehat H_{d,j}(K_n)=\rho_j^5p_n(t_j).
\tag{20}
$$
若 $q\le n\le10$，$p_n$ 的准确次数为 $n-q$，最高系数是
$$
\boxed{
[t^{\,n-q}]p_n
=\frac{c_q}{(n-q)!}
\prod_{\ell=0}^{n-q-1}(n-\ell)(n-\ell-11)\ne0 .
}
\tag{21}
$$
空积为1。高于这个次数的项只会落到 $c_0,\ldots,c_{q-1}$，故准确为零。
实际第五次幅度、$\epsilon_j$ 的平方作用及真右锚都与 R345 相同。

因此逐次多项式换基给
$$
\boxed{
(\widehat H_{d,1},\ldots,\widehat H_{d,m})
\bigl(\operatorname{span}\{K_q,\ldots,K_{q+m-1}\}\bigr)
=\mathbb R^m,\qquad m\le11-q.
}
\tag{22}
$$
$r\ne0$ 时，这是直接消费原 R345 的至多十一列；
$r=0$ 时，(14)、(21)给新增的至多六列范围。
没有重做任何数值矩阵或旧对应点计算。

对更多同形对应点，本模块的完整像准确是
$$
\{(\rho_j^5P(t_j))_j:\deg P\le10-q\}.
\tag{23}
$$
这只是 $\mathscr K$ 的范围，不是整个 $\mathcal R\cap\ker E$ 的限制。
任意不同根的联合问题不能套(22)；其完整本模块矩阵应直接由(12)评价。

另有已付的同包镜点使用方式：若偶母在 $x_\pm=\xi\pm b$ 上 $r_\pm=r_*\ne0$，则(13)使 $K_0,K_1$ 的两行行列式非零，正是 R401 的原两列。这里也只支付这一对，不把它变成全部内部根。

## 5. 与同一个 J⁺ 实际截面的真正联合实现

取(22)中的 m 个 raw 查询，记 $\mathbf H=(\widehat H_{d,j})$。
由(3)、(22)，
$$
\boxed{
(J^+,\mathbf H)(U)=J^+(U)\times\mathbb R^m,\qquad
(J^+,\mathbf H)(\mathcal R)=J^+(\mathcal R)\times\mathbb R^m .
}
\tag{24}
$$
增强响应商仍是 R433 的那个响应商，没有新的正字符需要单独猜测。

(24)只是线性代数；实际结论还需保所有基准。
从起点将原 R433 库与这些有限 $\mathcal R_{71}$ 原型纳入同一个共同合法窗口。所有查询 profiles、真实根、右锚及目标紧包络一次固定。
不放宽旧冻结窄窗口，不将 signed 列本身冒称实际零基准路径。

用 R433 的同一新商截面。原 J⁺ 响应基加上(22)的 K 列，其增强响应矩阵为真正可逆的块三角矩阵；原基的全部 H 值保留在左下块。每一个第三 prototype 先以原商截面清其完整商基准，余响应成本全部保留。

共享原型和真倒行后，成本仍具有原形式
$$
E_0(t)+n\left(2\sum_\alpha\widehat v_\alpha+
\sum_\alpha t_\alpha R_\alpha\right).
\tag{25}
$$
再作一次真实商校正，记录其全部 J⁺ 和 H 代价。所有内部整数、紧盒和校正块先固定；最后响应方程是
$$
n(a+Mt)+F(t,y)=y_{\rm resp},
\tag{26}
$$
其中 M 是固定可逆增强矩阵，$F,D_tF$ 在目标紧集上一致有界且与最后 n 无关。
一次固定有限 n 的收缩给同一个 $C^1$ 根。

因此对任意紧相容目标集，有一个固定有限实际词同时实现
$$
\boxed{J^+=y,\qquad \mathbf H=h.}
\tag{27}
$$
(27)中的 H 使用(16)的完整平台规范。原 E 目标已知时，R397 的平台因子化给 raw H 与它的确定差；在最终 E 零时二者一致。

Klein 成本是原 $V_{\rm base}+4V_B$，目标先减全部基准再除4；不存在另一次零费用校正。

这里允许新全局几何，但保持同一首阶母库、原局部保护芽与实际查询点。
不继承某条旧几何的 whole-E、Morse 或其它未付性质。
本稿没有重新计算 R431 的十九目标，它们保持原来同点构造。

### 5.1 若 C 已支付，如何准确追加

若后来已经有同一库上 $(J^+,\mathbf C)$ 的完整实际截面，则(18)使上述 K 列在全部 C 行严格为零，同一个块三角构造可追加 $\mathbf H$。
另一个足够的线性入口是准确等像
$$
\mathbf C(\mathcal R\cap\ker J^+)=\mathbf C(\ker J^+).
$$
它使增强响应商仍与原商同构，有限基与原 R433 的实现方法先给所需 C 截面，再按本节追加 H。
不是仅有几条非零 C 列就满足此前提。

全过程的全部 prototype 和第二次商校正的 C 基准仍进入(25)—(26)。

不能仅因为 signed K 的 C 为零，就说把本稿另一条实际路径拼上去仍保旧 C。
没有给定联合前提时，(27)只授 J⁺ 与显示的 H，不先授全部 C。

### 5.2 真正末包与完整 cell 边界

对全圆最右包，$n_{R,i}=n_{T,i}=0$，故在 $E=0$ 下
$$
H_d=a_i^3R_i\,s_i,\qquad
H_e=-a_i^3T_i\,s_i .
\tag{28}
$$
这是原完整 self cap $s_i$，没有以 whole self 总量零代替它。
若 $R_i\ne0$，支付 $H_d=0$ 即使两条内部通量同时为零。

R397 的更多实际零 suffix 位置来自十二包装中的**完整八副本块**，包括原三矩已闭合 circle 的全部最细编码包。它不是八个孤立同轴微包；R326 的三次有限差分权并不自行支付二次闭合。先在原完整 circle 上有两组三矩零，再对整个 circle 作真实副本、幅度与仿射输运，每份仍是零向量。
因此每个这样的 cell 与后续所有完整块都满足
$\sum R_i\mu_i=\sum T_i\mu_i=0$，保实际 R/T 权和三个原矩。
末包两 suffix 向量均零；首包为自身矩的对应负倍数，消-self 组合也准确为零。
不能用裸格点均值替代这条来源。

所以可在已有完整十二包装中选择符合(19)的至多十一（或六）个首/末包对应点，并由(27)在同一个 actual $J^+=0$ 背景上支付其两条 period 内部门。
这确实加强了 R397/R401 较早分开的实际结论，但不支付其余根。

## 6. 这组有限 self 门不会重新读出 λ⁺

令 $H_*$ 为 R406/R433 的原 signed 类：
$$
J^+(H_*)=0,\qquad \lambda_+(H_*)=1.
$$
令 M 为(22)的原矩阵，取
$$
\boxed{
H_*^{\,\mathbf H}
=H_*-\sum_{j=0}^{m-1}
\bigl(M^{-1}\mathbf H(H_*)\bigr)_jK_{q+j} .
}
\tag{29}
$$
这里 $\mathbf H(H_*)$ 是同一个完整原目标，含所有实际 self/ordered histories，不要求预先评价或将它置零。
所有 K 都在原响应层，故 $\lambda_+(K_n)=0$。
于是
$$
\boxed{
J^+(H_*^{\,\mathbf H})=0,\quad
\mathbf H(H_*^{\,\mathbf H})=0,\quad
\lambda_+(H_*^{\,\mathbf H})=1 .
}
\tag{30}
$$
因此这组有限 self 查询不能承载 $\lambda_+$ 的正障碍。
这个核见证是 signed 线性结论；实际存在另由第5节的完整成本构造支付。

若需要同时保额外 C，须先有真实
$R_C\in\mathcal R\cap\ker E$ 使
$\mathbf C(R_C)=\mathbf C(H_*)$。
以 $H_*-R_C$ 代(29)的起点，再用(18)，同样得到 C、H 都零且 $\lambda_+=1$。
本稿没有无条件假设这条 R_C 已存在；它正是 R433/R434 仍在研究的 ordered 响应像。
在(28)等原零-suffix范围内，C 本来经 E 因子化，不需另加这个前提。

## 7. 全部根的准确剩余问题

新公式(12)给同一最终 profile 库上本模块的**完整** self 矩阵。
它证明每个单点非盲，也证明上述有限对应组的实际联合支付。
它没有证明所有不同根的行都独立，也没有把(23)当成全响应像障碍。

若 C 已经支付，剩余 self/Hd 的准确对象仍是
$$
\mathfrak H(\ker(J^+,\mathbf C))/
\mathfrak H\bigl(\mathcal R\cap\ker E\cap\ker\mathbf C\bigr),
\tag{31}
$$
其中 $\mathfrak H$ 必须包含同一圆全部真实根，而不能对每个根分别挑一条几何。
$\mathscr K$ 是分母中一个已完全显式的十一维子模块。
其它响应可能增加其像；原 C 观察同点相容也不能删掉。

剩余全部内部点、平台仿射连接、k 值闭合、R394 的同相位十三行和完整第四 period，仍须继续。
本稿完成的是完整 self current、r 零边界、同一 actual J⁺ 上的真实有限追加，以及这组有限门不会产生新的 λ⁺ 障碍。
