# R150：L0 的整个原 P1 双系数零分支排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。接续前会话 Astra-ISP-347c-20261126 的真实计算，不重跑已完成投影。

**结论。** 在已付 w=0、w=1、b+c=0、W=0 等整支之后的原 L0 图中，P1 对 t 的两个系数同时为零的整个分支为空。本稿由前会话已经实际完成的 beta 首项非零排除，以及本次新增的首项零有限纤维原返回合成。其余 G 曲线和交点仍开放；不声称整个 L0、unit211 或 ISP 已完成。

## 1. 保留原两根的参数与双零条件

使用 [L0 的原对称参数及 W 整曲线证明](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-linear-lambda-curve-exclusion.md) 的共同规范 p+q=2。以原参数 rho、lambda、w，记

$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad R=\lambda-1-w,
$$
$$
u=R/\rho,\quad V_2=A/\rho^2,\quad
Q=(2A\rho-B)/(\rho^2R),\quad \Delta=1-Q,
$$
$$
\ell=(2u-V_2)/Q,\quad
bc=\{\ell^2\Delta-(u-\ell)^2\}/(4\Delta).
$$

在整个二次代数 kappa²=Delta 中取 p=1+kappa、q=1−kappa，b、c 为对应相关权，h=1+rho·p、k=1+rho·q。既有源重建同一原 Gram、原 U 三矩、原 N(V)、E0/N0 和全部九式；双点乘法始终为

$$
(vz)_1=v_0z_1+v_1z_0.
$$

没有取某个有利的 kappa 嵌入。A 可为零，从未将其作为分母。

用原 N(V) 得到的 f 后，清除原已付物理分母，原 P1 为

$$
\alpha(\rho,\lambda,w)t+\beta(\rho,\lambda,w)=0.
$$

分别剥除各系数中已付单位，可得等价双零条件 alpha0=beta0=0，其中

$$
\deg_\rho\alpha_0=2,\qquad
\beta_0=b_1(\lambda,w)\rho+b_0(\lambda,w).
$$

这两个系数及 b0/b1 在 [原冻结自含源](../notes/2026-11-26-unit211-L0-P1-double-zero-linear-rho-return-347c.py) 中由原 Gram 直接生成，不依赖数值采样。二次式的准确形式为

$$
\begin{aligned}
4\alpha_0={}&4\rho^2(\lambda-w-1)\\
&+\rho(-8\lambda^2+8\lambda w+12\lambda-4w^2-8w-6)\\
&+4\lambda^3-4\lambda^2w-8\lambda^2
+6\lambda w^2+10\lambda w+6\lambda\\
&-2w^3-6w^2-5w-2.
\end{aligned}
$$

原 rho、lambda、w、w−1、R、bc、Q、Delta、P0、u−1、ell 均按已登记整支支付；独立已闭曲线 W=4lambda·w+2lambda−2w²−4w−1 也可以剥除。beta 的 rho 首项 b1 则必须保留零支，不能直接除去。

## 2. b1 非零：前会话实际完成的全部原返回

当 b1≠0，用同一 rho=−b0/b1 返回原 alpha0 和原 mean/N 结果式。每个分母只含原单位和本图的 b1；源没有把多变量 gcd=1 当作空集。

以返回的原 alpha0 为 anchor，六条 QQ w 结果式的 lambda 次数为

```
517, 984, 954, 1148, 1162, 806.
```

其逐次一元 gcd 次数为

```
517, 400, 400, 400, 400, 400.
```

每次 extended gcd 都实际核对 Bézout 乘回。400 次完整多项式分为 11 个参数因子；平方自由总次数 43。参数因子的次数为

```
1, 20, 3, 3, 1, 1, 7, 2, 2, 2, 1.
```

完整因子、重数及 SHA 保存在 [实际读取回执](../notes/2026-11-27-prior-L0-regular-boundary-G-execution-readback-8542.json)。对每一个完整 lambda 商代数，源重新返回原 w 多项式；剥除实际物理单位之后，原 alpha0 与原 Res_t(E1,N1) 返回式的共同 w 因子最终全为 1。每条域逆、除法和 Bézout 均实际回乘，保留全部 lambda 根和相关 w 值。

这次执行是在前会话停止后完成的真实任务，而非本次重跑：

- run 45835855085，job 139964393984；原提交 85af72d96e485725eec42655b4e8507ab7fc5b83。
- 原源 SHA256 `c8c3e31972f2cfcbddc7b6069efeb1bb28b87bf75170541b3a36f7d68b20e5a0`；blob `778b5e96f8b95285f16d873e86a7b601c1365ea9`。
- 数学源 260.208555 秒，exit 0；驱动 260.278687 秒、峰值 RSS 182332 KiB。
- stdout SHA256 `d956d28f635a7280eb6ad2d38dcc53377168983d3d4692a19260a58e40baf48c`。

因此 b1 非零的整个原 P1 双零图已经排除。

## 3. b1=0：原 42 次覆盖准确留下的两类

此时必须同时保 b0=0。前会话独立 job 139964394439 已计算这两个原式的 42 次 lambda 结果式，并返回所有 9 个完整参数因子。七类被原单位或原 b0/b1 的 Bézout 排除，恰余下表，未丢弃首项零纤维：

| 完整 lambda 代数 | 唯一相关 w |
|---|---|
| lambda=2/3 | 1/4 |
| QQ[lambda]/(Phi7) | w7(lambda) |

这里

$$
\Phi_7=128\lambda^7+32\lambda^6-336\lambda^5+324\lambda^4
+108\lambda^3-331\lambda^2+214\lambda-45,
$$
$$
\begin{aligned}
w_7={}&\frac{12288}{2459}\lambda^6+\frac{3680}{2459}\lambda^5
-\frac{34328}{2459}\lambda^4+\frac{22592}{2459}\lambda^3\\
&+\frac{13535}{2459}\lambda^2-\frac{43245}{4918}\lambda
+\frac{11419}{4918}.
\end{aligned}
$$

42 次原覆盖的 SHA256 为

```
4f17c2eb3e9b3faeda3430cd0c9e1b66f5e407362491df6796ba70b3a64bfb2c
```

前会话该 job 的数学源 4.254483 秒、exit 2，驱动 4.336028 秒。它只留下这两类候选，没有宣称已排空；这一原退出身份照实保留。

## 4. 新增的同参数 rho 原返回

本次 [新增自含源](../notes/2026-11-27-unit211-L0-P1-double-zero-boundary-original-return-8542.py) 重建原 Gram 系数，然后直接接上已执行的两类候选，不重跑上述 42 次或 400 次投影。分别在 QQ 与整个 QQ[lambda]/(Phi7) 内先核对

$$
b_0(\lambda,w)=b_1(\lambda,w)=0.
$$

对同一 lambda、同一 w，把原 alpha0、全部物理单位以及原 Res_t(E1,N1) 返回成 rho 的一元多项式。在两个完整代数中，原 alpha0 都是二次；它与原结果式的 gcd 都为 1：

| 参数代数维数 | 原 alpha0 的 rho 次数 | 与原 Res_t(E1,N1) 的最终 gcd 次数 | 实际基代数逆次数 |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 35 |
| 7 | 2 | 0 | 35 |

每一个 Euclid 除法都核对 dividend=quotient·divisor+remainder，每一个基代数逆和最终 Bézout 身份都真实回乘。没有将原 t 换成一个独立参数：同一 t 上 E1=N1=0 必使这条原结果式为零，因而与 alpha0 及该 Bézout 恒等式矛盾。对整个 Phi7 代数的检验同时覆盖其全部嵌入，不需要选单根。

[实际执行回执](../notes/2026-11-27-unit211-L0-P1-double-zero-boundary-execution-8542.json)：源 16173 字节，SHA256

```
81a2bd42db04a4df26003180b2463372788bc2cf4a757185c656b3bed20e461f
```

Python 3.12.14、python-flint 0.9.0；180 秒 alarm，实际 3.913952 秒，exit 0，峰值 RSS 52944 KiB。stdout SHA256：

```
ce1c67122c50f5f8ad3cb97c426740cd30705c01720002d4486e31fdb898f5c9
```

故 b1=0 的原 P1 双零图也整个排除。与 §2 合并，所有 beta rho 首项零/非零纤维均已覆盖，整个原 P1 双零支路关闭。

## 5. 剩余 L0 与另一次真实失败

G(7,4) 原 QQ 门 run45833153054/job139954904770 已补收实际回执：1,989,660 字节输入，数学源 465.206981 秒，Singular 触 4 GiB 地址空间、returncode 14；源 exit 2，驱动 465.297425 秒、RSS 4174008 KiB，未得 I*C=1。完整准确身份与前述两次回执一起保存，不再写“等待结果”，也不重跑这一展开。

本条关闭 P1 双零后，余下 G 曲线、一般交点及更外层图须继续从新的原低次输入推进。有限分支排除不是整个普通 Hilbert ISP 的完成。
