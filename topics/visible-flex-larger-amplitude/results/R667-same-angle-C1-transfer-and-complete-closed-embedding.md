# R667：同角 C1 补界完成077087的闭嵌入

2026-11-20，Astra-larger-resume-24b2ab87-20261120；recover_evidence。

**状态：完整补充证明、799个未付胞的连续角覆盖、另50个弱粗界胞的预算精化及同一077087的非平面系数证明均已完成。** [R665](R665-continuous-C1-normal-cone-transfer-and-complete-immersion.md)已完成全闭面浸入但留下799个支撑未付胞；本条先只补这些胞，原已正123胞逐条复用。随后为明确的未来reach支撑预算，仅再补其中下界不足0.14的50胞。

完整922胞、全部角度、镜像半面及两帽合并得到

$$A_{1/4}F\cdot n\ge0.14208798>0.14,\qquad
|F_\phi\times F_s|\ge0.08558693>0,\qquad
\rho\ge0.16574514795>0.\tag{1}$$

因此077087准确闭C²球面映射是嵌入；R248的完整相位作用下，每个相位也为嵌入。加入本文明确选择的四个固定p4帽标记后，仍为强C²连续嵌入族，完整像幅度比大于0.22017，含反射的Euclidean商距离严格为正。本条尚不证明共同度量被准确实现，也不声称本077的完整曲率或reach已付；式(1)只支付reach所需的支撑组件。

## 1. 唯一实际场与被复用的证据

新场仍是 curvature-qp-spectral-hessian-four-step.npz，SHA256

077087b778921efd85e1b6bbe3b8389bd60f385e2de0e5a767b8f705bc847dc3。

基场仍为 [R663](R663-complete-closed-embedding-and-fixed-marker-noncongruence.md) 的0241，SHA256
0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023。
准确节点、S/R盒、binary自由系数、准确仿射T端口、完整解析lift及8阶Laurent余项都沿R665，没有改模型或重新拟合字段。

R665的完整输出 C1-077087-from-0241-full.json，SHA256
48a5b6de8e13a0fc032863f2acdd1a77b82e7e90f8090bb7d30c5a0655bcf568，
给出了已正123胞和未付799胞的完整划分。新源检查该报告绑定的基场、新场、旧第一jet证书均一致，保留其123个正结果，不把另一个场的正性混入。

未付胞为60–842及878–893。本次只为它们产生新的连续角信息。

## 2. 有限低模角盒，全部高模仍支付

原M=160的有限系数与R665的完整Taylor-Laurent工具不变。在每个准确径向piece及degree6控制点，将一个角分量写成

$$p(\phi)=p_{\le L}(\phi)+p_{>L}(\phi)+r(\phi),\qquad L=24.\tag{2}$$

其中 $p_{\le L}$ 包含常项及前24个偶角模，$p_{>L}$ 包含第25至160模；r是R665已付的160模外有限Laurent尾及完整实相位Taylor余项。于是逐控制点有

$$|p_{>L}(\phi)|\le\sum_{j>L}|p_j|.$$

给 $p_{\le L}$ 的准确有符号角盒两侧分别增加这个尾和r的准确上界，便包住原完整分量。实际实现从未把高模作为零；角低模只是计算区间的分组方式。

基场 $V_0,T_0$ 在该分组之前，已经把有限 q 部分与原 $f_s e_r$、$f\rho e_t$ 的低系数合并；Z部分也先合并 $\chi_sH_0$。差场 $\Delta V$ 先合并 $\Delta q_{s,Z}+\chi_s\Delta H$。因此保留R665需要的大项抵消。

本次核心完全相同，准确差场只改变0–12角模，但新代码并不以删去第13模以上原场为前提；全部原场高模和所有解析余项仍经过上面的包围。

## 3. 每个闭角段的严格低模区间

取Q=256，角中心 $\phi_j=2\pi j/Q$，半宽 $h=\pi/Q$。带宽 n=2L=48 的真实三角多项式 $p_{\le L}$ 在每个控制点使用R656/f512的严格有限三角变换，得到中心的 $p,p',p''$ 区间。

沿R656的有限带宽 Bernstein 导数界，设 $M_2=\|p''\|_\infty$，其最大绝对值点最近中心至多距h；在那里 $p'''=0$，所以

$$M_2\le\max_j|p''(\phi_j)|+\tfrac12n^2h^2M_2.$$

本次 $d=1-n^2h^2/2>0$，故

$$M_2\le{\max_j|p''(\phi_j)|\over d}.\tag{3}$$

在中心两侧的整个闭角段，Taylor公式给

$$p(\phi_j)-h|p'(\phi_j)|-\tfrac12h^2M_2
\le p_{\le L}(\phi)
\le p(\phi_j)+h|p'(\phi_j)|+\tfrac12h^2M_2.\tag{4}$$

把第2节的全部尾加入(4)，再对径向Bernstein控制点取上下包络，得到整个闭径向piece及当前闭角段上真实 $V_0,T_0,\Delta V,\Delta T$ 的三个分量区间。

π和三角变换来自R656已公开的Machin整数/Taylor向外构造，不使用普通FFT输出当证书。(3)的有限带宽只施加在明确保留的24模多项式上，不把完整analytic lift误说成带宽48。

## 4. 在同一个角盒中重建法线预算

在任一当前径向/角盒，直接从上节有符号区间得到

$$V_*\ge|V_0|,\quad T_*\ge|T_0|,\quad
d_V\ge|\Delta V|,\quad d_T\ge|\Delta T|.$$

同时用相同角盒的 $V_0,T_0$ 计算两种法线平方区间：

$$|T_0\times V_0|^2,\qquad |V_0|^2|T_0|^2-(V_0\cdot T_0)^2.$$

两者下界及旧基场全胞法线平方下界的最大值仍是真实下界。对其向下平方根得到当前 $w_0$。所有上界和分母都在同一角盒中，因此避免用rho较大处的 $T_*$ 配rho较小处的 $w_0$。

R665的法线差式与锥公式现在逐盒使用：

$$\eta_N=T_*d_V+V_*d_T+d_Vd_T,\qquad t={\eta_N\over w_0},$$

$$|N_1|\ge w_0-\eta_N,$$

$$A_\beta X_1\cdot n_1
\ge a_0\sqrt{1-t^2}-\sqrt{R_0^2-a_0^2}\,t-d_{\beta X},\quad t<1.\tag{5}$$

这里 $a_0,R_0$ 仍是合法旧全胞界，$d_{\beta X}$ 仍是R665全胞位置差界；无需为已经足够的这些量重算角分区。只有原失败的导数/法线角相关性被补入。

## 5. 全圆、镜像、帽与证据合并

原有限R/Z分量是偶角cos，T分量是偶角sin；完整delta是相同偶频率的sin，rho是cos。共同phi的两个场均有相同水平反射及半周对称。$|N|$、$|V|$、所有差范数与 $A_\beta X\cdot n$ 在这些作用下不变，因为 $A_\beta$ 与水平旋转/反射可交换，原参数方向使外法线按对应正交作用变换。

所以中心 $j=0,...,Q/4$ 的65个闭角盒连同这些对称覆盖完整圆周。没有借用R659单个固定见证的对称性；本条的量本身在所用反射下不变。

水平镜像将上半场的全部范数与支撑界等距传给下半场。两平帽独立使用准确 $\beta H_1>0$，Cartesian圆盘图正则；原两jet保证C²接合。

新全体报告逐一覆盖cell=0,...,921，其中123项直接取R665已付正结果，799项使用本条新角界。它们属于同一077087映射，每个原胞均有一份完整连续正性证据；证明的合并不要求每胞使用相同分辨率或相同估计方式。

## 6. 实际单胞与全部799胞返回

先对R665最坏胞833作一次必要补充读取。本次完整源、Q256/L24及K8给

$$t\le0.026681681773101606,\qquad
|N_1|\ge0.19424101890199397,$$

$$A_{1/4}X_1\cdot n_1\ge0.4832489298196652.$$

原粗式给该胞的 $t\le0.8884993$，因此这个改善来自同phi相关性，并非改变目标或删高模。单胞耗时0.574040362秒，exit0。

随后同源自然完成全部799个待补胞，实际59.869925401秒，exit0。没有重算已正123胞。新补的799胞共同支撑下界为

$$\sigma_{\rm new799}\ge0.3520579500410698.$$

连同复用123胞和两帽，完整共同结果为

| 全体量 | 向外结果 |
|---|---:|
| 正支撑 | 0.0013451648852334343 |
| 带面法线长度 | 0.08090829883612119 |
| 核心rho | 0.16574514795307824 |
| 两帽支撑 | 0.46956242842248536 |
| 未付胞 | 0 |

这个首次合并报告明确 complete_scope=true、all_covered_cells_paid=true、embedding_certified=true，同时 curvature_or_reach_certified=false、metric_certified=false。它已经完成正性，但其很小的支撑数尚不足后续reach预算。

为支付明确的 $\sigma\ge0.14$ 预算，使用相同冻结执行源、同Q256/L24/K8，另只补原123正胞中下界不足0.14的50胞。新50胞自然结束3.465859619秒，全部支撑至少0.38449521856147434；原799胞没有重跑。其准确胞集合为

$$\{32,\ldots,59,843,844,845,852,\ldots,859,876,877,894,\ldots,902\}.$$

每胞对两份已证下界取较大者仍是有效下界；未补的73胞保留旧结果。于是最终完整共同支撑为0.14208798386926672（最弱胞31），法线长度为0.0855869360569488（最弱胞903），给出(1)的短有理数。这次增加的结论是足够的支撑预算，不把重读原正性本身列成新发现。

## 7. 为什么正支撑给闭嵌入

R650的正定流投影结论在这里的输入已全部付清。简述其作用：对 $A_\beta$ 的线性流 $x(t)=e^{tA_\beta}x$，每条非零轨道与单位球面恰交一次。于是可沿轨道投影到单位球面，其微分核为 $\operatorname{span}(A_\beta x)$。

式(1)使真实闭浸入切平面处处不包含这个方向，且像避开原点。因此流投影与F的复合是从原紧连通球面到标准球面的局部微分同胚。它是覆盖映射，而目标球面单连通，所以是全局微分同胚。若F有两点同像，复合投影也有两点同像，矛盾；紧域上因此得到嵌入。

R248对完整未标记相位像给 $S_\alpha=R_\alpha S_0$，并且本条rho正保证原角图有效。旋转保持嵌入，且与 $A_\beta$ 可交换，所以全部相位的闭嵌入也已付。这里不从旋转像性质推导同一共同g的准确等距性；该问题仍由真正度量方程决定。

## 8. 同一077的非平面输入及四个明确固定标记

本次没有借用0241的非平面系数结论。以R661已刊完整Fraction源码对077作唯一一次新的全922胞读取，实际0.847618610秒自然结束，全部胞有非零轴迹及非零非恒定角高度多项式。共同轴端点准确下界和所选非零高度两jet的最小绝对值分别为

$$a_*={562178326815370681039402279\over1237940039285380274899124224}>0.4541,$$

$$z_*={1526595896721737\over72057594037927936}>0.0211.$$

断点仍为准确节点894；不是以浮点非零容差判断。R661的角解析延拓、半周对称及两轴迹证明遂给同一077活动像没有平面开片。有限接缝不含二维开集，镜像及可逆相位角图保持这个性质。

明确选择 [R661](R661-complete-nonplanar-activity-and-four-fixed-markers.md) 的四张固定图：上帽水平圆心 $(a,0),(0,a),(-a,0)$、下帽水平圆心 $(0,0)$，其中 $a=3/20$。半径依次为 $1/25,9/200,1/20,11/200$，高度全为 $h=1/1000$，在相应帽的外法向添加

$$u_i(x)=h\left(1-{|x-c_{i,xy}|^2\over b_i^2}\right)^4_+.$$

这些是完整准确多项式组件，无待拟合参数。四支撑盘互不相交，均位于水平半径1/5内，小于共同R；其边界具有零0/1/2 jet。帽图自身正则，并与原带面准确C²相接。077的准确高度为

$$H={4229442355341381\over2251799813685248}>1.$$

R661对任意H>1给这些帽图 $A_{1/4}$ 支撑至少 $64/267$、曲率绝对值至多5。与(1)组合，整个带标记闭球仍有统一支撑至少0.14208798。活动相位旋转不改这个界，四图逐材料点固定；因此第7节的流投影证明对全部相位仍给嵌入，原角图和接缝亦给强C²连续。

固定帽参考度量选择为这些图的共同诱导度量，活动部分保留原固定g；没有声称非零图仍保持旧平盘度量。固定握持区取上帽水平半径9/20以内的整个带标记图，其边界相反点间距离为0.9。

## 9. 同次位置差给严格整像幅度和Euclidean非全等

R665同一个077087全覆盖已付

$$d_H(S^{077}_0,S^{0241}_0)\le0.006085457.$$

两个场核心相同，R662的相位 $\pi/2$ 真实见证p完全相同，故见证位移eta=0。R662已证0241的整像见证距离至少0.914520539，因而

$$\operatorname{dist}(p,S^{077}_0)
\ge0.914520539-0.006085457=0.908435082.$$

与同一输入证书传得的077完整直径上界 $D\le4.123843488$ 配对，准确有理比较给

$$\delta_{{\rm hold},077}/D>0.22028>0.2.\tag{6}$$

这一步没有新增位置扫描，且全部量属于同一077场。第8节的外帽图到 $p_z=0$ 的竖直距离至少H，大于本条见证下界；D至多再加0.002。因此该明确标记族有

$$D_{\rm marked}\le4.125843488,\qquad
\delta_{\rm hold}/D_{\rm marked}>0.22017,\qquad
\operatorname{diam}(H_{\rm grip})/D_{\rm marked}>0.21813.\tag{7}$$

第8节的非平面活动性质及实际嵌入使R238的平面胚识别适用：平面胚补集由活动闭环带与四个闭图盘组成，后者的支撑圆半径互异，所以任何全等逐一固定四个圆心。这些三维圆心仿射独立，差向量行列式绝对值为 $4Ha^2>0$，故该全等只能是恒等，包含了反射情形。

式(7)的真实见证证明相位0与π/2的完整标记像不同，遂排除其Euclidean全等。若刚体作用能把两紧像的Hausdorff距离逼到0，则所用平移因两紧像有界而有界，O(3)本身紧；取子列得到一个真正全等，与前述结论矛盾。因此严格有 $\delta_E>0$，而不声称已经得到数值Euclidean商距离下界。

## 10. 完整源码、来源与复算

本条所列实际数值运行均在本地终端完成，没有GitHub Actions run编号；执行偏差及后续转公开Actions见[纠正记录](../notes/2026-11-20-public-actions-execution-correction.md)。来源不因证明发表而改写。

新小源 scripts/resume_20261120/fullclosed_C1_support_transfer_angles.py，11156字节，SHA256
2df727509871b604e8c359fb78484f88eb513372c8ca78eb7da8e9cd174b058b。

| 依赖/新报告 | SHA256 |
|---|---|
| R665原C1源 | ec21d8575ad2d121d04beaa2b7ebc1902c0b7604c0dfaf8777610ad27f616200 |
| R662原差界reader | f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0 |
| R656完整几何源 | 2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377 |
| 严格区间/三角核 | f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d |
| 同Hold准确节点报告 | fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692 |
| 旧0241完整第一jet证书 | 2bfe3a6e4371473e5b54e6b229a28facb2d9fba88e855d518287a5b780637125 |
| 新833角补界报告 | a9df760af482a12abaa744de5a44b3b0e6ddda70e49d73701e3e5ba91cdc8a84 |
| 新完整799补界合并报告 | 871484e7e64e2fb9e24c4d0796227f2c06f40969a7490aa418f096da15d54859 |
| 新50胞预算补界报告 | 611d1088c4a973ca4935b6c9becc4d26f43c039124155aaa80ae2588fc556738 |
| 077全非平面系数报告 | e3dbd25f0d0ca3ce9b1b2a2db563a74b3a6291f0fa0ef4b09cb0bbd7649ab2f6 |
| 已刊非平面完整Fraction源 | 43d1ac2351def55be984113726d5a22b9d483baa715fb4f5a653b2b83173f268 |

全部向外运算模型和准确字段身份沿R665。逐胞raw只留scratch；完整小源、全部参数和父链足以复算。令topic为本课题、work为仓库外重建目录：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python "$topic/scripts/resume_20261120/fullclosed_C1_support_transfer_angles.py" \
 --base "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --candidate "$work/geometry_path/curvature-qp-spectral-hessian-four-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --difference-source "$topic/scripts/resume_20261120/fullclosed_C0_difference_interval.py" \
 --transfer-source "$topic/scripts/resume_20261120/fullclosed_C1_support_transfer.py" \
 --base-certificate "$work/root/continuous-0241-complete-first-geometry-q2048-r1.json" \
 --prior-report "$work/recover_evidence/C1-077087-from-0241-full.json" \
 --out "$work/recover_evidence/C1-077087-from-0241-angle-complete.json" \
 --cells unpaid --angles 256 --low-modes 24 --taylor-degree 8
~~~

单胞833的命令只换cells与报告名。50胞预算补读保持相同源和所有参数，仅把out换为C1-077087-from-0241-angle-weak50.json，cells设为下面的完整列表：

~~~text
32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,843,844,845,852,853,854,855,856,857,858,859,876,877,894,895,896,897,898,899,900,901,902
~~~

两份报告的逐胞合并仅对下界取max、最后对全部胞取min，无需额外数值场计算。非平面新执行为：

~~~sh
python "$topic/scripts/resume_20261120/fullclosed_nonplanar_coefficients.py" \
 --bundle "$work/geometry_path/curvature-qp-spectral-hessian-four-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --out "$work/recover_evidence/nonplanar-077087-complete-coefficients.json"
~~~

这里新增的是旧报告所没有的局部同角相关信息、足够支撑预算及新077的非平面输入；没有重跑旧0241完整第一jet证书，也没有启动新的曲率或reach全扫。

公开源码路径均对应实际执行的同SHA字节；临时数组沿原输入链再生。纯位置输入若替代原诊断清单，计算语义保持，文件路径与输入清单SHA不冒称原raw报告逐字相同。
