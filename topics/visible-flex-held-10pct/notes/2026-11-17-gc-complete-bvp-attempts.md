# 三场 Gauss--Codazzi 圆领边值原型：实算记录

状态：**数值尝试，未求出合格解**。2026-11-17，子会话 `literature_mechanisms`。

## 实现

- `gc_bvp.py`：五次径向 B-spline；`L,N` 用 `cos(2ku)`，`M` 用 `sin(2ku)`；未知包括 `a` 与总弧长 `S`。残差就是原 Gauss 和两条 Codazzi，全程不除以 `N`。
- 初始 `a0=perimeter(ellipse)/(2pi)`；`a'=a''=L=M=0`。`N=a0^2 kappa_ellipse` 由完整角向函数作固定边界 lift 保留，不用低模截断替换初始椭圆。
- 终端 `a=.25,a'=-1,a''=0,L=M=N=0`，通过基函数零空间精确满足。为与可微的原方程兼容，也施加 `N_s=M_s=0` 于两端，以及终端 `a'''=0`。
- 曲率预算用正交二形矩阵 `[[L,M/a],[M/a,N/a^2]]` 的最大绝对特征值，默认软限 12。此处是待实现第二基本形式的曲率；当 PDE 残差非零时，不能直接把它当作实际重建曲面的曲率或 reach。
- 解析 Jacobian 的随机方向中心差分检查：步长 `1e-5` 时相对误差 `4.740855987e-11`，步长 `1e-6` 时 `3.065605011e-10`。未发现明显导数实现错误。
- `gc_bvp_seed.py`：把真实 Gauss--Codazzi 局部前缀与一个仅作初值的 Hermite 尾段相接，然后优化原方程。尾段没有被宣称等距。
- `gc_bvp_reconstruct.py`：独立积分移动标架以实际重建 `F`，再用角向谱微分检查 `F_u`；报告真实重建的度量误差、终端偏圆误差与最大高度。

这些脚本另依赖 `gc_prefix_explore.py` 中的等弧长椭圆初值函数。所有文件都小于 30 KB。

## 结果

下列 PDE 残差按正交坐标归一，即 Gauss 除以 `a^2`、第一 Codazzi 除以 `a`、第二 Codazzi 除以 `a^2`。

| 初始 B | 径向控制数 / 最大角模 k | 弧长上限 | 最终 max PDE | 重建高度 | 重建最大相对度量分量误差 |
|---:|---:|---:|---:|---:|---:|
|1|12 / 1|3.5|5.8390e-4|未检查|未检查|
|1|24 / 1|3.5|1.6124e-5|未检查|未检查|
|.99|24 / 3|1.8|9.4155e-4|未检查|未检查|
|.9|16 / 3|1.8|1.7042e-2|1.02707|4.4984e-2|
|.9|24 / 4|1.8|1.1575e-2|.95818|2.8865e-2|
|.9|24 / 4|1.4|5.5833e-2|.59480|1.0959e-1|
|.7|16 / 3|1.8|9.8550e-2|1.10739|4.4365e-1|

`B=1` 径向基准有已知精确旋转解，其残差随样条加密下降，说明程序能够分辨基本的径向离散误差。此验证不证明非旋转问题可解。

`B=.9` 的自由弧长单外张尝试会把 `S` 推至约 3.31，最大 PDE 仍约 `3.86e-3`。限制 `S<=1.8` 后，单外张、两/三次变号、真实 GC 前缀加尾段等多种种子都落入同一个平台，24 控制 / 4 模结果如表。对该场在更密的径向角向点重新评估，误差仍在低频和末段，不能归因于只漏了高角模。

特别是 `S<=1.4` 的图形重建高度确实小于 `.9`，终端也接近半径 `.25` 的圆（最大偏差约 `.00619`），但度量误差达约 11%。这正说明“帽子很短、端圈看起来圆”不能替代等距残差检查。`B=.7` 更未通过。

## 可复现命令

在同一目录放置脚本，NumPy/SciPy 已安装：

```sh
OPENBLAS_NUM_THREADS=1 python gc_bvp.py --B .9 --nc 16 --K 3 --flare 0 --oscillation .8 --waves 2 --length-max 1.8 --max-nfev 400 --output gc_bvp_B09_osc08w2.json
OPENBLAS_NUM_THREADS=1 python gc_bvp.py --B .9 --nc 24 --K 4 --length-max 1.8 --max-nfev 500 --resume gc_bvp_B09_osc08w2.json --output gc_bvp_B09_nc24K4.json
OPENBLAS_NUM_THREADS=1 python gc_bvp_reconstruct.py gc_bvp_B09_nc24K4.json --output gc_bvp_B09_nc24K4_geometry.json
OPENBLAS_NUM_THREADS=1 python gc_bvp_seed.py --B .9 --nc 24 --K 4 --length 1.4 --max-nfev 400 --output gc_bvp_B09_prefixseed_S14.json
OPENBLAS_NUM_THREADS=1 python gc_bvp_reconstruct.py gc_bvp_B09_prefixseed_S14.json --output gc_bvp_B09_S14_geometry.json
OPENBLAS_NUM_THREADS=1 python gc_bvp.py --B .7 --nc 16 --K 3 --length-max 1.8 --max-nfev 500 --resume gc_bvp_B09_osc08w2.json --output gc_bvp_B07_nc16K3.json
```

主要参数输出 SHA-256：

- `gc_bvp_B09_nc24K4.json`: `9216269206d8c616fec3eb0c5ef42e6f96ea556c07c4c9c49b8c2c0932fdb8b2`。
- `gc_bvp_B07_nc16K3.json`: `05438ea11e3acfdae03a7bb24ae6350f306a2eae2417a253f3f74897efa65bc0`。

这些输出均可重算，不提交可重算 JSON；按仓库规则只保留脚本、参数与哈希即可。

## 精确部分及未解决部分

可直接登记为已证明的是 已发布的 R2 中：Gauss--Codazzi 恒等式、初始椭圆的曲率代价、Fourier 线性化，以及 `a'=-1,L=M=N=0` 强制平面圆领的端点引理。数值部分只应放 `notes/`，不应写成已证明结果。

当前未解决的是非轴对称场同时满足退化圆领端点条件的边值问题。低阶有限样条端段并未产生精确解；从这些计算不能推出不存在解。其末端低频残差提示继续应改变退化端的表示或采用已知振荡端结构，而非只延长此前失稳的单向射击。
