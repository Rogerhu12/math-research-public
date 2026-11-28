# 保留原无限振荡尾的短二次模新输入和完整位置求解

[R285](../results/R285-elliptic-meridian-loops-close-the-true-infinite-second-mode.md) 严格解决任意真实尾线的有限回路接续。本实验另求一条较短的具体母线，改动外部有限背景、中央与前缀，冻结这条新母线的旋转度量 $ds^2+r(s)^2du^2$。旋转基底和其上的二次模都与 R262 保存的非圆 $X+C+W$ 不同。原有限/无限振荡背景在 $r\le1/4$ 保留真实源，真实 cuff 和原固定帽沿用此端口。有限观察仍未给出全域非线性误差和厚度比证明。

## 尾部、外缓段与前缀

从 [R100](../results/R100-second-harmonic-window-and-flat-tail.md) 的真实 $n=160$ 线 $\pi=0$ 出发，在原第 159 至第 0 层的全部 1440 个物理 profile 上传递正斜率方程。物理坐标用 $Q=H/r^4$，$p=r^4w(H_r-4H/r)$，则 $Q_r=p/(r^8w)$、$p_r=-12r^6wQ$。逐层缩放和累积对数保留真实方向，物理径向增量含完整 $A+\alpha B$。每原 profile 取 48、96、192 细分的四阶 Magnus，原 $r=.6$ 的 $H_r/H$ 为 5.71275438759、5.71275420518、5.71275419198。单位切端高度的原最大采样形状算子行和为 90689.27，原全部振荡尾加匹配短转角所得单位中央采样形状量约 204.60。

改在 $1/4<r<.6$ 以六段五次平滑步混合七个正斜率的对数，端点均水平至二阶。严格原始径宽为 $[16383/65536,16385/65536]$，所涉唯一原始曲线片为 $n=2,j=6$。原证明 primitive 的逆像在 $[8357777530011,8400007081657]/8796093022208$ 内，整个区间 $w=5764607523034235/288230376151711744$，导数恒零。故保留的无限尾与新缓段在真实 $r=1/4$ 连续接合。16384 个外缓段设计中选择单位 cut 高度的组合形状量约 330.58113，增加竖高 .01327，$H_{\rm cut}/H(.25)\simeq20463.09$。

由四个三次转角和三个匀角段组成短母线，弧长方程 $(r_s,z_s)=(\sin\phi,\cos\phi)$。给定新缓段终口的 $w$，取外端 $\phi=-\arctan(1/w)$、$\phi_s=0$，中央 $\phi=\phi_s=0$。在另一轮 16384 个设计上调整一段长度以使线性高度在中央为零。最终再以 DOP853 积分，得到三个实际长度 .020067316591739656、.5079510214300764、.1884727308154106；中心 $R\simeq1.2972826614023523$、cut 弧长 $1.470853458827246$、cut 高 $1.1335418412523464$、全半核弧长 $T\simeq1.921869818143367$。单位中央的采样前缀/尾形状量分别约 51.31/51.46。这里只报告有限 shooting 读数。

## 非零幅实际源及位置更新

以真实尾部线性解连同物理 $(f,h)$ 迹向外连续积分；短前缀的物理二次模遵循 R285 式 (1)。对单位中央水平振幅，把显式空间场 $f\cos2u\,e_r-(f/2)\sin2u\,e_\theta+h\cos2u\,e_z$ 乘以 $\epsilon$。中央规定真实支撑 $R+\epsilon\cos2\varphi$，物理材料由严格单调的 $R u=R\varphi-(3\epsilon/2)\sin2\varphi$ 给出；竖直一阶迹为单位轴向量，二阶径向迹为零。用跨整条半核的五次 Hermite 提升改正原种子的全部中央迹，在真实 cuff 端二阶为零。因此有限转移相位舍入不构成端口匹配证明。中央曲率半径至少 $R-3|\epsilon|$，半宽差准确为 $2|\epsilon|$。

其上加入二阶端迹为零的完整 XYZ 五次径向样条。角向 $x,y$ 各取奇数余弦、正弦，$z$ 取非负偶数余弦；表中 $m$ 表示每坐标保留的通道数。每次从完整六个空间导数计算原始相对算子误差及两个主曲率。原始尾的 17046 个径向采样含每个有限 profile 的物理标记，按 120 个移位角另观察整份深表。机器精度下极深层的多个物理半径会相同，原层标记保留；这仍是一份有限原生网格。原数学输入在第 160 层以下还具有 R100 的完整真实解。当前固定原小标记帽对相位的刚体对齐差仍有既知限制。

| $\epsilon$ | 径段、$m$ | 接受数 | 第一观察峰 | 独立移位峰 | 移位绝对主曲率峰 | 原生深表峰 |
|---|---|---:|---:|---:|---:|---:|
| 1/64 | 16、4 | 8 | .000380495 | .000374287 | 8.21392 | .000092669 |
| 1/64 | 32、7 | 5 | .000166551 | .000165568 | 8.21141 | .000114117 |
| 1/64 | 64、8 | 6 | .000055528 | .000056021 | 8.20709 | .000027680 |
| 1/64 | 128、8 | 10 | .000037688 | .000037693 | 8.27997 | .000010863 |
| 1/32 | 16、4 | 7 | .001561773 | .001530500 | 8.25826 | .000523443 |
| 1/16 | 32、7 | 9 | .002331900 | .002331680 | 8.71112 | .001995186 |
| 1/8 | 64、8 | 12 | .014212913 | .014202394 | 17.05025 | .009609473 |

同一 $\epsilon=1/64$、同一完整中央与同一新 $g$ 的四个实际位置由 Boehm 插结依次嵌入旧场，然后联合重解全部 XYZ 系数。原生深表在 16→32 有局部回升，四个整图移位峰连续下降。第一、二、五、六行的观察组为 670×144 与 650×181；第三、七行的独立组为 958×237，第四行另用 257 个移位角。附加一个允许整片帽沿轴共同平移的 1/32 位置步，在既有状态上未接受任何系数更新，最终帽位移仍为零。本表采用修正后的深部轴向二导数 $z_{ss}=-w_r/(1+w^2)^2$。早期观测器将该项写成正号；修正后 1/64 的原生深表曲率由 6.04512 改为 6.04561。此修正不改一阶度量或该态的整图曲率峰。1/8 位置的主曲率另作真实空间更新。

## 再生

取 `S` 为公开 scripts 目录、`M` 为 R262 原 M12 数据目录，`P4` 为 [原已证 primitive](2026-11-28-2ecf-original-background-depth8-extension.md) 的 depth4 输入（SHA `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9`），`W` 为新输出目录。以下使用 Bash、NumPy 与 SciPy，设置单线程 BLAS。`--out` 使用全新的输出名。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
mkdir -p "$W"
a=(--scripts "$S" --data "$M/m12-prefix-data.npz.gz")
python "$S/2ecf-r262-m2-real-buffer-seam.py" --scripts "$S" --primitive "$P4" --out "$W/g12-m2-real-buffer-seam.json"
python "$S/2ecf-r262-original-full160-m2-magnus.py" "${a[@]}" --steps 48 96 192 --out "$W/g12-original-full160-m2.json"
python "$S/2ecf-r262-full160-m2-stored-seams.py" "${a[@]}" --steps 192 --out "$W/g12-original-full160-m2-seams.json"
python "$S/2ecf-r262-full160-m2-physical-tables.py" "${a[@]}" --steps 192 --table "$W/g12-full160-m2-physical-table192.npz" --out "$W/g12-full160-m2-physical-table192.json"
python "$S/2ecf-r262-m2-short-oscillating-meridians.py" --full "$W/g12-original-full160-m2.json" --power 13 --coarse 18 --fine 128 --out "$W/g12-original-m2-short-meridians.json"
python "$S/2ecf-r262-m2-finite-outer-buffer-actual-II.py" --source "$W/g12-original-full160-m2-seams.json" --out "$W/g12-m2-buffer-actual-II.json"
python "$S/2ecf-r262-m2-buffer-matched-short-meridians.py" --full "$W/g12-original-full160-m2.json" --buffer "$W/g12-m2-buffer-actual-II.json" --power 14 --coarse 18 --fine 128 --out "$W/g12-m2-buffer-matched-short.json"
b=(--meridian "$W/g12-m2-buffer-matched-short.json" --buffer "$W/g12-m2-buffer-actual-II.json" --tail-table "$W/g12-full160-m2-physical-table192.npz")
run() { local fn=$1 ep=$2 k=$3 sp=$4 mo=$5 out=$6; shift 6; python "$S/$fn" "${b[@]}" --epsilon "$ep" --steps "$k" --spans "$sp" --modes "$mo" --out "$W/$out.json" "$@"; }
refine() { python "$S/2ecf-r262-m2-nested-physical-coeffs.py" --parent "$W/$1.json" --out "$W/$2.json" --spans "$3" --modes "$4"; }
c=2ecf-r262-m2-complete-physical-continuation.py
d=2ecf-r262-m2-dense-physical-continuation.py
f=2ecf-r262-m2-finer-physical-continuation.py
p=g12-m2-physical-eps1over64
run "$c" .015625 14 16 4 "$p"
refine "$p" "$p-prolong32" 32 7
run "$c" .015625 12 32 7 "$p-nested32" --parent "$W/$p-prolong32.json"
refine "$p-nested32" g12-m2-physical-nested64-seed 64 8
run "$d" .015625 9 64 8 "$p-nested64" --parent "$W/g12-m2-physical-nested64-seed.json"
refine "$p-nested64" g12-m2-physical-nested128-seed 128 8
run "$f" .015625 10 128 8 "$p-nested128" --parent "$W/g12-m2-physical-nested128-seed.json"
run "$c" .03125 16 16 4 g12-m2-physical-eps1over32-final --parent "$W/$p.json"
run "$c" .0625 10 32 7 g12-m2-physical-eps1over16-nested32 --parent "$W/$p-nested32.json"
run "$d" .125 12 64 8 g12-m2-physical-eps1over8-nested64 --parent "$W/$p-nested64.json"
```

| 源码或产物 | SHA-256 |
|---|---|
| `2ecf-r262-m2-real-buffer-seam.py` | `7cb6d8d8a5cde9cd38dc034e604c5da29dddd4cd716beb83ab111b0c2f7c977c` |
| `2ecf-r262-original-full160-m2-magnus.py` | `7d095165a8d6b58849e2f5dd3d5677b4691992531cb4ebcbbf28e8cd8516e42a` |
| `2ecf-r262-full160-m2-stored-seams.py` | `9ecf5533454b261b91779aa7edaaa8f1d463ccbf1ccfb93cd07730c3d771b0ab` |
| `2ecf-r262-full160-m2-physical-tables.py` | `fc5b84c9f129ecf07a5f62b1f6f13133a84db2b5a78566572aac72619196afc4` |
| `2ecf-r262-m2-short-oscillating-meridians.py` | `33f824c48834fea1ba927cdd1e2b908080479d580f1ef47db4e880ba69402fac` |
| `2ecf-r262-m2-finite-outer-buffer-actual-II.py` | `3eca3bfdb15bb2ae2a66b146ba2656f06757643e15cb8d7a3b2fb29e3fcd1939` |
| `2ecf-r262-m2-buffer-matched-short-meridians.py` | `493c4bce0ecb6000c41a37196fa0495ed958a3d694c732a756b9ea44679334d0` |
| `2ecf-r262-m2-complete-physical-continuation.py` | `363590687c755dc320cfa98ec6893764be6eae0f4322ee6eae9d93e65b60de82` |
| `2ecf-r262-m2-nested-physical-coeffs.py` | `7825a12bb158c6c1f135160a964a910501788c67c00b82815c76c275cc231771` |
| `2ecf-r262-m2-dense-physical-continuation.py` | `6fcccc5a2dea356c28ca683c632b1608a71054b4a266a912956341a294be5b55` |
| `2ecf-r262-m2-finer-physical-continuation.py` | `f39beb12745c598e757b468704e17981e4c525139169ce67e317d780b11dea97` |
| `g12-m2-real-buffer-seam.json` | `99478ce2672f62e41754a26c11f123be3cc290936a4c184d87a65e342ab45d4c` |
| `g12-original-full160-m2.json` | `89aa0eba12aeeab72150bd70ef59da541e1d18049b1a7ef9915869474dac2382` |
| `g12-original-full160-m2-seams.json` | `ada9f3f374a3209e28cf6cdb2c208828ab4c1059a9d8d8767bffa2bbf0a24ad4` |
| `g12-original-m2-short-meridians.json` | `df133a774216bea8dcca61a8ace8767736deecfb27431a62957191c2b89eeeab` |
| `g12-full160-m2-physical-table192.json` | `787916536da5b37e0be24b308dd202d8a75ac1b9b15a3755e20cfc00ac7aa28f` |
| `g12-full160-m2-physical-table192.npz` | `05bde4ce9d0599c69d2deffdd1c1c7c164b7d6ad5c0e265293ec24f91f023a84` |
| `g12-m2-buffer-actual-II.json` | `1ec215392da7e5cc1a7ce894b8844559cd72ccdca79842d36868031efbc50138` |
| `g12-m2-buffer-matched-short.json` | `2fb4d1f487c121b118f625f17b6fd3a9dd8b761199cb3c1fa9b8d94af87b054d` |
| `g12-m2-physical-eps1over64.json` | `b80e100bb1facb83dda1e9b6654ce3d8408483196448d2f092262e18558445b4` |
| `g12-m2-physical-eps1over64-nested32.json` | `01d200b2a3c1269a0ae190b0d7b9d8dd9deb48f62e1471be2076646f6c141779` |
| `g12-m2-physical-eps1over64-nested64.json` | `e08ec39aa62dc840b43084a7247d75847f1f7f71e0260d6080fa7da8afa48260` |
| `g12-m2-physical-eps1over64-nested128.json` | `f465568816c2d41f60a80db623fb7071193337d4d2b361aa2ec0c4bbc699896b` |
| `g12-m2-physical-eps1over32-final.json` | `ace1f264430767bd7dbb57352568cd134d275c794c2b8c88f57c3b1ef216bb76` |
| `g12-m2-physical-eps1over16-nested32.json` | `51c052d400654a013260cb74798beb02b625e5ff2788f79631fd71f3d0b84b0f` |
| `g12-m2-physical-eps1over8-nested64.json` | `0af1758f367887d6f73caceaabe02d761d6d376005b135f4cdb24e51c485ec60` |
