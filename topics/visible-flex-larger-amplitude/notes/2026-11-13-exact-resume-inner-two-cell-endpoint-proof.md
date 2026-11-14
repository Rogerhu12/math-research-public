# 同一真内场的 cell14→13→12 两胞元点读出

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本条只消费已存在的同一 R100 全场、已付 13 窗和无限块，以及
geometry_audit 的实际 cell13 端点核。原单位 S 积域、T 共享 `l1<=1/32`、
原连续条带、全部 mean/逆/真 far 不变；没有把点读出改称 whole-cell
范数，也没有建立新的固定点。

## 1. 精确输入算子的拼接

设 `V13up` 是前一 cell12 endpoint producer 准确保存的
`cell13_boundary_Vprime_upper`，`C12,w` 是同一 producer 及 canonical
交集给的第 w 窗初值列。两种候选在构造时均线性乘了**同一个准确数**
`V13up`，其余传播、frame、strip、真实 w 转换随后向上舍入。因此

```
C12,w / V13up
```

是绝对 strong balanced 输入质量 `H13,w` 到最终相对 P/K 真头的合法
上界。这里是消去保存列的构造尺度，不是用上界作分母把一个点值冒充
`V'` 归一化场帽。

新 cell13 实际核的输出采用绝对 strong balanced 质量；输入是 cell14
旧 `V'` strong 窗帽。该核已支付 14→13 的 frame/strip，原 cell12
列已支付 13→12 的 frame/strip，故各界面恰收费一次。cell13 使用
全部 1975 个既有面板和原 canonical 正矩阵，无新 ODE 或积分。

## 2. 完整 cell13 源与共有质量

在每个窗口，先算

```
H13,w <= initial13,w * r14,w
        + K13,s,w * (reference_s,w + DQ_s,w + Qe_w + Tdiff)
        + K13,ell,w * (reference_ell,w + DQ_ell,w + Qe_w + Tdiff).
```

完整 reference Laurent 源来自原 cell13 实际记录；全部 mean、逆尾
和零分子模式的既有证明保持。DQ、Qe 窗口支撑及完整 T 差取最新
`inner-window13-frequency-square-bootstrap-r3` 的同一真场记录。
所得点帽再与 `V13up * r13,w` 相交。

共同 near/rest 质量按原共享规则消费：初值对 cell14 各窗帽和共同质量
取准确 support；reference 逆尾每材料乘最大源列一次；DQ 聚合加权列
后再对同一输入共同质量取 support；Qe/T 的完整共同质量只乘最大
两材料源列和一次。共同点帽又与 `V13up * old_common13` 和各窗帽之和
相交。

随后将这些绝对点帽送入 `C12,w/V13up`，按窗帽和共同点质量取 support。
**原完整 cell12 reference、DQ、Qe、T 源全部另行保留**；不能因为输入
已经更小而把 cell12 的源删除。无限头直接保留 r3 的完整证书。

全部运算使用准确 Fraction；只有保存端点时向上取 160 位 dyadic。
原 whole-cell 帽完全未改。

## 3. 实际结果与范围

正式退出 0，wall `0.620094 s`、峰 `50,032 KiB`，45 个身份、覆盖和
正性门全部通过。primary 为 `inner-two-cell-endpoint-r1.json.gz`，SHA
`16c4eeeb1e598b024c6cafc3436b7680d22aa80bfc9f92fa46ef983b999477c7`。

| 输出 | 新完整上界（十进制只显示） |
| --- | ---: |
| 单模 94 | `4.41302371001014e-65` |
| near，94..184 | `4.3728220926566365e-64` |
| rest，186..8190 | `2.943054246119885e-76` |
| infinite，8192..∞ | `2.4064198523831224e-83` |

三带和 13 窗输出直接保存在顶层 `actual_R100_head_band_masses` 和
`actual_R100_head_window_masses`，单位、条带与原 617… 输入完全一致。
这次改善仅减少了 cell13 初值的粗度；near94 的主项仍是完整 cell12
DQ 源预算。没有宣称全外 cut 已过，也没有把这一局部读出当作课题完成。
