# CFC：原 TC96 的完整目标列与物理有限接口

日期：2026-11-28。责任会话：`visible-exact-astra-b0d5a16-20261128`。

本篇给出新的整批有符号列计算及其实际 owner，不把已完成的有限观测矩阵
当作全空间列。实际准入必须先有完整 TC 三目标、SC 三目标及其完整
58/224/32 正侧链、BFP19/DCP18、AP96、H96 七目标和 PWA96 七目标。任何旧 partial
prefix 均不满足这些条件。本篇写作时这些前置项并未全部实际成功，故不
登记 CFC 数值结果或完整 Schur 成功。

源文件为 [整批数学](../scripts/fourfold_codazzi_complete_finite_columns_math.py)、
[原载体恢复](../scripts/fourfold_codazzi_complete_finite_columns_carriers.py)、
[实际 owner](../scripts/fourfold_codazzi_complete_finite_columns_owner.py)。

## 1. 同一原列、完整误差和确切缺列

固定 [TC](R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md)
的原 96 个精确二进制试探列及同一个 selected 背景。原坐标是物理
root-even96 正交坐标；它们不是目标侧真实 $a=2H(0)$ 基底中的前96个
Fourier 坐标。对原第 $j$ 列，记 $Y_j^a$ 为试探腰 density，$Y_j$ 为
完整正侧原物理逆和负侧延拓给出的真 PDE 腰 density。完整 density
包含两条 primitive 和两条存储 mean。

[SC/JF](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md)
的实际 producer 在完整 P224 和全部五种残差列后计算

\[
 d_j=\sum_{k\in\{1,2,7\}}P_{k,\mathrm{low\_root97}}F_{k,j},\qquad
 z_j=\sum_{k\in\{1,2,7\}}P_{k,\mathrm{high\_root\_mixed}}F_{k,j},
 \qquad e_j=(d_j^2+z_j^2)^{1/2}.                       \tag{CFC.1}
\]

这里 $k=1,2,7$ 分别为完整 high collar、high body 和 raw low 源。
P224 已在原物理单位中包含全部 receiver；不另乘9，也不把高返回留空。
令 $F_{-,j},F_{\mathrm{st},j}$ 是原完整 negative root/strict 残差。
原 producer 随后保存

\[
 D_j=\operatorname{up}\bigl(
 C_R^{\rm used}e_j+C_O^{\rm used}F_{-,j}
                  +C_2^{\rm used}F_{\mathrm{st},j}\bigr),
 \qquad \|Y_j-Y_j^a\|_{\mathcal Y}\le D_j.           \tag{CFC.2}
\]

这项分解可在原
`fourfold_codazzi_joint_signed_finite_trial_error_math.py` 的
`complete_TC_column_errors` 和 SC owner 的首次调用、保存路径逐项检查。
原 SC 公共 `columns` 对象只保存全部 $D_j$ 及原完整
`original_received_gains`；内部计算的 $d_j,z_j,e_j$ 没有另作公共记录。
P224 只给完整单位 receiver 表，没有第 $j$ 列的另一个已保存 $e_j$。

若只能消费原字段，令 $\gamma_R>0$ 为原 **固定数值配权记录**
$C_R$ 的严格 lower endpoint。SC 使用的是该相同记录的 upper endpoint，
所以 $0<\gamma_R\le C_R^{\rm used}$，而 (CFC.2) 各项非负。于是

\[
 \|\text{原真 root correction}_j\|\le e_j
              \le D_j/\gamma_R.                     \tag{CFC.3}
\]

这是已保存正表达式的数值后果，不是从一个未知算子范数的 upper 倒推
其输入大小。owner 绑定原完整 SC 数学源码、实际执行和全部原配权记录。
它不再调用旧 SC target。首次 SC 科学执行尚未发生时，已加入
[同一次原计算被动保全全部 root96](../notes/2026-11-28-SC-passive-complete-root96-records.md)：
纯函数和三个原自然目标不变，只把已有的全部 $d_j,z_j,e_j$ 连同原
P224/TC positive/negative、joint math 和 receiver 身份写入同一个
完整 `columns` 对象。CFC 的实际接口直接复制这个完整 $e_j$ 向量，
因此不使用 (CFC.3) 的额外保守放大，也不重算原 SC 目标。

原 SC 的两张 $96\times96$ signed 矩阵分别是 physical primitive
receiver 和 declared incoming cosine receiver。它们都没有给出完整
目标列 $H_{\rm phys,j}$。将它们的第97至2240模式填零，会改变原算子。
本篇真正补的是整个目标 Hilbert 空间中的96列近似与无限维误差，以及
这些相同列的原 $\Theta$、mean、phase、height 读出。

## 2. 完整物理列的前向定义

同 [BFP](R147-supplement-complete-target-normalized-nu-forward-column-by-pullback.md)
的原次序，定义

\[
 f_j={I w_j^++I w_j^-\over2},\qquad
 X_j=B_a^{-1}U_H^{-1}f_j\in Y_a^0 .                  \tag{CFC.4}
\]

所有 normalizer 使用同一个真实 selected 腰 $q, n_g$。同号算子
$B_a=\mathrm{Id}+T_wI$ 的正频输入仅来自正频；不能替换为未投影的全乘法。
由 [WPM](R133-supplement-physical-reflection-mean-rank-and-complete-scalar-row-ledger.md)
的反射，试探 $f_j^a$ 是完整 degree96 的实偶 mean-zero 多项式。
同成员完整物理转移给

\[
 \|U_H^{-1}(f_j-f_j^a)\|_2\le {B_H D_j\over\sqrt2},
 \qquad \|f_j^a\|_2\le {\|Y_j^a\|_{\mathcal Y}\over\sqrt2}.     \tag{CFC.5}
\]

后一个完整旧 waist norm 直接复制，不重算旧 norm 目标。

owner 用原 SC 的同一 value-only 恢复前缀重建整个
`7671×193×96` 数组并核原 whole SHA。它在原 `full_waist_density`
完成之后、进入旧 RW rows 之前停止。原4个 derivative arrays、原 RW96
rows 和原两张 SC 矩阵都不需要为这个新目标重建。两条 primitive 的
和完整形成，再取全部96正频；imaginary part 的准确为零来自反射代数，
不来自浮点阈值。两条原存储 mean 也完整留下。

取任意512正频的精确 dyadic 试探 $\widehat x_j$。一次 floating
$512\times512$ solve 同时选择全部96 RHS，仅作 proposal。其插值、FFT
和有限 solve 不提供证书；若 proposal 失败，可选完整零 trial，随后
仍需接受完整残差计算的真实结果。

所有原2048个 $\widehat w$ 系数保持 whole SHA。完整正频前向像为

\[
 r_{n,j}=z_{n,j}+\sum_{\ell=1}^{512}
 {\widehat w_{n-\ell}z_{\ell,j}\over4i\ell},
 \qquad 1\le n\le2560,                             \tag{CFC.6}
\]

相应实函数记为 $r_j(t)=2\Re\sum_{n=1}^{2560}r_{n,j}e^{4int}$；
下面的 quadrature 使用这个完整实重建，不能遗漏因子2。

$z_{n,j}=0$ 仅表示这个有限 trial 在 $n>512$ 的系数。乘积实际支持为
$[-2047,2560]$，长8192的完整 directed FFT 卷积不发生 alias。必须先
做完整乘积再保留正频同号块；零、负输出的投影不是删除负输入误差。
原无限高模继续由 $w-\widehat w$ 和最终 $X_j-\widehat X_j$ 的全空间界承担。

## 3. 全部8192点的有向整批求值

所有 $G=K_{48}\circ H_{24}$ 点使用原 whole carrier；$G'$ 由完整
analytic chain rule 计算。它不是 grid difference。沿原完整8192个点，
对所有96列求值 $r_j(G)$，保存每个完整 point integrand 后才归约：

\[
 Q_j={1\over8192}\sum_{s=0}^{8191}
 {\left(r_j(G(t_s))G'(t_s)-f_j^a(t_s)\right)^2\over G'(t_s)}.
                                                               \tag{CFC.7}
\]

所有 source、image、point、transform arrays 均在 job private 区先保存
完整有向端点、读回、核 whole SHA，再消费。

为让96列共享一套单位圆幂，设 $u_s=e^{4iG(t_s)}$，用 exact binary64
中心 $\widehat u_s$ 和已付 $\tau_s\ge|u_s-\widehat u_s|$。
若 exact power 与中心 $c_{n-1,s}$ 的误差为 $\rho_{n-1,s}$，把下一次
中心乘积重新取 exact dyadic 中心，并支付该次完整 directed product
的误差 $\epsilon_{n,s}$，则

\[
 \rho_{n,s}=\operatorname{up}\{
 \rho_{n-1,s}+(1+\rho_{n-1,s})\tau_s+\epsilon_{n,s}\}
 \ \ge |u_s^n-c_{n,s}|.                            \tag{CFC.8}
\]

用的是 $|u_s^n|=1$，没有不断相乘的 rectangular enclosure。每一列
的多项式额外误差为全部 $\sum_{n=1}^{2560}|r_{n,j}|\rho_{n,s}$。
directed Box 在所有中心、系数和求和上另付逐次浮点误差。这里用的
复数 L1 magnitude 是 Euclidean magnitude 的上界，故保守但有效。

设 $\sigma=1/128$。BFP.11--13 对每一完整列同样给

\[
 A_{r,j}=2\sum_{n=1}^{2560}|r_{n,j}|e^{4n(\sigma+G_0)},\qquad
 A_{f,j}=2\sum_{n=1}^{96}|f^a_{n,j}|e^{4n\sigma},
\]

\[
 \rho_{\mathrm{fin},j}=
 \sqrt{Q_j+e^{-4\cdot8192\sigma}
                {(G_1A_{r,j}+A_{f,j})^2\over 2-G_1}}.          \tag{CFC.9}
\]

全部 true-$H$ flow error、原 $w$ 的两种完整误差乘积和 (CFC.5) 的
PDE error 依 BFP 原公式付上。两种 $w$ 产品均保存，才取较小的完整候选。
同一个已经实际付费的 $B_a^{-1}$ 界乘上该全残差，得到

\[
 \|X_j-Q_a\widehat x_j\|_2\le\delta_j,\qquad
 \|X-\widehat X\|_{\ell^2_{96}\to Y_a^0}
          \le \left(\sum_{j=1}^{96}\delta_j^2\right)^{1/2}.   \tag{CFC.10}
\]

投影 $Q_a$ 使用整个 true-$a$ 球，不能换成其 midpoint。512个目标坐标
全部保存。第513模以上仅对有限 trial 为零，真实 $X_j$ 的无限 tail
属于 (CFC.10)。不能把逐列最大误差当成整批 operator norm。

## 4. 同一列的完整原 Theta

对每个完整 $\widehat X_j$，直接消费
[DCP](R149-supplement-particular-density-Theta-and-complete-opposite-leakage.md)
的 generic 公式。原 model 全2240个 signed multipliers、true source
$b$、原全部2048个 $\alpha$ 系数和原 $C^\dagger$ 次序保持不变。
整批先形成

\[
 v_j=(\mathrm{Id}-T_{\widehat\alpha}I)\overline G\widehat X_j
\]

的全部2560个正频，符号为 minus。其 primitive 在原完整8192点
$\widehat p$ 上按 (CFC.8) 求值，再做整个 directed FFT。所有96个正
readout 和2048个异号 head 均先完整保存。DCP 的两条 alias rays、
异号无限 tail、true-$p$ 同伦、完整 $\alpha$ 误差、Krein 常数 $4/25$
和原 root readout $\Re z-\Im z$ 逐项保留。

若该有限目标列的完整 DCP error 为 $\varepsilon_j$，实际 whole-global
$\Theta$ 界为 $B_\Theta$，则原真列满足

\[
 \|\Theta X_j-c_j\|_2\le\varepsilon_j+B_\Theta\delta_j.     \tag{CFC.11}
\]

$B_\Theta$ 复用 DCP 已选的完整 UACT/WMT 候选；不能拿 UACT low96
误差当 whole-global error。把全部96列平方后求和，再付确切中心向
binary64 的完整 Frobenius 转换误差，得到一张完整有符号 $96\times96$
矩阵的 joint error。该矩阵保存了原 $\Theta X_j$，不是完整物理 square。

## 5. 真 PDE mean、phase、height 行

两条原存储 mean 是同一个 physical reflected mean 的两种存储坐标，
rank为1。整个 $\mathcal Y$ 误差 (CFC.2) 同时控制它们，故整个
$2\times96$ mean block 的误差不超过
$\sqrt{\sum_jD_j^2}$ 加完整有限载体中心误差。不能据此增加第二个
自由 mean unknown，也不能把完整 independent mean 方程删除。

这里96个 TC homogeneous 输入均有 $\kappa=0$；完整 $q,n_g$ 仍取真实
selected normalizer。独立 $\delta\nu$ 方向的 normalizer 导数、外
mean/Robin direct terms 和全参数源不属于这96列，必须保留在其各自
原参数列中。BFP/DCP 的 strict particular 只是已证的那一列，不自动
填充所有 direct-$\nu$ 端口。

由 [PRN](R149-supplement-complete-phase-receiver-in-original-negative-source-windows.md) 和
[PWA96](R149-supplement-PWA-height-row-and-common-ratio-phase-consumer.md)，
同一原列的 PDE correction，在其 actual world 外端口固定的这个列块上，
令

\[
 s_j=(e_j,F_{-,j},F_{\mathrm{st},j},0),\qquad
 r_P=(2600,184,69,245),\qquad r_H=(94013,6651,3001,8852).
\]

PWA96 的第六完整目标保存原四个输入窗口上的
$r_{PH}\ge r_P+\sup|\rho_P|r_H$，其中 $\rho_P$ 是同一个未 normalization
strict particular 的真实 phase/height 比值。其第七完整目标保留
independent world 两 receiver。CFC 直接读取这两个完整向量，不再计算
旧 ratio、height joint radius 或它们的 receiver 目标。新的每列费用为

\[
 b_{P,j}=r_P\cdot s_j,\qquad b_{H,j}=r_H\cdot s_j,\qquad
 b_{PH,j}=r_{PH}\cdot s_j .                         \tag{CFC.12}
\]

原连续 TC trial 的人为 jump 为零；不能给未来其他有 jump 的输入
免费采用本式。这里 $e_j$ 是原首次 SC 的完整保存记录。完整 AP96/PWA96
原 signed exact centres 直接复制，原
joint radius 加 $\sqrt{\sum_j b_j^2}$ 给新的真 PDE 行 joint radius。
没有再做一次原 phase、height、L1 或 residual 积分。

PWA96 自身的整行组合保留一个共享 $\rho_P$：exact centres 是
$p_j-\rho_c h_j$，joint error 已付
$E_P+\sup|\rho_P|E_H+\operatorname{rad}(\rho_P)\|h\|_2$。
CFC 消费该完整对象，不把96列变成96个独立 quotient。

完整 $Y_b,K_b$ world ports、raw phase chart correction、geometry impulses
及 independent physical mean equation 保留独立。尤其由96 physical
observations、两条存储 mean、phase、height 和一条 parameter column
组成的 $100\times97$ 观察表，不是 square inverse 证书。

## 6. 实际计算范围、完整 prefix 和下一接收层

一次自然目标覆盖全部96列。公共 owner 要求所有前置目标完整；科学
执行时不把某个成功列或前64个模式算作新的可重复目标。每64个模式
保存同一整批的所有幂中心、半径、累加值和误差完整对象，失败记录留下
准确位置及 whole receipt chain。所有数组只在 job 私有区，公共仅
保脚本、参数、run、完整 SHA、全向量误差和 failure/prefix 身份。

本计算向下一层真正供应的是完整 $H_{\rm phys}$ 的96个目标列及其
无限维误差，和同源的 $\Theta$/mean/phase/height 行。
[WGB](R133-supplement-exact-graph-parameterization-and-physical-finite-border.md)
与 [TQ](R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md)
仍要求同一个 high inverse 的有符号

\[
 PH^{-1}PKQ,\qquad PH^{-1}PU,\qquad PH^{-1}Pg
\]

及相同 RHS 的 $PH^{-1}Pf$，完整非均值 chart、world、parameter 边界
列和独立 physical scalar rows。现有无符号 high/finite bounds 不能
代替这些 signed carriers。UACT 真 $\Theta E_{96}^a$ 可逆是精确坐标
工具；它不会从此96列观察中生成这些缺失块。owner 将这些对象逐项留
在接口账目中，不把 CFC 十目标完成误记为剩余 Schur 或课题完成。
