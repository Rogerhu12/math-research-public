# R787：真实 518 位断点、同核继续与新精度完整核格入口

本条记录原公开运行 `43737413555` 的真实结束状态。它不声称准确原函数关系已经恢复，也不把有限格候选失败解释为精度不足。

## 1. 原运行与实际退出

原运行源提交为 `4092d1cc4d1156bc24a10ff820fd39c5713e8ad7`，计算 job 为 `132883028161`。核心仍为

`93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`，

标准库 runner 仍为

`42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6`。

核心回执明确为 `BudgetStop: All completed R787 stages remain available for exact resumption.`；`complete=false`、所有已完成阶段保留、准确 y 未恢复。runner 的 `process_exit_code=1`、`error=null`，结束回执时间为 **2026-11-15 21:49:24.756260 UTC**。这是原核心自己的预算退出；21:50:48 的 Actions 日志是后续整理输出结束，不应当与核心回执时间混为一谈。成功验证步骤如实失败，因为准确关系未完成。

对应小文件：

- `core-receipt.json`：308 B，SHA256 `ec4673e2b51e4b3e47b2fbea4ac75c34c7923e90d47ab3f80110cf35f426e8f7`。
- `run-receipt.json`：542 B，SHA256 `2184d2b06653df87d5e8f5166a582cc4e06025c6c1470ac32d04190dd615ccbc`。
- `public-actions-input.json`：7547 B，SHA256 `16732a6e67350e896a504d5105c1d97a5e548aff8c0ffefa9cfa28be084ac952`。
- `public-actions-run.log`：9945 B，SHA256 `82cffd8a479a841b5de42105d593ca7500b34ac1afe72e2a79594ecd287e9b6d`。

## 2. 已完成的真实 518 位

原小历史和原压缩回执一致给出最新完整阶段

`R787-prime-1000000753-dixon-00000518.json.gz`，

**73180954 B**，SHA256

`4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5`。

原素数仍为 `1000000753`。历史完整登记 518 条，不是把下一项进行中残差当成完整位。相较前一真实 430 位断点，本轮产生 88 个新完整位；此次整理移除 88 个被后继替代的旧 lift 文件，保留它们的文件名、字节、SHA、prime、digits，不改任何数学内容或其他完成阶段。

- `dixon-checkpoint-history.json`：120502 B，SHA256 `07875f05c10549fdbc6eeaf2bdd2071bcc2d74e35695c20698bfb86f634d1eed`。
- `dixon-output-compaction-receipt.json`：761 B，SHA256 `d4381a0ecbb30c1d9532b4dd46542c7c2e27f99b6dc72df5ca7a9ffd6ca4a37e`。
- 原 chart：5829 B，SHA256 `47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96`。
- 原 selection：5759 B，SHA256 `a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb`。
- 原 rational blocks：9169464 B，SHA256 `fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b`。

原 chart/selection/rational blocks 的字节来源均未改变。没有更换原自由方向、14 个模分支、原数域基或原 129×280 关系出口。

## 3. 可立即续用的公开产物

产物名为 `serre-global-R787-original-power5-function-relation-43737413555-1`，artifact id **14181899102**；完整 ZIP **451202899 B**，Actions 给出的 SHA256 为

`343bee0a0fb5bf8d9143d2dbc8b8d8fc0f0da3649bbb1d94748ef34f19d87249`。

实际完整清单 430709 B，1262 个文件，SHA256

`7a22beb22912c1d5c4c56a5faa577a529f6c5dab5bb4ea5251e9cd5c4264ba3f`。

ZIP 另含清单和引用，共 1264 个成员；引用文件 418 B，SHA256 `26f3e8b34fc579ff79502a224b5733c76cd7005a73ff6375c0a22fb47df1a970`。到期时间 **2026-11-16 21:50:48 UTC**。

本地只做下载、完整小文件哈希、JSON/schema 阅读，没有运行新的数学或重新生成旧证书。记录的完整 ZIP SHA 来自实际 Actions/API；它不冒充本地 Range 小文件检查已经重哈希整个 ZIP。原同核恢复入口会流式核完整 ZIP 及清单所有成员后恢复最新 lift。

## 4. 两个原源绑定的后继

### 4.1 原 93d3 核继续

原请求 `R787-public-original-power5-relation-request.json` **只更改 resume**，绑定上节真实运行、manifest、artifact 和失败结束状态。核心、runner、原 proof/method/field core、全部 R781/R786 源、原素数起点、每八位准确重构和 300 分钟预算不变。

恢复完整 518 位、原模分支和旧算术阶段后继续；不重做 1–518 位，不退回 430 或 259 位，也不切换 R802。当前仍无特征零原关系。

### 4.2 原完整核格的新精度消费者

[已证来源契约](R787-original-precision-increment-kernel-lattice-and-source-contract.md)的核心 `414fef537020ed2acbb98e4632c6132bb5f5e5fd4561c82bfe569a7381e0a7be` 和 runner `889cdf5e646759f1ffb79d5063ca604683668f8cc6bf77ac186134eedc635c88` 不改。

现在创建实际激活请求 `R787_precision_increment-public-request.json`，将 `new_checkpoint` 明确设为上述 518 位，并以真实 93d3 运行和完整 current 字节规格填写 `new_current_source`。源小集合只含 manifest、run/core/input、原 chart/selection 与完整 current；旧 430 位及原 1380 输入、42/56 全格载体沿既有接口保留，不下载或重算其他无关分支。

新的公开核心须检查完整 A/C 的来源及降模相容、真实归一化和全部尺寸，再构造 56×42 精度残差、unit minor、核基 K 与新完整格 K H，随后只做一次新的 56 维 LLL，并给完整幺模见证和原 129×280 准确出口。这些是该计算的数学内容；本条只完成实际来源绑定，尚未预称任何新格、候选、原关系或 y 成功。

旧 98 个固定 C 已被严格排除的结论原样保留。此新精度入口默认不复用它们：同一个整数 D 在新模数下可能产生不同 C，只有整个准确 C 相同才允许引用旧障碍。更深精度不是重跑旧 42/56 格。

## 5. 仍待原成功证书

真实 518 位和新消费者入口均不等于恢复准确原函数。只有原关系完整成立并输出合法的原函数 recipe，才能启动已经保存的原 R792 唯一 Fb 立方根及 R809 A/B 消费者；不把无穷远局部关系、短前缀或有限候选通过代替全出口。Serre 主目标、全 p 高度与同 h 三单位仍未完成。
