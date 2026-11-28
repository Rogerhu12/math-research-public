# R262：原 G12 完整原容差、几何与实际网格组成记录

**基础数值解已完成；更强比例继续。** [R262](../results/R262-original-G12-complete-tolerance-and-base-numerical-solution.md) 把原实际 G12/M48、Q-free 场的全前缀、18552 原尾单元、真内圆领、固定帽、全部时间、reach 和三份 STL 组成。最终全域相对度量上界准确为

$$U=\frac{9903518366085737341}{4951760157141521099596496896}<\frac1{500000000}.$$

全部有限尾共有 19041 个实际原源/W 交片，无漏单元；inner collar 104 片另付。这个上界属于原非线性求解保存场，未改 g、参数、几何或相位。前缀真实 cuff 图的一 ulp 差已用全域有理微扰支付，不能略去。

## 参数、当前数据位置和再生入口

原 `frozen_profile` 为 outward、`vu=.17`、`vd=.18`、`ramp=.4`、`cycles=1`、`cut_radius=.6`、`cut_slope=.5`、`ramp_law=flat`、`ramp_eta=.05`、`delta=.07254443456654512`，这里小数均按原清单保存的 binary64 精确解释。尾的真 cuff 为 `2702159776422297/18014398509481984`。原参考 q 为 `.1`。实际校正使用 M48、G12 求积及原 C2 quintic 重 knot 空间；全部完整 knot 和实角通道保留，实际场文件及网格身份在下表。

本次工作根为 `/workspace/scratch/2ecfcd6930d6`：

- 实际 field/result：`m12-work/h2-c2-m48-g12-04r1/`；原 grid/query/source：`m12-work/h2-c2-m48-g12-04/`。
- 原前缀及真 cuff 转移：`exact-work/g12-prefix-composed.json`、`exact-work/g12-prefix-original-cuff-transfer.json`。
- 全尾：`root-work/full-tail-production/`，两个已付50单元回执和真 collar 在 `root-work/`，原24 raw分片在 `exact-work/raw-cache/`。
- 两级完整组成：`root-work/g12-whole-original-tail-composition.json`、`root-work/g12-whole-original-closed-field-composition-v3.json`。
- 同场几何：`root-work/h2-c2-m48-g12-04r1-coarse-material.json`、`root-work/h2-c2-m48-g12-04r1-regional-geometry.json`。
- 三份实际 STL 及 manifest：`root-work/mesh-h2-c2-m48-g12-04r1/`；每份 4471284 bytes。

以上可重算大数据不提交 Git/Release。丢失时按[实际 G12 生成与完整六阶段](2026-11-28-2ecf-m12-g12-single-band-actual-field.md)、[完整前缀](2026-11-28-2ecf-m12-complete-original-prefix-total-Gram.md)、[真 cuff 转移](2026-11-28-2ecf-original-g12-prefix-actual-cuff-length-transfer.md)、[原背景 depth8](2026-11-28-2ecf-original-background-depth8-extension.md)、[原尾50单元](2026-11-28-2ecf-tail-correlated-C4-adaptive-cover.md)、[真 inner collar](2026-11-28-2ecf-true-inner-collar-total-Gram.md)和[同场几何/STL](2026-11-28-2ecf-m12-g12-full-geometry-and-closed-meshes.md)的原命令及参数重生。

## 完整尾生产和组成命令

下面采用 Bash。`TASKROOT` 指新再生根，`S` 指公开课题 scripts 的绝对路径；先依前述记录准备其同名相对文件。三路生产只分配互不相交的原源编号；顺序执行同样的20次命令也定义相同数学包络。本次实际每次命令均自然返回0。用新输出目录执行，不能覆盖旧回执。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
B="$TASKROOT/m12-work"
E="$TASKROOT/exact-work"
V="$TASKROOT/root-work"
G="$B/h2-c2-m48-g12-04"
F="$B/h2-c2-m48-g12-04r1"
mkdir -p "$V/full-tail-production"
common=(--scripts "$S" --data "$B/m12-prefix-data.npz.gz" \
  --grid "$G/grid.json" --field "$F/result.json.field.npz" \
  --result "$F/result.json" --correction-bounds "$F/correction-bounds.json")
while read -r lo hi; do
  label=$(printf '%05d-%05d' "$lo" "$hi")
  python3 "$S/2ecf-m12-tail-correlated-production.py" "${common[@]}" \
    --primitive "$V/original-tail-background-primitive-depth8.json.gz" \
    --raw-cache "$E/raw-cache" --span-start "$lo" --span-stop "$hi" \
    --angular 32 --radial-order 6 --angular-order 8 --max-radial-depth 12 \
    --out "$V/full-tail-production/g12-source-$label-v3.json"
done < <(python3 - <<'RANGES'
for lo in range(20,17020,1000):
    print(lo,lo+1000)
for lo,hi in [(17020,17470),(17500,18500),(18500,18552)]:
    print(lo,hi)
RANGES
)
reports=("$V/g12-tail00000-00020-adaptive.json" \
  "$V/g12-tail17470-17500-adaptive.json" \
  "$V/full-tail-production/"g12-source-*-v3.json)
python3 "$S/2ecf-m12-tail-cover-composition.py" "${common[@]}" \
  --primitive "$V/original-tail-background-primitive-depth8.json.gz" \
  --raw-cache "$E/raw-cache" --inner-collar "$V/g12-true-inner-collar-total-gram.json" \
  --reports "${reports[@]}" --out "$V/g12-whole-original-tail-composition.json"
python3 "$S/2ecf-m12-complete-original-field-composition-v3.py" "${common[@]}" \
  --prefix "$E/g12-prefix-composed.json" \
  --prefix-transfer "$E/g12-prefix-original-cuff-transfer.json" \
  --tail "$V/g12-whole-original-tail-composition.json" \
  --two-jet "$V/h2-c2-m48-g12-04r1-coarse-material.json" \
  --geometry "$V/h2-c2-m48-g12-04r1-regional-geometry.json" \
  --mesh-manifest "$V/mesh-h2-c2-m48-g12-04r1/mesh-manifest.json" \
  --out "$V/g12-whole-original-closed-field-composition-v3.json"
```

## 真实执行与保留的失败

三个完整尾 driver 各自有限结束，20个新范围全部退出0；最后范围结束后，完整原尾组成器实际退出0。首版整闭消费者误把原清单 `rCuff` 断言为字面量 `.15`，真实退出1，旧失败回执保留。检查追踪到前缀辅助图的 $2^{-55}$ 差后，严格前缀转移和整闭 v2 均实际退出0。最终 v3 只把输出的“中央圆柱”标签澄清为“中央端迹”：整个正长中央邻域已由 prefix 覆盖，不另引入一段曲面；真实完整检查仍退出0，度量/几何量不变。

补充FTC原函数余项方法及较浅C4试验不参与本条主证明；全尾只使用先前冻结的原v3生产者及旧50单元的自有回执。保存场的优化接受仍是原实际G12记录，所有本次数值包络细分不新增接受。旧 M14/M15/M16 失败、LSMR平台及其他场的较坏连续界保持，不改写为已完成。

基础全域 $U$ 与旧实际 $L_{12}$ 的准确比较给真实误差下降大于9.79415倍；其完整加密账本由 R262 第4节说明。旧STL manifest中的历史 `false` refinement标记不改写，本次同SHA全闭证书补齐其数学条件。没有据此证明无限序列的C2收敛或精确等距极限存在。

## 核心身份

| 对象 | SHA-256 |
|---|---|
| 原数据 | `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0` |
| 原grid | `94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0` |
| 实际field | `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8` |
| 实际result | `ec5a051715e9609c07082924c7872dd3eec0e183bdc660139f452108644b1e57` |
| R226校正界 | `d72e798d220014dbb553c4a54e06cf478a5f3be5154eacf78f67d2ffec2212a2` |
| 完整前缀辅助包络 | `7bd26dfa01ee9f9f910ac9839f438693bb5f3514e5cb486d81da8903160130d1` |
| 前缀真cuff有理转移 | `ae41d242d61e20731fc362fe46c245e87657d45cbe6408bf71c256c7b9ee4f31` |
| 原背景depth8 | `9f208c790470849af024bc15ac8bb961edc5dfb02f97332a1abef8b9a5a8c264` |
| 真内圆领 | `533d27c7d16f653dbb6426ea514f6ac0cf90e05a0c1371be0e90a77a98af9954` |
| 同场R249 | `a3acf6055e3a937aed730abf033957edf1ae0e9b0afb81ee602abcda10e2096a` |
| 同场R253 | `e9debef013807560ee7156b683fe5a07f51d7f2b6768d71e92c884223975b60c` |
| 三STL manifest | `c0f9624c5e01888c79a62de810a69c60423dd507b41608a576b3b6313cc5802b` |
| 原尾生产者 | `d7b6c58f17c8b61e64eb2ad57ed21306abaf0a6633fdeb1299b410c7c167bcc7` |
| 完整尾组成器 | `45b4c852afe1c58870d8490aa7fbd439061e719be4a3888ecf9ece391a7a69a0` |
| 最终整闭组成器 | `1e28eaafa81f7807ebf9e89f7e5bf4bf496ea3c95ca678be7015997fadd6b947` |
| 完整尾报告 | `16d5ac300ef24c48b6db5d923abdce3a003c192aa20c1d04a897e296a2efe611` |
| 完整闭场最终报告 | `7f965171e75d897b0f1a86f2cfb3cc697087a1b84f8fea650514320a5c4c093f` |
| 首版两步执行（保留失败） | `b1b49eb3d62104620c7ad1afda8e873b5d4de39c34450a6a712b9714d015123a` |
| 真cuff后v2成功执行 | `aec6b6a99723ec95520b67ba4035d558530cd94af7c801a7c3aa59804ddb8108` |
| 最终v3成功执行 | `101c9ba3a0fbb074c01926cc7ee5462978e1f3809ee998dc45201011ee30eb84` |
| 尾driver 0 完整退出 | `825ba5da6402af80aba12a190a94c60a00bdb652cd35a90e2f04bc811557277d` |
| 尾driver 1 完整退出 | `49f51da6e721b72cd9d32c52ee6cb046a865a389fc90ed5583735cba6c60eb1a` |
| 尾driver 2 完整退出 | `0bb4165aa62fd8c19b87f86ad23eaf7c6ef8b16f2f9e572e344d9ae4c6f37ad9` |

## 22份互补原尾回执

每项都含其实际row stream的SHA；完整报告逐片取最大并检验无漏、无重及原角恒等式。严格决定使用报告中的准确分数。

| 原源区间（左闭右开） | 报告SHA-256 |
|---|---|
| [0,20) | `a9de6eae53887dc247e98c06089e2239c50ea2e614f9166c8db8484e152f6cba` |
| [17470,17500) | `bebad33b9ba82c59cca905f20024043f9268926626f2556c34e0038968e1a884` |
| [20,1020) | `a120ce8fe160ac617adcc818e7ac517248c64a2c251407f570b866a19752d7af` |
| [1020,2020) | `51915587768270c3a9f4e60cf9673b5a400e1bff8c81769ca5edc94e10fc46c3` |
| [2020,3020) | `d5cbfa770a929d86d394734aafddc63eff11be44f2b41a997343c8fa0869df24` |
| [3020,4020) | `cf6fa40483ebaaed7d15a94cd7c3b7a478685c979f9a150f5b18352ab096b9d4` |
| [4020,5020) | `9c20f71a2072c7eac9a941879c591d12ae2514374013d776e4f3b2bb0ac141f1` |
| [5020,6020) | `1618a087c68d75d5262210f6eba4278235dd414fe4576e1028bd9ad61f79a178` |
| [6020,7020) | `8c0feb336c2c7de30e2b98149c2c97c1a5b71a3a2ad1083eb519efc55ffdab77` |
| [7020,8020) | `43250c46974a2b4e8260a48efb39466666de34c5a75a35623d641576ed5fe16a` |
| [8020,9020) | `b3970dbe68f40b5148b6e0797ae8f344addfee547166ed83d4f9a3195cf07372` |
| [9020,10020) | `b039e3e91d83bfcd4aab5cb40a5cd24bb3871c15d3f643ab093a74638f152ddf` |
| [10020,11020) | `1e11f04bae7d7b730aa82dfbea59d9e378baa4a7fed31f4a466794001c4197a5` |
| [11020,12020) | `cdf5095f7edbb36096449b1637e29212273dbf9a22356f04fb79c5e9dcb2a7fc` |
| [12020,13020) | `3c4ffde27a3ab88e9c3bf612dd9efcdadb83d60e72d415f9046ab5f15397e478` |
| [13020,14020) | `5d3611f6de2384c58934a534e3f5f0623f0181cd83a29f9892b666873eb00c7f` |
| [14020,15020) | `96e90e2b0a77219f5126469dea06aaacc44ef2b2b0046290dea8dc8d9740ef7b` |
| [15020,16020) | `236b5f7c0753509ed64ba3cd344f564cd51848e69b078f7e98444d461f3f3985` |
| [16020,17020) | `274b8d5623ad70153149ee156c787d4617fa19dad54645fbd9d381cf988b2436` |
| [17020,17470) | `3dc8a5607f3348ab5db5bc809e2cedd7eb840f7936dcaaa1e2be3f466203e350` |
| [17500,18500) | `7fa61dce94b36ac7ed7ed3df1916617491e7f183a4d052ebcb6a67d891b42d99` |
| [18500,18552) | `9d0263699fd93e966c2f10b9c322d397887b2095266d904d23c0b5799f7b1e60` |

三STL的各自SHA、拓扑与固定帽身份见R262第5节；它们是有限网格代表，不取代完整C2图的连续证明。
