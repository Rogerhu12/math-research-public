# 准确转折端点的真实时间场及残差

## 1. 对象、坐标和本次范围

`scripts/fourfold_phase_field_time_turn_collar.py` 将已有严格区时间场接到
真正的 \(\tau=\pm\pi/2\) 端点。几何仍是准确 R57 仿射点

\[
\delta_2=-\frac{15291006546051}{9007199254740992},
\]

显式径向对称化、无限 R33 原函数和同步目标度量均采用此前同一定义。
本次没有换到第四点，也没有用四舍五入导出的控制向量。

输入身份为：

| 输入 | SHA256 |
|---|---|
| `type_fixed_step02_d5_exact_affine_step2_object.json` | `aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1` |
| `type_fixed_step02_d5_exact_affine_step2_root_tight.json` | `c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb` |
| `r61_step2_bernstein_forward/manifest.json` | `2a76ac79b15f28aa3ea95f708d10e073b346e0c23809a0c8021d391c1c2a816a` |

参考保持 \(Y(\tau,x)=x/4+U(\tau,x)\)、\(q=e^L\)，状态 \(Y\) 是物理
角 \(\theta\)。所有参考导数始终对**物理时间 \(\tau\)** 求导。
这里只用辅助变量 \(\eta\) 稳定表达三角函数，没有改写成以 \(\eta\)
为时间的另一套 ODE。

本次证书分别覆盖一个负端小段的实标签和一个正端小段的复标签；
它们不构成全初值圆、全条带或完整往返。

## 2. 精确端点的表示

`PiTime` 保存准确数 \(q+p\pi\)，其中 \(q,p\in\mathbb Q\)。
参考 manifest 中 `rational_multiple_of_pi` 与普通 `rational` 端点
分别读取；子段、中心、半宽都先在这个二元有理表示中运算，再由 Arb
作有向求值。判断某个端点准确为转折点时，比较的是两个有理系数是否
为零。

因此首末端使用的是准确的 \(\pm\pi/2\)，不是 binary64
`1.5707963267948966`。Bernstein 的子段坐标仍准确按保存参考的时间
端点定义，导数除以对应的准确 \(\tau\) 半宽。

## 3. 消零后的真实场

设正根为 \(t_*\)，侧别 \(\varepsilon\in\{+1,-1\}\)，令

\[
\eta=\frac\pi2-\varepsilon\tau,\qquad
r=\varepsilon t_*\cos\eta,\qquad
r_\tau=t_*\sin\eta.
\]

在两个物理端点的内侧都有 \(\eta\ge0\)。虽然正、负侧
\(\eta_\tau\) 的符号不同，\(r_\tau\) 都等于上式。

显式对称化给出 \(a,\beta\) 偶、\(Z,\gamma\) 奇。因此水平 \(F\) 偶、
竖直 \(F\) 奇，\(E=\langle F_r\cdot F_r\rangle\) 偶，进而目标曲率
\(K_0\) 准确为偶函数。负端的几何 jet 仍在真实的**负径向 common
span** 上计算；只有标量曲率的消零式通过这条准确偶性使用正根展开。

令

\[
\rho=t_*(1-\cos\eta),\qquad
D_\rho(\rho)=-\frac{K_0(t_*-\rho)}\rho,
\]

在 \(\rho=0\) 处按可去奇点延拓。真正的根恒等式
\(K_0(t_*)=0\) 来自同一对象的根证书，未由浮点拟合设零。于是

\[
Q(\eta)=\frac{t_*}{1+\cos\eta}D_\rho(\rho),\qquad
-K_0(r)=\sin^2\eta\,Q(\eta).
\]

在物理实侧取正平方根得到
\(\sqrt{-K_0}=\sin\eta\sqrt Q\)。沿用移动标架
\(n=-a^2D,m=-a^2M,G=a^2W\)，保存分支号为 `sign` 时，真实时间场为

\[
f=-t_*\sin\eta\frac MD
   -\mathrm{sign}\,t_*\sin^2\eta\sqrt Q\frac WD.
\]

实现直接复用已独审的 `frame_field`，传入

```text
K = -Q
r_tau = t * sin_eta
branch_sign = saved_sign * sin_eta
```

其关于物理 \(\theta\) 的前两阶导数公式也随之保持正确，因为这些
新增时间因子不依赖状态角。复时间延拓中使用上述解析表达式，不对
可能变号的 \(\sin\eta\) 取绝对值。

在准确端点 \(\eta=0\)，\(f=f_\theta=f_{\theta\theta}=0\) 是恒等式。
参考自己的端点导数仍须计算并计入残差，不能因真实场为零而把它们
免费设为零。

## 4. 非零 \(\rho\) 常项与完整径向尾

取 \(R_K=3/5000\)，在正根处计算完整有向 Taylor 系数

\[
K_0(t_*-R_Kz)=\sum_{j\ge0}c_jz^j,\qquad c_0=0.
\]

目标均值 \(E\) 的无限 Fourier 修正先加入径向系数，再形成 \(K_0\)。
当保留 \(c_1,\ldots,c_N\) 时，有限消零多项式为

\[
D_N(\rho)=\sum_{j=0}^{N-1}d_j(\rho/R_K)^j,
\qquad d_j=-c_{j+1}/R_K.
\]

同时在完整复径向盘 \(|r-t_*|\le R_K\) 上检查 \(a\) 与 \(E\) 无零点，
从而证明 \(K_0\) 在该盘及其某开邻域全纯，并付
\(M_K\ge\sup|K_0|\)。本次有向门给出

\[
|a|>1.09677,\qquad |E|>1.50212,\qquad M_K<0.146.
\]

在归一复时间盘 \(|v|\le R\) 上，设 \(\eta=\eta_0+\eta_1v\)，

\[
L_\eta=|\eta_0|+|\eta_1|R,\qquad
c=\cosh L_\eta-1,\qquad
\rho_{\max}=|t_*|c<R_K.
\]

由 Cauchy 系数界，整个遗漏径向尾满足

\[
|D_\rho-D_N|
\le \frac{M_K}{R_K}
\frac{(\rho_{\max}/R_K)^N}{1-\rho_{\max}/R_K}.
\]

且 \(|1+\cos\eta|\ge2-c>0\)，故 \(Q\) 的遗漏尾不超过上述值乘以
\(|t_*|/(2-c)\)。代码用这个**完整外时间盘**上的误差，逐个时间系数
加入 \(\epsilon_Q/R^j\)。这一步与原函数 \(X=F_r\) 的无限尾支付
相互独立，均先于残差形成。

一般时间段中心处 \(\rho(0)\ne0\)。因此代码对已知的有限多项式
\(D_N\) 作完整 Horner 组合，保留每个径向高阶系数对低阶时间系数的
贡献。没有把带未知高阶项的形式级数平移到非零常项后当成准确函数。
真正遗漏的所有径向项已经由上式支付。

正、负侧实际几何 \(X,a,\beta,\gamma\) 的时间组合则仍围绕同一个
真实时间中心 \(r_0=\varepsilon t_*\cos\eta_0\)，其组合参数常项按此
恒等式准确为零。整个外时间盘的几何位移使用

\[
|r-r_0|\le |t_*|\left(
|\cos\eta_0|(\cosh H-1)+|\sin\eta_0|\sinh H\right),
\quad H=|\eta_1|R.
\]

该门保留转折处径向速度消失的事实。真实实时间的整个径向像另经
有向检查，严格位于同一个实际 common span 及所有标量合法域的交集。

## 5. 根的内部细化

仍以原 `c2cfad…` 根证书作为输入。计算在其中使用真实无限 \(E\) 修正
进行三次有向 interval Newton，取得更窄的内部根球：

\[
0.2383968737810713049499786996848
<t_*<
0.2383968737810713049499786997416.
\]

原根证书文件保持不变。每次收缩的 \(C\)、\(C'\) 和根球都写入新的
端点报告。正根共同 span 为

\[
\left[
\frac{8556839292003943}{2^{55}},
\frac{8636031980136455}{2^{55}}
\right],
\]

负端使用其准确负反射。

## 6. 两个保存参考子段的有向结果

负端使用第 0 段 `[0,1/8]`，固定标签 \(x=1/2\)。准确时间区间为

\[
\left[
-\frac\pi2,
-\frac{6938704240185783}{36028797018963968}-\frac{7\pi}{16}
\right].
\]

正端使用第 880 段 `[7/8,1]`，固定标签 \(x=1/2+i/512\)。准确时间
区间为

\[
\left[
\frac{219635683275077}{1125899906842624}+\frac{7\pi}{16},
\frac\pi2
\right].
\]

两例均采用 Q512、160 bits、时间阶 16、径向消零阶 \(N=24\)、外时间
半径 8、\(R_0=3/1000\)、\(R_E=1/400\)、归一角尾条带 \(8/25\)，
额外状态管半径 \(1/65536\)。以下十进制界都留有保守余量。

| 量 | 负转折、实标签 | 正转折、复标签 |
|---|---:|---:|
| \(\sup|e_0|\) | \(<1.104061\times10^{-10}\) | \(<3.744946\times10^{-10}\) |
| \(\sup|e_1|\) | \(<3.530337\times10^{-8}\) | \(<1.484017\times10^{-7}\) |
| 全部高阶时间 \(e_0\) 尾 | \(<9.356\times10^{-19}\) | \(<4.447\times10^{-19}\) |
| 全部高阶时间 \(e_1\) 尾 | \(<2.784\times10^{-18}\) | \(<2.729\times10^{-18}\) |
| 外时间盘 \(\rho_{\max}\) | \(<3.416\times10^{-5}\) | \(<3.917\times10^{-6}\) |
| 全部径向遗漏对 \(Q\) 的误差 | \(<4.134\times10^{-29}\) | \(<1.048\times10^{-51}\) |
| 外时间盘 \(\operatorname{Re}Q\) 下界 | \(>7.1282\) | \(>7.1601\) |
| 外时间盘 \(|D|\) 下界 | \(>2.0006\) | \(>1.0439\) |

根处均值 \(E\) 的无限误差小于 \(9.201\times10^{-29}\)；它已计入
径向系数和所有后续运算。

在单独定义的“左端真实初值准确匹配参考”的局部问题中，R60 门均
通过，整个对应子段的真实物理角误差分别小于

\[
4.153271\times10^{-13},\qquad
4.770566\times10^{-13}.
\]

这仍不是把完整分支已经累积的误差设成零。完整分支的初值、接缝和
累计管必须由完整覆盖程序另行支付。

真实端点场及角导数都准确为零，但正端保存参考自身的导数残差不为
零。报告给出

\[
e_0(\pi/2)\approx-7.3054404614\times10^{-14}
 +4.3374194797\times10^{-17}i,
\]

\[
e_1(\pi/2)\approx-3.8221635123\times10^{-15}
 -1.0213196089\times10^{-15}i.
\]

这些是已付款有向球的中心近似，完整球见 JSON；没有将它们删去。

## 7. 冻结文件与重放

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_field_time_turn_collar.py` | `4c925c5478eb5355eec750112d0c3496642d3111ca97583559e4a7f6e46d6536` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_reference_time_negative_turn.json` | `980ee8ffc1deb6262020a1b8e7a0e092923b84df71ada60bc1e2cb1000c1547c` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_reference_time_positive_turn.json` | `09745bb98efe61848b01e1596271726490efc193f53df8a1ff4e3c5c7433f2e1` |

两份报告还记录全部依赖源、实际参考 shard、精确时间、根收缩轨迹、
径向消零系数、时间 \(Q\) 系数、残差系数和全部尾界。

在课题目录重做负端例：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_field_time_turn_collar.py \
  --manifest data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --segment 0 --side -1 --sub-left 0 --sub-right 1/8 \
  --initial-label-real 1/2 --initial-label-imag 0 --quarter-nodes 512 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/negative_turn_replay.json
```

正端改为 `--segment 880 --side 1 --sub-left 7/8 --sub-right 1`
和 `--initial-label-imag 1/512`，输出使用独立路径。

后续二变量时间/初值角验证可复用该类已缓存的 `Q`、`sin_eta` 和真实
几何时间系数，按第 3 节向 `frame_field` 提供参数。这里没有认证完整
初值条带、完整 return map、参数导数、全频 PDE 逆或精确等距族。
