# 同一 M12 检查点的两档 critical 尾：连续 C² 比较

2026-11-09，`/root/coupled_prefix`。状态：**两个保存的有限 C² 图在共同物理外域上的连续向外舍入差界；另有唯一最坏跨的浮点定位。** 不是无限 Cauchy 证明、源 ODE 认证或新的真实 BVP 求解。

## 1. 固定对象及输入绑定

两个输入均来自最终 M12 真联解尾 `_0018`，其检查点 SHA256 相同；manifest 的全部 `parameters`、最内锚点和最外锚点逐项完全相同。

| manifest 短名 | SHA256 |
|---|---|
| `db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json` | `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104` |
| `db6f-tail-inc-flat17-m12-critical-r005-outer128-q512-manifest.json` | `79e0ebcdca1654e4186eb245c02ce89d0fd6c88cd174a3317d30bbd798d47c69` |

第一档 18,553 节点，第二档 20,953 节点。第二档改变 raw0 的输出分割及其内部 RK 取值步长；源检查点仍为 native64。**相同检查点并不表示两个 exporter 的内部数值源取值完全相同。** 各自的 stage 端点补偿保留在原 manifest；第二档报道的 Fr/Frr 补偿量约为 $3.87\times10^{-10}$、$2.23\times10^{-7}$，不从本次差界扣除。

## 2. 方法：低内存，原数学公式

新适配脚本为 `scripts/db6f-prefix-tail-c2-stream.py`，SHA256

`8da5bb581fbe45bbec10dde3cabce9d755cfdc43fb4d5a334aff90713828c4ea`。

它复用已经独立审查的 `db6f-audit-tail-stream.py`，SHA256
`adfcfbfe03643cf8a4284c078edb13d5caa49ad5eb7f94ce822ba8c27354a456`。
该类给出精确有理物理半径及每跨的 Fr 四次插值、精确积分所得 F 五次多项式、其 Frr 三次多项式的向外区间系数。底层连续后端 SHA256 为
`ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`。

新层只做以下存储操作：把每跨系数轴从 `(degree,C)` 转成 `(C,degree)`；按带符号频率标签嵌入两图模式的并集，缺失模式填精确零；缓存一个批次。随后仍调用未修改的 `db6f-tail-c2-compare.py`，SHA256
`673eb497bbb232932af779178d973e1fedeb333143086718931741af18302099`。

原比较器按 Fraction 合并两个物理径向分割，对每个公共跨精确仿射复合各自多项式，相减后作向外 Bernstein 系数界。角向导数通过各带符号整数频率的相应幂精确加权，再以 Fourier 系数和给全部角度的欧氏向量范数上界。没有角度采样来替代连续上界，也没有把近重合节点合并成另一张图。

`tail_theory` 已独立全文核对适配层，并从 AST 抽取其真实类验证轴、符号模式并集和缓存：2250 个复制区间端点及 1650 个补零槽全部相同。见 `db6f-tail-review-c2-stream.md/.json`。原低内存类与原全量 F/G/Gp 的全 M8/M12 按位核对见 `db6f-root-review-tail-stream.md`。本次进程真实 exit0，峰值 RSS 571,486,208 字节。

## 3. 连续差界

完整输出 `db6f-prefix-tail-m12-critical-r01-r005-c2.json` 绑定上述输入与所有后端哈希。两图的共同域为

$$
0.1525361819534748\le r\le0.6,
$$

这里显示的小数对应 manifest 的同一精确二进锚点；实际计算使用其 Fraction。公共分割有 **39,503 跨**。记两图相对于同一精确旋转背景的扰动之差为 $\Delta V$，则全域、全角度有：

| 导数 | 连续欧氏范数上界 |
|---|---:|
| $\Delta V$ | $5.647553103800752\times10^{-11}$ |
| $\partial_\theta\Delta V$ | $1.3535914211394948\times10^{-9}$ |
| $\partial_{\theta\theta}\Delta V$ | $3.6698673098541194\times10^{-8}$ |
| $\partial_r\Delta V$ | $3.6042877929189616\times10^{-9}$ |
| $\partial_{r\theta}\Delta V$ | $8.591523077773289\times10^{-8}$ |
| $\partial_{rr}\Delta V$ | $6.120922613335622\times10^{-4}$ |

rr 最坏公共跨为约

$$
[0.5277879619574253,\;0.5277881171726982].
$$

其全域 planar、height 分项上界分别为 $2.9097877948463535\times10^{-5}$ 和 $5.829943833850985\times10^{-4}$。

只对这个唯一最坏跨另作 97 个径向点、512 个角点的浮点定位，记录于 `db6f-prefix-tail-m12-critical-r01-r005-c2-worst.json`。观察到 rr 向量差约 $1.8919346333528294\times10^{-4}$，位置 $r\approx0.5277881139390467,\theta=0$。这不是区间下界；它说明该跨的差异不能全部归于向外包装宽度。少量源诊断由 `tail_theory` 接续，不再重复全域比较。

## 4. 使用范围

这些是物理 $(r,\theta)$ 坐标下、同一背景相消后的实际有限多项式图差。两图采用“最深保存端口 mean-height 扰动为零、向外累计”的共同规范。报告尚未比较最内 R6 collars，也没有加入组装闭图的公共高度平移规范。虽然此次两个外域锚点完全相同，适配器对一般输入仍只比较精确交集，不能把略不同锚点认成同一端口。

rr 差既不是 `actualXYZMetric`，也不是 `sourceFullD` 或 `fullTensor`。README 第5门的核心仍是固定 g 加密使实际等距误差达到求解/机器容差；**不另加“所有二阶图差达到 $10^{-11}$”门槛**。本结果用于辨清表示误差、曲率稳定性与精确极限证据。此次位置和一阶差已小，剩余 rr 最坏跨值得局部查因，但不打断 M14 紧容差因果试验和 M16 真联解。

## 5. 重跑

在仓库根目录运行：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-tail-c2-stream.py \
  topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r005-outer128-q512-manifest.json \
  /tmp/m12-critical-c2-independent.json --batch 64
```

输出必须使用新路径；脚本拒绝覆盖已有报告。最坏跨浮点定位可用 `db6f-prefix-tail-worst-c2.py --comparison <新报告> --out <新定位文件>` 重跑。
