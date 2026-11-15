# R357：真实三母纤维与三维有序 profile 正锥

日期：2026-11-15。**有限纸面建设性证明；没有执行求积、符号程序、参数扫描、人工测试或研究计算。**

本稿从实际偶紧母函数构造
$\mathcal F_\kappa=\mathcal J=\mathcal K=0$ 的正则基点及两个真实自由形状坐标，再用三种有限排序证明
$(\operatorname{Re}S_{P,Y,0}(f+ig),E_{04}^{P,0},-E_{04}^{P,1}/\xi)$
的三维实际正锥。宽常量项、母原子、正宽微包、间隙容量、全部原尾和完整副本均计入；没有将有限形状积分当作独立坐标。

这是一条可供后继联合支付使用的完整建设性结论。它不预先支付 P–Y 第零或第二外矩，不把旧 $\mathcal B_1$ 与同权 $\mathcal P_0$ 的控制当作独立。下面的三维正锥只是明确列出的三个真实坐标；它与两个母形自由坐标如何接成新的完整目标，须另按原式证明。
来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R278](R278-third-slope-gap-masses-break-the-first-moment-halfplane.md)、[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md)、[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)及 R354。

## 1. 原规范、真实目标与两个尚未付的门

沿用同一右锚 $JF(x)=\int_x^{r_*}F$，
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e},\qquad 0<t=\kappa^2<1/100.
\tag{1}
$$
可以固定 $\kappa>0$。所用非零量包括
$b,a-b,d+7e,d^2-e^2$ 及 $k_*=db/2-ea$。

$\mathcal M_j,\mathcal A_j,\mathcal B_j,\mathcal C_j,\mathcal D_j,\mathcal P_j$
仍分别对应
$[W_*,P],[Z_*,P],[Z_*,W_*],[Z_*,Y],[W_*,Y],[P,Y]$，
outer 为 $\phi=f\cos\theta+g\sin\theta$，inner 为
$D=f\odot f-\phi\odot\phi$。外矩始终是
$$
I_0(u,w)=\int u''w'',\quad I_1(u,w)=\int xu''w'',\quad
I_2(u,w)=\int(x^2u''w''+2u'w').
$$
写 $E_{22},E_{04}$ 时指 **$2I_j$ 的原 even 系数**，并记
$E_p=E_{22}-E_{04}$。非零常数缩放不会改变下文正锥性质，但不在原式中省略。

R354 的真实偶弱圆已满足
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j
=\mathcal C_j=\mathcal D_j=0\quad(j=0,1,2),\qquad \mathcal P_1=0.
\tag{2}
$$
当前只剩 $\mathcal P_0,\mathcal P_2$；本稿为它们提供新的真实强原型接口，不在这里宣称任一完整门已归零。
取该构造最后强控制器以前的同一实际入口，保(2)，且
$\Psi=-\Delta\sin^2\theta$、$\Delta>0$。旧弱核心、远宽过渡、补矩及中心全部固定。

§2—5 的原型本身全部位于正半轴。后继若将其与完整空间反射等幅配对，R354 的准确反射式会清掉
$\mathcal B_0,\mathcal B_2,\mathcal C_1,\mathcal P_1,\mathcal D_0,\mathcal D_2$；
$\mathcal M_j,\mathcal A_j$ 另由本文真实三矩和母条件保持。
必须先把本稿的有序参数映到所需的实际 reflection-even 目标，再做这种配对。
特别，下文 $V=-E_{04}^{P,1}/\xi$ 是**正半块**的真实参数，不声称反射后已经为零的 $\mathcal P_1$ 仍可任意指定。
$\Psi$ 与三个 directed 行为 reflection-even，也不能靠反射删去其成本。

## 2. 一个实际偶母形的三个原观察

对偶实紧 $v$，置 $p=v',r=v''$，定义
$$
m=\int r^2>0,\quad C=\int r^4>0,\quad
\nu=\frac{\int(y^2r^2+2p^2)}m,
$$
$$
X_2=\int y^2r^4,\quad N=\int yp r^3,\quad
V_2=\int p^2r^2,\quad U_3=\int vr^3,
$$
$$
\mathcal J=3V_2+U_3-2N,\quad
\mathcal K=V_2-\frac25N,\quad
J_2=U_3-2V_2=\mathcal J-5\mathcal K.
\tag{3}
$$
$\mathcal F_\kappa$ 是 R267 的真实母条件：
$$
\lambda C(\mathcal F_\kappa+\nu)
=\lambda X_2+\frac43(d+11e)N-\frac{8e}{3}(3V_2+U_3),
\qquad \lambda=-5(d+7e)/6.
\tag{4}
$$
因此在 $\mathcal F_\kappa=0$ 上，
$$
X_2-C\nu=\frac85N-\frac{16e}{5(d+7e)}\mathcal J.
\tag{5}
$$

下面证明存在实际正则基点
$$
\mathcal F_\kappa=\mathcal J=\mathcal K=0,
\tag{6}
$$
且 $\mathcal J,\mathcal K$ 可作为两个真实局部坐标。
这不是把三个积分常数当成自由输入；也不引用 R278 未曾完成的第四母参数构造。

### 2.1 宽常量项给一个严格简单的 J2 根

先选非负偶紧 $\psi$，$\int\psi=1$，三个相同窄支撑在
$0,\pm L_0$ 严格不交。令
$$
r_0=\psi_\epsilon-\frac12T_{L_0}\psi_\epsilon
-\frac12T_{-L_0}\psi_\epsilon,\qquad w=J^2r_0.
$$
$\int r_0=\int yr_0=0$，故 $w$ 真紧且偶，并有
$$
\int(w'')^3=\frac34\int\psi_\epsilon^3>0.
\tag{7}
$$
取偶紧 cutoff $\chi_R(y)=\chi(y/R)$，在 $w$ 的整个支撑上等于1；
它所有正阶导数的支撑与 $w$ 严格不交。对实际
$v_M=w+M\chi_R$，
$$
\boxed{
J_2(v_M)=J_2(w)+M\int(w'')^3+
M^4R^{-5}J_2(\chi).
}
\tag{8}
$$
core 中只 $U_3$ 增加线性项；宽过渡上的全部四次成本是最后一项。
先取足够大的有限 $R$，在
$M=-J_2(w)/\int(w'')^3$ 附近有一个简单真实根 $M_*$，
$\partial_MJ_2(v_{M_*})\ne0$。这只是一个有限多项式的简单根稳定性，不需要求积值或无穷宽输入。

### 2.2 同源伴随须在整个原子外翻号

$v_M$ 的宽常量平台不可被任意切开翻号。先把**整个** $v_M$
放入八个等距、互不交、关于零对称的完整原子：
$$
V_M=\sum_{\ell=0}^7 T_{\xi_\ell}v_M,\qquad
\widetilde V_M=\sum_{\ell=0}^7
(-1)^{\operatorname{popcount}\ell}T_{\xi_\ell}v_M .
\tag{9}
$$
间距此时取一个固定有限值，大于两个完整原子半径之和。
$V_M$ 偶，$\widetilde V_M$ 奇；所有 derivative squares 逐点相同，
而 $I_0,I_1,I_2(V_M,\widetilde V_M)$ 由 TM 的零、一次、二次矩准确为零。
$J_2(V_M)=8J_2(v_M)$，其简单根保留。

令
$$
e_M=\operatorname{EL}\!\left(\int V_M'(V_M'')^3\right)
=12r^2r'+6V_M'(r')^2+6V_M'rr'',\quad
K_M=\int e_M^2>0 .
\tag{10}
$$
这是奇函数。$K_M>0$ 的 R346 原证明只用非零真紧输入，故适用于本原子：
若 $e_M=0$，则先后由平端得
$V_M'rr'+r^3/3=0$、$V_M'r^3=0$，
在 $r\ne0$ 开区矛盾。
由于该 Euler 表达是局部平移协变的，$e_M$ 也是八个同形原子的和。
故 $V_M+\eta e_M$ 仍有逐原子翻号的同源伴随，三交叉矩仍准确为零。

### 2.3 三个真实变量的非退化 minor

固定 $L_*=1/2$，用真实小正母宽 $h$ 构造
$$
\begin{aligned}
u_{\gamma,z,M,h}(y)={}&
\gamma h^{3/2}V_M(y/h)\\
&+h^{3/2}(V_M+hz e_M)((y-L_*)/h)\\
&+h^{3/2}(V_M+hz e_M)(-(y+L_*)/h).
\end{aligned}
\tag{11}
$$
三个支撑严格不交，整体偶。原中央宽参数固定为1，不需要另解原能量条件 $\mathcal H=0$。
所有子原子都有上述同源伴随，左右按同一实际镜像构造。

仅归一后的三个标量延拓到 $h=0$。它们是 $h^2$ 及有限参数的解析函数，原因为积分只在三个互不交的有限 supports 上展开，多项式奇项被镜像消去；分母 $m,C$ 的归一极限严格正。
准确极限是
$$
\mathcal F_\kappa\longrightarrow
2L_*^2\left(\frac1{\gamma^4+2}-\frac1{\gamma^2+2}\right),
$$
$$
\frac{\mathcal J(u)}h\longrightarrow
(\gamma^4+2)\mathcal J(V_M)-4L_*K_Mz,\qquad
\frac{J_2(u)}h\longrightarrow(\gamma^4+2)J_2(V_M).
\tag{12}
$$
这里 $\int(V_M+\eta e_M)'((V_M+\eta e_M)'')^3
=K_M\eta+O(\eta^3)$；它正是(12)第二行的非平凡位置项。

在
$$
\gamma=1,\quad M=M_*,\quad
z=\frac{3\mathcal J(V_{M_*})}{4L_*K_{M_*}},
$$
三行极限为零；对 $(\gamma,z,M)$ 的 Jacobian 是三角型，三个对角项为
$$
-\frac{4L_*^2}{9},\qquad -4L_*K_{M_*},\qquad
3\partial_MJ_2(V_{M_*}) .
\tag{13}
$$
全部非零。有限维 IFT 给一个足够小但**实际正**的 $h$ 及真母根。
再固定这个 $h$，同一 minor 给一个真实二参数小族
$$
\boxed{
\mathcal F_\kappa(u_{\eta,\zeta})=0,\qquad
\mathcal J(u_{\eta,\zeta})/h=\eta,\qquad
\mathcal K(u_{\eta,\zeta})/h=\zeta.
}
\tag{14}
$$
$\operatorname{supp}u_{\eta,\zeta}\subset(-1,1)$ 可在首次选小 $h$ 时统一保证。
宽常量 $R$、原子间距、母宽 $h$ 此后均为有限固定量。
原 profiles 在 $h=0$ 不被当作合法输入；实际根及两自由坐标都位于 $h>0$。

## 3. 原有限 cell 数据与三个实际有序坐标

本节只使用(14)的基点 $\eta=\zeta=0$。
取
$$
\alpha_*=\frac{19}{40},\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
q=\frac1{16(1-\alpha)^2},\quad a_c=q(1-\alpha).
$$
故基点 $q=100/441\in(1/5,1/4)$；稍后的两个不同 $\alpha$ 取其小邻域。

每个实际微包为
$\eta_{w,\xi}(x)=w^{3/2}u((x-\xi)/w)$。
使用 R269/R343 的两种真实排序 $\rho=0,20$：
low 为 $64n$ 个宽 $\delta q$、平方幅 $(\alpha q,q)$ 的包，
high 为 $n$ 个宽 $\delta$、平方幅 $(\beta,1)$ 的包，
$n=2^M$ 为最终有限数，$M\ge11$。辅助中心是
$$
t^L_{k,\ell}=64A(k-(n-1)/2)+A(\ell-31.5),
$$
$$
t^H_k=B_\rho(k-(n-1)/2)+\rho A\sigma_k,\qquad
\sigma_k=(-1)^{\operatorname{popcount}\lfloor k/4\rfloor},
$$
$$
B_\rho^2=
\frac{A^2((64n)^2-1)-12\nu(1-q^2)-12\rho^2A^2}{n^2-1}.
\tag{15}
$$
所有 TM 符号、母包及实际间隙按原来源取；不是交换一个 abstract list。
$A$ 足大后两排序严格不交，并准确满足
$V_L-V_H=\nu(1-q^2)$。

先做八个完整第三副本，再做十二个完整 odd 副本；实际四次权和记 $\mathcal W>0$，共同加权中心取零。
在最后真实正中心 $\xi$，定义
$$
Q=\operatorname{Re}S_{P,Y,0}(f+ig),\qquad
S=E_{04}^{P,0},\qquad
V=-E_{04}^{P,1}/\xi.
\tag{16}
$$
原 R271 完整 self/cross 给
$V=\mathcal Wm^2\delta U_{01}$；$Q,S,V$ 都是实际原积分，且均准确为 $\delta$ 乘一个与最终共同中心无关的系数。
这是三复矩、完整 quartic 零/一次矩及真实方差的结果，不对任意 profile 宣称平移不变。

按 R343、R353 的原尾公式，在先固定母与 $n$ 后，
$$
\frac{S}{\mathcal Wna_cm^2\delta A}\longrightarrow s_\rho,\qquad
\frac{V}{\mathcal Wna_cm^2\delta A}\longrightarrow v_\rho
\quad(A\to\infty),
$$
其中 $a_c$ 为 cell 质量，和 Gaussian 系数 $a$ 区分；
$$
s_\rho=10928q-(32q+1)\rho^2,
$$
$$
v_\rho=(64q+1)\left[
\frac{16}{3}\frac{4095-12\rho^2}{b_\rho+64}
+\frac32\rho^2-512\right],\qquad
b_\rho=\sqrt{4096+\frac{4095-12\rho^2}{n^2-1}}.
\tag{17}
$$
完整有限式含母 $\Delta,\nu$、local 项和副本方差；只有除以 $A$ 后才消失。
于是
$$
s_0>0>s_{20},\qquad v_0<0<v_{20}.
$$
并且将两个列按正权消掉 $S$ 后，$V$ 严格负：
$$
v_0<-\frac{2731}{8}(64q+1),\qquad
v_{20}<88(64q+1),
$$
$$
88\cdot10928q<\frac{2731}{8}(1872q+400)\quad(q<1/4).
\tag{18}
$$
最后一个严格不等式的差等价于
$322610q<136550$，故有明确余量。
选择一个足够大的**有限** $A$ 即保这个实际符号。

每种排序均有 ordinary 和同源 companion 两版。
它们的 $S,V$ 准确相同，$Q$ 严格异号；只在 $Q$ 轴上的符号标签记为 $+,-$，不混淆 R278 所用 $\mathscr Q=-Q$ 的反号规范。
这仍用真正的 primitive，而非把单包 $P(u,u)$ 当作紧场。

## 4. 第三种真实排序打开共同 S,V 锥

只改变第三种原型。取小固定 $r_*>0$，
$$
H=\beta(\alpha)+r_*,\quad
q=\frac{H-1}{64(1-\alpha)},\quad a_c=\frac{H-1}{64},\quad
T_r=\frac{(H-\alpha)(H-\beta)}4>0.
\tag{19}
$$
low/high 仍为 $64n,n$ 个，third slope 为 $a_i^2=b_i^2$；
所有 mid 与 low **同宽 $q$**。
它们总四次质量规定为 $\sum_{\rm mid}b_i^4/q=nT_r$。

### 4.1 先固定 n，后固定有限容量，选择不循环

用 $\rho=0$ 的真实 gaps。R278 给
$$
J(D_{\rm real})=0,\qquad
J(xD_{\rm real})=
\delta\,64a_cm(B-64A)\frac{n^2/4-j^2}{2}>0
\tag{20}
$$
在第 $j$ 个整个 gap 内准确成立。
选靠近归一 $0,\pm1/\sqrt2,\pm\sqrt3/2$ 的五个 gap，
每个放 $N=2^s\ge8$ 个间距 $4q$ 的同形包。
设 $Nq\le A/32$，其整个半径小于 $A/16$，所以原真支撑装得下。

五簇的正四次概率解实际中心的零、二、四矩，
使它们准确等于原 low 中心分布。
除以 $(32nA)^2,(32nA)^4$ 后，目标趋于 $(1/3,1/5)$，
矩阵列趋于节点平方 $0,1/2,3/4$ 的 Vandermonde。
严格正极限解为
$$
(p_0,p_1,p_2)=(19/45,2/5,8/45).
\tag{21}
$$
关键是簇内半径界给出的误差 $O(1/n)$ 在
**整个** $Nq/A\le1/32$ 范围一致。
故先取一次足够大的有限 $n$，就对后续所有允许的有限容量保正；
不需要在增大 $A$ 以后再提高 $n$。

为同一母小邻域统一选参，可按 R278 固定 $q_{\max}<1/3$，
取 $A=\Lambda+\sqrt\nu$，$N$ 为不超过
$\Lambda/(32q_{\max})$ 的最大二幂。足够大有限 $\Lambda$ 时
$$
N\ge8,\qquad c_0A\le Nq\le A/32
\tag{22}
$$
在该邻域一致成立。
之后固定这个实际 $N$；小形状变化中不跳换整数。

每簇的真幅为
$$
b_j^4=nT_r\pi_jq/N,
$$
TM 符号使其自身三复矩全零。整个 mid 的 quartic 中心矩
$0,1,2,3,4$ 与 low 准确一致；奇矩由真实镜像支付。

### 4.2 新局部代价及真实有序响应

对任何所用中心次数至多4的 local self，R278 的准确代数给
$$
E_{22}=\left(\alpha+H-5+
\frac{(1-\alpha)(H-\beta)}{H-1}\right)E_{04}.
\tag{23}
$$
这取代旧两斜率的 $\alpha\beta$，没有沿用错误的旧比例。
相同宽度 $q$ 使(23)保全部有限宽项。
由(5)、完整 quartic 张量和该匹配，原
$\mathcal M_j=\mathcal A_j=0$ 继续成立。
本节不调用 R278 的旧四变量能量 IFT；该稿 §3–5、7–9 的
moment/capacity/history 身份本身已经适用于现在固定的实际母与斜率。
$\Psi$ 和 directed 行在末尾支付。

在 $\theta=\pi/2$，mid inner 差为零。
真实跨核与(20)给
$$
\Delta S=0,\qquad
\Delta V=\sum_j\mu_jJ(xD_{\rm real})|_j>0,\qquad
\mu_j=m\sqrt{nT_r\pi_jNq}.
\tag{24}
$$
整个真实支撑上的 primitive 是同一常数，所以没有点质量近似。
两侧对称 gap 使
$\Delta E_{04}^{P,1}=-\xi\Delta V$；原 $I_2$ 的导数补项也包含在(20)的真矩中。
由(22)，固定 $n,r_*$ 后
$$
\Delta V\ge c\,\delta A^{3/2},\qquad
S_{\rm old},V_{\rm old}=O(\delta A),\qquad S_{\rm old}>0
\tag{25}
$$
对足够大有限 $A$ 成立。因此第三列可以满足
$S>0$、$V/S$ 任意足够大。

ordinary/companion 的 $Q$ 两号仍保留。准确依据是先用
$\mathcal A_2=0,\mathcal F_\kappa=0$ 消整个 local 大中心项：
$$
\sum_i\operatorname{Re}(a_i+ib_i)^4
\frac{C\xi_i^2}{w_i}
=-C\nu\sum_i\operatorname{Re}(a_i+ib_i)^4w_i.
\tag{26}
$$
每个 mid primitive 真紧、积分为零，和 gap 上旧常 primitive 的交叉为零；
TM 前缀界使其自身平方积分不超过
$16m^2nT_r\pi_jq^2$，不随 $A$ 增长。
旧 ordinary 和 companion 的严格相反线性 $A$ 主项正是 R278 §8 的原有序式。
同一个有限 $A$ 可以同时满足(25)和 $Q$ 两号。
这里没有先把大中心项估成有界，也没有重新使用未满足的旧能量条件。

## 5. 独立的三维实际正锥定理

前两种排序的正组合在 $S=0$ 上有 $V<0$。
第三种与第二种消 $S$ 的正组合可由(25)取为 $V>0$。
所以三个真实 $(S,V)$ 列满秩2，并有全部三个分量严格正的零关系。

每种排序有相同 $(S,V)$ 的两个真实 $Q$ 异号版本。
先在各对内部用严格正权清掉 $Q$，再用上述三维正权清掉共同两行；
得到全部六个系数严格正的 kernel。
一对的差给 $Q$ 轴，三种共同列给其余二维，故
$$
\boxed{
\operatorname{rank}(Q,S,V)=3,\qquad
\ker\text{ 含严格正向量，}\quad
\operatorname{cone}_+=\mathbb R^3.
}
\tag{27}
$$
所有列均为实际有限 profiles。
若辅助证明用了同中心两列，先以非零三列 minor 的稳定性分开最后正中心；
$Q,S,V$ 的共同平移身份保持，随后选共同充分小的**有限正** $\delta$
使全部支撑严格分离。
实际复制权、形状、有限 $n,N,A,h,R$ 从未被设成极限对象。
同一次最终正公共幅度归一化只正乘每列，不改变(27)。

(14)、(27)是本稿的两个完整结论。它们可以用于同权 $(\mathcal B_1,\mathcal P_0)$ 的另一个联合问题；本文不据三维满秩宣称那四个实际坐标已经可任意支付。


## 6. 完整有限次序与保留的真实代价

全部选择按下列顺序完成。

1. 固定小共振参数及原母观察(3)—(4)。先取(7)的实际偶原子，再选有限宽常量过渡 $R$、简单根 $M_*$ 和八原子间距。
2. 在这份有限原子上选择一个实际小正母宽 $h$，用(13)解真三母根，再固定(14)的小参数盒。所有母和同源伴随都在共同紧区间，全部正宽不退化。
3. 选定 $\alpha_*$ 及第三斜率的小正 $r_*$。先取有限 $n$，由 §4.1 对整容量域的统一正性支付五簇矩阵；随后才取有限 $\Lambda,A,N$。两排序的严格负共同方向和第三排序的严格正共同方向、各自 $Q$ 两号由同一个足够大的有限选择同时保持。
4. 八个完整第三副本、十二个完整 odd 副本的有限位置与权重在此一并固定。其四次加权中心取零；所有 base 内部的原有序项均保留。只有在 inner 的完整三矩为零后，跨完整副本的项才由 R259/R263 消掉。
5. 固定最后不同的正中心，最后取共同有限正 $\delta$ 使所有真实包络严格分离。负的 scalar 值来自真实 profiles 的原值，正四次权来自(27)；没有以负幅度或 formal span 代替可达性。

所得每个完整原型都保三矩、full strong hook、完整第二／第三 range、
$\mathcal M_j=\mathcal A_j=0$（$j=0,1,2$）及全部36个 Gaussian odd 位置。
原 quartic 张量仍为 $A_4=5C_{22}$、$E_4=C_{22}$；
所以原 $\Psi=\psi\sin^2\theta$，$\psi>0$。
$\mathcal B_1,\mathcal B_2,\mathcal C_j,\mathcal D_j$、
$\mathcal P_0,\mathcal P_1,\mathcal P_2$ 和三个 directed 行，
除本稿明确给出的坐标/身份以外，都保留其完整真实值。
尤其没有要求 $\mathcal H=0$、$L_c=M_c=0$ 或旧能量支路条件；
它们不能从所用 R278 原式来源被暗中带入。

这些完整强 blocks 可按 R263 加到已固定的弱圆上，但任何后继支付都须把新增实际面积及 $\Psi$ 成本一起计入。
同一微包内部的 primitive 仍有真实左尾；有限矩匹配不是局部无尾的声明。
共同正物理区间及后继可能需要的完整反射，按 R354 的真实几何选择规则在全部有限 supports 选定之后处理；不扩大任意先前冻结的窄区间。

本稿不授整个72面积、第四 period、同一 gauge 的 joint ruling 或整个第四阶已解。
新的内容是可复用的真三母正则性、两个实际形状坐标，以及一个含真实历史的三维正四次锥。
