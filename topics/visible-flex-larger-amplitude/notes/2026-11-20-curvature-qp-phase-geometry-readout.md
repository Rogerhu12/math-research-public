# 首次曲率QP父的相位几何点读

2026-11-20，Astra-larger-resume-24b2ab87-20261120。**数值诊断，非全域几何证书。**

真实输入为曲率QP六步输出 `0c53537771085266634794d82a0f133e2d1f149d1af7e0248e136d9ceee6812d`。同原923节点、1845 node/mid、513准确角轨道代表读取完整F及六jet；上下镜像/四水平符号把原全体覆盖为同一有限点集。法向用Fphi×Fs，平帽方向为±ez；旋转架位置/法向的点积仍是实际欧氏量。

| 量 | 点读结果 |
|---|---:|
| H | 1.92533722376812 |
| 完整相位体D的点对下界 | 4.08253071691682 |
| beta=1/4的加权支持最小采样值 | .3369129742009585 |
| beta=2/5的加权支持最小采样值 | .23638200272231846 |
| Rot(pi/2) core witness | (0,1.414121785587319,0) |
| witness到活动体最近采样点距离 | .9536435714466487 |
| witness到每个未标记平帽的准确圆盘距离载体 | 2.104372290634258 |
| 最近点距离/直径下界的点读比值 | .23359127893270407 |

两种支持的最坏点分别在s=.955375/.95575、phi=pi/2；帽的beta|H|更大，所以未标记帽不降低本次最小点读。最近活动点在s=.305、phi=pi/2。采样上半z最小0，尚不能以此声称全上半z≥0或嵌入。

**界的方向不能反用。** min_sample support是连续最小支持的上方近似，正数不证明全域正支持。min_sample distance是到整个像距离的上界近似，不是held下界；再除Dlb所列.23359也不能证明delta_hold/D≥.2。它只表明这个沿旧R645路线选择的见证仍有继续做连续覆盖的余量，不能替代那项工作。当前最大采样Gram仍约.1801，先继续解同g与曲率约束；全域证书须绑定最终同一场。旧开放prefix证明不继承。

完整读者 `scripts/read_closed_phase_geometry_20261120.py` SHA256 `f125c251e8231b69f5d1709fca691669c1ce48f150f7858b1d3b5c46d35e3b31`；完整报告SHA256 `d40d6392a9069f76375238309289fd934a17a5dfc56533120a07056788378688`。本地session46335自然exit0，未写raw入库。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$TOPIC/scripts/read_closed_phase_geometry_20261120.py" \
 --repo "$REPO" --bundle "$WORK/curvature-qp-six-step.npz" \
 --out "$WORK/curvature-qp-phase-geometry.json"
~~~

固定非轴帽标记、包含反射的Euclidean商、同场连续支持/距离和全t reach均仍未付。R650与R645提供可接的条件工具；本点读不重新认领它们。
