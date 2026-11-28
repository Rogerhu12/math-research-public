# 真实 408 系数平领连接的两项全闭形变比例

**已证明。** [R294](../results/R294-actual-raised-flat-cuff-field-whole-strong-distance-bounds.md) 直接对前条位置作全部有理 Bernstein–Fourier 闭盒，径弧分割、准确端口和真实五次附加位置逐项计入。首个 2,080,769 盒证书过宽；增加径向分割和真角象限覆盖之后，33,292,289 个真闭盒给出整上连接 |y|<.893876、|P|<1.579445、对两真实见证的距离>.650747，z<.572515。合入 R267 整中央、.4 至 .32 完整开平环、η=.05 的真实互补喉、R219 两原整固定凸帽，整个闭材料像 D≤3.2、δheld/D>.2033584375、δE/D>.0506325。整闭嵌入、法球和共同度量精度另付。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-exact-full-shape-enclosure.py" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --correction polar-released40-optimized-higher-v2-065.json --output polar-raised-065-continuous-whole-shape.json
python3 -u "$S/2ecf-polar-released-exact-full-shape-enclosure.py" --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --correction polar-released40-optimized-higher-v2-065.json --quarter-cells 4096 --depth 4 --output polar-raised-065-continuous-shape-refined.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-exact-full-shape-enclosure.py | 668e3880499774311547bddfcd443d684e75e75fd5733ea7c3a038749694a3fe |
| polar-raised-065-continuous-whole-shape.json | 133e9bb10be20533ae5978893a7444f6224119b8821b97e1cb89b77c53b5554e |
| polar-raised-065-continuous-shape-refined.json | a59d2b0f32978b33c1fdca8e826448b1ac98d58cf02ca674f83b30a11daa8f87 |
| polar-raised-065-continuous-whole-shape-exit.json | ebfe84d59518d6ef9ae86b816c7e76c29a47300050e5e3f9ad6ab2a0ea186ed2 |
| polar-raised-065-continuous-whole-shape.log | cfd0528630d0cc94f64a23842a5c8246b7fbeb060e0e6e50674e02e08f85e88a |
| polar-raised-065-continuous-shape-refined-exit.json | a1a8552ac98e8ab2acb129259f79295baacd4142db8c959ac364b20c906171d5 |
| polar-raised-065-continuous-shape-refined.log | ef26cc965a89598ca028c8dd460e25ecfe7d196a8d65c5522456eedd6e49f0c7 |
