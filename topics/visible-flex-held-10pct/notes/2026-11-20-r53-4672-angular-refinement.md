# 同一真 R53 核心的 4672 外角细化

日期：2026-11-20。会话：Astra-held10-1b6d88ec-20261120。

本条接 [真核心区间证书](2026-11-20-m24-r53-true-core-jet-certificate.md)。2336 外角盒用于连续 metric 时已出现可定位的角包围损失，因此只对同一数学核心增加外角分辨率；没有改变 q/c/λ/profile、物理场、固定 mean1168 或任何 BVP 门。

## 1. 同一对象、同一源

输入 run.json 与 physical.npz 的 SHA256 仍为：

    c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a
    f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d

oracle 与 exporter 的 SHA256 不变：

    r53_validated_material_core.py
    743ed9b9a38cbc4ec2a3bf5b6d8d340cdc3d5c330bb37626ed453707e7bde197

    export_r53_core_angle_boxes.py
    748c56dc2ab0ab343c0719f506cd155ade58ef210c199a5718d36646c7c5afba

前两批 1168 均值节点、2336 外角节点与闭盒都保留，未重算或覆盖。

## 2. 实际终态

同源用 --nodes 4672 真实执行，exit 0，238.82 秒。包含 4672 个 literal binary ψ 节点及其完整相邻闭角盒；最后一盒的上界外向覆盖真实 \(2\pi\)，额外微小周期区间同样被覆盖。材料像在 sector/window/积分格点区间的两个端点分片取 hull，共 11004 个材料子盒，每 query 最多 5 片。

| jet | 节点最大区间宽 | 全角盒最大分量宽 |
| --- | ---: | ---: |
| \(\Gamma\) | \(1.117\cdot10^{-12}\) | .005367676 |
| \(\Gamma_u\) | \(3.648\cdot10^{-14}\) | .001499511 |
| \(\Gamma_{uu}\) | \(8.483\cdot10^{-14}\) | .005517916 |
| \(\Gamma_{uuu}\) | \(1.306\cdot10^{-12}\) | .082966431 |

范围宽度相对 2336 约减半。它们是严格几何输入范围，不是 metric 的误差，也不意味着任何尚未运行的完整径向证书已通过。

小记录只留 scratch：

    geometry-work/newg-m24-r53-core4672-angles.json
    SHA256 b78d1e73dd058f5668706810ecde1383ca9ed0a696c2ff12e24ae55c51ab89eb

新节点/盒数组同样不入 Git/Release：

    geometry-work/newg-m24-r53-core4672-angles.npz
    SHA256 714de484be1cce998f74604b9d588f38084b4e4132dc3c4b84279235aaf34f35

## 3. 字段与使用合同

psi、psi_lo、psi_hi 为长度 4672 数组；闭盒是 \([\psi_{\rm lo}[j],\psi_{\rm hi}[j]]\)。theta_point、theta_box 是 (2,4672)，由冻结 warp_e 和真 sin 进行严格单调映射包围。

point_F、point_Ft、point_Ftt、point_Fttt 及 box_F、box_Ft、box_Ftt、box_Fttt 均为 (2,4672,3)，第一轴 lower/upper，最后一轴 Cartesian。所有导数按材料 u；转换成计算角 ψ 的 H0/H1/H2/H3 必须使用完整初始角图链式法则，再减同一个基圆与同一个冻结 Fourier 投影。

bindings_json 记录 run/physical/source 身份、精确二进制核心系数、λ/S/b/k、warp_e 和末周期盒语义。mean1168 的旧严格节点数组继续原样复用，外角加密没有改均值图。

本条未证明前半 prefix 连续 metric、真非线性尾或完整闭族。后续验收须实际结合共同 Hermite 场、端点规范化 profile、固定均值和完整 lift，对整段径向范围进行证明。
