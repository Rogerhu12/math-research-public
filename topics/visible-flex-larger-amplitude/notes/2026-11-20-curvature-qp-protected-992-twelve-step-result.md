# 保护曲率 basin 的 v4b：0.992 数值余量下十二步（2026-11-20）

维护会话：`/root/geometry_path`。

## 已执行结论

从真实 6077 父点连续执行 12 个方向、31 个真实回溯 trial，12 个方向均接受，正常结束。终态为

`2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453`。

同一正径向加权 Gram SSE 从 **0.3691614454297028** 降到 **0.28981377553494947**；最终固定网格、永久保护 basin、整方向锁定任意点和新增局部极值点的必要乘积为 **0.9918137496658477**，通过本次明确采用的 **0.992 算法筛选线**。最终复查没有重现 v4a 的已知 basin 被记忆淘汰问题。

但全观察点 max Gram 为 **0.04620001982850197**，略高于输入的 **0.04536288807497124**。所以本次只能声称加权平方误差下降，不能声称统一误差同步下降。实际峰已移至临近尾端的 cell 893，下面给出真实谱读出及据此进行的后继径向扩展。

0.992 是新的数值余量参数；原同一 $g$、原全部 Gram 方程、仿射端口、README 的 reach ≥ 0.03D 和连续完成标准均未改变。它小于真实必要阈值 1，但有限点通过仍不能证明 reach 成立。主会话对输入 6077 的独立连续位置/局部曲率界另行登记；本文件不把那些局部证据外推为终态的全域 reach 证书。

## 固定数学范围及新的点保留规则

沿用 v3 的 $w_s=\tfrac12w_s^{\rm Simpson}+\tfrac12w_s^{\rm Gauss}>0$、所有 7377 个径向观察位置、2048 个全圆角点及完整轨道重数。无新增 metric 行，无删行、改标量或改 mesh。物理空间仍为 12 个非零偶角模、原 11 个径向中心三 jet 的 **1280 维**粗空间；实际场仍含全部 160 个角模。

v4b 完整源来自冻结的 v4a，作了具体的有限记忆修正：

- 两个 cell 821 已知 basin 种子永久保留并优先局部极值搜索；
- 额外永久保留 prefix seed `(cell168,u0,phi .52349044)`；
- 每个方向的全部任意曲率约束点与半径点，在其整条 line search 中固定保留；
- 被拒 trial 可增加 bounded memory，但不能挤出本方向已使用的点；
- 每次真正接受单独保存完整 NPZ；最终再独立读取当前已知点。

每个可能接受的 trial 仍完整扫描全部 Gauss/旧点。四个局部曲率优化名额中，三个永久 basin 优先，剩余名额用于动态峰；另作一次真实半径局部优化。每个位置都读当前两条主曲率分支，旧数值和旧符号不沿用。局部优化只是实际点见证，不是全胞上界。

默认 bounded grid memory 32/4、arbitrary memory 12/2 保留。实际每个 QP 有 **1188–1342** 行。线性方向目标为 **.9918**，真接受目标为 **.992**；最大原尺度线性行残差在各次修复后均为负，最大者 **-1.8584763936124737e-10**。

## 十二步真实记录

| 步 | $\alpha$ | 加权 SSE | 全点 max Gram | 全部当前已知点乘积 |
|---:|---:|---:|---:|---:|
| 1 | 1/4 | .35376249806745763 | .045854577237769645 | .9898100406153665 |
| 2 | 1/2 | .3305731835751826 | .04650085792895098 | .9907488138459075 |
| 3 | 1/2 | .3149585116567602 | .04661616278723302 | .991290478183405 |
| 4 | 1/4 | .30899664220404716 | .04654772160192788 | .9914214430863435 |
| 5 | 1/16 | .3076500170753223 | .046521490462674286 | .9915613972415664 |
| 6 | 1/2 | .3043931319581598 | .04661560808802667 | .9916808015295648 |
| 7 | 1/2 | .3014783273071226 | .04662033968049362 | .9916870245436631 |
| 8 | 1/2 | .29882393911791355 | .046524634456057035 | .9917206763342516 |
| 9 | 1/2 | .2963469808707634 | .04647823170104659 | .9916784221275491 |
| 10 | 1/4 | .29518119424541306 | .04644215815681374 | .991956745039796 |
| 11 | 1 | .2907655942831723 | .04625773184041271 | .9918204397140786 |
| 12 | 1/8 | .28981377553494947 | .04620001982850197 | .9918137496658479 |

初始 $\mu=.04$。第 5 步仅接受 $1/16$，故提高到 .16；第 11 步满步且模型比良好才降到 .08；第 12 步仅接受 $1/8$，故提高到 .32。中等步保持。所有接受步的数据目标实际/预测下降比介于 **1.0002710976248144** 与 **1.0027221308161745**。

最终 all raw SSE **669.9280674677266**，legacy raw SSE **167.73502716911253**，加权 mean SSE **5.9676397014349255e-5**，最小相对点度量行列式 **0.9704250502608698**。共同高度 **1.9084457083780124 → 1.906762350783263**。

## 最终已知几何点的实际复查

最终全网格采样 $K_{\max}=8.077966296277545$、$D_{\rm lb}=4.09263745976333$，乘积 **0.9918056238855338**。独立 arbitrary-point 复查得到：

| 位置 | $u$ | $\phi$ | 当前最大绝对主曲率 |
|---|---:|---:|---:|
| prefix cell 168 | 0 | .49912870613999527 | 8.077878157648463 |
| cell 821 低角 basin | .641036014849691 | .016458100805728012 | 8.077912335939747 |
| cell 821 原正分支 basin | .31333140566080153 | .6705328014810272 | 8.07791307798505 |
| 当前动态峰 cell 879 | 0 | .5341213196286112 | 8.078022632498193 |

真正被读取的最远任意点在 cell 881、
$u=.23340933060030847$、$\phi=.4827103840979572$，给
$D_{\rm lb}=4.0926424480653765$。与当前最大已知曲率相乘得
**.9918137496658477**。这些点都是同一原场的六 jet 读出。

供后继重读的静态小 manifest 有 28 个任意曲率位置、4 个任意半径位置、57 个固定 grid 曲率位置和 8 个 grid 半径位置；它记录位置而不授权沿用旧数值。其 SHA 为
`f5b49e696048fb7ff6a29170e81f15aad416251df090bd9b201d501d4a8ecb7d`。
后继完整空间方向已可消费较早的实际第 1 步 checkpoint，不必等待该十二步结束。

## 真实残差谱与后继选择

复用已发布读者 `scripts/read_gauss_residual_spectrum_20261120.py`，
源 SHA `1705bee9921b429152943f78065bc24f2b541898de71b5230d5deaa85ed1300c`，
对该终态实际读取一次。Parseval SSE 与算子 SSE 的差为
**2.7755575615628914e-16**。三个 Frobenius 分量能量为
**(.11313218707049826, .04226074664375473, .13442084182069652)**。

90% 角能量在 mode 6 以内，99% 在 mode 15 以内，mode 12 以上仅 **3.350272800942986%**；mode 24 以上仅 **0.10505742101507322%**。因此本次证据不支持盲目扩大角频率。

原最严重的 $1.1\!\le s\!\le1.6$ 区域现在约占 21.94%；$s\ge1.6$ 约占 52.48%。全点峰在 **cell 893、stage 1787、$s=2.3112662789819365$、$\phi=\pi/2$**：
$$
(r_{ss},r_{s\phi},r_{\phi\phi})
=(.04620001982850197,0,-.0017890025633446882).
$$
它位于原最后一个粗中心之后、解析 lift 断点之前。相邻 cells 892、890、889 也占前几位；能量最大的 cells 878、877、893、879 位于尾部。

后继因此先保持相同加权目标和 12 角模，只在现有原 mesh 上增加六个有依据的径向中心：
**1.077134370991557、2.020292089293148、2.100560831276262、
2.2410311297467116、2.301232686234047、2.321299871729826**。
最后一个是原符号 lift 断点 node 894。11 中心扩为 17，粗维 1280 扩为 1964；原所有 nodal 自由变量及 mesh 均不变。扩大的是搜索子空间，不是采样方程或数学模型。下一六步已经按该选择启动，不将本次加权目标下降误称为统一误差已解决。

## 身份与完整复现命令

- 执行源 `scripts/resume_20261120_curvature_qp_v4b.py`：
  `f8dee5e090e9353b611598e42c135bd3855d856aafe6e2e80499478eec40933f`，35414 bytes。
- 输入 6077：
  `607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941`。
- 输出 2b143：
  `2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453`。
- 完整结果 JSON：
  `d70aa370ca42914499be85d145d0f18664fd6b47b077a55f76bcae97e99ff384`。
- 实际残差谱 JSON：
  `21f5ba294f3a0fe697fa741e98e4125e01084c6f9aff46e8e677ed01f44f250c`。
- wall time **308.8377655149998 s**，exit 0。

初末仿射三 jet 差均为零，冻结 core 字节不变。任意点粗基 complex-step 相对误差 **4.843068322456892e-15**，直径导数误差 **0**；加权基与真实算子目标差 **5.551115123125783e-16**。

输入 6077、两个 memory JSON 的完整公开取得方法见
[v4a def1六方向](2026-11-20-curvature-qp-arbitrary-def1-result.md)；
carrier、原场及 witness JSON 的完整生成命令见
[负界恢复记录](2026-11-20-curvature-qp-arbitrary-restore-result.md)。
所有源码依赖均在本仓库。使用 repo checkout、topic="$repo/topics/visible-flex-larger-amplitude" 与仓库外 work 目录：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v4b.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz" \
 --memory-input "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.memory.json" \
 --local-memory-input "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.local-memory.json" \
 --witness-input "$work/root/gauss-twelve-step-02-local-curvature.json" \
 --witness-input "$work/root/gauss-six-step-local-curvature.json" \
 --protected-point 168,0,.52349044 \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-protected-992-twelve-step.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 4 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .992 \
 --linear-margin .0002 --damping .04 --steps 12 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/read_gauss_residual_spectrum_20261120.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-protected-992-twelve-step.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --out "$work/geometry_path/curvature-qp-protected-992-twelve-step-spectrum.json" \
 --angles 2048 --legacy-fraction .5
~~~

**尚未完成**：统一误差仍远高于 $10^{-6}$；连续度量、全域嵌入/reach、握持振幅与全部相位仍需实际证明。

