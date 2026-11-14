# 原 Newton 重组前释放旧 LU：单行生命周期修订

状态：**源码等价性证明与纯协议验证；尚未安装或运行此 Newton。**
作者：`db6f / coupled_prefix`，2026-11-09。本文不修改已绑定的原
Newton、谱权模块、true-M14 入口或任何活动运行；G5 仍未支付。

## 1. 确切改动

冻结原件为
`repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py`，
SHA256 `6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654`。
独立新定义 `scripts/db6f-prefix-domain-newton-release-lu.py` 的
`solve_newton` 函数相对原函数只增加一行：

```python
        if refresh:
            if factors>=8:break
            factor=None
            try:factor=splu(jac(y,p,ym,ff,fm,br))
            except RuntimeError:return y,p,True
```

删除新增的 `factor=None` 后，**整个函数源码逐字相同**，不是仅公式
相似；AST 也只多这一赋值。新文件没有 `install()`，导入它不会安装
Newton，也没有候选求解。新函数 SHA、原/新函数来源及实际纯检查
分别保存在本批 `-sources.json`、`-protocol.json` 和
`-observed-validation.json`。

Python 原赋值的右侧先求值：在 `jac(...)` 和 `splu(...)` 完成之前，
旧局部变量 `factor` 仍持有上一 LU。新赋值先解除这一局部强引用，
随后才用完全相同的参数求原 Jacobian 和原 `splu`。本改动没有变更
稀疏排序、pivot 参数、精度、步长、保护阈值、线搜索或配点方程。

## 2. 为什么这里不再需要旧因子

下面覆盖原函数全部相关控制流。`refresh` 是源码中的实际变量，
不是假定存在的 `recompute_jac` 选项。

| 入口或结果 | 原控制流 | 新版处理及理由 |
|---|---|---|
| 本轮原 residual/BC 已达内部停止条件 | 在进入 refresh 分支前 `break` | 新行不会执行 |
| `refresh=False` | 用先前已算的 `step,cost` 和同一 LU 做各试步 | 不执行释放，完整保留复用 |
| `refresh=True,factors>=8` | 先 `break` | 仍先 `break`，没有释放或额外 Jacobian |
| 第一次 refresh | 尚没有旧局部 `factor` | 赋值 `None` 合法，不声称节省 LU |
| 后续 refresh，构造新 Jacobian/LU 成功 | 用新 LU 计算新 `step,cost`，再线搜索 | 旧 LU 在这个路径不再被读取；新数值调用次序和参数相同 |
| `jac` 或 `splu` 抛出 `RuntimeError` | 立即 `return y,p,True` | 同一返回，不存在使用旧 LU 的回退分支 |
| 上两项抛出 `MemoryError` 等其他异常 | 异常传播 | 同样传播，不回退使用旧 LU |
| 新 `factor.solve(residual)` 抛出异常 | 它在原 `try` 之外，异常传播 | 原异常边界保持 |
| 线搜索的 `FloatingPointError` | 使用已构造的新 LU，拒绝本试步后继续 | 线搜索正文逐字未动 |
| 全步被接受 | `refresh=False` | 下一轮仍保留并使用该新 LU |
| 阻尼步被接受 | `refresh=True` | 下一轮进入上述替换分支 |
| 21 档均未接受 | 原 `no_step` 计数后 `break` | 没有额外分解或新返回规则 |

因此，在相同输入、同一原回调与数值后端下，凡两个版本的相应
数值操作均正常完成，它们执行相同的数值运算与接受判断，给出
同一数学算法。这个结论不把内存分配是否成功当作数学前提被满足：
改动的目的正是改变重叠对象的生命周期；资源异常可以因之不同。
这里也不许诺跨平台逐位确定性或新的数值收敛结果。

原局部 `factor` 没有作为返回值或全局值保存。这里的证明针对绑定
源码的原回调和 SuperLU 调用，不把任意恶意栈反射/自定义析构器也
当作数值等价模型。删除一个 Python 引用与底层分配器立即归还 RSS
是不同命题；本批只证明前者和程序控制流。

## 3. 原 STATS 与诚实的运行身份

原 `db6f-prefix-coupled.py` 在 `main()` 中执行
`from f6curve_domain_newton import install,STATS`，最后把该字典写入
`newton_domain_audit`。若新函数只用自己新建的同名字典，原 CP 将
记录错误的旧计数。因此新增的独立选择器
`scripts/db6f-prefix-select-domain-newton-release-lu.py` 必须在将来
显式选择时执行：

```python
derived.STATS = original.STATS
```

它不清零原字典，也不改原模块的 `solve_newton` 或 `install`。
选择器先核原源码、新源码、SciPy `_bvp.py` 的冻结 SHA，核原函数
源码/签名和当前 `_bvp.solve_newton is original.solve_newton`。
只在这些检查通过后加载新定义，共享原 NumPy、`splu` 和 STATS，
显式更换 `_bvp.solve_newton`。返回的 `Selection.check()` 给出
**不同的**新函数来源，并检查原函数未被改写、计数字典仍是同一对象。
选择失败会在仍拥有该新指针时恢复原指针；显式 `restore()` 同样先
检查当前身份，不能覆盖别人改变的函数。

本批没有调用 `select_newton()`，也没有调用任何原或新 `install()`。
当前已审 true-M14 v1 的运行门要求原函数身份，故**不能把这批新函数
直接塞入 v1 而继续声称通过其原身份门**。完整实际接线需要全新
selector/preparer/auditor 身份，新增来源绑定、记录每个 BVP 前后的
新函数身份，并保留原物理回调、真实 DN/J、8 轮 outer、原 BC、最终
seam 的全部门。这一接线另行实施/独审；本批不生成运行 launch。

## 4. 实际纯验证与范围

`scripts/db6f-prefix-check-domain-newton-release-lu.py` 读取两函数 AST，
核整函数单行差分，再只抽取实际 `if refresh` 条件块放入一个隔离
协议函数。输入是字符串、假 Jacobian、假因子和极小标量对象；
没有调用 `solve_newton`、`solve_bvp`、真实 `splu`、真实几何、DN 或 RK。

十个实际通过的场景为：首次替换、已有因子替换、全步后的复用、
8 次预算耗尽、Jacobian/LU 各自 `RuntimeError`、Jacobian/LU 各自
`MemoryError`、新因子求解的 `RuntimeError` 与 `FloatingPointError`。
两版每例的返回/异常及数值回调轨迹完全相同。弱引用检查显示：
旧版进入替换 `jac` 时旧因子仍活，新版在该点已解除本协议内的旧
强引用；复用和预算耗尽则两版都保留旧因子。另以隔离原字典模拟
实际 STATS 赋值，确认先前已导入的引用仍观察到同一计数变化。

实际工具回执：

- `25e397 / exit 0`：十类纯协议及源码差分通过，输出 SHA
  `1cfe353071f1c823e507285e81e41559d84094f8af2a03aa2afe0d2f6715c40e`。
- `26c6c3 / exit 0`：选择器的只读定义门通过，未导入/安装求解候选。
- `991163 / exit 2`：独立新进程中 SciPy 自带 Newton 尚未被原
  `install()` 替换，真实 `--check-current-gate` 按预期拒绝；前后
  函数对象未变，零安装、零求解。

这不是用人工正响应支付未来数学门。独立复跑应选择新的报告路径，
输出脚本拒绝覆盖已有文件。

## 5. 对 3 GiB 失败与原 4 GiB 重跑的实际含义

已闭 true-M14 attempt01 的真实 root 观察为 tool exit 2
（`55ec10`）；首 DN/J 成功单独保留。唯一谱权 BVP 的记录是
`MemoryError((21703500,), dtype('float64'))`，没有新 CP。
随后 selector 因缺 CP 出现的 `FileNotFoundError` 是关闭路径上的
次级错误，不是另一份数学结果。三个实际闭文件已绑入本批来源表。

在原 SciPy `construct_global_jac` 中，$n=43,k=14$，$m$ 个节点的
结构条目数为
$$
E_m=2(m-1)n^2+(m-1)nk+2n(n+k)+(n+k)k
   =(2n+k)(nm+k)=100(43m+14).
$$
故 $m=5047$ 时 $E_m=21703500$，一个 float64 values 数组本身需
173628000 字节；$m=6500$ 时 $E_m=27951400$，需 223611200 字节。
这仅是一项已知数组，不是完整峰值：源代码在第二个 `hstack` 右侧
计算时还保留第一个 values 数组及各块，随后另有 COO/CSC、ODE
Jacobian、LU fill、谱权中间量和运行时占用。

`solve_bvp` 的每轮网格调用一次新的 `solve_newton`。原函数返回时
不返回 LU；因此细化网格**第一次** factorization 本来没有这个
函数内的旧 LU。现有失败记录只给出 values 数组长度，没有保存
refresh 序号，不能确定本单行能否降低本次失败点的峰值。即使有
旧 LU，被省去的峰值也取决于实际 fill，不能从原稀疏矩阵条目数
推出其确切字节数。

原入口单纯从 3 GiB 改为 4 GiB DATA 上限，给予额外 1 GiB 的
每进程资源额度；它保留原数值源码和原关闭门。新单行版本可能
减少后续重组中的重叠 LU，而不提高额度。这两种作用不同，可以
分别归因；本批不把它们合并成已经有效的修复。4 GiB 是每进程
DATA 上限，不是 aggregate/RSS 预算。Node 原 old-space 1536 MiB
也不是 Node 总内存。8 GiB cgroup 下没有仅由这些上限推出的必然
冲突，但它们也不能保证同时占用、allocator、共享库与其他任务的
总量能容纳；需要真实资源观察，不能用本证明替代。

当前原 attempt02 的源码与资源 wrapper 完全不动。本批没有读取
其活动 trace 或把其未闭状态作为成功/失败证据。稀疏排序、LU
选项和容差没有作为本次附带“优化”改变。

## 6. 纯复跑命令

在 repo 根目录运行（只读取冻结来源、写一个新小报告）：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-check-domain-newton-release-lu.py \
  --out /absolute/new/unoccupied-lifetime-protocol.json

python topics/visible-flexible-closed-surface/scripts/db6f-prefix-select-domain-newton-release-lu.py \
  --original topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py \
  --check-definitions

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-select-domain-newton-release-lu.py \
  --original topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py \
  --check-current-gate
```

最后一条在独立未安装进程中应 exit 2；它不是运行 solver 的入口。
完整实际接线、新数据、真实退出和未参与者独立重跑都另行支付。
