# R138 补充：完整互补 Gram 谱体预算与五个实际有向量

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## SA.1 实际完整结果

[公开 Actions 44767124478/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44767124478)
已完成整个 4651 闭片的新谱最大值、四个新 upper 和条件性第五个 lower。
科学与 execution 均 `complete=true`、`failure=null`，科学 `proved=true`，
唯一 child 返回 0，无 timeout。原完整文件为：

| 文件 | bytes | SHA256 |
|---|---:|---|
| [spectral-body-energy-budget.json](../notes/spectral_body_energy_budget_ci/run-44767124478-1/spectral-body-energy-budget.json) | 24640 | `24c5923eb7a0b34c566c785ec11e33e7881b3ce6c35613a60cb9532238cf1b5e` |
| [execution.json](../notes/spectral_body_energy_budget_ci/run-44767124478-1/execution.json) | 15484 | `ce2787cd11267f3d47dcbab8f2dd76851ca64ebec09a72767bac313235f7438a` |

触发提交为 `388867bfa854c8ba4adf9c0a3e698206f84246be`，实际科学 checkout 为
`0377af29a9f976b7e2e97c40e143003ac920573f`。
Python 3.12.14、python-flint 0.9.0、320 bits；数学时间约 0.213076486 秒，
完整 child 约 0.678483897 秒。无旧科学目标、旧 geometry/drift/capacity ODE、
新数组、artifact 或 Release。

[SG.1–17](R138-supplement-complementary-Gram-spectral-body-energy.md)
与 [首次完整合同](../notes/2026-11-20-R138-spectral-body-energy-budget-contract.md)
的原对象、符号和单位全部保留：同实际 $Q_{repair}$、同内禀 $\eta_0,\nu_0$、
完整 moving 圆周、真实根 $r_*$、外端 $25/8$、全独立 mean。
原 body flow 仍在外端恒等锚定；后继根接收器采用
[RA 真根锚定流](R138-supplement-root-anchored-local-drift-and-capacity.md)，
不是重启已排除的旧根 $\Gamma$ 整因子方案。

## SA.2 四条 upper 与条件 lower

| 原保存字段 | 本次完整结果的方便严格界 |
|---|---:|
| `C_spectral_upper` | $C_{sp}<21.052653$ |
| `wE_spectral_upper` | $w_E<21.466300$ |
| `aEE_spectral_upper` | $a_{EE}<0.748166$ |
| `aEB_spectral_upper` | $a_{EB}<0.600361$ |
| `root_allowance_spectral_lower` | $C_{allow}>515.804199$ |

这些小数仅简写原完整十进制 ball，后继消费以整个原记录为准。
原中心值依次约为 21.052652069293264、21.466299717770207、
0.74816542958334535、0.60036018934862755、515.80419912764898。
第五个记录方向明确为 lower；不能把其上端或中心作为已证 lower。

科学先完成整片谱最大值并保存读回，再与旧 $C_E$ 的完整 upper 取 min。
旧 $C_E$ 约 32.133，故本次新的完整谱值给出了有效改进；
没有以旧 $C_E$ 代替任何未计算的片。
以旧 X/Y/GB 的整个记录继续得到

$$
w_E=\frac52\Gamma\sqrt{A_\Theta}
\left(\sqrt{C_{sp}}+\sqrt{C_H}\,h_E\right),
\qquad
a_{EE}=E_0w_E^2+E_1w_Eh_E,
$$
$$
a_{EB}=2E_0w_Ew_B+E_1(w_Eh_B+w_Bh_E).
\tag{SA.1}
$$

这里 $w_B,a_{BB},r_E,r_B$ 及旧全域 $\Gamma$ 都是原成功值，只读一次。
尤其 $r_E,r_B$ 仍为原 $H^{2/3}$ 根源路径；本次体 $H^{1/2}$ 上界不替换它们。

## SA.3 三个体门与准确半余量含义

从完整 saved upper 构造

$$
M=\begin{pmatrix}a&-c\\-c&d\end{pmatrix},
\quad a=2-a_{EE},\quad c=a_{EB}/2,\quad d=1-a_{BB}.
\tag{SA.2}
$$

本次的 $a_{lo}>0$、$d_{lo}>0$、
$D_{lo}=\operatorname{lower}(a_{lo}d_{lo}-c_{hi}^2)>0$ 三门都为 true。
因而本次确实计算并保存了第五个 lower：

$$
C_{allow,lo}=
\operatorname{lower}\frac{D_{lo}}
 {\operatorname{upper}\{2(d_{hi}r_E^2+2c_{hi}r_Er_B+a_{hi}r_B^2)\}}
>515.804199.
\tag{SA.3}
$$

分母使用 $a_{hi},d_{hi}$，没有混用行列式中的 lower margin。
对真正另行证明的源型费用 $C_*\le C_{allow,lo}$，原 SG.17 才给
$M-C_*rr^T\succeq M/2$，其中 $r=(r_E,r_B)^T$。
此处尚未给实际 $C_*$ 或低根接收器；`actual_root_cost_paid=false` 保持。
体三门成功不等于全边界型、正侧逆或非线性存在。

## SA.4 根锚定必要筛查也通过，但仍只是必要条件

源内固定的 [RN 必要筛查](R138-supplement-root-anchored-spectral-budget-necessary-screen.md)
三条 $C_{sp}<24$、$w_E<45/2$、$a_{EE}<102/125$ 都通过。
对应的完整 saved lower 违反标记全部为 false。
直接读取同一完整十进制球的整数端点，还严格得到较强的 RN.15：

$$
C_{sp}<23,\qquad w_E<22,\qquad a_{EE}<23/30.
\tag{SA.4}
$$

这一比较只读取已经保存的三个数，没有新积分或重跑 SG。
RN 的试探所迫根费下界 $37/30$ 与本次 $a_{EE}$ 已接近总预算 2；
后继仍须把实际低根接收器、高低交叉和 source 全部纳入同一比较。
不得因必要门通过而把任何未算根门置 true。

另一个已成的 [RD 局部漂移](R138-supplement-actual-root-anchored-local-drift-budget.md)
给 $\Gamma_{loc}<1001/1000$；该值不是本次 SG 的前置或被重新求值的目标。
后继 RA 能量变换应消费原 RD 完整球，仍须付其单个平方根因子、
物理 $\Theta$ 与完整 mean 的费用。

## SA.5 输入和全域保存资格

[manifest](../notes/2026-11-20-R138-spectral-body-energy-budget-inputs.json)
13216 bytes，SHA256
`59361c5bc3ca6491e271139c958e82a53acdeed961fd748a5b5118307370ef8f`。
26 当前输入的 bytes/SHA/blob 逐项与原 manifest 相同；5 历史原件为
positive4 加 germ1，准确恢复完整原 native。
旧 X 44737045152、Y 44740320925、GB 44745355257、RS 44758362539
的 actual/execution 四对全文身份与原 success/false scope 都保留。

新分区是原真根 germ 加全部 4650 原 positive 闭行，原 3594 接口仍在；
新完整分区 metadata SHA256 为
`f2e91be724226d0045f9ebddbec3e850b636399ec495f1a8a927d1d7eab04375`。
保守覆盖从根 interval 下端开始只为包围实际正侧，不把它当实际根；
germ 的 $K_-=0$ 仅在原真正正侧使用。所有谱最大值、角 mean、
修补 $4\cdot10^{-18}$ 和同一 $\eta$ 两端点的 Loewner 比较都按 SG 完整实现。

执行记录 5 次 README 检查，首条与末三条完整 receipt 保存且两种 diff 都为空；
它们相对已读规则提交 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`。
没有声称从小文件独立恢复未留存的第二条。
原整体读点、源/worker/hash 与退出值由两份完整结果共同绑定。

本结论仅关闭新的谱体能量和条件性余量数值槽。
真实 $D_H^{-1}$ 的根型、有限容量 Gram、全部根源、正侧全逆、
负侧/mean/$\nu$/matching 与最终固定度量可见闭族均继续未完成。
