# 完整自由空间的物理高度三角坐标与实际局部点

状态：新坐标代数及其实现的必要检查已完成；下面登记的首个实际方向已启动，未把启动或内迭代当作成功终态。它接续真实 `def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d` 父场，不重做先前重建或连续证书。

## 1. 可逆的完整空间变换

原自由向量最后一槽是高度 H。令 e_H 为该槽单位向量，令已刊物理粗空间最后一列为 B_H。该列按原节点取值构造 q_Z=b−χ、δH=1，其中

$$
b(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5.
$$

取 v_q=B_H−e_H，则 e_Hᵀv_q=0。定义

$$
A=I+v_qe_H^T,\qquad A^{-1}=I-v_qe_H^T,
\qquad A^Tg=g+e_H(v_q^Tg).
$$

由于 (v_qe_Hᵀ)²=0，两个逆式直接相乘得到单位阵。A 在全部原自由空间上可逆，A e_H=B_H；因此这是方向坐标变换，没有删除任何原场自由度。当前状态 x 不经 A 变换，也不重新插值。每一试步仍由原同一 quintic、core 和 analytic lift 计算实际物理场。

令 D_I 是已刊 DoubleIntegrated 的投影后 lift，采用已刊完整 A/E/D 的 H² 型正尺度，仅把其 H 槽尺度改为

$$
s_H=\sqrt{7S^3/120}.
$$

新的完整方向映射与转置为 A D_I z 和 D_Iᵀ Aᵀg。原端口约束及所有 A/E/D 缺陷仍保留；A 的修正 B_H−e_H 也在原合法自由空间内。

令 u=s/S，则 b_{uu}=60u−180u²+120u³，故

$$
\int_0^S b_{ss}^2\,ds
=\frac{3600}{S^3}\left(\frac13-\frac64+\frac{13}5-\frac{12}6+\frac47\right)
=\frac{120}{7S^3}.
$$

这个等式用于标定理想全域平滑高度方向的范数。实际实现沿用 B_H 的字面节点三 jet 和原共同 quintic/lift，不把它偷换成另一个连续场。实际 S=2.3712998717298257，s_H=0.8819381183411777，理想弯曲能量为 1.2856530149355654。

## 2. 粗空间在新范数中白化

对原自由物理步 w，新范数为

$$
\|w\|_{\rm new}^2=
\|\operatorname{DI.inverse}(A^{-1}w;\mathrm{affine}=\mathrm{false})/\mathrm{scale}\|_2^2.
$$

它与旧 q-H² 范数不同，不作两者相同的声明。所有原 A/E/D 与 core 正尺度不变。现有粗列除最后 B_H 外均无 H 分量，A⁻¹B_H=e_H。因此分离通道 Gram 的最后行、列改为零，只保留最后对角元 s_H⁻²；其余通道的原离散积分项保持。实现还以完整 inverse(A⁻¹Bα)/scale 字面值核对这次新分离公式。

若 G 是此新范数下的粗列 Gram，并取 RᵀGR=I，完整附加映射是

$$
T(z_i,z_c)=A D_Iz_i+B Rz_c,
\qquad
T^Tg=(D_I^TA^Tg,R^TB^Tg).
$$

在新范数的约束后积分坐标里，白化粗列是正交归一列。未加几何切向投影时，附加列使同一物理步的最小平方范数落在原新范数平方的 1/2 至 1 倍之间。这沿用已刊投影/附加列代数，不宣称旧 q-H² 的范数界自动适用于当前 A。

本次 1280 列的规范化 Gram 条件数 31651.625438905787；分离式与字面完整式固定探针相对差 3.484984639463611e−15。原 964 条端口小块的最大规范化条件数仍是 13.960165322888349。

## 3. 新任意位置约束

实际局部搜索在 def1 父场找到 cell 821、u=0.11022924905924839、φ=0.6372331788884487，即 s=1.0132184743085018。该真实点的最大绝对主曲率为 7.969807246586478；配同一父场实际 D 点下界 4.090098641737279，必要乘积为 0.9779189338251378。这个位置是下界见证，不是连续最大值证书。

新完整转置在这一位置直接使用原胞 Hermite(h,u) 的三 jet 权与直接角基，保留 core→ρ/θ→lift 和 H 链。其最强实际直径伙伴的乘积梯度必须进入本次活动行。每次非线性试步同时重新读取全部 7377 个旧/Gauss 径向观察，以及该任意位置；任何一点超出 0.03 D_lb K≤0.98 都拒绝。没有把历史 κ 数字当作新场的 κ，也没有增加或删掉度量方程。

## 4. 已实际完成的新实现检查与运行绑定

只对新增映射付一次必要检查，未重跑旧完整 Gram 证书：

- seed=2026112003，完整 T/Tᵀ 双线性相对差 4.0579055624076206e−15；两边 0.023084585449831975 与 0.02308458544983207。
- 在上述任意点的 κ 分支 1，完整坐标预测导数 7.9191731842692255；ε=1e−30 复步导数 7.9191731842692725，相对差 5.944238766947772e−15。
- 16 个选择行、数值保留秩 8；QR 后正交误差 3.774758283725532e−15。它只限制当前更新切向，不冻结当前非线性场的原变量。

本次实际方向：原完整自由变量 1,332,245、积分坐标 1,333,209，加 1280 粗列；M=160，N=2048、精确 quarter 代表 513；全部 7377 径向观察；μ=.0025、LSMR 最多 256 次；0.5 旧 Simpson + 0.5 新 Gauss 的全正径向积分权保持。此次比较必须用这个相同加权目标，并另列 all/legacy raw。首方向实际结果另记，不预告接受。

输入初读精确恢复父值：weighted SSE 0.9812955395142278，all raw 926.5506583275067，legacy raw 231.29820409605992，点 Gram 0.10186568199218482。Gauss κ 7.929778549028246，加入上述任意位置后 κ 7.969807246586478；有限点筛选通过，连续曲率、reach 与等距性仍未认证。

## 5. 完整小源

- `fullclosed_gauss_physical_height_lm.py`，31,950 bytes，SHA256 `d308f6d53ef34be692ca342f93a3874f8b160b41134e0ecc353d9670742523eb`。
- `physical_height_coordinates.py`，4,200 bytes，SHA256 `f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e`。
- `fullclosed_point_cotangent_witness.py`，13,562 bytes，SHA256 `a9da1f7e26f10c1b32aa787012be2b2a115be1200a22773f388eb41a9d3baa6c`。

其余 operator、同 g scalar carrier、积分源、coarse 源绑定均写入本次 report 的完整 SHA；原始数组仍仅 scratch。源码字面完整可复制，不用 SHA 冒充可取得的父数组。

## 6. 本次实际完整 CLI

下面命令的 cwd 为 `/workspace/scratch/24b2ab87057a`。所有选项均以此次真正运行的值展开，包括原来使用的默认值；三个新增源均显式列出。输出目录必须不存在，禁止覆盖旧预算。本次实际 session=80907；原命令将标准输出重定向至 `work/fullclosed_solver/logs/gauss-physical-height-first.log`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python work/fullclosed_solver/fullclosed_gauss_physical_height_lm.py \
  --repo math-research-public \
  --bundle work/fullclosed_solver/gauss-h2-projected-first-fixed/final.npz \
  --outdir work/fullclosed_solver/gauss-physical-height-first \
  --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
  --implementation work/recover_evidence/gauss_observed_closed_gram.py \
  --base-batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
  --observations work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --basis-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
  --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
  --helpers work/fullclosed_solver/fullclosed_lm.py \
  --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
  --scale-source work/recover_evidence/integrated_l2_scale_20261120.py \
  --geometry-source work/geometry_path/fullclosed_curvature_qp.py \
  --geometry-observed-source work/geometry_path/fullclosed_curvature_qp_v3.py \
  --point-source work/fullclosed_solver/fullclosed_point_cotangent_witness.py \
  --height-source work/fullclosed_solver/physical_height_coordinates.py \
  --witness-input work/fullclosed_solver/gauss-projected-first-local-extremum.json \
  --angles 2048 --stage-block 64 --legacy-fraction .5 \
  --low-modes 12 \
  --coarse-centers 0.3,0.6,0.8300000000000001,1.0570671854957785,1.1975374839662283,1.3580749679324564,1.5587468228902417,1.759418677848027,1.9400233473100337,2.140695202267819,2.26109831524249 \
  --reach-ratio .03 --reach-safety-factor .98 \
  --active-band .025 --active-max-rows 16 --active-rank-tolerance 1e-10 \
  --active-top-curvature 16 --active-top-radius 2 \
  --max-directions 1 --maxiter 256 --damping .0025 \
  --lsmr-atol 1e-6 --lsmr-btol 1e-6 --line-trials 15 --target 5e-7
```

新的 witness 输入是已实际找到位置的小 JSON，可由如下完整内容恢复；其中的 κ 不作为新场输入，每一试步重新评估：

```json
{
  "bundle_sha256": "def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d",
  "carrier_sha256": "71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112",
  "witnesses": [
    {"cell": 821, "u": 0.11022924905924839, "phi": 0.6372331788884487}
  ]
}
```

这个精简 JSON 是具有相同输入语义的恢复说明，不声称其文件 SHA 等于本次实际局部搜索完整报告。首次真实运行的 witness 文件 SHA 以 report 的 arbitrary_witness_sources 绑定为准。

## 7. 公开文件的位置对应

上面的实际运行命令保留了当时work路径。复现可把 `work/fullclosed_solver` 中四个新/共用Python源改用本题 `scripts/resume_20261120/` 中同名文件；同一观察源也在该目录。`integrated_l2_scale_20261120.py` 在本题 `scripts/`，两份 `fullclosed_curvature_qp.py` / `fullclosed_curvature_qp_v3.py` 分别对应本题 `scripts/resume_20261120_curvature_qp.py` / `scripts/resume_20261120_curvature_qp_v3.py`。这些只换路径、源字节身份保持；父def1的重建接[完整Gauss投影首步配方](2026-11-20-gauss-fullspace-projected-first-result.md)，其载体/上游输入由该配方继续连接。

之后发现的低phi第二basin见[本方向真实结果](2026-11-20-physical-height-first-result.md)。本准备条记录的单witness范围不能外推为所有后来已知点均通过。
