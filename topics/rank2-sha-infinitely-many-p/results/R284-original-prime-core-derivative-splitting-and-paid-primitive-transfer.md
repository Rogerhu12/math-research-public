# R284 — 原 $T_p$ 的微分转置、全正 theta 十六次周期及三个真实原函数的完整中央接口

日期：2026-11-13。**状态：以下真正的测度微分转置、全共同 theta 空间上的十六次周期、原 A/B 极项的全部主部及每层单位一阶极、H 连接项的十七维准确分解、原三零的保质量有限转置，以及付出边界后的角原函数比较均已证明。所得单位极和非零原函数观察尚未被原三条中央零控制；不据此宣称主目标完成。**

本篇沿用 R263/R266/R280/R282 的同一实际测度、正式周期和有限 theta 算子。
R283 的两个真实 $i$ 型空间及 CM 边界补偿在下文保持各自的角色。
全部矩阵计算为固定有理或 Gaussian 计算，没有目标素数扫描。

## 1. 真微分的转置改变 tame 行

设 $p\equiv1\pmod4$ 为普通好素数，删去固定有限坏集合，记
$$
\pi=\pi_0,\qquad b_0=\bar\pi,\qquad
\pi b_0=p,\qquad d=p-1,\qquad
\kappa_p=\frac p{b_0^2}=\frac\pi{b_0}.
$$
始终使用
$$
\mathcal A_G(T)=G(\Omega_0\log(1+T)),\qquad
T_p=b_{17}[b_0^2]_*\psi_p,\qquad
\psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbb Z_p}).
\tag{1}
$$
因此 $\nu_{G'}=\Omega_0^{-1}x\nu_G$。直接在测度上计算得到
$$
\boxed{T_p\partial_z^k=\kappa_p^k\partial_z^kT_p\quad(k\ge0).}
\tag{2}
$$
确切地，$\psi_p$ 把原 $x$ 改成 $px$，而随后按 $b_0^2$ 缩放把
该因子改成 $p x/b_0^2$；$\Omega_0$ 在两边相同。这证明 (2)，
没有从复 theta 同源图猜测一个微分权。

定义原单位 Mellin 和真正的 tame-one 行
$$
\begin{aligned}
M_G(u)&=\int_{\mathbb Z_p^\times}\langle x\rangle^{du}\,d\nu_G(x),\\
\mathcal M_{G,1}(u)&=
\Omega_0^{-1}\int_{\mathbb Z_p^\times}
x\langle x\rangle^{du}\,d\nu_G(x)=M_{G'}(u).
\end{aligned}
\tag{3}
$$
若 $G(iz)=iG(z)$，则 $M_G$ 在原 principal 分支恒为零；
其导数来源读取的是 (3) 第二行，不能把它替成同一个 $M_G$ 的标量倍。

对第 $n$ 个环带置
$$
\mathcal M_{G,1}^{[n]}(u)=
\Omega_0^{-1}\int_{p^n\mathbb Z_p^\times}
(x/p^n)\langle x/p^n\rangle^{du}\,d\nu_G(x).
$$
完整转置为
$$
\boxed{
\mathcal M_{T_p^nG,1}(u)
=b_{17}^n b_0^{2n}(b_0^{2nd})^u
\mathcal M_{G,1}^{[n]}(u).
}
\tag{4}
$$
所以 $T_p^nG'$ 的单位 Mellin 是右边再乘 $\kappa_p^n$。
求中央导数时必须保留 $2nd\log_pb_0$ 乘该环带质量。

Euler 算子 $E_z=z\partial_z$ 在实际局部解析分布上与 $T_p$ 交换；
其转置对单位核给 $E_z^*K_u=duK_u$。因此若一个来源 $N$ 已经
给出这种分布，则 $M_{(E_z+1)N}=(du+1)M_N$。
但 $N=K/z$ 的 Amice 式含 $1/\log(1+T)$，一般在非零 $p$ 幂
形式挠点有极。仅有原点形式除法不满足这个分布前提。
本篇全部使用真正有界的 $K$ 和 $K'$，不借此省去一个来源。

## 2. 三个实际原函数与 A/B 的真实三阶极

记
$$
u=x^{-1/2},\quad v=u^4,\quad t=\sqrt{1-v},\quad
Y=\vartheta^{68},\quad
\frac{\vartheta'}{\vartheta}=u^3\mathcal H(v).
$$
原三列为 $S_A=YQ_A(v)$、$S_B=YQ_B(v)$、$S_H=YtQ_H(v)$。
R277 的真正角原函数是
$$
Z_A=tB_A-B_A(0),\quad Z_B=tB_B-B_B(0),\quad
Z_H' =Q_H,\quad Z_H(0)=0.
$$
令
$$
K_i=\frac{YZ_i}{4u^3},\qquad
\mathcal A=68\frac{\vartheta'}{\vartheta}+\frac{3y}{x},
\qquad C_i=-\mathcal A K_i.
$$
由于 $u'=t$、$y/x=-t/u$，逐项微分给出完整来源恒等式
$$
\boxed{S_i=K_i'+C_i=L K_i,\qquad
L=\partial_z-\mathcal A
=\partial_z-68\zeta-71y/x.}
\tag{5}
$$
等价地，$C_i=YZ_i(3t/(4v)-17\mathcal H)$；
这正是 R277 的原低权伴随，并非新造的微分来源。

在真正的 $\alpha=1+i$ 拉回下
$$
v(\alpha z)=\frac{-4v}{(1-v)^2},\quad
t(\alpha z)=\frac{1+v}{1-v},\quad
u(\alpha z)=-\alpha x/y.
$$
当原 $T_0=(0,0)$ 处 $v\to\infty$ 时，第一式趋于零，而第二式趋于
**负一**。于是 A/B 的原点归一常数不能在这个分支删掉。
准确分解为
$$
\boxed{
K_A(\alpha z)=K_A^{\rm hol}+\frac{\alpha B_A(0)}8 R_T,\qquad
K_B(\alpha z)=K_B^{\rm hol}+\frac{\alpha B_B(0)}8 R_T,
\quad R_T=\sigma^{136}\frac y{x^2},
}
\tag{6}
$$
其中两项 $K_i^{\rm hol}$ 属于 $\mathcal S_{136}$，
$K_H(\alpha z)$ 也全纯。只有显示的一个最高项产生极，减掉它后
多项式次数正好落回全纯允许范围。完整多项式在 R283 的固定证书中给出。
这里
$$
B_A(0)=-\frac{1248227362551868}{22563055139625},\qquad
B_B(0)=\frac{727339049799116}{7521018379875}
$$
均非零。

$R_T$ 在 $T_0$ 有三阶极，在原点从 $z^{137}$ 开始。
所以原点很多低阶项看不见该极，但这不是全源可删去的理由。
唯一相应的 A/B 无极常数组合是
$$
S_{AB}=B_B(0)S_A-B_A(0)S_B,\qquad
K_{AB}=-\frac{Yy}{4}\bigl(B_B(0)B_A-B_A(0)B_B\bigr).
\tag{7}
$$
它属于 untwisted 的 $\sigma^{68}y\mathbb Q(i)[U]_{\le16}$。
相反，
$$
K_H=V_iP_G(U),\quad V_i=-x\vartheta\sigma^{67},\quad
P_G(U)=-\frac14U^{17}Z_H(1/U)
\tag{8}
$$
属于 twisted 的另一十七维空间，$\deg P_G=15$。
两者的真实 norm-two 拉回分居不同二挠块，不能共用一个矩阵。

## 3. 极项的完整 $T_p^n$ 主部与每层实际单位一阶极

式 (6) 的全纯部分有固定有限 theta 轨道；$R_T$ 则不能仅增加一个
固定极方向来处理。以下给出它的全部主部。

令
$$
r_{\gamma}(z)=\frac{\sigma(\gamma z)}{\sigma(z)^{p^n}}
\quad(\gamma=\pi^n,\bar\pi^n),\qquad
k_n=r_{\bar\pi^n}/r_{\pi^n}.
$$
对每个满足 $[\bar\pi^n]P=T_0$ 的点，置 $Q=[\pi^n]P$，
取输出处的加法局部参数 $s$，并记
$$
h_P=136\,\partial_z\log k_n(P).
$$
**定理 1。** 在输出 $\sigma^{136}$ frame 中，$T_p^nR_T$ 在 $Q$ 的
完整主部准确为
$$
\boxed{
-\frac{b_{17}^n k_n(P)^{136}}{b_0^{4n}}
\left[
\frac{\pi^{2n}}{s^3}
+\frac{\pi^n h_P}{s^2}
+\frac{h_P^2+136\pi^{2n}x(Q)}{2s}
\right].
}
\tag{9}
$$
其极支持恰为
$$
T_0+E_0[\bar\pi^n].
\tag{10}
$$
每个输出点只有一条奇异迹分支，最高极的系数非零。
此外，对每个 $n\ge1$，(10) 中至少一个实际点的一阶极系数是 $p$ 单位。

**证明。** R266 的真实迹迭代给
$$
T_p^nR_T=
\left(\frac{b_{17}}p\right)^n\sigma^{136}
\operatorname{Tr}_{[\pi^n]}
\left(k_n^{136}\,(y/x^2)\circ[\bar\pi^n]\right).
\tag{11}
$$
两种 CM 核互素，故 $[\pi^n]$ 在 $E[\bar\pi^n]$ 上为双射，
且一条 $[\pi^n]$ 纤维至多有一个点映到 $T_0$。
这证明 (10) 和奇异分支的唯一性。

在 $T_0$ 处直接由 $x(T_0+z)=-1/x(z)$ 得
$$
\frac y{x^2}(T_0+z)=-z^{-3}+O(z).
$$
输出参数 $s$ 对应逆像参数 $s/\pi^n$，再经 $[\bar\pi^n]$
变成 $s/\kappa_p^n$。
而
$$
\partial_z^2\log k_n
=\pi^{2n}x\circ[\pi^n]-\bar\pi^{2n}x\circ[\bar\pi^n],
$$
所以在 $P$ 处
$136\partial_z^2\log k_n=136\pi^{2n}x(Q)$。
把 $k_n^{136}$ 的二阶 Taylor 展开与唯一的 $-z^{-3}$ 相乘，
再用 $p=\pi b_0$ 整理，正得 (9)。这也保留了由一阶连接项平方产生的
一阶极，不能只计算最高极。

最后证明单位断言。置 $r_n=(p^n-1)/4$，写实际 division 多项式
$$
r_{\pi^n}=R_n(U),\qquad r_{\bar\pi^n}=B_n(U),\qquad
B_n^*(U)=U^{r_n}B_n(1/U).
$$
原 Frobenius 给 $R_n\equiv1\bmod p$，$R_n(0)=B_n(0)=1$，
而 $B_n$ 的次数为 $r_n$，最高系数为 $b_0^n$。
这些等式也可由 R270 的一次公式迭代得到。

除 $T_0$ 外，$[\bar\pi^n]^{-1}T_0$ 的四次旋转轨道准确由
$B_n^*(U)=0$ 参数化。由于 $[\bar\pi^n]$ 的整模型是 étale，
模 $p$ 有 $r_n$ 个互异根；它们既非 $U=0$，也非 $U=1$。
它们与 $B_n$ 没有共同根：后者是原 $[\bar\pi^n]$ 核的轨道。
因此在这些实际点上，$4xy$、$B_n$、$k_n$ 全为单位。

模 $p$ 的 $B_n'$ 次数为 $r_n-1$，最高系数
$r_n b_0^n$ 是单位，因为 $r_n\equiv-1/4\bmod p$。
它不可能在上述全部 $r_n$ 个互异根上消失。至少一个根于是满足
$$
h_P\equiv136\,(4xy)(P)
\frac{B_n'(U(P))}{B_n(U(P))}\not\equiv0\pmod p.
\tag{12}
$$
$p=2,17$ 已在坏集合中。对该点，(9) 的一阶极系数模 $p$ 准确为
$$
-\frac{b_{17}^n k_n(P)^{136}}{2b_0^{4n}}\,h_P^2\ne0.
$$
故它是单位，证明完成。$\square$

特别，虽然三阶极系数深度为 $2n$、二阶极至少为 $n$，
一阶极不会随迭代统一变深。各层出现新的最高阶 $\bar\pi^n$ 挠点，
故 $\{T_p^nR_T\}_{n\ge0}$ 线性独立。
原 A/B 未补偿原函数的全 $T_p$ 轨道是无限维的。
此处的单位位于 (10) 的非原点全局方向；
没有把这个主部单位当成原完整中央导数。

## 4. 正 theta 全空间上的真正十六次周期

现在限制到 R282 已明确的正密度普通 ray 类
$$
\pi_0\equiv\gamma_5=-1+2i\pmod{544\mathbb Z[i]}.
\tag{13}
$$
所有实际全纯来源统一经 $[2]$ 进入 $\mathcal S_{272}$。
R282 的对称 Heisenberg lift 保完整模 $544=2\cdot272$ 相位。
其 $\gamma_5/\bar\gamma_5$ 乘子为
$$
\phi=217+108i\pmod{544},
$$
且直接平方得到
$$
\phi^2=65+88i,\quad \phi^4=289+16i,\quad
\phi^8=33,\quad \phi^{16}=1\pmod{544}.
\tag{14}
$$
因此准确阶为十六。

令 $\mathscr M_\gamma=[\gamma]_*[\bar\gamma]^*$。
由完整 Heisenberg 协变，
$\bigl(\mathscr M_{\gamma_5}/(2+i)\bigr)^{16}$
与全部 Heisenberg 作用交换。
不可约性使其为标量；已付的实际参考 $S_8(2\beta z)$，
$\beta=4-i$，在 $\mathscr M_{\gamma_5}$ 下的本征值是 $2+i$，
故该标量准确为一。

再由 R282 的同一参考定标，
$$
T_p=\mu_8\,\frac{\mathscr M_{\gamma_5}}{2+i},
\qquad \mu_8=b_{17}/b_8\in\mu_4.
$$
于是有全空间结论
$$
\boxed{T_p^{16}=1\quad\text{于整个 }\mathcal S_{272}.}
\tag{15}
$$
它不只在旧的十七维 $\mathcal H_+$ 成立。
原全纯来源的 $[2]$ 拉回是单射，且与 $T_p$ 交换，
因此 (15) 也准确作用于其未缩放的实际来源。

奇来源必须保 primary 的负号：
在迹中令 $w\mapsto iw$，$\mathscr M_{\gamma_5}$ 对偶来源等于
$\mathscr M_{2+i}$，对奇来源等于 $-\mathscr M_{2+i}$。
故 R283 的两个不同 $i$ 块有
$$
\boxed{
T_p|_{\mathcal V_i}=-\mu_8N_i,\quad N_i=M_i/(2+i);
\qquad
T_p|_{\mathcal U_i}=i\mu_8N_i^{\,u},\quad
N_i^{\,u}=M_i^{\,u}/(1-2i).
}
\tag{16}
$$
twisted 块的特征多项式为 $(X+1)(X^{16}-1)$。
untwisted 块则只有十二个不同角色，最小多项式为
$(X^4-1)(X^8+1)$；不能用 twisted 的十六角色替换它。
式 (15) 同时容许这两个真实相位和不同角色重数。

实际 unit 来源的相位在这个类上还能完全定出：
$$
\boxed{\mu_8=-1,\qquad
T_pA=A,\quad T_pB=-iB,\quad T_pH=-iH,\quad T_pC_\beta=-iC_\beta.}
\tag{16a}
$$
这不是由角色名称猜出的相位。固定真实 $\mathscr M_{2+i}$ 在
同一 $\sigma^{68}$ frame 给
$$
\mathscr M_{2+i}A=-(2+i)A,\qquad
\mathscr M_{2+i}B=i(2+i)B,\qquad
\mathscr M_{2+i}C_\beta=i(2+i)C_\beta.
$$
其完整有限证明是：对输出 $U=a$ 取五次纤维
$UQ_{2+i}^4-aK_{2+i}^4=0$，在该商环中用
$(K_{2-i}/K_{2+i})^{68}$ 乘真实拉回多项式再取迹。
三个输出由正 theta 证明知次数至多十七；固定 $a=2,\ldots,19$
的十八个准确值逐项满足上述恒等式，故多项式恒等式成立。
R248 已付 H 的同一个 $i(2+i)$ 本征值。
偶来源的 primary 负号为正，而原实际 $T_pA=A$；
因此全空间定标中的 $\mu_8$ 必须为负一，余下 (16a) 随之成立。
该证明只使用一个固定 norm-five 算子。

## 5. H 的连接项具有准确十七维轨道

R283 的实际固定 CM5 证书证明
$$
\dim\langle K_H,N_iK_H,\ldots,N_i^{15}K_H\rangle=16.
$$
在 (13) 上，(16) 给同样的真实 $T_p$ 轨道维数。
由 (2)、(15)，
$$
T_p^{16}K_H'= \kappa_p^{16}K_H',\qquad
T_pH=\mu_HH,\quad \mu_H=b_{17}/b_{136}\in\mu_4.
$$
$C_H=H-K_H'$ 的极小多项式因此准确是
$$
\boxed{(X-\mu_H)(X^{16}-\kappa_p^{16}).}
\tag{17}
$$
两个因子的根具有不同 $p$-adic 赋值，且 $K_H'$ 的十六个角色都非零。
所以该轨道维数为十七。

更准确地，$\langle T_p^nC_H\rangle$ 与原正 theta 空间的交恰为
$\mathbb Q_pH$。证明不只用维数：若一个正 theta 来源 $K$ 的导数
仍属同次数正 theta 空间，则其 quasi-period 变换多出的
$N\eta_\lambda K$ 必须对每个周期消失，故 $K=0$。
共同 $[2]$ 拉回使这段论证没有半特征歧义。
于是导数轨道与正 theta 空间的交为零，证明上述交空间断言。

在这整个真实十七维空间中，两投影是整算子
$$
\boxed{
\mathscr P_0=\frac{T_p^{16}-\kappa_p^{16}}{1-\kappa_p^{16}},
\qquad
\mathscr P_1=\frac{1-T_p^{16}}{1-\kappa_p^{16}},
\qquad
\mathscr P_0C_H=H,\quad \mathscr P_1C_H=-K_H'.
}
\tag{18}
$$
分母是 $p$ 单位。这里的第二部分是原导数来源，未被第一部分的
中央零自动消去。

本篇的固定精确证书还给
$$
a_1=[U^{16}]N_iP_G=
\frac{193506512778819}{1286339269178163200}
+\frac{20715995503813}{551288258219212800}i\ne0.
$$
因为 $K_H'(0)=0$、$V_iU^{16}=-z+O(z^5)$，
真实 p-depletion 的两个 core 项给
$$
\boxed{
M_{C_H}(0)=\frac{\kappa_p}{b_8}a_1,\qquad
M_{K_H'}(0)=-\frac{\kappa_p}{b_8}a_1.
}
\tag{19}
$$
这不是质量零的伴随；固定坏集合以外，两个质量的赋值恰为一。

## 6. 两个原 A/B 零的全纯 CM 补偿

为了不把 (9) 的极族藏入一个错误的有限块，使用 R283 的真实
固定 CM 补偿。其存在、唯一性也可直接由以下三角算子核实。
对于 $K=\sigma^{68}yP(U)$，实际 (5) 给
$$
L K=\sigma^{68}\mathfrak L_uP,\qquad
\mathfrak L_uP=4U(U-1)P'+(70-68U)P.
\tag{20}
$$
它把次数至多十六的空间单射到次数至多十七的空间。
其唯一余核行 $\ell_u=(e_0,\ldots,e_{17})$ 由
$$
e_{17}=1,\qquad
e_j=\frac{34-2j}{35-2j}e_{j+1}\quad(0\le j\le16)
\tag{21}
$$
完全确定。

取原
$$
C_\beta=\vartheta(2\beta z)
=\sigma^{68}\bigl(UQ_\beta(U)^4+K_\beta(U)^4\bigr),\qquad \beta=4-i.
$$
这里 $Q_\beta,K_\beta$ 是 R248 的真实 division 多项式。
固定精确值为
$$
e_\beta=\ell_u(C_\beta/\sigma^{68})
=\frac{194313797443214851}{4512611027925}
-\frac{218295166992512}{31556720475}i\ne0.
$$
原边界准确满足
$\ell_u(S_i/\sigma^{68})=-B_i(0)/2$，$i=A,B$。
所以定义
$$
c_i=-\frac{B_i(0)}{2e_\beta},\qquad
E_i=S_i-c_iC_\beta
$$
后，存在唯一真正全纯的 $K_i^{\rm CM}\in\mathcal U_i$ 满足
$$
\boxed{L K_i^{\rm CM}=E_i,\qquad i=A,B.}
\tag{22}
$$
若 $q_j=[U^j](E_i/\sigma^{68})$，完整反解是
$$
p_0=q_0/70,\qquad
p_j=\frac{q_j+(72-4j)p_{j-1}}{70-4j}\quad(1\le j\le16);
$$
末项 $q_{17}=-4p_{16}$ 恰由 (21) 保证。
这给出完整有理证明，并保原点质量及唯一 CM 补偿。
两列按 (7) 相组合时，CM 项准确抵消，回到原 $K_{AB}$。

R283 的固定证书证明，两列 $K_A^{\rm CM},K_B^{\rm CM}$ 的单独
$N_i^{\,u}$ 轨道各为十二维，但联合轨道恰为整个十七维 $\mathcal U_i$。
它们不是同一个无极组合所能替代的两条输入。

## 7. 三条完整中央零的统一有限转置

令
$$
K_A^\circ=K_A^{\rm CM},\quad K_B^\circ=K_B^{\rm CM},\quad
K_H^\circ=K_H,\qquad c_H=0,
$$
$$
E_i=S_i-c_iC_\beta,\qquad D_i=E_i-(K_i^\circ)'.
$$
对三列，$E_i,K_i^\circ$ 均为原共同正 theta 来源；
$D_i$ 是实际有界连接来源。式 (2)、(15) 给
$$
\boxed{
E_i=\frac{T_p^{16}D_i-\kappa_p^{16}D_i}{1-\kappa_p^{16}}.
}
\tag{23}
$$

使用同一个真实参考 $J_\vartheta=M_\vartheta$，
$J_\vartheta(0)=1-b_0^{-1}\in\mathcal O^\times$。
置列向量
$$
\mathbf q_n(u)=\frac1{J_\vartheta(u)}
\begin{pmatrix}
M_{D_A}^{[n]}(u)\\M_{D_B}^{[n]}(u)\\M_{D_H}^{[n]}(u)
\end{pmatrix},
\qquad
\mathbf c=(c_A,c_B,0)^{\mathsf t}.
$$
R282 的全环带转置与 (23) 给完整的全 $u$ 恒等式
$$
\boxed{
\frac{(M_A,M_B,M_H)^{\mathsf t}}{J_\vartheta}
=
\frac{b_{17}^{16}(b_0^{32d})^u\mathbf q_{16}(u)
-\kappa_p^{16}\mathbf q_0(u)}
{1-\kappa_p^{16}}
+((2\beta)^d)^u\mathbf c.
}
\tag{24}
$$
没有把 $p$-core 当成原单位 Mellin，也没有省去尺度导数。
原三个质量为零。因此，三个完整中央导数同时为零，准确等价于
以下保留质量的一阶关系，加上恒成立的第一式：
$$
\boxed{
\begin{aligned}
b_{17}^{16}\mathbf q_{16}(0)
-\kappa_p^{16}\mathbf q_0(0)
&=-(1-\kappa_p^{16})\mathbf c,\\
b_{17}^{16}\bigl(\mathbf q_{16}'(0)
+32d\log_pb_0\,\mathbf q_{16}(0)\bigr)
-\kappa_p^{16}\mathbf q_0'(0)
&=-(1-\kappa_p^{16})d\log_p(2\beta)\,\mathbf c.
\end{aligned}}
\tag{25}
$$
右侧是原 A/B 各自真实边界的固定 CM 对数；H 行为零。
参考导数已由同一个 $J_\vartheta$ 商完整保留。

也可对 $T_p^jD_i$ 写 (24)–(25)，但其 unit 部分只是
$T_p^jE_i=T_p^jS_i-c_iT_p^jC_\beta$；
这给原三本征线和已付 CM 参考的实际线性组合。
它不把 $L(T_p^jK_i^\circ)$ 宣称为该 unit 部分。
真实连接交换差仍须支付。

现在可准确给出全部实际有限空间：
$$
\boxed{
\dim\left\langle T_p^nD_A,T_p^nD_B,T_p^nD_H:n\ge0\right\rangle
=37=4+33.
}
\tag{25a}
$$
其中 unit 部分恰为 $\langle A,B,H,C_\beta\rangle$，
导数部分的维数恰为 $17+16=33$。
证明是把 (23) 的两个整投影作用于联合轨道。
由 (16a) 和 $c_A\ne0$，$E_A$ 的 unit 轨道恢复 A 与 $C_\beta$；
再加入 $E_B,H$ 恰恢复上述四个独立来源。
独立性也可在原来源直接核对：A/B 的首个不同 jet 非零，
$C_\beta(0)=1$，而 H 属于不同的真实二挠块。
导数部分由 R283 的 A/B 联合十七维轨道及 H 的十六维轨道得到。
两个原函数块不同，且微分在正 theta 空间上单射，
所以其导数维数相加。第 5 节的 quasi-period 论证证明
unit 部分与导数部分相交为零，完成 (25a) 的证明。

因此 (25) 约束的是这三十七维真实空间的 unit 投影，
不是三十三条新增导数中央零。这个区别在 (23) 的整投影上是准确的，
并非从未知秩作出的估计。

## 8. 与 R282 原奇原函数的准确角比较

R277/R282 的奇来源为 $G_R=WP_R$，
$P_R(U)=U^{16}R_H(1/U)$，$W=-y\vartheta\sigma^{67}$。
由 $Z_H=(v-1)R_H+Z_H(1)$ 得到真正的固定多项式同构
$$
\boxed{
\mathfrak J(P)=4\,\frac{P-P(1)U^{17}}{U-1},\qquad
\mathfrak J(P_G)=P_R.
}
\tag{26}
$$
在 $1,U,\ldots,U^{16}$ 基下，
$[\mathfrak J]_{kj}=-4$（$k\ge j$），其余为零；
故 $\det\mathfrak J=(-4)^{17}$，在所有奇好素位整可逆。
分子中的 $P(1)U^{17}$ 是真实边界补偿，不能删去。

将 R283 的 $L$ 对角 $-4(17-j)$ 和 (26) 合并，得到
$$
\boxed{
H=W\,\mathfrak B(P_R),\qquad
\mathfrak B(Q)=U(U-1)Q'+(17-16U)Q,\qquad
\det\mathfrak B=17!.
}
\tag{27}
$$
这是原 H 对实际 $P_R$ 的准确一阶方程。
它保留整个 source carrier，并不把 $\mathfrak B$ 解释成 Mellin 标量。

在真正函数上，(26) 等价于
$$
\boxed{
G_R=\frac{4K_H}{y}+\frac{Z_H(1)Y}{t}.
}
\tag{28}
$$
右侧的两个全局极部相消；在原正式圆盘内都是实际有界来源。
其 Mellin 转置第一项为加法卷积
$4\langle\nu_{K_H}\otimes\nu_{1/y},K_u(x+y)\rangle$，
不是两个 Mellin 的乘积。第二项是显示的真实边界来源。

对 R282、R283 的实际矩阵，固定精确计算进一步给
$$
\boxed{\operatorname{rank}(N_+\mathfrak J+\mathfrak JN_i)=17.}
\tag{29}
$$
加号正是 (16) 的 primary 奇偶负号，不是任选的交换比例。
证书给非零 determinant norm。
所以这个付费同构没有把旧 $G_R$ 的 principal 中央轨道
与 $K_H$ 的 tame-one 轨道等变识别。真正的不同观察仍是 (28) 的
卷积、边界和 (29) 的交换差。

## 9. H 原函数的另一条完整非零观察及其准确参考

R283 的 twisted 双 CM 角色投影是
$$
\Pi_{\rm CM}K_H=a\,G_i(\beta z)+b\,G_i(\bar\beta z),
\quad G_i=-x\vartheta\sigma^3,\quad b=\bar a,
$$
$$
a=-\frac{21155876867859}{1286339269178163200}
-\frac{208102787314109}{7718035615068979200}i\ne0.
\tag{30}
$$
它是 raw $N_i$ 的 $-1$ 角色。
在 (13) 的真实 $T_p$ 下，该角色本征值为 $\mu_8$。
由于 $T_p$ 与固定单位 $\beta$ 的缩放交换，同样有
$T_pG_i=\mu_8G_i$。

注意 $G_i(z)=-z+O(z^5)$，故它本身不能用作 principal 分支的
质量参考。使用真正的
$$
J_i=M_{G_i'},\qquad
\boxed{J_i(0)=-(1-\kappa_p/b_8)\in\mathcal O^\times.}
\tag{31}
$$
这是 (2) 和原 p-depletion 的两个零次 core 项直接给出的等式。
它不是把 $J_8$ 的质量移到另一个 tame 分支。

于是全部 $u$ 有
$$
\frac{M_{(\Pi_{\rm CM}K_H)'}(u)}{J_i(u)}
=a\beta(\beta^d)^u+b\bar\beta(\bar\beta^d)^u,
$$
从而
$$
\boxed{
\left.\frac d{du}
\frac{M_{(\Pi_{\rm CM}K_H)'}(u)}{J_i(u)}
\right|_{u=0}
=d(a\beta\log_p\beta+b\bar\beta\log_p\bar\beta)\ne0.
}
\tag{32}
$$
两个十七素位的赋值证明 $\beta,\bar\beta$ 乘法独立；
R245/R246 已使用的 Brumer 定理给这两个原对数的代数线性独立，
而 (30) 的系数非零。

因
$\Pi_{\rm CM}=16^{-1}\sum_{j=0}^{15}(\mu_8^{-1}T_p)^j$，
(32) 给至少一条真实 $T_p$ 轨道的完整 tame-one 归一观察非零。
但原 H 的完整零准确作用于 (18) 的 $\mathscr P_0C_H$，
不作用于 $\mathscr P_1C_H$。原三零的全部已付信息是 (25)；
尚无恒等式把它扩成 (32) 的消失。

## 10. 固定精确证书与继续接口

本篇新增的
[固定精确脚本](../scripts/check-original-prime-core-derivative-and-angular-primitive.py)
及 [完整证书](../scripts/check-original-prime-core-derivative-and-angular-primitive.json)
给 (14)、(19)、(26)、(27)、(29) 的固定运算和非零 determinant norm。
实际 unit 相位的十八纤维证明保存在
[固定 CM5 脚本](../scripts/check-original-positive-cm5-eigenvalues.py)
及 [全部精确迹值](../scripts/check-original-positive-cm5-eigenvalues.json)；
它们给 (16a) 和 (25a) 所用的真实相位。
R283 的
[真实两个 i 块证书](../scripts/check-original-first-order-i-block-and-cm5.json)
给原函数多项式、两个真正 CM5 矩阵、A/B 的完整 CM 补偿、
联合十七维轨道和 (30) 的全部系数。

新的原算术接口已经是 (25)、(28) 和 (29)：
要从原三零得到 R282 或 (32) 的非零观察的消失，
仍须支付显示的连接交换差或加法卷积。
(9)–(12) 证明未补偿 A/B 的极项不能靠增加一个固定极方向、
或只看最高极的深度来省掉；(22)–(25) 则提供了保全部原输入的
准确有限替代。主问题保持开放。
