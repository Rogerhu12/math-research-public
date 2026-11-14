# 2026-11-13 执行中断、恢复与未推结果账

主目标未解决，继续工作，不在此检查点收尾。最后本课题已推提交
`e4f2036d882b50a0e24abe62c6754344539418cd`，含 R190/R192。
20:11–21:40 UTC 无可用执行环境；期间纯 JS 数学计算有返回值，但
重新接入时 `/tmp` 与 `functions.store` 全部清空。以下历史校验值
是本会话工具返回的记录，**不是已经恢复的磁盘文件**。

2026-11-12 21:41:18 UTC 正常终端实际 pull 到
`107ac6361ffd76db60e83d1c5d8078dcb9d0e844`；根与课题 README 相比
`dcd9b03531f06fc9ab0782c66ff19cf3a9493da8` 均无变化，本课题自 e4
也没有远端新增。21:06 到期的实际 pull 曾因环境不可用未执行；
21:05 的只读检查不算 pull。以后继续每小时实际 pull。

## 原已推输入完好

`scripts/data/p41_poincare_miller_jets47_saved.json.gz` 的 1340024 字节
及 SHA256 `2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed`
已在恢复后从磁盘复核：304 bits、454 steps。
不要重做这条群链、两条 CM304/454 或共同369链。
R184 两个完整 F2 校准值仍为 2015736/4073772；仅这两个旧行有800因子。

## root 必须恢复和复算

R193 全部2处：Hurwitz beta=(a+bi+cj+dk)/2，同奇偶坐标且范数n。
非Gaussian项 L=v2(c²+d²)，a=b=0时w=20，否则当
−(a²+b²)(c²+d²)在F41非平方时w=1，其他w=0。
I2=1/4 sum Lw+20rho(n)v2(n)−120rho(n)，I2(B,B)=−80。
细Gross长度/粗C2/marked Aut4的规范必须全部保留；81060非CM项历史检查通过。
旧证明/JS/证书字节9813/4642/37461，旧SHA依次
44748a6d72b2a7b361d5f943e128ee85c24fe072631228048cfddde946bb5350、
fc5b31b03f57d7db0f24b9c4eafc9c1f8be70500dc9015b8aee137e5114d7c2d、
26c5838bfb2d8d7c5f4e7714c1394a0a1ee2604ea2614ac0f85f5d85aeb5a372。

R195 全41处：I41(B,TnB)=−40rho(n)，C4=0。tame半稳定模型每Igusa
上CM与尖点各10，PhiB=0；qST=w^41，coarse z=w+w^-1−2，j切向41²。
不能把原Q41模型上的交点误认互异；长度均用v41(41)=1。
54非47常数已算，前三T1/T2/T3为4226475/1840520/3638646。
旧证明/JS/证书9503/5666/19266字节，SHA依次
47358b62f4e58fd854ffb60b2af55e174b4ec30bd1fe6f36791fc3b82021229c、
ce3339041c7bfae138acf20d71298922b7d8da7eba804ee9a0362cb72e9adfdf、
56f7b52bf45ba985af2f8b8b2921a61efe205a39598a7188c26d8923f1456ef4。

CM4/cusp全Norm代码需重写再核。CM4全局H=(W'f0−Wf0')/beta，
beta=−3/27652，325×73系数及全部59860项恒等式曾通过。
有理c=e0+A1e0，z=Wc/f0−z(P)，j−1728=(31104f0(P)²/Hc(P))z+…。
20点24阶ODE和165步整Weierstrass曾通过全部73列末端理想及Frob：
CM4 prefix logU407960、negative4163683、endpoint g1224585、j/z1233186。
最终必须用log_j=logU−logg−m log(j/z)。cusp prefix logU1104782、
negative2328615、g2255295；cusp用q41切向、80次域trace/4给20次Norm。

## qc代理恢复项

R194实际eta_B：199/219交93，20CM/80尖点/54Lie共154方程。
325分子compact SHA f1be6a6ae4e9cee06e0439d49c02234926099ba7825ee0cbacabe93d072a3e87；
negative q199 SHA26c3d25651a22b75eb3b337c4a35980102ec7529077f5598a1e4a53d767dc5ae。
全部小输入纯JS曾清cache独立重放；恢复后重新核磁盘证书。
T2/T3目标与原七个目标SHA一致，trace各59860项通过；实际tiny
T1/T2/T3=890368/463561/924161 mod47^4，family1的1730352独立复现R151。
旧R136 exponential与当前R141 family0不同，不混参数。

T2 q2 SHA27561507cd042969a364443e2e8661bd56490c4132d42afe008262ead7e6be87，
N2 SHAc93e61bf9a840b4ebb323b3e1f27b75c782d2eb5f28c23cf02d54669b09220bb。
T3 q3 SHAe972ebcc901cb96d2ab8844cdef1fb7f04f98a5b9c279694223ca39c0b1f952d，
N3 SHA095023f8d04a64f4593ff6e7052a78ba3d100c1660b6b0fe8374151094c535ed。
q2/q3全部40CM简单零，T2残数CM4=1/CM16=2，T3 CM36=2。

CM16 prefix NormU4362018/log513569、negative237986/log4296928、
g2817178/log3475650；4非单位盘0,3,15,18、max e2，另一有理参数
e1+A1e1重跑20点逐项同值。CM36 prefix NormU666144/log446970、
negative1563080/log4746248、g1102372/log1846865，6非单位盘，max e2。
原源码历史SHA CM16为8f3359df6d5531027ecf6da432a6a544ad3e1dbb707f62838e0ecb16c1348ac5；
CM36为034185d4390096b4cc5bb19fa3d42a85cbfff4deb3713d065b40a94830a16ffa。
恢复后优先直接读完整454，得到四种全Norm。

m mod47^4=459340，逆4074216，真实前三高度无800：
h1=(890368+logfB[Z4]_j−logfB[D]_q41)/m−4226475；
h2=(463561+logfB[Z4]_j+2logfB[Z16]−3logfB[D]_q41)/m−1840520；
h3=(924161+2logfB[Z36]−4logfB[D]_q41)/m−3638646。
尚未读取完整Norm前，R197不能称完成高度。

R199一般CM周期：T_nZ1=rho(n)Z1+2sum_{f|n,f>1}rho(n/f)Z_f；
Of项链用[fi]，不把i当f>1阶的整自同构。C4Z1=2Z2+2Z4。
54行共55导子、25960不重计支撑，(n,47)=1全部在同一未分歧Q47²。
976个n≤1000递推/度数式已核。R203正在核Hecke等变Lie规范：
直接M_T乘原框架gradient与实际T2/T3 eta有54个单位误差，不能省dlog运输。

## cm/lit代理恢复项

R191：degree42实子域principalization、eta rayfield、43处显式Hensel分裂。
R196：actual/reference WW差−i(kappap+2kappaq)，primal另有−ell_cyc；
真正Norm域导子p²q。R198：同q 79464次psi11、44 Robert Norm比值1、
tame[5]闭合；真正纯p见证Xp=u2，N(u2)=u0，ep,q=28K，贡献13b=−13epsilon。
R189有一个form-feed排版错误v_beta=\\f rac4，恢复时修为4/(beta x²+1)。

R200：全S固定、完整Kummer-zero规范dq=0；min D/p²在q可杀净且
剩余gauge唯一。Sha1_S(W)=0给Sha2_S(W1)=0，正确类型不可颠倒。
BCH的W→eta不反馈当前Omega2；全局mu_p² cup使cyclotomic项精确抵消：
Omega2=<wq,ep,q+eq,q>=epsilon(13+11v)。R198 ep的gauge稳定由
kappap|G_Kq=0保证。旧冻结证明19373B SHA
204cde40a47be4ba0917270d0f06ba221cadb140a02a080ca58c414d22306e33。

R201：Cl_S(F Lq)[43]的W部零（Γ-invariant character、HS两端消失、
p strict/q finite及lambda16）；χ-adic清S外divisor、有限逼近并除base p根，
普通S-unit exact Norm解存在。实际ωhat=(352,197)mod1849，high/low权差
power logs=(0,3)，回low V需ζ^6。若同C44/τ投影并S支持校正的V Norm
primitive指数t，v=2t−12，L=21t，故Omega2=epsilon(10−L)，零恰L10(t23)。
**L未算，不能拿R189 primal数值10冒认。** R202只留真正L求值。
lit核普通Norm见证的S外修正可降到base44次F的理想Artin；仍需真见证。
cm尝试固定{2,p}非交换governing field的二阶Frob坐标；尚未证明它决定L。

## 后续操作

各代理仅恢复独立/tmp；root写tracked、核新SHA、登记结果并正常commit/push。
原历史SHA若未逐字恢复，不强行冒认相同，改记新源码SHA和同一数学值的重放证据。
恢复一项就及时写HANDOFF、结果与log；不以环境故障或阶段性成果结束主目标。

## 第二次恢复：2026-11-12 22:16–22:23 UTC

再次确认/tmp与store全失，工作树保留。R193/R195已直接重写、真实Node完整执行，旧暂存SHA不再作为当前文件声明；完整清单见2026-11-13-restored-local-heights-and-b-norms-manifest.json。四类完整B范数亦全部再跑并直接写scripts/data，CM4/16/36/尖点最终log为2452507/1668829/5546/571990。R191/R196已真实重跑，根全文读证明通过；新文件清单见2026-11-13-second-recovery-agent-manifest.json。R194 tiny文件、R198–201/R204新稿继续恢复，L和主要目标未解决。

## 第二恢复批的实际落盘与复核（22:33 UTC 后）

R194/R197/R199/R203及R198/R200/R201/R204全部已真实落盘；根逐件完整阅读证明与辅助notes。R194加入由93维交空间推出有效gcd为零的RR论证。三tiny、完整四类范数和R195相同规范总装后，根独立重跑装配器得到首三高度3623418/2463646/4692386及同一证书SHA7c8da4e5275bb69d35ee36e904c798ab04e07b7775820ccf524a7bca84995392。原未推恢复任务已逐项关闭；新源码/证书SHA以两份第二批manifest为准，不追认旧丢失字节。R204正Artin与τ下降已有独立审计；实际L、剩51高度、完整QC及绝对一致性仍开。
