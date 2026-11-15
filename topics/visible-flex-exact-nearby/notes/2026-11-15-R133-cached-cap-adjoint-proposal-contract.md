# R133：仅复用完整标量 jets 的 97 输入物理伴随提案

本记录规定一个新的数值提案及其恢复身份。它使用已经公开完成的 7908 个 whole scalar jet 域和 64 个补齐的原生 midpoint；不重算旧 target、旧 forward cap 解或旧残差。完整帽伴随后验误差仍由 [A.1–A.29](../results/R133-supplement-full-cap-adjoint-high-to-low-boundary-grams.md) 支付。此提案本身不证明完整连续伴随边界值问题或高到低范数。

## P.1 同一背景与原输入

固定物理 $\eta_0$、原 $\nu$、连续修补后的 M32 背景，完整候选 index SHA256 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。
完整连续修补 definition 是
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
原 65 槽候选和全部 cumulative offsets 都保留，原 mean 不是新增自由参数。

原完整 quarter native 为
`770106a925812df4fc380785ca3e715b2a30a649a355fb888e0dcbe0e6a65298`。
它的八份 range receipts 逐一指定原 native、producer、worker、manifest、实际 artifact process。64 个旧 quarter 由原 plan
`406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a`
逐字节恢复；其余 7844 个 quarter 由原八个 range 恢复。全部 7908 条 request 必须恰为
$\{(i,4,j):0\le i<1977,0\le j<4\}$，每条 SHA 与完整 finish 中相同位置的 SHA 相同。

完整 native-point native 为
`41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8`。
它只补原 64 条缺失 midpoint。每条 original whole SHA 不变；point、原 whole 和其实际 parameter enclosure 包含同一固定 $\eta_0$。尾部 graft 使用原已成正宽 $10^{-9}$ 包络，并没有改称零宽或扩授整个参数盒。

新科学源只读这些标量包络；它不会重新调用 intrinsic target producer。原文件中关于旧特定 $w_0$ 的物理残差、输入维数和 Green 预算不自动转授给新伴随提案。

## P.2 浮点系数只定义新提案

对每一原 quarter 的 $\gamma,\beta,K,s$，选取已存 midpoint 的 0、1、2 阶 Arb 球的中点，构成新的浮点二次多项式。每个已选 binary64 数字都保存为数组，并记录完整原 jet 身份与新数组 SHA。恢复时使用保存的原数组，不假设不同 runner 的浮点选点或 BLAS 输出逐位相同。

这些二次多项式只是新有限提案的构造器。它们没有被当作真实系数的严格包络，也没有消去原 whole 三阶余项。后继连续残差消费者必须重新使用原 whole jets、原 midpoint jets 和完整模型余项，验证这里最终保存的真实 Hermite 函数。

角逆函数的浮点 Newton 过程同样只构造提案。没有以离散收敛、采样单调性或最终有限残差替代真实全频角坐标、乘法余项和无限 Fourier 输出。

## P.3 完整物理伴随有限系统

使用 128 个 odd $B$ 模、128 个 nonmean even $C$ 模和独立 $C$ mean，共 257 个实幅度槽。输入为 moving 角归一化的
$\sqrt2\sin(4j\varphi)$，$1\le j\le96$，再加独立 even mean，一共 97 列。

写
$$
Q_B=2u\circ\phi,\qquad
Q_C=\bigl(-u^2-K(2s\,\delta v+\delta v^2)\bigr)\circ\phi,
\qquad \ell=Ks^2.
$$

原物理一阶算子为
$$
A_{\rm phys}(b,c)=
\begin{pmatrix}
-2\beta b+\gamma\partial_\theta\bigl(Q_Bb+(Q_C-\ell)c\bigr)\\
\gamma b_\theta+\beta Q_Bb+\beta(Q_C-\ell-1)c
\end{pmatrix}.
$$

新有限提案采用 $z_r=-A_{\rm phys}^{*}z$ 的完整 257 槽投影：
$$
\begin{aligned}
(z_B)_r&=2\beta z_B+\gamma Q_B(z_B)_\theta
 +\gamma(z_C)_\theta-\beta Q_Bz_C,\\
(z_C)_r&=\gamma(Q_C-\ell)(z_B)_\theta
 -\beta(Q_C-\ell-1)z_C.
\end{aligned}
$$

这两式没有额外 $Q_{B,\theta}$ 或 $Q_{C,\theta}$；原 forward 第一行中的 divergence 已在取伴随时整体积分分部。完整修补背景的 residual Hessian $H_R^{*}$ 不在这个提案生成器内，但在真实伴随后验残差中单独完整保留。

## P.4 两端所有条件与均值

在内端 $L=9/10$，完整伴随条件是 $z_B(L)=S^*f=mVf$、$z_{C,0}(L)=a$。提案先在浮点节点 $\operatorname{float}(L)$ 采用原 128 个 physical odd 模的有限投影，全部 97 列同时求解。真实 $L$ 处的投影尾、角逆误差和极短首段差都留给真实内端残差。

在 $R=25/8$，原 finite reference Robin 的 128 行为
$$
z_{C,j}(R)-q_jz_{B,j}(R)=0,\qquad1\le j\le128.
$$

这里不另删或指定右侧 $C$ mean。左 129 行和右 128 行合成 257 个真实有限条件；实现另保原 QR 的独立 dummy 行，使 augmented 系统为 258 行。该 dummy 不是 $\nu$、不是物理 mean、也不改变相位参数。

$q_j$ 仅为原浮点 proposal 数据。真实 regular graph 的所有 nonmean 误差及独立 mean 行，按 A.7–A.12 另付；不得由这 128 行推断未知高频 Robin 已闭合。

## P.5 同一有限 QR 与独立动作

径向节点保留全部原 candidate cubic joins 和全部原 parent endpoints，再将落到同一 binary64 的重复节点合并。每个非零浮点格都不得跨原 candidate cubic join。最内 Hermite 多项式仅延拓至真实 $9/10$；不能把保存的首节点值直接冒充真实内端值。

同一个完整 257 状态 QR 因子供全部 97 个边界输入使用。QR、正向代回、反向代回、独立完整动作检查各自按已完成 atomic checkpoint 恢复，不重复已经提交到 checkpoint 的格。

独立有限检查先从供给的完整列合成物理三角函数，再逐点使用 P.3 的完整两个分量，而不是只重读 QR 的矩阵乘积。相对有限残差门固定为 $5\cdot10^{-8}$。通过该门只说明这个新浮点提案的有限方程一致性。

## P.6 精确 Hermite 对象

实际保存的 binary64 shared states 及每个格的左右单侧导数，按准确有理 Hermite 基定义分片三次函数。邻格共享同一 state，故提案本身在公共节点连续；导数可以有单侧差。完整 257 状态、97 输入、全部 mean 都保存。

物理输出 Gram 为 odd 和 nonmean even 幅度各乘 $1/2$，even mean 乘 $1$。输入 97 维使用归一化 moving odd 基加独立 mean 的欧氏 Gram。后继原物理与 moving 角的拉回需按 A.1–A.29 的真实测度因子消费。

此提案不是两份独立 forward/backward 数组的精确逆；也不把旧 forward97 列的转置当作伴随证书。

## P.7 公开执行与保留失败

所有新有限算术只在本公开仓库 Actions 执行。producer、worker、manifest、原完整 234 pins 以及新增依赖逐一冻结。wrapper 先按原 receipts 从同仓库 artifact 恢复 7908 条旧 whole 和全部原生 midpoint，再运行新 producer。

大型 QR、全部 97 状态列、导数和前缀只进入公开 Actions artifact。每次 child 结束后计算原字节 inventory，分成每件不超过 60000 UTF8 bytes 的小文本。下一次只在 source、manifest、完整输入 SHA 和 inventory 同时匹配时恢复。publication 失败与数学成功分开；实际 child0 和完整新提案 gates 已成时不再重复数学。

原科学失败、原 process 和已完成前缀全部保留。worker 每 10 分钟真实 pull，并核两份 README 差异；非快进按原授权立即 rebase 再 push。任何摘要也不得超过 60000 UTF8 bytes。

## P.8 后继必须实际支付的对象

本输出明确保持以下未付项：完整连续 $-z'-A_{\rm phys}^{*}z-H_R^{*}z$、真实两端和全部接口、无限 physical Fourier 残差、moving high 投影的真实 composition 尾、完整 $W_{\rm err}$ 和 $W_{\rm cap}$。随后只能将同一次输入的完整 97 维 Gram 与已成 true right Poisson Gram 合成；原 signed 交叉项须保到最后二次型或 trace。

本次不宣称 full cap high-to-low 范数、无限维 BVP 逆、负区高频逆或真正 $\nu$ Schur 已完成。
