# Inverse-Q 外段的实际全尾接入与内尾负载

本记录只闭存一个明确的新物理度量、实际完整有限线性响应及失败原因，不宣称强目标或非线性尾部已完成。原 layered64/wc01、所有既有输入和报告绑定的源保持不变。

## 1. 准确定义与原来源身份

原基准是 `2026-11-12-fd2d-layered64-wc01-recovery02-config.json`，SHA256 为
`d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994`。
局部候选是 `2026-11-12-fd2d-metric-inverse-q-raw0-candidate-01.json`，SHA256 为
`3fe9d09500459bb3aa6d9b50e9d6c38523730a1a4fa98b6ee67eab5ad7e558af`。

新 factory `fd2d-inverse-q-tail.mjs` 首先按原配置原样构造 160 格物理尾。取未改 raw1 的外端作为桥的内端，使用该物理端口的真实定义值 $r_0,w_0,w'_0$，而不是把候选 JSON 中显示的端值当作原解析端口的准确二进制定义。新外端指定

\[
 r_1=13/20,\qquad w_1=1/10,\qquad (\log w)'(r_1)=-7/r_1.
\]

桥由 metric lane 已闭的 `fd2d-metric-inverse-q-buffer.mjs` 与薄接口 `fd2d-metric-inverse-q-bridge.mjs` 定义：正 Bernstein $k(t)$，准确加权矩归一，$Q_t=t(1-t)k(t)$，及其无端点零除的有理对数导数原函数。最后以 $cS_5(t)$ 校准外端 $w$。这里的准确数学对象是这些公式及积分；固定 1024 格和 Gauss 求值是浮点 evaluator，不是区间证明。

只替换 `physical.cells[0].profiles`。保留原 `physical.source` 完整 160 格原 source、全部 $\mu_n$、`linearDeepParameters`，以及 raw1 至 raw159 的原实际物理 profiles。$\mu_n$ 只是 canonical momentum 的坐标尺度；替换物理 profile 不要求它继续代表原有限格的脉冲校准。

新 profile 按 9 个等长 $t$ 区间交给现有 shooting consumer。坐标变换同时缩放 $r_x,(\log w)_x$ 以及所提供的二阶导；它没有改变物理 $r,w,w_r$。所有完整配置、候选定义、源文件 SHA、内端约定和数值分段约定都嵌入 `physical.parameters.inverseQDefinition`，并另给摘要 SHA。这防止恢复缓存把不同 profile 误认为同一 $g$。

实际执行 `appendUnchangedDeepSource(...,196)` 成功：原 0 至 159 source 的 $\mu,\delta,R,c,$ length scale 和 calibration alpha 逐项保持，160 至 195 来自未改原 source。这个身份检查不是无限尾的数值证书。

## 2. 为什么拼接达到母面 C²

在任一固定取向 $\sigma=\pm1$ 下，回转背景可写为

\[
 X(r,u)=(r\cos u,r\sin u,z_0+\sigma\int_{r_0}^{r}w(v)\,dv).
\]

其第一基本形式为

\[
 g=(1+w(r)^2)\,dr^2+r^2du^2.
\]

只要 $w>0$ 且 $w\in C^1$，此图正则且 $X\in C^2$。接口的 $w,w_r$ 相等，选择同一个 $z_0$ 后，位置、一阶导和二阶导全部连续。桥的构造正好支付这两个端值。因此旧内尾和新外桥以 C² 母面接合。无需强迫 $w_{rr}$ 相同：那约束的是母面的三阶导。新外 cut 的两 jet 也按指定 $w_1,w'_1$ 支付。

这一步构造的是新的共同度量候选；它不构造非圆等距尾，也不把回转背景曲率界转成活动核的 reach。有限桥带来的高度差由实际积分记账，之后仍须与前缀和固定帽的真实高度协调。

## 3. 完整尾部响应必须包含旧内层的增益

对 real cosine 系数 $H(r)\cos(2u)$，线性尾方程及实际物理 II 为

\[
 J=H_r-4H/r,\qquad H_{rr}=-(w_r/w)J,
\]

\[
 \delta l=-H_{rr}/\sqrt{1+w^2},\quad
 \delta n=-\sqrt{1+w^2}\,J/r,\quad
 \delta m=2H/r^2-2H_r/r.
\]

另记 $\Gamma=J/w-4Hw/r$。相对量 $L=J/w$ 和绝对物理曲率响应不是同一个量。

设替换外侧 $N$ 格，原 bounded 线性解在接口 $r_N$ 的高度非零。由于旧内尾完全不变，且采用同一深端 bounded 方向，任意新的线性解限制到旧内尾后都是原解的常数倍。具体为

\[
 H_{\rm new}(r)=
 \frac{H_{\rm new}(r_N)}{H_{\rm old}(r_N)}H_{\rm old}(r),
 \qquad r\le r_N.
\]

证明：两解在深端属于同一一维初值子空间；二阶线性 ODE 的初值唯一性给出比例关系，之后用非零接口高度确定比例。上述 $\delta l,\delta n,\delta m,\Gamma$ 都是 $H,H_r,H_{rr}$ 的线性函数，因此同样按此比例缩放。若桥按 $H_{\rm cut}=1$ 归一且 $\gamma=|H_{\rm new}(r_N)|$，则完整连续峰值恰是

\[
 \max(I_{\rm bridge},\gamma C_{I,N}),\qquad
 \max(\Gamma_{\rm bridge},\gamma C_{\Gamma,N}),
\]

其中 $C_{I,N},C_{\Gamma,N}$ 是按单位接口高度归一的原内尾连续峰值。这个恒等式不依赖薄透镜近似或 binary64 正向方向猜测。

`fd2d_tail_inner_loads.py` 从原实际完整 n512 轨道读取这些常数的**采样下界**，并保留各峰所在的实际点。不得将该文件中的有限值称为连续上界。对于 $N=1$，采样 $C_{I,1}\approx1.01659255\times10^7$；因此即便桥本身 II 很小，$\gamma\approx0.096$ 仍会把大量响应传入 raw1。

## 4. 已真实执行的完整 160 格结果

新配置 `2026-11-12-fd2d-inverse-q-raw0-full160-01-config.json` 的 SHA256 是
`8dbe7f570c9ee7fa88e9eaa785b5fc9bc06194c9a6072db0815bc003efe0b3a3`。
构造及实际 source 扩展 session 48458 自然 exit 0，耗时 6.425 秒。

完整 m2 计算入口为 `fd2d-inverse-q-tail-m2-audit.mjs`，SHA256 是
`7d4741a65070544c17bc956ca59879921ed188492fb08021953a73b07f0e6666`。
它从未改深端 $\pi=0$ 起始，穿过所有 160 格；中途没有把 momentum 重置为零。采用直接 canonical momentum 恢复 $J$，避开深层 $H_r-4H/r$ 的相消。真实 session 30569 自然 exit 0，48.921 秒；报告 stem 为 `2026-11-12-fd2d-inverse-q-raw0-full160-m2-n256-01`。

| 量 | 实际有限结果 |
|---|---:|
| cut 半径 / $w$ | $0.65$ / $0.1$ |
| $D_2=H_r/H$ | $6.153846153823516$ |
| 与 $4/r_{\rm cut}$ 的差 | 约 $-2.26\times10^{-11}$ |
| 桥内端高度比 $\gamma$ | $0.09595427341627218$ |
| raw0 物理 II 行和峰 | $329.25522416726636$ |
| raw0 $|\Gamma|$ 峰 | $971.9564520963041$ |
| 完整尾部物理 II 行和峰 | $975463.9932940007$，raw1 |
| 完整尾部 $|\Gamma|$ 峰 | $10062049.763920128$，raw1 |
| 有限母面曲率采样峰 | $6.996583737280851$ |
| 有限经线长 | $0.33308596333452345$ |
| 有限高度差 | $0.028916858120417215$ |

接口位置和 $w$ 浮点差为零，$w_r$ 差约 $2.19\times10^{-17}$；cut 的 $w_r$ 误差约 $5.55\times10^{-15}$。S5 端值校准 $c\approx-7.55\times10^{-15}$。虽然很小，本计算仍重新推进了校准后的真实物理方程，没有直接把名义 $H=r^4Q$ 当作实际全尾解。

因此本候选确实实现了温和局部桥，但完整尾部放大比原 wc01 更差。它不进入新的非线性 DN 消耗。接口保留，后续设计直接优化上节的全尾耦合目标；局部 $N=2,N=3$ 如果只降低自身峰而不压低 $\gamma$，也不能凭局部结果升级为全尾候选。

## 5. 未支付的条件

本报告没有连续 ODE 包络、无限模态非线性尾、活动核全域曲率/reach 或强幅度结论。有限背景和端口数据只供新物理设计及后续实际 BVP 输入。失败数据的作用是定位可改的有限桥传输，不是证明同 $g$ 非线性分支不存在。
