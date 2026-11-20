# 实际 M24 前缀—桥接口的精确共同 Cartesian 二 jet

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：已证明，精确有理检查已实际执行。** 当前 `newg-wide-lambda0p002-m24-linear` 的端点归一前缀与 R60 真 primitive 桥，在

$$
 s_b=\frac{2227378746688979}{4503599627370496}
$$

处具有字面相同的位置、一阶及二阶 Cartesian jet。两边使用同一材料角、同一目标半径在接口处的两 jet、同一 1168 点均值规则和同一个高度原函数锚。**此接口不需要新增修补。** 该结论不包括桥—尾接缝或完整闭面。

## 1. 实际对象及逐项精确相等

本条沿用 [R60 真 C² 桥](../results/R60-actual-m24-c2-bridge-and-continuous-metric.md)、[端点归一前缀](2026-11-20-m24-prefix-absolute-height-certificate.md) 和 `explicit_m24_prefix_pieces.py` 的既定定义，未使用旧 GL 查询的导数冒充真 primitive 导数。输入 run／physical 的 SHA-256 分别为

```
c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a
f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d
```

新的 `certify_m24_prefix_bridge_shared_seam.py` 只重建触及接口的多项式片，用 exact binary64 有理系数和既有共同 Hermite 操作计算两侧 trace。未重新计算整桥 Bernstein 范围、背景积分、均值积分或曲率。

- $s_b$ 恰为物理场节点，左片编号 354、右片 355。前缀左片的共同右 jet 和桥右片的左 jet 对全部 73 个系数的 $0/1/2$ 阶导数逐项相同，**219 个精确差全部为零**。
- $s_b$ 在角样条同一第 22 片内部。两边对原样条施加完全相同的共同右二 jet Hermite 操作和同一精确 warp；$e,e_s,e_{ss}$ 的三个精确差全部为零。晚期角 cutoff 在 $3s_e/4>s_b$，在接口附近尚未作用。
- 端点归一前缀在此精确为 $(a,a_s,a_{ss})=(1,0,0)$。桥的真实半径为 $a_+(s)=1-\int_{s_b}^s\sin\phi(u)du$；初相位是冻结参数下的 $p(3u^2-2u^3)$，故 $\phi(0)=\phi_s(0)=0$，桥的入口两 jet 也精确为 $(1,0,0)$。这里没有假设有限 GL 积分恰等于真积分。
- 前缀 lift 在 $s\ge\operatorname{binary64}(.9)s_b$ 恒为零，因此整个接口左开邻域的 lift 及全部所需导数为零；桥上 lift 按定义为零。

所有 Fourier 系数及其径向两 jet 相同就意味着全角 Cartesian 场相同，不是只在有限角节点上比较。由 $|e(s_b)|<1$，共同材料角图

$$
 \theta=\psi-e(s)\sin3\psi/3
$$

在接口处有正的角导数，所以计算坐标共同两 jet 也给出材料坐标共同两 jet。

## 2. 均值的一阶 trace 相等，不靠数值接近

接口附近两侧都可以写成

$$
 P(s,\psi)=a(s)e_r(\theta(s,\psi))+q\mathcal B(Y(s))(\psi),
 \qquad F=P+Z(s)e_z.
$$

在每个固定字面角节点，均值求值函数由完整截面的一／二角导数构造单位切向、法向、binormal，取 Frenet 正根并加上角图对流的竖向分量。记其截面量为 $T,N,B$、$k_a=a\kappa$，则两边都是同一个实函数

$$
 M(s)=\frac1{1168}\sum_j
 \left[-\frac{a'}{k_a}N_z
 +\sqrt{1-(a'/k_a)^2}\,B_z
 +vP_{\psi,z}\right](s,\psi_j).
\tag{1}
$$

前缀实现以 Cartesian 分量写此式；桥均值核以旋转后的 $(e_r(\theta),e_\theta(\theta),e_z)$ 分量写此式。该标架变换正交且保定向，保持范数、叉积和竖向分量，所以两个表达式数学上相同。它不要求求值程序的舍入顺序相同。

已经绑定的前缀／桥均值证书保证所需固定节点的 Frenet 正根与归一化分母严格为正，故 (1) 在端点输入附近为光滑函数。第 1 节已支付 $Y,Y_s,e,e_s,e_{ss},a,a_s,a_{ss}$ 的共同值，因而链式法则给出

$$
 M_-(s_b)=M_+(s_b),\qquad
 M_-'(s_b)=M_+'(s_b).
\tag{2}
$$

实际检查还确认严格核心缓存中的 1168 个字面 $\psi_j$，与桥源 `2*np.pi*np.arange(1168)/1168` 构造的数组逐 bit 相同。二进制数组 SHA-256 为
`f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf`，两边权重精确为 $1/1168$。没有换成 512、1536 点规则或连续角平均。式 (2) 来自共同输入及同一函数，未从两个包围区间重叠推出相等。

## 3. 同一个原函数锚及完整接缝

令前缀的真原函数为 $Z_-(s)=\int_0^sM_-(u)du$。桥上按既定 R60 对象取

$$
 z_0:=Z_-(s_b),\qquad
 Z_+(s)=Z_-(s_b)+\int_{s_b}^sM_+(u)du.
\tag{3}
$$

$z_0$ 是这个实际函数值，**不是**从已证区间中独立选一个数；它的既有区间只用于尺寸证书。式 (2)、(3) 分别支付 $Z,Z',Z''$ 的精确相等。结合第 1 节的非均值两 jet，得到

$$
 (F,F_s,F_\psi,F_{ss},F_{s\psi},F_{\psi\psi})_-
 =
 (F,F_s,F_\psi,F_{ss},F_{s\psi},F_{\psi\psi})_+
 \quad\text{于 }s=s_b.
\tag{4}
$$

由共同正材料角图，(4) 同时成立于固定材料 $\theta$ 坐标。材料目标度量 $ds^2+a(s)^2d\theta^2$ 的两侧半径有共同两 jet，所以无需改动任何参考度量或图。中央圆柱入口的独立局部修补在 $s\ge.001$ 已恒为零，故不影响此接口及式 (3) 的高度。

这将两边已证的同对象结论接合起来；尚在运行的完整前缀连续度量仍须依其自身终态，不因本接缝证明而提前宣布完成。桥—尾的真实参考及非旋转 Cartesian 场另付。

## 4. 执行和复现

实际本地进程 `20387`，观察到 `exit 0`，耗时 16.1998 秒。脚本路径为 `scripts/resume_m3/certify_m24_prefix_bridge_shared_seam.py`，SHA-256：

```
f58ac8fae15149e68eb2827b60e4fdbfbec1e7dda8146465b4a7690fd835cb01
```

使用的共同桥库 SHA-256 为 `85aff94a38f57e184e8bd5ca99b87898f0fec41043b0eedc9325623c4fba2c00`；共同前缀库为 `1a0a45db78a9aa62884459a6542d20f6995ea152962030919fbbb74d8aee573e`。完整执行输出只留 scratch，散列写于执行记录。

在本课题目录运行，`$WORK` 为运行数据父目录：

```bash
python scripts/resume_m3/certify_m24_prefix_bridge_shared_seam.py \
  --source-run "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --core-mean-intervals "$WORK/geometry-work/newg-m24-r53-core1168-intervals.npz" \
  --core-mean-certificate "$WORK/geometry-work/newg-m24-r53-core1168-certificate.json" \
  --prefix-height-certificate "$WORK/n4-work/prefix-z0-normalized-certificate.json" \
  --bridge-geometry-certificate "$WORK/geometry-work/newg-m24-r59-c2-geometry-combination.json" \
  --bridge-mean-certificate "$WORK/geometry-work/newg-m24-r59-c2-mean-certificate.json" \
  --interval-kernel scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py \
  --support-dir scripts/resume_m3 \
  --out "$WORK/geometry-work/m24-prefix-bridge-seam-certificate.json"
```

前述输入按各原证书的源、参数重建；本条没有新增积分或求解任务。

[精简执行记录](2026-11-20-m24-prefix-bridge-seam-execution.json)保存输入／输出哈希与精确比较结果。
