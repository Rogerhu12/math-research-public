# R582 同付费尾口的真实 s-ODE 核心射击实现

日期：2026-11-26。新的计算范围，尚未科学执行。承接 run45805053770/job139857971246 的完整自然终态，从该次实际控制 mu=-.04、nu=-.04893431917441107 出发，不复算三次尾种子，也不重走24/48/96基拟合。

## 完整输入和目标

source-state 是72341 B的小配置，SHA256 76db383642af7d0fa12d2ee277c08787eef243867afb9de3afa03d9d1778b22e。它保原circle81q的完整身份、三份已付种子的小输入原文与摘要、最后两个均值控制、1214个actual几何节点及2413个完整fine节点。三份原尾种子的六jets未重算；原控制返回的0.4446435769999937 s与更早尾种子114.013392 s子进程墙钟分别保留，不合并成一个伪精确时钟。

此次直接解
\[
A_s=-3a_sA/a-4z_sC/a,\qquad
C_s=3a_s^2A/(az_s)+4a_sC/a,
\]
从同一s=.82实际口到s=.036核心。方程从不除a_s。目标是C_core/A_core=0且A_core非零，随后以lambda=.5/A_core统一归一整个场和全部jets。

外层SLSQP采用有界射影目标
\[
\tfrac12(C_{\rm core}/\sqrt{A_{\rm core}^2+C_{\rm core}^2})^2.
\]
在A_core非零的合格图中，它和C_core/A_core具有同一零集；实际接受与最终目标仍读取后者，不因使用有界目标而把A=0当成根。若A相对场范数不足1e-12，core_C_over_A记null且不接受。

初始nu子盒为原值±.001；只有自然求解停在该子盒边界、尚未达到根时，才按明确的新需要尝试扩大两倍，最多±.008。每次扩大都先重新证明整子盒的连续正性，未证范围不用于带除法ODE。mu从原值在±.04内可变，mu不改变z_s。所有控制保持支撑于(.06,.80)，故原尾口和开核心不变。

## 同一无限高度函数的两种独立用途

r582_continuous_mean_profile_20261126.py 的数学函数仍是原R566
\[
H(s)=-A\ell\int_0^{(L-s)/\ell}
\exp(-(2-\sin(\delta^{-2}))/\delta)\,d\delta .
\]
数值s-ODE使用一次固定相位分段累计，再对每个实际s作单个局部QUADPACK积分。它改变求值的复用方式，不改变H或17个原均值坐标；H_s和H_ss始终直接由原解析w公式给出。原CUT=.03只用于数值高度，遗漏界A ell CUT exp(-1/CUT)另保；任何QUADPACK非收敛消息均显式抛出并保留已付成本，不静默切片丢掉警告。

连续z_s证明另用独立的外舍入区间Riemann表。它不把QUADPACK误差估计当证明：

- 在[.03,最大delta]上，每个正被积函数的完整区间值乘该格长度，给上下积分界。优先细分贡献区间宽度最大的格；最终前缀用外舍入累加。
- [0,.03]的真积分位于[0,.03 exp(-1/.03)]，由2-sin>=1及delta exp(-1/delta)单调直接给出。无限尾没有被删掉。
- 对任意查询delta，完整已付前缀加最后一格的部分长度仍给真包含界。整s单元使用两个端点积分界与积分的单调性。
- 目标高度包络宽度1e-6、最大65536格只影响工作分配；后继正性判定使用实际输出的完整上下界，不以请求目标代替已达到宽度。

基本加减乘除每步用math.nextafter向外扩一binary64 ulp。exp端点用90位Decimal及相对1e-70、绝对1e-320的保守guard；x<-700时以上端exp(-700)包住，不依赖libm的exp舍入。sin端点用Machin公式的两个120项atan级数构造pi，90位角约化后用80项Taylor；在本入口|相位|<=1200、约化参数绝对值<4的明确范围，1e-60 guard远大于级数尾和有限十进制舍入和。整区间再用|sin'|<=1扩张。声明范围外直接拒绝，不能把不适用的guard继续当证书。

真实函数输入是源码/JSON给出的有限浮点参数、端点与结点，视为精确实数常量；归一化宽度定义为这些端点的真实实数差。区间 step、compact bump 和自由 B 样条分别以 Interval(right)-left、Interval(CONTROL_RIGHT)-CONTROL_LEFT、Interval(LENGTH)-CORE_END 包含该差，不能把预先舍入的浮点宽度当成精确宽度。clamp 使用同一精确端点，因此和内段归一化一致。数值 jets 仍使用原 binary64 宽度近似同一数学函数；正性证书使用上述真实宽度包络，数值RHS另检查当前a,z_s有限且严格正。

## 开端点、B样条及z_s连续包络

两处chi均是原expit(-1/x+1/(1-x))阶跃，使用真实左右宽度。端点不计算1/0。对0<x<=h<=.25，exp(-1/x)x^-2及其余所需正因子单调，给chi、chi_s的包含上界；右端通过x↦1-x准确反射。自由beta=4chi(1-chi)与beta_s仍用同一函数。

compact bump仍exp(4-1/t-1/(1-t))；端点导数上界可去掉<=1的exp(-1/(1-t))因子，用同一单调性，左右导数号分别保持正/负。中段直接区间计算。

P_z和P_z'通过原五次clamped B样条的de Boor递推给区间；跨结点的输入分到全部相交span再取并。导数系数为5(c_{j+1}-c_j)/(t_{j+6}-t_{j+1})，结向量只去首尾各一个，不改其身份。

最终使用真实
\[
z_s=1-\chi+\chi_s(h+H-.02-s)+\chi w
+\beta_s P_z+\beta P_{z,s}+\nu\psi_s .
\]
先覆盖整个[.036,L-.08]以及实际nu子盒，逐格自适应二分，只有每格下端都严格大于1e-6才授连续正图。原s=.82尾口包含于此范围。区间未决不是实际零点；返回其完整格描述与成本。初始小子盒未决时继续细分并缩小包含原nu的子盒，不请求用户确认。若最终仍未决，保原输入供进一步细分或 [R592](../results/R592-undivided-finite-order-crossing-and-exact-angular-bound.md) 换图；不冒充已进入合法有除法图。

## 真射击与参数导数

DOP853同时积A,C及对mu、nu的四个灵敏度分量。设矩阵为M(s;mu,nu)，则
\[
S_s=MS+M_{\rm control}(A,C)^T,\quad S(.82)=0.
\]
矩阵、两个控制导数和M_s均直接由同一a,a_s,a_ss,z_s,z_ss与psi,psi_s给出。没有空间有限差分，也没有除a_s；mu控制对a_s的导数是a_s psi+a psi_s。

基础rtol2e-11、atol2e-13、max_step=.01。当前完成/未完成的真实传递分开记录。时钟中断时保实际最后RHS位置/状态、已付RHS数和耗时，不能称为已回核心。

新的标量profile重用方式和新灵敏度公式有具体实现风险，因此只在同一正式run入口作一次原MeanProfile六jet对照、一次方向差分核；随后自动继续该run优化，没有另开验证run或等待用户批准。方向核新增两个真正核心传递，明确记费，仍是0次旧尾种子传递。

每个保留候选在实际s=.82按新ODE恢复六jets并和同一paid六jets比较。核心也输出完整六jets、原A/C、真实C/A及lambda，不能只输出一个不明归一标量。

## 几何门、网格与检查点

把原完整2413点fine网作为本次actual几何约束；新的fine加其全部中点。原MeanProfile/geometry_fields直接用于硬约束和参数Jac，保联合R=1.012、Y=.3928、tau=.06072及原球/条带/两主曲率/高度/E>=.25/det>=.1/mirror必要门。工作余量1e-4，高度行仍为0；实际接受raw细网违约<=1e-8。

完整fine发现新负余量时保其真实s，后端自然返回后采用并重新判候选资格。旧保留q不会自动继承加密网资格。只有通过新fine几何且真实|C_core/A_core|改善的候选会保留。每次完成的callback即时刷出实际control、核心读出、完整fine结果、实际/待加网、成本及源ledger。

最终在同一保留均值上，只再付一次rtol/atol缩8、max_step减半的核心ODE比较。若较细核心C/A或两读出差超过目标1e-9，就撤下“两个声明分辨率均观察到数值根”的状态。归一场在同一细观察点比较0、1、2阶ODE jet；这些由M和M_s给出，不能称为已经证明了DOP853稠密多项式的实际导数误差。

即使两次相符，也只记录数值根和误差观察；原尾口的无限cell截断与数值外传误差没有因此被认证，更没有获得有限非圆族、同一固定g非线性精化或全pair reach。

## 文件、运行与当前验证身份

新文件：

- scripts/r582_continuous_mean_profile_20261126.py：24700 B，SHA256 35060aa3e862c4852b30396493be37d1bd688281b4a093bd1e532d964e562631。
- scripts/r582_true_core_shooting_20261126.py：30333 B，SHA256 c7f445b98cc948fb7fc920c910aed25bd60e9b14af5971de62d3c9bc3301f534。
- computations/request-r582-true-core-shooting-20261126.json：75999 B，SHA256 3d26aa89e101c15d489447b11fbd5c7a64f6e938e8f23399cd06d6a3ee515b0a。
- workflow visible-r582-true-core-shooting-20261126.yml：2692 B，SHA256 df8ff194634d0569a4b82de38c1d1af3e8d7fc52fb52e2cabdc7fcc5932d23f5。

单lane/max1，1800秒合作科学段、50分钟job。固定Python3.12.14/numpy2.3.5/scipy1.17.0及既有两个Actions SHA。复用已经发布的stdin runner，保真实双仓pull、全部README差异、私库QUEUE核、七份源绑定、科学前删凭证及stdout-only限制。

helper及driver已在恢复环境后作完整AST、七份绑定和小输入逐项静态核；helper区间部分另有独立纸核。随后root指出预先舍入宽度与真实端点差的连续语义差别，已作上述三处最小区间修正并更新 helper→driver→request 的完整绑定。数值 jets、ODE、控制、网格与运行参数不变；driver仍保“更细ODE不确认原根时降级状态”。新修订再次仅作AST/哈希静态核，本地未导入或执行任何科学模块。
