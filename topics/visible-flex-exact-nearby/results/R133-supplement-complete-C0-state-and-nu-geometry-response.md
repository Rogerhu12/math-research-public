# R133：完整状态与度量参数到位置、标架和曲率的实际全区间常数

2026-11-14，visible-exact-astra-ac0d。

**已证明的条件性比较定理；全部系数常数已经实际计算。** 本篇在原
ac1 候选、准确原 $\eta_0$、整个 $0\le r\le25/8$ 上，直接消费已完成的
3071 个 strict 盒、真正根间隙盒和4650个 positive 盒，共7722盒。
新计算没有重跑候选求解、primitive、原几何 ODE 或已经完成的数值门。
未知状态保留全部角频率、真实均值与物理振幅。

设原完整 moving 状态为 $(u,v)$，另一状态为 $(\widetilde u,\widetilde v)$。
定义

$$
\epsilon=\max\{\|\widetilde u-u\|_{C^0_{r,\phi}},
                  \|\widetilde v-v\|_{C^0_{r,\phi}}\},
\qquad t=|\widetilde\nu-\nu|,
\qquad \epsilon\le10^{-3},\quad t\le10^{-5}.                 \tag{C.1}
$$

这里 $v$ 包含完整径向基态和偶均值；不是去均值后或除以振幅后的误差。
采用[完整 moving 标架方程](R133-supplement-moving-frame-with-complete-residual-and-mean.md)
分别生成两条径向模型。两者在 $r=25/8$ 的全角世界锚误差记为
$b_Q=\sup_\phi\|\widetilde Q-Q\|_{\rm op}$、
$b_F=\sup_\phi|\widetilde F-F|$。则

$$
\boxed{\begin{aligned}
\|\widetilde Q-Q\|_{C^0,\rm op}
 &\le b_Q+15.736315\epsilon+.304809t,\\
\|\widetilde F-F\|_{C^0}
 &\le b_F+1.950540b_Q+30.196406\epsilon+.105999t.
\end{aligned}}                                               \tag{C.2}
$$

对原代数第二基本形式矩阵 $S$ 与变化后矩阵 $\widetilde S$，有

$$
\boxed{\quad
 \|\widetilde S-S\|_{C^0,\rm op}
 \le141.332651\epsilon+3.988052t.
 \quad}                                                       \tag{C.3}
$$

只有另一状态确实解完整 GC 方程并产生相应浸入时，$\widetilde S$ 的特征值
才是该浸入的主曲率，$\widetilde Q$ 的相应列才是其几何单位法向。
原模型不必解 GC；本定理没有把原数值曲面当作精确等距曲面。

原全7296盒证书已给 $\|S\|<11.092578014346$。本篇另得其完整正特征值界
$\lambda_+(S)<3.856372$。因此在 (C.1) 的整个状态与参数邻域，若得到上述
精确 GC 解，必有

$$
 |\kappa|<11.233951<12,\qquad
 \kappa_+<3.997745<196/27.                                  \tag{C.4}
$$

这不证明存在满足 (C.1) 的解，也不证明它满足闭合、外帽或最终位移要求。

## 1. 同一个对象与 $C^0$ 原函数

候选 SHA256 是
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
原参数为

$$
 \alpha={6890507429876859\over9007199254740992},\quad
 \nu={-2572625729470897\over72057594037927936},\quad
 \eta_0={-7789843107295549\over4611686018427387904}.
$$

参数 $\eta$ 在本篇固定为准确 $\eta_0$；没有由较宽系数证书推授全 $\eta$
邻域。已完成的连续修复与原候选不同，若使用修复中心，其差必须计入
$\epsilon$。同样，任何 $\nu$ 变化造成的基态变化也属于完整状态差。

四重周期的长度为 $L=\pi/2$。周期锯齿核
$K_L(s)=L/2-s$，$0<s<L$，满足分布恒等式
$K_L'=L\delta_0-1$ 和零均值。以归一化测度卷积，定义

$$
 If(x)={1\over L}\int_0^L K_L(x-y)f(y)\,dy.
$$

于是 $(If)'=f-\langle f\rangle$、$\langle If\rangle=0$，而且

$$
 \|If\|_\infty\le {1\over L}\int_0^L|K_L(s)|\,ds\,
                       \|f\|_\infty
                  ={\pi\over8}\|f\|_\infty.              \tag{C.5}
$$

该式直接作用于完整 $f$，无需先估计 $\|f-\langle f\rangle\|$，所以没有
多余因子2。对核符号函数的连续逼近也说明此算子范数准确为 $\pi/8$。

strict 原证书中的 $u_\phi,d_\phi$ 是全圆周点态上界。由于 $u,d$ 是真实
四重奇函数，每一点距某个 $k\pi/4$ 零点不超过 $\pi/8$，故消费者取
$U\le(\pi/8)\|u_\phi\|_\infty$、
$D\le(\pi/8)\|d_\phi\|_\infty$。这些是 $C^0$ 界，本篇没有把它们误称为
Wiener 范数。positive 与根盒中的完整 $A_0$ 界蕴含所需的 $C^0$ 界。

## 2. 真实紧支度量控制的有限差分

原度量控制为 $E_\nu=E\exp(\nu w)$，$E_\nu=a^2\gamma^2$。半径 $a$ 和
$\beta=a'/a$ 不随 $\nu$ 变化。准确的紧支函数是

$$
 w(r)=4096s^6(1-s)^6,\quad
 s={r-1/20\over13/100},\qquad 1/20\le r\le9/50,
                                                               \tag{C.6}
$$

区间外为零；它在两个端点具有所需的五阶零 jets。令 $z=\widetilde\nu-\nu$。
由径向曲率的准确公式直接得到

$$
 \widetilde\gamma=\gamma e^{zw/2},\qquad
 \widetilde K=e^{-zw}
       \left(K+{z\beta w'\over2a^2\gamma^2}\right).         \tag{C.7}
$$

这是一条有限差分恒等式，不能只用中心的一阶参数导数代替。
在一个真实闭盒上，设

$$
 0<a_-\le a\le a_+,\quad |\beta|\le b,\quad
 0<g_-\le\gamma\le g,\quad |K|\le k,\quad
 |w|\le W\le1,\quad |w'|\le W_1.
$$

以 $t_0=10^{-5}$ 定义

$$
 G_\nu={gW\over2}e^{t_0W/2},\qquad
 K_\nu=e^{t_0W}\left(kW+{bW_1\over2a_-^2g_-^2}\right).
                                                               \tag{C.8}
$$

使用 $|e^x-1|\le|x|e^{|x|}$，(C.7) 给
$|\widetilde\gamma-\gamma|\le G_\nu t$、
$|\widetilde K-K|\le K_\nu t$。因此可以使用

$$
 G=g+G_\nu t_0,\qquad
 \widetilde g_-=g_-e^{-t_0W/2},\qquad
 \widetilde k=k+K_\nu t_0.                                \tag{C.9}
$$

支撑外两个参数增益准确为零。消费者在需要时按两个准确支撑端点拆盒，
从不将非零多项式延伸到支撑外。所有活跃盒的真实 $a_-$ 都由 strict
原证书提供；根间隙与 positive 区域不需要未供给的紧支参数下界。

## 3. 完整漂移、真实均值与连接差

在同一个盒内，记

$$
 \|u\|_\infty\le U,\quad \|v\|_\infty\le V,
 \quad\|d\|_\infty\le D,\quad |m|\ge\mu,
 \quad |v|\ge v_-,\qquad m=\langle v\rangle,
$$

其中 $m,v$ 都为负。设 $e_0=10^{-3}$，并取
$\widetilde\mu=\mu-e_0$、$\widetilde v_-=v_--e_0$。
消费者逐盒验证这两个数及度量下界严格为正。由于
$|\widetilde m-m|\le\epsilon$，以下分母都保持真正完整均值。

完整漂移满足

$$
 d=-\beta I(u^2+Kv^2).
$$

由 (C.5) 和有限差分，置

$$
 \begin{aligned}
 d_u&={\pi b\over8}
       \big(2U+e_0+\widetilde k(2V+e_0)\big),\\
 d_\nu&={\pi b\over8}K_\nu V^2,
 \end{aligned}\qquad
 \|\widetilde d-d\|_\infty\le d_u\epsilon+d_\nu t.         \tag{C.10}
$$

所有双变量混合项都已用 $e_0,t_0$ 上界吸收，未省略 $\epsilon t$。
真实比例的差满足

$$
 \left|{\widetilde v\over\widetilde m}-{v\over m}\right|
 \le r_v\epsilon,\quad
 \left|{\widetilde u\over\widetilde m}-{u\over m}\right|
 \le r_u\epsilon,
 \quad
 \left|{1\over\widetilde m}-{1\over m}\right|
 \le r_m\epsilon,                                         \tag{C.11}
$$

其中

$$
 r_v={1\over\widetilde\mu}+{V\over\mu\widetilde\mu},
 \quad r_u={1\over\widetilde\mu}+{U\over\mu\widetilde\mu},
 \quad r_m={1\over\mu\widetilde\mu}.
$$

令 $z_f=dv/m-\gamma u$，则其参考上界和差分增益为

$$
 \begin{aligned}
 T&={DV\over\mu}+gU,\\
 T_u&=Dr_v+{(V+e_0)d_u\over\widetilde\mu}+G,\\
 T_\nu&={(V+e_0)d_\nu\over\widetilde\mu}+G_\nu U.
 \end{aligned}                                             \tag{C.12}
$$

由先将差写成 $d\,\delta(v/m)+\delta d\,\widetilde v/\widetilde m$
再使用 (C.10)–(C.11)，得到
$|\widetilde z_f-z_f|\le T_u\epsilon+T_\nu t$。

径向反对称连接的三个系数取

$$
 p={\beta z_f\over\gamma},\qquad
 q=a\left(\gamma Kv+{du\over m}\right),\qquad
 \ell={ad\over m}.
$$

符号选择对下面的 operator norm 不影响。完整差分别被
$p_u\epsilon+p_\nu t$、$q_u\epsilon+q_\nu t$、
$\ell_u\epsilon+\ell_\nu t$ 控制，其中

$$
\begin{aligned}
p_u&={bT_u\over\widetilde g_-},&
p_\nu&={bT_\nu\over\widetilde g_-}
       +{bTG_\nu\over\widetilde g_-g_-},\\
q_u&=a_+\left(G\widetilde k+Dr_u
                   +{(U+e_0)d_u\over\widetilde\mu}\right),&
q_\nu&=a_+\left[V(GK_\nu+kG_\nu)
                   +{(U+e_0)d_\nu\over\widetilde\mu}\right],\\
\ell_u&=a_+\left({d_u\over\widetilde\mu}+Dr_m\right),&
\ell_\nu&={a_+d_\nu\over\widetilde\mu}.
\end{aligned}                                                \tag{C.13}
$$

三阶反对称矩阵的准确 operator norm 为其三个系数向量的欧氏范数。
定义

$$
 L_{\Omega,u}=\sqrt{p_u^2+q_u^2+\ell_u^2},\quad
 L_{\Omega,\nu}=\sqrt{p_\nu^2+q_\nu^2+\ell_\nu^2}.       \tag{C.14}
$$

则 $\|\widetilde\Omega-\Omega\|\le
L_{\Omega,u}\epsilon+L_{\Omega,\nu}t$。
位置速度在标架中的两非零分量为 $a\gamma$ 与 $az_f$，相应地可取

$$
 L=a_+\sqrt{g^2+T^2},\quad
 L_{f,u}=a_+T_u,\quad L_{f,\nu}=a_+\sqrt{G_\nu^2+T_\nu^2}.
                                                               \tag{C.15}
$$

这些公式只用完整 $C^0$ 范数，不假定有限频率、不删除均值，也不需要
用近似 GC 方程替换任何导数。

## 4. 从外世界锚向内的完整传播

两条径向框架方程都具有反对称连接；各自的基本解正交。变分常数公式给

$$
 \|\widetilde Q(r)-Q(r)\|
 \le b_Q+\epsilon\int_r^R L_{\Omega,u}(s)\,ds
             +t\int_r^R L_{\Omega,\nu}(s)\,ds.             \tag{C.16}
$$

没有 Gronwall 指数。对位置使用准确分解
$\widetilde Q\widetilde f-Qf=(\widetilde Q-Q)f
                                  +\widetilde Q(\widetilde f-f)$，
便得到

$$
 \begin{aligned}
 |\widetilde F(r)-F(r)|\le{}&b_F+b_Q\int_r^R L(s)\,ds\\
 &+\epsilon\int_r^R\left[L(s)\int_s^R L_{\Omega,u}(x)\,dx
                                         +L_{f,u}(s)\right]ds\\
 &+t\int_r^R\left[L(s)\int_s^R L_{\Omega,\nu}(x)\,dx
                                         +L_{f,\nu}(s)\right]ds.
 \end{aligned}                                               \tag{C.17}
$$

每个盒上的系数均取向外上界。若已经由外向内累计连接积分 $O$、位置系数
$P$ 和长度 $J$，下一个宽度为 $h$ 的盒准确按

$$
 P\leftarrow P+hLO+\tfrac12h^2LL_\Omega+hL_f,
 \quad O\leftarrow O+hL_\Omega,\quad J\leftarrow J+hL.     \tag{C.18}
$$

其中右端 $O$ 是更新前的值。$h^2/2$ 项是同盒三角区域的准确面积；
这既没有漏付本盒连接变化，也没有再次加入已独立支付的径向或角插值误差。
所有 integrands 非负，所以最内端的累计值同时控制每一个 $r$。
完整7722盒得到

| 累计系数 | 实际严格上界 |
|---|---:|
| $\int L_{\Omega,u}$ | $15.736314562$ |
| $\int L_{\Omega,\nu}$ | $.304808091$ |
| 状态到位置的双积分 | $30.196405189$ |
| $\nu$ 到位置的双积分 | $.105998012$ |
| $\int L$ | $1.950539012$ |

式 (C.2) 使用稍大的十进制有理数，因而不依赖展示舍入方向。

## 5. 曲率的完整有限差与严格正部

对应的代数矩阵为

$$
 S=\begin{pmatrix}Kv+u^2/v&u/v\\u/v&1/v\end{pmatrix}.
                                                               \tag{C.19}
$$

令

$$
 A_u=\widetilde k+{2U+e_0\over\widetilde v_-}
                         +{U^2\over v_-\widetilde v_-},\quad
 B_u={1\over\widetilde v_-}+{U\over v_-\widetilde v_-},\quad
 C_u={1\over v_-\widetilde v_-}.                             \tag{C.20}
$$

准确展开每个分式给
$|\delta S_{11}|\le A_u\epsilon+K_\nu Vt$、
$|\delta S_{12}|\le B_u\epsilon$、
$|\delta S_{22}|\le C_u\epsilon$。对称矩阵的 operator norm 不超过最大绝对
行和，故本盒曲率增益是

$$
 L_{\kappa,u}=\max(A_u+B_u,B_u+C_u),\qquad
 L_{\kappa,\nu}=K_\nu V.                                  \tag{C.21}
$$

其完整全域最大值分别小于141.332651和3.988052，证明 (C.3)。

对参考正曲率，若盒内 $K\ge0$，则 $\det S=K\ge0$，且 $1/v<0$，因此
$S$ 负半定，正特征值部分准确为零。否则设 $K_-\ge\max(0,-K)$，
取 $a_0=K_-V$、$c_0=-1/V$、$b_0=U/v_-$。因 $u^2/v\le0$，有
$S_{11}\le a_0$、$S_{22}\le c_0$、$|S_{12}|\le b_0$。
最大特征值的变分公式或二阶特征值表达式给

$$
 \lambda_+(S)\le
 \max\left(0,{a_0+c_0+\sqrt{(a_0-c_0)^2+4b_0^2}\over2}\right).
                                                               \tag{C.22}
$$

根间隙不强制曲率符号；在那里用完整 $|K|$ 作为 $K_-$。
全7722盒的 (C.22) 最大值小于3.856372。

消费者也保存了一条便宜的参考绝对行和界12.095499；它本身不足以证明12
的目标，本篇没有使用它。更强的原候选绝对特征值界来自已经完成的
[7296闭盒记录](../notes/2026-11-14-R133-final-complete-moving-residual.md)：
完整 native SHA256 为
`6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`，
字段 `bounds.maximum_candidate_principal_abs` 小于11.092578014346。
其 candidate、原参数、全圆周和共同 $\eta_0$ 与本篇相同，因此可以直接
与 (C.3) 组合，无需重算旧曲率。
特征值的 operator norm 扰动界同时控制绝对值与正部。把 (C.1) 的上限
代入，误差小于 $.14137253152$，从而得到 (C.4)。

## 6. 实际运算、输入范围和余下责任

源码为
[完整 $C^0$ 消费者](../scripts/fourfold_codazzi_complete_C0_geometry_response.py)，
实际正常返回0，耗时25.045895秒。保存每一个真盒的全部增益、真实 mean/v
间隙、紧支参数界和从外向内的累计积分；没有只保存全局浮点摘要。
输入 SHA、完整 native、准确命令见
[本次原生记录](../notes/2026-11-14-R133-complete-C0-state-nu-geometry-response.md)。

结合[完整角向证书](R133-supplement-complete-angular-model-geometry-from-moving-residual.md)
及[径向张量消费者](R133-supplement-directed-radial-ODE-error-and-tensor-native.md)时，
先由张量证书获得原模型相对于保存网格的误差，再加 (C.2)。如果输入状态
由 $H^1_4$ 控制，必须先使用已证明的完整 $H^1_4\to C^0$ 包含常数并恢复
真实物理振幅；不能把有限截断的系数范数直接当作 (C.1)。

本篇仍保留独立的 $b_F,b_Q$。真正外帽/深尾/静态 marker 必须给出同一个
世界锚及其比较费；$\nu$ 最终选择以后全族必须固定这个同一度量。
本篇未供给全局逆、实际非线性误差半径、精确闭合或 $C^2$ 连续闭族。
这些是继续工作的必要条件，不因已有数值余量而省略。
