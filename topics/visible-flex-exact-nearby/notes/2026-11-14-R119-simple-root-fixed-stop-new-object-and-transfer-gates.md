# R119 工作札记：一个真正简单根的外接线新对象及其已付转移门

2026-11-14，visible-exact / tail_connector。

**这是新的候选几何对象。** 本文保留此前三阶根对象及其 X/T/R 全部证明，不把新对象记成旧对象的另一个坐标。下文先准确构造新末段，并证明几何、固定 stop、第四误差、完整标签续接及原 regular 入口的转移。新的第二个 simple 根的实际 Airy 图、扩充后的联合两相位行、完整闭返回逆与最终强标签逆仍须接着证明；它们不由本札记最后的清单自动取得。

改动只发生在 $u=T=2^{24}$ 之后的有限 connector 的最后一组。原有限主体 $0\le r\le R=25/8$、自然 graft、全部原 intrinsic 参数、$a_*,z_*,\omega_*$、两个外 bump、$B=T-25/8$ 和 $L=\omega_*B$ 都按原定义保留。主放大段仍止于同一个 $\Omega=2^{360}$。新的末段在放大段结束后使用一次 $q=2\to-8$ 过渡，再使用一段 $q=-8$ 常平台；它替换原 $2\to-1$ 过渡、$-1$ 平台及 $-1\to-8$ 过渡。

## 1. 同一真实变量及新末段的唯一停止点

沿用 [R69](../results/R69-actual-closed-approximate-exterior-and-two-held-disks.md) (69.9)--(69.22) 的物理归一：
$$
 z_u=a^2/4,\qquad h=a^{-1},\qquad
 v=\log(h/h_T),\qquad
 (\log\omega)_v=q,\qquad
 \mathcal R_v=q(1-\mathcal R)+1-16\mathcal R^2 .
 \tag{S.1}
$$
这里 $\mathcal R=y'/(16\omega y)$ 是第四 Sturm 投影，不是径向位置 $R=25/8$。令
$$
 \eta=2^{-24},\qquad S(x)=10x^3-15x^4+6x^5 .
$$
原准备段及 $q=2$ 放大段不动。放大段末端的状态准确为
$$
 q=2,\quad \omega=\Omega,\quad \mathcal R=-1/2,\quad
 H_A=h_a\sqrt{\Omega/\omega_a}.
 \tag{S.2}
$$
在下一个长度 $\eta$ 的真实时间区间，定义
$$
 q(v)=2-10S(v/\eta),\qquad 0\le v\le\eta .
 \tag{S.3}
$$
两端的一、二阶 $q$ jets 为零。此段仍有 $-8\le q\le2$。原 R11 的 $|\mathcal R_v|\le4233$ 及 $4233\eta<1/3000$ 给
$$
 -1/2-1/3000<\mathcal R_b<-1/2 .
 \tag{S.4}
$$
严格右不等式也可直接看见：在 $\mathcal R=-1/2$ 上，
$\mathcal R_v=\tfrac32(q-2)\le0$，且过渡内部严格为负。令
$P_b=-\mathcal R_b$，则 $1/2<P_b<1/2+1/3000$。

先选定原实际参数族的一个径向基点 $\Pi^0$。其真实无限尾第四物理斜率为 $d_4^0\in(14,15)$；这是全强尾图的真实输出，不用理想单胞代替。置
$$
 P_*^0=\frac{d_4^0-1}{16-d_4^0}\in(13/2,14).
$$
在 (S.3) 之后令 $q=-8$。准确 ODE 为
$$
 P_v=16P^2+8P+7=16(P+1/4)^2+6,\qquad P=-\mathcal R .
 \tag{S.5}
$$
因此唯一停止长度为
$$
 \ell^0=\int_{P_b}^{P_*^0}\frac{dP}{16P^2+8P+7},
 \qquad 0<\ell^0<\frac1{12}.
 \tag{S.6}
$$
上界来自把积分上限改为无穷、略去分母中的 $6$，再用 $P_b>1/2$：
$\int_{1/2}^\infty [16(P+1/4)^2]^{-1}\,dP=1/12$。
在停止前 $P$ 有限，故 $y$ 的标量指数方程给 $y>0$。末端准确有
$q=-8$、$\mathcal R=(1-d_4^0)/(16-d_4^0)$；从该点接常平台 cut128，完整二阶背景 jet 相符。

**此后固定 $\ell^0$，不随 $\Pi$ 或未知标签改变。** 特别
$D_\Pi\ell^0=0$，不会引入一个未计入的移动 stop 源或变化的尾幅度。

若只为辨识另一个重停对象而形式地令终点等于 $d\in(14,15)$，其唯一长度满足准确导数
$$
 \frac{d\ell}{dd}
 =\frac{1}{d^2-8d+112}
 =\frac1{(d-4)^2+96}<\frac1{196}.
 \tag{S.7}
$$
但该重停对象的 $H_e\omega_e$ 会乘 $e^{-7\ell}$，其
$\epsilon_{\rm tail}$ 会乘 $e^{7\ell}$。原 $q=-1$ 重停中
“$\epsilon_{\rm tail}$ 不变”的恒等式在这里不成立，不能沿用。
本文使用的是固定 stop，故没有这项循环。

## 2. 新根确为简单根，且位于真正过渡内部

用向外物理时间 $t=\log a$，有 $A=aw_a/w=q+1$，故负型量
$Q=-A=-q-1$。新 (S.3) 上唯一零点由
$$
 S(x_0)=3/10,\qquad 3/8<x_0<2/5
 \tag{S.8}
$$
给出。两端值比较是准确有理比较，$S'>0$ 在 $(0,1)$ 上保证唯一。
在该小区间
$$
 \frac{243}{160}<S'(x)<\frac{15}{8},
$$
于是新根的真实斜率 $b_0=|Q_t|$ 满足
$$
 \frac{243}{16\eta}<b_0<\frac{75}{4\eta},
 \qquad 2^{27}<b_0<2^{29}.
 \tag{S.9}
$$
它与过渡两端均有正距离，所有控制 bump 都在第129胞元的下降坡内，与此根分离。$Q$ 在两侧变号，而不是只在一侧接零平台。

标准 quintic 的全段导数同时给
$$
 |Q_t|<2^{29},\quad |Q_{tt}|<2^{54},\quad
 |Q_{ttt}|<2^{82},\quad |Q_{tttt}|<2^{108}.
 \tag{S.10}
$$
这些是新根的实际输入；它们本身尚不是原 canonical Airy 图或强 $4/3$ 余项的复用证明。

新负分量从原 $e_X$ 走过第129胞元第二下降坡、cut128、$q=-8$ 平台，终于 (S.8) 的新根。它有两个真实 simple 根。原 $(129,2)$ 被排除的几何理由因而消除，但其加入旧完整网络仍须支付下文第9节列出的算子门。

## 3. 全部有限几何盒重新验证

新末端组总长 $\eta+\ell^0<1/8$。准备段总长仍小于
$1/3+2\eta$，所以其余短段总长满足
$$
 L_s<5/12+3\eta<1/2.
 \tag{S.11}
$$
主放大段的 $L_a<505/4$、双 bump 的 $L_b<75/16$ 及完整 connector 总长 $<127$ 都保持。

在新末端组，每个前缀满足
$$
 \Omega e^{-8(\eta+\ell^0)}<\omega<\Omega e^{2\eta}.
$$
因为 $8\eta+2/3<69/100<\log2$，最后得到
$$
 \frac12\Omega<\omega_e<\frac54\Omega,\qquad
 H_A\le H_e<\frac65H_A .
 \tag{S.12}
$$
这里只改变了旧末端下界 $4\Omega/5$；不能继续写那个旧值。
原准备段仍有 $\omega>9/10$，放大段只增大 $\omega$，新末段的下界远大于 $9/10$。从而整个有限段仍有
$$
 w/a=\frac1{4\omega}<5/18,\qquad w<1,\qquad
 a<7\cdot10^{-6},\qquad -7\le A\le3 .
 \tag{S.13}
$$

沿用原 $h_T\le h_a<3h_T/2$、$2/3<\omega_a<3$，由 (S.12) 重新得到
$$
 H_e\omega_e>\frac14h_T\Omega^{3/2},\qquad
 H_e^2\omega_e^2<8\Omega^3h_T^2 .
 \tag{S.14}
$$
第二式的准确系数上界为
$(6/5)^2(3/2)^2(5/4)^2(3/2)=243/32<8$。
因此后续 raw 两迹消去所需的 $H_e^2\omega_e^2$ 宽门没有改变。

参考曲率仍由 R69 (69.18) 的准确式计算。在准备段及放大段用原 $|1+q|\le3$、$\omega>9/10$；在新末端组用
$|1+q|\le7$、$\omega>\Omega/2$。完整 connector 的两主曲率依然小于 $5/6$。其高度费仍为
$$
 \Delta z_{\rm con}<\frac5{36}a_T^2 .
 \tag{S.15}
$$
这来自全程 $\omega>9/10$ 与 $a=a_Te^{-v}$，不依赖短段的旧排列。

## 4. 新物理安装及整条无限尾的二阶界

以下 $\rho,\lambda,\epsilon$ 是**新固定对象自己的数**：
$$
 \rho=\frac1{H_eb},\qquad
 \lambda=\frac1{4H_e^2b\omega_e\bar W_b},\qquad
 \epsilon=\frac1{4H_e\omega_e\bar W_b},
 \quad \bar W_b=\delta_{128}^6/b^7 .
 \tag{S.16}
$$
仍有 $1<b<2$、$\bar W_b>2^{-799}$。由 (S.14)，
$$
 0<\epsilon<2^{259}a_T<1,\qquad
 \frac\epsilon\rho=\frac b{4\omega_e\bar W_b}<2^{440}.
 \tag{S.17}
$$
先用这个新 $\epsilon$ 调用已对全部 $0<\epsilon\le1$ 一致的强尾图，然后整体等比缩放 $\rho$；不对旧非线性解作各向异性拉伸。
因 $\ell^0$ 固定，这两个尺度均与当前 profile 参数、标签无关。

对浅层完整双 bump/形状盒，原单调端值及
$|(\log p)_x|<(15/8)\Delta$、$|(\log p)_{xx}|<6\Delta$
保持。R69 (69.24)--(69.26) 的同一计算只需把
$\omega_e>4\Omega/5$ 换成 (S.12)，因而
$$
 \max_{129\le j\le4096}\{|w/a|,|w_a|\}
 <\frac85\,\frac{9375}{131072}
 =\frac{1875}{16384}<\frac18 .
 \tag{S.18}
$$
这不是将旧的 $9375/131072$ 原值直接授予新对象。
4097 以后只消费 (S.17) 的原 $2^{440}$ 宽门；因此
[当前完整外曲率](../results/R133-supplement-current-complete-exterior-curvature-and-common-world-caps.md)
(E.7)--(E.14) 的全层二 jet 账逐项保持：
$$
 \max_{\rm reference\ tail}\{|w/a|,|w_a|\}<1/8,\qquad
 \|F_\Pi-F_{\Pi,0}-\lambda_{\rm phys}e_z\|_{C^2}<2^{-64}X .
 \tag{S.19}
$$
所有源的物理换算都必须使用 (S.16) 的新数，不能混用旧 $\rho$。

于是参考无限尾高度费仍小于 $a_T^2/16$，真尾曲率仍小于 $1/4$。
完整非径向 finite connector/long 段的
$\|\mathsf S\|<2$、同世界外部距离 $<8\cdot10^{-6}$、
法向差 $<16\cdot10^{-6}$ 的证明只使用
(S.13)、(S.19) 及下节重付的小球，故保持。正支持覆盖、两真实平盘、径向物理长度和原 held 尺寸充分门亦保持；平帽高度依然是唯一 mean 积分的输出，不能为新旧对象分别归零。

## 5. 固定 stop 后所有实际参数的第四残差与导数

允许原双参数盒和全部已安装深控制；浅层形状盒也按已证明的 $C^4$ 半径使用。第129胞元第二下降坡原来没有装五盒，若现在为它安装同一个 $2^{-80}$ 实形状球，局部图证明并不改变：
浅篇 (P.5)--(P.8) 从头就以每胞**两个**下降坡计总变差及材料面积；第129胞原先只用其中一个。其第二个支集加入后仍在这个已核上界内，且与两个旧 bump 相离。两个根 germ 与所有平台、接缝 jets 均不变。

因此完整 cut128 真第四线重新满足
$$
 14<d_{4,\Pi}<15,\qquad
 |d_{4,\Pi}-d_4^{\rm ideal}|<2^{-38},\qquad
 |d_{4,\Pi}-d_4^0|<2^{-37}<2^{-35}.
 \tag{S.20}
$$
原两条 $\Gamma$ 导数仍分别为 $2^{-22}$ 与 $2^{-8}$。
这是同一新固定尺度下的尾高度方程：$w_a/w$ 中 $\epsilon$ 消去；局部低窗、两次接缝、mean 小根及无限强解的唯一性均保留。
浅形状的 Cauchy 参数费仍是 $2^{80}\|\dot\Xi\|_{\ell^\infty(C^4)}$，不以深层半径代替。

将新线从 cut128 通过**固定**新 connector 反传。两条第四轨迹满足
$$
 (\Delta\mathcal R)_v=[-q-16(\mathcal R+\mathcal R^0)]\Delta\mathcal R .
 \tag{S.21}
$$
基准轨迹仍在 $[-14,-1/6]$；共同管
$-15<\mathcal R<-1/8$ 内，因 $q\le2$，方括号至少为2。
输入 $\varepsilon_d=|d_{4,\Pi}-d_4^0|<2^{-35}$ 与
$|\Delta\mathcal R_e|\le15\varepsilon_d$ 保证反向 bootstrap 不碰管壁。
故原 fixed-stop 证明 (F.5)--(F.12) 在新全程重新给
$$
 \frac{|\lambda_4(T)+4\omega_*|}{4\omega_*}\le60\varepsilon_d,\qquad
 p_B=-\lambda_4(B)/4\in[5/4,8/5],\qquad
 |p_B-\omega_*|\le60\omega_*\varepsilon_d .
 \tag{S.22}
$$
对于一个固定外 bump 参数及任一真实参数方向，
$$
 |D p_B|\le60\omega_*|D d_4| .
 \tag{S.23}
$$
这由同一线性化 ODE 和正区反向 Riccati 收缩得到，不对 good-$t$ 选择函数求导。

原外双 bump 曲线使**基点新 connector**的第四线保持在原稳定目标；
基点在 $u=T$ 的第四线准确就是原 $(1,-\omega_*)$，故该基点曲线仍是原同一个函数。对一般 $\Pi$ 不重新宣称第四线准确不变。
原高模坏角证明只需新的非零右线、同一正区系数盒和 (S.22)，所以可以在控制参数与 $t$ 的乘积盒上重新选择一次，条件好集测度仍至少 $1-83/16384$。

## 6. $a_*,R$ 端的 regular 图及完整强标签入口

对于上节新公共 good 参数，未改的长段给新对象自己的真实 regular 线：
$$
 \frac{|\lambda_4+4\omega_*|}{4\omega_*}
       <240\varepsilon_d e^{-8L},\qquad
 |\lambda_m+m\omega_*|<2^{41}m\omega_*e^{-2mL}
 \quad(m\in4\mathbb N),
$$
$$
 |q_m-q_*|<2^{-512},\qquad
 q_*=(1+w_R^2)^{-1/2}.
 \tag{S.24}
$$
包括第四行，不把它设成0。$R,a_*,w_R,\omega_*,L$ 的定义和数值均未改变。

这准确说明可以复用哪些有限证书：在固定 $0\le r\le25/8$ 上的 intrinsic、candidate、repair、response、残差、finite Green、根图与几何数据，其科学输入逐字未改。依赖 exterior 的定理若已对整个 (S.24) 原盒、全部 low/head/mean/source 列证明，则其同一 uniform 不等式也适用于新线；若某项只对旧的一条外线或旧特定 Poisson 图证明，不能凭这句话转授。完整实际 native/receipt 的输入身份仍由最终消费者校验，不以“新数很小”替代。

完整 balanced 四态证明的全部实际输入是
$L_a<505/4,L_s<1/2,L_b<75/16$、平台 $A=3$、
短段 $A\in[-7,3]$、双 bump $A\in[7/8,9/8]$，
以及 (S.13)。它们已经重付；cut128 的相对四态缩放消去新 $\epsilon,\rho$，同一个初始因子 $2^{-467}X_\beta$ 保持。
因此总角费仍可取 $14825/64$，有限增长仍小于 $2^{20}$，从而
$$
 \sup N_b<2^{-447}X_\beta,\qquad
 \|T_BX\|_{\mathfrak C_{s_\beta}}<2^{-447}\|X\|_{\mathcal X_\beta},
 \quad s_\beta=\beta-\frac{88823}{400},\quad\beta\ge224 .
 \tag{S.25}
$$
完整 raw/grounded 的原角宽余量 $2683/800>3$、所有 mean 与二 jet 重建保持。没有只转授非mean两行。

同样，[fixed-stop D0](../results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.6)--(D.29) 的具体输入逐项是：新 good-angle、真实第四正斜率、
$H_e^2\omega_e^2<8\Omega^3h_T^2$、完整 connector 的
$-8\le q\le2$ 和长度 $<127$、真实 raw404 以及 (S.25)。
R74 §5 的 $e^{1143M}$ 只使用该 $q$ 盒和长度，没有使用旧末段排列。
所以新的径向算子仍满足原完整结果
$$
 \|\mathsf D_0^{-1}g\|_\beta
 \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}},\qquad
 \|\Pi\|_{\mathfrak C_\sigma\to\mathfrak C_\sigma}<2^{44}.
 \tag{S.26}
$$
这里保留1850宽差。新对象的同宽混频逆仍未由它证明。

## 7. 真正 mean、holonomy 与 ordinary/weak 源

所有段始终使用 total 通量
$\pi=\mu(h_t-dh_\theta)+F^t$。在径向尾上
$$
 \pi_0(t)=\int_{t_f}^t f_0(s)\,ds,\qquad
 H_0(t)=\lambda+\int_{t_f}^t\frac r w(\pi_0-F^t_0)\,dt .
 \tag{S.27}
$$
新 fixed-stop 有限段继续同一通量；长段 mean 跨度仍含
$4\omega_*L\,\pi_0$，不作非zero模的指数筛选。
全 nonlinear 四态方程及其 $M_t=0$ 恒等式未改，故沿新段仍使用同一个 holonomy-one 小根。唯一平盘高度 $\lambda$、真实 bare/total 端荷及原角规范均保留。

新 $\rho$ 下的物理 source 比例明确仍是
$$
 F^{\rm ref}=\rho F^{\rm phys},\qquad
 N^{\rm ref}=\rho^3N^{\rm phys},
$$
而 fixed-stop (D.19) 的准确 canonical 两行源为
$$
 \mathcal J_m=
 \binom{-\nu_mr^4F^t/(\sqrt{12}\mu_jp_*)}
 {r^4(f-imF^\theta+m^2F^t)/(12\mu_j)} .
 \tag{S.28}
$$
ordinary 是 $f=w^2e$。原完整 $\mathcal S^w_{1,\beta}$、
$2^{482}$ block-source 转换、$2^{95}$ projected source boundary 费及
$2^{92}$ regular affine Wronskian 费由同一 (S.25)--(S.26) 取得。
有限 connector 中另给 source 时，仍逐段保真实 variation-of-constants 积分及其新实际 $\omega(v)$；这里没有将该 source 冒作零。

因 stop 与尺度固定，尾 metric 参数列在固定物理半径中仍是
$$
 \delta w=w\left(\sum_i\psi_{1,i}\delta\gamma_{1,i}
                  +\sum_i\psi_{2,i}\delta\gamma_{2,i}
                  +\delta\Xi\right),\qquad
 \delta g_{aa}=2w\,\delta w .
 \tag{S.29}
$$
其 mean 高度列是同一真实积分。没有旧重停中的
$A\,\delta\ell$ 项；这来自 $D\ell^0=0$，不是删掉一个非零源。
最后选择一个参数后整个相位轨道必须使用同一个新目标度量。

## 8. 两个 $\Gamma$ 补偿已经保留和仍须扩充的部分

第129胞元第二下降坡的两原 bump 本来就属于
[双参数全图](../results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
(U.1) 的实际盒；先前仅是在内部 KAM 枚举中把这对坐标固定。
它们的两个不交支集、完整局部 $\Theta/\beta$ 变分密度和非零 Jacobian 不因 (S.3) 改变。新根、全部新 finite connector 和正片在这两个径向参数方向上固定，所以完整径向相位相对于局部 bump 的导数，仍只有原下降坡的那两项。新根 connection 与新增常平台给基点相位加自己的真实常数；不能把该常数设成旧值。

内部所有旧分量的联合补偿、全标签图与 source 列在 fixed-stop 新尺度上仍按原相对变量证明成立。新的 $(129,2)$ 行有额外 finite bridge 和 simple 根，因此它的实际非径向误差与参数导数必须加入同一个联合方程。只保留原局部 Jacobian 并不自动证明扩充后的全图收缩，也不自动固定它的完整 $1/M$ 相位。

特别，本文不使用已经出版的旧 X/T/R 的跨三阶根常数作为新末段的证明。旧三阶对象的全部数学成果仍有效；这里只为判断新构造是否更快关闭最终返回缺口，列出明确的新对象入口。

## 9. 接下来必须实际完成的三个门

1. **新根与新 positive 外片。** 以 (S.8)--(S.10) 的真根、真实物理 $\mu$ 和完整 mean 构造 canonical 两行/root graph；证明新根至原 $B$ 的完整 positive DN/Poisson、全部端荷和强 $4/3$ normal form。虽有已重付的 balanced 小球，也不能直接把只对旧胞元正片的参数范围当作此片的权限。

2. **扩充后的联合两相位和五盒网络。** 将 $(129,2)$ 的两个 $\Gamma$ 行、当前 $\Gamma^*$ 两列及新根相位加入同一个联合构造；对最后一个真实负窗重付两端 Green 比较、mixed pocket 型、high/low 阈值及源列，再对完整闭网络作谱选择。增加一个有限窗口不会改变原无限低尾的数学对象，但谱计数和其实际权必须明确记录。

3. **闭逆回原强标签。** 最后物理返回须使用新 positive 端图及真实 mean/holonomy 条件；不能从开放内部 inverse、unitarity 或紧性直接得 $(I-E_aT_a)^{-1}$。得到全频闭逆之后，还须用真实 $b_m,\zeta_j$、(S.16) 的尺度、ordinary/weak 两向源及 $\Gamma^*$ 全列恢复原 $\ell^1_{224}$ 标签合同，并完成 nonlinear 匹配。

这些是新候选尚未完成的门。本文已经支付的是新对象的明确存在、几何盒、固定 stop/第四误差及其导数、有限完整标签续接、真实 regular 原盒和所有源/mean 的身份；不是最终课题完成声明。
