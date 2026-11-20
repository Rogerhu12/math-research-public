# R679　角网格倍增的正权分解、共同旧角归因与固定场的一致性

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence，AI 辅助研究。**状态：完整的条件代数/分析结论及最小入口设计；没有执行新科学计算。** 本条固定实际径向节点、observation carrier、$M$、全部自由变量布局、精确 $g$、帽、$\lambda/\eta$ 与步长母范数，只讨论实际全角数 $N\to2N$。没有新 candidate、driver 或 Actions 预算。

与 [R676](R676-fixed-metric-refinement-and-complete-observation-transfer.md) 的一般共同父比较相比，新增内容是均匀角倍增的**准确偶/奇正权分解、quarter 端点权、梯度/残差 Hessian 分解、固定场角最大值单调性及带明确导数常数的一致性界**。与 [R678](R678-frequency-only-refinement-and-identical-parent-functional.md) 不同，$N$ 增加时自由空间不扩大，单个旧点的归一权确实改变，故不能沿用“同一个有限 Phi”的说法。

## 1. 固定的物理问题与有限观察问题

固定一个原 fullclosed 场，或 canonical R671 场

$$
F(s,\phi)=q(s,\phi)+f_\lambda(s)e_r(\Theta(\phi))
+\bigl(h_\lambda(s)H+k_\lambda(s)\bigr)e_z.
$$

同一精确 FullHold 定义、$S,R$、符号节点 $\alpha S+\beta$、shared-quintic $q$、$M$、fixed/free core、帽/marker、$\lambda$ 和两个准确 $\eta$ 端点全部保留。$\rho=\Theta_\phi>0$ 是原物理角图册条件。本条不以有限新角值宣称其连续正性已付。

径向观察点及其 literal target $a_i>0$、正权 $w_i>0$ 保留，包含全部原 node/mid、Gauss 和 retained rows。这里 $a_i$ 与参考 profile 使用实际父的同一载体约定；有限函数与准确连续 $a(s)$ 的费用仍分别记录。连续标量并未插值，也未改变目标 $g$。

令 relative Gram 为

$$
\mathcal E_i(\phi)=
\begin{pmatrix}
|F_s|^2-1&F_s\cdot F_\phi/(a_i\rho)\\
F_s\cdot F_\phi/(a_i\rho)&|F_\phi|^2/(a_i\rho)^2-1
\end{pmatrix},
\qquad
q_i(\phi)=\|\mathcal E_i(\phi)\|_{\rm op}.
$$

沿用 [R660](R660-positive-spectral-Gram-blocks-and-maximum-control.md) 的 $p=8$、$\varepsilon=.001$、$c=.05$，写成没有特征值分支问题的多项式

$$
\ell_i(\phi)=
\operatorname{tr}\left(
\frac{\mathcal E_i(\phi)^2+\varepsilon^2I}{c^2}
\right)^4.
$$

设 $N=4L>4M$。原全角为 $\phi_j=2\pi j/N$，新全角为 $\phi'_j=2\pi j/(2N)$。取原径向权总和 $W=\sum_iw_i$，定义

$$
\Phi_N(x)=\frac1{WN}\sum_iw_i\sum_{j=0}^{N-1}\ell_i(\phi_j;x).
$$

这仍是原求解器的均匀 **$\phi$** 观察目标；没有改成带 $\rho$ 权的材料 $\theta$ 积分。目标尺度保持 mean Phi，平滑零残差下界 $2(\varepsilon^2/c^2)^4$ 与 $N$ 无关。

$N>4M$ 是当前有限 $q$ 的 FFT/DCT 合成条件；Gram 的乘积、更高次的谱 loss 和完整解析 lift 并没有因此被证明截在同一频带。不能把这个构造条件当作角求积准确性或连续峰已解析的证书。

## 2. 准确偶/奇分解与 quarter 权

### 定理 679-A

保持同一实际场 $x$、径向 carrier 和目标参数，令

$$
\Phi_N^{\rm odd}(x)=\frac1{WN}\sum_iw_i
\sum_{j=0}^{N-1}\ell_i\left(\frac{(2j+1)\pi}{N};x\right).
$$

则准确有

$$
\boxed{\Phi_{2N}(x)=\tfrac12\Phi_N(x)+\tfrac12\Phi_N^{\rm odd}(x).}
\tag{679.1}
$$

同一个场的全部新样点最大值满足

$$
\boxed{Q_{2N}(x)=\max\{Q_N(x),Q_N^{\rm odd}(x)\}\ge Q_N(x),}
\tag{679.2}
$$

其中 $Q$ 对所有固定径向观察点和相应角集合取 $q_i$ 的最大值。

**证明。** 新全角索引偶数列为 $2j$，且 $\phi'_{2j}=\phi_j$；奇数列给另 $N$ 个点。将新全角和按奇偶拆开，归一分母从 $WN$ 变为 $2WN$，得到 (679.1)。点集是两个不交子集的并，得到 (679.2)。没有插值或有限 spectrum 截断。□

[R653](R653-exact-quarter-angle-closed-Gram-reduction.md) 已付原模型的准确 quarter 归约。其 Gram 对角项为 $\pi$ 周期偶函数，交叉项在相应反射下变号；$\ell_i$ 与 $q_i$ 都在该共轭下不变。因此可在 quarter 上逐字实现上式：

R671 更换的 $f/h/k$ 都是纯径向函数，$hH+k$ 位于 $Z_0$；同一角奇偶关系仍直接成立。

| 项目 | 原网格 | 双倍网格 |
|---|---|---|
| 实际 full N | $N=4L$ | $2N=8L$ |
| quarter 列数 | $L+1$ | $2L+1$ |
| 角列 | $\pi k/(2L)$ | $\pi k/(4L)$ |
| 原列映射 | $k$ | $2k$，准确整数映射 |
| 两个端点 multiplicity | $2$ | $2$ |
| 其余 multiplicity | $4$ | $4$ |
| 奇数新列 | 无 | $1,3,\ldots,2L-1$，均为 $4$ |

新偶数子集的 multiplicity 总和仍是 $N$，新奇数子集的总和也是 $N$，全部新网格是 $2N$。故 odd 统计自己的归一分母也是 $WN$，不能把它误除以 $2WN$ 后又在 (679.1) 中乘一半。

在 quarter 区间 $[0,\pi/2]$ 上，旧归一规则恰为复合梯形规则，odd 是同一旧角胞的复合中点规则；细一层梯形规则为两者的一半和。这是正权规则之间的准确恒等式。

每个旧样点的新归一权是原来的一半，全部旧点仍保正权。由于径向最小权相同，

$$
w_{\min,2N}=\tfrac12 w_{\min,N}.
\tag{679.3}
$$

消费 R660 的 finite-max 上下界时须使用新的 $w_{\min}$，不能沿用旧权下界。Phi 可以因采样改变而增或减；即使新旧 Phi 很接近，也没有由此付清角间连续峰。

### 2.1 梯度与正残差 Hessian

所有变量和物理模型固定，且 $\rho>0$，故逐点可微。对 (679.1) 微分即得

$$
\nabla\Phi_{2N}=\tfrac12\nabla\Phi_N
+\tfrac12\nabla\Phi_N^{\rm odd}.
\tag{679.4}
$$

把 [R664](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md) 的每点正残差 Hessian 拉回矩阵按角点求和，同样有

$$
K_{2N}=\tfrac12 K_N+\tfrac12 K_N^{\rm odd}.
\tag{679.5}
$$

这里 $K$ 仍是已刊的残差 Hessian 拉回部分，不宣称它等于完整变量 Hessian；真实 gradient 保留原公式。使用已含 orbit 的 native residual/J 时，先按原约定解除或正确使用 orbit，不能再加一次 multiplicity；spectral 三块已经包含其自身 Frobenius 交叉因子，也不额外乘一遍 $\sqrt2$。

N-only 的自由空间与正则范数不变，数据目标改变，所以新的最优值没有与旧最优值单调排序的结论。式 (679.2) 只针对**同一个固定场**；优化后场改变时须实际重新比较。

## 3. 固定场的角一致性及其准确边界

### 定理 679-B

假设固定有限场在所读全部径向点上具有连续角图册 $\rho(\phi)\ge\rho_*>0$，并有已知有限常数

$$
B_2=\frac1W\sum_iw_i\sup_\phi|\ell_i''(\phi)|,
\qquad
L_E=\max_i\sup_\phi\|\partial_\phi\mathcal E_i(\phi)\|_{\rm op}.
$$

令

$$
\Phi_\infty=\frac1W\sum_iw_i\frac1{2\pi}\int_0^{2\pi}\ell_i(\phi)\,d\phi,
\qquad
Q_\infty=\max_i\sup_\phi q_i(\phi).
$$

则

$$
|\Phi_N-\Phi_\infty|\le\frac{\pi^2}{3N^2}B_2,
\qquad
|\Phi_N^{\rm odd}-\Phi_\infty|\le\frac{\pi^2}{6N^2}B_2,
\tag{679.6}
$$

$$
0\le Q_\infty-Q_N\le\frac\pi N L_E.
\tag{679.7}
$$

因而沿 $N,2N,4N,\ldots$，固定场的角样点最大值单调趋于 $Q_\infty$，均值规则趋于同一 $\Phi_\infty$。

**证明。** 对一步长 $h=2\pi/N$ 的区间，线性插值积分与准确积分之差不超过 $h^3\sup|f''|/12$，中点规则之差不超过 $h^3\sup|f''|/24$。对周期全部 $N$ 个胞相加、除以 $2\pi$，再按正径向权平均，得到 (679.6)。周期首尾值相同，所以原均匀点平均等于复合梯形规则。

对任意对称矩阵 $A,B$，$|\|A\|_{\rm op}-\|B\|_{\rm op}|\le\|A-B\|_{\rm op}$。每个角点距最近均匀样点的圆周距离至多 $\pi/N$，沿短弧积分 $\partial_\phi\mathcal E_i$，得到 (679.7)。取最大值后常数仍为 $L_E$。样点集合逐层包含给单调性，右端趋零给极限。□

这些正则性在本有限模型中有直接含义：径向 shared-quintic 片固定后，$q$ 为有限角多项式，$e_r(\Theta)$ 是保留完整尾的解析角函数；只要连续 $\rho$ 有正间隙，relative Gram 与上述 trace 多项式在角上光滑。这里不要求一般 $C^2$ 曲面额外具有全部径向三阶导数；它使用当前明确 ansatz 的角正则性。

**没有在本条计算或付出 $B_2,L_E$ 的实际向外上界。** 所以 (679.6)—(679.7) 当前是可消费的条件界，不是任何新父的连续证书。$Q_\infty$ 也只覆盖已固定的径向观察点，径向胞间仍由已有完整连续核处理。

仅用相邻两层均值之差不能冒充严格误差界。例如光滑正函数 $1+\epsilon\cos(2N\phi)$（$0<\epsilon<1$）在 $N$ 与 $2N$ 规则上都给 $1+\epsilon$，准确均值却为 $1$。该例说明一般正权角规则的差值本身不支付余项；不宣称这个示例就是当前 candidate 的 Gram loss。

对一串**变化的**求解场 $x_N$，上述 fixed-field 收敛也不自动推出 $\Phi_N(x_N)$ 或连续度量误差趋零。需要同 $g$/模型的实际求解进展及相应连续覆盖，不能把观察一致性替代 README 的解精化标准。

## 4. 旧角的准确索引与 binary 位置

数学角的映射是 $k\mapsto2k$，不通过 nearest-angle 搜索。旧记录若给 quarter index $k$，其准确理想相位为 $2\pi k/N$；新索引 $2k$ 表示同一点。实际永久位置仍保原记录的 binary $\phi$，不先 round13、不归一到更粗小数、不因新 grid 很近就合并。

冻结 quarter 源的 literal 公式为

```text
phi = np.pi * arange(N/4+1) / (N/2)
```

在普通 binary64、整数索引可准确表示、无溢出/下溢且按该同一公式求值时，倍增后的偶数列是逐字相同的角载体。理由是乘积由 $\widehat\pi k$ 变为 $2\widehat\pi k$，正常数舍入与准确二倍缩放交换；随后分子、分母都乘二，商同值。$k=0$ 单独仍为零。此结论**不**表示两种长度 DCT/DST 的场合成或 residual bitwise 相同。

将来的实际 reader应同时记录数学映射和实际角数组是否相等。若实际环境的角载体生成政策不同，仍须保旧 literal $\phi$ 并用旧角准确读出；不能默认为相近角等于原材料位置。这里没有为角误差新增任意阈值。

完整位置导出继续使用已刊 `Locations`，但它必须用**父的旧 full N** 初始化，先把全部旧 `stage/angle` 编码解析为原 `cell/u/phi`，然后才给新 driver 的 $2N$。旧 arbitrary 点的 binary 值直接保留。合并所有 supplied manifests、最终 memory、trial 新点、source locations 和 protected representatives，保 round 前仍能恢复的不同位置；已经在历史上彻底丢失的信息不能伪造恢复。

源若记录了显式 $\phi$ 和 grid index 两种来源，应分别保其 provenance；不要把 float $\phi$ 强制投影到新 grid。新报告以后出现的新 grid index 则由它自己的 $2N$ 解释。原 radial carrier 不变，stage 到 cell/u 的映射也不变。core 不变的转移时刻，$\Theta(\phi)$ 及真实材料位置同样不变。

## 5. 完整方向范数及 $\mu$ 的单位不变

固定 $M$ 和原 mesh 后，DI 的 $h/\omega$、endpoint Gram 各块、angular-H² 的 $\nu/\nu_c$、physical-height 的 $\sqrt{7S^3/120}$ 都不依赖 $N$。原或 R671 的高度补偿 $b-\chi$、$b-h_\lambda$ 仍是同一纯径向 $Z_0$ 列。

保持 coarse low modes 与 centers 时，nodal $B$、`free_direction`、完整 inverse/scale Gram 和白化也不依赖 $N$。coarse 的角缓存会随新角网格重新生成，但不是这些物理方向及母范数的定义。因此 R678 的母范数和带 coarse 的最小商范数在本条中逐字是同一个数学范数。

完整 driver 的 $N$ 进入 $C_0=W N$、角观察与归一 normal/gradient；代码不会另乘或除 $\mu$。末 $\mu$ 从实际自然父报告恢复后，仍乘同一个 $\|z\|^2$。不按新行数人为乘二或除二 damping。新平均目标可能需要后续实际 trust 更新，这由冻结 driver 的原回溯规则处理，不能从行数变化预设最优 $\mu$。

## 6. 原/R671 径向 profile 的复用条件

原 polynomial lift 的所有 scalar profile 只依赖 $s,S,R,\mathrm{width}$。R671 的完整 $f,h,k$ 三 jet profile 也只依赖径向位置、原 scalar、$\lambda/\eta$；与 $N$、quarter、stage block 无关。

冻结 factory `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216` 的 canonical `definition()` **没有 N 字段**。它绑定 $M$、mesh、node report、原 observation carrier、scalar、$\lambda/\eta$ 和来源；保存的 profile/reference/observation 数组也都是径向数组。因此 N-only 不需要 R678 那样的新 $M$/node report 身份，输入 bundle、node report、observations 可原文件复用。

对于 canonical $\lambda=0$ 和非零 $\lambda$，已有 profile 能继续给相应连续 reader 使用，条件是：

1. 实际 bundle、当前 definition、$M$、mesh、node report、原 observation carrier、scalar、$\lambda/\eta$ 和 source 绑定一致；
2. profile 的 `model_definition_json` 逐对象等于该当前定义，所需径向数组与 mesh/位置匹配；
3. bundle 的 `reference_tail_carrier_sha256` 确实指向所给实际 profile 文件。

这些条件并不受 $N\to2N$ 影响。然而当前 `TailLiftContext.from_files/create_pair` **没有读取已有 profile 的缓存参数**：完整 driver 仍会构造其 tables，在相同径向点重取/缓存原整数 oracle 数据。连续 reader 的 `_load_profile_anchors` 才是已有显式 anchor 入口。这是“同 profile 数学上可复用”与“当前求解 factory 已实现该性能复用”的区别。

最小 N-only 衔接可直接使用冻结 factory，不先扩它的缓存 API。若 driver 重新保存 profile，必须使用实际新输出的 SHA；不得给新 SHA 配旧文件。即使数组完全相同，NPZ 文件身份也不能凭数学相等推定。将来若增加显式 profile 缓存消费者，应独立注明其源和全部上述绑定，不改 frozen factory 或伪造 metadata。

profile 复用仅支付同一标量/模型输入。它不支付新角上的曲率、支持、rho 正性或新 candidate 的连续度量。新角可能显露旧 grid 漏掉的峰；初始新 grid 过滤不通过时应如实返回，不能复制旧 finite flag。若此前有同一准确场且同身份的完整连续证明，其数学覆盖范围本来不依赖有限 N；仍须引用那条真实证明，而非把旧有限采样升级为连续证书。

## 7. 最小可实现入口设计

本条暂不写新大 driver。建议下一独立入口 `launch_angle_only_fullclosed.py` 复用已刊的自然父 helper、完整位置导出与 manifest-only AST 派生，保 frozen 原/R671 full driver 字节。执行流程明确如下。

### 7.1 prepare：只读完成报告和源身份

输入为真实 complete full/fine 报告、其 final bundle、实际 carrier/node/scalar、全部旧 manifests，以及派生父的实际 source。先绑定源完整 AST/末更新规则与 `final_bundle_sha256`，再恢复末 $\mu$；默认继承真实 QP module SHA，也可显式选择并单列。

核原 $N$、$M$、$J$、全部行数及谱目标参数，声明 $N'=2N$。保持径向和 field 文件路径、SHA；保持所有 free variables、low modes、coarse centers、母范数、$\lambda/\eta$、同尺度 damping 和实际几何政策。只把 full driver 的 `--angles` 变为 $2N$。不生成补零 seed，不重新保存 node report，不调用 R676 factor=1，也不新增或重混径向权。

完整位置先按旧 $N$ 导出准确 tuple，并绑定同 carrier。所有实际数组读取与执行继续只在公开 Actions。本文没有给这条设计分配实际方向数、运行时长或机器预算；若后续决定做一个完整方向，其算法参数和 source 仍须从该真实父明确记录。

### 7.2 必要归因读取：同一个新网格 buffer 的三份统计

冻结 full report 当前只记 all-grid Phi/max，没有 even/odd 独立统计，不能在纯 report 层凭空恢复。最小实现可保 driver 不动，在它自然返回后用一个小的**共同角 reader**读取实际父和实际 final 两个自由向量：同一个 $2N$ operator、同一个径向/profile 定义，逐 stage block 读全部 first jets，形成一份未加 orbit 的 raw Gram buffer。每个 buffer 同时计算：

| 统计 | 角列 | 自己的归一分母 |
|---|---|---|
| common old N | 新列 $0,2,\ldots,2L$ | $WN$ |
| genuinely new odd | 新列 $1,3,\ldots,2L-1$ | $WN$ |
| all new 2N | 全新 quarter 列 | $2WN$ |

同一份点态特征值/损失数组分区，记录各自 Phi、Frobenius 读数、max、worst stage/cell/u、旧/新 angle index、literal $\phi$ 和理想相位分数。这样 all max 与两个分区 max 的关系来自同一次数据评价，避免 R676 归因中“new-only 未单列”的缺口。

reader 不重扫连续证书，也不重算同报告已给的曲率场；其必要新信息就是这两个候选的 even/odd 分区。只构造一个当前 operator/profile 后依次 pack 两个向量，保同算术路径。若未来要省去这两次独立 first-jet 读取，可另显式发布仅附加统计字段的 driver 版本，从本来已有 residual buffer 取分区；不能暗改已冻结 driver，亦不能把未知派生体冒成当前末 $\mu$ helper 已知的 source。

若自然终态的自由向量与父逐字相同，reader 可以只读一次该实际场并明确记录复用，不能把两个文件名算成两个不同物理候选。

初始/终态 native driver Phi 仍各自按实际报告保留，独立 reader 的 float 求和顺序与 driver 不一定逐字一致。源应注明这项普通数值差异，不为压到某个任意阈值重复跑读者。

### 7.3 报告必须区分的比较

| 比较 | 可说明什么 |
|---|---|
| 父旧报告 $\Phi_N$ 与 reader 父 even Phi | 同一旧网格、同一物理父的不同合成/求和路径差 |
| reader 父 all 与父 even | 同场角规则改变；由 odd 分区解释，不算求解改善 |
| reader final even − reader parent even | 真正共同旧 N 的同函数变化 |
| reader final odd − reader parent odd | 新补角集合上的同函数变化 |
| reader final all − reader parent all | 真正同新 2N 目标的求解变化 |
| all/even/odd 的各自 max 与最坏点 | 明示新增角是否揭露此前漏峰 |
| 新 grid 初始/终态几何过滤 | 实际当前值，旧有限 flag 不继承 |

禁止用 `final Phi_2N − parent Phi_N` 作为单独的求解下降量。实际未返回任一必要候选/读出时，相关比较列为未付，不从别的 report 推造。全部原永久位置及新报告所发现的位置继续完整保存，raw 只留 runner。

## 8. 与精确时间相位、README 完成标准的关系

odd 角集是 chart $\phi$ 的半步补点。一般 $\theta=\Theta(\phi)$ 非线性，所以它**不是**材料角 $\theta$ 的固定时间相移；不得把 odd 统计冒作 $t$ 的新采样试验。

[R248](R248-finite-C2-phase-family-and-global-reductions.md) 的准确共同相位族及整面 sup 恒等式继续直接使用，不重设 t-grid 门。其结论涉及完整空间上确界；有限均匀 $\phi$ 点集通常不在任意材料相移下不变，因此它也不保证 finite Phi 对所有相位逐字相等。

N-only 改的是观察分辨率，不扩大 $M$ 所定义的场空间。它有助于发现角漏峰并在相同有限模型中继续求解；README 的频率精化仍由真正 M-only 空间扩展推进，径向精化仍由同 $g$ 的准确节点转移推进，所有实际场须给完整连续 metric/geometry 范围及必要网格导出。一次 N 倍增或固定场的角求积一致性均不宣称持续解收敛、$10^{-6}$ 连续等距或课题完成。

**本条已证明 (679.1)—(679.7) 及相应接口不变量；所有新 N 实际数值、连续常数和求解成效均尚未执行/未付。**

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
