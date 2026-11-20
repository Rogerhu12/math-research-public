# R141 准确 cell moment 的最小后继接入

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

这是纯定义接入说明，不是科学运行清单。44730452579/1 的源码、manifest、
参数和运行不变。待它完整结束并读取全部 actual/execution 后，才根据真正
未完成的目标决定后继 owner；不以性能优化为理由重复成功目标。

所用新引理是 R141 exact-cell Green moments 补篇 GM.1--17。
新纯模块为 fourfold_codazzi_low_centre_exact_cell_moments.py；
独立 adapter 为 fourfold_codazzi_low_centre_parent_moment_provider.py。
二者均不导入数值库、不读写文件、不含入口。

## 1. 为什么 whole-parent 缓存准确

当前 assembly 的 prepare_complete_kernel_context 最后定义
centre_matrix(outputs,inputs,box)，实际调用
_complete_signed_centre_matrix(packet_at(box),outputs,inputs)。
packet_at 只由 domain.cell_index 和 parent_indices 选择一个已完整包围的
原153 parent packet，**不依赖 box 的内点坐标或宽度**。
RefinedContext.centre_matrix 只是将 refined box 映回原155 comparison panel。
因此以下各矩阵球在一个155 comparison parent 内对所有 refined cells 和
全部4 subboxes 都相同：

- 完整低193的 AL 球，含原 signed primitive 和独立 mean row；
- high97..160 到完整低193的 C_LH 球；
- 同 parent 的原 Df、S 及 S inverse。

这只说明**同一个 enclosure 可缓存**，没有说实际系数函数在该 parent 恒定。
该源球覆盖原全部4650闭行、4801交集、collar 和完整参数身份；adapter 不缩小它。
三种非恒定角色仍按 GM.14--15 作逐点 PSD covariance upper。

原 refined defect 的 comparison ratio 可准确改写为
$$
 \frac{H_{\rm parent}/n}{h_{\rm parent}/n}
       =\frac{H_{\rm parent}}{h_{\rm parent}}.
 \tag{GI.1}
$$
右边保真正 variable-root length，只省掉两次独立 rounded division，
没有使用 h-midpoint，也没有改变原 comparison model。

## 2. 五种 source 的确切处理

| 原 source role | W | covariance资格 |
|---|---|---|
| ordinary_raw_low_source | I193 | 真正恒定，V=WWᵀ |
| transformed_low_source | 原 S inverse | 真正分格恒定，保原q球 |
| true_coefficient_defect | (AL−Hparent/hparent) S inverse | whole-parent球经GM.15 |
| low_second_kind_correction | (AL−Df) S inverse | whole-parent球经GM.15 |
| centre_high0_return_source | 原完整 C_LH，输入128 | whole-parent球经GM.15 |

实际 high feedback CFB 不被放进一个 local W。原高反馈/原 WJK F /
原真实 G_H 的不同资格完全保留。

每个 parent 只留一个 H/Q 模板和至多五个 source moment。
每 refined cell 仍读取各自的 directed L,R,ell,rho；不存在恢复长 parent
carrier 的步骤。QL/QR 和该节点的平衡行列只算一次供同 cell 全部角色使用。
adapter.packet 返回一个完整两三角之和的键，不伪造两个独立三角上界。

当前 high0 分支在返回 C_LH 前会先构造而不用整个 AL；新 adapter 按实际
分支直接构造 C_LH。defect 与 second-kind 同一次 parent pass 可以共享 AL；
它们若分属前后两阶段，则各自一次构造，不为缓存全部 parent 增加数 GB 常驻矩阵。

假设仍为1424 refined cells：旧三种非恒定角色每格四次请求 source；
high0 每次还多构造一个不用的 AL。新 defect pass 只需155个 AL，
通过后四源 pass 只需155个 AL 和155个 C_LH。这个计数是算法结构，
不是新的科学数值或运行时承诺。

## 3. 与现有 owner 的最少替换点

原 readonly admission、全部 native/candidate 身份、same320-bit exact
model chain、真实 h、refined-plan 构造、参考 chart 与节点表示保持。
新数学模块只加入新的 role，不替换原七个被绑定 module 的含义。
若旧 comparison-model 结论已成功，后继只消费其完整成功对象，不把它作为
新目标重报。

私有 carriers 没有公开数组可直接读取时，为新 moment 目标必须重新物化
同一个精确定义的内部表示。应明确记录这种必要内部工作，校验同一 model chain，
而不能写“没有数学计算”或声称旧 carrier 字节已恢复。它不产生第二条旧模型、
旧 norm、旧 endpoint 或旧 singular-value 结论。若有合法完整原私有表示可用，
先原样复用；不为避免物化另发布大数组。

替换仅涉及以下四段：

1. 原 make_packets(role) 的每 cell 调用改为 provider.packet(panel,role)，
   原 refined.PackedPackets.append 可直接接收同一个 IL/IR/OL/OR 结构。
2. defect 全部 packets 完成后，moment.prepare_shared_outputs 一次构造
   A/B/K，接 moment.complete_norm_with_shared_outputs 得完整 defect。
   保存同一完整 body upper、回读后再判 epsilon<1，门的意义不变。
3. 门通过才完整构造四源 packets；然后一次
   moment.complete_norms_with_shared_outputs 处理四源。它共享 J/right 流，
   每个角色的完整结果仍分别保存，四个 old role 顺序和真实源单位不变。
   原 green.actual_low_source_bound 的 body/gap、atom 和 second-kind
   identity 公式继续使用。
4. whole-point 阶段继续用原 refined.make_factor_provider 和
   local.whole_box_projection_bound；defect source covariances 消费新
   完整 PSD upper 的 IL/IR，输出 A/B 消费同一 shared 对象。
   新积分矩本身不授 whole-point transversality。

target计数只能计本次真正新完成的声明目标。若当前运行已成功某些 source，
新 owner 必须改为仅计算尚未完成或明确不同且有必要的比较目标，
不能把同一四源默认再跑一遍。当前结果未出，因此本说明不冻结 owner。

## 4. 原 atoms、两批流与 packing

当前完整递推中的 A/B/K 都和 source 无关。按旧顺序存入同一个
PackedMatrices，每 entry仍执行原 Arb 包含验证。
A0 和 Bm 是原准确零，初值不因未另读一个零球而改变。
Km 是完整 outer atom Gram，准备后立即读回 packed 值再向后传播，
与旧 complete_gram_norm_packed 相同。

J 原来以高精度矩阵直接传播，本接入继续如此，不为了复用而新增
binary64 rounding。一次 defect batch 与一次四源 batch共两次 J/right 流；
原来为五次。A/B/K 准备从五次降到一次。全部 root97（含mean）、
outer96（含Theta）和两三角仍各自完整。

严格比较 old/new 费用时，应分开：

- 相同矩阵的缓存/复用不会引入数学损失；
- GM矩积分改变 whole-cell 上界方式；
- 原已有 carrier/packed covariance rounding仍完整进入；
- 新source PSD majorant可能比旧entrywise方式松，也可能更有利；
- HS norm到operator norm的最后比较完全未改变。

不能将这些不同来源混称为“舍入改善”。

## 5. 明确的私有生命周期

shared 的 prefix 由 moment.prepare_shared_outputs 返回。
结果的 private_output_left_covariances / right_covariances 指向该同一 prefix。
新 norm 结果**没有**旧每-role private_storage_prefix；未来 owner 不能保留
旧的 packed_store.release(norm[private_storage_prefix])。

合法顺序是：

1. 全 defect packets；一次 shared A/B/K；完整 defect与严格门。
2. 若门 false，保存完整失败门后释放 provider parent、defect packets、shared。
3. 若门 true，provider.release_parent 后做四源 pass，以减少跨阶段大对象常驻。
4. 四源全部完整再同一 batch 汇总。保存每个角色结果后可以释放各自 IL/IR
   packets；shared 与 defect packets仍保留。
5. point receiver阶段结束、其全部 scalars已保存后，释放defect packets、
   source-covariance prefixes、shared["prefix"]，再释放原 output-packet和model区。

任意异常只保存完整小 scalar prefix 和真实失败信息。私有矩阵不发布。
不将失败角色已有部分packet当成一个完整范数。
释放动作只影响私有内存，不删除任何旧成功、旧失败或本次保存的 scalar。

## 6. 若当前完整 epsilon 未严格小于1：新门究竟改善什么

原四格积分先把整个 subbox 上的 OL/OR/IL/IR 各自变成矩阵球，
再形成 Gram 和两三角的非负 trace upper。它同时丢失：

- 单一时间参数在 exp(tH) 内部的相关性；
- 同格 causal 和矩形核之间的 signed cancellation；
- 积分量与逐点极大范围之间的差。

GM.3--8 对恒定 covariance准确积分；GM.5在最后取upper前保全部signed抵消。
对三种 varying sources，GM.14说明这个准确积分支配真实核，
所以它能形成一个真正不同的完整 epsilon upper。不是从旧epsilon取有利子项，
也不是缩小已付参数域。

但它**不会**缩窄当前 whole-parent coefficient packet。该包围按原逻辑不依赖
subbox，单纯把1424格加密或把4改成8不会改变actual coefficient uncertainty。
它也不会移除原mean、true-root宽度、node representation误差或HS损失。
若新的完整HS上界仍≥1，只说明这一比较配方未通过；
不能宣称 low算子奇异，更不能把未付 source/point/全逆门置真。

若原失败主要来自parent源球或不可避免的HS维数损失，后继应改进系数表示
或以不同完整 operator-norm certificate 代替HS充分条件；不能只反复细分相同球。
例如 differential storage inequality/完整Hamiltonian边值证书是不同数学目标，
需要完整新证明及boundary/atom条件，本说明不免费授予它。

## 7. 数值运行前后不混淆的计数

新moment阶段按 whole-cell moment 数量报告；不再把没有执行的“四个积分box”
作为完成计数。whole-point阶段仍有原每格四box，单独完整计数。
原success scalars只读，可复用其严格门，不把它们计成本次新目标。
新的 covariance normalization、Taylor尾和parent缓存统计是新目标内部元数据，
不另包装为新的“审核目标”。

只有公开 Actions 形成完整保存的bounds后，才能判断实际收缩是否改善。
本说明和adapter仅有AST检查，无科学导入、无数值调用、无新运行。
