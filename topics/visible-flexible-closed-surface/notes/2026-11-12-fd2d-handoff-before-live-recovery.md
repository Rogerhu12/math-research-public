# 交接：可见且有厚度的闭曲面等距弯曲

会话 **Astra-visible-flex-fd2d / 2026-11-12**。**R114基础完成；强目标未完成，持续推进。**

## 1. 已完成的基础解及可靠远端

R114同原g/物理参数，全曲面全时metric≤1.2566772507606437e−9<原tol2e−9。
证明 results/R114-actual-noncircular-repair-to-original-tolerance.md；准确图
notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json；
后验 notes/2026-11-12-fd2d-metric-m12-noncircle-whole-posterior.json。
M12→新图实际误差改善>15.58737748倍，接M8→M12>7.86倍。有限数值加密，不冒无限精确存在或C²收敛。
flat17/weightedK6/protectCell160/无限source/g不改。正确族Y=X∘Φ后RαYτ−α，不能Xα∘Φ。
逐时像集同旧M12：D≤3.787020263961937、reach/D>.0312033094、held/D>.0527832251、
diam(H)/D>.9354609822、含反射δE>0。三完整PLY已推，各71858点/143712面/4610固定帽点。

**已确认研究批次：c57249ac7dbda27de4bb178052cf78f81d641643；恢复源/完整证明批次277762b570d881636fdd0ed06d335c3d1ab48cd6。**
包含R128–132、精确平坦尾/正clock全部源与检查、新flatcut物理候选、
真实prefix IVP到s=.8090484941、root raw Jac01和首个signed full01失败、旧tail与旧prefix闭包。
该批之后的本地结果没有推送，不能因为旧HANDOFF写“已闭”便当作远端已有。

## 2. 规则同步与执行环境恢复

根README全文含授权及全部规矩已读。最后实际终端pull及两README差异检查：
`db44cc3e389449a315850f397cc65d32dcc1ea76`（2026-11-12 11:28 UTC），
相对已读API快照0fb5722af1bcd1f73676b56426f4aa0996a4a71e两README无差异。
每次pull立刻只读这两README差异并记录SHA，至少每小时；下次不晚于12:28 UTC。

约10:58 UTC旧执行器明确unavailable；11:23 UTC新执行器在/真exec0，
旧/workspace/scratch/fd2dbfd2c83e确实不存在。未推数组须重算，不假称保存。
当前普通git部分克隆：/workspace/scratch/fd2d-recovered-20261112/math-research，
仅检出本题。终端git认证实际成功，恢复使用普通git push；PAT只在命令环境中。
277762已保存R133/134证明及新身份的恢复源；旧数值测试不转借新源。
CI备份两源已在隔离bare-git实测正常发布、保留他人文字、规则变更中止；
暂不启动与本地重复的Actions。正在本地真重算初值、K15分支、新物理候选与实际body。

## 3. 强目标及已证工具

强目标held/D≥.2、δE/D≥.05，固定H、全时C²嵌入、reach/D≥.03、
同g全域metric≤1e−6与实际加密、真实尾/帽两jet接合、完整网格。
不加原2e−9门；不以中间结果、失败或时长收尾。
R121充分几何窗：cuff.32、ρ.136、D≤4.5、Z∈[.9,1.378641…]、活动|y|≤.85、中央A≥1.28；
δE/D≥2299/45000。全核球包、held排除、跨片法球仍须实付，窗口不是唯一允许几何。

R115/118准确同周长balanced中央；R116一阶GC/C²；R117真实height两jet→II；
R119有限三残差到实际ODE metric/曲率；R122真实体距离/法向；R124固定u角变分；
R125逐cell残差primitive；R126真实两jet领圈；R127 inverse-Q正warp。完整旧证明均在main。
small01准确clock全部237格全角连续前缀U=9.82291790194277e−7，只有小幅前缀，不预支强闭图。

R128精确平坦g=dr²+r²du²，F=(r cosu,X(r sinu),Zc−Z(r sinu))，
α=odd A S9((|y|−.34)/.46)，cut.8/cuff.32，r≤.34逐点固定。
A≤1.2全域κ≤4725/736、support≥.35；A1的|h2|严格>.104576455，分支覆盖.1。
R130完整广义柱面reach≥736/4725>.136，尾/平盘/上下尾法球与条件held预算完整。
尾alone相位仍全等，必须接真实非圆prefix和固定帽；机制历史见R43/R71。
R129独立l/m/n、Gauss+双Codazzi、moving chart/JVP，不在n=0处除法，不预付DAE可逆。
R131正径向clock覆盖所有正物理coast，固定T仅换坐标。
R132正Bernstein尾控制盒[0,1.2]给统一全尾曲率和R130预算。

## 4. 当前物理输入和可靠可重跑起点

候选 notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json，
SHA a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147。
中央直柱.5、early return K3.4、redeepen K6.8，末flatcut(.8,−1,0)；
end1.344258724456249，Tref.02/Tmax.22510364412376974，背景Zcut1.202982473751077。
真实非圆cut的Z必须由实际位置积分得到，不能直接取tail默认plane_height1.25。
实际最后phase_bridge是三次Hermite：背景n~d²、l~d、K~d³；不是五次阶数。

已推真实IVP80564/7cd1b3真0/42.962s：355节点止s=.8090484941089444，
末metric3.02e−10、κ7.15643。后一点高频污染单列，不排几何。
已推 notes/2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz
及closed-manifest；reader fd2d_flat_prefix_initializer.py SHA6300cd5e…effa9。
固定seedφ与材料u必须正确转换。共享节点Hermite只用作BVP初猜，不冒原DOP dense定义。

已推root raw三场：准确seed/tail lifting，cut correction=0时保全部cut均值。
K个中央参数+(K+1)tail+T，与gap行配平。Jac01真0、四类JVP相对≤1.11e−9。
signed K7 full01 64520/10452e真0但solver失败：30accepted、res10.36184、
fullG98.9739、形式κ206.415，中央n负。该失败完整实体/源已推，不给坏场追加证书。

## 5. 未推结果的真实记录：需取回原文件或重新运行

以下数值均是本次真实观察，不等于远端当前已有其数据：
- positive full01 4063/cc302c真0/156.157s，42accepted，res26.499，T趋1.60e−6，失败。
- bounded01 11056/18ee1a owner130，3accepted后res13.009/形式κ18.6476、
  中央nmin.00325/gap.82777；改方向以保中央域，未作几何否定。
- Schur01 92078/3d8f8f真exit1：首次方向后日志seconds键重复，0accepted；已在本地修复。
- Schur02 77250/a6cd91真0/19.131s，4accepted，res.37904765、
  fullG2.59876/形式κ21.5330/gap.900012，仍失败。
- Schur03 10897/1bf935真0/69.747s，60accepted，
  res.42933326/RMS.0371303/fullG10.37524/形式κ24.19534，仍失败，不再给纯F坏分支追加证书。
- 精确边界显式投影：cut全部correction=0；中央n=C*c、m=l=0，然后重算原全F。
  方向先消掉这些线性边界，再对内部场作稀疏Schur消元；
  16物理参数QP含tail盒/T正/中央采样曲率[.1,1/.136]/gap线性等式。
  这只是搜索域，不是全局不存在性或新增最终门。正确Armijo使用FᵀJd，
  原先每单位步强求10%相对下降会错拒约束下降方向，已经定位并修复。
- numeric较早退出IVP(.58→.94)再作固定参数线性Codazzi最近投影75%：
  K7/113nodes、T.02、中央0、tail全1；res3.06326570/形式κ7.12331191/fullG6.86972989。
  原selected-02 SHA474ed07d40eaddc7d8536a98dbcbbf09530d7757829d490da273f1695c680ba6，
  当前实体不可访问，应从已推IVP和恢复源重跑；不伪造数组。
- K7→K15准确Fourier零填充和Bernstein升阶初值已实际生成，只有初猜、不是加密成功；
  原输出SHA729115b864b684e0146c17e72c184b5cb7022b38eb43b6ea294111c40e1b429e，亦未推。
- 角诊断K7/15/31的fullG约6.68885/1.33332/.35904；固定φ对照更差8.82757/6.78065/1.24629，
  保留现moving chart。redeepen处未投影初值l24.205也说明曲率大并非只有漏模。
- fixed-m与谱Gauss/cap交替均未同时改善全F/全G/曲率；完整真实失败待恢复源后归档，不重复扫权。
  新同Frobenius对照的工具回执尚未返回，启动/退出未知。
- raw-native P1 reader/实际R124两jet接口曾真0，原节点值/角导连续，
  完整C²说明与R133 cut刚体对齐/真实Z/四cross-ball一维式已在旧环境写完但未推，完整证明与重建源码已随本批提交恢复；原数值仍须重跑。
  R134 Gauss+曲率cap区间完整证明已随本批登记。
  curvature_penalty主helper已写；checker调用在环境失联时未返回，不能声称检查通过。

R133/R134、raw native、Schur/Armijo、曲率项和初猜重建均已恢复为新源身份。
对应API恢复manifest只记录文本源，未把不可访问的旧数组冒为现存。

## 6. 当前执行方向

已恢复75%初猜源、Schur/Armijo与准确边界实现、K15升阶、独立曲率penalty；
在恢复终端真正计算并保存退出码/源SHA/完整主态。penalty只选有限formal曲率较小的分支，
原Gauss/Codazzi不改，最终仍需实际Cartesian图与连续证书。
numeric正用唯一local-recovery01重生桥初值→K15→penalty导数；根接续K15优化。
metric先以旧jac初场实际smoke固定u24态body，再消费新字段；geometry真生成K4.5物理候选。
同时直接设计redeepen K4.5/3.4、中央直柱.4的新物理prefix以减低真实曲率瓶颈；
正coast/flatcut/Z预算必须实际求解，外设计不能称同g加密。
全部prefix/tail/bridge/collar/common/mirror/caps、全时几何、同g加密、固定帽和三网格仍待完成。

## 7. 操作

不force push，不改写别人提交；每次pull立刻查两README差异并记读SHA。
H<10KB、MD<100KB、数据>1MB gzip、单件<5MB；只保复核必需数据。
不加冻结/独审/重求/C³/审批门。CI共享设施本课题可直接修，根LOG本题一行≤200字。
