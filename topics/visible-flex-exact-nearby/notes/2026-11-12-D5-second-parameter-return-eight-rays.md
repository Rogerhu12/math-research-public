# 同一 D5 精确 affine 第三点的八条参数二阶返回

状态：**浮点数值证据**。本计算把 R62 的实际二阶参数源沿完整两支积分，
给后续参数 Taylor 认证提供量级和可重做入口；没有以八个角的最大值替代连续上界。

对象仍为 SHA256 `e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`
的准确 $\delta_3=-7832869216826619/4611686018427387904$，
根证书为 SHA256 `afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f`。
初始角来自同一个 dyadic $H$（SHA256 `028a95679f5c6e6ff6438b539c9c427f745f976a4dbc70b46c0bb01dd0f4fb49`），
在 516 格中取索引 $0,64,129,193,258,322,387,451$。求参数导数时，这八个初始角保持固定，不随 $p$ 改动 $H$。

## 完整变分而非有限差分

积分的五行状态依次为

$$
(Y,L,z,v,\ell)=(Y,\log J,Y_p,Y_{pp},(\log J)_p).
$$

第一支初值为 $(H(x)/4,0,0,0,0)$，第二支从第一支五行终值继续；
实际移动根已包含在固定 $\tau$ 的场中，不再另加端点修正。
选支先 $\sigma=-1$、$\tau:-\pi/2\to\pi/2$，后 $\sigma=1$、逆向返回。
每个真实径向节点代表处重启 DOP853，rtol 为 $10^{-9}$。
两支分别 4056 和 4092 次 RHS，总 8148 次，记录运行时间约 431 秒。

输出采用物理角 $\theta$，同时提供 R31 的归一 $x=4\theta$ 字段。
对于 $\mathcal R(x,p)=4R(x/4,p)$，准确比例是

$$
\mathcal R_p=4R_p,\qquad\mathcal R_{pp}=4R_{pp},\qquad
\mathcal R_{xp}=R_{\theta p}=J\ell.
$$

八个角的结果为

$$
\max|\mathcal R_{pp}|\simeq1.4426088142682127\cdot10^{-4},\qquad
\max|\mathcal R_{xp}|\simeq0.030588384360373096.
$$

这些量不是 R31 的 $\mathcal A_S$ 范数，也不对整个参数盒给出上界。

## 与旧真实一阶算法的交叉对比

旧 complete regular516 报告使用固定 $x$ 参数源，随后付两端根移动；
新方法从一开始固定 $\tau$，将两端移动放入场。相同输入角的最大差：

| 量 | 差 |
|---|---:|
| 保存初始角 | $0$ |
| 物理返回角 | $1.4784703239456576\cdot10^{-8}$ |
| $J$ | $1.379441654236757\cdot10^{-7}$ |
| 物理 $R_p$ | $3.111447080886287\cdot10^{-11}$ |

这里比较的 regular516 容差为 $2\cdot10^{-10}$，且使用不同时间网格；
因此角和 $J$ 的差不能归因于二阶参数公式。实际 $R_p$ 的两种端点处理得到一致数值，
与 R62 的点态解析列对比相互补充。

## 复放

在课题目录运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_second_parameter_rays.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
  --comparison notes/2026-11-12-D5-exact-affine-step3-Hnodes516.json \
  --out notes/2026-11-12-D5-exact-affine-step3-second-parameter-rays8.json \
  --rays 8 --grid-nodes 516 --tolerance 1e-9
```

该报告完整保存两个分支的五行终值，参数和角尺度均有字段区分。
还欠无限原函数/FFT 与三角函数舍入、根中心、近根积分商、完整 ODE 残差、连续角域和参数域；
源程序与本报告不给这些缺项任何自动授权。
