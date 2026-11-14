# R513 — 两个隐藏 odd 核、反射交域与原 B0 的完整积分核

日期：2026-11-14。**状态：已证明。** 本篇在 R509 的同一个六 sigma 来源中，将剩余两输入的共同核心分解成两个有绝对定标的单轴核心。它们与 R506 的真实反射一起给精确的交叠域，并把原 $B_0$ 的反射运输写成一个保留隐藏输入的积分核。

新增 ray 仅把已有 $\pi_0\equiv2\bmod7$ 提升为 $\pi_0\equiv2\bmod49$。两条隐藏轴的真实系数都为 $\chi_{65}\lambda$，没有增加独立符号。反射没有下降成一个四变量几何变换；下文完整保留它在隐藏变量上的作用。本文不把尚未知的受限中央赋为零。

## 1. 同一原来源和两条正交隐藏轴

沿用
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad
\gamma=3+\omega,\qquad \gamma_{103}=11+2\omega,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad \beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d=p-1.
\tag{1}
$$
$\chi_{65}\in\{1,-1\}$ 是 R504 已付的同一个实际 odd 符号；
它与 R500 的 $\chi_V$ 不作未经证明的识别。

六个原输入按
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,x=\xi_4,c,d_0)^t,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84
\tag{2}
$$
排列。保 R509 的完整 $(Z,V,H,x,Q_1,Q_2)$ 框架，其中
$$
\begin{aligned}
Q_1={}&(-3-9\delta)\xi_1/14+\xi_2
 +(9-\delta)c/14+(9+13\delta)d_0/14,\\
Q_2={}&(11+5\delta)\xi_1/14+\xi_3
 +(1+3\delta)c/7+(-13+3\delta)d_0/7.
\end{aligned}
\tag{3}
$$
$Z,V,H,x$ 的 Gram 为 $\operatorname{diag}(27,3699,98777,1)$；
最后两行的 Gram 是
$$
G_Q=\frac17
 \begin{pmatrix}40&-6-19\delta\\-6+19\delta&46\end{pmatrix}.
\tag{4}
$$
前四行与后两行的全部交叉项均为零。

定义
$$
\boxed{
Q_0=Q_1+\omega Q_2,\qquad
Q_b=(13+7\omega)Q_1+(8+11\omega)Q_2.
}
\tag{5}
$$
更直接的正交构造是
$$
q=\langle Q_2,Q_0\rangle=(-29-4\delta)/7,\qquad
Q_b=\gamma(5Q_2-qQ_0).
$$
精确得到
$$
\boxed{\langle Q_0,Q_0\rangle=5,\quad
\langle Q_b,Q_b\rangle=515,\quad
\langle Q_0,Q_b\rangle=0.}
\tag{6}
$$
(5) 的行列式为 $5\gamma$，是当前普通处的单位。
实际原输入中的整行为
$$
\begin{aligned}
7Q_0={}&(-11-6\omega)\xi_1+7\xi_2+7\omega\xi_3
 +(-2-3\omega)c+(5-3\omega)d_0,\\
7Q_b={}&(-6-23\omega)\xi_1+(91+49\omega)\xi_2
 +(56+77\omega)\xi_3\\
&+(25+48\omega)c+(-94+27\omega)d_0.
\end{aligned}
\tag{7}
$$
因此整个新框架
$$
\mathcal F=(Z,V,H,x,Q_0,Q_b)
\tag{8}
$$
具有对角 Gram
$$
\boxed{G=\operatorname{diag}(27,3699,98777,1,5,515).}
\tag{9}
$$
其行列式为 $-380997\cdot5\gamma$；完整逆等于
$\bar{\mathcal F}^{\,t}G^{-1}$。附证书给出全部矩阵及其双侧逆。
这里仍是六个原输入的整单位坐标变换，没有改变实际联合测度。

## 2. 原半特征、完整中心和绝对 scalar

在 R509 的固定 ray 上增加
$$
\boxed{\pi_0\equiv2\pmod{49}.}
\tag{10}
$$
这与原模七条件兼容，其他已固定素因子与新增的七次幂部分互素。
沿用 $\pi_0\equiv2\bmod5$、$\pi_0\equiv2\bmod13$、
$\pi_0\equiv1\bmod103$ 及原模二条件。于是
$$
\boxed{
g_\pi=\pi_0/\bar\pi_0\equiv1\pmod{490},\qquad
g_\pi\equiv1\pmod{50470}.
}
\tag{11}
$$
这是 $2\cdot245$ 和 $2\cdot25235$ 的完整中心同余，
不能用原模七的条件代替。

固定所有正交伴随，以 $7\bar Q_i^{\,t}z$ 作实际原输入的变化方向，
$Q_i$ 的物理值变化为 $7N(Q_i)z$。两种物理尺度 $35$、$3605$
在当前处均为单位；原 sigma 系数为 (7) 的共轭整行。
这给真正的 theta 度数
$$
N(7Q_0)=245,\qquad N(7Q_b)=25235.
\tag{12}
$$
(7) 的五个非零系数模二全部为单位，故五个 odd 半特征的乘积
仍为标准 odd 半特征。与所有伴随的 Hermitian 交叉项为零，
所以没有随伴随变量变化的第一轴 flat twist。

由 (11)，完整 canonical Heisenberg 生成元及其共同中心都不变。
不可约性给两个 whole odd 核各为一个 scalar；还须绝对定标。
R504 已付整个 odd $\mathcal S_{65}$ 的真实核
$\chi_{65}I$ 及 $\chi_{65}^2=1$。取
$$
\gamma_{13}=4+\omega,\qquad N\gamma_{13}=13.
$$
非零固定拉回
$$
[\gamma_{13}]^*\mathcal S_5^{\rm odd}
 \subset\mathcal S_{65}^{\rm odd}
$$
与真实普通 core 交换。两个空间均已由完整中心知其 whole 核为
scalar，故比较这个非零拉回，严格得到 $\chi_5=\chi_{65}$。
再用非零固定拉回
$$
[7]^*\mathcal S_5^{\rm odd}\subset\mathcal S_{245}^{\rm odd},
\qquad
[7\gamma_{103}]^*\mathcal S_5^{\rm odd}
 \subset\mathcal S_{25235}^{\rm odd},
\tag{13}
$$
得到
$$
\boxed{
K_{245,p}=K_{25235,p}=\chi_{65}I
}
\tag{14}
$$
于各自的整个标准 odd 空间。上述 CM 乘子的范数都是奇数，
保持唯一 odd 半特征，且在普通处都是单位；比较不使用中央导数。

回到实际物理输出，(14) 给
$$
\boxed{
Q_0:\chi_{65}\lambda,\qquad Q_b:\chi_{65}\lambda.
}
\tag{15}
$$
这些是原完整来源的单轴核心，保其余五个输入和全部条件。

## 3. 原四态上的单轴矩形

沿用 R496、R506、R509 的实际四态 $(u,v,z,h)$。所有构造它们的
旧 $W$ 平移、完整 $W$ 核及 $F=K_{W'/2}^2$，都与 (5) 正交：
$$
Q_0,Q_b\perp Y,T_c,W,W',W_2,R.
\tag{16}
$$
所以这些操作与两条核心严格交换，包含原 quarter 中心和原
覆盖。由原 $\rho_0$ 上的 (15) 逐步传递，每一实际四态均有
同一个 (15)；没有把 quarter 来源直接重认成新的标准 odd 格。

记 $D_{r,s}$ 在 (8) 中固定前四坐标、将 $Q_0,Q_b$ 分别乘以
$\kappa^r,\kappa^s$。对任一实际四态 $\mu$ 及 $r,s\ge0$，
$$
\boxed{
\nu_\mu|_{\{Q_0\in p^r,\ Q_b\in p^s\}}
=(\chi_{65}\lambda)^{r+s}(D_{r,s})_*\nu_\mu.
}
\tag{17}
$$
它保任意其余坐标测试和实际紧开条件。
共同深度 $n$ 时的系数为 $\lambda^{2n}$，与 R509 已付的
两个隐藏输入共同核心完全一致。

令 $\nu_{\mu,4}$ 为忘掉 $Q_0,Q_b$ 的真正推前。对任意只依赖
$(Z,V,H,x)$ 的连续测试 $f$，准确有
$$
\int_{Q_0,Q_b\in p^n}f\,d\nu_\mu
=\lambda^{2n}\int f\,d\nu_{\mu,4}.
\tag{18}
$$
第一 $Y/W$ 的完整 CM 行与此推前交换，仍沿用 R483、R501、
R509 已付的周期、tame 型和 companion 质量。
(18) 不把一个含隐藏变量的测试变成四变量测试。

## 4. C 的真正隐藏部分及其反射轴

R506 的同一个物理输出是
$$
C=(\xi_1+\omega^2\xi_3-\omega x-c)/2,\qquad N(C)=1.
$$
在 (8) 中精确分解为
$$
\boxed{C=C_4+C_H,}
\tag{19}
$$
$$
\begin{aligned}
C_4={}&\left(-\frac1{18}-\frac{\delta}{27}\right)Z
 +\frac{-3+19\delta}{7398}V
 +\frac{127+24\delta}{98777}H+\frac{1-\delta}{4}x,\\
C_H={}&\frac{-11+5\delta}{70}Q_0
       +\frac{-31+23\delta}{3605}Q_b .
\end{aligned}
\tag{20}
$$
完整 Gram 给
$$
\boxed{N(C_4)=72/103,\qquad N(C_H)=31/103,\qquad
\langle C_4,C_H\rangle=0.}
\tag{21}
$$
两个隐藏系数都非零。本文没有为 $C_4$ 单独赋一个核心。

定义
$$
a_0=\langle Q_0,C\rangle=(-11-5\delta)/14,\qquad
a_b=\langle Q_b,C\rangle=(-31-23\delta)/7.
\tag{22}
$$
其范数分别为 $1,52$，故当前普通处均为单位。
原反射 $\mathcal U=I-2\bar C^{\,t}C$ 给
$$
\boxed{
Q_0^{\mathcal U}=Q_0-2a_0C,\qquad
Q_b^{\mathcal U}=Q_b-2a_bC.
}
\tag{23}
$$
它们与原两轴的交叉项为
$$
\langle Q_0,Q_0^{\mathcal U}\rangle=3,\qquad
\langle Q_b,Q_b^{\mathcal U}\rangle=411.
$$
例如 $Q_0-a_0C$ 是范数四、与 $C$ 正交的实际行，
但本文不从这一个范数计算推断其单轴核心。

R506 给完整来源作用
$$
\mathcal U_*(u,v,z,h)=(u,v,-z,-h),\qquad
\mathcal U_*\rho_0=\rho_0+h,\qquad W\mathcal U=W.
\tag{24}
$$
用 (24) 共轭 (17)，两条反射轴 (23) 也在同一个四态空间中
各有真实系数 $\chi_{65}\lambda$。
其物理压深为 $\mathcal U D_{r,s}\mathcal U$ 的对应单轴部分；
不另猜新的标准半特征。它们保旧 $W$，但通常改变第一 $Y$。

## 5. 全部真实交叠域

对 $r,s\ge0$，定义完整四条件事件
$$
\mathcal E_{r,s}
=\{Q_0\in p^r,Q_b\in p^s,
          Q_0^{\mathcal U}\in p^r,Q_b^{\mathcal U}\in p^s\}.
$$
由 (22)、(23) 的单位系数，准确有
$$
\boxed{
\mathcal E_{r,s}
=\{Q_0\in p^r,Q_b\in p^s,C\in p^{\max(r,s)}\}.
}
\tag{25}
$$
证明只是将每一对条件相减：第一对恰要求 $C\in p^r$，
第二对恰要求 $C\in p^s$；反向代入同样直接成立。

共同深度时写 $\mathcal E_n=\mathcal E_{n,n}$。此时 (20) 给
$$
\boxed{
\mathcal E_n
=\{Q_0,Q_b,C\in p^n\}
=\{Q_0,Q_b,C_4\in p^n\}.
}
\tag{26}
$$
对于不等深的 (25)，不能把 $C$ 换成 $C_4$：
较浅的隐藏变量仍可能与 $C_4$ 相消。
(25)、(26) 是同一个原六输入中的事件恒等式，不是两个边际
事件的拼接。$\mathcal E_{r,s}$ 也由定义在 $\mathcal U$ 下不变，
因为 $\mathcal U$ 交换每对轴并且 $\mathcal U^2=I$。

为完整列出实际物理运输，令 $c$ 为 (20) 在 (8) 的六个系数行。
则
$$
A_{C,n}=I+(\kappa^n-1)G\bar c^{\,t}c.
\tag{27}
$$
其六个坐标的增量都是 $(\kappa^n-1)C$ 乘以下列系数：
$$
\left(-\frac32+\delta,\quad
 \frac{-3-19\delta}{2},\quad
 127-24\delta,\quad\frac{1+\delta}{4},\quad a_0,\quad a_b\right)^t.
\tag{28}
$$
$C$ 自身乘以 $\kappa^n$，其正交伴随全部固定。
R506 的完整核是 $\lambda^n(A_{C,n})_*\mathcal U_*^n$。
用 $\kappa^n=-1$ 代入 (27) 就是原 $\mathcal U$，
因此没有把隐藏坐标从真实矩阵中删除。

## 6. 原 B0 上的精确反射积分核

保 R497、R503 的同一个
$$
Y=Z+\bar\gamma x,\qquad T_c=\gamma Z-27x,
\qquad
\mathcal B=\{Z,Y,T_c\text{ 均为单位}\}.
\tag{29}
$$
$V,H$ 在 $\mathcal B$ 中不限，$x$ 也不限；尤其保留 $x$ 深支及
两条真实近相消排除。令
$$
f_u(Y,T_c)=\langle Y\rangle^{du}
          \mathfrak h_{b,p}^{\times}(T_c/\Omega)
\tag{30}
$$
为 R497(21) 的完整正多项式测试。R503 的 $B_0(u)$ 正是将 (30)
在 $\mathcal B$ 上对 $\nu_{\rho_0,4}$ 积分。

实际 Hermitian 计算给
$$
\boxed{
a_Y=\langle Y,C\rangle=1+3\omega,\qquad
a_T=\langle T_c,C\rangle=-12-5\delta.
}
\tag{31}
$$
所以
$$
Y\mathcal U=Y-2a_YC,\qquad
T_c\mathcal U=T_c-2a_TC.
\tag{32}
$$
在 $\mathcal E_n$ 上，$C\in p^n$。
当 $n\ge1$ 时，(28)、(32) 保持 $Z,Y,T_c$ 各自的单位条件。
故 $\mathcal E_n\cap\mathcal B$ 是真正的 $\mathcal U$ 不变域。

由 (24)，完整六输入上首先得到
$$
\begin{aligned}
&\int_{\mathcal E_n\cap\mathcal B}
 f_u(Y-2a_YC,T_c-2a_TC)\,d\rho_0\\
&\hspace{8mm}=
 \int_{\mathcal E_n\cap\mathcal B}f_u(Y,T_c)\,d\rho_0+
 \int_{\mathcal E_n\cap\mathcal B}f_u(Y,T_c)\,dh.
\end{aligned}
\tag{33}
$$
现在才能使用两条真实隐藏核心。
令 $D_n=D_{n,n}$；它固定前四坐标，将隐藏坐标乘以 $\kappa^n$。
由于 (26)，$D_n^{-1}\mathcal E_n=\{C_4\in p^n\}$。
并且
$$
C\circ D_n=C_4+\kappa^nC_H.
\tag{34}
$$
对 (33) 的三项逐一用 (17)，取消共同的 $\lambda^{2n}$，
得到本篇的完整四变量边界接口：
$$
\boxed{
\begin{aligned}
&\int_{\{C_4\in p^n\}\cap\mathcal B}
 f_u(Y,T_c)\,d\nu_{h,4}\\
&=\int_{\{C_4\in p^n\}\cap\mathcal B}
 \Big[
 f_u\!\left(Y-2a_Y(C_4+\kappa^nC_H),
            T_c-2a_T(C_4+\kappa^nC_H)\right)\\
&\hspace{48mm}-f_u(Y,T_c)
 \Big]\,d\rho_0 .
\end{aligned}}
\tag{35}
$$
右侧仍在原六输入上积分，$Q_0,Q_b$ 已释放为全部原整域，
但它们通过 $\kappa^nC_H$ 完整出现在测试中。
左侧才是真正四输入推前。两边的 $Z,Y,T_c,C_4$ 条件均取原坐标，
没有暗改成反射后的另一组管。

(35) 对任意在单位域解析的 $f_u(Y,T_c)$ 同样成立。
还可以在两边同时乘任意旧 $W$ 的连续测试或实际紧开域指示，
因为 $\mathcal U$、$D_n$ 都固定 $W$。因此原旧 $W$ 混合管
在这条恒等式中可以完整保留。

对 (35) 在 $u=0$ 求导，右侧准确为
$$
\begin{aligned}
d\int_{\{C_4\in p^n\}\cap\mathcal B}
\Big[&
\log\langle Y-2a_YD\rangle\,
 \mathfrak h_{b,p}^{\times}((T_c-2a_TD)/\Omega)\\
&-\log\langle Y\rangle\,
 \mathfrak h_{b,p}^{\times}(T_c/\Omega)\Big]\,d\rho_0,
\qquad D=C_4+\kappa^nC_H.
\end{aligned}
\tag{36}
$$
这保留 log 项与多项式测试的全部法向碰撞。
$u=0$ 本身也给真实质量差；不能在求导前将它删去。

在 R497 的固定坏素数之外，全部多项式系数整且 $\Omega$ 为单位。
(35) 中 $D\in p^n$，故质量差和 (36) 的积分均在 $p^n\mathcal O$
中。这个整性界来自同一真实域上的完整测试差，并不声称其首项
非零，也不声称高阶隐藏矩为零。

## 7. 与原算术中央和未解补域的准确关系

R503 已付
$$
J_S(u)=B_0(u)+\beta\mathcal A(u,\kappa),
\tag{37}
$$
并付 $\partial_u\mathcal A(0,\kappa)$ 的单位第五阶及赋值五。
(35) 对 $B_0$ 内的真实 $C_4$ 深子域给一条新的混合 $Y$ 关系；
它保留了对应 $h$ 行和全部隐藏积分核。

尤其 $\nu_{h,4}$ 虽有第一 $Y$ 边际 $\omega^2\nu_S$，
本篇左侧含 $C_4$ 深条件和固定 $T_c$ 测试，不能由这一边际
直接赋中央零。第一 CM 投影在 (17) 中与隐藏方向交换，
却不与 (32) 的混合 $Y$ 反射免费交换。
若把 $\kappa^nC_H$ 从 (35) 删除，就已经更换了真实测试；
若将 $C_4$ 当成已经支付的单轴核心，则更换了已知来源结构。

因此本篇支付的是原固定 $B_0$ 的真实反射交域和完整积分方程。
(37) 的外域抵消仍须由这些方程或进一步算术关系控制。
主目标仍未完成。

## 证书与依赖

- [精确 BigInt/CM 证书](../scripts/check-r513-hidden-odd-cores-and-reflection-kernel.mjs)；
  [完整矩阵及数据](../scripts/check-r513-hidden-odd-cores-and-reflection-kernel.json)。
  同一证书函数已在 V8 执行通过，核了全部六行、双侧逆、对角 Gram、
  两个 odd 整行、完整反射交叉块及 (31)，不是有限采样猜测。
- [R509：同一五 sigma 的完整两框架、四输入推前及隐藏耦合](R509-original-five-sigma-two-y-frames-and-common-st-source.md)。
- [R506：整个 degree4 反射核和原四态](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)。
- [R504：实际 degree65 odd 符号和绝对定标](R504-original-two-axis65-core-and-complete-rectangles.md)。
- [R497：完整正伴随算术测试及全部第五阶](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R503：同一单位测试、全部浅环带及固定 B0](R503-original-unit-annuli-and-single-shallow-boundary.md)。
