# B030：保留实际 native H、补完 2,561 区间、按原恢复阶段续算

**状态：具体新科学范围与实现说明；尚不声称后继已执行。** 来源是 [native d191 的真实终态收据](2026-11-27-r566-native-d191-natural-final-agent.md)，run `45914886940` / job `140231615166`。新范围消费实际 q56594、原剩队列、真实 packed LDL/pending 和原完整费用；不重建或补写没有输出的完整 native workspace。

## 1. 原末态与这次必要工作

原保留 81q 的 SHA-256 为 `56594ecb1d8d94cd8463359dc2e40b4a681be6a4588296d63ae3eda3a240c7f3`，实际 eta `0.20868474226441153`。完整 coarse/fine 半径数 804/1610，FFT 1536/3072，物理峰轨道 1793，working 行 277；两类 pending 均空。原实际 trust `0.45050811767578125`，最后 trust 决定未完成；本范围保这个已采用值。

最终候选是另一真实 q，SHA `53ed9bb6db3208246487553d2061ab4e61baaf1ba4b2159332a5686249f0dbba`，原阶段 `geometry_restoration`，实际辅助量 e=0。它的原 complete-coarse、1610×3072 fine、nested 比较和原网格峰证据已支付；原 12013 个角向候选仅完成 9452 个，剩 2561 个。新范围首先用冻结的 `localize_saved_brackets` 原四点轨道目标完成**这 2561 个原区间**，合并全部 9452 个已付峰；不重枚举候选，不重播 paid prefix，不另做旧 coarse/fine/nested 前门。

重建原 oracle 和同 q 的必要 FFT 状态是新工作，完整计入本次 OracleLedger/elapsed。保留点原 fine 身份已等于当前 fine，不重查旧 baseline。只有出现新真实候选、原物理库增添原行或真正阶段切换时，才按原程序支付必要新行、J 和资格。

## 2. 原恢复阶段的完整接受关系

设原工作容差为 `tol`，实际完整几何余量违反为 `gtrial`。原 fine scan 与全部旧/新角峰仍按 `fine_geometry_limits(scan,margin)` 和原 `observation_metrics` 合并；原物理几何违反与余量违反分别保留。没有用物理违反 0 替换工作余量。

这条原候选必须同时满足：原 working/box/complete-coarse 已付门通过，原 nested 门通过，原角向队列完整闭合，`gtrial <= e+tol`，以及没有原阶段下超容差的新几何峰。Phase I 的 metric 行按原程序不活跃，不能把 metric 峰误当恢复阶段违规行，也不能给 e 添加一次 metric eta lift。

在以上原门之后，保留原接受式：

$$
g_{\rm trial}<\operatorname{RN}_{64}(g_{\rm old}-10^{-10}),
$$

或原成功恢复分支

$$
g_{\rm trial}\le {\rm tol},\qquad
V_{\rm physical}\le {\rm tol}.
$$

后一分支不要求 eta 下降。原待候选的已付 eta 网格读数 `0.20921002233215497` 略高于保留点，不能据此把真正成功的几何恢复错判为失败。只在完整队列已经闭合后运用上述接受式。

原部分返回之前已经把原网格违规证据合并到 pending；两类 pending 为空，且本次不改变 q、e、网格和阶段。因此只需合并新闭合角峰产生的新证据，不重新扫描旧网格。所有新几何违规坐标进入完整 physical pending，最坏原行进入 working 提案；工作矩阵的选择不删除任何完整物理门。

若补完后真正恢复成功，保留新完整 fine 资格，同时令 `current_complete_library_values_known=false`，让原 outer 流程启动必要的 metric 行选择。原 Phase-I coarse 资格没有评价活跃 metric 行，不能拿它为新 metric 矩阵免付费。相同 q 的旧 fine/nested 仍已付，不因此再跑一遍。

## 3. 未输出 best_geo 的准确处理

原 outer 8 已接受 fine 的准确余量为

`g_fine = 0.0004748151855263885`。

原 outer 9 coarse 重选执行 `best_geo=max(best_geo,-geometry_min)`，然后输出

`e = 0.010474815185526721 = RN64(best_geo + float(.01))`。

原输出没有单独保存新的 `geometry_min` 或 `best_geo`。**本范围不把 `e-.01` 当成原 exact best_geo，不支付旧 coarse 重播来弥补记录。** 它保留所有与已保存事实相容的原 binary64 值。

令 `c=float(.01)`，`e-` 和 `e+` 是 e 的相邻 binary64 数。按原 binary64 round-to-nearest/ties-to-even 加法，可能的准确实数和满足

$$
\frac{e_-+e}{2}\ \leqslant\ g+c\ \leqslant\ \frac{e+e_+}{2}.
$$

两端同时包含当且仅当 e 的 significand 最低位为偶；否则两端均不包含。减去准确 binary64 c，再与 `g>=g_fine` 相交，最后只保留区间内的 binary64 g。源码以 `Fraction` 保存准确有理中点，用 `math.nextafter` 向内找到首末 binary64 值。这里 g 为正数，因此有序 bit 编号也可准确记录可能值个数；没有扩张到负数或负零语义。

这个集合恰是一个有限、有序、连续的 binary64 段，不是关于连续几何误差的区间证书。函数

`g -> (gtrial < float(g - float(1e-10)))`

在这个序列上单调。因此对两个准确端点执行**原浮点减法与原严格比较**：两端一致，就等于所有可能原 g 的决定；两端不一致，保留真实未决状态、已闭队列和完整费用，明确输出 `original_missing_best_geo_comparison_undetermined`，不捏造一个 g，也不追加旧模型探针。

若原成功恢复分支成立，它本来就不依赖旧 g，直接照原分支接受。新完整接受后，原程序已经给出新的准确 binary64 `max(0,gtrial)`，状态变成单点。以后若原真实新 coarse 得到 a，则可能状态按原 `max(g,a)` 映射；其准确像仍是区间，端点分别 `max(lower,a)`、`max(upper,a)`。若 a 超过旧上端，就成为准确单点。原新 e 只在两端的原 `float(g+.01)` 一致时采用；否则保未决，不替换原算法。

helper 本地没有执行。以上准确中点、binary64 端点与可能值数的**实际数值**只在新公开科学进程、同一科学时钟内形成；首次恢复次数和时间单列，后续操作计入 elapsed。所有新 FINAL 都输出完整 `actual_retained_geometry_margin_state`，不会继续遗失这个必要标量的身份。

## 4. 真正继承的 H 与原模型身份

新 driver 把原 FINAL 的 `actual_curvature_checkpoint` 直接交给冻结 `TrueSecantSLSQP(...,checkpoint=...)`。其完整规范 JSON 为 74980 B / `f499980ad5de37b29a7b80263978e07df31d012c41e5d01a1ac06f90119dfd4e`，packed LDL 为 3403 doubles / SHA `ba6108794907e6f72be0c683d0752e6f657ac60ec394ad07b99acee6babc49d7`，pending 含 82 维真实 QP anchor、82 维真实固定乘子梯度和两条准确非零乘子行。

原模型字典保持相同：B030 81q 加一个 epigraph，原目标、原几何/metric 行函数源、原参数和 FFT、实际阶段共同确定 row function signature。q 在静态设计中变化，原 mean-E metric recipe 也随 q 变化；**没有固定一个新的 g**。工作行子集可变，但原 pending 中每条非零乘子对应行必须存在才更新；没有阈值省去小非零乘子。所需行缺失则按原 helper 跳过该 secant，保已有有限 H。

原 native MODE -1 已消费过的 secant 不能在外部再用一次；冻结 helper 保留这一不变量。H 只初始化新 backend 第一次原 QP，后续原 RESET_BFGS/I 逻辑不变。发生几何恢复到 metric 的真实语义切换时，原 signature 检查会 reset I，不能把不同阶段的梯度差合为同一模型 secant。

所以“恢复实际 H checkpoint”不等于承诺第一次新 QP 必定使用该 H：若剩余队列完成后直接转入 metric，正确行为就是依原签名重置。完整旧 native workspace 和完整 J 没保存；本次必要的重建/新 J 照常计费，不伪称 backend 在内存中续跑，也不重播旧 J 当诊断。

## 5. 具体文件、范围与成本

冻结科学源及接口：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `scripts/r566_native56594_partial2561_20261127.py` | 66583 | `c972c56133ff68705a91434d5ceeb404d5d7fe818d2cf168e2ac2b29efdfa09a` |
| `scripts/r566_original_margin_rounding_state_20261127.py` | 5781 | `ee963a595d611484b2459a51ed7ae0d702e18a0900f8c01d5e95f4d80c7b0491` |
| `scripts/run_inverse_state_gzip_stdin_20261127.py` | 12451 | `7126c56546b42b6a437271cb373d111e0164ec5f0bf583b4083917fa7e624d29` |
| `.github/workflows/visible-r566-native56594-partial2561-20261127.yml` | 6405 | `65a5a81ecae382c15331e84390afe13991290a08460c17c8d10a6bed5751a371` |

Request 为 `computations/request-r566-native56594-partial2561-20261127.json.gz`。它包含真正必要的原 FINAL 文本和 9452 个已付峰，没有整份 stdout，也没有编译二进制或旧完整 J。原科学 stdin 是 2474647 B / SHA `18ef8fbe552aaa514f28d27033e445c5b89d8ef9a22b36e5a77f357be23fc564`；首生成 request decoded JSON 为 2746505 B / SHA `1048c95fd2a7c4cf198256ccc11ebdbee5c1c7287bb81a164991ed62daa536a1`，gzip 为 441560 B / SHA `a89bb1b8886576345ef7bca4f82fd6ff8b32ba257093b719446db3e9e567d884`。发布前若仅更新已实际读取的规则 commit 元数据，request 字节/SHA 随之更新，科学 stdin 与上述科学源不变，以实际 Actions `INVERSE_ACTIONS_SOURCE` 为准。

gzip 使用单个 `.gz` 与 mtime=0；不是分块文件，也不是把可重算日志压缩后存储。新 stdlib runner 仅相对原 stdin runner 增加 gzip 解码及压缩/解码两层字节身份；public/private pull、根与题 README 差异检查、原 source pin、私库 QUEUE、绑定检查、凭证在科学前移除和 stdin 传递完全沿用。解码只在内存，不另建科学输入临时文件。

全部 20 个原 common parameters 保持原值：radial base 49，outer 120，maxiter 80，完整 coarse 上限 1025，物理峰轨道上限 2048，working 上限 1024，批 512，direction block 16，point batch 64，working radial batch 24，每字段 witness 6；角容差 `1e-10`，near band `.002`，pending peak `1e-8`，nested `1e-7`；trust 范围 `[.00390625,4]`、working backtrack 16；科学总范围 2400 s，末预留 30 s。新进程沿源实际 trust，没有额外放大。公开 job 50 min，单并发、`cancel-in-progress=false`。

时间与所有失败/未闭工作沿原 ledger：源已付 2370.546518149 s，之前已记录下界 17099.551640495 s；此前未记录部分仍未知。新剩区间只计本次新 evaluations/elapsed，9452 的旧 83830 calls/440.78279974299994 s 单独保源身份，不能作为本次新完成重复收费。必要 oracle/FFT、所有新完整 working J、官方 native source fetch/编译/import、H 的新线性代数和 optimizer 全计本次科学 elapsed；完整旧 cost 对象不裁剪。

原局部优化器、物理盒、粗细所有原行、角向四点轨道目标、原余量、nested 门和真实 raw/best 分离不变。已付 11 份 J 未保存矩阵，后继仅在真实需要组装当前 J 时计新成本，不追加方向/奇偶/限制映射探针。当前源码准备只做文本、AST、JSON、hash 与原完成日志解析，没有本地执行科学 helper、构建 native 或调用模型。
