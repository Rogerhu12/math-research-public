# 原模型完整 Phi：绑定实际 coarse 阻尼后顺序续六方向

日期：2026-11-20。会话：Astra-resume-public-20261120 / fullclosed_solver。

**状态：独立 Actions 入口与静态参数核对；未启动新的本地科学计算。** 此入口在新公开 job 已经返回的实际 coarse v7 父上，重新计算 `.992` 完整方向，再从真实接受状态及累积的永久几何位置继续后续方向。旧 job 的父 SHA、阻尼和方向数值都不充作新 job 的结果。

## 入口与准确身份

源：`scripts/resume_20261120/launch_full_phi_original_from_coarse.py`，8046 bytes，SHA256 `2a89e6d3889dc9693e2d2765e15e0a637953d34e0366dd004796d6d079f91652`。

它仅读取实际 coarse v7 JSON，要求其 `output_bundle_sha256` 等于实际输入 bundle 的 SHA256，并取正且有限的 `final_damping`。调用者不能另外传 `--damping`，因此不会把前一个 Actions job 的末阻尼误套到新的重建。此标量仍在 normalized-Phi 单位下；coarse 与冗余完整空间的步范数并不因此相同。

实际科学入口仍为冻结的原 `launch_full_phi_qp_actions.py`，SHA256 `6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63`。该 launcher、原完整 driver、v2 QP 和原不等式选行源字节都未改变。新入口没有 R671 尾模型参数，也不做物理场迁移。它逐字传递全部 manifest 路径，不改位置集合或未知量。

独立 provenance plan 保留实际报告 SHA、父 SHA、实际初始阻尼、完整科学 argv、所有输入/源 SHA 和完整 launcher argv。它不以 JSON 中的旧合格标签替代 driver 的真实初态和回溯检查。公开入口只允许在本仓库 Actions 执行；`--print-command` 只读报告/字节并打印命令，不导入任何科学场模块。

## 零绝对 QP 阈值的含义

原 `fullspace_feasible_active_cg_v2.py` 允许 `atol=0`。源码中该参数仅进入

$$
\tau_g=\mathrm{atol}+\mathrm{rtol}\,\|g_0\|_2.
$$

没有除以 `atol`，也没有要求它严格为正。令 `--qp-atol 0` 只是去除固定的绝对梯度地板；默认相对阈值 `rtol=10^{-6}` 仍在，每方向至多 256 次实际 Hessian 推进也仍在。活动集释放还使用该阈值和相对于当前投影梯度的下降尺度，并没有因为 `atol=0` 被关闭。

这不是提前保证某方向收敛，也不证明旧预算由绝对阈值限制。新 driver 报告应如实登记每方向停止原因、实际推进数、投影梯度、释放事件和非线性试步。若原 `.992` 首方向本来在 256 次预算处停止，零绝对阈值可以不改变其轨迹；不能在运行前断言与旧结果逐字相同。

## 六方向内的状态与阻尼

`--directions 6` 透传为原 driver 的 `--max-directions 6`。第一方向实际使用报告给出的初始阻尼。每次接受后，下一方向使用新场及该过程累积的全部永久几何记忆；每次实际拒步产生的新位置也保留。每方向重新读全原/Gauss 目标和必要几何筛选，不拼接旧数值。

后续阻尼使用未改原算法：仅在接受满步且实际/预测下降比大于 `.75` 时减半；本方向没有接受试步时乘四。接受半步本身不减半。六是本次实际批次长度，并非课题完成标准；初态不能通过必要几何筛选或已达到该数值 metric 目标时，原 driver 会如实提前停止，不编造余下方向。

数值筛选保持 `.992`，活动候选带 `.025`；最终 reach 仍须同场连续上界和 README 真标准支付。全部正常终态都保存在 `outdir/final.npz`，其字段为 `final_bundle/final_bundle_sha256`；这与输入 coarse 报告的 `output_bundle_sha256` 字段不同。

## 完整命令

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_original_from_coarse.py" \
  --coarse-report "$ACTUAL_RETURNED_COARSE_REPORT" \
  --repo "$REPO" --work "$WORK" \
  --bundle "$ACTUAL_RETURNED_COARSE_BUNDLE" \
  --carrier "$SAME_SCALAR_CARRIER" \
  --manifest "$COMPACT_COMPLETE_PERMANENT_POSITIONS" \
  --outdir "$WORK/full-phi-original-six" \
  --directions 6 --qp-atol 0 --maxiter 256 --active-rows 192
```

更多 manifest 可重复 `--manifest`，原顺序保留。此次 adapter 不会自行压缩或删改位置。命令中没有硬编码阻尼或从旧 run 复制的父 SHA。准备时附加 `--print-command`；实际输出目录必须是新的。所有 raw 数据仍留该 Actions job 的 work，公开结论在真实终态返回后另行登记。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
