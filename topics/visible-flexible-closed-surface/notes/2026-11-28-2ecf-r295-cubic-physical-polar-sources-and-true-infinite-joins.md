# 从四步固定度量场生成连续可证的三次物理截圈

[R295](../results/R295-integer-separated-meridian-tensors-and-the-real-infinite-cuff.md) 逐个物理极角证明四张新闭曲面全相位嵌入，支付双形变比例。控制表取自[原四步稀疏物理场](2026-11-28-2ecf-r289-sparse-physical-positions-and-native-query.md)在空间限幅以前的真实位置。起始诊断比较了空间限幅前、后的全部材料角导。一个移位网格上，这两项最小值分别约 .38146 和 .64533；固定物理极角处的高度径向导最小约 −.88107。三组不同分辨率的径向投影势尝试均未给全正界。随后实算 161 条极角上的 850 个径点，所有非相邻线段均无交叉。R295 的连续证明采用另立的准确三次物理场和全部整数格对。

在原真实截圈上以物理极角作自变量，用函数值、一阶物理切向求 $(R,z,u)$ 的角向 Hermite 数值插值；按真实非均匀材料点用 PCHIP 产生控制提议。第四场在角、径分别减掉六分之一局部二阶差分，减少取样控制点直接喂入三次样条造成的平滑误差。实际新场由量化整数控制表、真实无穷尾和确切资料定义。第四场的材料钟只调整网格密度；共同的真实 $g$ 沿用此前低帽的 $ds^2+r_0(s)^2du^2$。嵌入和两强比例已有闭区间结论，以下度量和曲率为实际有限观察。

| 真实场 | 1122 径点 × 145 四分区角的度量/曲率峰 | 移位 1063 × 173 的度量/曲率峰 | 全部 17046 原生深行 × 60 四分区角的度量/曲率峰 |
|---|---|---|---|
| 256×64，较早换入真实尾 | 1.15842545 / 34.799110 | 1.15845650 / 34.798950 | 1.15825528 / 34.799115 |
| 512×64，深接缝 | .160063812 / 38.879864 | .160082743 / 38.870628 | .160277025 / 38.803730 |
| 512×64，再作非均匀物理网格 | .143373219 / 12.854516 | .144413322 / 12.843933 | .081202051 / 12.590988 |
| 512×128，另作控制预校正 | .123012175 / 16.267751 | .122886031 / 16.250663 | .081864823 / 14.966774 |

第一场较早把低帽原位置过渡到平领线性截圈，整核误差反而超过 1。后移接缝减少了这一误差；第三场保持较低的实测曲率，第四场获得较低的全域度量峰。真实无穷尾在所有场上连续接入，原生观察用全部不同的物理两 jet 输入，四分区角按对称性覆盖整周。定量厚度和强目标度量精度仍待支付。

沿用[低帽真实源](2026-11-28-2ecf-similar-infinite-tails-and-true-low-wide-cap-physical-states.md)的 `S` 和 `W`。此外用 NumPy、SciPy、单线程 BLAS。所列控制归档从生成器和固定的实际 XYZ 重新产生。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
b=(--scripts "$S" --meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail-table "$W/g12-m2-exact-cuff32-tail.npz" --tail "$W/g12-m2-exact-cuff32-tail.json" --state "$S/../notes/2026-11-28-2ecf-r289-frozen-minimax-physical-coefficients.json")
python "$S/2ecf-r295-cubic-true-material-length.py" --meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail "$W/g12-m2-exact-cuff32-tail.json" --state "$S/../notes/2026-11-28-2ecf-r289-frozen-minimax-physical-coefficients.json" --out "$W/r295-real-source-material-length.json"
run() {
  name="$1"
  shift
  python "$S/2ecf-r289-cubic-meridian-physical-source.py" "${b[@]}" "$@" --out "$W/$name.npz"
  python "$S/2ecf-r289-cubic-meridian-exact-separation.py" --source "$W/$name.npz" --out "$W/$name-separation.json"
  python "$S/2ecf-r289-cubic-meridian-physical-observe.py" "${b[@]}" --source "$W/$name.npz" --out "$W/$name-actual.json"
}
run r289-cubic-meridian-N256-M64 --spans 256 --ang 64 --seam-den 32
run r289-cubic-meridian-N512-M64-b128 --spans 512 --ang 64 --seam-den 128
run r289-cubic-meridian-N512-M64-c15over16 --spans 512 --ang 64 --seam-den 128 --bias .9375
run r289-cubic-meridian-N512-M128-pre --spans 512 --ang 128 --seam-den 128 --bias .9375 --prefilter 1
```

下表给出实际源码、状态和整数回执指纹。早两张场的旧观察记录还含当时入口脚本的 SHA；随文当前入口的零偏钟分支与旧公式相同。整数分离、真实峰和系数归档均逐项列出。

| 入口或产物 | SHA-256 |
|---|---|
| `2ecf-r289-material-polar-meridian-sections.py` | `8fe67a1a5ad7eff54951e3722f7403f1510b910cb735e04aeb39b6d19bcc8872` |
| `2ecf-r289-physical-ray-meridian-projection.py` | `92954c268b0e94a28363b4482dc951ba5dfa7167c37dcb836b75f7bde2b41657` |
| `2ecf-r289-cubic-meridian-physical-source.py` | `9d616d0ad74a5f8a33199f61f73f924fe38d7e3f3ed6ef5bc7f2cd6ec02197dd` |
| `2ecf-r289-cubic-meridian-exact-separation.py` | `b77c0ad33c5867dd597ed206a31216b4e81bd8d78b2c4fa797bbc265decc2c5c` |
| `2ecf-r289-cubic-meridian-physical-observe.py` | `c7321ea88112409c3ad97c1a01dca9a25e297d8fb1d27eb0e8a05a23574ec5be` |
| `2ecf-r295-cubic-true-material-length.py` | `c7b4ee51f20a048f8286396f282ba0f752e51a817e68c71fa1266f1b4b910fb1` |
| `r295-real-source-material-length.json` | `93e92a306e8dd177b04827cbaebe01ca7595b765a66182459bad041891bc8d2a` |
| `r289-cubic-meridian-N256-M64.npz` | `4469d37983c77add7e516c0bdda9a90c142ce0f7a66043f2b59c0cd0034b116a` |
| `r289-cubic-meridian-N256-M64-separation.json` | `5c43851f2239c7c4d350b6df64748af699b6cfbbb0017e6206809ff6621a4bdc` |
| `r289-cubic-meridian-N256-M64-actual.json` | `308894c8d01e807beb01c81cbdf5b35ac0f61c15c139aa45c40a9a8e97761d21` |
| `r289-cubic-meridian-N512-M64-b128.npz` | `3b8b4283623996dfc918129df8c8988df8942c38ef0afe673576cc7b0aba570a` |
| `r289-cubic-meridian-N512-M64-b128-separation.json` | `422a830790f1a4e49506492e773da6d00b8140b3e4de16ea365aac11d0614cc6` |
| `r289-cubic-meridian-N512-M64-b128-actual.json` | `e378f0a7c7f3594d61777e193295836b42d2785a0629ddb8f40463a56086c21e` |
| `r289-cubic-meridian-N512-M64-c15over16.npz` | `0defe20442b31c700c2f00aae3dcd26b06da75e1cda71a441fe903210b67e214` |
| `r289-cubic-meridian-N512-M64-c15over16-separation.json` | `e9f1c837d9f7cd874b54366ab92417051363863c9dbb4efc500e30dc15cd73a0` |
| `r289-cubic-meridian-N512-M64-c15over16-actual.json` | `49b5cb5fa627e8b6bc3c7e33473641308c0499f9afafb8f0fbd723aebfe8d2bb` |
| `r289-cubic-meridian-N512-M128-pre.npz` | `441bc707362cd3d2ef8642facb51edd3308514f778e045054f274d9fa44a60f9` |
| `r289-cubic-meridian-N512-M128-pre-separation.json` | `5ec9afa5d11201ca41a262a89e4d6fe1147b8fcdf2e7ec047b471c471e6de7bb` |
| `r289-cubic-meridian-N512-M128-pre-actual.json` | `7ceb82a6476edc87977afa195467ad1a5224c0833891d86943a50ed92fb9545f` |
