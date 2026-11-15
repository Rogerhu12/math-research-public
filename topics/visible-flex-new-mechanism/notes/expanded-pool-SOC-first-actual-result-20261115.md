# 首次完整 expanded-pool SOC 实际：原状态精确续接，新分支本轮未触发

作者：tail_cost；root 负责原始日志复核、公开提交与研究入口。日期：2026-11-15 UTC。

## 1. 结论与准确范围

公开 run **43744903357**、job **132905938795** 已成功完成。十项新增接口人工检查全部通过；前次完整 checkpoint 的真实 159 坐标、163 物理坐标、原 reference、完整两网行池、controller 和九条记录的 norm-direction bank 均按原定义续接。

唯一新科学阶段产生七个外层模型、七次新接受。两网最大 η 从 **0.26636627797457657** 降至 **0.26634752076125723**，下降 **0.000018757213319342547**。末态通过原两网硬约束、旧 η 预算 167/625 以及原物理盒检查；**新 η 目标 13/50 尚未达到**。

本轮 **expanded-pool rebound 记录为空**。实际三次 SOC 都走已有的 same-layout 修正路径；没有一次“原 primary trial 失败并学到新行后，在相同 x、相同 y、扩展后的完整池上重建模型，再作一次 SOC”的新生产调用。因此，本结果验证了新开发接口、精确续接和未触发分支时的完整科学执行，**没有验证新 rebound 分支的科学收益，也不把本轮下降归因于它**。

以下结论均为既有公开原日志的消费；没有为本稿执行新优化、人工检查、求积或模型重算。

## 2. 运行、源与输入身份

| 项目 | 实际值 |
|---|---|
| 源提交 | 5fa2424a6316b1daa8453864ce223b128a43d72f |
| workflow | .github/workflows/visible-expanded-pool-soc.yml |
| run / job | 43744903357 / 132905938795 |
| COMPLETE schema | same159-complete-checkpoint-expanded-pool-SOC-v1 |
| COMPLETE status | complete-two-grid-expanded-pool-SOC-checkpoint-audit |
| stage status | shared-primary-plus-SOC-LP-budget-exit |
| stage error | null |
| request 字节 / SHA256 | 43,258 / 5815427252d8e15c848f71b8afb4226f7301f13a7fbbe2b9d9f43a6180f7433d |
| 原 configuration 字节 / SHA256 | 19,240 / b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |
| request 绑定 | 119 个文件 |
| COMPLETE 科学源绑定 | 117 个；按 basename 对 request 原路径逐项匹配，117/117 相同 |

原 configuration 完全保留；新算法 policy 通过显式接口与评价定义声明，没有写回 factorizer 的原 configuration。否则原方向库 context 的 hash 会改变，本次精确 bank 续接不能成立。

五个新增源的实际 SHA256：

| scripts/ 下的文件 | SHA256 |
|---|---|
| frame_metric_expanded_pool_soc.py | 4226ff562467cf49a62b71de4b0300bb69bae4abe1df1c04ebb2845171f719bf |
| frame_metric_expanded_pool_soc_recovery.py | db447f3395b3754a7adc95432fbb288aed2efe7393382bf6c6cbf9bc49ca963e |
| frame_metric_expanded_pool_soc_development.py | 1bc4fbee6c7212d1d5e3a67efecab69f8bab92ee7fe37d00294710b3fe653a66 |
| frame_metric_expanded_pool_soc_transfer.py | 28fd45a5f21ac2172bc86ed951065b12015c26d9fe6fea48965d21ef8dbe1c7c |
| frame_metric_expanded_pool_soc_audit.py | 6b35bc03d4740982aca95c84aa2d41048358aff48328abf1be5cd14c0c12fd6e |

数学输入来自前次 norm-memory run 43741276060 的完整 checkpoint；不重跑其 primary 优化。新报告明确 old_optimizer_calls_this_run=0、temporary_input_restorations=[]。原 checkpoint 两网 η、κ 的本次初始直接评价与原记录之差均为零。

正式入口与设计：

- [本次运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43744903357)
- [本次 job 原日志入口](https://github.com/Rogerhu12/math-research-public/actions/runs/43744903357/job/132905938795)
- [本次源提交](https://github.com/Rogerhu12/math-research-public/commit/5fa2424a6316b1daa8453864ce223b128a43d72f)
- [扩池同 trial SOC 设计](expanded-pool-same-trial-SOC-design-20261115.md)
- [前次 norm-memory 实际](norm-memory-first-actual-result-20261115.md)
- [前次十一模型诊断](norm-memory-eleven-model-diagnostics-and-next-SOC-interface-20261115.md)

## 3. 新开发与精确续接

### 3.1 十项新检查

本次 EXPANDED_SOC_DEVELOPMENT 的 all_passed=true。以下十项均为 true：

1. 真实步必须取 y−x，且与实际子空间应用逐位核对。
2. correction 报告按模型号绑定，并替换继承 metadata 中的 rho0。
3. 失败点完整两网视图复制后只读。
4. 初始 bank 的完整 hash 与条数同时检查。
5. 原 SOC 数组使用新池的 y 残差与重新建立的 x Jacobian。
6. primary registry 保持原顺序，所有已开始的 oracle 仍入总账。
7. 真实 rebind helper 采用相同 x/y、新行，并绑定两层 factory 完成后的最终 complete signature。
8. shared ledger 对正常返回与抛错的已开始调用均计费。
9. 原日志 parser 保原 COMPLETE 文本并要求完整十一模型。
10. pool version 或原 ID 顺序变化被拒绝。

人工输入只用于新增接口。原科学 LP、geometry、surface JVP、旧 optimizer、旧 developer suite 与研究输入读取计数均为零。rebind fixture 实际调用新增 context/rebuild 以及原 selected-model、primary/correction 数组接口；完整 factory 的昂贵科学部分使用明确 stub，不把 fixture 当作真实曲面 rebound 已验证。

首 run 43744268876 的只读数组 fixture 失败仍保留。修复仅让新 fixture 临时使用可写副本，再验证被捕获失败视图不随副本改变；生产 core、outer、原科学源和原预算未改。详见 [首开发失败说明](expanded-pool-SOC-first-development-readonly-fixture-failure-20261115.md)。

### 3.2 方向库与物理状态

第一次 primary LP 前，原方向事件重放后的记录为：

- expected_entries=actual_entries=**9**；
- expected_state_sha256=actual_state_sha256=
  **07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81**；
- original-bank-exactly-replayed-before-first-LP；
- passed=true。

没有复用旧数值切平面矩阵 A/b 或旧 optimizer。原方向记录在本次冻结模型下重新形成切平面。

原完整池输入 coarse=4418、fine=4092；最终 coarse=4418、fine=4188。fine 总增量还包含本次初始化/行池学习过程，不能把全部 96 条简单解释为七个模型中两次各一条的接受后学习。模型 m3 与 m7 明确分别新增一条 fine 行。

最终 bank 为 **11** 条，SHA256
**d5b1b9d6128f05e0003baa1c22b109d0d9d4fb6598bfa0ba93f0ec969c127cb8**。

最终 canonical 物理状态 SHA256：
**981e092c54a5a7059bc75ffaea2f2c8bfa47c0b4c2f5932a67bd3fc74cee5376**。

future_direct_checkpoint 保存本次完整 reference163、exact159、physical163、两完整行池、bank context/entries 和末 controller。该 runner 临时 payload 没有提交到仓库。

## 4. 唯一新科学阶段

### 4.1 末态门与目标

| 量 | coarse 原值网 | fine 原值网 / 两网最大 |
|---|---:|---:|
| 最终 η | 0.26634717887965675 | 0.26634752076125723 |
| 最大绝对主曲率 | 57.999967976099626 | 57.99998852110966 |
| 原硬约束组 | 通过 | 通过 |
| 旧 η 预算 167/625 | 通过 | 通过 |
| 新 η 目标 13/50 | 未通过 | 未通过 |

原 hard ball、内/外 strip、signed height、regularity、原 mirror 与独立直接曲率检查均保持；没有仅凭 LP residual 或曲率 auxiliary 判断通过。原 physical box 使用原变量和原界直接核验，没有 clipping。

cap 的仿射/重构 margin 分别出现 −2.7755575615628914e−17 与 −5.551115123125783e−17，故报告没有宣称它们精确非负；它们按既有 1e−9 容差通过。原“新目标整体合格”相关布尔值仍为 false。本次有限两网验证不升级为连续曲面、嵌入或全局 reach 证明。

### 4.2 调用与模型轨迹

共 **9 primary LP + 3 correction LP = 12 LP**，达到原共享 LP 上限；非线性 minimize 调用为零。七个模型各产生一个新接受点，accepted_iterates 数组的第一个条目是初始点，因此数组总长八不等于八次新接受。

| 模型 | 实际接受途径 | 关键 controller / 学习记录 |
|---|---|---|
| m1 | primary | 继承 streak=1 后按原规则增长，B 从 1/16000 到 1/8000 |
| m2 | 原 same-layout SOC | 原 17 项 hold guard 全真；B 保持 1/8000 |
| m3 | 原 same-layout SOC | 接受后学到一条 fine 行；hold 因学习/布局条件拒绝，B 降至 1/16000 |
| m4 | primary | B 保持 1/16000，原 streak 更新为 1 |
| m5 | primary | 原增长规则令 B 回到 1/8000 |
| m6 | 原 same-layout SOC | 原 17 项 hold guard 全真；B 保持 1/8000 |
| m7 | primary | 接受后学到一条 fine 行；无增长，B 保持 1/8000 |

m2、m6 的真实 total-step ratio 分别为 0.9707590156142386、1.0399278910637653；其 SOC correction 的原 body norm 分别为 9.82182212228011e−8、1.1147094691743575e−7。m3 ratio=0.9729260978078214，虽实际接受，其后学习仍正确阻止 hold。上述 ratio 只是原 guard 的组成，不能单独授 hold。

初始 B=1/16000、streak=1；最终 B=1/8000、streak=0。全阶段保持原 12 LP、40 shared values、120 active seconds 的限额，没有通过放宽半径、硬门或预算获得接受。

### 4.3 新 rebound 分支未触发

expanded_pool_rebound_records=[]。m3、m7 的新行都来自**合法接受之后**的学习，并非新分支要求的“第一次 primary trial 尚未接受、失败且扩池”事件。其余模型没有产生满足该入口的失败新行情形。

因此本轮没有新的 rebound x/y 生产上下文、扩池后的完整模型重建、对应 scalar/complete RHS 或 rebound correction 实验记录。十项人工确实检查了这些接口，但不能替代它们在真实失败 trial 上的首次科学调用。

## 5. 费用

| 费用边界 | 实际值 |
|---|---:|
| prepare | 10.637722714000006 s |
| optimization active | 29.83614996099999 s |
| run_audit | 154.35414899100002 s |
| process total | 164.99187472 s |
| peak RSS | 2,310,436 KiB |
| shared 普通完整值调用 | 22 |
| 末态独立完整值调用 | 2 |
| 总 counted 普通值调用 | 24 |

报告进一步分开：

- recovery 前 initial ordinary audit wall：105.455902887 s；
- recovery wall（含 active 开始前第一次 Jacobian）：47.769714229000016 s；
- final coarse geometry/audit/support：0.2586069509999902 s；
- final fine：0.4719710410000175 s；
- final two-grid comparison：0.06352159499999743 s。

这些是源码定义的计时边界；不能把 recovery 外差额臆测成新 SOC 成本，也不据不同起点阶段的耗时作受控加速结论。新增方向扫描与补行 Jacobian 由原 oracle 分账，未伪装成普通 geometry value 调用。

## 6. 原日志、临时输出与规则读取

| 原件 | UTF8 字节 | SHA256 |
|---|---:|---|
| 完整 job log | 3,194,767 | 14cafc198a1df4e7de2882994b37b9dffcf4284daacc49c670a9f65240926c3d |
| 原 EXPANDED_SOC_DEVELOPMENT JSON+LF | 14,219 | d5f6caa58189a34d9b059557e37323e173982c9301236acb3076781fbfc94b97 |
| 原 EXPANDED_SOC_COMPLETE JSON+LF | 829,044 | 664b1bc5ddf7d278d61a78a36c712395f850109bfb967f5fe1df6a769b224b07 |
| runner audit-summary.json | 1,260,789 | e0850f1c06b3a07c291ae9ae7b4eb0e7587189240bd45674dfa8e9933e316db6 |
| runner audit.json | 13,945,697 | b2be7a4c41d3bee8f132994dba657cc0c7708da1fac79d164d50e6092347f651 |

JSON+LF 指原 stdout marker 后的原 JSON 文本与一个换行，未重新序列化。runner 两个 payload 仅临时存在，未提交仓库、Release 或可重算 artifact。

本次科学前 public pull 完成于 **2026-11-15 18:07:21.146370 UTC**，before=after=5fa2424a6316b1daa8453864ce223b128a43d72f；两 README 无差：

- 根 README blob 21bd547f56590b7f2dd279d0297efb289a9b2783，SHA256 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9；
- topic README blob d0432faff569c8e9af7ed4809847e12880976c11，SHA256 e685cff0e67e6851a7911d4e9efbae0e7d326e093927af177f716f059b8c566b。

private pull 完成于 **18:07:24.586496 UTC**，before=after=17e2a1b2762f89fe859a976369259b85984f3ec4；规则无差、QUEUE 唯一本会话仍进行中。这里只记录状态元数据，不公开私有规则正文。

下一项可判定工作是只读检查既有失败 trial 是否已完整记录原 x/y 与相关池身份，从而明确是否能在不重跑旧 primary 优化的条件下首次应用新 rebound。现稿不预设那些失败点可恢复，也不通过简单延长同一阶段等待分支触发。
