# 固定均值系数的小步相位 Newton

状态：**浮点有限体校正；尚无精确等距闭面或严格类型证书。**

原 canonical phase24、原 M32 对照和它们的源哈希均不改动。
本记录使用独立的 `fourfold_phase_constrained.py`，在保存的相位函数上
额外线性消元一个 mean 系数。其余两个 mean 与非均值系数继续解同一
metric 最小残差系统，$\beta_4(0)$ 与保存的 `radius_shift` 完全保留。

## 1. 为什么分步

把外环抬高的整步线性 predictor 虽改善了外环曲率，却损伤中央实际
$N$，不能直接当作单个双曲核心的新背景。因此先从 canonical 与完整
predictor 的**向量差**取四分之一，不只改 mean 数值：

\[
v_{1/4}=v_{\rm canonical}+\tfrac14(v_{\rm predictor}-v_{\rm canonical}).
\]

canonical SHA 为 `63b5513b...`，完整原 predictor SHA 为 `0491c4a7...`。
四分之一初值的 mean 为

`(.8023710959615173,-.0038748103173118064,-.058078899858606516)`。

固定第2个 mean（半径 .5 bump）于最后一个值，做 M24/n201/Q256 的
两步校正。初始正规化1e-5；实际线搜索要求在 $x\in[0,.7]$ 采样
$N<0$。这一小步尚未消掉外负环，所以没有施加外区正曲率门。
同时记录整个有限体 $[0,3]$ 的 $N$ 与 target/actual Gaussian 类型。

新增 mean 消元在小例中作了方向核查：固定系数与固定相位振幅
按约束保持，中心差分 JVP 最大差5.77e-14、相对L2差4.38e-12。
每次组装前释放已不用的诊断缓存以控制内存，数学矩阵没有改变。

## 2. 两步已经完成并逐态保存

| 状态 | 完整 metric 最大样本 | 核心 $N$ 最大样本 | 外区 actual K 最小样本 |
| --- | ---: | ---: | ---: |
| 四分之一 predictor | 2.35694535e-4 | −.404103 | −.366949 |
| 接受步1 | 5.72021026e-5 | −.432008 | −.366137 |
| 接受步2 | 5.13953999e-5 | −.429657 | −.365588 |

metric/几何诊断使用1798径向点、Q256；类型扫描使用582径向点、Q256。
第二步 mean 为
`(.8005488322452297,-.0038042846655205777,-.058078899858606516)`。
完整有限体 $N$ 样本仍负，接近有限极端的最大值约−3.09e-11；
核心较大的负余量不能与极端的趋零量混用。

末态两倍最大模长为2.57759104，腰径向差.13237125，比例.05135464，
最大绝对主曲率7.298315，最小支撑函数.9146955。
target curvature 的三个正侧零点样本插值约
`.237356,.430209,.455134`；外负环仍在，未宣称修复完成。

文件位于 `data/phase_ring_continuation/`：

| 文件 | SHA256 |
| --- | --- |
| `quarter1_step00.npz` | `12e405e635a39f1d87dd9ea0e0623ad09e77448a5ca9b9acf4fee5ca0e4cdb82` |
| `quarter1_step01.npz` | `0b3de9d4a04910409100b68e0904fc911ef93874bb57ac6c1cf3396deaf7d956` |
| `quarter1_step02.npz` | `b337961ff2a192befe9f8b85edfd700c87c46babc0dcbe2b78cd2682850bd027` |

每个 NPZ 有同名 JSON，保存该实际向量的 type/geometry、固定系数、
激活的采样门及脚本哈希；`quarter1_run.json` 保存整段 history 和
当前原函数尾/alias 诊断。step00 是初始 predictor，01/02 是两次真正
接受的非线性校正，不把初态算作完成的 Newton 步。

原脚本 SHA256：
`3956b88e336ebc46dda54c0f3cf57c2da8996a6fd8a553393d942f3e9bb4cad6`。
各 JSON 的 `run_source_hash` 与 `current_reproducer_hash` 分开记录，
本批两者相同。单固定系数脚本未为多固定支持而修改；没有通过重新
跑大计算掩盖源版本差异。

精确重做入口：

```bash
mkdir -p /tmp/visible-exact-mean
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_constrained.py \
  --start-phase topics/visible-flex-exact-nearby/data/phase_ring_continuation/quarter1_step00.npz \
  --fix-mean-index 2 --iterations 2 --regularization 1e-5 --core-N-upper 0 \
  --cache /tmp/visible-exact-mean/quarter1.npz \
  --out /tmp/visible-exact-mean/quarter1.json
```

如只续末态，将输入改为step02。各次改善都会另存 `.stepNN.npz/.json`，
不会只留下一个被覆盖的大数组。实际类型门是采样条件，仍须另付
连续径向区间、角尾与舍入的统一误差界。

## 3. 后续与新类型约束 predictor

独立的实际类型约束 LP 已产生另一个完整 predictor，重新选择了
第0 mean 的近缩放方向，并在真实非线性采样中保持中央 $N<0$、
外环曲率正。后续采用独立的 `fourfold_phase_constrained_multi.py`
固定第0与第2 mean，只让第1 mean 和非均值吸收兼容残差；
这样不改变上面已归档单固定系数脚本的哈希。
它的每一个接受态仍需独立检查，不把 LP 预测或初值标签当作精确解。

多固定消元的小例 JVP 中心差分最大差1.65e-13，相对L2差1.54e-12，
固定第0与第2 mean 按值保持。当前两步计算的精确入口为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_constrained_multi.py \
  --start-phase topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_type_constrained_predictor.npz \
  --fix-means 0,2 --iterations 2 --regularization 1e-5 \
  --core-N-upper 0 --outer-floor 0 \
  --cache /tmp/visible-exact-mean/type-corrected.npz \
  --out /tmp/visible-exact-mean/type-corrected.json
```

该输入 SHA256 为
`bf8430db367ae5d328c953dc2ba631288f75f778ea720756811a72f01c1f2449`，
固定的 mean 是 `alpha0=.7396093769906578`、
`alpha2=-.049352132159964625`。这两步已经正常结束（exit 0），
实际审计与逐接受态已永久归档，见下一节。

## 4. 固定两个 mean 的两步结果

整个校正保持第0与第2 mean 不变，仅第1 mean 及非均值系数自由。
固定相位振幅与输入的真实 `radius_shift` 也保持不变。每个接受态
同时通过核心 $N<0$ 与外区 actual $K\ge0$ 的采样门。

| 状态 | 完整 metric 最大样本 | 核心 $N$ 最大样本 | 环区 $[.3,.6]$ actual K 最小样本 |
| --- | ---: | ---: | ---: |
| 类型约束 predictor | 5.90341769e-4 | −.204456 | +.0369585 |
| 接受步1 | 1.31532006e-4 | −.396622 | +.0620292 |
| 接受步2 | 7.84528322e-5 | −.411846 | +.0635238 |

metric/几何诊断仍使用1798径向点、Q256；类型扫描使用582径向点、
Q256。第二步 mean 为
`(.7396093769906578,-.005100267374734773,-.049352132159964625)`。
全外区 $[.3,3]$ actual $K$ 最小样本为+.0293380；target curvature
只有一个正侧零点样本插值 `.23847516397747534`。全有限体的 $N$
样本仍负，靠近截断极端的最大值约−3.006e-11；核心负余量与这个
坐标退化量不同。尚未给这些采样结论补齐连续区间与舍入证书。

第二步两倍最大模长2.5524944151，腰径向差.1314559619，比例
.05150097924，最大绝对主曲率7.584655792，最小支撑函数.9016708944。
实际 $U_4(0)=.059612958013$，固定的
$\beta_4(0)=.2074748402240008$；二者不是同一个振幅规范。
腰圈 detII 样本范围为 $[-1.84313,-.540794]$，
$N$ 为 $[-8.66506,-.411846]$。

文件仍位于 `data/phase_ring_continuation/`：

| 文件 | SHA256 |
| --- | --- |
| `type_fixed_step00.npz` | `de513c7fa6a9278fe98dac0d23f7fbe7e2128b20ffbfe65d421b738f4b66fbd2` |
| `type_fixed_step01.npz` | `cd0f215a94f38205b06dc2cee0d77f221e2b75ab20370f6a2506016e404d1ae6` |
| `type_fixed_step02.npz` | `05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883` |

各 NPZ 的同名 JSON 保存相应实际向量的诊断；`type_fixed_run.json`
保存整段 history、来源与最终原函数尾界审计。多固定脚本的
`run_source_hash` 与当前 `reproducer_hash` 均为
`60ad13a4398fac8cf7b3b58ecda166f8e1b90864e07f52ec283fefc9828a09a9`。
单固定脚本保留上一节的3956哈希，未用新实现覆盖历史版本。

按第三节命令重做即可；也可将输入换成归档的 `type_fixed_step00.npz`。
如从已有两步状态继续，则改为 `type_fixed_step02.npz`，其余约束
不变。每次改善仍另存逐态文件，不能只保存末态。

当前Q256与无限常速原函数之间，五个径向样本的解析 strip/tail/alias
上界最大值分别为：位置3.14e-16、$x$ 一阶3.42e-16、角一阶1.58e-13、
$xx$ 二阶6.29e-12、$x\theta$ 二阶1.72e-13、角二阶7.99e-11。
这些数值使用浮点求值，**不含舍入误差，也不是径向全区间证书**。
FFT 加倍后的原函数径向二 jet 最大差6.66e-15；同一有限原函数的
实际角导数与无限 $aT$ 公式之间最大差7.41e-11。

下一项只读参数分析在不可变的第二步图上重新计算三 mean Schur 列。
那一步**放开这里固定的第0与第2 mean**，仍保持
$\delta\beta_4(0)=0$ 与同一个 `radius_shift`，用于构造返回量的
参数方向；它不应与本节仅第1 mean 自由的两步校正混为一谈。

## 5. 同一第二步图的三 mean Schur 列

本节计算已经完成。输入仍为上一节 SHA `05d3e59c...` 的不可变图，
三列各指定一个单位 mean 变化，非均值相位补正最小化同一有限加权
线性 metric 残差。计算**放开第0与第2 mean**，保持
$\delta\beta_4(0)=0$ 和原 `radius_shift`，不额外固定高度、直径、
action 或返回数。正规化1e-10。

| 指定 mean | 裸列加权 L2 | 补正后加权 L2 | 最大未加径向权的标准化系数 |
| --- | ---: | ---: | ---: |
| 0 | .0399472 | .00771155 | .00781524 |
| 1 | .666651 | .113631 | .114802 |
| 2 | .385305 | .0713139 | .0722816 |

正规化带状线性系统残差最大5.40e-15；Robin 线性边界残差最大
3.66e-15。这里的有限 L2 残差不等于实际全区间 $C^2$ 范数，三列
也不是某个已经存在的精确等距族的切向。

实际 $J\delta$ 列的 Gram 矩阵（不是正规化方程的 Schur 近似）
特征值为

`(7.58324554e-12, 1.53485827e-6, .0180556516)`。

最软的单位 mean 方向约
`(-.99480722,.00368043,.10171062)`；主兼容行的单位方向约
`(-.05738462,-.84563646,-.53066560)`，整体符号任意。
软方向是否能调实际返回量必须用同一图的真实几何参数导数另算，
不能单凭小特征值认定为固定目标度规的 gauge。

`data/phase_ring_continuation/type_fixed_step02_schur_directions.npz`
大小306760字节，SHA256
`941c19642b4e74cbe5d68c311629bbe66f05df16fca26692c541ed61d6f29629`。
其 `candidate_vector` 与归档 step02 逐值相同，三列的 mean 尾块
严格为单位矩阵。同名 JSON 包含 Gram、各列残差、输入/源/依赖
哈希以及本节主动解除的 mean 约束。

运行源与当前复现源的 SHA256 均为
`d4fbd8be48679dcb6ab972b1d8ec9bb4d89f21314961d92dd03c7ef133228462`。
这是支持用保存的 `radius_shift_knots` 识别 phase predictor 的版本；
没有修改此前旧 Schur 数据所记录的历史运行源哈希。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_schur_directions.py \
  topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02.npz \
  --regularization 1e-10 \
  --cache /tmp/visible-exact-mean/type-fixed-schur.npz \
  --out /tmp/visible-exact-mean/type-fixed-schur.json
```

求解器从 phase 数据中读取底层表示与振幅，并正常释放三个 mean；
归档输入 metadata 中的 `fixed_mean_coefficients` 仅描述前两步
校正，不会在这个独立 Schur 计算中继续施加。
