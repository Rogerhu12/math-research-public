# R49：完整参考补偿下 Frenet 正根与均值原函数保持

**状态：已证明；纯解析结论，没有新的模型、积分或数值求解。** [R48](R48-exact-reference-compensation-for-mode-extension.md) 以共同竖直均值为假设证明完整表示相同。本条在原实际 Frenet 速度定义下支付这一假设：在同一物理轮廓、材料角图和正根分支内，精确参考补偿保持角向几何，故保持原均值速度及同原点的连续原函数。它不证明新的离散方程成立，也不把跨模式数的浮点评价称为逐字相同。

## 1. 场、坐标和分支的共同条件

在同一物理子午区间 $J=[0,L]$ 与同一周期坐标 $\psi\in\mathbb R/(2\pi\mathbb Z)$ 上，记尚未加入竖直均值的完整位置表示为 $P(s,\psi)$。它包括真实背景、全部有限状态和完整参考 lift，不能只取一个截断状态向量。

旧、新表示满足 R48 的全部共同定义：同一 $\Gamma$、背景、gauge、物理轮廓 $a(s)$、材料角图、同伦值及 $a\chi$ 窗；角基逐块嵌入，状态按 R48 式 (4)、(6) 转移。于是

$$
P_N(s,\psi)=P_M(s,\psi). \tag{1}
$$

这里暂不含任何 $m(s)e_3$。无均值版本的式 (1) 直接由状态项和参考 lift 项的抵消得到，不以尚待证明的共同 $m$ 为前提。

令同一材料角图为 $\theta(s,\psi)$，并使用原实际 `Flow.geo` 的

$$
v(s,\psi)=\frac{\theta_s(s,\psi)}{\theta_\psi(s,\psi)},
\qquad \theta_\psi>0. \tag{2}
$$

以下假设相应导数连续，并且原 Frenet 域条件在讨论点成立。写

$$
\begin{aligned}
d&=P_\psi, & \ell&=|d|>0, & T&=d/\ell,\\
w&=P_{\psi\psi}-\langle P_{\psi\psi},T\rangle T,
& n&=|w|>0, & N&=w/n,\\
\kappa&=n/\ell^2, & B&=T\times N, & a&>0,\\
\alpha&=-\frac{a_s}{a\kappa}, & 1-\alpha^2&>0,
&\beta&=+\sqrt{1-\alpha^2}.
\end{aligned} \tag{3}
$$

符号 $N$ 在式 (3) 表示主法向量；作为下标的 $N$ 表示新模式数，二者按位置区分。主法向量由上述公式确定，不能另换方向；$\beta$ 取与原程序相同的正根。

原 Frenet 速度泛函是

$$
\mathcal W[P;a,\theta]
=\alpha N+\beta B+v\,d. \tag{4}
$$

式 (3)、(4) 对应原 `Flow.frame` 中 `lam,T,nn,N,kap,Bin,alpha,beta` 及 `W=Vnormal+g['v']*d`。本条不假定有限投影已使 $P_s$ 的全部角频率等于这个速度。事实上，式 (4) 是任一满足上述域条件的完整场的确定泛函，独立于它是否已经解出离散 BVP。

## 2. 正根速度保持

**定理 1。** 若式 (1)—(3) 的共同条件成立，则

$$
\mathcal W[P_N;a,\theta]
=\mathcal W[P_M;a,\theta]. \tag{5}
$$

加入任意仅依赖 $s$ 的竖直平移 $m(s)e_3$，不改变这个速度泛函。

**证明。** 由式 (1)，两个场的 $d$ 和 $P_{\psi\psi}$ 相同。因此 $\ell,T,w,n,N,\kappa,B$ 逐点相同。同一 $a,a_s$ 给出相同 $\alpha$；共同的正根规则给出相同 $\beta$。由式 (2)，$v$ 也相同，式 (4) 遂相同。另一方面，$m(s)e_3$ 的两阶 $\psi$ 导数均为零，所以它不进入式 (3)、(4)。证毕。

这是对已给完整场的正根选择和代数运算的结论，不是新的曲率正性证书。若真实候选在某点没有支付 $\ell>0,n>0,1-\alpha^2>0$，不能用本条宣布它在那里有可用的连续正根。

## 3. 原均值规范与连续原函数

原 `height_integral` 对**均匀 $\psi$ 网格**上的 `fr['V'][:,:,2]` 作平均。本条的连续对应定义为

$$
\mu_P(s)=\frac1{2\pi}\int_0^{2\pi}
\bigl(\mathcal W[P;a,\theta](s,\psi)\bigr)_z\,d\psi,
\qquad
m_P(s)=m_0+\int_0^s\mu_P(\sigma)\,d\sigma. \tag{6}
$$

这精确说明所用规范是 $d\psi$ 平均，不暗换成带 $\theta_\psi$ 权重的材料角平均。实际原状态竖直块由非零频率 $\cos(3j\psi)$ 组成，背景和 lift 为平面项，故其未加均值的竖直分量确无常数 Fourier 项；式 (6) 给的正是原实现要补上的竖直均值速度。

**定理 2。** 在定理 1 条件下，$\mu_{P_N}=\mu_{P_M}$。任意两个初始竖直常数 $m_{0,N},m_{0,M}$ 给出

$$
m_{P_N}(s)-m_{P_M}(s)=m_{0,N}-m_{0,M}. \tag{7}
$$

特别地，同一原点 $m_{0,N}=m_{0,M}$ 下，两个连续均值原函数相同。因此 R48 的共同 $m$ 条件成立，并且

$$
P_N+m_{P_N}e_3=P_M+m_{P_M}e_3. \tag{8}
$$

**证明。** 式 (5) 的竖直分量逐点相同，在共同的周期变量上积分即得两个 $\mu$ 相同。对物理 $s$ 积分，并代入两个初值，得到式 (7)、(8)。证毕。

若 $\mathcal W$ 关于 $s$ 连续可微，且可在紧周期区间上交换微分与积分，则另有

$$
m_P'(s)=\mu_P(s),\qquad
m_P''(s)=\frac1{2\pi}\int_0^{2\pi}
\bigl(\partial_s\mathcal W[P;a,\theta]\bigr)_z\,d\psi. \tag{9}
$$

同一性同时保持这两个 jet。原分段光滑实际表示中，若 $a$、材料图、状态及所需混合 jet 在拼缝处连续，并保上述严格域条件，则式 (9) 的结论也连续延伸到拼缝。原 `velocity_s` 中的 $a_{ss}$、$v_s$、$d_s$ 和 $\partial_sP_{\psi\psi}$ 必须由同一完整表示取出；不能仅补位置而把旧径向导数原封不动复制。

## 4. 相同节点求积可得什么

连续原函数与生产求积值是两种对象。原 `height_integral` 先使用给定角点数 $K$ 的均匀网格，形成

$$
\mu_{P,K}(s)=\frac1K\sum_{j=0}^{K-1}
\bigl(\mathcal W[P;a,\theta](s,2\pi j/K)\bigr)_z. \tag{10}
$$

再在每个实际物理区间 $[l,r]$，以及查询点的末段区间，使用同一 Gauss 规则的字面节点 $g_i$、权重 $w_i$：

$$
Q_{P,K}(l,r)=\frac{r-l}{2}\sum_iw_i\,
\mu_{P,K}\!\left(\frac{l+r+(r-l)g_i}{2}\right). \tag{11}
$$

**推论 3。** 若定理 1 的精确完整场同一性成立，并且两次求积使用同一物理分段、查询点、$K$、节点和权重，则在精确算术下，式 (10)、(11) 及原程序按同次序形成的前缀和相同。

**证明。** 式 (5) 在每个共同角点和径向求积点成立，所以式 (10) 的每项相同；再乘同一权重并累加即可。无须假定 $\mu_P$ 是多项式。证毕。

这一推论不证明 Gauss 求积等于式 (6) 的真积分，也不提供它的误差界。它尤其不适用于仅保存旧 `raw.x` 后就默认归一化坐标相同的做法：这里的节点必须是同一**物理 $s$**。固定轮廓重基后的新 normalized chart，应按 [R47/R48 动态接口](../notes/2026-11-18-r47-endpoint-model-and-r48-state-transfer-source.md) 明确转换。

## 5. 实际升模仍须分别支付的部分

本条把 R48 的共同均值条件变成原连续速度泛函下的可证明结论，但没有去掉以下边界：

1. **有限投影。** 定理需要完整场式 (1)。只有 $E Z_M$、控制补零，或在有限角点看见接近，均不足以替代完整 $a\chi\Delta I$ 补偿。中间同伦若再强制改变新标准入口，必须保留 R47/R48 指出的入口变化。
2. **跨模式浮点评价。** 定义核心相同，不保证两个实际反函数、积分、投影或求和次序产生相同机器数。式 (5)、(10)、(11) 的精确算术推论没有为这些误差提供包围。
3. **不同节点或新插值。** 新角点数、新径向分段和从节点另造的 physical quintic 会改变实际计算输入。R48 连续补偿函数一般不在原 quintic 空间，不能把新插值自动代入式 (1)。
4. **新求解后的参数。** 若原 `fixed=True` 求解让 $p_0$ 或任一物理控制改变，则初始化时共同 $\Gamma$ 的条件未必仍成立；冻结轮廓本身不够。它不能被称为 README 第 5 条要求的固定全部物理参数精化。
5. **真实均值、接缝和审计。** 新候选依然执行它自己的原 `height_integral`、完整 metric、实际尾和均值／非均值两 jet 审计。定理不是跳过这些计算的理由，也不构成闭合、全时嵌入、reach 或目标握持比例的证明。

式 (8) 因而是**精确初值函数**的表示保持结论。它既不要求旧有限场已经满足全部未投影 PDE，也不把添加均值解释为消除了旧的非均值 PDE 缺陷。

## 6. 冻结源码依据

本条逐式使用以下已登记实际来源；原环境文件的完整路径与旧执行绑定见 [q060 来源注册](../scripts/resume_closed/q060_cosine_reference_binding.json)，新接口的全部依赖见 [R47/R48 来源准备](../scripts/resume_closed/r47_endpoint_transfer_source_preparation.json)。

| 来源与所用定义 | SHA-256 |
| --- | --- |
| `950f-prefix-adaptive-chart-bvp-v2.py`：`Flow.geo/frame/velocity_s` | `958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe` |
| `950f-prefix-warped-bvp.py`：零系数背景 `base` 与共同角基接口 | `eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70` |
| `fixed_metric_mode3_flow.py`：实际 $a,a_s,a_{ss}$、mode 与 gauge 定义 | `0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5` |
| `curve_stable_prefix_bvp.py`：`CylindricalPrefix.basis` 与 `height_integral` | `e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2` |
| [完整 lift](../scripts/resume_m3/round_raw_lib/exact_core_lift.py)：$a\chi$ 与所有所需角／径向 jets | `28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5` |
| [连续转移源](../scripts/resume_closed/r48_reference_state_transfer.py)：真实 physical PPoly 与三块补偿 | `fe7decedceb9b20d9fa70715a40494b24670f40dd28a4c88fc80033d7a14610a` |
| [R48](R48-exact-reference-compensation-for-mode-extension.md)：无均值场抵消与共同定义 | `aeeba196670c81f7f22554af827e44658cb23aa59d50df0afe66889244faed49` |

证明过程中只读上述原定义并核源码哈希，没有构造模型、求根、积分、谱采样或重新运行任何已登记数值结论。
