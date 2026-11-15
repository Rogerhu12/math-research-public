# R325：朝内弱核圆准确支付旧一层兼容式与三条完整 directed 门

日期：2026-11-15。**真实有限 profile 构造与纸面原式证明。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R320](R320-complete-reflected-area-payment-and-outward-one-history-obstruction.md) 已经支付一个真正弱 hook 圆的完整三矩面积，却证明其朝外排列仍有严格第四障碍。本稿改变曲段朝向与反射半侧的关系。先构造一个朝内反射圆，使同一个准确一层兼容量为负；再用真实强 hook 完整块的正值清掉它。最后只在强块内使用同一个低阶观察纤维上的有限频率扰动，准确支付三条完整 directed 行。

最终这些等式对全部相位成立，所用 profiles 仍有真实导数 rank-two 区域，完整三阶保持。它们共同使 R304、R306、R317、R320 使用的那条完整一层系数准确为零。本稿没有宣布完整第四 ruling、其他 Gaussian 面积与乘积、全 period 或平台方程已解。

主要来源：[R308 的弱核完整三阶](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R317 的一般 mixed 四行](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)、[R319 的朝向面积](R319-one-sided-weak-hook-area-obstruction-and-reflected-block-cancellation.md)、R320、[R259 的真实 cubic 变分](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R280 的实际强块布局](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R289 的实际交替包正锥](R289-universal-even-principal-space-and-positive-real-packet-cones.md)及 [R293 的初选有限观察纤维与有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 真实几何、目标与所付门

先固定已经安装的真实闭 hook 几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
以及同一个小共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
\tag{1}
$$
如使用此前已经安装的 universal whole-pure 零，这个身份也保持：本稿不再改变几何，且该已证明身份作用于最终重新选择的 profiles。这里不由 pure 零删任何局部或 ordered 尾。

本稿是一个新圆、新 seed 的构造。所有有限模板、幅度范围与最终位置先选定，再固定共同合法正区间 $I$、右锚和最终目标
$$
(X+\epsilon Y_f)^*\mathrm e.
$$
目标随实际选出的 $f$ 固定，不随圆参数 $\theta$ 改变。没有承诺在一个此前已经冻结且过窄的 $I$ 内装下任意大间距。

设
$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u.
$$
最终保持
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,\qquad
\mathfrak H(g;f,f)=0.
\tag{2}
$$
共同归一化后可令 $I_0(f,f)=I_0(g,g)=1$。弱条件给
$$
\mathfrak H(u;D)=\sin\theta\,\mathfrak H(g;f,f)=0;
$$
不增加第二个 hook。

沿 R317，记
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},
$$
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,
$$
$$
\begin{aligned}
a&=-\frac{51t^2+2t+8}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d_*&=\frac{6\kappa^3}{h_e},&
e_*&=-\frac{\kappa(15t+1)}{4h_e},&
c_P&=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\end{aligned}
\tag{3}
$$
完整 directed 行定义为
$$
H_j^X=-I_j(XD,PD)+2I_j\{u,X(u,PD)\}.
\tag{4}
$$
本稿支付
$$
\boxed{
I_j\{u,[W_*,P](u;D)\}=0\quad(j=0,1,2),
}
\tag{5}
$$
以及
$$
\boxed{
F_0:=H_2^P=0,\quad
F_1:=aH_1^R+bH_1^S=0,\quad
F_2:=d_*H_0^L+e_*H_0^U=0
}
\tag{6}
$$
对全部 $\theta$ 同时成立，并支付下文的完整一层系数。式(4)始终是原整个函数配对；没有只控制 principal。

## 2. 未将三行置零以前的准确一层身份

写
$$
p=f',\quad q=f'',\quad v=u',\quad r=u'',\quad
d_0=q^2-r^2,\quad A=Jd_0=PD,
$$
$$
C_\theta=\int r^2d_0,\qquad
D_\theta^{(4)}=\int d_0^2,\qquad
\mathcal J_\theta=\int(vq-pr)\,r q'.
\tag{7}
$$
这些均是完整 profiles 上的真实积分。

弱 hook 的原通量及 R317 给
$$
Y:=\int vr\,d_0'=-\frac23C_\theta-2\mathcal J_\theta,
$$
$$
B:=\int pq\,d_0'
=-\frac23(D_\theta^{(4)}+C_\theta)-2\mathcal J_\theta.
\tag{8}
$$
式(5)的第1矩给
$$
Z:=\int xr^2d_0'=C_\theta.
\tag{9}
$$
令 $X_2=\int x^2(q^2)'d_0'$、$T_1=\int xpq'd_0'$。原四行是
$$
\begin{aligned}
H_2^P&=-X_2-4Z+4Y-2D_\theta^{(4)},\\
H_1^R&=-X_2+2T_1-Z+2Y+C_\theta,\\
H_1^S&=-X_2-2Z+\tfrac12D_\theta^{(4)},\\
H_0^U&=-\tfrac32X_2+2T_1-2Y+Z+2B+
D_\theta^{(4)}-C_\theta.
\end{aligned}
\tag{10}
$$
没有在本节假定 $F_0,F_1,F_2$ 为零。

设
$$
\ell_0=-\kappa/2-6\kappa^3,\quad
m_0=\kappa(15t+1)/4,\quad p_0=41\kappa^5/216,
$$
$$
K_\kappa=\tfrac12(m_0-\ell_0e_*/d_*)
=-\frac{1+15t}{96\kappa}.
$$
原 local 项准确为
$$
-\frac{\kappa^3}{8}X_2+
\frac{\kappa^3}{16}D_\theta^{(4)}
-\frac{\kappa^3}{4}Z.
\tag{11}
$$
从(10)解 $X_2,T_1$，保留 $F_0,F_1$，得到
$$
\begin{aligned}
H_0^U={}&
\left(\frac23-\frac{5b}{2a}\right)D_\theta^{(4)}
+\frac{14}{3}\left(1-\frac ba\right)C_\theta
+8\left(1-\frac ba\right)\mathcal J_\theta\\
&+\left(\frac12-\frac ba\right)F_0+\frac{F_1}{a}.
\end{aligned}
\tag{12}
$$
式(11)相应为
$$
\kappa^3\left(\frac{5D_\theta^{(4)}}{16}
+\frac{7C_\theta}{12}+\mathcal J_\theta\right)
+\frac{\kappa^3}{8}F_0.
$$

令
$$
\begin{aligned}
N(t)&=16+184t-1713t^2-2475t^3-4590t^4,\\
P(t)&=8+114t-169t^2+231t^3-612t^4,\\
\Psi_\theta&=\frac{N(t)}{24P(t)}D_\theta^{(4)}
+\mathcal J_\theta+\frac7{12}C_\theta.
\end{aligned}
\tag{13}
$$
乘回原 $c_P$ 后，完整一层为
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}
=c_P(A_0F_0+A_1F_1+A_2F_2)+B_\kappa\Psi_\theta,
}
\tag{14}
$$
其中
$$
A_0=K_\kappa(1/2-b/a)+p_0/2+\kappa^3/8,\quad
A_1=K_\kappa/a,\quad A_2=\ell_0/(2d_*),
$$
$$
B_\kappa=
\frac{(41t^2+27)P(t)}
{2592h_e^3(51t^2+2t+8)}>0.
\tag{15}
$$
这保留原 local、chain、elementary history 与全部低阶项。$\Psi_\theta$ 只是一个准确兼容组合；只有另外三行确实为零以后，才可把它直接当作整个指定一层的值。

## 3. 三条 directed 行的完整相位次数

补出 R317 未单列的一行。R259 原 cubic 密度是
$$
F_{L,0}(u)=I_0(u,L(u,u))
=-\frac12\int u'(u'')^2.
$$
因 $A=PD$ 真紧，完整变分而非 diagonal 简化给
$$
H_0^L=DF_{L,0}(u)[A]-I_0(A,L(f,f)).
$$
原二导为
$$
(L(f,f))''=(f-xp)q'-\frac{xq^2+P(f,f)}2.
$$
保留可能非紧的 $P(f,f)$，使用
$$
\int d_0'P(f,f)=\int d_0q^2
=D_\theta^{(4)}+C_\theta,
$$
准确得到
$$
\boxed{
H_0^L=Y-\frac12D_\theta^{(4)}
+\int d_0'(f-xp)q'
-\frac12\int xq^2d_0'.
}
\tag{16}
$$
没有要求单包或 $P(f,f)$ 紧。边项消失用的是完整 $d_0$ 的紧支撑。

置
$$
\mathcal Q_4=\int(f''+ig'')^4 .
$$
若 $\mathcal Q_4=0$，记
$$
C_{22}=\int(f'')^2(g'')^2,\quad
E_4=\int(g'')^4,\quad B_4=\int(f'')^3g'',
$$
则逐项展开给
$$
D_\theta^{(4)}=4C_{22}\sin^2\theta,
$$
$$
C_\theta=(C_{22}-E_4)\sin^2\theta
-2B_4\cos\theta\sin\theta.
\tag{17}
$$
而 $vq-pr=\sin\theta\,(g'f''-f'g'')$，所以
$\mathcal J_\theta$ 也仅为 $\sin^2\theta$ 与
$\cos\theta\sin\theta$ 的组合。

式(8)–(10)、(16)表明：在弱 hook、(5)及 $\mathcal Q_4=0$ 下，三个 $F_i$ 和 $\Psi_\theta$ 全部只有这两个相位系数。尤其 $F_2$ 的该结论使用了真正的(16)，并非从 $\theta=\pi/2$ 的表格猜出。

对共同平移 $x\mapsto x-d$，$F_i$ 这些系数是 $d$ 的至多二次多项式；(10)、(16)逐项即给此界。$\Psi$ 的系数平移不变。后面会使用原十二个完整副本
$$
(f_j,g_j)=\gamma_j\,T_{d_j}(f,(-1)^jg),\qquad
\gamma_j^4=\binom{11}{j},
\tag{18}
$$
其中 $d_j$ 为等差的、使完整包络不交的真实位移。十一阶差分准确清所有 $\cos\theta\sin\theta$ 系数。这里每个副本已先有八副本的完整第三结构；额外平移不破其七次差分身份。最后只需在 $\pi/2$ 支付(6)与(13)，就支付它们的整个相位函数。

## 4. 朝内完整弱块及其严格正第零面积系数

先在一个固定有界局部包络内取 R308 型弱核基本圆，但把活动幂段改为左向
$$
f_0(x)=A_\nu(b_\nu-x)^{5/2}
$$
在 $g_0$ 的严格内部支撑邻域成立。$g_0$ 在外 cutoff 区为零。原三个复矩由另外三个实 rank-one 补包准确支付；补包和 cutoff 上 $W=0$。不增加第二 hook。

可以从最初令
$$
\int(f_0'')^2g_0''f_0'''=0.
\tag{19}
$$
这是对曲段上 $g_0$ 的一个真实线性条件。取两个不交、非零的小紧 bump，其二维实 span 必含一个非零核向量；若该泛函在其中已零，直接取任意非零向量。非零紧 $g_0$ 不会使 $g_0'f_0''-f_0'g_0''$ 恒零：否则在 $f_0'\ne0$ 的整个曲段内有 $g_0'=c f_0'$，与内部紧支撑矛盾。

rank-one 补包对(19)的积分是常数乘
$\int\eta''{}^3\eta'''=0$，所以原三矩回补不破坏(19)。再作 R308 的八个完整副本。每个真实四次权为正，故最终固定完整块仍满足(19)和
$$
m_0(\theta):=
I_0\!\left(u,J\{u''((f'')^2-(u'')^2)\}\right)
=M\sin^2\theta,\qquad M>0.
\tag{20}
$$
事实上
$$
m_0=-\int(u'')^2f''f''',
$$
而左向幂段有
$$
f''f'''=-225A_\nu^2/32<0.
$$
式(19)消去交叉相位项；rank-one 补包对此整个 $m_0$ 无贡献。全部真实曲段、补包、八副本均在这个固定完整块内，此后只移动其包络。

把它放在反射中心 $C_0$ 的右侧，局部坐标原点位于 $C_0+L$，并在左侧放完整镜像。这是朝内排列：右侧幂段向左，左侧向右。原真实反射律给
$$
m_0=0,\qquad m_2=2C_0m_1.
\tag{21}
$$
保留右原函数的实际常尾后，右块的平移及镜像使
$$
m_1(\theta)=2LM\sin^2\theta+\text{一个与 }L\text{ 无关的角函数}.
\tag{22}
$$
式(22)的 $L$ 系数是原带 $x$ 的积分，不是几何输入 phase 或成本的变换。

## 5. 面积全付，同时让准确兼容量严格为负

所有以下强模块都取 R320 的真实三矩 rank-one profiles，先放到最终不交包络并完成八副本与镜像；允许的 phase 只作用于这些整个平面对 hook 不可见的实际实 pair。它改变新 seed，不是对旧几何成本施加未证相位。

先用 R320 的一个实际强原型，乘一个固定复四次根，通过真实幅度和实正交变换使总 $\mathcal Q_4=0$。其所需四次权不依赖 $L$，因为 $\mathcal Q_4$ 平移不变。随后(22)准确成为
$$
m_1=(2LM+v_1)\sin^2\theta+
v_2\cos\theta\sin\theta.
$$
使用 R320 那四个 $\mathcal Q_4=0$、正锥为 $\mathbb R^2$ 的完整强模块，以一个固定的非负四次组合支付向量 $(0,-v_2)$。可以加固定严格正 balance，使所用幅度全正。其权也不依赖 $L$。重新记常数后，当前残余为
$$
m_1=(2LM+v_*)\sin^2\theta.
\tag{23}
$$

另取一个真实强 isotropic 模块：把 R320 的 $\mathcal Q_4=0$ 模块按四个相位 $0,\pi/4,\pi/2,3\pi/4$ 等幅组合。于是
$$
\mathcal Q_4=0,\qquad \mathcal Z_2=0,\qquad
S_*:=\int(F^2+G^2)^2>0.
$$
它的实际值为
$$
m_1=-3S_*\sin^2\theta/16,\quad
C_{\pi/2}=-S_*/4,\quad
D_{\pi/2}^{(4)}=S_*/2,\quad \mathcal J_{\pi/2}=0.
\tag{24}
$$
取足够大但有限的 $L$，使 $2LM+v_*>0$，再给该模块四次权
$$
w(L)=\frac{16(2LM+v_*)}{3S_*}>0.
\tag{25}
$$
真实 profile 幅度为 $w(L)^{1/4}$。式(21)、(23)–(25)准确支付全部三条面积、全部相位。

原弱曲段的 $\mathcal J$ 平移不变，所有强模块上 $\mathcal J=0$；除了(25)，此前所有四次数据与 $L$ 无关。因此同一个真实完整圆满足
$$
\Psi_{\pi/2}(L)
=C_*+\frac{2LM}{9}\left(\frac{N(t)}{P(t)}-7\right),
\tag{26}
$$
这里 $C_*$ 是一个固定有限常数，没有隐藏的随 $L$ 增长误差。其完整系数来自(24)，不是只算一个候选 local 项。

准确多项式恒等为
$$
7P(t)-N(t)
=40+614t+530t^2+4092t^3+306t^4>0.
\tag{27}
$$
故可选一个实际有限 $L$ 使
$$
\Psi_{\pi/2}(L)<0.
\tag{28}
$$
所有 profiles、三矩补包及真实幅度都在这一有限 $L$ 上固定。

对这个完整圆再作(18)。全部面积保持；其已付第三 ruling 在额外平移后仍零。$\Psi$ 的交叉相位被清，而 $\pi/2$ 值乘同一正数。因此得到真正导数 rank-two 的固定完整弱圆 $\mathcal B_-$：
$$
\Psi_\theta(\mathcal B_-)=\psi_-\sin^2\theta,
\qquad \psi_-<0.
\tag{29}
$$
它的 $F_i$ 也均为 $\sin^2\theta$ 乘实际 $\pi/2$ 值，但还没有被置零。

## 6. 真实强块提供正值，不借 signed 成本空间

从起点选 R280/R293 的一个真实强宏块 $\mathcal B_+$：保留其五个最终完整 block、两种实际编码、全部正四次权和八／十二副本。其原三矩、完整第三及全部72面积已由真实构造支付；每个微包上 $(f,g)$ 为同一实紧母包的两个实倍数，所以 $W=0$。

对它，由面积和 R306 有 $C_\theta=0$、$\mathcal J_\theta=0$，且
$$
D_\theta^{(4)}=4C_{22}\sin^2\theta,\qquad C_{22}>0.
$$
故
$$
\Psi_\theta(\mathcal B_+)=\psi_+\sin^2\theta,
\qquad
\psi_+=\frac{N(t)}{6P(t)}C_{22}>0.
\tag{30}
$$
把 $\mathcal B_-$ 与 $\mathcal B_+$ 放在两个不交的完整包络中，给后者真实四次权
$$
\rho^4=-\psi_-/\psi_+>0.
\tag{31}
$$
下一节将从原尾证明所需加法。因此该组合准确有
$$
\Psi_\theta=0
\quad\text{对全部 }\theta.
\tag{32}
$$

这里是两组实际实 profiles 的正幅组合。没有以响应 span 的负元代替真实路径，也没有声称强块自己的完整第四可行。所有弱曲段保持固定，故最终仍 $W\not\equiv0$。

## 7. 跨完整块的真实二次尾与三行加法

不能把旧 rank-one 逐微包局部化直接套到新的 rank-two 核心。本节只证明本稿确实需要的完整块加法。

对任一满足三矩圆的完整块 $i$，记
$$
D_i=f_i\odot f_i-u_i\odot u_i.
$$
原 E8 左尾表及三矩零给
$$
PD_i,\quad XD_i\quad (X\in E8)
$$
在该完整包络内真紧。没有要求其内部的各个微包独立三矩合法。

不同完整块的这些紧函数支撑不交。因此 $X(u_i,PD_j)=0$（$i\ne j$）：每个 local 乘积和每个同点 Volterra integrand 都为零。对相同块的 $X(u_i,PD_i)$，仍保留其可能的真实二次左尾
$$
p_2(x)=Ax^2+Bx+C.
$$
它与另一个紧外槽 $v$ 的全部原外矩准确正交：
$$
I_0(v,p_2)=I_1(v,p_2)=I_2(v,p_2)=0.
\tag{33}
$$
其中
$$
I_2(v,p_2)=\int\{2Ax^2v''+2v'(2Ax+B)\}=0;
$$
不能只删其中一个项。

由(33)，(4)的所有选中 $H_j^X$ 在不同完整三矩块之间准确相加。同理，当前面积 cubic $J(u''d_0)$ 的跨块尾只是常数，其外三矩无跨块贡献。(7)、(13)都是 local 完整密度，显然相加；(14)所含 local／history 总式因此也准确相加。

该证明同时处理弱核心与强控制宏块。其全部相关跨块坐标在初选观察映射中是恒零分量，不是未经证明的“固定尾不会变化”。强宏块内部原有的微包 ordered 项仍由原 $\mathcal F$ 与真实有限频率全式保留。

## 8. 从起点选择同一个母包与观察纤维

第5节的负值构造只需要一个实际非零偶母包，并未规定它的任何额外积分值。故在开始选择所有强模块以前，先按 R293 第6节选
$$
\mathcal F_\star=(\mathcal F,\ C),\qquad
C(u)=\int(u'')^4,
\tag{34}
$$
其中 $\mathcal F$ 是原全部真实三矩、self 平移系数与 ordered 接口；若 $C$ 已由旧分量决定，重复加入不改变构造。第7节的跨完整块项是已证明的零坐标。所有分量是实际连续的 $C^2$ 多项式泛函。

在同一个偶母包 Banach 域取 $\mathcal F_\star$ 的最大微分秩。选真非零 minor及固定纠正方向；在该点附近，最大秩性保证只纠正这些独立坐标就保持整个 $\mathcal F_\star$。不把任意给定母包当作 regular。

可如 R281/R293 选择
$$
u_0=\psi P_0,\qquad e_\ell=\psi P_\ell,
$$
各 $P_\ell$ 为有限偶多项式，$P_0$ 全区严格正，并同时令 $u_0''(0)\ne0$。最大 minor 与下面所需严格主秩条件都可在同一母包保持：沿正解析见证到最大秩见证的多项式直线，在任意小正参数避开有限个 minor 零点。

固定这个母包以后，才完成第4—6节的所有真实补偿、幅度、最终位置和(31)。高频阶段不会再改变(31)的幅度。每一个微包都保持其原 $\mathcal F_\star$ 值，特别 $C(u)=C(u_0)$。

强宏块上始终 $W=0$，原面积数据及 $\mathcal Q_4$ 也准确保持。因此其整个 $D_\theta^{(4)}$ 和 $\Psi_\theta$ 不变。弱核心完全不动，故(32)在所有允许高频幅度上都准确成立。

## 9. 三条所需 principal 的实际正锥

只在强宏块内选实际 rank-one 微包作扰动，写 $f_i=a_i u_i$、$g_i=b_i u_i$，
$$
R_i=a_i^2-b_i^2,\qquad \lambda_i=-a_i^2R_i.
$$
原表给三个完整行的最高三导部分。以
$$
H_a=\int x^2r^2(u''')^2,\quad
H_b=\int xv r(u''')^2,\quad
H_d=\int u r(u''')^2
$$
为列，矩阵为
$$
\boxed{
\begin{pmatrix}
4&0&0\\
4(a+b)&-4a&0\\
6e_*&2d_*-4e_*&-2d_*
\end{pmatrix},
\qquad \det=32ad_*\ne0.
}
\tag{35}
$$
每个微包另乘其真实 $\lambda_i$；完整低阶基线未被删除。强宏块原全部面积为零，所以其 directed 与相应对称观测的差准确为零，R293 的原恢复及 $C^1$ 估计可以使用。

还须证明同一个真实母包提供所需三维列，而不是只看(35)。取两个偶振荡形状 $\chi_\alpha=\psi Q_\alpha$。对局部坐标 $y$，其未乘(35)的列为正倍数的
$$
\begin{pmatrix}
\displaystyle\sum_\nu\omega_\nu\int(X+d_\nu+y)^2r_0^2\chi_\alpha^2\\[2mm]
\displaystyle W_c\int yv_0r_0\chi_\alpha^2\\[2mm]
\displaystyle W_c\int u_0r_0\chi_\alpha^2
\end{pmatrix},
\qquad W_c=\sum_\nu\omega_\nu>0.
\tag{36}
$$
这里 $\omega_\nu>0,d_\nu$ 保留该微包全部实际完整 copy 的四次权和位置；五个最后 block 的正权也包含其中。偶性使 $\int v_0r_0\chi_\alpha^2=0$，所以第二行没有被遗漏的 $X$ 或 copy 平移项。

第一行是 $X$ 的真二次多项式，最高系数为正。另两行可取不共线。事实上在中心附近
$$
\frac{yv_0}{u_0}
=\frac{u_0''(0)}{u_0(0)}y^2+O(y^4),
$$
且 $u_0r_0$ 不变号。取一个靠近零的偶局域形状、一个靠近充分小非零 $\pm y_1$ 的偶局域形状，其上述两积分之比严格不同；再用 $\psi$ 乘偶多项式的 $C^2$ 稠密逼近，严格差仍保持。由此两组(36)的实际 span为 $\mathbb R^3$。

每组使用 R289/R293 已存在的十二个实际交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
两个形状占用不同的原编码层；所有同名完整副本共享同一形状与参数。实际递增位置 $X_i$ 满足
$$
\beta_i=\frac1{\prod_{j\ne i}(X_i-X_j)},\qquad
\beta_i/\lambda_i>0.
$$
(36)的次数不超过二，故
$$
\sum_i\beta_i P_\alpha(X_i)=0.
\tag{37}
$$
这给每一组真实列的严格正核。每组非负锥等于其线性 span，两组合起来为 $\mathbb R^3$。不是把 signed principal span 当成实际控制。

## 10. 完整有限频率根；弱核心始终不动

对每个选中微包使用
$$
u_{N,z}=u_0+N^{-3}z\chi_\alpha\cos(Ny)
+\sum_\ell a_\ell(N,z)e_\ell
$$
并解原有限维隐函数方程，使
$$
\mathcal F_\star(u_{N,z})=\mathcal F_\star(u_0)
\tag{38}
$$
准确成立。同一个微包的全部八／十二副本与镜像共享同一解。纠正系数及其关于固定有限幅盒的一阶导数为 $O(N^{-1})$；固定光滑纠正方向的三导也趋零。

记最终整个弱强组合的三行向量为
$$
\mathbf F_N(\mathbf z)=(F_0,F_1,F_2)(\pi/2).
$$
第7节保留并准确消去了跨完整块项。强块的原最高平方与完整 $C^2$ 余项给
$$
\mathbf F_N(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{39}
$$
在一次固定的有限正幅盒上一致成立。$\mathbf F_{\rm base}$ 包含弱核心、所有强补偿、真实初始 tails 与各 copy 的原值；不要求它满足旧32维主空间的两条关系。本稿的目标空间就是 $\mathbb R^3$，第9节已付它的完整正锥。

由(37)可把 $-\mathbf F_{\rm base}$ 写成全部选中列的严格正组合。令其系数为 $(z_i^*)^2>0$，再选三个独立列，固定其余幅度。极限映射在 $\mathbf z^*$ 为零，三列 Jacobian为 $2z_i^*v_i$，可逆。

由一致 $C^1$ 收敛，足够大的一个实际有限整数 $N$ 给附近的正幅精确根
$$
\boxed{\mathbf F_N(\mathbf z_N)=0.}
\tag{40}
$$
没有把离散 $1/N$ 当作光滑参数；只使用非退化零在小 $C^1$ 扰动下稳定。也没有把主项零当作完整函数零。

原 $\mathcal F_\star$ 保持强宏块的全部面积与 quartic 值；弱块不动。故(5)、(32)对这一个有限 $N$ 仍准确成立。第3节的十二副本保相位交叉系数为零，因此(40)给(6)的全部相位零。最后将(6)、(32)代入完整(14)，得到
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0
\quad\text{对全部 }\theta .
}
\tag{41}
$$

## 11. 选择顺序、合法区间与第三恢复

完整顺序为：

1. 固定真实有限几何、(1)、canonical 右锚约定，及从起点的 $\mathcal F_\star$。
2. 选择一个实际最大秩正解析母包、纠正方向与两个有严格比值差的偶形状。它们用于全部后续强模块。
3. 固定左向弱曲段和线性条件(19)，完成真实三矩回补及八副本；再用固定强模块完成第5节。选一个有限大 $L$，不是无限远极限。
4. 固定所有完整包络、十二副本、R280 强宏块的五个最终位置与全部正权。可把全部有限集合放到足够大的正物理区域，使几何的 $x+\omega(s)$ 有统一正间隙，再固定一个包含它们且两端留空 collar 的共同 $I$。R105第4节要求的先有限几何、后共同物理区间，在这里被明确遵守。
5. 在这些最终位置确定(31)及完整三行基线。然后固定有限正幅盒，最后才选足够大的有限 $N$ 和精确根。此后不平移、不重锚，也不改变任何 copy 权。
6. 最后共同正实归一化 $I_0(f,f)=1$。所有零式四次齐次，第三零式三次齐次，原三矩同为二次，因此已付内容保持。新目标 metric 此时一次固定。

对几何有限路径及其已固定小参数包络，$h>0$、$\omega$ 有界，所以确可选择上述共同正区间；不是仅用 universal 延拓在移动极点上假作物理恢复。

高频仅改变强 rank-one 微包内部，同一个微包上的 $f,g$ 仍严格比例，所以 $W=0$。原弱曲段上 $A_fW=0$，其它区域仍 $W=0$；完整右锚给原弱 hook。原三矩纤维与编码保持每个完整块的二阶场局部化。第三 forcing 跨这些完整块真零；各块原八副本对完整相位 range 的七次差分仍逐参数成立。因此整圆的第三 period、ruling、两 collar、真实初值及 $\theta=0,\pi$ 种子全保持。

这不要求四个形式 cubic 槽分别有零 period；使用的是 R308 已付的完整相位恢复。新增强块的独立相位也只作用于其已证整个 hook 平面零的真实 pair。

## 12. 新结论的准确范围

本稿第一次在当前小共振 Gaussian 芽上给出一个真正弱单 hook、导数 rank-two 的实圆，同时准确通过：

- 完整三阶与原三矩圆；
- $A_{-2,-3}$ 面积的三个外矩、全部相位；
- 原三条 directed 门(6)、全部相位；
- 由完整 local／chain／history 合成的指定一层(41)、全部相位。

它不只把旧正余量改成负号，而是以同一实际 profiles 和一个有限频率精确根，把这组已知必要门全部清零。R320 的朝外否定仍成立；这里改变的是曲段朝向相对于反射侧的真实安排。

全局其他 Gaussian 面积与对称乘积未由本稿支付。强控制宏块自己的旧72面积虽保持，不能据此冒充新的弱强组合也满足全部72。其余零／一层函数、其他局部端口、canonical 平台与通量、第四 period、同一二阶 gauge 的 joint range 也仍需后继逐项处理。

所有高阶 Taylor 及有限参数准确等距、闭面嵌入、reach 与宏观握持等主问题要求，均没有从这组第四必要门的有限支付中推出。
