# R119 续篇：真射线耦合的全频 Airy 平衡、相关普通源与真实端口

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在前篇同一实际尾、同一 $\Gamma^*$、同一
宽角 KAM 图上，把完整射线生成元差送入一个明确的全频
Airy 两态平衡。全部内部负分量的扰动算子积分小于
$$
 \boxed{\quad 2^{-574}\overline X.\quad}                     \tag{B.1}
$$
普通 scalar Darboux source 的两个相关振幅一起变换后，具有
下面的真实 $L^2$ source 合同。两转向端完整高度/flux、
加权 mean 与独立高度常数均准确保留。

本结论保留完整参考 Airy 主项及 $\mathsf D_t$。
它没有证明该参考 Green 在最终 mixed-network 空间中的范数，
所以不从 (B.1) 单独推出完整高输入相对逆。

## 1. 固定原径向、实际宽域及明确的 Airy 尺度

依赖
[真射线振幅篇](R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md)
的全部实际对象。对 $i=(j,k)\in\mathcal I$，
$$
 q_0=\sqrt{-A_{\Gamma^0}},\quad
 S_0(t)=\int_{t_-}^tq_0,\quad
 s_*(t)=\min(S_0,L_0-S_0),
$$
$$
 \widehat\varepsilon_i
 =2^{80}(j+4)\delta_j^{443/256}e^{-640},\quad
 r_i=2^{22}
       \frac{\widehat\varepsilon_i}{\gamma_i^{\rm D}}\overline X,
 \quad \hbar_i=h_j/64.
 \tag{B.2}
$$
本篇仍使用同一 $64+3/8$ 真实角域，
$0\le s\le64+1/16$。扰动算子使用一次 $\hbar_i$，
ordinary-source 估计使用明确的 $2\hbar_i$。
所有分量上 $\sum_i2\hbar_i<24<64$；没有隐添角宽。

选择逐分量常数尺度
$$
 \varrho_i=\frac{32(j+4)}{\delta_j},\qquad
 \omega_m(t)=
   \left(q_0(t)^2+
          \varrho_i^2\langle m\rangle^{-2/3}\right)^{1/2},
 \quad \langle m\rangle=1+|m|,
$$
$$
 \mathsf D_m=
       \operatorname{diag}(\omega_m^{1/2},\omega_m^{-1/2}),
 \qquad m\in4\mathbb Z.
 \tag{B.3}
$$
$m=0$ 包含在内，独立常高度另行保存。
这是由实际层尺度给出的具体平衡，不是一个未指定的参数。
前篇的峰值界和真实 $\eta_j^2=\delta_j^3/32$ 给
$$
 q_{\max}<\varrho_i,\qquad
 \sup_{I_i}|A_{\Gamma^0,t}|
 <2^{13}(j+4)\delta_j^{-3}<\varrho_i^3.
 \tag{B.4}
$$
第二式使用 $|S''|\le6$、$|\psi_{xx}|\le6144$、
$|\Gamma_i^0|<2^{-19}$、各 log 跳幅小于 $3(j+4)$。
两个相邻胞元的较外尺度只使该上界改善。

## 2. 先回到共同参考角，完整参考项单列

前篇真实射线密度为 $Z_\sigma$。定义
$$
 \overline W_\sigma(t,\xi)
       =Z_\sigma(t,\xi+\sigma S_0(t)),\qquad \sigma=\pm1.
 \tag{B.5}
$$
这些只是各支的实际实平移，不混径向变量与角变量。
前篇参考部分的准确平移抵消后，完整方程变成
$$
 \overline W_t
 =\begin{pmatrix}q_0&0\\0&-q_0\end{pmatrix}
                          \overline W_\xi
   -\frac{g_0}{2}
       \begin{pmatrix}0&1\\1&0\end{pmatrix}\overline W
   +\mathcal E(t)\overline W+\overline F,
 \tag{B.6}
$$
其中 $g_0=A_{\Gamma^0}-1+q_{0,t}/q_0$，
$\overline F_\sigma=F_\sigma(t,\xi+\sigma S_0)$。
$\mathcal E$ 是前篇完整差算子按这两个平移共轭的结果；
平移是所有 Wiener 范数的等距算子，所以其已付宽差不变。

取同一当前物理尺度
$$
 \mu_0=\frac{w_{\Gamma^0}(t)}{\rho(\Gamma)e^t},
 \qquad \mathfrak k_0=\mu_0q_0,\qquad
 \mathsf O=\frac1{\sqrt2}
             \begin{pmatrix}1&1\\-1&1\end{pmatrix},
 \quad
 \mathsf D_q=\operatorname{diag}(\sqrt{q_0},q_0^{-1/2}).
$$
定义完整两态 $V_0=(z_0,v_0)^T$ 和平衡态 $Y$：
$$
 \overline W=\sqrt{\mu_0}\,\mathsf O\mathsf D_qV_0,
 \qquad Y=\mathsf D V_0.
 \tag{B.7}
$$
在开负型区这是准确可逆变换。径向参考项直接化为
$$
 (V_0)_t=
 \begin{pmatrix}0&1\\-A_{\Gamma^0}&0\end{pmatrix}
                    (V_0)_\xi+
 \begin{pmatrix}0&0\\0&1-A_{\Gamma^0}\end{pmatrix}V_0 .
 \tag{B.8}
$$
这里是 raw 高度梯度框架；不能把该零阶矩阵与相对
$(P,K)$ 框架的零阶矩阵直接互换。
完整平衡态方程因此为
$$
 Y_t=
 \left[
  \mathsf D_t\mathsf D^{-1}
  +\mathsf D\mathsf B_0\partial_\xi\mathsf D^{-1}
  +\operatorname{diag}(0,1-A_{\Gamma^0})
 \right]Y+\mathcal B(t)Y+\mathcal F,
 \tag{B.9}
$$
$$
 \mathcal B=
  \mathsf D\mathsf D_q^{-1}\mathsf O^T
        \mathcal E\,
                \mathsf O\mathsf D_q\mathsf D^{-1}.
 \tag{B.10}
$$
$\mathsf D_t$ 的所有高频转向项均在第一行保留。
本篇只估计最后的真实扰动和 source，绝不对第一行作一个
未证明的无权 Gronwall 断言。

## 3. 全频共轭费用：只出现一个实际 $q_0^{-1}$

对所有频率，
$$
 q_0\le\omega_m\le q_0+\varrho_i .
$$
所以 $\mathsf D\mathsf D_q^{-1}$ 及其逆作为 Wiener
Fourier 乘子，两者的 norm 均不超过
$(1+\varrho_i/q_0)^{1/2}$。
在两个分量的和范数或最大范数中，
$\|\mathsf O\|,\|\mathsf O^T\|\le\sqrt2$。因此
$$
 \boxed{\quad
 \|\mathcal B(t)\|_
       {\mathcal A_{s+\hbar_i}^2\to\mathcal A_s^2}
 \le2(1+\varrho_i/q_0(t))
      \|\mathcal E(t)\|_
       {\mathcal A_{s+\hbar_i}^2\to\mathcal A_s^2}.
 \quad}                                                    \tag{B.11}
$$
这是全部 $m$ 的同一个界，包括转向平衡中的
$\langle m\rangle^{\pm1/6}$；没有用有限频上界代替它。
需要支付的是 $\int\|\mathcal E\|/q_0$，下面直接计算。

## 4. 除以真实速度后的转向与坡肩积分

前篇已证明 $q_0$ 先不减、后不增。因此在峰值左侧
$S_0(t)\le q_0(t)(t-t_-)$，右侧相同地
$L_0-S_0(t)\le q_0(t)(t_+-t)$。全分量上准确有
$$
 s_*(t)/q_0(t)\le |I_i|<4\delta_j.                         \tag{B.12}
$$

更直接的准确分部积分同时支付所有转向和坡肩。
在峰值左侧，$q_{0,t}\ge0$、$s_*\le S_0$，并有
$$
 (S_0/q_0)_t=1-S_0q_{0,t}/q_0^2.
$$
从左端积分到峰值，因 $S_0/q_0\to0$ 于左端，得到
$\int q_{0,t}S_0/q_0^2\le$ 左段长度。
右侧令 $R_0=L_0-S_0$，则
$(R_0/q_0)_t=-1-R_0q_{0,t}/q_0^2$；从峰值积分到右端，
相同地得到
$\int |q_{0,t}|R_0/q_0^2\le$ 右段长度。
两式在平台 $q_{0,t}=0$ 处照常成立，故整个真实分量满足
$$
 \int_{I_i}|q_{0,t}/q_0|\,s_*/q_0\,dt\le |I_i|.
$$
连同 (B.12) 和已经支付的
$\int(1+|A_{\Gamma^0}|)<8(j+4)$，
$$
 \boxed{\quad
 \int_{I_i}|g_0|\frac{s_*}{q_0}\,dt
 <|I_i|[1+8(j+4)]
 <64(j+4)\delta_j .
 \quad}                                                    \tag{B.13}
$$
这覆盖整个真实下降坡肩，不要求 $q_{0,t}$ 点态很小。

另一方面，$g_\Gamma-g_0$ 仅支撑在参数 bump 内，
那里 $q_0>\sqrt{\Delta_i/\eta_j}$。
由前篇的完整径向振幅变化界，
$$
 \int\frac{|g_\Gamma-g_0|}{q_0}\,dt
 <64|\Delta\gamma_i|\sqrt{\eta_j/\Delta_i}
 \le2^{17}\widehat\varepsilon_i\overline X .
 \tag{B.14}
$$
最后，真实 $q/q_0\in(1/2,2)$，故
$$
 \frac{\|\mathcal R_\sigma\|}{q_0}
       \le32w^2(1+|A_\Gamma|)n.
$$
按前篇同一个完整积分和两个密度 pullback 的因子，
这一项的费用小于 $\widehat\varepsilon_i\overline X/16$。
因此保留前篇 (A.29) 的各项，而不是仅对其积分结果除以
一个不存在的 $q_{\min}$，得到
$$
 \boxed{\quad
 \int_{I_i}\frac{\|\mathcal E(t)\|}{q_0(t)}\,dt
 <
 \left[
  2^{18}\widehat\varepsilon_i
  +2^{43}(j+4)\delta_j
           \frac{\widehat\varepsilon_i}{\kappa_i h_j}
 \right]\overline X.
 \quad}                                                    \tag{B.15}
$$
两端原差为 $O(\sqrt s)$，所以除以 $q_0\asymp\sqrt s$
后仍有实际有限的算子上界。

## 5. 全部无限层的真正 Airy 费用

由 (B.11)、(B.15) 及
$2\varrho_i=2^6(j+4)\delta_j^{-1}$，
除前篇已经支付的 $2\int\|\mathcal E\|$ 外，新费用小于
$$
 \left[
  2^{24}(j+4)\delta_j^{-1}\widehat\varepsilon_i
  +2^{49}(j+4)^2
      \frac{\widehat\varepsilon_i}{\kappa_i h_j}
 \right]\overline X.
$$
使用同一真实 $\kappa_i$ 和 $h_j$ 下界，逐项包络为
$$
 2^{104}(j+4)^2\delta_j^{187/256}e^{-640},\qquad
 2^{161}(j+4)^3\sqrt j\,
                         \delta_j^{250/256}e^{-640}.
 \tag{B.16}
$$
在 $j=129$，两个值小于 $2^{-616}$ 和 $2^{-579}$。
其相邻比均小于 $3/4$，以后严格下降。
每层至多两分量，故
$$
 \sum_i\int_{I_i}\|\mathcal B\|dt
 <(2^{-651}+2^{-613}+2^{-576})\overline X
 <2^{-574}\overline X
$$
即严格得到 (B.1)。
这个结论使用全部 Fourier、完整无限求和和真实转向权。
在 $\|a\|_{\ell^1_{224}}\le1/8$ 上，同一全复域 Cauchy
还给完整一、二阶标签导数界
$$
 \|D\mathcal B\|_{\ell^1_iL^1_t}<2^{-571},\qquad
 \|D^2\mathcal B\|_{\ell^1_iL^1_t}<2^{-566}.
 \tag{B.17}
$$
它们包含联立度量与真角图的所有变化。

## 6. 两个相关源必须合起来再作 Airy 平衡

设
$$
 \Upsilon_\sigma(t,\xi)
       =\Theta_\sigma(t,\xi+\sigma S_0(t)),\qquad
 j_\sigma=(\Upsilon_\sigma)_\xi .
$$
则 $\overline F_\sigma=j_\sigma G\circ\Upsilon_\sigma$，
$G=\widehat s/\sqrt{2\mathfrak k}$。
两支确实来自同一个物理 scalar source；不能把它们换成
互不相关的输入。
准确相对角图为
$$
 C^\#=\Upsilon_-^{-1}\Upsilon_+
     =T_{S_0}C_+T_{S_0},\qquad
 \|C^\#-\mathrm{id}\|_{\mathcal A_{64+1/4}}\le r_i s_*.
$$
因此
$$
 \overline F_+=
       (C^\#)'\,\overline F_-\circ C^\#,\qquad
 \overline F_+-\overline F_-=
       (\mathcal P_{C^\#}-I)\overline F_-.
 \tag{B.18}
$$
其中 $\mathcal P_C f=C'f\circ C$ 是实际密度 pullback。
最终完整 KAM 匹配使 (B.18) 的差在两个端点同时消失。

前篇已经付清原物理 $e$ 经
$\chi^{-1}\circ\Theta_\sigma$ 的总角图。
增加上述参考实平移不耗宽；把每一支的公共复合放在一个
$\hbar_i$ 内，把 (B.18) 的差放在另一个 $\hbar_i$ 内，
可用原物理角上的 $\mathcal A_{s+2\hbar_i}$ source。
令
$$
 B_{\rm src}(t)=w(t)^{3/2}
                          \sqrt{a_{\rm phys}(t)/q(t)} .
$$
完整实际小球给
$$
 \|\overline F_\sigma\|_{\mathcal A_s}
       \le4B_{\rm src}\|e\|_{\mathcal A_{s+\hbar_i}},
$$
$$
 \|\overline F_+-\overline F_-\|_{\mathcal A_s}
       \le64\,\frac{r_i s_*}{\hbar_i}
                B_{\rm src}\|e\|_{\mathcal A_{s+2\hbar_i}}.
 \tag{B.19}
$$
这保留完整 source Jacobian、物理单位和 mean。

从 (B.7) 直接得到两个实际平衡源分量
$$
 \mathcal F_1=
   \omega_m^{1/2}
       \frac{\overline F_+-\overline F_-}{\sqrt{2\mu_0q_0}},
 \qquad
 \mathcal F_2=
   \omega_m^{-1/2}
       \sqrt{\frac{q_0}{2\mu_0}}\,
                     (\overline F_++\overline F_-).
 \tag{B.20}
$$
这里的 $\omega_m^{\pm1/2}$ 是完整 Fourier 乘子。
在整个分量上 $w/w_{\Gamma^0}$、$q/q_0$ 都在 $(1/2,2)$。
由 $\omega_m\le q_0+\varrho_i\le2\varrho_i$，
(B.12)、(B.19) 给
$$
 \|\mathcal F_1\|_{\mathcal A_s}
 \le2^{10}a_{\rm phys}w\,
       \frac{r_i\delta_j\sqrt{\varrho_i}}{\hbar_i}
                      \|e\|_{\mathcal A_{s+2\hbar_i}}.
 \tag{B.21}
$$
表面上的 $q_0^{-1}$ 已由真实双源差的 $s_*$ 消掉。

第二分量使用所有频率上的
$$
 \omega_m^{-1/2}\le
       \varrho_i^{-1/2}\langle m\rangle^{1/6},\qquad
 \sup_{m\in4\mathbb Z}
     \langle m\rangle^{1/6}e^{-\hbar_i|m|}
                 <2\hbar_i^{-1/6}.
$$
在另一份同样的实际余宽内，
$$
 \|\mathcal F_2\|_{\mathcal A_s}
 \le32a_{\rm phys}w\,
       \varrho_i^{-1/2}\hbar_i^{-1/6}
                       \|e\|_{\mathcal A_{s+2\hbar_i}}.
 \tag{B.22}
$$
两个证明各只用总共 $2\hbar_i$，不把宽差再相加一次。

实际全层预算进一步给
$$
 2^{10}(j+4)r_i\hbar_i^{-5/6}<2^{-593}<1 .
 \tag{B.23}
$$
它使 (B.21) 不大于 (B.22) 的右侧。
因此，使用两个分量的和范数，
$$
 \|\mathcal F(t)\|_{\mathcal A_s^2}
 \le64a_{\rm phys}w\,
       \varrho_i^{-1/2}\hbar_i^{-1/6}
                  \|e(t)\|_{\mathcal A_{s+2\hbar_i}}.
$$
代入实际 $a_{\rm phys}\le2\rho(\Gamma)$、
$w\le2^{11}\epsilon_{\rm tail}\delta_j^5$、
$\varrho_i^{-1/2}<\sqrt{\delta_j}$、
$\hbar_i^{-1/6}<4\delta_j^{-1/1536}$，得到
$$
 \boxed{\quad
 \|\mathcal F\|_{L^2_t\mathcal A_s^2}
 <2^{20}\epsilon_{\rm tail}\rho(\Gamma)
       \delta_j^{8447/1536}
            \|e\|_{L^2_t\mathcal A_{s+2\hbar_i}} .
 \quad}                                                    \tag{B.24}
$$
该式是真实 Airy 平衡中的 ordinary scalar source 合同，
不是把两个独立、可能不相合的振幅源套用同一个不成立的界。
一般 metric-source 的转换仍须保留其全部额外源行。

## 7. 两个真实转向端口及完整 mean

在左端 $\Upsilon_+=\Upsilon_-=k$；在右端，由完整 return
恒等式，同样有
$$
 \Upsilon_+(t_+,\xi)=\Upsilon_-(t_+,\xi)=:\Upsilon_+^e(\xi).
 \tag{B.25}
$$
两支的角 Jacobian 也准确相等，记共同值为 $j_e>0$。
端点邻域 $w_\Gamma=w_{\Gamma^0}$、$q=q_0$，
所以实际 $\mathfrak k=\mathfrak k_0/D$。
把真实 $W_\sigma$ 代回 (B.7)，得到准确有限端迹
$$
 z_0=\frac{j_e}{\sqrt D}\,z\circ\Upsilon^e,\qquad
 p_0:=\mu_0v_0
       =j_e\sqrt D\,p\circ\Upsilon^e .
 \tag{B.26}
$$
所有 $D$ 在同一端图中取值；两端各用自己的真实图。
这不是仅比较两个 principal DN 根。

若 $f$ 是原 raw 高度按完整物理端角图
$K_e=\chi_e^{-1}\circ\Upsilon^e$ 拉回的函数，
$P_e=K_e'(p_h\circ K_e)$ 是真实 raw flux 密度，则
$$
 \boxed{\quad f_\xi=\sqrt{D_e}\,z_0,\qquad
                    P_e=D_e^{-1/2}p_0.\quad}               \tag{B.27}
$$
从 $Y$ 恢复 $(z_0,v_0)$ 后，这组公式给全部真实端口。
完整相容及 holonomy 行是
$$
 \langle\sqrt{D_e}\,z_0\rangle=0,\qquad
 \langle D_e^{-1/2}p_0\rangle=\dot M.
 \tag{B.28}
$$
因为乘子是非恒定的，$z_0$ 自身的零模一般不为0。
故不能事先删除它，也不能把 $p_0$ 的零模当作完整 holonomy。
高度按
$$
 f=f_0+\partial_\xi^{-1}(\sqrt{D_e}\,z_0)
$$
恢复，保留独立平均高度 $f_0$。
原物理两迹再按真实 $K_e$ 反变换；原 grounded
normal/shear 与水平重建使用这些完整两迹。
若微分最终度量参数，前篇已经列出的尺度源、
平均高度移动切口项和所有坐标导数继续存在。

## 8. 到完整网络逆尚余哪一项

(B.1)、(B.17) 支付完整负型段的实际扰动在明确全频 Airy
两态中的费用；(B.24) 支付两个相关 ordinary 源的真实
转向权；(B.27)–(B.28) 把它们接回完整物理两迹和 mean。

下一项仍是对 (B.9) 第一行的同一真实径向参考，证明需要的
双端/端源 Green 范数，并将这些范数与相邻正型段的完整
$2\times2$ weak DN、最外有限 connector 和真实 regular
条件统一。特别要保留正型 DN 的两个 off-diagonal 反馈。
不能仅因 $\int\|\mathcal B\|$ 小，就跳过参考 Green 的
条件数；也不能将全部 ordinary-source 与 metric-source
合同彼此替代。

[全矩阵与实际无限层门程序](../scripts/fourfold_actual_Airy_ray_balance_20261113.py)
及
[完整报告](../notes/2026-11-13-R119-actual-Airy-ray-balance-budget.json)
记录本篇的可重跑输入与精确费用。
