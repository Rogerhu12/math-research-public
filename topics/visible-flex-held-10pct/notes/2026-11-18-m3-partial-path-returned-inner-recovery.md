# m3：λ=.02 真返回内层的原状态恢复接口

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 当前对象与结论

实际运行 94553 的首个 inner 已原式返回成功：493 节点、25 个状态分量、5 次自适应迭代，保存的最大 RMS 为 `9.873637694422844e-7`。随后唯一新高度请求的真实尾在 iteration 2、残差 `3.667862901158431e-9` 处线搜索失败。这个状态没有完整 physical checkpoint、均值积分、full metric 或新的尾接受；本条不重新计算这些已发生的数值事实。

新的 `m3_trace_path_raw_inner.py` 已实际读取并绑定这次原 returned-state、sidecar、失败尾和 103 个原定义/执行源，保留原节点、状态、完整八参数、原 cubic 与完整 RMS 向量。绑定执行成功，未重跑 inner 或任何模型方程。独立 `native_model()` 提供后续恢复对象的方法，尚未在本次绑定中调用；原联立控制流续接仍必须先得到同新 H 的真正尾接受。

## 精确保存的材料

原文件位于 `m3_work/q060-circle-trace-path-coupled-lam002-v1`：

| 文件 | SHA256 |
|---|---|
| `inner-00-returned.json.gz` | `bc2fee7117ba8d8d842ac3352290ce55e966813ebf8048494688ce6d46180cc0` |
| `inner-00-returned-dn-anchor.json` | `fcbe787e4e730c09fc54c8f971371edb5159a99cb22d480852714afa38ce642a` |
| `seed_tail_0001.json.gz` | `6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac` |
| `launch-plan.json` | `99b888b421ecaea72dbbafffca9811121ed8d663c62049c3ce03e54edc6b52be` |

reader 核对原 `x[0]=0,x[-1]=1`、严格递增 mesh、`25×493` 节点状态、`4×492×25` cubic 系数、8 个参数和 492 项 RMS。每个数组都用完整 binary64 字节哈希绑定；没有把 cubic 节点评价值替换成原 `sol.y`，也没有重建、删减或伪造 RMS 向量。

原原始解对象的 `message/status/niter/success` 都已保存，恢复时直接复制。`sol.yp` 没有保存在这份 returned raw 中，不把从 cubic 推导的数值称为原 `yp`。待续的原 post-tail 控制流不读取该字段。

## 部分 lift 与轮廓身份

恢复目标明确是 `exact_m3_finite_circle_trace_path_partial_lift`、路径 `finite-cosine-trace-synchronous-lift-v1`，λ 为字面 `.02`，径向窗为 `.5,.9`，数值 gauge/warp 为 `.06`，独立支撑种子为 `.059818741459951905`。完整七个物理控制仍为原 `p[1:]*pscale`，不调用旧 `ratio**j` restart。

保留原 `path_base_profile.delta=.06104275721220832` 和实际 `p0=-1.3637752370752413e-10`。因此当前候选物理轮廓 δ 是 `.0610427570758308`。没有把最终 δ 再当基底添加同一位移，也没有静默把 `p0` 归零。原 normalized chart、source、port、settings、qseed/gauge 和完整参数共同限定待恢复对象。

`native_model()` 先恢复真正原余弦参照的类，再构造这一固定 λ 的独立 `CircleTracePathEnvironment`；实际 `initial(p)` 仅用于创建同一个全控制核和附着其部分 lift。随后将保存的完整 x/y/p 和 cubic 装入对象，不调用 BVP、尾、均值、physical quintic 或完整审计。原 cubic 的系数和 knot 不变；返回的求值域限制在保存的 `[0,1]`，不提供域外外推。

`m3_trace_path_prefix.py` 是这个 raw reader 的已冻结源/计划检查依赖。它还包含未来 physical-quintic 的显式读取入口，但本次没有使用或验证那个入口，也没有凭空生成 physical checkpoint。

## 旧锚与新请求分开

sidecar 指向旧 H 的真实完整 actual response `ae01f13a…`，响应 payload SHA 为 `6e6b38f18dc84c7dbe4099532977866c8662b29b993e32c72ef368fe190247bb`。这只证明本次 inner 的仿射 DN 来源。

保存的旧 H 的 binary64 SHA 为 `36f201a193e1fd50b764af622d81d0b359e1a1a29e0f2608c2ebb73b06e6b2df`。新候选 H 的 SHA 为 `d594be33b2087c297971a7445db52e78b771f0b4f77682c3ab5ec7b1cac70890`。reader 用原 `sigma*q_gauge*y_end` 核其全部 8 项，并核失败尾的完整 request/config/source。它不把这两个 H 或两个响应互换。

恢复对象故意不设置 `obj.tail`。待同新 H 的真实原 worker/Jac/audit 通过以后，必须安装真实尾、执行原 BC 检查并形成 outer row 0；若该行尚未通过，才进入原 outer 1–7。原总 outer 预算保持 0–7，不再次运行已接受的 inner 0。旧锚或失败的新响应均不能在恢复时自动冒充 actual tail。

## 实际绑定与范围

新源位于 `scripts/resume_closed/m3_trace_path_raw_inner.py`，实际紧凑记录为同目录 `m3_trace_path_raw_inner_binding.json`。运行命令为：

```bash
python math-research-public/topics/visible-flex-held-10pct/scripts/resume_closed/m3_trace_path_raw_inner.py \
  --raw /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-path-coupled-lam002-v1/inner-00-returned.json.gz \
  --sidecar /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-path-coupled-lam002-v1/inner-00-returned-dn-anchor.json \
  --failed-tail /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-path-coupled-lam002-v1/seed_tail_0001.json.gz \
  --out /workspace/scratch/7322d0dee069/closed_work/m3-trace-path-raw-inner-v1/binding.json
```

此命令实际 exit 0（chunk `271e2b`），输出 SHA256 `6fdb3730f9aa1ede05e4a9a93a4ad4a518de0198d75bdd3d5ddf7e3a6b1c4549`。完整大数组仍只在原 scratch 记录中；Git 只保留可再生 reader、来源、参数和紧凑哈希。

本轮完成的是新真实返回态的可核对保存与恢复接口。没有新的 inner 求解、尾接受、均值/metric 数值或连续几何结论。
