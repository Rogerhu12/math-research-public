# 0241完整直径证书的局部加密

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

[R663](../results/R663-complete-closed-embedding-and-fixed-marker-noncongruence.md)已付同一0241的全部922胞、全部角、两帽及下半镜像。本次只加密其半径上界超过新的准确目标$D_*=4.0965$的单元，保留其余已有界；未重跑旧完整覆盖、未改变候选或g。

## 1. 合并严格界的规则

旧报告逐胞给$|F|^2\le B_i$。程序先确认旧报告的完整覆盖标志、连续原胞序列及候选/节点SHA均相同；对$B_i>D_*^2/4$的胞，用R658原位置专用源取得新完整胞界$B_i'$，然后取$\min(B_i,B_i')$。两个界都覆盖同一准确胞，取小者仍有效。其余胞逐字消费旧界；平帽使用旧准确$R^2+H^2$界。最后以向外平方根计算

$$D_0\le2\sqrt{\max\{B_{\rm cap},B_0,\ldots,B_{921}\}}.$$

第一级$Q=16384,r=16$只需胞876–882共七胞；第二级$Q=65536,r=64$只需仍未达到目标的880、881两胞。每次覆盖仍包含整个胞及全部角，不是局部极值点搜索。全部九次实际向外输出为：

| 原胞 | 第一级半径平方上界 | 如需第二级的新上界 |
|---|---:|---:|
| 876 | 4.173003484897833 | — |
| 877 | 4.18240706347855 | — |
| 878 | 4.190167300915344 | — |
| 879 | 4.195031857250507 | — |
| 880 | 4.196026198353221 | 4.194400758478471 |
| 881 | 4.195709340172068 | 4.194164214658781 |
| 882 | 4.191954235162541 | — |

合并后最大平方界由879胞给出$4.195031857250507$，其余915胞和两帽均已由原覆盖检查不更大。完整向外直径上界为$4.0963553836309226$，故可采用短准确有理界

$$\boxed{D_0\le4.096356.}$$

未改曲面而证书变紧；这不是曲面实际直径缩小的数值求解。

## 2. 同一固定标记族的比例

R663的四个真实固定p4图高度为$.001$，全族嵌入、强C²连续、无平面活动开片和含反射非全等已付。本次仅更换同一对象的更紧直径预算：

$$D_{\rm marked}\le4.098356.$$

同一[R662](../results/R662-complete-closed-C0-difference-and-inherited-size-amplitude.md)见证下界$L\ge.914520539$与固定握持区直径至少$.9$保持，因此按准确有理数比较，

$$\boxed{\delta_{\rm hold}/D_{\rm marked}>.22314,\qquad
\operatorname{diam}(H_{\rm grip})/D_{\rm marked}>.21960.}$$

若另外证明整张活动面的实际主曲率$|\kappa|\le8.1$，则R663的完整正支撑及标记曲率$\le5$与R650合成可支付reach目标，因为

$$8.1\cdot.03\cdot4.098356<1,\qquad
64/267>.03\cdot4.098356.$$

这句话是明确的条件预算。当前全域曲率覆盖尚在执行，本条不提前声明该条件已成立；全域度量和真正细化收敛也未支付。

## 3. 完整来源与复现

新增完整源 `scripts/resume_20261120/refine_complete_radius_from_paid_cover.py`，SHA256 `37f5d6350584b15a76b92b58b86fef1fd387bcb46766383241a5f4b531a73dee`。

候选SHA `0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`；准确节点报告SHA `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692`。已付完整一阶报告SHA `2bfe3a6e4371473e5b54e6b229a28facb2d9fba88e855d518287a5b780637125`，其原完整重建命令见R663。

未改R658位置源SHA `9085e6713faa1aba1dcc99a0e30ed038f33ca6ec24a2c187e9668a9c4fe26623`；R656几何源SHA `2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377`；向外区间核SHA `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。

实际报告 `continuous-0241-radius-refined-from-full-cover.json` SHA `89d7a63f59ce3438e38590e387e4132a4c62aaf66dc673e8904b4950a7efd44b`，46.582759秒自然退出0。全部原报告只scratch，小完整源/参数/输入身份及本紧凑结论保Git。Python3.12.14/NumPy2.3.5、单BLAS，未创建Actions run。

令`topic`为checkout内本题路径、`work`为仓库外工作路径：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/refine_complete_radius_from_paid_cover.py" \
 --bundle "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --radius-source "$topic/scripts/resume_20261120/fullclosed_radius_interval.py" \
 --paid-cover "$work/root/continuous-0241-complete-first-geometry-q2048-r1.json" \
 --target-diameter 4.0965 --levels 16384:16,65536:64 \
 --out "$work/root/continuous-0241-radius-refined-from-full-cover.json"
~~~
