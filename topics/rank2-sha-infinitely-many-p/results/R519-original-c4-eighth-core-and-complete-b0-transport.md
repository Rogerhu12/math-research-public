# R519 — C4 的 whole 八层核、完整交域返回与 B0 的真实移权

日期：2026-11-14。**状态：已证明。** 本篇支付 R513 中尚未使用的 $C_4$ 八层返回核心。它在原全部十六个 $W$ 四挠来源上成立，保全部隐藏输入，并严格下降到 R509 的同一个四输入。原旧 $W$、两条隐藏轴与本篇返回可以组成真正的深度矩形。

这不会使 $B_0$ 的单位条件保持不变。下文明确给出返回后的三条单位线及完整 Mellin/伴随测试，也保原单位补域。没有为 $C_4$ 猜一个一层 scalar。

## 1. 同一个实际 C4 轴和整周期

沿用 R513 的六输入
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,x=\xi_4,c,d_0)^t,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84,
$$
及完整正交框架
$$
(Z,V,H,x,Q_0,Q_b),\qquad
G=\operatorname{diag}(27,3699,98777,1,5,515).
\tag{1}
$$
符号 $\lambda,\beta=-\lambda,\kappa=p\lambda^2,\chi_{65}$、普通周期
及固定 ray 全与 R513 相同。本篇不新增 CRT 条件。

R513 已付
$$
C=C_4+C_H,\qquad
N(C_4)=72/103,\quad N(C_H)=31/103,\quad C_4\perp C_H,
$$
$$
\begin{aligned}
C_4={}&\left(-\frac1{18}-\frac{\delta}{27}\right)Z
 +\frac{-3+19\delta}{7398}V
 +\frac{127+24\delta}{98777}H+\frac{1-\delta}{4}x .
\end{aligned}
\tag{2}
$$
此处先保原六输入。清分母的实际整行是
$$
\boxed{
\begin{aligned}
A=206C_4={}&(41-2\omega)\xi_1+(42-42\omega)\xi_2
 +(-41-43\omega)\xi_3\\
&-103\omega x-101c+(4+6\omega)d_0.
\end{aligned}}
\tag{3}
$$
精确计算给
$$
\boxed{N(A)=29664=288\cdot103,\qquad
 A\perp W,\ Q_0,\ Q_b.}
\tag{4}
$$
(3) 有四个模二非零系数，故六个原 odd sigma 半特征在该轴
上的乘积为标准 even 半特征。

这里的 whole theta 度数是 $29664$，不是把物理范数 $72/103$
直接当成一个 theta 度数。固定全部正交伴随，沿
$\bar A^{\,t}z$ 移动原变量，物理值准确为
$$
A=29664z,\qquad C_4=144z.
\tag{5}
$$
$144$ 是当前普通处的单位，故返回后仍使用原物理 $\kappa$，
没有另改输出尺度。

完整伴随可以显式取为
$$
R_j=\bar A_6\xi_j-\bar A_jd_0,\qquad 1\le j\le5,
\tag{6}
$$
其中 $A_6=4+6\omega$、$N(A_6)=28$。矩阵 $(A,R_1,\ldots,R_5)$
的行列式为 $-\bar A_6^{\,4}N(A)$，当前处为单位；第一轴与后五轴
的全部交叉项为零，后五轴的非对角 Gram 原样保留。
因此 (5) 的 theta 空间归属是完整输入的断言。

对 R496 的全部实际来源
$$
f_t=T^{72}_{t,W}\rho_0,\qquad t\in E[4],
\tag{7}
$$
(4) 使平移在第一 $A$ 方向的参数为零。每个 $f_t$ 都处于同一个
标准 $\mathcal S_{29664}$ 与完整伴随张量格；没有从其四挠标签
删去原 flat twist，而是它在本轴上准确为零。

## 2. 整个 59328 中心及绝对八层锚

R496 已付当前 ray 的完整同余
$$
g=\pi_0/\bar\pi_0\equiv91+72\omega\pmod{576},
\qquad
g^8\equiv289=1+288\pmod{576}.
\tag{8}
$$
R509 的 $\pi_0\equiv1\bmod103$ 又给 $g\equiv1\bmod103$。
因为 $103$ 为奇数，CRT 准确推出
$$
\boxed{
g^8\equiv29665=1+29664\pmod{59328}.
}
\tag{9}
$$
例如一个完整代表为
$$
g\equiv35227+51912\omega\pmod{59328};
$$
附证书逐次相乘给第八次幂 (9)。

记 $N=29664$。在标准 even $\mathcal S_N$ 的完整 canonical
Heisenberg 群上，乘 $1+N$ 给恒等交织。两个指标上的新增中心
指数是 $\exp(\pi i(2+N)ab)=1$；这里只因 $N$ 为偶数才可如此
消去。于是 $K_{N,p}^8$ 在整个不可约 Heisenberg 空间上为 scalar，
但其绝对值仍须支付。

取
$$
\gamma_{103}=11+2\omega,\qquad
\Theta(12\gamma_{103}z)\in\mathcal S_{29664},
\tag{10}
$$
因为 $N(12\gamma_{103})=14832$。
这是原 degree2 参考 $\Theta$ 的非零固定 CM 拉回。
CM 乘子在普通处为单位，故其实际普通核心仍是
$\beta=-\lambda$，归一核心为 $-1$。
将 $K_{N,p}^8$ 的待定 scalar 作用到此非零锚上，得到一。
所以在**整个**标准空间中准确有
$$
\boxed{K_{29664,p}^{\,8}=I.}
\tag{11}
$$
没有只在一个来源上验证后便把标量推广到整空间；
先有 (9) 的 whole 交织，再由 (10) 定标。

## 3. 原十六来源、四态及真实旧 W 矩形

置 $r_4=72/103$，在原六输入定义
$$
P_{4,n}=I+\frac{\kappa^n-1}{r_4}\bar C_4^{\,t}C_4.
\tag{12}
$$
它将 $C_4$ 乘 $\kappa^n$，固定全部正交伴随，实际像格为
$\{C_4\in p^n\}$。由 (5)、(7)、(11)，对每个 $f_t$ 及其任意
线性组合，特别 R496、R506 的四态 $\mu\in\langle u,v,z,h\rangle$，
$$
\boxed{
\nu_\mu|_{\{C_4\in p^{8r}\}}
=\lambda^{8r}(P_{4,8r})_*\nu_\mu,\qquad r\ge0.
}
\tag{13}
$$
中间一层到七层的来源不在本文中预先压回四态；
(13) 只在已付 whole 八层返回上使用。

$C_4$ 与 $W,Q_0,Q_b$ 正交，所以相应物理缩放交换。
令 $P_{W,m}$ 为原旧 $W$ 的实际压深，$D_{a,b}$ 为 R513 的
两个隐藏缩放。对任意 $m,a,b,r\ge0$，整个来源准确满足
$$
\boxed{
\begin{aligned}
\nu_\mu|_{\substack{W\in p^m,\ C_4\in p^{8r}\\
                    Q_0\in p^a,\ Q_b\in p^b}}
={}&\lambda^{m+8r}(\chi_{65}\lambda)^{a+b}\\
&\cdot(P_{W,m}P_{4,8r}D_{a,b})_*K_W^m\nu_\mu .
\end{aligned}}
\tag{14}
$$
它保其余所有实际输入。整 $W$ 核交换 $u,v$，反号 $z,h$；
这仍是原来源矩阵，(14) 没有给不同物理域作商。

由于 (12) 固定两个隐藏输出，它与真正推前交换。
故对 R509 的四输入测度 $\nu_{\mu,4}$，同一个 (13) 原样成立。
第一轴矩阵是
$$
\boxed{
I_4+\frac{\kappa^n-1}{r_4}
G_4\bar c_4^{\,t}c_4,\qquad
G_4=\operatorname{diag}(27,3699,98777,1),
}
\tag{15}
$$
其中 $c_4$ 为 (2) 的四个显示系数。
这是本篇新的合法四输入操作；原 $\mathcal U$ 仍不是四输入变换。

## 4. R513 原交域现在有完整同源返回

沿用 R513 的实际事件
$$
\mathcal E_n
=\{Q_0,Q_b,Q_0\mathcal U,Q_b\mathcal U\in p^n\}
=\{Q_0,Q_b,C_4\in p^n\}
=\{Q_0,Q_b,C\in p^n\}.
\tag{16}
$$
当 $n$ 为八的倍数，(14) 给
$$
\boxed{
\nu_\mu|_{\mathcal E_n}
=\lambda^{3n}L_{3,n*}\nu_\mu,\qquad
L_{3,n}=P_{4,n}D_{n,n}.
}
\tag{17}
$$
$L_{3,n}$ 在真实三维子空间 $\langle C_4,Q_0,Q_b\rangle$ 上
同时乘 $\kappa^n$，固定其正交补。
$C$ 位于该子空间中，故 $L_{3,n}$ 与原反射 $\mathcal U$ 严格交换。
这说明 (17) 与 R513 的反射积分核相容；不是由来源关系猜到域相等。

还有一个可以准确取消的正交框架。令
$$
B_1=Q_0-a_0C,\qquad B_2=Q_b-a_bC,
$$
$$
a_0=(-11-5\delta)/14,\qquad a_b=(-31-23\delta)/7.
$$
它们与 $C$、旧 $W$ 正交，完整 Gram 是
$$
\boxed{
G_B=\begin{pmatrix}4&-7+\delta\\-7-\delta&463\end{pmatrix},
\qquad\det G_B=1800.
}
\tag{18}
$$
此行列式在当前处为单位；$B_1,B_2$ 内部并不正交。
同一个事件 (16) 准确等于
$\{C,B_1,B_2\in p^n\}$。
令 $P_{\mathcal B,n}$ 同时缩放 $\langle B_1,B_2\rangle$、
固定其正交补。R506 的 $C$ 核在偶数深度返回来源本身，
故可在上述相同事件中取消其真推前，得到
$$
\boxed{
\nu_\mu|_{\{B_1,B_2\in p^n\}}
=\lambda^{2n}(P_{\mathcal B,n})_*\nu_\mu,
\qquad 8\mid n.
}
\tag{19}
$$
逆推前只用于它的真实像格，因而是合法取消。
这是一条二输入共同核心；没有把它拆成两个未付单轴 scalar。

为显出其混合第一权，置
$$
D=31C_4-72C_H=103C_4-72C,\qquad N(D)=2232,\quad D\perp C.
\tag{20}
$$
设 $a_Y=1+3\omega$、$a_T=-12-5\delta$。
直接由正交投影相减得到
$$
Y\circ P_{\mathcal B,n}
 =Y+(\kappa^n-1)a_YD/72,\qquad
T_c\circ P_{\mathcal B,n}
 =T_c+(\kappa^n-1)a_TD/72.
\tag{21}
$$
(20) 只给实际行；本文没有单独为 $D$ 赋一层核心。

## 5. 原 B0 的三条准确单位线及完整测试

仍取
$$
Y=Z+\bar\gamma x,\qquad T_c=\gamma Z-27x,
\qquad\mathcal B=\{Z,Y,T_c\text{ 均为单位}\},
$$
$$
f_u(Y,T_c)=\langle Y\rangle^{du}
 \mathfrak h_{b,p}^{\times}(T_c/\Omega).
\tag{22}
$$
这是 R497、R503 同一个算术测试。
记
$$
a_Z=\langle Z,C_4\rangle=-3/2+\delta,\qquad
a_Y=\langle Y,C_4\rangle=1+3\omega,\qquad
a_T=\langle T_c,C_4\rangle=-12-5\delta.
$$
令 $b_L=103a_L/72$，$L=Z,Y,T_c$，以及
$$
Z_\perp=Z-b_ZC_4,\quad
Y_\perp=Y-b_YC_4,\quad
T_\perp=T_c-b_TC_4.
\tag{23}
$$
则 (12) 的真实第一权运输为
$$
\boxed{
L\circ P_{4,n}=L_\perp+\kappa^n b_LC_4
\qquad(L=Z,Y,T_c).
}
\tag{24}
$$
全部 $b_L$ 在当前处整。对 $n\ge1$，(24) 与 $L_\perp$ 模 $p$
相同，所以原三单位条件的确切拉回是固定事件
$$
\boxed{\mathcal B_\perp
=\{Z_\perp,Y_\perp,T_\perp\text{ 均为单位}\}.}
\tag{25}
$$
它通常不同于 $\mathcal B$。$x$ 在两个事件中都不被擅自限制为单位。

由 (13)，对 $n=8r\ge8$ 精确有
$$
\boxed{
\begin{aligned}
&\int_{\{C_4\in p^n\}\cap\mathcal B}
 f_u(Y,T_c)\,d\nu_{\mu,4}\\
&\quad=\lambda^n\int_{\mathcal B_\perp}
 f_u(Y_\perp+\kappa^nb_YC_4,\
     T_\perp+\kappa^nb_TC_4)\,d\nu_{\mu,4}.
\end{aligned}}
\tag{26}
$$
可以同时保任意旧 $W$ 测试或紧开条件，因为 (12) 固定 $W$。
对 (26) 求中央导数时，必须把两个显示参数同时代入原 log 权和
$\mathfrak h^\times$，不能只缩放第一 Mellin 参数。

以 $\mu=\rho_0$ 为例，定义
$$
B_{0,n}^{\rm out}(u)
=\int_{\mathcal B\cap\{C_4\notin p^n\}}
 f_u(Y,T_c)\,d\nu_{\rho_0,4}.
$$
R503 的同一个完整中央现在准确写为
$$
\boxed{
\begin{aligned}
J_S(u)
={}&\beta\mathcal A(u,\kappa)+B_{0,n}^{\rm out}(u)\\
 &+\lambda^n\int_{\mathcal B_\perp}
 f_u(Y_\perp+\kappa^nb_YC_4,\
     T_\perp+\kappa^nb_TC_4)\,d\nu_{\rho_0,4}.
\end{aligned}}
\tag{27}
$$
第一项的中央已有非零单位第五阶；后两项仍是完整实际补域。
(27) 并未由第一项非零就排除其余两项抵消。

## 6. 与隐藏反射积分核联用时的相位和域

R513(35) 在 $\mathcal B\cap\{C_4\in p^n\}$ 中保留
$$
C_4+\kappa^nC_H
$$
作为原 $\mathcal U$ 测试的真实参数。
若在 $8\mid n$ 时再用本篇 (13)，这个参数准确变为
$$
(C_4+\kappa^nC_H)\circ P_{4,n}
=\kappa^n(C_4+C_H)=\kappa^nC.
\tag{28}
$$
同时原 $Y,T_c$ 变成 (24)，单位域变成 (25)。
于是将 R513 核的两边都按 (13) 运输，并取消共同 $\lambda^n$，
得到
$$
\begin{aligned}
&\int_{\mathcal B_\perp}
 f_u(Y_n,T_n)\,d\nu_{h,4}\\
&\quad=\int_{\mathcal B_\perp}
 \big[f_u(Y_n-2a_Y\kappa^nC,\
          T_n-2a_T\kappa^nC)-f_u(Y_n,T_n)\big]\,d\rho_0,
\end{aligned}
\tag{29}
$$
其中
$$
Y_n=Y_\perp+\kappa^nb_YC_4,\qquad
T_n=T_\perp+\kappa^nb_TC_4.
$$
右侧仍在原六输入中积分，$C=C_4+C_H$，隐藏输入没有消失。
(29) 同样保旧 $W$ 条件。

由于 (17) 的三维同时缩放与 $\mathcal U$ 交换，(29) 是同一个
真实来源反射关系在准确域上的再表达；不能把它误读为独立新增的
零积分方程。它的用途在于让新的 $C_4$ 返回、原隐藏交域和旧
$W$ 管使用同一个可检验的测试，而不遗漏域外补偿。

## 证书、已登记的显示换基修正与范围

- [完整中心和原输入证书](../scripts/check-r519-c4-eighth-core-and-b0-transport.mjs)；
  [精确数据](../scripts/check-r519-c4-eighth-core-and-b0-transport.json)。
  同一 BigInt/CM 函数已在 V8 执行，核了 (3)、全部中心幂、Theta
  锚范数、原四输入块、两种正交投影及 (18)、(21)。
- R513 证书的显示函数已在独立提交 795725ad 中修正：$a+b\delta$ 在 $\mathbf Z[\omega]$
  中应显示为 $(a+b)+2b\omega$。原函数误将常数显示为 $a-b$。
  R513 正文整行、所有直接在 $\delta$ 基上运算的矩阵和证明均正确；
  整性及模二非零个数也不变。现脚本与 JSON 已重跑，显示整行与
  正文逐项吻合。
- [R513：隐藏 odd 核、真实反射交域和完整 B0 积分核](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R509：同一个四输入及真实隐藏耦合](R509-original-five-sigma-two-y-frames-and-common-st-source.md)。
- [R506：整个 C 反射核与旧 W 矩形](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)。
- [R496：模 576 完整中心和原十六来源](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R503：原固定 B0 及非零浅支](R503-original-unit-annuli-and-single-shallow-boundary.md)。

本篇的新结论是带完整中心的八层返回和 (14)、(17)、(19)、(26)
这些真实域公式。原三条 rank-two 算术来源的中央非零、以及固定
曲线上的无穷多个普通或惰性素数，仍待后续补域控制。
