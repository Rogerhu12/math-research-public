# 切口重参数带的真实 R58 背景导数界

2026-11-28，Astra-held10-7c4e33ee-20261128。

这次只补此前未付的近切口背景变化界，沿用 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 的同一定义和已经证明的归一化区间，没有重新归一化、选一个区间中点或换用 sampled cache。它还不是某个完整尾场的度量／曲率证书。

物理区间为 \(K=[R_c-d,R_c]\)，其中 \(R_c=\operatorname{literal}(.3)\)、\(d=\operatorname{literal}(.02)\) 均解释为 binary64 输入的准确有理数。对同一真实背景斜率函数，实际外向区间运算给出

\[
 |w|<109/1000,\qquad |w_R|<361,\qquad
 |w_{RR}|<3217025708\quad\hbox{几乎处处／一侧意义}.
\]

这些是保守界；尤其后二项不声称接近最大值。完整准确有理上界及来源 SHA 见 [小标量记录](2026-11-28-nearcut-true-background-bounds.json)。没有因上界较宽而改用点采样值。

## 实际覆盖与导数公式

独立入口 `scripts/resume_20261128/geometry/nearcut_true_background_bounds.py` 使用已经绑定原 kernel SHA 的 `Q060TrueBackgroundOracle`。真实半径随原 source 坐标严格递增。cell0 的 segments8、7、6、5 从切口向内连续相接，每片准确划分为128个有理区间，共512盒；最内片的真实内端半径上界为 `.2768392946628974`，严格小于 \(R_c-d\)。外端是真实定义中的准确 \(R_c\)。因此这四个完整片覆盖全部 \(K\)，无需以离散半径插值来填空。

每个盒保留真实归一化参数的区间依赖，并从 oracle 的 \(w_x,w_{xx},r_x\) 和一侧 \(r_{xx}\) 包围计算

\[
w_R=\frac{w_x}{r_x},\qquad
w_{RR}=\frac{w_{xx}r_x-w_xr_{xx}}{r_x^3}.
\]

全部盒核 \(r_x>0\)，源区间分割的准确端点也逐项验证无缺口。绝对值 cusp 处用 `r_xx_one_sided_hull`，没有断言全背景为 \(C^3\)。R58 的 \(w_R\) 连续，各有限片分段绝对连续；把上述一侧界沿片积分，得到整个 \(K\) 上 \(w_R\) 的 Lipschitz 界，足以控制逆图背景差的二阶导数。

实际运行40.6017秒；完整报告 SHA 为 `d93273cac7c712de4d9fc3230a835f4f0891328b00498fa48f3faca4a7bd9f02`。定义文件、归一化复用记录、oracle 和已证明积分 kernel 的 SHA 均记录，全部源盒保留在 scratch，未入 Git。

## 再生

先按 `seam_restore_true_background.py` 的既有记录恢复同一真实背景常量及归一化证明，再运行：

```bash
python scripts/resume_20261128/geometry/nearcut_true_background_bounds.py \
  --constants /absolute/work/true-background-constants.json \
  --normalization /absolute/work/true-background-normalization-reuse.json \
  --outdir /absolute/work/new-nearcut-background
```

默认宽度为字面 `.02`、每片128盒、60位外向区间；输出目录必须不存在。把这些界代入实际新尾场之前，仍须绑定它的完整旧尾证书、真实 cut 半径、全部模式与均值。当前没有据此宣布完整闭族完成。
