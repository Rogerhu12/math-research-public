# R142 shared-Green parallel source continuation

状态：源码和数学接续合同；没有新的实际积分结论。

本入口仅消费真实未完成的 sequential PS 或本入口自己的完整执行结果。运行中的同一源积分不启动第二份。当前 sequential PS 后继完成或真正失败后，先读取其完整 actual/execution/manifest；如果六个 defect 范数已完整，直接消费它们，不再运行此入口。

## 数学范围

依据 [DP](../results/R142-supplement-disjoint-source-slices-with-one-shared-Green.md)，旧已接受源前缀和不超过三个互不重叠的新源片严格可加。每片保留全部1424个细格的径向输出及全部193个端点观察；原母格划分、系数球、768-bit arithmetic、24阶 moment Taylor 和同格两有符号三角均不变。严格门仍为完整 body 范数小于1。

一次公开作业先物化原 Green 和 A/B/K，然后 fork 不超过三个工作进程。打包矩阵通过进程只读内存共享；每个工作进程有自己的 decoded cache、provider 和当前父区间模板。不得把科学数据写成大文件、artifact 或 Release。

## 入口与状态

- [owner](../scripts/fourfold_codazzi_low_centre_parallel_defect_owner.py)；
- [source-slice arithmetic and fork runner](../scripts/fourfold_codazzi_low_centre_parallel_parent_slices.py)；
- [metadata generator](../scripts/make_low_centre_parallel_defect_manifest.py)。

生成器只处理文本、AST literal metadata 和已有完整JSON。它不导入数值库，不计算新范数。使用下面命令时，三个 PREVIOUS 参数必须换为刚取得的**最新真实未成**输出，不能沿用已经被后续 run 接续的旧76格输入：

```bash
python topics/visible-flex-exact-nearby/scripts/make_low_centre_parallel_defect_manifest.py \
  --repo . \
  --previous-actual PREVIOUS_ACTUAL \
  --previous-execution PREVIOUS_EXECUTION \
  --previous-manifest PREVIOUS_MANIFEST \
  --manifest-out topics/visible-flex-exact-nearby/notes/NEW_PARALLEL_INPUTS.json \
  --workflow-out .github/workflows/NEW_PARALLEL_WORKFLOW.yml
```

owner 区分旧 PS kind 与新 parallel kind。旧 PS 必须是原固定哈希 `f45cf5788ef3be337127d65282eaf1496ef07fc1cdecb354665a86be899dd621` 的完整源码结果，且仍有同一比较模型和原 source-moment 实现；新入口恢复自己的片时还须同一当前 owner/source 实现。旧失败、全源未成、严格门未知和各项未付义务均保留。

每个工作进程只在一个完整母格的三球已正式保存后推进本片 cursor。主进程把片记录纳入自己的正式科学 JSON，完成顺序无需与源区间顺序相同。若停止，`disjoint_source_slices` 逐片记录真实已接受域，下一 run 只做缺少域。已有全三片但尚未最终汇总时，只做标量加和及平方根，不重新物化 Green。

只有完整旧前缀与三片无缝覆盖全部155个母格之后才形成全域六个球。原源积分的两个 mean、root97、outer96 不删除；source4、point、physical receivers、全有限 Schur、真实参数与非线性闭合没有从本步骤自动得到。

## 资源与失败保留

科学总墙时仍为19600秒，外层 worker 20100秒、Actions job 360分钟。并行数学阶段在余量中预留60秒用于子进程停止和最后一次正式 scalar 保存，至多20秒 drain；超时片只保留真实完成的父区间。全部三片共用一个 Actions job，不另外占三个并发作业。父进程现有逐项向外打包 guard 保留，子进程不写入 packed entries。

新实际输出须报告完整片覆盖、六个全域球或明确的未成状态、实际峰值内存和时间。尚未观察到实际加速比，不能将CPU并行度当作已证的速度保证。
