# 局部更换椭圆核心、准确保留外域物理场

**状态：已证明下述表示、闭角、端口及外域保留恒等式；尚未计算本新初态，不主张等距、嵌入或 reach。**

本笔记给出一个新度量设计和一次初态审计的定义。它不沿用“更换整套核心基后逐列复制相同数字”的全域输运，也不改变已发布的求解器。

## 1. 参考场与目的

公开 `actions-43634358250-1-core_transport_initial_audit` 已记录一次 $B=37/100$ 的全域语义输运初态。其边界位置二 jet 正确，但细网格直接度量误差约 $67$，不能据此直接加大求解预算。核心参数改变后，原来的 $\phi(\theta)$、$u_{\rm core}(\theta)$、整个径向种子和不可变高度参考都改变；相同的系数标签并不代表相同的物理场。

本次选用此前已接受的九高度态作为**完整物理参考**，其公开来源是：

- 原始 enriched $c_0$：`notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json`；
- 原始独立高度 selected：`notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json`；
- 短入口 bounded 场：`notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz`；
- 九高度已接受态：`notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz`。

后者的 canonical 物理身份以 `f198ba74` 开头。完整身份和上述四份解压后字节 SHA 必须由严格 loader 重建；不是仅比较此前缀。原 $c_0$ 仍是不可变来源，已接受的高度态不会替换 $c_0$。

参考场记为 $(a,T,b,z_c,X)$。它已经包含短入口表示和完整冻结的 body 度量。其公式采用 [R57](../results/R57-direct-reconstructed-metric-and-auxiliary-frame-space.md)、[R60](../results/R60-independent-center-speed-fixed-ports-and-position-two-jets.md) 的同一规范：

$$
\langle T\rangle_\theta=0,\qquad |T|=1,\qquad
X=a\Pi T+z_c e_z,\qquad z_c'=b.
$$

$\Pi$ 是每个径向位置上的零角均值周期原函数。它**不是**沿径向从核心积分所有 $X_s$ 的另一种表示。原 $b$、原共同原函数 $z_c$、其初值和查询无关求积规则，本次全部保留。

## 2. 唯一新设计与完整度量

旧核心半轴为 $(A,B_0)=(1,7/25)$，新核心为 $(A,B_1)=(1,37/100)$。半宽、材料角归一方式、两侧符号和物理帽保持原定义。令

$$
a_{0,j}=\frac{1}{2\pi}\int_0^{2\pi}
\sqrt{A^2\sin^2\phi+B_j^2\cos^2\phi}\,d\phi,
\qquad \Delta a_0=a_{0,1}-a_{0,0}>0.
$$

这里 $a_{0,j}$ 是准确积分定义，不把双精度椭圆积分的打印值冻结成另一条曲线。两个材料角各自满足 $\ell_j(\phi_j)=a_{0,j}\theta$。令 $u_j(\theta)$ 是现有 `EllipticCylinderPort` 的连续、奇、$\pi$ 周期切角增量，定义

$$
\Delta u(\theta)=u_1(\theta)-u_0(\theta).
$$

新 cutoff 的起点取原准确开核的端点 $s_c=Lc_f$。本次固定长度

$$
\ell=\frac{81}{500},\qquad
\chi(s)=
\begin{cases}
1,&s\le s_c,\\
1-S_{11}((s-s_c)/\ell),&s_c<s<s_c+\ell,\\
0,&s\ge s_c+\ell,
\end{cases}
$$

$$
S_{11}(x)=462x^6-1980x^7+3465x^8-3080x^9+1386x^{10}-252x^{11}.
$$

$S_{11}'=2772x^5(1-x)^5$，故 $0\le\chi\le1$，两端至五阶导数均相容。当前 $s_c=9/250$，修改结束于 $99/500=.198$，严格早于原自然帽补丁。保留 $S_{11}$ 是为了使新增 $a'$ 在入口始于五阶，不改旧完整 $a'$ 的三、四阶系数；这**不**意味着旧切角系数已满足新核心的完整 Cauchy 条件。

定义

$$
d(s,\theta)=\chi(s)\Delta u(\theta),\qquad
T^*=R_z(d)T,
$$

$$
a^*=a+\chi\Delta a_0,\qquad b^*=b,\qquad z_c^*=z_c,
\qquad X^*=a^*\Pi T^*+z_c e_z.\tag{1}
$$

目标度量是完整的新函数

$$
g^*=ds^2+(a^*)^2d\theta^2.\tag{2}
$$

其中 $a$ 使用原 selected 已冻结的完整定义，包含全部 body 系数；不是用新核心重新生成 `NegativeKRadialSeed`，也不是将旧 body 系数解释在新种子上。因为 $B_1>B_0$，被积速度逐点不减且在开集严格增，故 $\Delta a_0>0$。于是 $a^*\ge a>0$。开核上 $a^*=a_{0,1}$；修改区外 $g^*=g$。这是**新度量设计**，不是旧固定 $g$ 的加密精化。

## 3. 闭角、准确核心与外域六 jet

原表示的水平切向满足 $T_{xy}(\theta+\pi)=-T_{xy}(\theta)$，而 $d(\theta+\pi)=d(\theta)$。因此新水平切向仍有相同的半周期反号，其角均值为零。绕 $z$ 轴旋转保持 $T_z$ 原样，其原反射奇性给出零角均值。注意一般情况下**整向量 $T$ 并不满足 $\pi$ 反周期**；竖直分量必须单独处理。由此

$$
\langle T^*\rangle_\theta=0,\qquad |T^*|=1,
\qquad X^*_\theta=a^*T^*.
$$

所以闭角和 $G=(a^*)^2$ 是准确表示性质，而 $E=1,F=0$ 仍待求解。

在开核 $s\le s_c$，原 $T$ 是旧椭圆的水平单位切向，且 $b=\sigma$，$z_c=\sigma(w+s)$。角增量准确换成 $u_1$ 后，$T^*$ 是新椭圆的单位材料切向。中心化椭圆的角均值为零，故同一 $\Pi$ 规范给出

$$
a_{0,1}\Pi T^*=\Gamma_1(\theta),\qquad
X^*=(\Gamma_1(\theta),\sigma(w+s)).
$$

准确新柱端口和全部位置二 jet 因而成立。

在 $s\ge s_c+\ell$，$a^*,T^*$ 及其所需径向、角向导数都恢复原场，而 $z_c$ 从未改变。所以

$$
(X^*,X_s^*,X_\theta^*,X_{ss}^*,X_{s\theta}^*,X_{\theta\theta}^*)
=(X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}).\tag{3}
$$

其直接核查式是

$$
X^*-X=(a^*-a)\Pi T+a^*\Pi(T^*-T)+(z_c^*-z_c)e_z.
$$

前三项中的每个差在外域都为零，没有另一个角向平移常量。若未来允许改变 $b$，则还须单独支付 $\int_0^{s_c+\ell}(b^*-b)\,ds=0$ 才能保留外域位置；本次没有此变化。物理六帽及其共同高度保持原场，不能按径向行重新拟合帽高。

## 4. 可直接审计的导数公式

令 $Jv=e_z\times v$，$R=R_z(d)$，则

$$
T_s^*=R(T_s+d_sJT),
$$

$$
T_{ss}^*=R(T_{ss}+2d_sJT_s+d_{ss}JT+d_s^2J^2T),
$$

$$
T_\theta^*=R(T_\theta+d_\theta JT).\tag{4}
$$

而 $a_s^*=a_s+\chi'\Delta a_0$、$a_{ss}^*=a_{ss}+\chi''\Delta a_0$。将这些量代回 R60 的六 jet 公式：

$$
\begin{aligned}
X_s^*&=a_s^*\Pi T^*+a^*\Pi T_s^*+b e_z,\\
X_{ss}^*&=a_{ss}^*\Pi T^*+2a_s^*\Pi T_s^*+a^*\Pi T_{ss}^*+b_s e_z,\\
X_{s\theta}^*&=a_s^*T^*+a^*T_s^*,\qquad
X_{\theta\theta}^*=a^*T_\theta^*.
\end{aligned}\tag{5}
$$

实现无须重建任何变化后的角基或把旧系数重新拟合；只读原参考完整场，作式 (4) 的确定旋转和式 (5) 的重构。查询无关的共同高度原函数直接复用原参考。初态 driver 不提供可变化参数或伪造的优化 Jacobian。

## 5. 本轮审计边界

新 driver 只构造一个 $B=37/100$、$\ell=81/500$ 的新初态，不优化、不抬帽、不加入新入口 $Q$ 列，不与多个新 $g$ 混合比较。它应保留：

1. 四份来源的解压后字节 SHA、完整 accepted 状态和 $c_0$ 来源；
2. 新核心、完整 $g^*$、旧 $b/z_c$ 的分别定义与哈希；数值椭圆积分值不进入物理身份；
3. 全部结构节点、旧短入口相对节点和新 cutoff 的 24 个子区间；
4. 同网格原参考与新场的 metric、形状、曲率、镜像对、R66 新 $B$ 高度门；
5. 新核心六 jet、外域全部六 jet、原 $b/b_s/b_{ss}$ 和共同中心的差；
6. 同一新状态 $384\to768$ 的 $\Pi$ 评价差，以及稀疏/密查询的共同高度一致性。

人工路径只用明确温和的人工核心和构造报告，覆盖同一输入回放与完整审计，不调用真实候选，也不调用优化器。数学恒等式不等于有限 FFT 的严格误差界；输出差值原样保存，不能将数值近似零升级为连续嵌入或 reach 证书。

本次可保持外域既有的有限网格诊断，但外域本身仍有较大的等距误差和镜像法弦缺口。新核心的曲率和幅度预算更宽裕，也不自动补足连接。初态若失败，应按修改区内的实际分布决定下一步，而不是将准确端口和新 $G$ 误作全度量成功。

## 6. 实现与唯一公开调用

独立文件为 `scripts/frame_localized_core_initializer.py`。它只读旧源码，并拒绝更改传入的任何参考系数；没有可误用的参数 Jacobian 或求解入口。实际构造检查 `GITHUB_ACTIONS=true` 和准确仓库名，四输入必须来自本题公开 `notes/`。来源 loader 先完整恢复原始 $c_0$、原 selected、短入口 bounded 和九高度接受态，随后才建立新核心。

人工路径使用 $(A,B_0,B_1)=(9/10,18/25,4/5)$，保持与真实新设计相同的“增加短半轴”方向。它通过显式构造的人工四报告覆盖真实 IO、gzip SHA、完整状态回放、模型冻结、稀疏查询和输出摘要；不调用 LP、QP 或任何非线性优化器。人工路径拒绝构造真实 $B=37/100$。原函数、旋转 $s/s^2/\theta$ 导数和外域六 jet 的检查只在公开 Actions 执行；本地仅做源码语法解析。

先在同一公开 job 执行：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_localized_core_initializer.py \
  --check-only --out "$RUNNER_TEMP/localized-core-development.json"
```

然后只有一次新初态：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_localized_core_initializer.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --out "$RUNNER_TEMP/core-B037-localized-accepted-initial.json"
```

完整报告保留来源和大对象；每次 checkpoint 另写有科学用途的 `-summary.json`，包括来源/源码 SHA、新旧物理与度量摘要、各区段指标、端口/外域/查询比较、完整二 jet 的角加密差。摘要绑定完整报告字节，不代替其复现数据。失败也写小报告，不会因 loader 错误只留下空 artifact。
