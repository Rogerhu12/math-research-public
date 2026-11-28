# 固定 G12/M48 的完整原前缀连续相对度量界

> 2026-11-28 接口勘误：本文原数值回执的校正坐标使用 `T0=S+dyadic(.6)-dyadic(.15)`；原实际场使用清单真 cuff 的 `T1`，两者差 `2^-55`。本文 158 元素的包络按 T0 保留；[准确全域转移](2026-11-28-2ecf-original-g12-prefix-actual-cuff-length-transfer.md) 将其转回同一原实际 T1 场，上界 <1.235520846e−9。不得直接把旧 common_z 端点与原尾拼接。

会话 Astra-visible-flex-2ecfcd69-20261128。证书的物理场 SHA-256 为 `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`。源是原 $X+C$，保存的 $W$ 系数与其两个端点的二 jet 均绑定此场。采用原 $g$、真实中央弧长坐标与原连续相位时间范围。

## 结论与证明

**已证明。** 对同一实际 G12/M48 场，原前缀从 $n=0$ 连续覆盖到 $n=4552634583911787/2251799813685248$，合计 **158 个实际 W 元素、2800 个解析交集叶片**。全前缀、全周向、原全部相位的最大相对度量谱误差满足

$$
U_{\rm prefix} \le \frac{12236005774166093927}{9903520314283042199192993792}
<1.235521\times10^{-9} < B=2\times10^{-9} .
$$

最大证书界来自 W153。下表逐行计数来自完成回执。四个内核采用同一物理输入，其分工由准确元素下标决定。

| 已消费内核 | 完整 W 元素数 | 解析叶片数 |
|---|---:|---:|
| production | 16 | 374 |
| sixteen | 1 | 27 |
| four | 4 | 151 |
| hull | 137 | 2248 |

完整合成实际返回 0。输出 `g12-prefix-composed.json` 为 156333 字节，SHA-256 `7bd26dfa01ee9f9f910ac9839f438693bb5f3514e5cb486d81da8903160130d1`。其中每个元素另记证据 SHA、准确 $n$ 外包与最坏有理数。前缀/尾接口的准确 $q$ 盒为 $[69797742769972307967867523814084095580150384957599279669352100545086832349862582092684651997678391529874199147761153029697/34522986914101942756511462397940635211112362320306081280476136222465278369814573371284605883242163894339263697369694208000, 139595485539944615935735047628168191160314579109964200115806805675132840953810411742057349385284086541028825451554372232019/69045973828203885513022924795881270422224724640612162560952272444930556739629146742569211766484327788678527394739388416000]$，相应 $z$ 盒为 $[69797742769972307967867523814084095580150384957599279669352100545086832349862582092684651997678391529874199147761153029697/85333086881318181633374457630123008489361001767617832872281356228535183189304745172324034713974948037191615404845609989697, 46531828513314871978578349209389397053438193036654733371935601891710946984603470580685783128428028847009608483851457410673/56888724587545454422249638420082005659578604243333768840555105680676514210898245967112038272625733185221219321907762050673]$。


从实际非均匀 W B-spline knot 提取全部不同节点 $z_j$，不改变同一张物理图；原 Bézier 提取是每个 $[z_j,z_{j+1}]$ 上原五次多项式的等价表示。$n=\lambda q=Kz$，其中 $K=\mathrm{end}\,(S+b_{.6}-b_{.15})/S$。$S$ 是两段精确目标坡长与原桥长之和，$\mathrm{end}$ 是原 source mesh 末端，$b_x$ 表示保存的 binary64。因为 $K>0$ 且对桥长单调递减，每个真实 W 元素在前缀上的交集被 $[\max(0,z_j K_{\rm lo}),\min(\mathrm{end},z_{j+1}K_{\rm hi})]$ 包含。直接由原 data、bridge 与场重建后恰有158个正宽候选；首个从0开始，末个达到 $\mathrm{end}$，排序核查中相邻外包无缝。原真切点能随桥参数微移，各片按自身实际分析分支分别延拓；这种重叠不会在真实交界处漏算任何源或目标分支。

每个 W 元素的证据如下。0–15 来自原逐元素生产回执。16 用已经完整发布的 27 片证书。70、125、153、157 用四区域证书。17–69、71–79 与80–124、126–152、154–156 用两支不相交的共享余项计算。每个叶片解析区域再切于原 source cell、原 chart/cutoff、原 target、原中央 C 支撑的所有切点，在所选完整周向基本域上先一起计算 $X+C+W$ 的三条总 Gram，含原隐式角映射、真实中央弧长和所有一次导数的解析延拓，再用含余项的插值估计包整盒。精确 argmax 不依赖各版本的显示舍入。不同版本可在离散、余项宽度和局部系数估计上不同，拼合只使用对同一张函数各个完整子域的绝对上界。

逐片区间核、中央相位与 tensor 余项的证明见同日 `2026-11-28-2ecf-m12-prefix16-correlated-total-Gram.md`。原桥弧的精确参数、common-cut、cutoff、全部分支枚举和批共享余项的包含证明见 `2026-11-28-2ecf-m12-prefix-four-regions-and-shared-remainder.md`。原源实系数的 $D_3$ 及反射使 $E,G$ 偶、$F$ 奇，故基本域上三分量的矩阵算子界对全角成立。原纯相位旋转保持该界，且固定 g 的全部时刻共用同一上界。

合成器逐输入 SHA 绑定，分别核对每个实际 W 区间的外包端点，要求每个完整元素中每一叶片记录存在且其准确有理数上界过原 $B$，将按元素分组的全部 native 覆盖与其真实 knot 外包逐端点对齐。不同解析分支兼容性已在各元素供应器中枚举。最终按元素取有理数最大，故整个真实前缀得到标题结论。native 末端是 prefix/tail 的共同物理 $q=S$，即 $z=S/(S+b_{.6}-b_{.15})$；已算及此端点。完整曲面还须与同场 tail、inner collar 与冻结部分各自的界取最大。

## 完整重生配方

在同一台设备可串行执行各条命令。环境变量 REPO 是含原 topic scripts 与下列新入口的公开 checkout，INPUT 为同日 G12 单 band 笔记中公开配方的输入/输出根，OUT 为新目录。生成输入及其哈希已在该笔记、prefix16 笔记、四区笔记登记。输出包含本机 wall time，故重生时用数学条目、原始输入与源码身份核对；下列 SHA 记录实际 run 的文件字节。

以下配方使用 Bash、Python 3 与 NumPy。在旧生产进程按 `--full-prefix` 启动时，W0–15 已各自落盘；原进程在 W16 中途失去观测，最终退出码未知。W16 的证据来自独立完成的原入口。原反向长进程在 W104 中途返回 137，shell 报 Killed，原因未证；接续进程补了 W104–102。切换代理配置时，前向与反向进程均在完整回执写盘后手动停止，均真实返回 130。新一轮从 W54、W101 启动，只计算尚缺的47个元素。两支各以最多四个元素启动新的子进程，全部组均返回 0。原连续核的数学分片和阈值未改动。

```bash
set -euo pipefail
: "${REPO:?}" "${INPUT:?}" "${OUT:?}"
scripts="$REPO/topics/visible-flexible-closed-surface/scripts"
grid="$INPUT/h2-c2-m48-g12-04"
field="$INPUT/h2-c2-m48-g12-04r1"
mkdir -p "$OUT"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
orig=(--scripts "$scripts" --data "$INPUT/m12-prefix-data.npz.gz"
      --field "$field/result.json.field.npz" --grid "$grid/grid.json"
      --result "$field/result.json" --correction-bounds "$field/correction-bounds.json")
python "$scripts/m12-prefix-total-gram-local.py" "${orig[@]}" \
  --complete-element --element 16 --angular 128 --nr 6 --na 10 --batch 8 \
  --out "$OUT/g12-prefix16-total-continuous.json"
run_elements() {
  local family=$1 stem=$2
  shift 2
  python "$scripts/$family/m12-prefix-total-gram-full.py" "${orig[@]}" \
    --query-report "$grid/exact-tail-queries.json" --query-cache "$grid/exact-tail-queries.json.npz" \
    --angular 32 --max-angular 128 --nr 6 --na 12 --batch 8 --target 0.000000002 \
    --elements "$@" --out "$OUT/$stem.json"
}
run_elements prefix-fast-kernel g12-prefix-down-bridge-commoncut-total 70 125 153 157
chunked() {
  local family=$1 stem=$2
  shift 2
  local -a items
  while (( $# )); do
    items=("${@:1:4}")
    run_elements "$family" "$stem" "${items[@]}"
    mv "$OUT/$stem.json" "$OUT/$stem-batch-${items[0]}-${items[-1]}.json"
    shift "${#items[@]}"
  done
}
chunked prefix-production-kernel g12-whole-prefix-total-gram $(seq 0 15)
chunked prefix-hull-kernel g12-prefix-forward-hull $(seq 17 69) $(seq 71 79)
chunked prefix-hull-kernel g12-prefix-reverse-hull $(seq 156 -1 154) $(seq 152 -1 126) $(seq 124 -1 80)
python "$scripts/m12-assemble-original-prefix-total-gram.py" \
  --scripts "$scripts" --input "$INPUT" --initial "$OUT/g12-whole-prefix-total-gram.json.elements" \
  --forward "$OUT/g12-prefix-forward-hull.json.elements" --reverse "$OUT/g12-prefix-reverse-hull.json.elements" \
  --four "$OUT/g12-prefix-down-bridge-commoncut-total.json" --sixteen "$OUT/g12-prefix16-total-continuous.json" \
  --out "$OUT/g12-prefix-composed.json"
```

### 新增源码 SHA-256

- `prefix-production-kernel/m12-correlated-gram-interval-kernel.py`　`1b22d0a5572e3ef95e68dcf592d90483678190e65d1e97c0c349d37a767a62dc`
- `prefix-production-kernel/m12-original-central-arclength-interval.py`　`bec6fa9f1522a3ebe58916bf4f2264299fe67a5b2892c9765d560c8e67a14150`
- `prefix-production-kernel/m12-original-prefix-source-interval.py`　`087225a239fcd85ffd2776f90f1b1ba6a4f6e20f82d174b7ff94c09a9ee7c3c4`
- `prefix-production-kernel/m12-prefix-total-gram-full.py`　`f9377e0f857c186964992b126ac614c0ec9dc7bcca207ae6cfb0dc9ac3877f33`
- `prefix-production-kernel/m12-prefix-total-gram-local.py`　`2dcf8367a6fc2f12cf05dc35f22002f77e8e8b54c6d8fa58b6bb40d2d2d8a518`
- `m12-assemble-original-prefix-total-gram.py`　`fbc6809d48176573dd8de1baec64ca6b1e5ca8effc6e2376127f3a5855ed97cc`

### 完整输入 SHA-256

- `data_sha256`　`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`
- `field_sha256`　`5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`
- `solver_result_sha256`　`ec5a051715e9609c07082924c7872dd3eec0e183bdc660139f452108644b1e57`
- `grid_sha256`　`94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0`
- `correction_bounds_sha256`　`d72e798d220014dbb553c4a54e06cf478a5f3be5154eacf78f67d2ffec2212a2`
- `query_report_sha256`　`1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d`
- `query_cache_sha256`　`8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf`
- `meta_sha256`　`253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`
- `bridge_sha256`　`1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`

本轮两支合计13个独立短进程。实际逐批结果如下；每项均含该批的源码、精确交集与完整余项。可重生输出只列散列。

| 实际批报告 | 叶片 | 秒 | SHA-256 |
|---|---:|---:|---|
| g12-prefix-forward-hull-batch-54-57.json | 70 | 138.008 | `1de20133fbcbffdec7b33086b58a8d869c6ae2ef1c71d42d889583705e3b897e` |
| g12-prefix-forward-hull-batch-58-61.json | 68 | 87.301 | `a4e8a848196792dac1d264206b09bd51633923f1e4d33e1bb7dbcee0cebef798` |
| g12-prefix-forward-hull-batch-62-65.json | 40 | 81.629 | `bf57a6a3b18af6a06b7d8a94e2acff366ebb8f319a2054ddf559d9303fc5a166` |
| g12-prefix-forward-hull-batch-66-69.json | 43 | 73.221 | `d92a0510853fb877773f4d600c3ca49e646ae29659d4d47d454e697049d67ba8` |
| g12-prefix-forward-hull-batch-71-74.json | 53 | 79.673 | `c658020e6d12b2aba88f941c251f1475ac9271553b9f7f112078ebfd7b9375b5` |
| g12-prefix-forward-hull-batch-75-78.json | 54 | 114.119 | `98b9102e8f4d50bb902d72dec6fcae4455ecdfb4bb336352062b86be76abe864` |
| g12-prefix-forward-hull-batch-79-79.json | 20 | 53.207 | `b6b84bffbe0cb21c54aab6302274fe06cdf02014fab57b297ba3bff47486bdd3` |
| g12-prefix-reverse-hull-batch-101-98.json | 97 | 124.134 | `eece2294ff8f6cf1a4225fa18e2c968b7751de42e322d2aaa8b4f97306628d7c` |
| g12-prefix-reverse-hull-batch-81-80.json | 10 | 26.532 | `fa3c89454936adb31f2c63ac30cf70f54f51f3866e80f0dda04b9a8b5b513fce` |
| g12-prefix-reverse-hull-batch-85-82.json | 113 | 148.142 | `9120a214c14ea4886a0d56015a33d72fb327e9b146f1ab0b15d0d32825e5e6a8` |
| g12-prefix-reverse-hull-batch-89-86.json | 40 | 67.948 | `a6d8cdde84a965925f70236e09526bc22390fe43bd1bca8844bfc1e27718d7f5` |
| g12-prefix-reverse-hull-batch-93-90.json | 37 | 66.573 | `63ae433a2c9f2e7163d79726e94eeb323c33b32854ac2eba2264f25c6096d773` |
| g12-prefix-reverse-hull-batch-97-94.json | 40 | 63.727 | `61dc1b4b98c9b16cd520d89e38c7ee1e687fbc96b50807628ae047405fa89356` |
