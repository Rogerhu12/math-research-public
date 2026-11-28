# 直接物理极径、材料角与高度的同度量实际步

[R300](../results/R300-direct-unclamped-physical-tensors-and-six-fixed-metric-steps.md) 的初态从 R289 四次实步的最终空间位置直接建立。初始和末态在全部角度下分别证明了嵌入、空间包围和两项强形变比例。新位置允许更改三个真实函数；每次实际更新均重新量化为新三次控制表，最后的位置单独作整数检查。

在物理极角坐标 $(s,\theta)$ 写 $U=\pi w/2$, $h=-U_s/U_\theta,\ k=1/(r_0U_\theta)$。在圆柱正交标架中，令 $A=(R_\theta,R,z_\theta)$，则固定材料切向为 $V=(R_s,0,z_s)+hA$，另一个归一切向为 $W=kA$。对 $V,W$ 的三个实际 Gram 分量取解析变分，曲率直接从本图计算。真实二阶空间向量在该标架为 $(R_{ss},0,z_{ss}),(R_{s\theta},R_s,z_{s\theta}),(R_{\theta\theta}-R,2R_\theta,z_{\theta\theta})$。用二阶形式的实际主方向微分，对材料归一正负特征值、两侧曲率、板和握持距离加线性约束。每次步长判定重算完整非线性位置，优化后重新作认证。

第一套径向自由度把中央一格的修正强行归零、外边切断。874 变量的训练没有接受，有限小步的曲率陡增。改为在原物理 $s/T$ 上布置粗样条，中央宽度和角继续止动，竖直修正按奇延拓处理，右端保留三阶消失。782 变量的普通法方程有一次实步，移位峰 .12016668、曲率 14.96131。再从同一直接物理初态独立采用 600 变量稀疏极值规划，六次均获真实接受，步长 $1/8,1/4,1/4,1/8,1/4,1/4$。以下数据针对这一支。

| 同一固定 $g$ | 1122×145 四分区角的度量/曲率 | 移位 1063×173 的度量/曲率 | 全原生 17046×60 的度量/曲率 |
|---|---|---|---|
| 初始直接物理场 | .12188749 / 14.93075 | .12184194 / 14.91481 | .08175732 / 13.94998 |
| 六步末场 | .11510299 / 12.89165 | .11456356 / 12.87736 | .09699129 / 12.60533 |

末态另用原 physical primitive 在新张量每个径向 knot 和中点逐一求目标母线，1017 个真实径点和 257 个四分区角给 $.1148264892$，最大实测曲率 $20.38853114$ 位于 $s=1.45538353235,\theta=.969475858$。这一角径组补出了常规观察遗漏的曲率峰。首次写该附加回执因 NumPy 整数未转 Python 整数，在 JSON 输出时中止；转换后整次重新计算并自然完成。全部有限数值另于整数嵌入和形状证明记录。

使用 R295 [公开真实数据生产记录](2026-11-28-2ecf-r295-cubic-physical-polar-sources-and-true-infinite-joins.md)中的 `S,W,b` 环境，NumPy、SciPy、单线程 BLAS。HiGHS 采用 IPM；六步各轮真实状态均由脚本落盘，线性调用有 45 秒时限。

```bash
python "$S/2ecf-r295-final-image-direct-polar-source.py" "${b[@]}" --spans 512 --angles 128 --prefilter .5 --out "$W/r295-direct-physical-N512-M128.npz"
python "$S/2ecf-r295-direct-tensor-fixed-g-physical-solver.py" "${b[@]}" --source "$W/r295-direct-physical-N512-M128.npz" --radial 380 --angular 73 --space 32 --modes 7 --steps 6 --mu .025 --trust .0013 --out "$W/r295-direct-physical-LP600-own1.json"
for n in r295-direct-physical-N512-M128 r295-direct-physical-LP600-own1; do
  python "$S/2ecf-r289-cubic-meridian-exact-separation.py" --source "$W/$n.npz" --out "$W/$n-separated.json"
  python "$S/2ecf-r295-direct-physical-shape-bounds.py" --source "$W/$n.npz" --out "$W/$n-shape.json"
  python "$S/2ecf-r295-direct-physical-observe.py" "${b[@]}" --source "$W/$n.npz" --out "$W/$n-actual.json"
done
python "$S/2ecf-r295-actual-cubic-knot-rows.py" "${b[@]}" --source "$W/r295-direct-physical-N512-M128.npz" --out "$W/r295-direct-cubic-N512-true-knot-rows.npz"
python "$S/2ecf-r295-actual-knot-and-active-angles.py" "${b[@]}" --source "$W/r295-direct-physical-LP600-own1.npz" --knot-rows "$W/r295-direct-cubic-N512-true-knot-rows.npz" --out "$W/r295-direct-physical-LP600-own1-knot-fixed.json"
```

| 源或状态 | SHA-256 |
|---|---|
| `2ecf-r295-final-image-direct-polar-source.py` | `8bb89b6acfe623ec9ca37713efafed30ccddfd7647e0dcf565246aca1075df12` |
| `2ecf-r295-direct-physical-shape-bounds.py` | `31c7f15b0162984be57ce3d8c6ea2558c513602a11127b24f7bcccd4036e9b0f` |
| `2ecf-r295-direct-physical-observe.py` | `583df9a6463ef4e20e61ffc2660090035749fe1938756dd78fba607104883af1` |
| `2ecf-r295-direct-tensor-fixed-g-physical-solver.py` | `1b00584d1725f38be9f813952a4c954dc3f5f24a4b65de3c7ddecb3ff9222ff2` |
| `2ecf-r295-actual-cubic-knot-rows.py` | `8ed5606bedbb074355478463d3b1125e3162c7a0f229d821df1b39ddbe3f3730` |
| `2ecf-r295-actual-knot-and-active-angles.py` | `7eebefd35d10b74ba9909b33c5a596364a3eaad892512f9ce1fffebd14cd9294` |
| `r295-direct-physical-LP600-own1.json` | `b0d67ab643fa191ee8ff3a6bb26bd48f894a4e3f625c841761b143366111c748` |
| `r295-direct-physical-LP600-own1-knot-fixed.json` | `98462666f260c38be7c21105e603f8d729b2c1e253ce694ef70b72cb09756139` |
| `r295-direct-cubic-N512-true-knot-rows.npz` | `836f8ed7914ec495f29a473c52fa0d0b34a1b8018328820a52703afef8514b55` |
| `r295-direct-physical-N512-M128.npz` | `cf16ed27408b6566885ee70ced9a6a8b45b68287e1e08f380d0f8db1abd26ca2` |
| `r295-direct-physical-N512-M128-shape.json` | `5eba853478dabba953a5496c6bb3852cc1398cef45174b9a79193dc45570a1f6` |
| `r295-direct-physical-N512-M128-separated.json` | `e3b4dad745f7758fd88679418b1322bc50984900c4592203f98690e2c121046f` |
| `r295-direct-physical-N512-M128-actual.json` | `db50f3c5201e886211dbd4f48d9cb1ec09897c0f6370eacc7c042086d8cf6408` |
| `r295-direct-physical-LP600-own1.npz` | `d88fd5a3b8535bcf8536fde9d80a10779fbcef414cb5f93ea919787f8893ede6` |
| `r295-direct-physical-LP600-own1-shape.json` | `433eddff08d7020f922429fdd0352518ab40d7d4a2253d4c00ab85c6b40a01f0` |
| `r295-direct-physical-LP600-own1-separated.json` | `b9408adb882953655d7b1e8e043d5af204d08ae9a3d3442e216f501eaa8cdb70` |
| `r295-direct-physical-LP600-own1-actual.json` | `601a719831d2a6f9893e144c0dfe68aea1b1f22589712230e93bafeb85934c82` |
