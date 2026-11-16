# R815：696 个实际 CRT 素数断点与同核心续接

日期：2026-11-16。状态：**原 Mg 与 Γ 尚未完成；只登记真实已结束输出及继续同一任务的参数。**

## 1. 原公开任务实际结束

[run 43777837244](https://github.com/Rogerhu12/math-research-public/actions/runs/43777837244)，job `133008081839`，source `7cddfd0d5896f0d1ea7d49143dd1a91a68eb11d7`。原任务从582个素数继续；run receipt在 `2026-11-16T05:07:03.993245+00:00` 记录退出码124、complete=false和预算到达说明。**本轮没有 core receipt，也没有完整算子证书**，因此不将其写成一个实际 core BudgetStop，或由缺回执推断数学失败/算子完成。

真实最新完整步骤是 g/component0 的第696个素数，最后素数1000014397，模数20809 bits，295936个系数；最新小步骤回执逐项引用了当前完整CRT文件。原日志最后一条对应时间17843.817140411秒，与第696步骤一致。Γ尚未因此得到结果。

| 原对象 | 字节数 | SHA256 |
|---|---:|---|
| artifact 14198893567 | 4288349536 | c403e2702da6dd2402184f9f1781e5d6b55b8cdf23c178f0ff8e9156555a16b7 |
| full-outputs-manifest.json（5665项） | 1458846 | 8c03d9bc9e485a71494f5e73c9ea73bb05e492e579d4f5602c4a7a81ae959e55 |
| R815-target-g-component-00-CRT-current.json.gz | 919902566 | 506e675aef98da98f1d2cccb863fa0d1fa7758aecbc3bdedeff8178e9e86ae08 |
| R815-target-g-component-00-CRT-step-000696-receipt.json.gz | 3907 | 9195c6b23974a0995cb5a98d69b98478c13aa13fa0f91606cba6481165492d6d |
| run-receipt.json | 604 | 6da31af2f7bb515039fe3901fe367c224a1342cfd544a662e80604abb80bf3c3 |

Artifact名为 `serre-global-R815-original-normal-derivation-operators-43777837244-1`，到期 `2026-11-17T05:07:07Z`。前一CRT向量SHA为 `e783e2766badac8885169fbb086f2ef43e93280b67838e8e78efdfad34ca6b04`；第695回执为3892B/`37eb2f38d51b241d07e19c56ceba4acebb804c656b76d1b7e14a3c3f8064d13d`。这些只标识已成链，不以原current代替准确算子证书。

## 2. 此次实际源 IO

核真实run、source和artifact API身份，逐SHA读取完整manifest与四件小原输出：公开输入、run receipt、原日志、第696步骤回执。11次HTTP Range实际传输808536字节；最新回执的完整current规格和manifest逐字段一致。原输入确认相同core、wrapper、framework、targets、proof、模式和旧source。

本次没有下载或重哈希整个4.29GB ZIP、919.90MB current或所有大矩阵；大对象SHA来自完整已核manifest/API digest。下次公开冻结恢复器会对实际恢复源完成流式ZIP/成员核验，按原current续算。本地没有新数学或重建。

## 3. 保持原数学和全部完成阶段

只更新[公开请求](R815-public-original-normal-derivation-operators-request.json)的resume为上述实际新源。以下仍冻结：

- core `80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d`，wrapper `ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454`；
- framework `849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3`；
- targets=[g,Gamma]，300分钟预算、auxiliary_prime_start=1000000007、rowblock16、每8个素数重建；
- `deterministic_integer_points_with_weighted_degree_bound` 模式、原R806/R813的53件输入、原两图定义和完整准确恒等式。

从真实696-current继续下一尚未完成的阶段/素数，不重1–696或既有模块缓存。旧三已知列、49拒、九维固定调度均已经关闭，不重跑；不将缺core receipt补造为新数学结论。新run/job/source只在真实触发后填写HANDOFF。

Mg、Γ、原清极B、RR、η、height及全p一致性仍开放。
