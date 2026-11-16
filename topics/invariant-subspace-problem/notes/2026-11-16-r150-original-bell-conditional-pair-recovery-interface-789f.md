# Bell 原来源：只在真实 pairs 超时后续接的独立入口

日期：2026-11-16 UTC。作者：Astra-ISP-789f / normal_annihilator；AI-assisted GPT-6 Astra Pro。

**尚未运行。** 共享 executor 离线；没有声称本地 AST、Singular 或数学验证已做。首次实际 Python 解析在同一 Actions job 中完成。

## 1. 唯一合法分支

父来源固定为
~~~
notes/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
blob c5e81e3e97d0123df214a994667c5b046171ec82
31156 bytes
SHA256 da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d
~~~

子程序重新核父完整 receipt 的来源 SHA、原语义 binding，以及该 receipt 所指 **实际完整 stdout 文件** 的 bytes/SHA。只有下列条件全部成立，才计算：

- 父真实状态为 budget-checkpoint，末阶段是原 complete-original-weight-DD 且未完成。
- 该原 stdout 真有 all-original-source-identities-verified。
- 同 stdout 尚无 complete-bounded-Buchberger-check-verified，且没有 @@FAIL。
- 父 model、双 degree 自测及全部相邻完成 degree 的完整压缩/逻辑 SHA 均真；中断 degree 恰是第一个未完成 degree。

没有真实日志、身份不匹配或明确失败均报错。日志没有确认到 pairs 阶段则仅输出诊断并 exit0，**不重跑 std，不推测 std 或原来源已完成**。父已经完成亦不重复。

原进程中未 dump 的 G/S 没有被假称为缓存。合法分支重构一次，这是新付工作；来源/原母阵不变。

## 2. 独立检查点与全部验证

新 out：
~~~
{work}/original-bell-conditional-pair-recovery
~~~

子 binding 包含本源码 SHA、原父源码 SHA、实际父 receipt 完整 SHA 及父 binding。**不改父目录或原 binding。**

重构调用原已审 weighted liftstd，但在任何大 pairs 验证之前，完整输出每个 G 和全部18原来源 S。最终候选结束标记已出现时，先保存完整原 log 描述，再解析为完整 gz 候选。候选明确标记三个数学验证标志为 false。

之后分两层：

1. 真乘回 Original × S = G 的每列，并将全部18原生成元除 G 得零；该完整层完成才保存独立 source-verification transcript。
2. 对每一对 G，保完整原 weighted-lcm 分类。高于本 degree 的 pair 保作后继；本 degree 内 coprime-leading 用原乘积判据，其余每个 S-pair 实际 reduce 为零。每完成256个全 pairs 才写事务标记。恢复时重新核所有原 transcript 完整 SHA、相邻 cursor、三类累计计数，严格接在已付 pair 后。

只有全 pairs 数达到 n(n−1)/2 且原 source/reverse 已真，才记为本 degree 完成。某个 pair 失败不会被 budget 分支掩盖。MemoryError、输入失败、解析失败均 exit1；只有明确预算/信号为75。

若预算终止于候选重构，只有真实完整候选结束标记才能保存候选；否则不宣称存在候选。若预算终止于原 source 层，完整候选仍在、source 标志仍 false。若终止于 pairs，则只保存完成的256项前缀（最后完整总段可短于256）。

## 3. 数学范围

所有6均值、11 Hankel 与齐次参数仍保留。新源只是改变检查点与验证顺序，不改变任何原多项式、系数 place、weighted source 结构或完整性门。

本 degree 完成后才检查是否有纯 tt 幂列；若有，仍用独立 FLINT 将完整18原仿射来源乘回1。该结论仅属 F127/d100。

此 child 的新 binding/format 不会被偷偷伪装成旧 E consumer 的父来源。若真的产生 field1，须独立更新一个严格 child-parent 适配入口再实际做 E 来源乘回。本入口 **没有已经执行特征零提升的声明**。

## 4. 冻结源码

~~~
notes/2026-11-16-r150-original-bell-conditional-pair-recovery-789f.py
blob 3faeb6be262e3bf3e6c7aa361f1da9a13755bc32
23125 bytes
SHA256 d7a89c29e2f5fe5fbdcad29f9bac0c4c26f7249f4f6347193c18167c19a57a7d
~~~

仅额外取入原父31156字节源码，不需新的历史数组。父 model/自测/whole degrees 只来自本 run 的临时目录。

## 5. 同 job request 接续

将独立 step 追加到原 request 最后；requires 为空，因父75不是成功依赖，真正执行条件由本入口完整核验。预算900秒、4GiB、outer960；不设第二次900自动重试。

父 wrapper 已有真实硬门：必须让本次完整 outer 加120秒同时适合 session 的80分钟和 workflow 的88分钟。run 约08:32开始、第三次1800约09:32:37结束。若约09:33就启动，900仍可 fit；若发布较晚，**在请求中同时改为 --seconds600 / timeout660 / budgetResumeSeconds[600]**，不要降低原硬期限。算法 binding 不含软预算。

CLI：
~~~
python SOURCE.py
  --parent-driver {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
  --parent-out {work}/original-full-bell-homogeneous-source-prefix
  --out {work}/original-bell-conditional-pair-recovery
  --singular Singular --seconds 900 --memory-mib 4096
~~~

回执：
~~~
{work}/original-bell-conditional-pair-recovery/conditional-original-bell-pair-recovery-receipt.json
~~~

receipt 把完整 error 的 type/message 放在 parameters.error。完成/预算/失败和真实时间分别保留。所有数学数组仅留 job 临时目录，job 日志可读实际数学摘要；Git 仅新增源码、参数、执行身份与输出 SHA。
