# 真实前缀、开发尾及完整固定帽上的全部点对

**准确区间和几何证明。** [R271](../results/R271-gap092-three-complete-components-and-all-pairs-reach.md) 构造三个实际紧致分量，包括完整已证中央环带、两张全部开发尾以及两顶有开握持的完整 R219 帽。真实开发盘有界曲率直线测地线、外共法向、同帽双向滚动球、异侧高度与所有前缀—尾闭区间分离逐项支付。对 0≤A≤1.2 且 .50≤Z≤.53 或 0≤A≤1.06 且 .44≤Z≤.53，全部相位 reach≥.097，D_K≤3.2、held≥.64、δE≥.1609、闭握持区直径≥2.80588。K 与整闭面的差是两条待接连接带。断言的归一化尺度为三个紧集分量之并的直径 D_K。
先重生 [R267 的整个真实 gap 23/25](2026-11-28-2ecf-gap-092-accurate-full-prefix-and-all-normal-balls.md)。本次脚本固定消费其物理输出 SHA256，重新用 512 个闭格作向外有理积分/开方。证成窗口的前缀对尾距离下界分别 .197541 和 .198746，均大于 .194。对更宽 A≤1.2、Z≥.44 的矩形仅得 .174962，本条未据此断定该窗口 reach。

## 可移植重生

在含 R267 证书的运行目录 W 中执行，S 是公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-gap092-developed-cap-global-separation.py" --prefix-proof polar-gap092-entire-prefix-reach.json --output polar-gap092-tail-cap-global-separation.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-gap092-developed-cap-global-separation.py | ccd815f8f0ce9d49198044bf5bac8c30118c33215b6f8afb2a43381a2ec22dd5 |
| polar-gap092-tail-cap-global-separation.json | 16af40cd036f7ae7a9cdc66b52b8fc88efc584c4a356344d4d4252a0691be947 |
| polar-gap092-tail-cap-global-separation-exit.json | c641d3208bf4f1d64e0352ed5f5264f1e7f72cad800a324945e64908ae39a678 |
| polar-gap092-tail-cap-global-separation.log | f35e61b661dbf549825893f754f6caf6bdf347ab54987a25e99f1bdd0d798f89 |
