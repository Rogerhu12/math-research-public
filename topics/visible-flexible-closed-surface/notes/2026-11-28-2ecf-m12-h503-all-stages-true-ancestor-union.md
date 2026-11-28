# h503 原场全部七阶段和真正祖先并集

数值证据。原固定 g、X+C 源的 487→503 物理跨度加密，在相同 M64 角空间由准确 Boehm 暖输入起步。真实输入和保存场的身份及独立非线性观察见[独立观察与 R226](2026-11-28-2ecf-m12-h503-saved-field-independent-physical-gradient.md)。原七阶段执行器已自然退出0，七个子进程都返回0。

| G14/N3072实际暖输入→实际保存场 | 暖输入 | 保存场 |
|---|---:|---:|
| 11178个半径并集上的原度量峰 | 5.424143958602297e−10 | 4.944022957207955e−10 |
| 曲率观测峰 | 6.428917514613397 | 6.428917289882362 |
| 支撑观测下界 | 0.8178848938021344 | 0.8178848938021428 |

并集覆盖7042个当前独立半径及4136个缺失的旧半径；每个半径使用3072个独立角点，保留各代原观察。前后使用相同原源、目标 g、点集和物理六jet。每个旧点同样分别代入本步的暖场和保存场；该并集未定义混合求积能量，离散峰也不给出全域连续上界。两个旧微窗口另外检查546个半径，保存场峰4.943983491078894e−10，原源跨度17479、半径约0.5134772748712184924、新跨度198。微窗口报告里的before使用未加保存修正的原源，不能当作本步暖场峰。

此前R236旧分离三角方法在503个基元素、951个终子片上返回上界5.417527556396368e−5，超过1e−6；方法未利用原源与修正的交叉抵消。这是该上界的局限。已有的主证选择独立的原5778场。

| 原阶段 | 实际退出 | 秒 |
|---|---:|---:|
| actual-exact-warm-transfer | 0 | 3.514786 |
| actual-original-g-H2-direct-LM | 0 | 2242.923511 |
| actual-field-R226 | 0 | 21.349664 |
| actual-field-original-global-geometry-consumer | 0 | 0.127054 |
| actual-field-original-R236 | 0 | 1106.690247 |
| actual-field-existing-two-window-microspan | 0 | 58.176342 |
| actual-field-true-parent-and-child-ancestor-union | 0 | 675.889723 |

| 本次完整回执 | SHA256 |
|---|---|
| execution.json | `75caabd5ce3d1552ce9df14417a228a6d73437e9a60d48dc23a5756cd44ff174` |
| metric-budget.json | `7050e483b7c9832f3001a4c1866e1b0922c51c2429beaf08664894b3bb930555` |
| microspan-observer.json | `c4bc7f4a1f059258e2a273c58482507e2a8e5399b976e5d85569fb91143e2c77` |
| ancestor-observer-union.json | `74e242f6eeb071f25d51247ecc19f844c3f3b67a36b2f747313485e2c4b800de` |

## 重生

完整七阶段的输入、求解入口SHA和可移植执行命令见[原加密执行命令](2026-11-28-2ecf-m12-h503-retained-full-Gram-accepted-step.md)。已具备h503准确源、原暖场和保存场时，在课题目录可单独运行以下原点集并集；将尖括号替为本机的实际输入目录。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-quadrature-observer-union.py --scripts scripts --data <M12-prefix-data> --grid <h503-input>/grid.json --initial-field <h503-run>/warm-transfer.json.field.npz --field <h503-run>/result.json.field.npz --result <h503-run>/result.json --query-report <h503-input>/exact-tail-queries.json --query-cache <h503-input>/exact-tail-queries.json.npz --out <fresh-directory>/ancestor-observer-union.json
```

并集消费源码 SHA256 `eb8753969c3871705997f15bc153eaa3b0e1c6632b4f675f5492466cfa65487f`。
