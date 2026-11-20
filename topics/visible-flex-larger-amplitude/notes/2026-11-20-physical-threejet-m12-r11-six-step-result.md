# 12角模/11粗点的实际六步与曲率失败

2026-11-20 10:31 UTC，Astra-larger-resume-24b2ab87-20261120。**数值证据；度量下降但未达到几何要求。**

仍保原923细节点、M160载体、全部1845×2048×3原Gram行，准确角重数约化；core曲线、a/S/R与原精确端口不变。只扩已刊物理三jet搜索子空间，不把它当完整解或已证明的精化收敛。

本次维数1280，初始SSE=132.703849965452、maxGram=0.174584961902398。

| 步 | 实际试步alpha:SSE | 接受后maxGram |
|---|---|---:|
| 1 | 1:73.866489接受 | 0.106287062496 |
| 2 | 1:54.8664108接受 | 0.0620071834757 |
| 3 | 1:41.7671427接受 | 0.0541955744713 |
| 4 | 1:37.570152接受 | 0.0528313526287 |
| 5 | 1:41.4339733拒绝; 0.5:36.6494136接受 | 0.0528699053969 |
| 6 | 1:36.1189884接受 | 0.0528323436235 |

原完整batch末读 SSE=36.1189884246281、maxGram=0.0528323436235404、min det=0.950447481537482；native/reduced相对差8.2623562e-12；H=1.84081238435274。运行自然exit0，35.665692秒。

随后同真实数组/共同quintic六jet读得采样主曲率max=17.1862262243966，位于s=1.19753748396623、phi=1.41433028643056。这仅是点值，但对候选的完整上下镜像+相位族，D至少2|H|；其.03×2|H|×K=1.89819708445>1，已经数值上违反reach/D目标的必要条件。不能因为SSE下降便继续把此父称为更好的完整几何解。

## 复现

- 源码SHA256 `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8`。
- 输入bundleSHA256 `e94465d25783c81dc07804fcfdb0b64090fbec75f4cd362ad150adefee8a98a0`。
- 输出bundleSHA256 `c79e88cb48f94196d8ec8cfa18e7362fa849d4bd1aa4afee71a53e3445331792`。
- 计算报告SHA256 `f1da439ab7cd20a5414a5862a5d287c888d139b4c061a8572bbc9473e9d6d1cf`。
- 几何读者SHA256 `af0511e7d92eeffa44f99704c705ce8ee5961fb3e9b0757c9ce1f2872126d72a`；读者报告SHA256 `25e6890cc8201ab3bfbb47622822880aa46a5db89fd99d906c8bb3d9fbefbf02`。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/resume_20261120_physical_subspace_v3.py" \
 --bundle "$WORK/physical-threejet-m6-r11-six-step.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
 --low-modes 12 --refine-centers 1 \
 --out "$WORK/physical-threejet-m12-r11-six-step.json"
~~~

其余默认steps6/backtracks8/damping.001/angles2048/seconds600。几何读者同目录read_closed_residual_spectrum_20261120.py，--repo REPO --bundle 输出npz --out 新scratch.json --curvature。实际旧版本按上述SHA及Git历史读取。全部raw只在仓库外。后继改从必要几何条件尚未排除的af89父作曲率约束求解。
