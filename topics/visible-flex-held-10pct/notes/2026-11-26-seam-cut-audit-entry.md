# 原 accepted 尾切口的轻量连续高度审计入口

日期：2026-11-26。此文件登记一个待真实 accepted 输入运行的审计入口。
当前仅通过语法检查、精确解析背景 Darboux 零残差和区间端点转换校准；
没有产生新 full-H 接缝数值结论。

源码：
[seam_cut_height_compatibility.py](../scripts/resume_20261126/seam_cut_height_compatibility.py)。
输入是原 client 保存的 `.json` 或 `.json.gz` 包，
结构为 `{request,response,config,source_sha256}`；
脚本强制要求 `response.converged === true`，且
$0\le\mathrm{response.residual}\le\mathrm{config.solveTolerance}$
不超过已登记原门限 $2\cdot10^{-9}$，再读取 `response.jets`。
`height/slope/second` 是不含零模的完整物理
$\cos(\mathrm{spacing}\cdot j\theta)$ 系数，不再乘除 $\sqrt2$。
`meanSlope/meanSecond` 含原背景，保持原字面值。
`modes/spacing` 来自 `config` 或 `response.checkpoint.parameters`；
两者存在时须一致。

最小 CI 命令如下；`ACCEPTED_PACKET` 必须指向该 runner 实际保存的原包，
不能用手写 `converged=true` 的模拟数据代替。

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_cut_height_compatibility.py" \
  --tail-response "$ACCEPTED_PACKET" \
  --source-port "$WORK/m24-linear-port.json" \
  --out "$WORK/cut-height-continuous-audit.json"
~~~

依赖是 Python 标准库和 `mpmath==1.3.0`。脚本不调用求解器、不改变完整高度迹、
原 mean 或目标度量。目标 cut 固定为
$R=\operatorname{binary}(.3)$、$w=\operatorname{binary}(.08)$、
$w_R=-7w/R$。worker 保存的背景 `E/Ep` 另行记录；
不因它们与真实目标 cut 有微小差异而重写保存的高度系数。
原包的五个背景 cut 字段必须逐字等于该 runner 原 worker 导出的
`m24-linear-port.json` 的 `cut`。完整背景配置同时和该 port 及已登记
`2026-11-20-m3-m24-warm050-execution.json` 核对，包括全部 160 个
`valleyControls`、归一化/校准参数、方向及物理 depth。不得把
checkpoint 的数值网格深度替代配置中的物理 depth。
所有背景字面量与真实 R58 cut 的差另作精确有理记录；
脚本不会通过强行令两者相同来隐藏其误差。

## 连续条件实际如何支付

首先由精确有理 Fourier 系数的 $\ell^1$ 界给出连续 $S,D,A$ 下界。
若这个充分条件过松，再细分整个角周期，逐角区间求值并覆盖所有角度。
这不是以网格正值替代连续正值。

对于连续转角积分，脚本在复条带 $|\operatorname{Im}\theta|\le\sigma$
上用 $\cosh(m\sigma)$ 控制有限 Fourier 多项式，验证 $S$ 不为零且
$\operatorname{Re}D>0$，从而选取与实轴正根一致的解析 $\sqrt D$。
若 $|\omega|\le M_\omega$，由将 Fourier 系数的积分路径平移
到上下条带边界可得 $|\widehat\omega_k|\le M_\omega e^{-|k|\sigma}$。
因此真正等角 $N$ 点平均与连续归一化积分之差不超过

$$
\frac{2M_\omega}{e^{N\sigma}-1}.
$$

等角节点上的三角函数、平方根及求和使用外包区间运算，
这里没有把字面节点的浮点正交性当成精确恒等式。
若全局系数条带界过松，脚本仅返回覆盖全周期的区间积分；
不会把一个未经支付的高精度采样值输出为连续证书。

归一化 Darboux 残差完全使用 `Fraction` 作 Laurent 多项式运算。
若 $V_m=mh_m$，则 $u_\theta=iV$；代码在
$-B_H^2$ 项中正确保留 $i^2=-1$，最后除以 $ER^2$。
输出残差系数绝对值和是严格全角度上界。
二阶差异的系数仅按
[均值源码相容说明](2026-11-26-seam-mean-source-compatibility.md)
中的“同完整一阶迹”条件报告。

在 $S,D,A$ 分支已支付后，连续转角包围还能给出一个局部的唯一平均斜率根括区。
这只固定一个标量，不等同于完整径向尾 BVP 已解。
输出始终明示本脚本没有证明 full-H、桥一阶迹相同或 Cartesian $C^2$ 接缝。
warm `.25 H` 包即使通过这项审计，仍只是对应缩小输入的尾，
不能替代实际桥的 full-H 端口。

## 重建与执行状态

旧临时 checker 在共享环境重置时丢失；此版本依据已核对的真实 packet
结构重建。已执行 `py_compile`，以及不读取伪造 accepted 包的函数级
校准：解析旋转背景的 Laurent Darboux 残差精确为零，
有理数到区间和角区间到三角函数的包含关系成立。
第一份真实 accepted 包的运行记录应另存小摘要，不能把这些校准算成实际尾通过。
