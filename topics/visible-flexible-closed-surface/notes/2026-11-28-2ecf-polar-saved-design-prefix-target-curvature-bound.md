# 保存设计第7态的前缀目标 Gaussian 曲率分片准确上界

## 新支付的标量事实和范围

对实际保存的设计第7态（全部87个 alpha 及物理五次 B-spline knots 按存储 binary64 的准确二进有理数解释），本文在 **0≤s≤.1815625** 的原显式前缀 scalar recipe 上证明目标

\[
a=a_0 e^h,\qquad K=-a''/a=K_0-2(a_0'/a_0)h'-h''-(h')^2
\]

满足分片绝对上界

\[
|K|\le \frac{4757670150434392716537789033081}{79228162514264337593543950336}
\quad\text{（约 }60.0502397058346\text{）}<\frac{361}{4}=9.5^2.
\]

该证明包括每个前缀 piece 的内部、节点的两侧极限以及中央0≤s≤13/128的 K=0。它不使用 G10/G11 样点来证明上界。它只对**保存第7态的这一 provisional g**成立，不能借给后续已改变 alpha 的设计态。

这是目标标量的局部证界，不是位置场κ/reach的证书；|K|<9.5²只是与两主曲率均小于9.5不冲突的必要量级检查，不推出这样的嵌入存在。本文没有支付原目标各recipe拼接的严格两jet一致性，也未给原浮点源评估误差、connector/tail目标K或全闭reach。原数学scalar公式、存储参数和实际数值source近似严格分开。

## 证明

原源的前缀目标由中央椭圆自然平均半径、S9 ramp和正的 affine coast组成。实际输入 A≥B>0、v>0、L>0；椭圆速度逐点≥B，所以平均半径≥B。令

\[
S_9(t)=126t^5-420t^6+540t^7-315t^8+70t^9,\quad
S_9'(t)=630t^4(1-t)^4.
\]

0≤S9≤1，0≤S9'≤630/256。因此中央、ramp、coast的全部单侧片上，准确有理粗界为

\[
a_0\ge a_*:=\min(B,a_{coast})
=\frac{3631955636490541}{9007199254740992},\quad
|a_0'|\le v=\frac{3242591731706757}{72057594037927936},\quad
|a_0''|\le(v/L)(630/256)=\frac{945}{512}.
\]

其中实际 coast 常数来自已冻结 master，不重算或改变目标a0。每个保存的 quintic B-spline 用准确 Boehm knot insertion 提取 Bernstein 控制点；在17个实际前缀span内各二分5次，即32子片。对每个子片以准确差分求 h'、h'' 的 Bernstein 控制点，用凸包性质包住整个导数范围；最后跨各piece取最大，并向上舍到96-bit dyadic。

实际全前缀导数界的小数显示为 |h'|≤.305138533952553，|h''|≤55.434289812448796。每span使用自己的 M1、M2，而不是把不同span的最大值提前相乘；逐片

\[
|K|\le \frac{945/512}{a_*}+2\frac{v}{a_*}M_1+M_2+M_1^2.
\]

准确有理比较与保存的逐span输出给出开头的60.0502397058346上界。中央h完全为零，原a0为常数，所以中央K准确0。所有内部knot单侧都覆盖，未用开放区间隐藏端迹。

## 实际消费及复现

此准确核真正读取第7态、同一源的 ramp/coast masters及原数学scalar入口SHA，自然exit0；外部0.594323252999秒，peak child RSS27112KiB。新优化尝试/接受均0，它是一个已完成的证界计算，不能计作新设计或固定g接受。

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fast-step07-prefix-K" -- \
 python3 -u "$W/2ecf-polar-prefix-target-curvature-certificate.py" --scripts "$S" \
 --state "$W/polar-design-G10s-fast-step07-step01-state.json" \
 --ramp-master "$W/gap105-prefix-ramp-master.npz" \
 --coast-master "$W/gap105-prefix-coast-master.npz" --depth 5 \
 --output "$W/polar-design-G10s-fast-step07-prefix-K.json"
```

W/S按 G10完整源配方准备；ramp/coast生成命令和输入均已公开，第7设计态可按同一fast设计命令链实际重生。准确 helper 是公开 `6a65-m12-local-bernstein-angular-metric-budget.py` 中的 knot insertion，配合已公开完整 correction Bernstein extractor；没有读入未登记旧临时目录。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-prefix-target-curvature-certificate.py` | `3f5a4ae56a067f330b8b1bbb5c920549a3efe0a027eba9148d416cda3d34bd77` |
| `polar-design-G10s-fast-step07-step01-state.json` | `396fe2f485ef8d503a7677d09b1d3e66897a5638c6576668d02988c73e40b76b` |
| `gap105-prefix-ramp-master.npz` | `0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7` |
| `gap105-prefix-coast-master.npz` | `f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d` |
| `polar-design-G10s-fast-step07-prefix-K.json` | `1d4a64800a2cba82ab56244060c917edb240dcd00a6c3ef6713202aa92835c7e` |
| `polar-design-G10s-fast-step07-prefix-K-exit.json` | `b3e3006ce44e50dcb7d8f844045dad4001d98844ea8e1074ca1d4d563b49e875` |
