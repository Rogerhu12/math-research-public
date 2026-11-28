# 原 NS/PS 六次标量的整个 Phi 来源延拓输入

日期：2026-11-28（Asia/Taipei）。尚未执行的新目标；120 秒 / 1 GiB。

已成
[中心原 NS/PS 六次标量](../results/R150-appendix-unit211-Phi-zero-centered-original-NSPS-sixth-scalar-content-and-true-leading-support.md)
目前只按 $\Delta_N\ne0$ 证明了
$$
\mu N_S+\nu P_S=C_6+k n
 \pmod{(q_R,q_W,q_O)},\qquad n=p_0+p_1T+p_2z.
$$
虽然该次实际 $\mu,\nu$ 已经是 QQ 权/λ 多项式，仍不能仅据此删除 $k$ 中可能剩余的斜率分母。

本次真正新目标是取**同一实际**三乘子 $(\mu,\nu,-k)$，对其每个完整分母只用当前整个 Phi 图的旧已付单位作精确 gcd 除法和乘回，明确不允许把 $\Delta_N$ 加入此单位表。随后把三个原系数全部乘回。

若全部分母剩余为常数，则所有原三均值规则、完整 NS/PS 来源以及这三个最终乘子都在未倒置 $\Delta_N$ 的权环中。它是整域的局部化，其嵌入函数域单射；原函数域恒等式因此是该权环内的真正恒等式，直接覆盖整个 $\Delta_N=0$ 图，并证明 $C_6$ 属于整个当前 Phi 的原 $I_6$ 理想。没有依靠该图稠密点的集合论近似，也没有改变原多项式理想。

在新的整个原来源成功时，已成真实 $\lambda^6$ 头 $H_{42}\ne0$ 上可以规范首一。原三个均值仍给 $(1,T,z)$ 三生成元，故每个固定权对的必要代数由十八个 $\lambda^j(1,T,z)$、$0\le j<6$ 生成。只有在额外 $\Delta_N\ne0$ 时，旧精确二列模型才给十二生成元。新输入不删除整个 $H_{42}=0$，不声称整个 Phi 空。

若任何最终分母仍有未付因子，则保存它的完整支持，准确报告未取得全图延拓；不把旧补图式重写为新全图结论。

## 唯一源与前缀边界

建议源：
`2026-11-28-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-three-multiplier-regular-extension-8542.py`。

4857 字节，SHA256
`5d799b07f23bcc8bd00a2c210416926bbe648869723eb39eeee7c8b0f2b00277`。

直接依赖：
`2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py`，
SHA256 `baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6`，
可用 `ISP_PHI_CENTERED_NSPS_SOURCE`。
只取定义到实际 $k$ 形成的 6125 字节，前缀 SHA256
`4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d`；
不执行旧 $\lambda$ 内容 gcd、旧首项剥除或其后的任何目标。

其递归三件纯源码保持：

- I10：`2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`，`ISP_PHI_I10_SOURCE`；
- e797：`2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，`ISP_PHI_SLOPE_SOURCE`；
- 100ce：`2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，`ISP_PHI_FIRST_HEAD_RULE_SOURCE`。

前缀是新全图来源必须使用的实际定义，不是复跑一个旧大门或给已成补图结论加审核。没有旧 $\lambda^8$、大 cofactor、范数、投影或 Gaussian。所有嵌套 timer 钳制到本源同一个 120 秒截止；只输出小回执、来源身份、次数与 SHA，不存可重算载荷。
