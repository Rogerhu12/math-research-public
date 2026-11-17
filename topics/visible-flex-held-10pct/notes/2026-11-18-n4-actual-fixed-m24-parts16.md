# 原实际 n4 几何的 M24／parts16 完整联立通过有限门

维护日期：2026-11-18（UTC+8）。接
[实际 M20 固定几何精化](2026-11-18-n4-actual-fixed-m20.md)、
[M24／parts8 终态](2026-11-18-n4-actual-m24-parts8-terminal.md) 与
[最高模式残差定位](2026-11-18-n4-m24-tail-residual-location.md)。
本次已完成实际前缀—尾外循环及最终两阶 seam 审计，不只接受了 warmup。
完整标量证据为
[eta010_q010_fixed_m24_parts16.json](../scripts/resume_n4_tail/eta010_q010_fixed_m24_parts16.json)。

## 保持原几何并完成实际联立

物理参数保持原 $w_{\rm cut}=.08$、$\eta=.1$、规范幅值 $q_*=.01$、
$v_u=.35$、$\delta=.030027177128250468$、$v_d=.2483630655929876$。
输入为接受的实际 M20 checkpoint。完整核心三 jet 初值最大差
$2.09\times10^{-15}$，完整材料图差 $1.61\times10^{-15}$，1913 个旧节点保留。
原 parts8 失败迭代态仅通过原嵌套规则初始化 parts16；没有将失败态改判为接受。

本次模式 24，prefix 角求积 1536，原 BVP 容差 $10^{-8}$、节点上限 6000；
尾 spacing 4、$N=512$、parts16、每段 RK4 16 步，原残差门 $2\times10^{-9}$。
使用已独立逐项检查的 n4 共享 periodic 引擎；原方程、稀疏组装和根守卫不变。

四次实际尾均重新求解／评估。第一次全高度审计残差
$9.19312\times10^{-10}$；第三次在真实新高度上连同完整 Jacobian 接受，
残差 $8.26757\times10^{-10}$；第四次最终独立 audit 接受，残差
$9.82471432666221\times10^{-10}$。没有用线性 DN 代替这个外循环。

最后 prefix 有 1930 个节点，最大 RMS 残差
$9.996034925845326\times10^{-9}$，真实缩放 BC 残差
$4.398387951124165\times10^{-10}$。实际幅值为
$q=.009999853308619924$。三个 prefix Newton 步均完整接受，没有域或 merit 拒绝。

## 完整误差不是单调下降

| 诊断 | 已接受 M20／parts8 | 本次 M24／parts16 |
|---|---:|---:|
| 完整 prefix metric FFT $\ell^1$ | $1.95043\times10^{-9}$ | $8.15575\times10^{-9}$ |
| 完整 prefix flow defect | $3.34182\times10^{-8}$ | $1.75633\times10^{-7}$ |
| 完整 Cartesian Darboux defect | $3.51076\times10^{-6}$ | $2.46911\times10^{-6}$ |
| 最后实际尾 shooting residual | $1.66494\times10^{-9}$ | $9.82471\times10^{-10}$ |

本次完整 prefix metric 仍小于 $10^{-6}$，但比 M20 增大约 4.18 倍；
flow defect 也增大。Cartesian Darboux defect 则下降约 29.7%。
这不构成 metric 单调收敛证据，不能据此声称任意 $\varepsilon$ 已经解决。
本次 prefix 审计使用 4008 个径向位置和 1552 个整周角点。

最终实际尾的完整 Darboux 诊断为 $2.72958\times10^{-7}$，实际 metric 诊断
$4.81792\times10^{-12}$，最小根量 $A=.942545096511274$。
平均高度一／二阶 jet 差分别为
$1.50394\times10^{-12}$、$-3.49656\times10^{-11}$；
非平均一／二阶 jet 差分别为
$4.39839\times10^{-12}$、$1.88820\times10^{-8}$。
切口 metric 与 C1 metric FFT 诊断分别为
$7.95057\times10^{-9}$、$6.85898\times10^{-7}$。
这些仍是有限离散／采样审计，并未证明完整 Cartesian 连续粘接或无穷闭合。

## 来源、执行与范围

完整输出 checkpoint 哈希为
`9206147c67a9012351c623a7b5b09441b13b886d48f307dd88823a74c2312644`；
最后实际尾哈希为
`70504deb67f263d6780bfa75cbb932efd59d591eb42d1cb5968e80e364725992`。
采集时核对了全部 prefix 分块哈希和全部尾响应。

新执行包装 [refine_actual_tail_shared.py](../scripts/resume_n4_tail/refine_actual_tail_shared.py)
只保留共享客户端自己的 stderr 句柄、安装既有同核心紧证书并记录失败初值身份。
原固定几何 solver／TailMixin／实际外循环保持原样。
采集器 [record_shared_fixed_actual.py](../scripts/resume_n4_tail/record_shared_fixed_actual.py)
在原完整审计采集器上增加执行包装、初始失败态与资源来源。
命令、原／新源码、输出和日志哈希均在证据文件中。
worker 正常退出，内部总用时 1833.22 秒；资源记录不被解释为整个进程树峰值。

本支仍为 $\lambda=0$，未取得精确保护圆弧，也不是完整闭面或 10% 构造。
本层的实际意义是原物理几何下更高模数、更多尾分片的完整真实联立结果。
下一关键实验是把通过完整 metric 门的新 raw 圆化设计接到真实非线性尾，
而不是仅凭本层成功机械增加模式数。
