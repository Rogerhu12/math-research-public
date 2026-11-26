# 同固定 g、只改实际初始 H 的完整根读取：03b 第 34–35 步

日期：2026-11-26。实际 run `45820592817/1`，第 34 步采用已明确指定的 Jstar 工作字作为 H 初值，实际进入完整端点根求解并失败；第 35 步纯 reader 正常返回。没有新场、metric 方向或连续证书。此处不把不同失败迭代点的残差相减称为度量改进。

证据：[公开 part-008](2026-11-26-public-actions-45820592817-1-part-008.md) 第 34、35 条，读取时 Git blob `108de9647d5c9389825b712e7cbb2e7217cc6025`。完整科学 argv、七个来源 manifest 和输出身份均在该公开记录；本文不是删减后的重建入口。

## 1. 实际输入只改变初始 H

完整 launcher / driver / endpoint / base 的 SHA256 分别为：

- `c1d3e0e5da47d3edef42124a8020cba705e99ac4b522c758ee195e8d575a58bd`；
- `34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3`；
- `44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e`；
- `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf`。

实际科学源提交 `9f7b75456f88758d16385df6878f5519dbc1fe90`。reference 为 `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1`，carrier 为 `b0257d9e03da36a422eab4e424942d38ccf817ac40ceb3b42be4378b1260966f`，固定 g 为 `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb`，固定 18 字 Q definition 为 `05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e`。Q 未在当前自由点重算。

旧 H 字 `0x1.f27228dabd944p+0` 改为完整请求值 `0x1.ec0bc59b655d2p+0`；后者准确二进制有理数为 4328082246413033/2251799813685248。实际报告确认 nonheight_identical=true、height_target_changed=false、model_changed=false：

| 项目 | 实际身份 |
|---|---|
| 改 H 前完整自由点 | `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3` |
| 改 H 后完整自由点 | `efe12015c07babb2ebe02ca2f9689faa2433e37485249610ee7126a07ba8bd93` |
| 固定 moment-Q 模型 | `d03587cb5195b02157222edf13e32c8e84c2681672362fefefc6dbbf45442707` |
| source_mode | `explicit-height-new-reference-seed` |

这次实际采用 H 新字，不是仅在说明中建议；它仍是一个自由初值，未称准确连续 Jstar 积分。所有 1,333,370 个自由量与 45,324,288 个完整 metric 行保留。首读取使用原宽支持、.75 控制球、tolerance=2e−12、Newton 24、backtrack 18、Armijo=1e−4；没有借用旧球的 IFT 证书。

## 2. 初根真实失败

第 34 步 16.05577080600051 s，exit 1。报告 `zero-closure-frozen-moment-Q-Jstar-height-first/report.json`，119,922 bytes，SHA256 `75b868c7b8bd7b3f79950f26700a2ef7190c61195530f7043a34831e216dc1a8`。

实际 reason 为 `No actual endpoint-root backtrack decreased the same complete equation`。失败角索引 [0,1,2]，最大实际端点残差 .013491828979874587，最大实际控制修正范数 .4539401339485306。现有记录给出 280 次 root line-search evaluations、1 次失败，成功 root 角数为 0。原计数字段 root_iterations=0 并不表示未尝试根求解；它没有为本次失败中的每个局部 Newton 更新承诺完整计数，不能据此否认实际 280 次回溯。

初始曲率/半径历史各 1851 个地址。失败发生在初场读取阶段，尚无完整初始/末 metric、几何、bundle 或 μ 返回。0 个 metric/restoration 方向，0 个接受方向，0 个升级 angular jet、0 个完成的 implicit block。当前全网格根不可用，当前残差、控制范数、最小 Cz 奇异值及一二阶隐式 jet 缺陷均 null。

报告停止在 `actual_initial_zero_closure_field_read_failed`；不能把这个失败迭代候选当可接受场，也不能把不同旧运行停止点的残差差称为同一函数的改进。

## 3. 纯读取与缺项范围

第 35 步用完整 reader `2e5b340d622993af55060f22d1dc26bd1cc451218feb27f8b8ce7b1366de1fe9`，源提交 `190217fc6cc756302cc79b4a5b6db88eaf28a01e`，6.053762018997077 s，completed/0。纯 readout 50,978 bytes，SHA256 `6769d2c53319b9e5420b69f024171e8c28074cce1d89d69f1a93e94fe5f11bda`。它保持 complete=false/initial_failed=true，不重新求根。

第 34 条的 16 个 summary_errors 只指未产生的 initial/final metric、final geometry/bundle、方向和末位置字段；第 35 条的 9 个 summary_errors 只指 null 的末几何/位置。它们不能补零，也不等于纯 reader 异常。实际新 H 只完成了失败初根读取，不存在后续有限几何通过或连续完成结论。

本轮结果否定的是这一具体初值和已声明数值根策略的成功，未证明整个控制族、.75 球、同固定 g 或本课题无解。后继必须继续保全本次真实完整报告的地址责任，且不继承任何未产生的场或证书。
