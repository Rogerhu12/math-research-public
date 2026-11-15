# 选定行 Jacobian 首次公开开发：人工接续输入缺键，真实研究尚未开始

作者责任：本记录直接消费本仓库公开 Actions 的原日志与 metadata-only receipt；修复只涉及新人工夹具及其回执输出。没有在本地执行人工、原科学前缀或新优化。

## 实际来源

- run：[43716207246](https://github.com/Rogerhu12/math-research-public/actions/runs/43716207246)；
- job：[132818219795](https://github.com/Rogerhu12/math-research-public/actions/runs/43716207246/job/132818219795)；
- source：a99b8d88728bdd0c5c07c7419fe624b29118901d；
- lane：metric_height159_factorized_rows；
- 当次 driver SHA256：a4298bcb5191c7baa850e5568354060555ff13d037308425121d912f50067eed；
- [公开 provenance receipt](actions-43716207246-1-metric_height159_factorized_rows/receipt.json)：53133 字节，SHA256 61eb5d723b491ad1b2eac63d37be9ca525e50aed5509249ffaf936b93db03829。

公开 job 在新开发步骤退出。前置依赖、真正 pull/read 和 metadata-only 发布步骤均完成；退出不能解释为几何不可行或因子化数学错误。

## 原始错误及准确范围

聚合开发入口调用顺序为新 kernel/API/cache 子检查、接续子检查、编排 IO 子检查。错误发生在第二组的夹具构造：

    _new_handoff_fixture
      -> capacity_driver.reserve_prepared_stage
      -> replay['known_fine_metric_locations']
      -> KeyError: 'known_fine_metric_locations'

被复用的 labelled-array fixture 是较早冻结的纯元数据构造，没有这份后加容量适配器要求的峰位置列表。实际生产的 prepared replay 则由原输入链生成该字段。这里不能为生产接口改成“字段缺失也自动接受”；应完整给出新人工输入。

日志 traceback 证明第一组子检查函数已经返回，随后才到上述错误。但当次聚合错误处理没有保存那份返回对象；该函数也可能返回含失败检查的对象。因此本记录**不声称第一组全部通过**，更不声称总开发通过。

当次公开开发错误回执给出：

| 字段 | 实际值 |
|---|---|
| completion | implementation_check_failed |
| passed | false |
| development.all_passed | false |
| error.type | KeyError |
| error.message | 'known_fine_metric_locations' |
| 开发进程总秒数 | 4.491779401000002 |
| 完整 implementation source 哈希数 | 97 |

本次预定七个真实研究输入恢复均为 **0 次**；新真实优化也是 **0 次**。新小人工里已经发生的原 API/几何评价不属于真实研究候选计算，不能将其称为“完全没有执行代码”。

## 最小修复

仅修改 frame_metric_height159_factorized_rows_audit.py：

1. 新 fixture 调用 reserve_prepared_stage 前明确设置自己的 known_fine_metric_locations=[]。空列表表达这个纯元数据夹具没有先前记录的峰；不从缺键猜测真实输入。
2. 每个新开发分组返回后，立即在公开 stdout 打印 DEVELOPMENT_PART，保实际结果、本 source/run 和 driver 哈希。后面若失败，不再丢失前面结果；没有凭控制流推测 passed。

生产函数、三份已审 helper/adapter/development 源、数学公式、相同 159/163 族、原普通值、所有几何门、行池、容量、SOC controller、预算和 98 项 research 参数均未改变。没有新增旧 suite 或真实科学重跑。下一请求仍是完成尚未获得完整公开回执的新开发，然后首次执行原定唯一新科学阶段。

修订 driver：

- 73477 字节；
- SHA256 65b3dbb4318d6809a6cdfc053171c48f8f74a27b265586853c2858e8d63a4bb6。

本条只记录静态修复，尚不称修复后的开发已通过。

## 来源绑定与规则同步

42 个显式科学源码绑定逐项与公开 receipt 一致；另三个 workflow/publisher/print 绑定由部署请求控制。错误回执还记录继承实现的完整 97 源哈希。没有改旧来源或用宽松字段比较绕过原 handoff。

本次公开预研究实际 pull/read 到 32692cf1199ed09b428431b5d6e56c10b726c9cd，两份公开 README 无差后恢复计算 source。私有规则同步于 2026-11-15 12:54:58 UTC 完成真实 partial clone/pull，HEAD 为 b5ebad355fcbb9bd6f04a988e68f425ffa42f280；已知 README 身份无变、QUEUE 唯一且仍进行中。这里只记录同步元数据，不发布私有正文。

publisher 遇远端前进后真实 pull --rebase 并复核两 README，再发布回执。公开 receipt 的最后 readmes_read_commit 为 69765fcd81ca84819cdeb09c4fe14c55fdb5fb80。没有强推。

## 临时输出身份

按根规则 15 只保存来源与哈希，payload 不入仓库、Release 或 artifact。

| runner 临时件 | 字节 | SHA256 |
|---|---:|---|
| metric-height159-factorized-rows-development.json | 12588 | e756e45b14fb3db628f07e0fccdc8c18e8f165a6f3ca77e45ae6be93b5913cba |
| pre-research-private-pull.json | 559 | fd8e20fe3ab30b1ad56c52c844cf0417868b057c5a77c13c1c16d87d3c7237e4 |
| pre-research-pull.json | 253 | 5120c2ed223723de723ba6f9e8774ffcbcea5f709627ef33e137fd9189a5e484 |

本次没有研究主输出；不能据失败开出任何效率、改善或曲面可行性结论。
