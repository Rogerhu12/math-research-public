# 固定新 g 的实际 depth12/far225 延长

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

## 实际结果

受 root 的大作业串行安排，tail 在05:25:32 UTC完成正式求解和短谱并释放 worker 后，本次使用独占窗口运行

```sh
python computations/closure_scaled_endpoint_replay.py \
  --input notes/2026-11-12-closure-rational-q003-m8-d8-s16-l1024-response.json.gz \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --out-prefix notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive \
  --depth 12 --linear-far 225 --node-heap 768
```

exec session96326已经工具确认 `exit0`。初始化75.39秒，全程119.72秒；child峰值RSS390468KiB。完整响应压缩包93261字节。窗口已立即交还 root，没有继续并行启动下一大作业。

旧289个 shooting 节点由 depth-only adapter 逐值保留，144个新增节点只作线性初猜，随后运行原完整非线性求解。实际 history 为

$$0.020405071484944456\longrightarrow2.1825665269857528\times10^{-11}.$$

即完成一次 Newton。早先消息里“无需新 Newton”的口头判断已经更正，不能以最终残差恰等于旧浅段主导残差来推断未执行 Newton。

完整有限 audit：metric $4.44780320613701\times10^{-15}$；full Darboux defect $2.317353333882727\times10^{-17}$；holonomy $3.360524636073244\times10^{-21}$；leading minimum $0.9937826803363398$，$D$ minimum $0.9999966889251244$。

同一固定 g、同一浅端有限高度多项式，depth8到depth12的 cut 数据变化为：非均值高度0，slope最大 $3.3881317890172014\times10^{-21}$，second最大 $2.6469779601696886\times10^{-23}$，两个 mean correction 都未变。以保存的共同 cut 背景计算的有限谱物理梯度差上界为 $3.3778446525835578\times10^{-21}$，协变 Hessian Frobenius差上界为 $3.37784316058531\times10^{-20}$。它们仍是浮点有限谱比较。

## 实际 canonical 端迹和 strip 诊断

实际 physical node12 的半径为浮点 $0.05002889966825686$，$w=1.0072314093684093\times10^{-11}$。第一模数据为

$$Q_2=-2.2863945785201636\times10^{-41},\qquad
\Xi_2=5.706585942679951\times10^{-40}.$$

这里 $\Xi$ 已由完整 finite root 按真实 physical canonical 公式转换；checkpoint 原 momentum 是 $\Pi$。本次二者差在浮点层逐项为0，不宣称实数层数学相等，mean correction输出0也具有同样限制。

实际端点后接未认证线性延拓所得保留 M8 低高度标签：

| 绝对远端角宽 | $\log_2\ell^1$ | 到R18图域 $2^{-1947}$ 的数值bit余量 |
| --- | ---: | ---: |
| $(\log2)/4$ | -2341.334660575594 | 394.334660575594 |
| 1 | -2338.949270493816 | 391.949270493816 |
| 8 | -2318.751539921371 | 371.751539921371 |
| 80 | -2111.003454033360 | 164.003454033360 |
| 96 | -2064.837212724913 | 117.837212724913 |
| 128 | -1972.504730108019 | 25.504730108019 |

这些量不包含未保留的低9–46模，也不包络真实源积分、数值径向积分或从node12到真深图的非线性校正。不能仅凭余量宣布 R18 真 trace 已匹配。

## 源参数核销与语义

新 ready 包读取全部160个原 source cell 的参数，不重新求校准根。精确分数账本已对148个相关胞元及全部适用配置核销；见
`notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json`。
R22/R23的有限参数范围条件现在已支付，真实源积分误差仍单列。

worker source 参数表、成功后的 canonical 转换、strip诊断都只增添输出；accepted-trial callback只存恢复点，保留原下一轮Jacobian与success gate。运行时文件hash保存于ready和
`notes/2026-11-12-closure-scaled-endpoint-runtime-manifest.json`。

本次可完成的结论是同一固定新g的真实有限深度延长和源参数核销。完整无限尾匹配、全频浅头校正与最终前缀联解继续依赖 R18/R22/R23所列准确接口，不能把有限Robin延长称为精确闭合。
