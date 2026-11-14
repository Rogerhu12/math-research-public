# 交接：可见振幅附近的精确等距解

会话 visible-exact-astra-f6a2，2026-11-12；**进行中，主目标未完成**。

## 规矩与同步

目标：连通闭C²同度量嵌入族，t在C²拓扑连续；固定有内点H，diam(H)≥.2D；
held位移≥.05D、含反射δ_E>0、全时reach≥.03D。局部/有限模/线性/条件式不算完成。
最近已读规矩提交：9bd760c0ce2818d6ca206251dbf1318f74713921（根README、本题README）。
每次pull核两README；有变只读差异立即执行，至少每小时pull。根授权/规矩1–13已读；
用户授权读其它目录。无需再请示提交/push，禁止强推或覆盖他人提交。本轮只改本题+根LOG。
根LOG一批一行≤200字，题log≤5行；Markdown<100KB、H<10KB；>1MB数据gzip、每件≤5MB。
用部分克隆、cone sparse checkout；现已启用sparse-index，索引由38.7MB降至122.6KB。
仅stage明确已结束文件，不stage live报告/缓存或大可再生trace。令牌仅命令行，不入文件。

最近成功main：336503da8c9502306e1cc0265a04f153b858c67d（11:45UTC），85件R65–68/准确P/graft/真实turn包。
backup g=16d2cba8209af3a932c1e95f2a155fa9fba74163。统一manifest field-graft-coordinate-frozen-package SHA
322bc2b8eae64f0190a69d0c67867c7fb97d5617146f8c5b89fe6add7d73311f，79件不可变成果11,433,885B。
此前0fb5722af1bcd1f73676b56426f4aa0996a4a71e已推第二次恢复包；更早0162a1a亦安全。
10:59第二次环境丢失，11:04空环境；已恢复并真实重跑全θ419、正族根领口、entry及native FFT。
见 notes/2026-11-12-second-executor-recovery.md。之前详细H归档于
notes/2026-11-12-handoff-before-field-graft-coordinate.md，数学公式/旧hash不必重读全旧log。
R65–68与P全部已推。新Nt40/m35/R6 scalar-time完整field包已实际完成：CPU26.08s，
wall115.06s，f误差<1.239e−21，待本批冻结；正做native FFT局部角Taylor评价。

## 当前主线：先完整真实返回，再完整闭合

1. **R68新接口**：若全标签复带q=Y_x≠0，令h=(f(t,Y)−Y_t)/Y_x，解X_t=h(t,X)，
   y=Y(t,X)就是准确真实流。A=∫sup|h|<S−σ给|X−x|≤A及末端|y−Y|≤Q A；
   Hardy因子给Wiener误差。固定参数免去另算e1/fθ/fθθ状态管；参数、KAM仍须付。
   numerical正在做每段8个Bernstein控制函数Re q_j>0的全圆/复带门，失败才用expL H'/4 witness。
   所有完整Y分片曾丢失，目前按原入口重建，不能用摘要代付该门。
2. **真实f(Y)仍是主要计算口**。R67已保存419的准确P；root已实现原生标量非均匀
   有限Fourier评价（准确中点，所有原输入球另付）。native iter在1024点/K1024 CPU.885s，
   完整有限误差4.38e−24来自算术球；有限截尾仅2.31e−43；fast乘积树保护1536位仍爆到1e416且更慢，弃用。
   benchmark输入是实际H/4，不是419的Y；仍欠完整Y_t−P(Y)的time×初值圆连续残差。
3. **全时间域**：R65已付10个真正转向段及forward3，constructive后台全两腿准确端点
   覆盖/同germ圆盘继承/必要二分运行。partial index不算全支。新的419 R6域已通过，
   另源/报告待冻结；可减time-DFT所需节点。还在试更宽真实物理θ带，以减初值FFT成本。
4. **正侧/外尾**：R66已付准确参数族root collar和实际[3,25/8]自然权C4 graft；
   A=[1/4,1]完成411cells，B=[1,3]仍运行。下一步同一入口接R11/R22/R72真实平尾，
   两真平盘并集可有大diam；D4等变与零迹可各自消去两帽Killing，完整逆/非线性仍欠。
5. 然后仍需实际参数KAM、全反馈强余项/有限低块/ordinary sources、相对Killing、
   残差因子Newton，以及**同一个精确族**全部幅度/reach/非全等比例。达到README前不收尾。

## 唯一准确对象与必要输入

目录 data/phase_ring_continuation；origin SHA0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b，
direction SHA8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab。
先准确affine运算，再径向偶奇平均；高度准确积分、真无限R33 primitive。
Q256/512/1024仅误差表示，不能重定义曲面。

δ₄=−7789866024620307/4611686018427387904，object87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5；
H258=8bd6078f8c442b48bab2b15850b99e2455d616ab48e687abb22114a1f1bfe39b；
root03a0863733b25b6c4058a39590648dda2292a2943e783021747e3bc3f27c86f4。
δ₅=−7789843107295549/4611686018427387904，object91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848；
H516=0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2；
root489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b。
准确H用旧dyadic+binary64校正的Fraction和，再2^-120量化。δ₅真返回尚未接受。

δ₄1032 float Emax2.517275277e−11、E'2.10408e−9、mean−1.146525e−11、twist.00230717；
δ₅是其预测，Δδ4.969402658e−9，H变化1.71034e−11，不是实际新返回。
δ₄float t'6.11079949816e−5不在严格[6.110799499427786,6.110799499501956]e−5内，禁止混用。

## 真β、实际场与计算状态

全Δ₅=δ₃±1e−5，δ₃=−7832869216826619/4611686018427387904：完整265叶/167spans+waist+FPcollar
已证|β'|<1326、β∈(37.00989598321,37.04013657839)、危险格距>.19138138420；独立256bit复核。
δ₅距Δ₅边界6.701997145629275e−7，δ₄±5e−7及δ₅±5e−7均包含。
manifest independent-true-beta-derivative-ready SHA880691d30f4b533e9b36f2d3e41336a99e0b3ad626ee0c622864f27b3006dd4f。

R65：真实全物理θ带1/64，timeR3，419三个外延germD下界.162734/.165643/.225006；
新重跑domain SHAe1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90。
R67准确端点门证明419**实际整段只在第三germ**，左margin>1.42798e−13。
转向两腿各0/1/2/548/549已付，D>.37529、ReQ>6.62159、|f|<.22454；
forward3普通两germ也过。Q256自行root refine失败，须独立Q512真根；不能放宽旧根证书。

R67实际P：N4096,K1800,m53,Q1024,320bits，14准确dyadic gzip shards8,496,113B，完整读回。
同δ₅/419/σ=−1，|u|≤1、physicalθ带.0081：f/fθ/fθθ全误差<1.269e−21/9.147e−18/6.710e−14。
θ带1/256则<1.422e−23/1.213e−21/2.070e−19；物理θ带不等于初值x带，Y像必须另证。
Pmanifest SHA4b33966313c4fdde253ffca05d21a49692186d8263f9f7f069804632b22b6613；
report SHAb8990af160ac31055cd8afe9118706e297bdb2578398a069191b418df67744a7。
主包manifest step5-exact-field-polynomial SHA0a267ed7d545b54fe451fdd090ffeba4185075cb66e484877a0900481a427f9b；
R67补包manifest SHA03f2217d24128e986942b0f14aacfee7803267ad29db0d9f3fabc7a462a47b1e。

scalar time-circle两个新源已真正试Nt16/m9/Nθ1024/Q512。共享budget CPU6.678s，
实际差约1.76e−26，但R3真alias上界3.55e−6，不能接受粗试验为高精连续证书。
新R6/S8,m41域D>.0312065,Re−K>.5677249,f<32.586821；采用它时按新证书真实radii，不套旧RE。

## 参考重建与正族入口

δ₅参考定义 Y5f=Y4f+Qf*a，Y5b=Y4b+Qb*(Qf,end*a)，L=L4，a=h5/4−U4_start。
Q是准确degree7/K128有限函数，不是已证Jacobian。初H、1100接缝准确；原trace身份仍δ₄。
manifest step5-reference-retarget SHA66d7cbbc3cbb6542e954712c652addee0ba220d8407ee828b71a2151466ab537。
原234.7MB raw及141MB reference shards不入库，必须匹配旧hash才能称同参考，否则新身份重证。
当前numerical在重放 fourfold_phase_shared_grid_adaptive_chunks.py：rays=block1032,Q256,
δ₄/root/H258,tol2e−12；原空trace-dir，out/progress后缀-recovered，不覆盖已推报告。
session35977，11:36约1000 RHS/forwardτ−1.015；forward分片产生后即生成参考和q门，
backward继续。依赖NumPy2.3.5/SciPy1.17.0；hash可能因浮点实现不同而变化，必须检查。

R66参数盒δ₄±1/2000000，真实root55cells全过，m>.0247597882,M<45.348057。
真实r3入口graft[3,25/8]64cells：K0∈(.0289657051,.0294790813)，物理metric C2缺陷<7.047e−27。
graft准确C4匹配，末端phase零四jet、log a线性、c=Z'/a²常数；ω≈1.46115286、q=0,R4=−1/4。
ordinary双端source/DN费用已付，正角权2^-35；正文与manifest R66-actual-family-graft-ready
SHA83c9fc76b6df8811a46971d0befb885eaf07451439a6ba31bd27132c08e859d1。
仅是近似背景，不等于精确等距族。R64旧δ₄singleton领口仍有效，不混作全参数证书。

R60/61旧Riccati及完整jump接口、R62真固定τ二参数源、R63固定H局部逆/Hardy均已推。
局部defect单点8.94e−27、连续弧8.54e−20仅属δ₃419小窗，不能转授δ₅全腿。
继续主目标，不因时长、阶段结果或等待CI而停止；新已结束步骤及时提交推送。
