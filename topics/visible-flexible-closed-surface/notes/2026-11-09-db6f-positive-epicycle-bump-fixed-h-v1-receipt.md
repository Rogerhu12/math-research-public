# 正 C 固定 H 新稿：实际纯有理执行回执

2026-11-09；作者执行与闭来源记录，不是独立审查。

## 固定来源

- 正文：[ec5093a6d7c368dfaf80855d03c5c0f19ac51afe](https://github.com/Rogerhu12/math-research/blob/ec5093a6d7c368dfaf80855d03c5c0f19ac51afe/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-bump-fixed-h-v1.md)。
- Git blob：34ba5cd303512e203a22501db57b11dd4e844470。
- UTF-8 字节数：23577。
- 正文 SHA-256：7ea4f91fef4401f37dab9e8b4ba1228d7fe384ed70757df28bca912a157e083a。
- 正文末唯一 JavaScript 代码围栏：1,816 ASCII 字节；SHA-256：9c3f4d13f4e4ffe184806f3a9bc54bfa3e800f13cbfeec999e8ec2927948b351。
- 固定提交回读与作者保存的完整正文逐字相同；提取代码与作者保存的检查源逐字相同。

## 实际执行

在固定提交回读后，直接执行该代码围栏中的原字符串。
运行环境是 functions.exec 的 JavaScript/V8，不是终端；没有可声称的 shell exit code。
clock 工具开始与结束均实际返回 2026-11-09 23:10:47 UTC；
functions.exec 实际返回 Script completed，13 项全部 PASS，无异常。

| 检查 | 精确左端 | 精确右端 | 左端严格小于右端 |
|---|---:|---:|---|
| U upper | 10384982881/62500000000 | 17/100 | PASS |
| center norm | 199/125 | 8/5 | PASS |
| H distance squared | 81/16 | 13467/2500 | PASS |
| whole initial radius | 800001/500000 | 13/8 | PASS |
| H diameter fraction | 1/5 | 9/13 | PASS |
| normal tube margin | 2176/15625 | 1/5 | PASS |
| v difference coefficient | 28133/12500 | 3/1 | PASS |
| parameter chord squared | 102409/1 | 103041/1 | PASS |
| u second derivative | 34000069/500000 | 69/1 | PASS |
| full Hessian | 35000069/500000 | 71/1 | PASS |
| sqrt six majorant | 6/1 | 25/4 | PASS |
| sphere length majorant | 110/7 | 16/1 | PASS |
| nonstandard cone angle | 1/31250 | 6/1 | PASS |

代码只做 BigInt 有理数四则运算和比较。
没有几何数组、隐函数求解、PDE、BVP、tail、RK、网格或主优化数据。
这些 13 个门不能替代 Gram、同材料 H、空间嵌入、带边 reach、全 E(3)
或混合能量定理的全文证明。此处没有计入未参与者独跑。

## 依赖状态及冻结边界

正文保持原样不追改。正文冻结时，单调 Q 稿 9daa8aba8a341855811d2f1c164bfb3ca7eab0bc
尚在独审，故 §9 如实写成依赖该固定定理的条件结论。
此后收到未参与者完整审查接受记录 15b02049c367e344901fb13264a950f8ff5bf933，
路径 notes/2026-11-09-db6f-tail-review-monotone-flat-collar-smooth-data-v1.md，
blob 13a91fb1a309840fb4bc341c761e8914518548ff。
这不自动替代本文固定 H 实例自己的全文独审，后者仍待完成。

新实例仍是两条边界的环带。没有闭曲面、指定外部接口、有效 0.05D 像幅度
或全时间 0.03D reach，也不支付主 flat17 的 G5。
