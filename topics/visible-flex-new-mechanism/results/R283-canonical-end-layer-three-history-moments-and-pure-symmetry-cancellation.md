# R283：canonical 零端一次层的三历史矩、真实端势与 pure 对称消去

日期：2026-11-15。**完整纸面推导；没有执行新的 profile 求积、符号目标、秩计算或开发检查。**

本稿把 [R276](R276-canonical-fourth-periods-at-analytic-zero-ends-and-finite-first-layer-conditions.md) 与 [R281](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md) 中的有限一次端层，进一步化为三个明确的真实历史数。关键不是重新选择三阶平台值，而是使用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 对该平台值已经强制的齐次方程。

结论有两层。

1. 对任一真实三阶平台尾，与初阶场的完整 cross 恢复，其一次局部层准确是一个二次多项式的一阶作用，加一个真实 s 端势。因此合法第三阶闭合之后，零端只剩三个加权历史矩。
2. 对当前已经付清 whole pure 成本的几何，完全对称的三次历史自动消失。固定种子 f 的整圆，只剩有序跨槽 C(g;f,f) 的一个二次多项式；两个 mixed 周期目标在同一比例活动包上的一次端层不是两个独立函数。

这三个剩余数尚未被评价，也没有在本文证明它们由全部 Gaussian 面积或六条能量条件推出。本文不宣称第四 period 或 joint ruling 已完成。

## 1. 固定的真实对象

固定同一条光滑闭几何、同一全路径起点 s_0、同一 profile 区间 I 和右零 collar。采用 R56 的 canonical 初值，保留原第二、第三累计 history。写

$$
z=x+\omega,\qquad e=h z-k,\qquad
\gamma=h_s,\qquad \nu=\omega_s=\frac{k_s}{2h},
$$

$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad
\lambda=\frac{\gamma z-h\nu}{h^2}.
\tag{1}
$$

移动框架满足

$$
T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,\qquad
\boldsymbol\alpha_s=h^2T.
\tag{2}
$$

分子及实际场的约定是 U=F V_U/z，F=(T,N,B)。初阶场为

$$
V_{Y_f}=\left(-\frac{f'}2,\,0,\,hf-\frac e2 f'\right).
\tag{3}
$$

取最细活动包的一端 x=x_e，邻接的开放平台满足 f=g=0。在该活动包中 g=\ell f，\ell 为实际常数；f 是 R281 已构造的非零解析 prefactor 乘指数平端函数。以下 x 导数以撇号标在 profile 上；几何量的 s 导数显写下标或在专门的几何公式内使用撇号。

R276 的精确局部分解为

$$
G_\theta=P_{e,\theta}+T_{e,\theta}f
+(f')^2 t^{-4}B_{e,\theta}(t).
\tag{4}
$$

P_{e,\theta} 是实际平台多项式，不是可以另选的常数。本文只识别中间的一次层，既不删除平台门，也不删除逆解的零端通量分支。

## 2. 真实三阶平台尾必有的齐次结构

先暂记任一 canonical 三阶恢复场在这个零平台上的实际延拓为 \Pi。因为第三 forcing 含一个初阶场，在零平台上的四个局部分子配对全部为零，但右积分尾一般不为零。R56 与 [R248](R248-complete-fourth-harmonics-and-complementary-block-reduction.md) 给

$$
P_\Pi=p(s),\qquad B_\Pi=0,\qquad
\eta_{0,\Pi}=-\frac12p_s,
$$

$$
\mathcal W_\Pi(s,x)=a(s)x^2+b(s)x+c(s),
\qquad
(\mathcal W_\Pi)_s=K_0p-\lambda p_s.
\tag{5}
$$

所有 a,b,c,p 都来自这同一实际场；(5) 不准将它们独立指定。二次次数来自全路径 canonical 初值与右锚恢复，不是对平台函数作截断。

令

$$
A_\Pi=\frac12(\mathcal W_\Pi)_x-\frac{p_s}{2h}.
$$

则原分子为

$$
V_\Pi=(A_\Pi,\ zp,\ eA_\Pi-h\mathcal W_\Pi).
\tag{6}
$$

在 z 坐标中写成

$$
(V_\Pi)_T=a z+t_0,\qquad
(V_\Pi)_N=pz,\qquad
(V_\Pi)_B=\eta z+q_0.
\tag{7}
$$

这里下标 0 只是区别 t_0,q_0 与 profile 坐标，不表示重新锚定。准确系数是

$$
t_0=\frac b2-\omega a-\frac{p_s}{2h},
\qquad
\eta=-h t_0-ka-p_s,
$$

$$
q_0=-k t_0-h(c-\omega b+\omega^2 a).
\tag{8}
$$

把 (5) 的 x 二次、一次与常数系数逐项比较，得到

$$
a_s=kp,\qquad
\eta_s-p=h\tau,\qquad
(q_0)_s-\frac{\gamma}{h}q_0=-k\tau,
\qquad
\tau=(t_0)_s-\frac{\gamma}{h}t_0.
\tag{9}
$$

这些是真实齐次平台方程。特别，\Pi 一般不是 ambient rigid 场；后面的计算不作这种假设。

## 3. 完整 cross 的一次层：所有局部原函数准确消掉

考察单位对称 forcing H(Y_f,\Pi)，其中 H(U,U)=(dU)^2。记其 R56 密度为 \mathcal R(Y_f,\Pi)。这里的“一次层”是对 x=x_e 的局部增量而言：真实右尾固定保留在平台多项式中，f 及其局部导数和积分按局部次数分层。

设

$$
C=a+e\eta,\qquad
U_T=a z+t_0,\qquad U_B=\eta z+q_0.
$$

原 x 配对是

$$
T_x=\frac{h\eta}{2}f'-\frac{C}{2}f''.
$$

由于 f 在 x_e 全平，从 x_e 积起的一次局部恢复准确为

$$
P^{[1]}=\frac{C}{4h}f'-\frac{\eta}{2}f,
\qquad
B^{[1]}=\frac{U_B}{2}f-\frac{U_T+eU_B}{4h}f'.
\tag{10}
$$

例如 (P^{[1]})_x=-T_x/(2h)，且 (10) 在零端为零。这一检验同时保留正右积分的符号；没有将全区间的真实 P 尾置零。

初阶分子的协变 s 导数为

$$
\nabla_sV_{Y_f}
=\left(0,\ h(f-zf'/2),\ \gamma f-e_s f'/2\right).
$$

真实平台分子的两个相关协变分量为

$$
(\nabla_sV_\Pi)_N=(zp)_s+kU_T+U_B,\qquad
(\nabla_sV_\Pi)_B=(U_B)_s-zp.
\tag{11}
$$

把 (10)—(11) 放入完整的原密度

$$
\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\lambda P_s+
\left(kz-\frac{k^2+1}{h}\right)B-\frac{\gamma}{h^2}B_s
\tag{12}
$$

并使用 (9)，准确得到

$$
\boxed{
\mathcal R(Y_f,\Pi)^{[1]}
=\mathscr B(s,x)f'-\mathscr B_x(s,x)f,
}
\tag{13}
$$

其中

$$
R(s,x)=\frac{1+e^2}{h^2},
\qquad
\boxed{
\mathscr B=
\frac14\left[
\left(t_0-kq_0-\frac{\gamma}{h}\tau\right)R
-\tau R_s
\right].
}
\tag{14}
$$

这不是只取最高阶的式子。T_s、P_s、B_s 中的实际 history 导数及 frame 项均已进入 (12)。

给出两个便于逐项复核的中间式。首先，K_0P+(K_0/z)B 中一次层合为

$$
\left(kz-\frac{k^2+1}{h}\right)
\left\{\frac{q_0}{2}f-
\frac{t_0+eq_0}{4h}f'\right\}.
$$

其次，(12) 最终 f 的系数为

$$
-\frac{(t_0-kq_0)e}{2h}+\frac{h\tau\lambda}{2}
=-\mathscr B_x.
\tag{15}
$$

因此没有留下 f'' 或局部 \int f 项。虽然原未化简表达可以包含这些形式，canonical 齐次平台关系把它们全部准确合并为 (13)。R(s,x) 对 x 二次，所以 \mathscr B 也只对 x 二次。

## 4. 三个历史矩和准确 s 端势

定义两个真实平台 director 系数

$$
v=\frac{t_0}{h},\qquad w=\frac{q_0}{h},
\qquad
\rho=v_{ss}+v-kw.
\tag{16}
$$

式 (9) 给 w_s=-kv_s、\tau=h v_s。于是 (14) 有更简洁的完整形式

$$
\boxed{
\mathscr B=\frac14\{h\rho R-\partial_s(hv_sR)\}.
}
\tag{17}
$$

所以

$$
\boxed{
\mathcal R(Y_f,\Pi)^{[1]}
=\frac14h\rho(Rf'-R_xf)
-\frac14\partial_s\{hv_s(Rf'-R_xf)\}.
}
\tag{18}
$$

(18) 是一个原式恒等，不是先忽略局部项后得到的近似。

在任一实际区间 [s_0,s_1] 上积分时，二次多项式必须取为

$$
\beta_\Pi(x)=
\frac14\int_{s_0}^{s_1}h\rho R\,ds
-\frac14[hv_sR]_{s_0}^{s_1}.
\tag{19}
$$

不能把 (19) 的端项在任意中间 germ 上另设为零。若 \Pi 确为同一闭几何上的真实周期第三场，则其平台值和所需 s 导数周期，(19) 端项准确相消。这时置

$$
\zeta=\omega-\frac{k}{h},
\qquad
R=(x+\zeta)^2+h^{-2},
$$

$$
J_{e,0}(\Pi)=\int h\rho\,ds,\qquad
J_{e,1}(\Pi)=\int h\zeta\rho\,ds,
$$

$$
J_{e,2}(\Pi)=\int (h\zeta^2+h^{-1})\rho\,ds.
\tag{20}
$$

定义实际二次多项式

$$
\mathcal P_e[\Pi](x)
=J_{e,0}(\Pi)x^2+2J_{e,1}(\Pi)x+J_{e,2}(\Pi).
\tag{21}
$$

则单位 cross 的全 period 一次层是

$$
\boxed{
\mathscr P\{H(Y_f,\Pi)\}^{[1]}
=\frac14\{\mathcal P_e[\Pi]f'
-(\mathcal P_e[\Pi])'f\}.
}
\tag{22}
$$

每个 J 是沿同一个完整 s 周期的积分，系数来自该 x 平台的真实三阶历史。不同平台的 J 可以不同；没有把它们认作一个共享的自由三向量。

### 4.1 为什么三标量就是准确零端门

对任一非零多项式 Q、任一非零指数平端 f，

$$
Qf'-Q'f=0
\tag{23}
$$

不可能在整个单侧零端 germ 成立。取足够小的单侧区间，使 Q 除可能在端点外没有零点，则 (f/Q)'=0。因为 Q 在端点至多有限阶零，而 f 全平，f/Q 的端点极限为零；(23) 迫 f 在该区间恒零，矛盾。

在 R281 的解析端芽中还能直接看出首指数：若 Q 在端点为 k 阶零，Qf'-Q'f 是非零解析 prefactor 乘 e^{-c/t} 和有限 t 幂；Qf' 的首项比 Q'f 高一个负 t 次数。它不能被 (f')^2 t^{-4}C^\infty 的二次余项抵消。

因此

$$
\boxed{
\mathscr P\{H(Y_f,\Pi)\}^{[1]}=0
\iff
J_{e,0}(\Pi)=J_{e,1}(\Pi)=J_{e,2}(\Pi)=0.
}
\tag{24}
$$

这比任意多项式微分加积分呈示的形式有限性更强：对当前 canonical 平台，只须这三个真实数，不需要分别检查所有原 word 系数。

## 5. 哪一部分已经由真实闭合支付

把平台场改写回物理 u=h/z 坐标：

$$
\Pi(s,u)=\mathbf a_3(s)+u\{v(s)T(s)+w(s)B(s)\},
$$

$$
\mathbf a_3=aT+pN+\eta B.
\tag{25}
$$

由 (9)，

$$
\mathbf a_{3,s}=h^2(-vN+v_sB).
$$

定义实际角速度向量

$$
\boldsymbol\Omega_3=wT-v_sN-vB.
$$

准确有

$$
\boxed{
(\boldsymbol\Omega_3)_s=-\rho N,\qquad
\mathbf a_{3,s}=\boldsymbol\Omega_3\times\boldsymbol\alpha_s.
}
\tag{26}
$$

于是 \rho=0 当且仅当该平台场在整个连通 s 区间上是一个固定 ambient rigid infinitesimal motion：

$$
\Pi=\mathbf c+\boldsymbol\Omega_3\times
(\boldsymbol\alpha+uN),
\qquad \mathbf c,\boldsymbol\Omega_3\text{ 为常向量}.
\tag{27}
$$

这是由齐次方程得出的等价关系，不是对一般 \Pi 的预设。所有真实 rigid 平台分量在闭周期的一次层中自动消失，因为它们使 (20) 的 integrand 为零。

若几何、frame、\Pi 全部闭合，则 (26) 进一步给已付的六条向量闭合矩

$$
\int\rho N\,ds=0,\qquad
\int\rho(N\times\boldsymbol\alpha)\,ds=0.
\tag{28}
$$

第二式来自
(\mathbf a_3-\boldsymbol\Omega_3\times\boldsymbol\alpha)_s
=\rho N\times\boldsymbol\alpha。若空间曲线尚未闭合，必须保留相应的实际端差；本文只在已经构造的闭 hook 上用 (28)。

(28) 的权函数与 (20) 的三个标量权函数不同。没有来源证明后者属于前者的线性张成，就不能由“第三场已闭”宣称 (20) 自动为零。本文也没有把满足 (28) 的任意 \rho 反向授予 canonical 第三场。

## 6. 使用的是哪一个 whole pure 零身份

本节明确增加一项几何假设，区别于只有 M=0、T=\kappa\mathfrak H 的情况：

$$
\boxed{
M_X=0,\qquad T_X=\kappa\mathfrak H,\quad\kappa\ne0,
\qquad \pi V_X=0
\text{ 对全部共同右 collar profiles 成立。}
}
\tag{29}
$$

所用对象是 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) §7.3 式(17) 的**实际**闭路径 X：完整控制 D 已经插入四个真实 prototype 副本，连同原 frame 桥、全成本和位移一起闭合，得到 \pi V_X=0。不是仅引用该文定理 B 的 S=P，或把某个响应像等号误当目标为零。

[R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md) §1 式(1) 已明确 (29) 的 universal 函数意义；同文 §2 式(5) 给原完整 canonical period 的精确相位式

$$
V^0_\theta=\sin^2\theta\,V_d+
2\cos\theta\sin\theta\,V_e.
\tag{30}
$$

若选择 [R227](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md) 所安装的新端芽，使用的是该文保留完整 \mathcal E(V) 的实际 IFT；[R241](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md) 的联合安装同样明确保留 universal pure 控制。本文仅对这样选定的几何应用 (29)。若未作这一步，§2—5 的通用三历史公式仍成立，以下自动消项不应使用。

特别，(29)—(30) 都是**整个 s 周期之后**的函数身份。本文不声称任意 s 的 canonical pure forcing、任意平台多项式或任意三次原尾为零。对独立新增的二阶 gauge 或任意 incoming 第三初值，也必须另写其完整 cross；本文不将它们藏在 (29) 中。

## 7. 当前两个 mixed 目标共用一个有序三次历史向量

沿用 R213 的准确规范。设

$$
Z_c=2Z(f,g),\qquad
\Pi_{fc}=W_{fc}=-4C(f;f,g),
$$

$$
Z(a,b)=\operatorname{Range}H(Y_a,Y_b),\qquad
C(a;b,c)=\operatorname{Range}H(Y_a,Z(b,c)).
\tag{31}
$$

W_{fc} 是原完整第三圆在种子处的相位导数的负值，不是额外选择的第三 gauge。由完整圆的周期和 collar 合法性，它本身也是周期、双 collar 的实际第三场。R213(4) 给

$$
V_e=\mathscr P\{H(Y_f,W_{fc})\}.
\tag{32}
$$

取其在当前零平台上的实际尾，按 (16)—(21) 定义

$$
\boxed{Q_e(x)=\mathcal P_e[W_{fc}](x).}
\tag{33}
$$

因此准确有

$$
V_e^{[1]}=\frac14(Q_e f'-Q_e'f).
\tag{34}
$$

要确定 V_d 的一次层，不需要重新展开第四平方项。选择一个满足
\cos\theta_*+\ell\sin\theta_*=0
的相位，且 \sin\theta_*\ne0。在本活动包上，第一 profile
\phi_{\theta_*}=(\cos\theta_*+\ell\sin\theta_*)f
恒零。

原第四 forcing 为

$$
-H(Z_\theta,Z_\theta)-2H(Y_{\phi_\theta},W_\theta).
\tag{35}
$$

在这个相位，第二项的局部一次层为零。第二场是实际平台二次尾加局部二次项，所以其平方也不产生一次层；不能把其平台或二次层一并删掉。由 (30) 及 R276 一次指数与二次余项的分离，得到

$$
V_d^{[1]}=2\ell V_e^{[1]}.
$$

从而整圆的准确一次层为

$$
\boxed{
(V^0_\theta)^{[1]}
=\frac12\sin\theta(\cos\theta+\ell\sin\theta)
(Q_e f'-Q_e'f).
}
\tag{36}
$$

式 (36) 只用了真实全 period 的 pure 身份，没有使用逐 ruling 的 pure 零性。

R213(7) 中的两个二阶 gauge 目标是

$$
G_c=-\frac{V_d}{4\kappa},\qquad
G_s=-\frac{V_e}{2\kappa}.
$$

因此它们的一次端层准确满足

$$
\boxed{
G_c^{[1]}=-\frac{\ell}{8\kappa}(Q_ef'-Q_e'f),
\qquad
G_s^{[1]}=-\frac1{8\kappa}(Q_ef'-Q_e'f).
}
\tag{37}
$$

特别，g=0 的活动包上，G_c 的一次层自动为零，但 G_s 一次层仍保留同一个 Q_e。一般比例包上两者只差真实比例 \ell。

由 (24)，在已付平台和端通量分支下，R281 的两个零端光滑逆解门共同等价于

$$
\boxed{
J_{e,0}(W_{fc})=J_{e,1}(W_{fc})=J_{e,2}(W_{fc})=0.
}
\tag{38}
$$

\kappa\ne0 已由原 hook 安装保证。式 (38) 不授内部退化匹配、其他平台条件或同一个 w 的 ruling 方程。

### 7.1 完全对称三次历史究竟在哪里被消去

也可直接看出已支付的是哪部分历史。将 R248(6) 的同一完整 forcing用于 period，而不是 ruling，得到 universal pure 四次根

$$
\mathcal V_{\rm p}(q)=
-\mathscr P\{H(Z(q,q),Z(q,q))\}
-4\mathscr P\{H(Y_q,C(q;q,q))\}.
\tag{39}
$$

它与 \pi V_X 只差固定非零的相位规范因子，故 (29) 使 (39) 对所有共同右锚 q 为零。这里是整个 period 身份；(39) 的 integrand 不必为零。

M=0 使 Z(q,q) 的同端几何值按原规则周期相接，而
T=\kappa\mathfrak H、\mathfrak H(q;q,q)=0
使 C(q;q,q) 的 characteristic period 为零。因此这些用于 (39) 的形式分解场在 s 上周期；即使单独一项尚有左尾，也不妨碍使用 (19) 的周期端势消去。

对 q=af+bg，只要 a+b\ell\ne0，其在当前活动包上是非零解析平端。式 (39) 的平方项没有局部一次层；余下一次层是

$$
-\{\mathcal P_e[C(q;q,q)]q'
-(\mathcal P_e[C(q;q,q)])'q\}.
$$

由指数分离与 (24)，它迫

$$
\mathcal P_e[C(q;q,q)]=0.
\tag{40}
$$

左边是 (a,b) 的三次多项式，已在一个非空开集上为零，所以对全部 (a,b) 为零。极化给

$$
\mathcal P_e[C(g;f,f)+2C(f;f,g)]=0
\tag{41}
$$

及其余完全对称三槽关系。合法第三圆还给
\mathfrak H(g;f,f)=0：
这是把
\mathfrak H(\phi_\theta;f^2-\phi_\theta^2)=0
和对角恒零代入后所得的弱条件，不必假定所有 hook 槽都各自为零。因此 C(g;f,f) 的 s period 同样已付。

综合 (31)、(41)，

$$
\boxed{
Q_e=-4\mathcal P_e[C(f;f,g)]
=2\mathcal P_e[C(g;f,f)].
}
\tag{42}
$$

式 (42) 展示了一个真正剩余的**有序跨槽**。完全对称部分已被实际全 pure 身份支付；有序项没有因此变为零。

等价地，原整圆第三场
W_\theta=-2\{C(\phi_\theta;f,f)-C(\phi_\theta;\phi_\theta,\phi_\theta)\}
的三历史多项式满足

$$
\mathcal P_e[W_\theta]=-\sin\theta\,Q_e.
\tag{43}
$$

这也可由 (36) 与一般的 -2 cross 公式直接推出。式 (43) 不是 W_\theta 的点态身份；其真实 cubic 尾和 quadratic history 仍然存在。

## 8. Q_e 的原来源：线性 second history 与完整 quadratic third history

给出一个不需要重新编 forcing 的准确来源接口。固定八矩基 \Phi_i，采用 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(12)、(16)—(17) 的同一全路径 history：

$$
M(s)=\sum_i M_i(s)E_i,\qquad
m_i(s)=\int_{s_0}^s M_i(t)\,dt.
\tag{44}
$$

对单位 C(a;b,c)，先保留原恢复

$$
Z(b,c)=K_s(b,c)-Y_{\Phi_m(b,c)}.
$$

其平台 P 尾是原真积分

$$
p_C(s)=\frac1{2h}
\int_{x_e}^r V_{Y_a,x}\cdot V_{Z(b,c),x}\,dx
=p_C^{\rm loc}(s)-\sum_i m_i(s)p_{C,i}(s),
\tag{45}
$$

$$
p_{C,i}(s)=\frac1{2h}
\int_{x_e}^r V_{Y_a,x}\cdot
V_{Y_{\Phi_i(b,c)},x}\,dx.
$$

K_s 中所有原局部恢复、右原函数和真实几何导数都保留。式 (45) 仅按已存在的 m_i 作准确线性分离，不重锚，也不把积分右方的 profile 合并成独立变量。

再令

$$
I_{ij}(s)=\int_{s_0}^s M_i(t)m_j(t)\,dt,\qquad
A_{ij}=I_{ij}-I_{ji}.
$$

在当前零平台上记
Q_{ij,e}(x)
为 \Phi_i(a,\Phi_j(b,c))(x) 的真实二次多项式尾。令
L_{C,e}(s,x)
为 R73 的完整局部三次密度 \mathcal C_s 的实际 s 积分尾，包括原 \Psi 链式项。则 canonical characteristic 准确为

$$
\boxed{
\mathcal W_{C,e}
=L_{C,e}-\sum_{i,j}I_{ij}Q_{ij,e}.
}
\tag{46}
$$

这里 L_{C,e} 的原初值是同一 s_0 的 canonical 值；在某个中间几何 germ 再使用 (46) 时，必须保留已经累计的段首值。

因为 m(s_0)=0，

$$
\boxed{
\mathcal W_{C,e}
=L_{C,e}
-\frac12\sum_{i,j}m_im_jQ_{ij,e}
-\frac12\sum_{i<j}A_{ij}(Q_{ij,e}-Q_{ji,e}).
}
\tag{47}
$$

这就是实际三阶平台尾的零/一层局部来源、对称 quadratic history 和反对称面积来源。它没有把这些生成元假定为独立；在例外 germ 上可再用 [R245](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md) 的四 Gaussian 呈示，但不删负指数 history 或真实中心常数。

对当前有序源，取 a=f、(b,c)=(f,g)，将 (45)—(47) 整体乘 -4，得到实际 W_{fc} 的 p 与 \mathcal W。接着只按 (8)、(16)、(20) 作线性操作，就得到 (38) 中的三个数。因而：

- 一次端层对真实第三平台数据是线性的；
- p 已保全部一次 second history；
- \mathcal W 已保完整 m_im_j 与 A_{ij}；
- 没有 W_{fc} 的平方或任意独立第三初值进入这一层。

最后沿全 s 周期的积分仍须实际保留。本文不把这一额外全周期积分冒称为 R245 的逐 ruling 二十一生成元已经完成评价。

## 9. 已自动支付的平台、同平台两端与尚欠的内容

若相邻零平台位于一个 R245 完整第三 block 的外包络之外，则 W_\theta 及其相位导数 W_{fc} 在该平台准确为零。因此 (38) 自动成立。这里使用的是完整八复制组已经支付的第三 ruling、原 canonical 初值及全部恢复局域性，不是把单个微包当成完整 block。

若两个相邻微包之间共用同一开放零平台，(5)—(8) 是这个整个平台上的同一真实多项式。它们两侧零端的 Q_e 因而相同。可以按内部零平台而非重复按两个端点登记 (38)；两个活动包的比例 \ell 可以不同，(37) 会如实改变相应目标系数。

一般内部平台上 W_{fc} 可以不为零，也可以含非 rigid 的实际 director 变化。全部已付 Gaussian 面积是特定四次 profile 外矩，六条能量也有各自准确的原槽。没有进一步身份时，它们不能替代 (45)—(47) 的三次右尾与 (20) 的几何加权矩。本文没有证明某个当前内部 Q_e 非零，也没有把原 F 纤维的观察表自动扩大为保持 Q_e 的表。

本稿完成的新增结论是：

1. 从完整 R56 得到真实平台的一次层 transgression (18)，保留准确端势；
2. 将当前 canonical 端门压到实际三阶非 rigid director 的三个明确矩 (20)；
3. 用已安装几何的 whole-period pure 身份，准确消掉完全对称三次历史，并将两个 mixed 目标统一为同一个 Q_e；
4. 给出 Q_e 的原一次/二次 history 来源 (45)—(47)，以及完整 block 外端的自动零性。

实际平台门 P_e''=0、未付的内部 Q_e、所有内部退化与总通量、完整对称二 history ruling、零/一层 ruling 以及同一二阶 gauge 的 joint 方程仍按各自原条件保留。特别，本稿不会把 R280 或 R284 的已付面积/能量，误报为原 fourth period 或完整构造已经成立。

