# R59：移动相位 frame 的复角模长门

2026-11-12，visible-exact-astra-f6a2。

**解析恒等式与充分条件已证明；数值适用范围以完成报告为准。**
本文改进 R56 的复角分母估计，保留实际无限 R33 primitive，使用
移动相位 frame 中的准确消去。环境丢失前的宽条带任务没有完成；
重建后的完整592-cell报告须重新生成并审查。有限 probe 不代替全域。

## 1. 准确 frame 与特征速度

对同一显式反射的 R33 图，令
\[
 T=cU+s e_z,\quad c=\cos\gamma,\quad s=\sin\gamma,\quad
 U=(\cos\phi,\sin\phi,0),\quad V=(-\sin\phi,\cos\phi,0),
 \quad\phi=\theta+\pi/2+\beta,
\]
并记
\[
 X=F_r,\quad F_\theta=aT,\quad
 P=1+\beta_\theta,\quad u=\gamma_\theta,\quad
 p=\beta_r,\quad q=\gamma_r,
\]
\[
 h=X\cdot U,\quad v=X\cdot V,\quad z=X_z,\quad
 Q=cz-sh,\quad R=ch+sz=X\cdot T.                         \tag{59.1}
\]
这里 Q 是 frame 投影，与 R58 的退化目标商 Q 不同。复角下点积
和叉积均为双线性解析运算，只有不等式中的向量模使用通常复欧氏范数。

原始二型与实际面积平方准确满足
\[
 n=-a^2D,\quad D=PcQ-uv,\qquad
 m=-a^2M,\quad M=pcQ-qv,\qquad
 G=a^2(Q^2+v^2).                                        \tag{59.2}
\]
因此在实双曲核心（选择实际径向 \(\sqrt{-K_0}\) 分支）
\[
 f_\sigma=-\frac mn-\sigma\sqrt{-K_0}\frac Gn
 =\frac{-M+\sigma\sqrt{-K_0}(Q^2+v^2)}{D}.               \tag{59.3}
\]
这里 G 是实际图的面积平方，不能换成目标度量的面积。求这个速度
不需要引入复面积平方根或复 \(\zeta\) 分支。独立控制盒本身只继承
分母与商的结论；共同 target 根来自 R57 的准确 affine 子族。

## 2. 消去后的角导数

由 \(X_\theta=a'T+aT_r\) 与 frame 求导，
\[
 Q_\theta=aq-Psv-uR,\quad R_\theta=a'+Pcv+uQ,\quad
 v_\theta=apc-Ph,\quad h_\theta=a'c-aqs+Pv.              \tag{59.4}
\]
设
\[
 A=P_\theta c-2Pus,\quad B=Pq-up,\quad C=P^2cs+u_\theta.
\]
则
\[
 D_\theta=AQ+acB-Cv,\quad
 D_{\theta\theta}=A_\theta Q+AQ_\theta
       +a(-suB+cB_\theta)-C_\theta v-Cv_\theta,          \tag{59.5}
\]
其中
\[
 A_\theta=P_{\theta\theta}c-3P_\theta us
           -2Pu_\theta s-2Pu^2c,
\quad B_\theta=P_\theta q+Pq_\theta-u_\theta p-up_\theta,
\]
\[
 C_\theta=2PP_\theta cs+P^2(c^2-s^2)u+u_{\theta\theta}.
\]
同理，设
\[
 A_M=p_\theta c-(pu+qP)s,\qquad C_M=pPcs+q_\theta.
\]
有
\[
 M_\theta=A_MQ+cBR-C_Mv,                                \tag{59.6}
\]
\[
 M_{\theta\theta}=(A_M)_\theta Q+A_MQ_\theta
      +(-suB+cB_\theta)R+cBR_\theta-(C_M)_\theta v-C_Mv_\theta,
\]
\[
 (A_M)_\theta=p_{\theta\theta}c
 -(2p_\theta u+pu_\theta+q_\theta P+qP_\theta)s
 -(pu+qP)uc,
\]
\[
 (C_M)_\theta=(p_\theta P+pP_\theta)cs+pP(c^2-s^2)u+q_{\theta\theta}.
\]
面积平方的一阶导数也保留抵消：
\[
 G_\theta=2a^2\{a(qQ+pcv)-R(uQ+Pcv)\},\qquad
 G_{\theta\theta}=2a^2\{Q_\theta^2+QQ_{\theta\theta}
                                  +v_\theta^2+vv_{\theta\theta}\}. \tag{59.7}
\]
这些式子仅用 \(c^2+s^2=1\)、\(h=cR-sQ\) 和 (59.4)。独立
`fourfold_phase_frame_algebra_check.py` 对11个多项式恒等式作准确
有理符号核对；本文同时给出可直接逐式求导的表达，不以数值检查代证。

## 3. 连续复条带的基础上界

固定实径向闭单元及其中所有实控制参数。将所有 phase 系数与其
径向导数用有向区间包住。对物理角 \(|\operatorname{Im}\theta|\le\sigma\)，
若频率 \(\omega_k=4k\)，令
\[
 I_\phi=\sigma+\sum_k|b_k|\sinh(\omega_k\sigma),\quad
 I_\gamma=\sum_k|g_k|\sinh(\omega_k\sigma),\quad
 \Gamma=\sum_k|g_k|\cosh(\omega_k\sigma).
\]
则
\[
 \|U\|,\|V\|\le e^{I_\phi},\quad
 |c|\le e^{I_\gamma}=C_0,\quad
 |s|\le\Gamma e^{I_\gamma}=S_0.                          \tag{59.8}
\]
所有 \(P,u,p,q\) 的任意所需角导数，用对应频率幂乘 cosh 权的
系数绝对和包络；P 的零阶另加1。

设实轴已有严格 \(\|X_h\|\le H\)、\(|X_z|\le Z_+\)、
\(X_z\ge Z_->0\)，且 \(a\le a_+\)、\(|a'|\le a'_+\)。则
\[
 H_1=e^{I_\phi}(a'_+C_0+a_+|p|C_0+a_+|q|S_0),\qquad
 Z_1=a'_+S_0+a_+|q|C_0,
\]
\[
 |h|,|v|\le (H+\sigma H_1)e^{I_\phi}=V_0,\qquad
 |z|\le Z_++\sigma Z_1.                                 \tag{59.9}
\]
这些来自沿竖直线积分准确 \(X_\theta\)，已包含 frame 自身的复增长。
把这些上界代入 (59.4)–(59.7)，每次乘加向外舍入，即得到连续
\(n,m,G\) 的零、一、二阶模长上界；不依赖复节点采样最小值。

## 4. 模长分母门

首先在条带的两条边界准确计算
\[
 \operatorname{Re}P(x\pm i\sigma)
 =1+\sum_k\omega_k b_k\cos(\omega_kx)\cosh(\omega_k\sigma).
                                                               \tag{59.10}
\]
使用区间 cosh 乘**带符号**的区间系数，不能把 cosh 只换成上端点
后忽略系数符号。等距实节点间的费用由
\(\sum_k\omega_k^2|b_k|\cosh(\omega_k\sigma)\) 乘半网格宽支付。
于是得到整个边界的 \(P_->0\)。由于 ReP 为周期条带上的调和函数，
最小值原理把同一下界延伸到内部。

若 \(c_-=1-\Gamma^2/2>0\)，则
\(\operatorname{Re}\cos\gamma=\cos(\operatorname{Re}\gamma)
\cosh(\operatorname{Im}\gamma)\ge c_-\)，因而 \(|c|\ge c_-\)。
准确式
\[
 z_{\theta\theta}=a'uc+aq_\theta c-aqus
\]
给连续上界 \(Z_2\)。实轴的一阶竖直 Taylor 项纯虚，故
\[
 \operatorname{Re}z\ge z_-:=Z_--\tfrac12\sigma^2Z_2.
\]
若 \(z_->0\)，则反三角不等式给
\[
 |Q|=|cz-sh|\ge c_-z_--S_0V_0=:Q_->0.                  \tag{59.11}
\]
这是 Q 的模长下界，不宣称 ReQ>0。再一次用反三角不等式，
\[
 |D|\ge P_-c_-Q_--|u|V_0=:D_->0,\qquad
 |n|\ge a_-^2D_->0.                                    \tag{59.12}
\]
这里 \(a_->0\) 已由同一实证书/区间 radius 供给。

也可独立保留 R56 型二阶实部门
\[
 \operatorname{Re}n(x+iy)\le n_{{\rm real},+}
                   +\tfrac12\sigma^2\|n_{\theta\theta}\|.
\]
两个证明给出的正模长下界可取较大者。新门通过时，旧实部上界仍
可能为正；不能把 (59.12) 改写成 Re n<0。

## 5. 特征系数二阶商界

若 \(|n|\ge d>0\)、\(|n'|\le n_1\)、\(|n''|\le n_2\)，而
\(|F^{(j)}|\le F_j\)，则
\[
 |F/n|\le F_0/d,
\quad |(F/n)'|\le F_1/d+F_0n_1/d^2,
\]
\[
 |(F/n)''|\le F_2/d+2F_1n_1/d^2+F_0n_2/d^2
                         +2F_0n_1^2/d^3.               \tag{59.13}
\]
分别取 F=m,G，得到 drift 与 wave factor 的二阶连续界。实际
\(\sqrt{-K_0}\) 及固定转向时间的径向缩放需另行乘入；二阶参数导数
还须 R58 与实际场链式项。保守界很大时须细分实际流管或使用更小
内条带的 Cauchy 界，不能仅因分母非零就推断 KAM 小量条件成立。

## 6. 实现、恢复与结论边界

验证器 `scripts/fourfold_phase_modulus_characteristic_strip.py` 使用
R57 已完成的592个闭径向单元及其无限 primitive 实界，重建同一
独立控制点盒；负半轴由显式反射得到。每个端点均按保存 binary64
的准确有理数解释，邻接相等及完整覆盖均检查。

恢复版每25单元原子保存带源/依赖/输入 hash 的报告；resume 必须
逐项匹配配置并保持已完成单元为有序前缀。`--indices` 只产生 probe，
其 `complete_radial_coverage=false`，不能用于全域结论。完整报告仅在
全部592个单元通过后设置 `proved_uniform_denominator_nonzero=true`。
超过1MB的纯数据使用gzip，不把实时未完成报告纳入冻结完成清单。

本定理只扩展实际场的复角系数域。真实返回域仍须 R60 的连续
残差/二阶管/全初值覆盖，完整 Wiener 残差与参数 KAM 仍须各自付款。
没有因此构造精确等距闭曲面或达到本题可见振幅与 reach 标准。
