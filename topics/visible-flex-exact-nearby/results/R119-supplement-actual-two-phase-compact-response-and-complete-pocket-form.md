# R119 续篇：实际两相位的 compact 响应、全部参数行及整负窗控制型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对第70束同一个实际 incoming 可达邻域，本篇
支付此前单独保留的两个真实参数列。对一个真正未使用区间内的
第67束方向，完整首密度相位的变分仍带 $\rho^5$；两相位的无限
联立平均行给每一层自身的 $D_\psi\Gamma_i^*$ 界。加入这两列后，
整个负窗的实际 physical Cauchy crossing form 在明确的中心
$m=\pm M$ 两迹空间上仍大于 $d_*/8$，$M^2/B\le1$。

这里没有把 $D_\psi\Gamma^*$ 设为零，也没有固定其它层来求本层。
输出的全部角频、两个 mean、Jacobian、normal shear 和仿射源
仍保留。当前结论针对 **fresh unused 支集**：在第68束已启用的
有限参数盒内，需要比较
$D_\Omega\Gamma^*-D_\Omega\bar\Gamma$，并保留真实径向补偿
$D_\Omega\bar\Gamma$；本文不把它冒作仍然为零。
不同 $M$ 的混频簇和物理 principal 端口的完整参数识别也未由
本篇的单频中心压缩型自动得到。

## 1. 当前对象与一个共同可达邻域

使用[受控全图](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
的真实 $\Gamma^*(\mathbf a,\Omega)$，其中全部 principal 返回
与完整首密度相位分别等于固定目标 $\omega_i,\beta_i^0$。
采用[整负窗证明](R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md)
的
$$
 \mathcal X\le2^{-1048576},\qquad
 2^{-40}\delta_j^{-1/8}\le M\le\sqrt B,\qquad
 \rho=2^{-2204}M^5B^{-4}\Delta^{-11},\quad
 d_*=2^{-22000}M^{50}B^{-39}\Delta^{-103}.
 \tag{C.1}
$$
这里 $\rho$ 只表示 compact 支集宽；fixed-stop 的物理腰尺度
$\rho_{\rm waist}$ 是另一个固定正数，沿本方向不变。
原 fixed-stop incoming 的 $2^{-60000000}$ 标签界实际进入 (C.1)，
并不需要假定完整外方程 $\mathcal F=0$ 已经解决。

对任一完整负分量 $i$，记较深胞元号为 $j_i$，
$J_i=j_i+5$、$\delta_i=\delta_{j_i}$。令 $\mathcal C_i$ 是该负
分量实际相交的至多两个胞元，定义
$$
 \mathcal N_i=\sum_{k\in\mathcal C_i}(N_k^c+N_{k-1}^c),\quad
 \mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i,\quad
 N_k^c=2^{200}h_k^{-5}\frac{\zeta_k}{\mu_k\delta_k^2}.
 \tag{C.2}
$$
约定 $N_k^c=0$ 于 $k<129$。最外截断分量不进入两相位方程，
仍属于原外部匹配行。完整旧前缀和两个规范接缝给
$$
 \sum_i\mathcal W_i<2^{160024}.
 \tag{C.3}
$$
这是原 $\sum_k(K_k^{\rm ref})^2N_k^c<2^{160016}$ 的直接消费者：
$K_k^{\rm ref}=2^{5000}(k+4)^5\delta_k^{-10}$，
邻胞 $J$、$\delta$ 的比至多2，各 $N_k^c$ 的计数至多8。
因 $2^{10000}J_k^{10}\delta_k^{-20}$ 严格大于每个所需
$2^{10}J_k^4\delta_k^{-6}$，无需扔掉129--8192前缀。

控制所在胞元仍记为 $j$，且
$$
 P_j=h_j^{-14}\delta_j^{-7/4}
       =2^{-42}\delta_j^{-231/128}>1 .
 \tag{C.4}
$$
所有本篇导数都在一个实际固定标签 $\mathbf a$ 上计算。
只有当明确写 $\Gamma^*$ 时才沿联合选择支变化。

## 2. 真首密度相位的准确 action 形式

采用相对背景变量
$$
 \mathsf J=1+K+EU,\quad D=1-w^2(2K+K^2+EP^2),\quad
 \upsilon=\sqrt D/\mathsf J,\quad q=\sqrt Q,\quad
 r_D=-\log D,\quad \ell=\log(\mu_0q)+r_D .
$$
其中 $U=P_\theta$、$V=K_\theta$，$\mu_0=w/r$。
背景漂移为 $d=E(V-P)/\mathsf J$。当前真实 Jacobi 密度为
$$
 \widehat G=
 \begin{pmatrix}(q\upsilon)^{-1}&-d(q\upsilon)^{-1}\\
 -d(q\upsilon)^{-1}&d^2(q\upsilon)^{-1}-q\upsilon\end{pmatrix},
 \qquad
 \kappa_{\rm den}
 =-\tfrac12\operatorname{div}(\widehat G\nabla\ell)
       -\tfrac14\nabla\ell\cdot\widehat G\nabla\ell .
 \tag{C.5}
$$
完整背景方程的准确恒等式给
$$
 (\partial_t-d\partial_\theta)r_D=2Qw^2U/\mathsf J.
$$
因此令
$$
 L_0=-1-Q+\frac{Q_t}{2Q},\quad
 R=2Qw^2U/\mathsf J,\quad
 \mathscr B_\ell=\frac{L_0+R}{q\upsilon},\quad
 \mathscr A_\beta=\frac{(L_0+R)^2}{q\upsilon}
                           -q\upsilon(r_D)_\theta^2 ,
 \tag{C.6}
$$
在任一原固定 strict 子段准确有
$$
 \int_s^t\langle\kappa_{\rm den}\rangle\,d\tau
 =-\tfrac12[\langle\mathscr B_\ell\rangle]_s^t
       -\tfrac14\int_s^t\langle\mathscr A_\beta\rangle\,d\tau .
 \tag{C.7}
$$
证明只需将散度的角部分在真圆周上积分为0；二次项准确是
$(\ell_t-d\ell_\theta)^2/(q\upsilon)-q\upsilon\ell_\theta^2$。
它没有遗漏 $d$、两分支密度或 mean 乘积。

第49/55束的实际有限部定义是
$\beta_i=-\tfrac14\operatorname{FP}\int_{I_i}
\langle\kappa_{\rm den}\rangle dt$，有限部按两根的真 canonical
截面取值。因而对支集严格在内部、端 jets 为0的显式 metric
变化，边界项不变，并且
$$
 \dot\beta_{i,\rm explicit}
             =\tfrac1{16}\int\langle\dot{\mathscr A}_\beta\rangle dt.
 \tag{C.8}
$$
这只是紧支部分；整个实际背景响应的 boundary/finite-part
变化会在第4节完整加入。

## 3. 不损失 $\rho^5$ 的直接项

在控制区间 $I$ 内，$Q=7+Bf(x)$、$dt=(\Delta/B)dx$，
$1<Q/B<2$，且
$$
 |Q_t|<B^2,\quad |Q_{tt}|<B^3,\quad |Q_{ttt}|<B^4 .
 \tag{C.9}
$$
这些只用真实 quartic 的 $|f'|<2,|f''|<30,|f'''|\le45$
及 $\Delta>80$。未用整个负窗的粗导数去估本支集。

将 $\mathscr A_\beta/B^{3/2}$ 记为
$\mathfrak a(q_1,y,w,Z)$，其中
$q_1=Q/B$、$y=Q_t/B^2$、$Z=(P,K,U,V)$。
由 (C.6)，它准确等于
$$
 \mathfrak a=
 \frac{[-B^{-1}-q_1+y/(2q_1)+2q_1w^2U/\mathsf J]^2}
                  {\sqrt{q_1}\upsilon}
       -B^{-1}\sqrt{q_1}\upsilon(r_D)_\theta^2 .
 \tag{C.10}
$$
这里
$(r_D)_\theta=2w^2[(1+K)V+EP U]/D$，没有径向状态导数。

以下给出所用 tame 常数。在实际支集，令
$n=\sup_I w^{-1}(\|p\|_{\mathcal A_2^2}+
\|k\|_{\mathcal A_2^2})\le4\mathcal N_i\mathcal X$。
在复邻域
$|q_1-q_{1,0}|\le1/4$、$|y-y_0|\le1$、
$|w|\le1/8$、$\|Z\|<1/16$ 上，
$$
 |\mathsf J-1|<1/4,\quad|D-1|<1/128,\quad
 |\upsilon|,|\upsilon^{-1}|<2,\quad
 |\mathfrak a|<2^{12}.
 \tag{C.11}
$$
例如 (C.10) 方括号小于5、平方项系数小于4、最后项小于4，
总计小于104。Wiener 代数中同样成立。

在实际小球和宽1上，至多五个复方向每个取半径 $2^{-11}$，
其和小于 $1/256$，严格留在 (C.11) 内。多方向 Cauchy 给
所有所需至多五阶混合导数小于
$5!\,2^{55+12}<2^{80}$。
因此只对 $(q_1,y,w)$ 求至多四阶导时，
$\mathfrak a-\mathfrak a|_{Z=0}$ 的 bound 是 $2^{80}n$；
含一或两个 $Z$ 方向的相应导数 bound 是 $2^{80}$。
这是显式完整复域的 Cauchy，不是径向 jets 外推。

实际相对两场方程
$$
 P_t=V+(Q-1)P,\qquad
 K_t=\frac{Q(2K+U+K^2+KU+w^2P^2)+E(V-P)^2}{\mathsf J}
 \tag{C.12}
$$
在宽2到1上给
$\|Z_t\|<2^{12}Bn$、$\|Z_{tt}\|<2^{30}B^2n$。
具体右边及其角导的线性系数和小于 $2^9B$；
分母求导、$\partial_tQ$、$\partial_tw=-Qw$ 与再一次角导
分别放宽 $2^3,2^4,2^3,2^5$，仍小于显示的二阶常数。
完整角 Fourier 和参与这些代数估计。
此外 $|w_t|\le2B|w|$、$|w_{tt}|\le6B^2|w|$，
$(q_1,y)$ 的一、二阶导分别小于 $B,B^2$。

用第61束的真实 profile 向量场
$\mathcal B=w\partial_w+f\partial_k$，有
$\dot Q=-\psi_t$、$\dot Q_t=-\psi_{tt}$，
显式背景部分为 $\psi\mathcal B$。
在相对变量中 $\mathcal BP=-P$、
$\mathcal BK=f/w-K$，其完整角导的 norm 小于 $2^8n$。
由 (C.10)--(C.12)，对
$\Delta\mathscr A=\mathscr A_\beta-\mathscr A_\beta|_{Z=0}$，
$$
 |(\partial_Q\Delta\mathscr A)_t|<2^{96}nB^{3/2},\quad
 |(\partial_{Q_t}\Delta\mathscr A)_{tt}|<2^{116}nB^{3/2},\quad
 |\mathcal B\Delta\mathscr A|<2^{96}nB^{3/2}.
 \tag{C.13}
$$
第二式的最坏项是 $2^{80}\|Z_{tt}\|B^{-1/2}$；
其它项至多两个一阶导的乘积，$n^2\le n$。
这逐项说明了放宽的常数，不要求方向的第五径向导数。

因为 $\psi,\psi_t$ 在支集两端为0，准确有
$$
 \int\dot{\Delta\mathscr A}\,dt
 =\int\psi\{(\partial_Q\Delta\mathscr A)_t
       -(\partial_{Q_t}\Delta\mathscr A)_{tt}
       +\mathcal B\Delta\mathscr A\}\,dt .
 \tag{C.14}
$$
原两个 phase 核被第67束方向准确消去；其径向 $\dot\beta$ 为0。
这个径向核仅用支集内部的 $Q$，与外面两个 bump 的当前取值无关。
所以该消去在当前 $\Gamma^*$ 的径向参考也准确成立。
用 $\int|\psi|dt\le2(\Delta/B)\rho^5$，得到
$$
 |\dot\beta_{i,\rm direct}-\dot\beta_{i,\rm radial}|
       <2^{128}n\Delta\sqrt B\,\rho^5 .
 \tag{C.15}
$$
这就是原 $\rho^5$；没有由一个 $C^4$ 参数圆盘粗付成常数。

## 4. 全窗背景响应、根有限部和真实 principal 行

固定当前 $\Gamma$ 的实际 gauged 响应满足
$$
 \widehat n_i<2^{832}\mathcal N_i\mathcal X P_j\rho^5 .
 \tag{C.16}
$$
在 strict 部分，对 (C.6) 的真实有理函数作状态微分直接给
$$
 |\widehat{\mathscr A}_\beta|
 <2^{32}\widehat n_i
 \left[\frac{(1+Q)^2}{q}+\frac{Q_t^2}{q^5}+q\right],
$$
$$
 |\widehat{\mathscr B}_\ell|
 <2^{32}\widehat n_i
           \left[\frac{1+Q}{q}+\frac{|Q_t|}{q^3}\right].
 \tag{C.17}
$$
这里没有 $\widehat z_t$；(C.6) 已用完整背景方程消去了它。
原 strict 的 $W$ 积分小于 $2^{64}J_i^2\delta_i^{-5}$，
两个固定 strict cut 的 $Q$ 离0有界，其边界项小于
$2^{64}b_e\widehat n_i$。

两个根不能只靠该 strict 积分处理。根 canonical 势满足
$|V-V_0|<2^{32}n_i$；对实际 CK 收缩作方向微分，其逆范数小于2。
从宽2的输入到宽 $1/2$ 的势及 graph，保留原复逆和 height 因子，
可分别取
$$
 |\dot V|<2^{64}\widehat n_i,\qquad
 |\dot g|+b_e|\dot H|<2^{32}\widehat n_i .
 \tag{C.18}
$$
原初值到四态的 Lipschitz、两特征 ODE、$2/3$ 幂和复逆各付
因子2；缩半径/角域时至多增加 $2^{16}$ 的 Cauchy 费用，
均在 (C.18) 内。此处 metric 方向在整个根 germ 为0；
只有实际状态响应进入这个导数。

单根有限部准确为
$b_e[\tfrac12\int_0^H\langle V\rangle/\sqrt\xi\,d\xi
-5/(48H^{3/2})]$。因此其 $\beta$ 导数是
$-b_e\int_0^H\langle\dot V\rangle/\sqrt\xi\,d\xi/4$。
参考 $b_e$ 不变；constant canonical cut 到原固定 $t$ cut 的
有向 graph 差再付 $|\kappa_c|<2^{17}b_e$ 和 (C.18)。
两者合计小于 $2^{128}b_e\widehat n_i$。
真正 finite-part 发散项已先相消，未比较两个发散积分。

把边界、两个根和全 strict 段相加，可统一写为
$$
 |\dot\beta_{i,\rm response}|
       <2^{224}J_i^3\delta_i^{-5}\widehat n_i .
 \tag{C.19}
$$
两个 mean 及物理高度乘子都已在 (C.5)--(C.19) 中。

principal 行使用
[真正两射线响应](R133-supplement-actual-compact-ray-endpoint-response.md)。
控制所在分量的直接径向端值为0；其它分量没有直接 metric 支集。
其一般响应式先按实际 $\widehat n_i$ 读取，再用 (C.16)。
连同标准角 $x=4\theta$ 及 $\sqrt{B_i}<2^4\sqrt{J_i}
\delta_i^{-3/4}$，得到
$$
 \sqrt{B_i}\|\dot R_i\|_{C^6_*}
       +B_i^{-1/2}|\dot\beta_i|
 <2^{1100}\mathcal W_i\mathcal XP_j\rho^5 .
 \tag{C.20}
$$
在控制所在分量，(C.15) 的正规化后项为
$2^{128}n\Delta\rho^5$，也落在 (C.20) 内。
所有其它分量都只消费其自己的 $\widehat n_i$；
没有把最浅行的粗值填入每一深层。

## 5. 全部两参数的真实联立导数

这里只线性化已经存在的联合全纯 $\Gamma^*(\mathbf a,\Omega)$；
不把 rotation number 当作整个圆周 map 空间的一个免费光滑函数。
在当前真实共轭
$\mathcal R_i\circ h_i=h_i\circ T_{\omega_i}$ 上，令
$H_i=h_i'\circ T_{\omega_i}$。完整参数变分的平均行准确是
$$
 \left\langle
   \frac{(D_\Gamma\mathcal R_i[\dot\Gamma])\circ h_i}{H_i}
 \right\rangle
 =-\left\langle\frac{\dot{\mathcal R}_{i,\psi}\circ h_i}{H_i}
                                                     \right\rangle.
 \tag{C.21}
$$
$\dot h_i/h_i'$ 的 coboundary 平均为0；参数列始终在当前 $h_i$
处评价。第二行是
$D_\Gamma\beta_i[\dot\Gamma]=-\dot\beta_{i,\psi}$。
二者共同保留全部交叉层。

把第一行按物理角改回并乘 $\sqrt{B_i}$，第二行除以 $\sqrt{B_i}$。
径向对角块就是
$$
 A_i^0=
 \begin{pmatrix}T_{1,i}&T_{2,i}\\-B_{1,i}/2&-B_{2,i}/2\end{pmatrix}.
$$
原整个真实盒的行列式下界 $|\det A_i^0|>2^{-12}$、
显示的两 bump 系数界给
$$
 \|(A_i^0)^{-1}\|_{\ell^1_2\to\ell^1_2}<2^{15}.
 \tag{C.22}
$$
没有用一个只在径向原点的导数替代当前真实块。

以下同时支付完整非对角行。当前强尾的 KAM 输入可取
$\varepsilon_i=2^{36}J_i(N_{j_i}^c)^\#A_*$。
由原逐步估计
$\|v_i\|<20e_n\varepsilon_i(\gamma_i^{\rm D})^{-1}d_n^{-2}$，
$e_n\le\bar a2^{-8n}$、$d_n=2^{-n-4}$，再求一个角导并求和，
$$
 \|h_i'-1\|<2^{19}\varepsilon_i\bar a/ \gamma_i^{\rm D}
            <2^{96}J_i^2\delta_i^{-1}\mathcal N_i\mathcal X .
 \tag{C.23}
$$
这里 $\sum_n80\,2^{12}2^{-5n}<2^{19}$；
$1/\gamma_i^{\rm D}<2^{34}\sqrt{j_i}\delta_i^{-3/4}$。
这是逐行界，不仅是旧全局 $\mu_{\rm KAM}$ 的上界。

实际非径向 return 减径向平移的全角幅度小于
$2^{20}J_i\mathcal N_i\mathcal X$。
在整个 $\ell^\infty$ 参数方向上取半径 $2^{-32}$ 的复盘，
其导数小于 $2^{53}J_i\mathcal N_i\mathcal X$。
实际 $\beta-\beta_{\rm radial}$ 用原
$2^{144}J_i^3\delta_i^{-5}\mathcal N_i\mathcal X$，
同一全参数 Cauchy 费用为 $2^{33}$。
与 (C.23)、$\|H_i^{-1}\|<2$ 合并，真实 normalized 矩阵满足
$$
 A=A^0+E,\qquad
 \|(E\dot\Gamma)_i\|_1
 <2^{256}\mathcal W_i\mathcal X\|\dot\Gamma\|_{\ell^\infty(\ell^1_2)} .
 \tag{C.24}
$$
整向量复盘支付的是完整行范数，未逐列取界后丢掉无限列和。

由 (C.3)，
$\|(A^0)^{-1}E\|<2^{160295}\mathcal X<1/2$。
所以整个实际平均/第二相位行可一起反演，norm 小于 $2^{16}$。
用 (C.20) 的真实 forcing，得到
$$
 \|\dot\Gamma^*\|_\infty
       <2^{161140}\mathcal XP_j\rho^5 .
$$
再把这个全局解代回第 $i$ 行，而不丢掉其 $\mathcal W_i$，
得到真正逐行结论
$$
 \boxed{\quad
 |D_\psi\gamma_{1,i}^*|+|D_\psi\gamma_{2,i}^*|
       <2^{1120}\mathcal W_i\mathcal XP_j\rho^5 .
 \quad}                                                     \tag{C.25}
$$
具体地，第一项为 $2^{1115}\mathcal W_i\mathcal XP_j\rho^5$；
反馈项相对于它小于 $2^{160296}\mathcal X<1/2$。
原两个相位的径向显式 $\psi$ 导数准确为0，所以右边没有一个
未支付的径向 $O(1)$ 列。

这也说明相位等变性：$\psi$ 是径向方向，原联合选择在
$\mathbf a_m\mapsto e^{im\phi}\mathbf a_m$ 下不变，
故 (C.25) 的真实参数导数在该轨道上同样不变。
最终选择一个目标度量后，整个相位轨道仍共用它。

## 6. 两参数列对整负窗型的实际费用

需要一个比第70束多一角导的完整物理估计。相同证明改用
$\mathcal F_{7/2}$ 和 root balanced $H^4$，仍在原闭窗内：
$$
 \sup_{I_i}
 [\|u\|_{H^2}^2+(1+Q)\|u_\theta\|_{H^1}^2+\|v_J\|_{H^1}^2]
       <2^{8400}J^{20}\delta^{-34}\|Z_M(c)\|_2^2,
 \qquad v_J=\pi/\sqrt{\mu_0}.
 \tag{C.26}
$$
详细的新费用如下。中心输入平方多付 $M^2\le B$；
strict 恢复式再求一次角导，仅对已经完整支付的解析乘子求导。
根图对 $U,U_\phi,U_{\phi\phi},U_\xi,U_{\xi\phi},U_{\xi\xi}$
使用径向基本定理。最后一个的径向导数由
$$
 U_{\xi\xi\xi}=b^{-2}U_{\phi\phi}
          +(\xi/b^2)U_{\xi\phi\phi}-V_\xi U-VU_\xi
$$
给出。$|V_\xi|<129$、两角导由同一已付复域控制，
完整额外 trace 常数可取 $2^{44}$；物理 chain rule 放宽到
$2^{128}b\|\mathcal Y\|_{H^4}^2$。
根区和 strict 区的 $\delta$ 次数因此分别为 $125/4,131/4<34$；
$J$ 次数至多 $33/2<20$。全部二进制费用低于8400。
这里确实支付了输出导数，没有以有限输入声称输出无穷尾消失。

第61束 $\mathcal K_{\rm act}$ 的完整型只需
$u_\theta,v_J,(v_J)_\theta$ 和一阶角系数；其 $Q$ 已被准确消去。
当前系数、$f_k$、$\mathcal Bd$ 及所需角乘子小于 $2^{20}$，
所以 $|\mathcal K_{\rm act}|\le2^{40}$ 乘 (C.26) 的能量。
两个原 bump 的幅度小于1，整个负窗长度小于1。
由 (C.25)，本窗直接 metric 补偿贡献除以 $d_*$ 后小于
$$
 2^{22000}\mathcal N_{i|j}\mathcal X J^{92}\delta_j^{-68}.
 \tag{C.27}
$$
这里 $\mathcal N_{i|j}$ 是第70束包含完整邻胞的六项和。
较深编号相对控制胞元至多再多付 $2^{10}$。
具体二进制和为
$8400+40+1120+10+10980+133+77+1000-42=21718<22000$；
真实 $\delta$ 费是 $40+57/2-25/8+231/128<68$，$J$ 次数91。
首层 (C.27) 的对数小于
$$
 22000-20010-1048576+14\cdot92+8197\cdot68
                 =-487902<-480000 .
 \tag{C.28}
$$
其无限层比也严格小于1。

还须加入全部 $\Gamma$ 引起的背景响应，不能只计本窗两个 bump。
原完整复参数图和局部四态界，在同一方向盘 $2^{-32}$ 上给
$$
 \widehat n_i^{\,\Gamma}
 <2^{64}\mathcal N_i\mathcal X\|\dot\Gamma^*\|_\infty
 <2^{161204}\mathcal N_i\mathcal X^2P_j\rho^5 .
 \tag{C.29}
$$
这里减去每个实际 bump 的局部 $F_1$ gauge；
其规范化四态为 $O(\mathcal N_i\mathcal X)$，
$D_\Gamma w/w$ 由真实 bump 幅度支付。
使用整个 $\ell^\infty$ 复方向，所有其它层的反馈也已包含。

由第70束的整窗物理能量和同一 $\mathcal H$ 商法则，
(C.29) 的额外型除以 $d_*$ 后小于
$$
 2^{182000}\mathcal N_{i|j}\mathcal X^2J^{84}\delta_j^{-60}.
 \tag{C.30}
$$
未放宽的二进制费为181176；首层对数小于
$182000-20010-2\cdot1048576+14\cdot84+8197\cdot60
=-1442166<-1400000$。真实全局规范与全部邻胞都在这里。

## 7. 完整沿选择支的型、两端和源

令 $\varphi_{s,i}$ 是两个原 metric bump，并在各自负窗写
$$
 \Psi_{\rm tot}=\psi+\dot\gamma_{1,i}^*\varphi_{1,i}
                         +\dot\gamma_{2,i}^*\varphi_{2,i},\qquad
 \widehat z_{\rm tot}
    =D_\psi(p,k)+D_\Gamma(p,k)[\dot\Gamma^*]
                                      -\Psi_{\rm tot}F_1 .
 \tag{C.31}
$$
其它窗的 $\psi=0$，但其参数和背景响应没有清零。
真实 $\dot Q=-(\Psi_{\rm tot})_t$，所以第61束完整 gauge 恒等式
直接适用；根附近 $\Psi_{\rm tot}$ 及其 jets 为0。

第69/70束的 $\psi$ 部分、(C.27) 的本窗 metric 补偿及
(C.30) 的全部参数背景响应相加，得到
$$
 \boxed{\quad
 \int_{I_i}
 [\Psi_{\rm tot}\mathcal K_{\rm act}(Y)
                -\mathcal H_{\widehat z_{\rm tot}}(Y)]dt
       >\frac{d_*}{8}\|Z_M(c)\|_2^2,\qquad
 Y_c\in\mathcal E_M,\quad M^2\le B .
 \quad}                                                     \tag{C.32}
$$
这一次已经沿实际两相位选择支求导，未固定 $\Gamma^*$。
正定型仍以真实整窗、固定原 physical 端点和中心两迹来定义。
不同频率中心数据的交叉矩阵不是 (C.32) 的量词，不能自行删除。

原 ordinary/weak 源及其参数列是
$$
 s=(-aF^t,\ g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat s_{\rm tot}
   =D_{\psi,\Gamma^*}s-\Psi_{\rm tot}\mathsf B s .
 \tag{C.33}
$$
它们与全部两 mean 共同按原有序 Duhamel 传播，仍没有 $F_t^t$。
物理 $\pi_{0,t}=g_0$，高度 mean 是
$\langle dh_\theta+a\pi-aF^t\rangle$；
bare-flux 两端另需真实 $F^t$ 迹。
根/变图源沿原 Piola、height 和 normal-shear 公式消费，(C.26)
对齐次状态的图迹估计没有转授任意粗源新的径向正则性。

最后，本篇仍保留 physical principal 端图的参数依赖。
已经支付的是实际相位函数的平均行与完整 physical crossing form；
不是裸 pullback 的同阶 operator-norm 导数。
fresh 支集转到已经启用的第68束盒内时，径向补偿本身一般非零，
必须先减掉并重新接上真实 $D_\Omega\bar\Gamma$。
随后还需完整混频簇和高低网络接线，才能消费这些方向去闭合
非线性 $\mathcal F$。本篇没有作这些未证推断。

必要代数及有理预算：
[源码](../scripts/fourfold_actual_two_phase_compact_response_20261114.py)，
[实际记录](../notes/2026-11-14-R119-actual-two-phase-compact-response-budget.json)。
