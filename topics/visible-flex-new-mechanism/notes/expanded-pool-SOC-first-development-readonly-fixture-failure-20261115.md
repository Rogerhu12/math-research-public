# 扩池同试点 SOC 首次公开运行：只读数组人工例失败

日期：2026-11-15。本文仅消费已经完成的公开 job 日志，不含重新执行或新科学计算。

## 结论

首轮运行在新增 developer fixture 内停止，**尚未进入完整 checkpoint 恢复、新方向库真实核验或新科学阶段**。错误是人工例向原 FullGridValues 的只读 rows 数组赋值。原 finite() 接口确实将其输出设为不可写，因此这是新测试对缓存变更方式的错误假设；没有证据表明生产 freeze/rebuild/SOC 数学失败。

本轮没有产生 EXPANDED_SOC_DEVELOPMENT 完整报告，不能登记十项新检查通过。已输出的 EXPANDED_SOC_PRIOR_WORK_REUSED 仅确认旧112份依赖匹配、旧12项开发和旧已完成科学不重跑，不能替代本轮新检查。

## 公开身份

| 项目 | 真实记录 |
|---|---|
| Run | 43744268876 |
| Job | 132903998961 |
| Source | 455f6c7e2e70ec5db2564de0db085074821dbf1c |
| Workflow | .github/workflows/visible-expanded-pool-soc.yml |
| Job 结论 | failure |
| 失败阶段 | 新 developer_check()，在 prepare_transfer 之前 |
| 原日志 UTF-8 字节数 | 92,856 |
| 原日志 SHA256 | ec8e5b383b7dd53d2dcc0dfecedbe2ce93e3e1bc1cf8c69f0c9fe5182c7370a8 |

日志来源：[公开 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43744268876/job/132903998961)。日志仅读取既有结果，未上传或提交可重算 payload。

三个新源的本轮绑定：

| 文件 | SHA256 |
|---|---|
| scripts/frame_metric_expanded_pool_soc.py | 4226ff562467cf49a62b71de4b0300bb69bae4abe1df1c04ebb2845171f719bf |
| scripts/frame_metric_expanded_pool_soc_recovery.py | db447f3395b3754a7adc95432fbb288aed2efe7393382bf6c6cbf9bc49ca963e |
| scripts/frame_metric_expanded_pool_soc_development.py | b5b8da5e87bc762d5771f46edbf8628e2a4274ee710043bcedf398db069dd934 |

## 具体失败及调用边界

原 traceback 依次为：

1. audit.main() 调用 development.developer_check()；
2. developer_check() 调用 _real_array_rebind()；
3. _real_array_rebind() 在当时第175行执行对 live rows 的赋值；
4. NumPy 报 ValueError: assignment destination is read-only。

对应代码的目的，是确认此前冻结的 failed-y 视图不会被后续缓存变化污染。原 FullGridValues 构造器使用 frame_entry_body_subspace.finite()，该函数复制数组后执行 out.flags.writeable=False。因此人工例不能原地修改它。

这次异常发生在真实 rebuild_failed_context、完整 factory stub、SOC 数组核、ledger fixture 和 parser fixture 完成之前；整份新检查尚未返回。代码前部即使已形成局部布尔变量，也没有已发逐项结果足以将其当作完整通过回执。

本轮实际调用范围：

- 旧开发套件执行：0。
- 旧 optimizer 执行：0。
- 新研究 checkpoint 恢复：0。
- 新普通几何、方向 JVP、科学 LP：0。
- 新扩池后真实 SOC 触发：0。
- 新真实 initial bank 9/hash 门：未到达。
- 新科学实际有效性或性能结论：无。

这里只根据调用次序和实际异常位置界定范围，不将 workflow 的 failure 推成几何不可行。

## 最小修复

仅修改同一个新 developer fixture：

1. 保存原只读 live rows 对象；
2. 用它的一个可写副本替换该人工 live-cache 属性；
3. 修改副本，检查已冻结 failed-y 的值和只读属性保持；
4. 恢复原只读对象。

该修复不更改 core、outer、原几何、模型、LP/RHS、预算、真实验收、row 学习、controller 或 bank 哈希规则；也不把旧只读约定放宽。

修后 developer 源：

- 文件：scripts/frame_metric_expanded_pool_soc_development.py。
- UTF-8：20,175 B。
- SHA256：1bc4fbee6c7212d1d5e3a67efecab69f8bab92ee7fe37d00294710b3fe653a66。
- 未挂 blob：078446cf189ff88b9789b5055ec855ab609c1e2c。

本文不声称修复后的检查已运行或通过。后续只需继续尚未完成的新开发入口与首次新科学；原已完成的旧科学与旧开发保持不重跑。首轮失败保留于本记录及原 run。

## 规则同步元数据

本轮公开实际 pull 于 18:00:53.242588 UTC 完成，读到 source 455f6c7e2e70ec5db2564de0db085074821dbf1c；根 README 与本题 README 均无差异。

- 根 README blob：21bd547f56590b7f2dd279d0297efb289a9b2783。
- 根 README SHA256：6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9。
- 本题 README blob：d0432faff569c8e9af7ed4809847e12880976c11。
- 本题 README SHA256：e685cff0e67e6851a7911d4e9efbae0e7d326e093927af177f716f059b8c566b。

私有规则实际 pull 于 18:00:57.232954 UTC 完成，元数据记录 head 3e1c3ec396fbba3afecd2c8cd5a938ddfbf7ab26、根 README blob 5ba164843b1f5802184178a82d786264404873a3，规则无差异，本会话 QUEUE 唯一且进行中。本文不保存私有正文。

作者责任：tail_cost 消费原公开日志并撰写本失败说明；root 负责原始证据复核、发布和后续唯一公开派发。未进行本地新人工或科学执行。
