# R348：真实平移与原 Green 自项支付正负一面积的完整第一外矩

日期：2026-11-15。**完整纸面构造。** 未执行符号程序、求积、profile 扫描、人工测试或研究计算。

[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md) 已在三个负 Gaussian pair 的完整九矩之外，支付正方向与 $B_{-1}$ 之间的第零外矩。本稿增加这个 pair 的**全部相位第1外矩**。所有旧九矩、新第零矩、原 $\Psi$ 与三条 directed 行在同一个最终弱圆上保持。

先从原算子给出完整平移：它确实引入与 $Y$ 配对的其他方向及未付的 $[P,Y]$，不能因第零外矩已零就使用普通外矩平移。随后在新增的强 rank-one 原型上，另用完整 nonlegal self 和真实 Green 尾证明一个准确特化：其第一 self 对实际共同中心的导数是第零 self 的两倍。这个特化给两个真实符号，再与 R346 六目标正锥联合，完成新门。

主要来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md)、R346 及 [R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 同一原问题与新增的完整门

保持 R346 的同一真实有限几何与弱单 hook：
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0.
$$
共振端芽仍为
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\qquad
0<t:=\kappa^2<1/100.
$$
取
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\ V=\Phi_{p_1},\
T_1=\Phi_{t_1},\ Y=\Phi_{p_2}.
$$
这里 $T_1$ 是原二次算子，不是几何第三张量。记
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
原 $B_1=-\kappa h_eY$、$B_{-1}=Z_*$，所以 $[Z_*,Y]$ 与原 $A_{1,-1}$ 的三个外矩只差同一个非零因子。

仍令
$$
u=f\cos\theta+g\sin\theta,\qquad D=f\odot f-u\odot u,
$$
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\quad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_j=I_j\{u,[Z_*,W_*](u;D)\},\qquad
\mathcal C_j=I_j\{u,[Z_*,Y](u;D)\}.
\tag{2}
$$
$Jq(x)=\int_x^{r_*}q$，所有原函数用同一右锚。$I_2$ 始终包含 $2u'w'$。

本稿的结论是同一个最终圆上
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=0\ (j=0,1,2),\qquad
\mathcal C_0=\mathcal C_1=0,\qquad
\Psi=F_0=F_1=F_2=0,
}
\tag{3}
$$
全部相位成立。$\mathcal C_2$ 不由本文支付。

## 2. 一般弱核心的真实平移确实含其他 pair

令 $T_su(x)=u(x-s)$，将平移后的原场拉回原坐标。原 primitive 按
$$
J_0\mapsto J_0,\quad J_1\mapsto J_1+sJ_0,\quad
J_2\mapsto J_2+2sJ_1+s^2J_0
$$
变换。这些式子使用实际共同右零 collar，没有添加自由常数。

原八式直接给
$$
Z_*^{(s)}=Z_*+sZ_1+s^2Z_2,\qquad
Z_1=(e-d/2)R+(2e+d/2)S,\quad Z_2=3eP/2,
$$
$$
\boxed{
Y^{(s)}=Y+sY_1+s^2Y_2+s^3Y_3+s^4Y_4,
}
$$
$$
Y_1=2V-T_1/2,\quad Y_2=L-U,\quad
Y_3=-(R+S)/2,\quad Y_4=-P/4.
\tag{4}
$$
例如 $Y$ 的原式
$-xu^2+x^2uu'-x^3u'^2/2-x^2J_2/4$
连同上述 $J_2$ 变换逐次给(4)，而不是只平移外矩权。

定义完整三次括号
$$
\begin{aligned}
K_0&=[Z_*,Y],\\
K_1&=[Z_*,Y_1]+[Z_1,Y],\\
K_2&=[Z_*,Y_2]+[Z_1,Y_1]+[Z_2,Y],\\
K_3&=[Z_*,Y_3]+[Z_1,Y_2]+[Z_2,Y_1],\\
K_4&=[Z_*,Y_4]+[Z_1,Y_3]+[Z_2,Y_2],\\
K_5&=[Z_1,Y_4]+[Z_2,Y_3].
\end{aligned}
\tag{5}
$$
第6项 $[Z_2,Y_4]=0$ 仅因两者都是 $P$ 的倍数。
于是对任意实际紧 profiles，完整平移为
$$
\boxed{
\mathcal C_1^{(s)}
=\sum_{\ell=0}^5s^\ell
\left[
I_1\{u,K_\ell(u;D)\}
+sI_0\{u,K_\ell(u;D)\}
\right].
}
\tag{6}
$$
第二矩同样是
$$
\mathcal C_2^{(s)}
=\sum_{\ell=0}^5s^\ell
\left[I_2(u,K_\ell)+2sI_1(u,K_\ell)+s^2I_0(u,K_\ell)\right],
\tag{7}
$$
其中各 $K_\ell$ 的 inner 槽仍为原 $D$。

特别，$K_2$ 包含 $(3e/2)[P,Y]$，$K_1$ 包含 $R/S$ 与 $Y$ 的括号。未付的 $Y$–$P$、$Y$–$W_*$ 方向及其他完整组合不能由旧九矩删去。本文不对原弱核心使用
$\mathcal C_1^{(s)}=\mathcal C_1+s\mathcal C_0$，也不把下面的单包特化推广到任意弱 rank-two pair。

## 3. 两个完整 nonlegal 第一 self

令 $u$ 为任意实紧 profile，$v=u'$、$r=u''$、$t_3=u'''$，
$$
A=J(r^2),\quad B=J(xr^2),\quad
C=J(x^2r^2+2v^2),\qquad \mu_j=I_j(u,u).
$$
不要求任何单包 $\mu_j$ 为零。原二次输出与导数是
$$
Lu=uv-\frac{xv^2}{2}-\frac{x^2A}{4}+\frac C4,\qquad
(Lu)'=(u-xv)r-\frac{xA}{2},
$$
$$
(Lu)''=(u-xv)t_3-\frac{xr^2+A}{2},
$$
$$
Uu=xv^2+xB+\frac C2,\qquad
(Uu)'=2xvr+B-\frac32x^2r^2,
$$
$$
(Uu)''=(2xv-3x^2r)t_3+2vr-2xr^2.
\tag{8}
$$
这里 $Xu=\Phi_X(u,u)$。

R271 的原 cubic 密度给
$$
F_{Y,1}(u)=
\int\left(x^2ur^2-x^3vr^2+\frac{x^4r^3}{6}
+2uv^2-\frac23xv^3\right).
\tag{9}
$$
而 $F_{L,1},F_{U,1}$ 的原密度分别是 $v^2r,-2v^2r$，都是全导数。
沿(8)这些可能带尾的方向仍应使用 R259 的 local 变分与 Green 项；不把 $u+\tau Lu$ 或 $u+\tau Uu$ 冒称为紧输入族。

定义
$$
S_{X,Y,1}(u)=2I_1\{u,[X,Y](u;u\odot u)\}.
$$
完整结果为
$$
\boxed{
S_{L,Y,1}(u)=\int\left[
2x(u-xv)^2r^2+\frac23x^3(u-xv)r^3+\frac{x^5r^4}{12}
\right],
}
\tag{10}
$$
$$
\boxed{
\begin{aligned}
S_{U,Y,1}(u)=\int\big[
&-2xu^2r^2+8x^2uvr^2-6x^3v^2r^2-2x^3ur^3\\
&+\frac83x^4vr^3-\frac5{12}x^5r^4
-\frac43xv^4+\frac83uv^3\big].
\end{aligned}}
\tag{11}
$$

### 3.1 原 local 变分及全部 primitive 项

(9) 密度的三个偏导为
$$
F_u=x^2r^2+2v^2,\quad
F_v=-x^3r^2+4uv-2xv^2,\quad
F_r=2x^2(u-xv)r+\frac{x^4r^2}{2}.
\tag{12}
$$
将 $Lu,(Lu)',(Lu)''$ 代入
$\int(F_uw+F_vw'+F_rw'')$。
所有 $A$ 项的系数准确为
$$
\frac{x^2v^2}{2}-2xuv-x^2ur+x^3vr
=\left(-x^2uv+\frac{x^3v^2}{2}\right)'.
$$
用 $A'=-r^2$ 积分后，这一项与原 local 的
$x^2uvr^2-x^3v^2r^2/2$ 抵消。
$C$ 项为
$$
\frac14C(x^2r^2+2v^2)=-\frac14CC',
$$
故其完整积分是 $\mu_2^2/8$，没有设左尾为零。
其余 local 项用
$(u-xv)'=-xr$ 和 $rr'=(r^2)'/2$、
$r^2r'=(r^3)'/3$ 整理，得到
$$
D_{\rm loc}F_{Y,1}(u)[Lu]
=-S^{\rm loc}_{L,Y,1}(u)+\frac{\mu_2^2}{8},
\tag{13}
$$
其中 $S^{\rm loc}_{L,Y,1}$ 就是(10)右边。

对 $Uu$，$B$ 的完整系数为 $4uv$，所以
$$
\int4uvB=2\int xu^2r^2.
$$
$C$ 项为 $-CC'/2$，真实积分是 $\mu_2^2/4$。
余下 local 项同样用(8)及紧 outer 的普通 IBP，给
$$
D_{\rm loc}F_{Y,1}(u)[Uu]
=-S^{\rm loc}_{U,Y,1}(u)+\frac{\mu_2^2}{4}.
\tag{14}
$$
例如其中含 $t_3$ 的四项是
$$
4x^3(u-xv)vr t_3-6x^4(u-xv)r^2t_3
+x^5vr^2t_3-\frac32x^6r^3t_3,
$$
逐项积分后正给(11)所需的 $r^2,r^3,r^4$ 系数。
没有把 $A,B,C$ 的尾项藏进 local 余项。

### 3.2 Green 两项准确抵消

进入 self 的 $I_1$ concomitant，取左端值减右端值，为
$$
g_1(X,Y)=x(X'''Y-X''Y'+X'Y''-XY''')
+X''Y-XY''.
\tag{15}
$$
右 collar 全零。真实左尾为
$$
Lu=(-\mu_0x^2+\mu_2)/4,\quad
Uu=\mu_1x+\mu_2/2,\quad Yu=-\mu_2x^2/4.
$$
直接代(15)得到
$$
G_1(Lu,Yu)=\mu_2^2/8,\qquad
G_1(Uu,Yu)=\mu_2^2/4.
\tag{16}
$$
$D_{\rm loc}F_{L,1}[Yu]$、$D_{\rm loc}F_{U,1}[Yu]$ 是端点含 $v^2$ 的全导数，仍为零。故 self 等于
$-D_{\rm loc}F_{Y,1}[Xu]+G_1(Xu,Yu)$。
(13)、(14)与(16)准确相消，得到(10)、(11)。
这是两个真实非紧二次方向的完整证明。

## 4. 原第零 self 的真实中心导数

R270 的两条完整第零 self 是
$$
\begin{aligned}
S_{L,Y,0}=\int\big[
&u^2r^2-4xuvr^2+3x^2v^2r^2+x^2ur^3\\
&-\frac43x^3vr^3+\frac5{24}x^4r^4\big],
\end{aligned}
$$
$$
\begin{aligned}
S_{U,Y,0}=\int\big[
&-u^2r^2+8xuvr^2-9x^2v^2r^2-3x^2ur^3\\
&+\frac{16}3x^3vr^3-\frac{25}{24}x^4r^4-\frac23v^4\big].
\end{aligned}
\tag{17}
$$
将(10)、(11)的 local 密度只对显式 $x$ 求导，逐项就是(17)的两倍。因所有 profile 同时真实平移后，拉回坐标只将这些 local 密度中的 $x$ 换为 $x+s$，所以对任意紧单包有
$$
\boxed{
\frac{d}{ds}S_{X,Y,1}(T_su)=2S_{X,Y,0}(T_su),
\qquad X=L,U.
}
\tag{18}
$$
这不是对一般三槽面积的普通矩平移；它是(10)—(17)中全部原变分和尾项抵消后的准确身份。

对真实不交 rank-one 微包，
$\Gamma_{L,Y,j}=\Gamma_{U,Y,j}=0$ 对三个外矩都成立。
原尾作用也可直接核：$Y$ 的尾为 $-\mu_2x^2/4$，
$$
L(u,\operatorname{tail}Y)=Y(u,\operatorname{tail}L)
=\mu_2D_+u/8,
$$
$$
U(u,\operatorname{tail}Y)=Y(u,\operatorname{tail}U)
=\mu_2D_+u/4.
$$
因此完整微包和的 even 系数也满足(18)，使用的是真实 self 和，而非删除了一个非零跨核。

## 5. 全有限宽、全 copy 的新门

从 R346 §5 的真实 even 母小族取
$$
\mathcal F_\kappa(v_\tau)=0,\qquad
\mathcal J(v_\tau)/h=\tau,\qquad |\tau|<\tau_*,
\tag{19}
$$
其中 $h>0$ 已固定且有限。该族由 R270 的真 $(\gamma,z)$ minor 构造；所有形状常数同随 $v_\tau$ 变化。仍取两斜率
$$
1/3<\alpha<1/2,\quad
\beta=(5-\alpha)/(1-\alpha),\quad
q_0=[16(1-\alpha)^2]^{-1}.
$$
完整八／十二副本、真实居中排序与准确方差全部按 R346 放入。

写
$$
K=64na_c\mathcal W,\qquad a_c=q_0(1-\alpha),\qquad
A_\tau=(1-q_0^2)\Gamma_\kappa h\tau,
$$
$$
\Gamma_\kappa=\frac{\kappa(1-9t)(39t+1)}
{4h_e(81t+7)}\ne0.
$$
R346(18)的全部有限余项记为
$$
R_\tau=
a_4C(\overline M_{4,H}-\overline M_{4,L})
+\mathcal B_\kappa(\overline V_H-q_0^2\overline V_L)
+\mathcal D_\kappa(1-q_0^4).
\tag{20}
$$
它包含原所有真实 copy 中心与方差；固定实际相对布局后不随共同中心 $\xi$ 变化。

设 $E^{(j)}_{22},E^{(j)}_{04}$ 是 $2\mathcal C_j$ 的 even 系数。对 $j=0,1$，原两斜率 self 关系都给
$$
E^{(j)}_{22}=\alpha\beta E^{(j)}_{04},
\tag{21}
$$
因为逐包 $a_i^2(a_i^2-5b_i^2)=
\alpha\beta b_i^2(a_i^2-b_i^2)$，而原跨核为零。

已知准确第零式为
$$
E^{(0)}_{04}(\xi)=K\delta(A_\tau\xi^2+\delta^2R_\tau).
\tag{22}
$$
在辅助共同中心 $\xi=0$，even 母包、镜像中心与对称四次 copy 权使(10)、(11)的全部 even 系数为零：两密度每一项在母反射下都是 odd。原十二复制再清 odd 相位。因此 $E^{(1)}_{04}(0)=0$。

把(18)应用于这个完整实际 rank-one block，并积分(22)，得到
$$
\boxed{
E^{(1)}_{04}(\xi)
=2K\delta\left(\frac{A_\tau\xi^3}{3}
+\delta^2R_\tau\xi\right).
}
\tag{23}
$$
这保留了有限宽的整个常数 $R_\tau$；并非只取一个 leading 项。
辅助零中心只用于已经化为多项式的原式身份，实际全部支撑仍置于正区间。

## 6. 四个真实方向支付完整第一矩的二维目标

固定两个不同的 $\alpha_1,\alpha_2\in(1/3,1/2)$，各取实际
$\tau=\pm\tau_0\ne0$。先选有限间距及四个互不交的正中心区间，再选充分小的有限正 $\delta$。
由(23)，在每个已固定正中心，
$$
\frac{E^{(1)}_{04}}{2K\delta}
\longrightarrow
\frac{(1-q_0^2)\Gamma_\kappa h\tau\,\xi^3}{3}
\quad(\delta\downarrow0).
\tag{24}
$$
极限严格异号，有限余项有界，故正有限 $\delta$ 已取得两个真实符号。
所有支撑、相对位置和母包参数都处在原严格开域内。

这四列的 $\mathcal C_1$ 向量沿
$$
\pm(\alpha_1\beta_1,1),\qquad
\pm(\alpha_2\beta_2,1).
\tag{25}
$$
$\alpha\beta$ 严格递增，故四列满二维且有严格正核，其正锥是 $\mathbb R^2$。这支付的是整个相位函数，两个 odd 系数使用原十二完整复制，而非有限角采样。

各新原型还准确满足
$$
\mathcal M_j=\mathcal A_j=0\quad(j=0,1,2),\qquad
\mathcal B_0=0,\qquad C_\theta=J_\theta=0.
\tag{26}
$$
原因与 R346 §6 相同：真 $\mathcal F_\kappa=0$ 支付原完整面积，母包保持 even，真实排序与反射给原 $\mathcal B_0$；quartic 张量不变。
其 $\Psi=\psi_i\sin^2\theta$、$\psi_i>0$。
它们的 $\mathcal B_1,\mathcal B_2,\mathcal C_0$ 一律保留实际值，下一节联合支付，不先假为零。

## 7. 全式伸缩使旧六目标与新两目标三角分离

原 $Y$ 完整权为 $+1$、$Z_*$ 为 $-1$，所以
$$
\boxed{
\mathcal C_1(f_H,g_H)=H^{-2}\mathcal C_1(f,g),\qquad
(f_H,g_H)(x)=(f,g)(x/H).
}
\tag{27}
$$
同一真实右零 collar保证原函数的全式齐次；这不是 principal 权。
旧三组分别满足
$$
\mathcal B_1:H^{-5},\quad
\mathcal B_2:H^{-4},\quad
\mathcal C_0:H^{-3},\quad
\Psi:H^{-7}.
\tag{28}
$$
把§6四个新原型作共同大有限伸缩 $H$，第四幅度乘 $H^2$，其
$\mathcal C_1$ 列保持不变，旧六目标依次变为
$O(H^{-3}),O(H^{-2}),O(H^{-1})$。

R346 §8 已构造一个真实六目标矩阵
$$
M_6:\lambda\longmapsto(\mathcal B_1,\mathcal B_2,\mathcal C_0)
$$
满秩并有严格正核。其原十二列的 $\mathcal C_1$ 值记为 $D_6$；这些是实际列值，不是新自由参数。
令 $C_1^{\rm new}$ 为(25)的四列。新的八目标矩阵满足
$$
M_{8,H}\longrightarrow
\begin{pmatrix}
M_6&0\\
D_6&C_1^{\rm new}
\end{pmatrix}.
\tag{29}
$$
极限矩阵满行秩8。

取 $k_6>0$、$M_6k_6=0$。
新四列正锥为 $\mathbb R^2$，故可取 $k_{\rm new}>0$ 使
$C_1^{\rm new}k_{\rm new}=-D_6k_6$；先取一个非负表示，再加严格正零关系即可。
于是极限有严格正核。固定一个非零八列子式，仅用这八列修正趋零的残差，就在足够大的有限 $H$ 得到严格正核和满秩：
$$
\boxed{\operatorname{cone}_+(M_{8,H})=\mathbb R^8.}
\tag{30}
$$
所有列来自实际不交强完整 blocks；R263 的 inner 三矩零使不同完整 blocks 的 cross 准确消失。原弱核心内部不使用逐微包表。

## 8. 同一负 Ψ 基线上的精确支付

从 R346 最后强控制器之前接入。原弱部分、宽恢复、补矩、所有旧模块与最终中心全部固定，已准确满足
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=0,\quad
\mathcal C_0=0,\qquad
\Psi=-\Delta_0\sin^2\theta,\quad\Delta_0>0.
\tag{31}
$$
取当前真实 $\mathcal C_1$ even 残差为 $r_{\rm old}\in\mathbb R^2$。
原三条 directed 行作为完整有限基线留给最后控制步骤。

固定(30)的有限原型组、严格正核 $k>0$ 与实右逆 $R_8$。
将整组再作共同正伸缩 $S$，第四幅度取 $S^5c_i(S)$，其中
$$
\boxed{
c(S)=k+R_8(0,0,0,-r_{\rm old}/S^3).
}
\tag{32}
$$
四个目标块依次是 $\mathcal B_1,\mathcal B_2,\mathcal C_0,\mathcal C_1$，每块二维。
由完整权，原矩阵输出实际变为
$(1,S,S^2,S^3)$ 倍。所以对足够大的有限 $S$，
$c(S)>0$ 且有界，并且
$$
\Delta\mathcal B_1=\Delta\mathcal B_2=\Delta\mathcal C_0=0,\qquad
\Delta\mathcal C_1=-r_{\rm old}.
\tag{33}
$$
每列自身的旧零(26)同时保持。

若固定列的 $\Psi$ 系数为 $\psi_i>0$，新增真实成本是
$$
S^{-2}\sum_i c_i(S)\psi_i\,\sin^2\theta.
\tag{34}
$$
选有限 $S$ 使其小于 $\Delta_0/2$；同一个更大有限 $S$ 可把全部新正支撑放在旧固定 profiles 右方。没有移动旧弱块、旧中心矩或已付目标。

此后沿 R346 原控制器入口，用初选有限 $F^\star$、固定真 minor 和有限 $N$ 的正核根，准确付原三条 $F_i$ 并将 $\Psi$ 归零。
该控制器自身完整72面积全零，同纤维纠正保其原值，因此也保新 $\mathcal C_1$。不是把“旧六目标可控”当成“全部 Gaussian 可控”。

## 9. 完整有限选择次序与余项

先固定原几何及 R346 的实际负余基线；再在正母宽上选真实 $v_{\pm\tau_0}$、两种 $\alpha$、有限间距和四个正区间；选正有限 $\delta$ 取得(25)；随后固定原六目标库及各列新矩值，取有限 $H$ 得八目标严格正核；最后取有限 $S$ 和(32)的正第四幅度，才固定最后强控制器并求有限 $N$ 的完整根。

共同合法正区间按 R105/R114/R271 的原范围，从全部有限原型及几何包络一次选择，包含最终支撑和严格 collar。有限 $N$ 只在已经选好的强控制区内变化。不对任意先前冻结窄区间作扩大承诺，也不在支付以后整体平移圆。

本稿最终增加完整 $\mathcal C_1=0$；它不假设原弱核心满足(18)，不删除(5)中的任何未付括号。所有新控制都由新增真强 blocks 承担，原弱单 hook 和完整第三 range 保留。

R259 表中尚未逐项支付的是
$Y$–$P$ 的三个外矩、$Y$–$W_*$ 的三个外矩，以及 $Y$–$Z_*$ 的第2外矩。
即14个形式 even 位置，仍不宣独立；R271 给 $Y$–$P$ 第1矩的一条准确重复。剩余 ruling 函数、完整第四 period、同一个 gauge 的 joint 条件及全等距族仍未由本文完成。
