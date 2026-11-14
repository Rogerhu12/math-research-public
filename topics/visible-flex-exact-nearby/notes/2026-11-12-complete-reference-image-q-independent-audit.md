# 完整有限参考的像门与 q 门独立审查

本次独立通读两份源码及两份证明，未重复作者的真实大批扫描。
结论是所述有限参考门的主要有向界与数学论证一致；下文列出一个不参与
证书的诊断字段注意事项。没有据此授予真实流 Jacobian、非实时间 q 门，
或尚未读取的全腿 cover runner。

## 绑定的版本

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_complete_reference_segment.py` | `3a6cbc6f1a2d490db72ecc4b977eca26becd4468284efd2fbf09023e2072a33f` |
| `scripts/fourfold_complete_reference_real_time_q.py` | `c74cf5220f08e6e083c147741a3905a01ddc2995a56b475f541bd54abf80157d` |
| `notes/2026-11-12-complete-reference-real-time-image.md` | `b05e8bfa523a1c3ebf5812e67d5b6ac887088830d9d8d36d34d522ddf89d47e4` |
| `notes/2026-11-12-complete-reference-real-time-q.md` | `a5d5bafb96a5294f8f2b759508147d2f3fced05c6bbb4be91489b724a3498996` |

## 1. 同一个完整有限函数

`complete_bernstein` 读取原段的八个 U 控制和八个 Q 控制，并核对其
shard 身份。前腿逐控制保留完整 `U+Q*a`；后腿逐控制保留完整
`U+Q*Qforward_end*a`。静态因子没有时间依赖，故乘法不改变七次
Bernstein 时间次数。Laurent 卷积不截断，频率偏移和零模位置正确。
零模实投影仅利用该准确乘积在实标签上的真实实值性；这里保留的是
准确系数的球包络，没有暗选未经付费的新中点。

`complete_periodic` 与已审的独立 package 实现共享完整代数。准确
subspan 的单项式表示可以用原整段的 Bernstein 凸性门，不必把复时间
单项式模和当成更差的实时间像门。

## 2. 像的连续角向覆盖

若 C 的正频率系数为 c_k，则上标签边界的虚部是实 Fourier 多项式，
其正频率为 `i*c_k*sinh(k*S)`，均值为 `S/4`。源码的符号正确。
实轴实值性给下边界的相反虚部，所以相同模界覆盖两个边界。

源码先给每个完整 Fourier 模求角导，再折叠到 DFT 格点。这种折叠
只计算有限多项式在节点的准确值；即使有限最高频率超过格点 Nyquist，
也不会遗漏高模的导数。闭单元半宽为 π/N。Taylor 表保留
`h^j/j!`，完整实角余项使用全部有限模的
`2*sum |c_k|*(k*h)^(p+1)/(p+1)!`。实角线段上指数导数的模没有额外
增长，因此无需错误地再补 `exp(k*h)`。

每个主证书单元先取有向上端点，之后才取全节点最大值。全标签带用
调和最大值原理，全实时间用八个非负 Bernstein 权重；两个覆盖步骤
均与源码一致。

## 3. q 的正实部与模界

归一化标签 x 对应物理角 θ=x/4，故 q=Y_x 的均值准确为 1/4。
两标签边界的 `Re q` 具有正频率
`i*k*c_k*cosh(k*S)`；源码随后按与像门相同的完整闭角单元方法给
上下界。每格先取有向端点，再作 min/max，避免重叠球的偏序选择。
源码另外计算
`1/4+2*sum k*|c_k|*cosh(k*S)`，它是完整 q 的模界，不能误读为仅
实部界。

若 `Re Y_x >= m > 0`，凸标签带上沿直线积分给
`|(Y(z)-Y(w))/(z-w)| >= m`，从而参考 lift 单叶。实周期提升的实轴
满射性以及半径 S 圆盘上的 Rouché 论证，给物理像包含宽 mS 的开带，
并给解析逆导数不超过 1/m。证明中的这些结论正确，但均属于所选
有限参考；真实流的接近误差仍需另付。

## 4. 诊断字段与范围限制

像门内 `maximum_node_Imag_modulus` 使用
`max(abs(v) for v in tables[0]).upper()`。当球有重叠时，这个普通 max
未必选择最大的上端点，因此这个字段不能独立当作严格的全节点最大
上界。实际证书 `physical_theta_image_strip` 使用先逐格 `.upper()`
后取 max 的另一条路径，不依赖该字段，故主要连续像门不受影响。
作者已获知并保留当前冻结字节，后续版本可改诊断字段。

本审查没有重跑 0/419/549 或全 550 段，没有审阅新增
`fourfold_complete_reference_real_time_cover.py` 的续跑闭包，也没有把
两份局部 helper 的正确性替代最终全域报告的完整性检查。
