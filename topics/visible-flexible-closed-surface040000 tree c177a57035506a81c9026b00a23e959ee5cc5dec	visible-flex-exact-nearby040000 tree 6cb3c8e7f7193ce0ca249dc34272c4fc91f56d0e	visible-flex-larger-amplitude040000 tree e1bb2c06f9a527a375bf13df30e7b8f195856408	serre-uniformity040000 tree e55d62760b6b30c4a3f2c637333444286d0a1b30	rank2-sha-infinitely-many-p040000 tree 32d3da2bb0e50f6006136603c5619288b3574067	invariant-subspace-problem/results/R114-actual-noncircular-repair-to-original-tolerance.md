# R114：实际闭族的非保圈修复达到原求解容差

2026-11-12，Astra-visible-flex-fd2d / root，接 R21、R25、R112。

**结论：实际新 C² 闭族在同一原 g、同一物理参数和整个 t∈[0,1] 上满足**

\[
\boxed{\sup_{p,t}\left\|g^{-1/2}(F_t^*e-g)g^{-1/2}\right\|_{op}
\le1.2566772507606437\times10^{-9}<2\times10^{-9}.}
\]

这里的上界已包含全部前缀、尾、镜像、圆领、固定帽、非线性拉回余项及唯一精确桥的目标转移。
它来自实际已保存的字段和完整连续区间计算，不是采样最大值、线性化预测或尚未实例化的充分 box。
同一新族保留 R21/R25 的全部像集几何，并已提供三个时刻的完整网格。

这完成 README 所接受的**基础数值交付及到原容差的有限加密证据**。
它不证明无限维精确等距族存在，不证明任意继续加密必在 C² 中收敛，亦不支付更强幅度目标。
按 README 要求，研究继续推进 held/D≥.2、δE/D≥.05 或相应严格存在，不能在此停止。

## 1. 实际对象、固定数据和可计算定义

原参考图 X 是 R21 指定的第一档 critical M12：

| 定义 | 实际文件 | SHA256 |
|---|---|---|
| common 前缀 | `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json` | `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2` |
| 同一有限尾 | `2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json` | `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104` |
| 原前缀目标供应 | `2026-11-09-db6f-root-flat17-m12-target.json` | `7b307dd26afbe669a9b52d9f1795ed49c775288f9c9d679759b6036cc3c5c47b` |
| 唯一精确桥 | `2026-11-09-db6f-root-exact-bridge-m12.json` | `1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa` |

以上文件均在 `notes/`。固定 flat17 的 vu=.17、vd=.18、ramp=.4、ramp_eta=.05、cycles=1、
delta=.07254443456654512、warp_reference_q=.1，及 weightedK6 的 width=.45、rCut=.6、wCut=.5、
protectCell=160、ell0、calibrationSteps=512 和同一无限 source 全部不变。
没有调动物理层数、尺度比、taper 或 g 来掩盖误差。

新的数值自由度是实际材料位移 \(v=(p,q)\)，允许 p 依赖材料角。
定义 \(\Phi=\mathrm{Id}+v\)、\(Y=X\circ\Phi\)。
保存的两字段分别在

- `notes/2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json`；
- `notes/2026-11-12-fd2d-metric-m12-gauge-tail-c2-streamfit-01/tail-field.json`。

两者各1025节点，定义数据为各节点共享的值、一阶和二阶 jet；区间上采用准确五次 Hermite 公式。
前缀保留512个三重周期的 ψ 模，尾保留192个材料 u 模，包含全部实际 cosine/sine 分量。
每件定义分片均 gzip 且小于5 MB；JSON 逐件绑定 hash。
字段是这些有限保存数据定义的准确 C² 函数，不是把拟合采样值冒称为连续函数。

完整可计算闭族清单为
`notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json`，
SHA256 `7cc24cf74d61da9415e3b63b460c5ed1af4681974c6ee84b31771e4facf519bc`。
它绑定前缀、尾、固定帽、原 g、精确桥、两字段、导数证明、旧几何证书及同像集网格。
`scripts/fd2d-metric-repaired-closed-map-v2.py` 的 `make/phi/demo` 提供清单生成与材料点浮点评估，
包括跨工作区的目录解析；其浮点查询误差并不替代本结果的连续证书。

前缀原材料角为 \(u=\psi-e(s)\sin(3\psi)/3\)，并满足严格正 Jacobian。
前缀 p 是 native s 位移；若物理经线坐标为 \(\sigma=s/\lambda\)，则对应位移为 \(p/\lambda\)。
尾 p 则直接是物理 σ 位移，保存的径向 jet 对 r 求导；尾变换按同一原 w 的单调弧长逆定义。
不能将它当作 r 位移，亦不能直接把 ψ 平移当作材料相位。

## 2. C²、固定接缝与全局可逆

完整字段报告
`notes/2026-11-12-fd2d-metric-m12-global-field-bounds-01.json`
连续覆盖每个 native 径向区间及所有有限角模，得到

\[
|p|\le1.5348355764193366\times10^{-11},\qquad
|q|\le2.1748397698072635\times10^{-11},
\]
\[
\|Dv\|\le1.5498138864425113\times10^{-8}<1,
\qquad \|D^2v\|\le1.9167021163731551\times10^{-4}.
\]

报告按原物理材料坐标支付 warp 和桥尺度的导数换算，未把 ψ 导数直接当作 u 导数。
中央满足 p=0、p_ss=0、q_s=0；原 warp 的中央导数也准确为零。
以 p 奇、q 偶延拓，中央镜像为 C²。
两侧 cut 有完整零字段开邻域；尾字段支撑在 r∈[.401953125,.5900390625] 内，
所以深尾、圆领及固定帽的字段恒零，全部接口两 jet 准确一致。

R112 §5 的提升条带证明直接适用：\(\|Dv\|<1\) 给双 Lipschitz 下界，
周期性、固定径向边界和次数一给全局满射。
因此 Φ 是原闭材料曲面的 C² 微分同胚，并在两完整固定帽上恒等。
这已经是实际已支付的可逆性条件；没有仅检查有限点 Jacobian 的正号。

## 3. 完整连续线性残差

记 \(h=X^*e=g+E\)，\(\mathcal L=E+\mathcal L_vg\)。
同一目标正交标架下，R112 的完整三项 Lie 导数均计入。
在尾部使用准确换元 \(k=dr/d\sigma=-(1+w^2)^{-1/2}\)；
前缀先消去 warp 造成的坐标 Gram 主项，再连续包围小残差。
实际有限字段的全部模态均保留。

| 区域 | 连续完整覆盖 | 线性相对算子上界 |
|---|---:|---:|
| 上前缀全部 native 域 | 3604个精确径向盒，全部角度 | 8.581678122630337e-10 |
| 尾字段活动域 binary .4至实际cut .6 | 5030个精确径向盒，全部角度 | 1.2566186391203421e-9 |
| 原 cuff 至 binary .4 | 原完整证书的26965行按精确半径合成 | 原 metric≤1.1313778765583975e-9 |

前缀由[0,2400)和[2400,3604)两份互不重叠的完整局部报告组成。
`scripts/fd2d-metric-prefix-union.py` 核对相同 geometry、target、字段及定义分片，
核对每个 cell/subdivision 恰出现一次、准确有理端点连续且覆盖两端，才产生
`2026-11-12-fd2d-metric-m12-prefix-linear-complete-03.json`。
前段上界为8.581678122630337e-10，后段为2.4640934296327403e-10。

完整尾报告为 `2026-11-12-fd2d-metric-m12-tail-linear-full-03.json`。
已完成区间的准确复用没有删去坏区间或改变图；旧1043盒的主动exit130、
下一轮1807盒的正常边界停止及最终5030盒的实际exit0记录均保留。

连续包围使用准确限制多项式、径向 Bernstein hull、完整角弧或全部 Fourier 系数的绝对和。
normal 算术仅扩大极小区间及下溢预算；只读三角矩阵的准备量可以缓存。
degree12径向加速把更高次幂的完整 signed range 加回同一个角系数，未删高次项；
其后不作径向微分。全部这些规则的证明和逐区间记录均随数据保存。
它们改变区间计算成本，不改变实际字段、原 g 或真实有限 Fourier 模。

## 4. 已实际支付的非线性后验

采用 R112 §4.1 的移位点恒等式，避免要求旧 C² 图的三阶导数。
在字段支撑及连线段上，已证明的原目标界为

\[
f\ge2/5,\qquad G_0=121/100,\quad G_1=11/5,\quad G_2=1000.
\]

若 \(|p|\le A,|q|\le B,d=\sqrt{A^2+B^2}\)、\(\|Dv\|\le\kappa\)、
\(\|D^2v\|\le H\)，旧图的相对误差为 δ，则

\[
N_* =\tfrac12G_2A^2+G_1\kappa d+2G_0Hd
+2\kappa\delta G_0+\kappa^2(1+\delta)G_0,
\quad \gamma\le1+G_1A/f_{\min}^2.
\]

实际新图相对本区域目标的完整误差至多
\(\gamma U_{lin}+\max(1,f_{\min}^{-2})N_*\)。
下表由实际区域字段界及旧图 δ 计算，没有使用未实现的宽松候选 box：

| 量 | 前缀 | 尾活动域 |
|---|---:|---:|
| 实际位移长度上界 d | 2.453749046526999e-11 | 1.8045171815041106e-11 |
| 实际 \(\|Dv\|\) 上界 | 7.676502902047499e-9 | 1.3800468383231936e-8 |
| 实际 \(\|D^2v\|\) 上界 | 6.283364928357972e-6 | 1.9160107909253822e-4 |
| 非线性坐标余项 \(N_*\) 上界 | 9.227133199781653e-16 | 9.377820016581995e-15 |
| 自身目标的完整 metric 上界 | 8.581735793553537e-10 | 1.256677250760643e-9 |
| 转到原固定 g 后上界 | 8.585055115033048e-10 | 1.2566772507606437e-9 |

前缀唯一桥的目标差已有 ε0≤3.319321476658082e-13，准确使用
\(\epsilon_0+(1+\epsilon_0)U_0\)，只转移一次。尾直接相对原 g，无此目标替换。
未变深尾上界为1.1313778765583975e-9，固定帽误差为零。
取全部区域及其镜像的最大值，即得本文开头的完整原 g 上界。

实际组合脚本 `scripts/fd2d-noncircle-actual-pullback.py` 已自然exit0。
输出 `notes/2026-11-12-fd2d-metric-m12-noncircle-whole-posterior.json` 绑定全部输入，
并明确 `exact_isometric_family_proved=false` 与 `infinite_refinement_convergence_proved=false`。

## 5. 全部时间、闭合和像集几何

在活动部分取

\[
F_t=R_{\alpha(t)}\circ Y\circ\tau_{-\alpha(t)},
\qquad \alpha(t)=2\pi t/3,
\]

固定帽逐点不动。τ平移的是物理材料角 u。
因为 Φ 在接口开邻域恒等，旧公共圆领两 jet 原样保留；新全族仍是同一连通闭材料曲面的 C² 嵌入。
对紧曲面上的 C² 图，角平移在 C² 范数下连续；旋转也连续，因此 t↦Ft 在 C² 拓扑连续。
原 g 在活动带对 τ 不变，故完整相对误差的空间上确界在所有 t 上相同。
本族没有时间积分离散误差，毋须用有限帧推测其余时刻。

注意本式一般不是 \(X_t\circ\Phi\)，因为非保圈 Φ 未必与 τ 交换。
另一方面 Φ 是活动圆柱的全局微分同胚，所以每一相位的活动**像集**恰等于旧活动像集，
两帽像集也完全相同。R21/R25 因此直接给

| 全族性质 | 已证明界 |
|---|---:|
| 整体直径 D | ≤3.787020263961937 |
| 全时绝对 reach | ≥562949953421312 / 4763997235009095 |
| 全时 reach / D | >0.03120330942723168 |
| 固定闭 H 的直径 / D | >0.9354609822667627 |
| held / D（不作刚体对齐） | >0.05278322519892998 |
| δE（含所有旋转、平移和反射） | 严格大于0 |

非全等性使用同一活动三阶矩和原三凸起固定帽的 R16/R21 证明；没有将材料点滑动计入 held。
这是同像集的准确转移，不需要另外假定新的曲率差分 box，亦不重新借用不同图的几何数字。

## 6. 实际固定 g 的下降链与严格存在差距

R21 的既有完整比较给
\(\mathcal E_{12}<(50/393)\mathcal E_8\)，且

\[
\mathcal E_{12}\ge
L_{12}=\frac{370012576184137}{18889465931478580854784}.
\]

该下界属于同一critical M12实际图，不是拟合值。
本文的新上界 U 与它作向外算术比较，实际得到

\[
L_{12}>15.5873774837922\,U.
\]

所以 M8→M12→本次实际材料修复形成同一物理 g、参数和时间范围下的真实下降链，
最后达到**原先就固定的**2e-9求解容差。新增自由度是实际数值字段的径向和角向表示，
没有重新拟合 g，也没有用额外物理层数压低一个不消失的缺陷。
旧 M14 的回升和所有失败继续保留，不宣称所有尝试的阶数都单调。

这支付的是 README 接受的有限数值收敛证据。
它没有证明完整无限加密序列的紧性、无限尾非线性精确解或严格非线性逆定理。
从有限误差界到“存在精确等距族且与这些有限图严格邻近”的无限维结论仍有差距；
本文不把1.26e-9写成准确零，也不借此声称更强比例的精确存在。

## 7. 网格交付与复现

三个文件均在 `notes/`，各71858顶点、143712面，gzip约1.3 MB，单件小于5 MB：

- `2026-11-12-fd2d-visible-m12-t0.ply.gz`；
- `2026-11-12-fd2d-visible-m12-t1of4.ply.gz`；
- `2026-11-12-fd2d-visible-m12-t1of2.ply.gz`。

每件实际序列化网格已通过闭定向流形及径向 PL 嵌入检查；公共面连接相同，4610个固定帽顶点逐位一致。
`2026-11-12-fd2d-visible-m12-family-audit.json` 保存完整交付检查。
由于本文逐时像集与旧图相同，这些是新族的同一几何网格；它们的顶点材料标签仍沿旧参数化，
不能直接当作新 Φ 的材料质点轨迹。浮点网格也不替代连续 reach 证明。

从课题目录可直接合并已保存的完整分区报告并重算后验；这不需要重求旧BVP：

```bash
python scripts/fd2d-metric-prefix-union.py \
  --part notes/2026-11-12-fd2d-metric-m12-prefix-linear-front-03.json \
  --part notes/2026-11-12-fd2d-metric-m12-prefix-linear-back-03.json \
  --out notes/local-prefix-union-NEW.json \
  --rows notes/local-prefix-union-NEW.rows.jsonl.gz

python scripts/fd2d-noncircle-actual-pullback.py \
  --budget notes/2026-11-12-fd2d-noncircle-pullback-budget.json \
  --prefix-linear notes/local-prefix-union-NEW.json \
  --tail-linear notes/2026-11-12-fd2d-metric-m12-tail-linear-full-03.json \
  --tail-regions notes/2026-11-12-fd2d-metric-m12-tail-gauge-support-regions.json \
  --field-bounds notes/2026-11-12-fd2d-metric-m12-global-field-bounds-01.json \
  --old-whole notes/2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json \
  --old-prefix notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-metric.json \
  --bridge notes/2026-11-09-db6f-root-exact-bridge-m12.json \
  --meshes notes/2026-11-12-fd2d-visible-m12-family-audit.json \
  --closed-map notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json \
  --out notes/local-whole-posterior-NEW.json
```

重建实际字段和连续区间的入口、原参数及其边界覆盖规则分别保存在 field-definition、
continuous-tail-proof、normal-interval、radial-range、cached-trig 等笔记及对应脚本中。
复现是可用能力；不把额外冻结、独审或再次求解设为本结果登记的前置条件。

## 8. 当前继续的强目标

本文的完整数值族已保证 held/D>.0527832、reach/D>.0312033、δE>0，
但没有达到 held/D≥.2 和 δE/D≥.05。R113 的窄 cuff/固定帽构造，
R115 的同周长中央支持族及 R116 的一阶 Codazzi/中央曲率参数化正在用于新的实际闭核。
它们各自已证明的局部几何窗口不替代一个真正通过全域 metric、尾接合及 reach 的强目标族。
后续工作继续求这个完整族；不把本次基础数值闭合作为收尾理由。
