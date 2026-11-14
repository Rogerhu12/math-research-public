# 正全局径向归一参数证明的独立复核

2026-11-09，复核者 `/root/tail_theory`。被审新推导的作者为 `/root/independent_geometry`。结论：**PASS，覆盖下述新推导及账本**。

审查对象：`2026-11-09-db6f-audit-positive-radial-alpha.md` 的 §4–7 解析 TV、几何级数、保护端与归一参数证明，以及 `scripts/db6f-audit-tail-radial-alpha.py` 的参数绑定和 Fraction 账本。

冻结证明 SHA256：`1f39f9d214d25defe2ff5ef9a23dd723de590ab966f075f84a15ffe0117d7e80`；冻结脚本 SHA256：`33aea516fe806c2d803b9990d9c5cba838f26f128b3c9c6a82159569a69b07df`。

**独立性边界：** §3 的 cell-0 积分器由本复核者编写，已由该文作者独立审查；本报告不重新以“独审”名义审查自己这部分实现。以下把其已审区间结果作为明示输入，仅审核另一代理独立提出的内尾分析与拼合。组合证明的不同组成部分分别有未参与者的审查。

## 逐项复核

1. 在常值 cap 下，raw log slope 每个转换段为 $C+\Delta S(x)-\lambda x$，其导数正值集合在 $\Delta>0$ 时至多为一个区间，因为 $S'=30x^2(1-x)^2$ 先增后减。第一 jump 为正、最后 jump 为负；中间两个 jump 的和为 $-\log R_n<0$，故其中至多一个为正。任意 valley control 被准确吸收为共同中间平台，未假定它很小。

2. cap 是 raw log slope 的非减函数，随后 $f(w)=w/\sqrt{1+w^2}$ 也非减。因此每个至多两段的上升区间贡献不超过 $M_n$。用 $TV=2V_+-(f_{end}-f_{start})$、$0\le f\le M_n$ 得 $TV\le5M_n$，不需要跨 cell 的端点抵消。保护段的 $\chi\le1$ 只减小 curvature-width 项，因此仍被该界覆盖。

3. 独立从 $\mu_n=\epsilon\delta_n^{11/4}$ 与 slope $\mu_n e^v/(\delta_nr^7)$ 推得 source 系数为 $1/(2^{15/4}\delta_0)$、衰减指数为 $2^{-7n/4}$。有限校准表内 $\widehat\alpha_n\ge1/2$，$n\ge10$ 的 valley control 为零，全部 log 平台均满足 $e^v\le64$。由参数盒得到 $w\le1280\,2^{-7n/4}$ 的数值系数无遗漏。

4. $W_{10}=5/(512\sqrt2)<25/3584$；比率 $2^{-7/4}<1/3$ 等价于整数不等式 $128>81$。所以几何和界 $75/7168$ 正确。有限 cell 的和被一个显式无穷数列上界包围，并未把它等同于无限非线性解的收敛。

5. 保护端额外旧径向项的 $j_0=1$，用整个旧源厚度上界虽宽但有效。由 $T/\sqrt{12}<1/60$ 与 $e^x\le(1-x)^{-1}$ 得 $r_{old}-a_c<a_c/59\le3/1180$。这里没有把 cell 0 端点保护项漏掉；它已经在作为输入的九段 cell-0 证书中。

6. 将 $A_0<21/100$、内尾 TV 界与旧径向项相加，精确有理数小于 $3/8$。另一方面 $r_d<r_{old}<9/59<4/25$，$r_{cut}>59/100$，故真目标宽度 $L>43/100$。由于 $B\ge B_0>0$，唯一 $\alpha=(L-A)/B$ 严格为正。

7. 正权重上界 $3$ 给 $B<3(r_{old}-a_c)<9/1180$。这与 cell-0 的正下界组合为文稿所列粗 $\alpha$ 区间。逐段新径向速度严格为正：$\chi>0$ 处 free term 为正，$\chi=0$ 端点旧径向项为正。因此积分归一不是形式上解出一个没有单调性的参数。

## 程序与独立复跑

已逐行检查有限表 hex/value 一致性、冻结参数相等、calibrationSteps 固定、源盒、cap/valley/weight 条件、源代码哈希、已审 cell-0 程序哈希、checkpoint 和 bookkeeping 绑定。最终不等式均使用 `Fraction`；显示小数未参与严格真假判定。

独立复跑写出 `2026-11-09-db6f-tail-review-positive-alpha-replay.json`，全部 JSON 字段与作者结果逐项相同。额外直接按 Fraction 核对圆整 $A$ 上界小于 $3/8$，且 $43/100-A_{upper}>0$。

本次未发现需要修改的数学问题。结论给出该冻结解析旋转背景的唯一正全局径向归一参数；**没有**将数值 $97.645347\ldots$ 当成精确参数。要把有限非线性映射的 metric 核验转到该精确背景，仍须支付这个参数的精细误差或直接包围背景。共同 Cartesian 接缝、全局 reach、非线性无限尾与 README 完成也不在本审查结论内。
