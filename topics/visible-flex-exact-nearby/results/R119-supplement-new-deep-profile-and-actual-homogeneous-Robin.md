# R119 续篇：固定深切换的新真实平尾、第四接线与重新证明的全模 Robin

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇明确构造一个新的径向目标族：前4096层
保留原 profile，更深层的背景比改成 $16\sqrt2$。新尾完整地
$C^2$ 接到平盘，三个主剪切面积不变；其每个非零四重模都有
真正的无限平尾线。第四线通过真实有限 connector 重新匹配，
双 bump 也按新全模右线重新选择。由此得到新实际齐次外 Robin，
并重新支付它与原 Robin 的差。

本篇不是把原 $\Gamma$ 或 R94 native 重命名。新全标签非线性图、
尾部普通源的完整 affine DN、相对网络逆和实际可用输入仍需
继续证明。末节显式保留新归一化的 $\delta_{4096}^{-3/2}$ 费用。

## 1. 新对象的准确逐层定义

固定
$$
 J_*=4096,\qquad b=9/2,\qquad C=2^b=16\sqrt2,
 \qquad \delta_j=\frac2{25}2^{-j},\qquad
 \eta_j=\frac{\delta_j^{3/2}}{4\sqrt2}.
 \tag{N.1}
$$
所有胞元位置、三个长 $\delta_j$ 的平台、四个长 $\eta_j$ 的
log-quintic 坡和两个长 $\eta_j$ 的端平台都保留原 R72 定义。
仍取 $dt=dy/\sqrt{12}$、$r=e^t\in[1,2]$。

令
$$
 c_j=\begin{cases}64,&j\le J_*,\\ C,&j>J_*,\end{cases}
 \qquad
 \mu_j=\begin{cases}
    \epsilon\delta_j^6,&j\le J_*,\\
    \epsilon\delta_{J_*}^{3/2}\delta_j^{9/2},&j>J_*.
 \end{cases}                                                \tag{N.2}
$$
每个胞元的五个平台现在准确是
$$
 1,\quad64/\delta_j,\quad\delta_j/(65/64),\quad1/\delta_j,
       \quad c_j.                                          \tag{N.3}
$$
相邻平台之间仍按同一个 $S(x)=10x^3-15x^4+6x^5$ 对 log 值插值。
在两下降坡内部仍可加入已规定的 bump $\gamma_{j,k}\psi_{j,k}$，
$|\gamma_{j,k}|\le2^{-16}$；定义新的实际背景
$$
 w^\dagger_\Gamma(r)=\mu_jp^\dagger_{j,\Gamma}(r)/r^7.
 \tag{N.4}
$$
新族以 $\dagger$ 标记，原族无该标记。它们在深层不是一个统一的
相对小扰动：因子 $(\delta_{J_*}/\delta_j)^{3/2}$ 可以增大。
后面使用的是新对象的直接证明。

准确的接缝恒等式是
$$
 \boxed{\quad c_j\mu_j=\mu_{j-1}.\quad}                    \tag{N.5}
$$
它也在 $j=J_*+1$ 成立。所有 log 过渡的端点一、二导数为0，
参数 bump 的完整二 jet 为0；因此 (N.5) 同时匹配
$w,w_r,w_{rr}$，而非仅匹配高度。$z_r=-w$ 由外端一次高度积分
恢复，平盘高度是输出，不额外固定。

## 2. 新的平坦性、型别及参考几何

最后一下降落差改为
$\Delta^\dagger_{j,2}=|\log\delta_j|-\log c_j$，第一下落仍为
$\log65+2|\log\delta_j|$。因为 $16<c_j\le64$，全部实际层上
仍有 $j/2<\Delta^\dagger<3(j+4)$。下降坡始终严格负型；
原参数 bump 支集的导数符号证明仍逐项成立。
两个上升坡和它们的真实型别零点准确不变。

记 $L_j=1+|\log\delta_j|$。直接对 (N.4) 微分，使用
$|S'|\le15/8$、$|S''|\le6$、$|\psi_x|\le96$、
$|\psi_{xx}|\le6144$，可统一取
$$
 |w|\le2^7\mu_j\delta_j^{-1},\qquad
 |w_r|\le2^{16}\mu_jL_j\delta_j^{-5/2},\qquad
 |w_{rr}|\le2^{27}\mu_jL_j^2\delta_j^{-4}.
 \tag{N.6}
$$
这些是整个真实 profile 的界，包含所有参数支集和接缝。
对 $j>J_*$，分别成为常数乘
$$
 \epsilon\delta_{J_*}^{3/2}\delta_j^{7/2},\qquad
 \epsilon\delta_{J_*}^{3/2}L_j\delta_j^{2},\qquad
 \epsilon\delta_{J_*}^{3/2}L_j^2\delta_j^{1/2}.
 \tag{N.7}
$$
三者都趋于0。因此把 $w$ 在极限圆内延成0，确实是 $C^2$ 的；
积分高度至少为 $C^2$，并有原平盘的完整零高度导数 jet。
整体等比缩放 $a=\rho r$ 只给有限的 $\rho^{-1},\rho^{-2}$ 因子，
不改变该极限结论。

同一微分还给任意两个参数序列在第 $j$ 层的差，至多为
$$
 2^{36}\mu_jL_j^2\delta_j^{-4}
        \max_k|\gamma_{j,k}-\widetilde\gamma_{j,k}|
 \tag{N.8}
$$
的二阶包络。深端仍是 $L_j^2\delta_j^{1/2}$，故参数的乘积拓扑
给新参考面的真实 $C^2$ 连续性。没有把原较快的 $\delta_j^2$
二阶衰减直接移用到这里。

正半径的旋转图和最终平盘仍是单值嵌入；参考高度按外端固定后
向内积分，故不会改变先前有限核心。新尾的全部点仍位于同一
径向薄环。曲率所需的是 $w/a$ 和 $w_a$，(N.6) 的深段最大值
发生在第一修改层：相邻上界比分别小于
$2^{-7/2}$ 与 $(1+1/L_j)2^{-2}<1$。
其在 $j=J_*+1$ 不超过原 $j=J_*$ 同型包络的两倍；相对于原浅层 $j=128$
的 $w_r$ 包络，其额外比至多
$8(L_{J_*+1}/L_{128})2^{-(7/2)(J_*-128)}<1$。
R69 的尾曲率证明用的较宽全层包络因而仍由未变的浅层端点控制；
原 $9375/131072<1/8$ 的几何严格余量保留。
这里的结论是新参考几何；尚未赋予任何非径向新解 reach。

## 3. 新实际线性方程、源和三个不变的主剪切

先固定一个 $\Gamma$，不使用尚未重建的非线性标签图。
物理 raw 高度变分为 $h$，令 $H=h/\rho$。对 $m\ne0$，
$$
 H_{tt}+(A^\dagger-1)H_t-m^2A^\dagger H=rwe_m,
 \quad A^\dagger=w_t/w.
$$
取同一准确 canonical 状态
$$
 \nu_m=\frac{m^2(m^2-1)}{12},\quad
 k_m=\frac{m^2-4}{\sqrt{12}},\quad
 W_1=\frac{\nu_mH}{r^4},\quad
 W_2=\frac{p_*^\dagger}{\sqrt{12}r^4}(H_t-m^2H).
 \tag{N.9}
$$
直接微分给完整含源方程
$$
 \boxed{\quad
 W_y=\begin{pmatrix}k_m&\nu_m/p_*^\dagger\\
                           -p_*^\dagger&-k_m\end{pmatrix}W
       +\begin{pmatrix}0\\
            \mu_j(p_*^\dagger)^2e_m/(12r^{10})\end{pmatrix}.
 \quad}                                                     \tag{N.10}
$$
这里保留了 $\mu_j$、两个真实 $p_*$ 因子及 $\rho$ 的高度单位；
不能将新源 norm 写成旧 $\epsilon\delta_j^6$。
mean 不使用 (N.9) 的 $\nu_0=0$，而是准确保留
$$
 p_{h,0}=(w/r)(H_t)_0,\qquad
 (p_{h,0})_t=\langle w^2e\rangle,\qquad
 (H_0)_t=(r/w)p_{h,0}.
 \tag{N.11}
$$
一个独立的整体高度常数仍必须携带。

三个长平台的下、上、下剪切面积依次为 $64,\alpha,1$，
$\alpha=65/64$，完全未改。真实端状态换到下一胞元时必须除
第二分量以 $c_j$。所以准确的理想端口矩阵为
$$
 B_{m,c}^{\infty}
 =\begin{pmatrix}1&0\\0&c^{-1}\end{pmatrix}
   \begin{pmatrix}1&0\\-1&1\end{pmatrix}
   \begin{pmatrix}1&\alpha\nu_m\\0&1\end{pmatrix}
   \begin{pmatrix}1&0\\-64&1\end{pmatrix}
 =\begin{pmatrix}
  1-64\alpha\nu_m&\alpha\nu_m\\
  (64\alpha\nu_m-65)/c&(1-\alpha\nu_m)/c
 \end{pmatrix}.
 \tag{N.12}
$$
其行列式是 $1/c$，不是旧的 $1/64$。
相应真全胞元矩阵 $B_{m,j,\Gamma}^\dagger$ 也准确有
$\det B_{m,j,\Gamma}^\dagger=1/c_j$，因为连续 $W$ 系统 trace 为0。

## 4. 真矩阵误差及每个模的无限平尾线

R72 的主平台在本对象上完全相同。六个短段在所有
$16\le c\le64$ 上仍满足 $\delta/2<p_*<64/\delta$；
最后两个短段的较精确面积只会把 $\eta/64$ 改为不超过
$\eta/16$。对全部短段直接积分 (N.10) 的 generator 给
$10m^4\sqrt\delta$ 的原上界。三个未改真平台的误差仍不超过
$5630m^8\delta$。将短段差插回其实际顺序，原因子
$66,4\nu_m,3$ 给 $15840m^8\sqrt\delta$；末端
$\operatorname{diag}(1,1/c)$ 的 norm 不超过1。因此在
$10m^4\sqrt\delta\le1$、$m^2\delta\le1$ 下，直接得到新对象的
$$
 \|B_{m,j,\Gamma}^\dagger-B_{m,c_j}^{\infty}\|_\infty
                     \le32768m^8\sqrt{\delta_j}.
 \tag{N.13}
$$
同一估计在 $|\gamma|<2^{-15}$ 的复参数盒成立：原逐点模长单调
证明仍适用新的下降落差，平台及端点值为同一固定实数。

对每个固定 $m\ge4$，取
$N(m)\ge\max(J_*+1,\lceil16\log_2(1+m)+120\rceil)$。
此后 (N.13) 小于 $2^{-35}$。由 (N.12) 直接看，在
$|s|\le1/8$ 上的真实 Mobius 图
$$
 T_{m,j}(s)=\frac{(B_{m,j}^\dagger)_{21}
                          +(B_{m,j}^\dagger)_{22}s}
                         {(B_{m,j}^\dagger)_{11}
                          +(B_{m,j}^\dagger)_{12}s}
 \tag{N.14}
$$
分母模长大于 $62\alpha\nu_m$，其像在 $|s|<1/12$，
导数模小于 $2^{-24}$。这同时使用真实行列式 $1/c_j$。
从任意更深截面给定该 disk 内方向再向外传播，得到每个固定浅
截面的唯一一致极限；其后通过有限个准确可逆胞元回到 cut128。
该线从未为0。

在 disk 内每次向外的第一分量倍率大于
$62\alpha\nu_m>2^{10}$，所以向深端高度幅度至少每层缩小
$2^{-10}$。每胞元内部的连续流可直接用
$\int p_*<66$、$\int p_*^{-1}<3$ 和有界 $k_m\ell_j$
给一个只依赖此固定 $m$ 的有限上界。
从 (N.9) 与真实高度方程恢复一、二径向导数，最多增加
$C_mL_j\delta_j^{-5/2}$，故所有高度二 jet 确实趋0。
取参考水平分量 $U=U^{\rm phys}/\rho$，按实际线性等距重建
$U=w(m^2H-rH_r)/(m^2-1)$、$U_r=wH_r$ 恢复，二 jet 同样趋0。
于是得到的是每一模真正的无限 $C^2$ 平尾线，而非有限截断的线。

本节尚未给一个统一的全标签/全源强 norm，不能据逐模存在
宣称任意 Sobolev 边界输入已经重建为整个外尾上的 $C^2$ 场。

## 5. 第四真线在旧前缀上的准确隔离

对 $m=4$，$\alpha\nu_4=325/16$，(N.12) 是
$$
 B_{4,c}^{\infty}=
 \begin{pmatrix}-1299&325/16\\1235/c&-309/(16c)\end{pmatrix}.
$$
全部 $j\ge129$ 的误差 $e_j=2^{31}\sqrt{\delta_j}<2^{-35}$。
在同一 $|s|\le1/8$ disk 上，分母大于1296，像实际上位于
$|s|<1/16$，且 $|T'|<2^{-24}$。故新、旧无限第四线都已由
实际收缩唯一确定，适用于整个参数盒。

对同一个原始参数序列 $\Gamma$ 比较两族。两者在
$129\le j\le J_*$ 的真实矩阵逐项相同；$s_{J_*}$ 均在
$1/16$ disk。因此有准确的完整深尾误差
$$
 |s_{128}^\dagger(\Gamma)-s_{128}(\Gamma)|
 <2^{-3-24(J_*-128)}=2^{-95235}.
$$
实际物理斜率仍按 cut128 的原单位换算，故
$$
 \boxed{\quad
 |d_4^\dagger(\Gamma)-d_4(\Gamma)|<2^{-95228},
             \qquad 14<d_4^\dagger(\Gamma)<15.
 \quad}                                                     \tag{N.15}
$$
原证明给出的距离14、15的有理余量远大于这个界。
本式比较的是同一个 $\Gamma$，不将将来两套 KAM 输出的参数
擅自视为相同。全纯依赖和距离复边界的 $2^{-16}$ 给相应参数
导数差界 $2^{-95212}$。

## 6. 重新确定有限 connector，保持实际尺度和全部 jets

以新真实 $d_4^\dagger$ 定义
$$
 R_*^\dagger=(1-d_4^\dagger)/(16-d_4^\dagger)\in(-14,-13/2).
$$
使用原实际准备段、$q=2,R=-1/2$ 放大段和最后两个固定短过渡，
仅按 [重调接线篇](R119-supplement-retuned-fourth-connector-and-common-bumps.md)
(C.10)--(C.12) 的真 Riccati 逆重新选择 $q=-1$ 主段停止长度。
这是真正同时命中尾方向与 $q=-8$ 的两 jet 接线。
由 $|dR_*/dd|<16$、$|d\ell/dR_*|<1/512$，
$$
 |\ell^\dagger(\Gamma)-\ell(\Gamma)|<2^{-95233}.
 \tag{N.16}
$$
$H_e\omega_e$ 在这个主段准确不变，所以
$$
 \epsilon_{\rm tail}^\dagger=\epsilon_{\rm tail},\qquad
 \rho^\dagger/\rho=e^{-(\ell^\dagger-\ell)}.
 \tag{N.17}
$$
前4096层的维度化 profile 保持原式；其物理整体缩放必须按
(N.17) 读取，不能在 fixed-$a$ 参数导数中删去该项。
所有 mean 高度移动切口项继续按真实高度积分保存。

## 7. 新全模输入重新选 bump，而后才定义新 Robin

重调后，真实第四线在 $u=T$ 再次准确为 $(1,-\omega)$。
双 bump 的第四保持曲线因而仍是同一个
$s=s(2^{-17}t)$。但其它模必须使用本篇新真实无限平尾线，经新
connector 回传，得到新的非零 $\Lambda_m^\dagger(T)$。
它们与 bump 参数无关，因为 bump 两端背景二 jet 准确保持。

逐项应用 R11 附录 A 的真实坏集证明，得到新的闭好集
$$
 G_\Gamma^\dagger=\left\{t\in[0,1]:
 |\sin\angle(\Lambda_m^\dagger(B;t),(1,\omega))|
                \ge2^{-39}\ \text{ 对全部 }m\in4\mathbb N\right\},
 \quad |G_\Gamma^\dagger|\ge1-83/16384.
 \tag{N.18}
$$
这里重新选择的是新尾的全部右线；没有沿用旧好参数。
仍只作逐点选择，不声称最小好参数随 $\Gamma$ 连续。
负帽可用同一反射参数。

长段 $0\le u\le B=2^{24}-25/8$ 及其入口
$a_*,z_*,\omega$ 严格未改。于是对新的真实齐次解
$$
 |c_+/c_-|\le2^{39}e^{-2m\omega B},\qquad
 |\lambda_m^\dagger+m\omega|
              \le2^{41}m\omega e^{-2m\omega B},\qquad
 \lambda_4^\dagger=-4\omega.
$$
真实 grounded 两迹仍是
$v=A_0y-4y'/m^2$、$p=-y+4y'/A_0$，
$A_0=4\omega+a_*^2/z_*$。因此本对象的新外部系数是
$$
 \gamma_m^\dagger
 =\frac{1-4\lambda_m^\dagger/A_0}
         {A_0-4\lambda_m^\dagger/m^2},\qquad m\ne0,
 \quad \gamma_0^\dagger=0.
 \tag{N.19}
$$
最后的 mean 行来自真实平移解和零 holonomy flux，不是把非零
公式形式上代入0。R74 (74.19)--(74.23) 的完整代数在相同的
实际入口上重新给出
$$
 \boxed{\quad
 m/7<\gamma_m^\dagger<m/5,\qquad
 \big\||D|^{-1/2}(\Gamma^\dagger-|D|/(4\omega))|D|^{-1/2}\big\|
                       <2^{-36}.
 \quad}                                                     \tag{N.20}
$$
所有四重模及负模共轭均在其中；这是从新无限真线重新证明的
齐次 DN，而非从旧 DN 连续性猜测所得。

还有更强的新旧比较。两者的准确稳定系数
$\gamma_m^{\rm st}=(1+4m\omega/A_0)/(A_0+4\omega/m)$ 完全相同，
各自真实误差均小于 $2^{42}m e^{-2m\omega B}$。所以
$$
 \boxed{\quad
 \big\||D|^{-1/2}(\Gamma^\dagger-\Gamma)|D|^{-1/2}\big\|
 <2^{43}e^{-8\omega B}.
 \quad}                                                     \tag{N.21}
$$
这里真实 $\omega>7/5$、$B=2^{24}-25/8$ 进一步给
$2^{43}e^{-8\omega B}<2^{-2^{27}}$，并非删除该差。
任意固定阶角平滑 norm 也可直接保留
$\sup_{m\ge4}2^{43}m^q e^{-2m\omega B}$。
两端高度/flux 矩阵和外端平均高度一起保留；长段普通 metric-source
仍必须带 R74 (74.16) 的两个 $J,R_m$ 端项。

## 8. 新有限帽闭边界实现可重新实例化，外尾重建另付

先在有限 Fourier 数据上用本篇真逐模外线定义
$\Gamma^\dagger$，再由 (N.20) 作闭延拓，得到自伴非负的阶1
边界算子，其常数槽准确为0。
同一个未改有限正帽的完整散度 form，加上这个真正的新边界
form，定义新的 coercive realization：root trace 与外 regular
mean 两行按原要求同时给定。非mean Robin 的正下界及原体能量
保持 coercivity，独立平均由两迹规范控制。

[完整正帽 Airy/contact 篇](R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md)
§4 的证明只用该真实 form、同一局部根图及其实际 height gradient、
一个在 collar 内消失的 root ramp，以及外端为纯常数的 regular
延拓。两种试验延拓的新增边界费用都为0。因此该证明可对
**新** $\Gamma^\dagger$ 重新实例化，其
$C_w<70.378782$、ordinary source 合同
$C_s<140.771775$ 和相应局部 contact 结论使用同一有限输入盒。
这不是旧 Poisson 算子与新算子相等的声明。

这个闭的有限帽实现不授予任意 Sobolev 迹在完整新外尾上的
$C^2$ 重建。额外新尾 ordinary sources 的 affine DN/contact
列也不在上述仅支持于 root collar 的源结论中。它们必须由
新全标签、完整 mean 和真实源空间继续证明。

## 9. 新归一化费用和必须继续完成的项目

保持原内部规范振幅 $\zeta_j=\epsilon\delta_j^{39/4}$ 时，
新的准确局部非线性比例为
$$
 \frac{\zeta_j}{\mu_j\delta_j^2}
 =\begin{cases}\delta_j^{7/4},&j\le J_*,\\
    \delta_{J_*}^{-3/2}\delta_j^{13/4},&j>J_*.
   \end{cases}
 \tag{N.22}
$$
它在切换处与旧阶相接，并没有免费降低实际输入。
尤其
$$
 2^{6144}<\delta_{J_*}^{-3/2}<2^{6150}.                      \tag{N.23}
$$
新深层多出的 $3/2$ 幂必须和这个完整全局因子一起计算。
若再支付原 $h_j^{-5}$，候选状态指数是
$\delta_{J_*}^{-3/2}\delta_j^{827/256}$，但本篇尚未以旧 chart
自动授予该新非线性界。

需要继续完成的是真实新全标签 Green 与 mean 图、全部普通/metric
源空间、有限旧前缀的条件数，以及从当前外入口经长段准确传播后
确能进入的标签球。即使未来的算术预算允许例如 $2^{-10000}$
的标签球，也不能仅选择一个抽象小球就称实际 regular 数据已入球。
同样，齐次 Robin (N.20) 不替代这些有源、高输入及全非线性问题。

[准确新对象与门程序](../scripts/fourfold_new_deep_profile_and_Robin_20261113.py)
及 [完整报告](../notes/2026-11-13-R119-new-deep-profile-and-Robin-budget.json)
记录接缝、真矩阵、第四无限深误差、完整物理源单位与新旧 DN 差。
