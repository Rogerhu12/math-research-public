# 完整背景、有限包组装和全尾 consumer：独立审查与全量重放

2026-11-09，Astra-visible-flex-db6f0b0e/root。**PASS，限于下列绑定对象。** root 未实现这里被审的 primitive、producer、overlay、w_r 继承或 consumer；各方法先经独立审读，再以新的输出文件完整重跑。数组仅留本地文件并经终端 git 传输，没有复制到对话。

本稿补充早期 primitive 与 producer 试算审稿，不覆盖它们的历史文件或哈希。冻结数学供应方法仍是原来已通过审查的版本；这次把其重放范围扩大到真正用于全尾证书的有限计划。

## 1. 完整18个原函数 profile

作者 `db6f-tail-background-primitive-stable-depth2.json.gz` 与 root `db6f-root-review-background-primitive-stable-depth2.json.gz` 逐字段比较：所有物理参数、紧 alpha 包、输入 hash、数学源 hash、全部18个 profile 和每个叶完全相同。唯一变化是 settings.out 和耗时。

覆盖恰为 raw cell 0、1 的各9个 segment，含8,451个解析叶与420个直接范围叶。stable source 的代数等价性已有 independent_geometry 的独立审查；primitive 的部分积分余项、双向强锚、条件逆像语义由 root 早期全文审稿支付。完整重放没有把近似逆解当成证明，也没有改变 source calibration。

## 2. 全域生产计划逐项重放

root 对 strict prefix 的 spans [0,4423) 重新运行最终 producer，得到4,999行。与作者保留 shard 中相同选区的全部数组逐元素相等，包括物理局部坐标、w/w_r 系数、余项及诊断字段。作者另外的 collar 行与已审 coarse collar 在精确零补高次槽后完全相同。

原全域 strict 运行被中断的事实仍保留；其5000行保存 shard 只声称 collar 加上这些完整 span。retainer 已由另一审查者逐字段重放，不因 `finished` 字段而把未完成余域算入。

随后 root 使用自己的完整 primitive 重跑实际采用的4个 suffix 计划：

| 物理 span | 最大细分深度 | 行数 | 重放结果 |
|---|---:|---:|---|
| [4423,4637) | 0 | 214 | 全部数组相同 |
| [4567,4572) | 2 | 20 | 全部数组相同 |
| [4568,4569) | 3 | 8 | 全部数组相同 |
| [4571,4572) | 3 | 8 | 全部数组相同 |

producer 最终代码 SHA256 为 `75ef3b0426f31926d2e529d18f3b57beda8bc40fdca0cf7f9c26bf33442db1b7`。其已审包含性不依赖工作容差达标；达到最大深度后的宽包仍有效，只可能无法通过下游实际误差门。所有这一类诊断保留，没有删掉未达工作宽度行。

完整独立命令和每组输入/输出 hash 见 `db6f-root-review-final-background-replay.json`；可执行复现器为 `scripts/db6f-root-replay-final-background.py`。早期统一窄 w_r 容差的 suffix 重放曾中断，另有 interruption 记录，未冒充本次有限计划。

## 3. overlay 的数学与代码审查

冻结 `scripts/db6f-audit-overlay-tail-packet.py` SHA256 为 `87218edf0b73b6e67dae3c58a618841601dc64b093b24519820bcfd63efca839`。

两输入必须 finished，数据 hash 实际核验；有限 map manifest 及 checkpoint、calibration、cell0 A、inner A、outer B 的源绑定相同。fine 的每个选中 span 必须从局部0到1、严格递增、相邻端点逐位相等，因而该整个 span 可由 fine 代替 coarse。

程序只删除 coarse 中已被完整 fine 覆盖的 span，保留其余行；给不足的多项式次数补精确零；拼接后按 span 和局部左端排序。若原 coarse 已全域覆盖，各 fine 已完整覆盖所选 span，则这些操作保持全域点值包含性。补零没有数值拟合或重新舍入系数。正式 consumer 另对最终全域 partition 重验，因此没有仅信任此 helper 的 finished 标志。

当前所有 overlay NPZ 均小于1MB，故此绑定运行符合仓库压缩要求；helper 的一般5MB拒绝条件不是今后免除1MB以上 gzip 规则的许可。

## 4. 继承 coarse w_r 的数学与代码审查

冻结 `scripts/db6f-audit-tail-inherit-coarse-wr.py` SHA256 为 `718ae3b47154083cf0c5a17fd65cea6dad25b4440fd8e31d1dbcad1ba9748f1e`。

源和有限 map 的五项绑定同上。coarse 必须每原 span 恰有一个 [0,1] 行，且 w_r 高次幂槽全部精确为零；重复 coarse span 明确拒绝。每个选中 fine 行严格满足 $0\le u_l<u_r\le1$，并有同一原 span 的 coarse 所有者。

若已证明 $w_r(r)\in[c_-,c_+]+[-R,R]$ 在整个原 span 成立，它自然也在任一 fine 子盒成立。程序将 fine 的 w_r 多项式高次槽置精确零，把常数端点及其余项原样复制；w 的全部系数、余项和所有物理坐标不动。这不要求新的 w_r 区间是旧 fine 区间的子集，只要求两个供应器包围同一精确背景。

供应多项式在 consumer 中只用于点值，二者不要求互为保存多项式的导数，因此这种独立替换有效。root 已逐行审读 helper，未发现本次绑定输入的数学缺口。

## 5. 最终数组及完整 consumer 重放

root 从已审 coarse 包开始，依次叠加自己重跑的 prefix 和4个 suffix 计划，再对 spans>=4423 继承 coarse w_r。得到 `db6f-root-review-final-reconstructed-packet.json`，共5,237行；所有最终数组与作者 `db6f-audit-tail-tight-final-packet.json` **逐元素完全相同**。同一复现器自动作了这一比较，另外的 `db6f-root-verify-full-replays.py` 又独立读文件核验。

root 还用另一次独立重建的 inherited packet 完整运行 consumer，输入同一个4637跨精确有限尾，角分割128、径向分割1、直接曲率触发阈值8.5。它对全部 collar 和有限跨的5,237行结果与作者逐项相同，所有数学报告字段也相同：

- 相对 metric 算子上界：`9.968938237875866e-7`；
- 实际主曲率绝对值上界：`8.46544537300005`；
- 全部盒的曲率均已解决，10盒走直接曲率路线；
- 全部行数据的 SHA256：`46702bb0f50d99a0dfc728b669e726c942cdd6791751587a83ccb2d263baba83`。

source、后端及所有作者/复跑文件 hash 和逐项比较结果在 `db6f-root-review-full-tail-replays.json`。数值界解释为保存的向外 binary64 数；精确阈值 Fraction 比较及全闭图组合另由汇总脚本完成。

## 6. 精确范围

这次完整重放支付真正用于当前 M8 全尾证书的 primitive、生产计划、组装和 consumer。它不替代上游解析背景证明，不替代 R17 的完整闭图和固定帽证明，也不由“数组相同”单独推出算法数学正确；各方法审稿与本稿共同构成证据链。

它没有生成新的非线性源解，没有证明无限 Fourier/无限尾的精确等距解存在，没有完成 README 第5项或网格交付。R18 可引用这些已审组件与全量重放，严格范围仍为当前明确有限闭近似族的全域几何和误差阈值。
