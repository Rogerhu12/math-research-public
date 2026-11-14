# R119 续篇：真实径向负分量的全频 Cauchy、连续源及已付条件数

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对目前真正的 $\Gamma^0$ 径向尾，给出每个
完整内部负型分量上、任意两个内部截面之间的双向 Cauchy 界。
在真实密度 Airy 状态中，全部 $m\in4\mathbb Z$（包括0）满足
$$
 \boxed{\quad
 \|U_{0,m}(t,s)\|_{\ell^1(\mathbb C^2)}
 <2^{14}(j+4)\delta_j^{-1}\langle m\rangle^{5/3}.
 \quad}                                                     \tag{G.1}
$$
同时给出连续源的完整 Duhamel 界、普通物理源的实际权和独立 mean
高度/flux 两行。下面明确计算这个条件数对前篇扰动比较的费用：
现有粗界还不能支付整个原 profile 的无限相对逆。
这里没有把有限根 collar 的常数移用到当前双转向分量。

## 1. 原对象、状态及全部真实端点

沿用 [实际 Airy 平衡篇](R119-supplement-actual-Airy-balance-of-ray-coupling-and-sources.md)
的同一个参考 $\Gamma^0$、当前真实物理尺度 $\rho$ 和区间
$I_i=[t_-,t_+]$，$i=(j,k)$。写
$$
 q=q_0=\sqrt{-A_{\Gamma^0}},\qquad
 \ell_i=t_+-t_-,\qquad
 \mu_0=w_{\Gamma^0}/a_{\rm phys},\qquad M=\langle m\rangle=1+|m|.
 \tag{G.2}
$$
所有区间均取实际两个转向端；最外固定 cut 分量不是这里的双端
对象。保留的真实几何界为
$$
 \frac{\delta_j}{4}<\ell_i<4\delta_j,\qquad
 q_{\max}^2<256j\delta_j^{-3/2},\qquad
 q\text{ 先不减后不增},\qquad q(t_-)=q(t_+)=0.
 \tag{G.3}
$$
长度下界来自至少一个完整的 $\sqrt7$ 平台；其实际长度是
$\delta_j/\sqrt{12}$。上界及单峰性已经在射线篇 (A.22)--(A.23)
逐段证明，包含参数 bump、接缝和非转向陡坡肩。

原 raw 高度梯度参考状态 $V=(z,v)^T$ 满足
$$
 V_t=\begin{pmatrix}0&1\\q^2&0\end{pmatrix}V_\xi
       +\operatorname{diag}(0,1+q^2)V.
 \tag{G.4}
$$
原 Airy 乘子是
$$
 \varrho_i=32(j+4)/\delta_j,\qquad
 \omega_m=(q^2+\varrho_i^2M^{-2/3})^{1/2},\qquad
 Y=\operatorname{diag}(\omega_m^{1/2},\omega_m^{-1/2})V.
$$
本篇保留整个 $\mathsf D_t$，并采用明确的密度状态
$$
 X=\sqrt{\mu_0}\,Y.                                      \tag{G.5}
$$
两个时刻都用各自真实 $\mu_0,\omega_m$，不将它们冻结成一个
方便的常数。这个乘子在两个有限转向端均严格为正、有限。

## 2. 真正单调的密度和整个负段的有限变化

准确有
$$
 (\log\mu_0)_t=A_{\Gamma^0}-1=-1-q^2<0.
 \tag{G.6}
$$
所以不能用两次不相关的最大最小估计来计算它的变化。
每个负分量只有一个下降坡，其 log 落差仍是
$\Delta_{j,1}=\log65+2|\log\delta_j|$ 或
$\Delta_{j,2}=|\log\delta_j|-\log64$。参数 bump 的两端值为0，
故不改变该总落差。负区两端的上升小片段只减少密度的总下降；
胞元接缝处的 $64$ 与相邻层 $\delta^6$ 比例准确抵消。因此
$$
 \log\frac{\mu_0(t_-)}{\mu_0(t_+)}
 \le8\ell_i+\Delta_{j,k},\qquad
 \boxed{\quad\frac{\mu_0(t_-)}{\mu_0(t_+)}
                    <2^8\delta_j^{-2}.\quad}              \tag{G.7}
$$
这里 $e^{32\delta_j}<2$，$2\cdot65<2^8$。
从 (G.3) 还得到实际全层界
$$
 \ell_i q_{\max}<64\sqrt j\,\delta_j^{1/4}<1.
 \tag{G.8}
$$
最浅层可由 $4096\cdot129\,2^{-129/2}<1$ 核验，后续的
平方包络每层乘 $(j+1)2^{-1/2}/j<1$。
这不是说 $q_{\max}$ 本身小，而是同时使用了真实短径向长度。

## 3. 辅助正速度只用于能量证明

对每个频率定义
$$
 \sigma_m=(M\ell_i)^{-1},\qquad
 \Omega_m(t)=\sqrt{q(t)^2+\sigma_m^2},\qquad
 X^{\rm aux}_m=
   \sqrt{\mu_0}\operatorname{diag}(\Omega_m^{1/2},\Omega_m^{-1/2})V_m.
 \tag{G.9}
$$
这只是一套用来证明 (G.1) 的能量；没有用 $\Omega$ 替换实际 PDE
中的 $q$。直接微分 (G.4) 得到完整准确矩阵
$$
 (X^{\rm aux}_m)_t=
 \left[
 im\begin{pmatrix}0&\Omega_m\\q^2/\Omega_m&0\end{pmatrix}
 +\frac12\left(\frac{\mu_{0,t}}{\mu_0}
                +\frac{\Omega_{m,t}}{\Omega_m}\right)
                     \begin{pmatrix}1&0\\0&-1\end{pmatrix}
 \right]X^{\rm aux}_m.
 \tag{G.10}
$$
主项的 Hermitian 部分 norm 准确为
$$
 \frac{|m|}{2}\left(\Omega_m-\frac{q^2}{\Omega_m}\right)
 =\frac{|m|\sigma_m^2}{2\Omega_m}\le\frac1{2\ell_i}.
 \tag{G.11}
$$
所以双向传播的 Euclidean norm 均满足
$$
 \|U_m^{\rm aux}(t,s)\|_2
 \le\exp\left\{\frac12+rac12\int_I
   \left(\left|\frac{\mu_{0,t}}{\mu_0}\right|
        +\left|\frac{\Omega_{m,t}}{\Omega_m}\right|\right)dt\right\}.
 \tag{G.12}
$$
所有导数在实际各片上积分；$q^2$ 是 $C^1$，$\Omega_m$ 严格正，
故端点与仅 $C^2$ 的 profile 接缝无额外分布项。

$\Omega_m$ 与 $q$ 同样单峰，且两端均为 $\sigma_m$，所以
$$
 \exp\left(\frac12\int_I|\Omega_{m,t}/\Omega_m|dt\right)
 =\Omega_{m,\max}/\sigma_m
 \le1+M\ell_iq_{\max}<2M.
$$
将 (G.7) 代入 (G.12)，使用 $e^{1/2}<2$，得到
$$
 \boxed{\quad \|U_m^{\rm aux}(t,s)\|_2
                         <64\delta_j^{-1}M.\quad}         \tag{G.13}
$$
同一证明包含 $m=0$，而不是事后把非零模的除频率公式套到 mean。

## 4. 回到原真实 Airy 权：完整两端费用

由真实长度上下界，
$$
 1<8(j+4)<\varrho_i\ell_i<128(j+4).
$$
因此对每一个 $m$ 和每一个内部时刻，
$$
 1\le\frac{\omega_m}{\Omega_m}
 \le\varrho_i\ell_i M^{2/3}<128(j+4)M^{2/3}.
 \tag{G.14}
$$
令 $R_m=\operatorname{diag}(\sqrt{\omega_m/\Omega_m},
\sqrt{\Omega_m/\omega_m})$。$X_m=R_m X_m^{\rm aux}$，
$R_m$ 与其逆的 Euclidean norm 均不超过
$\sqrt{128(j+4)}M^{1/3}$。两个实际时刻都支付后，(G.13) 给
$2^{13}(j+4)\delta_j^{-1}M^{5/3}$。
从 Euclidean norm 转为两分量和 norm 再用因子2，即得 (G.1)。
没有省略一次端口框架或把一个单端 norm 当作双端条件数。

## 5. 全 Fourier Cauchy 和真正连续的 Duhamel 源

给定 $0<\hbar\le1$，所有频率满足
$$
 \sup_{m\in4\mathbb Z}M^{5/3}e^{-\hbar|m|}
                         <16\hbar^{-5/3}.
$$
故 (G.1) 在完整 Wiener 空间上成为
$$
 \mathcal K_i(\hbar)
 :=2^{18}(j+4)\delta_j^{-1}\hbar^{-5/3},\qquad
 \|U_0(t,s)\|_{\mathcal A_{r+\hbar}^2\to\mathcal A_r^2}
                   <\mathcal K_i(\hbar).
 \tag{G.15}
$$
若 $X_t=\mathcal L_0X+G$，则任意初始截面 $s\in I$ 有准确表示
$$
 X(t)=U_0(t,s)X(s)+\int_s^tU_0(t,\tau)G(\tau)d\tau.
 \tag{G.16}
$$
积分方向同时覆盖 $t<s$。其强 Fourier--径向 norm 满足
$$
 \sum_m e^{r|m|}\sup_{t\in I}|X_m(t)|_1
 <\mathcal K_i(\hbar)
       \left[\|X(s)\|_{\mathcal A_{r+\hbar}^2}
              +\int_I\|G(t)\|_{\mathcal A_{r+\hbar}^2}dt\right].
 \tag{G.17}
$$
证明先对每模取整个径向上确界，再求和；没有交换
$\sum\sup$ 与 $\sup\sum$。连续 $L^1$ 体源即可，亦可用
$\sqrt{\ell_i}$ 将 $L^2$ 体源代入。这个是完整有源 Cauchy 解，
不是只对齐次两列作有限谱试算。

## 6. 前篇实际成对普通源可直接消费

前篇已经在原物理角给出两支相关 ordinary scalar source 的
真实 Airy 向量 $\mathcal F$，其 norm 为
$$
 \|\mathcal F\|_{L^2_t\mathcal A_{r+\hbar_i}^2}
 <2^{20}\epsilon_{\rm tail}\rho\,
    \delta_j^{8447/1536}
             \|e\|_{L^2_t\mathcal A_{r+3\hbar_i}},
 \quad\hbar_i=h_j/64.
$$
本式只是前篇 (B.24) 的角宽向上平移一次 $\hbar_i$。
密度状态的真实源是 $G=\sqrt{\mu_0}\mathcal F$。
同一跨胞元实际界 $w_{\max}\le2^{11}\epsilon\delta_j^5$ 和
$a_{\rm phys}\ge\rho$ 给
$$
 \|G\|_{L^2_t\mathcal A_{r+\hbar_i}^2}
 <2^{26}\epsilon^{3/2}\rho^{1/2}\,
     \delta_j^{12287/1536}
                   \|e\|_{L^2_t\mathcal A_{r+3\hbar_i}}.
 \tag{G.18}
$$
于是零初值参考响应由 (G.17) 真正满足
$$
 \boxed{\quad
 \sum_m e^{r|m|}\sup_I|X_m|_1
 <2^{45}(j+4)\epsilon^{3/2}\rho^{1/2}
       \delta_j^{11519/1536}\hbar_i^{-5/3}
            \|e\|_{L^2_t\mathcal A_{r+3\hbar_i}}.
 \quad}                                                     \tag{G.19}
$$
全部两支源的相关性早已在 (B.18)--(B.24) 支付，不能把它们
重新拆成任意独立的 $q^{-1/2}$ 输入。实际 single-pass 的费用是
$\sum_i3\hbar_i<36<64$，仍在已证明的同一宽角域中。

这给的是参考算子消费真实 transformed source 的响应。
它不说只加入这个响应就已经解了实际扰动方程；实际
$\mathcal B X$ 仍是另一个必须处理的全算子源。
一般 metric-source 仍须先准确转换，不能用 scalar $e$ 合同代替。

## 7. 两个 mean 行、全部端口及物理恢复

在零非径向参考上，若 $V$ 确来自单值高度，则 $z_0=0$，
而 $p_0=\mu_0v_0$ 是独立通量。对于一般已给的参考体源
$F_V$，其 mean 方程准确为
$$
 (z_0)_t=(F_{V,1})_0,\qquad
 (p_0)_t=\mu_0(F_{V,2})_0=:s_0^{\rm ref}.
 \tag{G.20}
$$
在真正的参考 raw 高度方程中 $F_{V,1}=0$、$v=h_t$，
独立 mean 高度准确满足
$$
 h_0(t)=h_0(s)+\int_s^t\mu_0(\tau)^{-1}
       \left[p_0(s)+\int_s^\tau s_0^{\rm ref}(v)dv\right]d\tau.
 \tag{G.21}
$$
原实际全层界给
$$
 \int_I\mu_0^{-1}dt<2^{11}\frac\rho\epsilon\delta_j^{-6}.
 \tag{G.22}
$$
对于这个参考物理 scalar source，$s_0^{\rm ref}=\langle w_0^2e\rangle$；
零初始高度和通量时，(G.21) 进一步给
$\sup_I|h_0|<2^{34}\epsilon\rho\delta_j^{9/2}\|e\|_{L^2_t\mathcal A_0}$。
一般初始 mean 通量仍按 (G.21)--(G.22) 完整支付。
故该 mean 源行有明确有限的真实费用，不被非零模的
$\partial_\xi^{-1}$ 替代。常高度 $h_0(s)$ 必须一起保留。

作为一般比较框架，(G.1)--(G.17) 允许 $z_0$ 本身非零；
实际非径向 Airy 端口的相容性是加权的，而不是 $z_0=0$。
由 (G.5) 恢复 $Y$ 和 $(z,v)$ 后，真实端口仍完整采用
$$
 f_\xi=\sqrt{D_e}\,z_e,\qquad
 P_e=D_e^{-1/2}\mu_0v_e,\qquad
 \langle\sqrt{D_e}z_e\rangle=0,\qquad
 \langle P_e\rangle=\dot M.
 \tag{G.23}
$$
$(f_e)_0$ 独立保存，两个端点分别使用已构造的真实 $K_e$。
正型 [同端角 DN](R119-supplement-positive-DN-in-actual-Airy-endpoint-angles.md)
正好消费这些 $f_e,P_e$，并保留两个非对角反馈。
当前 $(z,v)$ 的参考 Cauchy 方程不允许将 (G.23) 的加权 mean
条件提前换成未加权投影。特别 $s_0^{\rm ref}$ 只有在真正的
参考物理 scalar 方程中才直接等于 $\langle w_0^2e\rangle$；
一般 transformed source 必须按 (G.20) 读取。

## 8. 相对共轭实际支付了什么，哪里仍然不闭合

在密度状态中实际扰动仍是同一个 $\mathcal B$，因为乘上的
$\sqrt{\mu_0(t)}$ 对角变量是常数。因此参考 interaction generator
$$
 \mathcal C(t)=U_0(t_-,t)\,\mathcal B(t)\,U_0(t,t_-)
$$
具有准确可消费的界
$$
 \int_I\|\mathcal C(t)\|_{
     \mathcal A_{r+3\hbar_i}^2\to\mathcal A_r^2}dt
 \le\mathcal K_i(\hbar_i)^2
      \int_I\|\mathcal B(t)\|_{
     \mathcal A_{r+2\hbar_i}^2\to\mathcal A_{r+\hbar_i}^2}dt.
 \tag{G.24}
$$
两个 Cauchy 方向和中间真实角复合各用一次宽差，不能删去任一项。
真实 $h_j$ 满足 $\hbar_i^{-1}<2^{10}\delta_j^{-1/256}$，故
$$
 \mathcal K_i(\hbar_i)^2
 <2^{70}(j+4)^2\delta_j^{-2-5/384}.
 \tag{G.25}
$$
前篇 (B.16) 的两个主要项是
$\delta_j^{187/256}$ 与 $\delta_j^{250/256}$。
乘上 (G.25) 后分别成为
$$
 \delta_j^{-985/768},\qquad \delta_j^{-199/192}.
 \tag{G.26}
$$
这个**具体充分估计**没有给出可和小量。它不是对实际逆不存在的
证明，也不抹掉前篇已经正确的生成元小界；它精确显示为什么尚
不能从那些小界直接推出全尾 Neumann 逆。

此外，(G.24) 是一次共轭的有宽差估计。即使将来其右侧可和，也
不自动授予任意多次重复都不耗宽的 Neumann 级数；实际全频传播或
完整网络 Green 仍须有自己的合法函数空间证明。

若今后明确重新构造极深 profile，使同一相对背景输入的层幂增加
$3/2$，这里只能作一个待消费的算术观察：两指数将变为
$167/768$ 与 $89/192$，均正。原 $\Gamma^0$ 和本 native
**没有**授予那个新 profile 的存在、source 或 complete-network
合同。该更改必须另行逐项证明并固定最终公共度量。

[准确能量与预算程序](../scripts/fourfold_reference_negative_Cauchy_condition_20261113.py)
和 [完整报告](../notes/2026-11-13-R119-reference-negative-Cauchy-condition-budget.json)
核验 (G.10) 的全部项、Hermitian 费用、当前全层常数及两个没有
被隐藏的相对指数。
