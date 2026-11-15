# R133：原非 mean 残差窄域限制与三带迹系数的实际结论

状态：实际公开执行完成；完整源项及系数表已逐项回读，供独立核对。本篇只消费既成小回执，不运行数值。

本篇使用 [MC 原 raw mean 身份更正](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md)、[MA 五例修正后高阶域](R133-supplement-actual-raw-mean-fee-and-restored-high-collar-domain.md)、[LT 三带迹](R133-supplement-finite193-middle-band-and-infinite-collar-trace.md) 及 [NR 消费者合同](R133-supplement-saved-nonmean-restriction-and-three-band-trace-consumer.md)。固定原 $\eta_0$、$|\delta|\le d=10^{-10}$，角频率为物理 $4j$，圆周测度为 $(2/\pi)\,d\phi$，径向积分为真实 $dr$。

## 1. 实际运行和完整身份

**(NA1)** 唯一成功运行是公开 [run 43720373326/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43720373326)，job 132830847866；科学子进程返回 0，全部 **13/13** 门通过，新标量计算时间 3.5207349350000072 秒。五组完整表均已生成。运行没有建立未知核心解、GH 逆或低曲率入口；相应结论字段均保持 false。

完整小证据为：

- [execution.json](../notes/saved_nonmean_three_band_trace_ci/run-43720373326-1/execution.json)：56,961 B，Git blob 15a2723774908cbbfe3768b9b71ef3f544dc1df5，SHA256 401d41d80b394970736136f4f39e3a5dcb2ecc1728378dfc43ae2b11da6d184e。
- [actual-result.md](../notes/saved_nonmean_three_band_trace_ci/run-43720373326-1/actual-result.md)：6,957 B，Git blob c9a7802d9e6950fcbe52744d582cbee8ba01fbec，SHA256 9ddb4d00a80d829e807e4803b040f891fd0abee2aaf65f35144d46c58b6593dc。

execution 内完整 actual_scientific_receipt 按原规范 JSON 恢复，逐字得到 48,369 B、SHA256 45e348a9279d4455a7bd07a071f9b558de11866ebbbda517d9d00931e0907f35，与子进程原输出 hash 完全相同。完整预发表包为 58,161 B、SHA256 6defe4ace5dd9cf0fb1879f4145cfff6eecb999492e87a086de113be00840da0；其中全部科学字段及完整报告分别与最终发表内容相同。

**(NA2)** 冻结科学源为 scripts/fourfold_codazzi_saved_nonmean_three_band_trace.py，26,039 B，blob 9a0b5fa72652c9f16c46c8ff7aa9202bbbf8fe2f，SHA256 129f7f7955bb8d11385b9804353f0e389761ba38cc74467436a9600283376934。实际 manifest SHA256 为 e9ea51e344e873096d14e2c18d25da085c82e268de1039bd0e09a3c7a3b972ec，worker SHA256 为 7f1bd9e510cbbe226e251234893b5e603cd7b4584101cf0a01de086cd19ab612。科学 checkout 为 e3e8a96665af1638bbf6be05be639b4f889103d1，触发 workflow commit 为 e71a6d93f0e9579bf5cd78f0a49a88243329aeb3。

全部 19 个小输入、40 个原自然 native、7721 行、原 $[0,25/8]$ 连续覆盖均核过。原完整行规范 SHA256 仍为 06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6。新行审计 308,257 B 只临时保存，持久证据仅保其 hash 6dd025f2ff8961546d82ea3e7555d0920b83015525ab6c20082be7ccd5468995。

**(NA3)** 首次 43719591979/1 在 worker 的预发表大小门失败，日志未输出其 child 返回值及 gate 计数，临时新结果丢失。因此该次科学结果仍记为未知。用户授权恢复丢失的新结果后，仅修改 infra：去重来源审计和容量 metadata，保完整 hash/count、README 真 pull 序列、实测容量；在大小门前另打印实际 child、全部门计数及完整科学 hash。科学源和公式不变。当前成功锁定后，不再运行这组新限制。

原 target、FFT、cubic residual、mean flow、原残差积分和 Green 调用均为 **0**；MA 两个成功 mean 窗及五例高阶授权逐字复制，原 91 例记录和此前 false 的低入口记录均未修改。

## 2. 原字段和新的两个真实限制域

**(NA4)** 每行读取的量严格是原 uncorrected_response_nonmean，不是 mean-completed 向量。原 row producer 先构造完整 $R=D_{\rm raw}q_{\rm raw}-F_{\nu,\rm raw}$，随后取 $(R_1,P_\perp R_2)$，存其 L2_sup、L2_L2_radial、H1_sup、H1_L2_radial。原 mean 残差独立保存。

令
$$
P(r)=\operatorname{diag}\bigl(K(r)^{-1/4},K(r)^{1/4}\bigr).
$$
对原闭行 $I_i$ 与新窗口的真实交长 $\lambda_i$，采用两个完整上界的较小值
$$
\min\{\lambda_i s_i^2,L_i^2\},\qquad
\min\{\lambda_i s_{i,1}^2,L_{i,1}^2\}. \tag{NA4}
$$
$L_i$ 始终是原整行积分范数；不按交长比例缩小它。每行的 $P^2$ 上界由同一完整正 $K$ 区间给出，先乘入平方积分，再跨行求和和开方。没有 $\alpha$ 因子。

**(NA5)** 两域分别为
$$
I=[17/20,19/20],\qquad I_*=[589819/655360,589829/655360].
$$
前者真实长度 $1/10$、140 原闭行；后者长度 $2^{-16}$、2 原闭行，中心 $c=9/10$、$\ell=2^{-18}$。以下为完整 Arb 输出向外放宽的界：

| 真实窗口 | raw nonmean $L^2_{r,\phi}$ | $P$-scaled nonmean $L^2_{r,\phi}$ | raw nonmean $L^2_rH^1_\phi$ | $P$-scaled $L^2_rH^1_\phi$ |
|---|---:|---:|---:|---:|
| $I$ | $<7.914995000\cdot10^{-7}$ | $<1.209073435\cdot10^{-6}$ | $<5.020362459\cdot10^{-4}$ | $<7.667143883\cdot10^{-4}$ |
| $I_*$ | $<9.970067345\cdot10^{-10}$ | $<1.602332537\cdot10^{-9}$ | $<5.494816645\cdot10^{-7}$ | $<8.833547009\cdot10^{-7}$ |

$P$-scaled 角导范数取原完整 $H^1$ 界与 $640$ 倍完整 $L^2$ 界之小，分别仍小于表末两值。原 raw nonmean 支撑至 quarter degree $160$，故 $640$ 是真实最高物理频率。

## 3. 全部修补、均值和已知高投影源

**(NA6)** 在 $I_*$ 上，全中心修补及 canonical continuity offset 的新增限制费为
$$
p_I\sqrt{|I_*|}\left(B_{\rm repair}+B_{\rm offset}\right)
<3.926959183\cdot10^{-14}. \tag{NA6}
$$
其中原完整费分别为 $B_{\rm repair}<1.131919447\cdot10^{-15}$、
$B_{\rm offset}<5.840950986\cdot10^{-12}$；$p_I$ 只在此出现一次。原修补/offset 作用于完整 finite 响应后的支撑仍不超过 $160$，其角导费也是 $640$ 倍。

与 MC 已付的原整量正上界比较后，五例具有逐字相同的新完整高投影响应界：
$$
S_{96}<1.602371807\cdot10^{-9},\qquad
S_{96,\phi}<8.833798334\cdot10^{-7}. \tag{NA7}
$$
这两个量只用于 $H_{96}Pb_0$ 及其角导；不把它们称为原 canonical 完整源 $Ps_0$ 的界。

**(NA8)** 原恒等式保持为
$$
f_\delta=f_0-\delta b_0+\delta r_0e_2-\delta^2T_2-\delta^3T_3. \tag{NA8}
$$
$f_0$ 是原 degree-$32$ 背景的完整残差，支撑至 $96$；$b_0,T_2,T_3$ 分别保至 $160,224,288$。$r_0$ 是独立 raw mean，已由 MA 完整支付。它仅在本节高投影下精确消失；完整方程中的 mean 和原连续修补均不删。

复用原完整 $T_2,T_3$，新公开结果给
$$
\begin{aligned}
\|H_{96}Pf_\delta\|_{L^2}&<3.596675358\cdot10^{-18},\\
\|H_{96}P\partial_\phi f_\delta\|_{L^2}&<3.167386591\cdot10^{-15},\\
H_{288}Pf_\delta&=0,\qquad H_{288}P\partial_\phi f_\delta=0.
\end{aligned} \tag{NA9}
$$
最后两个等号使用完整 finite 支撑，含所有 mean，不是以小数近似零。

## 4. 五例真实三带系数

**(NA10)** MA 保留的五个 raw $C^0$ pair 半径为 $\rho=2^{-20},2^{-24},2^{-28},2^{-32},2^{-36}$。每例仍以**同一个**实连续双侧 $H^1$ 真解 $Q$ 为前提，且 $h=Q-Q_\delta$ 在对应 $C^0$ 球内。记
$$
z=Ph,\quad Z_L=\|\Pi_{96}z\|_{L^2(I_*)},\quad
Z_H=\|H_{96}z\|_{L^2(I_*)},\quad
c_L=\|\Pi_{96}h(c)\|_{L^2_\phi}. \tag{NA10}
$$
$\Pi_{96}$ 包含反射类完整 193 维及 even mean。

五例完整实际表均给出以下共同安全上界：
$$
\begin{aligned}
E_{96}&\le F_{96}+7592.106 Z_L+270369.153 Z_H,\\
E_{288}&\le F_{288}+\beta_L(\rho)Z_L+284625.782 Z_H,\\
V_{96}&\le4.932 E_{96},\qquad V_{288}\le4.932 E_{288},\\
\sqrt{\Lambda_{288}}V_{96}&\le167.365 E_{96},\qquad
\Lambda_{96}<384.002 .
\end{aligned}\tag{NA11}
$$
$E,V$ 的完整定义为 LT7、LT9、LT15–16；包括 actual mean 的主速度、rank-one 反应、真实 drift 和两侧 cutoff 源。用 LT20 完整三带正交式时可直接使用 execution 中各例较尖值。

| $\rho$ | $E_{288}$ 的 $Z_L$ 系数安全上界 $\beta_L(\rho)$ | 已知 $F_{96}$ 贡献的 middle $H^1$ 上界 |
|---|---:|---:|
| $2^{-20}$ | $0.012265943$ | $6.019547661\cdot10^{-16}$ |
| $2^{-24}$ | $0.000766621368$ | $6.019536711\cdot10^{-16}$ |
| $2^{-28}$ | $0.000047913836$ | $6.019536027\cdot10^{-16}$ |
| $2^{-32}$ | $0.000002994615$ | $6.019535984\cdot10^{-16}$ |
| $2^{-36}$ | $0.000000187164$ | $6.019535981\cdot10^{-16}$ |

实际 source 字段在五例完全相同；不同主速度、非线性差系数、各原 case hash 及高阶授权均各自保存。独立核对五个原 case SHA 后，均与原 91 例中相应对象相等。

**(NA12)** 对 NA10 的同一真解，MA 已付 $\|h(c)\|_{H^{8193}}<2^{377903}$，故
$$
\|H_{288}h(c)\|_{H^1}\le2^{24}V_{288}^{16384/16385}. \tag{NA12}
$$
middle $97\ldots288$ 单独付 $\sqrt{\Lambda_{288}}V_{96}$；它不乘 $2^{24}$。完整 finite-cut 读出为
$$
\|h(c)\|_{H^1}^2
\le\Lambda_{96}^2c_L^2+\Lambda_{288}V_{96}^2+
2^{48}V_{288}^{32768/16385}. \tag{NA13}
$$
全部未知 $c_L,Z_L,Z_H$ 均保留。它们未由 $\rho$ 的粗 $C^0$ 上界替代。

## 5. 已知项的正预算和未知项消费门

**(NA14)** 由 W 的已付实际 known-angle 界，统一充分半径为
$$
r_*=\frac{63d}{320}=1.96875\cdot10^{-11}.
$$
各例实际保存的 $r_*-\text{known-middle-upper}$ 均严格大于
$1.9686898045\cdot10^{-11}$。这是已知源项后的正预算，不是实际未知解的入口已经通过。

例如，对 NA10 的同一真解，在五例中选定一个 $\rho$，下列具体条件足以触发 W 低入口：
$$
\begin{aligned}
384.002 c_L
&+167.365\bigl(7592.106 Z_L+270369.153 Z_H\bigr)\\
&+2^{24}\Bigl[4.932\bigl(\beta_L(\rho)Z_L+284625.782 Z_H\bigr)
\Bigr]^{16384/16385}
<1.96868\cdot10^{-11}.
\end{aligned} \tag{NA14}
$$
这是 NA11–13 的三角放宽：已知 middle 项另用表中最大值。两者之和仍严格小于 $r_*$。故 NA14 同时给 $\|h(c)\|_{H^1}<r_*<2^{-10}$ 及
$$
\|\gamma\|_{A_0}
\le\frac{13|\delta|}{200}+\frac{\|h_v(c)\|_{H^1}}{15}
<\frac{10^{-9}}{128}. \tag{NA15}
$$
$\gamma$ 是与原物理基点曲率之差；已知选参方向、完整 mean 与真实物理角转换均按 W 保留。

**(NA15)** 未来输入必须属于同一已匹配状态。若先取得 raw moving 左右两个半窗的体范数 $B_L^\pm,B_H^\pm$，可按
$$
Z_L\le1.721\sqrt{(B_L^-)^2+(B_L^+)^2},\qquad
Z_H\le1.721\sqrt{(B_H^-)^2+(B_H^+)^2} \tag{NA16}
$$
进入 NA14；$1.721$ 包围本次全部 $P$ 范数。原 Green 的 whole_inner_body 仅为 $[0,9/10]$，可以限制到左半窗；其 true_cut_trace 仅为 $r=9/10$。右半窗 $B^+$ 必须来自真实帽的同一匹配状态。Green 的 operator gain 必须先乘完整实际负荷；特殊有限 $A_{LH}$ 列不能充当普通源增益。

如有完整 signed finite cut，可按 LT26–27 直接输入
$\partial_\phi(\Pi_{96}h_v-j_\delta\langle h_v\rangle)$ 的相关范数及独立 $\langle h_v\rangle$。单一 $c_L$ 上界不自动等于该相关量。真实 $C$ mean 恒等及 $B$ mean 只约束 mean，不能删除非 mean shape。

## 6. 近似迭代态及尚未支付的输入

**(NA16)** 对近似态，$H_JPf$ 是独立 ordinary residual，必须在 NA9 的已知项之外加入；其角导须按 LT22–23 完整收费。actual mean-speed 的 $f_2/m$ 项仍在。当前五例沿用真解 $f=0$ 的速度和高阶授权，不能将同一数表无费授给任意近似态。若近似态尚无同一高阶门，使用 LT22–23 的两能量直接读出，并独立支付该态所有系数门。

**(NA17)** 当前已实际完成：原 raw nonmean 两域限制、全部修补费、五例完整 $E/V$ 系数、已知高投影源以及正的剩余预算。仍需真实 $c_L$、双侧同态 $Z_L/Z_H$、真实 cut 匹配，以及核心解或相应迭代的来源。回执保持 actual_core_solution_proved、complete_infinite_BVP_inverse_proved、actual_low_curvature_entry_proved 三项为 false。

本篇给出 NA14 的具体三量门；MA 的 raw mean、LT 的所有 mean/rank 源及右帽半域独立保留。
