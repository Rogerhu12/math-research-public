# 把原 RMS 两个 Lobatto 取点纳入原 Newton 试步域：单一新入口

状态：**源码和唯一启动计划已准备，尚未执行新初猜重建、BVP 或实际 DN。**
它回应上一条真实失败 `2026-11-18-q060-circle-trace-coupled-rms-domain-failure.md`：
原 Newton 只直接检查节点和中点，返回后原 RMS 在额外取点越过 Frenet 域。
这次新增同一原域检查的取点覆盖，保留原物理问题、有限控制空间、方程和所有阈值。
不重跑旧入口来补造其未保存状态。

## 1. 原调用链与漏检位置

本次绑定实际安装的 SciPy **1.17.0**，其 `scipy/integrate/_bvp.py` SHA-256 为
`59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2`。
原 `f6curve_domain_newton.py` 为
`6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654`。
新 plan 和 record 同时锁定版本、文件和派生 Newton 源，不把某个通用 SciPy 说明代替实际实现。

原 `prepare_sys` 返回 `col_fun` 和 Jacobian callable。
`col_fun(Y,P)` 返回原四元组

$$
(\texttt{cr},\texttt{ym},\texttt{ff},\texttt{fm}),
$$

其中 `ff` 是原节点 RHS，`fm` 是原中点 RHS。
原 Newton 的 trial 域检查来自这次调用及原 BC；额外 Lobatto 点原先到 Newton 返回后才检查。
原 RMS 使用相同 $x,h,Y,\texttt{ff}$ 构造 cubic 后取

$$
x_m=x[:-1]+\frac h2,\qquad
s=\frac h2\sqrt{\frac37},\qquad
x_1=x_m+s,\quad x_2=x_m-s.
$$

每个残差分量原样除以 $1+|f|$，再计算

$$
\left[\frac12\left\{\frac{32}{45}\|r_m\|^2+
\frac{49}{90}(\|r_1\|^2+\|r_2\|^2)\right\}\right]^{1/2}.
$$

这份 RMS 公式、尺度和停止判断不改。

## 2. 唯一新增的数值检查

新 `m3_lobatto_domain_guard.py` 包装原 `prepare_sys`，保留它传入的实际
$x,h$ 和 `fun_wrapped`，不通过 `cumsum(h)` 重造网格。
新 trial `col_fun` 按以下顺序工作：

1. 调用原 `col_fun(Y,P)`，取得其原四元组；
2. 调用原 `_bvp.create_spline(Y,ff,x,h)`；
3. 按实际 SciPy 的同一字面运算顺序计算 $x_1,x_2$；
4. 依原 RMS 的顺序调用 `fun_wrapped(x1,sol(x1),P)`，再调用 $x_2$；
5. 若两次原 RHS 均返回，返回**同一个原四元组对象**。

新检查不计算残差范数、不比较一个新 RMS 阈值，也不修改四元组内容。
它只让同一原 `FloatingPointError` 在已有 trial 域分支被拒绝。
原 Jacobian callable 直接返回，没有新增关于这些检查点的残差行或 Jacobian 行。

原 24 次 Newton 循环、最多 8 次 factorization、21 档 backtracking、
仿射不变 merit 及其接受条件全部保留。
初始状态若不能通过新增覆盖，也按同一原异常退出，不剪裁几何数据或强行接受。
这个规则加强有限试步的域覆盖，会改变数值迭代路径；它不是旧失败轨迹的逐位重放。
有限五点覆盖也不自动成为连续径向/全角 Frenet 证书。

## 3. 在更内层保存真实状态

原失败暴露出：只在 `solve_bvp` 返回后保存，覆盖不到其内部 RMS 抛错。
新记录在以下边界落盘完整状态：

- 原 Newton 初始求值之前；
- 原首次 `evaluate` 成功之后；
- 每次原 `accepted` 赋值完成后；
- 普通 return 和 `except RuntimeError` 的 singular return 之前；
- 若异常逃出 Newton，保存最近一次实际求值状态及异常阶段。

每份保存包含完整 $x,h,y,p$、七项实际物理控制、原节点 `ff`（已经产生时）、
由同一原 `create_spline` 构造的完整 cubic（可用时）、实际 DN 锚和来源。
outer 的 inner 编号、prepared-system 编号、Newton-call 编号及循环 iteration 分开记录。
Newton 层尚无 BVP 最终 RMS/message/success，因此这些字段明确为 null。
异常快照不单独给一个接受结论。当前源的该文字标签为 `Unaccepted evaluation`；
它不能用来断言这个状态从未被接受：例如后续 Jacobian 抛错时，最近求值可能就是
已经接受的当前状态。应以单独的 `accepted_assignment` 记录判断；本条将这个标签局限
明确保留，不据此伪造新的状态分类。当前尚无该新方法的实际执行或误分类实例。

每个 accepted snapshot 是真实状态恢复材料，但没有保存 LU、step、cost、refresh；
从它重新调用 Newton 会重置这些算法状态，不能称作逐位原控制流续接。
真正 return 前的 snapshot 则给出原随后的 RMS/mesh 流程所用状态。
本条没有为了保存而改变任何原求解返回对象。

安装次序固定为：原 domain Newton install → 既有只读 trace install →
新 `prepare_sys` 域覆盖和观察调用。
既有 trace 仍委托原 domain 模块的函数，原 sparse LU/Jac 记录保留。
旧源码文件不修改；带观察语句的 Newton 函数单独写入新 scratch 目录并绑定 SHA。

## 4. 保持同一声明设计和起始锚

新入口使用之前唯一 q060→circle 初猜：
$q=0.05210565550627671$，M8/25 状态，
$B_2,\ldots,B_6,T,U$，$\lambda=1$，窗口 $a=.21,b_p=.32,b_c=.4$。
基础 profile 仍是旧 q060 最终冻结值，新 `p0=0`、`fixed=False`、warp reference $.06$。
原初始数组的完整哈希、七项物理控制和尺度保持；不扫 $q,t,u$，不换 M 或窗口。

首个相同八项 $H$ 仍使用原真实 accepted DN 锚，任何后续新 $H$
仍经原 actual solve/Jac/audit 和原 BC 判断。
原域 floor、6000 节点上限、RMS/BC/merit 门、八轮 outer、
原 physical C2 导出和 prefix/seam 审计均沿用上次冻结入口。
不存在本次新接受态，不能据此声明同 $g$ 的终点精化、metric 或握持比例。

## 5. 冻结文件与已执行范围

本次实际执行仅为 metadata/source 准备：

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/run_q060_circle_trace_lobatto_guard.py \
  --prepare /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-lobatto-guard-v1
```

工具 chunk `ceaa2c`、真实 exit 0。
读取 69 项绑定来源和原数据身份，生成派生函数并作语法编译，没有执行核心、初猜、BVP 或 DN。
新唯一计划为 `lobatto-launch-plan.json`，SHA-256
`da2c3d945ac45fcb04dc456c7e00283fb1c8b9bdbe4d2fe5fb5d3c8687c2374b`。
后续只能使用同目录 **`lobatto-launch-command.json`** 中的独立 observer 命令。
同目录由父入口生成的普通 `launch-plan.json`/`launch-command.json`
只是未执行的继承比较材料，不是这次新方法的启动项。

可入库四件为本 note、`m3_lobatto_domain_guard.py`、
`run_q060_circle_trace_lobatto_guard.py` 和
`q060_circle_trace_lobatto_guard_entry_record.json`。
旧入口、旧失败输出和任何已登记的状态都未覆盖。
