# 完整粗三 jet 子空间首次六步

2026-11-20 10:05 UTC，Astra-larger-resume-24b2ab87-20261120。**数值证据；未达完成标准。**

执行环境在约10:03 UTC恢复，原scratch数组可读，故直接复用真实63维父，没有重建、改名冒认或重跑旧证书。运行源码为 `scripts/resume_20261120_physical_subspace_v2.py`，完整公式在同日 `physical-threejet-subspace-formulas` note。保持全部923节点、1845个节点/真实五次中点、M160及原N2048角行，通过R653重数压成513代表角；所有1332245原自由坐标仍定义完整模型，173维仅是这次搜索子空间。core曲线及固定标量、S/R、网格不变；原准确仿射约束首末均逐项为零。

| 步 | 接受 alpha | 原 Frobenius SSE | 最大采样 Gram 算子误差 |
|---|---:|---:|---:|
| 初始 | — | 6430.55548312495 | .586426369922 |
| 1 | 1 | 1332.37909507 | 0.427203375888 |
| 2 | 1 | 964.316130259 | 0.383003711408 |
| 3 | 1 | 896.975561293 | 0.338090674079 |
| 4 | 1 | 834.506725822 | 0.317603801865 |
| 5 | 1 | 818.53143035 | 0.312762000876 |
| 6 | 1 | 817.506137096 | 0.310475030101 |

六步都接受满步，阻尼从.001起每步除3，没有修改目标或加入隐藏可行门。完整原batch算子末读为 SSE817.5061370945074、最大采样误差.31047503010094935、最小采样determinant .7976487736505589。子空间与原算子末SSE相对差2.1516202428526835e−12。末峰在stage1689，s=1.3279741896887884，phi=π/2。H从1.9392157715615652变为1.8634439054578367；自然退出0，耗时10.023249115秒。

这说明原值帽缺少中心速度/加速度的限制确实影响初猜；补上全部粗三jet显著下降，但不能证明在此子空间或原完整空间存在精确解。`.310475`仍远超1e−6；这不是全域metric、全t嵌入、reach、held或固定参数精化结论。下一实际工作已从同一末数组启动完整空间带正列尺度的augmented方向，并继续保留原完整目标。

## 复现身份

- 本机exec session23957，Python3.12.14、NumPy2.3.5、SciPy1.17.0；单BLAS/OMP线程。
- v2源 SHA256 `03e74db84062daf009eb99ec6348d727817abb0a012a0e61eda6d9fc4d5e77e2`。
- base源 `1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7`；batch `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`；dense定义 `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`。
- 实际输入bundle `af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505`。
- 新输出bundle `f062a4b2684c09e55f90265468699eea638ee8739f3e16d99fa6bd874036971a`。
- 完整JSON报告 `bac8d1ace8aaf502b5a0360d5e41304a1fcaf3bfe32b62f4cd524ef7617ce49f`。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/resume_20261120_physical_subspace_v2.py" \
 --bundle "$WORK/physical-fit-six-step.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
 --out "$WORK/physical-threejet-six-step.json"
~~~

未显式参数为angles2048、low-modes3、steps6、backtracks8、damping.001、seconds600。输出同stem npz。只有小源码、配方、SHA和紧凑科学结论入库，raw保持仓库外。
