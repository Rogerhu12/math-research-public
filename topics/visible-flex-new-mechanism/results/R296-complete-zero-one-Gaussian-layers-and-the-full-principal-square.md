# R296：完整零／一层 Gaussian 余式、真实主平方与一个新增的一层方向

日期：2026-11-15。**完整纸面推导与有限频率存在性证明；没有执行求积、符号程序、profile 扫描、新人工检查或研究计算。**

[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md) 已在同一个实际圆上支付全部反对称面积和对称二层 Gaussian history。不能据此删去零层、一层，或将它们未经原式核对便称为 $C^2$ 数据。本稿给这两层的准确剩余表达，并证明完整第四 ruling 的三阶主项是一个保留局部恢复和真实 history 的平方。这个平方与 [R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md) 的二阶场最高 jet 使用同一个实际分量；本稿不使用 R295 的额外结论。

一个具体后果是：此前的30维主控制空间还没有覆盖全部一层。本稿从真实 $E_{-3}$ 系数提取一个新方向，证明增广主秩恰增一，并在保全部已付条件的真实有限频率圆上准确指定该单个必要量。取它非零证明旧条件不蕴含一层消去；取零也只支付这一条，不冒称四个一层函数或零层商已经支付。

主要来源：[R56 原恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 原八矩与 chain](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221 局部三线性式](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R243 完整有限判据](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)、[R245 Gaussian 归约](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R249 真实字独立](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R282 原二层系数](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md)、[R285 原主项降阶](R285-principal-splitting-of-symmetric-Gaussian-products.md)、[R289 主空间](R289-universal-even-principal-space-and-positive-real-packet-cones.md)、[R293 有限频率与初选低阶纤维](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)及 R294。

## 1. 固定实际对象及两个不同的 $Q$

从初始安装选择
$$
h=h_eH,\quad H=e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad 0<\kappa^2<1/100.
\tag{1}
$$
联合安装及原全路径条件按 R241/R293。不是在已经冻结的几何上改变 $\kappa$。共同右积分仍为
$$
Jv(x)=\int_x^{r_*}v,\qquad
z=x+\omega,\quad e=hx+j,\quad
j=2\varepsilon\kappa\sigma^2,\quad
\gamma=h_\sigma,\quad \mathcal Q=1+e^2 .
$$
所有 $\sigma$ 导数固定真实 profile 坐标 $x$。写
$$
\phi=f\cos\theta+g\sin\theta,\qquad D=f\odot f-\phi\odot\phi .
$$
内槽是对称双线性槽。真实三矩 $I_0,I_1,I_2$ 为 R282 的规范，尤其 $I_2$ 保留 $2u'v'$。

令 $\mathsf M(\sigma)$ 为 R73 的瞬时八矩算子，中心 history
$$
\mathsf m(\sigma)=\int_0^\sigma\mathsf M(t)\,dt
=\mathsf Q(\sigma)+\sum_{\rho\in\mathcal S}E_\rho(\sigma)B_\rho,
\qquad \mathcal S=\{1,-1,-2,-3\}.
\tag{2}
$$
$\mathsf Q$ 是真实奇 Laurent 算子，不是几何多项式 $\mathcal Q=1+e^2$。
$$
E_\rho=\int_0^\sigma H^\rho,\qquad
\mathsf M=\mathsf Q'+\sum_\rho H^\rho B_\rho .
$$
四个 $B_\rho$ 是原几何固定的算子；它们不是新的自由输入。

这里的中心初值只用于 R243(2) 已证明的真实偶部比较。原全路径传入的二、三阶 history 不被改写；它们的完整组合在同一个 $\mathcal W_e$ 商内处理。下文所有中心零值都不授权对实际路径重新起算。

记原 physical ruling 配对为 $\mathfrak b_\sigma$，而
$$
\mathcal E_\sigma(a,b)=\mathfrak b_\sigma(Y_a,Y_b)
=\frac1{4h}\int\{\mathcal Q a''b''+2h^2a'b'\}.
\tag{3}
$$
至少一槽紧时，(3)仍保真实有尾另一槽的全部端项。

## 2. 第三局部恢复和变化 profile 的准确拆分

令 $\mathcal K[H]$ 表示 R56 由 forcing $H$ 求出的 **$W=0$** 局部恢复；$P,B,\eta_0$ 全按原式计算。静态二次输入记 $K_\sigma(a,b)=\mathcal K[H(Y_a,Y_b)]$。于是
$$
Z(D)=K_\sigma(D)-Y_{\mathsf mD}.
\tag{4}
$$

另定义
$$
K_\sigma^{(0)}(\phi;D)=
\mathcal K[H(Y_\phi,K_\sigma(D))],\qquad
\ell_\sigma(\phi;D)=R[H(Y_\phi,K_\sigma(D))].
\tag{5}
$$
这里必须对整个 $K_\sigma(D)$ 作真实 $\sigma$ 导数。

当第二 profile $b$ 随 $\sigma$ 变化、$b_\sigma=v$ 时，局部恢复有额外项 $J_\sigma^{\rm ch}(a,v)$。它的 $P,B$ 为零，其分子为
$$
\left(\eta^{\rm ch}/h,\,0,\,e\eta^{\rm ch}/h\right),\qquad
\eta^{\rm ch}(a,v)=
\frac{2he\,a''v-2h^2a'v-\mathcal Q a''v'-J_e(a,v)}
{16h}.
\tag{6}
$$
$J_e$ 为 R73 原 weighted primitive。验证只需保
$$
(T_{\sigma x})_{\rm ch}=V_v\cdot V_a'/2,\qquad
(P_\sigma)_{\rm ch}=P(a,v)
$$
代 R56(6)；没有另选 profile 锚。

因此真正第三响应
$$
C(\phi;D)=K_\sigma^{(0)}(\phi;D)
-K_\sigma(\phi,\mathsf mD)
-J_\sigma^{\rm ch}(\phi,\mathsf MD)-Y_{W_C}
\tag{7}
$$
满足
$$
(W_C)'=\mathscr C_\sigma(\phi;D)
-\mathsf M(\phi,\mathsf mD),\qquad
\mathscr C_\sigma=\ell_\sigma-\Psi_\sigma(\phi,\mathsf MD),
\quad W_C(0)=0 .
\tag{8}
$$
$\Psi_\sigma$ 正是 R73(15)，未省略变化 profile 的 chain。完整 ruling 仍为
$$
\widehat{\mathscr K}_\theta
=-\mathfrak b_\sigma(Z,Z)+4\mathfrak b_\sigma(Y_\phi,C).
\tag{9}
$$

## 3. 零层与四个一层的完整原式

对 (8) 中 $\int\mathsf M(\phi,\mathsf mD)$ 使用同中心恒等
$$
\int_0^\sigma \mathsf Q'(\phi,B_\rho D)E_\rho
=\mathsf Q(\phi,B_\rho D)E_\rho
-\int_0^\sigma H^\rho\mathsf Q(\phi,B_\rho D).
$$
所有下端项为真实中心值；$\mathsf Q(0)=E_\rho(0)=0$。

定义
$$
\begin{aligned}
W_0(\sigma)=\int_0^\sigma\Big\{
&\mathscr C_t(\phi;D)-\mathsf Q_t'(\phi,\mathsf Q_tD)\\
&-\sum_\rho H(t)^\rho
[B_\rho(\phi,\mathsf Q_tD)-\mathsf Q_t(\phi,B_\rho D)]
\Big\}\,dt .
\end{aligned}
\tag{10}
$$
则准确有
$$
W_C=W_0-\sum_\rho E_\rho\mathsf Q(\phi,B_\rho D)
-\sum_{\rho,\tau}K_{\rho,\tau}B_\rho(\phi,B_\tau D),
\quad K_{\rho,\tau}=\int_0^\sigma H^\rho E_\tau .
\tag{11}
$$
(10)的 integrand 全是奇 Laurent 系数乘固定真实 profile。其积分是偶 Laurent 系数，必须扣除真实中心常数；指数相加为零时用普通多项式积分，不除以零。

设
$$
Z_0=K_\sigma(D)-Y_{\mathsf QD},\quad
C_0=K_\sigma^{(0)}(\phi;D)-K_\sigma(\phi,\mathsf QD)
-J_\sigma^{\rm ch}(\phi,\mathsf MD).
$$
令 $\mathcal T_\sigma(c;a,b)=\mathfrak b_\sigma(Y_c,K_\sigma(a,b))$，使用 R221(17) 的完整原式。零层准确为
$$
\boxed{\mathscr R_{0,\theta}
=-\mathfrak b_\sigma(Z_0,Z_0)
+4\mathfrak b_\sigma(Y_\phi,C_0)
-4\mathcal E_\sigma(\phi,W_0).}
\tag{12}
$$
每个 $E_\rho$ 的系数准确为
$$
\boxed{\begin{aligned}
\mathscr R_{\rho,\theta}={}&
2\mathcal T_\sigma(B_\rho D;D)
-4\mathcal T_\sigma(\phi;\phi,B_\rho D)\\
&-2\mathcal E_\sigma(\mathsf QD,B_\rho D)
+4\mathcal E_\sigma\{\phi,\mathsf Q(\phi,B_\rho D)\}.
\end{aligned}}
\tag{13}
$$
它就是 R221 的线性 gauge 响应中，把历史算子换成 $\mathsf Q$、取 $w=B_\rho D$ 的表达；这里 $B_\rho D$ 因三矩确实紧。这个解释不将一个随 $\sigma$ 变化的 gauge 擅自当作固定合法 gauge：所需 chain 已在(6)、(10)、(12)中另行保留。

全部二层支付后，完整剩余式是
$$
\boxed{\widehat{\mathscr K}_\theta
=\mathscr R_{0,\theta}
+\sum_{\rho\in\mathcal S}E_\rho\mathscr R_{\rho,\theta}.}
\tag{14}
$$
$\mathscr R_0$ 为偶 Laurent，$\mathscr R_\rho$ 为奇 Laurent。R249 的真实独立性给这一 germ 的准确剩余条件：
$$
\boxed{
\mathscr R_{\rho,\theta}\equiv0\quad(\rho\in\mathcal S),\qquad
\mathscr R_{0,\theta}\in\mathcal W_e
}
\tag{15}
$$
对全部角成立，其中
$$
\mathcal W_e=\operatorname{span}\{h,\ \sigma^2,\ (1+4\varepsilon^2\kappa^2\sigma^4)/h\}.
$$
(15)不是将零层强迫为零。它也不以低 Taylor 阶单独判断 quotient：即使某个 $E_\rho\mathscr R_\rho$ 的最低总 Taylor 项可由 $\mathcal W_e$ 匹配，真实 $E_\rho$ 系数仍必须整个为零。

## 4. 用于全部层的真实三阶分解

以下只作 profile 导数阶数的准确整理。置
$$
v=u',\quad r=u'',\quad t=u'''.
$$
沿用 R285 的 $C^2$ 余项类：允许全部真实右 primitive、其左值、有序跨包项和 Green 边项。符号 $\equiv_2$ 只表示差为此类，绝不表示差已零。

将右积分中仅线性含 $t$ 的项按 R285 的
$$
J(A t)=-\int_0^r A(x,u,v,s,\mathbf J)\,ds
-JD_0\!\left(\int_0^r A(x,u,v,s,\mathbf J)\,ds\right)
\tag{16}
$$
作准确降阶。右端原函数端值由零 collar 为零；左值原样保留。这样得到有限的 local polynomial 加真实 $C^2$ primitives 的表示。下文的 $\partial_r^{\rm loc}$ 对该表示的 local $r$ 求导，将其真实 primitive 变量独立保留；这是明确的代数步骤，不是对某个不交包尾取零。

对任意八矩算子 $X$，写
$$
X(u,u)''=\alpha_X t+\beta_X,\qquad
\alpha_X=A_{1,X}u+2A_{2,X}v-2C_Xr,
\quad C_X=B_{0,X}+xB_{1,X}+x^2B_{2,X}.
$$
其输出本身不含 local $r$，而
$$
\partial_r^{\rm loc}X(u,u)'=\alpha_X.
$$
原六项式随后给一个有用的准确恒等：
$$
\boxed{
\partial_r^{\rm loc}X(u,Y(u,u))=\alpha_X\alpha_Y/2 .
}
\tag{17}
$$
确实，直接含 $w'$ 的系数是 $A_{1,X}u/2+A_{2,X}v$；三个原 primitive 在(16)后贡献 $-C_Xr\alpha_Y$。它们合为(17)。剩余真实 primitives 没有被删除。

## 5. 局部第三 density 的关键恒等

R221(14) 的对角式为
$$
\eta=\frac{
\mathcal Q(2\gamma vr-e_\sigma r^2)-2h\gamma e v^2
+J\{(\gamma\mathcal Q-2hee_\sigma)r^2-2h^2\gamma v^2\}}
{16h^2}.
$$
定义
$$
\boxed{\beta=\eta_r^{\rm loc}/h
=\frac{\mathcal Q(\gamma v-e_\sigma r)}{8h^3},\qquad
L_\sigma=\alpha_{\mathsf m}/2+\beta .}
\tag{18}
$$
原二阶分子 $V_Z'$ 的最高 $t$ 项为
$$
(V_Z')_{\rm prin}=(1,0,e)L_\sigma t .
\tag{19}
$$

这里必须证明局部第三 density 的贡献，不能只观察(19)便猜完整 ruling 是平方。为此置
$$
A=\mathcal Qr-hev,\quad C=he\,u-\mathcal Qv/2,\quad
n=h(u-zv/2),\quad t_0=\gamma u-e_\sigma v/2 .
$$
对 forcing $H(Y_u,K_\sigma(u,u))$，R56 的原 $P_C,B_C,T_\sigma$ 在(16)后满足
$$
(P_C)_r^{\rm loc}=\frac{A\beta}{4h},\qquad
(B_C)_r^{\rm loc}=\frac{C\beta}{2h},\qquad
(T_\sigma)_r^{\rm loc}=nzh\beta+t_0(e\beta_\sigma+e_\sigma\beta).
\tag{20}
$$
例如直接原 right integral 是
$$
P_C=\frac{A\eta+J(\mathcal Q t\eta)}{4h^2};
$$
其 $r$ 导中的 $\mathcal Q\eta$ 与 primitive 的 local 项准确相消，给(20)。不要求 $\eta$ 的左尾零。

将(20)代 R56(5)，$\beta_\sigma$ 的系数是
$$
\frac{et_0}{2h^2}-\frac{e_\sigma A}{4h^3}
-\frac{\gamma C}{2h^3}=2\beta .
$$
$\beta$ 的三个 $u,v,r$ 系数分别为
$$
\frac{k\mathcal Q}{2h}=-A_{1,\mathsf M},\qquad
-\frac{K_{0,x}\mathcal Q}{4h}
+\frac{\gamma e e_\sigma}{2h^3}
-\frac{\gamma^2\mathcal Q}{4h^4}
=-2A_{2,\mathsf M},\qquad 2C_{\mathsf M}.
$$
这些是 R73 原系数，不是一个新近似。因此
$$
\ell_r^{\rm loc}=2\beta\beta_\sigma-\beta\alpha_{\mathsf M}.
\tag{21}
$$
另一方面，R73 原 $\Psi$ 中
$w=\mathsf M(u,u)$ 满足 $w_r^{\rm loc}=0$、$w'_r{}^{\rm loc}=\alpha_{\mathsf M}$，并有
$$
(J_e(u,w))_r^{\rm loc}=-\mathcal Qr\alpha_{\mathsf M}.
$$
准确得到
$$
\Psi_\sigma(u,\mathsf M(u,u))_r^{\rm loc}
=-\beta\alpha_{\mathsf M}.
$$
故真正局部 density 的恒等是
$$
\boxed{(\mathscr C_\sigma(u;u,u))_r^{\rm loc}
=(\beta^2)_\sigma.}
\tag{22}
$$
中心偶几何给 $\beta(0)=0$。由(8)、(17)、$\mathsf m(0)=0$，遂有
$$
\boxed{(W_C)_r^{\rm loc}
=-\alpha_{\mathsf m}^2/4+\beta^2}
\tag{23}
$$
于对角单包。所有中心常数按真实初值核过；不在其他位置重新取零。

## 6. 完整第四主项恰为同一个平方

在一个 rank-one 微包上写 $\phi=c_i u_i$、$D=d_i u_i^2$，
$d_i=a_i^2-c_i^2$。第三局部恢复的最高项，由 R56 四项直接给
$$
(\eta_C)_{\rm prin}
=-c_id_i\,\frac{\mathcal Q(\gamma v-e_\sigma r)}
{8h^2}L_\sigma t.
\tag{24}
$$
其中 $T_{\sigma x}$、$e_\sigma P_x$、$\gamma B_x$ 的 $u$ 项与 $ee_\sigma v$ 项准确抵消；$P_\sigma$ 已是(16)后的 $C^2$ 表达，没有遗漏三阶项。

将(19)、(23)、(24)放回**完整**(9)。按共同因子
$\mathcal Q t^2/h$，三项的系数依次为
$$
-d_i^2L_\sigma^2,\quad
-2c_i^2d_i\beta L_\sigma,\quad
c_i^2d_i(-\alpha_{\mathsf m}^2/4+\beta^2).
$$
其和准确为 $-a_i^2d_iL_\sigma^2$。

跨包不额外产生两个三阶导的乘积。右方内包在当前包上的 $K$ 尾满足 $P=p(\sigma)$ 为 $x$ 常数、$B=0$、$\eta=-p_\sigma/2$。代原恢复，$\ell$ 和 $\Psi$ 的相应 profile 表达只含当前 $u,u'$，没有 local $r$ 导。其余含一次 $t$ 的真实 cross/Green 项按(16)保入 $C^2$；没有把单包尾称紧。

因此，对包括全部实际副本的任意不交 rank-one 表示，
$$
\boxed{
\widehat{\mathscr K}_\theta
\equiv_2
-\sum_i a_i^2d_i(\theta)
\int \frac{\mathcal Q}{h}
L_\sigma[u_i]^2(u_i''')^2 .
}
\tag{25}
$$
这是完整零、一、二层共同的原式分解，不只一个渐近层。特别(13)的主项为
$$
\boxed{
\mathscr R_{\rho,\theta}\equiv_2
-\sum_i a_i^2d_i
\int \frac{\mathcal Q}{2h}\alpha_{B_\rho}
\left\{\alpha_{\mathsf Q}
+\frac{\mathcal Q(\gamma u_i'-e_\sigma u_i'')}{4h^3}\right\}
(u_i''')^2 .
}
\tag{26}
$$
(25)的二层部分与 R285 完全一致；不能因为二层完整系数已经零，就将其中的主项或相应 $C^2$ 余项单独删掉。

## 7. 一个确实新增的一层必要量

令 $B_{-3}=cP$、$P(u,u)=J(u''^2)$，原 $c\ne0$。
一层系数为奇函数，故它在中心的值自动零。定义
$$
\mathcal N_\theta=c^{-1}\partial_\sigma
\mathscr R_{-3,\theta}(0).
\tag{27}
$$
在已付全部 Gaussian 二层和面积的类上，(13)准确化为
$$
\boxed{\begin{aligned}
\mathcal N_\theta={}&
2\dot{\mathcal T}_0(PD;D)
-4\dot{\mathcal T}_0(\phi;\phi,PD)\\
&-2\mathcal E_0(\mathsf M_0D,PD)
+4\mathcal E_0\{\phi,\mathsf M_0(\phi,PD)\}.
\end{aligned}}
\tag{28}
$$
这里删掉的是 $\mathsf Q'(0)=\mathsf M_0-\sum B_\rho$ 中**已经支付的完整** Gaussian 对称项和交换子；没有删未知余项。
$\dot{\mathcal T}_0$ 可直接由 R221(17)代
$$
h=h_e,\ e=h_ex,\quad
\gamma=2\varepsilon h_e,\quad
e_\sigma=2\varepsilon h_ex+4\varepsilon\kappa
$$
取得：原 $\mathcal T$ 对 $\gamma,e_\sigma$ 线性，中心其他导数乘零。

记 R285 的六方向为 $P,R,S,L,U,V$，另 $T_1=\Phi_{t_1}$。R73 在中心准确给
$$
\mathsf M_0=
-\frac{\kappa}{2h_e}L-\frac{\kappa h_e}{2}V
-\frac{\kappa}{8h_e^3}P
+\frac{\kappa^2-1}{8h_e^2}R
+\frac{\kappa^2-1}{8}T_1,
\tag{29}
$$
而
$$
2\dot\beta_0=
\frac{\varepsilon\mathcal Q_0}{4h_e^2}\alpha_R
+\frac{\varepsilon\kappa\mathcal Q_0}{2h_e^3}\alpha_P,\quad
\mathcal Q_0=1+h_e^2x^2,\quad \alpha_{T_1}=x^2\alpha_R .
\tag{30}
$$
在 $\theta=\pi/2$ 置原 $\lambda_i=-a_i^2R_i$，得到
$$
\mathcal N_{\pi/2}\equiv_2
\sum_i\lambda_i\int
\frac{\mathcal Q_0}{2h_e}\alpha_P
(\alpha_{\mathsf M_0}+2\dot\beta_0)(u_i''')^2 .
\tag{31}
$$
它保全部有限低阶余项作为准确基线。

## 8. 该主行不在旧30维空间中

用 R289 的齐次变量
$$
A=-2u'',\quad B=2u'-2xu'',\quad C=u-xu',
$$
赋权 $0,1,2$，并给 $x$ 权1。设
$$
W=aB+bxA,\quad Z=dC+e_-(xB+x^2A/2),\quad
V_*=x^2C-x^4A/4 .
$$
这里 $a,b,d,e_-$ 为真实 Gaussian 常数，$a,d,e_-\ne0$。

(31)的 integrand symbol 中，权5部分只有
$$
\boxed{
\frac{h_e(\kappa^2-1+2\varepsilon)}{16}\,x^4AB .
}
\tag{32}
$$
它来自 (29)、(30)的 $T_1$ 方向。共振时括号为 $3\kappa^2/2-1$，在(1)内不为零。

旧三十 Gaussian 主行在权5部分仅张成
$$
xAV_*,\quad WV_*,\quad x^2WZ,\quad xZ^2.
\tag{33}
$$
$L_c,M_c$ 分别为权10、9，不添加权5行。
若 $x^4AB$ 属于(33)，先比较 $C^2$ 迫 $xZ^2$ 系数零；比较 $BC$ 迫 $WV_*$ 系数为 $x^2WZ$ 系数的 $-d$ 倍；比较 $AC$ 迫 $xAV_*$ 系数零；最后比较 $B^2$ 迫余系数零，因为 $ae_-\ne0$。矛盾。

真实 even 配对不会恢复这条依赖。R289 的 ±母坐标分离表明：对所有偶母包、偶 $\chi$ 及真实平移，二次 jet 多项式的普遍零仅为不带 $x$ 的 $uu'$、$u'u''$；权分别为3、1，不可能消去(32)。

于是旧秩30加(31)，主秩准确增为31。真实振荡平均的共同因子 $1/2$ 和全部正 copy 权不改变此结论。没有执行数值秩，也没有把条目数作为秩证据。

## 9. 同一旧条件内的真实单 jet 灵活性

这个新方向不仅是形式上“未检查”。可以从构造起点取 R294 的 $\mathcal F^+$，保全部原 self、真实三矩、ordered 楔及 corrected self 平移系数，并联合考察
$$
(\mathcal V,\mathcal N_{\pi/2})\in\mathbb R^{33}.
$$
R293 的两个**完整**线性关系仍对每个允许 profile 成立，所以真实映射始终落在 $\mathscr S\times\mathbb R$，维数31。第8节给该空间的全部主秩31。

R289 的正解析 Hermite 见证及 R293 §6 的 polynomial-path 论证，可在同一个正解析母包上同时取得这个31阶主 minor和 $\mathcal F^+$ 最大秩 minor。有限个偶 $\chi$ 选定后，每组仍使用十二个真实交替包。新行的位置次数至多6，旧行至多10；原11×12 Vandermonde正核因此不变。联合正锥恰为 $\mathscr S\times\mathbb R$，每组可加严格正核，使全部选中幅度严格正。

所以，对任意先固定的有限实数 $\tau$，完整基线到
$$
(\mathcal V,\mathcal N_{\pi/2})=(0,\tau)
$$
的差有严格正平方幅表示。取31条独立列，固定其余幅，极限 Jacobian 可逆。R285 降阶、(25)与同纤维纠正给固定有限正幅盒上的真实 $C^1$ 收敛；足够大的**有限** $N$ 遂有准确根。

在五个最后完整 block 中分别进行，并选择其 $\mathcal N$ 目标使真实正四次加和为 $\tau$。各 block 的原 $\mathcal F^+$、位置与权不变，所有原完整面积与楔保持；每个 block 的 $\mathcal V=0$，R294 使全角二层零。十二包装、三矩、完整第三、六能量和解析正 prefactor按原证明共同保持。

故得到两个准确而有限的结论：
$$
\boxed{\text{原已付条件允许 }\mathcal N_{\pi/2}\ne0,}
\qquad
\boxed{\text{也可同时再付 }\mathcal N_{\pi/2}=0.}
\tag{34}
$$
第一式证明全二层与六能量不蕴含全部一层消去；第二式只新增一个必要 jet 的支付，不等于 $\mathscr R_{-3}\equiv0$，更不等于四个一层函数全零。

## 10. 全部剩余主量的有限接口与未付边界

(18)的 $L_\sigma$ 是 $u,u',u''$ 的线性式，其三个 $x$ 系数次数分别至多2、3、4。因而 (25)的所有几何系数的主量都属于以下有限 symbol 空间：
$$
\begin{array}{c|c}
\text{jet 单项式}&x\text{ 次数}\\ \hline
(u'')^2&0,\ldots,10\\
u'u''&0,\ldots,9\\
uu''&0,\ldots,8\\
(u')^2&0,\ldots,8\\
uu'&0,\ldots,7\\
u^2&0,\ldots,6
\end{array}
\tag{35}
$$
共有54个生成元；even普遍零至多先删上述两个常数奇项，给52维**通用上界**。这不是实际零／一层观测的秩，不证明它们全可达，也没有支付潜在 principal-annihilator 上的真实 $C^2$ 基线。

(10)—(13)给所有零／一层的准确有限来源；(22)—(26)给其共同高阶结构。任何进一步从起点加入的低阶纤维，必须把所需实际 $C^2$ self、尾和全部有限平移系数具体列出。保持它们不等于将它们任意指定为零。若新的主关系仅在高阶成立，仍须先核其完整余项，不能照搬 R293 的两条已付关系。

因此下一问题已经可以一次针对(15)的有限全系数，而非只逐个取大参数渐近层。仍须保原五相位、同一真实右锚、真实 prefix 比较及 $\mathcal W_e$ 商；实际闭路径其他段、canonical period、平台/flux、内部 Laurent 条件和同一个二阶 gauge 的 joint 匹配都未由本稿支付。更高阶收敛、有限等距族及主课题的嵌入和厚度指标也不在(34)的结论内。
