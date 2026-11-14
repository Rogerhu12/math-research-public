# 饱和源反射 + 无限 Gaussian 六帽 pilot：冻结实现

日期：2026-11-14。状态：**源码与人工开发检查冻结，可由公开仓库 Actions 运行唯一研究 case。** 本地未评价真实研究候选，未运行优化。原反射版与未饱和热版均保留供复核，本次实际入口只选饱和版。

准确帽、热平滑和源半径出生门分别见 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md)、[R48](../results/R48-six-cap-angular-jump-and-heat-extension.md)、[R51](../results/R51-heat-source-radial-birth-and-saturated-reflection.md)。这次修正不声称有限场类存在准确 `R=0`，也没有度量、闭合嵌入或完整 reach 证书。

## 1. 明确的新基场，原度量与准确物理帽不变

保留准确径向度量 `g=dt²+a(t)²dθ²`、原椭圆柱核心、材料坐标、原 enriched 234 个自由列和原始固定系数 `c0`。源输入固定为

`notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json`。

不以失败的单向弯尾末态替换 `c0`。输入读取会核旧实现 SHA、完整核心/端口/空间/度量/形状身份、所有精确二进制有理系数及原模型记录。

六帽仍为准确 `R=137/500` 外盘、`rc=11/50` 握持盘，六法向为 `jπ/3`，幅度为 `[3/16,1/8,1/8,3/16,1/8,1/8]`，采用 S9。令 `d=R√3/2`、`w=R−d`，这次只把反射源位移改成

\[
c=\frac w4=\frac R4-\frac{R\sqrt3}{8},\qquad
e(\varepsilon)=c\tanh(\varepsilon/c),\quad \varepsilon=a(t)-R,
\]

\[
E_{sat}=3g_{cap}(R)-3g_{cap}(R-e)+g_{cap}(R-2e).
\]

`e(0)=0,e′(0)=1,e″(0)=0`，故准确帽端的完整二 jet 不变。对所有非负有限 `ε`，

\[
R-2e>R-2c=\frac{R+d}{2}>d.
\]

两个内源圆始终高于帽出生半径；这条严格代数范围不依赖候选计算。`c` 与源半径下界均按 `Q(√3)` 写入物理身份，浮点 tanh 只是评价。新内部源坐标的 `e_t,e_tt` 由链式

\[
e_t=(1-\tanh^2(\varepsilon/c))a',
\]

\[
e_{tt}=(1-\tanh^2(\varepsilon/c))a''-
\frac{2\tanh(\varepsilon/c)(1-\tanh^2(\varepsilon/c))}{c}(a')^2
\]

计算，没有把这些导数替换到物理度量 a 中。

仍固定 `h=1/10`、`τ0=1/128`，

\[
\widetilde E=e^{\tau(t)\partial_\theta^2}E_{sat},\quad
\tau(t)=\frac1{128}((t_f-t)/h)^6,
\]

\[
f_{new}(c)=B_{old}+Bc+
\chi(t)\{\mathrm{flat}+\widetilde E-f_{old}(c_0)\},\quad
\chi=1-S_9((t_f-t)/h).
\]

这个无限热积分是数学定义。有限 GH 只是评价，不能将其有限平移和的角光滑性混作无限函数的性质。详细混合 jet 和端口估计见 [Gaussian 评价说明](polygonal-tail-Gaussian-evaluation-20261114.md)。自由参数列 `B` 不乘 cutoff，故原完整参数 Jacobian 保留；固定 `c0` 进入新基场和身份。位置依旧由共同的 R28 整圈原函数及核心锚定中心积分重构。

## 2. 文件分工与无隐式换模型

| 文件 | 责任 |
|---|---|
| `polygonal_tail_heat_extension.py` | 冻结的无限 Gaussian 定义、直接 Jet22 复合与小批 GH 评价 |
| `polygonal_tail_saturated_heat_extension.py` | 独立饱和源坐标、准确代数身份及人工检查 |
| `frame_collar_polygonal_heat.py` | 共同求解/预算门/审计流程，显式 `extension_factory` 接口 |
| `frame_collar_polygonal_saturated_heat.py` | 唯一实际入口，明确选饱和 factory，并记录自身与新 module 的 SHA |

没有运行期 monkeypatch，也不修改原七个实现或已冻结的准确六帽/原反射实现。默认调用共同 runner 仍代表未饱和热版；薄 driver 显式标 `saturated-reflection-Gaussian-c_equals_cap_width_over_4`。新热 identity、完整 model/space hash 和这个标签均能区分两者。

每次 GH 精化先逐项断言完整 model、space、anchor、heat、metric、tail、core、port 和精确系数列表完全相同。GH 阶数、采样与求积只在 evaluation/configuration 中记录。薄入口报告共锁 13 个真实源码 SHA。

## 3. 一个 case、两类工程门、一次主要优化

径向仍使用准确有理的 61 层：49 个左段节点、补丁九个子区间、开放尾三个子区间；角向 192。每个准确节点及定义 hash 均保存。初态使用原 `c0`，系数逐位保持；无截断或裁剪。

先保存旧场的只读球审计和新网格上的未改前缀位置二 jet 对照，再按确定规则选择评价阶数：

1. 同一冻结初态比较 GH32 与 GH64 在整个已采样补丁上的 `value/s/θ` 最大差。若不超过 `1/10000`，选 GH32。
2. 只有第一项失败时才增加 GH128，比较 GH64 与 GH128。若过门，选 GH64。
3. 两项都失败时仅保存三档固定参数诊断，不启动优化。

每档固定系数成本分别保存；提高积分阶数造成的成本变化不记作优化下降。`ss/st/ssθ`、R 和全部位置二 jet 差同样原样保存，但不冒充连续曲率证书。

评价门通过后还要求选定档的初始新目标 cost 不超过 `1`。两个阈值均为明确的计算预算门，失败不构成数学排除。通过后仅运行一次 `least_squares`：234 个未知量、系数盒 `[-8,8]`、最多 250 次函数评价。整个优化只比较同一选定 GH 阶数内的成本。每十次评价或 60 秒保存当前最佳 checkpoint。

活动形状目标仅为球与条带：`|X|≤101/100`、`|y|≤19/50`，权重 `2/sqrt(Nr*Nθ)`；旧高度、椭圆量只保作诊断。完整域条件若真正成立时才可用 R40 的宏观预算，采样惩罚不支付连续包含、嵌入或 reach。

## 4. 独立误差账与内存

最终保存选定 GH 下的均匀 `121×384` 和 `121×768` 评价，以分离位置原函数 Π 的角 FFT 误差；再在同参数、固定 384 角下比较选定 GH 和其加倍档。另并入补丁端点、13 个补丁节点与径向分段点。真实帽的位置二 jet 以同一个 `h_cap=side*zc(L)` 比较，不为每行另配高度。

GH 每批至多八个节点。共同 runner 又按径向行分块，当前 192/384/768 角下每次最多 16384 个 `(t,θ)` 点；因此单个批次的 Jet Taylor 数组约不超过 10 MB。至少保留一整角行，因此极端未来角数超过这个目标时须另审，不把当前内存说明扩到任意配置。分块只切独立径向查询，不改变节点、权重、角查询或模型；中心积分仍在完整径向网格上完成。

当前只是浮点评价：源代数值、GH、FFT、中心求积、tanh 导数舍入都没有连续认证。全部完成/嵌入/reach 标志保持 false。

## 5. 最终人工检查

全部只用不同于研究模型的小型人工输入，没有真实候选评价或优化。独立同行已静态复核饱和公式、代数身份、factory、参数 Jacobian 不变性、两门流程、同身份加密和分行逻辑。

| 检查 | 最差结果 |
|---|---:|
| 饱和源 `e_t` 有限差分 | `2.8311e-10` |
| 饱和源 `e_tt` 有限差分 | `1.9262e-8` |
| 饱和标量空间 jet 相对差 | `7.1942e-9` |
| 准确帽端完整 Jet22 差 | `1.8190e-12` |
| 饱和全 runner 参数 Jacobian 相对差 | `3.3699e-9` |
| 独立目标成本公式差 | `5.56e-17` |
| 未改前缀七项位置/R 差 | `0` |
| 整批与逐行同查询评价差 | `0` |
| GH 改阶时完整物理身份/系数一致 | `true` |

人工 24 角下，**核心端 X 分量的 Π 重构**与准确核心存在 `1.6693244404564211e-6` 差；这个不利数值完整保留。固定同一核心、状态和系数，角数加倍到 48/96 后分别为 `3.6584624219859855e-11`、`2.7018723498128807e-14`。核心不调用热外延，因此这一定位直接针对 Π 截断；没有放宽门限。其他核心 jet 和尾端检查约为机器舍入水平。

同一人工饱和 runner 的 GH16→32 仍有 `ss` 差 `8.5750e-3`、`ssθ` 差 `1.0559e-1`，也保留在输出中。`passed` 只覆盖链式、身份、拼接和实现检查；不声称研究参数的高阶求积已精确。

检查文件：

- `notes/polygonal-tail-heat-extension-check-20261114.json`
- `notes/polygonal-tail-saturated-heat-check-20261114.json`
- `notes/frame-collar-polygonal-heat-check-20261114.json`
- `notes/frame-collar-polygonal-saturated-heat-check-20261114.json`

## 6. 冻结哈希与公开 Actions 命令

| 源码 | SHA256 |
|---|---|
| `polygonal_tail_heat_extension.py` | `abb965c27ce1aa19acd74a54cf301b3ff5589182a116d69819963717d56aa699` |
| `polygonal_tail_saturated_heat_extension.py` | `cda1570637d8b9bdc8d5891a944ee6fc2a6a2252d56141c2a6b8053b73ccfcdc` |
| `frame_collar_polygonal_heat.py` | `15dec10f4adbe5f7adce7f0a6f3abbfbfbe0fcdf14d52f1d08272cb1246a209f` |
| `frame_collar_polygonal_saturated_heat.py` | `483d0decb4cedd083ee3c9da8b499096c4aa51b3c23bb0140f8f7281f5a248fa` |

饱和全 runner 的最终人工输出 SHA256 为
`af6c033facaccd6a25a66985a63c649f585b03acae06033018102b3be9bdf8d2`。

仅在公开仓库 Actions 的研究命令：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_collar_polygonal_saturated_heat.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --out "$RUNNER_TEMP/frame-ellipse-six-cap-saturated-heat-fixed.json" \
  --support-width 1/10 --tau0 1/128 --heat-order 32 \
  --initial-cost-limit 1 --initial-heat-first-jet-limit 1/10000 \
  --radial-nodes 61 --angular-nodes 192 --quadrature-order 4 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --field-bound 8 --max-nfev 250
```

该命令尚未在本地执行；研究结果由公开 Actions 的实际日志、输出和来源回执决定。代码在非指定公开 Actions 环境下拒绝研究回放与求解。
