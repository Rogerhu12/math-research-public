# R582：原390链自然到真实4354，并保留尚未闭 fine 的 c13d 半步

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

原运行自然结束后读取其唯一 FINAL。run46125750420 /
job140919842900，源码4482fcc2f767581c9b0e09ff0b086c08a204038e；
job08:25:33–09:05:45 UTC，run于09:05:46自然 success。
科学 termination 仍是 scientific_clock_checkpoint_not_complete；
新实际科学耗时2370.2626640790004秒，没有把 runner success 当作科学完成。

## 来源及实际规则读取

- 原完整 log：5411637 B，SHA256
  f3e996d31dd6157693392ac89d531f948637a4281c8434a1d140a488c1616eaa。
- 原唯一 FINAL JSON：505464 B，SHA256
  a3dc4b6162bbe1849da3ba6356a20a5a74d768ba0147e661eac28053ed1dbf92。
- 原入口 r582_6e91_original390_resume_20261128.py：
  8992 B，SHA256
  0b0bce610865bb44c892b8b3e847553bf84d528fb0c37276f2e342963a12be3b。
- 原科学 stdin：
  a21bc8e922a79c0831fc9f5f06adae95bc489c739a349993aec9193a2f8f4045。
- runtime于08:25:56实际 public pull到
  9910862b6df38654003e653bb7a02e9421d9d29d，两README diff均为空；
  08:26:00实际 private pull到
  b320d90e10497cf2dadee5c9d89fce3de39e720b，根规则未变、QUEUE仍本会话。

原科学源及接受代码未变。原三内口比较、24/48/96 fit、已付方向检查及
七点诊断均未重放；旧拒 a938 也未作为另一次独立扫描重做。

## 真正已接受的当前态

新增6次完整 metric 接受。最后实际97q为
4354ee43ae0a98bbffac485c27f826b82507acd18d999a9cf4534cbda430c9f5。
p=.181、stage0、metric phase、trust2不变。原390运行的新材料网格（62878个 Hermite 端点）为
f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c。
上一6e91来源的材料网格为 0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991。

原390 coarse在完整优化中发现并加入11个缺失径向峰，当前已经构造和使用
401×1536 coarse；fine从16296扩到16312×3072，所有旧fine点保留。
当前pending为0，无角升级或角升级证据。准确身份：

- coarse401：
  04650f567de37017689535096d75f1e6b68cb48970dc6022c5688b6b7565145a。
- fine16312：
  bc08a5b4a84ab1af1b688a2e117da65d3efc3b5e1de0cc12c37994e71e7a5692。

最后真实4354在完整fine上的结果：

| 量 | 实际值 |
|---|---:|
| η最大值 | 3.266724887865865e−5 |
| η取得点(s,θ) | (.4647216796875, 2.955469651326335) |
| 原物理几何违反 | 0 |
| 带工作余量几何违反 | 4.56012918398363e−12 |
| 工作违反组 | curvature_minus |
| 样本球半径最大值 | .7800891227055584 |
| 样本 abs(y)最大值 | .3925874148916422 |
| 样本绝对主曲率最大值 | 16.452569170035574 |
| 曲率取得点(s,θ) | (.8715482369363079, 0) |
| det最小值 | .6296034508812749 |
| mean E范围 | [.6296172452765353, 1.175983017500729] |
| z最小值 / 面积最小值 | .02 / .21999999999999997 |

以上是该同态完整有限网的实际观察。尚未给其连续reach，也不能借旧59a4
的几何资格。当前mean仍是设计变量，完整固定g族和宏观比例未达标。

九次完整 callback fine中6次接受依次为：

| q短名 | η | 工作几何违反 | 结果 |
|---|---:|---:|---|
| f8f747a1 | 3.2994052756807335e−5 | 8.815703635839389e−11 | 接受 |
| 84440877 | 3.294767066830406e−5 | 4.3915092916291254e−11 | 接受 |
| b42b4850 | 3.292667770904423e−5 | 2.0968892421036056e−11 | 接受 |
| a232391f | 3.2904771152475476e−5 | 1.0667577064749079e−11 | 接受 |
| 851287af | 3.285451593415534e−5 | 9.73242709747732e−8 | 拒绝：fine工作几何 |
| e9d8e6bd | 3.271285345822014e−5 | 8.826605245315644e−12 | 接受 |
| 26646ddc | 3.2748048274889436e−5 | 0 | 拒绝：没有metric改进 |
| 36c4fdd1 | 3.289595922395527e−5 | 0 | 拒绝：没有metric改进 |
| 4354ee43 | 3.266724887865865e−5 | 4.56012918398363e−12 | 接受 |

这九个均是原raw回调相对当时真实best的二分之一物理步；独立epigraph
提升不改变它们的物理q。表中fine未接纳态不被写成接受态。

## 自然截止时正在检查的真实 c13d 不能丢弃

最后raw后端q是
df3e0b3b152f3db73ff492c4457981d2a4cedd99034c5159fa32c2140c5770a9，
extra=3.257474306230681e−5。其当前完整coarse行违反为
9.721249702400112e−8，所以raw本身并不合格。

原callback已经真实走到二分之一物理步：

q_half = q_4354 + .5 (q_raw − q_4354)。

按原binary64运算重构该97q，得到与原FINAL完全一致的
c13d4621694b8374853c1b50cf11b399c7e6b4e3c64fe675f1ff3468f5eac9c8。
其原完整coarse物理/完整lifted行违反均为1.908916601178756e−12，
box违反0；原epigraph为3.258807336041912e−5，
相对raw已真实提升1.3330298112308042e−8。
这个上界低于当前best的fine η，因而原算法确实进入它的完整fine资格。

它未完成fine，也未接受。不能因为时钟截止把它当已拒路线，更不能把它
当已有fullfine资格的状态。在继承的原 warm initializer 槽中可放这个准确
未闭 trial，使原callback在新optimizer之前完成它的实际fine资格；
它的身份明确为 separate physical half-step，不冒充上一轮raw。

## 未完fine的115块没有可复用prefix证据

已读冻结 r582_physical_epigraph_continuation_20261127.py 的
FineObserver.scan、callback及snapshot路径。scan仅在局部变量中积累
fields、eta_parts、report、attainers及NormAccumulator。它每块收费，
却没有逐块emit或持久化prefix；只在完整返回后才能形成scan及峰数组。
snapshot没有这个局部扫描状态。

原log只有2个完整baseline及9个完整callback scan：
9次16296点、2次16312点，共179288径向点、1408块。
最终计数是194008径向点、1523块，差额准确为：

- c13d已计算但未保存可复用统计的115块；
- 每块128点，共14720径向点；
- 当前目标fine16312点，尚余1592点未读；
- prefix的实际values/行峰/角峰/范数累积均未保存。

因此仅有计数不足以把下一次1592点拼成完整资格。不能虚构prefix summary。
为完成这个真实trial，需要新的完整16312点pass；此前115块仍是已付费用，
后继重读部分是缺少已保存科学值造成的必要损失，必须如实收费。
原4354同p/q/grid的完整fine证据则仍在FINAL，原baseline可直接复用，
不为独审再次扫描它。

## 全部新费用及未fold费用

| 费用 | 已记录 |
|---|---:|
| 科学实际秒 | 2370.2626640790004 |
| 完成outer中的完整J / 方向块 / values | 8 / 104 / 72 |
| 当前未完成outer、尚未fold的J / 方向块 / values | 2 / 26 / 10 |
| 完整fine scans | 11 |
| 全部fine块（含未完） | 1523 |
| 全部fine径向点（含未完） | 194008 |
| 全部完整coarse callback行检查 | 11 |
| 已完成callback fine | 9 |
| 新physical回溯行检查 | 37 |
| 精确lifted物理候选 | 10 |
| 已走物理halving次数 | 10 |
| 无严格metric希望的coarse合格评估 | 25 |
| 因原coarse物理/metric希望未过而跳过fine | 1 |

新geometry AD blocks130，value calls1553；请求parameter-direction points
584346624、spatial points692379648，模型新准备径向点33399。
R604观察595992576个径向角点、194008参考径向点，直接复用1523个
geometry块；这些计数互有包含，不能再当不相交科学开销相加。

实际新材料再生仍收费：dense tail RHS960932、160段/1 transfer，
core forward RHS2510、short backward RHS206、Hermite端点62878；
235893个height QUADPACK RHS。未保存的完整材料数组和SLSQP/BFGS/J
工作数组均没有伪称恢复。原祖先所有费用仍随同一冻结输入链保留。

下一原401 scope保持p目标.8、末η≤1e−7、当前阶段约2.5e−7，
不改变原物理/metric接受门。先处理真实c13d余资格，再继续原正常优化。
