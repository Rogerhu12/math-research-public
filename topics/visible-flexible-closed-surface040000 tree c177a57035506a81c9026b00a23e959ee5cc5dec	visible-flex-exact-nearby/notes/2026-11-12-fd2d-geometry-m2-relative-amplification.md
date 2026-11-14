# 完整 m2 轨道、相对第二基本形式与温和 deep phase

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

**状态。** 第 1–3 节是线性化的准确恒等式及其完整推导；第 4–6 节是实际脚本生成的有限数值轨道和敏感性检查。尚未得到非线性活动核、非线性尾匹配或强目标闭族。扫描改变了物理度量；只有最后固定的某一输入才能用于后续同 g 加密。

原 v4 文件 `2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json` 未改，SHA256 为
`1180a59ddea1a62036b04e814fbf2f4b7aa419efc71c0035a49ace722a552a9d`。
新 p148 输入是 `2026-11-12-fd2d-moderate-deep-p148-frozen-01.json`，SHA256 为
`4b35ff865ac94f0d58754cdb287117a7f422e28385b4dd7983581453fef4cf0a`。
原中央 a0、原冻结初前缀、cuff .32 和 cut .4 两 jet 保留；最后 deep phase 及浅 coast T 改变，因此新旧完整 g 不同。

## 1. 从实际一阶等距位移得到 f,g 方程

设旋转背景

$$X_0(s,u)=a(s)e_r(u)+z(s)e_z,\qquad
v=a',\quad b=z'=\sqrt{1-v^2}>0.$$

其材料度量为 $ds^2+a^2du^2$。选择朝内单位法向

$$N=-b e_r+v e_z,\qquad e_1=v e_r+b e_z,\quad e_2=e_\theta.$$

正交第二基本形式为

$$l_0=-a''/b,\quad m_0=0,\quad n_0=b/a,\qquad l_0n_0=-a''/a=K.$$

对整数 $k\ge2$，考虑实际位移

$$V=f(s)\cos(ku)e_r-\frac{f(s)}k\sin(ku)e_\theta
       +g(s)\cos(ku)e_z. \tag{1}$$

这里 f 是径向位移的余弦系数，g 是高度位移的余弦系数；它们不是相对曲率参数。角向一阶度量误差自动为零，因为
$e_\theta\cdot V_u=f\cos(ku)-f\cos(ku)=0$。
剩余两个一阶度量方程为

$$v f'+b g'=0,\qquad
a f'+(k^2-1)vf+k^2bg=0.$$

第二式由 $X_{0,s}\cdot V_u+X_{0,u}\cdot V_s=0$ 得到。因此

$$f'=-\frac{(k^2-1)vf+k^2bg}{a},\qquad
g'=\frac{(k^2-1)v^2f/b+k^2vg}{a}. \tag{2}$$

下文计算取 $k=2$，并以中央 $f(0)=1,g(0)=0$ 归一化。真实小幅初始化必须另乘物理幅度 $\varepsilon$。

## 2. q 坐标、准确 coast 传播及曲率变分

定义

$$q=\frac{vf}{b}+g.$$

由于 $b'=-va''/b$，有 $(v/b)'=a''/b^3$。用 (2) 消去 $g'$ 得到准确系统

$$\boxed{f'=\frac{vf-k^2bq}{a},\qquad q'=\frac{a''f}{b^3}.} \tag{3}$$

这避免在混合曲率系数中反复计算两个可能相消的大数 $vf/b$ 与 g。程序在 phase 段直接使用 $b=\cos\phi$，没有在 $|v|\simeq1$ 时通过 $1-v^2$ 相减计算 b。

### 2.1 每个 coast 的准确解

在 $v,b$ 常数的 coast 上，q 恒定。若 $v\ne0$，从任一锚点 $a_*$ 出发，

$$f(a)=\frac a{a_*}f_*+\frac{k^2bq}{v}\left(1-\frac a{a_*}\right). \tag{4}$$

若 $v=0$，则 $a=a_*$ 且

$$f(s)=f_*-\frac{k^2bq}{a_*}(s-s_*). \tag{5}$$

这是 (3) 的直接积分，对正向和反向轨道均成立。脚本对全部 coast 使用 (4)–(5)，只有其余段使用 DOP853。

### 2.2 第二基本形式的一阶变化

一阶等距条件使正交化的第一阶修正为零。单位法向的一阶变化为

$$\dot N=\frac{f'}b\cos(ku)e_1
-\frac{b(k-1/k)f-kvg}{a}\sin(ku)e_2.$$

这由 $\dot N\cdot e_1=-N\cdot V_s=f'\cos(ku)/b$、
$\dot N\cdot e_2=-N\cdot V_u/a$ 及 $\dot N\cdot N=0$ 得到。
代入实际第二导数，有

$$\dot n=\frac{V_{uu}\cdot N+X_{0,uu}\cdot\dot N}{a^2}
=\frac{(k^2-1)f}{a^2b}\cos(ku), \tag{6}$$

$$\dot m=\frac{V_{su}\cdot N+X_{0,su}\cdot\dot N}{a}
=-\frac{k(k^2-1)q}{a^2}\sin(ku). \tag{7}$$

为核对 (6)，其分子在代入 (2) 前为
$b(k^2-1)f-vk^2g-avf'/b$；g 项相消，f 项化为 $(k^2-1)f/b$。
对 (7)，代入前的系数为

$$\frac{(k/b-b/k)f'}a
-\frac v{a^2}\{b(k-1/k)f-kvg\};$$

代入 (2) 后正是 $-k(k^2-1)(vf/b+g)/a^2$。
最后对 Gauss 等式 $ln-m^2=K$ 求一阶变化，得到
$\dot l=-l_0\dot n/n_0$。

故 $k=2$ 的相对变分恰为

$$\boxed{\eta=\frac{3f}{ab^2},\qquad
\zeta=-\frac{6q}{ab},\qquad
\dot n=n_0\eta\cos(2u),\quad
\dot m=n_0\zeta\sin(2u),\quad
\dot l=-l_0\eta\cos(2u).} \tag{8}$$

即使 cut 高度系数 g 很小，$b^{-2}$ 仍可使相对曲率变分非常大。因此单看 terminal height gain 无法决定可用小幅初值。

对 (8) 求导，并使用 (3)，还得到

$$\eta'=\frac{2va''}{b^2}\eta+\frac2a\zeta,\qquad
\zeta'=-\frac{2a''}{b^2}\eta
-\left(\frac va-\frac{va''}{b^2}\right)\zeta. \tag{9}$$

脚本用这些准确导数对有限采样区间中的符号变化做驻点括号搜索。没有证明未被括号捕获的所有驻点均不存在，所以报告的最大值仍是有限数值估计。

## 3. cut 的线性 height jet 与 II 端口完全一致

设 cut 半径 r，$v=a'_{cut}<0$，$w=-b/v>0$。真实高度一阶模态为
$g_k\cos(ku)$，其径向导数为 $D_k g_k\cos(ku)$。
此时 $g_s=vD_k g_k$，所以 (2) 给

$$f_{cut}=-\frac{w(rD_k-k^2)}{k^2-1}g_k,
\qquad q_{cut}=\frac{rD_k-1}{k^2-1}g_k.$$

从而

$$\boxed{\dot n_{cut}=\frac{(rD_k-k^2)g_k}{r^2v}\cos(ku),\qquad
\dot m_{cut}=-\frac{k(rD_k-1)g_k}{r^2}\sin(ku).} \tag{10}$$

这是准确的一阶关系。不能将 linear height 的有限值代入非线性平方根，再把其二次偏差误当成一阶公式不一致。

当前有限端口为 $r=.4,w=.1,D_2=7.657720764629502$，准确 cut jet 为
$v=-10/\sqrt{101}$、$a''=1750/10201$。p148 的完整正向轨道给
$f_{cut}=.01026225761326097$、$g_{cut}=.32859844773793095$。
(8) 的未乘幅度 II 系数为 $\dot n=1.9337702363470062$、$\dot m=-8.474095185199545$；
(10) 给 $1.9337702361383713$、$-8.474095185614743$。约 $4.2\times10^{-10}$ 的差对应有限 terminal 方向残差及端口数值误差，没有被定义成零。

## 4. 原 v4 的完整轨道

报告：`2026-11-12-fd2d-v4-full-m2-report.json`；逐段/逐点数据：
`2026-11-12-fd2d-v4-full-m2-trajectory.npz`。

| 完整半核指标，单位 f(0)=1 | v4 实际有限数值 |
|---|---:|
| 最小 b | .0009999998333332927 |
| 最小参考 n0=b/a | .0018121512509883856 |
| η 的最大绝对值 | 10935.300183195672 |
| ζ 的最大绝对值 | 23245.013805075756 |
| η 峰位置 | s=1.5025194999147076，cut brake 开头 |
| ζ 峰位置 | s=1.5023115331391483，cut brake 开头 |
| terminal f | −.0015214185838399123 |
| terminal g | −.04871984196393613 |
| 归一 terminal 方向残差 | 2.482642851172222e−6 |
| 线性相对 II 控制到 1% 的幅度 | 4.301997875267517e−7 |

旧 v4 元数据中的 backwards-root 方向残差约 $1.24\times10^{-10}$ 及 gain $-.048718224$ 没有通过本次完整正向传播得到同样数值。原输入和旧报告均保留，未倒改。当前准确 coast、稳定 q 坐标与独立 f,g 正向计算一致到下表范围；根本上说明旧近水平射击的端口方向对小误差敏感。

## 5. pdeep=1.48,…,1.54 的七个独立新 g

保持 v4 匹配浅 coast 之前的全部数据，取 deep phase $-p_{deep}$，同时调整 T 到同一个有限 m2 cut 方向。要求
$p_{deep}>\arctan(10)$，保证后面的 cut brake 仍有正长度。这里只扫描七个值，没有将其描述为全参数最优。

| pdeep | T | terminal g | η 最大绝对值 | ζ 最大绝对值 | min n0 | 背景含尾高 |
|---:|---:|---:|---:|---:|---:|---:|
| 1.48 | .013443229317711 | .328598447738 | 136.655645 | 224.767197 | .159896875 | 1.222818386 |
| 1.49 | .013752546740258 | .335274317206 | 136.655645 | 224.767197 | .142740407 | 1.221541465 |
| 1.50 | .014032158847673 | .345511642461 | 136.655645 | 224.767197 | .125471355 | 1.220330909 |
| 1.51 | .014277133806047 | .361192859165 | 136.655645 | 224.767197 | .108093510 | 1.219181227 |
| 1.52 | .014477745555138 | .386128347990 | 136.655645 | 224.767197 | .090611091 | 1.218082212 |
| 1.53 | .014611099157257 | .429403695747 | 136.655645 | 224.767197 | .073032946 | 1.217010619 |
| 1.54 | .014605463721592 | .519630861010 | 180.770689 | 224.767197 | .055318090 | 1.215894717 |

七条均有相同前段的有限最大旋转母线曲率 $7.159407372526366$。各归一 terminal 方向残差绝对值不超过 $1.84\times10^{-11}$。背景高度在 R121 允许区间内只是候选背景预算，不能替代真实非轴对称核的位置与曲率。

p148 在这七条中有最好的 n0 下限和最小的 cut gain，完整 max|ζ| 比 v4 约小 103 倍。其剩余峰值来自共同前段 $a'\simeq-.98$ 的回摆，而不再来自最后 deep coast：

- η 峰：$s=1.012565618620451$，$b=.19931985056586662$；
- ζ 峰：$s=1.011371941690864$，$b=.1990399310981623$；
- 最小 b：$.09067162446430946$；完整半核长度 $1.6139766557368653$；
- terminal 方向残差：$3.3661665250438624\times10^{-12}$；
- 1% 相对 II 的线性幅度约 $4.449047784111779\times10^{-5}$，5% 约 $.00022245238920558894$。

初次分支建议用 $\varepsilon=4\times10^{-5}$ 或 $10^{-4}$。这只是初值大小；即使相对 II 为 5%，背景最大曲率已接近 $1/.136$，所以不自动满足 reach 预算。最终实际 $l,m,n$、帧/位置图、metric 及 reach 仍逐项支付。

## 6. 有限误差范围、数据约定与复现

主轨道采用 DOP853，rtol=$3\times10^{-14}$、atol=$3\times10^{-16}$、每个归一段 max_step=.02。
对照采用 rtol=$2\times10^{-12}$、atol=$2\times10^{-14}$、max_step=.04；独立 f,g 坐标对照采用 rtol=$2\times10^{-13}$、atol=$2\times10^{-15}$、max_step=.02。

| 有限敏感性检查 | v4 的 η / ζ 差 | p148 的 η / ζ 差 |
|---|---:|---:|
| 收紧容差前后，全段有限点比较 | 4.994e−4 / 8.133e−4 | 1.085e−8 / 1.096e−8 |
| q 系统与独立 f,g 系统 | 2.688e−5 / 4.377e−5 | 2.120e−9 / 2.191e−9 |
| 驻点括号初网格 129→257，最大值变化 | 1.783e−10 / 7.276e−12 | 0 / 0 |
| 端口方向反向解按中央 f=1 归一后，与正向轨道比较 | .093980 / .152741 | 1.166e−9 / 1.178e−9 |

最后一行 v4 的差包含真实有限方向未完全匹配的影响，并非单纯的 ODE 积分误差。p148 反向中央 g/f 为 $2.3592099406813666\times10^{-13}$，v4 为 $-1.4806488232782293\times10^{-8}$。
这些检查均不是严格区间 ODE 误差界，JSON 中 `rigorous_interval_error_bound` 和 `continuous_interval_certificate` 保持 false。

**数据约定。** 两份 npz 均含逐点 s、段索引 piece、a/v/b/acc、f/g/q、η/ζ、参考 n 及背景母线曲率。字段 `u` 历史上命名为 u，实际是该径向段的归一坐标 $\tau\in[0,1]$，不是材料角。角向初值仍使用准确材料 $u_{mat}$ 的 $\cos(2u_{mat})$、$\sin(2u_{mat})$；固定 balanced 法向计算角 φ 入口使用 $u_{mat}=S_{seed}(\phi)/a_0$，不能直接把角因子改成 cos(2φ)。

`fd2d_partial_return_parameter.PartialReturnParameter(source=新 p148 JSON)` 可直接提供同一候选的 coast T 参数及固定段 τ 的 JVP。默认 source 仍是旧 v4，消费者必须明确传入新路径。改变 T 也是物理 g 的改变，后续固定 g 加密不能混入不同 T 的结果。

复现命令（在课题目录执行，使用新输出 stem，避免覆盖已闭存实际报告）：

```sh
python scripts/fd2d_m2_linear_trajectory.py --candidate notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json --out-prefix notes/v4-full-m2-reproduction
python scripts/fd2d_moderate_deep_screen.py --out-prefix notes/moderate-deep-m2-reproduction
python scripts/fd2d_m2_linear_trajectory.py --candidate notes/2026-11-12-fd2d-moderate-deep-p148-frozen-01.json --out-prefix notes/p148-full-m2-reproduction
```

完整文件清单与 SHA 在 `2026-11-12-fd2d-m2-geometry-closed-manifest.json`。自动选择文件 `...moderate-deep-m2-01-selected.json` 与单独命名 p148 文件的物理 a(s) 相同；元数据不同，所以 SHA 不同。详细完整轨道绑定单独命名的 p148 文件。

## 7. 对下一真实核设计的具体含义

共同前段的 $a'\simeq-.98$ 已成为温和 deep 候选的放大峰。下一物理设计比较应调整该前段的回摆深度/加速度，同时保留真实端口和全段幅度核对，不能只降低 cut gain。
另一方面，真实 cut→cuff 长度给高度系数的准确必要界；见 [tail 长度证明](2026-11-12-fd2d-geometry-tail-length-necessary-bound.md)。
p148 的 $.3286$ gain 只是一阶导数。把它乘约 $.455$ 的大幅目标得到约 $.1495$，不能据此证明任何非线性分支不存在；真实大幅分支可以改变平均高度、其余模态及这条线性化后的关系。
R121 帽和标记窗已经完整支付，但新活动核的全域球包、held 球排除和原闭核 reach 仍是待由真实非线性解消费的条件。
