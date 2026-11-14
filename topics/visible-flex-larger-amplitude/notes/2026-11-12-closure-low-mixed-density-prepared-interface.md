# R98 低46混合密度有序消费者：准备记录

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

状态：**源码已保存，尚未 Python/Arb/终端执行；不是新的数值证书。**
原 m94/96 的真实中窗积分仍是第一优先。此入口只支付原 R98 所需的低输出三档材料算子，不重复已有 ODE；没有注册新的结果编号。

## 1. 固定输入与数学比较

几何输入严格锁定实际 R90 的完整主包：
notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json，
SHA256 e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03。

原有序预算主包：
notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json，
SHA256 86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45。

98个原工作块必须在CLI环境中恢复，或依据已冻结几何入口重新生成后逐块核对主包SHA。不得经API分块、编码或搬运大数据。可用 --profile-root 指向恢复后的同名工作块；每一份仍必须与原主包的完整SHA相等。

保持全部18真实段、10793原材料叶、10878原几何子片、全部46模式和两物理分量。源是 source-$x$ 第二源 $N$，不重复乘 $r_x$。范数中的 $V_I$ 恰为原向上80位 dyadic；不把它替成全区间 $V_{\min}$。

令 $\mathfrak c_I=s_{I,\sup}+|\ell|_{I,\sup}$，$\sigma=17/16$。冻结几何入口的 weak_density 在 $\rho=0$ 计算
$$
 A_I=E_I s_{I,\sup}+(E_I+w^2/9)|\ell|_{I,\sup},\qquad
 R_I=\operatorname{up}(\sigma V_I),
$$
再保留完整 mean 和完整分母的正值上界。因此保存的 weak_candidate_cap 满足
$$F_I\ge A_I R_I^2\ge \sigma^2\mathfrak c_I V_I^2.$$
这是方向明确的正比较，不把 $F_I$ 当成真实背景密度的相等值。

对 $p=2,1,0$ 定义逐源叶上界
$$D_{p,I}=\frac{F_I}{\sigma^2 V_I^{\,2-p}}.$$
则在该叶的每个实际位置都有
$D_{p,I}\ge(s+|\ell|)V_I^p$。
除法在原叶位置完成，然后才进入原有序核。没有把一个已经聚合的 $\Gamma$ 除以 $V_{\min}$。

对每模及目标分量，消费者沿 R90 的准确正公式计算
$$
 \frac{1+m}{|W_m|_{\min}}
 \left[
  \sup_I\frac{|\chi_{m,c}|}{F V_I}
       \sum_{J\preceq I} A_{\phi,m,J}D_{p,J}
 +\sup_I\frac{|\phi_{m,c}|}{F V_I}
       \sum_{J\succeq I} A_{\chi,m,J}D_{p,J}
 \right].
$$
同片左右都用完整片质量是原已付保守比较。每分量先取完整径向 supremum，再求和两分量及全部46模。第二次扫描结束，准确 Fraction 前后缀质量必须逐项相等。

$p=2$ 时只是原所有源密度除以同一常数 $\sigma^2$。因此消费者额外逐模、逐分量、逐源积分以及全窗总和检查，新值不超过原已付 weak_candidate_cap 上界除以 $\sigma^2$。这给计算次序及单位的独立既有基准。

## 2. 条带及切口读出

输出固定 $\tau_*=18/125$。原 source-to-state 指数在相同常条带下准确抵消，因此以上 $\Gamma_{Lp}$ 适用于任意共同常条带，不依赖原几何数值标签 $1/64$。

若源来自 R93 的实际变条带，已知
$\tau(x)\ge1/64$，先保守支付每个输出模式的
$$
 e^{m(\tau_*-\tau(x))}
 \le e^{m(18/125-1/64)}.
$$
指数由纯 Fraction 的96项 Taylor 加严格几何尾计算。此倍率仅用于已经有限的 $m=2,\ldots,92$ 输出；没有免费提升未知高场的解析宽，也未给无限输出逆。

各模同时输出真实切口源功能：
$$
 |Q_m(b)|\le
 \frac{\sum_J A_{\chi,m,J}D_{p,J}}
 {|W_m|_{\min}e^{m\tau_*}},
$$
以及相应 $(1+m)e^{m\tau_*}$ 强质量版本。变条带版显式另乘上述指数费用。

原几何完整覆盖的最后一个 (cell11,segment0,x_left=0) 子片还输出准确 local_V，作为 node12 外侧范数值。它没有另求源或重算几何。该字段只在真正执行后存在；当前不能由全域 $V_0=2^{-40}$ 假定其值。

## 3. 精确执行入口与资源

新源码：computations/closure_outer_low_mixed_density_ordered_v1.py，
SHA256 7d3aed00e96bd9186cb8274e329435fa2d2a310271d6700e92876152f6c90646，
17142字节。

该源码同时锁定：

- 原几何producer：c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829；
- 原有序预算helper：e2113502398ebb1d4649a82a813ef0d6f2f90802ef9da52cbac8e37d36a39d83；
- 原流式JSON helper：6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0。

从课题目录运行，所有输出必须新prefix：

    python computations/closure_outer_low_mixed_density_ordered_v1.py \
      --geometry notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json \
      --reference-budget notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json \
      --profile-root /absolute/path/to/hash-verified-derived-profiles \
      --out-prefix /absolute/fresh/closure-low-mixed-r1 \
      --rss-kib 40960

若原工作块路径仍可读，省略 --profile-root。该程序只使用标准库和冻结标准库helper，不导入flint、NumPy或任何MJS，不启动源积分或ODE。40MiB是主动观察门，不是操作系统硬限。运行应继续由原 resource_run 留真实 wait4/峰值证据；超门或异常必须保留失败包，不能归因数学。

预期主包包括：

- 每模三档常条带、变条带费用后的低输出核；
- 两物理分量分别的最坏源/目标位置；
- 原精确有序源质量和切口读出；
- node12 原叶 $V_b$ 与原 $b,w_b$；
- 全部原块SHA和12个结构/算术门。

这些结构门不包含 R98 的最终三块自映和 Schur 门。只有将实际中窗全范围、非零头迹和高块一起代入后，才能判断低—中—高全频联立；不能因这个低窗consumer退出0就称整个PDE完成。

## 4. 本次状态证据

2026-11-12 23:47:01 UTC 的终端检查在进程创建前返回
No usable execution environment is available。没有 owned Arb/Node/终端会话。此源只经静态逐段检查和文本SHA计算，没有伪报 Python AST或任何数学运行。原 m94/96 唯一96MiB授权保持，恢复时仍先执行该真实中窗。
