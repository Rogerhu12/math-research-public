# 实际43方向的原 new519 行块精确归因

## 冻结入口与范围

新增 `computations/exact_20261114_new519_rational_residual_attribution.py`，
20,457 字节，SHA256
`c76206ba6efebdaadbda2f9633722772fd7e1bd434a382ac37074bc133affa7b`。

它固定消费 actual43 的原 Q/Pi 方向，以及已经完成的三对象 exact-action 结果。全部科学算术只在本公开仓库 Actions 执行。当前仅已通过 Python AST 解析；未导入运行、未执行本地科学计算。

固定前置源：

- `exact_20261114_single_step_rational_action.py`：`9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e`。
- 原1372系统 adapter `exact_20261114_rawcell0_step_system.py`：`fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81`。
- actual43 完整 result gzip：`cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e`。

读取 frozen exact reader 的纯字节/有理数辅助函数，不调用其 `compare_action`，也不重新乘四个局部 A。原 native、RHS、J、ODE、solve、trial 均不调用。

## 原行、节点与端口

原 stage43 有12个普通 RK 步，扩展映射 `old_to_new[43]=519`。flow step11 是该 stage 最后出口，所以其 shooting 方程位于 new519，入方向为 $\delta_{520}$，出方向为 $\delta_{519}$。

原保存矩阵 short-J 已施原出口 Pi/port。三个 exact-action 形状输出使用同一端口约定，本入口不再次除 port。两条 mean 输出属于附带读出，不属于原224条形状 stage 方程，因此不加入本行块的范数。

原 adapter 的有限残差定义为保存的 binary64 减法：

`residuals[519] = out[11] - states[519]`。

这不是精确有理相减的另一个定义。本入口读取 actual43 已导出的完整原 residual 数组，取其中原始第519行；不重新用出口和节点做减法。

所有节点映射、cell 的原 stage/step/port、complete block manifest 中的原 short-J SHA，与 action 的原41 short-J descriptor 交叉核对。原 sigma519 同时与 actual43 完整尺度数组和 exact-action 的原 numberRecord 逐位核对。

## 最小新增工件

原三件取件包已有 result、完整原方向和 checkpoint。新五件取件器
`exact_20261114_fetch_pinned_gauge_row519.py`
（SHA256 `6498c160514520a3fbc64856d365e42af05a9ad51d88e6a46c149538d693699e`）
从同一已钉 actual43 ZIP 再保留：

| result 中的描述器 | 原相对路径 | 形状 | 字节 |
|---|---|---|---:|
| `original_bound_system_arrays['stage-residuals']` | `large-arrays/step-system-stage-residuals.f64le` | 1372×224 | 2,458,624 |
| `original_bound_system_arrays['original-scales']` | `large-arrays/step-system-original-scales.f64le` | 1×1373 | 10,984 |

两件均核完整描述器 SHA/bytes，并与 checkpoint 的原矩阵 `raw_array_sha256` 交叉。没有新增28/41大阵下载，没有取 G、LU 或全行 ledger。

## 同一方向上的精确归因

令 $y_o,y_c,y_r$ 分别为已经保存的：

- 原41 short-J 对实际 $\delta_{520}$ 的精确作用；
- 本次四局部 A 同次浮点传播得到的 observed short-J 的精确作用；
- 本次四局部 A 解释为精确有理数后的 RK4 作用。

三者共享原残差、方向、端口和尺度，定义

$$
e_x=\frac{y_x-\delta_{519}+r_{519}}{\sigma_{519}},
\qquad x\in\{o,c,r\}.
$$

所有224分量及以下平方范数均为精确有理数：

$$
N_x=\sum_{j=0}^{223}e_{x,j}^2.
$$

逐对保存 $d_{ab}=e_a-e_b$，并完整给出

$$
N_a-N_b=2\langle e_b,d_{ab}\rangle+\|d_{ab}\|_2^2.
$$

此外以 $d_1=e_o-e_c$、$d_2=e_c-e_r$ 保存六项总账：

$$
N_o=N_r+
2\langle e_r,d_1\rangle+
2\langle e_r,d_2\rangle+
\|d_1\|_2^2+
\|d_2\|_2^2+
2\langle d_1,d_2\rangle.
$$

每个交叉项保留符号，不能把相互抵消的项改成“误差占比”。精确相等关系逐项核对；若失败保留实际错误。最大分量只作位置读数，归因不使用“两个最大值之差”。

这些是固定原 $\delta,r,\sigma$ 上的三种有限线性行块。即使某个替换令本块平方范数下降，也不自动意味着全部1372行或原 nonlinear trial 改善；它同样不证明保存局部 A 的 root/连续导数准确性。原41未保存局部 A 的复现限制继续保留。

## 同47顺序接线

先完成四A捕获和三方向 exact-action，再读该实际 `result.json.gz` 的 SHA。然后：

```bash
python "$VISIBLE_TOPIC/computations/exact_20261114_new519_rational_residual_attribution.py" \
  --exact-directory "$VISIBLE_OUT/native-stage43-exact-action" \
  --exact-result-sha256 "$ACTUAL_EXACT_RESULT_SHA" \
  --direction-result "$RUNNER_TEMP/actual43-selected/rawcell0-gauge-correction/result.json.gz" \
  --direction-result-sha256 cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e \
  --out "$VISIBLE_OUT/new519-residual-attribution"
```


输出目录必须是新目录。三方向结果中必须确实含 `actual43-best-node520`；本入口核对完整 case、来源描述器、全部实际输入向量字节及已保存 action 差，而不是只读取 summary 范数。

输出包括：

- `input-binding.json`：完整原矩阵、行、映射、源及输入身份；
- 四个小 raw 文件：原 r519、出/入方向、原 sigma；
- `all224-exact-rows.json.gz`：所有逐分量作用、原尺度残差、平方、差及交叉项账；
- `result.json.gz` 与小 `summary.json`：精确平方范数、 signed 分解、耗时/RSS和失败回执。

有理数保存十六进制 numerator/denominator；十进制读数仅为明确近似。没有使用平方根浮点值代替精确平方范数，没有新增科学接受门。
