# R133 续篇：原全实参数区间的固定端口帽主体 Sobolev 逆

2026-11-15，visible-exact-astra-0df9。

**已证明下列固定端口转授。** 本篇把 [V1–14](R133-supplement-complete-real-delta-fixed-base-cap-linear-inverse.md) 的实际主体小量转到 $-3/2\le s\le2114$。整个原实区间 $|\delta|\le10^{-8}$、同一修补中心和方向、同一固定 $\eta_0$ 不变。帽内 $\nu$ bump 仍恒零。

本篇的外端线性行固定为原 $\delta=0$ 的完整真实 long 行；内端仍为固定 $D\Psi_0$ 的非mean $C$ 行。V 已另证真实改变外行的 $s=0$ 结果，但它的高阶转授不能凭本篇自动取得。这里先支付完整主体和基逆的 Sobolev 模块，保留真实改变外行的独立入口。

## 1. 原物理模块与不变的基逆

使用 [S1–24](R133-supplement-shifted-Sobolev-complete-gauge-Hessian-and-cap-tail-Schur.md) 的同一模块
$$
 \|x\|_{\mathfrak M_s}
 =\left(\sum_{n\in4\mathbb Z}\langle n\rangle^{2s}
                    \sup_I|x_{B,n}|^2\right)^{1/2}
 +\left(\sum_{n\in4\mathbb Z}\langle n\rangle^{2s}
                    \sup_I|x_{C,n}|^2\right)^{1/2},
 \quad I=[9/10,25/8].
 \tag{W.1}
$$
原 one-sided 迹、jump、两条 curvature mean 和物理源单位全部保留。
ordinary 源用 $L^2_rH^s$；angular-divergence 的势用
$\mathfrak M_s$；独立端荷及 jump 使用原完整 $H^s$ 范数。
不将 $\ell^2\sup_r$ 改成 $\sup_r\ell^2$。

记 $G$ 为 S.2 的完整物理基逆，含真正 $B_0$ 图和完整
Robin/$C_0$ 行。记
$$
 K=G H_{R_0},\qquad \mathcal G_0=(I-K)^{-1}G .
 \tag{W.2}
$$
这里 $H_{R_0}$ 是原非解连续中心的完整 residual Hessian。
S.3 已给 $\|K\|_{\mathfrak M_0}<1/64$。
$\mathcal G_0$ 正是原固定规范方程的基逆，而非删除 residual 后的物理逆。

全部角翻译先在完整 $4\mathbb Z$ 模块定义。P.11–P.14 的
Jacobian 差公式也作用完整两分量，不插入反射投影。
在实际奇/偶子空间上，由原反射不变性和唯一性，最后的解就是原
moving 方程的解。这样既不把反射投影当解析 lag 算子，也不将一般
all-$4\mathbb Z$ 原 moving 相位行免费删掉。

## 2. 先把完整基逆的复角域收窄

S.4、S.12 已付下列原解析算子族：
$$
 \sigma=2^{-7},\qquad
 \sup_{|\operatorname{Im}z|\le\sigma}\|K_z\|<2^{64},
 \qquad K_z=C_zKC_{-z},
 \tag{W.3}
$$
且完整物理 $G_z$ 的 ordinary/divergence 列小于 $2^{10}$。
真实独立 mean、Robin、内端和 jump 的基点 lift 也在同一个原
完整正核与边界反演中。L.4–L.7 的未闭列小于16、复反馈逆小于10；
即使合计全部独立列，可统一放宽到 $2^{14}$。
见 [完整物理帽—尾篇](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)。
其原 $f_B|D|^{-2}$ 列亦由 L.6–L.8 支付。

(W.3) 的大界本身不许可复 Neumann 反演。取
$$
                  \sigma_*=2^{-128}.
 \tag{W.4}
$$
S.13 的完整 lag 分解 $K=\sum_\ell K_\ell$ 给
$\|K_\ell\|\le2^{64}e^{-\sigma|\ell|}$。
对实 $a$ 和 $|b|\le\sigma_*$，
$$
 \|K_{a+ib}-K_a\|
 \le2^{64}\sum_\ell e^{-\sigma|\ell|}
                         (e^{|b||\ell|}-1)
 \le {8\,2^{64}|b|\over\sigma^2}\le2^{-47}.
 \tag{W.5}
$$
最后一步只用指数为整数的二进制比较。真实平移 $C_a$ 等距，
所以 $\|K_a\|<1/64$。因而
$$
 \sup_{|\operatorname{Im}z|\le\sigma_*}\|K_z\|<1/32,\qquad
 \sup\|(I-K_z)^{-1}\|<2 .
 \tag{W.6}
$$
得到同一完整基逆的真正有界解析族
$$
 \mathcal G_{0,z}=(I-K_z)^{-1}G_z .
 \tag{W.7}
$$
所有上述独立列可安全统一取界 $2^{16}$。这一界由原源列、真实
mean 行和 W.6 得到，不对源的未知 Fourier 支持作任何限制。

## 3. 完整实际方向在固定复角的联合界

V.2 已实际验证
$$
 \|Z\|_{\mathscr A_{1/64},\mathrm{pair}}<.898277121481<1.
$$
原规范系数表和 S.5 给
$\|\Phi_0-\mathrm{id}\|_{\mathscr A_{1/64}}<1/256$。
对 $\sigma_1=1/128$，按 V.7 相同的逐系数指数级数，
$$
 \|Z\circ\Phi_0\|_{\mathscr A_{\sigma_1},\mathrm{pair}}
 \le\|Z\|_{\mathscr A_{\sigma_1+
                  \|\Phi_0-\mathrm{id}\|_{\mathscr A_{\sigma_1}}}}
 \le\|Z\|_{\mathscr A_{1/64},\mathrm{pair}}<1 .
 \tag{W.8}
$$
这里 $\sigma_1+1/256<1/64$，仍有严格余宽。
$\mathscr A$ 始终是逐 Fourier 系数先取全帽径向 supremum 的范数。
所有真 mean 与组合后产生的无限模保留。

写 $Y=\delta Z$，帽号固定为与原 $\Phi_0$ 复合。于是
$$
 \|\widehat Y\|_{\mathscr A_{\sigma_1},\mathrm{pair}}
      <10^{-8}<1 .
 \tag{W.9}
$$
这是一条已给系数的联合解析界，并不要求未知解角解析。

## 4. 主体反馈的有界解析族

使用 [P1–21](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md)
完整 $\Pi_0,\mathcal I_0,\mathcal H,M,P,E$ 和
$a_Y,b_Y$，其有序关系为
$$
 \mathcal V_Yx
 =\partial_\theta\{M\widehat{a_Y(\mathcal Hx)}\}
       +W_\theta\langle C\widehat{a_Y(\mathcal Hx)}_2\rangle
       +P\widehat{b_Y(\mathcal Hx)}
       -W_\theta E_{b_Y(\mathcal Hx)} .
 \tag{W.10}
$$
全部 primitive 与 mean 均保持其准确加权常数。

在宽 $\sigma_1$ 的共同已付系数域，S.5、S.9 和 V.3 允许粗取
$$
 \|\widehat Q_0\|_{\rm pair}<16,\quad
 \|C\|,\|B\|,\|W_\theta\|<1,\quad |m|<8,\quad |m|^{-1}<1/3,
$$
$$
 \|\Pi_0\|<8,\quad \|\mathcal I_0\|<2^8,\quad
 \|\mathcal H\|<2^{13},\quad \|P\|<2,\quad \|M\|<1,\quad
 \|E_f\|<4\|\widehat f\|,\quad b_*,g_*<8,\quad k_*=1 .
 \tag{W.11}
$$
例如 $\mathcal I_0$ 的原有序式给
$8(1+8)^2/4<2^8$；$E_f$ 给 $(1+8)/4<4$。
平移不改变 radial scalar $m,\beta,\gamma,K$。

逐项代入 P.12–P.13 的四个 primitive 项及全部 mean 项，
用 $\|\widehat Y\|<1$ 吸收二次项，可统一取
$$
 \|\widehat{a_Y(\mathcal Hx)}\|,
 \ \|\widehat{b_Y(\mathcal Hx)}\|
      <2^{34}\|\widehat Y\|_{\mathscr A_{\sigma_1}}\|x\|_{\mathfrak M_0}.
 \tag{W.12}
$$
其费用可直接检查：四个 primitive 项在乘 $\beta$ 之前合计小于
$2^{15}\|\widehat Y\|\|\widehat h\|$，gamma 项小于
$2^7\|\widehat Y\|\|\widehat h\|$；
ordinary mean 项小于 $2^{13}\|\widehat Y\|\|\widehat h\|$。
再使用 $\|\widehat h\|<2^{13}\|x\|$ 即得 W.12。
没有增加未知的角导数或径向导数。

W.10 的 divergence 势界小于 $2^{34}\|\widehat Y\|$；
ordinary 模块界小于 $2^{37}\|\widehat Y\|$。
转换到 $L^2_rL^2_\theta$ 再付 $\sqrt{|I|}<2$。
故由 W.7 的 $2^{16}$，在窄共同 strip 上
$$
 T_{\delta,z}=\mathcal G_{0,z}\mathcal V_{\delta Z,z},
 \qquad
 \sup_{|\operatorname{Im}z|\le\sigma_*}\|T_{\delta,z}\|<2^{64}.
 \tag{W.13}
$$
这是完整算子族；不以逐个矩阵 entry 代替算子界。
它的系数平移给出 $T_{\delta,z}=C_zT_\delta C_{-z}$。
其真实未平移值继续使用 V.11 的更小界
$$
                         \|T_\delta\|<1/4.
 \tag{W.14}
$$
不将 W.13 的大界代入真实反馈门。

## 5. 同一大尺度权给全部有限角阶

取准确固定尺度
$$
 M=2^{1024},\qquad W_{s,M}(n)=(1+n^2/M^2)^{s/2},
              \qquad -3/2\le s\le2114 .
$$
此时 $\tau=|s|/(2M)<2^{-1013}$。
S.15 的完整 operator-valued lag lemma 直接给
$$
 \|W_{s,M}T_\delta W_{s,M}^{-1}-T_\delta\|
 <8\,2^{64}2^{-1013}2^{256}
 =2^{-690}<2^{-600}.
 \tag{W.15}
$$
于是
$$
 \|W_{s,M}T_\delta W_{s,M}^{-1}\|<1/3,\qquad
 \|(I-W_{s,M}T_\delta W_{s,M}^{-1})^{-1}\|<2 .
 \tag{W.16}
$$
没有频率截断；mean 的权准确为1。

对每条 W.7 已付输入列，lag 平移和同样的权商给
$$
 \|W_{s,M}\mathcal G_0 W_{s,M}^{-1}\|
 \le2^{16}\sum_{\ell\in4\mathbb Z}
                    e^{-(\sigma_*-\tau)|\ell|}
 <2^{147}.
 \tag{W.17}
$$
这里 harmless 地求和所有整数，并用
$1+2/(e^{\sigma_*/2}-1)<2^{131}$。
输入和输出各保自己的 radial norm；只变共同 angular weight。
$f_B$ 列先正规化为 $\mathcal G_{0,f}\Lambda^{-2}$，
所以原输入多两角导的单位不被删除。

因此固定原真实端口的完整帽主体逆
$$
                   \mathcal G_{\mathrm{body},\delta}
                      =(I-T_\delta)^{-1}\mathcal G_0
 \tag{W.18}
$$
在 shifted 模块中，各声明输入列的 norm 小于 $2^{148}$。
回通常 Sobolev 权只需总因子 $M^{|s|}$，不是它的平方。
由于 $1024\cdot2114+148<2200000$，得到一个统一安全界
$$
 \|\mathcal G_{\mathrm{body},\delta}\|_{\mathfrak D_s\to\mathfrak M_s}
                          <2^{2200000},
           \qquad -3/2\le s\le2114,\quad |\delta|\le10^{-8}.
 \tag{W.19}
$$
$\mathfrak D_s$ 表示本篇逐条列出的原 ordinary、divergence势、
端荷和 jump 源范数之和；$f_B$ 使用原 $H^{s+2}$ 入口。
mean 兼容荷和唯一 height gauge 按原合同保留，不能把不兼容源
自动解释为真实闭方程解。

## 6. 量词与尚缺的真实变动外行

W.19 在固定 $D\Psi_0$ 物理模块中成立。按原 S.6 的实际固定半径
链式法则可另付 moving $H^s$ 的读出费用，但本篇不交换一个
未证明的 moving $\ell^2\sup_r$ 角复合。

未知反射变分的完整原 moving 主体已由上述不变子空间继承。
一般 all-$4\mathbb Z$ 的标量角相位仍按 G 的原方程单独恢复；
径向 $\Gamma^*$ 亦非这个相位。

将 W.19 用到 V 的真正改变外端，尚须证明那些准确 frozen
外行在相同窄 strip 上有有界解析族，或者给等价完整有限角估计。
单独的复背景界、自然物理角的 long 导数或裸角复合都不能冒作
这个新入口。所需外行还包括独立 mean、真正 $B_0$、仿射源和
$f_B$ 的原两角导单位。

本篇是原全实参数区间的完整帽主体高/负阶子项，不是内主体
全逆、精细 $\nu$ 响应、非线性状态球或最终几何族。
全部原成功数值只作为已付常数消费，没有新增数值计算。
