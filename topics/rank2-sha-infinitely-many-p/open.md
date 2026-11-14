# 未解决的问题

固定一条 $E/\mathbb Q$，证明代数秩至少二且对无穷多个 $p$，
$\Sha(E/\mathbb Q)[p^\infty]$ 有限。**主目标未完成。**
全文证明和旧支线的准确边界保存在 [results.md](results.md)，本文件保留当前接口与未付条件。

## O1. 固定曲线的秩证书：已完成

首选固定曲线为
$$
E=E_{17}:y^2=x^3-17x,\qquad P=(-1,4),\quad Q=(9,24).
$$
R4的完整二次同源下降给精确秩二、挠子 $C_2$，并证明两点独立。
R239的E136:y²=x³−136x、R294的新j0曲线y²=x³+17均精确rank2。新曲线的R288三次CM覆盖、R290/297原Schwartz、R295完整普通中央桥及R301惰性解析半因子均已付。R302已付原E1 degree2参考、六点常数1/6与CM全权平方；R303完整惰性Selmer比较已付，仍缺无穷中央非零。

## O2. 普通中心非零：准确充要条件已证，无穷性未证

R3的cyclotomic二次系数非零是无条件充分条件。
当前更精确的主接口为R40/R51：对普通目标素数 $p\ge13,p\ne17$，
$$
\Sha(E/\mathbb Q)[p^\infty]\text{有限}
\iff[T^2]F_p^-(T)\ne0\iff J_p'(0)\ne0.
\tag{O2.1}
$$
这里使用完整Selmer主项、实际Katz分支及已证反对称MW高度非退化；
没有附加cyclotomic regulator假设。
若额外Sha自由余秩为 $r_p$，则 $r_p$ 偶、$\operatorname{ord}F_p^-\ge2+r_p$。
分支非恒零或复临界值非零不计算中心零阶。

旧四次CM的原截面A、57800平方常数、全部规范，以及R55/56/57/60的整Newton、Hurwitz和参考证书完整保存在[本轮原open检查点](notes/2026-11-14-open-through-r412.md)的O2。其准确有限判据仍是某个n有v_p(((p−1)p^n)!b_((p−1)p^n))<2n+2；逐p完备证书不保证跨p命中。R270/274/275保前三权与共同取消，R277保原log及全部边界；真norm2/P0比较和无穷命中仍开。

### 新 j=0 固定曲线的普通接口（R295）

R332–396的原负矩/Soulé、Faber/Hirota/AS、norm2/3、三aux与移动权、432/12球核心及全部准确系数保[本轮完整open](notes/2026-11-14-open-before-r541.md)。**仍待做：** R364两个指定完整Laurent行的联合非零；R353非恒定Y权的合法中央控制；R376/396同一个完整组合的中央补域（保所有tame和尺度log）；R339虽每个p/任意深度有原非零子域，仍须由原中央零合法传播或控制补集，移动负权不能按固定有限池作鸽笼。R336两条指定行保全部h中项，不得只选已知单位端点；R332同CM型Katz对偶不交换普通地点。

对 $E^{(0)}:y^2=x^3+17$、$p>7,p\equiv1\pmod3$，同一实际
$S=\sigma^{34}x^2P_4(x^3)=\sum s_mz^m$ 给整测度及单位 Mellin 函数 $G_p$。
完整周期和 Euler 因子给
$\mathcal K_p=48940416(1-\omega)\Omega_p(1+T)^{-a_{34,p}}G_p^2$；
通常 Selmer 的比较保留全部 Sha，给 $2+r_p\le2\operatorname{ord}_0G_p$。
所以 $G_p'(0)\ne0$ 足以初级有限，且准确等价某个 $n\ge0$ 有
$v_p(m_n!s_{m_n})<2n+2$，$m_n=(p-1)p^n$。
原 $s_{12}=-988\cdot17/105$ 已给 $p=13$ 的有限证书；**待证无穷不同 $p$ 命中**。
R300 已由完整34维迹、CM13单重线及整性支付真正p-core，给全部tame/环带；待证同一原中央导数的无穷非零。

R487 原全CM移动支与参考非零环带差均保[完整接口](notes/2026-11-14-open-before-r527.md)。**待做：** 消全部Δ_n和216条真实管差；保高13/19覆盖、未知参考导数/质量，近相消不交不赋零。


R490 已付C26的CM差、JC′非零及真实H5伴随，第二边际JB′+JS′是固定非零log。**待做：** 保混Aunit和反卷积A/D实际移动，将辅助非齐次行接原S；不把B当合格曲线。全公式保[原完整接口](notes/2026-11-14-open-before-r527.md)。

R476/477/480/482/484 的八维完整桥、Λ612逆、六格CM标签、H51整moment与4080态全lift条件保[最新完整open归档](notes/2026-11-14-open-before-r490.md)。仍须原条件域的实际转置，Href的Jref′B(h)+(1+λ)B(∂h)、所有外谱和移动管均未删；来源张满与有限核心不自动赋中央零。

R494 已付wholeB56绝对核心及原三态KB=RKW R、KQ=−χKB、KU=−KWKB。原M的W/Q/U各自任意深度和R共同深度全部闭合，u/v只依nW+nQ奇偶交换，精确标量χ^(nQ+r)λ^(nW+nQ+nU+3r)；所有第一Y移动式与单B/A²-W-A²的λ^-4像格比较保正文。**待做：** 将R493保持Y的真实六sigma几何与这些完整矩形接合，控制非齐次参考差的实际补域，不能把来源核心词相同当域相同。

R492 已付原二Theta全principal=H3⊗C3+S⊗Λ+H5⊗CS，JC3′非零、JCS′=−JS′。**待做：** 同一完整域的反对称积分无穷非零或合法消回S；混Aunit非独立乘积测试。全Mellin/环带/系数保[原完整接口](notes/2026-11-14-open-before-r527.md)。

R493–523完整五伴随、原词域、四态/CM核心、几何18阶与来源96阶、隐藏轴及正测试的全部当前接口见[本轮完整open](notes/2026-11-14-open-before-r533.md)。**仍待做：** 原Y/旧W的完整联合补域、固定B0、全部Href参考质量/导数、C4八层和E*三输入的真实词交域。必须保同ray/固定坏集/大p门、Tc/E/K/Q0/Qb各隐藏项、κ尺度与所有逆权；不能从边际零、有限轨道或共同核心推出受限联合零。R515/523原sigma carry、R518有限Eunit逆、R519真实三条单位线、R520共同三深矩形继续按原文使用。

## O3. 固定级数的prime diagonal：两个方向的实际对象

R409给原S34/T72共同sigma有理递推，准确读取a_p^N=[z^(p+1)]A_N modp；共同好惰性p上任一个非零即初级有限。到10000的614个共同好p无联合零仅为有限证书。**待证：** 无穷p的两个指定对角不同时为零；首层同零不等价完整中央失败。

旧四次CM的两条准确对角、完整固定F/H/Theta/P/B/W定义与权阶梯同余保[本轮完整open](notes/2026-11-14-open-before-r542.md)的O3：普通R55是G_ord的指定系数，惰性R52是Xi的指定系数；两者都给充分判据而未付无穷命中。原Xi非D-finite和连接p曲率不排指定对角的其他有限几何模型。普通首层不同权由同一Hasse因子联系，不能当独立条件。

已排范围继续保持：theta乘积是加法卷积，log不能拆因子；同CM型Katz对偶固定原反圆点，不给J奇偶性；现有BDP/BDGR/Agboola、Romik最终同余不付本固定早期对角。R20/24/29的CLS单塔与Padé转换不能代原反圆J。有限扫描始终不作无穷性输入。

## O4. 原高秩类、完整 Heegner 点与两步门

R8给准确正合列 $0\to\mathbb Q_pv_p\to\operatorname{Sel}^0(\mathbb Q,V_pE)\to T_p\Sha\otimes\mathbb Q_p\to0$，$v_p=\log_p(Q)P-\log_p(P)Q$。
Castella实际导出类非零在本曲线等价初级有限，但归属及非零仍需独立输入；Kim/Calonge2026的前提未付。
R37/39的反对称MW块与高度代数线性独立不排cyclotomic二次regulator或strict三次式零；不可删潜在Sha方向。

### 完整原类、已联合输入与仍需通过的门

O4所有原规范、16个域、82个CM中心、完整Hilbert类迹、carry及局部/全局区别完整保存在[O4检查点](notes/2026-11-14-open-r475-r477.md)的同名部分；下列问题均仍开放，不因压缩正文而关闭。

R119/R149–156在同一无穷普通/nonanomalous素数集已付原Q非扭、范数零、hQ=o(p)、非p除、辅助aell单位及源简单；真实O格Q=δ^aεw，E17与E389均已证a≤1足以原Sha[p∞]为零。E17保a偶；E389保lengthShaA=2(a+1)。**仍须证明同一原类的a≤1或等价低增广项非零**，高度、非p除、源简单及环境函数非零均不能替代。

R232/R234/R237原两矩、两类observer及完整definite群环保同一个原ell与全类群迹；所有p完成上的两矩非零等价a≤1，原β(Q)=f(0)P_-仍待非零。反圆四阶/导出高度note的第二高度必须控制整个S+并匹配原λ，局部Kummer或Heisenberg平方中心零不够。

R130/R134–148的全p完成、真实Frobenius规范及SL2/PSL2轨道保原D2观察；原D2失败等价C=D/n²在指定CM点正则，须控制指定纤维而非别处极点。p不除类数、单点稠密或总迹零不迫所需类群和。R154原固定商覆盖次数ell(ell−1)，R157双反射失败同步，未增加独立测试。

R271/R281/R285最大阶真实Θ1低于I³的条件已通过完整Selmer接到Sha；R296原88类和R304 conductor完整Euler下降均付。**待做：** 指定p类不落pCl，以及变化q的全Hilbert trace在同一无穷输入上低项非零。有限p11/13/17证书和提高恢复精度都不解决这一步；高Kolyvagin节点原始性不能直接降到所需两层。

## O5. 强声称来源审计：此支线已完成

R240另排除已发表polyquadratic plectic的具体输入：有理rank≥2使平凡特征minus投影为零，且其系数p限于固定曲线有限个乘法坏位。其他更高导数或新类不在此结论内。

R5对arXiv:1703.02215的统一有限lifting中间引理给完整计数反证。
它不能充当主题证明；否定该论证也不是主问题的否定答案。继续其他开放分支。

### 原两标量、全局平方迹及循环能量

R161原canonical-Frob差除p给完整整提升；保全部完成的两个有理矩I1/I2同时零 iff 整个原D2行零，不需源简单。R164真实δ除法保N项，半层内自动深度仅一层p；原像高度成本不能删。
R165的GKZ含完整NΓ/Fricke条件，heart界只限线性映射；R168高度级数有同一原标量未知量。R172/R225完整能量和Gram整恢复任意k=a+kS，前两量非零 iff k≤2；局部kS−1不计入ShaA。仍须无穷输入上的早期非零，不重做有限恢复。全部准确公式与证明保存在对应结果。

固定E24由R398证精确rank2及Sha[7∞]有限；实际T72=S34H38、H38质量1。R401给κ24=1/(6∛3)，R397/R400普通全core/通常Selmer和R402惰性全桥均已付；首项一常数10534551552。**待做：** 同一无限集合上两真实中央至少一条非零。R399在固定ray mod279072给四源交叉与Y/Z重叠全core，保两移动单位管det−395；同时失败迫原B_N导数v≥6N及全部负矩尾。仍须控制其完整补集，不能从交叠或深整性直接收尾。

## O6. 中心相对类群与全局单位：准确核尚缺跨p上界

对目标split p，R7/R12给
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)=2\lceil c_p/2\rceil,
\quad c_p=r_\pi(E),\quad c_p\in\{1,2\}\iff\Sha[p^\infty]=0.
$$
固定四次去扭转后的目标是非平凡角色；秩零基本曲线仅控制平凡角色。
范数、非Wieferich已知点或全局单位指数素于p都没有给目标局部上界。

R30–R35令 $D_p=\mathcal A_p/(T-p)$，得到更适合本题的准确等价
$$
s_{\infty,p}=q_p+1,\quad q_p=\operatorname{rank}D_p\text{为正奇数},\quad
\Sha[p^\infty]\text{有限}\iff q_p=1.
$$
固定两点给饱和满射 $\lambda_p:D_p\twoheadrightarrow\mathbb Z_p$，核 $N_p$ 保全部Sha方向。Bley–BKS已付完整Fitting中心理想及真实辅助类，每层商为 $D_p/p^nD_p$；仍须证明 $N_p$ 对无穷p有限。

R36的两条整Bockstein行为 $p^{b_p}\mathcal L/\theta$ 和 $v_w/\theta$，
$\theta=T-p$、$b_p=\min(v_p\log P,v_p\log Q)-1$。
p13辅助109的精确非零3已复算。继续除一次中心需要整S单位格上的原始关系，
外积中心为零不自动给这条关系。[整单位记录](notes/2026-11-13-o6-integral-unit-division-and-one-prime-mrs-descent.md)已自证一次全局除法；[CM5记录](notes/2026-11-13-original-unit-cm5-norm-and-translated-centres.md)付D_a=VθC_e及全部Smith商。R286准确识别Tor为θC_w∩C_w[θ]；若原λ杀A[θ]，真实dual-number变形给统一p^C z_n/θ²全局相容。该条件等价λ避开长度1块，坏q≥3及MW高度并不自动支付。R293已付非零socle的真实主化、两因子有界Tor及ε=u(z/θ)∧s；全中心理想损p^d而特定两行损p^(2d)，余下为原单位评价非零。

### 现成单位或增长界的准确边界

完整Coleman范数相容及逐p的 $\mu=0$ 不控制 $\lambda\le3$；固定单位的目标角色仍含移动端点。Cartier、定量深度与人为中心因子均未控制原始生成元，准确范围见results。

Knospe/细Selmer结果未控制原中心核；真实反共轭四次角色不从Q下降。proper系统长度n需要模p^ceil(log_p(n+1))的塔数据，准确范围见results。

## O7. 惰性中央权与真实解析半因子：正在推进

旧四次CM的原惰性signed参考、Kato混合比较、两阶乘/非单位Euler抵消、全部中央Newton与完整尾界，原文完整保存在[本轮open检查点](notes/2026-11-14-open-through-r412.md)的O7和[原中央证书背景](notes/2026-11-13-open-theta-background.md)。准确接口仍为2≤s_p≤ord A_p、ord A_p=2ord J_p，原J′非零足够初级有限；不把另一tame支的统一单位当原中央，逐p完备证书仍须无穷命中。新j0两曲线的真实惰性全桥见R303/R402，完整基准与高轴见下文O8。

## O8. 固定有限候选、惰性原格及新的算术代数化

截至R495的本节所有原问题、常数、来源预算和未付条件完整保存在[本次open检查点](notes/2026-11-14-open-before-r496.md#o8-固定有限候选或新的算术代数化)，均未关闭。以下保当前接续口；原quartic、O4/O6、R364以及普通补域继续按该检查点顺序推进。

R418/473三原j0来源的函数域、规范化、权10980整conductor和固定Amice零阶已付。来源代数维仍二，完整中央零对同一评价映射的严格门aI+2bI<3（或aI3+3bI3<3）尚未付；乘子/规范化列没有自动中央零。真实全D/q及所有13+r_c carry、p饱和与全局范数成本保留。

R468–511 的完整来源预算、所有常数、旧结论及尚未支付的逐项接口完整保存在[本轮open归档](notes/2026-11-14-open-before-r540.md#o8-固定有限候选惰性原格及新的算术代数化)，均未关闭。当前共用接口是同一真实F/Q/t/g、十九角和原M=c*U0m13J，不从环境秩、单个尾项或不相容的修正推出原非零。

原M首提升仍是JbarR+J(P0)/p=w^(s−13)(B0+εB1)，B0/B1须同一R并保26行；R481原p³规范形保低ell缺行、两次s移位及高尾。R485/486两个真实同预算连接项都保；混权primitive第三核不能逐权拆掉。R489/491整cube基准首双jet类恒零，不删真实forcing。

R495已付χ=−KC≥2b、κ=C²≥2b−2、H1(mC)=0及整个3C同预算返回。R498原低ell首像是Iη=(t^(s−r),t^max(ell−r,0)(ζ−η)²)，真左行仍须KX|3C及全部原列条件。R502真Bockstein保rawζ³、实际ξ、活V1/C混合、Gaussian/t-w和低行高尾；完整p239证书已公开恢复成功，不复跑。

R505的ξ=3Tβcont(F)，接触余核对偶H0(C,KX|C(qP))、q=h−k；q<χ才可按已付同预算格吸收。R507全Γ算子P=B N(6N−1)及forcing psa保唯一ε行sp，但P(imJ)⊂imJ尚未证。R511实际ξ=(3/4)T2βmir(F²)，镜消失等价βcont落真实∂η像，源H0(C,N²(−hP))须真实提升除2eη；h<κ+χ不使该边界满射。**待做：** 原特定forcing/ξ在全部同源连接和原M低尾/carry上的实际余类，及同一修正d2→G2；R543/545/547按自己的真实返回推进，不自动关闭这些接口。

R514/517 的完整固定3/2charge返回、十九角/ambient门、原Γ转置和r缓冲条件保[本轮归档](notes/2026-11-14-open-before-r544.md)。R543/545/547只按各自实际预算扩展，FH2从未等于全J。R521固定边界长3c(u+4b)与显示forcing残数b²m(4t0−1)仍须杀真正res H0(3C,IηLc)和全部原列。R524真边界核的三层及两条连接α/β保持同源，第一层负度不能删另外两层。**待做：** 原二次临界候选的完整联合边界像、forcing与同一R/carry；不能把边界非零、局部Taylor清极或容量算作原jet非零。R550正沿实际(F,e)H2交概形继续。

R522 已付共同H0的整个三度偶张量；H0unit正六次测试保其余五输出全部联合，同时还原原S/两T且被T和旧W核原样保留。原五深网格测试质量整条0，Y中央v5n无需新ray，两个T归一局部差也v5n。**待做：** 在这同一个测试下控制原三条完整补域及第一Y移动；H1unit可加，不能把全域两T相等与非零子域差当矛盾。

R527 H0/B六次逆和四输出联合、A深完整逆域/三处移权、中央与非零质量v5n保[完整接口](notes/2026-11-14-open-before-r529.md)。**待做：** 原S/T不同unit管的补域；保七质量项、四R及固定大p门。

R526原低轴PlogTheta=2t/3、T≤2Δ+1有理接触界和单/两权核排除保[此前完整接口](notes/2026-11-14-open-before-r525.md)。多权已由R525推进；完整M/后两块/固定conductor未删。

R528 D14三轨道正测试保π3，原子管差/质量v5n；与R522差给真正同域混合零行。全log矩/固定坏集保[完整接口](notes/2026-11-14-open-before-r529.md)。**待做：** 隐藏纤维补偿与原观察核；D_n不是π3事件。

R525已付原有限低轴的全次数resultant零估计及真实多权Wronskian门H≤C+E+q[2k(3C+E)+2q+1]。二次临界非零核至少常数N^(1/3)权；低ell时至少((17/147)^(1/6)−o1)p^(1/6)，primitive p²/p³约化同受限。**待做：** 与原三层连接/forcing及全部carry联立，或加强到允许的O(N)支持；当前支持发散本身不排原核，也不赋中央非零。

R529已付J/K whole6、E whole9 β及Kunit六次逆；任意J深返回整个(J,Y,ξ2,d0)和原S。原五深小管v5n、质量整条0，同域W−6δY差v5n+3，无新ray/大p门。**待做：** 保W的K/E项，将原T行的Kdeep1及P0−P_K两补偿与完整carry补域联立；不把四输出身份冒称S/T共同返回。

R530已付来源/全目标两端p除连接的整共轭与同一p²左右提升的完整混权和，保所有Gauss/高尾/wrap；统一移位可逆及有限精度小整数代表已付。**待做：** 原实际配对与C2，不由源可逆代像饱和；严格限同一B或conductor·B矩阵，裸Q保A未证。R534已用P/VP双接触支付跨s精度；不能把ODE自身延长。

R531已付两套纯伴随框架C/F与D/E、wholeβ和实际Γn carry；Qhat_n逐次数逆返回整个(Y,W,W′,G)，原Y/W不移。原D_n三中央/质量及两差均v=n，完整五项质量和所有log保留。**待做：** 控制同一Γn内的真实纤维补偿，并用真正改变Y的原操作接完整中央；D_n不是所保π4的事件，不能丢补集。

R532已付原J/A5完整六轴框架及whole核心；真实二维来源准确是两个原整张量之和、秩二，混合矩/原Y系数完整给出。Kunit逆返回(J,A5,B2,C30)，原五深网格的六条件精确重写。**待做：** 用同一完整张量与原W的全部六系数联立实际补域；两个边际都零不等于联合源零，旧W隐藏项不能删。

R534已付P、VP同时消至T≤3s的全参数零估计，原三Gaussian行的真实Wronskian法向误差完整计入。首核支持界左端2(s−d)+ell，primitive p²/p³约化由真实m_d的0/1 Smith去掉2d损失，左端准确2s+ell；二次临界支持≥((3/7)^(1/3)−o1)N^(1/3)，低ell≥((68/147)^(1/6)−o1)p^(1/6)。**待做：** 原允许O(N)支持的核与两真实α/β连接、原forcing及同一整修正；支持发散不等于核不存在，不新增来源中央零。

R535已把原三sigma准确写成Norm3 Fourier框架中的完整Hesse五项，付清相位/全部theta型及整来源；E深/Kunit/R3deep五输出四项核和原D_n全部高阶中央式全显式。**待做：** 在这个同一来源中找真正混Y的完整关系；旧W的E系数非零，须用未忘E的五项测度及真实log/单位域，七个低矩不足。原补域未消。

原Fermat商移位族的范围已在[整谱投影与核方程说明](notes/2026-11-14-fermat-shifts-and-kernel-syzygy-boundary.md)证明：它恰生成canonical j对角算子，全部完整配对是Cα=M Qα−F*α M的核方程组合。**待做：** 计算尚未完成的原候选/实际提升或支付核像稳定；仅增加α/有限差分不新增独立Smith条件。

R536真实七行十列纤维补偿由显示整右逆支付全部λ/κ；删正文固定D_*有限坏集后，同一Γ/π4返回原source，原D_n严格零质量/logx而中央及两差均v=n。三个不交carry平均成T不变测试，旧W核保持，T D_n为原h的非零Wdeep子管。**待做：** 控制真实Wcore后Y+(κn−1)(37−3δ)W/72权及全部原单位/输入补域；不能把这项去掉后调用原S零。

R538未改P_K的E深/Kunit整条四输出返回已付，系数βn(8+20κ3n−κ6n)/27；配真实J/B2/C30深和Y_r给同一原S完整行，外域可留在三伴随深内。N分量在±近相消镜管的完整积分准确相消（各v5n）。**待做：** 余A5深及J/κr+K深条件、L/M完整分量和W→W−2(1/3−δ)K真实移权；不能把一个分量的配对认成整个ρ的补域消失。

[三层乘积与分歧成本笔记](notes/2026-11-14-deep-three-layer-product-and-ramification-cost.md)已保实际残项：A⊗B=C不构造同格修正；局部Taylor校正需(EF)²清极而升5C，原3C预算不足。k=0/1的局部Cartier改写仍保全局α/β，不以该改写关闭原forcing。

## 保持的完成标准

有限多个p、未证明的高度或消失阶假设、未核实新稿及数值证据均不算完成。
固定曲线与无穷素数两个量词不变；这里只需初级有限，全Sha有限另需有限素数支撑。
子问题完成后继续本文件的下一个未付条件，不以阶段报告等待确认。

旧R246/R251/R253–256的完整剩余接口保存在[证明与接口索引](notes/PROOF-INDEX.md#原norm2与固定对数的剩余接口)，原条件未删除。

### R533：固定负矩的实际双单位来源

原两degree6核和四条I−2(f4)/I−5(f1)接口、显示非可迭代纤维见[R533](results/R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)及[完整本轮open](notes/2026-11-14-open-before-r546.md)。**待做：** 真双unit负矩与原S/T全部补域、完整算术分支的比较；不从条件矩迭代或U边际零删K³纤维。R540完成时按其真实有限角色及普通地点继续。

### R539：原混Y两态与放大域

完整K8两态、原q_n保持、偶深m的逆权同行及Dn中央v=n−m保[R539](results/R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)和[本轮归档](notes/2026-11-14-open-before-r550.md)。**待做：** 保原Y_m/W_m所有单位补域与M转置；R541支付奇深逆权，R544已推进至真正S3和唯一余域，均未赋未移动第二态中央零。

原J反射尝试的完整来源界见[2026-11-14-j-reflection-three-dimensional-cm-boundary.md](notes/2026-11-14-j-reflection-three-dimensional-cm-boundary.md)：N7³特征ω与原三算术线的−1不同，三个投影全零，不能赋它中央零。R538真实A5/近相消条件仍开，继续f4完整有限角色和原补域比较。

R533两固定负矩的第一层现有[准确递推与有限记录](notes/2026-11-14-degree6-negative-moment-first-layer.md)。**待做：** 指定AS/ABS对角的无穷非零或完整算术比较；有限147点及p61的首层零都不决定实际负矩非零。

### R537：原切向来源核

完整条件和旧接口保[本次归档](notes/2026-11-14-open-before-r545.md)及[R537](results/R537-actual-tangent-kernel-inseparable-degree-and-source-saturation.md)。来源核/饱和已付；其物理问题由R543、R545逐步推进，原全部同D/charge、十九角和forcing条件不删除。

### R541：真正第二态与三支实际补域

原八度第二态准确为−G_*ρ0=R_*ρ0+ω²H_*ρ0，全部矩阵、四个原sigma及三支cut保留。任意奇偶L/M深用真实逆权/逆测试返回原S/T；一层深两观察有共同单位域，其差为显示log比。第三η支给原degree136截面，另外两支仍需degree544，不免费赋其中央零。完整见[R541](results/R541-original-degree8-second-state-and-exact-sigma-transport.md)。**待做：** 公共深域与G/R/H三支转置补域的实际比较，及η的完整CM投影在同一cut中的作用；R/G两支、所有C/F/G隐藏条件和逆尺度必须同时保留。

### R543：实际切向jet核的小余量

两个准确线束、K_+=κ+μd1²+μd2²、T_J=s−r−1/T_M=s−r−14及Clifford界保[R543](results/R543-actual-tangent-jet-kernel-small-remainders-and-unit-smith-block.md)和[完整归档](notes/2026-11-14-open-before-r546.md)。R545的新连接另付有效极平衡和整单位块，并未改变原切向算子。**待做：** forcing对全部真实边界核及其余原列的配对，保ξ/V1、同一d2/G2及低尾。

### R542：第三支原S/E2312投影与全外谱

R541第三η支的全部23坐标给N7^9Fη=Fη+S(2z)，原S投影−1/2、E2312投影26(1−δ)/3；D33两块循环10/8、共同18维，四rank0参考和12外谱全部保持。真实Y边际有完整非齐次普通核Kη=−η−S及任意深度返回，全部tame/尺度/质量已付；同cut联合运输仍开。见[R542](results/R542-original-third-sigma-arithmetic-projections-and-affine-core.md)。**待做：** 按R541三支真实域执行这些CM投影；保四参考的未知中央与十二外谱、[2]逆尺度log质量、[4]的G/R两支。边际核心不得提升为整六输入几何身份。

### R545：平衡后的真实物理单位块

同一实际因子可取整数c平衡两边界，完整多项式连接保全部零阶/Euler项、十九角及固定两charge返回；准确有效极次数降为κ。原低ell强窗给核〈d^(2c),d^cF,F²〉、2κ+χ−2个真实单位Smith因子及全精度整Schur消元，原M十三/二十六carry保持；余下forcing与原中央未赋非零。见[R545：原角平衡连接与完整物理单位块](results/R545-angular-balanced-connection-and-full-physical-unit-block.md)。**待做：** 在同一个整Schur余矩阵上计算实际forcing/ξ、活V1及同一修正d2/G2；固定两charge须在原预算内或真实扩大。R547继续原垂直零新增charge块及两块的实际交，不由单位块大小推出完整原矩阵满秩。

### R546：η的完整五伴随行已付

原LH整数框架与全部半特征支付第三η支的完整CM13/19转移，三固定投影分离成S2/new/Href乘完整五伴随；质量−1/2、26(1−δ)/3、−1/(1008b)均单位。两原零中央控制任意独立五伴随测试，共同深核心与参考非零环带差全付；混合W/L及全部CM分支、参考/外谱仍保留。见[R546：第三sigma支的完整五伴随CM转移](results/R546-original-third-sigma-full-five-companion-cm-transfer.md)。**待做：** 把R544实际η测试差和唯一余域按每条CM支转置到这些行；C/F/G测试独立于Y可用，但W/L混合条件不能删或当独立伴随。完整卷积单位不允许免费穿过cut，参考未知导数和外谱仍保持。

### R540：原固定负二矩的完整算术点

原f4/f1的实际有限角色ξ、导子(6)、二/三处完整环面及Schwartz、Hermite/周期和全权平方已付；固定负二矩准确读取36c4·17^(3/2)Ωp I−2²的primitive Katz值。真实复反射ξ^-1ψ0³根数−1，与f1正一次的ξψ0³不同；全部普通Euler和同CM-type对偶保持，负矩非消失仍未付。见[R540：原六度完整Schwartz与负二Katz点](results/R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)。**待做：** 同一原普通地点的ν_−值在无穷p非零，或真实非齐次/椭圆单位比较后与R533两单位域及完整S/T补域联立。不能从根数−1、正一次非零或147点首层证据推这个负点；常数c4若用单位性须另删其固定有限支撑。

### R547：同预算单位块与真实cube余列

原W_F(H)=F EH−2(EF)H在同一H3内零新增charge；T_J=s−r/T_M=s−r−13的强窗给2κ+χ个单位，且其像与全部ξ高epsilon尾交零。联原F²H1在q=T−h>κ时有(5κ+3χ)/2个单位，显示子格只剩原F³一条非单位来源；原其余列、全forcing/carry及与R545两像的联合交仍保留。见[R547：零charge垂直单位块与原cube单列余项](results/R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)。**待做：** 同一Schur余矩阵中完整R502四项、原其余W_D列及R524连接的实际像；原ξ为[3eξ]∈coker E_q，单项不代完整类。R550继续(F,e)H2理想块与真交概形/镜接触，禁止把R545与垂直块单位数直接相加。

### R544：同一两态的实际S3与唯一余域

原第三η支与ρ0在带ω²的H及输入反射下成完整S3，三个旋转框架的whole核、逐步归一词域和六步混Y返回全付。Lunit精确拆成三不交环带与唯一全单位余域，原S/T双零接到一个明确η测试差；同一L-odd六输入有负矩单位，但原补域、混合权和外谱全部保留。见[R544：原S3两态与三个真实环带补偿](results/R544-original-s3-and-exact-mixed-unit-complement.md)。**待做：** R548按R546完整CM分支联立η(Φ1−Φ2)、ρ0(Φ1−Φ0)与原V余域；保公共Uκ的log比，不能用source群关系删真实物理缩放、q∘A^-1或混合单位条件。L-odd负矩仍须合法接完整中央。

### R550：整个H3的真实分歧像与forcing有限商

同预算(F,e)H2的Koszul商是长κ的真实交概形Z，整个H3物理首核在Z的像准确为ev_Z(kerβ)，且ev_Z在N³(−TP)上单射；理想块核为F Kmir，两条原连接保持。完整清极forcing用乘积厚化长κ+9d∞保固定边界重叠，局部分歧单位不代原全像非零。见[R550：原H3首核在分歧商的真实像](results/R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)。**待做：** 原特定forcing/ξ是否满足res_Z kerβ与res真实三层核的完整相容，并与R547 cube列、R545和原全部W_D列联立；H3→Z已满射不能把该商再当额外独立障碍。R552沿同一原M的T=s−r−13和全部carry继续。
