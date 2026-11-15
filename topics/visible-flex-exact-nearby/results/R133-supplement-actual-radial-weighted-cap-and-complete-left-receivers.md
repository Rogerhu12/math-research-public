# R133：实际径向加权帽接收算子、完整均值与六组后验界

2026-11-15。状态：新的公开标量消费已成功；完整科学结论、过程、十五门与六组权重均已逐项回读。本篇只解释该次实际结果，不运行新数值。

依赖 [RW 完整核与径向权重](R133-supplement-true-cap-local-receivers-and-radial-weighted-posterior-bounds.md)、[M 零宽两输入实际帽](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)、[RB 真角与普通体范数转换](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md) 及 [RC 右侧宽窗 C0](R133-supplement-actual-right-cap-wide-C0-collar-entry.md)。原 MA/NR/WC、帽存在性、所有成功和失败记录均保持原样。

## RA1. 实际运行与完整身份

公开 run **43729429382 / 1**，job **132858381096**，由部署 commit `f1a97ec0436c38aa274ffc1636a4d8277a0f803e` 的 push 自动触发。原始科学子进程退出码为 **0**；数学实际用时 **2.0260824950000114 秒**，子进程包装观测 **3.0006872980000026 秒**。工作流所有步骤完成，最终 conclusion 为 success。

| 冻结文件 | Bytes | SHA256 |
|---|---:|---|
| scientific source | 31066 | `f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb` |
| public worker | 33129 | `e15f0e49fbd84da0b165489cbd8f04ef36477e53e502a12daf3362ced4f458e6` |
| complete input manifest | 17341 | `333bff731ec491b362feb665b54bcb2173bbbdc571f3459e03b63a63af72a3af` |

原件目录为 `notes/radial_weighted_cap_receivers_ci/run-43729429382-1-radial-weighted-cap-receivers/`，相对于该目录：

| 完整实际原件 | Blob | Bytes | SHA256 |
|---|---|---:|---|
| `actual-radial-weighted-cap-receivers.json` | `a4d46696df6125524d7491cd1d4efde156794aee` | 57702 | `ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9` |
| `process.json` | `df608c6a12fb193106fba64fb23fd7afad37de29` | 16350 | `daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6` |
| `actual-result.md` | `8c75230ee8cb0219b37c1908b0018902757c5137` | 7874 | `cae252d828b2872a697ec7eac6c2136944e390077f796ce8d30e442f5b7ecaa2` |

完整十五个 structural/source 门全部 true，六个实际 $\chi$ 门也分别成立。后者是每一行的独立数值判断，不是从子进程退出码代推。

## RA2. 原对象、覆盖和保留量

对象仍是 `ac1d5b98…` 的完整连续修补 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，固定原 $\eta_0,\nu_0$、真实 $\alpha$。实际应用是 M 的实反射两输入域：
$$
 G_\gamma=\|\gamma\|_{A^0_\theta}<10^{-9},\qquad
 \|f_B\|_{\dot A^2_\theta}<2^{-60},\qquad
 \rho=3\,10^{-6},\quad \zeta=9.9\,10^{-10}.
 \tag{RA.1}
$$
这里 $\gamma$ 是物理角的内端非零 Fourier 曲率输入；并非原 moving low97 的截断向量。两类输入都保持零宽定义。

所有 ordinary 源点仍覆盖整个真帽
$$
 I_{\rm cap}=[9/10,25/8],
$$
只有普通体输出限制到
$$
 I_+=[9/10,19/20].
 \tag{RA.2}
$$

消费者精确恢复原 7296 行 residual、其中 1341 个帽行、949 个全频率参考行和原 1346 个完整交段。在原交段上插入准确 $19/20$ 后，本次新积分使用 **1347 个真有理交段**。没有按输出区间长度比例缩小旧全帽积分。

完整原 physical $B,C$ source constants 及已成零权 L1 结果逐字复制。所有十八项 pin 通过，包括六个历史输入；恢复仅到 runner 临时目录。原 target、Fourier、ordinary residual enclosure、repair、mean flow、Riccati 与 Green 传播重算数均为 **0**，旧零权积分也未重算。

本次完整临时逐行审计为 5,176,130 B，SHA256
`a281148465b16e43fb24d2ffb1bd08837f29a4396a5d9d6c1ca080540f139a9d`；
仅小结论保留。数学完成后、最终 Git 出版前，完整 science 与完整 report 已通过 56,032 B 的 prepublication payload 输出，SHA256
`5f3d512702e4ad7f716880c9a11032578e840fc8cc1e26385451b843b37cb01c`。
最终测得 projected topic 198,374,631 B；没有新 artifact 或 Release。

## RA3. 新左端 ordinary 接收核

RW 的准确 $H(L,t)=0$ 给非零模 $B(L)$ 的单 backward 核。真实 $C$ mean 使用自己的 backward 核，不能令非零频率趋于零来代替。以下全部是实际有向上端的宽十进制值：

| 新已知源或端传播 | 严格上界 |
|---|---:|
| $\eta_{B,L}$，实际反射非零模 | $1.874524923\,10^{-9}$ |
| general parity 的 $B$ 总接收界，另收完整 $B$ mean | $3.996032985\,10^{-9}$ |
| $\eta_{0,L}$，以完整 $F_C$ 支付独立 $C$ mean | $1.601563478\,10^{-9}$ |
| $e_D$，所有 $M\ge4$ 的右 $d_R$ 传播 | $2.241107877\,10^{-19}$ |
| $e_0$，右 $C$ mean 传播 | $8.281109667\,10^{-11}$ |
| $e_B$，独立右 $B$ mean 传播 | $1.306411016\,10^{-10}$ |
| $q_+(L)$ | $1.389936764$ |

这里 source-point $q(t)$ 与输出点 $q(L)$ 没有互换。实际反射 $B_0=0$ 仅用于对应实际子族；消费者仍完整记录了 general-parity mean 核。$\eta_{0,L}$ 支付完整 $F_C$，不是声称其真实 mean 等于该上界，也没有将其删除。

这些是 unclosed known-source receiver。完整 nonlinear $Q$ 及外图回馈在下一节逐行收费。

## RA4. 六个完整径向权重均通过后验门

每个权重使用原 949 闭行上准确向下取整的 dyadic 速率：
$$
 \lambda_\kappa
 =\kappa\,\operatorname{dyadic\_lower}
 \{\min(4s_D,-2\beta,-\beta(\ell+1))\},\qquad
 w_\kappa(r)=\exp\left(-\int_L^r\lambda_\kappa\right).
 \tag{RA.3}
$$
选择 $\kappa=1/16,1/8,1/4,3/8,1/2,3/4$。完整逆频率区间
$z=1/M\in[0,1/4]$ 分为64个有向闭区间；不存在只以 $M=4$ 代替全高频的步骤。
两条 mean 分母各自保留。

记
$$
 X_{w_\kappa}
 =\sum_k\sup_r w_\kappa(r)|x_{B,k}(r)|
  +\sum_k\sup_r w_\kappa(r)|x_{C,k}(r)| .
$$
$Q$ 的完整值系数为
$$
 A_Q=0.051432066+13\rho=0.051471066.
$$
每行分别使用
$$
 X_{w_\kappa}\le
 \frac{\eta_{\kappa,0}+H_{C,\kappa}G_\gamma}{1-\chi_\kappa},
 \qquad
 \chi_\kappa=K_\kappa A_Q+0.006H_{D,\kappa}+0.00075 .
 \tag{RA.4}
$$
$\eta_{\kappa,0}$ 包含全部 ordinary body 源与真实外端 $r_D,r_{C,0}$；
$w_\kappa(R)$ 使用完整 Arb 球，所以除以它的 outer 项也保持有向性。

| $\kappa$ | $\chi_\kappa<$ | $\eta_{\kappa,0}<$ | $X_{w_\kappa}$ 的 affine 上界 | $G_\gamma$ 的系数上界 |
|---|---:|---:|---:|---:|
| $1/16$ | .827986078 | $2.580477\,10^{-7}$ | $1.500156\,10^{-6}$ | 13.893857 |
| $1/8$ | .787308914 | $2.215182\,10^{-7}$ | $1.041502\,10^{-6}$ | 11.236657 |
| $1/4$ | .729944450 | $1.678167\,10^{-7}$ | $6.214155\,10^{-7}$ | 8.849797 |
| $3/8$ | .695270080 | $1.310582\,10^{-7}$ | $4.300796\,10^{-7}$ | 7.842804 |
| $1/2$ | .677101984 | $1.048738\,10^{-7}$ | $3.247891\,10^{-7}$ | 7.401522 |
| $3/4$ | .680307324 | $7.104519\,10^{-8}$ | $2.222297\,10^{-7}$ | 7.475732 |

所有六行的 `complete_weighted_posterior_applies` 都是 true、`candidate_failure` 都为 null。此表各行是完整估计，不能从不同权重中逐项挑取 $\eta,K,\chi$ 再组成未证的界。

## RA5. 完整 ordinary 右体范数与两条内端曲率行

定义真实物理差的普通体 pair-sum
$$
 B_+^{\rm phys}
 =\|x_B\|_{L^2(I_+;L^2_\theta)}
   +\|x_C\|_{L^2(I_+;L^2_\theta)}.
$$
先按两分量各自的 joint supremum，再积分真实 $dr$，得到
$$
 B_+^{\rm phys}\le
 \left(\int_{I_+}w_\kappa^{-2}\right)^{1/2}X_{w_\kappa}.
 \tag{RA.5}
$$
没有把普通 $L^2_r$ 结论升级成 Fourier-sum radial-sup module。

| $\kappa$ | $B_+^{\rm phys}$ affine 上界 | $G_\gamma$ 的系数上界 |
|---|---:|---:|
| $1/16$ | $3.387830\,10^{-7}$ | 3.137677 |
| $1/8$ | $2.375608\,10^{-7}$ | 2.563019 |
| $1/4$ | $1.446248\,10^{-7}$ | 2.059653 |
| $3/8$ | $1.021579\,10^{-7}$ | 1.862920 |
| $1/2$ | $7.875944\,10^{-8}$ | 1.794826 |
| $3/4$ | $5.620922\,10^{-8}$ | 1.890860 |

同一行的完整内端估计分别为
$$
 \|P_{\ne0}x_B(L)\|_{A^0_\theta}
       \le b_{\kappa,0}+b_{\kappa,\gamma}G_\gamma,\qquad
 |\langle x_C(L)\rangle_\theta|
       \le c_{\kappa,0}+c_{\kappa,\gamma}G_\gamma .
 \tag{RA.6}
$$

| $\kappa$ | $b_{\kappa,0}<$ | $b_{\kappa,\gamma}<$ | $c_{\kappa,0}<$ | $c_{\kappa,\gamma}<$ |
|---|---:|---:|---:|---:|
| $1/16$ | $1.160327\,10^{-7}$ | 2.447225 | $4.499434\,10^{-8}$ | .401887 |
| $1/8$ | $8.389370\,10^{-8}$ | 2.274834 | $3.387940\,10^{-8}$ | .348243 |
| $1/4$ | $5.448005\,10^{-8}$ | 2.139111 | $2.407002\,10^{-8}$ | .319982 |
| $3/8$ | $4.123311\,10^{-8}$ | 2.107669 | $2.026198\,10^{-8}$ | .340286 |
| $1/2$ | $3.421862\,10^{-8}$ | 2.127017 | $1.921662\,10^{-8}$ | .401425 |
| $3/4$ | $2.874429\,10^{-8}$ | 2.293827 | $2.570731\,10^{-8}$ | .810910 |

$C$ mean 从完整 outer $C$ mean、ordinary source 和同一个 $Q$ 回馈恢复；
它不因内端 prescribed 数据是非零模而变成零。两个最终完整 scalar upper
可以取最小值；仍不允许拆开某一行的 source 与反馈项交叉取最小。

特别地，在 tail 输入子球 $G_\gamma<10^{-9}/128$ 上，实际原件直接给
$$
 \begin{aligned}
 B_+^{\rm phys}&<5.622400\,10^{-8} &&(\kappa=3/4),\\
 \|P_{\ne0}x_B(L)\|_{A^0_\theta}&<2.876221\,10^{-8} &&(\kappa=3/4),\\
 |\langle x_C(L)\rangle_\theta|&<1.921975\,10^{-8} &&(\kappa=1/2).
 \end{aligned}\tag{RA.7}
$$
这是同一实际帽族的不同完整后验界，不是另一次帽求解。

## RA6. 真 moving 输出、selected 差与 finite support

RB 的真角普通 $L^2$ 转换给因子80。对 $J=96$ 或288，
canonical $Z_{\rm can}$ 的完整支撑止于96，故
$$
 H_J(Q_*-Q_\delta)=H_J(Q_*-Q_0).
$$
先在真角中比较 $Q_*$ 和同一个 $Q_0$，再取原 moving 投影，得到
$$
 \|H_J(Q_*-Q_\delta)\|_{L^2(I_+;L^2_\phi)}
 \le80B_+^{\rm phys}.
 \tag{RA.8}
$$
并未将物理和 moving 的 Fourier 投影认作同一个算子。

例如 $\kappa=3/4$ 的完整高投影上界为
$$
 4.496738\,10^{-6}+151.268782G_\gamma .
 \tag{RA.9}
$$
完整 selected pair 则仍另外支付已知物理差
$10d\sqrt{|I_+|}$，$d=10^{-10}$；同一行给
$$
 \|Q_*-Q_\delta\|_{L^2(I_+;L^2_\phi)\oplus_1}
 <4.514627\,10^{-6}+151.268782G_\gamma .
 \tag{RA.10}
$$
径向 $P$ 尚须按对应 collar bound 作用一次。所有式均须是跨人工 cut
真正匹配的同一状态，才能与左半 Green 输出合并。

## RA7. 当前差距的准确含义

新计算确实补出了原来没有的 ordinary 左端源核、六个合法加权后验及明确的
右体/内端 affine 加 $\gamma$ 两列。它没有支付 [WA](R133-supplement-actual-wide-collar-mean-and-six-ordinary-half-trace-tables.md) 的未知低迹门。

从完整记录可见，当前上界在小 $\gamma$ 子球里由 known-affine body source
项主导，而不是由内端 $\gamma$ 列主导。该 affine 项来自完整原 residual 的逐格
绝对包络、统一 inverse-angle composition 费用，以及 $C$ mean 的完整 $F_C$
上界。原输入没有在这次消费者中提供足以恢复逐模符号或径向相关抵消的数据。
因此：

- 已显示的是这些**上界的瓶颈**，不是实际 residual 或实际解差的下界。
- 不得将完整 $F_C$ 上界任意减去 nonmean 上界来制造更小 mean。
- 单独令 $\gamma=0$ 不会删除已知基点体源；原实际 cap base mismatch 仍存在。
- 本次 ordinary 右体界不能替代左侧 finite193 cut、33--96 的新合法 receiver、
  225--288 真 high 数据或原 core GH。
- RC 的右半宽 $C^0$ 已付条件与窄 MA 的同态高阶条件仍独立；本次未扩大 MA 域，
  也未证明 core 存在、低曲率 selfmap 或全局匹配。

下一步局部组件/mean 与相关 receiver 的改进应继续按原完整字节产生独立新结论。
本次成功的六组科学结果已经冻结，不以调整常数或另一次运行覆盖。
