# 12角模/23粗点的实际六步与曲率失败

2026-11-20 10:31 UTC，Astra-larger-resume-24b2ab87-20261120。**数值证据；度量下降但未达到几何要求。**

仍保原923细节点、M160载体、全部1845×2048×3原Gram行，准确角重数约化；core曲线、a/S/R与原精确端口不变。只扩已刊物理三jet搜索子空间，不把它当完整解或已证明的精化收敛。

本次维数2648，初始SSE=36.1189884246281、maxGram=0.0528323436235404。

| 步 | 实际试步alpha:SSE | 接受后maxGram |
|---|---|---:|
| 1 | 1:28.1266121接受 | 0.0760518510568 |
| 2 | 1:20.9814771接受 | 0.0681555468268 |
| 3 | 1:39.5669114拒绝; 0.5:18.4925889接受 | 0.0612081344173 |
| 4 | 1:27.1784335拒绝; 0.5:16.304297接受 | 0.0461122460462 |
| 5 | 1:22.5800574拒绝; 0.5:15.0856037接受 | 0.045033392087 |
| 6 | 1:21.4684772拒绝; 0.5:14.3683024接受 | 0.0441174452165 |

原完整batch末读 SSE=14.3683024122662、maxGram=0.0441174452164619、min det=0.95308089542632；native/reduced相对差1.0856591e-11；H=1.83882698072916。运行自然exit0，45.097302秒。

随后同真实数组/共同quintic六jet读得采样主曲率max=44.3647434238134，位于s=1.11726874198311、phi=1.34376717018782。这仅是点值，但对候选的完整上下镜像+相位族，D至少2|H|；其.03×2|H|×K=4.89474523205>1，已经数值上违反reach/D目标的必要条件。不能因为SSE下降便继续把此父称为更好的完整几何解。

包含真实中心对称点对后，D点下界=4.06509373259603，必要产品.03DlbK=5.41040521321125。不将浮点排除冒作严格不存在定理。

## 复现

- 源码SHA256 `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8`。
- 输入bundleSHA256 `c79e88cb48f94196d8ec8cfa18e7362fa849d4bd1aa4afee71a53e3445331792`。
- 输出bundleSHA256 `47da48d14b51170d1ee1ad068ea29f32747529b56e740eaa07973d7bb83ce61f`。
- 计算报告SHA256 `85996971e0afe05e2cd877ce816621499d4954b4fd5a0e8daf2ca905acaf9da5`。
- 几何读者SHA256 `20a1ec387bbe0c3de6489cdd216477c5d09f8089acd79c7d0a11db1d6ae320fd`；读者报告SHA256 `706b1ae83cbb45526aa3bd42c1c38827e0514b9be5fd9964bab4dcd697bc4071`。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/resume_20261120_physical_subspace_v3.py" \
 --bundle "$WORK/physical-threejet-m12-r11-six-step.npz" \
 --operator "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
 --low-modes 12 --refine-centers 2 \
 --out "$WORK/physical-threejet-m12-r23-six-step.json"
~~~

其余默认steps6/backtracks8/damping.001/angles2048/seconds600。几何读者同目录read_closed_residual_spectrum_20261120.py，--repo REPO --bundle 输出npz --out 新scratch.json --curvature。实际旧版本按上述SHA及Git历史读取。全部raw只在仓库外。后继改从必要几何条件尚未排除的af89父作曲率约束求解。
