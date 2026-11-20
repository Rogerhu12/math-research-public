# 扩充到六个角模的完整粗三jet修正

2026-11-20，Astra-larger-resume-24b2ab87-20261120。**数值证据，非完成结论。**

前一173维实际父的完整角谱中，第4、5、6模能量分别占25.6129%、20.0754%、12.2690%；累计90%需到第6模、99%到第9模。Parseval给原完整SSE817.5061370945073。该一次读取使用随后保存的 `read_closed_residual_spectrum_20261120.py` 中同一DCT-I/DST-I公式，原读取在终端heredoc执行，不冒作该脚本已跑。因而扩充低角模3→6，保持原5粗径向中心；维数是314（15×20+13+1），不是313。

| 步 | 接受alpha | 原SSE | max采样Gram |
|---|---:|---:|---:|
| 1 | 1.0 | 419.289323682 | 0.206163253744 |
| 2 | 1.0 | 393.393238185 | 0.205768399091 |
| 3 | 1.0 | 305.62458855 | 0.207598271965 |
| 4 | 0.5 | 281.781976594 | 0.203597253447 |
| 5 | 0.5 | 270.602293068 | 0.200444698561 |
| 6 | 0.5 | 268.949655967 | 0.197410916238 |

完整原算子末读：SSE 268.949655967394；maxGram 0.197410916238466；min determinant 0.844327744812299；H=1.85492455282273。子空间/原目标相对差2.1801101e-12。六步自然exit0，15.63033秒。精确仿射端口首末均零；core曲线、固定a/S/R、原细mesh保留。

随后对该真实末数组运行上述read脚本（`--curvature`）：所有1845×513点的主曲率绝对值max=10.7456816578884，位于s=1.3179405969409、phi=1.34376717018782，min area=0.0937562813690915。这是点值、不是连续上界或reach。末角谱90%需mode8、99%需mode12，作为后继增加角模的依据。诊断报告SHA256 `2f3ac5f3eae32e8de80075f42115c4d6c77f2d2d84d5971d14aaa4a3f50ffa31`。

最大采样误差仍远超1e−6；未给全域metric、全t强C²/嵌入/reach、固定握持与D/held/E，或固定参数精化到容差结论。真实SSE接受不自动代表几何全部改善。

## 配方与身份

- 源 SHA256 `03e74db84062daf009eb99ec6348d727817abb0a012a0e61eda6d9fc4d5e77e2`。
- 输入 SHA256 `f062a4b2684c09e55f90265468699eea638ee8739f3e16d99fa6bd874036971a`。
- 输出bundle SHA256 `7bf4a3b5660537990425a1182a07dfb95e96e4038fe9d771ee764466c435dd0b`。
- 完整报告 SHA256 `7a9c645fff45a63f513d044e83abfffef8299f8dfd605873cc73602534e8be96`。
- 原dense/batch/base SHA同前173维结果；新source完整刊入scripts。
- 实际中心：`[0.6, 1.0570671854957785, 1.3580749679324564, 1.759418677848027, 2.140695202267819]`。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/resume_20261120_physical_subspace_v2.py" \
 --bundle "$WORK/physical-threejet-six-step.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
 --low-modes 6  --out "$WORK/physical-threejet-m6-six-step.json"
~~~

其余默认steps6、backtracks8、damping.001、angles2048、seconds600。raw只在仓库外；保存完整源/配方/SHA及紧凑结论。
