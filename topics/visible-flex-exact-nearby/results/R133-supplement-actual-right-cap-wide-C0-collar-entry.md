# R133 续篇：实际右帽的宽 collar C0 门

2026-11-15，visible-exact / tail_connector。

**已证明的局部结论，供独立复核。** 本篇只消费已经成功的原 ordinary 源、weighted-Q、实际正帽存在性和真实换角结论。所有下列有限小数均按准确有理数使用；没有再次运行 target、旧 residual、Green、mean-flow 或 collar 科学程序。

结论是：在下面完整原输入域内，实际帽解与同一个 selected affine reference 的原 moving 两分量之差，在整个真实帽上满足
$$
 \|u_*-u_\delta\|_{L^\infty_{r,\phi}}
 +\|v_*-v_\delta\|_{L^\infty_{r,\phi}}
 <8.2297\,10^{-5}<10^{-4}.                         \tag{RC.1}
$$
因而，若该帽与另一段在 $r=9/10$ 是同一真实状态，本篇已经支付 WC 最宽 ordinary 表在右半 $[9/10,19/20]$ 上的 $C^0$ 球前提。左半、整 collar 的同态 $H^1$、五个窄 MA 高阶球、未知 body/cut 小量以及最终低 $\gamma$ 门不由本篇支付。

## 1. 同一帽、原输入域和全部均值

使用：

- [实际全模帽 X.1--X.12](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)；
- [加权端点定理 E.1--E.23](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md)；
- [实际 ordinary L1/端点报告](../notes/2026-11-15-R133-actual-cached-cap-L1-reference-endpoint.md)；
- [完整物理帽源与二次余项 A.5、A.17--A.19](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md)；
- [两输入零宽图 M.1--M.5、M.12](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)；
- [真实非线性 physical-to-moving 桥 RB.4--RB.24](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md)。

参考中心是原 ac1 候选的 440866 连续修补。固定原 $\eta_0$ 及帽上 intrinsic 数据，区间和空间为
$$
 I=[L,R]=[9/10,25/8],\qquad \sigma=1/8192,
$$
$$
 \|x\|_{X_\sigma}
 =\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_I|b_k|
  +\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_I|c_k|.
                                                               \tag{RC.2}
$$
这是两分量各自的 Fourier-joint 范数之和。不是先取每个 $r$ 的 pair 范数再取 supremum，也不是 ordinary 径向 $L^2$。

实际帽 $W_*=\widehat W+x=(B_*,C_*)$ 取原实反射类：$B_*$ 奇、$C_*$ 偶；输入为
$$
 \gamma=P_{\ne0,\theta}(C_*(L)-\widehat C(L)),\qquad
 \|\gamma\|_{A_\sigma}\le10^{-9},\qquad
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60}.                  \tag{RC.3}
$$
$f_B$ 是原归一非mean高度，物理高度为 $s_B f_B$；$s_B$ 不设为1。右端使用同一个真实 nonlinear long 曲率图。其 $C$ mean、holonomy mean 和独立 height 解释保持原样；左端 $C$ mean 是输出。$B$ mean 为0仅因为这里明确指定了共同反射类。

同一结论还适用于已发布 M 的实反射零宽子族：
$$
 \|\gamma\|_{A_0}<10^{-9},\qquad
 \|f_B\|_{\dot A^2_0}<2^{-60}.                        \tag{RC.3a}
$$
M.1--M.4 在这个完整 product 域直接重实例同一个 $X_0$ fixed point、$\rho,\zeta$、weighted $q_w$、ordinary 源和 true outer 常数；两个未知输入都未作复角平移。一般 full-parity 辅助族另有 $B$ mean 值 $2^{-80}$ 与导数 $2^{-49}$，但在本篇指定的实反射子族，真实 $B$ mean 准确为0，所以以下逐项值界不增加这两项。M.12 给这个实子族的真实 inverse angle 和完整均值。本文不以 $A_0$ 假设冒正角宽，也不扩到一般非反射输出。

由已经完成的 X 或相应 M 子族，
$$
 X:=\|x\|_{X_0}\le\rho,
 \qquad \rho=3\,10^{-6},
$$
$$
 Z:=\|c_{\ne0}(R)\|_{A_0}\le\zeta,\qquad
 \zeta=9.9\,10^{-10}.                                \tag{RC.4}
$$
本篇是在这个已经存在的同一个解上改进值界，不另求解一个帽，不把它扩大到尚未匹配的 core。

## 2. 不重复收费的完整值不等式

原实际 ordinary 源增益已经包含两行及真正的 ordinary mean：
$$
 \eta_{\rm ord}<3.038615335\,10^{-7}.                  \tag{RC.5}
$$
原 reference 的左 nonmean $C$、右 nonmean $d$ 增益分别小于3和10，右 $C$ mean 的增益不大于1。E.18 对 (RC.3) 同一个高度域内的已知端值给出
$$
 \|r_D\|_{A_0}<2\,10^{-15},\qquad
 |r_{C0}|<2.05\,10^{-19},\qquad r_{B0}=0.             \tag{RC.6}
$$
这些是准确外图在已知 $Z_0$ 和当前 $f_B$ 的值费用。高度没有被设为0；既然它已经在 (RC.6) 的统一域中，就不再次加入一个 Cauchy 导数费用。

因此包含内端 $\gamma$ 的全部 known load 满足准确有理比较
$$
 \eta
 <3.038615335\,10^{-7}
       +3\,10^{-9}+10(2\,10^{-15})+2.05\,10^{-19}
 <3.07\,10^{-7}.                                     \tag{RC.7}
$$

完整线性 Gauss 列来自原 physical joint 窗，
$$
 \max(\|Q_B\|_{\mathscr A_0},\|Q_C\|_{\mathscr A_0})
 <.051432066,\qquad K_G<16.                          \tag{RC.8}
$$
精确二次余项，包括分母和全部卷积 mean，满足
$\|\mathcal R_Q(x)\|<13X^2$。这是值估计；其导数的26不能误用来重复计算该项。

原真实 outer 的 nonmean 与 mean 导数在整个 $Z$ 域分别小于 $.006$ 和 $.00075$。只对右端变化 $c_{\ne0}(R)$ 积分它们，得
$$
 10(.006)Z+.00075Z\le.061Z.                            \tag{RC.9}
$$
其中两条 outer 输出都计入了主体；$C$ mean 没有并入 nonmean 端点。

于是同一实际 fixed point 满足
$$
 X<\eta+16(.051432066)X+208X^2+.061Z
   <3.07\,10^{-7}+.824X+.061Z.                       \tag{RC.10}
$$
最后一步仅使用已经成立的 $X\le\rho$，因为
$$
 16(.051432066)+208(3\,10^{-6})
       =.823537056<.824.                             \tag{RC.11}
$$
本式没有再乘原 closed-cap resolvent；这里每一列都只使用一次 unclosed reference 核。

## 3. 准确有理比较和完整右端域

由 (RC.4)、(RC.10)，
$$
 X<\frac{3.07\,10^{-7}+.061(9.9\,10^{-10})}{.176}
    <1.75\,10^{-6}.                                  \tag{RC.12}
$$
最后一个严格号是如下准确分数比较，而非新浮点计算：
$$
 \frac{176}{1000}\frac7{4000000}
 -\left(\frac{307}{10^9}
             +\frac{61}{1000}\frac{99}{10^{11}}\right)
       =\frac{93961}{10^{14}}>0.                     \tag{RC.13}
$$

右端不变域仍是原 X 的已经支付结论。为明确其反馈并未省略，实际 weighted 门
$q_w<3.561348304031\,10^{-6}<3.562\,10^{-6}$ 和 $K_e<5$ 还给
$$
 Z<3\,10^{-14}
      +3.562\,10^{-5}X+65X^2+\frac Z{200}
 \le3\,10^{-14}
      +(3.562\,10^{-5}+65\rho)X+\frac Z{200}.
                                                               \tag{RC.14}
$$
这里依次是 known ordinary/端数据、完整 linear $Q$、完整 quadratic $Q$ 和真正 nonlinear outer；最后的 $C$ mean 仍另在 (RC.9) 内。代入 (RC.12)，准确有理比较
$$
 .995(4.06\,10^{-10})
 -\left[3\,10^{-14}+.00023062(1.75\,10^{-6})\right]
       =3.55\,10^{-13}>0                             \tag{RC.15}
$$
证明 $Z<4.06\,10^{-10}$。本篇主结论只需较宽的原 $Z\le\zeta$，不把这个新值界当作一次新端点求解。

## 4. 与真实 selected reference 比较

令
$$
 Q_\delta=(u_\delta,v_\delta)=Q_0+\delta Z_{\rm can},
 \qquad |\delta|\le d=10^{-10},\qquad
 W_\delta=\Psi(Q_\delta).                            \tag{RC.16}
$$
$Z_{\rm can}$ 是原明确的连续修补方向，绝非把原 mean trial 换成 exact scalar-flow 后的另一方向。帽上的 $\nu$ bump 为0，故本比较中帽的 intrinsic 系数不随这条 selected 变化而改变；它没有断言 $Q_\delta$ 解 PDE。

RB.22--RB.23 已在真实有限32/96支撑、完整 mean 和同反射角规范下证明
$$
 \|B_\delta-\widehat B\|_{L^\infty(I\times\mathbb T)}
 +\|C_\delta-\widehat C\|_{L^\infty(I\times\mathbb T)}
 \le10|\delta|.                                      \tag{RC.17}
$$
该式是两个 global suprema 的和。没有将
$\sup_r(\|h_1(r)\|+\|h_2(r)\|)$ 与它互换。

令
$$
 H_B=\|B_*-B_\delta\|_{L^\infty(I\times\mathbb T)},\qquad
 H_C=\|C_*-C_\delta\|_{L^\infty(I\times\mathbb T)}.
$$
由 (RC.2)、(RC.12)、(RC.17)，
$$
 H_B+H_C<1.75\,10^{-6}+10d
             =1.751\,10^{-6}.                        \tag{RC.18}
$$
这个 affine 基点差被完整保留。

## 5. 真两角的 C0 比较，不损失测度因子

回到 RB.10--RB.16 的准确实角。记
$\Phi_i(\theta)=\theta+m_i I_\theta C_i$，
$m_i=1/\langle C_i\rangle_\theta$，$\Theta_i=\Phi_i^{-1}$。
同一个反射规范固定了积分常数。设 $h_C=C_*-C_\delta$，
$\mu=\langle h_C\rangle_\theta$，则
$$
 m_*-m_\delta=-m_*m_\delta\mu,\qquad
 \Phi_*-\Phi_\delta
       =m_* I_\theta(h_C-m_\delta\mu C_\delta).        \tag{RC.19}
$$
括号的 ordinary mean 准确为0。它包含完整 $\mu$ 项，没有以 nonmean 投影删去真实 mean 变化。

RB.4--RB.9 给 $|m_*|<7$、
$\|m_\delta C_\delta-1\|_\infty<1/31$、
$\Phi_\delta'\ge32/33$。这里 $I_\theta=\partial_\theta^{-1}P_{\ne0}$ 的 sawtooth 卷积在全部 $L^\infty$ 输入上有范数不大于 $\pi/8$。直接使用
$$
 I_\theta(h_C-m_\delta\mu C_\delta)
 =I_\theta h_C-\mu I_\theta(m_\delta C_\delta-1)
$$
及 $|\mu|\le H_C$，就得该 primitive 的上界
$(\pi/8)(32/31)H_C$；没有先用可能多出2的
$\|h_C-\mu\|_\infty$。再用已知 inverse lift 的下导数界，所以
$$
 \|\Theta_*-\Theta_\delta\|_\infty\le4H_C.              \tag{RC.20}
$$
这个比较只微分已知 inverse lift $\Phi_\delta$，不要求未知 $C_*$ 的角导数。

置 $F_i=(B_i/C_i,\,1/C_i)$。由
$|C_*|>1/7$、$|C_\delta|>1/6$、$|B_\delta|<1/128$，
同一个物理角中两个分量的 global supremum 之和满足
$$
 \|F_*-F_\delta\|_{\infty,\oplus_1}
      \le7H_B+43H_C.                                 \tag{RC.21}
$$
RB.7 和 RB.23 对已知 $F_\delta$ 还给
$\|\partial_\theta F_\delta\|_{\infty,\oplus_1}<1$。
使用真实恒等式
$$
 Q_*-Q_\delta
  =(F_*-F_\delta)\circ\Theta_*
     +F_\delta\circ\Theta_*-F_\delta\circ\Theta_\delta
$$
得到
$$
 \|Q_*-Q_\delta\|_{\infty,\oplus_1}
      \le7H_B+(43+4)H_C\le47(H_B+H_C).                 \tag{RC.22}
$$
supremum 在实圆上的组成无需 $L^2$ 换测度常数。RB 的 $8/5$ 测度费属于 ordinary $L^2$ 版本；本式没有将 ordinary $L^2$ 免费提升到 $C^0$，而是直接从已成 $X_0$ 与 (RC.17) 的 global suprema 出发。

由 (RC.18)，最终的准确有理比较为
$$
 47\,\frac{1751}{10^9}
     =\frac{82297}{10^9}
     =8.2297\,10^{-5}<10^{-4},                        \tag{RC.23}
$$
即 (RC.1)。

## 6. 对 WC/WA 的准确转授范围

[宽 collar 定理 WC](R133-supplement-wide-collar-half-trace-and-independent-narrow-high-domain.md)
和[实际六表 WA](R133-supplement-actual-wide-collar-mean-and-six-ordinary-half-trace-tables.md)
采用同一个 $Q_\delta$、原 moving 角、真实 $dr$，其最宽表为
$\rho_w=10^{-4}$。因此对本篇实际帽在
$I_+=[9/10,19/20]$ 的 restriction，右侧的 raw pair $C^0$ 小球前提已经成立。

这没有支付以下不同条件：

- $I_-=[17/20,9/10]$ 上的同一个真实 core 状态及其宽球；
- 跨 $r=9/10$ 的完整同态匹配及整 collar $H^1$；
- 同一个 cut 上 MA 五个窄球之一的 $H^{8193}$ 前提；
- WA.17 的 finite193 cut、左/右 ordinary body 和 high-body 三量；
- WC/WA 的低 $\gamma$ 自映像、全部 core 逆或全局闭合。

尤其不能从 (RC.1) 把右侧普通 $L^2$ body 填成0，不能从 $\gamma$ 小把实际 $B(L),C_0(L)$ 基点差删掉，也不能把本结论称为窄 MA 球已经成立。后续 receiver 消费仍需保完整 ordinary 源、未知 $Q$、真实 outer 和独立 mean。
