# 原前缀下坡、桥与 common-cut 的全角总 Gram 证明

日期 2026-11-28，会话 Astra-visible-flex-2ecfcd69-20261128。固定原 Q-free G12/M48 场，证明范围为四个完整 W 元素与全部角度。精确度量、中心相位、端点和相位范围沿用原题。下表为真实执行中各元素的最大证书上界。

|W元素|解析交集叶片|连续上界（显示值）|
|---:|---:|---:|
|70|76|1.350685871926604e-11|
|125|6|3.656616434697399e-13|
|153|27|1.2355208436861686e-9|
|157|42|6.089842493749590e-10|

四区并集的准确上界为 $12236005774166093927/9903520314283042199192993792<2\times10^{-9}$。第二种算法在 W153 的全部 27 片独立返回 $12236169650330293391/9903520314283042199192993792$。两者自然 exit 0，计时各 606.111627207 和 79.783867296 秒。其余 W 元素由后续运算覆盖。

## 实际解析延拓与余项

沿用同日 prefix16 完整相关 Gram 笔记的区间运算、真中央弧长和二元 Chebyshev 插值引理。目标正交标架下，在每个物理点先求 $Y=X+C+W$，矩阵条目为 $E=|Y_q|^2-1$, $F=Y_q\cdot Y_u/f$, $G=|Y_u|^2/f^2-1$。对每个角盒先形成 $\max(|E|,|G|)+|F|$ 的连续上界，再取所有盒之最大。经原场实系数的三折旋转、反射对称，基本角域 $[0,\pi/3]$ 覆盖整个角圆。与原全相位转动恒等式相容。

以严格区间夹住原桥的根参数，令 $\lambda=\mathrm{end}/S$，$T=S+b_{.6}-b_{.15}$，$K=\lambda T$，$n=\lambda q=Kz$。其中 $b_x$ 表示原 binary64 输入 $x$ 的准确二进有理数。枚举每个 W 元素、原 source cell、chart 段、目标段、中心校正支撑的所有相交分支。把移动的物理切点转入 $n$ 的外包区间，对交集作真实解析分支的延拓。各包按端点排序后验证无缝覆盖整个元素包。W157 在 $n=\mathrm{end}$ 截断。下坡与上坡平坦拼接段的多项式在每个小区间的局部坐标表达，从而保留导数运算中的有效精度。

桥的 $\phi=(3p_t-Lp_s)t^2+(-2p_t+Lp_s)t^3$，$f=1-L\int_0^t\sin\phi(v)\,dv$。在扩展参数域上 Bernstein 界给出 $|\phi|\le2047/1000$。对 sin 到 31 次的 Taylor 多项式做精确多项式积分得到 94 次 primitive；整个 primitive 余项按报告中准确有理数支付（小于 $2.22\times10^{-26}$）。在真实单调域，以左右端点夹住 $f$；其正阶 Jet 通过物理导数 $f_q=-\sin\phi$ 递推。原 chart 的 clamped cubic 与 $x=3/4$ 后的 quintic cutoff 都按原切点拆分。

旧 common-cut 末端准确取原查询 cache 中带分子/分母的值以及原保存的一二阶 jet，计入尾端径向到 native 的变换。以 $w=1/2$, $r=5404319552844595/9007199254740992$, $w_r=-7w/r$，$k=-(1+w^2)^{-1/2}$，$k_2=-ww_r/(1+w^2)^2$，末端三 trace 是 $T_0,kT_r/\lambda,(k^2T_{rr}+k_2T_r)/\lambda^2$。与原始末端三 trace 之差按原 3、4、5 次 Hermite 形函数补回，原 M24 系数零填充到 M64，保留原竖向符号与平均高度的既有约定。供区间消费的查询报告和 cache 都绑定到实际场的同源求解报告。

第二种算法在一批同一解析分支的实际源片中，对每片实际区间端点 $l_i,r_i$ 取 $c_i=(l_i+r_i)/2,h_i=(r_i-l_i)/2$，令 $n_i=c_i+h_i\chi$。将位置多项式及其物理 native 一阶导数多项式各自准确仿射复合到 $\chi\in[-1,1]$；分别逐系数取整批的区间包。同时取 $c_i,h_i$ 的包，通过 $n=c+h\chi$ 向原 chart、目标、C 与 W 供应器传参。每一个真实片的固定参数向量均在此参数盒中，故沿 $\chi$ 和角变量分别区间微分时，一次包住整批每个真实片的归一化高阶导数。两变量插值公式按 prefix16 引理支付完整余项。节点仍逐真实片算原始总 Gram 及系数，只有导数余项共享。该包含关系仅依赖参数集合包含每个实际向量，即使舍弃部分参数相关性仍然成立。

## 可移植命令

从公开仓库 checkout 调用。环境变量 REPO 是 checkout 路径，INPUT 指向 G12 供应数据目录，OUT 为可写输出目录。INPUT 的相对文件布局及字节身份见本页与同日 2ecf-m12-g12-single-band-actual-field、其 G12/G14 exact-query-extension 笔记；实际求解和 R226 均用同一 G12/M48 场。工作区的 INPUT 实例为 m12-work。每组五脚本保留 basename，分别存入 scripts/prefix-fast-kernel 与 scripts/prefix-hull-kernel。

```bash
set -eu
: "${REPO:?}" "${INPUT:?}" "${OUT:?}"
scripts="$REPO/topics/visible-flexible-closed-surface/scripts"
grid="$INPUT/h2-c2-m48-g12-04"
field="$INPUT/h2-c2-m48-g12-04r1"
mkdir -p "$OUT"
run_gram() {
  family=$1
  basename=$2
  shift 2
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$scripts/$family/m12-prefix-total-gram-full.py" \
    --scripts "$scripts" --data "$INPUT/m12-prefix-data.npz.gz" \
    --field "$field/result.json.field.npz" --grid "$grid/grid.json" --result "$field/result.json" \
    --correction-bounds "$field/correction-bounds.json" --query-report "$grid/exact-tail-queries.json" \
    --query-cache "$grid/exact-tail-queries.json.npz" --elements "$@" \
    --angular 32 --max-angular 128 --nr 6 --na 12 --batch 8 --target 0.000000002 \
    --out "$OUT/$basename.json" > "$OUT/$basename.log" 2>&1
}
run_gram prefix-fast-kernel g12-prefix-down-bridge-commoncut-total 70 125 153 157
run_gram prefix-hull-kernel g12-prefix153-shared-remainder 153
```

报告的 SHA-256 指定实际 run 输出；JSON 也含本机耗时，因此重生时比较数学条目和身份，运行耗时会变化。

### prefix-fast-kernel

实际报告 `g12-prefix-down-bridge-commoncut-total.json`，610763 bytes，SHA-256 `dad03ff7fa1679b6bbd70fcbff07af1750789bd376cb779f79d701568353a66a`。

- `m12-prefix-total-gram-full.py`　`ca312cf789ea68e8a24b6611dca837a30423bfd62044ba3f3cc4894888c5f2f1`
- `m12-prefix-total-gram-local.py`　`2dcf8367a6fc2f12cf05dc35f22002f77e8e8b54c6d8fa58b6bb40d2d2d8a518`
- `m12-correlated-gram-interval-kernel.py`　`1b22d0a5572e3ef95e68dcf592d90483678190e65d1e97c0c349d37a767a62dc`
- `m12-original-central-arclength-interval.py`　`a7383af52d787a048f66a6386e381c7074d596e149a1af9c3de104bea5bc5afc`
- `m12-original-prefix-source-interval.py`　`087225a239fcd85ffd2776f90f1b1ba6a4f6e20f82d174b7ff94c09a9ee7c3c4`

### prefix-hull-kernel

实际报告 `g12-prefix153-shared-remainder.json`，122096 bytes，SHA-256 `23c4a7f449f4a0deb6ea06e590d1f536738e57a6f0f6c8f9d4627ffe646d2fe3`。

- `m12-prefix-total-gram-full.py`　`7f08d341f683418c9bf130d034b81b4f8125506bcef2ae43a08b38ef5c54177e`
- `m12-prefix-total-gram-local.py`　`2dcf8367a6fc2f12cf05dc35f22002f77e8e8b54c6d8fa58b6bb40d2d2d8a518`
- `m12-correlated-gram-interval-kernel.py`　`c62057bc164af305aac63ea20d84570a34c72716bea3ae5788a4344b2c5b6ddf`
- `m12-original-central-arclength-interval.py`　`bec6fa9f1522a3ebe58916bf4f2264299fe67a5b2892c9765d560c8e67a14150`
- `m12-original-prefix-source-interval.py`　`a8bac5eb1fcac791096771b37e8421f9c39496b24c5830a32a9f456634e8cb11`

### 实际输入 SHA-256

- `data_sha256`　`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`
- `field_sha256`　`5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`
- `grid_sha256`　`94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0`
- `solver_result_sha256`　`ec5a051715e9609c07082924c7872dd3eec0e183bdc660139f452108644b1e57`
- `correction_bounds_sha256`　`d72e798d220014dbb553c4a54e06cf478a5f3be5154eacf78f67d2ffec2212a2`
- `query_report_sha256`　`1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d`
- `query_cache_sha256`　`8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf`
- `meta_sha256`　`253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`
- `bridge_sha256`　`1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`
