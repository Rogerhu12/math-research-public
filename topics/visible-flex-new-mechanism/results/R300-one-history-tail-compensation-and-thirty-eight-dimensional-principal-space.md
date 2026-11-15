# R300：完整一层 Gaussian 的真实尾、38维主空间与未付低阶相容

日期：2026-11-15。**完整纸面原式推导。** 本稿没有执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R296](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md) 已从原第四恢复准确分离零层与四个一层 Gaussian 系数，并证明一层确有此前二层主空间没有覆盖的方向。本稿先给这四个一层系数的**完整相位与真实尾接口**，再把其全部 $\theta=\pi/2$ 系数写成120行的准确有限呈示，证明实际 even principal 秩为38。旧三十二必要量只占其中30维，故可再联付八个独立一层观察；其余原行留下明确的有限 $C^2$ 相容门。本稿不处理零层及其 $\mathcal W_e$ 商，也不把主秩当成全部函数可解。

结论是：从实际圆的最初选择起，把下文明确的有限连续 $C^2$ 多项式观测并入 R293 的观察映射，可以在保持三矩、全部真实有序面积、六能量、完整第三及已付二层的同一个有限频率圆上，使每个一层系数准确满足
$$
\mathscr R_{\rho,\theta}(\sigma)
=\sin^2\theta\,\mathscr R_{\rho,\pi/2}(\sigma).
$$
因此一层的全角缺口可准确缩到四个原 $\sigma$ 函数，而非二十个未经归约的相位函数。[R299](R299-complete-centered-ruling-angular-reduction-by-corrected-pure-self-fibers.md)已给包含零层的更强全 germ 角归约；本稿第2–8节保留可直接核对的逐一层有序核，后半的新任务是四个实际函数的主空间与低阶相容。四个函数仍须整个支付。

主要来源：[R56 原恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 全八矩](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221 局部三线性式](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R259 全八算子 local adjoint 与真实尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R280 三个真实矩面积](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R293 初选任意有限低阶观察纤维](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R294 二层校正 self](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)及 R296。

## 1. 一层的原两类项与共同约定

固定同一真实几何、共同正 profile 区间 $I=[\ell,r_*]$ 和原右积分
$$
Jv(x)=\int_x^{r_*}v(t)\,dt.
$$
沿 R296 的初始安装取共振小参数，不事后修改一个已经冻结的几何。记
$$
e=hx+j,\quad \mathcal Q=1+e^2,\quad z=x+\omega,\quad
hz=e+k,\quad \gamma=h_\sigma,\quad \delta=j_\sigma,\quad
e_\sigma=\gamma x+\delta.
\tag{1}
$$
原矩是
$$
\mathbf I(u,v)=
\left(\int u''v'',\ \int xu''v'',\
\int\{x^2u''v''+2u'v'\}\right),
\quad
\mathcal E_\sigma=\sum_{j_0=0}^2 w_{j_0} I_{j_0},
$$
$$
(w_0,w_1,w_2)=
\left(\frac{1+j^2}{4h},\frac j2,\frac h4\right).
\tag{2}
$$
外矩指标写成 $j_0$，避免与几何 $j$ 混淆。

取原三矩圆，令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
$$
$\odot$ 始终是对称二次槽。四个固定 Gaussian 方向为 $X=B_\rho$，$\rho\in\{1,-1,-2,-3\}$；完整第二历史的 elementary 部分写成
$$
\mathsf Q_\sigma=\sum_{Y\in E_8}q_Y(\sigma)Y.
\tag{3}
$$
这里 $\mathsf Q_\sigma$ 是整个八维算子，不把它缩成四个 Gaussian 方向。R296 的准确一层式为
$$
\boxed{
\mathscr R_{\rho,\theta}
=\mathscr L^X_\theta+
2\sum_{Y\in E_8}\sum_{j_0=0}^2
q_Yw_{j_0}\,\mathscr H^{Y\to X}_{j_0,\theta},
}
\tag{4}
$$
其中
$$
\begin{aligned}
\mathscr L^X_\theta
&=2\mathcal T_\sigma(XD_\theta;D_\theta)
-4\mathcal T_\sigma(\phi_\theta;\phi_\theta,XD_\theta),\\
\mathscr H^{Y\to X}_{j_0,\theta}
&=-I_{j_0}(YD_\theta,XD_\theta)
+2I_{j_0}\{\phi_\theta,Y(\phi_\theta,XD_\theta)\}.
\end{aligned}
\tag{5}
$$
$XD_\theta$ 与 $YD_\theta$ 因原三矩准确紧支撑。方向箭头不能删掉：第二行只含 outer $Y$，并非未经证明可互换的对称 cross。变化 profile 的 chain 仍在 R296 的零层，本稿不把它重新分配到(4)。

## 2. 先写全 $\mathcal T$ 的非紧第一槽 Green 项

R221 的 $K(a,b)$ 分子和第一场分子是
$$
V_K=(\eta_{ab}/h,\ zP_{ab}+b_{ab},\ e\eta_{ab}/h),\qquad
V_c=(-c'/2,\ 0,\ hc-ec'/2).
$$
若 $a,b$ 紧、$c$ 右端为零而左端有二次尾，原物理配对给
$$
\begin{aligned}
\mathcal T_\sigma(c;a,b)
={}&\frac1{2h^2}\int \mathcal Q c'''\eta_{ab}\\
&+\left[\frac{\eta_{ab}}{2h^2}
\left\{hec'-\mathcal Qc''
+\frac{\mathcal Qc'-2hec}{z}\right\}\right]_\ell^{r_*}.
\end{aligned}
\tag{6}
$$
这是先保 $-[V_c\cdot V_K/(hz)]_\ell^{r_*}$，再对 $\eta'$ 真正分部所得；不能把有尾的 $c$ 套进 R221 的 compact 版(15)。

令 $\widetilde{\mathcal T}$ 表示 R221(17)的显示局部多项式表达，允许把带尾 $c$ 代入该**表达**。它不因此自动等于物理 $\mathcal T$。置
$$
F_c=\mathcal Qc''-2hec'+2h^2c,\qquad F_c'=\mathcal Qc'''.
$$
真实 Fubini 使用 $F_c(x)-F_c(\ell)$。因右端值为零，(6)准确化为
$$
\boxed{
\mathcal T_\sigma(c;a,b)-\widetilde{\mathcal T}_\sigma(c;a,b)
=-\frac{\eta_{ab}(\ell)}{2h^2}
\left.\frac{(1-ke)c'+2hkc}{z}\right|_\ell .
}
\tag{7}
$$
这里用的仅是 $hz=e+k$。后面整个 $XA$ 若由合法零三矩槽 $A$ 产生，则它真紧，(7)为零；单个 $X(u_i^2)$ 一般不紧，不能逐包删(7)。

真实左值只依赖原三矩 $\mathbf m=\mathbf I(u,u)$：
$$
\boxed{
\eta_-(\mathbf m)=
\frac{[\gamma(1+j^2)-2hj\delta]m_0
-2h^2\delta m_1-h^2\gamma m_2}{16h^2}.
}
\tag{8}
$$
它就是 $-\partial_\sigma\mathcal E_\sigma(u,u)/4$，不是新的自由尾变量。

## 3. 二次 inner 尾的准确零配对与 local 有序核

令 $p=Ax^2+Bx+C$ 是来自右方微包的真实二次尾。对紧 $u$ 直接代 R221(14)，原 $J(u)$ 项成对抵消，得
$$
\boxed{
\eta(u,p)=
\frac{\gamma B-2A\delta}{16h^2}F_u .
}
\tag{9}
$$
因此
$$
\boxed{
\mathcal T_\sigma(u;u,p)
=\frac{\gamma B-2A\delta}{32h^4}
\int \mathcal Q u'''F_u
=\frac{\gamma B-2A\delta}{64h^4}[F_u^2]_\ell^{r_*}=0.
}
\tag{10}
$$
只要求 $p$ 在该 outer 支撑的邻域等于上述多项式；取 cutoff 不改变原 mixed integrand。式(10)不是把 inner 左尾置零。

同一个多项式满足
$$
F_p=2\{(1+j^2)A-hjB+h^2C\},
\tag{11}
$$
它关于 $x$ 为常数。故另一种次序的 formal 表达准确为
$$
\widetilde{\mathcal T}_\sigma(p;u,u)
=\frac{F_p\,\eta_-(\mathbf m(u))}{2h^2}.
\tag{12}
$$

定义两个二次槽上的 local bilinear 结构
$$
\begin{aligned}
\mathcal B_{\rm loc}^X(A,B)
&=-\widetilde{\mathcal T}(XA;B)
-\widetilde{\mathcal T}(XB;A),\\
\mathcal C_{\rm loc}^X(u\odot v,B)
&=-2\{\mathcal T(u;v,XB)+\mathcal T(v;u,XB)\},\\
\mathcal K_{\rm loc}^X&=\mathcal B_{\rm loc}^X+\mathcal C_{\rm loc}^X .
\end{aligned}
\tag{13}
$$
在合法 whole 槽上，(7)保证
$\mathscr L^X=-\mathcal B_{\rm loc}^X(D,D)+
\mathcal C_{\rm loc}^X(\phi^2,D)$。

令 $p_X(\mathbf n)$ 为原 $X$ 对应的真实二次尾。由(10)—(12)，左 outer 微包矩 $\mathbf m$ 与右 inner 矩 $\mathbf n$ 的完整 local 有序核是
$$
\boxed{
\Gamma_{\rm loc}^X(\mathbf m,\mathbf n)
=-\frac{\eta_-(\mathbf m)F_{p_X(\mathbf n)}}{h^2}.
}
\tag{14}
$$
这是全部跨包贡献；其反对称部分是原三矩的普通双线性楔。它不是仅保某一个 local 主项。

## 4. local 校正 self 确为 $C^2$ 多项式观测

置 $v=u'$、$r=u''$，并定义以下真实 compact cubic：
$$
\mathcal G_\sigma(u)=\mathcal T_\sigma(u;u,u)=\int g_\sigma(x,u,v,r).
$$
一个直接可审的密度是
$$
\begin{aligned}
F&=\mathcal Qr-2hev+2h^2u,\\
D&=(\gamma\mathcal Q-2hee_\sigma)r^2-2h^2\gamma v^2,\\
\Psi&=\gamma\mathcal Q^2vr^2-\frac{e_\sigma\mathcal Q^2}{3}r^3
-2h\gamma e\mathcal Qv^2r,\\
g_\sigma&=\frac{FD-(\partial_x+v\partial_u+r\partial_v)\Psi}{32h^4}.
\end{aligned}
\tag{15}
$$
因为 $\Psi_r$ 正是 R221(17) 中 $u'''$ 的系数，(15)仅将那个线性三导项作一次真实分部。compact 端点的 $\Psi$ 为零；$g_\sigma$ 的 $x$ 次数至多4。

对任意原 $X(u,u)$，定义
$$
D_{\rm loc}\mathcal G_\sigma(u)[Xu^2]
=\int(g_uXu^2+g_v(Xu^2)'+g_r(Xu^2)'').
$$
这是密度表达，不把带尾方向假称为允许的 compact 变化族。在 $\widetilde{\mathcal T}$ 的 cubic 原式求一阶变化时，$\Psi$ 的端点一阶变化准确为零，因为 compact 基点的 $u,v,r$ 全为零。因此 formal self 为
$$
\mathcal K_{\rm loc}^X(u^2,u^2)
=-2D_{\rm loc}\mathcal G_\sigma(u)[Xu^2].
\tag{16}
$$
这一步已经包含(7)区分的物理/表达差；没有将 physical noncompact self 无偿换成 compact self。

结合(14)，校正值是
$$
\boxed{
\widehat k_{\rm loc}^X(u)
=-2D_{\rm loc}\mathcal G_\sigma(u)[Xu^2]
+\frac{\eta_-(\mathbf m)F_{p_X(\mathbf m)}}{2h^2}.
}
\tag{17}
$$
原二次表给 $(Xu^2)''=\alpha_Xu'''+\beta_X$，其中 $\alpha_X$ 为 local 一次多项式，$\beta_X$ 只需 $u,u',u''$ 及三个真实 quadratic primitives。因此(17)至多有一个线性三导项 $A(x,u,v,r)u'''$，没有三导平方。用
$$
A u'''=D_x\!\left(\int_0^rA(x,u,v,s)\,ds\right)
-\left(\partial_x+v\partial_u+r\partial_v\right)
\left(\int_0^rA(x,u,v,s)\,ds\right)
\tag{18}
$$
准确去掉它；端点原函数为零。其余项以及(17)最后的原矩乘积都是连续四次 polynomial/$C^2$ 泛函。

所有几何因子仍属于 R221 的18个生成元
$$
\gamma h^{i-4}j^k,\quad \delta h^{i-4}j^k,\qquad
i+k\in\{0,2,4\}.
\tag{19}
$$
将(17)按(19)取系数，得到18个明确观测 $\widehat k_{\alpha,X}^{\rm loc}$。这些生成元可以在具体端芽上相依，计数不宣秩。

## 5. directed history 的完整八维核，不能借旧面积略过

令 $Y$ 为全 $E_8$ 中任一方向，$X=B_\rho$。对原外矩 $j_0$ 定义
$$
\begin{aligned}
\mathcal B^{Y\to X}_{j_0}(A,B)
&=\frac12\{I_{j_0}(YA,XB)+I_{j_0}(XA,YB)\},\\
\mathcal C^{Y\to X}_{j_0}(u\odot v,B)
&=I_{j_0}\{u,Y(v,XB)\}+I_{j_0}\{v,Y(u,XB)\},\\
\mathcal K^{Y\to X}_{j_0}&=\mathcal B^{Y\to X}_{j_0}
+\mathcal C^{Y\to X}_{j_0}.
\end{aligned}
\tag{20}
$$
式(5)第二行正是 $-\mathcal B(D,D)+\mathcal C(\phi^2,D)$。不要求 $(Y,X)$ 的完整面积预先为零。

以下列出全八个原尾与作用，供(22)直接读取。$p=Ax^2+Bx+C$，
$D_-u=u'$、$D_0u=xu'-u$、$D_+u=x^2u'-2xu$：
| 方向 | 原 $p_X(\mathbf m)$ | 原 $X(u,p)$ |
|---|---|---|
| $P=\Phi_{r_0}$ | $m_0$ | $-2A D_-u$ |
| $R=\Phi_{r_1}$ | $m_0x$ | $B D_-u$ |
| $S=\Phi_{s_0}$ | $m_1$ | $-2A D_0u$ |
| $L=\Phi_{p_0}$ | $-m_0x^2/4+m_2/4$ | $(C/2)D_-u-(A/2)D_+u$ |
| $U=\Phi_{s_1}$ | $m_1x+m_2/2$ | $B D_0u-A D_+u$ |
| $\Phi_{p_1}$ | $-m_1x^2/4$ | $(C/2)D_0u$ |
| $\Phi_{t_1}$ | $m_2x$ | $B D_+u$ |
| $V=\Phi_{p_2}$ | $-m_2x^2/4$ | $(C/2)D_+u$ |

记最后列系数为 $\mathbf a_Y(p)$。三个原外矩给
$$
\mathbf t_-(\mathbf m)=(0,-m_0,-2m_1),\quad
\mathbf t_0(\mathbf m)=(m_0,0,-m_2),\quad
\mathbf t_+(\mathbf m)=(2m_1,m_2,0).
\tag{21}
$$
它们等于 $2\mathbf I(u,D_\bullet u)$，不省略 $I_2$ 的一阶项。

对两个真实二次尾 $p=A_px^2+B_px+C_p$、$q=A_qx^2+B_qx+C_q$，沿 R294 保
$$
\begin{aligned}
\beta_0(p,q)&=-2A_q(2A_p\ell+B_p),\\
\beta_1(p,q)&=-2A_q(A_p\ell^2-C_p),\\
\beta_2(p,q)&=-2A_q\ell^2(2A_p\ell+B_p)
-2B_q(A_p\ell^2+B_p\ell+C_p).
\end{aligned}
$$
定义 directed 第三尾
$$
T^{Y\to X}_{j_0}(\mathbf m,\mathbf n)
=\sum_{\bullet=-,0,+}
a_{Y,\bullet}(p_X(\mathbf n))\,t_{\bullet,j_0}(\mathbf m).
$$
于是完整有序核为
$$
\boxed{
\begin{aligned}
\Gamma^{Y\to X}_{j_0}(\mathbf m,\mathbf n)
={}&\beta_{j_0}(p_Y(\mathbf m),p_X(\mathbf n))\\
&+\beta_{j_0}(p_X(\mathbf m),p_Y(\mathbf n))
+T^{Y\to X}_{j_0}(\mathbf m,\mathbf n).
\end{aligned}}
\tag{22}
$$
第三项只有 outer $Y$，系数为1；把它换成 R294 的两个 outer 平均会改变问题。

原 nonlegal self 是
$$
k^{Y\to X}_{j_0}(u)
=I_{j_0}(Yu^2,Xu^2)+2I_{j_0}\{u,Y(u,Xu^2)\}.
$$
R259 的真实 cutoff adjoint 与 Green 项给
$$
k^{Y\to X}_{j_0}
=D_{\rm loc}F_{Y,j_0}[Xu^2]+\beta_{j_0}(p_X,p_Y).
$$
故
$$
\boxed{
\begin{aligned}
\widehat k^{Y\to X}_{j_0}(u)
={}&k^{Y\to X}_{j_0}(u)
-\tfrac12\Gamma^{Y\to X}_{j_0}(\mathbf m,\mathbf m)\\
={}&D_{\rm loc}F_{Y,j_0}[Xu^2]
+\tfrac12\{\beta_{j_0}(p_X,p_Y)-\beta_{j_0}(p_Y,p_X)\}\\
&-\tfrac12T^{Y\to X}_{j_0}(\mathbf m,\mathbf m).
\end{aligned}}
\tag{23}
$$
其中 $F_{Y,j_0}(u)=I_{j_0}(u,Yu^2)$ 的24个 local cubic 密度由 R259(11)给全。

这保住了 directed 差项。三个 $\beta$ 差依次是
$$
2(A_XB_Y-A_YB_X),\quad
2(A_YC_X-A_XC_Y),\quad
2(B_XC_Y-B_YC_X),
\tag{24}
$$
均与任选左 collar $\ell$ 无关。与(18)同样，(23)唯一三导仅线性出现，其系数 local，准确降为连续四次 $C^2$ 观测。无需单包 inner 紧，也无需 $(Q_\sigma,X)$ 属于原六 Gaussian pair。

## 6. 两类角余项都只剩校正 self 与原三个面积

对任一上面明确的 $\mathcal B,\mathcal C$，令 $\mathcal K=\mathcal B+\mathcal C$。设
$$
F=f^2,\quad G=g^2,\quad \Delta=F-G,\quad H=f\odot g.
$$
有 $D=s^2\Delta-2scH$。在原十二完整副本准确清掉 odd 角项以后，
$$
\boxed{
q_\theta=s^2q_{\pi/2}+s^2c^2\Xi,\qquad
\Xi=\mathcal K(\Delta,\Delta)-4\mathcal K(H,H).
}
\tag{25}
$$
这是原二次槽的完整四次身份，对 directed $\mathcal C$ 同样成立；没有假定两个二次槽互换对称。

令不交实微包从左到右为 $u_i$，
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad
\mathbf m_i=\mathbf I(u_i,u_i).
$$
保原真实三矩
$$
\sum_iR_i\mathbf m_i=0,\qquad
\sum_iT_i\mathbf m_i=0.
\tag{26}
$$
按(14)或(22)完整展开后，统一有
$$
\boxed{
\Xi=\sum_i(R_i^2-4T_i^2)\widehat k(u_i)
+\sum_{0\le a<b\le2}\gamma_{ab}\mathcal A_{ab},
}
\tag{27}
$$
$$
\mathcal A_{ab}=
\sum_{i<k}(R_iR_k-4T_iT_k)
(m_{a,i}m_{b,k}-m_{b,i}m_{a,k}),
\quad
\gamma_{ab}=(M_{ab}-M_{ba})/2.
\tag{28}
$$
$M$ 是相应准确 $\Gamma(\mathbf m,\mathbf n)=\mathbf m^TM\mathbf n$ 的矩阵。证明是先用(26)消其对称部分：
$$
\sum_{i<k}(R_iR_k-4T_iT_k)\Gamma_{\rm sym}(\mathbf m_i,\mathbf m_k)
=-\frac12\sum_i(R_i^2-4T_i^2)\Gamma(\mathbf m_i,\mathbf m_i).
$$
剩余恰为(27)。这三条面积就是 R280 的原规范，含真实
$m_2=\int x^2u''{}^2+2u'{}^2$；没有把它换成点质量矩。

## 7. 必须从最初规定的新有限观察 $F^1$

本节扩展的是**初始定义**，不是在旧已冻结圆上声称新观测自动保持。

以 R294 的 $F^+$ 为基底，从最初再加入：

1. 对 $Y\in E_8$、$X=B_\rho$、$j_0=0,1,2$ 的(23)，取其共同平移 $u_t(x)=u(x-t)$ 的全部多项式系数；
2. 对(17)的18个几何系数 $\widehat k^{\rm loc}_{\alpha,X}$，同样取全部平移系数。

全部原二次算子的坐标次数至多4；R259 的 cubic 密度和三外矩使(23)平移次数至多10。式(15)次数至多4，故 local 类至多8；为统一入口也允许保至10的零系数。矩补偿项显然满足同一界。

因此第一类至多 $8\cdot4\cdot3\cdot11=1056$ 个标量，第二类至多 $18\cdot4\cdot11=792$ 个标量，共至多1848个新增生成观察。它们可大量相依；**1848不是秩，也不是新的必需参数数。** 系数可由11个预定合法小平移值的固定插值定义，故连续 $C^2$ 性不要求对 profile 求十阶导。

把这些明确四次 $C^2$ 多项式与旧 $F^+$ 合并为 $F^1$。R293§6允许从起点选定任何这样的有限映射：在正解析母包空间先同时选真实最大秩 minor 与所需 principal witness，再取同 $F^1$ 的有限纠正。这里不另假1848个量能够独立指定，也不将它们的目标统一指定为零。

原等平方背景格点满足
$$
b_i^2=B,\quad R_i\in\{-B/2,8B\},\quad
R_i^2-4T_i^2=\frac{7B}{2}R_i,\qquad
\sum_iR_it_i^d=0\quad(0\le d\le10).
\tag{29}
$$
因此若各微包保持同一母包的 $F^1$ 平移系数，(27)中的每个 self 和准确为零。这不是泛称“低阶不变”，而是逐项使用(17)、(23)、(29)。

原三矩与三个有序面积仍是 $F^+$ 的同一次构造中已付的真实量。每个完整副本的 inner 零三矩使其二次输出紧，故不同完整副本的交叉为零；R183八复制与 R259十二正四次幅副本继续保完整第三并消 odd 角。所有新 quartic 的平移次数仍不超过10，因此原十二差分不需改变。最后正幅混合完整 blocks 时，每一项四次齐次、跨 block 为零，(27)继续成立。实际 seed/目标仍按原从起点构造定义，不在求根后随意移动一个完成的圆。

## 8. 同一个实际有限圆上的准确缩减

**定理。** 从最初以 $F^1$ 代替旧 $F^+$ 运行 R293/R294 的纸面有限频率存在性构造，保持原三矩、全部 Gaussian 面积、三个真实有序矩面积、六能量、完整第三及全部二层。则对全部 $\sigma,\theta$ 和四个 $\rho$，准确有
$$
\boxed{
\mathscr R_{\rho,\theta}(\sigma)
=\sin^2\theta\,\mathscr R_{\rho,\pi/2}(\sigma).
}
\tag{30}
$$

证明由(27)、(29)给两类 $\Xi=0$，再按(4)对实际几何函数线性合并。(19)已包含 local 全几何系数，(3)使用完整八维，所以不是只在有限 $\sigma$ 节点或单个中心 jet 成立。原 R293 同任意有限 $F^\star$ 的有限正频率 $C^1$ 极限及精确 IFT 仍适用；新的 shape 约束不改变三阶 principal，因为纠正的 $C^2$ 范数趋零。证毕。

式(30)将一层全角零准确化成
$$
\mathscr R_{\rho,\pi/2}(\sigma)\equiv0,\qquad
\rho=1,-1,-2,-3.
\tag{31}
$$
它们是四个原函数，不是四个自由标量，更未被(29)支付。R296 的新一层 principal 及非蕴含例继续提醒：已经支付二层不保证(31)。若从起点把该新增一层控制与 $F^1$ 一同构造，可按同一个有限观察扩展保持本稿的全角缩减；也不能把单个 Taylor 必要量当作四函数全部为零。

零层 $\mathscr R_{0,\theta}$、它与 $\mathcal W_e$ 的完整函数成员门、原 canonical periods、同一个二阶 gauge 的联合相容性以及收敛/嵌入/reach均不在本稿已付范围。尤其本稿没有把一层的真实 Green 补偿当成两个非紧场的一般零层公式。


## 9. 四个原函数的准确120行呈示

以下固定共振 $\varepsilon=\kappa^2/4$ 与 $0<\kappa^2<1/100$；它们均在实际几何的初始选择时规定。保
$$
h=h_e e^{\varepsilon\sigma^2},\qquad
j=2\varepsilon\kappa\sigma^2,\qquad
\gamma=2\varepsilon\sigma h,\qquad
\delta=4\varepsilon\kappa\sigma.
$$
原 elementary history 的 $h^r$ 层只在 $r=-3,-2,-1,0,1$。对一个非零 $r$ 的偶多项式 $P(j)$，其真实分解可写成
$$
\int_0^\sigma h(t)^rP(j(t))\,dt
=\sigma h(\sigma)^r Q(j)+h_e^r b E_r(\sigma),
$$
$$
\boxed{
P=(1+rj/\kappa)Q+2jQ'+b.
}
\tag{32}
$$
$Q$ 为普通多项式，$Q'$ 在(32)中表示对 $j$ 求导。$r=0$ 的项直接逐项积分，$j^m$ 给 $\sigma j^m/(2m+1)$。所有初值都是真实中心0；没有用负指数 Gaussian 的极限替代原函数。

R73 及 R296 的原一层式于是准确属于
$$
\boxed{
\mathscr R_{\rho,\pi/2}(\sigma)
=\sigma\sum_{n=-4}^{2}h(\sigma)^n
\sum_{m=0}^{d_n}j(\sigma)^m\,\mathscr O_{\rho,n,m},
}
$$
$$
(d_{-4},d_{-3},d_{-2},d_{-1},d_0,d_1,d_2)
=(5,5,4,4,3,2,0).
\tag{33}
$$
这里 $\mathscr O_{\rho,n,m}$ 是对原式(4)进行有限系数抽取的真实 quartic profile 泛函，含全部局部恢复、右尾和 directed history。每个 $\rho$ 保30个生成行，共120行；某些行可相依或为零。

次数界可直接核：$\mathsf Q$ 的五层最高 $j$ 次数依次为3、3、2、2、0；再乘 $\mathcal E$ 的 $h^{-1}(1+j^2),j,h$ 得(33)。$\mathcal T$ 的18个几何生成元代共振后也落在同一清单内。由于 $e^{\varepsilon\sigma^2}$ 对 $\mathbb R(\sigma)$ 超越，各个(33)的 $\sigma h^n j^m$ 独立。因此四个一层函数整个为零，当且仅当这120个原行全部为零。120是呈示大小，下面另证明其实际 principal 秩。

## 10. 真实 elementary 系数的完整 principal 表

使用 R289 的三个齐次 jet 符号
$$
A=-2u'',\qquad B=2u'-2xu'',\qquad C=u-xu',
\quad V=x^2C-\frac{x^4A}{4},
\tag{34}
$$
分别赋权 $0,1,2,4$，而 $x$ 权1。四个 Gaussian 方向的符号，除去非零 $c,\zeta$，是
$$
A,\qquad W=aB+bxA,\qquad
Z=dC+e_-\left(xB+\frac{x^2A}{2}\right),\qquad V.
\tag{35}
$$
常数沿原共振值：
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{17t^2+4t}{32h_e^2},\quad
d=\frac{6\kappa^3}{h_e},\quad
e_-=-\frac{\kappa(15t+1)}{4h_e},\quad t=\kappa^2.
\tag{36}
$$

R296 的 $\beta=\eta_r^{\rm loc}/h$ 给
$$
2\beta=\frac{\mathcal Q(\gamma B+\delta A)}{8h^3}.
$$
将真实 $\alpha_{\mathsf Q}$ 按(32)归约，有准确表
$$
\boxed{
\alpha_{\mathsf Q}+2\beta
=\sigma\sum_{r=-3}^{1}h^r V_r(j).
}
\tag{37}
$$

| $r$ | $V_r(j)$ |
|---:|---|
| $1$ | $\kappa V/2$ |
| $0$ | $p_0(j)(xC-x^3A/4)+q_0(j)x^2B$ |
| $-1$ | $\ell(j)C+m(j)xB+n(j)x^2A$ |
| $-2$ | $r(j)B+s(j)xA$ |
| $-3$ | $p(j)A$ |

其中全部多项式如下，表中的字母仅是本段系数名，不是新的独立 shape 变量：
$$
p_0=-\frac{\kappa j}{3}+\frac{j^2}{5},\qquad
q_0=\frac{3\kappa^2-2}{16}-\frac{\kappa j}{48}-\frac{j^2}{40},
$$
$$
\begin{aligned}
\ell&=-\frac{\kappa j^2}{2}-2\kappa^2j-\frac\kappa2-6\kappa^3,\\
m&=\frac{\kappa j^2}{4}+\frac{11\kappa^2j}{8}
+\frac{\kappa(15\kappa^2+1)}4,\\
n&=\frac{\kappa j^2}{8}+\frac{5\kappa^2j}{8}
+\frac{\kappa(16\kappa^2+1)}8,
\end{aligned}
$$
$$
\begin{aligned}
r&=\frac{\kappa j^3}{16}+\frac{\kappa^2j^2}{4}
+\frac{\kappa(17\kappa^2+4)j}{32}
+\frac{\kappa^2(51\kappa^2+14)}{64},\\
s&=\frac{\kappa^2j^2}{8}+\frac{7\kappa^3j}{16}
+\frac{\kappa^2(17\kappa^2+4)}{32},\\
p&=\frac{\kappa^2j^3}{24}+\frac{5\kappa^3j^2}{36}
+\frac{\kappa^2(18+41\kappa^2)j}{216}
+\frac{\kappa^3(41\kappa^2+27)}{216}.
\end{aligned}
\tag{38}
$$

这些数来自真实 $M$，可不运行任何程序而逐项验证。例如共振时 $M_{s_1}=-(j+j^3)/(4h)$；用(32)求出的 elementary 多项式是
$$
Q_{s_1}=\kappa j^2/4+5\kappa^2j/4+\kappa(15\kappa^2+1)/4.
$$
其余常数余项恰为原 $B_{-1},B_{-2},B_{-3}$ 的真实系数；$h^1$ 部分是 $\kappa\sigma h V/2-\kappa h_eE_1V$。加上显示的 $2\beta$ 得(38)，没有自由挑选一个更大的 coefficient 空间。

R296 原式给(33)的全部 principal：
$$
\mathscr R_{\rho,\pi/2}\equiv_2
\sum_i\lambda_i\int
\alpha_{B_\rho}\,
\frac{\mathcal Q}{2h}(\alpha_{\mathsf Q}+2\beta)
(u_i''')^2,\qquad
\lambda_i=-a_i^2R_i.
\tag{39}
$$
$\equiv_2$ 表示差为真实连续 $C^2$ 数据，而非差已为零。由(37)定义
$$
K_n(j)=\frac{x^2}{2}V_{n-1}(j)
+jxV_n(j)+\frac{1+j^2}{2}V_{n+1}(j),
\tag{40}
$$
不在 $[-3,1]$ 的 $V_r$ 为零。各 $K_n$ 的 $j$ 系数就是共同 principal 的全部实际生成符号。

### 10.1 七个真实 coefficient 空间的维数

令 $\mathscr L_d$ 表示权 $d$ 的线性 jet 多项式空间：
$$
\mathscr L_0=\operatorname{span}\{A\},\quad
\mathscr L_1=\operatorname{span}\{xA,B\},\quad
\mathscr L_d=\operatorname{span}\{x^dA,x^{d-1}B,x^{d-2}C\}\ (d\ge2).
$$
由(38)—(40)，得到的是准确空间，不只是次数上界：
$$
\boxed{
\begin{array}{c|ccccccc}
n&-4&-3&-2&-1&0&1&2\\ \hline
\operatorname{span}[j^m]K_n&
\mathscr L_0&\mathscr L_1&\mathscr L_2&
\mathscr L_3&\mathscr L_4&
\operatorname{span}\{xV,x^4B\}&
\operatorname{span}\{x^2V\}\\
\dim&1&2&3&3&3&2&1
\end{array}}
\tag{41}
$$

给出非退化的逐项依据，避免将最大次数直接当秩：

- $K_{-4}$ 的 $A$ 系数有非零 $j^5$ 项；$K_{-3}$ 的 $B$ 系数最高项 $\kappa j^5/32$，$xA$ 系数最高项 $5\kappa^2j^4/48$，所以两列独立。
- 对 $K_{-2}=c_2C+b_2xB+a_2x^2A$，令 $E=b_2+3c_2/4$、$D=a_2+c_2/4$。$c_2$ 的四次首项是 $-\kappa j^4/4$，$E$ 的三次首项是 $3\kappa^2j^3/16$，而 $D-(10/9)E$ 的二次首项是 $7\kappa^3j^2/12$。三次序准确不退化。
- 用基 $(xC-x^3A/4,x^2B,x^3A)$ 写 $K_{-1}$，三个系数记 $c_1,b_1,d_1$。$c_1$ 四次首项为 $j^4/10$；$b_1+c_1/8$ 三次首项为 $3\kappa j^3/16$；$d_1$ 二次首项为 $3\kappa^2j^2/16$。
- 用基 $(V,x^3B,x^4A)$ 写 $K_0$，系数 $c_0,b_0,d_0$ 满足：$c_0$ 三次首项 $j^3/5$，$b_0+c_0/8$ 二次首项 $\kappa j^2/16$，$d_0=\kappa^2(j+4\kappa)/16$。
- $K_1$ 在 $(xV,x^4B)$ 上的系数分别是
$$
\frac{\kappa j}{3}+\frac{j^2}{10},\qquad
\frac{3\kappa^2-2}{32}-\frac{\kappa j}{96}-\frac{j^2}{80}.
$$
前者常数零，后者常数非零；两者独立。$K_2=\kappa x^2V/4$。

每个断言都只用显示的有限多项式身份。没有执行消元、采样或把数值小量当成非零证明。

## 11. principal 的自由符号维数40与实际 even 秩38

四个一层函数彼此由真实 Gaussian 字独立性分离；同一函数内的 $h^n j^m$ 也已在(33)分离。因此它们的 principal 空间准确是四个实际方向(35)分别乘(41)的空间之和。

记 $\mathscr H_d$ 为权 $d$ 的全部二次 jet 多项式。其维数依次为
$1,2,4,5,6,6,\ldots$。按权分级，所得真实自由符号空间为：

| 权 $d$ | 空间 | 维数 |
|---:|---|---:|
| $0$ | $\mathscr H_0$ | 1 |
| $1$ | $\mathscr H_1$ | 2 |
| $2$ | $\mathscr H_2$ | 4 |
| $3$ | $\mathscr H_3$ | 5 |
| $4,5,6$ | 各为 $\mathscr H_d$ | 各6 |
| $7$ | $V\mathscr L_3+\operatorname{span}\{x^4BZ\}$ | 4 |
| $8$ | $V\mathscr L_4$ | 3 |
| $9$ | $\operatorname{span}\{xV^2,x^4VB\}$ | 2 |
| $10$ | $\operatorname{span}\{x^2V^2\}$ | 1 |

权0至4直接由 $A\mathscr L_d$、$W\mathscr L_{d-1}$、$Z\mathscr L_{d-2}$ 取得。权5中，$A(x^4B)$、$A(xV)$ 及 $W\mathscr L_4,Z\mathscr L_3$ 给全部六项。这里 $a,b,d$ 均非零。

权6需要一处真实系数检查。$V\mathscr L_2+Z\mathscr L_4$ 已给五维，另一列是 $x^4WB$。在 $V=Z=0$ 上，它不为零，当且仅当
$$
d+2e_-\ne0,\qquad 4be_--a(d+2e_-)\ne0.
$$
原常数准确给
$$
d+2e_-=-\frac{\kappa(3t+1)}{2h_e},
$$
$$
4be_--a(d+2e_-)
=\frac{\kappa}{128h_e^3}
(867t^3+251t^2-10t-8).
\tag{42}
$$
在 $0<t<1/100$ 内括号严格负，所以权6确为六维。权7的额外 $x^4BZ$ 不被 $V$ 整除；其后各权由(41)直接得到，没有漏添一个未实现的方向。

总自由维数为
$$
1+2+4+5+6+6+6+4+3+2+1=40.
$$
R289 的真实 even 母包/偶 $\chi$/可变实际平移判据在该有限多项式空间上的普遍核，恰为不带 $x$ 的 $uu'$ 与 $u'u''$。它们分别为权3、1，确都属于上表。没有其他普遍核。因此
$$
\boxed{\operatorname{rank}_{\rm actual\ even\ principal}=40-2=38.}
\tag{43}
$$
这里“actual”指存在同一个正解析 even 母包及有限个真实偶 $\chi$ 取得此秩；不是用多个互不相容母包的形式秩拼成一条路径。R289 的有限 Hermite witness、R293 的正 prefactor polynomial-path 方法同时给这一见证和从起点规定的任意有限 $C^2$ 观察的最大秩 minor。

旧全部 principal 也在这个空间中。尤其不需另加一个 $M_c$ 方向：R238 的
$$
\Psi=x^2u''-2xu'+2u=\frac{2V}{x^2},\qquad
\Theta=3x^2u''-5xu'+4u=\frac{4V}{x^2}-\frac{xB}{2}
$$
给
$$
S^{\rm prin}=\frac{x^2V^2}{16},\qquad
\mathfrak T^{\rm prin}=-\frac{xV^2}{8}+\frac{x^4VB}{64}.
\tag{44}
$$
两者已经是表中权10、9的原列。式(44)只比较 principal；本稿没有用它擅写新的完整能量函数恒等式。

## 12. 可再准确联付八个独立必要观察

旧 R293 的真实向量 $\mathcal V$ 有32个条目、两条完整线性关系，主秩30；R291 和 R286 已支付两条关系的真实低阶部分。第11节证明其 principal 空间包含在(43)内。

因此能从120个真实行 $\mathscr O_{\rho,n,m}$ 中选八个，使它们与旧30个独立观察的 principal 组成38维基。这个选择是对(38)—(41)固定实矩阵作有限基选择，不是把120行各自当作独立可调目标。

从构造起点采用至少包含 R299 全角观察的有限 $F^\star$；可同时含本稿显式 $F^1$。联合真实映射
$$
(\mathcal V,\mathcal O_1,\ldots,\mathcal O_8)
$$
始终落在 $\mathscr S_{30}\times\mathbb R^8$；前两条完整关系没有被改变。38个 principal 真实独立。有限个偶 $\chi$ 各自仍用 R289 的十二个真实交替包，因为所有位置多项式次数仍不超过10；每组的 Vandermonde 核在除去原 $\lambda_i$ 符号后严格正。故联合正锥为该38维空间，且可加正核使全部选中幅度严格正。

对任意预先固定的有限八维目标，先用此正锥支付准确基线与目标之差，再选38条独立幅列，固定其他正幅。原 $N^{-3}$ 振荡及同 $F^\star$ 的有限纠正，给固定有限正幅盒上的真实 $C^1$ 收敛。充分大但有限的 $N$ 上，IFT给准确目标。所有操作在每个最终完整 block 的实际位置完成，之后只按原正四次权组合，保持旧全部门。

因此特别可以同时做到
$$
\boxed{\mathcal V=0,\qquad \mathcal O_1=\cdots=\mathcal O_8=0.}
\tag{45}
$$
这是比 R296 单个一层 jet 多的真实有限存在性结论。它仍没有说全部120个原行已经为零，也没有产生一个本地数值候选。

## 13. 明确保留的 $C^2$ annihilator 相容门

对任一未选一层行，用其 principal 在38维基中的准确系数定义
$$
\mathcal D_\nu=
\mathscr O_\nu-\sum_{a=1}^{30}c_{\nu a}\mathcal V_a
-\sum_{b=1}^{8}d_{\nu b}\mathcal O_b .
\tag{46}
$$
$\mathcal V_a$ 指旧32行中一个真实独立坐标选择；已知两条完整关系另保。由 R296 的完整平方及本稿的原系数抽取，(46)的三导平方符号至多留下第11节的两个普遍 even 核：不带坐标因子的 $uu'(u''')^2$ 与 $u'u''(u''')^2$。在本稿每个真实微包关于其自身中心为偶的类上，它们的积分准确为零；同纤维纠正与所用偶振荡保持这个类别。其余三导平方消失，线性三导按(18)去掉。因此每个 $\mathcal D_\nu$ 在这个准确允许类上有连续 quartic/$C^2$ 表达，含其真实 self、Green 与有序尾，不能随意设零。本稿不把这一受限结论升级为任意非偶 profile 上的 $C^2$ 身份。

在(45)成立后，全部一层函数为零准确等价于
$$
\boxed{\mathcal D_\nu=0\quad\text{对其余全部原行}.}
\tag{47}
$$
保守地至多有112个此类生成条件，可能大量冗余；本稿不宣称其秩112，也不宣称它们独立于全部旧观察。

把这些量从起点加入一个更大的观察清单，只会**保持其真实初始值**，不会把未知或非零基线改成零。若要进一步解(47)，必须证明原等背景/原面积/旧能量已经蕴含其中哪些完整身份，或给同一实际母包与排列中能改变剩余基线的真实机制。主秩38本身不支付这个低阶兼容。

因此本稿的新增结论准确止于：全一层的显式原尾接口、120行准确呈示、实际 even principal 秩38、与旧门共同的八个新增必要观察控制，以及剩余真实 $C^2$ 相容门(46)—(47)。零层商、原period、同一gauge联合、收敛与几何主目标仍须分别继续。
