# 回折开发尾两端角的真实整径线初值

**数值证据。**

取 R282 的内峰 p=.48，分别取真实端角 e=−.20 与 +.16，原喉、两帽与 gap=23/25 前缀实际保留。对两个端口分别从头求 65 个空间极角下的规定速率候选；每角 12 个实际样条间隔、三维位置由极时钟/全 Fourier-Hermite 源组成，终端和初端依实际端口函数。两输入的空间径线曲率、速度、真实轴向闭合修补与位置系数均单独保留。这里的原模型在 G10/G11 由数值端口 primitive 评价，未把有限六 jet 对比升格为连续绑定。

| 实际末角 e | 全 G10 R² | G11 metric / κ / held |
|---:|---:|---|
| -0.2 | 1454.064874 | 6.5658431503 / 56.246592097 / 0.62629064291 |
| 0.16 | 1047.518261 | 5.3819796019 / 54.72868718 / 0.6324890339 |

两种输入的独立指标都比旧单峰 ridge 的独立 1.48836/16.95694/.64932 差。真实返回尾的严格分片预算与这两个有限整连接的结果分开记录。

## 可移植重生

W 含新 gap 的 G10/G11 源及其 H65/Γ95 两份 master，S 为课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-returning-bend-full-ray-surface.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --amplitude .48 --flat -.2 --geometry-weight 120000 --field polar-gap092-returning-rays-down.npz --output polar-gap092-returning-rays-down.json
python3 -u "$S/2ecf-polar-returning-bend-full-ray-surface.py" --mode observe --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --design polar-gap092-returning-rays-down.json --field polar-gap092-returning-rays-down.npz --trace-nodes 2048 --output polar-gap092-returning-down-full.json
python3 -u "$S/2ecf-polar-returning-bend-full-ray-surface.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --amplitude .48 --flat .16 --geometry-weight 120000 --field polar-gap092-returning-rays-up.npz --output polar-gap092-returning-rays-up.json
python3 -u "$S/2ecf-polar-returning-bend-full-ray-surface.py" --mode observe --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --design polar-gap092-returning-rays-up.json --field polar-gap092-returning-rays-up.npz --trace-nodes 2048 --output polar-gap092-returning-up-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| polar-gap092-returning-rays-down.npz | 5ea62618f8ede5ca6f25c1d7e741a7f20591f9152b5a916fc54fa3b8135210bc |
| polar-gap092-returning-rays-down.json | ce55d48fb5604e0cc2ba5600b5d53216afae26968e027f82e571688e3816a48c |
| polar-gap092-returning-down-full.json | 8a62d13ef9ef449c5199c8ca3d2d0c3465eaf22659274927ff49e1ec585e95c9 |
| polar-gap092-returning-rays-up.npz | 0499cf32724b94125f7b748b83725327704150292f330fa400e4138e86ea2a9e |
| polar-gap092-returning-rays-up.json | 5b38384b8cb625f192ce99e7768ae75083c76d9647d64769edcac306b6dc559c |
| polar-gap092-returning-up-full.json | 5ed377eae70561f052b53327a1d040e480350f97fce93775511252c961e4f1f2 |
| polar-gap092-returning-rays-down-exit.json | 17d294a63b881e4eef9c07be42a33d0fe3df24fa232be87bdaac149b12d31a25 |
| polar-gap092-returning-rays-down.log | 30990b2aff271a36cddc8e674942b02a396467be26a3ca07882aa247f66d2583 |
| polar-gap092-returning-down-full-exit.json | d12b2ca336c9c717253bc6d8b9ad5f90ee031797cca1f0747f2640715ce4d774 |
| polar-gap092-returning-down-full.log | 7b8cc11f5e2fd372a875e0cd1829be8f88696a52cc7b4a28ea6ea5823a058e3e |
| polar-gap092-returning-rays-up-exit.json | b86cae03c2089c39197e9aecbeadb0d056ad942bd3c35ee04f17b4748343e8f7 |
| polar-gap092-returning-rays-up.log | c188a35a46776dd03b79cd1aeaf93c7c354f7693bf543d25fd800df85a3463b1 |
| polar-gap092-returning-up-full-exit.json | 3dd75667935a9c30a3256ff22240a263cdf70c367a8647df98af167c2169d054 |
| polar-gap092-returning-up-full.log | 8a5df1f93dc3954dd427718af9775bbf9ee1809ea56f991f8a4f471427cf1960 |
