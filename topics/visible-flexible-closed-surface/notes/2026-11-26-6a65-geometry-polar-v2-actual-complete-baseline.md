# 独立 polar v2：两组完整直接缓存及 5292 列、13+q2 行的真实自身基线

状态：**启发式/数值证据**。两个实际缓存进程和 assemble 已完成，新模型自己的完整值进程自然退出 0。没有优化接受；该基线仍远未达到等距/曲率目标。后续 full-H LM 使用这份真实 INITIAL，不继承旧 gap 或 Cauchy 的接受计数。

## 1. 冻结的位置和独立目标度量

位置取已登记的 positive-height weighted polar 构造，加独立 v2 稳定端口反参。
前缀的 master 仍严格绑定 R233 原保存源，参数
$$
c=.1015625,\quad b=.1815625,\quad
L=.7956739498716915,\quad S=.9772364498716914,
$$
真实 cuff 位于 $S+.48=1.4572364498716914$。
中央轴为 $A_c=1.4532280772048913$、$B_c=.4032280772048914$；
R205 尾幅度 $.8746432018013935$，真实 cuff 高度 $.51$；高度速度 Bernstein 次数 31。
完整 Cartesian 修正支撑在 $(b,S)$，两端的 0/1/2 jets 为零，因此当前阶段固定整个前缀及真正 R205 尾。所有三个 Cartesian 分量和全部实 Fourier 通道保留，不施加反射或半转限制。

目标 $g$ 与该 polar 位置独立：前缀取原标量，原 $[b,b+.2]$ 紧窗口取原 zero-parameter Cauchy/window 场的自然周长定义，其后取同一原 zero-parameter 标量半径。原显式 interface-probe 文件只用于定义这个目标，并未被冒充旧实际 baseline 或 CI checkpoint；新 polar 位置的值则是本次真正计算。目标没有换成新 polar 场的周长。

新位置来源身份 SHA：
`90488346b7de882e952b174244f747a85fc6e4d4babb00e8aac8aafcbad35073`。
两个实际进程独立得到逐字相同的目标 radius/first/second 导数数组。该有限数值消费器和准确积分的数学定义仍保持区分，未补造全域舍入误差证书。

## 2. 实际两网格缓存

新有限求积明确为原 polar 观察所用的 **97 个完整物理节点**：
前缀节点、65 个 sine-squared 连接节点、全部物理端点及尾部节点，径向非均匀梯形权除以 $S$。
两个角规则分别为 128 和 192，所有角覆盖完整周期；每组在联合目标中乘 $1/2$。
两组现在都属于训练目标，不把其中一组称为独立第三观察。
这不是旧 gap 分支的 514/343 径向网格，也不借用其有限目标值。

每点直接计算同一位置场的
$(X,X_s,X_u,X_{ss},X_{su},X_{uu})$，
未投影为新的 Fourier/Hermite 背景。两组实际合计 31,040 点。
原 $32$ 径向/$M=12$ 的完整 Cartesian 基通过四个原物理 cell 中点插入和 $M=24$ 扩展，得到 $36\times147=5292$ 列；这里从零系数开始，不把旧场的系数或接受继承进来。

| 真实阶段 | 自然退出 | 耗时 | 峰值 RSS |
|---|---:|---:|---:|
| v2 的 $97\times128$ 缓存 | 0 | 181.534858887 秒 | 206128 KiB |
| v2 的 $97\times192$ 缓存 | 0 | 289.171440190 秒 | 208616 KiB |
| assemble | 0 | 工具实际确认 | — |
| 新 13+q2 完整值 | 0 | 1.049347103 秒 | 73360 KiB |

128 组实际重算后，位置六-jet 数组及目标半径数组均与 v1 已成功组逐字 SHA 相同。
该组 130 次端口反参全走原成功路径，实际最大残差
$7.105427357601002\cdot10^{-15}$。
192 组 129 次走原路径，1 次走周期括区路径，实际最大残差
$4.707345624410664\cdot10^{-14}$；原失败的点已真正计算完成。
原 $5\cdot10^{-14}$ 门槛未放宽，原 v1 失败缓存没有改标为 v2 成功缓存。

## 3. 完整自身 13+q2 基线

新行是 R242 的离散 $q=2$ 形式
$$
r_A=\sqrt{w_{\rm metric}}\left((.5/\sigma)^2-1\right)_+,\qquad
\sigma=\frac{|X_s\times X_u|}{a_*}.
$$
保留全部原 13 行和全部 5292 列；每组的半权只支付一次。总行数
$$
31040\times14=434560.
$$
hinge 等号处采用已登记的零广义导数。$\eta=\sigma^2$ 是归一化 Gram 行列式，不是面积元；实际面积元为 $a_*\sigma$。
本次有限成本不能作为 R242 的连续积分成本上界使用。

参数仍为 metric $\tau=.05$、curvature $\tau=10^6$、曲率 guide $9.5$，
其余完整 point 参数随 prepared/source 固定。实际结果：

| 指标 | 本次真实 baseline |
|---|---:|
| 总 $R_{14}^2$ | **97.05124504890188** |
| 全部原 13 行成本 | 96.84143416251015 |
| 新面积行成本 | .2098108863917284 |
| metric 成本 | 95.44192462509095 |
| curvature 成本 | 1.399509537419207 |
| geometry 成本 | 0 |
| 最大相对度量误差 | **.9394005187239691** |
| 最大自身主曲率绝对值 | **104.97845760048854** |
| 最小采样归一化 Gram 行列式 $\eta$ | .06078747774805643 |
| 最小采样面积比 $\sigma$ | .24655116659236562 |
| 对握持参照点的最小采样距离 | .7097393857126268 |

七个原几何罚行的采样超限均为 0。它们和采样握持距离不自动给出连续 reach 或闭面族的形变量证明。

最坏度量/面积点仍为
$s=.8163906842065027,u=\pi/2$：
$$
E=.060599481276030896,\quad
F/a_*=-1.6345129174411586\cdot10^{-13},\quad
G/a_*^2=1.0031022785685113.
$$
最小/最大归一化 Gram 特征值为 .060599481276030875 / 1.0031022785685113；
沿经线速度 .24616961891352657。最坏曲率为同点的
$(104.97845760048854,.6750044280102543)$。
这与 R247 固定 $\rho$ 的高度族限制一致，新的求解保留完整 XYZ 修正以改变该局部几何。

两组各自已经包含半权，其总成本分别为
48.52564606933636 和 48.52559897956552。
原固定 $g$ 的独立必要采样诊断给
$$
\max|K_g|=\max|{-a_{ss}}/a|=6.076099189577641
$$
于 $s=.7494966999245619$，
$(a,a_s,a_{ss})=(1.003089823093259,-.5136450261323053,-6.09487326117053)$。
它低于 $1/.097^2$，只说明这些节点未触发该必要障碍，不是连续 target-curvature 证书。

## 4. 复生和输出身份

源码入口：
`6a65-geometry-nonfold-cartesian-prepare-v2.py`
SHA `4e6aaee2178c621e1207f6d5b06d58d075aea1c0566f84c8b506cfd588db0ddd`；
背景
`6a65-geometry-nonfold-polar-background-v2.py`
SHA `58e7080d51c0c0a7d584e688c9ec1b995fdffb72c0c0a21eec9a8f23f178c3fd`。
其余端口稳定反参来源、v1 失败事实和实际 six-jet 核对见
[独立反参说明](2026-11-26-6a65-geometry-polar-inverse-failure-and-stable-source.md)。

两个 `prepare cache` 独立进程之后，运行
`prepare assemble --training-group TRAINING_GROUP --observer-group OBSERVER_GROUP --scripts SCRIPTS --background BACKGROUND --prefix FRESH`。
本次准备文件 `nonfold-cartesian-direct02-prepared.json` SHA：
`a67e6e08843161fa0e324770aeea4a6a5ba3ac8385413991b92732bdc0905086`。

完整求解入口
`6a65-geometry-nonfold-polar-q2-full-normal-v2.py`
SHA `18ba78db845473cfeef6125cde41e733b36ce096963e01ab1fec43041dadc37a`，
以 `--prepared PREPARED --steps 0` 和对应 public scripts/base/background/
joint/area/full-normal 源路径生成本次 baseline。
两个半权组的完整方程、全部跨 Cartesian/角通道的物理 normal 和原 $\lambda S$ 正则项均保留；
本次没有执行一次 normal/LM 来凑 baseline 的接受计数。
`--steps 1 --state INITIAL` 是独立后续真实求解，本说明不预支其结果。

| 实际输出 | SHA-256 |
|---|---|
| training sealed group | `9a98c838007f15a09ade4afbe8508c2fe5866450dcf758040ceca2e2da25434e` |
| observer sealed group | `cea0f2f62522c5beeac9ca322ce4ab178e0ef97593f7c7e97d08844a5681a3ad` |
| baseline INITIAL | `d92d0edce2f52b2a6ef6a1944c91792e71ebe76a5027d2a8a882323be33c9e80` |
| baseline report | `e7f382c986e3e8d95bca0957ee9eaa8e1cb31356ae5d551a457f7e37e9debdc2` |
| baseline 实际外部退出记录 | `ce7a970f591e11d9b25635165157a7cec9a8e9e221a941855b103464a4bc849b` |
| training 实际外部退出记录 | `dcab2eeddff93fd08b79b8b09d62256b0741a7858ec7d2926fc1f25b0ddcff1b` |
| observer 实际外部退出记录 | `2025478345b79a5247c6854c174c68ab1ea794b93c70fb00067a8a6b8d65ff63` |

本次为本地实际执行，无借用的 Actions run。
所有输出和原始数组留临时区；按根 README 第 15 条只提交生成源码、参数、本小结及哈希。

当前固定前缀只有已登记的小非零度量误差，尚不能据此宣称全域误差趋机器容差；
之后必须修正准确前缀或扩展真实修正支撑，并重新支付完整前缀几何。
全闭 $C^2$ 同 $g$ 连续族、全时 reach、无标签握持变化量和同一几何的收敛链均仍待完成。
