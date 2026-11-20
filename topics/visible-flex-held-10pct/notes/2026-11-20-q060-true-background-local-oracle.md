# 当前 4.625 尾背景的真部分积分、物理半径两 jet 与实际 x 图跳跃

维护会话：Astra-held10-1b6d88ec-20261120。

本文接 R58 及
`2026-11-20-q060-tail-tight-integral-certificate.md`，把其同一真实背景做成可调用的区间接口。
首 valley 是 **4.625**；不是 R21 的 3.125 背景。未运行新 BVP 或 shooting。

新源为 `scripts/resume_n4/q060_true_background_oracle.py`，伴随
`certify_q060_background_chart_jump.py`。[真实执行摘要](2026-11-20-q060-true-background-local-oracle-execution.json)保留输入／输出哈希、完整命令和查询。完整生成区间与数组仅留 scratch，按根 README 第 15 条不入库。

## 1. 固定的数学对象与归一化

输入仍是 R58 从原 `q060-port.json` 导出的 160 个 cell 常数。每个
`calibrationAlpha` **取已经记录的 binary64 数对应的精确有理数**；本次没有重新校准。
`delta0`、`etaRatioAtN0`、各 `R`、valley/cap/weight 参数也沿用该定义。
`oldCut`、原始半径与各 log/exp 取 R58 所写的真实公式，不把保存的 JS 派生近似值重新定义成该公式的真值。

在原 cell/segment 内，记原始径向函数为 \(r_o(x)\)，\(b_o=r_o'>0\)，
真实 log 坡度为 \(z(x)\)，\(w=e^z>0\)，\(E=1+w^2\)，正权为 \(W\)。令

\[
A=(1-\chi)b_o j_0+\chi\frac{|w_x|}{8E^{3/2}},
\qquad B=\chi\frac{b_oW}{E}.
\tag{1}
\]

普通段 \(\chi=1,j_0=1\)；最外保 cut 段 \(\chi=1-S_5\)、
\(j_0=1+(r_c/r_{o,c}-1)S_5\)；最深保护段 `(159,0)` 取
\(\chi=S_5,j_0=1\)。其余 `cut-preserving` soft cap、首 cell 的五层正权和全部有限 valley 与 R58 相同。

设 \(\mathcal A,\mathcal B\) 是全部 160 个修改 cell 的真实积分，
\(r_{160}^o\) 为同源真实深端。唯一归一化是

\[
\alpha_*=
\frac{r_c-r_{160}^o-\mathcal A}{\mathcal B},
\qquad r_x=A+\alpha_*B.
\tag{2}
\]

程序读取已经真正执行过的紧积分证明，使用其精确有理端点包围

\[
161.1632545693437\le\alpha_*\le161.1632546049038.
\]

**该区间是唯一数 \(\alpha_*\) 的包围，绝不选其中点作为新物理参数。**
更紧的同一真实积分证书可缩小计算不确定度，不改变目标 \(g\)。保存的
\(\alpha_J=161.16325458995925\) 仍是原 JS 数值构造的归一化；原 ready/checkpoint
不能仅凭参数相同就声称已经针对式 (2) 得到完整认证。

程序同时核紧积分源 SHA、证书所用常数文件 SHA，以及与路径无关的完整定义 SHA
`e764e2cc370f0b7a8a55324f2744702017c16690195f45db92ca66b9781bae56`。
后者含参数、160 个 cell 常数、原 port SHA 和 factory SHA；换校准根会被拒绝。

## 2. 部分积分的可验证计算

每一查询严格保留原 \((n,j,x)\)。从外切口向内累加

\[
I_A(x),I_B(x),I_{wA}(x),I_{wB}(x)
=\int_{(n,j,x)}^{\text{cut}}(A,B,wA,wB),
\]

从而

\[
r(x)=r_c-I_A(x)-\alpha_*I_B(x),\qquad
H_{\rm drop}(x)=I_{wA}(x)+\alpha_*I_{wB}(x).
\tag{3}
\]

对于整段 \(x\in[l,u]\)，四个积分均是非负 integrand 的反向 primitive，故取
\(\int_u^1\) 的下界和 \(\int_l^1\) 的上界，加上外侧各完整段即可覆盖**全部**该区间。
不是节点插值，也不是径向梯形求积。

普通段的两个含绝对值积分用真实总变差：

\[
\frac{d}{dx}\frac{w}{8\sqrt{1+w^2}}
=\frac{w_x}{8E^{3/2}},\qquad
\frac{d}{dx}\frac{-1}{8\sqrt{1+w^2}}
=\frac{ww_x}{8E^{3/2}}.
\tag{4}
\]

若区间上 \(z_x\) 符号确定，直接取真实端点原函数差。未定符号的盒递归细分；
剩余小盒使用非负 integrand 的整盒范围乘长度，所有这类盒的区间**逐项相加**。
`variation_tolerance` 只是每个未定临界小盒的停止阈值，不冒称全域误差等于这一数。
最终返回的区间已经包含全部小盒费用，不需要预先假设极值个数。

\(B,wB\) 使用原已付 C4 Simpson 余项。若 \(c_4\) 包围 Taylor 系数
\(f^{(4)}/4!\)，长度 \(h\) 的一盒余项不超过
\(h^5\sup|c_4|/120\)。同时交非负整盒范围，子盒误差预算二分。
soft cap 与两端分支 C4 匹配，因而跨 cap 阈值仍适用。
最外段与保护端 `(159,0)` 的实际平滑混合分别直接用四通道 Simpson；没有把后者误当成 \(\chi=1\)。

全部细分端点、长度和中点以 `Fraction` 处理，输入 float 指它的精确 binary 值，
输入字符串如 `"1/3"` 指该精确有理数。log/exp/sqrt 与导数计算进入独立 60 位区间上下文；
输出同时带精确有理端点及向外 binary64 显示端点。该对象不会修改其他审计的全局精度。
达到深度限制时抛错，不输出未经包含的“最佳估计”。

cut 处直接使用式 (2) 的解析身份 \(r=r_c\)、\(H_{\rm drop}=0\)；
保护端使用 \(r=r_{160}^o\) 和紧证书的四个全积分。此举保留同一真实定义的精确端点，
没有用极小区间中点移动 cut。接口目前暴露 \(0\le n<160\)，不伪称提供了未存逐 cell 校准根的无限深逐点查询；
其后的同源深尾仍由 R58 的独立界承担。

## 3. 真正的 C² 径向坐标及实际跳跃

式 (1) 保证 \(r_x>0\)。程序用

\[
r_x=(1-\chi)P+\chi Q,\quad
P=b_oj_0>0,\quad
Q=\frac{|w_x|}{8E^{3/2}}+\alpha_*\frac{b_oW}{E}>0
\]

的凸组合下界，避免在 \(\chi\in[0,1]\) 时丢掉 \(\chi+(1-\chi)=1\) 而得到假零下界。
因此物理半径 \(R=r(x)\) 是严格单调 C1 坐标。对真实 primitive
\(h_R=w\)，有

\[
h_{RR}=\frac{w_x}{r_x},\quad
g_{RR}=1+w^2,\quad g_{\theta\theta}=R^2,
\quad
\kappa_m=\frac{w_x}{r_xE^{3/2}},\quad
\kappa_\theta=\frac{w}{R\sqrt E}.
\tag{5}
\]

\(w,w_x,r_x\) 连续且 \(r_x>0\)，所以旋转图在物理 \(R\) 中为 C²，
包括所有 \(|w_x|\) 尖点。源 x 的二阶量只能作分段经典导数及双侧极限包围。
所有普通 cell/segment 接口处，\(S_5',S_5''\) 为零。令 \(d>0\) 是该侧的原始 log 半径导数，
\(b_{\rm join}=w_x/d\)。共同 raw/cap 端值及平坦插值保证 \(b_{\rm join}\) 两侧相同；
这里保留真实 soft-cap 导数，不能在被 cap 的接口直接写成 \(-7w\)。同一接口的正权 \(W_{\rm join}\) 也左右相同，故

\[
r_x=d\left\{\frac{|b_{\rm join}|}{8E^{3/2}}
       +\alpha_*\frac{r_oW_{\rm join}}{E}\right\}.
\]

因此 \(w_x/r_x\) 的两侧值相同，不需要假设源 x 的长度尺度一致。
首 cell 内部层接口的 \(W_{\rm join}\) 可以是 .5、3 或 .05，只有真正 cell ports 的权重为 1；
未 cap 的接口才有 \(b_{\rm join}=-7w\)。最外/最深特殊混合的一、二阶平坦性分别恢复原 cut/deep 两 jet。


本次还对当前真实背景证明了一个**实际非零跳跃**。在 `(cell0,segment1)`，从原临界点附近开始，
区间端点严格异号且整盒 \(z_{xx}>0\)；61 次有理二分得到唯一简单根，根盒宽
\[
1/11529215046068469760000000000<10^{-28}.
\]

根上 \(w_x=0\) 精确。令 \(C=w_{xx}/(8E^{3/2})>0\)，则
\(r_{xx}^{\pm}=\alpha_*B_x\pm C\)。真实双侧结果为

| 量 | 向外包围 |
|---|---|
| 根处 \(w\) | `[0.011254026986701002, 0.011254026986701004]` |
| \(r_x\) | `[0.0007016643401473256, 0.0007016643403021449]` |
| 左侧 \(r_{xx}\) | `[-0.0007384401021645676, -0.0007384401021645637]` |
| 右侧 \(r_{xx}\) | `[0.0007384751438342222, 0.0007384751438342263]` |
| 跳量 \([r_{xx}]\) | `[0.0014769152459987898, 0.0014769152459987900]` |
| 正向 primitive 图的 \([h_{xx}]\) | `[1.662124403554053e-5, 1.6621244035540533e-5]` |
| 两侧共同 \(h_{RR}\) | `0` 精确 |

这里 \(h_{xx}=w_xr_x+wr_{xx}\)，故最后的非零跳量是 \(w[r_{xx}]\)。
这不是有限差分或邻点采样，确实排除了“原 x 图全域 C²”的说法。

对一般非旋转分量 \(H(x)\)，

\[
H_{RR}=\frac{H_{xx}}{r_x^2}-\frac{H_xr_{xx}}{r_x^3}.
\tag{6}
\]

即使旧 \(H(x)\) 是全域 C² quintic，式 (6) 通常仍跳。
正确的双侧兼容是 \([H_{xx}]=H_x[r_{xx}]/r_x\)，而不是直接令 \([H_{xx}]=0\)。
后续尾图必须明确共享**物理 R 的 Cartesian/Fourier 两 jet**，再拉回原 x 定位；
当前旧 raw 与旧 x 插值没有因此取得 C² 认证。

## 4. 半径反解、符号与实际 native 参数化

`at_radius(n,j,Rlo,Rhi)` 先证明目标半径位于该段两端半径之间，再执行带正导数区间的 interval Newton／认证二分。
归一化区间或积分范围阻止继续收缩时，保留有效根盒并报告 `x_tolerance_met=false`，
不按中点选择符号，也不移动 \(\alpha_*\)。跨段或无法证明归属的目标会明确拒绝，调用者应拆分成相邻段或保留原 x 盒。

本次真实反解 `R="0.29998"` 位于 `(0,8)`，7 次收缩达到 x 盒宽 `<1e-10`；
得到

\[
h_R\in[0.08001561059516062,0.08001561059516275],
\quad h_{RR}\in[-0.314561012623279,-0.3145610124672103].
\]

高程符号约定必须保留：接口 `height_drop_to_cut` 是正的
\(\int_R^{r_c}w\)，`z_relative_to_cut` 是其负值，即 **正向 primitive**
\(h(R)-h(r_c)\)，其导数为式 (5) 的 \(+w\)。若上半曲面的 cut 向内高程增加，
应取 \(Z(R)=Z_c+\texttt{height_drop_to_cut}=Z_c-\texttt{z_relative_to_cut}\)，
全部竖直一、二 jet 统一反号。上表 primitive 的 x 二阶跳量也相应反号，绝对量不变。
接口不擅自选新的非旋转 mean 常数。

实际 M24 metadata 已只读核验：8 physical cells、9 pieces/cell、16 shooting parts，
共 1152 stages。stage 按外到内存储，内部原坐标仍
\[
x=a+(b-a)\xi,\qquad 0\le\xi\le1;
\quad r_\xi=(b-a)r_x,\quad r_{\xi\xi}^{\pm}=(b-a)^2r_{xx}^{\pm}.
\]

原 `states[k+1]` 是 stage k 的内端，`states[k]` 是外端，其 momentum 还带原 `portRatio` 约定。
当前已接受 `.25` warm checkpoint 仍只有 1153×48 两组模态数据；不是完整 full-H 联立终态。
原 source 的实际非零高度模态是
\[
H_j=r_J^4u_j,
\]
其中 \(r_J\) 是**该原 finite profile 的半径**。转换到真 \(R\) 共享图时，先明确保存哪一个实际
\(H_j,H_{j,R},H_{j,RR}\)；若需要新的归一状态再置 \(u_j^*=H_j/R^4\)。
直接保留 \(u_j\) 并用 \(R^4u_j\) 会无声改变物理场。
全部 Cartesian 模态、切向/径向两 jet 和同一个 mean primitive 都仍须按此新图定义，
不能只在非零高度模态做变换就声称已得到完整曲面。

`bind_native_metadata` 真正检查的是全部已序列化物理输入与每个 stage 的仿射坐标；
它明确返回 `field_transfer_certified=false`。metadata 没有单独序列化全套 runtime 校准根、
每次 JS 函数值与归一化，因此本接口不把这一输入检查冒充 finite-oracle 逐点误差证明。

## 5. 已执行的查询与可调用方法

六查询真实执行 exit 0，111.708 秒；另反解 exit 0，42.168 秒；根／跳量证明 exit 0，0.154 秒。
均为单核积分或只读计算，零个 BVP/shooting。

| 实际查询 | 真半径范围 | 高度 drop 范围 |
|---|---|---|
| cut `(0,8,1)` | `0.3` 精确 binary 输入 | `0` |
| 原 stage0 全区间 | `[0.29999835289025056,0.3]` | `[0,1.3177129726732838e-7]` |
| 首 valley `(0,4,1/2)` | `[0.2557157699521046,0.25571576995733797]` | `[0.001307511816125376,0.0013075118161882976]` |
| cell0 内端 | `[0.13552134105814048,0.13552134106992453]` | `[0.02185461364530009,0.021854613646014653]` |
| 原 stage1151 的 \(\xi\in[1/2,1]\) | `[0.05056136930126389,0.050561384382556286]` | `[0.022772024922056,0.02277202492305905]` |
| 修改背景最深端 `(159,0,0)` | 真实 \(r_{160}^o\) | `[0.0227720899833582,0.0227720900108743]` |

stage1151 此处是一个完整半区间；半径显示宽度主要是真实区间长度，不能解释成积分误差。
此外 cut 两 jet 精确保留
\(r_c=0.3,w_c=0.08,h_{RR}=-7w_c/r_c\)。

Python 可直接 import `Q060TrueBackgroundOracle`：

```python
o = Q060TrueBackgroundOracle(constants, normalization_certificate)
box = o.at_source(0, 4, "1/2", "501/1000")
native_box = o.at_stage(metadata["stages"][1151], "1/2", "1")
inverse = o.at_radius(0, 8, "0.29998", x_tolerance="1e-10")
print(o.json_value(box))
```

完整重现调用（`repo_dir`、`work_dir` 和恢复后的 `source_topic` 由使用者指定；输入常数与紧证书可以按已有同源命令再生）：

```bash
node "$repo_dir/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_collar_disk/dump_background_constants.mjs" \
  "$source_topic" "$work_dir/bootstrap/q060-port.json" "$work_dir/true-tail/constants.json"
OPENBLAS_NUM_THREADS=1 python "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/certify_q060_background_integrals_tight.py" \
  --input "$work_dir/true-tail/constants.json" \
  --out "$work_dir/true-tail/tight-integrals-certificate.json" --cells 32
OPENBLAS_NUM_THREADS=1 python "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/q060_true_background_oracle.py" \
  --constants "$work_dir/true-tail/constants.json" \
  --normalization-certificate "$work_dir/true-tail/tight-integrals-certificate.json" \
  --queries "$work_dir/true-tail/queries.json" \
  --metadata "$native_run/static-metadata.json.gz" \
  --out "$work_dir/true-tail/query-result.json"
OPENBLAS_NUM_THREADS=1 python "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/certify_q060_background_chart_jump.py" \
  --constants "$work_dir/true-tail/constants.json" \
  --normalization-certificate "$work_dir/true-tail/tight-integrals-certificate.json" \
  --out "$work_dir/true-tail/chart-jump.json"
```

首次导出常数前创建 `true-tail` 输出目录。`queries.json` 的六项和独立反解请求已完整保存在小实录中，
不依赖未公开的大数组。`--metadata` 对 source/radius 查询可省略，stage 查询才需要实际 metadata。
旧源恢复与 port 的生成入口沿用已公开 bootstrap；本接口没有读取断线旧 job 的未知终态，也未复制旧 closed-map 接受结论。

本次完成的是**指定真背景的可计算连续局部 oracle 与坐标正则性辨析**。
它为同一真实 \(g\) 的后续共享 R-C² 图提供 primitive 和背景两 jet。
原有限 JS oracle 到该真背景的全 IEEE/libm 误差、非旋转实际场的共享图转移、full-H 真 DN、
连续 metric/曲率及封口仍各按原门验收，没有被上述查询替代。
