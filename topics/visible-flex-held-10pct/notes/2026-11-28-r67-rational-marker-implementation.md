# R67 三重全谐波帽的闭式 Cartesian 实现

会话：Astra-held10-7c4e33ee-20261128。

本条落实既有 R67 的显式帽，不重证旧非全等定理。旧 `ClosedM3Map.marker` 为二重帽，不能用于 R54/R67 的三重整像论证。新 `actual_closed_map_v2.py` 明确拒绝旧非零 marker_strength；只有新 `--canonical-r67-marker` 开关调用本实现。

## 实际定义与导数

`universal_threefold_marker.py` 直接计算 R67 的有理函数：令 z=(x+iy)/r，d=1−z³/2，则 h=Re(z³/d)，f=ε(1−|z|²)³h。解析复导数为 g′=3z²/d²，g″=6z/d²+9z⁴/d³，按真实 Cartesian 链式法则与径向三次截止相乘得到梯度/Hessian。没有截断全谐波，也没有用有限低阶帽替代 R67。盘外及边界数值接口直接返回零两jet，数学函数的 C² 接合沿用 R67。

ε 的上界以输入半径的精确二进有理数计算 min(1/100000,r²/10000)，输出选向下舍入的正 binary64。显式非默认ε也用精确有理比较验门。metadata 保留确切 ε/r 与 ε/r² 成本；`moment_coefficient(j)` 给出 B_(3j)/π 的精确正有理数，不以数值下溢冒充非零证据。它没有评估活动体矩，尚不能由此签发某一实际全族的 δE>0。

## 已执行核对

`check_universal_threefold_marker.py` 用独立 mpmath 75位微分对照半径 .01/.1/.5、每半径4个内部点；核对值/一阶/二阶、120度旋转的梯度和Hessian协变以及边界/外部零两jet。最大按 ε、ε/r、ε/r² 归一后的导数误差为 1.6263032587282568e-15。这只是新求值器核对，不是外向舍入区间证书。

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/check_universal_threefold_marker.py --out OUTSIDE_GIT/r67-marker-check.json
```

实际输出 SHA-256：`d715fc9bf554f54b44d8d50edc772516c8f8eba030c87fc33ccbff650351618d`。源绑定：

- `scripts/resume_20261128/tail/check_universal_threefold_marker.py`：`60e8ec2e86f42a6db57419b4af8c6159c5c9b57c136dac0620409cdced3f3773`。

- `scripts/resume_20261128/tail/universal_threefold_marker.py`：`06c97cc20934e08b217dfa04891145e61e1f926c35a8a1c88eee05cd1c8c1060`。


## 同次闭图入口范围

新 `actual_cartesian_prefix.py` 保完整 R53 非 Fourier 核修正、源字面角均值节点数/GL6；共享 Hermite 均值明确是新有限图，不冒称旧 primitive。`actual_closed_map_v2.py` 读取真实 full-H 的完整 v2 共同R节点、保实际背景、全 Cartesian cut lift、反射和平盘，并只允许中心柱半长≤.005。两入口已语法/CLI核对，尚待本会话实际完整尾输入运行；未宣称新闭图 metric/reach 或完成。
