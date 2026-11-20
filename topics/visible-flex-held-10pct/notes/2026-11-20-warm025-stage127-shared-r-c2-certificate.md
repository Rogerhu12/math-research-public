# 已有 .25 warm 的 stage127：明确共享 R-C² 图与全域度量证书

维护会话：Astra-held10-1b6d88ec-20261120。日期：2026-11-20 UTC。

本条使用当前首 valley **4.625** 的 M24 新 profile 已接受 `.25` warm 检查点。
没有新的 shooting 或 BVP；它不是 full-H 响应，也没有宣布全尾完成。
结论是一个**实际有限参数定义的新曲面分量**：在原 stage127 所覆盖的 literal 物理半径区间，
共享 quintic 图处处 C²，并对同一 R58 真实背景证明

\[
\left\|g^{-1/2}(DF^TDF-g)g^{-1/2}\right\|_{\rm op}
<1.128\times10^{-9}<10^{-6},
\qquad |k_i(F)|<8.000976.
\tag{1}
\]

这些界覆盖 **17 个完整径向块、全部角度**。并非原 source 的有限 metric 数字、DFT 节点或径向采样的替代叫法。
该分量包含上一条真实背景 x 坐标二阶跳跃附近；物理 R 图仍为 C²。

源：

- `scripts/resume_n4/extract_q060_stage_from_native_record.py`：只读原 native 产物，核输入并恢复两类均值增量。
- `scripts/resume_n4/export_q060_saved_stage_r_jets.mjs`：只重评价一段既有初值的原有限 RK 流，导出明确字面参数。
- `scripts/resume_n4/certify_q060_stage127_r_quintic.py`：精确共同两 jet、连续 Gram 和曲率证书。

完整可再生数据留 scratch；同名 `-execution.json` 只保存来源、调用、哈希与小结论。

## 1. 实际来源和两类 mean 的恢复

检查点是
`m3-work/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz`，SHA
`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。
它的已有 `.25` 响应 `converged=true`，原残差 `1.8946163107633334e-10`，状态为 1153×48。
既有原生最终 fresh-J 调用为
`m3-work/newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json`。

只读提取器复用已发表的 `read_batch_output` 协议解析器，核 record 的 input/output/metadata/manifest SHA
及 payload token，再把**全部 1152 个 stage 的原生初始 48 分量**与已接受
`checkpoint.states[k+1]` 比较；最大差真正等于 **0**。
因此取回的两个附加 mean 槽来自该真实已接受检查点的既有流，不是另一个 warm 比例或猜测补值。

原 stage k 的内端是 `states[k+1]`；输出 momentum 在外端要按原 `portRatio` 转回 `states[k]`。
原生输出槽 `2M` 是非旋转扰动 mean 的本段增量，槽 `2M+1` 是旋转背景 primitive 的增量。
从最深有限端按原从内到外的顺序累加，在 stage127 内端得到

\[
(m_{\rm pert},m_{\rm bg})=
(-2.692206334612768\times10^{-10},\ 0.0009253164581766512).
\]

两槽分别保存。新图的高度扰动只使用第一槽；真实背景 primitive 另由 R58 定义。
**不把总 mean 再加入一次背景。** 原数据仍只是一个数值 primitive；本文把所选公共节点数据明确作为新有限图的参数，
没有把它称为无限维 PDE 的真 primitive。

## 2. 断点、两 jet 和新图的精确定义

stage127 是 `(cell0, segment1, raw x∈[0,1/16])`。原 native RK 网格含 17 个步长和 18 个节点，
包括原 cusp 分割点。它的局部坐标保持 \(x=\xi/16\)；这个 x 只用于追溯数据来源。

每个断点取原 source 在该节点评价得到的 **binary64 `radiusJS` 对应的精确有理数**。
这些数现在是声明过的 literal 新 R 网格，**不是** 真 \(R(x_i)\) 的区间中点，也未假称两者相等。
真实目标 \(g\) 不随这个有限场网格改变。

使用原 `relativeActualDevelopment` 的 Cartesian 发展，包括其 Darboux 缺陷 \(\Omega\) 的角 primitive 校正。
高度一、二 jet 来自原 `createMomentumPhysicalJetEvaluator` 的隐式 root 微分；
平面 rr 参数来自原 `createRelativeSpatialJetEvaluator` 的四阶有限差分，步长为原 \(\xi\) 中 `5e-5`。
这些 rr **只作为新图有限参数的选择**，不声称已经证明它们是某个精确 PDE 图的真实位置二导数。
在 cusp 节点将该步长加倍时，平面 rr Fourier 系数最大变化为
`2.443485540154726e-14`，仅作为数据稳定性诊断记录。

节点的实际非零高度系数先按原值
\[
H_j=r_J^4u_j
\]
计算。没有把同一 \(u_j\) 直接乘真 \(R^4\) 来暗改高度。
原 stage 外端的状态和两 mean 增量取已有 native/cp 的公共值；内部点只重评价原已有初值的 RK 流，
不运行 Newton、全尾射击或新边界搜索。

取 `planarModes` 中 128 个 \(m\equiv1\pmod3, |m|\le192\) 的实系数，
高度模态为 \(0,3,\ldots,72\)。令

\[
V_x+iV_y=\sum_m a_m(R)e^{im\theta},\qquad
V_z=\sum_j h_j(R)\cos(j\theta).
\tag{2}
\]

在每个相邻 literal 断点间，\(a_m,h_j\) 取唯一 quintic Hermite 多项式，匹配两端同一份字面
\((v,v_R,v_{RR})\)。全部输入 binary64 都作为精确实有理数；跨度是断点的**精确差**。
相邻多项式共用节点两 jet，故式 (2) 在物理 R、全部角度中严格 C²。
实际执行用 `Fraction` 验证了 15606 条端点标量等式，包含 0/1/2 阶，不以浮点“小跳量”冒充一致。

背景取同一真实 R58 图
\[
X_0=(R\cos\theta,R\sin\theta,h_*(R)),\qquad h_*'=w_*,
\quad F=X_0+V.
\]

可整体加原装配所需的一个共同竖直常数；式 (1) 不依赖它。
上半曲面若用反向高程，则整个竖直背景和扰动一起反号，度量与绝对曲率界不变。
这里没有完成相邻所有 stage、prefix 或 cut 的 Cartesian seam，只完成这一实际分量内部的 C² 定义。

## 3. 同一真 g 的 R 域覆盖

真实背景仍使用唯一归一化
\(\alpha_*=(r_c-r_{160}^o-\int A)/\int B\)，固定 160 个已保存的 binary 校准根。
程序调用前一条 `q060_true_background_oracle.py`，从 `(0,1,0)` 的真半径锚出发：
左侧覆盖相邻 `(0,0)` 的最后 \(10^{-6}\) 原 x 小段，右侧覆盖 `(0,1)` 至 \(1/16+10^{-6}\)。
真实部分积分的区间严格证明该相连区间的半径两端包住全部 literal R 断点。

因此不需要假设原 JS 半径误差为零；该 finite 网格确实落在同一真背景的已认证坐标范围内。
整个 R 分量的真实坡度被包在

\[
0.01112281824804677\le w_*(R)\le0.011514288681339363.
\tag{3}
\]

证明中选一个字面有理辅助常数 \(w_0\)，记
\(w_*(R)=w_0+e(R)\)、\(|e|\le\Delta_w\)，两者均明确保存在证书。
这是精确误差分解；没有把 \(w_0\) 换成新的背景坡度或中点归一化。
R58 的 \(w\le41/100\)、\(|k_i(X_0)|\le8\) 也只在该真实 4.625 背景合同下使用。

## 4. 相消后的全角、连续径向 Gram 证明

设 \(e_r=(\cos\theta,\sin\theta)\)、\(e_\theta=(-\sin\theta,\cos\theta)\)，
\(E=1+w_*^2\)。真实归一化误差矩阵是

\[
\begin{aligned}
A_g&=\frac{2(e_r\cdot V_{R,xy}+w_*V_{R,z})+|V_R|^2}{E},\\
B_g&=\frac{e_r\cdot V_{\theta,xy}+R e_\theta\cdot V_{R,xy}
                 +w_*V_{\theta,z}+V_R\cdot V_\theta}{R\sqrt E},\\
C_g&=\frac{2R e_\theta\cdot V_{\theta,xy}+|V_\theta|^2}{R^2}.
\end{aligned}
\tag{4}
\]

背景的 \(E,R^2\) 在这个恒等式中已经严格相消，不把两个接近 1 的区间平方硬相减。
式 (4) 对所定义的有限 \(F\) 恒成立，不假设它先满足等距方程。

把式 (2) 代入，先在相同 Fourier 频率精确合并线性项：

\[
\begin{aligned}
L_A&=2\sum_m a_m'\cos((m-1)\theta)+2w_0\sum_j h_j'\cos(j\theta),\\
L_B&=\sum_m(Ra_m'-ma_m)\sin((m-1)\theta)
       -w_0\sum_j jh_j\sin(j\theta),\\
L_C&=2R\sum_m ma_m\cos((m-1)\theta).
\end{aligned}
\tag{5}
\]

所有径向系数是精确有理多项式。负频率按 cos 偶、sin 奇合并，保留高度与平面项的实际相消。
每一频率的多项式转为 Bernstein 系数，以系数凸包取得整块绝对上界，然后求 Fourier l1。
这一步覆盖所有 \(R\) 和 \(\theta\)，不使用角度或径向网格最大值。

记全角、整块的 \(|V_R|\le u\)、\(|V_\theta|\le v\)、
\(|V_{R,z}|\le u_z\)、\(|V_{\theta,z}|\le v_z\)，本块最小半径为 \(R_0\)。令
\(\eta^2=u^2+(v/R_0)^2\)。由 \(E\ge1\)，

\[
\begin{aligned}
|A_g|&\le \|L_A\|+2\Delta_wu_z+u^2=:a,\\
|B_g|&\le (\|L_B\|+\Delta_wv_z)/R_0+\eta^2/2=:b,\\
|C_g|&\le (\|L_C\|+v^2)/R_0^2=:c.
\end{aligned}
\]

二次混合项使用 \(uv/R_0\le\eta^2/2\)，故对称矩阵的算子范数不超过
\(\max(a,c)+b\)。全 17 块的最大值为式 (1) 的 `1.1276927598946533e-9`。
仅使用粗近等距梯度界 \(2\eta+\eta^2\) 会得到约 `4.051e-6`，不能过门；
本条实际支付的是式 (5) 的相消，未把该粗界改名成接受。

## 5. 连续二 jet 与曲率

真实参考正交标架下，扰动的协变 Hessian 是

\[
\begin{aligned}
H_{11}&=V_{RR}/E-(ww_R/E^2)V_R,\\
H_{12}&=(V_{R\theta}-V_\theta/R)/(R\sqrt E),\\
H_{22}&=V_{\theta\theta}/R^2+V_R/(RE).
\end{aligned}
\]

由于 \(|w_R|/E^{3/2}\le8\)、\(w\le41/100\)，
\(|ww_R|/E^2\le82/25\)。所有 \(V\) 的一、二偏导仍以同一 quintic 的精确 Bernstein/Fourier l1 包围。
得到

\[
\|V\|<6.08195\times10^{-8},\quad
\eta<2.025219\times10^{-6},\quad
\beta:=\sqrt{\|H_{11}\|^2+2\|H_{12}\|^2+\|H_{22}\|^2}
<0.000942602.
\]

\(\eta<1\) 保证浸入，实际第一基本形式不小于 \((1-\eta)^2g\)。
参考图的协变 Hessian 在其法向上，单位参考方向的绝对二基本形式不超过 8。
对新图任意单位法向作内积也不增加此界，所以

\[
|k_i(F)|\le\frac{8+\beta}{(1-\eta)^2}<8.000976.
\]

这里只需要真实背景和新图 C²，没有使用源 x 的不存在的经典二导，也没有使用跨节点三阶光滑性。

在 17 个保存的原 RK 中点半径，程序还用精确有理代入比较新图与所保存的**有限字面 Fourier 参考**。
全部角度的 0/1/2 阶 l1 差分别不超过

\[
1.386912\times10^{-20},\quad
1.189013\times10^{-14},\quad
5.854190\times10^{-10}.
\]

这个比较只覆盖这 17 个径向平面，参考也是有限数据；它不取代式 (1) 的连续证书，
也不把 FD 二阶升级成原 PDE 的连续位置导数。

## 6. 实际执行和后续拼接合同

三步均真正 exit 0。只读绑定后，局部原流/数据导出 8.206 秒，连续证明 68.838 秒。
可搬迁调用如下，`repo_dir` 与 `work_dir` 为实际仓库和运行根：

```bash
OPENBLAS_NUM_THREADS=1 python "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/extract_q060_stage_from_native_record.py" \
  --checkpoint "$work_dir/m3-work/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz" \
  --native-record "$work_dir/m3-work/newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json" \
  --stage 127 --out "$work_dir/n4-work/q060-tail-geometry/stage127-saved-native-input.json"
OPENBLAS_NUM_THREADS=1 node "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/export_q060_saved_stage_r_jets.mjs" \
  --input "$work_dir/n4-work/q060-tail-geometry/stage127-saved-native-input.json" \
  --out "$work_dir/n4-work/q060-tail-geometry/stage127-literal-r-data.json"
OPENBLAS_NUM_THREADS=1 python "$repo_dir/topics/visible-flex-held-10pct/scripts/resume_n4/certify_q060_stage127_r_quintic.py" \
  --data "$work_dir/n4-work/q060-tail-geometry/stage127-literal-r-data.json" \
  --constants "$work_dir/n4-work/q060-tail-geometry/constants.json" \
  --normalization-certificate "$work_dir/n4-work/q060-tail-geometry/tight-integrals-certificate.json" \
  --out "$work_dir/n4-work/q060-tail-geometry/stage127-true-background-quintic-certificate.json"
```

提取器的旧 metadata/manifest 仍带原运行路径；搬迁时先按原来源恢复并使 record 中路径正确，
保持文件 SHA 和状态绑定，不伪造一份新计算记录。没有现存 native call9 的完整真实输出时，
不能把未知全尾 mean 增量假填成零。

本条已足以冻结该实际局部分量。批量全尾需要在每个相邻 stage 真正选择一份公共 Cartesian 两 jet：
内部 node k 采用外侧 stage `k-1` 的内端数据，内侧 stage k 的外端共用它；
两个 mean 仍从相同 native 增量统一累计。最深端应共用另行已付圆领的唯一节点，cut 则与真 cut 合同明确匹配。
两份浮点端点“很近”不能代替该共同定义。本条没有把这个尚待全尾执行的规则算成已完成的全尾拼接。
