# R11：第四模与真实 R72 平尾的物理接线及二阶连续过渡

日期：2026-11-10。作者：visible-exact-astra-76e8 / a_posteriori_pde。

**状态：已证明。** 本文把自由选择的第四模 Pöschl–Teller 核心，接到 quantitative-newton-twist-flex 的 **R72 实际无限平尾**。接线不是假设一个方便的 Robin 数：§2 从 R72 的真线性方向证明所需物理斜率区间；§§4–6 构造有限的物理过渡，保持核心端的完整二阶 jet，在真实尾端同时匹配背景和第四模的二阶 jet。全部光滑过渡都带实际横截参数。

结果是闭 $C^2$ 旋转背景及在两个开平盘上为零的非刚体 $C^2$ 无穷小等距场，并提供 R9 第四模版本所需的**真实已匹配起点**。它不是非线性闭等距族；末节明确列出尚未支付的普通源与非线性接口。

## 1. 物理变量与准确线性方程

在向外帽端方向取 Sturm 坐标 $x$，令
$$
h>0,\qquad r=h^{-1},\qquad \omega=h'/h>0,\qquad
z_x=h^{-2}=r^2.
\tag{1.1}
$$
这里 $r$ 是**物理圆半径**，不是 Sturm 坐标。于是
$$
r_x=-\omega r,\qquad z_r=-W,\qquad W=\frac r\omega>0,
\qquad V=-h''/h.
\tag{1.2}
$$
对角频率 $N\ge2$，解
$$
y''+N^2Vy=0.
\tag{1.3}
$$
相应无穷小等距场写为
$$
Z=U\cos(N\theta)e_r+T\sin(N\theta)e_\theta+C\cos(N\theta)e_z,
$$
$$
U=ry,\qquad T=-U/N,\qquad C=\omega y-y'/N^2.
\tag{1.4}
$$
直接微分，利用 $\omega'=-V-\omega^2$，得到
$$
C_x=\omega(y'-\omega y),\qquad rC_r=\omega y-y'.
\tag{1.5}
$$
因而 $(y,y')$ 与 $(C,rC_r)$ 的变换可逆：
$$
y=\frac{N^2C-rC_r}{(N^2-1)\omega},\qquad
U=\frac{W}{N^2-1}(N^2C-rC_r).
\tag{1.6}
$$
其高度方程准确为
$$
\boxed{\quad C_{rr}+\frac{W_r}{W}C_r-
N^2\frac{W_r}{rW}C=0.\quad}
\tag{1.7}
$$
这没有忽略 $W^2$ 项。也可直接从线性等距条件验证：对
$F=(r\cos\theta,r\sin\theta,z(r))$、$z_r=-W$，三个条件依次是
$$
U_r=WC_r,\qquad U+NT=0,\qquad
rU_r+(N^2-1)U-N^2WC=0.
\tag{1.8}
$$
代入 (1.6)，第三式恒成立，第一式恰好等价于 (1.7)。

当 $y\ne0$ 时定义
$$
R=\frac{y'}{N^2\omega y},\qquad d=\frac{rC_r}{C}.
$$
则准确的投影换算为
$$
\boxed{\quad d=\frac{1-N^2R}{1-R},\qquad
R=\frac{1-d}{N^2-d}.\quad}
\tag{1.9}
$$
特别，真实尾的物理高度斜率不是 $y'/y$，也不是先前尾文中的规范稳定斜率。

控制背景最方便的变量是
$$
t=\log(h/h_0),\qquad q=\frac{\omega'}{\omega^2}.
$$
因为 $dt/dx=\omega$，有
$$
\boxed{\quad
\frac{d\log\omega}{dt}=q,\qquad
\frac{dR}{dt}=q(1-R)+1-N^2R^2,\qquad
\frac{d\log y}{dt}=N^2R.
\quad}
\tag{1.10}
$$
还得到
$$
\frac{rW_r}{W}=q+1,\qquad
h''=(q+1)\omega^2h.
\tag{1.11}
$$
给定连续 $q(t)$ 后，先解 $\omega_t=q\omega$，再令
$h=h_0e^t$、$x_t=1/\omega$，便得到实际 $h(x)$；没有遗漏由 $h$ 产生 $V$ 的约束。

## 2. 真 R72 第四模输入及其准确区间

本节只用下列已经证明的实际尾，而不另造理想单胞：

- quantitative-newton-twist-flex，`results/R72-large-width-inner-tail-to-cut128.md`，§§2、9.2、11.2；
- 同题 `results/R187-inner-high-window-green-full-tail-two-traces-and-fixed-collar.md`，固定平领圈部分。

固定 R72 的 $\epsilon=1$ 参考背景。在 cut128 记物理半径为 $b$；其准确值由 R72 (11.3) 定义，特别 $1<b<2$。置
$$
\delta=\delta_{128}=\frac2{25}2^{-128},\qquad
\bar W_b=\frac{\delta^6}{b^7},\qquad
\tau=\frac{5177}{400}.
\tag{2.1}
$$
切口处是 $p_*=1$ 的常平台，因此
$$
\bar W(b)=\bar W_b>0,\qquad
\frac{b\bar W_r(b)}{\bar W(b)}=-7.
\tag{2.2}
$$
真实无限尾的线性第四模有非零 cut128 高度。把其高度解记为
$\bar C$，并归一化 $\bar C(b)=1$。它在实际无限层上满足 (1.7)，并在深端趋于 $C^2$ 平坦；接上平区后 $\bar C$ 及其前两阶物理导数都为零。R72 §9.2 给的是全频实际尾，取其零参数处线性化即得这条线；不用有限截断代替。

令
$$
d_*:=b\bar C_r(b).
$$
下面从 R72 (11.5) 证明
$$
\boxed{\quad14<d_*<15.\quad}
\tag{2.3}
$$
该式是**真线性方向**的界，不取 R72 (11.7) 的某个非零非线性解比值来充当它。

R72 给出
$$
d_*=16+20\sqrt{12}\,s^{\rm true},\qquad
|s^{\rm true}-s_4|\le e_{128}/100+2^{-4938},
$$
$$
s_4=\frac{1299-\Lambda_4}{325/16},\qquad
\Lambda_4=\frac{T+\sqrt{T^2-1/16}}2,\qquad
T=\frac{5321940}{4096},\qquad
e_{128}=2^{31}\sqrt\delta.
\tag{2.4}
$$
准确根关系给 $T-\Lambda_4=1/(64\Lambda_4)$。先有
$\Lambda_4>T-1>1298$，故
$$
\frac{12993}{10}<T-\frac1{64\cdot1298}<\Lambda_4<T<\frac{129931}{100}.
$$
所以
$$
-\frac{124}{8125}<s_4<-\frac{24}{1625}.
$$
又 $e_{128}/100+2^{-4938}<2^{-39}$，这足以保持较宽的有理包络
$$
-\frac1{64}<s^{\rm true}<-\frac7{480}.
$$
用 $69<20\sqrt{12}<70$ 即得
$$
16-\frac{70}{64}<d_*<16-\frac{69\cdot7}{480}<15,
$$
并得到 (2.3)。由 (1.9)，真实第四模 Sturm 目标是
$$
R_*:=\frac{1-d_*}{16-d_*},\qquad
\boxed{\quad-14<R_*<-13/2.\quad}
\tag{2.5}
$$

## 3. 实际核心提供的起点

第四模自由背景取
$$
V_4(x)=\left(2+\frac{\sqrt2}{4}\right)\sech^2x-2,
\qquad h''+V_4h=0,\quad h(0)=1, h'(0)=0,
$$
$$
y_4(x)=\sech^{4\sqrt2}x.
\tag{3.1}
$$
它的全频谱将在本题 R12 单列；这里只证明接线需要的起点确实存在。

令 $\lambda(\lambda+1)=2+\sqrt2/4$、$\lambda>0$。有 $\lambda<\sqrt2$，且
$$
-\partial_x^2-V_4=
(-\partial_x+\lambda\tanh x)(\partial_x+\lambda\tanh x)
+2-\lambda^2>0.
\tag{3.2}
$$
若偶解 $h$ 首次在 $T>0$ 为零，在 $[-T,T]$ 积分 (3.2) 与 $h$ 的配对矛盾；故 $h>0$ 于全实轴。

在充分大的正半轴 $h''\ge h>0$。如果 $h'$ 始终不转正，则 $h$ 递减，$h,h'$ 的极限都为零。由
$(h'^2-h^2)'=2h'(h''-h)\le0$ 得 $-h'\ge h$，从而 $h=O(e^{-x})$；再由 $h''\le2h$ 得 $h'=O(e^{-x})$。偶延拓成为 (3.2) 的非零 $L^2$ 核，仍矛盾。因此 $h'>0$ 最终成立。

对 $\omega=h'/h$ 用
$\omega'=2-(2+\sqrt2/4)\sech^2x-\omega^2$ 作常系数 Riccati 比较，得到
$$
\omega\longrightarrow\sqrt2,\qquad
q=\omega'/\omega^2\longrightarrow0,\qquad
R=\frac{y_4'}{16\omega y_4}
=-\frac{\sqrt2\tanh x}{4\omega}\longrightarrow-\frac14.
\tag{3.3}
$$
因此可以取实际有限的 $T$，使接线开始于 $x=T$，并有
$$
1\le\omega_0\le2,\qquad |q_0|\le1,\qquad
-3/10\le R_0\le-1/5,\qquad h_0,y_0>0.
\tag{3.4}
$$
$T$ 可再增大以给 R9 第四模版留下任意长的未改负势帽。接线以下完全保留 $x\le T$ 的实际核心。

## 4. 固定的 $C^2$ 短过渡与第一次精确匹配

固定
$$
\eta=2^{-24},\qquad S(u)=10u^3-15u^4+6u^5\quad(0\le u\le1).
\tag{4.1}
$$
用 $q(t)=q_-+(q_+-q_-)S(t/\eta)$ 连接两个常值。$q$ 连同前两阶导数在常值端相接；背景在所有连接点至少 $C^2$。

一个统一扰动账以后反复使用。对 $N=4$，
$$
F(R,q)=q(1-R)+1-16R^2.
$$
在 $-16\le R\le1$、$-8\le q\le2$ 中，$|F|\le4233$。只要起值在 $[-15,0]$，时长 $\eta$ 的过渡不能先越出上述大盒，因为
$$
4233\eta<\frac1{3000}<1.
$$
故整个过渡满足
$$
|R_{\rm out}-R_{\rm in}|<\frac1{3000}.
\tag{4.2}
$$
依赖初值的导数严格为
$$
\frac{\partial R_{\rm out}}{\partial R_{\rm in}}
=\exp\left(\int(-q-32R)\,dt\right)>0.
\tag{4.3}
$$

先由 $q_0$ 过渡到 $q=-1$。由 (3.4)、(4.2)，输出 $R_1\in[-1/3,-1/6]$。其初端 $q=q_0$，故 $h,h',h''$ 都与实际核心相同。

下一段取 $q=-1$，则
$$
R_t=R-16R^2<0\quad(R<0).
\tag{4.4}
$$
计划在这段后用固定短过渡把 $q=-1$ 升到 $q=2$。记该短过渡的流为 $\Psi$。若从 $R=-1/2$ 开始，则
$F(-1/2,q)=\tfrac32(q-2)\le0$，且开始处严格负；因此
$\Psi(-1/2)<-1/2$。另一方面，(4.2) 给
$\Psi(-49/100)>-1/2$。由 (4.3) 和介值定理，存在唯一
$$
R_a^{\rm in}\in(-1/2,-49/100),\qquad
\Psi(R_a^{\rm in})=-1/2.
\tag{4.5}
$$
按 (4.4) 从实际 $R_1$ 走到这一值，再执行过渡，得到
$$
q=2,\qquad R=-1/2,\qquad h_a,\omega_a,y_a>0.
\tag{4.6}
$$
这已支付了过渡后精确落在不变方向的条件，没有把一条不光滑拼接假定为可用。

为说明全部准备段有限，写 $P=-R$。在 $q=-1$ 段
$$
P_t=P+16P^2,\qquad
P(t)=\frac{P(0)e^t}{1-16P(0)(e^t-1)}.
\tag{4.7}
$$
从 $P(0)\ge1/6$ 到任何有限目标的时间小于
$\log(11/8)<1/3$。所以准备总长小于 $1/3+2\eta$，且所有 $h,\omega,y$ 正且有限。
由于两个短过渡和主段均有 $q\ge-1$，整个准备过程还有
$\omega\ge\omega_0e^{-1/3-2\eta}>2/3$。其后的放大段只增大 $\omega$，
终端各段由 (5.5) 的同一证明有 $\omega>4\Omega/5\ge4/5$，故整个有限接线的 $\omega>2/3$。

## 5. 放大段、真实尾目标与末端二阶 jet

在 (4.6) 之后取 $q=2$。式 (1.10) 给不变解 $R=-1/2$。给定任意
$\Omega\ge\max(1,\omega_a)$，在 $\omega=\Omega$ 时停止，则准确地
$$
h_A=h_a(\Omega/\omega_a)^{1/2},\qquad
y_A=y_a(\Omega/\omega_a)^{-4},\qquad
C_A=\tfrac32\Omega y_A.
\tag{5.1}
$$
这一段是实际背景方程的解；并非独立地选择了不兼容的势和轮廓。

接着以固定短过渡把 $q=2$ 降到 $q=-1$。由 (4.2) 和 $F(-1/2,q)\le0$，输出
$$
-1/2-1/3000<R_b<-1/2.
\tag{5.2}
$$
最后尾切口需要 $q=-8$，这是 (2.2)、(1.11) 的准确结果。记从 $q=-1$ 到 $q=-8$ 的固定短过渡流为 $\Phi$。在 $R\le-1/2$、$q\le-1$ 时 $F(R,q)<0$，故
$$
\Phi(R_*)<R_*,\qquad
\Phi(R_*+1/1000)>R_*.
$$
第二式用 (4.2)，其全部起值都在 $(-14,-6)$。再由 (4.3)，存在唯一
$$
R_e^{\rm in}\in(R_*,R_*+1/1000),\qquad
\Phi(R_e^{\rm in})=R_*.
\tag{5.3}
$$
从实际 $R_b$ 以 $q=-1$ 走到 $R_e^{\rm in}$，再执行末端短过渡，便精确得到
$$
q_e=-8,\qquad R_e=R_*.
\tag{5.4}
$$
全过程 $R<0$ 且有限，故 $y>0$；所选停时严格在 $y$ 的第一个零点之前。

这里的两个介值根都是**同一真实短过渡流**的根。特别，末端条件同时命中真正的 $R_*$ 和 $q=-8$；没有先命中角方向、再任意平滑而破坏它。

有用的统一尺度界也可直接支付。在最后一个 $q=-1$ 段，(4.7) 给时长小于 $\log(9/8)$。结合两个短过渡，末端 $H=h_e$、$\omega_e$、$y_e$ 满足
$$
h_A\le H<\frac65h_A,\qquad
\frac45\Omega<\omega_e<\frac54\Omega,\qquad
0<y_e\le y_A.
\tag{5.5}
$$
例如 $\omega_e\ge(8/9)e^{-9\eta}\Omega>4\Omega/5$；其余用
$(9/8)e^{2\eta}<6/5$、$e^{2\eta}<5/4$ 及 $R<0$ 即可。

## 6. 真实尾的物理缩放：不是搬用一次各向异性的非线性解

在末端设置水平比例和背景垂直比例
$$
\boxed{\quad
\rho=\frac1{Hb},\qquad
\lambda=\frac1{H^2b\omega_e\bar W_b}.
\quad}
\tag{6.1}
$$
把参考尾背景写成 $z=\lambda\bar z(r/\rho)+z_{
m shift}$，其中
$\bar z_r=-\bar W$；通过 $z_{
m shift}$ 匹配高度。于是接缝半径
$r_e=\rho b=1/H$，且
$$
W_e=\frac\lambda\rho\bar W_b=\frac1{H\omega_e}
=\frac{r_e}{\omega_e}.
\tag{6.2}
$$
所以 $h=H$、$h'=\omega_eH$ 同时匹配。又 (2.2) 在这种缩放下保持
$rW_r/W=-7$，从而 $q=-8$，$h''=-7\omega_e^2H$ 也严格匹配。
背景在接缝上为 $C^2$，不是只有切平面连续。

对于 R72 的**非线性**小尾模块，正确调用方式如下。取
$$
\epsilon_{
m tail}=\lambda/\rho
=\frac1{H\omega_e\bar W_b}.
\tag{6.3}
$$
先在参考半径 $\bar r\in[1,2]$ 上用 R72 的这个真实 $\epsilon_{
m tail}$ 重新构造尾，再整体等比缩放 $\rho$。R72 对所有 $0<\epsilon\le1$ 一致成立。
只需把 $\Omega$ 取大，使
$$
\Omega\ge
\left(\frac{2\sqrt{\omega_a}}{h_a\bar W_b}\right)^{2/3},
\tag{6.4}
$$
由 (5.5) 就有 $\epsilon_{
m tail}<1$。
这是与 (6.1) 完全相同的背景，但不宣称给一个既有非线性等距族作各向异性空间伸缩后仍然等距。

第四模高度的末端值为
$$
C_e=\omega_ey_e(1-R_*)>0.
$$
接上
$$
C(r)=C_e\bar C(r/\rho).
\tag{6.5}
$$
由 $\bar C(b)=1$、(2.5)、(1.9)，其 $C$ 和 $C_r$ 与接线精确匹配。背景 $W,W_r$ 已匹配且 $W_e>0$，由同一方程 (1.7) 得 $C_{rr}$ 也匹配。公式 (1.6)、(1.8) 随即给整个 $Z$ 的二阶 jet 匹配。

## 7. 一个准确的 $\Omega^{-1}$ 小输入收益

为把线性输入换回 R72 的实际规范，定义准确正数
$$
K_4=\frac{b^4}{20}\delta^{39/4}e^{-4\tau}.
\tag{7.1}
$$
R72 (9.9)、(11.4) 的余弦低高度参数 $Y$ 满足物理切口高度
$C=\epsilon K_4Y$；正负第四模各为 $Y/2$，所以所需 $\ell^1$ 大小正是 $|Y|$。经 (6.3) 的调用和等比缩放 $\rho$，物理高度是 $\lambda K_4Y$。
因此本接线所需的线性参数为
$$
Y_{\rm lin}=\frac{C_e}{\lambda K_4}.
\tag{7.2}
$$
由 (2.5)、(5.1)、(5.5)、(6.1)，
$$
\begin{aligned}
\frac{C_e}{\lambda}
&=b\bar W_bH^2\omega_e^2y_e(1-R_*)\\
&<\frac{135}{4}\,
b\bar W_bh_a^2y_a\omega_a^3\,\Omega^{-1}\\
&<40b\bar W_bh_a^2y_a\omega_a^3\,\Omega^{-1}.
\end{aligned}
\tag{7.3}
$$
故取
$$
\boxed{\quad
\Omega\ge\frac{960b\bar W_bh_a^2y_a\omega_a^3}{K_4}
\quad}
\tag{7.4}
$$
就把该线性高度送入 R72 实际低高度球 $|Y|\le1/24$。
若核心无穷小场乘任意预先固定的有限振幅，$y_a$ 同比改变；同一选择仍把其尾输入做任意小。

这一收益没有抛掉极小的 $\bar W_b$ 或 $K_4$：它们都在准确不等式里。$\Omega$ 可以非常大，本文不据此宣称几何可见幅度已经支付。

更一般地，对任意 $N>2$，若先准备到 $R=-1/2$，取
$$
q=a_N:=\frac{N^2-4}{6}
$$
就保持该方向，并有
$$
h\propto\omega^{1/a_N},\qquad
y\propto\omega^{-3N^2/(N^2-4)},\qquad
C/\lambda\propto\omega^{-1}.
\tag{7.5}
$$
第四模的选择不是为了改变这一指数，而是为了使用已经证明的 R72 $4\mathbb Z$ 全频非线性尾。

## 8. 开平盘、闭 $C^2$ 无穷小场与双 bump 的实际起点

R72 §9.2 给真实尾背景和高度扰动的全部物理二阶 jet 趋于平坦。将平背景延至轴上的圆盘，并把非零角模延为零，得到 $C^2$ 封口。也可使用 R187 已给出的固定开平领圈，其参考半径区间 $[.99,1.015)$ 在整个参数族中不变。

这里不要求退化的 Sturm 坐标一直正则到平盘：$W\to0$ 时 $h'=1/W$ 可以发散；封口的 $C^2$ 结论是在物理 $r$ 坐标里证明的。

整个向量场亦为 $C^2$。确实由 (1.8)
$$
U_r=WC_r,\qquad U_{rr}=W_rC_r+WC_{rr},
$$
而 (1.6) 给 $U\to0$；所以 $U,U_r,U_{rr}\to0$，$T=-U/4$ 也一样。$C$ 的二阶 jet 已由真实尾给出。这避免了无依据要求 $C_{rrr}$ 有界。

在负 $x$ 端镜像使用同一接线和尾。核心、两条单调帽端与两个平盘合成闭 $C^2$ 旋转嵌入。沿向外帽端有 $r$ 严格递减而 $z$ 严格递增；镜像端相反，故新部分不自交，亦不穿过未改核心。场 $Z$ 在两个开平盘上恒零，在腰圈的法向第四模不为零，故不是刚体速度场。

如需保持核心全部高频算术结构，可在上述接线**之前**的未改 Pöschl–Teller 远帽上放置 R9 第四模版的双 bump。其外端真实第四模线已经由本构造精确等于原 $y_4$ 的线，所以该版定理的“实际已匹配起点”在这里确实满足；外端衰减斜率是
$$
-\frac{y_4'(T)}{4y_4(T)}=\sqrt2\tanh T\in[1,3/2]
$$
（增大 $T$ 即可）。双 bump 两端的 $h,h',h''$ 保持，故本物理接线和实际尾不需随 bump 参数另改。

## 9. 曲率账及尚未完成的非线性接口

任一有限接线段的旋转主曲率满足准确界
$$
|k_\theta|=\frac{h}{\sqrt{1+h'^2}}\le\frac1\omega,
\qquad
|k_s|=\frac{|h''|h^2}{(1+h'^2)^{3/2}}
\le\frac{|q+1|}{\omega}.
\tag{9.1}
$$
全部过渡只有 $-8\le q\le2$，且末端 $\omega\asymp\Omega$；放大不强迫末端曲率增长。真尾的曲率还须按其实际缩放统一估计，本文不把局部曲率界自动写成全局 reach 下界。

本结果已经完成的是：

1. R72 真实无限尾的正确物理第四模目标，而非理想稳定行或非线性参考比值；
2. 与实际 n4 核心同时匹配的有限接线，包含全部短 $C^2$ 过渡；
3. 核心端与尾端的实际背景及无穷小场二阶 jet；
4. 双 bump 匹配曲线所需的真实起点，及准确的尾规范小输入界。

剩下的关键问题没有被 (7.4) 代付。R72 的低高度球给出一个**完整非线性**尾；它的全部高模两迹及 mean 是方程的输出。把线性 $Y_{\rm lin}$ 送进这个球，会产生非线性高模与斜率修正，不能把它们删去，再说核心已经匹配。

需要进一步构造同一个核心—接线—真尾算子的全频普通源右逆，处理每模真实两迹、mean 与临界第四模的可解条件；再支付非线性迭代、可见幅度及全局 reach。本稿不证明上述步骤，也不把它登记为课题主完成。

## 附录 A：真实接线起点上的第四模双 bump 定理

本附录给 R9 的第四模版本及全部更换常数，使上述真实接线与高频方向排除属于同一个背景。

取 $0<\ell\le1/16$，$L=3+2\ell$、$\gamma_0=\ell^2/512$。把 R9 的两个明确 bump 放在实际未改帽
$$
[T-L,T],\qquad
\operatorname{supp}\phi_1=[T-L,T-L+\ell],\quad
\operatorname{supp}\phi_2=[T-\ell,T].
\tag{A.1}
$$
增大 $T$ 后，该整个区间满足 $-3\le V_4\le-1$、$|h'/h|\le2$，而右端仍接本文 §§4–8 的真实 connector 和尾。置
$$
h_{s,u}=h\exp(s\phi_1+u\phi_2),\qquad
|s|\le\gamma_0,\quad0\le u\le\gamma_0.
\tag{A.2}
$$
两端背景二阶 jet 恒定；整个矩形有 $-4<V_{s,u}\le-3/4$、$|w_{s,u}|<3$。

对每个 $n\in4\mathbb N$，使用 R72 **未冻结的完整内部标签空间**：令本模标签为 1、其余为零，在零参数处取得真实齐次线性尾，再通过固定 connector 向左传播；负频率由实共轭取得。其切口向量不为零：若在任一有限切口为零，则真实二阶方程唯一性使整个本模为零，与其内部标签为 1 矛盾。由此得到与 $(s,u)$ 无关的右端实输入线 $\Lambda_n$。这里没有把“冻结所有高标签为零”的有限低高度子族当作高模 Robin 线。

第四模的这条线由本文的实际匹配恰为原 $y_4$ 的线，归一化可写
$$
y_4(T)=1,\qquad
-\frac{y_4'(T)}{4}=\zeta_4=\sqrt2\tanh T\in[1,3/2].
\tag{A.3}
$$
因而 R9 中“起点已匹配核心”的输入在此已被证明。取任意固定的增长目标
$G_n=\operatorname{span}(1,b_n)$、$b_n\in[4/3,3/2]$。

**结论。** 存在唯一 $C^1$ 匹配曲线
$$
s(0)=0,\qquad -\gamma_0/64<s(u)\le0,\qquad0\le u\le\gamma_0,
\tag{A.4}
$$
使第四模在左端 $T-L$ 的方向始终精确等于原 Pöschl–Teller 第四模方向。沿这条曲线，存在测度至少 $1-83/16384$ 的 $t=u/\gamma_0\in[0,1]$，同时满足全部 $n\in4\mathbb N$ 及其共轭负频率的
$$
|\sin\angle(L_n(t),G_n)|\ge
\frac{\ell^3}{2^{27}}.
\tag{A.5}
$$
取 $\ell=1/16$ 得统一下界 $2^{-39}$。两帽可用同一个 $t$，其共同好集测度至少 $1-83/8192>0$。

**证明。** 以左端状态 $(y,y'/n)$ 长度为 1 归一化，沿用 R9 的准确变分式
$$
D_n=(y_n'-w_{s,u}y_n)^2+(n^2-1)(-V_{s,u})y_n^2,\qquad
K_{n,i}=2n\int\phi_iD_n,\qquad
\partial_i\theta_n=-K_{n,i}.
\tag{A.6}
$$
反向 Riccati 不变区间给整个参数矩形的
$$
y_4>0,\qquad
\sqrt3/2\le-\frac{y_4'}{4y_4}\le2.
$$
于是所有需要替换的第四模常数为
$$
\frac{45}{4}y_4^2\le D_4\le181y_4^2,
\tag{A.7}
$$
其中上界为 $(8+3)^2+15\cdot4=181$。两支持相距 3，故
$$
\frac{K_{4,2}}{K_{4,1}}
\le\frac{1448}{45}e^{-12\sqrt3}<\frac1{64}.
\tag{A.8}
$$
最后严格界可用 $\sqrt3>5/3$、$e>2$：指数分母大于 $2^{20}$，而 $64\cdot1448/45<2^{12}$。
归一化时 $y_4(0)>1/3$；内支持上
$y_4\ge e^{-8\ell}/3>1/6$，因此
$$
K_{4,1}\ge
8\cdot\frac{45}{4}\cdot\frac{\ell}{2}\cdot\frac1{36}
=\frac54\ell>\frac12\ell.
\tag{A.9}
$$
解真实参数 ODE $s'(u)=-K_{4,2}/K_{4,1}$、$s(0)=0$，(A.8)–(A.9) 使其在整个参数区间延拓并留在 (A.4)；(A.6) 使第四模角严格恒定。

全部其它模式的坏方向估计完全不依赖被固定的是第三还是第四模。为明确给出联立账，在
$|\sin\angle(L_n,G_n)|<\varepsilon\le1/20$ 时，正向 Riccati 比较给
$y_n>0$、$\sqrt3/2\le y_n'/(ny_n)\le2$，从而
$$
\frac9{16}n^2y_n^2\le D_n<17n^2y_n^2,\qquad
\frac{K_{n,1}}{K_{n,2}}\le\frac{544}{9}e^{-3n\sqrt3}<\frac1{256}.
$$
结合 (A.8)，在同一匹配曲线上有
$$
\frac{d\theta_n}{dt}
=-\gamma_0K_{n,2}
+\gamma_0K_{n,1}\frac{K_{4,2}}{K_{4,1}}
\le-\frac{\gamma_0n^3\ell}{32}.
\tag{A.10}
$$
径向角速度至多 $4n$，故参数角值域长至多 $8nL$，只遇到至多 $3nL+2$ 个模 $\pi$ 的坏角区间；每个坏区间因 (A.10) 只能向下穿越一次。逐个换元并对 $n\ge2$ 的更大频率集求和，R9 §6 的准确总账仍是
$1328\varepsilon/(\gamma_0\ell)$。代入
$\varepsilon=\gamma_0\ell/2^{18}$ 得坏集测度至多 $83/16384$。只保留 $4\mathbb Z$ 不增加它；两端再用并集界即得结论。证毕。

最后，若把增长目标选成未改长帽 $[2,T-L]$ 的实际正增长方向，R7 的衰减/增长配对给本背景的反射估计
$$
\left|\frac{d_n}{c_n}\right|
\le2^{40}e^{-(8/3)n(T-L-2)}
\qquad(n\in4\mathbb N).
\tag{A.11}
$$
这里屏障长度必须是 **$T-L-2$**：双 bump 占用的长度不能再计入未改屏障。第四模自身的反射恰为零，因为其方向已精确保持。尾部内部标签的统一逆向权及普通源估计仍应另付；(A.5) 单独不把该权消掉。
