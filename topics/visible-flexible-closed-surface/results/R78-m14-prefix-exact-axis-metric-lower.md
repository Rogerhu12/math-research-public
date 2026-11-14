# R78：本轮 M14 保存前缀的严格轴点误差下界

作者：`/root/numerical_recovery`；2026-11-10。
**状态：已证明；全文未参与者独审及真实独立重放通过。**
本稿只对实际已经导出的有限 prefix 与其 frozen target 给严格点下界。
尚未生成的 exact common-cut 图及 exact-bridge 转移明确留作后续绑定；不把本稿当完整闭图或 README 完成。

## 1. 实际对象与程序

本轮 root restart8000-02 已真实成功，并通过完整 final；其后按全审计划，原 gzip 单件实际触文件上限，另名采用新无损分片族。
实际 base 为 `2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json`，
SHA `11cd5569b3c2218591a757aea966f9aa25963fa1a3ec69fbb0b6729cb141a42d`。
M=24 是 Cartesian 有限表示，原 BVP 为 M14/N512，不能混为一次源方程频率加密。
base 含 6599 个原生节点，由已保存的 binary64 两 jet 及 mean increments 定义精确有限图。
它不是区间运算生成的一族任意系数图，也不由浮点 power coefficients 定义。

actual target SHA `dbfb5c348a6921b078c1ee25c9aa5874856de303afd11b1e6277ac1eebdbbd8c`；
基础全域 metric 报告 SHA `b076c6c052a00d72d201ca9c76a3a5a724e9dc70350437cb14fa90d430f0c48a`，
6604 区间上界 1.4677456599912536e-7。后者仅用于完整输入身份及研究定位，不把它用作下界。

新只读检查器：`scripts/78718-prefix-nodal-axis-lower-v1.py`。
它核六份冻结 reader/codec/continuous/common-cut/metric/supplier 源的实际 SHA，
由已审 storage reader 重组原 gzip/NPZ 字节并核整个逻辑 SHA、各片哈希、全部数组 dtype/shape。
核 target/base/metric 的真实连接、所有系数有限、mesh 严格增加，随后只读一阶 nodal jets。
不导入 BVP、RHS、tail evaluator、SciPy solver，不生成新的图，不修改物理参数或数据。
完成前再次核全部来源及实际数据文件字节身份。

检查命令（在本题目录，实际执行）：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-prefix-nodal-axis-lower-v1.py \
  --geometry notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json \
  --target notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-target.json \
  --metric-certificate notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base-metric.json \
  --out notes/2026-11-10-78718-numerical-prefix-axis-lower-01.json
```

真实工具启动 `baa0a5` / session84911，随后 `950f89` 自然 exit0；不是程序自行声称出口。
零 solver/ODE/geometry producer。12246 个轴点比较只选择一个反证见证，没有调整候选参数。
独立重放必须改 `--out` 到新文件，因为检查器拒绝覆盖。

## 2. 精确有限图在轴点的一阶导数

写保存图

$$
F(s,\psi)=R(s,\psi)e_r(\psi)+T(s,\psi)e_\theta(\psi)+Z(s,\psi)e_z,
$$

$$
R=r_0+\sum_{j=1}^{M}r_j\cos(3j\psi),\quad
T=\sum_{j=1}^{M}t_j\sin(3j\psi),\quad
Z=z_0+\sum_{j=1}^{M}z_j\cos(3j\psi).
$$

原 `ExactHermite` 使用共享节点二 jet 的精确五次 Hermite 多项式。
每个多项式在两个端点匹配值、一阶导和二阶导。
精确 mean-increments 只替换 $z_0$ 的节点位置，保留所存 $z'_0,z''_0$；
因此在任意内部原生节点 $s_i$，每个 $r'_j,t'_j,z'_j$ 恰等于对应保存 binary64 数的精确二进有理值。
左右跨同用这一 jet，故无需任选单侧极限。

在 $\psi=0$ 或 $\pi/3$，令 $\sigma_j=1$ 或 $(-1)^j$。严格恒等式为

$$
R_s=r'_0+\sum_{j=1}^{M}\sigma_jr'_j,\qquad
T_s=0,\qquad
Z_s=z'_0+\sum_{j=1}^{M}\sigma_jz'_j.
$$

由于 $e_r,e_\theta,e_z$ 正交且在求 $s$ 导数时不变，

$$h_{ss}=|F_s|^2=R_s^2+Z_s^2.$$

三角因子只用 $\cos(j\pi)=(-1)^j$、$\sin(j\pi)=0$ 的恒等式；
程序从不近似计算 $\pi$ 或三角函数。每次读入 float 后均立即 `Fraction.from_float`，
所有求和、乘法和与预算比较均为 Python 任意精度整数有理运算。
显示上下端点由 Fraction 与 binary64 直接比较后用 `nextafter` 向外取整，并再次核有理包含。

## 3. 冻结目标上的 Rayleigh 下界

冻结辅助坐标图为

$$\theta(s,\psi)=\psi-e(s)\sin(3\psi)/3.$$

原 frozen target 是材料坐标中的 $ds^2+a_0(s)^2d\theta^2$。
上述两个轴点满足 $\theta_s=0$，因此不论该点的 $a_0,e,e'$ 数值如何，
目标系数严格为 $(g_0)_{ss}=1$。本结论无需目标 packet 的近似 $a/e/ep$ 系数。
对任意正定目标 $g_0$，相对误差算子范数至少为任意方向的 Rayleigh 商，故

$$
\left\|g_0^{-1/2}(h-g_0)g_0^{-1/2}\right\|_{op}
\ge\frac{|(h-g_0)(\partial_s,\partial_s)|}{g_0(\partial_s,\partial_s)}
=|R_s^2+Z_s^2-1|.
$$

这是单点下界，而不是离散点的上界、残差估计、L1 傅里叶上界或经验外推。
一个严格超过预算的点就足以排除该保存图相对于此目标的全域预算；
比较更多验证盒不会改变这一事实。

### 实际有理见证

原生节点索引 **1518**，$\psi=\pi/3$；$s$ 的精确值为

$$s=2474546589463719/9007199254740992.$$

节点经线度量的精确正误差为

$$h_{ss}-1=195218973193994774141785525686442227132484300518388614511974314980962119494394380394542319233604772662814099505/2521728396569246669585858566409191283525103313309788586748690777871726193375821479130513040312634601011624191379636224.$$

向下舍入显示值 **7.7414749922943985e-08**，
严格大于原预算 $1/500000000$。所有精确导数及误差分数都在 JSON 见证内，未把数组读入对话。

## 4. common-cut 支撑关系与精确目标坐标缩放

原已审 common-cut make 的实际表达式是

```python
start = int(np.searchsorted(mesh, mesh[-1] - args.width))
```

请求宽度仍为原 `.15`。本检查逐字使用相同 binary64 减法和 searchsorted；
这只是读取将来原 make 的确定性支撑位置，没有构造新图或假设新的末 jet。
实际 `start=6124`，$s_{start}$ 下端显示 1.8720381178742067，
而见证索引 1518 严格小于 start，$s_i$ 显示 0.27472985991302756。

common-cut adapter 对原 mode 系数补零至完整尾基；只在 `range(start,len(mesh)-1)` 中增加修正。
故若按该冻结定义从本 base 构造 common-cut 图，它在此见证所在邻域与 base 完全相同。
补零改变数组维数而不改变函数。这是确定性数学支撑结论，尚不是“该 common-cut 产物已经存在”。
镜像 wrapper 的入口二 jet 修改只影响第一跨，见证在内部；此处无需再估计镜像误差。

还必须尊重原 exact-bridge 的坐标约定。已审
`2026-11-09-db6f-exact-bridge-and-metric-transfer.md` §3 先将图还原为真实材料角，
再用 $u=\lambda s$，$\lambda=S_0/S_*$ 把保存域送到精确目标域。
虽然轴点固定材料角仍等于固定辅助角，但经线速度乘 $\lambda$，所以最终方向误差为

$$|\lambda^2 h_{uu}-1|,$$

不能直接省略 $\lambda$。若新实际 bridge 提供正的严密区间
$0<\lambda_-\le\lambda\le\lambda_+$，当前见证 $h_{uu}>1$ 下的可用条件下界为

$$\lambda_-^2 h_{uu}-1,$$

前提是右端正；否则取包含 $\lambda^2 h_{uu}-1$ 的区间到零的距离。
这只需要本轮真正桥证书中的缩放区间，不需要整图重跑连续 metric；
也不需要在轴点估算半径扰动。将来桥/共同图的 SHA 必须实际存在并绑定此 base/target/own tail 后，
才可生成那份新转移证据。本报告的 `new_exact_bridge_target_transfer=false`、
`complete_closed_graph_rejection=false` 明确保留此缺口。

本次结果不推所有同一物理 $g$ 的 M14 图均不合格，不排其他频率或数值求解；
它只排除这一个冻结有限 prefix 对 frozen target 达到原预算。
当前误差约 7.74e-8，不能通过改变包围方式、增加验证盒或把主 BVP RMS 当 metric 来消除。
下一步定位保存源曲线、谱投影、分支与表示各项误差，保持原物理 $g$。

## 5. 冻结文件与复核范围

- `scripts/78718-prefix-nodal-axis-lower-v1.py`：9205 B / SHA256 `661bc0daf17b303cfc3c093b9f913b9f003f68f0463b24bda0557ad72c48cbf8`。
- `notes/2026-11-10-78718-numerical-prefix-axis-lower-01.json`：7601 B / SHA256 `ccce95078e16f2b503dc3df1f19503c8e15b8362647007db5f9ea243f1c746cf`。
- `notes/2026-11-10-78718-numerical-prefix-axis-lower-01-observed-exit.json`：2104 B / SHA256 `782b5ead75bb552245f16c27d62d4c9f7746a26a016b6bb46ff0b4127b821d05`。

来源的逐文件身份、实际逻辑 gzip/NPZ 与分片闭包都保存在报告中。独审须核全文数学、全部新脚本、原 Hermite 与 common-cut 关键定义，并以新输出名实际重放；任何未来桥/闭图仍须另行实际绑定。

## 6. 冻结来源、完整独审与正式范围

[原稿](../notes/2026-11-10-78718-numerical-prefix-axis-lower-v1.md)8767B，
SHA256 `989f3109bb4bd7af752b7e81044f4b8bbc431f59be8a8008b668c6facee9cbe3`；
[完整独审](../notes/2026-11-10-78718-audit-prefix-axis-lower-v1.md)13591B，
SHA256 `5658a242b85b0671209e84a2860dbb0eff2e687c7c3b022f490c5027b73b1f21`。
root26e639全文回读。正式数学正文只改标题/状态，原稿、原数据与源码保持冻结。

未参与者真实 b1bd09/session43214→e22b4c 自然exit0，0BVP/ODE/producer。
[独立报告](../notes/2026-11-10-78718-audit-prefix-axis-lower-01.json)7601B，
SHA256 `97e229ad32c4b1efc0d305ed5c1ff9734e6304e1e8f3dcd326b842c938634083`；
6a3722随后核除运行秒数外与作者报告全部字段同一，六源/八输入实物未变。
本结果只排除这一个有限prefix相对frozen target的原预算；真实exact-target/common图仍须本图λ和身份绑定。
