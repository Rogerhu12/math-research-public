# 交接

- **目标/完成标准：** 完整解决可分无穷维复 Hilbert 空间普通不变子空间问题。原候选A是否有非零真闭不变空间仍未知，绝不把下面中间结论当完成。Astra-ISP-1cf8c51d / 2026-11-13（UTC+8）接手并持续工作；根README授权及13条、本题README已读。
- **规则读取检查点：** 162a3a50d2a5f7fc8a508c0b51e221734e988fc8。最近实际 git pull --rebase origin main：2026-11-12 19:10:08 UTC；两README差异空。后续逐pull比较，至少每小时一次。
- **工作树：** /workspace/scratch/1cf8c51d8ffd/math-research→/tmp/isp-1cf8c51d-math-research；main，blob:none/sparse，仅本题。共享盘满后仅迁本会话568文件，逐文件SHA256一致，路径保留。PAT只在命令行进程环境；普通git push，非FF/远端ref竞争立即实际pull --rebase再推，禁force，不写根LOG。
- **main恢复核实：** R206–209已main44c5ba276；R210正文/附录及7份相关稿按47c6d2恢复回执逐blob核对，接手已推main **e4cb6645dd81d46d3359326ab1d00283c292da52**。R211旧完整草稿已逐式重做并推 **a897afcfde426afea68a8f89597e00e09c3aaaa4**。旧scratch的R210_R212命名草稿只读保留，R212尚未见完整结果，故新结果从R213起避免冲突。
- **完整旧接口：** notes/2026-11-13-handoff-before-R213-1cf8.md、notes/2026-11-13-handoff-takeover-1cf8.md 保留全部此前H；更早open快照仍在notes。本H不丢掉这些文件的证明依赖。
- **本会话未登记新稿：** /workspace/scratch/1cf8c51d8ffd/agent-notes/（实际/tmp/isp-1cf8-agent-notes）。boundary已完整写可移动纠错块的多项式尾、全孔前缀一致衰减；normal_states已写真实慢半群平方根增长/正常态指数尾及指定测试族指数成本下界；root正在全文核对后逐条登记推送。root独占共享状态和git，代理继续推导。

## 实际模型

H=L²(Z₂,Haar)，Af(y)=w(y)f(y−1)，w(0)=0、w(y)=α_v₂y。
−logα_j=(280/3)16^j−90·8^j+300·2^j−850/3；
W_n=∏bits d_j，−logd_j=100·16^j−105·8^j+(150j+25)2^j。
N_j=A^(2^j)/d_j=E_j+η_j E_j* N_(j+1)，N_j²=η_jN_(j+1)，η_j≤e^(−770·16^j)。
V_j=(1−N_j)/(1+N_j)，h独立第j位时V_jh=χ_jh。
C f(y)=overline(f(−1−y))，B(f,g)=〈f,Cg〉，内积首变量线性。
Haar E_j为物理e10；负整数边界孔表示中E_j是消灭e01。两个表示不能互换。

## 已证基础与界限

- R125/128/140/184：全部非零ℓ² first全H循环；闭域/通常伴随核心；全部有限放大不变子商图核心。G快解析逼近代数及指定正逆场普遍单射稠密；一般慢Acal/一般first限制像不在已闭范围。
- R172/176/180–186：多模式自然幂、Bell及联合循环；联合循环不排单核。R189–199不同正锚不可无证合并。R203/204适应Cantor正逆及ℓ¹族只在预定可数资料上成立。
- R196/201：双正抵消同域、双逆真实核；横向商无界非全域；移去真核仍无统一下界。R161/164/193/198的伴随/Calkin/尾逃逸均未排任意慢尾。
- R209：任意ℓ¹无限支撑复Cayley系数，输入/输出均有限孔次数迫输入有限head；核恰最低非零层有限旗。无支撑gap条件。有限支撑有反例；无限次数饱和仍开。
- R207：同一有限柱Pm对first范数交换子→0和完整图逼近；指数次数权控制危险分支全零头的低次数概率，只有下界成本，没有相反上界。
- R208：危险平方核全等向且⊂closureRanT。实际头图 M={(-Jy,y)}；共同像N=closureWL=closure(ZL+WL)，商Q上W_Q=Z_Q=0可能。单bit只控制||P_CM J_j P_M||，不是整个投影commutator。尾商度量若非零则谱对称且全本质，半正只能零。

## 边界与正常态最新接口

两边界慢算子T_N、T_Y系数a_j=(j+1)^−2；B为负整数加权后移，M=kerT、N=closureBM、Q=N/Ce0。
R185/188/195给无限核与非标准norm理想，不含A幂且与非零G/boundedK零交。R187给closureB^rM=N、closureBN=N；R200给M∩RanB^r=B^rM⊕Ce0。
**N=M仍开**；有限次数在环境中稠密不传到核内。

- R210：固定正UHF态φ湮灭J=cl(S Acal)，同一子列φ(N_jk),φ(Y_jk)→√3/4。全Banach商弱零路线已否定；只限Haar-normal测试仍开。
- R210附录：φ(S*S)=0及原S单射排任何受支配Haar-normal正部分；四位真空连乘预算排边界正常部分。标准g_s∈N，去e0后在稳定Q实现同一Acal泛函，**没有整个UHF商同态**。
- R211：共同有限树窗口和固定线性修复给弱*连续Cantor/连续相位态族。商及稳定Q的Calkin像中均有ℓ¹高位闭子空间，下界2/5；全部态双重纯奇异，不提供Haar正常见证。
- 高位弱复制：真实comm误差≤64η_(j−1)，精确弱零复制保每个固定UHF E的作用范数。所有B幂在M/N/Q非紧；标准与弱首修复构造均在N。
- 快速head残差：A_m=e^(8m2^m)，若v_k∈F_mk→g且A_(mk+1)||Tv_k||→0则g∈N。统一dist(v,N)≤A_(m+1)||Tv||+κ_(m+1)||v||，κ→0；只给未知M⊖N超快尺度尾下界。
- 相邻双反射：真2×2域、CH及奇余数给 B(BD0u,JjJkv)=2ηB(KK′u,Jkv)。危险sqrt的D0字符为16b²(b/a−1)²；E/B全H无界，但未知核限制仍未判定。

## R213 本轮新结论

完整文：results/R213-walsh-block-deletion-and-coefficient-tail-kernel-obstruction.md。
对X=a*+Σa_jV_j、Y=φ(Bell₂)、M=ker(X−Y)，R161给同一核T*|M有界，R208给删除完整域。
逐坐标P_M n_jP_M≥β_j²P_M；更强的有限块秩一删除D_I=|Ω〉〈Σaχ/||a_I||₂|，其纯comm范数≤(1+√5)||a_I||₂，真实carry O(gη_(m−1))、Bell差O(||a_I||₂²+g²η)。得到
|| (I−Q_m) f ||≥c ||a_≥m||₂ ||f||（η_(m−1)/||a_≥m||₂→0）。
规范a_j=(−1)^j(j+1)^−σ、1/2<σ≤1时下界m^(1/2−σ)，非零核向量的最大Walsh指标(2σ−1)阶加权二次型必发散。
此处Q_m是Haar有限柱投影，不是边界全孔前缀投影。更慢尾仍可能，未排核。

## R214 本轮边界推进

R213已推main 2b7d62a9b11ac7f65543a5da436c25c2c1c28b24。完整R214位于results/R214-movable-correction-blocks-and-polynomial-tail-obstruction.md。固定r≥1，以任意后移块[L,2L)纠错真实右移，再归一化精确修复，得到x_L∈BM、x_L−e_r⊥F_(L−1)、||x_L−e_r||≤C_rL^(3r/2)。于是f∈N⊥有|f_r|≤C_r(m+1)^(3r/2)||(I−P_m)f||；未知M⊖N的临界最高位3r阶二次型必发散。实际T_N*e0在N⊥达到r=1的3/2尺度，但它在M⊥，不是缺陷反例。必须另用核方程，N=M仍开。

## R215 真实增长与正常尾

R214已推main ac878b7eed043b8a6f86766b1bbdc886516931d9。R215完整文在results/R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md。任意|c_j|≤(j+1)^−2及N/Y混选，真幂四次预算给||exp(zT)||≤exp(16√|z|)、||(c+T)^−1||≤(2/c)exp(128/c)。真低头/尾张量测试J_m∈S Acal满足||P_mJ_mP_m−P_m||≤1/4、||J_m||≤24(m+1)e^(256(m+1))。任意秩Haar正常正湮灭态有sqrt(q_m)≥e^(−256(m+1))/(128(m+1))，有限放大零子商同样；不声称J_m强收敛，不从任意秩/有限秩推出尾速率。root双侧增长稿已独立核验待R217；normal_states继续精确型及有限秩。

## R216 整个边界核的前缀控制

R215已推main cf047a46b5a0b3350d90132cda97e899c2523a13（14次实际rebase/push循环；逐次两README差异空）。R216完整文在results/R216-uniform-occupied-prefix-decay-in-actual-slow-kernels.md。Q_m投到n≡−1 mod2^m，||Q_17r f||≤2e^(−4r)||f||，任意γ<1有||Q_m|M||≤Cγe^(−γm)。全部M嵌入e^(s v2(n+1))加权域（s<1）；固定k最高剩余类同率，故(B*)^k|M环境下方有界、P_MB^k:H−→M满射。不能换成最高位尾或压缩伴随；仍不足α_m^−1右移权。boundary已另写实际局部右移像误差趋0而核残差爆炸的稿，待核验；root局部Haar增长稿也已完成待复核。

## R217 圆周一致增长

R216已推main 984895dfca30cf070dced9542d8868a0f8f00afd。R217完整文在results/R217-slow-symbol-entire-order-and-directional-resolvent-growth.md。保留O(log r)真实低头，远位单孔相位张量给||exp(zT)||≥exp(√|z|/27)；全满孔块唯一阶矩阵元给||R(λ,T)||≥|λ|^−1 exp(1/(256|λ|))，真实差用Duhamel/两次预解范数支付。结合R215得整函数阶1/2、1，任意复相位及混选统一。normal_states已完成精确Gamma型稿（拟R218），root固定Haar柱局部型稿也完成；完整推导均在agent-notes待逐项发布。全空间型不替代未知限制增长。

## 继续与禁用捷径

boundary继续任意M内右移域密度/TF=0对正交补的额外限制；kernel继续秩一块删除后的局部配对及未知核上第二次除法；normal_states继续有限秩正常正湮灭关系；root核对、逐条推送并推进独立整函数/预解增长方向。
全H quasiaffinity≠限制dense；形式阶≠有界除法；C不自动保M；强小量除慢系数须有预算；纯奇异态不代替Haar-normal目标；环境稠密不传未知子空间；不要从下界推相反上界。普通ISP完成前不停在阶段总结。
