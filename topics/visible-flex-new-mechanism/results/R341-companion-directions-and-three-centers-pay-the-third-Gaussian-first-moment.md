# R341：真实伴随方向与三中心矩支付第三 Gaussian 面积的完整第一外矩

日期：2026-11-15。**完整有限纸面构造。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R339](R339-opposite-sign-weak-blocks-pay-the-third-Gaussian-zero-moment.md) 已用真正异号的弱块支付第三面积 $A_{-1,-2}$ 的第零外矩，同时保留两个完整面积、$\Psi$、三条 directed 行及指定完整一层。本稿增加同一第三面积的**全部相位第一外矩**。

支付分成两个真实方向。普通与包内伴随两种强块给第一外矩两个 even 系数之差的正、负值；其完整伸缩权为 $-5$，而 $\Psi$ 权为 $-7$，所以可以用正幅、有限伸缩以任意小的正 $\Psi$ 成本支付该差。剩下的共同 $\sin^2\theta$ 系数则由两个相同负 $C$ 弱块和一个正 $C$ 弱块的真实第二中心矩支付；同一个构造准确保持第一中心矩，故不会重新打开 R339 的第零外矩。

全部普通尾、伴随内部 primitive、十二复制的真实中心方差及最终正位置均保留。最后同纤维有限频率根仍只在强控制器内进行，整个弱部分固定。本文没有支付第三面积的第2外矩，也没有把控制器自身的72面积零扩成整个圆的72面积零。

主要来源：[R267 原 self 与真实母包形状](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R262 完整有序有限和](R262-ordered-primitive-obstruction-for-the-multiwidth-energy-branch.md)、[R265 真伴随构造](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md)、[R275 原第一外矩及 Green 尾](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R334 完整第2矩与伸缩](R334-positive-dilations-pay-the-full-second-Gaussian-area-with-the-old-layer.md)、[R337 原平移及第三面积第零矩](R337-true-translation-excludes-the-same-sign-reflected-weak-block-architecture.md)、R339，以及 [R293 有限观察上的真实有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 同一几何、原规范与新增目标

固定 R339 的同一真实有限几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
及其共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad 0<t:=\kappa^2<1/100.
$$
沿用
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},
$$
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d_*=\frac{6\kappa t}{h_e},\quad
e_*=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
本稿的 $U$ 始终是 $\Phi_{s_1}$；R275 原文称其为 $T$。

令
$$
u=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u,
$$
并记
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\quad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_j=I_j\{u,[Z_*,W_*](u;D)\},\quad
\mathcal R_j=I_j\{u,[R,S](u;D)\}.
\tag{2}
$$
其中
$$
I_0(u,w)=\int u''w'',\quad I_1(u,w)=\int xu''w'',\quad
I_2(u,w)=\int(x^2u''w''+2u'w').
$$
所有原积分使用同一右锚和实际零 collar。

本稿要在同一个最终圆上准确得到
$$
\boxed{
\mathcal M_j=\mathcal A_j=0\quad(j=0,1,2),\qquad
\mathcal B_0=\mathcal B_1=0,\qquad
\Psi=F_0=F_1=F_2=0
}
\tag{3}
$$
对全部 $\theta$ 成立。$\Psi,F_i$ 使用 R325/R334/R339 的完整原式，包括真实基线与原尾。

## 2. 第一外矩的真实平移公式

R337 原算子平移为
$$
P^{(s)}=P,\quad R^{(s)}=R+sP,\quad S^{(s)}=S+sP,
$$
$$
Z_*^{(s)}=Z_*+sV_*+\frac{3e_*s^2}{2}P,\qquad
W_*^{(s)}=W_*+s(a+b)P,
$$
$$
V_*=(e_*-d_*/2)R+(2e_*+d_*/2)S.
$$
定义
$$
\chi_\kappa=(e_*-d_*/2)b-(2e_*+d_*/2)a
=\frac{\kappa(28t^2-35t-4)}{64h_e^3}\ne0.
\tag{4}
$$
在弱 hook 与旧 $\mathcal M_j=0$ 下，原 $[R,P]$、$[S,P]$ 均归同一个已经为零的 $J(u''((f'')^2-(u'')^2))$ 槽。这里 $a+3b=-(153t^2+26t+8)/(64h_e^2)\ne0$，所以由原 $\mathcal M_j$ 确实可以推出该槽的三个外矩为零。完整二次平移项因此对所用外矩为零。保留外 $x$ 同时平移，得到
$$
\boxed{
\mathcal B_0^{(s)}
=\mathcal B_0+s(a+b)\mathcal A_0+s\chi_\kappa\mathcal R_0,
}
$$
$$
\boxed{
\mathcal B_1^{(s)}
=\mathcal B_1+s\mathcal B_0
+(a+b)(s\mathcal A_1+s^2\mathcal A_0)
+\chi_\kappa(s\mathcal R_1+s^2\mathcal R_0).
}
\tag{5}
$$
同样，
$$
\boxed{\mathcal R_1^{(s)}=\mathcal R_1+s\mathcal R_0.}
\tag{6}
$$
式(6)中 $[R^{(s)},S^{(s)}]$ 新增的 $[P,S]+[R,P]$ 仍由同一旧面积清去；不是仅搬移积分权。

原完整 mixed 身份给
$$
\mathcal R_0=\frac23 C_\theta,\qquad
C_\theta=\int(u'')^2\{(f'')^2-(u'')^2\}.
\tag{7}
$$
于是当 $\mathcal A_0=\mathcal A_1=0$，
$$
\mathcal B_1^{(s)}
=\mathcal B_1+s\mathcal B_0+s\chi_\kappa\mathcal R_1
+\frac23s^2\chi_\kappa C_\theta.
\tag{8}
$$
这个二次中心项是后面真实支付的对象。不能在已付 $\mathcal B_0$ 后再任意共同平移而忽略它。

## 3. 弱宏块中心化：真实复制方差留在常项中

取 R339 已实际完成内部常项、宽 cutoff、三宽补包、旧面积修正和八／十二复制的两种内部宏块，暂用各自辅助中心坐标表示，记作 $\mathcal W_-$、$\mathcal W_+$。它们满足
$$
\mathcal M_j=0\ (j=0,1,2),\qquad
\mathcal A_0=\mathcal A_1=0,
$$
$$
C_\theta(\mathcal W_\pm)=C_\pm\sin^2\theta,\qquad C_-<0<C_+,
$$
$$
\Psi(\mathcal W_-)=-\Delta\sin^2\theta,\quad
\Psi(\mathcal W_+)=\psi_+\sin^2\theta,\quad
\Delta>0,\ \psi_+>0.
\tag{9}
$$
这些系数是已经恢复所有宽尾后的完整值。

在十二复制之前，反射基本块的 $f,g$ 都为偶。原 $[Z_*,W_*](u;D)$ 与 outer 奇偶相反，$[R,S](u;D)$ 与 outer 奇偶相同；右锚反射的误差只是真二次多项式。对紧 outer，
$$
I_j(u,p_2)=0,\qquad j=0,1,2,
\tag{10}
$$
其中 $I_2$ 的 $2u'p_2'$ 必须一并保留。因此中心坐标中的
$\mathcal B_0=\mathcal R_1=0$。

十二副本的正四次权为 $\rho_j=\binom{11}{j}$，相对中心为
$s_j=(j-11/2)D_{\rm cp}$。故
$$
\sum_j\rho_js_j=0,\qquad
\sum_j(-1)^j\rho_js_j^m=0\quad(0\le m\le10).
\tag{11}
$$
(5)、(6)连同(11)给包装后的
$$
\mathcal B_0(\mathcal W_\pm)=\mathcal R_1(\mathcal W_\pm)=0
\quad\text{在其辅助中心坐标中}.
\tag{12}
$$

令完整实际中心值
$$
H_\pm(\theta)=\mathcal B_1(\mathcal W_\pm).
$$
全部 odd 已清，所以它们是
$\cos^2\theta\sin^2\theta,\sin^4\theta$ 的有限线性组合。这里保留了
$$
\frac23\chi_\kappa C_{b,\pm}
\left(\sum_j\rho_js_j^2\right)\sin^2\theta
\tag{13}
$$
这一真实复制方差项；$C_{b,\pm}$ 是复制前反射基块的实际系数。它进入 $H_\pm$，不被当成零或独立可调常数。

把整个内部宏块放到最终物理中心 $X$，(5)、(8)准确给
$$
\boxed{
\mathcal B_0(\mathcal W_\pm@X)
=\frac23\chi_\kappa C_\pm X\sin^2\theta,
}
$$
$$
\boxed{
\mathcal B_1(\mathcal W_\pm@X)
=H_\pm(\theta)+\frac23\chi_\kappa C_\pm X^2\sin^2\theta.
}
\tag{14}
$$
辅助中心计算只是在多项式原算子中作真实平移的代数准备；最后所有物理支撑均位于合法正半轴。

## 4. 两个 even 系数之差是一个完整 diagonal self

采用 R275 的真实规范
$$
S_{Z,W,1}(q)=2I_1\{q,[Z_*,W_*](q;q\odot q)\}.
$$
令
$$
k_*=\frac{d_*b}{2}-e_*a
=-\frac{\kappa(1173t^3+177t^2+122t+8)}{256h_e^3}\ne0,
$$
$$
p_*=\frac{d_*(a+b)+2e_*(4a+b)}3,\qquad
D_*=2d_*(a+b)+e_*(11a+5b).
\tag{15}
$$
对任意紧实 $v$，写
$$
C_2=\int x^2(v'')^4,\quad N_1=\int xv'(v'')^3,\quad
U_3=\int v(v'')^3,\quad V_2=\int(v')^2(v'')^2,
$$
并定义真正 local 四次量
$$
\mathscr L_\kappa(v)
=\frac{D_*}{12}C_2-p_*N_1
+\frac{d_*(a+b)}3U_3+\frac{a(4e_*-d_*)}{2}V_2.
\tag{16}
$$

R275(6)的四条 nonlegal self 及原 Green 项准确合为
$$
S_{Z,W,1}(v)
=\mathscr L_\kappa(v)
+\frac{k_*}{2}\left\{\ell\mu_0^2+\int_\ell^{r_*}[J(v''^2)]^2\right\}
-k_*\mu_0\mu_1.
\tag{17}
$$
这里 $\mu_j=I_j(v,v)$，左尾项 $\ell\mu_0^2$ 与 $-\mu_0\mu_1$ 均真实存在。该式是四次多项式身份，故可非共轭极化到复输入。

对合法复 $q=f+ig$，原三复矩为零，特别 $\mu_0=\mu_1=0$。因此
$$
\boxed{
S_{Z,W,1}(q)
=\mathscr L_\kappa(q)+\frac{k_*}{2}\int[J(q''^2)]^2.
}
\tag{18}
$$
只有在这一步，完整 $J(q''^2)$ 才因整个圆的三矩而真紧。

若 odd 已清，写
$$
2\mathcal B_1(\theta)
=E_{22}\cos^2\theta\sin^2\theta+E_{04}\sin^4\theta.
$$
则
$$
\boxed{E_{22}-E_{04}=\operatorname{Re}S_{Z,W,1}(f+ig).}
\tag{19}
$$
证明不要求 ordered 双线性形式对称。将真实四次 self 写为
$B(f^2,f^2)$ 等槽，左边是
$$
B(f^2,f^2)+B(g^2,g^2)-B(f^2,g^2)-B(g^2,f^2)-4B(fg,fg),
$$
恰为 $\operatorname{Re}B((f+ig)^2,(f+ig)^2)$。两个不同方向的 cross 都保留。

以后若直接写未加倍的
$\mathcal B_1=v_{22}\cos^2\theta\sin^2\theta+v_{04}\sin^4\theta$，
其差 $v_{22}-v_{04}$ 是(19)的二分之一。这个正因子不影响后面的正锥，但规范不混用。

## 5. 先选真实母包，再构造普通与伴随两坡块

使用 R265 的实际 even 母包与 odd 伴随。可先取偶实紧 $\psi$，在八个对称、不交位置上定义
$$
v(y)=\sum_{j=0}^7\psi(y-t_j),\qquad
\widehat v(y)=\sum_{j=0}^7(-1)^{\operatorname{popcount}(j)}\psi(y-t_j).
$$
同一最细包上仅改变符号，所以对任意 $p,q\ge0$，
$$
v^{(p)}v^{(q)}=\widehat v^{(p)}\widehat v^{(q)},\qquad
\mathbf I(v,\widehat v)=0.
\tag{20}
$$
真实 TM 三个符号矩支付第二个等式，不只支付 $I_0$。

按 R267 §§3–5 加入中央正幅和真实三母包宽度，选择一个固定正母宽及真实正参数，使
$$
\mathcal F_\kappa(u_0)
=\frac{\mathcal K_\kappa(u_0)}{C}-\nu=0,
\quad
C=\int(u_0'')^4>0,\quad
\nu=\frac{\int y^2(u_0'')^2+2(u_0')^2}{m},\quad
m=\int(u_0'')^2>0.
\tag{21}
$$
该选择有 R267 的实际非零 $\gamma$ 导数和正宽母根，不把积分常数独立指定。同步取同参数伴随 $\widehat u_0$，仍满足(20)。$u_0$ 为偶，$\widehat u_0$ 为奇。

这里只使用 R267 的初始母包及完整面积身份。随后不要求它的最终六能量隐函数分支；本稿对所需 $\Psi$ 另作完整支付。因而可以固定这个真实母包，再把下述间距作为新的有限选择。

固定任意
$$
\frac13<\alpha<\frac12,\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
q_0=\frac1{16(1-\alpha)^2},\quad n=2^{11}.
$$
低组 $64n$ 个包用宽 $q_0\delta$、系数
$(\epsilon_i\sqrt{\alpha q_0},\sqrt{q_0})$；
高组 $n$ 个包用宽 $\delta$、系数
$(\epsilon_k\sqrt\beta,1)$。
取中心
$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\quad
t^H_k=B(k-c),\quad c=(n-1)/2,
$$
$$
B^2=\frac{A^2((64n)^2-1)-12\nu(1-q_0^2)}{n^2-1}.
\tag{22}
$$
实际中心是 $\xi_i=\xi_0+\delta t_i$；本节先在辅助中心 $\xi_0=0$ 写式，最后的物理平移按第7节处理。$\epsilon_{64k+l}=\epsilon_k\epsilon_l$ 是原 TM 符号。先选足够大的有限 $A>10+\sqrt\nu$，再选一个正有限 $\delta$。R262 的真实间隙保证高包在每格低包31与32之间，所有支撑严格不交。没有执行扫描。

普通版在各外包取
$$
f_-=\sum a_i\eta_i,\qquad g_-=\sum b_i\eta_i,
\quad \eta_i=w_i^{3/2}u_0((x-\xi_i)/w_i).
$$
伴随版取
$$
f_+=f_-,\qquad
g_+=\sum b_i\widehat\eta_i.
\tag{23}
$$
每个最细子包都沿真实实 rank-one 方向；因此 full strong hook 张量为零。原三矩来自(20)、(22)，完整第三按原八副本真实 range 支付。

R267 的准确 self 表给两版均满足
$$
\mathcal M_j=\mathcal A_j=0\quad(j=0,1,2)
\tag{24}
$$
在八／十二完整包装后、全部相位成立。对 $\mathcal A_2$，所需的恰是(21)；原 $\Gamma_{P,L},\Gamma_{P,U}$ 为零。伴随只改变最细包第二系数的符号，even self 不变，odd 由十二副本支付。

两版共同的完整 quartic 张量为
$$
A_4=5C_{22},\qquad E_4=C_{22},\qquad B_4=D_4^{\rm tens}=0.
\tag{25}
$$
所以
$$
C_\theta=0,\qquad J_\theta=0,\qquad
D_{4,\theta}=4C_{22}\sin^2\theta.
\tag{26}
$$
$\Psi$ 因而是严格正的常数乘 $\sin^2\theta$。所有符号变化都来自真实 profiles，不来自负四次权。

## 6. 完整 primitive 的两号，保留每个单包自项

设
$$
\Delta_u=\iint|y-z|u_0''(y)^2u_0''(z)^2\,dy\,dz,\qquad
K_u=\int[J(u_0''\widehat u_0'')]^2,
$$
$$
a_c=q_0(1-\alpha)>0,\quad \ell_c=2q_0\sqrt\alpha,\quad
H_c=2\sqrt\beta,\quad U_x=x^2-6x+1.
$$
$K_u$ 的 integrand 是原真实紧 primitive；$\Delta_u,K_u$ 均由已固定母包决定。

普通版的低、高复平方质量分别为
$-a_c+i\ell_c\epsilon_i$ 与 $64a_c+iH_c\epsilon_k$。
R262(13)保留全部跨 cell 历史，给
$$
\begin{aligned}
\operatorname{Re}\int[J((f_-+ig_-)''^2)]^2
=\delta\bigg\{&
nm^2\left[A(21856a_c^2-32\ell_c^2)-\frac{H_c^2B}{2}\right]\\
&-\frac{n\Delta_u}{2}(64q_0^3U_\alpha+U_\beta)
\bigg\}.
\end{aligned}
\tag{27}
$$
最后一项是单包真实自项。其来源是对总质量为零的复密度使用
$$
\int(J\rho)^2=-\frac12\iint|x-y|\rho(x)\rho(y)\,dx\,dy,
$$
先区分同包和异包后才展开；没有把有限包替换为点质量。

对伴随版，real 密度完全相同，但 imaginary 密度在每个外包的全积分已为零。由 R265(11)、(13)，
$$
\begin{aligned}
\operatorname{Re}\int[J((f_++ig_+)''^2)]^2
=\delta\bigg\{&
21856nm^2a_c^2A-\frac{n\Delta_u a_c^2}{2}(64q_0+4096)\\
&-4nK_u(64\alpha q_0^3+\beta)
\bigg\}.
\end{aligned}
\tag{28}
$$
第二、第三项完整保留。特别，伴随内部 primitive 没有被设成零。

普通式的 $A$ 主量严格为负：$a_c\le1/8$、
$H_c^2\ge28$、$B>64A$ 给
$$
A(21856a_c^2-32\ell_c^2)-H_c^2B/2
<-\frac{1109}{2}A.
\tag{29}
$$
伴随式的 $A$ 系数严格为正。其余项均与 $A$ 无关。

还必须核(18)中的 local 项，而不能只由(27)、(28)下结论。令
$$
H_{\rm loc}
=\frac{D_*}{12}(X_2-C\nu)-p_*N_1
+\frac{d_*(a+b)}3U_3+\frac{a(4e_*-d_*)}{2}V_2,
$$
所有母积分取同一 $u_0$。真实方差(22)、偶性及
$64q_0U_\alpha+U_\beta=0$ 准确给
$$
\boxed{
\operatorname{Re}\mathscr L_\kappa(f_\pm+ig_\pm)
=-64n\delta q_0U_\alpha(1-q_0^2)H_{\rm loc}.
}
\tag{30}
$$
两版相同，且与间距 $A$ 无关。这里用的是完整方差身份，不是仅说 $\mathcal F_\kappa=0$。

结合(18)、(27)–(30)与 $k_*\ne0$，一个足够大但有限的 $A$ 给两种
$\operatorname{Re}S_{Z,W,1}$ 严格相反的符号。这个选择发生在母包固定以后，旧等式(21)、(24)对任何该合法 $A$ 本来就成立。

## 7. 包装、真实尾、伸缩与一个低成本差方向

在普通基块的辅助中心，TM 反序使 $f$ 为奇、$g$ 为偶；在伴随基块，$f,g$ 都为奇。原反射式与(10)给两版 $\mathcal B_0,\mathcal R_1$ 的 even 相位为零。由(24)、(26)，(5)、(6)又使这些 even 值在实际平移下不变。

原八副本不改变这些零；十二副本清掉剩余 odd 相位。因此两种完整强宏块都满足
$$
\boxed{
\mathcal B_0=\mathcal R_1=C_\theta=0,\qquad
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2).
}
\tag{31}
$$
原 $\mathcal B_1$ 的 even 部分在平移下准确不变；odd 部分的真实平移多项式由原十一差分清去。因此八／十二复制只将(19)的差乘一个正四次权和，并不添另一个未知中心项。

记这两条真实未加倍 $\mathcal B_1$ even 向量为 $v_+,v_-$，按其差的符号重命名，使
$$
\Delta(v_+):=(v_+)_{22}-(v_+)_{04}>0,\qquad
\Delta(v_-)<0.
\tag{32}
$$
对任意实际标量目标 $r$，有有限严格正四次权 $\lambda_\pm$，使
$$
\lambda_+\Delta(v_+)+\lambda_-\Delta(v_-)=r.
\tag{33}
$$
例如先解一个非负表示，再加一个严格正的零 balance。它们的真实 profile 幅度是 $\lambda_\pm^{1/4}$。

对整块 $f_\Lambda(x)=f(x/\Lambda)$，原算子完整权为
$P:-3,\ R,S:-2,\ L,U:-1$。由原 $I_1$ 的 $x$ 与两次外导数，
$$
\boxed{
\mathcal B_1(f_\Lambda,g_\Lambda)=\Lambda^{-5}\mathcal B_1(f,g).
}
\tag{34}
$$
原 $\Psi$ 是全式八阶 local 四次积分，
$$
\Psi(f_\Lambda,g_\Lambda)=\Lambda^{-7}\Psi(f,g).
\tag{35}
$$
(34)不是 principal 估计。将(33)的权同时改为 $\Lambda^5\lambda_\pm$，整个 $\mathcal B_1$ 向量不变，而新增 $\Psi$ 恰为
$$
\Lambda^{-2}S_\Psi\sin^2\theta,\qquad S_\Psi>0.
\tag{36}
$$
可以取一个有限 $\Lambda$ 将其成本做得任意小。

这些强块可以放在任意最终不交的合法位置，因为(31)使(8)的全部位置项准确为零。R334 的四个 $\mathcal A_2$ 模块也有同样的 $\mathcal B_0=\mathcal R_1=C_\theta=0$：其偶母包、真实 TM、旧三面积及 $\mathcal A_0=\mathcal A_1=0$ 足以重复本节的反射证明；此结论不要求它们自己的 $\mathcal A_2$ 为零。它们的 $\mathcal B_1$ 也平移不变，并且在 R334 的 $\Lambda^5$ 放大后整值不变。

## 8. 先固定所有内部积分和正权，不提前决定共同中心

从起点复用 R339 两种已经完成宽恢复的内部宏块(9)，构造本稿新的最终圆。不是在 R339 已冻结的最终圆上事后无偿移动中心。

先选一个有限比值 $R>1$，使
$$
w=-\frac{C_-}{RC_+}>0,\qquad w\psi_+<\Delta/4.
\tag{37}
$$
再固定
$$
0<p<1/R.
\tag{38}
$$
负宏块将有两个相同内部副本，其正四次权分别为 $1-p,p$；正宏块的权为 $w$。其总 $\Psi$ 仍是
$$
(-\Delta+w\psi_+)\sin^2\theta<-\frac{3\Delta}{4}\sin^2\theta.
$$
三个物理中心尚未固定，但其内部相对位置、全部真实 copy 权及所有成本已经固定。

旧 $\mathcal M_j,\mathcal A_0,\mathcal A_1$ 继续为零。其实际 $\mathcal A_2$ 残差不随最后中心改变。因此先用 R334 的四个真实方向完整支付该二维目标；选有限正伸缩，使这四个模块新增 $\Psi$ 小于 $\Delta/8$。同时记录它们完整的、平移不变的 $\mathcal B_1$ 向量。

然后读取当前 $\mathcal B_1$ 两个 even 系数之差。弱块的(14)中位置项均为共同 $\sin^2\theta$，所以该差不依赖尚未确定的三个中心。用(33)准确支付它，再取(36)的有限伸缩，使这两模块的新增 $\Psi$ 也小于 $\Delta/8$。

到此所有内部 profiles、宽度、复制、正四次幅和两类强模块均已固定。所有新增强块对 $\mathcal B_0$ 为零。两个 even 系数相等后，$\cos^2\theta\sin^2\theta+\sin^4\theta=\sin^2\theta$，所以未付的 $\mathcal B_1$ 仅剩一个共同系数；记不含三个宏块最后中心项的完整有限值为 $b_{\rm loc}$。它包括 $H_\pm$ 中的真实复制方差及六个强模块的完整贡献，不是一个 freely chosen self 常数。

$\Psi$ 此时仍有严格负储备
$$
\Psi=-\Delta_{\rm rem}\sin^2\theta,\qquad
\Delta_{\rm rem}>\Delta/2>0.
\tag{39}
$$
它与最后三个中心无关。

## 9. 三个真实正中心同时支付第零与第一矩

取一个以后足够大的有限 $X>0$。正宏块的中心定为
$$
Y=RX.
$$
两个负宏块的中心为 $x_1,x_2$，先要求
$$
(1-p)x_1+px_2=X.
\tag{40}
$$
由(14)、(37)，完整第零矩准确为
$$
\mathcal B_0
=\frac23\chi_\kappa
\{C_-X+wC_+RX\}\sin^2\theta=0.
\tag{41}
$$
所有强模块在(31)中已经单独贡献零。

第一矩的完整值现在是
$$
\mathcal B_1(\theta)=
\left[
b_{\rm loc}+\frac23\chi_\kappa
\{C_-((1-p)x_1^2+px_2^2)+wC_+R^2X^2\}
\right]\sin^2\theta.
\tag{42}
$$
这里没有省略不同实际 copy 的二次中心和；它们的内方差已包含于 $b_{\rm loc}$，剩余项只是(14)的真实宏块移动。

令
$$
S_*=-\frac{3b_{\rm loc}}{2\chi_\kappa}.
$$
由 $wC_+=-C_-/R$，(40)使(42)所需的中心二阶和化为
$$
C_-\left\{\frac{1-p}{p}(X-x_1)^2-(R-1)X^2\right\}.
$$
取准确的
$$
\boxed{
x_1=X-\sqrt{\frac p{1-p}
\left\{(R-1)X^2+\frac{S_*}{C_-}\right\}},
\qquad
x_2=\frac{X-(1-p)x_1}{p}.
}
\tag{43}
$$
充分大的有限 $X$ 使根号为正，并给所需二阶和准确等于 $S_*$。因此
$$
\boxed{\mathcal B_0=\mathcal B_1=0\quad\text{全部 }\theta.}
\tag{44}
$$

还必须支付真实支撑。由(38)，
$$
\frac{x_1}{X}\longrightarrow
1-\sqrt{\frac{p(R-1)}{1-p}}>0,
$$
$$
\frac{x_2}{X}\longrightarrow
1+\sqrt{\frac{(1-p)(R-1)}p}>R.
\tag{45}
$$
所以 $X$ 足够大且有限时，
$$
0<x_1<Y<x_2,
$$
相邻间距都随 $X$ 线性增大。三个内部包络已经固定且有限；可一次选 $X$ 使其全部严格不交，整个支撑位于合法正半轴，并使每个内部十二副本的真实中心也为正。

这不是沿一个可能相交的平移路径调用连续性。式(43)直接给最后的准确位置，(45)给该位置的严格支撑间隙。两个负块并不都放在正块左侧；右方负块提供了第一中心矩固定时所需的第二中心矩方向。

此后不再共同平移这三个块，也不再改变其幅度。四个 $\mathcal A_2$ 模块与两个差方向模块按(31)放在其它最终不交正包络内，不改变(44)。$\Psi$ 仍是(39)，旧两完整面积也全部保持。

## 10. 最后同一有限频率根保持新第一矩

从构造起点按 R325/R334 初选强控制器的真实有限观察
$$
\mathcal F_\star=(\mathcal F,\int(v'')^4),
$$
其中 $\mathcal F$ 含原全部72 Gaussian 面积 self 的实际平移系数及三矩有序接口。选择其真正最大秩母包、固定非零 minor、纠正方向及两种 even 振荡形状；没有将前面任意母包自动称作 regular 点。

在剩余最终正位置构造原 R280/R293 强控制宏块。它自身的全部72面积为零，故新 $\mathcal B_0,\mathcal B_1$ 都为零。其
$\Psi=\psi_{\mathcal C}\sin^2\theta$，$\psi_{\mathcal C}>0$。
以正四次权 $\Delta_{\rm rem}/\psi_{\mathcal C}$ 准确消去(39)。

随后只在该控制器的强 rank-one 微包内作同 $\mathcal F_\star$ 的有限频率变化。R325 的真实两形状、实际交替位置与全部完整 copy 权给三条 $F_i$ 的正锥 $\mathbb R^3$。本稿全部固定模块、最终真实位置、原尾与低阶项都进入同一个完整有限基线：
$$
\mathbf F_N(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{46}
$$
取严格正 balance 与三个独立列，固定其余正幅。非退化零在小 $C^1$ 扰动下稳定，故一个足够大但有限的整数 $N$ 给
$$
F_0=F_1=F_2=0.
\tag{47}
$$
这不是只令最高平方为零。

同 $\mathcal F_\star$ 纠正保持控制器自己的全部72面积与 quartic 值。因此它对新 $\mathcal B_1$ 始终准确贡献零，$\Psi=0$ 也保持。三个弱宏块、六个面积模块、(37)、(43)中的正权与实际中心全部固定。由原完整相位归约，(47)及所有已列面积均对全部 $\theta$ 成立。

最后 R325 的完整一层恒等给
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0.
\tag{48}
$$
本稿没有把这一单层系数的零扩成整个一层函数或完整第四 ruling。

## 11. 原块加法、合法区间与依赖次序

每一个参与相加的对象都是完整三矩圆，所以其每个 $D_\theta$ 的二次输出 $XD_\theta$ 真紧。不同完整块的同点 inner 乘积为零；同块 nested 输出仍可能有真实二次左尾，但(10)使其与另一个紧 outer 的三个原矩准确正交。两个 directed 方向分别保留后，得到本文所有面积和三条 $F_i$ 的原式加法。$\Psi$ 为 local 四次积分，直接相加。

这仅对完整三矩块成立。第6节的外包并非各自三矩闭，其真实 primitive 平台和自项一直保留在(27)、(28)。

完整第三保持原几何 $M=0,T=\kappa_H\mathfrak H$、真实弱单 hook、共同初值及右锚。八副本作用原完整相位 range，镜像只作用 profiles；没有反射几何或要求四个中间槽各自周期。所有强区均 full hook 零，弱核心中的真正 rank-two 开段始终存在。

选择顺序为：

1. 固定真实有限几何与非零 $\kappa$，初选最后控制器的 $\mathcal F_\star$、最大秩母包和纠正方向。
2. 完成 R339 两种内部弱宏块的原 cutoff、宽矩补偿、所有修正和复制，固定实际 $C_\pm,\Psi_\pm,H_\pm$。
3. 固定(37)、(38)的 $R,w,p$。三个最终中心尚未指定；旧 $\mathcal A_2$ 目标及新 even 差均不依赖这些中心。
4. 完成 R334 四模块的正幅支付及有限伸缩。再以第5–7节实际普通／伴随块支付 even 差，并把它们的完整 $\Psi$ 成本纳入(39)。
5. 此时 $b_{\rm loc}$ 与全部内部包络已经固定。按(43)选三个最终实际中心，再把六个强模块和强控制器放在其它不交合法正包络中。
6. 对上述整个有限集合选共同有限正区间 $I$ 和右锚。固定几何上 $h>0$、$\omega$ 有界，原合法条件 $x+\omega(s)>0$ 在充分右半轴有统一正间隙。可从第5步直接在该半轴安排坐标，最后只选择包含这些既定坐标的有限 $I$，不能再整体搬移。
7. 全部位置、幅度、复制固定后，取一个有限 $N$ 完成(47)。最后作一次共同正幅归一化，并固定新 seed 的目标 metric。

原实际有序 self、宽过渡费用和最终位置从未作为自由独立坐标。所有支撑、伸缩、幅度、频率都有限，未运行任何科学或人工程序。

## 12. 准确新增结论

在同一真实几何上存在一个新的弱单 hook、导数 rank-two 三矩圆，其完整三阶已经支付，并且同一最终 profile 满足
$$
\mathcal M_0=\mathcal M_1=\mathcal M_2
=\mathcal A_0=\mathcal A_1=\mathcal A_2
=\mathcal B_0=\mathcal B_1=0
$$
全部相位；同时保留 $\Psi=F_0=F_1=F_2=0$ 及完整一层系数(48)。

R337 的同号架构障碍仍真。本文沿 R339 已造的真正异号 $C$ 通道，进一步改变正、负块的最终次序和第二中心矩；普通／伴随方向只负责原第一矩的另一个 even 分量。没有把有限 self 表当成任意可指定量。

第三面积 $\mathcal B_2$、其余 Gaussian 面积、其它对称乘积与零／一层函数、canonical 平台／退化通量、完整第四 period 及同一个 gauge 的 joint 仍未支付。强控制器自身的全72零不等于整个弱强组合的全72零。本文从起点选择新圆及新 seed，目标 metric 在最后固定，不声称对 R339 已冻结旧 seed 的目标作无偿变形。
