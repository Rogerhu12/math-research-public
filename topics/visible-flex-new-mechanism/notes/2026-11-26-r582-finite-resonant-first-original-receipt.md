# R582 有限非圆首 run：新内场已付，冗余高度求积导致实现失败

原始自然终态：run `45824332845` / job `139924470256` / source
`d1e1da311acc61e11143fb2888f7613a4eaeb53a`，job conclusion=`failure`。
本条在 job 完成后一次读取完整原 stdout；没有活读运行中日志。

## 1. 真实身份

- 原 stdout：472257 UTF-8 B，SHA256
  `578b102f0ef09b4250fc3e9e266422e04e116c00ed51d782ce61fb16a20fcdd8`。
  原文仅在 Actions 与 scratch `/tmp/runlogs/job-139924470256.log`。
- request：103414 B /
  `c10309837d46d587ab7112e667fac4b8af339ba60a2e88b6867bb1f20151386a`。
- stdin 完整小输入：96819 B /
  `387d58a18278b1b46cbbe6e834d24d42c8eeb84bf9d3e95e3030d629dac51852`。
- driver：`f7e4c570cc11f6810973d5357a5543ec9754416ab3a55302876cc70486246d7c`；
  Model：`584f02a67af1c0e87a68dac629d6e17b9b1bad93cef2c4c65b5a3b0c2253639f`；
  field：`1b046b20541fcee05d5c8722dfdd5a509e7018348aab7182bec77c0813a8b395`。
  原 13 项 source binding 在入口全部通过。
- `FINITE_RESONANT_FIELD` JSON：114947 B /
  `cc24a459204ceed3047e2de437d9268242bb2eef1764830f8982bf26e3c9ee1d`。
- implementation checkpoint JSON：1356 B /
  `65c29976d6d87d007073ce77e70530473cd77e7951b2c2734532b789db57dba6`。
- FINAL JSON：119117 B /
  `7376b0a882baa61d651dab169fbc65448ee0914389794d61adb63c6c6a91157c`。

公开实际 pull 于 12:56:43.644363–12:56:45.829523 UTC，从 source 到
`ae7de02d9388d130d4e18ab38ef44112d74167be`；根和课题 README blob
保持 `282e86b…`、`d0432fa…`，diff 空。私库实际 pull 于
12:56:47.900829–12:56:49.052607，从 `3b82e4c…` 到 `2348ed01…`，
根 blob `5ba1648…` 一致，QUEUE 唯一且仍为本会话进行中。

## 2. 已完成的新内场不能算成无科学启动

本次复用旧 M169/factor8 起始归一状态，完成了一份新的 dense outward
场，共 **160 段、960944 RHS**；新 inner DtN 和旧三种子比较均未执行。
另外完成新 exact-core forward：2510 RHS，以及新短 tail-backward：
206 RHS，各 1 次。

新 dense 口减去已付 normalized 口乘同一 λ 的六 jets，依次为：

    -8.646512325571898e-18, 8.031769693772617e-16,
    -8.171241461241152e-14, -5.259681579161679e-15,
    6.328271240363392e-14, -5.879741138414829e-13

core forward 到 .82 与新 dense tail 的 `(A,C)` 差是
`[1.5297986673008107e-12,1.055763809709731e-11]`。这些是浮点差，
没有改写成准确返回或 ODE 误差证明。

共同端点 Hermite 内场已完成：原采样候选 63045，合并后 **62878**
端点；完整结点/六 jets 的 binary64 SHA256 是
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。
额外 material 观察选中 2956 端点，连同中点为 5911 个位置；未选
端点最大 jet 为 `7.838393053637985e-13`。这不是区间内误差界。

数值种子确有零 suffix，数学无限核与其 C² 差未认证；未计算内尾的
标记位置是 u=`1006.8799923538346`、s=`.8936970895024391`。
274689 个非零原始 jet 分量在归一缩放时下溢为数值零。不能从
`uncomputed_inner_tail_query_points=0` 误推无限内尾已算：这个计数只说
本次被实际查询的有限端点没有进入该返回分支，既不计 L，也不消除下溢。

FIELD 输出的已用科学时间为 `69.98889437100001` 秒。完整 FINAL
科学时钟为 **`70.62187625499996` 秒**。child 从
12:56:54.942375 到 12:58:06.244205，wall=`71.301830` 秒，包含导入/
打印/异常退出，不能替换科学时钟。

## 3. 失败位置及未获得的几何状态

两个 Model 构建被发起，累计投递 10929 个径向位置。在构建细网的
`field.angular_radial_jets` 时，只需参考 `a,a_s,a_ss` 的二导商法调用
了 `ContinuousMean.jets`，而该接口还计算了不需要的 H 高度。
原异常链为：

    fine = Model(par, fine_nodes, 2*nt, field)
      -> field.angular_radial_jets
      -> self.mean.jets / base_jets
      -> height_one
    ArithmeticError: partial actual height quadrature:
      Extremely bad integrand behavior occurs at some points of the
      integration interval.

这是冗余高度求积的实现失败，不能作为有限非圆数学障碍。
没有 `FINITE_RESONANT_START`、完成的几何细扫、方向核、Jacobian、
SLSQP 或 callback。FINAL 中 `actual_grid_p`、`actual_retained_p`、
retained、last trial 与自然 OptimizeResult 都是 null；实际约束/细网
数组为空。计划 p=.181、初 trust=.01 未成为已优化或已接受状态。

最终 field 计数：

- `continuous_profile_radial_values=14095` 是入口投递位置数，不能说
  这 14095 处的整套 profile 已全部完成。
- height queries 6963，cache hits 913，QUADPACK RHS 471744，
  nonconvergences 1。
- dense tail radial queries 62443；material Hermite queries 10929。
- 原模型新 `actual_weight_calls=1023386`、`outer_RHS=960944`；
  `inner_RHS=linear_least_squares=mean_control_candidates=0`。
- 新完整几何/后端统计字典为空，因为尚未进入这些阶段。

## 4. 下一输入是必要修补，原已付账不抹去

后继只把该商法所需的参考 radius 0/1/2 jets 按相同 step、Bspline、
固定 μ bump 的解析公式直接计算，避免不需要的 H 积分。不得删掉
原 4811 点、材料点或近重复点来绕开异常，也不重跑旧 core shooting、
三种子比较或圆核恢复。

本次内场只输出 mesh hash 和小摘要，没有把整份 62878×6 数组保存
到日志、缓存或文件。因此后继若需要再次生成该数值 material 表示，
其全部新费用必须列作**已识别内场的必要再求值**，并保留这里已付的
70.62187625499996 秒及完整计数；不能称成零成本或首次计算。

本次 README、固定 g 精化、准确有限等距族、连续全 reach 全部未完成。
