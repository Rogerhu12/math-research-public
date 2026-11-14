# R119 续篇：实际正型跨端传输的指数权、全参数差与完整 affine 源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在此前已付实际 KAM 端角的每个内部正型分量，
完整 DN 的两个跨端块均得到真实的半光学长度解析增益。实际块与同一
径向参考块的差也满足这个指数加权估计，保留所有频率和 mean。
这个结论直接作用于真实散度 PDE，不从绝对 Cayley 小差倒除一个
指数小的 transmission。所有源仍按其真实支集、密度、两个端点和
总 flux 计费。

本篇是全网络中的跨端算子合同。它保留半个光学长度的衰减，未声称
参考的全部指数衰减都可以被逆掉；最后明确指出尚需接合的网络空间。

## 1. 同一实际正型段及完整比较矩阵

采用[实际正型 DN 到完整 Airy Cayley](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)
的同一对象、两个真 KAM 端角、先 drift 再光学插值的真坐标
$\Xi(t,\eta)=(t,\Phi(t,\eta))$。参考

$$
 \mu_0=w_{\rm ref}/a,\qquad A\ge0,\qquad
 \ell=\int_{t_-}^{t_+}\sqrt A\,dt,
 \quad \tau(t)=\int_{t_-}^{t}\sqrt A\,ds.
 \tag{T.1}
$$

为避免与标签混淆，把当前标签记为 $a_{\rm lab}$。真实参数已经按
$\Gamma=\Gamma^*(a_{\rm lab})$ 选择；本篇的 $A$ 在正型段上不依赖
下降 bump，物理尺度仍使用这个实际 $\Gamma$ 的尺度。

令 $\mathsf C(t,\eta)$ 是前篇 (C.7) 的准确矩阵，即

$$
 \mathscr E_a(h,v)=\int_I\mu_0\left\langle
 \mathsf C(t,\eta)(h_t,\sqrt A h_\eta),
                         (v_t,\sqrt A v_\eta)\right\rangle dt.
 \tag{T.2}
$$

前篇已逐项给出全部 Jacobian 和交叉项。在完整复角条带
$|\operatorname{Im}\eta|\le1/8$，其每个误差系数由

$$
 \epsilon_I=2^{104}(j+5)^2\mathcal M_j\delta_j^{-3/2}\|X\|,
 \qquad \sum_I\epsilon_I<2^{320}\|X\|,
 \quad\|X\|\le2^{-262144}
 \tag{T.3}
$$

控制。总和包含两正分量、所有有限前缀、两次规范接缝和无限深尾。
下文作一个安全的 Fourier 代数放宽
$\widehat\epsilon_I=2^8\epsilon_I$。

实际几何还给一个比 $\ell<1$ 更适合本篇的界。由同一
$\Delta^+<3(j+4)$、quintic 的 $S'\le15/8$、
$|I|<\delta_j^{3/2}$，

$$
 A_{\max}<2^{12}(j+4)\delta_j^{-3/2},\qquad
 \ell<2^6\sqrt{j+4}\,\delta_j^{3/4}<2^{-80},\quad j\ge129.
 \tag{T.4}
$$

最后的包络随 $j$ 严格下降；新首剪切 $2^{128}$ 已包括在真实
$\Delta^+$ 界中。没有把一个旧 profile 的 optical 数值授予新尾。

## 2. 全部频率的两个准确端点能量单位

用前篇实际径向矩阵

$$
 \mathsf S_m=\beta_m^{-1}
       \begin{pmatrix}\alpha_m&-1\\-1&\delta_m\end{pmatrix},
 \qquad \det\begin{pmatrix}\alpha_m&\beta_m\\
                            \gamma_m&\delta_m\end{pmatrix}=1.
 \tag{T.5}
$$

定义两个正 Fourier 算子

$$
 D_-=(\alpha_m/\beta_m)_m,\qquad
 D_+=(\delta_m/\beta_m)_m,
 \quad B_0=(-1/\beta_m)_m.
 \tag{T.6}
$$

它们保留原真实径向解，不用大 $m$ 渐近式替代。
包括 $m=0$ 时仍有
$D_{-,0}=D_{+,0}=R_I^{-1}$、$B_{0,0}=-R_I^{-1}$，
$R_I=\int_I\mu_0^{-1}dt$。所以本篇的每个端点空间都保留 mean，
不需要把共同常数槽商掉。

记 $\mathcal H_\pm$ 的 norm 为 $\|D_\pm^{1/2}f\|_2$。
径向 harmonic lift $H_0(f,0)$、$H_0(0,g)$ 的完整能量分别准确为
$\|f\|_{\mathcal H_-}^2$、$\|g\|_{\mathcal H_+}^2$。
实际 DN 写为

$$
 N_a=\begin{pmatrix}N_{--}&B_{-+}\\
                           B_{+-}&N_{++}\end{pmatrix},
 \qquad B_{-+}=B_{+-}^*\quad\hbox{在实背景上}.
 \tag{T.7}
$$

下面同时支付这两个跨端块，不把它们当成一个可忽略的误差。

## 3. 变角宽弱形式：不引入 $A_t$ 或径向接缝导数

令 $|D|$ 是物理四重频率 $|m|$ 的乘子，包含 $m=0$。
取 $0\le r\le1/16$、$\alpha=1/2$，定义

$$
 \rho(t)=r+\alpha\tau(t),\qquad
 W(t)=e^{\rho(t)|D|},\qquad
 \rho'=\alpha\sqrt A.
 \tag{T.8}
$$

由 (T.4)，$0\le\rho<3/32$。四重 Fourier 系数的 Cauchy 界给

$$
 \sum_{k\in4\mathbb Z}e^{\rho|k|}
       \|\widehat{(\mathsf C-I)}_k(t)\|_{\rm op}
 \le 2\epsilon_I\left(1+\frac2{e^{4(1/8-\rho)}-1}\right)
 <2^8\epsilon_I=\widehat\epsilon_I.
 \tag{T.9}
$$

这里 $e^{1/8}-1>1/8$ 已足够。由
$e^{\rho|m|}\le e^{\rho|m-n|}e^{\rho|n|}$，(T.9) 直接证明

$$
 \|W(\mathsf C-I)W^{-1}\|_{L^2\to L^2}
                      <\widehat\epsilon_I.
 \tag{T.10}
$$

这是真正乘法矩阵的 Fourier 卷积界，不是裸角 pullback 的同宽小差。

对加权未知 $u=Wh$ 和测试 $v$ 定义

$$
 \mathbf d_-u=(u_t-\rho'|D|u,\sqrt A\,u_\eta),\qquad
 \mathbf d_+v=(v_t+\rho'|D|v,\sqrt A\,v_\eta),
$$
$$
 \mathcal B_{\rho,a}(u,v)=\int_I\mu_0
   \langle W\mathsf C W^{-1}\mathbf d_-u,\mathbf d_+v\rangle dt.
 \tag{T.11}
$$

对有限 Fourier 数据直接求导给准确恒等式
$\mathcal B_{\rho,a}(Wh,v)=\mathscr E_a(h,Wv)$。
它只用 $\rho'$；没有 $A_t,A_{tt}$ 或拼接点上的隐藏 source。
均值的 $|D|$ 项准确为0。

参考部分的实部精确抵消两个交叉项：

$$
 \operatorname{Re}\mathcal B_{\rho,0}(u,u)
 =\int_I\mu_0\bigl(|u_t|^2+(A-\rho'^2)|u_\eta|^2\bigr)
 \ge(1-\alpha^2)\|u\|_{\mathscr E_0}^2.
 \tag{T.12}
$$

同时 $\|\mathbf d_\pm u\|_{L^2_{\mu_0}}\le(1+\alpha)\|u\|_{\mathscr E_0}$。
(T.3)、(T.9) 因而给

$$
 \begin{aligned}
 \operatorname{Re}\mathcal B_{\rho,a}(u,u)
 &\ge\left(\frac34-\frac94\widehat\epsilon_I\right)
                   \|u\|_{\mathscr E_0}^2
 >\frac12\|u\|_{\mathscr E_0}^2,\\
 |\mathcal B_{\rho,a}(u,v)|&<3\|u\|_{\mathscr E_0}\|v\|_{\mathscr E_0},\\
 |(\mathcal B_{\rho,a}-\mathcal B_{\rho,0})(u,v)|
 &\le\frac94\widehat\epsilon_I\|u\|_{\mathscr E_0}\|v\|_{\mathscr E_0}.
 \end{aligned}                                            \tag{T.13}
$$

零 Dirichlet 能量空间与原正型定理相同。$A=0$ 的真实转向端不损坏这些
估计，因为所有 $|D|$ 项都带已经保留的 $\sqrt A$。
Lax–Milgram 给这个完整加权问题，而非先假定原解已解析增宽。

## 4. 真正跨端传输与其加权差

先给左端数据 $f$、右端数据0。令 $f_r=e^{r|D|}f$，以
$u_D=H_0(f_r,0)$ 作 lift。对 $u=u_D+z$，(T.13) 给

$$
 \|z\|_{\mathscr E_0}\le6\|f_r\|_{\mathcal H_-},\qquad
 \|u\|_{\mathscr E_0}\le7\|f_r\|_{\mathcal H_-}.
 \tag{T.14}
$$

$h=W^{-1}u$ 具有原来的两个边界值；其一阶径向能量也由
$u_t-\rho'|D|u$ 控制。原真实 Dirichlet 唯一性将它准确识别为此前
构造的真实解。这一步同时证明了加权正则性。

用 $v=H_0(0,g)$ 测试，完整弱 DN 恒等式为

$$
 \langle e^{(r+\ell/2)|D|}B_{+-}f,g\rangle
                  =\mathcal B_{\rho,a}(u,H_0(0,g)).
 \tag{T.15}
$$

故真正全频算子满足

$$
 \boxed{\quad
 \|D_+^{-1/2}e^{(r+\ell/2)|D|}B_{+-}
            e^{-r|D|}D_-^{-1/2}\|_{2\to2}<32.
 \quad}                                                    \tag{T.16}
$$

反方向取 $\rho(t)=r+(\ell-\tau(t))/2$；其导数只是换号，(T.11)–(T.14)
全部保持，因此也有

$$
 \|D_-^{-1/2}e^{(r+\ell/2)|D|}B_{-+}
            e^{-r|D|}D_+^{-1/2}\|_{2\to2}<32.
 \tag{T.17}
$$

这是两个真实端点及它们各自原 KAM 角坐标中的传输，不重新改动端角。

对同一输入，记 $u_0$ 为加权参考解，$\delta u=u_a-u_0$。
它的两个边界均为0，由准确差方程

$$
 \mathcal B_{\rho,a}(\delta u,v)
 =-(\mathcal B_{\rho,a}-\mathcal B_{\rho,0})(u_0,v)
$$

和 (T.13)–(T.14) 得
$\|\delta u\|_{\mathscr E_0}<32\widehat\epsilon_I\|f_r\|_{\mathcal H_-}$。
再在 (T.15) 中作差，右侧上界小于
$(3\cdot32+7\cdot9/4)\widehat\epsilon_I<128\widehat\epsilon_I$。
因而可安全取

$$
 \boxed{\quad
 \|D_+^{-1/2}e^{(r+\ell/2)|D|}(B_{+-}-B_0)
       e^{-r|D|}D_-^{-1/2}\|<2^{16}\epsilon_I,
 \quad}                                                    \tag{T.18}
$$

以及交换左右的同一个界。参考 $B_0$ 是 (T.6) 的完整精确块。
把两个方向和所有真实分量相加得到

$$
 \sum_{I,\,\pm}\|\text{(T.18) 的加权差}\|
 <2^{337}\|X\|\le2^{-261807}.
 \tag{T.19}
$$

这里每个 summand 使用自己的真实 $\ell_I$ 和 $D_{\pm,I}$。
它不是把不同层的光学长度混成一个常数。

## 5. 原 Airy 单位及完整参数导数

前篇 reference-normalized Airy 高度由
$Y_h=W_e\sqrt{\alpha_{0,e}}f_e$ 给出。记准确 Fourier 乘子
$L_e=\alpha_{0,e}^{-1/2}W_e^{-1}$，则 $P_a=L^*N_aL$。
定义

$$
 \mathcal D_e=L_e^2D_e,\qquad
 P_{+-}=L_+B_{+-}L_-.
 \tag{T.20}
$$

所有这些参考乘子都与 $e^{s|D|}$ 可交换，所以 (T.16)–(T.18)
在 $B,D$ 换成 $P,\mathcal D$ 后准确保持，常数不变。
真实 normal shear 是对角算子，只增加前篇的完整 $T_0$，不删除
任一 cross block。真实 root frame 的后续完整三角变换仍须按前篇
(C.25)–(C.30) 使用，不能只变换高度行。

尺度 $\rho(\Gamma)$ 在这里也没有藏进固定参考。正段上
$D_e\propto\rho^{-1}$，而 $L_e\propto\rho^{1/2}$，所以
$\mathcal D_e$ 和归一的参考 $P_0$ 准确与该尺度无关。
对复参数先将 form 的共同 $\rho^{-1}$ 因子提出，使用同一个正的
参考 form 即可证明 (T.13)。

由完整系数的联合全纯性及 (T.13) 的统一逆，加权 cross 算子在
$\|a_{\rm lab}\|_{224}<A_*=2^{-262148}$ 上为真正的有界算子值全纯
map。这一步使用的是散度系数和有界 form 逆；没有声称粗 Sobolev
pullback 本身无损耗解析。特别 (T.19)、$\|X\|<16\|a_{\rm lab}\|$
给所有分量组成的强 $\ell^1$ 算子族

$$
 \|\mathcal T(a_{\rm lab})-\mathcal T(0)\|
                      <2^{341}\|a_{\rm lab}\|_{224}.
 \tag{T.21}
$$

在 $\|a_{\rm lab}\|<A_*/2$，Cauchy 取半径 $A_*/4$ 给
$\|D\mathcal T(a_{\rm lab})\|<2^{343}$。
导数包括当前 $\Gamma^*(a_{\rm lab})$、两端角、drift、密度和参考 Airy
单位的实际依赖；式 (T.21) 本身只归一到 (T.20) 的 frame。
若微分原非线性方程，另产生的度量 source 仍须按真实参数源合同输入；
这个算子族导数不把它变为固定目标的齐次 Jacobi 列。

## 6. 完整 ordinary/weak source 与实际支集的指数筛选

在已经指定的真实角图中，方程是

$$
 \operatorname{div}(G_a\nabla h)=\widehat s-\operatorname{div}\widehat F.
 \tag{T.22}
$$

原物理源的准确 Piola 变换仍为

$$
 \widehat s=\Phi_\eta(s_h\circ\Xi),\qquad
 \widehat F^t=\Phi_\eta(F^t\circ\Xi),\qquad
 \widehat F^\eta=(F^\theta-\Phi_tF^t)\circ\Xi.
 \tag{T.23}
$$

ordinary Darboux 源满足 $s_h=w_{\rm ref}^2JD^{-3/2}e$。
保留这个物理因子，不将它换成单位源。
定义真正加权源量

$$
 \mathcal S_\rho=sqrt{R_I}\|W\widehat s\|_{L^1_tL^2_\eta}
 +\frac32\left[\int_I\left(
 {\|W\widehat F^t\|_2^2\over\mu_0}
 +{\|W\widehat F^\eta\|_2^2\over A\mu_0}\right)dt\right]^{1/2}.
 \tag{T.24}
$$

只消费满足这个完整量有限的源。任意粗 weak source 在转向端并不自动满足
其中的 $A^{-1}$ 权。

准确变权后的 source 泛函为

$$
 \mathcal L_\rho(v)=\int_I\left[
 \langle W\widehat s,v\rangle
 +\langle W\widehat F^t,v_t+\rho'|D|v\rangle
 +\langle W\widehat F^\eta,v_\eta\rangle\right]dt.
 \tag{T.25}
$$

其中 $\rho'|D|v$ 是必须保留的真实 weak-source 项。
对在至少一端为0的 $v$，径向原函数给
$\|v(t)\|_2\le\sqrt{R_I}\|v\|_{\mathscr E_0}$。
因此 $|\mathcal L_\rho(v)|\le\mathcal S_\rho\|v\|_{\mathscr E_0}$。

两个 Dirichlet 数据都为0时，完整方程是
$\mathcal B_{\rho,a}(u,v)=-\mathcal L_\rho(v)$，故
$\|u\|_{\mathscr E_0}\le2\mathcal S_\rho$。
真实**总 outward flux** $q=(G_a\nabla h+\widehat F)\cdot n$ 满足

$$
 \langle W_+q_+,g\rangle
 =\mathcal B_{\rho,a}(u,H_0(0,g))
                      +\mathcal L_\rho(H_0(0,g)).
 \tag{T.26}
$$

所以

$$
 \|D_+^{-1/2}W_+q_+\|_2<8\mathcal S_\rho,
 \quad
 \left(\|D_-^{-1/2}W_-q_-\|_2^2+
       \|D_+^{-1/2}W_+q_+\|_2^2\right)^{1/2}<16\mathcal S_\rho.
 \tag{T.27}
$$

左端单列由 $H_0(g,0)$ 给出，方向号数按 outward 保留。
全 mean 的准确守恒关系仍是

$$
                  (q_-)_0+(q_+)_0=\int_I(\widehat s)_0dt.
 \tag{T.28}
$$

若源确实支持于 $\tau\le\tau_s$，取
$\rho(t)=r+(\tau(t)-\tau_s)/2$，其中
$\ell/2\le r\le1/16$。则源支集上 $W\le e^{r|D|}$，目标端具有
真正增加的宽 $r+(\ell-\tau_s)/2$。(T.27) 因而给从真实支集到目标端的
指数筛选。反方向完全同样。没有已知支集距离时，仍使用 (T.24) 的完整
加权源合同，而不虚构额外衰减。

若输入给在原物理 $\theta$ 上，(T.23) 的复合也必须付角宽。实际
$\Phi-\mathrm{id}$ 的完整 $\mathcal A_{3/32}$ norm 小于 $1/128$；因此
给原 ordinary $e$ 宽 $\rho(t)+1/128$ 即足以直接消费总图，并可安全取

$$
 \|W(t)\widehat s(t)\|_2
 <2^{16}w_{\rm ref}(t)^2
                  \|e(t)\|_{\mathcal A_{\rho(t)+1/128}}.
 \tag{T.29}
$$

weak 源仍按 (T.23) 的全部两分量输入，尤其不删除 $\Phi_tF^t$。
若要恢复 bare Jacobi flux，需要另外支付
$W_\pm\widehat F^t|_{t_\pm}$ 的真实端点迹；内部 (T.24) 不授予这些迹。
对于支集严格离开目标端的源，该目标端项按其真实局部零值消失，而非一般
$L^2$ 源自动消失。

## 7. 在实际全网络中的准确权限

(T.18) 比绝对 DN 或 Cayley 差多支付了真正的跨端指数权。它可与相邻
负型段的完整 Airy/strict 两迹一起使用，并且 (T.19) 已保留全部层的
真实几何因子。另一方面，参考 cross 通常具有接近
$e^{-M\ell}$ 的衰减，本篇只反向加了 $e^{M\ell/2}$。
所以没有从 (T.18) 推出 $B_0^{-1}(B_a-B_0)$ 同宽有界。

完整 $F$ 的剩余步骤仍须在同一个 paired-port 空间中，利用这些实际
跨端块、对角 DN、负型全 Cauchy、两条 mean 和 source 行建立整个
允许 Cauchy 子空间及外边界 Schur 逆。参考内部标签 Green 的
$\mathcal X_{224}$ 单位也必须准确进入该空间；不能因本篇局部和很小就
跳过这个识别。实际 incoming 固定点的超小量已经可用，但不替代此算子门。

`scripts/fourfold_actual_positive_transmission_20261113.py` 与
`notes/2026-11-13-R119-actual-positive-transmission-budget.json`
核对全部实际光学门、变权强制性、完整 source 因子和全层求和预算。
