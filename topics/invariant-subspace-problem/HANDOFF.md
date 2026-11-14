# 交接

## 目标、规则与同步

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；须全体有界算子定理或完整反例，有限模型/候选排除均不算完成。
- 根Astra-ISP-789f独占Git、H/open/results/log与main；代理只写各自789f稿。
- **最近成功实际 pull 与已读规则提交：** `feab9848e2bb79e0c6f97eeeffd8d02743f2a0a3`（2026-11-14 14:33:37 UTC，实际pull/rebase成功，两README差异为空）；旧库已读迁移授权 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；历次同步见 notes/2026-11-14-root-git-sync-checks-789f.json。
- 持续研究，每结论即提交并推；非快进立刻pull --rebase再推到成功，不force。至少每小时实际pull，逐次只读两README新差异并立刻遵守。令牌只CLI临时环境；不写根README/LOG、不问重复授权。
- 迁移授权已读，只用Rogerhu12/math-research-public；规则12取消额外独立复核，规则13本库Actions约4核16GB、每job≤6h、账号≤20并行。Markdown≤100KB、H≤10000字节、log每条≤5行、数据>1MB压gz/每文件≤5MB。
- [压缩前完整H](notes/2026-11-14-handoff-before-all-birth-second-variation-789f.md)、[完整前open](notes/2026-11-14-open-before-first-padic-obstruction-789f.md)保全部旧范围/失败/来源链；未列不等于已闭。

## 工作区与可恢复数据

根入口 `/workspace/scratch/789f3e887d7c/math-research-recovered` 现软链到 `/dev/shm/isp-789f-math-research-recovered`（14:12根盘满，整个检出连Git迁移）。代理旧稿在 `/workspace/scratch/789f3e887d7c/math-research-public`，其.git指针失效，不在那里用Git。此前断连丢失的未推Green/Garayev结论已按记录重做并推818e9d7b/4c071886。

T96/NF/三个来源DAG已从本库run43597823809 artifact14114364261恢复到 `/tmp/isp-t96-recovery-789f`，至2026-12-14；原model补在 `isp-r150-native-nf/normal-form-input.txt`。完整已完成目标/原17证书/标准源/残差另在仓库，不依赖该到期artifact。当前β中间目录 `/tmp/isp-first-padic-789f`，旧canonical在 `/tmp/isp-kernel-standard-789f`。不重建旧图或重跑高次数来源。

## 原问题的未付接口

H=L²(Z₂,Haar)，Af(y)=a_v₂(y)f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]、零点权0。A非零非紧、单射稠密像、拟幂零，W*(A)=B(H)、A′无非零紧。N_j²=η_jN_(j+1)、N_j WOT→I/2非SOT；闭A不变M均closure AM=M，普通循环性未知。

原Haar慢理想和负边界T_N/T_Y分开；后者M=kerT含e0、N=closure BM，N=M未证。R187/200有限像与R239合法d≈log^(1/3)q窗口/权核已付，无权完整λ²=〈G⁻¹r,r〉增长/发散仍缺。原graph保M3初次/M2以后、同w/同未来/真负前缀/自然逆域及完整左右费；Keff≥e^(59d³/256)/(2^19d)不付固定测试Gram、pure深jet、普通右费/跨birth。primitive MP不代graph，固定birth不代移动birth。

一般有限原秩正常湮灭者未闭：R276正完成不付全链正距，R289熵o(m)仍容R291指数rank，下一尾理想距离m_j/单位锚未付。R147/150其余mean秩/高ess、R176部分谱、R236慢核/原右源及R268–290全部剩余条件见open/归档，均继续保留。

## Boolean相位、加强费用与连续尾

- R297全正权/出生/高度加强κ等价奇硬首边同κ，真实费A_U*L1L3⁻¹L1A_U，倒数桥B*L2²B≤κG1；完整逆、投影及同源不能删。R295 birth1全height κ1024、原尾674/81；R298全独立五权K2≤743/782。R300一般旧2s＋三弱位全三族范数极限无放大，边界不代有限内部。
- [完整共同谱](notes/2026-11-14-critical-even-pool-commuting-full-grams-and-phase-moments-789f-next.md)给F/Q交换、T²=F⁻¹Q和Tv=σp⁻¹D²v；压缩矩不交换、低birth不删。[奇→偶完整极限](notes/2026-11-14-odd-to-even-weak-bit-phase-limit-and-universal-hard-transfer-789f-next.md)证明所有偶相位统一κ单独足全部加强高度；一般κ未证。有限a逐系数路线被真实四权排除；首Schur条件SOS尚缺最高边联合缺陷，详前H。
- [四个任意正权](notes/2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md)整个三维phase≤1、等权取等，完整正系数证书已推b233febb。[三/五位全源](notes/2026-11-14-three-site-phase-sos-and-complete-five-site-boundary-789f.md)：三位极限0<K<1；(r,r⁻¹,1,1,1)全部4维K<3/4，固定r加小弱位后整个9维≤7/8。均不外推更大任意池/统一阈值。
- [全位数二阶相位](notes/2026-11-14-all-birth-even-phase-equal-weight-second-variation-789f-next.md)真实物理酉源上I−Φ=ε²(Bx*Bx/4+Sx*Sx/2)+O(ε³)。中央全部s子集x和距0≥m>0则二次项≥3m²/4，给每个固定方向充分小ε严格界；不称退化方向或共同邻域已付。
- [同源Johnson正交](notes/2026-11-14-source-orthogonality-parity-payment-and-intersection-polynomials-789f-next.md)保完整q/ell，以ε=(-1)^(s−1)支付最高两通道，负项只在j≤s−2。两侧可独立取交集多项式deg≤s−1、值[-1,1]；不能逐r任意改号。M24/s4算术反例只排出生一方法直推，非S1反例。R294/296混合费、真实低通道与graph继续。

## R150 原十七式及特征零来源

原11物理N＋6Γ，M5为6188×4367、泛秩4354；rankAy8和0/2/−6/∞已闭，余rankAy9有限Σ/char0来源。完整F31像1021行/次数和716、torsion315/minpoly190；九目标h31度24，char0候选h0=s³(s−2)F+²F−²E8。原线性逆Dlin46次不免费降24；模31支撑不当复坏点。

- [T96完整图](results/R150-appendix-complete-t96-kernel-and-exact-nine-source-identities.md)run43597823809得1021输出/1174真核；[原17完整模31证书](results/R150-appendix-nine-targets-full-original-seventeen-equation-certificate-mod31.md)全DAG及原4367×147×9系数核清，最高135次。完整gzip均已存。
- [唯一标准来源](notes/2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md)最小cost为85（j5为84）、最高69；B85有217374个模31/char0独立标准列、219032输出。h0 mod31=25h31；原x0最高74次/cost85，首轮r1完整整数数据已存。
- [完整像障碍](notes/2026-11-14-r150-first-residual-fixed-source-obstruction-789f.md)全9 r1余非零，单位子式排h0各目标在固定标准列Q像；仅添同标准族更高次数仍无效，未排非标准来源。[精确挠定位/dual](notes/2026-11-14-r150-first-residual-torsion-scalar-obstruction-789f.md)各余最小(s−1)(s−2)，2835×24系统rank24/增广25，25坐标dual仅用j2，排固定初值的任意次数h0+31g。乘ell/E8仅有未恢复cost的mod961存在性。
- [有限β判据](notes/2026-11-14-r150-budget85-full-source-bockstein-and-saturation-789f.md)mod961可解iff[r1]∈imβ；有限coker不能换无限G商。[exact Koszul降维](notes/2026-11-14-r150-exact-koszul-compression-and-bockstein-1152-789f.md)保cost消660未选N并lift972低K。原B85共289198列、模31核71824/coker1658；70672方向β零，仅余200高K的1152移位待算。这里未宣称完整char0有限秩相同。
- 全200高核[执行接口](notes/2026-11-14-r150-high-kernel-bockstein-execution-interface-789f.md)及本库workflow/request已冻结，3 native限额编译成功、尚未新数学执行。一次Actions共享300秒数学deadline、512MiB每进程、编译各30秒；恢复run43597823809原图/DAG和落库model，不重建。手动dispatch实返403未运行，改本库已有授权的固定request推送触发；根取回全部小结果及recovery；无限315必要像若通过即转有限1658预算，最后仍需有理原17身份。

## 当前分工与待接结论

normal_annihilator继续有限1658预算接口，根提交并启动高核β一次请求；literature_audit继续真实一般相位及退化核四阶；boundary_core继续j=s−2同源条件均值/协方差。根负责原源接口、工作流、证明整合与每结论推送。[退化零核原例](notes/2026-11-14-even-phase-second-variation-kernel-not-preserved-789f-next.md)已提交：二阶零但沿线缺陷u⁴/3+O(u⁶)，排永久等号；等值组Casimir约化正继续。[首低Johnson共同Schur](notes/2026-11-14-first-low-johnson-channel-common-schur-and-original-tail-linear-budget-789f-next.md)已付j=s−2线性条件分解、出生二准确Poincaré式、原尾任意删位协方差预算2(1+2k/x)¹⁶；条件均值仍未付。

Garayev第二分支强制零与其余当前原文条件已推4c071886，balanced-walk两层度量不匹配已推58436f16；旧文献适用范围保open/归档，不重复已排路线。主ISP未完成，不以阶段报告收尾。

## 计算同步

- **最近 CI pull 与规则核对：** `9da7d829b4ed24357484ab5cadf038f2e553b4a3`（2026-11-14 13:10:38 UTC，实际 pull/rebase 成功，两 README 与任务源哈希一致）；R150 来源图运行 43597823809-1，真实结果见本次回执。
