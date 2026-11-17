# 内向真前缀的新有限右边界：首109项遗漏高度速度谱

2026-11-17，Astra-larger-parallel-16f63c8b / constructive_model。

**实际数值证据；尚无新 BVP 接受态。** 本条登记一个新边值问题与已执行的边界导数 probe。它固定原内向标量剖面，保留全部338个 Frenet ODE，将原右端的109个 principal 行替换为109个未投影 $V_z$ 的遗漏余弦系数零约束。这是明确的新有限边界，既不继承原 terminal 条件，也不称为真实无限尾 DN。此时完整 BVP 已启动，有限终态将另行追加，不把启动或满行秩算作收敛。

## 1. 完整问题与固定标量剖面

真接受父文件为仓库外 `parallel-inward0997-m112.json.gz`，SHA256：

```text
11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327
```

保留其 $M=112,N=2048$、整个区间 $[0,.997]$、全部状态和固定前三 core 参数，仅把它用作新问题的初猜。`duration=0`，没有声称把原问题延长。

采用同一个 `inward_scalar_profile`：在 $s=.995$ 之后使用曲率1.5的内向定义，两侧 ramp 长度均 .02，过渡积分 GL32；保留原 `fixed_scalar_profile`、`analytic_extension_origin=.99`。这份标量定义的参考平端在 $s=2.2847166467351667$，不表示当前场已经到达那里。

高阶core仍是未知，因此计算角φ下的rho并非逐点固定。[R240](../results/R240-canonical-material-metric-and-refinement.md)给出在rho>0时经各自固定原点材料换元后的共同规范目标g=ds²+a²dΘ²；本次尚未完成共同材料网格的六jet收敛检查，更没有完整闭面同g结论。

浅端保持原来的229行：$A_0=1$，前三个 $A_j$ 固定，112个 $B_j+2jA_j=0$，以及113个 $Z_j=0$。所有 $3M+2=338$ 个方程

$$
y_s=\operatorname{Proj}_M V(y,a'/a)
$$

继续完整进入 collocation，未删高度、低频或任何 Fourier ODE。

新的右边界为

$$
\mathcal B_j(y(.997))=
\frac{2}{N}\operatorname{Re}\operatorname{FFT}
\bigl[V_z(y(.997),a'(.997)/a(.997))\bigr]_{2j}=0,
\quad j=113,\ldots,221. \tag{1}
$$

$V$ 是 `q.local(...)["V"]` 的未投影速度，先取全2048角样本，再提取这些系数。最大角频442严格低于 Nyquist 1024，没有端点频率碰撞。229浅行加109右行恰为338行；它并未把原投影后的零高模误写成新约束。

## 2. 同一有限 FFT 函数的导数

[新源](2026-11-17-parallel-model-inward-omitted-velocity-bvp.py)调用冻结的 `Frenet.local/variation` 求 $V_z$ 对角向一、二阶 jet 的六组逐点偏导，再作有限 FFT 卷积。输入模式仍为原112个余弦/正弦状态；只将输出频率改为 (1) 的226至442偶数频率。对实余弦输入使用正、负频率核的半和，对实正弦输入使用 $(-iK_++iK_-)/2$，输出统一取两倍实部。

导数 probe 直接对同一个字面边界做五个随机方向复步，步长 $10^{-28}$。实现对实 FFT 余弦泛函作复线性延拓，即分别 FFT 复场的实部与虚部，避免 `real(FFT(...))` 把复步导数丢掉。

初始实际结果：

| 量 | 数值 |
|---|---:|
| raw 边界最大系数 | $7.94497171537\times10^{-6}$ |
| Jacobian 维数 | $109\times338$ |
| 最大奇异值 | 7890.57574833 |
| 最小奇异值 | $.000142489640554$ |
| 原矩阵条件数 | $5.53764871441\times10^7$ |
| 按行归一化后的条件数 | $4.47879717447\times10^7$ |
| 行范数范围 | 129.831057831 至6344.55748934 |
| SVD 数值秩 | 109，阈值 $5.92196203838\times10^{-10}$ |
| 五方向最大相对无穷范数误差 | $9.58523113670\times10^{-15}$ |
| 五方向最大绝对误差 | $2.95941049444\times10^{-12}$ |

五个相对误差依次为 $4.87,4.15,7.70,9.59,2.87$ 倍 $10^{-15}$。这些检查支持所实现 Jacobian 确实微分了 (1)，但原行已经高度病态。满行秩不保证与整段 ODE 传递后的全局边界问题可稳定求解；实际 QR 的末端缩减矩阵还可能更病态。

由于按行归一化没有明显改善条件数，本次实际求解**不归一化**右行，保留 raw 余弦系数，`bc_tol=1e-11` 也直接作用于它们。输出同时保存每项 raw 系数，不以缩放残差替代实际边界误差。

## 3. 冻结源与实际命令

新源 SHA256：

```text
d6b9f58cf75f2e9dc0aa6777263d901edd71f4e5216eff3bbe82c59c8782b4eb
```

其余关键依赖保持冻结：Frenet symbol `7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831`，continue `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`，inward profile `1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0`。driver复用现有 `feasible_newton`、全部 `q.jacobian` 和 separated QR 实现，不改已冻结的源。

从仓库根执行已完成的 probe：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-inward-omitted-velocity-bvp.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-inward-omitted109-probe.json \
  --probe-only
```

probe报告 SHA256 为 `61f713081941a003fedf0d3f546c070e60dffeadeff5bbe043a619b7289b8ada`。运行时间字段使重跑 JSON 字节可变，公式、全部输入与逐项数值保留在报告中；可再生 raw 不入库。

随后实际启动的完整 BVP：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-inward-omitted-velocity-bvp.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-inward-omitted109-bvp.json.gz \
  --tol 1e-8 --max-nodes 1800
```

输出定义明确绑定新边界种类、输出频率、raw尺度、输入 SHA 和同一个 inward scalar profile。若出现真接受场，实际 $C^2$ quintic 读出须使用冻结的 `scripts/parallel_20261117_prefix_inward_readout.py`，不能用仅认识旧 Profile 的读取程序。当前没有接受、Gram、全 $t$、闭合或 reach 声称。

## 4. 完整 only-Z 零目标 BVP 的实际有限终态：未接受

上述原始命令已执行至其设定的 `tol=1e-8, bc_tol=1e-11, max_nodes=1800` 有限终态，未修改运行源或扩大预算。输入始终为接受父 `11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`，原338个ODE、229个浅行与新的109个 raw $V_z$ 零目标行全部保留。

网格由510点加至1457点。第二轮要求再加2815点，超过1800点总预算，返回 `success=False, status=1`（maximum number of mesh nodes exceeded）。最终完整 collocation RMS 为 $8.424855169493225\times10^{-5}$，全部边界残差与109个 $V_z$ 系数最大值同为 $1.599867002296410\times10^{-6}$，分别仍远高于本次设置。109个目标系数的最大值虽由初始 $7.94497171537\times10^{-6}$ 降低，但没有得到新接受解。

本次共有16次完整 QR 因子和16个接受的阻尼 Newton 步；约化矩阵条件数介于 $4.02970587331\times10^{10}$ 与 $6.33923324362\times10^{11}$。接受若干 Newton 步不等于整个 BVP 已收敛。运行约1741.58秒；结束原因是已声明的节点预算，不是按时长中断。

未接受终态的辅助读数：保持原前三 core，但其余 core 已变化，采样 $\rho_{\min}=.164006587994$、轴向 core gap $.959319925100$。用同一个冻结 `OmittedRows` 在真实末状态上读取全部327个候选系数，R/T/Z 三组最大绝对值分别为 $2.16171182905\times10^{-5}$、$3.08573543812\times10^{-6}$、$1.59986700230\times10^{-6}$。这里只报告未接受终态的有限谱，不把它当成实际等距误差、reach 或可接帽几何。

完整 raw 输出 `parallel-model-inward-omitted109-bvp.json.gz` 的 SHA256：

```text
6d339813bb4f12d6839b7f630081560fd885933b4e6db514d6b359f2d34a43d6
```

源仍为本条已冻结的 `d6b9f58cf75f2e9dc0aa6777263d901edd71f4e5216eff3bbe82c59c8782b4eb`；原命令、原接受输入和内向 scalar 定义均保持不变。没有对该未接受场运行要求接受态的 quintic 读者，也不把它用作后继接受父。下一有限试验将从原11960350父重新出发，使用另行定义的固定 $U^T$ 全327谱组合与固定母向量的 $\beta=63/64$ 目标；这与本次 only-Z 零目标是两个明确区分的边界问题。
