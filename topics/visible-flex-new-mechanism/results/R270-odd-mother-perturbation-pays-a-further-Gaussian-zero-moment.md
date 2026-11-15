# R270：奇母扰动与四变量隐函数定理支付另一完整 Gaussian 第零外矩

日期：2026-11-15。**完整纸面建设性证明；未执行求积、参数扫描、符号消元程序、人工检查或研究计算。**

本稿接 [R267 的幅/宽母形状](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)和 [R269 的真实重排与四块混合](R269-reordered-real-masses-pay-a-complete-Gaussian-zero-moment.md)。新增一个真实母包参数：在右母子包中作小奇扰动，左母子包取它的镜像，整体母包仍为 even。这个参数用于原 $A_{1,-1}$ 面积的整个第零外矩，并与原能量及已付面积方程同时求解。

结论只增加这一完整角函数的支付，不声称 $A_{1,-1}$ 的其余两外矩为零。最终保留三矩、完整第三、六能量、整个 $A_{-2,-3}$ 与 $A_{-1,-3}$、全部36个 Gaussian odd 条件，以及 R269 已付的整个 $A_{1,-3}$ 第零外矩；另付整个 $A_{1,-1}$ 第零外矩。原72式账中仍有20条形式 even 等式未由这些结论支付，不能把这个数当作独立秩。

其他来源：[R259 原 self/cross 接口](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R256 原能量展开](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)、[R265 同源伴随母包](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md)、[R268 完整 sine-four](R268-full-sine-four-area-obstruction-for-centered-microcells.md)。

## 1. 原系数、原槽和要支付的完整角函数

固定共振 $\varepsilon=\kappa^2/4$，$h_e>0$，实际 $\kappa\ne0$ 足够小。记

$$
L=\Phi_{p_0},\qquad S=\Phi_{s_1},\qquad Y=\Phi_{p_2}.
$$

本节的 $L$ 是算子；后文母包的固定中心距离另记 $L_*=1/2$。原 Gaussian 方向为

$$
B_1=\zeta Y,\quad B_{-1}=dL+eS,\quad
\zeta=-\kappa h_e,\quad
d=\frac{6\kappa^3}{h_e},\quad
e=-\frac{\kappa(15\kappa^2+1)}{4h_e}.
\tag{1}
$$

故 $[B_1,B_{-1}]=-\zeta\{d[L,Y]+e[S,Y]\}$。因 $-\zeta\ne0$，可用括号中的原组合检验零，不改系数或目标。

R259 给 $\Gamma_{L,Y}=\Gamma_{S,Y}=0$：这是跨不交微包尾核为零，不是交换子本身为零。对真实三矩圆

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
$$

要支付的是

$$
2I_0\{\phi_\theta,
(d[L,Y]+e[S,Y])(\phi_\theta;D_\theta)\}=0
\quad\hbox{对全部 }\theta.
\tag{2}
$$

本稿不把 pure 对角值代替 (2)。

## 2. 两条真实单包 self，含原 Green 端项

令 $u$ 为任意实紧微包，$v=u'$、$r=u''$、$t=u'''$；所有 primitive 仍取同一个右锚。令 $J_0=J(r^2)$、$J_1=J(xr^2)$、$J_2=J(x^2r^2+2v^2)$。原二次场为

$$
Lu=uv-\frac{xv^2}{2}-\frac{x^2J_0}{4}+\frac{J_2}{4},
\quad
Su=xv^2+xJ_1+\frac{J_2}{2},
$$

$$
Yu=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2J_2}{4}.
\tag{3}
$$

这里 $Xu$ 简写 $\Phi_X(u,u)$。这些二次场一般有非零左多项式尾，不能假称紧。

定义
$\mathsf S_{X,Y,0}(u)=2I_0\{u,[X,Y](u;u\odot u)\}$。
从 R259 的原 local 变分接口得到

$$
\boxed{
\begin{aligned}
\mathsf S_{L,Y,0}
=\int\big[
&u^2r^2-4xuvr^2+3x^2v^2r^2+x^2ur^3\\
&-\frac43x^3vr^3+\frac5{24}x^4r^4
\big],
\end{aligned}}
\tag{4}
$$

$$
\boxed{
\begin{aligned}
\mathsf S_{S,Y,0}
=\int\big[
&-u^2r^2+8xuvr^2-9x^2v^2r^2-3x^2ur^3\\
&+\frac{16}3x^3vr^3-\frac{25}{24}x^4r^4
-\frac23v^4
\big].
\end{aligned}}
\tag{5}
$$

给出端项及可直接核对的导数。原 cubic densities 为
$-vr^2/2$、$vr^2-xr^3$ 和
$xu r^2-3x^2vr^2/2+x^3r^3/3-v^3/3$；其 Euler 密度分别为

$$
\begin{aligned}
E_L&=-2rt-vr'',\\
E_S&=(2v-6xr)r''-8rt-6xt^2,\\
E_Y&=(2xu-3x^2v+2x^3r)r''
 +(4u-8xv+6x^2r)t+2x^3t^2.
\end{aligned}
\tag{6}
$$

令 $\mu_j=I_j(u,u)$。$Lu$ 左尾是
$-\mu_0x^2/4+\mu_2/4$，$Su$ 左尾是
$\mu_1x+\mu_2/2$，$Yu$ 左尾是 $-\mu_2x^2/4$。
因此 $L,Y$ 的 $I_0$ Green 余项为零；$S,Y$ 的余项进入 self 时准确为
$-\mu_1\mu_2/2$。

将 (3) 代入 $E_SY-E_YS$，原 primitive 的最后剩余项为

$$
\frac12\int\{J_1(x^2r^2+2v^2)+xr^2J_2\}
=-\frac12[J_1J_2]_{\rm left}^{\rm right}
=\frac{\mu_1\mu_2}{2}.
\tag{7}
$$

它恰消上述 Green 项，然后得到 (5)。式 (4) 的两个 quadratic 左尾自身配对为零。其余项使用 $J_i'$ 及紧 $u$ 的 IBP 给 (4)—(5)。这保留了原 $\mu_i$，没有先令单包三矩为零，也没有把仅对合法复 profile 的 compact 对角公式逐包套用。

## 3. Even 母包的准确中心/宽度分解

现在 $u$ 为 even，辅助坐标记 $y$。置

$$
C=\int r^4,\quad X_2=\int y^2r^4,\quad
N=\int yv r^3,\quad
W=3\int v^2r^2+\int ur^3,\qquad
\mathcal J(u)=W-2N.
\tag{8}
$$

取原 $I_0$ 归一的微包
$\eta_{w,\xi}(x)=w^{3/2}u((x-\xi)/w)$，$w>0$。由 (4)—(5) 的真实换元，

$$
\boxed{
d\mathsf S_{L,Y,0}(\eta_{w,\xi})
+e\mathsf S_{S,Y,0}(\eta_{w,\xi})
=\frac{a_4C\xi^4}{w}+w\xi^2\mathcal B_\kappa(u)
+w^3\mathcal D_\kappa(u),
}
\tag{9}
$$

其中

$$
a_4=\frac{5(d-5e)}{24},\qquad
\mathcal B_\kappa=6a_4X_2-4(d-4e)N+(d-3e)W,
\tag{10}
$$

$$
\begin{aligned}
\mathcal D_\kappa
={}&(d-e)\int u^2r^2-4(d-2e)\int yuvr^2\\
&+(d-3e)\int y^2(3v^2r^2+ur^3)
-\frac43(d-4e)\int y^3vr^3\\
&+a_4\int y^4r^4-\frac{2e}{3}\int v^4.
\end{aligned}
\tag{11}
$$

没有将 $\mathcal B_\kappa,\mathcal D_\kappa$ 当作独立参数。

沿用 R267 的真实母条件

$$
\lambda=-\frac{5(d+7e)}6,\qquad
\mathcal F_\kappa(u)=\frac{\mathcal K_\kappa(u)}{C}-\nu(u),
$$

$$
\lambda\mathcal K_\kappa
=\lambda X_2+\frac43(d+11e)N-\frac{8e}{3}W.
\tag{12}
$$

原 $\mathcal K_\kappa/C$ 对小 $\kappa^2$ 光滑。直接消去 $X_2-C\nu$ 得到对所有 even 母包的恒等

$$
\boxed{
\mathcal B_\kappa-6a_4C\nu
=6a_4C\mathcal F_\kappa+\Gamma_\kappa\mathcal J,
\qquad
\Gamma_\kappa=\frac{d^2-e^2}{d+7e}.
}
\tag{13}
$$

特别在旧 $\mathcal F_\kappa=0$ 门上，新 leading 条件是 $\mathcal J=0$。这不是任意附加一个积分值，因为 §5 将用真实扰动支付它。

实际取 $0<\kappa^2<1/9$。此时

$$
\Gamma_\kappa
=\frac{\kappa(1-9\kappa^2)(39\kappa^2+1)}
 {4h_e(81\kappa^2+7)}\ne0,
\tag{14}
$$

而 $\Gamma_\kappa/\kappa$ 光滑且在零处非零。本稿没有假用不保证属于安装小邻域的特殊值 $\kappa^2=1/9$。

## 4. 两斜率使本层两个 even 条件准确同向

保持 R269 的两斜率
$\beta=(5-\alpha)/(1-\alpha)$，$1/3<\alpha<1/2$。
每个最小实际包上，$(a_i/b_i)^2$ 等于 $\alpha$ 或 $\beta$；共同实幅度与伴随的 $g$ 符号不改变这个事实。逐项有

$$
a_i^2(a_i^2-5b_i^2)
=\alpha\beta\, b_i^2(a_i^2-b_i^2).
\tag{15}
$$

本 pair 的跨包核全零，所以 R259 的上三角式没有剩余 history 项。
因此它的两个 even 系数准确满足

$$
\boxed{\mathcal E_{22}=\alpha\beta\mathcal E_{04}.}
\tag{16}
$$

这对任意同包 self 权都成立，不只对 (9) 的 leading 项。两个 odd 系数仍由原十二完整复制清零。故对一个完整两斜率 block，只需准确解 $\mathcal E_{04}=0$，便支付整个 (2)。

把八/十二复制也纳入，令 $\mathcal W>0$ 为共同四次权和，$\bar V_L,\bar V_H$ 及 $\bar M_{4,L},\bar M_{4,H}$ 为实际中心 shape 坐标的加权二、四矩。两类总中心为零，三次中心矩也为零：两种原排序各自中心反演对称，两层正四次复制权也关于中点对称。令 block 的最后物理中心为 $\xi_0>0$，低/高实际宽为 $\delta q,\delta$，$a=q(1-\alpha)$。由 (9) 准确得到

$$
\begin{aligned}
\frac{\mathcal E_{04}}{64na\mathcal W\delta}
={}&\xi_0^2(1-q^2)(\mathcal B_\kappa-6a_4C\nu)\\
&+\delta^2\big[
a_4C(\bar M_{4,H}-\bar M_{4,L})
+\mathcal B_\kappa(\bar V_H-q^2\bar V_L)
+\mathcal D_\kappa(1-q^4)\big].
\end{aligned}
\tag{17}
$$

用了准确方差差 $\bar V_L-\bar V_H=\nu(1-q^2)$。
式 (17) 保留完整有限 $\delta$ 余项；仅令 $\mathcal J=0$ 并不足以使真实 $\mathcal E_{04}$ 为零。后文把 (17) 整体放入主隐函数定理。

## 5. 一个真实奇扰动，且其响应严格非零

取非零 real even $v\in C_c^\infty$。定义

$$
N_0(v)=\int v'(v'')^3,\qquad
e_v=\operatorname{EL}(N_0)
=12r^2t+6v't^2+6v'r r'',\quad r=v'',\ t=v'''.
\tag{18}
$$

$e_v$ 为紧 odd 函数。记

$$
K=\int e_v^2.
$$

这里严格 $K>0$，无需 generic 假设。因为

$$
\frac{e_v}{6}
=\left(v'rt+\frac{r^3}{3}\right)'.
$$

若 $e_v\equiv0$，平端使括号为零，进而
$(v'r^3)'=r^4+3v'r^2t=0$，平端再给 $v'r^3=0$。
在 $r\ne0$ 的任一开区间便有 $v'=0$，与 $r=v''\ne0$ 矛盾；故 $r\equiv0$、$v=0$，矛盾。

置 $v_\eta=v+\eta e_v$。反射给
$N_0(v_{-\eta})=-N_0(v_\eta)$，真实变分给
$DN_0(v)[e_v]=K$，故准确的四次多项式有

$$
N_0(v_\eta)=K\eta+O(\eta^3).
\tag{19}
$$

这是真实函数的正响应，不是指定一个抽象 shape 常数。

## 6. 保持整个母包 even 的三变量形状

固定 $L_*=1/2$。在原中央幅/宽 $\gamma,s>0$ 外，加实际参数 $z$，令 $\eta=hz$，并定义

$$
\begin{aligned}
u_{\gamma,s,h,z}(y)
={}&\gamma(sh)^{3/2}v(y/(sh))\\
&+h^{3/2}v_{hz}((y-L_*)/h)\\
&+h^{3/2}v_{hz}(-(y+L_*)/h).
\end{aligned}
\tag{20}
$$

右、左两项互为镜像，所以整个 $u$ 严格 even。先在有限参数邻域取小正 $h$，三支撑严格不交；$\gamma,s$ 近1，所有实际宽度正。

辅助母坐标可以跨零；本节只用已写出的多项式微分积分。最终外包置入正物理区间以后才使用原物理算子，不在辅助零点擅用含 $1/x$ 的另一表示。

原 R256/R267 归一母条件为

$$
\mathcal H(u)=27\nu(u)-\frac{K_2(u)}{A_0(u)},
\quad
A_0(u)=\int(u'')^2(u''')^2,
$$

$$
K_2(u)=27\int y^2(u'')^2(u''')^2
-20\int yu''u'(u''')^2
+2\int\{(u')^2+u''u\}(u''')^2.
\tag{21}
$$

与 $\mathcal F_\kappa$ 同时保留。新的形状方程为 $\mathcal J(u)/h=0$。

先核真实归一极限。记
$m(\eta)=\int(v_\eta'')^2$、
$\mu_1(\eta)=\int y(v_\eta'')^2$、
$\mu_2(\eta)=\int\{y^2(v_\eta'')^2+2(v_\eta')^2\}$。
准确有

$$
m(u)=\gamma^2m(0)+2m(hz),
$$

$$
I_2(u,u)=\gamma^2s^2h^2\mu_2(0)
+2\{L_*^2m(hz)+2L_*h\mu_1(hz)+h^2\mu_2(hz)\}.
\tag{22}
$$

$m,\mu_2$ 为 $\eta$ 的 even 多项式，$\mu_1$ 为 odd；
因此新增中心交叉 $h\mu_1(hz)$ 仅为 $O(h^2)$，没有遗漏一个常阶 $z$ 项。

同样，$h^3A_0,h^3K_2,hC,h\mathcal K_\kappa$ 由真实换元是参数解析函数。其新增 odd 中心项也都带 $h\eta=h^2z$；所有偶能量的 $\eta$ 一阶项为零。因此在 $h=0$，

$$
\mathcal H_0=54L_*^2
\left(\frac1{\gamma^2+2}-\frac1{\gamma^4s^{-3}+2}\right),
$$

$$
\mathcal F_0=2L_*^2
\left(\frac1{\gamma^4s^{-1}+2}-\frac1{\gamma^2+2}\right),
\tag{23}
$$

且两式的 $z$ 导数为零。这只延拓有限标量，不把零宽 profile 当合法输入。

对 $\mathcal J$ 则有更直接的完整公式：

$$
\boxed{
\frac{\mathcal J(u_{\gamma,s,h,z})}{h}
=\gamma^4s\,\mathcal J(v)+2\mathcal J(v_{hz})
-\frac{4L_*}{h}N_0(v_{hz}).
}
\tag{24}
$$

由 (19)，其解析零宽值为

$$
(\gamma^4s+2)\mathcal J(v)-4L_*Kz.
\tag{25}
$$

取
$z_0=3\mathcal J(v)/(4L_*K)$。在 $(\gamma,s,z,h)=(1,1,z_0,0)$，
三个真实归一条件都为零，形状 Jacobian 是

$$
\begin{pmatrix}
12L_*^2&-18L_*^2&0\\
-4L_*^2/9&2L_*^2/9&0\\
4\mathcal J(v)&\mathcal J(v)&-4L_*K
\end{pmatrix}.
\tag{26}
$$

其行列式 $64L_*^5K/3\ne0$。实际隐函数定理给小正 $h$ 的
$\gamma_h,s_h=1+O(h^2)$、$z_h=z_0+O(h^2)$；
真实 odd 扰动幅 $hz_h=O(h)$，并且三个原积分条件准确成立。
这里不要求 $z_0=0$，也未以它代替原中央幅度或宽度。

## 7. 四个主变量同时支付完整有限宽方程

固定留有严格间隙的小正 $h$，以后不再令它趋零。选择 R269 两种排序中的任一种，在该 block 的最终正物理区间中取中心 $\xi_0$。然后固定有限间距 $\Lambda$、八/十二完整复制及其共同四次加权中心零。

主方程是

$$
F=\delta^3L_c=0,\qquad
G=\delta(M_c+3L_c/\xi_0)=0,\qquad
\mathcal F_\kappa=0,\qquad
\mathcal E_{04}=0.
\tag{27}
$$

对最后一式使用 (17) 的解析归一函数

$$
\mathcal R=
\frac{\mathcal E_{04}}
 {64na\mathcal W\delta\,\xi_0^2(1-q^2)\Gamma_\kappa h}.
\tag{28}
$$

$\delta>0$ 时分母非零。由 (13)、(17)，在 $\delta=0$，

$$
\mathcal R_0
=\frac{\mathcal J(u)}h+
\frac{6a_4C}{\Gamma_\kappa h}\mathcal F_\kappa(u).
\tag{29}
$$

因此在母根上 $\mathcal R_0=0$；从第四 Jacobian 行减去第二项系数乘第三行后，形状三行恰为
$\mathcal H,\mathcal F_\kappa,\mathcal J/h$，其非退化已由 (26) 在实际正 $h$ 延续。

R256 的第一行在唯一简单 $\alpha_0$ 根处只有非零的 $\alpha$ 导数，形状导数都乘原 $P(\alpha_0)=0$。第二行在同根处是非零因子乘 $\mathcal H$；所有未求根前的共同 copy 方差项仍保留。因此四式对 $(\alpha,\gamma,s,z)$ 的完整 Jacobian 可逆。

真实 IFT 给充分小正 $\delta$ 的四个参数，使 (27) 全部准确为零。
特别使用的是 (17) 的整式，不是删掉其 $\delta^2$ 余项；(16) 和原 odd 包装遂支付整个 (2)。

所有归一式除去显式公共 $\kappa$ 后对小 $\kappa^2$ 光滑；例如 (28) 只使用 $a_4/\Gamma_\kappa$ 等在 $\kappa=0$ 有解析极限的比值。可先在紧小 $\kappa^2$ 区间统一取正 $h$、有限间距、正 $\delta$，再选择原联合安装允许的非零小 $\kappa$。没有从逐固定 $\kappa$ 的未控阈值擅推一条联合曲线。

## 8. 新 odd 扰动不破坏 TM3 同源伴随

为了同时保 R269 的 pure 正负方向，母 $v$ 从一开始取 R265 的真实形式

$$
v=\sum_{j=0}^7\psi(\,\cdot-t_j),\qquad
\widehat v=\sum_{j=0}^7\epsilon_j\psi(\,\cdot-t_j),
$$

其中 $\psi$ 为 real even 紧包、对称不交中心 $t_j$ 及原 TM3 符号 $\epsilon_j$。
由于 (18) 是 local 微分多项式，支撑不交时

$$
e_v=\sum_j e_\psi(\,\cdot-t_j).
$$

于是定义
$\widehat v_\eta=\sum_j\epsilon_j(\psi+\eta e_\psi)(\,\cdot-t_j)$，
便在每个最小子包上保持同一 profile，只翻转第二方向的符号。对所有所需导阶，

$$
v_\eta^{(p)}v_\eta^{(q)}
=\widehat v_\eta^{(p)}\widehat v_\eta^{(q)}.
\tag{30}
$$

单子包现在不必 even，但三交叉矩仍是中心的次数至多2多项式，TM3 准确消掉它们。与 (20) 配套，明确取

$$
\begin{aligned}
\widehat u(y)={}&\gamma(sh)^{3/2}\widehat v(y/(sh))\\
&+h^{3/2}\widehat v_{hz}((y-L_*)/h)
-h^{3/2}\widehat v_{hz}(-(y+L_*)/h).
\end{aligned}
$$

中央 $\widehat v$ 为 odd，故 $\widehat u$ 也是 odd；左项负号只翻转第二方向。每个最小子包的同源平方恒等保持，三个母子包各自的三交叉矩都为零，因而整个母 pair 仍满足原接口。

完整 $M_4,M_1,N_1$ 也没有遗漏：带一个或三个伴随因子的项在每个八子包组内由 TM3 的零/一次矩消去；不带奇伴随因子的 $N_1=\int u'(u'')^3$ 因整个 $u$ 为 even 而为零。其他四次 even 矩由原两斜率及每组均值支付。因此 pure $\mathscr Q$ 的共同平移规律仍与 R269 相同。

新 pair (2) 的 even self 只用每个最小子包的实幅度平方，且其 cross 核为零，所以伴随替换保持准确的 $\mathcal E_{04}=0$。全部 odd 项仍依赖完整十二复制；本稿没有以平方相同直接跳过 odd 条件。

八复制的完整第三闭合仍按 R183 的微包比例与第七差分成立；十二复制的平移次数上界仍由原算子给出。新 odd 母扰动没有改变这些次数或同锚约定。

## 9. 已付有序面积符号与最后四个 block

需要重新核新母包的符号，不能只引用旧参数根。由 (20) 的真换元和 $\eta=hz_h=O(h)$，所有 even 形状常数只在旧 leading 中出现 $O(h^2)$ 改变，中心一阶矩项带 $h\eta$。于是

$$
C\nu-\mathcal L=O(h),\qquad
\Delta/4=2L_*m_v^2+O(h),
$$

$$
\boxed{C\nu-\mathcal L+\Delta/4>0}
\tag{31}
$$

在先选的小正 $h$ 上具有严格余量。第一式保 $\gamma_h,s_h=1+O(h^2)$ 的原抵消；第二式是三个母子包的真实二次密度距离积分，其首项未改变。

R269 的原方向负 $\mathscr Q$、伴随正 $\mathscr Q$、居中正 $S_{04}$ 及重排负 $S_{04}$ 的准确公式因此都仍适用，常数必须取当前真实母包。固定 $h$ 后，它们所有不带间距 $A$ 的项有限；选择一个足够大的有限 $\Lambda$ 留下各严格号，随后才进行 §7 的四变量主 IFT。小正 $\delta$ 的连续性保持这些号。

在四个最后不交物理区间中，分别构造两种次序与两种方向的四个完整 block，每个都先准确解自己的四式 (27)。之后按 R269：

1. 各次序内部用正四次幅度清 pure $\mathscr Q$；
2. 再在两种次序间用正四次幅度清完整 $S_{04}$。

所有旧条件和新增 (2) 均在每个 block 内已为零。R259 跨完整 block 核因 inner 完整三矩为零消失；本 pair 本身甚至没有跨微包核。故上述正幅相加保持全部已付条件，R269 的 $E_{22}-E_{04}=-\operatorname{Re}\mathscr Q$ 仍支付整个 $A_{1,-3}$ 第零外矩。

不同 block 的实际 $\alpha,\gamma,s,z,\delta$ 可以不同；(16) 只需在各 block 内使用，而不要求混合后仍有统一两斜率参数。我们先各自支付其全角零，再相加，不能把一条旧两斜率等式越界强加给混合后的整圆。

## 10. 结论范围

新参数是一个真实 $C_c^\infty$ 母形方向；其非零导数由 (18)—(19) 的严格积分证明支付。两个宽度层的 IFT 分开：先固定小正母宽 $h$ 并得到非退化三形状根，再选择实际有限次序/复制间距，最后用四个真实参数求主正宽 $\delta$ 的完整能量和面积方程。所有最后 profile 的宽度、幅度、间隙严格正有限，没有取零宽对象充当答案。

当前准确已付的是：

- 三矩、原完整第二与第三 range；
- 共振 germ 的六个已识别能量；
- 整个 $A_{-2,-3}$ 与整个 $A_{-1,-3}$；
- 六 Gaussian 面积的全部36个 odd 角条件；
- 整个 $A_{1,-3}$ 和整个 $A_{1,-1}$ 的第零外矩。

仍有20条形式 even 等式未支付，不宣独立；其余零/一层 history、完整第四 period、完整有限等距族、嵌入、reach 和宏观幅度也不由本稿成立。共同正归一化保全部齐次零；构造选择新的 profile 圆及种子目标，不冒原 fixed-seed 的一次允许变形。

本稿没有执行或请求研究计算。