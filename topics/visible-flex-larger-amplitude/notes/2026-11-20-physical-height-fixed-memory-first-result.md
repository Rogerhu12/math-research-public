# 永久记忆完整方向：13ce 的真实接受及扩展峰复核

状态：一次完整变量方向实际完成，保留全部当前记忆的线搜索接受，另作较新的静态位置清单与局部峰复核后仍通过数值余量 .992。尚未达到等距误差 1e−6，也没有连续全域曲率、reach、all-t 或其他课题完成证书。

## 1. 来源与字面预算

输入是 v4b 已刊实际接受 checkpoint，SHA256 `24de4d7ea9d94c66f1daa948c96b1a396369e450ea34688d72016f14be4dda5a`。执行 [完整准备与公共CLI](2026-11-20-physical-height-fixed-memory-preparation.md) §4 的完整 CLI，保留其全部源、同 g scalar carrier、原自由空间、积分端口与物理高度 map。运行 session=67573，自然结束 exit=0。

driver SHA256 `ae596f07e8808737e26f95ec67d79d81bf696af264b11fc791165abf05a8697b`，point-memory 源 `029f581c74082e36fd37663192a0bb42a20ef595c324c1d4e1e8f85e1657c26e`。初始记忆 57 κ +13 半径位置；64 强制/补充切向行，保留秩49；相对特征截断 1e−10，QR 正交误差 1.13e−14。新任意半径行的唯一复步检查误差 4.82e−15，已见准备条。

实际 μ=.0025、LSMR256、stop=7，完整方向总时 412.1692325010008 秒，准备及线性阶段 391.87669660699976 秒。端口误差 3.852305844112558e−18，归一选定活动行最大剩余 1.0610845260645078e−8。后者反映有限精度与数值秩截断，不冒充逐行精确零。

## 2. 同一目标上的实际试步

这里 weighted SSE 始终指相同 0.5 Simpson +0.5 Gauss 全正径向权与完整角轨道的 Frobenius 目标。所有旧 1845 径向行、5532 新 Gauss 行均在。保留 all raw / legacy raw 作为另外两项诊断。

| 状态/α | weighted SSE | all raw | legacy raw | 最大点 Gram | 实际 .03 D_lb K | 判定 |
|---|---:|---:|---:|---:|---:|---|
| 父 24de | .353762498067458 | 698.728195663276 | 174.876363321934 | .045854577237770 | .989810040615 | 初始扩展点筛通过 |
| 1 | .205048749050080 | 702.014746161250 | 175.488426313725 | .025206928344901 | 1.047700367037 | 拒绝 |
| 1/2 | .250628775081355 | 670.484790365220 | 167.673934336676 | .033872133693236 | 1.005263924915 | 拒绝 |
| 1/4 | .294942833768993 | 677.080336171129 | 169.384307431580 | .039817176839628 | .989821435548 | 接受 |

两次拒绝都来自实际新 prefix 峰：全步 s=.4、φ=.5460971604872883，K=8.530898853740148；半步 s=.3975、同 φ，K=8.187984084793918。旧 .52 左右的记忆不等于覆盖了这些角位置。程序当场把两个新位置追加，之后的 α=1/4 试步仍读取它们，没有淘汰原来任何 κ 或 radius 位置。三次试步的最远点也追加。结束记忆为59个 κ 位置、16个 radius 位置。

终态数组 `work/fullclosed_solver/gauss-physical-height-memory-first/final.npz` SHA256 `13ce4975470b0aca3717ce20402616688857f5fd3b844f83d1a4f338af418614`。完整方向 checkpoint SHA256 `08a5a33307080fdb79bacbc5e4f75c7cfc855b17e774f1204dedb943543e8c6e`。

终态 H=1.9047239100109745，weighted mean=6.0732536305587275e−5，min determinant=.9696582417743098，min E=.981481872685819，ρ 点最小=.16593115485590282、旧 Lipschitz 下读=.13815214948946042。最大点 Gram 在 s=2.3112662789819365、φ=π/2。L∞ 数值仍比所需 1e−6 大得多。

完整单位步的 δY/δU/δA 节点最大值为 .013427086820134958、.5132423244087436、32.76413258866586，δH=−.014034528045907687；实际接纳四分之一步。δA 包含物理高度方向的 −χ 补偿，不能把该节点坐标数值当物理曲率。

LSMR normr=.006449864862615571、normar=3.757742448136276e−5、normA=50.97152179673157、condA=19.804214789296847、normx=.19999486106177797。inner 达256上限，不是线性收敛证书。

## 3. 较新分支的位置也在13ce上重新读取

运行期间并行支线自然得到 2b143... 的新末态及不可变小清单 `curvature-qp-protected-992-final-witnesses.json`，SHA256 `f5b49e696048fb7ff6a29170e81f15aad416251df090bd9b201d501d4a8ecb7d`。它增加了包括 cell879 的位置；不能把其 κ 数值移到 13ce。

13ce 完成后，对该清单的28个任意 κ +4个任意 radius位置全部重新取实际六 jet。该清单的固定 grid 位置已属于本轮全 Gauss 真扫，不需再次扫整网格。随后从已知 basin 的明确种子作6次κ局部细化及1次半径细化，Nelder–Mead x/f tol=2e−10、maxiter=300，七次均 success=true。仍只登记实际点下界，不称局部或全局最大值。

| basin | 胞 | 局部细化后 u | φ | 13ce 的实际 K 或 D 点读 |
|---|---:|---:|---:|---:|
| 低 φ 负κ | 821 | .5623967900940712 | .01647442473047767 | K=8.063363121077368 |
| 正κ旧峰 | 821 | .11933136826617066 | .637359756535856 | K=7.922578279740278 |
| 正κ另一峰 | 821 | .30609099495509184 | .6706637320737123 | K=7.943004737697658 |
| prefix新峰 | 169 | 4.696403266279958e−13 | .5455195530767629 | K=8.017551386186287 |
| 后段新峰 | 879 | 0 | .5592634589171386 | K=7.917658717568544 |
| lift段峰 | 903 | .5849640708808106 | π/2 | K=8.005084934218393 |
| 半径峰 | 881 | .13902671036061404 | .49182653766192996 | D_lb=4.091847949611797 |

合并原全 Gauss、永久位置集合及上述新真点，必要点乘积为

$$
.03\,(4.091847949611797)(8.063363121077368)
=.9898216756186741<.992.
$$

因此当前已知点的扩展检查仍通过。这个标签不涵盖所有连续位置，更不推成 reach 下界。

## 4. 后验读的完整小源与命令

`read_known_geometric_basins_v2.py` SHA256 `03edefb832daefd5500099e33d30e0eb279ea2e6d22770b393200aa0eaaa5556`，只在已冻结字面 LocalField 上添加小位置清单的实际读出，未更改六 jet、标量或场。其完整报告 `work/fullclosed_solver/gauss-height-memory-known-basins.json` 为21,272 bytes，含所有实际读数、优化状态与输入/source SHA。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/read_known_geometric_basins_v2.py \
  --repo math-research-public \
  --bundle work/fullclosed_solver/gauss-physical-height-memory-first/final.npz \
  --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --local-reader math-research-public/topics/visible-flex-larger-amplitude/scripts/read_closed_local_extremum_20261120.py \
  --fixed-manifest math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-992-final-arbitrary-locations.json \
  --curvature-point 821,.562229728555,.016474359428 \
  --curvature-point 821,.11780409507141673,.6373598417541457 \
  --curvature-point 821,.30551485567674064,.6705379653782393 \
  --curvature-point 169,0,.5460971604872883 \
  --curvature-point 879,0,.534121319629 \
  --curvature-point 903,.582726039876,1.5707963267948966 \
  --radius-point 881,.308662314558,.474515173763 \
  --grid-curvature 8.0170467877243 --grid-diameter 4.091846962221483 \
  --reach-ratio .03 --safety .992 \
  --out work/fullclosed_solver/gauss-height-memory-known-basins.json
```

## 5. 与并行父的有限比较

同一 full Gauss 加权目标下，2b143... 的 weighted SSE=.289813775535 比13ce的 .294942833769略低；13ce最大点 Gram=.03981717684则低于2b143...的约 .04620002，且其已知点曲率乘积约 .98982低于约 .99181。两个指标不应混成一个“最优”标签。后继依据实际科学目的选父；全部原始场及来源均保留，不用状态报告取代真实候选数组。

## 6. 公共位置参数与原始输出保存范围

原后验报告SHA256 `03b9fb167f602aa3f2f02d4d2b45277706c8cd989543bfd6ae1c148c5a4a3bd8`。其原f5b输入含诊断输出，按根规矩不把整件raw入Git；公开纯参数文件保留本次实际读到的28κ+4半径位置及carrier身份，SHA256 `0fef52a47c57315ffb4d6e86caddf62c0380eebf0f69a3e7d9d7a3de2f44b116`。上面公共CLI消费这份完全相同的位置参数，重新读取的数学对象/位置不变，元数据路径与文件SHA自然不同。原grid位置在本次完整Gauss扫描内，未据此减少任何原方程。全部NPZ/方向/逐点报告仅scratch；完整源、数值预算和全部输入位置可重建。
