# 2026-11-12：直接相邻块的配点 Jacobian

visible-larger-20261112。线性代数与存储改进，**不是新的闭图或更强幅度声明**。

## 相同方程

`root_block_collocation.py`取代本进程内SciPy的`prepare_sys`，保留原配点函数和边界函数。点上Jacobian分24个径向区间独立求值，不改变角积分、物理g、参数或容差。设区间长h，端点状态Jacobian为J0/J1，中点为Jm，则保留原公式

$$A=-I-\frac h6(J_0+2J_m)-\frac{h^2}{12}J_mJ_0,$$
$$B=I-\frac h6(J_1+2J_m)+\frac{h^2}{12}J_mJ_1.$$

参数块同样保留原中点链式项，边界A/B/P原样使用。存储为局部A/B/P与端点BC，不再创建全局COO/CSC/CSR与两份整数坐标。`DirectBlockQRFactor`使用既有的平衡相邻QR消元及同一forward/backward解法；root固定g包装器先清除不用的旧factor，再构建新factor。

这些都是存储/运算顺序变化。不会放宽Newton、线搜索、域检查、外层网格误差或边界验收。分批的浮点运算顺序有轻微变化，**不宣称逐位相同**。环境版本及原函数hash另存JSON。

## 真实Jacobian核对

`root_block_collocation_check.py`在保存的真实neck上取122个节点子集，分别装配原稀疏矩阵和直接块，比较同一RHS的Newton步。子集仅为线性系统核对，不是重新求解或加密。第一次检查误把`--nodes100`当作缩网格；固定g恢复实际合并成957点，因此主动中断，改为检查器内部明确选子集。

| 系统 | 固定g M20 | 含delta/LB控制 M12 |
|---|---:|---:|
| 状态维数 / 参数数 | 61 / 20 | 37 / 12 |
| 原保存节点数 | 859 | 873 |
| 检查节点数 | 122 | 122 |
| 最大Jacobian条目差 | 5.68434e−13 | 4.97854e−12 |
| 与原块QR步的相对差 | 8.12270e−14 | 1.04570e−12 |
| 与稀疏LU步的相对差 | 6.86409e−13 | 1.06903e−12 |
| 相对后向误差 | 4.51406e−16 | 3.14705e−15 |

两个JSON记录原矩阵、输出、全部源码hash和完整浮点值。核对之后已经启动原q0775固定g/M20/N512/tol1e−7的真实恢复。首859点QR峰260392KiB，原稀疏装配同点585316KiB；首Newton配点残差仍6.30753546e−13。后续solver在1634点通过，但物理包保存前signal9；完整失败与恢复防护见root-c2-refinement.md，仍没有该tol的已保存物理曲线。

## 实际非线性尾联解

`root_actual_bounded_neck.py`也使用直接块，并在每次点上Jacobian批次后回收已不可达的Flow自引用环。它使用原stored-tail完整H/真实DN和实际验收；prefix的delta/LB仍为设计未知量，因此不得称作固定prefix-g加密。已启动恢复q085到M16真实尾联解，用旧真实q040/M14尾响应作初猜（M14→16符合原remesh要求）；旧物理尾数据不变，当前配置的angular/linearSteps比旧warm更高。有限尾闭合仍不等于精确无限闭合。

首次actual M16 worker完成ready和旧M14→M16 warm后，在第一次真正solve请求前退出，parent随后BrokenPipe。没有新的实际接合响应，也无证据判方程不可解。下一轮延后worker启动到prefix warm和GC后，并记录关闭前后returncode；只是降低并发内存与补诊断。

## 本轮完成的存储验证与后续实际接口

上述未保存的同g tol1e−7轮现已正式重做，1634节点/3轮、178.49秒、峰422684KiB、完整exit0。raw与物理五次包均成功先行落盘，原默认audit也正常完成；详见root-c2-refinement笔记。真实raw写出和物理包写出已被实际运行覆盖，显式`--postprocess-only`恢复入口尚未另跑，二者不能混称为都已验证。

后续补验：显式`--postprocess-only`已真实完成，82.54秒/峰228604KiB/exit0；物理五次系数逐位相同，全部默认audit及固定物理数据精确一致。恢复报告和命令另存`root-raw-postprocess-check`两个小JSON；本段更新覆盖上一段“尚未另跑”的当时状态。

actual bounded入口新增可选`--geometric-flow-cache-size`（默认0），仅缓存相同构造输入的前缀Flow，不缓存真实尾求解。`strong_actual_cache_check.py`通过实际嵌套加载链，在M16/N384的真实warm上重复3点前缀J/PJ：逐值一致，4 miss之后4 hit；尾启动guard调用0次，没有worker/BVP。显式cache8可用于后续实际联解，原完整H、true DN、physicalBC与mean验收不变。延后tail启动仍独立保留。

另外真实`tail_height`已核实包含bridge.sigma=−1，完整向量为−q*y[iz:]；禁止再为了让H2同号而额外做π/2旋转。实际强分支的正H4与容量ray的负H4仍需真正的完整向量求解。

## 06:05 UTC：真实尾中间状态即时恢复

实际入口现在允许显式 `--client stored-resumable`，默认仍是 `stored-bounded`。前者直接复用已完成M24/M32的原g客户端，保存接受trial但仍执行最终完整Jacobian/audit。另在每次成功affine内层解之后、真实非线性尾复核之前，保存独立raw配点状态；该记录明确 `solver_success=false`，只能重启，不能绕过真实边界验收或作为物理C²曲面。详见 `2026-11-12-root-actual-resumable-recovery.md`。
