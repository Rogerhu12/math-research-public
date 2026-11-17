# smallcut q18 的真实非线性尾：首批延拓与定位

会话：Astra-held10-new-construction-20261117。仅有限 Fourier、有限非线性深度的实际 Darboux/momentum 方程计算；没有完成闭曲面，没有把线性 T 门当作非线性上限。

## 输入和规范

运行时生成的输入 `SCRATCH/q18-H.json`（本次SHA为 `73a83713ec4b64df8e26c9fd3889bda4a28513069accb0b7b21b0b0f880c0b55`，不提交数组）来自已冻结 smallcut 前缀 q=.180001320757266、cut r=.3，w=.08，w_r=−1.866666666666673，完整材料角 u 的 20 个 cos(2ju) 高度系数。H1=.0021936155625693187。它不是空间极角 atan2(Xy,Xx)。实际 upper 前缀的平均 z_r<0；原尾 worker 使用 orientation=+1、平均 z_r>0。因此实际 upper 对接方向为输入 **−λH**，最后反射整个 z（包括非线性均值）再平移。正 λH 只作控制支路。

原固定物理尾参数为 `smallcut_original_m8_config.json`。参数文件以7个非零物理控制和 `valleyControlsPadTo=160` 保存；入口精确补零后才传给原worker。这只改变配置的磁盘表示。真正物理构造深度 protectCell=160；有限非线性深度8、far线性48；M8、角求积128、每profile数值分片2、每片RK32。M8省略的H系数l1为2.0011196298596636e−8，仍是待精化误差。所有原始 D/S/A guards 保留，初始实验显式 floor=.01，不是源码默认.1。完整零模、非线性角根、非线性流和实际周期展开度量均保留。

## 实际接受点

表内 metric 是原取消相消 R16 实际 Cartesian 展开的一阶度量诊断；Kformal 是实际有限高度方程二 jet 推出的形算子诊断。它不能代替全部连续二 jet 或无限尾证书。

| 真实输入 | M / N | floor | root 残差 | min A | min D | metric | Kformal |
|---|---:|---:|---:|---:|---:|---:|---:|
| −.04 H | 8 / 128 | .01 | 9.64e−10 | .56205 | .999734 | 7.29e−10 | 8.00186 |
| −.06 H | 8 / 128 | .01 | 1.44e−10 | .32198 | .999600 | 6.27e−9 | 8.01890 |
| −.07 H | 8 / 128 | .01 | 2.27e−9 | .20127 | .999533 | 2.63e−8 | 8.02955 |
| −.07 H | 12 / 256 | .01 | 1.13e−9 | .20220 | .999532 | 4.73e−9 | 8.02949 |
| −.078 H | 8 / 128 | .01 | 5.09e−9 | .01540 | .999479 | 7.13e−8 | 8.03975 |
| −.0781 H | 8 / 128 | 1e−4 | 3.05e−9 | .0026304 | .999478 | 7.27e−8 | 8.03994 |

最初在 .04→.06 的冷/普通 warm 跳步发生 momentum Newton line-search failure；原 78718 full-shooting tangent warm 后实际接受了 .06，因此该初次失败不是容量上限。后来的 .0625 也一度停在1.27e−9的浮点残差（阈值1e−9）；明确换探索容差1e−8后重新求解实际残差5.37e−11。没有删 guards 以把失败改称通过。

从 .0781 向 .0782 的正A分支尝试在初始 root line search 失败，未保存负A/D/S解，不能据此宣布不可延拓或非存在。后续M12/M16固定g检查另记，不混入本条已完成表格。

## A 谷的实际几何诊断

`analyze_root_minimum.mjs` 对 −.0781H 的有限流按每片32步寻找最小A点，并调用原完整物理二 jet、R16 Cartesian二jet和有限根Gram。结果：raw cell0/segment4、r=.2526298661353142、w=.0035806129653297588、w_r=−.001027491992155442、u=0。

该点 g 的 K_g=−1.4562636121769528e−5，反射轴强制混合项 b=0。有限高度得到

- a=−.01835589118470677，b=0，c=.00003728126086255193；
- a c−b²−K_g=1.3878305354147858e−5；
- 实际Cartesian曲率=.01835589112345119，实际度量误差3.889910973565384e−9；
- 有限Gram特征值范围[.06859234157476951,1.4207516209961266]。

这说明这里的小metric不能被误读成C2 Gauss相容性已收敛：几乎整个K_g仍由有限投影缺陷承担。在精确同g、同反射轴条件下，若c→0且K_g固定负，a=K_g/c必发散。低M有限解在此处看似平滑，不能代替精确C2穿零论证。

另有独立的有限图代数说明（见本文末节）：对固定M与固定求积，在D,S>0且完整Gram正定时，finite momentum确实可定义更大的图，但这不保证谱极限。原guard版本仍原样保留，本条未把该代数条件冒充新通过解。

## 较宽有限首脉冲的实际试验

直接改变全尾的首脉冲/全局warp α时，β控制沿用导致原cell7的线性初猜放大：λ=1e−7时，在r=.050468044,w≈6.465e−13，首模目标L已到2.585。故极小幅初始guard失败是这一新初猜/背景调谐问题，没有得出宽尾不存在。

为隔离该问题，`hybrid_outer_factory.mjs` 将所有 n≥1 原物理cell逐对象保留，只改变第0cell。新径向速度写为正A(x)+αB(x)，其两端以S5恢复原速度，α由原第0cell宽度.1644886093636216唯一确定。端口 r,w,w_r 均核至0或5.6e−17。新旧两端具有同样实际二jet，但**新的DN不等于原DN**；所有此类结果都未匹配回前缀。

有限实际试验：

- peak .8、外峰.02、valley cap .1、β4.25：尾背景高度.06396145；真实−.001H接受，metric2.31e−11，但Kformal12.03，−.003H初猜失败。
- peak .8、外峰.1、valley cap .4、β8：背景高度.06494294；−.0001H接受，minA .87516；−.001H初猜失败。它的新首模D≈−185.04，处于不利的响应位置；没有把它当成原匹配尾。
- 同上β12：−.0003H接受、minA .75299，−.001H初猜失败。

这些是几种已实际解过非线性方程的有限设计失败/受限记录，不是线性LP上界，也不排除重新调谐的宽脉冲、有限阻尼段或别的非线性支路。

## 两侧Cartesian seam

`export_tail_cut.mjs` 从完整有限状态重建实际尾cut的 X,Xr,Xu,Xrr,Xru,Xuu；`audit_tail_cut.py` 使用原前缀实际两jet，以r_s=−1/√E、r_ss=−w w_r/E²换元。只做反射整个z、绕轴刚转和平移，不把材料角换成空间极角。−.04H与完整q18前缀当然不匹配，实测六jet最大范数依次为.00222385、.03120555、.00410978、.16402473、.05047874、.01107248。它证明实现已能检查真实接头，并不声称缩小幅度的尾接上完整前缀。

平面rr目前采用原四阶局部profile差分；还需步长检查和连续表示。只有 λ=1、完整20模及相应新DN回馈前缀后，才可能谈本题实际接头。

## 可复现源与命令

`nonlinear_tail_recovery_manifest.json` 的39个不可变小源文件均已逐字与46fe93d4bb708fdfb7935e91b8141ea77586f0d2核对，共240707字节。用现有 `recover_prefix.py` 恢复到仓库外scratch，再运行本批入口即可。原源码、source-cache blob验证、guards和接受标准没有修改。`continue_tail.py` 仅把client要调用的worker路径显式选择，并令source hash仍从原client目录读取；实际worker SHA另记。

先按已发表 `smallcut_delivery_manifest.json` 再生固定q18 M20检查点，并保留其恢复源目录 `PREFIX_SOURCE`。完整高度端口由下列入口生成（`smallcut_endpoint.py`另管Cartesian两jet）：

```sh
python scripts/nonlinear_tail/extract_H.py SCRATCH/fixed-r30-p20-q18-m20/fixed.json.gz \
  --source-topic PREFIX_SOURCE/bundle/topics/visible-flexible-closed-surface \
  --output SCRATCH/q18-H.json
```

下面命令以本目录脚本所在位置为工作目录；`recover_prefix.py` 使用父目录已有入口，`REPO` 为仓库，输出目录均在仓库外。不同恢复清单用不同 scratch 目录，避免把前缀源与尾源的版本默默覆盖。

```sh
python ../recover_prefix.py --repo REPO --dest SCRATCH --manifest nonlinear_tail_recovery_manifest.json
OPENBLAS_NUM_THREADS=1 python continue_tail.py \
  --source-topic SCRATCH/bundle/topics/visible-flexible-closed-surface \
  --config smallcut_original_m8_config.json --height-trace SCRATCH/q18-H.json \
  --out SCRATCH/negative-first \
  --lambdas=-.0001,-.0003,-.001,-.003,-.01,-.02,-.04 \
  --audit --stop-on-failure
```

后续把新配置的 `initialCheckpoint` 指向该 `response_0007.json.gz`，选择 `--worker 78718-prefix-tail-tangent-fourier-worker.mjs`；先 `.045,.05,.055,.06`（均取负号），再以solveTolerance=1e−8细步到.078。floor1e−4实验从已接受.078另起新输出目录；不能复用旧试验目录写覆盖。M12输入保持物理参数并改modes=12/quadrature=256、同一−.07H重解。

所有小参数、已完成批次摘要和响应SHA在 `nonlinear_tail_stage1_summary.json`。巨大轨迹和响应数组仅留scratch；没有纳入本条交付。响应hash是本次出处标识，跨平台重跑应比对数值结果与误差，不要求含绝对路径的gzip逐字一致。

## 附：有限投影 momentum 图在 A=0 处的条件代数

本条只证明固定 Fourier 模数、固定角求积的有限方程可在哪个开集上定义。它不证明穿过 A=0 的无限维 Darboux 解，也不把有限根变成精确等距闭曲面。原正 A worker 保留，任何新实验必须另名并记录新的有限图。

设 z=w²>0, E=1+z，P 与 Pθ 由固定有限 Q 向量给出，记 T=Pθ、K=L−T、Y=1+K。

\[
 U=2K+K^2+EP^2,\quad D=1-zU,\quad S=1-zP^2,
 \quad A=1+K+ET.
\]

在每个求积点 D,S>0 时，定义真实角连接的归一化密度

\[
 B(L,Q)=\frac{U}{\sqrt D(1+\sqrt D)}+
 \frac{(1+K)T}{S\sqrt D}.
\]

原 `general_root_tail_momentum.mjs` 的 `moments=L+quad` 是此式的字面有限 Fourier 投影。验证只需两个代数恒等式：它的 `fc` 满足 `1/2+fc=1/(sqrt(D)*(1+sqrt(D)))`，`gc` 满足 `1+gc=1/(S*sqrt(D))`。所以没有改掉任何均值或非线性乘积。

因 `D+z(1+K)²=E S`，第一项也等于 `(D^(−1/2)−1)/z`。对L求导给 `(1+K)/D^(3/2)`；第二项导数为 `T[D+z(1+K)²]/[S D^(3/2)]=ET/D^(3/2)`。故对 L 保持 Q（因此 P,T）不动，有

\[
 \partial_LB=\frac{A}{D^{3/2}}.
\]

令 φ₀=1、φⱼ=√2 cos(mⱼu)，Q_N 为实际离散角平均，并取 N>2 max mⱼ 以确保表示基的离散正交性；本批M/N均满足。选择这些归一化系数坐标。有限矩映射的 Jacobian 正是

\[
 G_{ij}=Q_N\!\left(\frac{A}{D^{3/2}}\phi_i\phi_j\right).
\]

原源码利用离散正交性写成 `I+Q_N(bm φ_i φ_j)`，两式相同；非线性乘积的 alias 仍按实际求积保留。若 G 正定，则原 Cholesky 求解仍合法；即使个别求积点 A=0 或 A<0，G 也可能保持正定。严格正定和 D,S 严格正均为有限维开条件。隐函数定理因而给出完整均值在内的局部唯一光滑 L=L(Q,π,r,w)。不需要逐点 A>0 来调用这个有限维定理。

原有限 momentum 的 Q/π 右端只有 S、sqrt(D) 和固定正几何量作为分母；点态流量为 `(1+K)Uang/(S*sqrt(D))`，其中 `Uang=−∂uL+...`。它没有除 A。隐式根求导与物理二 jet 仅再求解 G。因此在该开集上，整个有限 ODE 及有限物理二 jet 都延拓为光滑函数。

新的有限图若采用这一结论，必须同时保留：

1. 每个求积点 D>0、S>0；
2. 完整 G 正定（Cholesky 成功并记录最小谱值/条件数）；
3. 原有限矩残差、完整零模、全非线性右端不变；
4. 求积/谱加密、真实 Cartesian 两 jet 与几何误差独立检查。

它只是比逐点 A>0 更大的有限图。不能从某一个 M 的 G 正定推到任意大 M：若连续 A 在一段角区间为负，局部化试验函数会令无限维乘法二次型不正。这正是后续谱加密必须揭示的限制。若 G 失去正定但仍可逆，原 Cholesky 算法已不适用，另换不定线性代数也不能当成本条已完成。

几何上，在取 n_z=√(D/E) 的高度图中，正交基下周向第二基本形式系数为

\[
 c=\frac{wA}{r\sqrt E\sqrt D},
 \qquad b=\frac{wUang}{r\sqrt D}.
\]

因此 A=0 本身不使第一基本形式退化。在精确 Gauss 方程成立时，若该点 K_g<0 且 b²=−K_g，仍可有有限 a 和 c=0。有限投影场未必精确满足该相容条件，必须实际报告 a c−b²−K_g，而不能用它省略验证。
