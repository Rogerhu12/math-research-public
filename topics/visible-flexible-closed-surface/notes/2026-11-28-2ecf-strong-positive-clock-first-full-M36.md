# 真实角 coast 母场的 M24→M36 物理位置加密及第一接受

**有限数值证据。** 固定 [R268](../results/R268-strictly-convex-physical-meridian-clock.md) 增长约 .006 的同一 $g$。以[54 个角依赖 coast 方向](2026-11-28-2ecf-strong-clocked-angular-coast-directions.md)的最后完整实际场（两次接受、第三次拒绝）为母场。先把已确定的 54 项固定写回位置源，再将原全部 45 个径向函数的 Cartesian 角空间从 M24 加到 M36。保留每个原角通道和原系数，新增系数严格置零。每个新增函数使用真正的复合物理 $s$ 导数，并非在 $s$ 中强认五次；角度增加不改径向时钟、角半径、端口或任何原方向。当前总维 $45\times219=9855$。

三份源各在自身角网格从原延长与母场显式重建固定的 54 项。零延拓 G10 两成本分别为 .028574922366565565、.05299012068110211，G11 metric .19410314074160112、曲率 15.962196827680213、held .6795950954642273，与母场实际观察相符。脚本保留双 G10 完整 4291840 行，原七个几何 guide、三 Gram 行、三曲率行、倒面积行和所有跨通道协方差。增强成本与 54 项阶段相同；每次都同时要求原 14 行成本下降。

首个真正 M36 正规步使用物理 $H^2$ 增量阻尼 .03，完整系统相对残差 $2.568\times 10^{-14}$ 以下。原长 1 被拒，实际步长 .5 被接受。原 14 行成本降至 .02380719979788449，增强成本降至 .04134358713557999；G11 真实峰降至 .17082202624299275，曲率升至 18.28583548854889，held 降至 .6718504063541518。G11 全 668 径点、256 个半步错移角和 540 个训练外径点仍独立。首步完成用时约 733.7 秒（含初始化）。尚无全域误差或整闭 reach；相同几何／相同 $g$ 的真实加密一步本身不足以给出收敛。

在上引两记录的 `common`、`DATA`、`SCRIPTS` 环境重生 source、clock、原 own0 及 54 项第三次尝试。实际 run `Astra-visible-flex-2ecfcd69-20261128 / clock-d006-coast-M36`，单 BLAS 线程。

```bash
python "$SCRIPTS/2ecf-strong-clock-release-fourier.py" "${common[@]}" --clock clock-H65-d006.json --observer "$DATA/polar-physical-H65-independent.json" --warm clock-H65-d006-fixed-00.json --lifting clock-d006-angular-coast-03.json --coast-dir "$DATA" --prefix clock-d006-coast-M36 --frequency 36 --steps 3 --damping .03
```

本条只登记已保存的 M36 初值 `e1c4e3d4fa315d2b978eb64306c9c1a9b4941214a4153ef7e58a32b6ae2861f0` 与第一接受 `23104929b3c344136b1833e8396e5b2de5744024178cd41643f95c0d6e2c1d2d`。母场完整 SHA 为 `2334f21a716ab7f3f4c2e4ed75bb35bb3b12986546d109a4e6015c7e960fa73f`。不把首步回执写作三步完成；报告含本次实时时间，可重算数组不提交。
