# exact_closure：执行器更换后的未推包重做记录

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

约07:46 UTC，exec-server报 `executor key changed during session recovery`，新执行器看不到旧工作树。下面记的是中断前已由工具正式观察的结果；原未推文件已经不可见，必须重新生成，不能把本记录代作恢复的数据包。

## 已完成而须重做的真实区间计算

M8线性 session88489 正式exit0，2227个panel、221.412387773秒、峰67624KiB（含JSON输出）。同一实际新有理深g、physical node225→12、完整213胞元、实际8个保存binary高度定义线性参考。每个胞元都有逐模sup包围；不是端点代全段。

- 第一胞元 X 的log2上界为 -123.06689355334580768787009327737。
- 最大 X/R23半径比不超过2.9301277333290688e-11。
- 完整非线性源的胞元L1范数之和不超过1.2844878361679841e-51；完整mean保留。
- 原group gzip 1314429B，SHA256 `f1dff81b293b5b6085bc8825769875997bb89eb6898a6aca6582769b2692ecd0`。
- 原linear入口SHA256 `1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e`。
- 原projective helper SHA256 `45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97`。
- R26 source helper SHA256 `97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47`。
- 原4件v2源码JSON.gz归档17866B，SHA256 `84a865de3bcaacb2e268617092ca0f64923ad886a87e7912279d2f804fcad514`。

Green session82011 正式exit0，19.261253657秒、峰56376KiB。真实低窗Wronskian核把R23完整源的低频投影映回全部胞元强范数，得到

$$\eta\le3159843714651572576465137747092799057133187720535785487121\,2^{-200}<0.001966375571193024.$$

第一胞元响应X上界1.7653866394318422e-40，log2为-132.05713961103263。原R29半径1球的映射界0.007865502285、Lipschitz界0.01573100457，全部门已通过。直接代入R23还可取相对修正半径1/500，因为

$$\eta(501/500)^2<1/500,\qquad4\eta(501/500)<1.$$

这是线性R18远直线及固定8个浅高度下的辅助M8点态投影问题，完整mean由holonomy小根决定；不是原worker压缩Galerkin、真实非线性R18图或全频闭合。相应1/500独立ledger尚未在旧执行器落盘；重做时须写出精确dyadic检查。

重做命令（在课题目录，使用新的输出prefix）：

```sh
python computations/closure_real_linear_head_enclosure.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-ledger notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json \
  --response notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-response.json.gz \
  --out-prefix notes/2026-11-12-closure-real-linear-q003-m8-recovered \
  --modes 8 --reference-modes 8
python computations/closure_real_head_green_enclosure.py \
  --columns notes/2026-11-12-closure-real-linear-q003-m8-recovered.json.gz \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out-prefix notes/2026-11-12-closure-real-green-q003-m8-recovered
```

## 46列及运行失败

早期46列的独立坐标箱、普通投影商各有一次区间失败。保留det=1的单调Möbius方向后，session55710在全部213胞元/10225个panel传播完后正式exit1（904.000340975秒、58964KiB）；首次未排除浅高度零的是physical m48。此时23个低列的高度门已通过，但旧driver没有提前保存cell包。不能从它推断真实高度图有零点。

改进后的v2使用独立正端点和符号保存共同幅度，并在高度门之前写全部cell流。M8已经用这一版成功。46列v2 session73042在执行器更换时失联，没有观察到exit码或完成结果，必须整项重做。

新g强H的Node session19376（cache96/heap256）和46110（fresh cache8/heap256）都在ready之前收到signal9。后者有监控：wall133.233183974秒、user CPU11.535836秒、system CPU1.365639秒、RUSAGE child峰238920KiB，最后/proc VmHWM239416KiB；均没有trial或成功响应。原因未确定。固定g/H/原门不变；没有把私有缓存变更称作原因修复。

## 持续主线

我负责真实low46流/Green和j>46深trace的正比较流频带。tail代理负责完整头内非线性forcing的解析尺度闭合。任意L1_r W_tau源到同一固定tau的全频X并非有界，不能每轮固定丢strip后仍宣称同Banach空间收缩。移动strip或自然物理高度/一阶场范数的严格处理仍在推进。

所有恢复文件仍按当前新源码记录hash；若重建源码字节不等于旧hash，必须明确是重建版本，并重新计算相应数值。未推结果不能以仅有摘要代作已恢复数据。
