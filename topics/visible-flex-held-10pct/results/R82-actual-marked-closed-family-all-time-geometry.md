# R82 — 实际 .12 cut 标记闭族的全时嵌入与 reach

本条把 R79 的真实 .12 修补前缀和 R80 的真实整尾绝对几何接成同一张全时 C² 闭图，然后支付实际查询中已选定的正短柱与 canonical R67 三重帽的全部几何成本。原场仍为 λ=.002、q=.06、M24/N512 的原始 raw-H factor1，不是八轮 coupled physical-H，也没有准确 λ=1 握持圆弧。

## 实际全图界

全部相位、上下反射及完整 1152 段/18460 spans、原深领、平盘、中央短柱与固定双帽共同满足：

| 量 | 严格证书中的向外界 |
|---|---:|
| 位置范数 | ≤ 1.1925083405194168 |
| 完整初始直径 D | ≤ 2.3850166810388336 |
| 正支撑 X·n | ≥ 0.6420099883604928 |
| 主曲率模 | ≤ 精确 123/10 |
| 全时 reach | ≥ 精确 10/123 |
| 全时 reach / D | ≥ 0.03408815278085106 > 3/100 |

完整报告保存准确 Fraction；表中十进制只作向外展示。新标量入口实际 exit0，命令墙钟 .266352396 秒。没有重新求 BVP、native 积分、原有限 Fourier 多项式、连续角盒或真背景积分。

## 同一个实际柱长和帽

本条严格使用已真实查询的 binary64 `cylinder_half_length=.0025`：半长是 `5764607523034235/2305843009213693952`，总长是 `5764607523034235/1152921504606846976`。这个正数满足总长 ≤1/100，但它与精确有理数 1/200 不相等。后续活动矩应按这个总长代入 A3(ell)=A3(0)+ell*m3；不需要重做任何前缀积分。

帽半径是原 cuff 字面半径的一半，准确为 `900719925474099/36028797018963968`。实际正幅度是向下舍入后 `4722366482869643/75557863725914323419136`。此幅度准确满足 R67 的 min(1e−5,rc²/1e4) 限制。使用原全谐波有理函数帽，没有任何 Fourier 截断。

## 完整 Cartesian 接缝

原完整有限尾的全部共享边界、原均值、深领和平盘已付 C²；实际物理半径恒等 c=Rc 已独立严格验证。R79 使用真实弧长表达式 ap=−(1+w²)^−1/2、app=−w*wR/(1+w²)² 构造完整端点二jet差，所以前缀与尾部的六个 Cartesian jet 函数准确共享。不能把 query 的浮点误差打印当作这一事实的证明。

中心处的原 Hermite 目标在 ψ 图满足 X=Γ(θ)、Xs=e_z、Xss=b Γu，其中 θs=0、θss=b，且 Xψ=ρΓu、Xψψ=ρ²Γuu+ρψΓu、Xsψ=0。准确同一个反角图给

$$F_s=e_z,\quad F_{ss}=X_{ss}-(\theta_{ss}/\rho)X_\psi=0,\qquad F_u=\Gamma_u,\quad F_{uu}=\Gamma_{uu},\quad F_{su}=0.$$

因此上下半面分别平移 ±ell/2 后，与 Γ×[−ell/2,ell/2] 的完整二jet准确接合。实际共享角图的全域 ρ 下界为正，记录为 `4683743612465315/9007199254740992`；没有假设不同角参数恰好相同。新柱的支撑和核心曲率来自同一前缀 s=0 的已付连续界。

R67 帽在其边缘的值、梯度、Hessian 全部准确为零，并只作用于实际平盘内部。其余平盘为旋转不变的 collar，故固定帽与所有水平旋转的活动片在全相位中都共用同一二jet。最终 atlas 是一张无边界 C² 浸入球面。

## 有理预算和 reach

设 R0 为前缀与整尾的共同最大位置范数上界，h=ell/2，ε 为上述实际帽幅度。R54 的点对对应和 R67 帽位移界给

$$|F|\le R_0+h+2\varepsilon,\qquad D\le 2R_0+\ell+4\varepsilon.$$

前缀与尾部平移后的支撑分别只损失 h；柱的水平法向支撑直接继承核心。帽本身使用本次真实 pole 高度区间加 h，而不是采用 sampled query 的高度值。R67 给帽支撑

$$\frac{Z_{\mathrm{lower}}+h-26\varepsilon}{\sqrt{1+(24\varepsilon/r_c)^2}}.$$

并给帽曲率 ≤252ε/rc²。开方在原严格有理工具中向上包围。取各片最小支撑与最大曲率，得到上表值；其中全图曲率仍由原前缀的精确 123/10 控制。

套用已经证明的 R23 正支撑球面法向偏移定理，每个相位均嵌入，reach≥min(support,1/K)=10/123。所有旧片仅作刚体旋转/平移，帽固定不动，故以上是全相位结论，不是时间采样推断。

## 尚未由本条支付

本条只证明这张实际新闭图的完整 C² 几何、全时嵌入及 reach/D。完整 tail metric 的 Taylor 补充仍单独在跑；同场全前缀第三活动矩与尾通量界正在接合，δE 不由本条预先声明。准确 λ=1 圆弧、二维握持片的 10% 指标、冻结物理参数的同 g 精化收敛及题目完成标准仍分别欠付。

实际 source/query/R79/R80/完整尾/背景归一化/所有原均值/accepted packet/physical-R 恒等及 R23/R54/R67 文本均绑定 SHA。路径与小标量见同名 JSON，完整标量报告留在 scratch。

## 连续时间和可复现入口

取同一紧致参考球面的上述固定 atlas，令相位为 $\alpha(t)=9t/20$，$0\le t\le1$。各活动片只是同一 C² 场的水平刚性旋转与角平移，固定帽不动；紧集上到二阶的各导数一致连续，因此角平移在 C² 范数下连续。共同边界的全部二阶 jet 对每个相位准确一致，有限 atlas 的这一连续性可整体拼合，故 $t\mapsto F_t$ 在 C² 拓扑连续。这里不需假设场有三阶连续导数。

源入口 `scripts/resume_20261128/tail/closed_map_marker_cylinder_geometry.py` 的实际参数及 source/input/output SHA 见[小记录](../notes/2026-11-28-tail-actual-marked-column-closed-geometry.json)，原说明见[笔记](../notes/2026-11-28-tail-actual-marked-column-closed-geometry.md)。实际 summary SHA 为 `57480474eab2110d41053fee5ada0f02548dbb1b9e2fbaf56b9a16ce9fea742c`。前提分别来自 [R79](R79-actual-width012-cut-prefix-continuous-metric-geometry.md)、[R80](R80-actual-complete-tail-absolute-geometry.md)，全局正支撑/reach 定理直接应用已登记 [R23](R23-shared-jets-closed-c2-geometry.md)，帽使用 [R67](R67-universal-threefold-marker-and-euclidean-noncongruence.md)，没有重证明这些结构结果。
