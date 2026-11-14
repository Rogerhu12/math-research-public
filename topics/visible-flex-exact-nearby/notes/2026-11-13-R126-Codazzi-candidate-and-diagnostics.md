# R126 实际两场候选：完整径向输入、去混叠演化与首根诊断

2026-11-13，newton_source。

本记录严格区分三层：R125 已证明某个未定量宽度上的真实 PDE 分支；
本篇给可完整求值的**确切有限候选**；下面长区间演化和残差数值仍是
**浮点/有限网格诊断**。本篇没有证明到0.235或正帽的真正 PDE 延拓。

## 1. 优先复核输入：整个 $[0,1/200]$ 上的有限候选

已完成并冻结：

- `scripts/fourfold_phase_codazzi_dense_candidate.py`；
- `notes/2026-11-13-codazzi-dense-r0005-n1024-floating.json`；
- `notes/2026-11-13-codazzi-dense-r0005-n1024-candidate.npz.gz`（2,282,239字节）；
- 其去混叠依赖 `scripts/fourfold_phase_codazzi_evolution_probe.py`。

候选不是单端点或散点表。它有21个径向多项式段，全部与3个实际 scalar germs
对齐，覆盖确切 $[0,1/200]$。每段的 $B,C$ 是 degree-7 径向多项式，
角 Fourier 模为 $4j$，$|j|\le511$。均值保留，Nyquist 准确为零。
所有保存的 binary64 实、虚部按**确切 dyadic 有理数**解释；负模由正模准确取共轭，
常数模为实数。

压缩 NPZ 内的主要数组为：

| 数组 | 含义 |
|---|---|
| `time_nodes` | 22个共享径向节点；metadata另存每个节点的确切分数 |
| `positive_endpoint_coefficients` | 节点上两场的0至511正 Fourier 系数 |
| `positive_dense_corrections` | 每段6组内部稠密系数，每组包含相同完整正模 |
| `scalar_germs` | 每段所属真实 scalar germ；metadata另存确切端点分数 |
| `metadata` | 全部输入/producer SHA、模式/多项式约定及精确参数 |

每段写 $x=(r-r_i)/(r_{i+1}-r_i)$，共享端点系数为 $L,R$，内部系数为
$F_1,\ldots,F_6$，其**定义**是

$$
\begin{aligned}
c(x)&=(1-x)L+xR+x(1-x)Z(x),\\
Z(x)&=F_1+x\{F_2+(1-x)[F_3+x(F_4+(1-x)(F_5+xF_6))]\}.
\end{aligned}
$$

因此 $c(0)=L,c(1)=R$ 准确成立，$B,C$ 及所有角导数在段界连续。
一阶径向导数允许跳跃；后验比较应按分片/积分形式使用残差，
无需把未支付的时间节点跳跃藏进误差。采用真实端点差而非浮点 DOP853
内部的 $F_0$；此次两者有限 Fourier $\ell^1$ 差约 $4.07\,10^{-15}$，
但严格验证直接针对上述新定义，不需要把 DOP853 本身当成可信算法。

`DenseCandidate.coefficient_jet(piece,x)` 返回一段的完整正 Fourier
系数及径向一阶系数；`DenseCandidate.evaluate(r)` 是浮点便利接口，
返回 $B,C$ 的 $r,\theta,\theta\theta,r\theta$。严格求值应把保存 dyadic
系数和节点分数送入有向算术，再用同一个多项式公式。

初始参考 $B_0=0$，$C_0$ 直接用 R33 的有限相位公式

$$
C_0(\theta)=-\frac{1+\sum_j4j\,\beta_j(0)\cos4j\theta}{a(0)}
$$

选择，无需从无限 primitive 的两次角微分重新产生尾。
它是参数中心的浮点选择；与真实全参数初值之差仍须有向计算。

此候选配合**真实** $k(r)=\sqrt{-K_0(r)}$ 定义
$P=(B+k)/C,Q=(B-k)/C$。它们不是有限 Fourier 多项式，但已由有理式完整定义。
真实全参数系数必须进入残差。R126 的准确转换
$R_P=(R_B-PR_C)/C$、$R_Q=(R_B-QR_C)/C$ 可以避免单独计算 $k'$ 后再大数抵消。

21个浮点诊断径向点给（不是全域上界）：

$$
\max |R_{B,C}|\approx6.92\,10^{-10},\quad
\max |\partial_\theta R_{B,C}|\approx1.14\,10^{-7},
$$

$$
\max |R_{P,Q}|\approx1.53\,10^{-9},\quad
\max |\partial_\theta R_{P,Q}|\approx4.37\,10^{-7},\quad
D_1\approx50.12,\quad D_2\approx6856.
$$

真正可用的连续/full-$\eta$ 残差和屏障须由另一个 native validator 给出。
生产此候选只用7.79秒；容差 `rtol=3e-11, atol=3e-13, max_step=.00025`。

| 文件 | SHA256 |
|---|---|
| dense producer | `81630e41d5fb8d34f9424d291a35000371a15e21778dbbb19e0272f2edc151c2` |
| 去混叠依赖 | `2d9e8a9dd185e13c1c506a628f36847fe6180390bca3b60014d7c1beb8a69c36` |
| dense报告 | `da8d65d9eb11ffe0520f64548e1710f1316efc66f91a33719ac76f7f9a8722e6` |
| 完整压缩候选 | `a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f` |

## 2. 两场去混叠比直接位置形式稳定

`fourfold_phase_codazzi_evolution_probe.py` 在2倍角网格计算非线性后投影，
保留均值和全部其余有限模；同时沿径向重构位置和正交框架。
诊断的 metric/source 使用重构**位置的实际 Fourier 导数**，
不是把 $F_\theta=aY$ 等尚待比较的框架关系直接当成真等式。

| 区间/角数 | metric defect | 真实位置 source | 最小 $|C|$ | 两场去投影残差 |
|---|---:|---:|---:|---:|
| $[0,.235]$, 512 | $3.00\,10^{-8}$ | $1.44\,10^{-5}$ | 0.34510 | 0.005605 |
| $[0,.1]$, 1024 | $1.96\,10^{-12}$ | $1.31\,10^{-8}$ | 0.34704 | $2.72\,10^{-8}$ |
| $[0,.235]$, 1024 | $7.92\,10^{-12}$ | $2.85\,10^{-8}$ | 0.34502 | $1.80\,10^{-6}$ |

上表都是有限采样诊断。1024角到.235时，框架正交缺陷约
$8.97\,10^{-14}$，位置角兼容缺陷约 $8.52\,10^{-12}$。
样本主曲率绝对值小于7.594、支撑函数大于0.90129；修正
$C^0<.000344$、原诱导材料 $C^1<.016847$、Hessian小于1.477738。
这些数值说明应使用真实局部几何，而不能把某个充分 Hessian 档误当必要条件。

完整报告/端点采用以下前缀，每个都有 `-floating.json` 和
`-endpoint-floating.npz`：

- `notes/2026-11-13-codazzi-evolution-r0235-n512`；
- `notes/2026-11-13-codazzi-evolution-r010-n1024`；
- `notes/2026-11-13-codazzi-evolution-r0235-n1024`。

端点 NPZ 的 `state` 列顺序为 $B,C,F[3],X[3],Y[3],\nu[3]$，也另存文字列名。
它们是后续候选选择的输入，不是整个径向轨迹；只有第1节 dense文件完整定义一段轨迹。

## 3. 首根处是 $K_0$ 退化；未观察到 $C$ 临零

`scripts/fourfold_phase_codazzi_resume_probe.py` 从冻结的.235端点短程续算。
结果为：

| 续算终点 | 终点浮点 $K_0$ | 此次续算最小 $|C|$ |
|---:|---:|---:|
| 0.2383 | −0.00590464170446 | 0.42853 |
| 0.23839687429986536 | 约 $9.97\,10^{-12}$ | 0.42744 |
| 0.239 | 0.0330822361302 | 0.42075 |

中间一行是既有根证书的中心数；浮点 $K_0$ 接近零不替代根区间证书。
从.2383到.239的样本 metric defect仍约 $7.85\,10^{-12}$，source约
$7.41\,10^{-9}$。因此直接位置离散形式在.216附近的停滞没有被两场形式
复现为一个真实 $C=0$ 门槛。它也没有证明完整 PDE 可以如此越过根。
R126 的严格负曲率能量在 $K_0=0$ 退化；正曲率一侧的有限续算另需解析或
椭圆论证，不能沿用该能量结论。

三个续算前缀为 `notes/2026-11-13-codazzi-to-r02383-n1024`、
`notes/2026-11-13-codazzi-to-target-root-n1024`、
`notes/2026-11-13-codazzi-to-r0239-n1024`，均保存报告和端点。

## 4. 端点 Riemann 全谱输出

入口 `scripts/fourfold_phase_codazzi_endpoint_fields.py` 以有理链式公式计算
$B,C$ 及角一、二阶，$p,q$ 及角一、二阶，半离散残差及其角导数。
在2倍网格输出全部有限谱，同时另存严格 Hermitian 的 dyadic $B,C$ 参考
及其与原浮点 FFT 的有限 $\ell^1$ 差。

已完成的前缀为
`notes/2026-11-13-codazzi-r010-n1024-Riemann`、
`notes/2026-11-13-codazzi-r0235-n1024-Riemann`、
`notes/2026-11-13-codazzi-r02383-n1024-Riemann`，
各有 `-fields-floating.json` 和 `-spectrum-floating.npz`。
谱内包含16个具名字段及实际物理频率。

这些端点有理变量的 Fourier 支持一般无限；导出的双网格谱没有证明其剩余尾为零。
各谱报告明确没有连续径向信息、没有时间误差证明，也没有 full-$\eta$ 覆盖。
真正后验输入应优先采用第1节完整 finite candidate，再以真实系数作有向残差验证。

## 5. 已实际通过的真实目标系数输入

根进程另已运行 `scripts/fourfold_phase_codazzi_coefficients.py`，完整原生报告为
`notes/2026-11-13-Codazzi-target-coefficients-r0-to-0p001-native.json`。
它覆盖真实闭径向区间 $[0,1/1000]$、整个原辅助参数盒和完整无限角primitive，
不是从上述浮点轨迹估计系数。$E,E',E''$ 均从原几何的完整Fourier乘积与
全部尾构造，$K,K'$ 按同一固定目标准确公式计算。实际已得保守有向界

$$
-.879381<K<-.832620,\quad
1.024426<\gamma<1.050147,\quad |\beta|<.001052,\quad |\kappa|<1.898.
$$

初始真实有限相位曲率的全角/全参数界为
$-7.593298<C(0,\theta)<-.346523$，并保存一至三阶角导数的完整界。
这些是原目标和初值的严格输入；它们本身不证明数值候选的连续残差、
R126屏障或指定宽度的精确PDE分支。相关连续validator正在另行运行。
