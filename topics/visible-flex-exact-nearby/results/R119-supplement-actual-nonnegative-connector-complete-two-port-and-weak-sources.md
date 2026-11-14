# R119 续篇：实际非负 connector 的全频两端逆、零曲率平台端口与完整 weak 源

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 对已经固定停止长度、尺度和双 bump 的真实对象，
本篇处理最后一个 $q=-1$ 主平台的内端 $C$ 到原 $u=B$ 的整个有限
connector。它包含两个零曲率主平台、整个长 $q=2$ 放大段和两个
实际 bump。它不包含 $C$ 内侧最后的 $q=-1\to-8$ 过渡。

在同一个实际非径向背景上，这整个区间有一个完整的两端变分逆。
内端高度只需 $L^2$；内端总通量也落在 $L^2$，全部 Fourier 模和
mean 都包括。其内端 DN 块满足
$$
             2^{-373}I<\mathcal N_{CC}<2^8 I.            \tag{E.1}
$$
这给出真正的内端 Neumann/外端 Dirichlet 逆，而不使用
$e^{1143|m|}$ 的有限 connector Cauchy 上界。
正文同时给普通源、径向 $L^1$ weak 源和有限 affine 跳的完整合同。

这里没有将 $C$ 认作 cut128 或开放网络端口 $e_X$。
$e_X\to\mathrm{cut128}\to C$ 的真实负段、其三阶退化转向，
以及这些新端口到原根波、强标签和最终 returned 方程的变换仍须支付。

## 1. 实际区间及没有改动的几何

使用以下同一对象的已证输入：

* [固定停止的实际 connector](R133-supplement-fixed-stop-connector-and-complete-regular-ports.md)
  (F.1)--(F.4)，以及
  [完整固定停止 D0/source 定理](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
  (D.1)--(D.3)、(D.16)、(D.18)--(D.23)；
* [R11](R11-matched-mode-four-physical-tail-connector.md) §§4--5 的实际
  quintic、两个 $q=-1$ 停止段与 $q=2$ 放大段；
* [平衡 connector 全标签域](R119-supplement-balanced-connector-label-domain-224.md)
  (W.1)、(W.11)--(W.16)，包括 mean 和所有非线性高输出；
* [准确物理 Hamiltonian/source 恒等式](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
  (J.2)--(J.5)、(J.17) 与 (J.24)。

令 $C$ 是沿原 $u$ 增大方向，最后一个 $q=-1$ 主平台的终点，
亦即最后那个 $q=-1\to-8$ quintic 的起点。保持实际物理半径 $r$，
置
$$
 t=\log(r/r_C),\qquad 0\le t\le\ell=\log(r_B/r_C).
                                                               \tag{E.2}
$$
这是向外、从 $C$ 到 $B$ 的方向，与 R11 的 $\log h$ 方向相反。
从 $C$ 开始先经过最后的整个 $q=-1$ 主平台，然后按真实反向次序
经过其余 connector 和双 bump。全区间准确满足
$$
       0\le -Q=q+1\le3,\qquad 1<\ell<132.              \tag{E.3}
$$
上界来自
$505/4+1/2+75/16=2103/16<132$。
准备段由 $\omega_0<2$、$q\le2$ 和长度 $<1/3+2^{-23}$ 给
$\omega_a<16$，而 $\Omega=2^{360}$，故
$L_a=\frac12\log(\Omega/\omega_a)>178\log2>1$。

设最内那个 $q=-1$ 主平台在本坐标中为 $[0,\ell_0]$。
R11 的 $P=-R$ 从 $P_b<1$ 走到 $P_e>2$，且
$dP/d(\log h)=P+16P^2$，所以
$$
 \ell_0>\int_1^2\frac{dP}{P+16P^2}>\frac1{66}>
 \frac1{128},\qquad \ell_0<\log(9/8)<\frac18 .          \tag{E.4}
$$
这些停止值是已固定基点的值；没有随当前标签重停。
于是 $Q=0$ 在整个 $[0,\ell_0]$ 上准确成立。
双 bump 上则有 $7/8<-Q<9/8$，长主平台上 $-Q=3$。
因此 (E.3) 不是将真实曲率号数替换成正下界。

所有量均使用 R69 的 $z_u=r^2/4$ 归一。
特别径向密度是
$$
 \mu_0=w/r=\frac1{4\omega},\qquad
                 2^{-363}<\mu_0<5/18 .                \tag{E.5}
$$
下界使用整个实际区间的 $\omega<(5/4)2^{360}$；
准备段和双 bump 的 $\omega$ 远小于这个值。
因子 $1/4$ 保留，不能使用 R11 早期未归一公式 $w/r=1/\omega$。

## 2. 同一实际非径向矩阵和沿漂移流的准确变换

令 $p=h^{\rm bg}_\theta/r$、$k=h^{\rm bg}_r$ 为背景扰动的原变量。
用前述 Hamiltonian 定理的有量纲 $J$、$D$ 和 $E=1+w^2$，定义
$$
 d=\frac{E(k_\theta-p)}J,\quad
 v_*=\frac{w\sqrt D}J,\quad
 \mu=\frac{J}{rD^{3/2}},\quad c=\mu v_*^2.
$$
真实 raw Jacobi 矩阵和总通量为
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv_*^2\end{pmatrix},
 \qquad \pi=\mu(h_t-dh_\theta)+F^t,
                                                               \tag{E.6}
$$
$$
 \operatorname{div}(G\nabla h)=g-\partial_tF^t-\partial_\theta F^\theta.
                                                               \tag{E.7}
$$
$h$ 是当前 Jacobi 变化，不是背景变量；它没有有限 Fourier 支撑。

平衡定理给整个实际区间的 $N_b<2^{-447}X_\beta$、$X_\beta<1$，
并有超过三单位的额外角宽。故将 $P=p/w,K=k/w$ 的所需角导补齐后，
(J.17) 的相对量 $n$ 可保守取 $n<2^{-440}$。
该处完整商法则立即给
$$
 \frac12<\mu/\mu_0<2,\quad \frac12<c/\mu_0<2,\quad
 |d|+|d_\theta|+|d_{\theta\theta}|<2^{16}n,\quad
 |\partial_\theta\log\mu|<2^{16}n .                    \tag{E.8}
$$
例如 $J/w=1+K+EP_\theta$，其与1之差及所需角导都由
$P,K,P_\theta,K_\theta$ 和上述宽度余量支付。
$D-1$ 由相同原有理式小于 $3n$；在半径 $1/8$ 内对倒数和平方根
作绝对幂级数，并保留两个分量和商法则，费用小于 $2^{16}n$。
这里不对未知 $h$ 使用解析性。

解真实流
$$
 \Phi_t(t,\eta)=-d(t,\Phi(t,\eta)),\qquad \Phi(0,\eta)=\eta,
 \qquad j=\Phi_\eta .
$$
由 $\ell<132$ 和 (E.8)，变分方程
$j_t=-d_\theta j$、
$(j_\eta)_t=-d_{\theta\theta}j^2-d_\theta j_\eta$ 给
$$
 1/2<j<2,\qquad |j_\eta|<1/4,\qquad
 \|\mathcal C_{\Phi(t)}\|_{H^1\to H^1},
 \|\mathcal C_{\Phi(t)^{-1}}\|_{H^1\to H^1}<2 .
                                                               \tag{E.9}
$$
最后两项直接用换元和一阶链式法则，未把裸角小位移称作同阶 norm 小差。
$\Phi$ 以真实径向变量为时间，跨实际 quintic 接缝照常成立。

置 $H=h\circ\Phi$。准确的能量和 Piola 变换为
$$
 \mathfrak a(H,V)=\int_0^\ell\!\!\left\langle
      A H_t\overline{V_t}+B H_\eta\overline{V_\eta}\right\rangle dt,
$$
$$
 A=(\mu\circ\Phi)j,\qquad
 B=\frac{(-Q)(c\circ\Phi)}j,\qquad
 2^{-365}<A<2,\quad 0\le B<24,\quad B|_{[0,\ell_0]}=0,
                                                               \tag{E.10}
$$
$$
 \widetilde g=j(g\circ\Phi),\qquad
 \widetilde F^t=j(F^t\circ\Phi),\qquad
 \widetilde F^\eta=(F^\theta+dF^t)\circ\Phi .
                                                               \tag{E.11}
$$
于是
$$
 \partial_t(AH_t)+\partial_\eta(BH_\eta)
    =\widetilde g-\partial_t\widetilde F^t
                       -\partial_\eta\widetilde F^\eta,
 \qquad P=AH_t+\widetilde F^t=j(\pi\circ\Phi).           \tag{E.12}
$$
$A$ 中是乘 $j$，不是除 $j$。这些公式保留原 weak 源的两个分量。
此外 (E.8)--(E.9) 给
$|\partial_\eta\log A|<1$，后文的 $A^{-1}$ 乘法因而有明确 $H^1$ 费用。

## 3. 完整能量空间及内端的真实 L2 Poisson 列

令 $V_0$ 为光滑周期、两端零迹函数在
$\|V\|_{\mathfrak a}^2=\mathfrak a(V,V)$ 下的完备化。
$A$ 的正下界给
$$
 \|V\|_{L^2_{t,\eta}}\le 2^{190}\|V\|_{\mathfrak a},\qquad
 \sup_t\|V(t)\|_2\le2^{187}\|V\|_{\mathfrak a}.
                                                               \tag{E.13}
$$
直接使用 $\ell/\sqrt{\inf A}$ 与 $\sqrt{\ell/\inf A}$ 即得。
这使 $V_0$ 成为 Hilbert 空间并保留真正的两端零 $L^2$ 迹；
没有在 $B=0$ 的平台上假定椭圆角控制。
由 (E.8)--(E.10)，该能量等价于
$\int(|V_t|^2+(-Q)|V_\eta|^2)$，其中 $Q$ 只依赖径向变量。
先作完整 Fourier 逼近，再对有限个径向系数作零端光滑逼近，
证明该完备化正是上述有限能量、零端迹的弱解类，
没有在零平台边缘附加隐藏边界条件。

对内端数据 $f_C\in L^2$，取
$$
 E_Cf_C=(1-t/\ell_0)_+f_C .
$$
其角导即使只是分布，也全落在 $B=0$ 的区间。
以 Fourier 截断再取能量极限，得到合法的完整 lift，
且
$$
 \|E_Cf_C\|_{\mathfrak a}<16\|f_C\|_2,\qquad
 \sup_t\|E_Cf_C(t)\|_2\le\|f_C\|_2.                   \tag{E.14}
$$
第一式用 $A<2$ 与 $\ell_0>1/128$。
这正是允许内端 $L^2$ 数据的实际几何原因。

外端给原物理角数据 $f_B\in H^1$。
在流坐标中用线性 lift $(t/\ell)(f_B\circ\Phi(\ell))$。
由 $\ell>1$、$\ell<132$、(E.9)--(E.10)，
$$
 \|E_Bf_B\|_{\mathfrak a}<128\|f_B\|_{H^1},\qquad
 \sup_t\|E_Bf_B(t)\|_2<2\|f_B\|_{H^1}.               \tag{E.15}
$$
例如流坐标下，未作端点 pullback 的能量平方不超过
$(2/\ell+24\ell/3)\|f_B\|_{H^1}^2<2^{12}\|f_B\|_{H^1}^2$。
没有忽略 $q=2$ 平台的全部角导数。

对任意两端数据，在 $E_Cf_C+E_Bf_B+V_0$ 中作能量最小化。
其唯一极小者 $H_f$ 满足
$\mathfrak a(H_f,V)=0$，$V\in V_0$。
整个频率空间的 Lax--Milgram 定理给真正的 Poisson 算子，
并有
$$
 \|H_f\|_{\mathfrak a}
 <16\|f_C\|_2+128\|f_B\|_{H^1}.
                                                               \tag{E.16}
$$
它与光滑有限 Fourier 问题的能量极限相同。
实际非径向卷积从未被投影回输入频带。

## 4. DN 的完整四块、mean 与实际内端逆

使用原物理角及原总通量，定义外法向端荷
$$
        p_C=-\pi(0),\qquad p_B=\pi(\ell).
$$
外端的对偶角变换是 (E.12) 的 $P=j\,\pi\circ\Phi$；
内端流准确为恒等，所以内端没有附加角图或密度。

齐次 DN 定义为
$$
 \langle\mathcal N f,e\rangle=\mathfrak a(H_f,H_e),\qquad
 \mathcal T=L^2_C\oplus H^1_B,\quad
 \mathcal T^*=L^2_C\oplus H^{-1}_B .
                                                               \tag{E.17}
$$
它是同一完整物理 Green pairing 给出的自伴正算子。
(E.14)--(E.16) 逐块给
$$
 \|\mathcal N_{CC}\|<2^8,\quad
 \|\mathcal N_{CB}:H^1\to L^2\|
 =\|\mathcal N_{BC}:L^2\to H^{-1}\|<2^{11},\quad
 \|\mathcal N_{BB}\|<2^{14}.                           \tag{E.18}
$$
当 $f_B=0$ 时，$H_f(\ell)=0$，而 $H_f(0)=f_C$，
所以 Cauchy--Schwarz 在真实径向区间给
$$
 \mathfrak a(H_f,H_f)\ge
 \frac{\inf A}{\ell}\|f_C\|_2^2>2^{-373}\|f_C\|_2^2.
                                                               \tag{E.19}
$$
(E.18)--(E.19) 证明 (E.1)，特别
$$
          \|\mathcal N_{CC}^{-1}:L^2\to L^2\|<2^{373}.
                                                               \tag{E.20}
$$
因此对任意完整内端总通量、外端高度和下文源，内端高度可由
(E.20) 唯一恢复。没有删除未知高频，亦没有只证明单模非零。

整个两端 DN 的核准确是共同常高度
$\{(c,c):c\in\mathbb C\}$。
若能量为0，则 $H_t=0$；在真实 $q=2$ 主平台 $B>0$，
故 $H_\eta=0$，于是 $H$ 为同一个常数。反向显然成立。
不能把内外两个 mean 分别商去。齐次时准确有
$\langle p_C\rangle+\langle p_B\rangle=0$；
有源时此和为 $\int\langle g\rangle dt$。
这正是原总通量 mean 行，未被 holonomy-one 背景条件置零。

## 5. L2 普通/weak 源和真正的仿射 DN

先假定
$$
 G_0:=\widetilde g-\partial_\eta\widetilde F^\eta\in L^2,
 \qquad \widetilde F^t/\sqrt A\in L^2,
$$
并置
$$
 S_2=2^{190}\|G_0\|_2+
                        \|\widetilde F^t/\sqrt A\|_2 .
                                                               \tag{E.21}
$$
对零端数据，准确的弱方程为
$$
 \mathfrak a(W,V)=-
 \int\langle G_0,\overline V\rangle dt
 -\int\langle\widetilde F^t,\overline{V_t}\rangle dt .
                                                               \tag{E.22}
$$
右边 norm 至多 $S_2$，所以有唯一 $W\in V_0$ 且
$\|W\|_{\mathfrak a}\le S_2$。
对非零端数据再加 $H_f$。因此在原物理角
$$
 \|h\|_{L^2}\le2^{202}\|f\|_{\mathcal T}+2^{192}S_2 .
                                                               \tag{E.23}
$$
所有积分使用原 $dt\,d\theta$；没有把它换成某一短支集的平均测度。

总 conormal 必须用原 Green 恒等式定义：
$$
 \langle p,e\rangle
 =\mathfrak a(H,E_e)+
        \int\langle G_0,E_e\rangle dt+
        \int\langle\widetilde F^t,(E_e)_t\rangle dt .
                                                               \tag{E.24}
$$
它与 lift 无关。在齐次 harmonic lift $H_e$ 上，
$\mathfrak a(W,H_e)=0$，故
$$
       p=\mathcal N f+\ell_{\rm src},\qquad
       \|\ell_{\rm src}\|_{\mathcal T^*}<2^9 S_2 .
                                                               \tag{E.25}
$$
例如 $\|H_e\|_{\mathfrak a}<2^8\|e\|_{\mathcal T}$，
$\|H_e\|_2<(32+2^{190}2^8)\|e\|_{\mathcal T}$，
直接代入 (E.24) 给此常数。
共同常数测试函数仍准确给 $\int g$，包括全部 mean 源。

原 physical norm 到 (E.21) 也有显式合同：
$$
 S_2<
 2^{194}\bigl(\|g\|_{L^2}
       +\|F^\theta\|_{L^2H^1}
       +\|F^t\|_{L^2H^1}\bigr).                      \tag{E.26}
$$
使用 (E.11) 和
$\partial_\eta\widetilde F^\eta
 =j[(F^\theta)_\theta+d_\theta F^t+d(F^t)_\theta]\circ\Phi$ 即得；
此外
$\|\widetilde F^t/\sqrt A\|_2^2
 =\int |F^t|^2/\mu\,dt\,d\theta$。
没有要求 $F^t_t$ 存在。角向 weak 源的显示一阶费用不能省掉：
在 $Q=0$ 平台，能量本来不控制未知测试函数的角导。

## 6. 原径向 L1 weak 源：准确先消去径向分量

为兼容原完整 weak-source 合同的径向 $L^1$，允许
$g$ 为取值 $L^2_\theta$ 的有限径向测度，$F^t,F^\theta$
为取值 $H^1_\theta$ 的有限径向测度。记其总变差 norm 之和为
$$
 \mathscr P=
 \|g\|_{\mathcal M_tL^2}
 +\|F^t\|_{\mathcal M_tH^1}
 +\|F^\theta\|_{\mathcal M_tH^1}.
                                                               \tag{E.27}
$$
绝对连续的 $L^1_t$ 数据是其特例。
端点原子作为独立 boundary 荷给出；本节测度先取在开区间内，
避免左右迹号数的约定混淆。

在 (E.11) 中按实际流作测度的角 pullback，不改变径向位置。
定义准确径向原函数
$$
 K(t)=-\int_{[0,t)}A(s)^{-1}\,d\widetilde F^t(s),\qquad K(0)=0.
                                                               \tag{E.28}
$$
这里 $K$ 是本节的源 lift，与背景相对变量 $k/w$ 无关。
因为 $|\partial_\eta\log A|<1$、$A>2^{-365}$ 以及 (E.9)，
$$
 K_*:=\sup_t\|K(t)\|_{H^1}<2^{370}\mathscr P,\qquad
 \|G_0\|_{\mathcal M_tL^2}<4\mathscr P .
                                                               \tag{E.29}
$$
这些只用 Banach 值 Stieltjes 积分和 $H^1$ 乘法；
不取 weak 源的径向导数。

令 $H=K+V$。分布意义下准确有
$$
 AH_t+\widetilde F^t=AV_t,\qquad
 \partial_t(AV_t)+\partial_\eta(BV_\eta)
              =G_0-\partial_\eta(BK_\eta).            \tag{E.30}
$$
对 $V_0$ 的新零端源 functional norm 至多
$$
 S_1=2^{187}\|G_0\|_{\mathcal M_tL^2}
          +\left(\int B|K_\eta|^2\right)^{1/2}
       <2^{377}\mathscr P,                            \tag{E.31}
$$
其中 $\sqrt{24\ell}<64$。
使用 (E.13) 的真正径向 sup bound 支付测度源。
$V$ 的端数据为 $(f_C,f_B-K(\ell)\circ\Phi(\ell)^{-1})$。
于是同一个全空间能量逆给唯一的 $V$，继而给 $H$ 和实际总通量。

齐次 DN 仍为 (E.17)，源只增加一个完整仿射列。
它包含 $-\mathcal N(0,K(\ell)\circ\Phi(\ell)^{-1})$ 和
(E.30) 的全部 source contact，不能只保其中一个。
逐项用 (E.18)、(E.29)--(E.31) 得
$$
 \|\ell_{\rm src}\|_{\mathcal T^*}<2^{400}\mathscr P,
 \qquad
 \|(h,\pi)\|_{L^2_{t,\theta}}
 <2^{202}\|f\|_{\mathcal T}+2^{600}\mathscr P .
                                                               \tag{E.32}
$$
给出足以核查的整数账：
$\|K(\ell)\circ\Phi^{-1}\|_{H^1}<2K_*$；
全 mixed DN norm 小于 $2^{16}$；
新 source contact 小于 $2^9S_1$；
故仿射端荷小于 $2^{17}K_*+2^9S_1<2^{400}\mathscr P$。
状态用 (E.13)、(E.16) 和
$\|K\|_{L^2}<16K_*$，总二进制指数小于580。
最后 $\pi\circ\Phi=AV_t/j$，
由 $A<2,j>1/2$ 有 $\|\pi\|_{L^2}<2\|V\|_{\mathfrak a}$。
因此 (E.32) 不把仅有 $L^1$ 导数的 $H$ 冒作原能量空间的元素。

(E.30) 是原全 weak 方程的准确变量替换。
它既没有抛掉径向分量，也没有在零曲率平台免费调用
$B^{-1/2}$。普通源、两个 weak 分量和 mean 都有同一个确定的解。

## 7. 所有有限 affine 跳、两 Gamma 列和 bare/total 区别

若在实际截面 $t_s$ 给物理跳
$$
 h(t_s^+)-h(t_s^-)=a_s,\qquad
 \pi(t_s^+)-\pi(t_s^-)=b_s ,
$$
其中 $a_s\in H^1$、$b_s\in L^2$，将它准确编码为
$$
 dF^t=-\mu(t_s)a_s\,\delta_{t_s},\qquad
 dF^\theta=d(t_s)\mu(t_s)a_s\,\delta_{t_s},\qquad
 dg=b_s\,\delta_{t_s}.                                \tag{E.33}
$$
于是第一行的 jump 是 $a_s$，而
$F^\theta+dF^t=0$ 使第二行 jump 准确为 $b_s$。
在流坐标中，$[K]=a_s\circ\Phi$、$[P]=j(b_s\circ\Phi)$。
原 conormal 的两个号数、height jump 与 flux jump 都保留。
(E.8) 给每个这样的原子可在 (E.27) 中支付
$$
                     \|b_s\|_2+4\|a_s\|_{H^1}.       \tag{E.34}
$$
有限求和即可；没有给任何跳乘一个虚假的径向支集长度。

固定停止 D0 定理 (D.22) 明确当前 compact 与浅层
$\Gamma$ metric 方向支集在 mixed tail，finite connector 与长段无源。
所以对于这些实际方向，本篇内部 $g,F$ 为0，但其到达 $C$ 的
完整两迹仍是端数据。联立 $\Gamma^*$ 时，两列
$D\Gamma_1^*,D\Gamma_2^*$ 分别通过 (E.17)--(E.20)，
不能因本段无体源而删去端列。
另给有限 connector 源时直接加 (E.25) 或 (E.32)；
若一个新的参数方向改变本段 metric，则必须把它的真实 $(g,F)$
和端点几何项加入 (E.27)，这里不将其范数预先设为0。

本篇始终使用总通量 $\pi$。若最终接口要求 bare flux，
准确为 $\pi_{\rm bare}=\pi-F^t$；
端点 $F^t$ 的真实迹和其费用须另给。
任意径向 $L^1$ 或测度范数本身不授予这个端点迹。

## 8. 精确 Cayley 以及它尚未代付的全局部分

令
$$
 \mathcal L=\operatorname{diag}(I_C,\langle D_\theta\rangle_B),
 \qquad
 \mathcal K=\mathcal L^{-1}\mathcal N\mathcal L^{-1}
       :L^2\oplus L^2\to L^2\oplus L^2 .
$$
(E.18) 使 $\mathcal K$ 为有界自伴非负算子，
$\|\mathcal K\|<2^{16}$。
以真正高度和总通量定义
$z=\mathcal L f$、$\eta=\mathcal L^{-1}p$，
则 incoming $\alpha=z+i\eta$、outgoing $\beta=z-i\eta$ 满足
$$
 \beta=\mathcal R\alpha
       -2i(I+i\mathcal K)^{-1}\mathcal L^{-1}\ell_{\rm src},
 \qquad
 \mathcal R=(I-i\mathcal K)(I+i\mathcal K)^{-1}.
                                                               \tag{E.35}
$$
$\mathcal R$ 真正 unitary，源列 norm 不超过
$2\|\ell_{\rm src}\|_{\mathcal T^*}$。
这是由本实际两端逆和完整 Green pairing 推出的 Cayley，
不是给未知外接线直接赋予一个 unitary 假设。
mean 共常数保留为特征值1，独立 mean 通量和所有仿射 mean 行仍在。

因此 $C$ 端现在有同物理角、同高度/总通量单位的全频 $L^2$ 图
(E.1)，并有其完整 inverse、Poisson 和源合同。
外端 $B$ 仍明确使用 $H^1$ 高度、$H^{-1}$ conormal；
不能将该列改称任意 $L^2$ 外口或原 Airy incoming 列。

下一真正缺口是从已定位 $e_X$ 经过未覆盖的 $(129,2)$ 外负分量、
cut128 和末端 quintic 到 $C$。在末端 $q=-1\to-8$ quintic 上，
$Q$ 从0以三阶开始，先前简单 Airy 根定理不覆盖该端点。
还须支付原网络波与 (E.35) 的双向变换、全部 returned 源和原强
标签/平端条件，再闭合主体与外接线。式 (E.35) 本身不证明
$I-\mathcal R\mathcal S_{\rm open}$ 可逆。

本证明只进行解析恒等式、变分存在唯一性和显示的整数上界推导；
没有新增或重跑任何数值 target、旧 native 或 GitHub Actions 计算。
