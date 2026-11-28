# 在 p32 的实际完整两组 G10 上投影握持支撑平面

取[p32 同 g 真实七项几何峰势](2026-11-28-2ecf-stadium-p32-seven-physical-guides.md)的第三态。对每个实际 $X_0(s,u)$ 和两个 $p_\pm=(0,\pm A,0)$，冻结 $n_{\pm,0}=(p_\pm-X_0)/|p_\pm-X_0|$。对新位置 $X$ 的线性条件
$$n_{\pm,0}\cdot(p_\pm-X)\ge.652$$
逐点推出对应的真实距离至少 .652。所有 $958(128+192)2=613120$ 个原训练点/支持方向都检查。用每个径点各侧最坏角做约束生成，首轮 154 个不同线性行已足以使全部 G10 行过关；完整非省略的两组原 4291840 行及 G11 在实际位移后重新评价。

此前对第一态试固定 45 度支撑 $\pm y-z\le A-.65\sqrt2$。其三组实测最大违反分别 .168262、.168270、.168434，尽管独立实际 held=.646111。在 152 个正基幅度变量且两类位移一阶导限 .35、二阶导限 8 的有限盒内，此线性程序首轮以 HiGHS infeasible 返回 1。该回执只说明这次设定的求解结果，未给严格排除证书。

新适配平面的初态真实独立 held=.64580284。第一组位移用两个真实齐次端口的 Cartesian 方向 $\Delta y=-\sin u\,B\beta$、$\Delta z=B\gamma$，各有 76 个系数。第二组把两组系数限制到各三个预定的非负平滑形状：在保留径向基的 Greville 坐标 $t_i$ 上取 $[4t_i(1-t_i)]^3$ 乘二次 Bernstein 基，再以实际 76 个 quintic 基生成物理位置函数，始终保留原夹紧端口两 jet。两次均从同一原态和同一冻结方向出发，独立角未入线性程序。导数限制沿声明的有限径点检查。目标为径向积分位移的加权线性函数，$z$ 权 2.5。

| 真实位移 | G10 两组 metric 峰 | G10 曲率峰 | G11 metric | G11 曲率 | G11 冻结支撑最小 | G11 真实 held |
|---|---:|---:|---:|---:|---:|---:|
| 原场 | .09594014 | 12.38234 | .10546481 | 12.65427 | .64580284 | .64580284 |
| 152 个幅度 | .23525423 | 20.47168 | .23593356 | 20.41325 | .65198869 | .65199022 |
| 6 个平滑幅度 | .13062406 | 12.38231 | .13044750 | 12.65419 | .65203192 | .65203448 |

6 个平滑幅度的完整 G10 实际 held 两组均大于 .65200254，七个实际位置 guide 和原面积障碍为零。其独立 .65203 也是真实距离；连续表面和完整时间的握持球排除仍待证明。152 个幅度的尖锐位移使曲率变差，不能据线性可行性推断 metric 或 reach。两组三组全域评价后的两个实际进程均自然退出 0。

沿用上引 p32 原完整场的 `hfargs` 与 `stadium_args`，命令如下。

```bash
python "$SCRIPTS/2ecf-strong-stadium-linear-hold-projection.py" "${hfargs[@]}" "${stadium_args[@]}" --fixed-stadium stadium-p32-new018-full-03.json --prior-guide stadium-p32-geo015-01.json --prefix stadium-p32-linear-marg001
python "$SCRIPTS/2ecf-strong-stadium-adaptive-hold-planes.py" "${hfargs[@]}" "${stadium_args[@]}" --fixed-stadium stadium-p32-new018-full-03.json --prior-guide stadium-p32-geo015-03.json --prefix stadium-p32-radial-support --plane radial --distance .652
python "$SCRIPTS/2ecf-strong-stadium-smooth-hold-projection.py" "${hfargs[@]}" "${stadium_args[@]}" --fixed-stadium stadium-p32-new018-full-03.json --prior-guide stadium-p32-geo015-03.json --prefix stadium-p32-smooth-support --plane radial --distance .652 --profile-count 3
```

上述后两份实际状态 SHA-256 为 `3d5fb3f3c00e510e11b0632619189965206b159910ac3f59f81fe2b091ac1b9b` 与 `b3bcd38b8846cce8e6daa6fa6f33e5f11f4694216132b3d71ee8c96ac33ca9d6`。对应三个源码依次为 `9121c7a2242f3e445f377fc3e9ce9b1f610e7155e7aa407cd62dcb0a027adc88`、`65a4496b2631e84269eb8008a0cc3890fe05f8aca3fe506f08478e7caf5747a0`、`ecfaccce14ba3cc870bce0570e537bf40aee21b84f21c1f00f0012c75f05c3c6`。
