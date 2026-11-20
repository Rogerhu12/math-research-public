# 同六角模的嵌套径向粗空间细化

2026-11-20，Astra-larger-resume-24b2ab87-20261120。**数值证据，非完成结论。**

在全部原有限行和同一真实314维末场上，将每个粗径向区间二分到最近既有模型节点，保留原5个中心，共11中心；三jet ×20角通道，另13个core水平A和1个H方向，共674维。该嵌套只扩搜索空间，原923节点、同g与全部N2048残差点完全不变，不是已证明的求解精化收敛。v3仅给已刊v2增加显式centers及嵌套二分参数，公式不变。

| 步 | 接受alpha | 原SSE | max采样Gram |
|---|---:|---:|---:|
| 1 | 1.0 | 220.243787985 | 0.178313745969 |
| 2 | 1.0 | 148.764458188 | 0.181419293375 |
| 3 | 0.5 | 138.961983391 | 0.178298932491 |
| 4 | 0.5 | 135.329937079 | 0.176722177341 |
| 5 | 0.5 | 132.937196395 | 0.175649281017 |
| 6 | 1.0 | 132.703849966 | 0.174584961902 |

完整原算子末读：SSE 132.703849965452；maxGram 0.174584961902398；min determinant 0.866624039915665；H=1.83880249048724。子空间/原目标相对差6.4190078e-12。六步自然exit0，16.68442秒。精确仿射端口首末均零；core曲线、固定a/S/R、原细mesh保留。

最大采样误差仍远超1e−6；未给全域metric、全t强C²/嵌入/reach、固定握持与D/held/E，或固定参数精化到容差结论。真实SSE接受不自动代表几何全部改善。

## 配方与身份

- 源 SHA256 `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8`。
- 输入 SHA256 `7bf4a3b5660537990425a1182a07dfb95e96e4038fe9d771ee764466c435dd0b`。
- 输出bundle SHA256 `e94465d25783c81dc07804fcfdb0b64090fbec75f4cd362ad150adefee8a98a0`。
- 完整报告 SHA256 `c6745a4d58ad84987686e100401e699bcaeb8e1629a29a377279e89aeb0c65c5`。
- 原dense/batch/base SHA同前173维结果；新source完整刊入scripts。
- 实际中心：`[0.3, 0.6, 0.8275, 1.0570671854957785, 1.1975374839662283, 1.3580749679324564, 1.5587468228902417, 1.759418677848027, 1.9600905328058122, 2.140695202267819, 2.26109831524249]`。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/resume_20261120_physical_subspace_v3.py" \
 --bundle "$WORK/physical-threejet-m6-six-step.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
 --low-modes 6  --refine-centers 1  --out "$WORK/physical-threejet-m6-r11-six-step.json"
~~~

其余默认steps6、backtracks8、damping.001、angles2048、seconds600。raw只在仓库外；保存完整源/配方/SHA及紧凑结论。
