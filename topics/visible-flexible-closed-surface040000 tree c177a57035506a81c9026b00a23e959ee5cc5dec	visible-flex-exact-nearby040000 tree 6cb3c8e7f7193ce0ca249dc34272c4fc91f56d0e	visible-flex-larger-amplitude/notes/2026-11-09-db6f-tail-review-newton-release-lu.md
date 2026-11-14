# Newton 重组前释放旧 LU：函数批次完整独立审查

2026-11-09，`/root/tail_review_continued_2`。
审查对象为作者七件封存批次
`prefix-newton-release-lu-publication.json`，SHA256
`59e915d98e058adbdaf8682b6c3cfaed8cd07045a5a2d271686974a90ecdd29d`。
本审全文阅读原/新 Newton、显式选择器、作者纯检查程序、完整方法稿，
并复核所引用的原 coupled 安装/计数路径、谱权旧身份门和 SciPy Jacobian 组装/网格循环。

**结论：通过，限于单行生命周期修订及其显式函数选择接口。**
它保持原数学算法、容差、factorization 参数、线搜索和计数对象，
诚实地给新运行函数一个不同的来源身份。
本批不是可直接塞入旧 true-M14 v1 的完整 launch；完整新的 true-M14
selector/preparer/auditor 接线另须全文审查。
这里没有调用 `select_newton()`、任何 install、完整 Newton、BVP、真实 LU、DN、root、RK 或 flow。

## 1. 函数源码与控制流证明

冻结原 `f6curve_domain_newton.py` 为
`6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654`。
新 `db6f-prefix-domain-newton-release-lu.py` 为
`23ec0f1fe25bc8f904b771f020449c7d95e071d2fc17b6daf4caa93ccd31880b`。
本审独立从 AST 找到两份唯一 `solve_newton` 定义；去掉新函数唯一的
`factor=None` 行后，整个函数源码逐字相同，去掉该赋值后的 AST 也完全相同。
插入位置确为：

```python
if refresh:
    if factors>=8:break
    factor=None
    try:factor=splu(jac(y,p,ym,ff,fm,br))
    except RuntimeError:return y,p,True
```

原 Python 赋值先求右侧。旧 `factor` 因而在替换 `jac` 和 `splu` 期间仍有该局部强引用。
新语句先解除这个引用。此处的正确性须覆盖全部控制流，而不能只说“上一次 LU 大概不用了”。

1. 内部 residual/BC 停止条件在分支之前，原已达标路径完全不执行新语句。
2. `refresh=False` 时，新语句不执行，仍用原保存的 step/cost 和原 factor 作试步；
   这是全步接受后复用旧 Jacobian 的实际路径，未被破坏。
3. `refresh=True` 但 `factors>=8` 时仍先退出，既不释放旧对象，也不增加 Jac/LU 调用。
4. 允许 refresh 时，在新 `splu` 返回前没有任何后续语句需要读取旧 factor。
   成功后原代码也会以新 factor 覆盖旧值；新版本只提前释放旧引用。
5. `jac` 或 `splu` 抛 `RuntimeError` 时，原代码立即返回 `(y,p,True)`；
   没有使用旧 LU 的恢复分支，所以提前释放不删除已有回退算法。
6. `MemoryError` 和其它未被捕获异常仍向外传播；本改动没有把它们变成成功或静默退回旧 LU。
7. 新 factor 的 `solve(residual)` 本来在上述 try 之外。其异常边界未改，
   之后21档线搜索、merit 常数 .4、domain 拒绝、接受计数及下一次 refresh 判定也全部逐字未改。

第一次 refresh 尚无旧局部 factor；赋值 None 合法，但该次不能声称省去一份旧 LU。
只要相应数值操作在两个版本中均完成，数值回调次序、参数与数学接受规则相同。
资源异常能否出现本来就是此改动希望改变的对象，因此不能进一步断言两版资源失败轨迹相同。
本审也不推导跨运行/跨平台逐位一致性。

这个论证针对已绑定的实际回调及 `splu`，不把任意栈反射或任意析构器副作用加入数值接口。
“解除一个 Python 局部强引用”不等于“原生分配器立即把相同字节数归还系统”，
更不等于已证明新的峰值或收敛。本方法稿正确区分了这些命题。

## 2. 显式选择、原 STATS 和恢复协议

全文审过的选择器为
`db6f-prefix-select-domain-newton-release-lu.py`，SHA256
`bc7d376ca52a565e5b345aeef40319578ae8ea3b74dbe0333c5e26c927c68916`。
它本身不作为 true-M14 solver 使用。

### 2.1 先要求原安装身份

`original_runtime_gate` 先核两份源码的冻结 SHA 与单行 AST 差分，
再核 SciPy `_bvp.py` 的确切 SHA、原 function/install 的来源和签名。
它明确要求当前 `_bvp.solve_newton is original.solve_newton`。
在还只有 SciPy 自带函数的全新进程中，应当拒绝选择，不能由“函数签名类似”跳过原安装门。

`select_newton` 的第一条可执行语句是这个 gate。
随后仅加载已绑定的新定义，核 NumPy 与 splu 对象相同，再共享原 STATS，
最后才更换 `_bvp.solve_newton`。
原模块导出的 `solve_newton` 和 `install` 始终保持原对象，不被冒名改写。

### 2.2 计数字典必须共享

原 coupled main 通过 `from f6curve_domain_newton import install,STATS`
先取到原字典，最后把它复制到 CP 的 `newton_domain_audit`。
新函数若留用自己的同名初始字典，真实 CP 就会保存过时计数。
选择器明确在指针更换之前作

```python
derived.STATS = original.STATS
```

本审确认该语句唯一、顺序正确，且没有清零原字典。
作者隔离纯协议还使事先保存的导入引用观察到同一字典的7→8计数变化；
本审独立逐字重放该协议。

`Selection.check()` 同时要求原字典仍是保存对象、derived 模块及新函数 globals
继续使用这个对象，并核原 NumPy/splu 仍为相同对象。
因此“数值算法只改一行”与“原记录的运行计数仍真实”两个要求都显式覆盖了。

### 2.3 新身份与恢复

`Selection.check()` 返回新函数的路径、源码 SHA、行号、签名和 runtime module，
标明 `changed_runtime_identity=True`；它没有谎称新函数还是旧函数。
选择后检查失败时，仅当仍拥有所设置的新指针才恢复原指针；
显式 `restore()` 先核当前身份，避免覆盖未知第三方改动。
二次 restore 或再次运行原 install 使身份失效时，都不能静默继续宣称新选择有效。

旧 true-M14 的 `runtime_newton` 要求原函数对象，所以它必须拒绝此新身份。
完整集成须另建入口并记录每个实际 BVP 前后新身份、原物理回调和原 STATS；
不得删除旧门或直接把新实现写到原冻结文件中。
本次通过不等于已审过尚在实施的完整新接线，更不等于已实际安装成功。

## 3. 两条独立纯验证

### 3.1 本审自写的九场景检查

本审新增 `db6f-tail-review-newton-release-lu-lifetime.py`。
它不用项目 import、NumPy 或 SciPy，只把真实 AST 中的 refresh 条件块
放进另写的协议函数，使用标量 marker、fake Jac/factor/solve 和弱引用。
未调用完整原/新 Newton，也未构造一个 BVP 候选。

实际 **`9f213a / exit0`**，报告
`tail-review-newton-release-lu-lifetime-check.json`，11229 bytes，SHA256
`53ca99e44b658a0758aa871a787e931fa1ef8ad350b57ff7bcfc304fe95a42a7`。
九个场景是首次 refresh、后续 refresh、最后一次允许 refresh、旧因子复用、
预算耗尽、Jac/LU 各自 RuntimeError、Jac/LU 各自 MemoryError。
所有场景的数值 callback trace 与返回/异常均相同；
后续 refresh 的新版在假 Jac 和假 LU 入口已无旧对象强引用，旧版则仍保留。
复用和预算耗尽仍保留旧因子。

### 3.2 作者十场景的独立原样重放及真实负门

全文读过作者检查程序后，在独立新路径重放。
实际 **`c4c2dd / exit0`**，14261 bytes 的报告与作者原报告逐字同，SHA256
`1cfe353071f1c823e507285e81e41559d84094f8af2a03aa2afe0d2f6715c40e`。
它补核 factor.solve 的 RuntimeError/FloatingPointError 原传播边界、
原 STATS 别名，以及新文件不能冒充原源码的负门。

随后单独新进程执行选择器的正常 `--check-current-gate` 分支。
实际 **`662898 / exit2`**；报告 SHA256
`303d36428b070382fb5a386b5ba3fe5f2f33af5f6d0ad1534317308029b7db09`，
其 `NOT_SELECTED/ready=false` 原因是原 domain Newton 尚未安装，
且原运行指针前后相同、零安装、零 solver。
这是真实只读 CLI 负门，不是人工伪造的 ready 响应；也不支付未来正安装或数学成功门。

## 4. 资源失败的可推断范围

作者绑定的已闭 attempt01 三件来源经过重哈希；root 实际观察 receipt
`55ec10/tool exit2` 与 guard child2 一致。
唯一 weighted BVP 的记录为 `MemoryError((21703500,), dtype('float64'))`，
后续缺少成功 CP 导致的 FileNotFoundError 是次级关闭错误。
没有新 CP、coefficients 或 final seam。
本审只使用这份已经关闭的记录，未读取 attempt02 活动输出。

从实际 SciPy `compute_jac_indices` 与 `construct_global_jac` 的结构块大小，
逐项得到

$$
E_m=2(m-1)n^2+(m-1)nk+2n(n+k)+(n+k)k
=(2n+k)(nm+k).
$$

对 n43/k14，是 $100(43m+14)$。独立精确整数检查给：

| 节点 m | 结构条目 | 单个 float64 values 数组字节 |
|---:|---:|---:|
| 5047 | 21703500 | 173628000 |
| 6500 | 27951400 | 223611200 |

所以该失败 shape 与 m5047 的完整 values 数组大小对应。
这仍是按原结构作的形状推断，不是保存了这张网格、实际 traceback 中的 refresh 序号，
也不是测得完整峰值。源码在第二个 hstack 右侧仍持有前一个 values 及各块，
随后还有 sparse 格式、ODE Jacobian、LU fill 和其它分配。
不能用这一个数组字节数估算完整资源需求。

SciPy 的自适应循环对每张新网格另调用一次 solve_newton；
原 Newton 返回值不含 factor。因此新网格的第一次 factorization 本来没有该函数内的旧 LU。
现存 shape 记录不能确定恰在有旧 LU 的 refresh 失败，
所以不能断言本单行必然修复那次 3GiB 失败。

另独立逐字核原资源 wrapper：4GiB 版相对3GiB版只有 CAP 常数变化，
两者都保留更严格的继承上限和原空间 guard；这与解除 LU 引用是不同操作。
本审读取 `/sys/fs/cgroup/memory.max` 实际为8589934592字节，
仅作为本次操作环境的观察。每进程 DATA 与 aggregate cgroup/RSS、Node old-space
并不是同一种预算，不由这些数字推出任何未来运行必然容纳或必然冲突。

## 5. 封存与剩余门

独立闭包检查 `db6f-tail-review-newton-release-lu-closure.py`
实际 **`ed576a / exit0`**，报告8659 bytes，SHA256
`d57bd729e7157a87f6f54d2bf4d734b4a684c4d5736abad2b31b016a40805090`。
它重核作者7件/52348 bytes、13来源、独立逐字协议重放、九场景自写检查、
正常负门、STATS选择顺序、精确整数条目数及3→4GiB wrapper差分。

定稿前一次 `abd7cf/exit1` 只因本审闭包检查错误地把函数 docstring
视为第一条可执行语句；修正为跳过 AST docstring 后上述正常检查通过。
当次没有写成功报告，未改作者任何封存源码或方法稿。

本批可供新的 true-M14 入口显式引用；真正接线仍须独立来源/运行身份/负门审查，
实际正运行及所有原方程成功条件须由 root 另行取得。
没有因该实现检查产生新数值候选或完整闭面，也没有支付 G5 或最终独立全流程。
