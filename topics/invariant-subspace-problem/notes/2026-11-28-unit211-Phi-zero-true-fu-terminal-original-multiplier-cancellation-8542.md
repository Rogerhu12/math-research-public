# 新输入：f=u 的实际终端原乘子与一次纯 u 覆盖

日期：2026-11-28（Asia/Taipei）。尚未执行；源 SHA256 ff50d323eb8f8b04572baf077cccb8554b529daf0e74b974337e2010e863ae01。120 秒、1 GiB，共用最初绝对截止。

## 1. 与已成 C92 门的区别

[已成同点原列定理](../results/R150-appendix-unit211-Phi-zero-true-fu-C92-same-point-original-weight-cover.md)从可达 DAG 边分母的粗 LCM 得到 $C_{92}^{13}$，并由独立原 $u=0$ 排除给出 261 个不同权对上界。

本次目标是实际反传终端原乘子，合入 $\Psi$ 的原来源，允许分子分母真正约消，最后只从实际原乘子取一次纯 u 覆盖。不会重跑旧 C92 的粗 LCM、正目标序列或因式支持门。

只再生已确定的前十八个必要列
$$
Q^i\{\widetilde E,y\widetilde E,\widetilde O,y\widetilde O,
       \widetilde N,y\widetilde N\},\qquad i=0,1,2,
$$
及其已定十二坐标 DAG。明确删去 NS、PS 定义和后六列。必要前缀的原 SHA 与实际使用 SHA 均打印；原成功源字节不改。

## 2. 全十二坐标与完整多项式返回

反向累积真正原系数
$$
\Omega_j\in\mathbb Q(u),\qquad
\sum_{j=0}^{17}\Omega_j r_j=1
$$
并将十二坐标全部乘回。这里仍只是固定 $Q^iy^j$ 多项式容器，不假完整 y 商。

合并相同原列来源后，令
$$
\beta_i=\sum_{j\text{ 来自 }i}
 \Omega_jQ^{a_j}y^{b_j},\qquad i=E,O,N.
$$
对完整差
$$
\sum_i\beta_i\widetilde F_i-1
$$
按首一 $\Psi(Q)$ 短除，实际返回
$$
\sum_i\beta_i\widetilde F_i-1=\kappa\Psi.
\tag{1}
$$
除法的全部分子多项式和分母都乘回，不只验证模坐标。

## 3. 合入真正 Psi 原乘子

为构造新最终原乘子，唯一需要再生的旧定义是 $\Psi$ 首个三乘三原来源：

将 $\widetilde E,\widetilde O,\widetilde N$ 的 y 三系数排成 M。取第一行 adjugate 的三个余子式 $c_i$，直接逐列返回
$$
\sum_i c_i\widetilde F_i=\det M.
$$
在有理式中计算并完整约消
$$
\nu_i=\frac{\Psi c_i}{\det M}.
$$
每个 $\nu_i$ 的最终分母必须实际全属原已付支持，并返回
$$
\Psi=\sum_i\nu_i\widetilde F_i.
\tag{2}
$$
这仅是新目标所需的三个原乘子定义，不执行旧其余两个 cofactor、旧 gcd 或旧纯权结论门。计算中的 $\det M$ 不被视为物理单位；(2) 的最终正则分母与完整乘回保留它的全部零纤维。

由 (1)–(2)，真正终端原乘子为
$$
B_i=\beta_i-\kappa\nu_i,\qquad
\sum_i B_i\widetilde F_i=1.
$$
再按既有准确行尺度换回原 $E,O,N$，把 NS、PS 的系数取为实际零，得到五原值的完整多项式身份
$$
1=\sum_{i=0}^4\Gamma_iF_i.
\tag{3}
$$

## 4. 只用最终实际极点

对 (3) 的实际约分后分母，逐项剥除既有原权支持及已独立支付的 u。u 的来源是
[R150 原零基点 mean 排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)；同步非零 p 缩放给 $d_0'=u/p$，与当前对称规范相容。新 $\theta=u-\ell Q$ 单位在本源中不使用。

各剩余分母必须实际为纯 u 多项式。取其 LCM 为 $C_{\rm new}$，逐项确认 $C_{\rm new}\Gamma_i$ 的剩余分母全已付，并全原式返回
$$
\boxed{C_{\rm new}=\sum_i(C_{\rm new}\Gamma_i)F_i.}
\tag{4}
$$
因此本次是一次幂的原理想覆盖。整个 $C_{\rm new}=0$ 保留；仅在它确为非零常数时才排空当前整个 f=u 支。

若它非恒定，完整 QQ 因式乘回与平方自由幂整除给不同 u 数量；乘已成首一 Q 三次只得到不同 $(u,Q)$ 权对界，不自动得到固定权全部原几何点数。

## 5. 资源与三源码依赖

先打印已经完成的 (4)，再对新多项式作精确支持分类。不保存或传递可重算系数缓存。

规范 stem：
2026-11-28-unit211-Phi-zero-true-fu-terminal-original-multiplier-cancellation-8542。

依赖：

1. 2026-11-28-unit211-Phi-zero-true-fu-same-point-twelve-by-twentyfour-8542.py，SHA e35e019e9ee84448b8e4e5afc31c81f449b8b515598329e2fb8c2e38d4870aa6；
2. 2026-11-28-unit211-Phi-zero-true-fu-single-y-original-scalar-cofactors-8542.py，SHA 9d591ab41ed41cc7dbee8ac3e9ce326ef68348455751ae9ad1cea954a7d463cb；
3. 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

第一份只到 target 定义之前，固定修改为十八必要列；第二份只到原 det 定义前并删除 NS/PS 两行；第三份只提供原算术。所有变更都限定于本新源的内存定义前缀，不修改已执行文件。
