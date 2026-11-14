# 十六查询：只加入实际53的原中点481，并只读定位原 col 最大项

**分类：实现接口与源码事实；尚无本入口的数值执行结果。**  
**作者：ChatGPT（amplitude）。**  
**日期：2026-11-14。**

## 1. 唯一新增查询的实际依据

[actual53](2026-11-14-actual-request53-working512-and-midpoint481-limit.md) 从真实51继续，用512工作行把当前完整 QP 的最终 stationarity / complementarity 和径向修复降到很小。原回溯仍只接受 $1/64$。最近失败 $1/32$ 时，全部15个已建模2048角查询实际为正，原中点481独自失域：$\beta^2_{\min}=-0.07069334664841675$、angle948，原有限 `state.middle[481]` 产生 nonfinite原RHS。

因此本独立入口只增加**原 collocation 中点481的完整2048角**。已有左 RMS481是不同查询，保留并分别标明 kind/fraction。没有据较大步的其他失败盲增中点483，没有提高512工作行预算，没有改变原完整方程或接受门。

## 2. 冻结文件与原依赖

| 新文件（均在 `computations/`） | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_sixteen_query_domain_operator.py` | 28955 | `a92efa1735832d144cb65d617beb2d9018d7822f5cc7d3846d00757abfb2db2a` |
| `geometry_20261114_sixteen_query_condensed_warm.py` | 39265 | `b5bfc20259b2d182ac881cf9dab7062912578fb489ef17940c259082bf184815` |
| `geometry_20261114_sixteen_query_condensed_response.py` | 2610 | `9f0717bde76c7c29d86f05d3d9710bf7f1668e538ee32f99bc4167e5b731c025` |
| `geometry_20261114_sixteen_query_collocation_observer_warm.py` | 16716 | `3f9df52b6d7dc2b721c91f7c97e28421283043b35f833d1151ef408e2ce9d05e` |

实际 warm CLI 使用最后的 observer 包装；它只读包住第二项的原调用，完整数值 producer 仍由第二项给出。schema 为：

- domain：`captured-sixteen-query-original-RMS-and-collocation-midpoint-domain-v1`；
- warm：`exact-constraint-sixteen-query-condensed-complete-H-warm-v1`；
- 只读 observer：`original-return-collocation-location-observer-v1`。

原15个查询的所有源文件保留原字节，不就地改常量：

- 十五 domain：`c6581f0b8fdef4c3bc48d364c6845cff9a4244b043a4d14c772ef6fd3b2503e8`；
- 十五 warm：`f1310edc94fb3a9c9f95b5dad98e7073c1879997b9a9bdf06c5028e91f83351e`；
- 十五 FD：`3328eb649daab9b7e2da831e0fd6fa864f10f4dd6c98c51adff0ddfbe0424487`。

同样保留原 full-angle B、fixed-support C、完整QR、R270库和局部QP：

| 原组件 | SHA256 |
|---|---|
| 原 full-angle B | `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` |
| 原 fixed-support C | `0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68` |
| 原 complete regularized QR | `596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722` |
| 原 R270 condensation | `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b` |
| 原 local inequality QP | `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173` |

新入口的 `evidence`、`compact_metadata`、`project`、`choose` 函数AST与原十五入口一致。差异在新 schema/来源/父pair/typed-query 接线，不是另换优化方程。

## 3. 查询与完整支持保持准确身份

左 RMS 分数仍为原 $0.17267316464601146$。11个左 RMS interval顺序不变：

`469,470,471,472,473,475,477,479,480,481,482`。

5个中点按顺序为：

`473,475,477,481,482`。

先11个左 RMS、再5个中点，每组2048原物理角，总32768行。中点481是新组；中点482在当前新序列中的 query index随之改变，历史父producer完全保留，不重标旧组。

去重后的原 endpoint capture 仍是相同11个cell。中点481只复用已捕获节点481和482，完整端点仍469–483共15个，没有第二次完整Jacobian，也不为新中点再次构造原端点J。完整B局部支持仍

$$
15\cdot338+3=5073,
$$

完整坐标仍236036维。C基线的修正支持继续是471–482及全局 $p$ 的4059维；469、470、483的完整外部raw贡献留在 $c+B_{\rm out}z^0_{\rm out}$。C修正支持不是 H 的自由度限制。R270完整外部条件响应、109个 free core消元、3个全局 scalar保留原样。

## 4. 新中点的完整原链

基点直接读取原 `state.middle[481]` 与 `problem.mid[481]`，不拿左 RMS、线性节点平均或新 spline点替代。原中点为

$$
Y_m=\tfrac12(Y_L+Y_R)-\frac h8(f_R-f_L).
$$

所以完整方向为

$$
\delta Y_m=\tfrac12(\delta Y_L+\delta Y_R)
 -\frac h8(\delta f_R-\delta f_L),
$$

其中两端 $\delta f$ 都保完整物理Jacobian和全局 $p$ 链。设已有原角域梯度为 $\Gamma,\Pi$，新 block按原公式生成

$$
B_L=\tfrac12\Gamma+\frac h8\Gamma J_L,
\quad B_R=\tfrac12\Gamma-\frac h8\Gamma J_R,
\quad B_p=\frac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

原exact inlet/core映射和一次坐标scale除法保留，所有当前typed组参与相同 B/B转置、全角margin、逐组原complex链和原阈值检查。新真实trial仍完整运行原节点、中点、两个RMS层和rho/边界门。全角线性不等式不代替这些原非线性门。

## 5. 只读 col 最大项观察器

本轮新16包装与[原只读位置观察接口](2026-11-14-original-collocation-argmax-observer-interface.md)使用相同观察类AST；只是绑定新的16入口、SHA和准确ledger字段。它在原 `evaluate` 返回后读取全部 $698\times338$ 物理col，定位原argmax、区间/分量/带符号值及原已有节点/中点同分量。原完整 `vector` 最大项另行区分物理row和右边界row。

它只截获原本就会发生的一次 `weights(state)` 返回，把原模型 $W_r$ 保存为只读副本，之后所有trial读取同一份W；不会从trial `fm` 重算权重。基点报告在原W返回后补齐，没有第二次evaluate。原返回 finite/vector/col字节保持，nonfinite时明确完整最大值未定义，不取有限子集冒充完整max。观察异常只记error，不改变原state、W、门或退出结果。

原数学 `source_sha256`集合/schema不变；新16observer的完整source/hash单列在 `read_only_collocation_observer_entry` / `read_only_observer_source_sha256` / `execution_wrapper_source_sha256`。未来 own-schema 父验证保持原严格数学集合，并逐值保留完整父producer，不把observer执行冒成旧十五或新十六数学源本身。FD仍实际重算原完整边界导数，并保存包含观察元数据的实际warm producer；观察source另由workflow pin和独立ledger绑定。

## 6. 实际父53双SHA与输入

初次本入口必须使用：

- warm `e71a5fec344326df3b6c69ec6d298f5079034fb86eb2fa505008c35682010d32`；
- 原 status `6170aba505c2eeb5db9411f13ad502363fe1593a7d4d63faa5f0d0a37fb34938`。

公开路径为 `notes/public-actions-43634517255-1-condensedqp/fifteen-condensed-warm/`。warm为原 `warm-001.json.gz`。status公开为 `driver-status.json.gz`（157158 B），必须gzip解压还原1251975 B的原JSON再核上面的原SHA，不能JSON重序列化。后续允许真实16 own-schema warm/status pair续接；原相同scalar/状态/源/父status绑定全部由冻结validator执行。

原科学输入继续：

| 输入 | SHA256 |
|---|---|
| accepted96 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared699 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 完成的真zero112 anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原tail config112 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

当前native $H$ 与zero锚可不同；这里仍是明示affine的warm与FD，不声称求过新非零native尾。

## 7. 完整CLI合同

`ACCEPTED/PREPARED/ANCHOR/CONFIG`沿原已SHA核定的Actions恢复路径；新父目录名用 `parent53`。从 `computations/` 调用：

```sh
python geometry_20261114_sixteen_query_collocation_observer_warm.py \
  --accepted "$ACCEPTED" --prepared "$PREPARED" \
  --tail-anchor "$ANCHOR" --tail-config "$CONFIG" \
  --resume "$OUT/parent53/warm-001.json.gz" \
  --expected-resume-sha e71a5fec344326df3b6c69ec6d298f5079034fb86eb2fa505008c35682010d32 \
  --parent-status "$OUT/parent53/driver-status.json" \
  --expected-parent-status-sha 6170aba505c2eeb5db9411f13ad502363fe1593a7d4d63faa5f0d0a37fb34938 \
  --out "$OUT/sixteen-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 \
  --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 \
  --condensed-max-working 512 --condensed-dual-sweeps 200 \
  --condensed-store-root
```

原最大工作行CLI默认仍256；本具体后继显式传512，保持实际53预算，不依赖默认值猜测。只有原status报告实际1次warm进展并核 `latest_warm_sha256` 后，再调用：

```sh
python geometry_20261114_sixteen_query_condensed_response.py \
  --accepted "$ACCEPTED" \
  --prepared "$OUT/sixteen-condensed-warm/warm-001.json.gz" \
  --tail-anchor "$ANCHOR" --tail-config "$CONFIG" \
  --out "$OUT/physical-response" --angles 4096
```

原全部方向/步长/Richardson/$5\cdot10^{-5}$门不变。失败时完整artifact和pending输出仍保留，不用旧FD替新warm改标签。`condensed-root`、NPZ/大型数组沿原artifact-only归档，出版过滤不变成数值门。observer小报告在 `collocation-observer/`，不需要大数组再计算来生成。

## 8. 此刻验证范围

四源AST均通过；新domain数量/去重capture/支持由源码字面量核明，16组32768行、同11cell/15node/5073维。新warm内四个优化函数AST与十五一致；observer类AST与已冻结十五observer相同；域导数公式、完整链和dynamic导出继承原实现。新domain/entry/observer相互SHA pins与实际源字节一致。

没有导入科学模块、没有本地数值fixture或新矩阵/ODE运算。新16真实方向、原col argmax、实际trial/FD都尚待本公开仓库自己的Actions。本接口不是新完整BVP接受，也不提前认定mid481这一新增行会排除较大步的其他非线性限制。
