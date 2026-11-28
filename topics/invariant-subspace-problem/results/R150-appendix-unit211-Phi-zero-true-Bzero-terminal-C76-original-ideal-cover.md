# 正确整 B 支的四原乘子一次返回：C76 与至多 76 个不同权对

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：本条准确范围已证明。**

## 1. 定理与准确范围

在当前正确的 $\Phi=0$、$D_{\mathrm{val}}\ne0$ unit211 图，令
$$
B=-Q^2+(12u^2-20u+8)Q-16(u-1)^2.
$$
沿[整 B 的原 I6 十二乘二呈示](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)的有理坐标
$$
x=\frac{Q}{4(u-1)},\qquad
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac43(x^2-x+1),
\tag{1}
$$
记
$$
F=x^2-x+1,\quad H=2x-1,\quad
\beta=5x-1,\quad J=7x^2-4x+1,\quad
C_2=23x^2-11x+2.
$$
所有这些分母的支持已由原权单位及先前整 $C_2$ 排除支付。当前系数环为
$$
A=\mathbb Q[x,1/(xF(x+1)H\beta JC_2)].
$$
不倒置旧的所选头 $H_3=11x^3-18x^2+6x-1$。

设 $I_4$ 是四个真实原条件
$$
I_4=(E_1,E_{\mathrm{Be}},E_{\mathrm{Bo}},N_1)
$$
在同一点的原坐标环中的理想。本次实际完成四个原乘子的全系数返回，得到非零平方自由多项式 $C_{76}\in\mathbb Q[x]$，满足
$$
\boxed{\deg C_{76}=76,\qquad C_{76}\in I_4.}
\tag{2}
$$
这里是 $A$ 上的原多项式理想身份；并未把原已付系数分母冒充为 $\mathbb Q[x,\lambda,f,t]$ 中无分母的整数身份。

完整有理不可约分解为
$$
C_{76}=\gamma\,C_{(2)}C_{(34)}C_{(40)},\qquad
C_{(2)}=2x^2+4x-1,\quad\gamma\in\mathbb Q^\times,
\tag{3}
$$
三个因子的次数分别为 $2,34,40$，幂次都为一。故整 B 上不同 $(u,Q)$ 权对至多 76 个。式 (1) 的逆式表明没有把多个 x 值合并后再重复计数。

本定理保留三个因子的全部零纤维；没有排空整 B，也没有给固定权处全部几何点数的有限上界。它将前篇[粗 C315 覆盖](R150-appendix-unit211-Phi-zero-true-Bzero-C315-original-ideal-weight-cover.md)的权对界改善为 76，且这次原身份只需一次幂。

## 2. 必要原输入与中心坐标

先前整 B 呈示已经在已付权环内给出一条原线性式
$$
L_{\mathrm{raw}}
=p_0+(a\lambda+b)f+(c\lambda+d)t,\qquad
\Delta=ad-bc\in A^\times.
$$
在 $L_{\mathrm{raw}}=0$ 上作双向已付坐标变换，得到中心坐标 $\omega$。四个原二次的代入式记为 $F_i'$，$0\le i\le3$。已有原组合给
$$
q=\omega^2+q_1\omega+q_0=\sum_{i=0}^3\tau_iF_i',
\qquad
\ell_i=F_i'-a_iq,\qquad \deg_\omega\ell_i\le1.
\tag{4}
$$
$q_0,q_1$ 对 $\lambda$ 的实际次数分别为 2、1。

本次只取以下七个必要原模行：
$$
\ell_0,\ \omega\ell_0,\ \ell_1,\ \omega\ell_1,\
\ell_2,\ \omega\ell_2,\ \ell_3,
\tag{5}
$$
其中 $\omega$ 倍按首一 q 返回两坐标。没有再执行 NS、PS 定义、后五行、旧三个标量 cofactor、C315 的粗 LCM 或旧正幂目标门。

必要定义生成 32 个 DAG 节点；真正终端组合只涉及其中 24 个。每一条边都已逐两坐标乘回，临时 $\mathbb Q(x)$ 主元没有被视为物理单位。

## 3. 新终端系数及真正原四式返回

这次从终端 $(1,0)$ 反向累计实际、约分后的原系数，完整返回
$$
\sum_{j=0}^{6}\Omega_jr_j=(1,0).
\tag{6}
$$
实际只有 $\Omega_0,\Omega_1,\Omega_6$ 非零，对 $\lambda$ 的次数依次为 6、5、7；其余四项为零。这是实际系数的完整两坐标身份，不是仅由泛型 rank 断言原点为空。

定义
$$
\beta_0=\Omega_0+\omega\Omega_1,\quad
\beta_1=\Omega_2+\omega\Omega_3,\quad
\beta_2=\Omega_4+\omega\Omega_5,\quad
\beta_3=\Omega_6.
$$
在完整的 $\mathbb Q(x)[\lambda,\omega]$ 中，对
$$
\sum_i\beta_iF_i'-1
$$
作首一 q 短除，实际余式为零，记商为 k。由 (4) 得
$$
B_i=\beta_i-k\tau_i,\qquad
\boxed{\sum_iB_iF_i'=1.}
\tag{7}
$$
源码将 (7) 的全部 $\omega$ 系数重新乘回；不是只在二坐标余式中验证。

现在才取四个实际、已约消的 $B_i$ 的 pure-x 分母 LCM。其次数为 91。剥除既有已付支持后得到次数 76 的 $C_{76}$，并再次全式返回
$$
\boxed{C_{76}=\sum_i(C_{76}B_i)F_i'.}
\tag{8}
$$
所有乘子的剩余分母均属于 A。没有为任何中间主元增加新物理单位。

由于双向坐标代入的核是 $(L_{\mathrm{raw}})$，且 $L_{\mathrm{raw}}\in I_4$，式 (8) 通过原坐标同构提升为 (2)。该论证不要求四式商自由，也不把原 $D_{\mathrm{val}}$ 倒置到计算中。

## 4. 精确支持的可再生定义

$C_{76}$ 由唯一冻结源中的实际终端四乘子、最终分母 LCM 和已付因子剥除确定。完整系数不作为可重算缓存入库。其规范指纹以及完整因式指纹为：

| 对象 | 次数 | SHA256 |
|---|---:|---|
| 最终四乘子分母 LCM | 91 | 4cf4a451f93187280303fedb234a9dd5576183470f121eba9f840615b3c659ed |
| $C_{76}$ | 76 | 5eb0b13c682928e24c8449fa7dbbfa7a890fd72438897a4ae98de523ae778242 |
| $C_{(2)}$ | 2 | 8aac1a314fc4ee290a3fb1a7a3c0358f5fe7bcb822eae7975d3928f66e67a354 |
| $C_{(34)}$ | 34 | b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff |
| $C_{(40)}$ | 40 | ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a |

程序的算术 context 将 B 参数 x 打印为 u；表中及 (3) 已按原几何参数统一改记 x，未改任何源码或指纹。

完整 QQ 因式乘回成功；最大幂次为一，平方自由支持次数仍为 76。三个整原常数域是后续输入，不因泛型四式单位而被删除。

## 5. 唯一实际执行与来源

- [精确源](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.py)，Git blob 4fb7fa723660043b5179c0f1302494064c1955f2，SHA256 73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35。
- [输入说明](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.md)；[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.execution.json)。
- 唯一 Actions run 46118011351，job 140896068934；内层真实 exit 0，0.569564090 秒，44912 KiB。
- 精确源提交 be718a38bfaa86f4455ab8d2c7a361b527c6ee85；实际 pull 到 260ee6ac332ec91ab78d0f200b41dd6b1054e093，2026-11-28 06:44:51.158470 UTC，两 README 无变化。
- stdout 2566 字节，SHA256 62e8b731c5724a207727a61afe8b8ef6ebd34f78af31f272e9cb612625801be6。

本次有 102 次多项式精确除法、14 个种子坐标、50 个边坐标、10 个零行坐标、4 个终端坐标及 2 个完整 $\omega$ 原身份返回。数学结论由这些实际身份支付，不以工作流绿色代替内层结果。
