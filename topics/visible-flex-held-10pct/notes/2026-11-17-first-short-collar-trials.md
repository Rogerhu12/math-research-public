# 新短尾的前两次实际设计（均未合格）

2026-11-17；Astra-held10-f00f08c9-20261117。状态：数值证据，失败尝试。

## 对象和复现

输入是历史接受的 m2/v55v60/q20/M16 前缀的完整 Cartesian 端口两jet，源 checkpoint 在历史提交8ef38046e8b04adc6da1093c0730e1fc8747c2c9。恢复仅用于读取旧结果，未重复求解。端口N=512，材料s=1.628925980576648，平均高度1.2879820451408475；输出NPZ SHA-256为 `deecabf3efddc06cad0dc8fc63facc7d0965a9e81472cbbff22807bc6704df5f`。

本题脚本 `scripts/short_collar_design.py` 以完整端口三条Cartesian Fourier向量（含高于校正阶数的原模）定义起始二jet，用五次Hermite接到半径.15、高度增加.25的平面圆领；内部五次B样条与8个谐波类校正的全部端点二jet为零。设计参数 nc=16、m=8、length=.65，5点Gauss/样条跨及64角点优化，201×256另行采样。所有g均为设计阶段，不是固定g精化。

```bash
python scripts/short_collar_design.py --trace q20_endpoint.npz --out collar-fixed-E.json --length .65 --rise .25 --nc 16 --m 8 --nfev 120
python scripts/short_collar_design.py --trace q20_endpoint.npz --out collar-free-E.json --length .65 --rise .25 --nc 16 --m 8 --nfev 160 --free-E --seed collar-fixed-E.json
```

第一步对E取常数length²，G取该位置场的角均值；第二步允许E也取角均值。F始终为零目标。两个版本都保完整位置/两jet边界，不把不匹配拼接藏入数值误差。

## 结果与解释

|实验|真实停止|独立网格metric max|κ max|support min|E范围|
|---|---|---:|---:|---:|---|
|q20_length065_rise025.json|`ftol` termination condition is satisfied.；98次|0.002008800779|12.1214498|0.1779277854|[0.4219026495589859, 0.4233479169588191]|
|q20_length065_rise025_freeE.json|The maximum number of function evaluations is exceeded.；160次|0.0867001611|5686197.124|-0.05370496701|[1.1904473774479374e-06, 2.7129964653016203]|

固定E版达到有限求解器ftol停止，但metric约.002，不是合格解。其曲率峰在s=.68、u=0、位置约(.34900846,0,1.55117282)，κ≈12.12145；这一弯曲也超过当前完整尺寸可支出的3% reach预算。

自由E版在优化节点上的RMS降至约1.25e-5，独立网格却发现E接近零、曲率约5.69e6、支撑为负，且metric升至.0867。故它发生参数/浸入退化，不能采用节点残差作为可行性证据。后续增加严格正速度和实际曲率/支撑约束，并改用严格恒速旋转参考母线以减少Cartesian多项式表示误差。

解析Jacobian在一个固定随机方向上用1e-5、1e-6、1e-7三档中心差分核对，相对差分别约1.59e-10、4.77e-11、4.70e-10；这只核实现的一阶导数，不核存在性。

## 输出身份

本地运行，无Actions run ID；再生输出不提交。

- `q20_length065_rise025.json`：SHA-256 `486080442f3451eda6137c1f7484969e681a6e2aecae84b6f7bc2d3ae0b89874`；耗时约75.59秒。
- `q20_length065_rise025_freeE.json`：SHA-256 `10737bd3ff8094590f44171555a9bb5b5f751a76f0ff85f51c3e0f1326c5629f`；耗时约127.72秒。

仍未支付：连续全域metric、正浸入、曲率/reach、全时闭合以及固定g加密；这两次均不构成10%候选。
