# 一般 Phi=0 紧凑两均值输入的真实 SIGALRM 冻结记录

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 原输入与实际结果

本次是已冻结源
[2026-11-27-unit211-Phi-zero-general-compact-scalar-means-original-input-8542.py](2026-11-27-unit211-Phi-zero-general-compact-scalar-means-original-input-8542.py)
的唯一首次执行。它在 $\lambda,x,y$ 参数的首一二次 $\rho$ 代数中，只用原 $P_{f,1}$、$L_{\mathrm{num}}$ 两个显名几何分母代入紧凑标量均值，未组装前次 ed0 失败的统一 Gram。

- 源 blob：`da72af76c34d79121c5e03ad12a0f3bbb6bf1796`。
- 源 SHA256：`879168b21528a5adebebac3b16f75d2096236f4f54032ea45e5d7b397cbe00b1`。
- 实际 run/job：46022929932 / 140586912947。
- 实际 source commit：`968dae1ec89a5d5526a3ed6ebfac88bf18e09b00`。
- 内层退出码 **−14，SIGALRM**；120.067181546 秒；816684 KiB。
- stdout：524 字节；SHA256 `2c29e7a0f7f05d1545dc45bd19bb0f6f01e1f8e369894d76e9eca3ef216145f2`。
- 执行前真实 pull 后根及课题 README blob 均未变化。

最后完整数学段在 4.491162642 秒：原 P1 与 $N(V)$ 的两条同源线性恢复已乘回，78 次二次商乘法、234 个原差系数身份。此后没有任何完整 $R_2$ 行、$W_4$ 行、两列行列式或必要参数曲线返回。

这次日志没有 FLINT 分配异常或 Python traceback，准确分类是源内 120 秒时限触发。不能把它写成前一 ed0 的内存分配失败，也不能从缺少阶段输出猜测是哪一个具体乘法或 gcd 终止。

## 冻结范围与后续

保留本源和实际凭据，不提高限额重跑。本次完成的两条恢复线不支付任何新增一般面排除；此前已经给出的通用紧凑多项式恒等式不受此参数代入未完成影响。

下一输入应改变实际代数表示，例如保留 $z=Qt$ 为独立未知，使用原 N1 的非零二次头先作首一约化，再把原 $N(V)$ 线作为额外必要式；不把同一已超时分母代入改名后重放。
