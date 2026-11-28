# R87 首个恢复后正参数场的真积分核心实际返回

本条使用恢复后的真实原门接受场 $\lambda=\operatorname{float}(0.002)$、
$M=16$，完整重算其真积分核心。它支付当前核心的角域与归一化责任，
不复用旧 $q=0.06$ 场或旧低参数核心的数值界。

## 来源与实际调用

真实输入为
`R87-strict-recovery-20261128/lambda002_m16-from-unaccepted/run.json`，
SHA256 为
`754987d85ec08772adcfb216bb4c2f3599b1ebe83c08ccad842e7c68c110b782`。
本次调用重新执行未经修改的 `accepted_original`，核对源、全部原门、
完整 1051 节点返回和物理文件，并重新绑定：

- 原 `inner-00.npz`：`ca544c75c6cf95277103a1210d828e77b973e6a04261faf4a8d7188cc7d3ae0e`；
- 物理 `physical.npz`：`01b5c057250c19a49e2202ba32cd922e3c2210ed8e7bd6bcef2935842b7c4380`。

独立入口为
`scripts/resume_20261128/analytic/certify_r87_actual_true_core.py`，
SHA256 `a9f3b280cab1feab6eebcae8963f3b197f701583c74775cfbe5561d30bf61604`。
实际命令：

```sh
python -u topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/certify_r87_actual_true_core.py \
  --source-run /workspace/scratch/7c4e33ee17de/held10-design-work/R87-strict-recovery-20261128/lambda002_m16-from-unaccepted/run.json \
  --original-core-source /workspace/scratch/7c4e33ee17de/held10-design-work/multistage-source/notes/fixed_metric_mode3_core.py \
  --outdir /workspace/scratch/7c4e33ee17de/held10-analytic-work/r87-lambda002-m16-true-core-20261128-a
```

工具 TTY `40407` 实际返回 exit 0，终态块 `7f1290`。
进程内时间 40.745686895999825 秒，实际峰 37640 KiB。
仅重建完整 16 系数小核心，没有构造前缀均值、全 Jacobian、BVP 或尾端。

## 沿用的精确定义及本次实际重算

原 `warm_phase_validated_core.build_oracle` 已经包含一般 $S,b,k,\lambda$
的真积分定义。它的零 phase 控制特化恰好是原 R53 material-support
核心。本次明确取 `controls=[0]`，没有把源场重标成 phase 场，也没有
新增物理控制。记录保留原 oracle 的元数据以及这一特化的实际作用。

所有原支持系数均按真实 binary64 数的精确有理数解释；本次的
$S=\operatorname{float}(0.675)$、$b=\operatorname{float}(0.3)$、$k=1/2$
和正参数也同样处理。三重扇区是真实 $T=2\pi/3$，并非把浮点
`2*np.pi/3` 宣称为精确周期。

既有证明的本次执行依次重算：

1. 完整支持系数给出的实反函数与复解析条带；浮点原反函数仅作种子，
   每个种子仍由向外舍入残差与 Taylor 余项包围。
2. 真正窗口加权积分与 $\beta$；不把源的 GL12 / 24 格补偿值当真积分。
3. 真正位置积分；原 GL12 节点、权重的有理包围和完整解析余项全部付入。
4. 三重闭合归一化与完整扇区曲率三 jet。

位置定义为

$$
z_0=\frac{\int_0^T i e^{i\phi(u)}\,du}{e^{iT}-1},
\qquad
\Gamma(u)=z_0+\int_0^u i e^{i\phi(v)}\,dv.
$$

故 $\Gamma(T)=e^{iT}\Gamma(0)$，三次旋转闭合；导数遵守同一扇区
旋转关系。反射对称性证明真 $z_0$ 为实数。本次另核完整区间虚部含零，
没有丢弃某个浮点虚坐标并冒称精确闭合。

逆函数 Taylor 次数为 24，实际 `cells_per_unit=128`；位置分区有
276 个真实扇区格。全部原角域格的曲率区间实际返回，无未决格。
这不是通过有限采样猜测全角范围。

## 实际结果

真补偿与真归一化实坐标的区间为：

$$
\beta\in[1.7622656090333364,\;1.7622656090336268],
$$

$$
\operatorname{Re}z_0\in[1.0122237535159064,\;1.012223753516333].
$$

完整报告同时保存每个端点的精确二进制有理数，以上十进制仅用于显示。
归一化虚部一致性区间为
$[-2.0102438232546227\times10^{-13},\;2.0072832285222888\times10^{-13}]$。

源中记录的有限 GL 补偿值重新生成后逐位相同，并且由真区间得到

$$
|\beta_{\rm finite}-\beta|
\le \frac{665}{4503599627370496}.
$$

独立正权逆函数积分证书与这个真积分 oracle 的 $\beta$ 区间相交。
该相交检查用于交叉核对；任一严格区间本身的证明并不依赖另一结果。

全角向外舍入界如下：

| 量 | 本次严格区间或上界 |
|---|---:|
| $\kappa$ | $[0.9114460782935574,\;1.1088736702108144]$ |
| $|\kappa_u|$ | $0.308277142233272$ |
| $|\kappa_{uu}|$ | $1.4128908792183754$ |
| $|\Gamma'''|$ | $1.2297010062178115$ |
| $|\Gamma''''|$ | $2.7766046605273806$ |
| 完整覆盖格 | 276 |
| 未决正曲率格 | 0 |

源 SHA、完整系数、条带半径、所有求积常数和精确端点保存在实际报告
`held10-analytic-work/r87-lambda002-m16-true-core-20261128-a/summary.json`，
SHA256 `f81f8a66c2d85793fd0999e368071d70125b65701ef9d040fd7b0432e506804c`。
旁边的 `scalar-normalization.json` SHA256 为
`a8d1d738a17a6a3dd77e009d503e3ae11b3b1cc4cab4c6291e716136d4351dda`。
小记录副本随本说明入库；不保存中间 oracle 数组。

## 对后继的精确作用范围

既有 `AngularRanges` 采用的就是同一零 phase 真积分入口，因此新的
R87 参数没有落入旧 `r53_validated_material_core` 狭窄 $k=0.2,S=0.5$
初始化门。完整连续几何必须继续使用真 oracle 对 lift 和中心修补的
贡献，不把源 `core.evaluate` 的有限位置积分当数学定义。

本条没有证明有限浮点位置程序在每个实角度的导数等于它返回的 jet；
没有把这次核心界搬给当前继续中的较大参数场。它也不支付前缀或尾的
连续度量误差、全曲面 reach、全参数嵌入、固定 $g$ 精化或任何
$\lambda=1$ 完成条件。最终实际场仍须以自身完整系数和相同真积分定义
重新生成相应全图证书。
