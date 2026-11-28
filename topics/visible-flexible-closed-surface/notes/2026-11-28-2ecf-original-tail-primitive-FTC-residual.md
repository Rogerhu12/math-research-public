# 原尾背景逆图的基本定理余项与真实215单元计算

**已证明的余项公式，附完整有限计算。** 本条保留原 G12/M48 field5778bee4、全部原数据、实际源和原 g；只改变原背景均匀值误差的一项上界。它没有进入 [R262](../results/R262-original-G12-complete-tolerance-and-base-numerical-solution.md) 的主全尾组成，R262使用先前冻结的原v3和旧50单元。已完成的全尾不需重跑。

原背景累计半径写成 $R(x)$。原消费者以四个有序控制点的三次 Bézier 多项式 $x(q)$，$0\le q\le1$，近似真实反函数，取 $r(q)=r_l+(r_r-r_l)q$。控制点有序且在 $[x_0,x_1]$ 内，故整个多项式也在该闭区间内。令

$$e(q)=R(x(q))-r(q).$$

因为原径向导数 $R_x=A+\alpha B$ 连续，微积分基本定理直接给

$$
\|e\|_\infty\le |R(x_0)-r_l|+
  \|R_x(x(q))x'(q)-(r_r-r_l)\|_\infty .
$$

实现分别使用已验证原函数的 `profile.point(x0)` 区间、原 $A+\alpha B$ 的**零阶值区间**和 $x'$ 的 Bernstein 包。不对绝对值分支处不存在的高阶导数作假设，也不对值余项求导。与旧消费者原本有效的原函数残差取最小值，得到的新数仍是严格上界。原 $|dw/dr|\le24$ 把这个误差乘24传到背景斜率的均匀值误差，再在总 Gram 中只乘实际竖向校正项。原所有角频、完整源/W交叉项及余项仍保留。

原求界在横跨超过64个 primitive 叶时改用整宽单调界；某些绝对值接缝附近这会使有效但很宽的界触发多层径向细分。新增公式直接控制累计误差，不改变背景、源或保存位置。

## 实际输出及未通过的较浅试验

原冻结v3对困难单元18284已经完成44个闭片，深度至12，U<3.213e−10；它属于R262主证明。另一个仅统一采用C4值余项的试验，在18284、最大径深4时实际自然退出0，但给 U≈8.055906221e−8>B；这是上界不够紧，不能解释成实际场违反B。

本条新增基本定理余项版本对原单元区间 **[18285,18500)** 实际运行，215/215个单元、全部角度闭覆盖，自然退出0。全范围准确上界为

$$\frac{9866096300349564977}{39614081257132168796771975168}
<2.490552851\cdot10^{-10}<2\cdot10^{-9}.$$

总内部计时825.656814272秒；第一单元18285分成18片，真实运行135.882秒。时间只记录实际执行，不参与不等式。此215单元回执本身不声称整个尾或整个闭面的覆盖，不把两个不同范围的计时作加速比较。

## 复算

先按 [R262重生记录](2026-11-28-2ecf-complete-original-G12-base-numerical-composition.md) 恢复实际同场输入、原24 raw和depth8背景，并采用其中 `common`、`E`、`V`、`S` 变量。

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 "$S/2ecf-m12-tail-correlated-uniform-c4.py" "${common[@]}" \
  --primitive "$V/original-tail-background-primitive-depth8.json.gz" \
  --raw-cache "$E/raw-cache" --span-start 18284 --span-stop 18285 \
  --angular 32 --radial-order 6 --angular-order 8 --max-radial-depth 4 \
  --out "$V/g12-source18284-uniform-c4-probe.json"
python3 "$S/2ecf-m12-tail-correlated-primitive-residual.py" "${common[@]}" \
  --primitive "$V/original-tail-background-primitive-depth8.json.gz" \
  --raw-cache "$E/raw-cache" --span-start 18285 --span-stop 18500 \
  --angular 32 --radial-order 6 --angular-order 8 --max-radial-depth 12 \
  --out "$V/g12-source18285-18500-primitive-residual.json"
```

| 对象 | SHA-256 |
|---|---|
| 原生产v3 | `d7b6c58f17c8b61e64eb2ad57ed21306abaf0a6633fdeb1299b410c7c167bcc7` |
| 较浅统一C4试验源码 | `98edaeb10f1de53c84f5586cd50eb41ea83362d310c350457daec69940c9741a` |
| 较浅试验回执 | `ab086b1857906a82e249391b6f3f302dd3aa4f10f12f9ae6f1046a507fdc5fe5` |
| 基本定理余项生产源码 | `7eee08e5fbd6ecee491e6b44ca0c1e777224ed4f3388429455bf0b73e32f726a` |
| 完成215单元报告 | `52c94397032e55c839a5a86ac46af2afdfc1c382b2e8ccb9d206d3ff16e5b5e3` |
| 完整逐片row stream | `29ba0941ae6a0b6e7f6ba53488d1b64d69ce45e48b3fa9ddab121032d32f1eb8` |
