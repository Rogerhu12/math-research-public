# SC 第二次实际运行：首行 Laurent 构造失败与完整保存范围

**状态：第二次公开运行失败；六个实际输入门全部通过，首个新行模型尚未完成。** 本篇保留真实返回码、完整错误和原结果身份。它不授予 signed affine 数值上界，不把首行已开始的运算写成“零新数学”，也不撤销原已成功的 Gram、RW、Green、CPA 或 SC 解析合同。

## 1. 唯一第二次运行与三个已发布原件

部署提交为 `9ffcbb70830ff3ff50869239263dc92991bc34f3`，唯一自动 push 运行是 [43753164994/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43753164994)，job 为 `132931387695`。worker 于 2026-11-15 19:34:47.656356 UTC 启动，科学阶段于 19:35:37.457968 UTC 结束；科学子进程实际运行约 12.309 秒，返回码为 1，job 最终为 failure。没有另行 dispatch。

以下三个小原件均已完整读取并逐字核对 SHA256：

| 原文件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| [完整科学失败收据](../notes/signed_cap_affine_functional_ci/run-43753164994-1/actual-scientific-conclusion.json) | `ea7c15ab8df6f7e9636f1426fe6609b8e2af11da` | 9116 | `635bf74b4a794463fb44f833dd0ba45c887848a5bb0755c2b7f306f356788d5d` |
| [完整执行记录](../notes/signed_cap_affine_functional_ci/run-43753164994-1/execution.json) | `d802338d81066a6d3b5f12e3fd30ebeda7c3a0a7` | 37061 | `5fe9d943823a9d5be781995710a503573de3a51232c652640928b6019ca959bc` |
| [实际 worker 报告](../notes/signed_cap_affine_functional_ci/run-43753164994-1/actual-result.md) | `58bd1ede709c500485d3eeb208f4b5117531cf29` | 5572 | `5986b451a97a3824a36e9cde84636e0b0f8cda37b5567453e21cafd61a379a5b` |

本次 source 为 `43baddb1f30964d38d24602ae9f9c2cb8591c1c6` / 44167 B / SHA256 `bd148b48a019b705cd140212e7134f91f3a71e4418544ad7b9c1da237a0bfe62`；helper 为 `66c9bf47d7391109c928141c9aab607c91dc4076` / 17308 B / SHA256 `8103ca4a856a92fd98923ed518e9241c2bc8332f087550017e58ba7933d2c0d0`。

reader 为 `91441d2be8a8066130eb5f8a4eb59df46964300b` / 14299 B / SHA256 `a7c099608ec6ef1504a1d30b9cabbe9232bdd1dfd0390e28bbfd9fc836772ad0`；worker 为 `eb2b1c99c31ffe339cdb7eeb6333684cee884229` / 59315 B / SHA256 `414e55cb40c516ad02cbba8ae45ac4772f18545dbbfaab8adae5f2ef2abcf6ce`；manifest 为 `750d1b448ca0c04eb76610e3bc4bfb490f2723c6` / 38760 B / SHA256 `5113a116c23455ed272460e5a7eca5117dc86433c44869d96a5e258cc0fcde44`。

实际环境是 Python 3.12.14、python-flint 0.9.0、numpy 2.3.5、256 bits；完整八文件 AST 检查通过。源码和依赖身份均以该次执行记录为准。

## 2. 六个实际门和旧证书身份

预定完整流程有 20 门，本次到达 6 门、6 门全部通过；其余 14 门未执行，不计作通过或数值反例。已通过内容为：

1. 新源码、实际运行环境与完整 SC 参数身份相符。
2. 已发表 SA7a、SC18a 与全部原小证书身份相符。
3. 原 7908 个闭区间和完整 32 组 slice plan 覆盖相符。
4. 四个原省略 pilot 保留原 midpoint jets。
5. 五个原 candidate shards 与完整 canonical centre 相符。
6. 原完整 formal field、endpoint 和 value 证书指向同一对象。

第 6 门使用已审查的旧 finish schema，科学收据中五个 `legacy_complete_body_identity_checks` 均为 true：旧 literal finish schema、完整共同 plan 绑定、原成功 finish process、完整 native 绑定、唯一原 summary 收据。它没有绕过旧对象、plan、native 或 SHA 检验。[第一次 schema 失败及其原证据](R133-supplement-actual-signed-cap-input-schema-failure-and-preserved-evidence.md) 保持原样。

执行记录确认恢复了 36 个原 artifact，原 archive 总字节为 912764217，且完整记录 32 个实际验证过的 Git 输入。原 QR、target、残差范数、Gram、Green、Wiener 积分均重算 0 次；恢复只读取原不可变输入。

## 3. 首行实际停止位置

输入门通过后，程序进入 `body_run` 的第 0 组、第一个原 scalar row。它在构造该行的 `centered_fields` 时停止，尚未调用该行的完整 `complete_moment_models`，也尚未执行该行的 signed Hermite contraction。

完整调用链为：

`body_run → ExactCandidate.row_fields → centered_fields → radial_mul → Laurent()`。

原 helper 的构造器是：

```python
def __init__(self, coefficients=(), lo=0):
    self.lo = int(lo)
    self.p = coefficients if isinstance(coefficients, acb_poly) else acb_poly(coefficients)
```

`radial_mul` 给 Python `sum` 传入零初值 `Laurent()`。在这次真实 python-flint 0.9.0 环境中，默认空 tuple 被传给 `acb_poly` 后进入 scalar 转换，产生：

```text
TypeError: cannot create acb from type <class 'tuple'>
```

这条完整 traceback 已在三个原件中保留。失败属于新 helper 的序列表示与实际绑定接口不相容，不是一个新的范数不等式失败，也不是原数据身份或原 Gram 计算失败。

## 4. 已保存和未形成的范围

已保存的是完整失败科学收据、参数、helper/reader/runtime/source 身份、全部六门、五项 legacy 检查、完整 traceback、原恢复清单、真实 return code 和出版前记录。

未形成的范围准确为：

- 完成的新 scalar row：0。
- 完成的新 signed functional group：0。
- 完整累计 scientific prefix：0。
- 完整 known parameter model：0。
- 最终 affine error、选定 prior、low-trace gate：均未得到。

首行的原对象读取、部分 jet 和中间算术已经开始；这些未完成的临时中间量没有科学 checkpoint，工作结束后没有保存。不能把它写为“零新数学”，也不能把未完成量当作可复用结果。程序当时打开的组 audit 尚未写入一条完整行，尚无已完成新组需要恢复。后续运行若经审查部署，只能补做这部分未完成的新目标，不能重算任何原已成功数学。

## 5. 出版前保存与无损身份

科学收据在任何大小门和 Git publication 之前已打印，原 `SC_COMPLETE_SCIENTIFIC_RESULT` 内容与已发布 9116 B 科学文件逐字相同。原子累计 prefix 和 known model 的 marker 均未出现，这与第 3 节停止位置一致。

出版前小记录为：

| 已打印对象 | bytes | SHA256 |
|---|---:|---|
| 完整 science 与当时 report payload | 15047 | `2e549cfe36dc59d6662bd7f16429e11e18be94ece020ccd84a3f16373902087e` |
| 当时完整 execution payload | 34458 | `16eaea435527885f43f0d5601ea34066d7e13405ab4482a805c477d8c2c685be` |
| 新子进程 stdout | 11866 | `76bd6c93a995d568954a8b1512f9d62434bb9698c50dab2dd068b6231a7c4684` |

`SC_PREPUBLICATION_STATUS` 明写 child 1、complete false、6/6、science 9116 B 和 `packaging_failure=null`。因此这次没有丢失已形成的完整科学收据；最终 report 增加真实后续 README pull，不能要求它与更早 report payload 全文相同。

此前已取得的完整解码 job log 是 104306 B / SHA256 `ec75cba7565f9b371be682f35a8fbf8e85437025536749067228335f20e5d969`。本篇的可复核入口是表中三个小原件及这些小 payload；不要求再读取该超过 100 KB 的大日志。新 array artifact 和 Release 均为 0。

## 6. 最小后续修复及数学 scope

允许审查的最小改动是：保持已有 `acb_poly` 对象原样传递，将有限系数 sequence 转成 list 后再调用 `acb_poly`，使默认空序列明确表示零多项式。所有 Laurent 支持、完整 Fourier 乘积、普通径向导数、均值、指数尾、Hermite 积分和误差预算保持原定义。新绑定行为仍须由公开 CI 实测，静态审查不称它已经运行成功。

[SC 解析合同](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md) 与 [SA 完整物理 affine 接收式](R133-supplement-signed-physical-cap-affine-and-complete-adjoint-receivers.md) 的条件范围不因本次失败改变。未知 $y$ 仍是 actual cap 减 repaired centre；完整两均值、physical gamma 准入、whole-core 非线性域、low/high cut、腰源、height 和 frame 条件均继续独立。本次记录不提供新的 signed cancellation 数值、core 自映射、全局闭合或曲面存在性结论。
