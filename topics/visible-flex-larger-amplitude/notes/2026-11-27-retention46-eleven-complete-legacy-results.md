# Retention 46：十一份完整旧闭合结果的来源、参数、结论与恢复

作者：construction（GPT-6 Astra Pro，AI 辅助），2026-11-27。

本批提议只从当前树退存十一份已经生成的旧结果，毛量 **2,800,118 B**。完整生产源码、原数学参数、实际运行记录、证明、输入档案和已知消费关系保留。恢复依赖固定 Git 对象；没有读取、解压这十一份候选正文，没有重新运行任何科学计算，也没有把保全工作当成新的数学进展。

完整源与输入注册表和完整参数台账分别为：

- [retention46 完整源与输入注册表](../computations/resume-20261127-retention46-source-input-registry.json)，94367 B，SHA256 **d68978957c5ed3fcf948be0eb3e5b1e8a344a62ec6ff3afc3fa889c940b63bb9**，Git blob **206a6e724db6a1eb0743bcae8298117ec157f60b**；189 个完整文件身份。
- [retention46 完整台账](../computations/resume-20261127-retention46-legacy-exact-raw-retention.json)，89242 B，SHA256 **d744ff98ccbe2dd7007156d72be0576faa24aa3b3c8e85e8f4cc832e697b429c**，Git blob **771a00d1ae8fa092f5b6e06e785d6ec330b968a7**；十一条候选、十份原资源对象及全部原 argv、另一个明确标注的 source-derived 复算 argv、递归文件组、实际结论和逐文件恢复项。

这些文件不是原输出的数值替身。需要消费某个原输出时，先从固定历史恢复其完整原字节，再走原消费者的完整身份检查。未知 whole SHA256 不用 Git blob SHA 代填，也不从显示小数重造。

## 1. 固定观察点与精确范围

本次只读观察的实际 HEAD 是：

**ad53b75a50916bd96599d6962bc7e16b166cafbb**

对应 root tree 为 **139c711d058e8efb0e04e83a4cc6a0510d47f7fe**，课题 tree 为 **1cd2fc8caea5810ed4f7ac6823cf0ff40dc5dd6b**。notes、computations、results 的三个 recursive tree 返回均未截断，完整 tree 身份保存在注册表。

十一份候选均在该固定提交下实际存在，路径、Git blob 和字节数已经逐项对应。某些更早退存的输入需要从 **60321451c058c6a51da58c37ae5ec6f2d1145f74** 恢复；注册表对此逐项显式列出历史提交，没有假设当前树仍保存其正文。

所有路径均相对本课题目录：

| 条目 | 完整候选路径 | 字节数 | whole SHA256 来源状态 |
| --- | --- | ---: | --- |
| ret46-01 | 2026-11-12-closure-nonlinear-low-far-lift.json | 305,722 | whole SHA256 未知，保留 null |
| ret46-02 | 2026-11-12-closure-plateau2-nonlinear-low-far-lift.json | 305,739 | whole SHA256 未知，保留 null |
| ret46-03 | 2026-11-12-closure-newg-strong-m20-real-low-far-lift.json | 305,825 | whole SHA256 未知，保留 null |
| ret46-04 | 2026-11-13-exact-resume-common-strip-r1.json | 316,677 | 已有小记录给出 whole SHA256 |
| ret46-05 | 2026-11-13-exact-resume-common-strip-r2.json | 162,099 | 已有小记录给出 whole SHA256 |
| ret46-06 | 2026-11-13-exact-resume-localV-budget-r1.json | 274,079 | 已有小记录给出 whole SHA256 |
| ret46-07 | 2026-11-13-root-joint1200-independent-saved-consumer.json | 287,422 | 已有小记录给出 whole SHA256 |
| ret46-08 | 2026-11-13-closure-r100-spectral-r1.json | 214,941 | 已有小记录给出 whole SHA256 |
| ret46-09 | 2026-11-12-closure-r53-balanced-axes-r1.json | 174,797 | 已有小记录给出 whole SHA256 |
| ret46-10 | 2026-11-12-closure-r53-balanced-axes-r2.json | 178,357 | 已有小记录给出 whole SHA256 |
| ret46-11 | 2026-11-12-closure-joint-rho-sensitivity-r1.json | 274,460 | whole SHA256 未知，保留 null |

只有这十一条进入删除列表。R43、R44、R45 已退项目没有重复计入；原 ports 缺口和原 driver 不匹配的 Nelder 文件继续保留。本批不删除任何源码、请求、原参数、证明、运行资源、小型归档清单、当前 Fejér 输入或当前科学返回。

## 2. 完整来源怎样保留

每个条目都有确切生产源、完整输入路径集合、数学默认值与实际显式参数、原运行证据、输出范围及后续消费说明。原命令中的绝对路径和参数字面保存在台账的 **full_original_resources** 中，没有省略原 Node 内存参数、Python 的 -B、不同 cutoff 列表或 far 指数。

十份原资源记录保存正式 exitcode、signal、wall time、RSS、完整 argv 和资源包装器 SHA。原包装器是完整的 **computations/strong_resource_run.py**，SHA256 为 **bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59**。包装器未修改求解行为，其 exit0 和数学结论在本台账中分开记录。

localV 预算消费者是一个不同情况：本次没有找到其单独的原资源/argv 文件。保留的完整证明明确记录了实际完成、约 0.3644 秒与 23272 KiB，并给出输出及输入身份。台账从完整源码构造了包含全部五个 required options 的复算 argv，明确标为 **source-derived invocation**，没有把它冒充当时捕获的原 shell 命令或 wait4 记录。原完整证明和精确 physical-interface 文件保留，原结果 whole SHA256 由该 interface 的输入归因给出。

复用先前保全只复用已闭合的具体来源，范围不扩大：

- retention44 的完整源和输入注册表保留原旧核、真实输入与固定恢复对象。
- retention45 的完整 R100 head、低46/Green helper 来源及原资源可直接引用；其七条删除项不再次删除。
- 本次对新增生产源、运行资源、小清单和实际读写点做了纯源码/小文本核对。没有导入科学模块，没有执行 Arb、Fraction 数学例题、ODE、F/J、root、目标函数或几何扫描。

## 3. 三份 low–far lift

### 3.1 各自完整的实际入口

三份结果分别来自：

1. **computations/closure_nonlinear_low_far_lift.py**，SHA256 **ad4c3ff2efa58dd9091a004d742fa455e60f7394a18c979210d713e8fdc6af78**。
2. **computations/closure_plateau2_nonlinear_low_far_lift.py**，SHA256 **8f81ad3111939b441c77e8892f31561b532ea7ea700db9d4867f829506f01b17**。
3. **computations/closure_rebased_nonlinear_low_far_lift.py**，SHA256 **2e16ddf58f84081516c8716055628207ddd7d36cfabb8d1bd1004e02e731081d**。

三个文件的完整来源和 helper 文件均保留，不用一个程序名覆盖三个数学输入。它们逐项读取相应 columns、ordered、reference、box、ready，以及原 columns 清单引用的六个完整列组。完整 46 个偶模式 2…92、213 个胞元 12…224、完整 mean 和逆的原公式均保留。

六个列组包含 01–08、09–16、17–24、25–32、33–40、41–46，注册表列出了全部固定历史 blob 和大小。不能用早先 m8 小清单代替它们，也不能只恢复前八列。原 ready 的完整物理参数和全部源定义仍是整文件输入。

原精度为 192 位。实际第三条命令显式传 **--far-log2-bound=-2224**，不是该源码的未用默认 -2200。各 reference/box 也是不同完整对象，不能互换。

### 3.2 原结论没有升级

[R36](../results/R36-nonlinear-low-far-graph-feedback.md) 的原结论是 q003 低46投影头及实际 R18 低非线性 far 图反馈。原完整比较小于 4/5，额外 Lipschitz 和逐行 slack 费用按原证明保留。

[R38](../results/R38-shallow-plateau-strip-and-nonlinear-low-head.md) 改变已声明的 plateau2 范数权重，保留同一原问题及实际全列。其小比较常数不能替代完整高频接合或 mean 接缝。

[R39](../results/R39-actual-strong-m20-node12-low46-head.md) 使用实际 strong-m20 选定的边界参考。原默认统一 1% 球失败仍然失败；后续非等盒另付成功，原比较上界 0.271653516 以及完整 low-far 反馈小于 0.271654 的结论按原范围保留。它不把投影头提升为完整外 Darboux 解，更不证明闭面、reach 或当前 Fejér 目标。

原 strong-m20 完整响应的 whole SHA256 **528fd51921f7cad71445d76669b44e60279c0fc31cddf9041f8ea5b1f7477962** 及其固定 Git 恢复也加入注册表。该父身份不能代替三条独立 lift 的完整 reference/box/argv。

## 4. 两份 common-strip 阈值扫描

两次都使用完整的 **2026-11-13-exact-resume-common-strip-v1.py**，SHA256 **f1a65067877403c508c13c1e290948738f3fd89d85c21dfb0844b138ed749b90**。精确源 SHA 请以注册表原字为准：该字段在注册表及稳定清单中保存为完整 64 位值，本说明不承担替代源码身份的作用。

两条实际 cutoff 参数分别为：

- r1 使用原默认 **5760,8192,16384,32768,65536,131072,262144,1048576**。
- r2 显式使用 **33792,34816,36864,40960**。

所有 10793 个原叶、18 个原 source/frame stream、25 个比较块、原正 dyadic frame、每个进入跳跃及完整 source/target 顺序都保留。原参数是 kappa=1/2^18、epsilon=1/2^25、window ratio=33/32、initial strip=18/125。原 frame helper 的完整 SHA **828ea557a5f9b702658eed425cc6344128d7e4be4a13a3efefc1d25b6c302fe5** 单独保留，未把旧对数函数改成浮点近似。

台账列出全部十八份框架包的原 whole SHA、大小、原路径及 panel 数；完整 hybrid leaf stream 及其 whole SHA 也保留。不能用仅有 leaf count 的记录代替这些实际输入。

[完整 common-strip 证明](2026-11-13-exact-resume-common-strip-proof.md) 和 [R118](../results/R118-common-strip-and-actual-middle-physical-cap.md) 保留原失败阈值。5760、8192、16384、32768 未支付共同 1/64 floor；这些结果没有因本批退存被改成成功。后续选择 34816 的完整 primary 和完整 leaf stream 不在删除列表。该共同条带计算也没有自动解掉新增的 14528 个正有限模式，更不支付非线性全耦合或 cut。

## 5. localV 十八块双模预算

完整源为 **2026-11-13-exact-resume-localV-budget-consumer.py**，SHA256 **5a5855d7fd25d7bdfa5d4c7589a041d2e964b79c0320132a4adc40e719291e5f**。它的四个完整输入是：

- 完成的 localV-v8 primary **2026-11-13-exact-resume-localV-r3.json.gz**。
- fresh R104 完整 causal primary **2026-11-13-exact-resume-causal-r1.json.gz**。
- 已完成 balanced-head ledger **2026-11-13-exact-resume-balanced-head-r1.json**。
- R101 全源准确摘要 **2026-11-13-closure-r101-exact-summary-r1.json**。

程序保留 cell11/segment0…8 再 cell10/segment0…8 的全部十八块、m94/m96、三种 source 材料 2/1/0、完整 mean 小根与逆、所有正半径和距离权。原距离目标 1/2、物理域 2^-34、中心常数10、固定96bit向上 dyadic 规则均原样。

原 causal 输入有两个不同身份：gzip whole SHA **eab2106db893c33c408683dd6405b89fc9bfacaf92faace7d56324063eea0669**；程序核的解压 JSON SHA **9e28fcf3ea53003e16ec8720a2fd4c52da0d16a40c8a90398c0b847d0f2fc317**。它们没有混为一个值。

[原完整证明](2026-11-13-exact-resume-localV-fixed-point-proof.md) 和 [R114](../results/R114-actual-localV-middle-two-mode-fixed-point.md) 给出该明确双模投影方程的唯一解、十八块自映/收缩及原 physical sum 小于 2^-62。其它中频、低反馈、无限高反馈、all46 cut 和闭面结论没有随之支付。旧 v6 checkpoint limit、v7 文件名预检失败和旧 aggregate scalar test 的 false 状态也没有被改写。

保留的 **localV-physical-interface.json** 明确以本候选的 whole SHA 为 source_sha256。因此这个字段是被消费结果的身份，不是程序源码 SHA。台账已单独注明。

## 6. joint1200 独立保存行消费者

完整消费者 **computations/root_joint1200_independent_consumer.py**，SHA256 **c88217b8e9048b69f7078d46cc9e39502e83a03a0226f15fe1cfd3ae3a3c4fbc**，原实际 exit0、3.811214685 秒、峰48184 KiB，6096项检查通过。该运行记录完整保留。

它读取完整原1200分量证书、原生产者及原运行资源，并核对八个 frozen inputs、完整 conditional-image packet、25个 source block 和25个 target block。台账显式保留原八输入 records 及所有 target original_path；注册表列出全部五十个块的固定 Git 身份。source summary 的完整原 source_records 留在其未改归档中，不能把 summary 当成只有计数的替代文件。

原程序并不重新计算 ODE、near-window kernel、浮点提议或原映射。它完整检查保存的半径、像、Jw、权重和物理域；原映射数学公式的源码审查由 [原完整审查记录](2026-11-13-root-joint1200-independent-audit.md) 承担。这一区别在本台账中保持。

原结论属于旧固定背景的 full-frequency mixed-boundary ball：低46、有限非低94…34814、无限高从34816开始，原真实 mean 和逆都在。1200是分块范数的数量，不是1200频率截断。all46 参数 cut、其它外域、闭面、全相位 reach 和新强幅构造仍是独立责任。

## 7. R100 六轮谱包及已知消费者

完整源 **computations/closure_outer_low_spectral_r100_v2.js**，SHA256 **eac90d6f7c816a67590c2c07d031e24d27af0adfd21e1b5ef5411891943b903e**。原实际 argv 完整保留九个输入及 Node 的 **--max-old-space-size=48**、**--max-semi-space-size=4**。

特别保留实际执行路径 **root-r100-source-reweight-r1.json**；不把源码里未用的默认 basename **root-r100-complete-source-reweight-r1.json** 冒充实际输入。相应 head 已由 retention45 完整保全，whole SHA 仍是 **617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9**。

原程序做六轮完整46 signed-pair 包围，保留 Neumann 0…4 全项及正的整个5+尾、完整 mean、完整逆和原 R100 分组参数域，使用 BigInt 分数与128bit向上 dyadic。原三十门通过、完整低中心范数小于9.084等结论由 [R101](../results/R101-hybrid46-low-spectrum-and-complete-middle-sources.md) 保留。

已知直接消费者仍保持：

- **closure_r101_actual_spectral_summary.py** 对本 whole SHA 严格硬钉，并与 wider 主包一起核完整谱/覆盖/尾。
- 原 wider 主包明确绑定本候选，没有把未知中高增量免费提升到更宽条带。
- R127 low-frequency 输入 manifest 的 low_spectrum 角色明确指向本候选。

本批不是断言这些消费者今后不再需要原数据。未来任何相应消费必须恢复相同 whole 原输出；完整稳定清单、生产源码和小结论仍在，精确大结果也能按固定 Git 对象恢复。

## 8. R53 两次轴配平与 rho 诊断

### 8.1 两个 R53 版本保持真实区别

v1源 **closure_balance_parameter_axes.py** 与 v2源 **closure_balance_parameter_axes_v2.py** 是两份不同完整程序。原三输入 lifts、parameter-ball、axes 都保留，原641行半径/J/W、213胞元、46轴、真实物理半径及完整 mean/域责任不减。

v1守住旧 far 预算 R*e，正式成功但所有轴增益为0。v2显式采用实际 saved lifted-map far slack 的一半，八个精确有理门通过，增益为0…21二进制位。它不是给 v1 改标签。两者的域是加权 l1 球，不是可以同时取各轴最大值的乘积盒；物理高度转换是实际 b^4，不另乘一个 w。

[R53](../results/R53-actual-full46-head-parameter-domain.md) 的完整参数族定理及其未付 outer Schur/大幅闭面范围保留。退存两个生成账本不删除原46轴全数值的恢复路径。

### 8.2 rho 输出仍是浮点诊断

完整源 **closure_joint_majorant_diagnostic.py**，SHA256 **95a5dbe9c8959fa0f306e4128165deb9f27ce37ab1be245318a70079f262ccd9**。实际参数仅为 **-60,-90,-120,linear**；源码默认中的 -30 没在这次原 argv 执行，台账没有补入。

输入除了 low、high、density，还包括 high.gamma_source 指定的完整 middle causal packet。全部路径身份及历史恢复保留，没有因为它是嵌套读取就遗漏。原214行正比较、完整213胞元与低46、64步正提议、NumPy eigenvalue/inverse 和下溢记录均沿原源。

[R49](../results/R49-current-scalar-majorant-two-cycle.md) 区分了约2.22942的浮点诊断、线性极限约2.22940与独立 exact two-cycle 结论。本候选的 formal exit0 不等于区间谱证书，也不证明原非线性问题无解。确切的 separate two-cycle 程序和结果不在本批删除范围。

## 9. 恢复规则与消费者责任

每个候选均可直接按固定提交恢复完整字节，形式为：

~~~sh
git show FIXED_COMMIT:topics/visible-flex-larger-amplitude/RELATIVE_PATH > RECOVERY_PATH
~~~

这是恢复文档，不是本轮执行过的命令。直接 Git 恢复与数值再生成分开：

1. 直接恢复使用固定 commit、完整 path、Git blob、bytes 和已知 whole SHA；未知 whole SHA 保持 null。
2. 如果未来确实要重跑原计算，再恢复完整 source、所有原输入、嵌套块和原参数，保留原路径字符串及摘要守卫。
3. 内嵌绝对 path 不能通过编辑 hashed JSON 来“适配”。应在恢复目录提供原路径或等价文件系统别名，保持整个原记录字节与所有哈希检查。
4. 原输出往往记录 elapsed、RSS、路径或原执行环境；不承诺重跑产生相同 whole SHA。需要历史原字节时直接恢复固定对象。
5. 新科学执行只进入既有授权环境；这批保全不安排、不要求额外 scientific replay，也不增加 fixture、AST 或新准入关卡。

已知消费者已经明确列出，未作“仓库不存在其它消费者”的泛化断言。完整历史对象始终可恢复，因此未来真实消费者的输入责任并未删除。

## 10. 实施与容量

本说明及两份 JSON 均小于100000字节。候选正文读取次数为0，解压次数为0。本 worker 只创建未引用远端 blobs，没有更新 ref、queue 或现树，也没有删除文件。

root 最后按其新鲜树元数据比对十一条候选的 path/blob/bytes，只实施相同对象的普通树更新，并同时刊入完整三份保全文件。任何元数据不符都不静默删除。这个必要身份对应不是新的科学审核门。

最终三份新增文件共 **201942 B**；从毛量2,800,118 B扣除后的当前树净释放为 **2598176 B**。这为完整源码、参数和真实返回卷提供空间，不削减当前科学算法或把未知未来结果登记成完成。

本批没有改变 README 的任何目标，也没有支付新的数学界。保留的旧结论仍按其原固定背景、参数域、频段和证明范围解释。
