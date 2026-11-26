# 新 gap 前缀到真实 Cauchy 后段的紧支撑完整两 jet 连接

会话：Astra-visible-flex-6a65 / geometry；日期：2026-11-26。

## 1. 本次结论与输入身份

已经实现一个可直接消费**当前实际 Cauchy checkpoint**的供应器：新 gap $1.05$、$v=.045$ 的真实前缀保留到 $b=.1815625$，只在 $[b,b+.2]$ 内修改原位置场；其后直接调用原位置提供器及原 R205 真尾。幅度参数、实际 cuff 高度、物理末端均读取原 checkpoint，不重新指定。

当前实际 CI checkpoint 留在同一 runner，未下载到本地。本地已完成的两次自然 `exit 0` 检查使用明确新建的 `interfaceProbeOnly` 零自由系数输入，**不是 CI checkpoint、完整目标 baseline 或接受步**。它们支付新接口的接缝、原状态身份、导数实现核验；新 gap 全场的真实 metric、曲率、held、面积及完整求解仍须由同 job 实际 checkpoint 重新支付。

新前缀已在 `9ae1291f5709` 发表。其 master 文件及完整有限场定义见 `2026-11-26-6a65-geometry-coupled-gap-prefix.md`。本构造不重新计算该 Cauchy 流，不把有限 ODE 解当作准确 GC 流。R224 给出的全角 coast 域证书与本地 prefix 数值 consumer 之间的完整转移缺口仍在。R225 已单独支付总周长及统一缩放集合误差，但未支付完整角反参及两 jet；本接口不自动继承这些尚未证明的界。

## 2. 原场读取与真实末端

`6a65-geometry-cauchy-tail-source.cjs` 的原 SHA256 保持为

```
f5036c5f2df96ee75ef970a6f6f9c21bb7bb9447e623abd1674759736a14e440
```

新增 `6a65-geometry-cauchy-source-radial-cuts.cjs` 只补元数据。它读取同一个 `source.q.position.radialCuts`，不改状态、目标度量、位置或角原函数。原 `sourceFileSHA256` 保留，新增 `sourceMetadataAdapterSHA256` 单列新适配器身份。`completeIntegrationCuts` 在原 core cuts 外加入原 R205 的 $r=.34$ 转折及 $r=.32$ 真平 cuff。

原核心末端记为 $S$。整个半曲面接口的物理域是

$$
0\le s\le S+.48.
$$

当 $s>S$，返回原

$$
X^{\rm old}(s,u)=\operatorname{tailPoint}(.8-(s-S),u,Z_c;A_q).
$$

$A_q$、$Z_c$ 均从完整原 $z$ 读取，$Z_c=\mathrm{base.height}+z_{\rm cut}$。它们既不是中央椭圆半轴，也不是重新选择的 guide 值。真 cuff 的 $r=.32$ 在数值接口显式固定，以免相减舍入落到定义域外。原 $z$ 在查询前后逐列 `Object.is` 核查不变。

## 3. 显式紧支撑连接

记新前缀为 $X^-$，真实原场为 $X^+$。在同一物理 $s$ 与同一材料角 $u$ 下，先定义整条入口圆周上的函数

$$
\Delta P=X^-(b,\cdot)-X^+(b,\cdot),\quad
\Delta V=X^-_s(b,\cdot)-X^+_s(b,\cdot),\quad
\Delta A=X^-_{ss}(b,\cdot)-X^+_{ss}(b,\cdot).
$$

令 $h=.2$、$t=(s-b)/h$，使用

$$
H_0(t)=1-10t^3+15t^4-6t^5,
$$

$$
H_1(t)=t-6t^3+8t^4-3t^5,
\qquad
H_2(t)=\tfrac12(t^2-3t^3+3t^4-t^5).
$$

定义窗口内原材料场

$$
Y(s,u)=X^+(s,u)+H_0(t)\Delta P(u)
 +hH_1(t)\Delta V(u)+h^2H_2(t)\Delta A(u).
$$

窗口左侧直接使用新前缀，右侧直接使用原场。三个多项式在 $t=0$ 的物理 $0,1,2$ 阶导数分别选择 $\Delta P,\Delta V,\Delta A$；在 $t=1$ 的三个阶数都为零。因此两侧的 $X,X_s,X_{ss}$ 相等。对整条入口函数求 $u$ 导数又得到 $X_u,X_{su},X_{uu}$ 相等。这里没有把完整端迹换成若干端点值，也没有重新拟合旧后段。

实际实现还读取 $X_{ssu},X_{suu},X_{ssuu}$，使连接后的 $s,u$ 两 jet 以及周长的 $s$ 二阶导数来自**同一个**位置公式。旧场每次都在所请求的真实 $(s,u)$ 上查询；没有用 Fourier 或 Hermite 插值投影背景。Hermite 多项式只用于显式新增的紧支撑改变量。

该结论是位置场的 $C^2$ 接合，不宣称窗口等距、浸入、嵌入或曲率合格。若实际端迹很大，$h=.2$ 也可能不合适，须用该真实输入的几何结果决定。

## 4. 窗口内自然周长度量与完整角重参数

在 $Y_u\ne0$ 的区域，记

$$
q=|Y_u|,\qquad
a(s)=\frac1{2\pi}\int_0^{2\pi}q(s,v)\,dv.
$$

径向导数为

$$
q_s=\frac{Y_u\cdot Y_{su}}q,
\qquad
q_{ss}=\frac{|Y_{su}|^2+Y_u\cdot Y_{ssu}}q
 -\frac{(Y_u\cdot Y_{su})^2}{q^3},
$$

$$
a_s=\frac1{2\pi}\int q_s,\qquad
a_{ss}=\frac1{2\pi}\int q_{ss}.
$$

定义 $I(s,v)=\int_0^v q(s,w)\,dw$，以唯一严格单调的角映射 $v=v(s,u)$ 满足

$$
I(s,v)=a(s)u,\qquad 0\le u\le2\pi.
$$

其导数完整为

$$
v_u=\frac aq,\qquad
v_s=\frac{ua_s-I_s}{q},
$$

$$
v_{uu}=-\frac{a^2q_u}{q^3},\qquad
v_{su}=\frac{a_s-(q_s+q_uv_s)v_u}{q},
$$

$$
v_{ss}=\frac{ua_{ss}-I_{ss}-2q_sv_s-q_uv_s^2}{q}.
$$

对 $\widehat X(s,u)=Y(s,v(s,u))$，使用

$$
\widehat X_s=Y_s+Y_uv_s,\qquad
\widehat X_u=Y_uv_u,
$$

$$
\widehat X_{ss}=Y_{ss}+2Y_{su}v_s+Y_{uu}v_s^2+Y_uv_{ss},
$$

$$
\widehat X_{su}=(Y_{su}+Y_{uu}v_s)v_u+Y_uv_{su},\qquad
\widehat X_{uu}=Y_{uu}v_u^2+Y_uv_{uu}.
$$

于是 $|\widehat X_u|^2=a(s)^2$。这是**只改材料角**的重参数，不缩放或平移截面，因此窗口内几何集合、曲率与对固定点的距离都保持。$E=1$、$F=0$ 没有由此得到，仍交完整位置求解。

左侧准确形式 coast 与右侧 R201 原场均以恒速材料角表示。连接在两端保留全部相关混合导数，故上式在端点退化为恒等角映射并保留完整 $C^2$ 接合。实现于左侧调用已登记的 prefix normalization，右侧直接返回原 source；窗口内只用自然周长。数学定义使用准确积分；本次执行使用声明的有限 Fourier 求积及 Newton 逆，尚无这些求积的统一余项界。

新的目标半径因此分段为：原新前缀半径、窗口自然周长半径、窗口后原 checkpoint 的完整半径。它是新的物理度量输入，不能称作原 $g$ 下的一次改进。输出配置令中央 gap 为 $1.05$、$v=.045$，保留 $S$、$A_q$、$Z_c$；之后必须用全部 $\rho$ 列拟合 $a, a_s$。最终有限 base 加 $\rho$ 的实际度量及全场仍须重新评价。有限全局拟合也可能改动供应器的窗口外几何，不能转借“窗口外直接相等”的结论给拟合后的场。

## 5. 可用于真实输入的端迹预算

以下只给本显式连接的确定预算，不把有限角采样的最大值当作连续上确界。若 $p,v,a_2$ 分别是三条完整入口差函数的连续范数，则

$$
\|Y-X^+\|\le p+\frac{16h}{81}v+\frac{54h^2}{3125}a_2,
$$

$$
\|Y_s-X^+_s\|\le\frac{15}{8h}p+v+\frac h{10}a_2,
$$

$$
\|Y_{ss}-X^+_{ss}\|\le\frac6{h^2}p+\frac{27}{5h}v+2a_2.
$$

对角导数以相应的 $\Delta P_u,\Delta V_u,\Delta A_u$ 范数替换即可。常数来自显式多项式极值；例如 $H_1$ 在 $t=1/3$ 达到 $16/81$，$H_2$ 在 $t=2/5$ 达到 $54/3125$，$\|H_0'\|=15/8$。$H_2''$ 的三次 Bernstein 系数是 $(1,-2,1,0)$，从而 $\|H_2''\|\le2$。这些预算揭示缩短窗口会放大速度与二阶导数，不能只看位置差选择 $h$。

若记 $D_s=Y_s-X_s^+$、$D_u=Y_u-X_u^+$，则

$$
|Y_s\times Y_u|\ge |X_s^+\times X_u^+|
 -|X_s^+||D_u|-|X_u^+||D_s|-|D_s||D_u|.
$$

真实连续端迹界及旧场面积下界足够时，这提供一条直接检查窗口浸入的充分条件；当前本地探针没有支付这些连续界。

窗口后几何直接相等，因此改变中央见证点时可使用准确恒等式：若 $A_{\rm new}=A_{\rm old}+d$，则对同一点 $(x,y,z)$，

$$
\min_{\pm}|(x,y,z)-(0,\pm A_{\rm new},0)|^2
=\min_{\pm}|(x,y,z)-(0,\pm A_{\rm old},0)|^2
 +2d(A_{\rm old}-|y|)+d^2.
$$

这解释为何保留已有后段比整体重新压缩其几何更有针对性。数值应用仍须读取当前实际 checkpoint 的 held 与宽度，不能代入已遗失或不同物理输入的 baseline。

## 6. 实际本地接口回执

公共 candidate SHA256 为

```
9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d
```

本次明确新建零自由系数 probe 的 SHA256 为

```
caea08fb40e0d431bbd9dad90d833f20ea50cd5f0798df8cd0435426e7b54750
```

它有 1788 列、$A_q=.8746432018013935$、$Z_c=.51$、$S=.9772364498716914$，除实际 cut-height 和 tail-amplitude 两列外自由系数为零。不是任何 CI 已接受态。

### 接缝及一个自然周长探针

`cauchy-short-window-zero-probe01` 实际自然 `exit 0`，外部时间 $3.333914517$ 秒，峰值 RSS $132812$ KiB；原 oracle 子进程也自然 `exit 0`。

在五个非原生角上，完整六 jet 的左接合最大差为 $1.9552\times10^{-16}$；右接合及窗口外直接 source 对比全为零。此处是所请求有限点的真实差，不是连续域误差证明。

在 $s=.2525625$，256 点周长求积、五个请求角给出：

| 项目 | 实际值 |
|---|---:|
| 材料角逆残差 | $8.8818\times10^{-16}$ |
| $\max||X_u|^2/a^2-1|$ | $4.4409\times10^{-16}$ |
| 新自然半径 $a$ | $1.0095013261722645$ |
| $a_s$ | $.04550948089189985$ |
| $a_{ss}$ | $.13409987755850913$ |
| 原 source higher-jet 一致性最大差 | $4.6337\times10^{-14}$ |

五个请求角上的入口修正最大范数分别为 $\Delta P=.02062344$、$\Delta V=.22162099$、$\Delta A=4.78980800$。它们只属于此接口 probe，不能视为当前 CI 的端迹，也不能视为全角上界。

该报告 SHA256：

```
a671b05ebb467786f61dd7a53745d65625572454130c11dd4558a533ac45f228
```

### 一个内部完整导数检查

`cauchy-short-window-zero-jets01` 实际自然 `exit 0`，外部时间 $11.085744278$ 秒，峰值 RSS $202684$ KiB；同样不是新全场 value。它在上述 $s$ 处、$u=.947,3.641$、步长 $2\times10^{-5}$ 上使用五点差分，与**同一个**归一化位置公式返回的完整导数比较：

| 检查 | 最大相对差，以 $\max(1,|\cdot|)$ 归一 |
|---|---:|
| $\partial_s X=X_s$ | $7.91\times10^{-11}$ |
| $\partial_s X_s=X_{ss}$ | $1.31\times10^{-10}$ |
| $\partial_s X_u=X_{su}$ | $2.27\times10^{-11}$ |
| $\partial_u X=X_u$ | $9.49\times10^{-9}$ |
| $\partial_u X_s=X_{su}$ | $2.11\times10^{-7}$ |
| $\partial_u X_u=X_{uu}$ | $5.30\times10^{-9}$ |

半径一、二阶导数的差分别为 $4.83\times10^{-12}$、$1.31\times10^{-13}$。角向误差保留了 256 点求积与差分的限制；本次没有宣称所有导数达到舍入误差，也没有从该检查给出统一误差界。正式 export 的默认周长求积是 1024 点，仍须在实际新场上记录结果。

该报告 SHA256：

```
3ef1b539c1377000a102e6b1ef2bfcb0669b97da87e99994236e579511c04068
```

## 7. 同 job 消费接口

源码 `6a65-geometry-cauchy-short-window.py` 导出 `ActualCauchyOracle`、`ShortWindowMaster`。后者提供：

- `raw(s,u)`：前缀、真实原场或显式窗口；
- `normalized(s,u,quadrature)`：上述完整两 jet 与 $a,a_s,a_{ss}$；
- `correction_ports(u)`：入口全部角导数的实际差；
- `target_config(actual_checkpoint)`：保留真实物理末端和 $A_q,Z_c$ 的新 gap 配置，不含旧 $z$；
- `export`：完整半曲面采样、逐截面 metric/曲率/held/面积诊断、新配置与来源 SHA；原数组只写 runner 的 Git 目录外。

角接口采用 $[0,2\pi]$ 的材料角支；闭圆周按周期延拓。export 包含前缀 master 节点、其间点、全部原 `radialCuts`、窗口、完整后段与真 cuff，不只导出内部核。

同 job 中把实际 checkpoint 传给 `--checkpoint`，而不是本地 probe。新前缀 master 由已发表的 `6a65-geometry-coupled-gap-prefix.py` 在同一 runner 重生或消费该 runner 当轮已生成的文件；不从仓库或 artifacts 搬运原始 checkpoint。示意命令的路径均须绑定本次真实文件：

```sh
python scripts/6a65-geometry-cauchy-short-window.py export \
  --scripts-dir scripts \
  --candidate "$candidate" --checkpoint "$actual_checkpoint" \
  --ramp-master "$new_ramp_master" --coast-master "$new_coast_master" \
  --window .2 --angles 128 --quadrature 1024 \
  --output-prefix "$fresh_outside_git_prefix"
```

将导出 NPZ 中 $s\le S$ 的网格交给 `6a65-cauchy-global-position.cjs reference`，以新 `-target-config.json` 构造完整新 reference；再由 `6a65-cauchy-global-warm-fit.py --fit-radius` 拟合完整 theta/phi/height/rho 列。真实 R205 尾仍在样本与回执中保留，但参考拟合本身只到 $S$。最后才计算该新完整 provider 自己的 value、normal、LM，所有接受与有限几何结论各自记账。

本结论没有把接口成功或 $G$ 归一化当作完成课题；准确等距族、完整封帽的全局嵌入、全时 reach 与 held 强比例均仍未完成。


## 8. 冻结实现身份

| 完整源码 | SHA256 |
|---|---|
| `6a65-geometry-cauchy-short-window.py` | `bcf00e15fbe036dabb14df793ef7caf246c3b00aac385f40d6469954be3c9560` |
| `6a65-geometry-cauchy-source-radial-cuts.cjs` | `3553ab18a3ca6f7de551687ba6d099484a9a06eff2736aa6cfce12368487d9e1` |
| `6a65-geometry-cauchy-short-window-check.py` | `f6995a246187bac50a86cf6c9ab3ad9c44b3dfa668270f0c6c6a5c6ebeb23f06` |
