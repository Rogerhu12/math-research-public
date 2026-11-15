# R267：幅度与宽度母包同时支付完整 A_{-1,-3} 面积与原联合能量

日期：2026-11-15。**完整纸面结论；没有执行新的原式归约、profile 求积、参数扫描或几何计算。**

本稿从原八个二次算子出发，计算 $[P,p_0]$、$[P,s_1]$ 的全部三个单包外矩，保留单包真实左尾。在 R256 的两坡、不交偶母包族中，完整 Gaussian $A_{-1,-3}$ 的六个 even 表项归为一个准确的母包形状方程。给中央母包增加正实幅度后，它与原 $M_c$ 所需的形状方程具有可逆 Jacobian；主宽度的三参数隐函数定理遂能同时支付整个 $A_{-1,-3}$、六能量、整个 $A_{-2,-3}$、全部 odd 面积条件及三矩、全部第三槽。

新条件与 R265 的正、负 $\mathscr Q$ 分支相容，还可正四次混合支付 $\mathscr Q=0$。这不是完整第四 ruling 的解，其他 Gaussian 面积、零一层 history 及 period/joint 仍未由此解决。特别，不把表项数当作独立秩或把当前部分构造称为完整候选成功。

来源：[R250](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R252](R252-two-further-Gaussian-areas-exclude-the-even-packet-exceptional-family.md)、[R256](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)、[R257](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)、[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R262](R262-ordered-primitive-obstruction-for-the-multiwidth-energy-branch.md)、[R265](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md)。

## 1. 同一共振 germ 与原算子

固定共同右锚 $r_*$，$JF(x)=\int_x^{r_*}F(t)\,dt$，所以 $(JF)'=-F$。采用真实共振例外端芽

$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad \omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad h_e>0,\quad \kappa\ne0.
\tag{1}
$$

本稿处理的 Gaussian 方向为

$$
B_{-1}=dL+eS,\qquad B_{-3}=cP,\qquad
P=\Phi_{r_0},\ L=\Phi_{p_0},\ S=\Phi_{s_1},
$$

$$
d=\frac{6\kappa^3}{h_e},\quad
e=-\frac{\kappa(15\kappa^2+1)}{4h_e},\quad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}.
\tag{2}
$$

令

$$
\lambda=-\frac56(d+7e)
=\frac{5\kappa(81\kappa^2+7)}{24h_e}\ne0.
\tag{3}
$$

$c$ 也非零。以下只除以这些已经准确识别的非零因子。

对任意实紧 $u$，写 $v=u'$、$\rho=u''$、$\tau=u'''$，以及
$A=J(\rho^2)$、$B=J(x\rho^2)$、$C_2=J(x^2\rho^2+2v^2)$。原式是

$$
P(u,u)=A,\quad
L(u,u)=uv-\frac{xv^2}{2}-\frac{x^2A}{4}+\frac{C_2}{4},\quad
S(u,u)=xv^2+xB+\frac{C_2}{2}.
\tag{4}
$$

本节及下一节不假设单个 $u$ 三矩为零；三个输出可以有真实左尾。

## 2. 三个原 self 矩与全部端项

原矩为
$\mathbf I(u,w)=(\int u''w'',\int xu''w'',\int(x^2u''w''+2u'w'))$。
记四次积分

$$
\begin{aligned}
\mathsf C&=\int\rho^4,&\mathsf X_1&=\int x\rho^4,&
\mathsf X_2&=\int x^2\rho^4,\\
\mathsf N_0&=\int v\rho^3,&\mathsf N_1&=\int xv\rho^3,&
\mathsf V&=\int v^2\rho^2,&\mathsf U&=\int u\rho^3.
\end{aligned}
\tag{5}
$$

对 $[X,Y](u;D)=X(u,YD)-Y(u,XD)$，定义
$\mathbf S_{X,Y}(u)=2\mathbf I\{u,[X,Y](u;u\odot u)\}$。准确有

$$
\boxed{\mathbf S_{P,L}=
\left(\frac{\mathsf C}{6},-\frac{\mathsf X_1}{3},
\frac43\mathsf N_1-\frac56\mathsf X_2\right),}
\tag{6}
$$

$$
\boxed{\mathbf S_{P,S}=
\left(\frac{7\mathsf C}{6},
\frac83\mathsf N_0-\frac73\mathsf X_1,
-\frac{35}{6}\mathsf X_2+\frac{44}{3}\mathsf N_1
-8\mathsf V-\frac83\mathsf U\right).}
\tag{7}
$$

这些公式对非三矩闭的单个实际微包也成立。

### 2.1 直接原函数证明

由 (4)，

$$
L'=u\rho-xv\rho-xA/2,\quad
L''=(u-xv)\tau-x\rho^2/2-A/2,
$$

$$
S'=2xv\rho+B-3x^2\rho^2/2,\quad
S''=2v\rho-2x\rho^2+2xv\tau-3x^2\rho\tau.
\tag{8}
$$

代入原双线性极化式，全部 primitive 在二导中准确组合为

$$
[P,L](u;u^2)''=x\rho^2\tau+\rho^3/3
=(x\rho^3/3)',
$$

$$
[P,S](u;u^2)''=-4v\rho\tau+7x\rho^2\tau+\rho^3.
\tag{9}
$$

同一右 collar 支付

$$
[P,L](u;u^2)'=x\rho^3/3,\qquad
[P,S](u;u^2)'=-2v\rho^2+\frac73x\rho^3-\frac23J(\rho^3).
\tag{10}
$$

第二式的真实尾仍保留。代入三矩并 IBP 得 (6)、(7)。例如 $I_2$ 的 $x^2\rho$ 部分对第二式给
$8\mathsf N_1/3-35\mathsf X_2/12$，其 $2v$ 部分给
$-4\mathsf V+14\mathsf N_1/3-4\mathsf U/3$；
最后只用紧 $u$ 的
$\int vJ(\rho^3)=\int u\rho^3$。
相加并乘 2 即为 (7)，没有设 $J(\rho^3)$ 左尾为零。

### 2.2 非紧方向的 Green 对照

R259 的三个 cubic 密度可取为：

| 算子 | $F_{X,0}$ | $F_{X,1}$ | $F_{X,2}$ 的密度 |
|---|---|---|---|
| $P$ | $0$ | $2\rho^3/3$ | $4x\rho^3/3-2v\rho^2$ |
| $L$ | $-v\rho^2/2$ | $0$ | $-xu\rho^2+x^2v\rho^2/2-v^3/3$ |
| $S$ | $v\rho^2-x\rho^3$ | $0$ | $2xu\rho^2-4x^2v\rho^2+x^3\rho^3-4v^3/3$ |

中列零密度的原代表分别为 $v^2\rho,-2v^2\rho$，其紧积分为零。对非紧变分方向仍使用 R259 的 local Euler 表达，而不把 cubic 身份直接延到任意非紧输入族。

令 $\mathcal L_0=D^4$、$\mathcal L_1=xD^4+2D^3$、
$\mathcal L_2=x^2D^4+4xD^3$。
完整 self 等于 local 变分差加
$\mathcal B_j(X,Y)=\int(X\mathcal L_jY-Y\mathcal L_jX)$。
若 $g_0=XY'''-X'Y''+X''Y'-X'''Y$，三个 Green 原函数是

$$
g_0,\quad xg_0+XY''-X''Y,\quad
x^2g_0+2x(XY''-X''Y)-2(XY'-X'Y).
\tag{11}
$$

以 $\mu_j=I_j(u,u)$ 记真实左尾，则
$P=\mu_0$、$L=(-\mu_0x^2+\mu_2)/4$、
$S=\mu_1x+\mu_2/2$。
三个端项对 $(P,L)$ 是 $(0,\mu_0^2/2,0)$，对 $(P,S)$ 是
$(0,0,2\mu_0\mu_1)$。
local 变分中恰出现相反两项，分别来自
$\int A\rho^2=\mu_0^2/2$、
$(AB)'=-(B+xA)\rho^2$。
这与 (9)、(10) 的直接证明完全一致，不能从一开始把单包二次输出假称紧支撑。

## 3. 完整面积所需的一个 local 形状量

R259 的原尾作用给
$\mathbf\Gamma_{P,L}=\mathbf\Gamma_{P,S}=0$。
这是两项真实尾作用准确相消，而不是假设跨包 history 不存在。因此不交微包的此 pair 外矩只保 (6)、(7) 的 self 和。

由 (2)，

$$
[B_{-1},B_{-3}]=-c\{d[P,L]+e[P,S]\}.
\tag{12}
$$

前两个 self 分量分别正比于
$(d+7e)\mathsf C/6$ 和
$-(d+7e)\mathsf X_1/3+8e\mathsf N_0/3$。
第三个是 $\lambda\mathcal K_\kappa(u)$，其中

$$
\begin{aligned}
\mathcal K_\kappa(u)={}&\mathsf X_2
-\frac{8(141\kappa^2+11)}{5(81\kappa^2+7)}\mathsf N_1\\
&+\frac{48(15\kappa^2+1)}{5(81\kappa^2+7)}\mathsf V
+\frac{16(15\kappa^2+1)}{5(81\kappa^2+7)}\mathsf U.
\end{aligned}
\tag{13}
$$

各比值对 $\kappa^2=0$ 光滑。仅归一参数在零处延拓，实际仍取 $\kappa\ne0$。

若 $u$ even，对 $\eta_{w,\xi}=w^{3/2}u((x-\xi)/w)$，

$$
\mathsf N_0(u)=0,\quad
\mathsf C(\eta)=\mathsf C(u)/w,\quad
\mathsf X_1(\eta)=\xi\mathsf C(u)/w,
$$

$$
\boxed{\mathcal K_\kappa(\eta)
=\xi^2\mathsf C(u)/w+w\mathcal K_\kappa(u).}
\tag{14}
$$

令

$$
\nu(u)=\frac{\int x^2(u'')^2+2\int(u')^2}{\int(u'')^2},
\qquad
\mathcal F_\kappa(u)=\frac{\mathcal K_\kappa(u)}{\mathsf C(u)}-\nu(u).
\tag{15}
$$

所有项来自同一个实际母包。

## 4. 三外矩、两个 even 系数均完整归约

沿用 R256，$n=2^{11}$，
$q=1/[16(1-\alpha)^2]$、
$\beta=(5-\alpha)/(1-\alpha)$、$1/3<\alpha<1/2$。
低组 $64n$ 个包宽 $q\delta$、系数
$(\epsilon_i\sqrt{\alpha q},\sqrt q)$；
高组 $n$ 个包宽 $\delta$、系数
$(\epsilon_i\sqrt\beta,1)$。
两组同中心均值，准确方差差为

$$
V_L-V_H=\nu(u)(1-q^2).
\tag{16}
$$

真实三矩、R250 全角面积及第三 lift 按 R256 保留。对
$\phi_\theta=f\cos\theta+g\sin\theta$、$D_\theta=f^2-\phi_\theta^2$，
R259 给每外矩两个 even 系数

$$
\mathcal E_{22}=\sum_i(a_i^4-5a_i^2b_i^2)S_i,\quad
\mathcal E_{04}=\sum_i(a_i^2b_i^2-b_i^4)S_i.
\tag{17}
$$

odd 由预先放入的十二完整副本消掉，此 pair 没有其他 cross 核。
对 $I_0$，(14) 将 (17) 化为已付的 quartic 张量；
对 $I_1$，$\mathsf N_0=0$ 与两组同均值再次给其公共倍数。
这两个完整整圆外矩已经为零。

对 $I_2$，除 $-c\lambda$ 外的低、高 self 平均记为 $K_L,K_H$。准确有

$$
\frac{\beta(\beta-5)}{\beta-1}
=\frac{\alpha(\alpha-5)}{\alpha-1}=\alpha\beta,
$$

$$
K_H-qK_L=\delta(1-q^2)
\{\mathcal K_\kappa(u)-\mathsf C(u)\nu(u)\}.
$$

所以

$$
\boxed{
\mathcal E_{04}
=-c\lambda n(\beta-1)\delta(1-q^2)\mathsf C(u)\mathcal F_\kappa(u),
\quad \mathcal E_{22}=\alpha\beta\mathcal E_{04}.
}
\tag{18}
$$

显示因子均非零。故在已付 odd/低阶条件下，
$\mathcal F_\kappa=0$ 等价于整个 $A_{-1,-3}$ 的全 $\theta$、三外矩同时为零。

对八、十二完整复制，平移给两组二次中心矩加相同的常数和一次项；已零的前两矩与 (16) 将其消掉。因此 (18) 只乘公共四次权和。结论作用于已经完整包装的实际 profile，不是解完未包装方程后任意搬移能量零点。


## 5. 正幅度参数补足真实 shape Jacobian

取 R265 的固定非零 even 母包 $v$，并可同时带其伴随 $\widehat v$。固定 $L=1/2$，令

$$
u_{\gamma,s,h}(x)=
\gamma(sh)^{3/2}v(x/(sh))
+h^{3/2}v((x-L)/h)+h^{3/2}v((x+L)/h),
\tag{19}
$$

$\gamma,s>0$ 在1的小邻域，$h>0$ 足够小，使三个母子包严格不交。新增的是中央真实幅度，不是一个可独立赋值的积分。

记 $m_v=\int(v'')^2$、$C_v=\int(v'')^4$、
$\mathcal A_v=\int(v'')^2(v''')^2>0$，以及 R256 的原分子

$$
\mathcal B(v)=
27\int x^2(v'')^2(v''')^2
-20\int xv''v'(v''')^2
+2\int\{(v')^2+v''v\}(v''')^2.
\tag{20}
$$

不交、even 性及真实宽度换元给

$$
\nu(u)=
\frac{2L^2+\nu(v)h^2(\gamma^2s^2+2)}{\gamma^2+2},\qquad
\mathsf C(u)=\frac{C_v}{h}(\gamma^4s^{-1}+2),
$$

$$
\mathcal K_\kappa(u)=\frac{2L^2C_v}{h}
+h(\gamma^4s+2)\mathcal K_\kappa(v),
$$

$$
\mathcal A(u)=\frac{\mathcal A_v}{h^3}(\gamma^4s^{-3}+2),\qquad
\mathcal B(u)=\frac{54L^2\mathcal A_v}{h^3}
+\frac{\mathcal B(v)}h(\gamma^4s^{-1}+2).
\tag{21}
$$

四次量的中央幅度是 $\gamma^4$，二次矩质量则是 $\gamma^2$。

定义两个原归一函数

$$
\mathcal H(u)=27\nu(u)-\frac{\mathcal B(u)}{\mathcal A(u)},\qquad
\mathcal F_\kappa(u)=\frac{\mathcal K_\kappa(u)}{\mathsf C(u)}-\nu(u).
\tag{22}
$$

它们由 (21) 在 $(\gamma,s,h^2)$ 中解析延拓。只这些有限标量在零宽处延拓，不声称 profile 的零宽极限合法。在 $h=0$，

$$
\mathcal H_0=54L^2
\left(\frac1{\gamma^2+2}-\frac1{\gamma^4s^{-3}+2}\right),
$$

$$
\mathcal F_0=2L^2
\left(\frac1{\gamma^4s^{-1}+2}-\frac1{\gamma^2+2}\right).
\tag{23}
$$

在 $\gamma=s=1$，两值均零，且

$$
D_{(\gamma,s)}(\mathcal H_0,\mathcal F_0)
=L^2\begin{pmatrix}12&-18\\-4/9&2/9\end{pmatrix},
\qquad \det=-16L^4/3\ne0.
\tag{24}
$$

所以足够小正 $h$ 有真实正参数
$\gamma_h=1+O(h^2),s_h=1+O(h^2)$，
使两原积分准确为零，实际二参数 Jacobian 仍可逆。
也可先由 $\mathcal F_\gamma\ne0$ 解 $\gamma=\gamma(s,h^2)$；
原点处 $\gamma_s=1/2$，限制后的 $\mathcal H_s=-12L^2\ne0$。

(13) 对小 $\kappa^2$ 光滑，故可在固定紧小参数区间统一选择上述邻域与正 $h$。实际结论始终取非零 $\kappa$。

## 6. 主宽度的三个完整方程

现在固定正 $h$。在母参数紧邻域中，所有支撑间隙统一为正。按 R256 选择两组中心，可先声明任意有限
$A=\Lambda+\sqrt{\nu(u)}$、$\Lambda\ge10$，$B$ 仍由真实方差式决定。再一次选定完整八、十二复制的统一间距。所有有限选择均在主宽度 $\delta$ 之前完成。

用已经完整包装的原能量定义

$$
F(\alpha,\gamma,s,\delta)=\delta^3L_c,\qquad
G(\alpha,\gamma,s,\delta)=\delta\{M_c+3L_c/\zeta_0\}.
\tag{25}
$$

R256 从原 $S,\mathfrak T$ 的有限多项式证明联合解析延拓；新增幅度只以有限正幂进入同一公式。每组中心零和副本的正四次权中心零，使 $G$ 潜在负次幂在尚未求 $\alpha$ 根时就已经消失。

记
$Q_L=64\alpha(1-\alpha)/q$、$Q_H=\beta(\beta-1)$、
$P=Q_L-Q_H$。其唯一简单根 $\alpha_0\in(1/3,1/2)$ 已在 R256 证明。完整归一值为

$$
F(\alpha,\gamma,s,0)
=\frac{\mathcal W n\mathcal A(u)\zeta_0^{10}}{64}P(\alpha),
$$

$$
\begin{aligned}
G(\alpha,\gamma,s,0)=
\frac{\mathcal W n\zeta_0^7}{64}\big[
&27\mathcal A(u)\{Q_LV_L-Q_HV_H+P V_{\rm cp}\}\\
&+\mathcal B(u)(Q_Lq^2-Q_H)\big].
\end{aligned}
\tag{26}
$$

$V_{\rm cp}$ 是已经选定的完整副本共同四次加权方差。没有删去它，也没有在求根前置 $P=0$。在 $\alpha=\alpha_0$，

$$
G(\alpha_0,\gamma,s,0)=
\frac{\mathcal W n\zeta_0^7Q_0(1-q_0^2)}{64}
\mathcal A(u)\mathcal H(u).
\tag{27}
$$

对三个原方程

$$
F=0,\qquad G=0,\qquad
\mathcal F_\kappa(u_{\gamma,s,h})=0,
\tag{28}
$$

在 $(\alpha_0,\gamma_h,s_h,0)$ 全部为零。第一行对 $\alpha$ 的导数非零，对 $\gamma,s$ 的导数为零；后两行的 $(\gamma,s)$ 子式等于 (24) 的正 $h$ 延续，第二行只另乘非零因子。故三方程对 $(\alpha,\gamma,s)$ 的 Jacobian 可逆。

真实隐函数定理给充分小正 $\delta$ 的
$\alpha(\delta),\gamma(\delta),s(\delta)$。
由 $\delta>0$，前两式准确给 $L_c=M_c=0$；第三式按 (18) 支付整个 $A_{-1,-3}$。
原 TM 与十二复制给 $L_s=M_s=0$；
共振时 R256 的完整含尾身份 $N_c=6M_c,N_s=6M_s$ 支付最后两门。

旧三矩与全角 $A_{-2,-3}$ 对这三个参数逐点成立，因为它们只要求同一 even 母包、两坡比例和准确方差。完整第三及全部 odd 由同一包装保留。取统一严格间隙的紧邻域，再缩小正 $\delta$，整个有限支撑云即能放入先选正物理子区间。

这是三个完整积分方程，不是三个 leading 根；不把母包积分当独立旋钮，也不以形式秩代替真实参数实现。

## 7. 新 shape 根保留负 Q 分支

R262 的 cell 求和只使用共同二次质量及两坡排列，对新 $u_{\gamma,s,h}$ 仍适用。母包所需的正因子是
$\mathsf C\nu-\mathcal L+\Delta/4$，其中 $\mathcal L,\Delta$ 沿用 R257。

这里准确有

$$
\mathcal L(u)=2L^2C_v/h+h(\gamma^4s+2)\mathcal L(v),
$$

$$
\Delta(u)=4Lm_v^2(\gamma^2+1)
+h(\gamma^4s+2)\Delta(v).
\tag{29}
$$

第二式保中央二次质量 $\gamma^2m_v$；两条中央—外侧交叉与两外侧交叉的距离项准确是
$4Lm_v^2(\gamma^2+1)$。

于是

$$
\begin{aligned}
\mathsf C\nu-\mathcal L
={}&\frac{2L^2C_v}{h}
\left(\frac{\gamma^4s^{-1}+2}{\gamma^2+2}-1\right)\\
&+h\left[
\frac{C_v\nu(v)(\gamma^4s^{-1}+2)(\gamma^2s^2+2)}{\gamma^2+2}
-(\gamma^4s+2)\mathcal L(v)\right].
\end{aligned}
\tag{30}
$$

母根 $\gamma_h,s_h=1+O(h^2)$ 使 (30) 为 $O(h)$，而

$$
\mathsf C\nu-\mathcal L+\Delta/4
=2Lm_v^2+O(h)>0.
\tag{31}
$$

先固定留有严格余量的正 $h$，再按主分支连续性缩小 $\delta$，R262 的两个负项仍各自严格负。因此有同时完成新增整面积的真实负号 block $\mathscr Q_-<0$。

这里不要求母宽与主宽之间未经证明的一致极限；顺序始终先 $h$ 后 $\delta$。

## 8. 正伴随与两个完整 block 的准确混合

按 R265，用同一 $\gamma,s,h$ 在三个母子包中同时构造伴随 $\widehat u$。准确有

$$
u^{(p)}u^{(q)}=\widehat u^{(p)}\widehat u^{(q)},\qquad
\mathbf I(u,\widehat u)=0.
\tag{32}
$$

替换 $g$ 后，每个最小子包只改变第二系数的符号，所有 even local self 不变。本稿 pair 的原 cross 核为零，所以 (18) 的全部 even 条件准确保持；odd 仍由十二完整副本支付。没有从某个 diagonal 值相等推一般 mixed 身份。

R265 正号公式保持不变，只用新母包的实际常数：

$$
\begin{aligned}
\operatorname{Re}\mathscr Q_+
={}&10928nm^2a^2A-\frac{na^2\Delta}{4}(64q+4096)\\
&-2nK(64\alpha q^3+\beta)\\
&+64nq(\alpha^2-6\alpha+1)(1-q^2)(\mathsf C\nu-\mathcal L),
\end{aligned}
\tag{33}
$$

$a=q(1-\alpha)$，$K=\int[J(u''\widehat u'')]^2$ 真紧。
固定 $h$ 及母根后，后三项与间距 $A$ 无关，第一项系数严格正。
先取有限大 $\Lambda$ 留正余量，再进行 §6 的三变量主 IFT；
母根与 Jacobian 不因此退化，最终连续性给真实 $\mathscr Q_+>0$。

两个 block 分别在两个最终不交位置独立完成新能量/面积根和完整包装。取正幅度
$c_-^4=\mathscr Q_+$、$c_+^4=-\mathscr Q_-$。
三矩、完整第三、六能量、两个整 Gaussian 面积和全部 odd 准确相加；
R259 跨核由右侧 inner 完整 block 的三矩为零消去。
每个完整 $J(q_\pm''^2)$ 真紧，故

$$
\mathscr Q(c_-q_-+c_+q_+)
=c_-^4\mathscr Q_-+c_+^4\mathscr Q_+=0.
\tag{34}
$$

这里没有负的四次实际幅度权，也没有把 span 当作正半群。

## 9. 安装、参数与剩余范围

先固定共同物理区间、右锚和共振参数。依次选择带伴随的 even $v$、紧参数邻域、真实正母宽 $h$、各最终 block 的有限间距和副本位置，最后取小正主宽 $\delta$。实际 profile 都光滑、严格正有限宽、带共同双零 collar；不同两坡方向仍在支撑上出现，正幅度小改变不将它们退化成单一方向。

若需使用已有几何安装结论，(13)、(21)—(28) 对小 $\kappa^2$ 的归一参数光滑，可在紧参数族上先固定正 $h,\delta$ 与有限位置，再选安装允许的非零 $\kappa$。不把 $\kappa=0$ 的形式零面积当作实际结论，也不将 $1/\kappa$ 放入安装 Jacobian。原 canonical pure、矩、frame 与第三结构按已经证明的完整几何定理保持。本稿选择新 profile 圆及其种子目标，不能冒称原固定 seed/目标下的一次允许变形。

新增准确结论是：R265 的全部已付条件可以与整个 $A_{-1,-3}$ 同时成立，所有三外矩和两个 even 系数均已支付。原 self 与 Green 端项是逐函数身份；隐函数方程对应原完整积分。

其余四个 Gaussian 面积的 even 表仍须按 R259 处理，可列 24 条但不宣其独立；其中包含已付 $\mathscr Q$ 的一个线性组合，也不据此断言剩余秩恰23。零、一层 history、完整 period/joint 未由本稿解决。

尤其，当前 cell 排列还存在另一个 even 条件的已知限制，故本稿不是完整第四候选成功声明。后继若改变真实包次序，必须重新支付准确三矩、完整包装和原函数边界，再用同一 self/cross 接口判断；不得只按已付能量的数目推断完整可解。
