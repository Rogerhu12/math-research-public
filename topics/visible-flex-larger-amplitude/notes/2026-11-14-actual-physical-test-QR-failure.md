# 新 R252 物理角边界的完整 QR 实际结果

状态：**数值证据／失败尝试；没有新接受场。** 本次与 request13 使用同一699节点和完整物理角方程，仅恢复原完整 separated QR 线性后端。

## 实际身份与来源

- request14，[run43596465579](https://github.com/Rogerhu12/math-research-public/actions/runs/43596465579)，source 7b66e4482374e9328c4c67c94d373bad1d5bfce1，job132451945179。
- 12:46:38Z 创建；实际全求解在12:50:28Z exit2，后续闭合/R249跳过；publisher普通推送2d1a128成功。
- artifact14114552872，20,443,420 bytes，ZIP SHA f5069ad32fe4a9fd52c1e21ba9f2c8b05bf3bed8c1d72e285d46173aa959aef0。
- [原报告目录](public-actions-43596465579-1-coupling112physicalqr/)保留小文件；[publication](public-actions-43596465579-1-coupling112physicalqr/publication.json)逐项记录26个原输出，超过5MB的pending仅artifact。
- 新独立入口 SHA256 430a918c988252156ab4efe1580a54da83a77f0f0779bfe5c0b91f8f80ddef69。实际编译通过后运行；完整R252、原物理/core/scalar、原非线性门与真实尾不变。

主要依据：[reduced-001](public-actions-43596465579-1-coupling112physicalqr/full-DN112/reduced-001.json)、[driver-status](public-actions-43596465579-1-coupling112physicalqr/full-DN112/driver-status.json)、[FD](public-actions-43596465579-1-coupling112physicalqr/physical-response/response-check.json)及该run原日志。

## 新小块确实改善，但完整回代仍不准确

实际全J FD再次通过，Richardson最大9.650162479919298e−10，18.946512742秒；FD文件SHA 1fe3b4d18f84c8294f53e4621091b60584d4147169b6d898422c092f29c3590f。

完整QR453×699/free112用126.921022437秒，峰RSS768584KiB。实际末端小块condition119589.80909759151，与request13用同一旧Uend的小诊断一致；独立SVD报告119589.80909759157只是计算末位差，所有所列阈值rank112。它没有解决全段回代误差：

| 原完整残差位置 | 最大绝对值 |
|---|---:|
| 物理collocation | .00047862814045515286 |
| 常值core行 | 8.326672684688674e−17 |
| 常值参数行 | 3.3306690738754696e−16 |
| 左BC | 2.834538206068217e−15 |
| 新右BC | 4.067065843866249e−8 |

原RHS最大.0071105950777444905，因此完整相对残差为 **.06731196689194341**。最坏在interval697、物理row332（z107）。方向最大352.4182215783007；入口三参数方向为[-.9095536502690355,.28156797593045507,.8161755597379171]，cut端常值漂移近roundoff。

与request13完整band LU的方向352.4392787582113及接近的三参数方向相比，巨大方向在两个完整消元中相近，不能全归因某一次band分解误差。反之，QR的全残差远大于band保留校正后的8.22590e−7相对残差，不能据小块condition恢复就宣称完整线性求解已准确。

reduced-001.json 的SHA为75c95a020334243572f8d82686263ccc938448e13ad64ef9431ec7605290aa8b，完整小packet SHA53616b7c71c06d3c4927c345a8867604d2e8d55eda3fc144b462b7f4e1cfb906；均已发表。

## 原非线性结果与未记录的信息

原17trial回溯没有接受更新；随后原插值到966节点，current域无效，status2、RMS=None、边界9.607979435481746e−8，elapsed161.643184603秒。phase为inner-newton-not-accepted，new_coupled_finite_acceptance=false。

这个QR入口保留原QR诊断，没有安装band入口的逐trial域记录。因此这里只报告真实回溯未接受和日志中的invalid-current，**不补写**每个trial是否全部非有限或具体坏节点数。它仍严格复用自己的真实零锚一次，新H worker请求0；失败不是非零尾求解失败。

超限pending5,959,614 bytes，SHA7ba1741992af376396004a7c7143e95a23a114c094ce29c019e9f6e00d1f3f27，只在artifact；driver-status SHA ddfeccc8c0b628d2feda492060c928d926942ff83b2303638ce504add6e01d39。

## 接续

不重复同699/新Rφ/原QR。request15/run43596755251已实际通过仅末bridge解析补点的原完整域/RMS预检与真J FD，并进入其完整带LU；具体新节点数、局部L/R及全方向仍按其实际产物报告，不能从step成功臆填数值。

[R255](../results/R255-circle-reference-linear-isometry-and-coast-shear.md)只给未截频精确圆的解析参照，解释coast大剪切与bridge局部尺度，不把它套成当前有限Jacobian恒等式。待实际加密结果分辨网格效应；如仍失败，继续选择保持全部原方程和最终容差的有依据全局化，不能以增广常值行的软最小二乘把变化的c(s)/p(s)冒共同g。
