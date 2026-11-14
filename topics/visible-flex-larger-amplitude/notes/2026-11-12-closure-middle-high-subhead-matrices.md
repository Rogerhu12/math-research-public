# 中高频深头201个真实正比较矩阵

2026-11-12，exact_closure。

为补R33中频源传播所需的深段，独立入口
`computations/closure_positive_subhead_matrices.py` 已对cells24..224
及两个完整偶频窗2050..4096、4098..8190计算真实正比较矩阵。
作业56089正式exit0；resource也保存exitcode0，49.6391秒、
峰32316KiB。共1892个实际Peano面板、201个完整胞元。

输入仍是R26/R22已经核销的同一真实源与160行浅表；选择输出
子区间不改变半径积分的原锚点。每个模用
$(Q,\Xi/\nu_m)$，$\nu_m=m^2(m^2-1)/12$。绝对值的协作比较系统为

$$\frac{d}{dr}\binom{|Q|}{|\Xi|/\nu_m}
\le\begin{pmatrix}d&\nu_m a\\b_0&d\end{pmatrix}
\binom{|Q|}{|\Xi|/\nu_m},\qquad d=(m^2-4)/r,$$

其中 $a,b_0>0$ 是既有真实系数。比较矩阵各系数对m单调，
所以频窗上端同时控制该窗每个偶频，不依赖真实有符号流的
跨模单调性。标量对角准确积分为
$(r_{\rm out}/r_{\rm in})^{m^2-4}$；正Peano余项沿用R34的
已证公式。每个面板严格满足AB不超过1/4。

输出 `closure-middle-high-subhead24.json.gz` 的
`cell_rows[].positive_cell_matrices` 与旧九窗包完全同规范。
它没有包括跨胞元缩放：向外从n进入n−1时，第二分量仍须乘
$1/\rho$，$\rho=2^{11/4}$。位置相关的源到canonical转换和
变角宽由实际源消费者保留，不能直接将本包叫作源Green界。

## 可以使用的正流部分区间结论

这些是协作系统的正比较矩阵，全部面板majorant都逐项不小于I。
任意有序子区间的首尾部分面板，其正标量积分不大于对应完整
面板积分，所以同一Peano正上界也不大于完整面板矩阵。对剩余
面板将被省略的正矩阵改成I，只会逐项减小乘积；半径比的正
标量因子亦不增。因此每个已存完整cell矩阵也逐项控制该cell
内任意向外有序子区间的比较流。

这一证明可以支付消费者所需的整cell分量sup，但在浅层谷底
会过粗，不能替代tail代理已经保留源位置的本地标量核。本次只
补深段201个cell，不含12..23的高频新积分。

## 复算

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-middle-high-subhead24-resource.json -- \
  python computations/closure_positive_subhead_matrices.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-ledger notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json \
  --start 24 --far 225 --bands 2050:4096,4098:8190 \
  --out-prefix notes/2026-11-12-closure-middle-high-subhead24
```

源SHA、输入SHA、全部准确Arb端点及产品上限均记录在包中。
本包不单独证明全频头部闭合，也不改变R38的低窗边界条件。
