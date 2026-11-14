# R504 — 两条真实十八度轴、六十五度核心与完整正交矩形

日期：2026-11-14。**状态：已证明。** 本篇在 R496 的同一个原六
sigma 联合及四个实际来源中，付清原反射所产生的第二条十八度轴。
两轴的和、差给范数 $65,7$ 的正交方向。范数 $65$ 方向的原
半系数不能删除：在真实二重覆盖的整个 $\mathcal S_{260}$ 中，
本文付清全部 Heisenberg 中心、绝对标量和十六个原 quarter
来源的作用。由此得到改变原 $Y$ 的完整 scalar 核、与原自由
sigma 方向的全部双深矩形，以及两个有相反完整返回的真实三层管。

这里没有把投影后的独立伴随条件认成未投影的混合管，也没有
给 $H_{\rm ref}$ 或其他辅助来源赋中央零。主目标仍未完成。

## 1. 原变量、真实反射及两条十八度轴

沿用 R493、R496 的原规范
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2.
\tag{1}
$$
令 $\xi=(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0)$ 为六个未缩放的独立
原 sigma 输入，$\rho_0=-\nu_\sigma^{\otimes6}/84$。本篇的
$Y_s$ 是物理输出，不是 R501 中双倍后的生成轴：
$$
\begin{aligned}
Y_s&=(\delta,2\delta,3+\omega,2-\omega,1,2)\xi,\\
W&=(\delta,2\delta,3+\omega,2-\omega,3\delta,4)\xi.
\end{aligned}
\tag{2}
$$
R493 的 $Y_s$ 保持矩阵 $T$ 满足 $T^3=I$。其实际 $W$ 保持
反射记为 $\mathcal U$；在 $I=(\xi_1,\xi_3,\xi_4,c)$ 上
$$
\mathcal U=I-v_0\bar v_0^{\,t}/2,\qquad
v_0=(1,\omega,-\omega^2,-1)^t,
\tag{3}
$$
其余两输入固定。原来源身份为
$$
h=\omega^2T_*\rho_0,\qquad
\mathcal U_*\rho_0=\rho_0+h.
\tag{4}
$$
所有等式均保原六输入及 canonical lift。

置
$$
V=V'=\tfrac12WT
=(2+2\omega,\delta,2+2\omega,0,2+\omega,2)\xi,
\qquad V^\flat=V\mathcal U .
\tag{5}
$$
两个实际方向的 Gram 是
$$
\boxed{
\begin{pmatrix}
\langle V,V\rangle&\langle V,V^\flat\rangle\\
\langle V^\flat,V\rangle&\langle V^\flat,V^\flat\rangle
\end{pmatrix}
=\begin{pmatrix}18&29/2\\29/2&18\end{pmatrix},\qquad
\det=455/4.}
\tag{6}
$$
这里 $\langle a,b\rangle=\sum a_i\bar b_i$。尤其二者不正交。

定义真正正交的物理输出
$$
\boxed{
R=V+V^\flat,\qquad
C=\tfrac12\bar v_0^{\,t}\xi_I,\qquad
a=-2+\omega.}
\tag{7}
$$
准确有
$$
V-V^\flat=aC,\quad
V=\frac{R+aC}{2},\quad V^\flat=\frac{R-aC}{2},\quad
\langle R,R\rangle=65,\quad
\langle C,C\rangle=1,\quad \langle R,C\rangle=0.
\tag{8}
$$
所以差轴的范数是 $Na=7$。它的深条件与 $C$ 的深条件等价，
但其非零单位尺度 $a$ 在测试中仍须保留。

两个完整行向量为
$$
\begin{aligned}
R={}&(5+\tfrac72\omega,\ 2+4\omega,\ \tfrac52+3\omega,\
-\tfrac12-\tfrac32\omega,\ 3+\tfrac52\omega,\ 4),\\
C={}&(\tfrac12,\ 0,\ -\tfrac12-\tfrac12\omega,\
-\tfrac12\omega,\ -\tfrac12,\ 0).
\end{aligned}
\tag{9}
$$

## 2. 真实二重覆盖及四个完整伴随

(9) 的半系数要求保覆盖。用生成轴 $2R,2C$，其完整 theta
次数是 $260,4$。给 $i=2,3,4,5$ 定义四个固定伴随行
$$
Q_i=260e_i-4\bar R_iR-260\bar C_iC .
\tag{10}
$$
每个 $Q_i$ 都在 $\mathcal O_K^6$；它们与 $R,C$ 正交。完整
坐标矩阵
$$
\mathcal A=(2R,2C,Q_2,Q_3,Q_4,Q_5)^t
\tag{11}
$$
的行列式绝对值是 $8\cdot260^4$。例如先把 (10) 中的 $R,C$
项消去，只剩四个 $260e_i$，余下两列 $\xi_1,d_0$ 的 $R,C$
小行列式为 $-2$。故 (11) 在当前普通 $p$ 是整自同构。

完整 Gram 的第一块是 $\operatorname{diag}(260,4)$，与后四轴
的全部交叉项为零。后四轴之间的非对角 Gram 原样保留；附证书
列出整个矩阵，未将它替换为四个不明独立来源。原 quarter
平移在后四轴若留下 flat character，可在这四轴再取固定
$[4]$ 覆盖，第一两轴不变。

设
$$
f_m=\mathsf T^{72}_{m/4,W}\rho_0,\qquad
m\in\mathcal O_K/4\mathcal O_K.
\tag{12}
$$
由于
$$
\langle W,2R\rangle=116+28\omega,\qquad
\langle W,2C\rangle=0,
$$
(12) 在第一 $2R$ 轴的平移恰为
$(29+7\omega)m/260\in E[260]$，在 $2C$ 轴不平移。
所以全部十六个实际 $f_m$ 确实在同一
$\mathcal S_{260}\otimes\mathcal S_4$ 与完整伴随格中。没有
把原 $\mathcal S_{65}$ 的形式核心免费用于这些 quarter 来源。

## 3. 奇六十五度的绝对标量

现有固定 ray 满足
$$
g=\pi_0/\bar\pi_0\equiv1\pmod{130},\qquad
g\equiv131\pmod{520},\qquad g\equiv3\pmod8.
\tag{13}
$$
附证书由 R488 的
$\pi_0\equiv23776637887+77586679170\omega
\pmod{81011810880}$
直接核 (13)；以后已用的兼容细分保持这些条件。

在 R454 已固定的 odd sigma 半特征与完整中心规范中，
$g\equiv1\bmod130$ 使整个 $\mathcal S_{65}$ 的归一核心为一个
单位标量，记为 $\chi_{65,p}$，简称 $\chi$。
其绝对平方不是猜测。取真实两输入
$$
F(z,t)=\sigma(z-8t)\sigma(8z+t).
\tag{14}
$$
两轴次数都是 $65$，交叉项为零；每一轴恰有一个奇系数和一个
偶系数，故两个半特征都是原 odd sigma 特征。变换行列式是
$65$，在当前 $p$ 可逆。两个原 sigma 同时取深的标量是
$(-\lambda)^2=\lambda^2$；在两个输出使用 whole odd 核则是
$\lambda^2\chi^2$。非零完整来源 (14) 因而严格给
$$
\boxed{\chi^2=1.}
\tag{15}
$$
本文不猜测这两个可能符号中的一个，也不需要新加 ray。

## 4. 整个 $\mathcal S_{260}$ 核及绝对锚

令 $N=260$，在标准 Schrödinger 基上
$Xe_j=\zeta_N^je_j,\ Ze_j=e_{j+1}$。完整比值
$g=131=1+N/2\bmod2N$ 由算子
$$
P_Ne_j=e_{131j}
\tag{16}
$$
实现。所有中心都可直接读出。对于 $b,c\in\{0,1\}$，
$$
\mathsf T^{N}_{(b+c\omega)/2}e_j
=(-1)^{b(j+c)}e_{j+130c}.
$$
因此
$$
\boxed{P_N=\frac12\sum_{t\in E[2]}\mathsf T^N_t,\qquad P_N^2=I.}
\tag{17}
$$
(17) 的绝对符号由整个非零子空间
$[2]^*\mathcal S_{65}^{\rm odd}$ 定标。其三个非零半周期
canonical lift 都是 $-1$，故 $P_N=-1$ 于这个子空间。
真实单位拉回 $[2]^*$ 与完整 ordinary restriction 相容；
该子空间上的真实归一核心是 $\chi$。由不可约完整 Heisenberg
交织的唯一性，
$$
\boxed{K_{260}=-\chi P_N.}
\tag{18}
$$
这里 (14)、(17)、odd 半特征都参与了绝对定标；没有只用
projective 比值写 (18)。

原 $C$ 轴的 whole $\mathcal S_4$ 核是
$K_4=R_C$，其物理反射就是 (3)。R506 以完整 frame、$g=3\bmod8$
及非零 $\sigma(2z)$ 锚支付这个规范：$\sigma(2z)$ 的真实归一
核心和反射特征均为 $-1$。下面保该已付的实际 $C$ 核。

## 5. 全部原 quarter 来源的格相位

先在 $\rho_0$ 上比较 $R$ 半平移与 $C$ 半平移。准确整数向量
$$
k=R-\omega C
=(5+3\omega,\ 2+4\omega,\ 2+3\omega,\
 -1-2\omega,\ 3+3\omega,\ 4)
\tag{19}
$$
满足
$$
\sum Nk_i=66,\qquad
\sum\overline{\omega C_i}\,k_i=-1.
\tag{20}
$$
对任意 $\ell\in\mathcal O_K$，六个 sigma 的周期半特征乘积为
$(-1)^{66N\ell}=1$；(20) 的交替部分为零，完整指数 cocycle
也为一。所以是整个来源身份
$$
\mathsf T_{R,\ell/2}^{260}\rho_0
=\mathsf T_{C,\omega\ell/2}^{4}\rho_0.
\tag{21}
$$
(21) 的右边有 $\omega\ell$，不能把它换成同一 $\ell$。

再置 $k_0=W/2-C$。完整证书给
$$
\sum N(k_0)_i=19,\qquad
\sum\bar C_i(k_0)_i=-1.
$$
同一个周期公式准确得到
$$
\mathsf T^4_{C,\ell/2}\rho_0
=(-1)^{N\ell}\mathsf T^{72}_{W,\ell/2}\rho_0.
\tag{22}
$$

现在在 (21) 左右保原 $W$ quarter 平移。
令 $\det(\ell,m)$ 是基 $(1,\omega)$ 上的整数交替式，
$[x]_\omega$ 是 $\omega$ 系数。由
$\langle W,R\rangle=58+14\omega$，完整交换因子是
$$
(-1)^{[(29+7\omega)\bar\ell m]_\omega}.
$$
另一次 $W$ 平移相乘的 canonical 因子是
$(-1)^{\det(\omega\ell,m)}$。两指数模二相同，因为
$29+7\omega\equiv\omega^2\bmod2$，故准确相消。
由 (21)、(22)，整个 $P_N$ 的十六列公式遂为
$$
\boxed{
P_N f_m=f_m-\frac12\sum_{\ell\in\mathcal O_K/2}f_{m+2\ell}.
}
\tag{23}
$$
这证明保六个原变量、所有隐藏条件的来源等式，而非首边际相等。

沿用 R496
$$
e_0=\rho_0,\quad e_1=K_W\rho_0,\quad
h=e_1+e_2=-\tfrac12\sum_{\ell\in\mathcal O_K/2}f_{2\ell},\quad
u=e_0+h/2,\quad v=e_1-h/2,\quad z=q-h/2.
\tag{24}
$$
在标签 $m\bmod4$ 上，$v$ 在十二个 primitive quarter 的系数
都是 $1/4$；$z$ 的这些系数是 $(-i)^{Nm}/4$；
$u,h$ 支持在四个 even 标签。由 (23) 逐项得到
$$
\boxed{
P_N(u,v,z,h)=(u,-v,z,-h),\qquad
K_R(u,v,z,h)=\chi(-u,v,-z,h).
}
\tag{25}
$$
这里 $K_R$ 表示实际物理 $R$ 方向的归一核心。单位尺度 $2$
不改变其深条件或原规范标量。

## 6. 完整正交双深矩形与所有物理测试

对 $r,s\ge0$，记原物理收缩
$$
A_{R,r}=I+\frac{\kappa^r-1}{65}\bar R^{\,t}R,\qquad
A_{C,s}=I+(\kappa^s-1)\bar C^{\,t}C.
\tag{26}
$$
它们交换，保 (10) 的四个完整伴随，并且准确分别缩放 $R,C$。
R506 的实际 $C$ 源作用为
$\mathcal U(u,v,z,h)=(u,v,-z,-h)$。
由 (18)、(25)、正交性及同一完整张量格，
$$
\boxed{
\begin{aligned}
\nu_u|_{R\in p^r,\ C\in p^s}
 &=\chi^r\lambda^{r+s}(-1)^r(A_{R,r}A_{C,s})_*\nu_u,\\
\nu_v|_{R\in p^r,\ C\in p^s}
 &=\chi^r\lambda^{r+s}(A_{R,r}A_{C,s})_*\nu_v,\\
\nu_z|_{R\in p^r,\ C\in p^s}
 &=\chi^r\lambda^{r+s}(-1)^{r+s}(A_{R,r}A_{C,s})_*\nu_z,\\
\nu_h|_{R\in p^r,\ C\in p^s}
 &=\chi^r\lambda^{r+s}(-1)^s(A_{R,r}A_{C,s})_*\nu_h.
\end{aligned}}
\tag{27}
$$
特别 $r=s=n$ 时，$v,z$ 是**同一个**完整标量
$\chi^n\lambda^{2n}$，而 $u,h$ 的标量是
$(-\chi)^n\lambda^{2n}$。这保所有四伴随的任意紧开条件与
连续测试，不能将该实际矩形缩成一个边际断言。

第一输出与旧 $W$ 的准确变化为
$$
\boxed{
\begin{aligned}
Y_s\circ A_{R,r}A_{C,s}
 &=Y_s+(\kappa^r-1)\frac{34+\omega}{65}R
         +(\kappa^s-1)(1+3\omega)C,\\
W\circ A_{R,r}A_{C,s}
 &=W+(\kappa^r-1)\frac{58+14\omega}{65}R,\\
V\circ A_{R,r}A_{C,s}
 &=(\kappa^rR+a\kappa^sC)/2,\\
V^\flat\circ A_{R,r}A_{C,s}
 &=(\kappa^rR-a\kappa^sC)/2.
\end{aligned}}
\tag{28}
$$
因此 (27) 真正改变 $Y_s$，不能在原中央权中把这部分省掉。
环带、单位补集和多个深矩形都由 (27) 作相邻差或容斥；
(28) 的全部指示函数和 Mellin 权随之转置。

## 7. 两条十八度轴的相反完整返回及实际三层管

R496 的实际两层 $V$ 核为 $F$，满足 $Fv=z,Fz=-v$；
$Fu=u,Fh=h$。由于 $\mathcal U$ 是真实单位反射、保持完整
来源与坐标格，其共轭是实际 $V^\flat$ 两层核。由
$\mathcal U(v,z)=(v,-z)$，准确有
$$
\boxed{
\begin{aligned}
\nu_v|_{V\in p^2}&=\lambda^2(A_{V,2})_*\nu_z,&
\nu_v|_{V^\flat\in p^2}&=-\lambda^2(A_{V^\flat,2})_*\nu_z,\\
\nu_z|_{V\in p^2}&=-\lambda^2(A_{V,2})_*\nu_v,&
\nu_z|_{V^\flat\in p^2}&=\lambda^2(A_{V^\flat,2})_*\nu_v .
\end{aligned}}
\tag{29}
$$
这里 $A_{L,2}=I+(\kappa^2-1)\bar L^{\,t}L/18$。两个
第一权分别读
$$
Y_s\circ A_{V,2}
=Y_s+(\kappa^2-1)\frac{17-3\omega}{18}V,\quad
Y_s\circ A_{V^\flat,2}
=Y_s+(\kappa^2-1)\frac{17+4\omega}{18}V^\flat.
\tag{30}
$$

还可把 (25)、(29) 合成两个真实的单管条件。
在正交 $(R,C)$ 平面中置 $A=A_{R,1}$、$B=A_{V,2}$；它们
保四个完整伴随，实际矩阵是
$$
A=\begin{pmatrix}\kappa&0\\0&1\end{pmatrix},\qquad
B=\frac1{72}
\begin{pmatrix}
7+65\kappa^2&65a(\kappa^2-1)\\
\bar a(\kappa^2-1)&65+7\kappa^2
\end{pmatrix}.
\tag{31}
$$
直接求逆给完整格的准确像：
$$
\boxed{
\begin{aligned}
AB\mathcal O^6
 &=\{R+a\kappa C\in p^3\mathcal O\},\\
BA\mathcal O^6
 &=\{(65+7\kappa^2)R+65a(1-\kappa^2)C\in p^3\mathcal O\}.
\end{aligned}}
\tag{32}
$$
四伴随没有附加限制。(32) 第一行本身蕴含 $R\in p\mathcal O$；
第二行本身蕴含 $V\in p^2\mathcal O$，且逆像的另一坐标仍整。
例如第二行消去 $R$ 后，另一逆像坐标的主系数是
$72/(65+7\kappa^2)$，为单位。

同一个 $\nu_v$ 在这两个完整管上准确返回
$$
\boxed{
\nu_v|_{AB\mathcal O^6}
 =\chi\lambda^3(AB)_*\nu_z,\qquad
\nu_v|_{BA\mathcal O^6}
 =-\chi\lambda^3(BA)_*\nu_z.
}
\tag{33}
$$
所以 (33) 对任意完整测试都是两个有确定相反符号的实际来源
等式。附 $C$ 单位时，第一管有 $v_p(R)=1$，第二管有
$v_p(R)=0$；两管不相交。这个不相交断言并不允许删除其
补域，也不将两个不同的 $Y_s$ 转置权认成同一个权。

## 8. 回到原五个 sigma 的新增 scalar 方向

R493 的原矩阵逐项给
$$
CT=\omega^2\xi_4,\qquad
\boxed{RT=(3+\omega,\ 2\delta,\ 6+3\omega,\ 0,\ -1+\omega,\ 4).}
\tag{34}
$$
因此 (4)、$K_Rh=\chi h$ 将 (25) 合法运输到原 $\rho_0$：
(34) 的新 $65$ 度轴具有真实 scalar core $\chi\lambda$，
完整保独立 $\xi_4$ 和它的四个其余伴随。
五个非零 sigma 系数的范数为
$$
7,\quad12,\quad27,\quad3,\quad16,
$$
总和 $65$。这不把一个零质量 theta 来源认作新的曲线。

原五输入总和仍为
$$
Z_{27}=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+c+2d_0.
$$
准确
$$
\langle Z_{27},RT\rangle=34+\omega,\qquad
27\cdot65-N(34+\omega)=632=8\cdot79.
\tag{35}
$$
因此这是原五 sigma 中确实改变 $Y_s=Z_{27}+(2-\omega)\xi_4$
的第二个已付 scalar 方向，不是原 $Z_{27}$ 的重复缩放。

## 9. 与三曲线中央条件的准确边界

R501 已付完整同伴随行
$$
P_{\rm new}v=S_{\rm new}\otimes\Lambda_{\rm old},\qquad
P_{\rm new}z=-S_{\rm new}\otimes\Lambda_{\rm old},
$$
参考行也按同一 $\Lambda_{\rm ref}$ 反号。
(27)、(29)、(33) 给这些原来源的实际新深域与 word-domain。
可是 $R,V,V^\flat$ 均改变 $Y_s$；(28)、(30)、(31) 显示
这种变化不为零。故不能直接把未经相应 CM 分支转置的原
$Y$ 单位中央放到这些管上。当前原三条秩二曲线中央零所给的
独立伴随行仍须按 R483、R501 的完整 projector 运输。

新增内容是原六输入上付清的 $65$ 核、正交矩形、两个有相反
来源返回的实际三层管，以及原五 sigma 中 (34) 的真实 scalar
方向；它们没有预付尚缺的混合管补域消元。

## 证书与依赖

- [精确可执行 JavaScript 证书](../scripts/check-r504-original-two-axis65-core.js)；
  [全部 Gram、十六列相位和完整物理 frame](../scripts/check-r504-original-two-axis65-core.json)。
  证书中的整数和二进制有理运算均在精确范围内；相同主体已在
  当前 V8 环境实际执行，全部断言通过。
- [R454：odd 全核心规范及真实两 sigma 平方锚](R454-original-odd33-core-and-exact-residual-slope-transport.md)。
- [R493：原六 sigma 几何及 $T,\mathcal U$](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R496：真实十八度轴、全部 quarter 相位与四态](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R501：完整 CM 交换和同一五伴随行](R501-whole-cm-exchange-and-identical-five-companion-rows.md)。
- [R506：原反射方向整个四度核心与完整 W/C 矩形](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)。
