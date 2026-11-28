# 新真实 λ=.002 前缀：M16 原尾在温和幅度处返回，随即续完整 M24

## 真正返回了什么

来源仍为本会话新恢复的 λ=.002/M24、879 节点完整原门前缀；source run SHA 为 `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`。本次没有把历史 M16 失败包当成初值，也没有重算已接受的 M8/M12 请求：从新真实 M12/N256 接受包 `ccba27ff6af8686f24197591e9314fedf96f15ebfdb431971a5616ad573f296c` 的完整 1153 行状态继续。

2026-11-28，C 段在 **M16、N256、f=.5** 返回原 worker 完整接受响应，程序正常 exit 0。这里 `H_j(f)=H_j f^(j+1)`，并非把所有模一律乘 .5。实际请求保原 audit，未请求最终完整 height-jet Jacobian；原求解器末轮仍重新支付 fresh-final-J。所有深度 8、16 个 shooting parts、1152 段、16 RK/audit steps、原残差阈值 `2e-9`、原根分支与投影门不变。

| 实际输出 | 值 |
|---|---:|
| 原残差 | 1.0313974716235569e-9 |
| audit actualMetric | 3.3410281097491495e-15 |
| audit fullD | 2.6663741668865455e-11 |
| audit normalizedFullDefect | 7.279247166583977e-10 |
| audit minLeading | .8200817643208473 |
| audit minD | .9995941334989235 |
| audit formalCurvature | 8.148045697357949 |
| audit maxPhysicalPV | .00016154923195029508 |
| audit holonomy | 2.2701012382007283e-18 |

真正接受包为 `tail-mild-modes-20261128-c/m16/tail_0001.json.gz`，SHA `07981819451ea4d2f48c69f39f7d5c43d3039899915c7c9d5e62fd8bbcda05c3`；自身 native manifest SHA 为 `4a3d1b39d7b145650db58e2afd59447ff041bc97b487187f6726e3437ec03bd5`。完整原场、checkpoint 和原所有 native 记录继续留在仓外；小 JSON 绑定实际路径/哈希。

## 无损交接已实际继续

C 的退出是请求的“在真 M16 接受后释放资源”边界，不是任务结束。D 段已经从此接受包开始 **M24/N512 原 native2**，输出目录 `tail-mild-modes-20261128-d`，真实初值的 SHA 与上述接受包一致。接下来的原完整维数幅度序列为 `.5,.625,.75,.875,.9375,1`，最终 f=1 才要求完整原 H 与原 full height J。D 没有接入另行测量中的六处 inv_nq 优化候选；活原二进制未修改。

本条只新增原尾温和升模 M16 成功的有限事实。它没有完成 full-H、actual outer prefix–tail coupling、共同度量精化、完整闭图 C²/metric/reach 或本课题完成标准；这些工作继续由真实后继执行。
