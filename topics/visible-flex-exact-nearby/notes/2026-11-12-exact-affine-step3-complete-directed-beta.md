# Exact affine 第三步的完整有向 beta

## 1. 准确对象与结论

对
[type_fixed_step02_d5_exact_affine_step3_object.json](../data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json)
定义的准确 affine 图，
\[
\delta_3=-\frac{7832869216826619}{4611686018427387904},
\]
完整有向计算证明
\[
\boxed{37.02315597217<\beta(\delta_3)<37.02687658944.}
\tag{1.1}
\]

这里使用 R37 全核心 \(\ell\) 的零阶口径、R50/R52 的有限部定义，
物理频率 \(n=4j\)，\(\beta\) 为完整往返相位的 \(1/j\) 系数。
其同对象的高频算术输入满足
\[
\operatorname{dist}\left(
 \beta(\delta_3),\frac{\pi}{2\sqrt5}(2\mathbb Z+1)
\right)>0.20464135208.
\tag{1.2}
\]

(1.2) 对应 nearby D5 目标
\[
\rho_*=\frac{15121+\sqrt5}{27422},
\qquad 13711\rho_*^2-15121\rho_*+4169=0.
\]
它支付的是本准确点的次相位与奇 norm 格的分离；
实际 principal return 与 \(\rho_*\) 的匹配、完整散射余项及低块仍需各自支付。
不能据此将 \(\delta_3\) 自动标成最终 KAM 参数。

完整报告：
[beta-exact-affine-step3-complete-enclosure.json](2026-11-12-beta-exact-affine-step3-complete-enclosure.json)。

## 2. 输入身份及准确运算顺序

| 对象 | SHA256 |
|---|---|
| exact affine step3 descriptor | e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f |
| D5 origin NPZ | 0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b |
| actual parameter direction NPZ | 8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab |
| step3 tight root certificate | afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f |

运算从准确 binary64 原点和方向出发，以准确有理数 \(\delta_3\)
在 Arb 中形成 \(c_0+\delta_3v\)、\(\alpha_0+\delta_3w\)。
随后乘固定 base 的三次/二次幂，实施明确径向奇偶对称，并构造无限 R33
primitive。高度来自准确 slope 积分。
没有将 affine 系数先导出为一份四舍五入 NPZ 再当作同一图。

完整来源和证明方法见
[原图有向 beta 说明](2026-11-12-symmetric-complete-directed-beta.md)，
本次仅改变准确输入对象；所有原始分母、无限 primitive 尾、目标 E 尾、
真实根、collar、bulk、角误差和覆盖都为本对象重新计算。
原 sym 图的 beta、旧 D5 center 的普通浮点诊断都没有被转授。

## 3. 真根、collar 与全 bulk

以已有同族唯一简单根证书初始化，含无限 E 修正的 native Arb Newton 给出
\[
.23839687372973993292984897619358
<t(\delta_3)<
.23839687372973993292984897625034.
\]
固定准确切口为
\[
b=\frac{268136140016943}{1125899906842624}.
\]
准确径向对称和 quarter 频率换算给
\[
\beta(\delta_3)=\frac12
\left(I_{\rm bulk}+I_{\rm collar}\right).
\]

完整 collar 严格满足
\[
1307.20897680857<I_{\rm collar}<1307.20897711147.
\]
其径向 Taylor 尾不超过 \(1.514489\,10^{-7}\)，
完整角误差不超过 \(1.341133\,10^{-13}\)。
参数为 192 bits、Taylor degree 24、series precision 72、
quarter nodes 512、角 nodes 2048、根复圆盘半径 \(0.0006\)、
归一角宽 \(0.02\)。复圆盘分母门和真根 deflation 对本对象完整通过。

Bulk 仍用全部准确正、负 binary knots 分区，167 个原始 span。
两个独立任务覆盖 \(0\ldots83\)、\(84\ldots166\)，分别接受
136、121 个子区间，加上 \(0\le r\le2^{-20}\) 腰部小段。
所有任务无失败叶片。两份分片各保留 complete=false；
合并器重新校验全部准确端点后才给完整报告 complete=true。

原始 span 的物理多项式选择、极小相邻 knots、全部无限角尾、
连续角间隙、密度中的根号分支、腰部的奇对称积分商均沿同一冻结引擎支付。
在 128-bit Arb 积分层使用每原始 span \(0.0002\) 的预算，
并将实际误差球按保存的 lower/upper 端点合并。
最终 beta 半径小于 \(0.001860309\)。

## 4. 算术检验与实际限制

完整区间在归一化后满足
\[
52.70339113473<
 \frac{2\sqrt5\,\beta}{\pi}
<52.70868790150.
\]
因此到全部奇整数的距离大于 \(0.29131209850\)，
再乘 \(\pi/(2\sqrt5)\) 得 (1.2)。
合并器枚举实际区间附近全部奇整数，并对遗漏的远格点付统一距离界。

当前结果是准确点的证明。将它用于参数修正或 KAM 邻域时，
需要同一参数区间的 beta 界或统一 beta 导数预算。
目前已开始对明示测试盒
\(\delta\in[\delta_3-10^{-8},\delta_3+10^{-8}]\)
作保相关 germ 的统一 collar/bulk；
在完整覆盖前不把它当作已证 beta 邻域，亦不称其最终 KAM 盒。

## 5. 冻结文件和复放

| 文件 | SHA256 |
|---|---|
| scripts/fourfold_phase_beta_affine.py | b82724a2af026b9b9ee935f3df0eb95e7feb36ac5f65db9694085b5a4ad25991 |
| scripts/fourfold_phase_beta_affine_combine.py | b7c3a985af8a489f2a0b88aedb7a3e74721d3644925ed86bf431362e1a914cfe |
| notes/2026-11-12-beta-exact-affine-step3-collar.json | 037cd700677da4a34b423de431e9b22ab9903b5cd844a6a9348e6ccd0ee8918d |
| notes/2026-11-12-beta-exact-affine-step3-bulk-part00.json | c073d072bfb25c7774a8749b8d37b7ec6539e64a1203c59d96d8d1613a249b09 |
| notes/2026-11-12-beta-exact-affine-step3-bulk-part01.json | 1df2298ed56599e6e068118787ffb24937a9d92ff8ea36366f2c1b49d36e0d79 |
| notes/2026-11-12-beta-exact-affine-step3-complete-enclosure.json | 179c58121f284ea16c2522e4e3f1493f109f857d37be5de60cf445bbe8750680 |

全部 native 依赖 hash 也保存在各报告和合并报告中。
在本课题目录复放：

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_affine.py collar --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json --out notes/2026-11-12-beta-exact-affine-step3-collar.json

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_affine.py bulk --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json --collar notes/2026-11-12-beta-exact-affine-step3-collar.json --max-cells 84 --out notes/2026-11-12-beta-exact-affine-step3-bulk-part00.json

第二 bulk 任务改为 --start-cell 84，去掉 --max-cells，输出 part01。

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_affine_combine.py --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json --collar notes/2026-11-12-beta-exact-affine-step3-collar.json --parts notes/2026-11-12-beta-exact-affine-step3-bulk-part00.json notes/2026-11-12-beta-exact-affine-step3-bulk-part01.json --out notes/2026-11-12-beta-exact-affine-step3-complete-enclosure.json

重放的耗时字段可不同，源码/输入身份及科学区间必须重新核对。
