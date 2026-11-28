# 准确全前缀所有点对的定量 reach 预算

**已证明。** 对 R233/R232 准确原前缀，包含两条真实边界圈的整个环带作为闭集的 reach 至少 $1/9.867915>.1013$。证明见 [R259](../results/R259-accurate-whole-prefix-two-sided-reach.md)。全后缀、与后缀点对及未来实际修正的前缀仍须分别包含。

使用 R257 的 1024 全角区间末圈高度与同一固定材料经线弧长，整个环带离 $(p(u),s)$ 不超过 .0143。欧氏弦不超过 $2/9.867915$ 时，对应中央椭圆弧弦比最多 1.189851、上界路径的比例最多 1.196491、所得内距小于 .277108。准确 coast 在两个边界皆有外向 $f'>0$。实际 $C^2$ 端口、原固定度量误差与曲率皆保留。

在课题根运行，$W$ 是按原记录恢复两个 master 与 R257 末圈报告的输出目录。新计算只用精确分数核实常数。重新生成的 R257 报告有计时字段；新入口按实际几何 SHA、行流、全角格数及区间精度绑定输入。

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/2ecf-polar-accurate-prefix-secant-budget.py \
  --ramp "$W/gap105-prefix-ramp-master.npz" --coast "$W/gap105-prefix-coast-master.npz" \
  --exit-ring "$W/polar-accurate-exit-angular-graph-1024.json" \
  --output "$W/polar-accurate-secant-budget.json"
```

| 对象 | SHA256 |
|---|---|
| 新入口 | 0535a729e8738e137bfa3606086f532e1a5de2e93a1a5cd91b66a05724e4fdbb |
| 完整准确分数报告 | 16aa6f9f2df638366c6d296aad380df53d0ade6cfbf116091c2f25574043d72c |
| stdout | fe33004be7cea722151682aca61858eba69ea2b3ffd986b952b2f1d0acfc5870 |
| 外部回执 | bccadcd2e3ef9a2f658ec6d704d6de3ee7df8e985026f0c14818446eed4d5679 |
| 原 R257 末圈报告 | 3f7c39bf060996d3d9c101880050d9cab5cc0ad843790cd262fd1ea95112366a |
| 原 R257 末圈行流 | ea4c715a8f25007bd49674bbcaafd5eb3bc60627c3069112825b29e0d1782a4c |
| 准确 ramp master | 0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7 |
| 准确 coast master | f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d |

真实外部进程自然返回 0，用时 .289505 秒，峰值 RSS 24352 KiB。计时及路径按本次原样记录。新的结论由 R259 的全点对论证与其引用的连续输入共同给出。
