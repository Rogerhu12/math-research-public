# 当前真实 native576 迭代接 R273：源码可行性与最薄接口

- 作者：`geometry`；日期：2026-11-14 UTC。
- 分类：只读源码分析与条件接口；没有选定下一算法、没有新增执行源或工作流、没有科学计算。
- 相关证明：[R273](../results/R273-complete-native-damped-square-root-chain.md)。
- 本文针对未来某个**真实当前迭代状态**；不把 actual28/54 的固定旧输入重新标成新状态。

## 1. 原同步调用的精确切点

从已保全原 runtime core 的 internal solve 源，可见每轮次序为：

```javascript
const ev=evaluate(states,target,true,scales);
last=ev;
history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD});
opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
if(ev.norm<(opts.tolerance??1e-10))break;
const cor=correction(ev,states,target);
history.at(-1).chartCondition=cor.maxChartCondition;
opts.progress?.({...history.at(-1),phase:'correction'});
```

之后是原十个 alpha、原 `evaluate(trial,target,false,scales)`、原 guard、原严格 norm 下降和原失败语句。

因此最薄的新算法切点是**替换单个 `correction(ev,states,target)` 调用**，把这一次真实 `ev`、当前 state、target、原 scales 和 iteration 传给一个独立同步桥。with-J evaluate、原 tolerance 判断和完整原试探循环不应替换。若当前状态已通过原 tolerance，这个分支本来就不执行 correction；接线必须保留该行为。

这里的 correction 是原核心词法作用域中的函数。仅赋值一个导出的 `dn.tail` 属性，并不会改变原 solve 内部调用。需要独立 hook 对唯一源锚作明确可逆替换，记录原 core、instrumented core、原/新内部 solve、唯一替换及原十试探正文的 SHA。已有 capture/replay 的 source-roundtrip 方法可复用；新身份不能冒充未修改的求方向算法。

## 2. 从本次 ev 保全什么

当前原 native 布局仍是 `M=112,K=224,depth=576`；全部577节点、129248个方向未知量都保留。新的输入应来自**同一次**完整 with-J evaluate，具体为：

| 保存对象 | 原来源 | shape 或范围 |
|---|---|---|
| 原完整 shape J | `ev.flows[n].J`，已含原 port 转换 | `[576,224,224]` |
| 原段残差 | `ev.residuals[n]` | `[576,224]` |
| 原段输出 | `ev.flows[n].out` | `[576,224]` |
| 本轮状态 | `states` | `[577,224]` |
| 当前 cut residual | 按原顺序 `states[0][j]-target[j]` | `[112]` |
| 当前 far residual | `ev.end` | `[112]` |
| 原 target | 本次 solve 的 `target` | `[112]` |
| 原尺度 | 当前 solve 的 `scales` | `[577]` |
| 原 far graph | 原 `graphs[depth]` | `[112]` |
| 物理 H | 本次真实 request.height | `[112]` |
| 已算 guard/mean | 每段 `minA,minD,meanHeight` | `[576,3]` |

每项保留原 binary64 字节及负零；不重新求 residual 来替代已有原数组，不从旧28复制某段 J，也不按旧坐标插值当前状态。cut residual 可按原 subtraction 顺序额外保存，不能假定为零。每段的 shape J 为原实际 floating with-J 数组，不宣称是真实连续映射精确导数。

数组 manifest 与本轮 receipt 至少绑定 iteration、state rawSHA、完整 H/target、sigma、far、graphs/gains、raw-node/stage 布局、source/config/runtime identity、完整 J 流 SHA、r 流 SHA及原 `ev.norm/minA/minD` 的原 numberRecord。若原 solve 已在前面接受若干步，此处绑定的是该轮状态，不是首次注入的 selected seed。

单是576个224×224 f64 J约231MB；保存其他本轮原数组的量级较小。这是保全已经算出的 J，不新增 RHS/ODE/J 调用。大阵只进 artifact，Git 保留完整 manifest 与有界报告。

## 3. R273 因子类本身可以用动态 depth

冻结 `exact_20261114_native_damped_chain_qr.py` 的 SHA 为
`9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。
其 `NativeDampedChainQR` 构造器从 `system.depth/K/M` 取维数；逐段流读 `system.stages()`。factorize 和 solve 使用动态 D，不在算法内把 D 写死为1372。完整 penalty、cut/far、常数能量与回代都保留。

可复用的 system API 如下。

| 接口 | 新576对象应提供的内容 |
|---|---|
| `B` | 既有数组、描述器、f64 bytes和元数据 helper |
| `M,K,depth` | 本次原 native 的112、224、576 |
| `binding` | 新当前状态/本轮矩阵的独立身份，不能用旧 `e929…` 或 actual54 ID |
| `arrays['original-scales']['raw_sha256']` | 当前原 sigma 的真实字节身份 |
| `all(name)` / `raw(name)` | 本次 stage r、cut r、far r、sigma、far G 等完整原数组 |
| `stages()` | 顺序输出全部576个真实 J；不得删行或截模 |
| `J_rows[n]['raw_sha256']` | 本次对应原 J 完整块的字节身份 |
| `stage_bytes()` / `stage_raw(n)` | 同一原 J 的精确读回；不重新形成它 |
| `cells` | 当前原 stage/rawCell/rawSegment 来源映射 |

不过，冻结文件的 **main、SYSTEM_NAME、外部 schema 与 exact-readback context** 是 actual54的1372目标。不能直接运行该 main，再把其标签改为576。需要新独立薄入口使用上述当前对象，显式给新 source/schema/result 身份。

完整 exact-row 核的 `stage_job/boundary_job/decode` 可按动态维数复用，但新 context 的 row order、来源标签与矩阵身份须准确对应当前576系统。旧 direct-LD context 会附加旧1372来源语义，不能未经说明套用。这里的精确读回仍是保存的有限数组代数诊断，不是原 nonlinear trial 的新阈值。

对原576对象，完整方向已经是原577节点；`old_to_new` 可显式为恒等映射。不存在1373→577的插值或限制费用，但完整state与direction身份仍须绑定。

## 4. 同步 JS→Python 的两种明确边界

### A. 原 solve 内同步求方向

原 `solve`/`correction` 都是同步函数，不能返回 Promise 后让原十trial把它当方向。最薄同进程接线是：

1. 新 hook 在 cor 调用处从真实 ev 保存本轮输入，完成 manifest 后再启动 child。
2. 使用同步子进程调用新 Python 方向入口；原 Node 在此等待。
3. Python 只读上述本轮原件，返回完整原坐标577×224方向和独立 result。
4. Node 校验该方向实际 result/source/input identity、全 raw 字节、全部行与负零，直接返回 `{delta,maxChartCondition:null}`。
5. 原十trial立即使用该完整方向。原 scope 中不再调用另一遍 correction，不重算同一个 with-J evaluate。

子进程 stdout/stderr 应各写独立本轮日志文件；不能继承原 native worker 的 JSON 协议 stdout。Node 与 Python 要明确各自退出码、actual error和未完成状态，避免不完整方向冒成功。每轮独立目录也能防止陈旧结果误入当前状态。其内存预算应计入仍驻留 Node 的原 ev/J 与 Python 同时工作的部分，磁盘预算包含全部保留的因子及常数行。

这需要新独立 hook/薄 Python入口；当前57只做第一次缓存基态的一轮 replay，其 hook 不能原样充当这样的完整多轮算法。本文未实现或选定该方案。

### B. 明确的两阶段继续

也可在本次完整 evaluate 后保存并计划停止，另一个 Actions 步骤从这些真实新数组求方向，再以同一真实新基态的已存 with-J结果运行原十trial。

此时 replay 的缓存标签必须是这份新 capture，不能仍写 actual28；新的 direction、本轮state/H/sigma/far与原 guard 来源全部重新绑定。若试探接受，再从实际 selected 状态启动原完整 native，重新计算新 J 与 fresh audit。这是明确的多阶段流程，不是假称一个未中断的原 solve，也不等于已经实现自动迭代 R273。

## 5. soft cut/far 与最终原验收

当前有限线性残差的符号应保持：

$$
e_{\mathrm{cut}}=r_{\mathrm{cut}}+\delta Q_0,
\qquad
e_n=r_n+J_n\delta y_{n+1}-\delta y_n,
$$

$$
e_{\mathrm{far}}=r_{\mathrm{far}}+\delta\Pi_D-G_D\delta Q_D.
$$

R273使用全部原尺度行和每个节点的显式eta penalty，没有把cut/far设成硬约束。得到的方向必须完整交给原 trial，不能私自清零cut或far分量。H、target、far graph和原sigma始终保持本次原问题；改变求方向算法不改变最终方程。

原试探仍是 $\alpha=1,1/2,\ldots,1/512$，原no-J evaluate、原全部guard与严格原norm下降。R273的L2下降、模型梯度或保存有限矩阵的exact e都不替代它，也不追加成功门。

完整 native 成功仍须原solve容差、完整cut jets/mean、所需heightJetJacobian和fresh audit实际返回。最终返回时的原 evaluate/J路径也不绕过。若Riccati或R273方向之后再次失败，必须保存真实失败当轮的状态和对应数据；不能把最初一次有效方向描述成完整迭代成功。

## 6. 当前结论

源码层面的切点和动态 QR 核都明确。必要的新内容是当前576系统身份适配、同步桥或明确分阶段状态机，以及真实新状态的读回合同；不需要改g、ODE步、原far、原sigma或原十trial正文。

本条只说明可行接口，没有证明当前非线性问题会因该更换而收敛，也没有依据尚未返回的57试探预选该方法。57真实结果仍优先按原记录审计。
