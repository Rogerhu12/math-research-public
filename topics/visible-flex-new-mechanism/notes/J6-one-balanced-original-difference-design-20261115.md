# R161 消费设计：R160 之后只检验一条 balanced 原差

日期：2026-11-15。**新源码与人工接口检查；本地没有运行研究目标。**

本消费器依赖已发表的 R159 忠实性定理和 R160 的完整 pure 原式身份。它不重新求解 pure，不重建旧 31 个核基，不重复旧 40 列生成或任何 profile 评价。本次只问同一组已证明的有理系数是否已经支付完整 J6。

## 1. 唯一新问题及准确逻辑

目标是 R136 完整正规加速度系数

$$
J_6=[h^{-2}]\bar A_{kk},
$$

其状态键为 `[-2,0,0,0]`，不是删去历史或部分 forcing 的系数。R160 已证明

$$
\pi J_6=\pi K_6,
$$

其中 $\pi$ 是完整 $-4$ 模式，使用原 R116 全局列号

$$
K_6=-\frac1{64}C_0-\frac1{64}C_{88}
-\frac1{128}C_{41}-\frac1{32}C_{73}
-\frac5{128}C_{81}+\frac1{256}C_{193}.
\tag{1}
$$

九基中的 $C_{48},C_{112},C_{170}$ 系数恰为零。本消费器从 R160 原证书读取这些**准确有理数**，同时核对九基局部编号与旧全局编号，不从模素数坐标或采样拟合取得它们。

令 $H_6=J_6-K_6$，这已经是普适 pure-zero 的完整 canonical 函数。R159 证明

$$
H_6=0\quad\Longleftrightarrow\quad\Xi H_6=0,
\tag{2}
$$

其中 $\Xi$ 只取完整 mixed $-2$ 模式中两个 $q$ 和两个 $\bar q$ 的双次数原式。唯一新目标为

$$
\boxed{\Xi\bigl((J_6)_{-2}-\sum c_i(C_i)_{-2}\bigr).}
\tag{3}
$$

若 (3) 的完整原差经 sound 同右锚积分分部规则归零，(2) 立即给全部 profiles、全部相位的完整身份 $J_6=K_6$。不需要另算其它 mixed 荷。若 sound 代表非零，只报告这次固定候选未取得原式身份，**既不证明 $J_6\notin R$，也不证明 $J_6\notin E_D$**。本消费器不包含 43 枢轴 Schur 分离或新成员搜索。

## 2. 已完成 pure 证据的来源门

固定 R160 公开实际：

- run `43660884663`；source `b41c6f13ffbe56543d3593acb0b9023d8320e93c`；lane `general_pure_J6_membership`。
- 原 producer `literature_general_pure_J6_membership.py`，23040 字节，SHA256 `48afb00617c5c5251bde7ab2f7782740ff43bf4318cfd78193137c3343c0f745`。
- main `general-pure-J6-membership.json`，64382 字节，SHA256 `d52e8cea9d0e7db1ca1b5348336ca18e0d7e38ab1e98d8c5ade79b84c9825660`。
- `receipt.json`，37243 字节，SHA256 `825cfe157853f75513ece5ae728e9a4db15c718b3195d72ead36afe9d2905ae2`。
- `general-pure-J6-membership-certificate.json.gz`，15080 字节，SHA256 `03e4e377632a7bfea3225d8ef27339bf26567f5aaa818ec7d23f9ce1a74568bd`；raw 101758 字节，SHA256 `bd9eabce279313b74dc51adfc1b55c4bac72369544fb7a1ec33c296cfdc246d6`。

消费器要求 `completion=complete`、`result.general_pure_J6_member_proved=true`，并核对证书中的 `one_J6_proposal` 与主报告。其 307 项原差 SHA256 为 `53958fd1febb5dd07595e9a807c3576923dfc8c00408fe463941d3560458cfab`；fresh 原代表必须为零，准确有理系数字段必须为真。

证书的 11 个原根仅作为已发表原证明的数据绑定使用；本次**不解码、不正规化、不评价**这些 pure 原根，也不调用旧 pure 求解器。对六项系数的读取同时检验：

1. 原九基局部编号到 `original_position` 和 R116 全局编号的对应；
2. 对应 pure 原根 SHA 与证书内已保存的原 SHA；
3. 完整 mixed 导出中同一 `quadratic_index/third_index/third_original_sha256` 及 pure 原 SHA。

因此不会用外形相同但来源不同的 mixed 列替换 (1)。旧 31 条关系只属于已发表背景，本次不读取它们来重新证明任何秩。

## 3. 只读取已发完整 mixed 原式

### 3.1 目标

复用 R136 的完整 648 根导出，公共目录为

`notes/actions-43654534244-1-acceleration_layer_mixed/`。

原完整导出 `acceleration-layer-mixed-original-expressions.json.gz` 的 stored SHA256 为 `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e`，raw SHA256 为 `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38`。其 source/main/receipt 的完整固定身份由已冻结 `prior.FAMILY` 复用。

仅解码 `family_0191_-2`，原 SHA256 为

`19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f`。

状态、family、完整与真权投影的原 SHA 必须全部相同。原 pure SHA `9f28420162242f5899bcbf4bb2398b793935ebad021b8f57bbd1fe129f4a0ab1` 仅作来源对照。

### 3.2 六个响应

复用 R131 的完整 50 列两模式原导出，目录为

`notes/actions-43653293263-1-g_translation_successor/`。

`G-third-translation-original-expressions.json.gz` 的 stored SHA256 为 `226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e`，raw SHA256 为 `eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7`。同样复用已冻结 `prior.RESPONSE` 的 source/main/receipt 身份。

只解码六个非零系数对应的 mixed 原根。解码涉及完整原 atom 表的拓扑恢复，但不会计算其它根、重建响应算子、重跑旧 forcing，或将原根代入某个 profile。六个旧列不分别正规化；本次仅将它们按 (1) 组成一个原差。

## 4. 颜色投影与右锚

原代数的每个 profile atom 是一个有色 jet，或一个具有固定右端的原 monomial 积分。每个 atom 的颜色次数等于其所有内层 jet 次数之和。故 (3) 可通过筛选原 monomial 的累计颜色次数准确取得，积分本身和锚均不改变。

本次不把 $q,\bar q$ 合并成同色，不取绝对值平方，也不把 $(2,2)$ 抽取称为真实输入相位旋转。R159 的使用只在已消 pure 的普适原函数差上。

输入 mixed 原式只允许三种双次数：$(4,0),(3,1),(2,2)$，总次数均为四，真实 profile 仿射权为 $-2$。筛选后使用已冻结 `ColoredWords` 的完整 shuffle/同右锚 IBP 规则；不使用仅支持一个 profile 颜色的 pure normalizer。所有积分均保持

$$
I(F)(\xi)=\int_r^\xi F(\eta)\,d\eta,
$$

只有已证明在共同右 collar 为零的正 profile 次数边界项才用于 $I(D F)=F$。不设左尾为零，也不重选锚。

## 5. 新源码与人工检查

新增独立源码：

`scripts/literature_J6_balanced_original_difference.py`。

本地执行仅 `--toy-only`，不读取已发表研究报告或原根。八项新人工检查覆盖：

1. pure 成功标志、准确 Q 系数及局部/全局列号绑定；拒绝未证 pure、模系数标志、浮点数和错列；
2. 内嵌右原函数中的颜色累计次数；
3. 投影与微分、同右锚线性积分交换；
4. 原导出只选择请求的 mixed 根；
5. 非零原差由真正的右 collar IBP 得到 balanced 零；
6. 非零代表只标未决；
7. 整体差的颜色投影保持原有理系数；
8. 新原差和未决原式导出/还原后的 SHA 一致。

人工中使用的 balanced 差包括

$$
I((q\bar q)')q\bar q-q^2\bar q^2,
$$

它在归约前不是零原表达式，但因共同右 collar 严格等于零。这不是任何实际 J6 目标的评价或证明。

## 6. 公开执行与资源

新增人工开发：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_J6_balanced_original_difference.py --toy-only --output /tmp/J6-balanced-development.json
```

唯一实际：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_J6_balanced_original_difference.py --output /tmp/J6-balanced-original-difference.json
```

默认三组输入目录均指向上述已发表目录。实际路径严格要求 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。人工分支不读取研究输入。

预算为 180 秒、1024 MiB 软轮询 RSS、500000 coefficient nodes、100000 atoms、120000 terms、500000 colored primitive calls。8192 位参数只保留既有辅助接口的局部 guard 语义，不称为全部算术的硬位数上限。没有新增线性消元或模运算。

输出上限：main 90000 字节、原证书 gzip 1500000 字节、必要时完整报告 gzip 1500000 字节，合计不超过 3090000 字节。超 main 时完整内容进入 gzip，main 保留来源和结论；不分片 API 读取大数据。输入接口异常与资源退出均写明阶段和错误，不能当数学阴性。

## 7. 输出和后续消费

主报告 `J6-balanced-original-difference.json` 包含：

- R160 成功 pure 身份、准确六项 Q 系数及来源；
- R136/R131 的完整字节来源和本次七个 mixed 原根标签；
- 唯一 balanced 原差的完整原 SHA、term count、sound 代表和规则统计；
- `complete_two_mode_J6_equals_exact_R160_response_combination`；
- 不论结论如何都保持 `complete_J6_nonmember_proved=false`。

`J6-balanced-original-difference-certificate.json.gz` 保存七个输入 mixed 原根、固定组合、未投影完整 mixed 差和 balanced 差，共 10 根，以及完整新 word 代表。根名与 SHA 均可独立还原。对成功情形，完整函数身份由**已消费的 pure 原证明 + 本次 balanced 原差零 + R159**三部分共同构成，不把本次投影单独提升成完整身份。

若 (3) 未归零，本次即停。未来是否进入 31 维响应核或 34 维扩展核成员问题、是否消费旧 42 枢轴与 R153 已保存残差构造隐式 Schur 分离，均是另外的有目标工作；本源码不自动执行它们。

本次无新几何、无 profile 采样、无额外第四 ruling、更高阶或主课题完成声明。
