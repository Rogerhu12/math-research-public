# 已付 R80 源到 R82 整腿模数的实际积分

`fourfold_integrated_parameter_source_budget.py` 将已完成的 R80 全 169 个闭径向叶
及真实 root collar 转成固定参考坐标的 B1、B2。它不计算有符号平均，也不声称 twist 非零。

固定参考是 descriptor SHA256
`097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052` 所定义的 δ5 retarget。
550 段真实有限参考 q=Y_x 在整个实时间和归一标签带 1/512 上已经证明
Re q>0.03、|q|<1.05。因此 Y 的物理角像不超过 21/10240，严格包含于 R80 已付的 1/56 角带。
Y、q 与各段时间尺度在参数区间内固定；R80 场源则覆盖其保存的完整参数区间。

若某正径向叶的实际 s=r/t(p) 包络为 [s_-,s_+]，则两半腿的物理时间长度上界为
2(asin(s_+)−asin(s_-))。本程序先以准确 Fraction 将包络裁到 [0,999/1000]，
随后用 Arb 支付 asin 长度；root collar 另付
2(π/2−asin(999/1000))。包络有少量重叠时只多计费用，不漏覆盖。

\[
 B_i=\int |g_i|\,du
 \le\frac1{0.03}\sum_{\text{leaves}}
     2(\arcsin s_+-\arcsin s_-)\sup|f_{p^i}|,
 \qquad g_i=h f_{p^i}/q .
\]

没有额外的归一角因子 4。

实际完整输出 `2026-11-12-step5-integrated-parameter-source-budget.json` 给出
B1<1077.689852253、B2<9646.363329155；仅用整域最大值的对照分别为
2000.16950233、20400.77223528。累计物理时间包络长小于 3.141592751815，略大于 π
来自参数径向包络重叠。该改进不花费新的真实几何计算。

这些仍是较粗的余项输入。真实 g1/g2 有符号有限积分、其真实误差 E1/E2、当前 g0 的 A，
以及 R31 所需加权平均均必须另付；不能以本报告替代它们。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_integrated_parameter_source_budget.py \
  --out notes/2026-11-12-step5-integrated-parameter-source-budget-replay.json
```

冻结源 SHA256：`5a37b36b42936e69921b9ab921b691a6860030dd48859ec22ed24fe045b118cf`。
已跑报告 SHA256：`1157bc1b8ad6f70b9fbd65aeaee6152da842e066d22b216cd2ca87620e5f5a41`。
R80 输入报告 SHA256：`33c2bdddb0c4e1172275b961da0a2e5e23486299168efe80c4cb6870c30dd556`。
完整 q 报告 SHA256：`87aeff7e8824c7d6301c6f33cbeea506e584004c5bee1591512a556348cbfd8c`。
