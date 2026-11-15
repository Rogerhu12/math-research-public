# R224：共同偶 germ 的完整 ruling 偶部不变量与正 ε 严格障碍

日期：2026-11-15。**完整纸面证明；无新的研究计算。**

来源为 [R56 完整右锚恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 逐点八矩及真实历史](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R184 全部二、三阶 gauge 的 joint 判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R193 原八包四系数正性](R193-full-width-positive-obstruction-for-frozen-eight-derivative-packets.md)、[R216 四阶平点门](R216-fourth-ruling-obstruction-at-a-single-flat-state-point.md)、[R218 共同偶非平 germ](R218-common-even-nonflat-germs-and-exact-universal-pure-control.md)及 [R221 完整 ruling 矩映射](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)。

本稿给一个适用于正 $\varepsilon$ 的新必要门。它不把常态的 $\sigma^2$ 项直接延续为非平 germ 的障碍，而先准确计算所有允许 gauge 的**偶部像**。在标准 $k=\omega=0$ germ 上，再用同中心局部解析模型的增长证明：R193 同一个原八包及其已付光滑邻域，在每个实际允许的正宽度和任意正 $\varepsilon$ 下，均不能通过完整第四 ruling。

真实二、三阶传入历史不设为零；它们在偶部商中的消失由完整恢复组合证明。用于增长比较的解析延拓只延拓局部公式，不延长实际闭路径。

## 1. 固定几何、固定圆及偶部

固定 R184 的同一个真实几何、目标度量和第一圆

$$
\phi_\theta=\cos\theta\,f+\sin\theta\,g,\qquad
D_\theta=f^2-\phi_\theta^2,
\tag{1}
$$

并假设 canonical 二、三阶已通过周期与双 collar range。全部 profile 使用同一个固定区间 $I=[\ell,r]$、共同零 collar 和右积分

$$Jv(\xi)=\int_\xi^r v(\eta)\,d\eta.$$

取真实几何点 $s_*$，写 $\sigma=s-s_*$。假设它的一个双侧开邻域准确具有 R218 germ

$$
\boxed{
h(\sigma)=h_e e^{\varepsilon\sigma^2},\qquad
k(\sigma)=k_e,\qquad \omega(\sigma)=\omega_e,\qquad
h_e>0,\quad\varepsilon>0.
}
\tag{2}
$$

其中 $\xi+\omega_e>0$ 于共同物理区间。若 $s_*$ 是周期首末接口，双侧邻域按真实周期识别。使用同一个真实 frame；下文只取内积，frame 的共同旋转不改变任何式子。

对 germ 函数定义

$$
\operatorname{Ev}A(\sigma)=
\frac{A(\sigma)+A(-\sigma)}2.
\tag{3}
$$

置

$$
d=h\omega_e-k_e,\quad e=h\xi+d,\quad
\gamma=h_s,\quad\delta=d_s,\qquad
\mathbf w=
\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{4}
$$

于是 $h,d,e,\mathbf w$ 为偶函数，$\gamma,\delta,e_s$ 为奇函数。记局部三矩空间

$$
\mathcal W_e=\{\sigma\mapsto\mathbf w(\sigma)\cdot v:
v\in\mathbb R^3\}.
\tag{5}
$$

这是全局第三 gauge 空间在该 germ 上的限制，允许其三列有真实依赖。

为避免与 R56 的几何多项式 $K_0$ 混淆，原 canonical 第四 ruling 在本文记为 $\mathscr K^0_\theta$。

## 2. 完整 gauge ruling 的偶部准确落在三矩空间

R73 的逐点第二密度为

$$
r_s(a,b)=\Phi_{M_{\rm raw}(s)}(a,b),\qquad
\mathsf m(s)=\int_{s_0}^s M_{\rm raw}(t)\,dt.
\tag{6}
$$

积分起点 $s_0$ 是原全字起点。令

$$
\mathsf m(\sigma)=\mathsf m_*+\mathsf o(\sigma),\qquad
\mathsf m_*=\mathsf m(s_*),\qquad
\mathsf o(\sigma)=\int_0^\sigma M_{\rm raw}(\tau)\,d\tau.
\tag{7}
$$

**引理 1。** $M_{\rm raw}$ 在 germ 上为偶函数，所以 $\mathsf o$ 为奇函数。

**证明。** R73(4)–(6) 中状态零阶项都是偶函数。其余项只有
$\gamma e_s,\gamma^2,\lambda\gamma,\lambda d_s$ 等两项奇函数之积，其中
$\lambda=e_s/h^2$ 为奇。故六项式的全部系数偶。固定 E8 的坐标重建是线性的，全部八坐标亦偶。没有作 $s$ 分部积分，也没有删除真实 $\mathsf m_*$。证毕。

R221 的完整局部三线性项为

$$
\begin{aligned}
\mathcal T_s(c;a,b)=\frac1{32h^4}\int_I\Big[
&Q^2c'''\{\gamma(a'b''+a''b')-e_sa''b''\}\\
&-2h\gamma eQ\,c'''a'b'\\
&+(Qc''-2hec'+2h^2c)
\{(\gamma Q-2hee_s)a''b''-2h^2\gamma a'b'\}
\Big]\,d\xi,
\end{aligned}
\tag{8}
$$

其中 $Q=1+e^2$。每一项恰含一个 $\gamma$ 或 $e_s$，其余几何因子偶。因此 $\mathcal T_s(c;a,b)$ 在 germ 上为奇函数。这包括 R221 的全部 18 个局部几何项；右尾已经在 (8) 中真实转置，不曾置零。

令

$$
\mathsf A_*=\Phi_{\mathsf m_*},\qquad
\mathsf A_{\rm odd}(\sigma)=\Phi_{\mathsf o(\sigma)}.
$$

由 R221(12)，任意固定 profile $w$ 的完整线性 ruling 响应为

$$
\begin{aligned}
\mathcal B_\theta(w)
={}&2\mathcal T_s(w;D_\theta)
-4\mathcal T_s(\phi_\theta;\phi_\theta,w)\\
&-2\mathcal E_s((\mathsf A_*+\mathsf A_{\rm odd})D_\theta,w)\\
&+4\mathcal E_s(\phi_\theta,
(\mathsf A_*+\mathsf A_{\rm odd})(\phi_\theta,w)),
\end{aligned}
\tag{9}
$$

其中

$$
\mathcal E_s(a,b)=\mathbf w(s)\cdot\mathbf m(a,b).
$$

于是准确有

$$
\boxed{
\operatorname{Ev}\mathcal B_\theta(w)
=\mathbf w(\sigma)\cdot
\left[
-2\mathbf m(\mathsf A_*D_\theta,w)
+4\mathbf m(\phi_\theta,\mathsf A_*(\phi_\theta,w))
\right]\in\mathcal W_e.
}
\tag{10}
$$

特别地，24 个真实 history 项的偶部只剩真实常值 $\mathsf m_*$ 乘三列 $\mathbf w$，没有把它们分别设零。

式 (10) 对任意同 collar 的 $w$ 都成立，尚不需要施加新增第三 range 的合法性条件。故它当然覆盖 R184 全部允许的光滑相位 $w_\theta$，而不局限六矩为零的充分子类。

R184 的平方项及第三齐次项分别是

$$
-\mathbf w\cdot\mathbf m(w_\theta,w_\theta),\qquad
-2\mathbf w\cdot\mathbf m(\phi_\theta,\chi_\theta),
$$

也都属于 $\mathcal W_e$。因此

$$
\boxed{
[\operatorname{Ev}\widetilde{\mathscr K}_\theta]
=
[\operatorname{Ev}\mathscr K^0_\theta]
\quad\text{于 }C^\infty_{\rm even}/\mathcal W_e.
}
\tag{11}
$$

**偶部必要门：**

$$
\boxed{
\operatorname{Ev}\mathscr K^0_\theta\in\mathcal W_e
\quad\text{对全部 }\theta.
}
\tag{12}
$$

这与完整 period 是否已经支付无关；若 (12) 失败，任一合法全局二阶 gauge 及全部第三齐次改动都不能支付第四 ruling。

## 3. 三矩偶空间及准确微分恒等

由 (4)，

$$
\mathbf w_0=\frac{1+k_e^2}{4h}-\frac{k_e\omega_e}{2}
+\frac{\omega_e^2h}{4},\quad
\mathbf w_1=-\frac{k_e}{2}+\frac{\omega_e h}{2},\quad
\mathbf w_2=\frac h4.
\tag{13}
$$

因 $\varepsilon>0$，$h,h^{-1},1$ 在任何 germ 开区间上真线性独立。故

$$
\mathcal W_e=
\begin{cases}
\operatorname{span}\{1,e^{\varepsilon\sigma^2},
e^{-\varepsilon\sigma^2}\},&k_e\ne0,\$$2mm]
\operatorname{span}\{e^{\varepsilon\sigma^2},
e^{-\varepsilon\sigma^2}\},&k_e=0.
\end{cases}
\tag{14}
$$

这里第二行不要求 $\omega_e=0$；$h_e$ 只改变常系数。

令 $t=\sigma^2$，对偶光滑函数使用可去的算子

$$
\mathcal D_t=\frac1{2\sigma}D_\sigma.
$$

则 (12) 等价于以下整个 germ 的准确 ODE：

$$
\begin{cases}
(\mathcal D_t^3-\varepsilon^2\mathcal D_t)
\operatorname{Ev}\mathscr K^0_\theta=0,&k_e\ne0,\\
(\mathcal D_t^2-\varepsilon^2)
\operatorname{Ev}\mathscr K^0_\theta=0,&k_e=0.
\end{cases}
\tag{15}
$$

例如若 $A(\sigma)=\operatorname{Ev}\mathscr K^0_\theta(\sigma)$，所有相应中心 jets 必须满足

$$
A^{(2m+4)}(0)
=4(2m+3)(2m+1)\varepsilon^2A^{(2m)}(0),
\tag{16}
$$

其中 $k_e\ne0$ 时 $m\ge1$，$k_e=0$ 时还包括 $m=0$。首条分别为

$$
A^{(6)}(0)-60\varepsilon^2A''(0)=0,\qquad
A^{(4)}(0)-12\varepsilon^2A(0)=0.
\tag{17}
$$

实际 canonical germ 是实解析的：R56 的有限分离表示只有关于 (2) 的解析几何系数、固定 profile 积分及有限阶三角 ODE。因此对该 germ，全部 (16) 也充分给出 (15)。单独一条或有限若干条只作为必要门。

式 (14) 解释了不能直接使用常态 $\sigma^2$ 项的原因：

$$
\frac{e^{\varepsilon\sigma^2}-e^{-\varepsilon\sigma^2}}
{2\varepsilon}\longrightarrow\sigma^2.
$$

三矩系数可以随 $\varepsilon$ 发散。常态的非零二次项本身不证明任一正 $\varepsilon$ 的 (15) 失败。

## 4. 真正中心化：只在商中消掉传入 history

以下取 R183/R199 的合法三矩圆，故

$$
\mathbf m(D_\theta)=
\mathbf m(f,f)-\mathbf m(\phi_\theta,\phi_\theta)=0.
\tag{18}
$$

对任一固定矩阵 $\mathsf m_*$，R73 六项式的局部部分在两 collar 为零，三个真实右尾的左值由 (18) 为零。因此

$$
w^*_\theta=\mathsf A_*D_\theta
\tag{19}
$$

是真正同 collar 的固定光滑 profile，而非带未记录二次左尾的对象。

用同一个右锚，在局部模型中取中心第二累计矩阵
$\mathsf o(0)=0$，得到

$$
\widehat Z_\theta
=K_s(D_\theta)-Y_{\Phi_{\mathsf o(\sigma)}D_\theta}.
\tag{20}
$$

然后按 R56 对 forcing
$-2H(Y_{\phi_\theta},\widehat Z_\theta)$ 恢复第三场
$\widehat U_\theta$，只把其中心 characteristic 初值规定为零。所有局部 normal 与 $\eta$ 恢复项仍由原 forcing 决定，不能同时置零。

与真实原历史的差准确为

$$
Z_\theta=\widehat Z_\theta-Y_{w^*_\theta},
$$

$$
U_\theta=\widehat U_\theta
+2\widehat Z_B(\phi_\theta,w^*_\theta)
+Y_{\chi^*_\theta}.
\tag{21}
$$

第一式直接来自 (7)。第二式来自 R56 线性恢复及两个第三 forcing 的差
$2H(Y_{\phi_\theta},Y_{w^*_\theta})$；其剩余齐次差是一个与 $\sigma$ 无关的 profile $\chi^*_\theta$。它记录真实第三初值，没有将原 $W_3$ 设零。

中心化模型未必满足左 collar 的第三 range，所以 $\chi^*_\theta$ 不必另被宣称为一个合法全局 gauge。但与紧支撑 $\phi_\theta$ 的 ruling 配对仍有
$\mathcal E_s(\phi_\theta,\chi^*_\theta)=
\mathbf w\cdot\mathbf m(\phi_\theta,\chi^*_\theta)$；
R221 已支付这个单紧支撑槽的真实端项。所有值在固定 I 上存在。

中心矩阵为奇函数，所以 (10) 对中心模型给
$\operatorname{Ev}\widehat{\mathcal B}_\theta(w^*_\theta)=0$。
把 (21) 代入完整第四 forcing，得到

$$
\boxed{
\operatorname{Ev}\mathscr K^0_\theta
=
\operatorname{Ev}\widehat{\mathscr K}_\theta
-\mathbf w\cdot
\left\{\mathbf m(w^*_\theta,w^*_\theta)
+2\mathbf m(\phi_\theta,\chi^*_\theta)\right\}.
}
\tag{22}
$$

这才是在 ruling 偶部商中与前缀历史无关的准确原因。

实际上中心模型的 $\widehat{\mathscr K}_\theta$ 自身为偶：

- 第一场的 TB 分量偶，N 分量为零；
- 第二局部 normal 分量偶，$\eta_2$ 奇，中心第二 history 奇，所以第二场 N 偶、TB 奇；
- 完整第三 forcing 的 $J,T_\xi,T_s$ 奇，$T_{s\xi}$ 偶；R56 因而给 $P_3,B_3$ 奇、characteristic RHS 奇、中心 $W_3$ 偶、$\eta_3$ 偶；
- 第三场 TB 偶、N 奇。第四 ruling 的
  $Z_u\cdot Z_u+2Y_{\phi,u}\cdot U_u$ 因而偶。

协变导数的框架矩阵把 TB 与 N 互换，上述奇偶已经包含这个作用；不是只对标量分量作普通导数。因此

$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\quad\bmod\mathcal W_e.
\tag{23}
$$

## 5. 标准 $k_e=\omega_e=0$ germ 的两个真实二阶系数

现在取

$$
k_e=\omega_e=0,\qquad
h=h_e e^{\varepsilon\sigma^2},\qquad
v=\frac{h_s}{h}=2\varepsilon\sigma.
\tag{24}
$$

定义固定 E8 算子

$$
\mathsf R(a,b)=a'b'+\xi J(a''b''),\qquad
\mathsf T(a,b)=\xi^2a'b'
+\xi J(\eta^2a''b''+2a'b').
\tag{25}
$$

它们分别是 R73 的单位 $r_1,t_1$ 坐标。直接代入 R73(4)–(6)，除这两坐标外全部为零，且

$$
\boxed{
r_s=a(\sigma)\mathsf R+b(\sigma)\mathsf T,\qquad
a=\frac{v^2-1}{8h^2},\qquad
b=-\frac{1+v^2}{8}.
}
\tag{26}
$$

令真实中心累积系数为

$$
A(\sigma)=\int_0^\sigma a(t)\,dt,\qquad
B(\sigma)=\int_0^\sigma b(t)\,dt
=-\frac{\sigma}{8}-\frac{\varepsilon^2\sigma^3}{6}.
\tag{27}
$$

对于每个固定 $\varepsilon>0$，$a$ 是多项式乘衰减高斯函数，故 $A$ 有界；而

$$
B(\sigma)^2\sim\frac{\varepsilon^4\sigma^6}{36}
\quad(\sigma\to+\infty).
\tag{28}
$$

注意 (27) 是准确原函数，不是常态近似。

为追踪局部项，置

$$
\mathcal H(q)=\frac q\xi-\frac12q'.
$$

第一场在真实正交框架中的物理分量为

$$
Y_q=\left(-\frac{q'}{2\xi},\,0,\,h\mathcal H(q)\right).
\tag{29}
$$

R221(14) 在 (24) 上逐项化为

$$
\boxed{
\eta_{ab}
=\frac{v}{16h}\bigl(\mathsf R(a,b)\bigr)'
-\frac{hv}{8}\mathcal H\bigl(\mathsf T(a,b)\bigr).
}
\tag{30}
$$

验证只需
$\mathsf R'=a'b''+a''b'-\xi a''b''+J(a''b'')$
以及
$\mathsf T'-2\mathsf T/\xi=-2\mathcal H(\mathsf T)$。
因此没有丢掉任何右尾。

第二 normal 分量另有

$$
\rho_{ab}=h\,\rho^+_{ab}+h^{-1}\rho^-_{ab},
\tag{31}
$$

其中固定 profile 为

$$
\rho^+_{ab}
=\frac{ab}{2\xi}-\frac{ab'+a'b}{4}
+\frac{\xi a'b'}4+\frac18J_2^*(a,b),
$$

$$
\rho^-_{ab}
=\frac18\left(J_0(a,b)+\frac{a'b'}{\xi}\right).
$$

式 (30)、(31) 连同
$K_s=(\eta/(h\xi),\rho,\eta)$ 给第二局部场的全部分量。以下增长论证不把它省略，只准确比较其阶数。

## 6. 完整第三动态的最高增长与误差界

本节将同中心解析模型延拓到全部实 $\sigma$。$h,h^{-1}$ 及所有有限几何系数实解析，固定 profile 积分仍是常系数；R56 是有限阶三角恢复，所以这个形式局部模型有整个实轴的唯一解析延拓。物理 $\xi>0$ 始终不变。

这只是用来检验一个局部解析身份；实际闭路径并未延长。

固定相位，并记

$$
R_D=\mathsf R(D_\theta),\quad
T_D=\mathsf T(D_\theta),\quad
O_D=A R_D+B T_D.
$$

由 (20)，

$$
\widehat Z_\theta=K_s(D_\theta)-Y_{O_D}.
\tag{32}
$$

全部估计均在固定紧 I 的任意一个所需有限 $C^m_\xi$ 范数中成立；常数可依赖 $\varepsilon,h_e,f,g$，不需对 $\varepsilon\downarrow0$ 一致。$\xi$ 与零有正距离。

### 6.1 真实 chain 项与局部第三项

R73(15) 在 (24) 上的准确额外链式算子是

$$
\boxed{
\Psi_s(a,b)=-\frac v8\{\mathsf T(a,b)+h^{-2}\mathsf R(a,b)\}.
}
\tag{33}
$$

因此中心第三 characteristic history 满足

$$
(\widehat W_3)_s
=-2\ell_s(\phi_\theta;D_\theta)
+2r_s(\phi_\theta,O_D)
+2\Psi_s(\phi_\theta,(O_D)_s),
\tag{34}
$$

其中 $\ell_s=R[H(Y_\phi,K_s(D))]$ 是整个真实局部场的 forcing，保其全部 $s$ 导数。

从 (29)–(31) 和 R56(5) 可直接给

$$
\ell_s(\phi;D)=O(1+\sigma^3),\qquad
\Psi_s(\phi,(O_D)_s)=O(1+\sigma^3).
\tag{35}
$$

为说明第一界没有隐藏正指数项：$K_s$ 的 T 分量为 $O(1+\sigma)$，N 分量为 $O(h+h^{-1})$，B 分量为
$O((h+h^{-1})(1+\sigma))$；协变导数使其中最高多项式阶只增加一。故 $T_s/(2h^2)$ 为 $O(1+\sigma^3)$。相应 $P,B$ 是
$O((h+h^{-1})(1+\sigma))$，其 $s$ 导数最高为
$O((h+h^{-1})(1+\sigma^2))$。R56 中的
$K_0=-\xi/h$、$\lambda=v\xi/h$ 和 $\gamma/h^2=v/h$
正好消掉正 h 幂。剩余负 h 幂衰减，得到 (35)。

第二界由 (33)、$(O_D)_s=aR_D+bT_D$ 直接成立，不得省略这项。

在 $2r_s(\phi,O_D)$ 中唯一五次多项式主项为

$$
2bB\,\mathsf T(\phi,T_D)
=(B^2)_s\,\mathsf T(\phi,T_D).
$$

其余含 $bA$ 的项积分为 $O(1+\sigma^3)$；含 $aA,aB$ 的项因高斯衰减可积。由中心初值为零及 (34)、(35)，

$$
\boxed{
\widehat W_3
=B^2\,\mathsf T(\phi_\theta,T_D)+O(1+\sigma^4).
}
\tag{36}
$$

这个主项的系数为 1，来自第三 forcing 的准确因子 $-2$ 和
$Z=K-Y_O$，不是从常状态结果类比所得。

### 6.2 第三恢复的局部部分较低

第三场仍是 R56 的完整恢复

$$
\widehat U_\theta=K_{3,s}-Y_{\widehat W_3}.
$$

由 (32)，第二场 T 为 $O(1+\sigma^3)$，N 为 $O(h+h^{-1})$，B 为
$O((h+h^{-1})(1+\sigma^3))$。其真实协变导数及 R56(6) 给

$$
\eta_3=O((h+h^{-1})(1+\sigma^4)).
\tag{37}
$$

具体地，第三 $P,B$ 为
$O((h+h^{-1})(1+\sigma^3))$，其一次 s 导数和
$T_{s\xi}/h$ 为 $O((h+h^{-1})(1+\sigma^4))$；(6) 的其余速度因子至多再给同一次幂。这保留全部局部恢复，并足以说明
$K_{3,s}$ 的 TB ruling 配对为 $O(h(1+\sigma^4))$。其 N 分量与 $Y_\phi$ 的 ruling 导数正交，不需假设它为零。

## 7. 偶部的准确非三矩增长

定义两个固定 profile 双线性型

$$
E_-(a,b)=\frac14\int_Ia''b'',\qquad
E_\infty(a,b)=\frac14\int_I
(\xi^2a''b''+2a'b').
\tag{38}
$$

在 (24) 上，R221 的原 ruling 能量准确是

$$
\mathcal E_s(a,b)=h^{-1}E_-(a,b)+hE_\infty(a,b).
\tag{39}
$$

$T_D$ 为同 collar profile，因为 (18) 使全部 E8 尾为零。若另一槽有真实左尾，(39) 与紧支撑槽的配对仍按 R221 的端项证明成立。

由 (30)–(32)、$A=O(1)$，第二场中
$-B Y_{T_D}$ 的平方是唯一 $hB^2$ 级项。其余局部项或交叉项至多为
$O(h(1+\sigma^4))+O(h^{-1}(1+\sigma^6))$。
由 (36)、(37)，第三场与 $Y_\phi$ 的同级项准确来自
$-B^2Y_{\mathsf T(\phi,T_D)}$。故

$$
\boxed{
\lim_{\sigma\to+\infty}
\frac{\widehat{\mathscr K}_\theta(\sigma)}
{h(\sigma)B(\sigma)^2}
=
\mathscr C_\theta
:=-E_\infty(T_D,T_D)
+2E_\infty(\phi_\theta,\mathsf T(\phi_\theta,T_D)).
}
\tag{40}
$$

这是完整 forcing
$-H(Z,Z)-2H(Y_\phi,U)$ 的符号和因子。它不删第三局部项；这些项由 (37) 在除以 $hB^2$ 后趋零。

另一方面，任一 $\mathcal W_e=\operatorname{span}\{h,h^{-1}\}$ 函数满足

$$
\frac{c_1h+c_2h^{-1}}{hB^2}\longrightarrow0.
\tag{41}
$$

如果 (12) 在实际 germ 上成立，(22) 迫
$\widehat{\mathscr K}_\theta\in\mathcal W_e$ 于该 germ。两边都是同一中心模型的实解析函数，因此恒等延拓到整个实轴，(40)、(41) 便迫

$$
\boxed{\mathscr C_\theta=0\quad\text{对全部 }\theta.}
\tag{42}
$$

式 (42) 是正 $\varepsilon$ germ 的严格必要条件，与
$\varepsilon$ 的大小无关；证明没有在 $\varepsilon=0$ 附近取一致误差。

## 8. 与 R193 的 $c_6$ 准确对齐

设 $q=f+ig$，普通复双线性延拓 (25)、(38)。令

$$
\mathscr F_T(q)=
E_\infty(\mathsf T(q,q),\mathsf T(q,q))
+2E_\infty(q,\mathsf T(q,\mathsf T(q,q))).
\tag{43}
$$

R53 的有限相位代数对任意对称二次算子及对称能量成立。因此 (40) 中 $e^{-4i\theta}$ 的**实部展开复幅**是

$$
\boxed{(\mathscr C)_4=-\frac18\mathscr F_T(q).}
\tag{44}
$$

现在逐项核标准常状态的规范。R73 在 $h=1,k=\omega=0$ 给

$$
\mathcal R_0=-\frac18(\mathsf R+\mathsf T),\qquad
E_0=E_-+E_\infty.
\tag{45}
$$

对 $q_\lambda(\xi)=q_{\rm raw}(\xi/\lambda)$，置 $\xi=\lambda x$。
直接由 (25)，

$$
\mathsf R(q_\lambda,q_\lambda)(\lambda x)
=\lambda^{-2}\mathsf R(q_{\rm raw},q_{\rm raw})(x),
$$

$$
\mathsf T(q_\lambda,q_\lambda)(\lambda x)
=\mathsf T(q_{\rm raw},q_{\rm raw})(x).
\tag{46}
$$

同样的双槽换元适用于嵌套项；$E_-$ 增加 $\lambda^{-3}$，
$E_\infty$ 增加 $\lambda^{-1}$。故 R53 的标准
$\mathcal F(q_\lambda)$ 中最高宽度项 $\lambda^{-1}$ 只能来自两次
$-\mathsf T/8$ 和 $E_\infty$，准确为

$$
\frac1{64\lambda}\mathscr F_T(q_{\rm raw}).
\tag{47}
$$

R193 已证明

$$
\lambda^7\operatorname{Re}\mathcal F(q_\lambda)
=c_0+c_2\lambda^2+c_4\lambda^4+c_6\lambda^6,
\qquad c_j>0.
$$

比较 (47)，得到准确身份

$$
\boxed{\operatorname{Re}\mathscr F_T(q_{\rm raw})=64c_6>0.}
\tag{48}
$$

再次用 (46)、(38)，

$$
\mathscr F_T(q_\lambda)=\lambda^{-1}\mathscr F_T(q_{\rm raw}),
$$

所以 (44) 的真实部为

$$
\boxed{\operatorname{Re}(\mathscr C)_4
=-\frac{8c_6}{\lambda}<0.}
\tag{49}
$$

普通复平方与模平方没有混用；$c_6$ 的四个严格正有理槽及正立方根基均来自 R193 已完成的准确结果，本稿没有重算积分。共同正实归一化只乘一个正四次幂。

## 9. 正 ε 标准偶 germ 的全宽度排除及光滑范围

由 (42)、(49) 得到：

**定理。** 取 R193 同一个八包圆，或其 §5 已付的同三矩 $C^\infty$ 平滑邻域。若真实几何包含一个双侧开 germ

$$
h=h_e e^{\varepsilon(s-s_*)^2},\qquad
k=\omega=0,\qquad h_e>0,\quad\varepsilon>0,
$$

则对每个能放入共同物理区间的正宽度 $\lambda$，完整第四 ruling 都不能通过。排除覆盖 R184 全部合法二阶 gauge、全部第三齐次 gauge、任意真实二、三阶入历史；不依赖第四 period 是否已为零。

R193 的 C7 原型用于提供准确系数。真正几何结论可直接取其已经证明的一个光滑邻域：准确三复矩重补后 $c_6$ 仍严格正。本稿没有靠渐近数值或近似矩把它变成 C∞ 例子。

对原冻结支撑，仍需
$[\lambda,155\lambda]\Subset I$；平滑后使用相应略增支撑和严格余量。代数上任意 $\lambda>0$ 的符号，不意味着任意宽度都能放入同一个固定物理区间。

这证明共同偶非平 germ 虽已移除四阶平点，仍可能保留一个独立 ruling 障碍。全域 Morse、整 pure 与有限通量已付的结论均不受影响；它们从未自动支付本稿的偶部商。

## 10. 尚未被排除的范围

一般 $(k_e,\omega_e)$ 的偶 germ 仍有第 2–4 节的准确偶部商、ODE 与中心 history 分离，但本稿没有对其全部 canonical 偶部作增长分类。特别，不把第 9 节的 $k_e=\omega_e=0$ 结论推广为任意端口的排除。

R199 改变末 step 的 faithful 圆应使用自己的完整 $\mathscr F_T(q)$。若其改动另外被限制在一个保持 (48) 严格正的固定支撑 C4 邻域，排除当然仍适用；这里的连续性直接由 (43) 的有限导数与同锚积分给出，不省略嵌套项中的高阶导数。仅有 faithful 性不授这一符号，也不能把 R193 原系数直接移植给任意 R199 圆。

式 (15) 可为其他几何/profile 提供准确必要恒等。通过它仍不说明完整 period 与 odd ruling、或同一个 w 的 R221 联合方程可解。本稿不排除选择其他圆或其他 germ 来支付这些新门，也不构成一般等距机制的不可能性证明。
