# R353：真实有序尾与三个正中心支付 Y–W 的完整第一外矩

日期：2026-11-15。**完整有限纸面建设性证明；没有执行求积、符号程序、序列枚举、profile 扫描、人工检查或研究计算。**

[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md) 已在同一个弱单 hook 圆上支付四个 Gaussian pair 的全部三外矩。本稿继续剩余 $Y$–$W_*$ pair，支付它的**整个第一外矩**，保全部12个旧外矩、$\Psi$、三条 directed 行和指定完整一层。

原 $Y$–$W_*$ 跨核是 $b\mathbf K_3$，并不为零。新的证明先保留它，计算完整 nonlegal self，再把原普通／伴随、居中／重排四种真实原型放入三个正中心。严格正核来自两个真实一维概率分布的共同均值和第二矩；不是把 self、ordered tail 或位置矩当作独立输入。

主要来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md)、[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md)、R349。

## 1. 原规范与本稿新增目标

固定原真实几何 $M=0$、$T=\kappa_H\mathfrak H$、$\kappa_H\ne0$，共振端芽及同一右锚。仍用
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\ Y=\Phi_{p_2},
$$
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e},\quad
0<t=\kappa^2<1/100.
\tag{1}
$$
置 $k_*=db/2-ea\ne0$。特别 $b\ne0$。

对 $u=\phi_\theta=f\cos\theta+g\sin\theta$、
$D=f\odot f-u\odot u$，保留原
$$
\mathcal M_j=I_j(u,[W_*,P](u;D)),\quad
\mathcal A_j=I_j(u,[Z_*,P](u;D)),
$$
$$
\mathcal B_j=I_j(u,[Z_*,W_*](u;D)),\quad
\mathcal C_j=I_j(u,[Z_*,Y](u;D)),
$$
并记
$$
\mathcal P_j=I_j(u,[P,Y](u;D)),\qquad
\mathcal D_j=I_j(u,[W_*,Y](u;D)).
\tag{2}
$$
本稿新增 $\mathcal D_1=0$，对全部相位成立。
原 Gaussian pair $(1,-2)$ 与之仅差非零常数 $-\zeta$。

R259 原跨核为
$$
\Gamma_{R,Y,j}=0,\qquad
\Gamma_{S,Y,j}=\mathbf K_{3,j},
$$
$$
\mathbf K_3(\mathbf m,\mathbf n)
=\left(\frac{m_0n_2}{2}-m_1n_1,
-\frac{m_2n_1}{2},-\frac{m_2n_2}{2}\right).
\tag{3}
$$
所有 $I_2$ 始终包含 $2u'w'$。

## 2. 两条完整第一 self

令 $u$ 为任意实紧 profile，$v=u'$、$r=u''$，
$$
A=J(r^2),\quad B=J(xr^2),\quad
C=J(x^2r^2+2v^2),\qquad \mu_j=I_j(u,u).
$$
不要求 $\mu_j=0$。定义 $S_{X,Y,j}=2I_j(u,[X,Y](u;u^2))$。

准确有
$$
\boxed{
S_{R,Y,1}
=-S_{L,Y,0}-\frac1{12}\int(v-xr)^4,
}
\tag{4}
$$
其中 $S_{L,Y,0}$ 为 R270 的完整原式。
另一条为
$$
\boxed{
\begin{aligned}
S_{S,Y,1}={}&
\int\left(2xuvr^2-x^2v^2r^2-x^2ur^3
+x^3vr^3-\frac5{24}x^4r^4\right)\\
&+\frac12\int xCr^2-\frac{\mu_1\mu_2}{2}.
\end{aligned}}
\tag{5}
$$
(5)的 primitive 和左尾均未删。

### 2.1 原 local 变分及 Green

原 cubic 为
$$
F_{R,1}=\int(xr^3/3-vr^2),\qquad
F_{S,1}=\int xr^3/3,
$$
$$
F_{Y,1}=\int(x^2ur^2-x^3vr^2+x^4r^3/6+2uv^2-2xv^3/3).
\tag{6}
$$
原输出是
$$
R(u,u)=v^2+xA,\quad R'=2vr+A-xr^2,\quad R''=2(v-xr)r',
$$
$$
S(u,u)=B,\quad S'=-xr^2,\quad S''=-r^2-2xrr'.
$$
$Y,Y',Y''$ 用 R349(7) 的完整原式。

对 $R$，$D_{\rm loc}F_{R,1}[Y]$ 中的原 $C$ 项是
$\int vrC=\frac12\int v^2(x^2r^2+2v^2)$；
$D_{\rm loc}F_{Y,1}[R]$ 的原 $A$ 项是
$\int4uvA=2\int u^2r^2$。
两者均只使用紧 outer 的 IBP。
剩余含 $r'$ 的差为
$$
5x^3ur^2r'-7x^4vr^2r'-6x^2uvrr'
+6x^3v^2rr'+\frac32x^5r^3r'.
$$
分别按 $(r^2)'/2,(r^3)'/3,(r^4)'/4$ 积分后，完整 local 结果是
$$
\int\left[
-u^2r^2+4xuvr^2-x^2ur^3+\frac53x^3vr^3
-\frac72x^2v^2r^2-\frac7{24}x^4r^4-\frac{v^4}{6}
\right].
\tag{7}
$$
用 $\int xv^3r=-\int v^4/4$ 展开 $(v-xr)^4$，即为(4)。

对 $S$，原 primitive 差为
$$
-\frac12\int xCr^2-\int B(x^2r^2+2v^2)
=-\mu_1\mu_2+\frac12\int xCr^2.
\tag{8}
$$
它使用 $B'=-xr^2,C'=-(x^2r^2+2v^2)$ 和真实左值。
其余含 $r'$ 的差是
$$
5x^3ur^2r'-5x^4vr^2r'+\frac32x^5r^3r',
$$
完整 IBP 给(5)第一行。

原 $I_1$ Green 为
$$
g_1(X,Y)=x(X'''Y-X''Y'+X'Y''-XY''')+X''Y-XY''.
$$
左尾 $R=\mu_0x,S=\mu_1,Y=-\mu_2x^2/4$ 给
$$
G_1(R,Y)=0,\qquad G_1(S,Y)=\mu_1\mu_2/2.
\tag{9}
$$
所以(8)仍剩 $-\mu_1\mu_2/2$，恰为(5)。
这些是完整 self，不是只在合法复输入上推得的逐包近似。

## 3. 第零 self 与真实中心导数

同一原变分给
$$
\boxed{
S_{R,Y,0}=\int\left(
4uvr^2-2xur^3+5x^2vr^3-7xv^2r^2-\frac76x^3r^4
\right),
}
\tag{10}
$$
$$
\boxed{
S_{S,Y,0}
=\int\left(
2uvr^2-2xur^3+3x^2vr^3-2xv^2r^2-\frac56x^3r^4
\right)
+\frac12\int Cr^2-\frac{\mu_1^2}{2}.
}
\tag{11}
$$
核尾的短途径是 $F_{R,0}=F_{S,0}=-\int r^3/3$：
$R$ 的 primitive 总和 $\mu_0\mu_2/2$ 与原 Green
$-\mu_0\mu_2/2$ 抵消；
$S$ 保留 $\frac12\int Cr^2-\frac12\mu_1^2$，其 Green 为零。

将实际平移输入拉回，$C^{(s)}=C+2sB+s^2A$、
$\mu_1^{(s)}=\mu_1+s\mu_0$、
$\mu_2^{(s)}=\mu_2+2s\mu_1+s^2\mu_0$。
由(4)—(11)直接得到
$$
\boxed{
\partial_sS_{R,Y,1}(T_su)=S_{R,Y,0}(T_su),\qquad
\partial_sS_{S,Y,1}(T_su)
=S_{S,Y,0}(T_su)-\frac{\mu_0^{(s)}\mu_2^{(s)}}2.
}
\tag{12}
$$
末项正是原完整 $S_{P,Y,1}$。

跨核同时满足
$$
\partial_sK_{3,1}(\mathbf m^{(s)},\mathbf n^{(s)})
=K_{3,0}(\mathbf m^{(s)},\mathbf n^{(s)})
+K_{1,1}(\mathbf m^{(s)},\mathbf n^{(s)}).
\tag{13}
$$
因此对完整不交 rank-one 微包 block，
$$
\boxed{\partial_\xi\mathcal D_1=\mathcal D_0+b\mathcal P_1.}
\tag{14}
$$
这是包含全部 self 和 ordered history 的真实中心式。
本稿只对新增强 blocks 使用它；原弱 rank-two 核心不被套入(14)。

## 4. 保 C0 真零的原四变量族

本稿重新消费 R270 的完整四变量 IFT，而非只取它的零宽母形。
先选同源 TM3 母包／伴随，固定小正母宽 $h_m$。
在原正则母根上固定
$$
\mathcal H=0,\qquad \mathcal F_\kappa=0,\qquad\mathcal J=0.
$$
主变量 $(\alpha,\gamma,s,z)$ 解原四式
$$
\delta^3L_c=0,\quad
\delta(M_c+3L_c/\xi)=0,\quad
\mathcal F_\kappa=0,\quad
\mathcal C_0=0.
\tag{15}
$$
最后一行使用 R270(17)的全 finite-copy 公式，不删 $\delta^2$ 项。
R270 原四行 Jacobian 可逆；每个最后真实中心、排序与有限间距固定以后，充分小的正 $\delta$ 给准确根。

$\delta=0$ 的共同 $\alpha_0$ 是
$$
p(\alpha)=256\alpha(1-\alpha)^5-(5-\alpha)=0
$$
的原唯一简单根。
由于 $(11/20)^5>1/20$，有
$p(9/20)>144/25-91/20>0$，而 $p(1/2)<0$；
故
$$
9/20<\alpha_0<1/2,\qquad
q_0=\frac1{16(1-\alpha_0)^2}>\frac15.
\tag{16}
$$
实际参数在 $\delta>0$ 时随同一个真 IFT 变化，不将它们冻结在极限。

每个原型准确满足
$$
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2),\quad
\mathcal B_0=\mathcal C_0=0.
\tag{17}
$$
它保 full strong hook、三矩、八副本完整第三及十二副本全部 odd，
且 $\Psi=\psi\sin^2\theta,\psi>0$。
$\mathcal B_1,\mathcal B_2,\mathcal C_1,\mathcal C_2,\mathcal D_1$ 均先保真实值。
不同最后中心的根可以不同；它们都趋向同一个正母根。

## 5. 两种真实排序和全部尾的有限归一

令 $n=2^{11}$、$\beta=(5-\alpha)/(1-\alpha)$、
$a_c=q(1-\alpha)$。
使用 R269/R343 的两个实际次序 $\rho=0,20$，
$$
t^L_{k,l}=64A(k-(n-1)/2)+A(l-31.5),
$$
$$
t^H_k=B_\rho(k-(n-1)/2)+\rho A\sigma_k,
$$
$$
B_\rho^2=
\frac{A^2((64n)^2-1)-12\nu(1-q^2)-12\rho^2A^2}{n^2-1}.
\tag{18}
$$
完整 eight/twelve copy 的实际位置、四次权和镜像中心都包含在内。
两排序各有普通与伴随版本。

令 $v_\delta$ 为当前实际母包，$m_\delta=I_0(v_\delta,v_\delta)$，
并记 $m_*=\lim_{\delta\downarrow0}m_\delta>0$、$a_{c,*}=q_0(1-\alpha_0)$。
$\mathcal W$ 为完整复制的四次权和。以下始终以固定极限正数
$$
\mathcal N_*=\mathcal W n a_{c,*}m_*^2
$$
归一；完整有限宽公式中的母矩仍是 $m_\delta$。取极限的顺序只用于证明实际开性：
先对每个有限 $A$ 用(15)的标量 $\delta\downarrow0$ 延拓，再令归一系数的 $A$ 增大；实际选择仍是先固定有限 $A$，然后选有限正 $\delta$。

原 $2\mathcal P_0$ 的 sine-four 系数和 R271 的完整有序量满足
$$
\frac{E_{04}^{P,0}}{\mathcal N_*\delta A}\longrightarrow s_\rho,\qquad
\frac{\mathcal Wm_\delta^2\delta U_{01}}{\mathcal N_*\delta A}
\longrightarrow u_\rho,
\tag{19}
$$
$$
s_\rho=10928q_0-(32q_0+1)\rho^2,
$$
$$
u_\rho=(64q_0+1)
\left\{\frac{16}{3}D_\rho+\frac32\rho^2-512\right\},
\quad
D_\rho=\frac{4095-12\rho^2}{b_\rho+64},
$$
$$
b_\rho=\sqrt{4096+\frac{4095-12\rho^2}{n^2-1}}.
\tag{20}
$$
这些来自原非紧 self、方差和真实 prefix 求和；
母包的 $\Delta,\nu$ 和 local 余量仍在完整公式中，除以 $A$ 才趋零。

R343 已逐原式证明
$$
z_\rho:=-s_\rho-u_\rho,\qquad
z_0>0>z_{20}.
\tag{21}
$$
它只需要 $q_0>1/5$，并不要求把 $\alpha$ 固定为 $9/20$。
同时 $s_0>0,u_0<0$，$s_{20}<0,u_{20}>0$，所以
$$
\boxed{m_\rho:=s_\rho-u_\rho,\qquad m_0>0>m_{20}.}
\tag{22}
$$

把 $2\mathcal B_1/k_*$ 的两个 even 坐标改为
$(E_{22}-E_{04},E_{04})$。
每种排序的普通／伴随列，其归一极限记为
$$
(p_{\rho,O},z_\rho),\quad (p_{\rho,C},z_\rho).
$$
原完整 primitive 公式 R343(17)—(19)给
$$
\boxed{p_{\rho,O}<0<p_{\rho,C}.}
\tag{23}
$$
普通版的 $A$ 系数由真 ordered sum 为负，伴随版为正；不是对一个 formal list 反序。
原 local 部分由准确方差消去间距依赖后仅为有界余量。

## 6. 新 D1 的完整归一，不遗漏 centre-zero 项

给出(19)怎样进入 $\mathcal D_1$，避免只以 principal 猜测第六行。

对一个固定 even 母包和一个实际排序，取
$$
\mathcal K=V_2-\frac25N,\qquad
V_2=\int(v_\delta')^2(v_\delta'')^2,\quad
N=\int yv_\delta'(v_\delta'')^3.
$$
为免与§2的原 primitive 混淆，本节另记
$$
C_4=\int(v_\delta'')^4,\quad
X_2=\int y^2(v_\delta'')^4,\quad
U_3=\int v_\delta(v_\delta'')^3,
$$
$$
\mathcal J=3V_2+U_3-2N,\qquad
\mathcal L=X_2-\frac83N+\frac43U_3+V_2,
$$
以及 $\nu=I_2(v_\delta,v_\delta)/m_\delta$、
$\Delta=\iint|y-z|(v_\delta''(y))^2(v_\delta''(z))^2\,dy\,dz$。
单包仍为真实 $w^{3/2}v_\delta((x-\xi)/w)$。
本节每条有限宽身份使用同一个实际 $v_\delta$，以及实际 $q,a_c$；
只在§7归一极限时才取它们的极限值。
使用中心导数时先固定这整个母形与内部相对布局，再平移完整原型；
不沿着四变量 IFT 的未知参数对中心微分。
R349 的准确母身份
$X_2-C_4\nu=\frac85N-\frac{16e}{5(d+7e)}\mathcal J$
连同(10)、(11)，给整个 ordinary block 的
$$
E_{04}^{D,0}(\xi)
=\xi\{b E_{04}^{P,0}+K\delta(1-q^2)\mathcal G\},
\tag{24}
$$
其中 $K=64na_c\mathcal W$，且
$$
\mathcal G=(b-a)\mathcal K
-\left\{\frac{2a(5d+7e)}{5(d+7e)}
+\frac{2b(5d-e)}{15(d+7e)}\right\}\mathcal J.
\tag{25}
$$
这是同一个实际母包的值，不是额外可调坐标。

核(24)的 primitive 步骤是：对 even 单包，
$$
\int r^2J(x^2r^2+2v^2)
=\frac{\mu_0\mu_2}{2}+\frac{\xi w\Delta}{2},
$$
再将真实 $\mathbf K_{3,0}$ 配对全加回。
其 sine-four 正好给
$\xi E_{04}^{P,0}-K\delta\xi(1-q^2)(C_4\nu-\mathcal L)$；
全部 $\nu w^2$ 和 self 的 $\Delta/4$ 保留。
余 local 经方差化成(25)。
伴随版在 $\theta=\pi/2$ 的 local quadratic 数据及 inner $D$ 完全相同，所以(24)也准确适用。

由 R271 原式
$$
E_{04}^{P,1}=-\mathcal Wm_\delta^2\xi\delta U_{01}
$$
和(14)，得到
$$
\begin{aligned}
E_{04}^{D,1}(\xi)
={}&\frac{\xi^2}{2}
\{b(E_{04}^{P,0}-\mathcal Wm_\delta^2\delta U_{01})
+K\delta(1-q^2)\mathcal G\}\\
&+\delta^3\Theta_{\rho,O/C}.
\end{aligned}
\tag{26}
$$
$\Theta$ 是完整辅助中心零值。它含原 self、ordered tail 和所有 copy 方差；在固定有限 $A$ 后有限且连续。
同中心零的全式权为 $\delta^3$，不需要把它强行设零。
所有原 copy 的中心偏移也收入这个准确常数。

对 pure 差，用合法复 $q=f+ig$。三复矩为零；原
$S_{P,Y,1}(q)=0$。由(10)、(11)可直接核
$$
\partial_\xi S_{R,Y,0}
=\int(-2ur^3+10xvr^3-7v^2r^2-\tfrac72x^2r^4),
$$
$$
\partial_\xi S_{S,Y,0}
=S_{P,Y,0}
+\int(\tfrac{10}{3}xvr^3-v^2r^2-\tfrac23ur^3-\tfrac32x^2r^4).
\tag{27}
$$
全角 quartic 张量和实际方差使这些 local 实部的中心高次项准确消去，余下 $O(\delta)$ 部分不随 $A$ 增长。整个 block 在辅助中心反射，$E^{D,0}_{22}-E^{D,0}_{04}=0$。因此(14)给
$$
E^{D,1}_{22}-E^{D,1}_{04}
=\frac{b\xi^2}{2}\operatorname{Re}S_{P,Y,0}(q)
+\xi^2O(\delta)+\delta^3\widetilde\Theta_{\rho,O/C}.
\tag{28}
$$
这里 $O(\delta)$ 是上述明确 local 四次密度的实际值，而不是假设未识别 history 低阶；固定母邻域后其除以 $\delta$ 有界且与 $A$ 无关。

R341/R343 的准确 pure 身份又给
$$
\operatorname{Re}S_{P,Y,0}
=-\operatorname{Re}S_{Z_*,W_*,1}/k_*+O(\delta),
\tag{29}
$$
同样由真实方差保证余 local 不增长。
所以(26)—(29)及(19)共同决定下一节新两行。有限 $\Theta,\widetilde\Theta$ 在先固定 $A$ 后随 $\delta^2$ 消退，未被当成原式零。

## 7. 十二实际列的六行极限

R343 完整平移给
$$
\mathcal B_2(\xi)=\xi(2\mathcal B_1+\chi_\kappa\mathcal R_2),
$$
其中 $\mathcal R_2$ 是原真实 self，$O(\delta)$ 且不随 $A$ 增长。
结合前节，先将每个完整 $2\mathcal B_1,2\mathcal B_2,2\mathcal D_1$
角函数写出其 raw even 系数 $E_{22},E_{04}$；六个真实坐标取
$$
\left(
\frac{E^{B,1}_{22}-E^{B,1}_{04}}{k_*},
\frac{E^{B,1}_{04}}{k_*},
\frac{E^{B,2}_{22}-E^{B,2}_{04}}{k_*},
\frac{E^{B,2}_{04}}{k_*},
\frac{2(E^{D,1}_{22}-E^{D,1}_{04})}{b},
\frac{2E^{D,1}_{04}}{b}
\right).
$$
这六个数再除共同正量
$\mathcal N_*\delta A$，在(19)的有序标量极限下，列准确趋于
$$
\boxed{
v_{\rho,\pm}(\xi)
=(p_{\rho,\pm},z_\rho,\,
2\xi p_{\rho,\pm},2\xi z_\rho,\,
-\xi^2p_{\rho,\pm},\xi^2m_\rho).
}
\tag{30}
$$
这些坐标缩放都是固定非零实数，不改变 rank 或正锥是否为全空间。
未对实际 profile 取零宽；下一节只用极限的严格余量一次选择有限参数。

## 8. 正半轴三个中心给严格正核和 rank6

由(21)、(22)，
$$
r_\rho=m_\rho/z_\rho>0.
$$
先为两种排序各选三个正中心和严格正概率。
要求两概率具有同一正均值 $c$，并令其第二矩满足
$$
r_0\,\mathbb E_+(\xi^2)
=r_{20}\,\mathbb E_-(\xi^2).
\tag{31}
$$
这可以明确完成：先任选两个大于 $c^2$ 的正数
$Q_+,Q_-$，使 $r_0Q_+=r_{20}Q_-$；
例如
$Q_+=2c^2(1+r_{20}/r_0)$、
$Q_-=2c^2(1+r_0/r_{20})$。
给定 $V=Q-c^2>0$，在三个正点 $c/2,c,T$ 上取
$$
p_T=\frac{V}{(T-c)(T-c/2)},\quad
p_{c/2}=\frac{2V}{c(T-c/2)},\quad
p_c=1-p_T-p_{c/2}.
\tag{32}
$$
有限 $T$ 足够大时三概率皆严格正，均值为 $c$、第二矩为 $Q$。
可分别用于两排序。

在每个中心，先由(23)取 ordinary/companion 的严格正概率，使 $p$ 坐标为零。
再将两排序的中心概率分别除以 $z_0$ 和 $|z_{20}|$。
这样全部12列都有严格正权：
第一、第三、第五行逐中心为零；
第二行按两组总质量抵消；
第四行按共同均值抵消；
第六行由(31)抵消。
故(30)有一个**全分量严格正**的 kernel。

rank6 也直接可核。在 $\rho=0$ 的三个不同中心，
每对 ordinary/companion 的差给
$(1,2\xi,-\xi^2)$ 的三个纯 p 行；
每对的正配对给
$(1,2\xi,r_0\xi^2)$ 的三个 z 行。
两组三阶 Vandermonde 都非零，因此六行独立。

上述“同中心两列”只用于构造一个明确的极限矩阵。
现在将全部12个中心分别作足够小的固定扰动，使它们互异且仍为正。
选择一个原非零六列 minor，仅用它纠正 kernel 的小残差；
rank6 与所有权的严格正性保持。
这一步之后，各最后中心固定。

再先取充分大的**有限** $A$，使 $\delta=0$ 的准确归一列接近(30)；
随后取共同充分小的**有限正** $\delta$，并在每个固定中心独立解(15)。
真实正宽包络此时严格分离，母参数、全部尾和中心值都已恢复。
同一个 minor 继续给真实矩阵的严格正核。因此
$$
\boxed{
\operatorname{cone}_+\{(\mathcal B_1,\mathcal B_2,\mathcal D_1)
\text{的12个真实列}\}=\mathbb R^6,
}
\tag{33}
$$
且每一列的 $\mathcal C_0$ 准确为零。
没有把只在 $\delta=0$ 的 profile 当成实际原型，也没有略过 finite-copy 余项。

## 9. 与三个旧 C 目标联合成真实十二维正锥

记(33)的实际矩阵为 $M_6$。
它的 $\mathcal C_1,\mathcal C_2$ 值保为原值；
$\mathcal C_0$ 每列准确为零。

先加入 R346 的四个真实 $\mathcal C_0$ 正锥原型。
将它们作大有限正伸缩 $H_0$、第四幅度乘 $H_0^3$。
原完整权是
$$
\mathcal B_1:-5,\quad\mathcal B_2:-4,\quad
\mathcal D_1:-3,\quad\mathcal C_0:-3,\quad
\mathcal C_1:-2,\quad\mathcal C_2:-1,\quad\Psi:-7.
\tag{34}
$$
所以它们的 $\mathcal B_1,\mathcal B_2$ 趋零，
$\mathcal D_1$ 保有限真实值，$\mathcal C_0$ 列固定。
在八行 $(\mathcal B_1,\mathcal B_2,\mathcal D_1,\mathcal C_0)$ 上，极限为
$$
\begin{pmatrix}M_6&D_{\rm new}\\0&C_0^{\rm new}\end{pmatrix}.
\tag{35}
$$
$D_{\rm new}$ 的新 $\mathcal D_1$ 不能删除；但 $M_6$ 的正锥为全 $\mathbb R^6$。
先选 $C_0^{\rm new}$ 的严格正 kernel，再由 $M_6$ 正锥消其上部真实值并加一个正 kernel，便得到(35)的严格正 kernel。
它满秩8，故一个有限 $H_0$ 已给真实八行结论。

随后加入 R348 的四个 $\mathcal C_1$ 原型，第四幅度乘新的大有限 $H_1^2$。
全部旧八行趋零，新的 $\mathcal C_1$ 两行固定；
旧库的 $\mathcal C_1$ 值仍保留。
原 block-triangular 正核论证遂给真实十行。

最后加入 R349 的四个 $\mathcal C_2$ 原型，第四幅度乘新的大有限 $H_2$。
其余十行趋零，得到一个满秩12、含严格正 kernel 的实际24列矩阵
$$
\boxed{
M_{12}:
(\mathcal B_1,\mathcal B_2,\mathcal D_1,
\mathcal C_0,\mathcal C_1,\mathcal C_2),\qquad
\operatorname{cone}_+(M_{12})=\mathbb R^{12}.
}
\tag{36}
$$
每次都先固定前面的真实有限列，再取新的有限伸缩。
这些原型的完整支撑都在正半轴，故同一次有限伸缩还可使新一组支撑严格位于全部旧组的右方；各组内部的相对位置和尾项不再改变。
没有只由线性 span 推断正四次可达，也没有假定旧第零 C 值在新增原型中自动为零。

## 10. 同一个最终弱圆的原残差与 Ψ 成本

从 R349 最后强控制器以前接入：
原弱核心、全部旧中心与补矩已经固定，
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=\mathcal C_j=0
\quad(j=0,1,2),\qquad
\Psi=-\Delta_0\sin^2\theta,\quad\Delta_0>0.
\tag{37}
$$
记其当前真实 $\mathcal D_1$ even 残差为 $r_D\in\mathbb R^2$。

固定(36)的严格正 kernel $k$ 和一个实右逆 $R_{12}$。
把整组新原型共同正伸缩 $S$，第四幅度取 $S^5c_i(S)$，
$$
c(S)=k+R_{12}(0,0,-r_D/S^2,0,0,0).
\tag{38}
$$
各块的实际缩放依(34)为
$1,S,S^2,S^2,S^3,S^4$。
对足够大的有限 $S$，$c(S)>0$ 且有界，原矩阵身份准确使
$$
\Delta\mathcal B_1=\Delta\mathcal B_2
=\Delta\mathcal C_0=\Delta\mathcal C_1
=\Delta\mathcal C_2=0,\qquad
\Delta\mathcal D_1=-r_D.
\tag{39}
$$
各原型自身的旧 $\mathcal M_j,\mathcal A_j,\mathcal B_0$ 零保持。

新增 $\Psi$ 全成本是
$$
S^{-2}\sum_i c_i(S)\psi_i\,\sin^2\theta.
\tag{40}
$$
有限 $S$ 可使其小于 $\Delta_0/2$，并同时把所有新正包络移到旧固定 profiles 右方。
旧弱中心不动；没有在面积支付后整体平移。

最后只在原同 $F^\star$ 强控制器中求有限频率的完整正核根，支付三条 directed 行并使 $\Psi=0$。
该控制器自己的全部72面积准确为零，原固定纤维保这些值；
所以它也保(39)。
所有 complete blocks 的 inner $D$ 三矩为零，inter-block cross 精确消失；
各 block 内部的原有序尾则已经完整计入(3)—(29)。

## 11. 有限选择次序与尚未支付的门

固定原几何与负余基线后，先取 R270 的真母根；
选择两个真实排序、ordinary/companion 四类和原完整复制；
用(30)—(32)固定有限正中心，再分开重合的辅助中心；
取有限 $A$，其后才在所有最后中心选择共同有限正 $\delta$ 并解原四 IFT。
固定这12个实际列后，依次选有限 $H_0,H_1,H_2$，
再选有限 $S$ 与实际正四次权；
最后在已固定的强区求有限 $N$。

共同有限正区间依 R105/R114/R271 的原范围，在全部有限原型与几何包络一次确定，保右锚与 collars。
原算子和原 metric 的新 seed 随最终构造一次固定；
不对一个任意先前冻结窄区间或旧固定圆承诺这些改动。

本稿完整增加
$$
\boxed{
\mathcal D_1(\theta)=0\quad\text{对全部 }\theta,
}
$$
并保持 R349 的全部12个旧外矩、三矩、完整三阶、
$\Psi=F_0=F_1=F_2=0$ 和原指定一层系数。

仍未支付的是 $Y$–$P$ 三个外矩及 $Y$–$W_*$ 的第零、第2矩。
本稿不宣它们独立，不宣 canonical 第四 period 或同一 gauge 的 joint 已解。
尤其新模块的 $Y$–$P$ 第一矩保为真实代价，未假定它保持某个后续另行选择的零；它当前尚不属于(37)的已付清单。
