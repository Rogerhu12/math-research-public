# 正确 $\Phi=0,\ f=u$ 的终端一次 $C_{17}$ 原理想覆盖

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本稿在当前 $D_{\mathrm{val}}\ne0$ 的正确原 $\Phi=0,\ f=u$ 图上，把[粗 $C_{92}^{13}$ 原覆盖](R150-appendix-unit211-Phi-zero-true-fu-C92-same-point-original-weight-cover.md)收紧为真正终端乘子的**一次 $C_{17}$ 原理想身份**。其不同权对界为 $48$；整个 $C_{17}=0$ 保留，不宣称 $f=u$ 已空。

## 1. 同一个原图与固定容器

沿用[正确单 $y$ 原输入](R150-appendix-unit211-Phi-zero-true-fu-single-y-common-weight-curve.md)：
$$
s=u-1,\quad L=Q-2s(u-2),\quad K=Q+4s,\quad
M_n=2uL-L^2-u^2Q,
$$
以及单坐标 $y=4s^2-Q+2L\lambda$。原五条必要式为
$$
F=(E_{\mathrm{Be}},E_{\mathrm{Bo}},N_1,NS,PS).
$$
其分母只在已付原权环内。此次还使用独立的[原零基点 mean 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)支付 $u$，其同步非零 $p$ 缩放使 $d_0'=u/p$。不借已撤回的紧凑公式。

既有原来源给出首一 $Q$ 三次
$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3
-1040u^2+528u-112.
\end{aligned}
$$

本次仅重建已确定十八条原定义列
$$
Q^i\{\widetilde E,y\widetilde E,
      \widetilde O,y\widetilde O,\widetilde N,y\widetilde N\},
\qquad i=0,1,2,
$$
在模 $\Psi$ 后的十二个 $Q^iy^j$ 坐标，$i<3,j<4$。这里的十二维仍只是固定多项式容器，**不是完整 $y$ 商代数**；不做未付的 $y^4$ 作用。

NS、PS 的定义和后六条原列本次均未执行；它们最后的原乘子确为零。旧 $C_{92}$ 的粗 DAG 分母 LCM、正目标序列及因式支持也未重跑。

## 2. 从真实终端系数返回完整多项式

新源实际反向累积十八条原列的系数 $\Omega_j\in\mathbb Q(u)$。十二个容器坐标全部返回
$$
\sum_j\Omega_j r_j=1.
$$
定义 DAG 有 $78$ 个节点，终端可达 $60$ 个；十二个原系数非零。

将来自同一原多项式的列重新合并，得到
$$
\beta_i=\sum_{j\ {\rm 来自}\ i}\Omega_jQ^{a_j}y^{b_j},
\qquad i=E,O,N.
$$
对完整分子作首一 $\Psi$ 短除，实际返回
$$
\sum_i\beta_i\widetilde F_i-1=\kappa\Psi.
\tag{1}
$$
这里检查的是完整多项式差与除法乘回，不只是十二坐标中的模等式。

为了合入 $\Psi$ 的真实原来源，只计算新目标必需的第一个 $3\times3$ 定义：把 $\widetilde E,\widetilde O,\widetilde N$ 按 $1,y,y^2$ 排成 $M$，取 $\operatorname{adj}(M)$ 第一行的三个余子式 $c_i$。逐列返回
$$
\sum_i c_i\widetilde F_i=\det M.
$$
计算并实际约消
$$
\nu_i=\frac{\Psi c_i}{\det M}.
$$
各 $\nu_i$ 的最终分母全部位于原已付支持，且
$$
\Psi=\sum_i\nu_i\widetilde F_i
\tag{2}
$$
完整乘回。因此计算中的 $\det M=0$ 并未被当作可删原支；(2) 在其全部零纤维仍成立。

由 (1)–(2) 得
$$
1=\sum_i(\beta_i-\kappa\nu_i)\widetilde F_i.
$$
再除以准确的原行尺度，得到真正原乘子 $\Gamma_E,\Gamma_O,\Gamma_N$，
$$
\boxed{\quad
1=\Gamma_EE_{\mathrm{Be}}+
  \Gamma_OE_{\mathrm{Bo}}+\Gamma_NN_1.
\quad}
\tag{3}
$$
这一步的实际完整分子分母已经约消。

## 3. 只由最终原乘子得到一次覆盖

逐项从 (3) 的实际分母中去掉已付权因子及独立支付的 $u$；其余分母实际都是纯 $u$，次数分别为
$$
17,\quad17,\quad14.
$$
前两个完全相同。它们的首一 LCM 为 $C_{17}$。实际检查每个 $C_{17}\Gamma_i$ 的最终分母全已付，并完整返回
$$
\boxed{\quad
C_{17}=(C_{17}\Gamma_E)E_{\mathrm{Be}}+
       (C_{17}\Gamma_O)E_{\mathrm{Bo}}+
       (C_{17}\Gamma_N)N_1.
\quad}
\tag{4}
$$
所以是一次幂的原理想身份，而不是从粗分母次数估计猜出的覆盖，也不把有理函数域中的 $1$ 当作所有原权点的单位。

$C_{17}$ 的完整 QQ 因式为非零有理常数乘
$$
(u-2)^2(2u-1)(2u^2-4u+1)
(2u^3-8u^2+12u-7)F_9(u),
\tag{5}
$$
其中
$$
\begin{aligned}
F_9={}&32u^9-320u^8+1440u^7-3848u^6+6870u^5\\
&-8886u^4+8828u^3-6650u^2+3296u-763.
\end{aligned}
$$
因式乘积完整返回；仅 $u-2$ 为二重，其余四因子均一次。平方自由部分次数 $16$；实际短除验证 $C_{17}$ 整除这个平方自由部分的平方。所有五个因子的全部复零纤维都保留。

注意运行中一元多项式默认把变量打印为 x；本稿的该一元变量始终是原 $u$，不是 $B=0$ 权图的另一个参数。

## 4. 同点范围与计数

由 (4)–(5)，不同 $u$ 至多 $16$。首一 $\Psi(Q)$ 保留所有 $Q$ 首项退化问题，给至多
$$
\boxed{48\ \text{个不同 }(u,Q)\text{ 权对}.}
$$

结合[全 $f=u$ 中心首一二次](R150-appendix-unit211-Phi-zero-true-fu-centered-v-monic-quadratic-and-two-mean-source.md)，每个权对至多两个 $(\lambda,T,t)$，因此至多 $96$ 个不同 $(u,Q,\lambda,T,t)$ 点。继续按同篇的完整规范恢复，$\rho$ 二次给至多 $192$ 个有序 Gram 点，两 simple 值的首项已付二次再给至多 $384$ 个完整规范不同点。

本次程序本身只返回 (4) 及 QQ 因式；后面 $96/192/384$ 是与独立中心二次定理的纸面合成，不冒称程序已构造完整有限代数。所有计数都是不同点数，不是整个非约化原 scheme 的长度。整个 $C_{17}=0$ 仍是当前真实后继输入。

## 5. 唯一实际执行

源：
[2026-11-28-unit211-Phi-zero-true-fu-terminal-original-multiplier-cancellation-8542.py](../notes/2026-11-28-unit211-Phi-zero-true-fu-terminal-original-multiplier-cancellation-8542.py)。

- 源 blob：c58584beb4f195d70e9183c116eed89304d9c317。
- SHA256：ff50d323eb8f8b04572baf077cccb8554b529daf0e74b974337e2010e863ae01。
- Actions run：46121349236；job：140906375035；内层 exit $0$。
- 驱动时间：0.330607481 秒；峰值子进程 RSS：41876 KiB。
- 源提交：ebfa29f5ace357092d4c69329028afb9741c9e02。
- 真实 pull 后：4562d8c809f3ced3a5e8668928702e1b47bb50b3；2026-11-28 07:28:34.108726 UTC 两 README 无变化。
- stdout：4437 字节；SHA256 fd405046406c3cedd37cf6dcb1c8b4a2fe3fae8ec5d7c3f88730889c41aef306。

$C_{17}$ 的 SHA256 为 82805c6529f521837e116b0aac2aeb726328c0a85316ff724d8bb6d71ae1547c；平方自由部分 SHA256 为 3f7a33d09b946a16b3a19e3d48d7e99a5b6a969306e94f15aa98fc79e7ecb731。小回执保真实分母、原返回阶段及身份；不保存可重算系数缓存。执行前的 db5f 草稿只修正了 qreduce 的返回接序，未执行，不能记为实际失败。
