# 两个不同实际刚动开片与新负曲率 ramp

[R299](../results/R299-two-exact-moving-circular-patches-on-a-short-phase-Cauchy-inlet.md) 给一条新单位速、真实闭合的非解析凸中央，低、高常曲率开弧分别为 $1/5$ 和 $(\pi-.3)/(\pi-1.5)$。两个共同材料片在同一半弧度相位中分别有正、负转角。支撑在其中的任意非负光滑外法向凸起随各自的真实刚体携带，完整附件圆柱带全时嵌入且严格保持它自身的同一度量。高度 2 的两明确定义附件给指定材料端点对距离改变大于 .8575。完整闭像的 Hausdorff 比例尚待支付。

有限输入的两侧轴向圆柱长均为 .2，新 $g$ 取单位周长半径和 .06 物理 ramp，终速 .006。在真实材料 $u$ 中直接使用初值 $n=k(u),m=0, X=\gamma+.2 e_z,e_1=e_z,e_2=T,N=-N_{out}$。位置和移动标架在超采样角网上作点值演化，$n,m$ 用各自 D2 奇偶频带投影。各出口保存全部 $P,V,A$ 的真实有限 Fourier 系数，可任意复用其六个空间位置导数。四个独立自然结束的 DOP853 过程均到达同一物理终点，实际 $n$ 记录的最小值大于 .1995。

真实 Hermite 观察组使用每格三个内部 Gauss 点，用比积分 frame 网更密的独立均匀材料角，计算位置本身的全部六个导数及相对 Gram。首格左端含准确中央、常竖向和零二阶径迹。数值积分与 Fourier 误差可在粗频率处挡住只加密物理径网的收益。

| $n,m$ 频带 | 积分角数 | 独立角数 | 17 个径节点 | 33 个径节点 | 65 个径节点 |
|---|---:|---:|---:|---:|---:|
| 63 | 256 | 528 | $1.456784\,10^{-6}$ | $1.473494\,10^{-6}$ | $1.481897\,10^{-6}$ |
| 127 | 512 | 1040 | $1.082895\,10^{-8}$ | $1.100547\,10^{-8}$ | $1.109579\,10^{-8}$ |
| 255 | 1024 | 2064 | $4.991085\,10^{-10}$ | $1.574098\,10^{-11}$ | $6.354985\,10^{-12}$ |
| 383 | 1536 | 3088 | $4.990847\,10^{-10}$ | $1.572510\,10^{-11}$ | $3.950444\,10^{-12}$ |

全部组的最大实测绝对主曲率约 1.731。127 频以下形成角截断误差平台，255 与 383 频的实际径向细化均明显下降。127 频下，真实出口 $m$ 的绝对峰约 .17660；383 频时约 .17682。新增接头须从本状态的真实 $P,V,A$ 出发。

取 `S` 为课题公开 `scripts` 目录、`W` 为工作目录；依赖 NumPy、SciPy。每次输出应取新文件名。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python "$S/2ecf-r299-rational-inlet-and-two-rigid-markers.py" --cells 256 --out "$W/r299-rational-inlet-two-markers.json"
for m in 63 127 255 383; do
  python "$S/2ecf-r299-short-phase-positive-curvature-arc-cauchy.py" --scripts "$S" --modes "$m" --nodes 65 --length .06 --speed .006 --out "$W/r299-arc-m$m-h65-field.json"
done
```

最初的 63/127 两份 JSON 于附加第二圆弧的独立位置对照之前生成，因此它们的入口摘要与最终脚本有别，实际出口状态和 Hermite 计算相同。

| 源、状态或回执 | SHA-256 |
|---|---|
| `2ecf-r299-short-phase-positive-curvature-arc-cauchy.py` | `ddca29ade1f88572eb417d1756ddc9f98b706d3646a471986d6acc09a80bfc4d` |
| `2ecf-r299-rational-inlet-and-two-rigid-markers.py` | `c58fec03518404bf6e2c884fd1c7282a2f572128b0a84711dc7aec76585a1b62` |
| `r299-rational-inlet-two-markers.json` | `054c836177cbc9b318afb5233527d925398304a468034a968ddec981a53930b2` |
| `r299-arc-m63-h65-field.npz` | `42ca02e5d63cf32eeaadae73688d7a59a81d62c3e63dc311aabbdfaef3487e73` |
| `r299-arc-m63-h65-field.json` | `bec6d6e22c28e9b1764ff56328d4aceb4ae941ca6d3f3cc9f84f157c3c2da33d` |
| `r299-arc-m127-h65-field.npz` | `2c408c16e5829514820d48f8092a71d1db0e72bbd3c307bb1d693132cce30ce8` |
| `r299-arc-m127-h65-field.json` | `cc7dbacb7aa8c7c96ecb2be41c13b14827ca45a4b39e781b7e9cdbf4594e2277` |
| `r299-arc-m255-h65-field.npz` | `e44974388333ede4817ea3490becf147d5399bf72710226929f84d24ee0d2c07` |
| `r299-arc-m255-h65-field.json` | `741802d1a35bbd181cbf6bc1720030542808d81022647428b46dc43b376c605f` |
| `r299-arc-m383-h65-field.npz` | `044b0e7aa97a3842712da4a82f9e9d5d324ff6bb4f7d45ef8c5a7ebbdd6e8802` |
| `r299-arc-m383-h65-field.json` | `55f8ae678ad9c58a32a6f37a0a449565f11f3aac7b5e7f0b520a530e2ec17811` |
