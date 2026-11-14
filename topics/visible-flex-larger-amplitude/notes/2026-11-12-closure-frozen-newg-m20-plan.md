# 完整实际 M20 向量的新 g 深12作业：冻结校准准备

2026-11-12，exact_closure。**仅完成静态准备，未启动 Node 作业。**

## 输入、度量和保持的量

输入使用已经正式成功的
`2026-11-12-root-vu032-q085-fixed-actual-m20-frozen-recovered-audit-response_0001.json.gz`，
SHA256 `b667b7b24fd60756c341132fd14d9fe2a15857a96eb4d6598186f86741e4d091`。
其完整20个高度原样进入新请求，首项
$H_2=-2.1668387574702766\cdot10^{-5}$；未裁高项、未倍乘、未平滑。

新配置保留 modes20、quadrature512、steps12、shootingParts8、
linearSteps2048、全部原物理参数与非线性容差，只将实际非线性
depth8延长到depth12、linearFar48延长至225。真实warm重接后还须
重新求解，不能把新增144个stage的线性初猜称为非线性解。

n≥160 使用 R15 原有的明确有理65/64定义，所以这是相对旧stored
尾的**新固定度量**；旧响应只是初猜。本次新适配没有再次改这个
已经命名的新g，也没有改0..159的浅头或保存的 global warp alpha。
R26真实实积分端口与floating stored端口的区别继续保留。

## 仅改变工厂构造的独立适配

`strong_frozen_rational_model.mjs` 在内存中读取原
`closure_rational_tail_model.mjs`，只替换唯一工厂构造调用，复用
`strong_frozen_calibration_factory.mjs` 已守卫的160个binary alpha。
深源函数源码和所有原文件不动。新manifest保留原adapter哈希，
另外完整记录新wrapper、变换后源码、工厂、ledger和profile指纹。

原工厂已经通过独立几何调用的5点rational与7点stored历史指纹
逐位相等检查；本新组合还没有实际构造，必须在下一独占窗口由
worker的相同守卫检查，不将静态准备当作新非线性结果。

新独立文件：

- `computations/closure_frozen_endpoint_worker.mjs`，SHA256
  `a91bfaef3eb7c4c11890c88585f5a840c49b37a7808da4ba4ea352d15f59871e`。
- `computations/closure_frozen_metric_endpoint_job.py`，SHA256
  `c7383a1b71af2cbf0dc78ad6691c5a81e60b2747c9f1d1f1b7144823f49fc614`。
- `computations/strong_frozen_rational_model.mjs` 由strong代理编写，
  SHA256 `fb542f2cced2aea09cc9f1a1f157c6a17d290d3a8ea58386f6da0ce2e018a9aa`。

worker保留原同一 scaled engine、全部实际方程、Newton试步和门；
已接受试步仍在下一次完整Jacobian前立即写 recovery-only 记录。
本次请求不输出Jacobian，只求完整响应与audit；这不改变方程或
验收阈值。private point cache取8，只改变缓存存储。

## 已完成的静态准备与下一执行命令

`closure_frozen_metric_endpoint_job.py prepare` 已正式 exit0。
完整不可变计划与配置保存为
`2026-11-12-closure-newg-strong-m20-frozen-d12-f225-plan.json`、
`...-config.json`。计划含全部20H、所有输入/源码SHA和新旧分辨率。
额外七点stored参考是
`2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json`。

等root交付独占大Node窗口后，使用：

```bash
/workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-resource.json -- \
  /workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/closure_frozen_metric_endpoint_job.py run \
  --plan notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-plan.json \
  --node-heap 192
```

192 MiB是这次明确的V8 heap上限，另有native内存；不是已证明的
最低live heap，也不是对先前signal9原因的诊断。wrapper记录真实
退出码及wait4资源。若已有输出，runner拒绝覆盖，需明确使用
新prefix恢复。当前strong占大窗口，本说明不授权并行抢槽。
