# R101：实际完整返回的 split-Wiener 误差与真实参数圆周共轭

2026-11-12，visible-exact-astra-f6a2；constructive-route 实际有理预算，
independent-audit 端点参数接合。

**状态：已证明的中间结论。** 对当前准确四重族及其完整真实返回，存在
原半径 $10^{-9}$ 参数盒内的真实参数，使完整返回解析共轭到 R100 的
二次无理旋转。这里使用原来保存的有限端点、准确 dyadic 预校正及全部
真实流误差；不修改旧报告的输出，不把有限残差当成真实误差。

本结果解决 open 中的实际 R31 门。它不是整等距 PDE 的强逆，也没有
完成固定开帽的非线性零解或课题要求的闭面连续族。新目标的完整低阶
相位算术、全部高低反馈和非线性闭合继续办理。

## 1. 具体结论

令 $\varphi=(1+\sqrt5)/2$，采用 R100 的准确目标

$$
 \rho_*=\frac{690433168\varphi+94331801}
              {1251918455\varphi+171045842},\qquad d_*=\pi\rho_*.
 \tag{101.1}
$$

原真实几何参数及已经保存的准确增量为

$$
 p_0=-\frac{7789843107295549}{4611686018427387904},\qquad
 \mu=
 -\frac{7503610915091864083421307370189835928331761396892589761028645157230256948727508775433}
 {8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296}.
 \tag{101.2}
$$

令 $H$ 为保存的准确 dyadic 共轭，$J=\operatorname{id}+w$ 为运行
43308150283 保存的准确有限校正，记实际 full return 为 $\mathscr R_p$。
则存在真实 $p_\infty$ 和实解析、保向、次数一圆周微分同胚
$\Phi=\operatorname{id}+\phi$，使

$$
 |p_\infty-(p_0+\mu)|<3.272147902\,10^{-11},
 \qquad |p_\infty-p_0|<3.2723\,10^{-11}<10^{-9},
 \tag{101.3}
$$

$$
 \mathscr R_{p_\infty}\circ H\circ J\circ\Phi
 =H\circ J\circ\Phi\circ T_{2d_*}.
 \tag{101.4}
$$

在正宽度 $s_\infty=1/2048$ 上，

$$
 \|\phi\|_{s_\infty}<1.102524382\,10^{-8},\qquad
 \|\phi'\|_{s_\infty}<3.284319905\,10^{-5}.
 \tag{101.5}
$$

范数均为含平均模的 $2\pi$ 周期 Wiener 范数
$\|f\|_s=\sum_{k\in\mathbb Z}|f_k|e^{s|k|}$。
$T_d(x)=x+d$。这些常数包含真实源、所有 Fourier/Taylor 尾和舍入，
不是 ODE 射线或有限模的拟合值。

## 2. 原始输入和对象同一性

全部几何、完整时间覆盖和原误差沿用如下不可变输入：

| 输入 | SHA256 |
|---|---|
| complete-flow actual_endpoint.json.gz | f8d958ce1af4cac5d4053d8c7569d33c049a917d84094e55944842fad4228328 |
| complete-flow 可读算术摘要 | f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52 |
| 新目标 preNewton report.json | 030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a |
| 原完整 g0/index.json.gz | 4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45 |
| 原 g0/ordered_accumulator.json.gz | 52fb2fa12b20f02e3aed3e7a2fbbe36e64586ed264080d05dda19de9aba3b0fd |
| symmetric local-J0 完整 report.json.gz | f77211c4d7710dae2a737558ceae980c4d780666d4f91f2a730004981802d301 |
| 同一 local-J0 完整系数 | 27d9815a2c0ae5d23b6825b0a978a920db1fb8af005f6e9423da394950320834 |
| 原准确 $H$ | 0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2 |

完整流端点及 g0 两项在 data/phase_ring_continuation/step5_complete_flow_ci_43301401638/
及其 g0 子目录；预校正在 step5_half_prenewton_43308150283/；
local-J0 在 step5_local_J0_symmetric_ci/。
可读摘要为 notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json。
准确 $H$ 的路径由 preNewton 报告原样记录。

这里必须确认 local-J0 和 center 参数累计中的零阶有限多项式相同，
不能只比较显示出来的旧误差数值。已经实际运行的
fourfold_ci_complete_parameter_flow_v2.py::build_indices
从唯一的 $(\text{segment},\text{准确subspan})$ g0 选择建立参数 index。
每个候选都须匹配选中 g0 的原 SHA；前 32 段也调用同一
validate_parameter_report 核 reference_certificate_sha256。
保存的 parameter-input-selection.json 给出该原 g0 index、
555 叶、550 段，以及 center index

    e6159a89b7f26c875d916138076af51f582dd24370b701ee9fe14603a9605585

的 SHA。execution.json 保留 g0/selection/center/hybrid 四阶段真实 exit 0；
原 endpoint 阶段因旧 R31 门失败 exit 2，未被本证明改写成成功。

实际可选参数密度生成核调用同一 parameter_local_from_g0_norms。
其零阶 first[0] 直接从该 g0 的 first_integral_file 加载，并验证原 SHA；
零阶 local[0] 为零。g0 的 validate_saved 同样验证首积分文件、
density coefficient SHA 和参考身份。g0 的 add_ordered_segment 与
advance_parameter_integrals 的零阶数学递推都是

$$
 C_{\rm new}=C+G_j,\qquad D_{\rm new}=D+G'_j C,
 \tag{101.6}
$$

右侧使用旧 $C$，保留完整乘积频率。参数累计又验证
same_g0_certificate_sha256，hybrid 验证 center/uniform 相同 g0
及完全相同的 first[0]。因此不同 Arb 包裹和末尾零系数包围的是同一个
准确有限多项式 $W_*=C+D$。

endpoint_three_orders_spatial 对这个多项式取准确 dyadic 系数中心 $a$，
完整支付 $\|W_*-a\|_{3/1024}$。本证明保持 $a,P_0,P_1,\mu,w$ 全部不变。
local-J0 精修的完整校正不加进 $a$；它的范数作为误差一并保留。
这使原 preNewton 的全部有限残差仍适用。

逐文件源 SHA 与已执行选择证据另见
[同一有限密度身份链](../notes/2026-11-12-center-g0-symmetric-J-identity-audit.md)。

## 3. 坐标误差中只有真正 sup 项需要 Hardy

记 $\sigma=3/1024$、外标签带 $1/256$、$R=1/1024$。
完整真实参考坐标流 $X=X_{p_0}$ 由 R68/R72 给出。令

$$
 j=\|\text{完整 symmetric 校正}\|_\sigma
           +\text{全部未补回 local 余费}.
$$

[local-J0 精修证明](../notes/2026-11-12-saved-local-J0-symmetric-refinement.md)
给出了 $J_j=\tfrac12G_j'G_j+\text{奇偶bracket}$ 的准确恒等式，
并只从原正预算中减去已核实分量的下界。330 个已处理叶保留完整乘积；
225 个未处理叶保留全部旧费。于是所有 local 项的准确和 $J_{\rm total}$
满足

$$
 \|J_{\rm total}\|_\sigma\le j
 <2.807274\,10^{-15}.
 \tag{101.7}
$$

具体地，两个相加项分别小于 $3.480705\,10^{-16}$ 和
$2.459203\,10^{-15}$。不能只取第二项而继续沿用原有限多项式。

真实 $X$ 与完整有限有序积分的差，由 R72 (11) 控制为真正 sup 余项
$r$，其计算直接使用原 $A,E,R$：

$$
 r=E(1+A/R)+\frac{A^3}{2(R-A)^2}
 <3.779199\,10^{-17},
 \tag{101.8}
$$

其中原有向输入给
$A<4.092564\,10^{-8}$、$E<1.850690\,10^{-18}$，且 $A<R/2$。
这里没有从一个总误差上界反向减去其它上界。

令 $c=\|W_*-a\|_\sigma$。原 gzip 已实际按 SHA 读出

$$
 c<2.096632\,10^{-85};
 \tag{101.9}
$$

算术程序保留原显示球中心加半径的准确有理上端点，未将打印中点当界。
因此

$$
 X=\operatorname{id}+a+e,\qquad
 \|e\|_s\le j+\mathcal H(\sigma-s)(r+c),
 \quad
 \mathcal H(v)=\sqrt{1+\frac4{e^{2v}-1}}.
 \tag{101.10}
$$

$c$ 本来已是 Wiener 费用；把它也乘 $\mathcal H\ge1$ 只是保守多付。
$j$ 保持直接 Wiener 费用。该拆分保留全部高 Fourier 模、真无限 primitive、
时间和角尾、真实场近似以及 chronological 三阶尾。

以下采用

$$
 \rho=\frac{2047}{1048576},\qquad
 \|w\|_{5/2048}<9\,10^{-12}.
$$

在 $s=\rho+\|w\|_\rho$，用 $e^{2v}-1\ge2v$ 的准确有理比较得
$\mathcal H(\sigma-s)<46$。因此

$$
 \|e\circ J\|_\rho\le j+46(r+c).
 \tag{101.11}
$$

R86 的真实 sup source/tail 给更紧的数字，但本定理使用 (101.8)
这条较保守、独立写全的 R72 路线；无需依赖另一个尚未证明的拆分。

## 4. 参考图的导数从真实近旋转恢复

设冻结的物理参考末端为 $x/4+U(x)$，令

$$
 L(x)=x+4U(x),\quad
 \Gamma_p=\mathscr P_p\circ H,\quad
 G_p=H^{-1}\circ\Gamma_p,
 \tag{101.12}
$$

其中 $\mathscr P_p$ 为 R77 的真实 half return。参考对 $p$ 固定，
所以准确有

$$
 \Gamma_p=L\circ X_p.
 \tag{101.13}
$$

本节不能把 $H^{-1}$ 和 $L'$ 的两个粗范数相乘来传递 $e$；
它们的复合有一个已验证的、接近 $1$ 的导数。

令 $u=X-\operatorname{id}$。真实流给 $\|u\|_{\sup,\sigma}\le A$。
由 R63 的两边界 Parseval 和 Cauchy--Schwarz，对于 $d=\sigma-s>0$，

$$
 \|u\|_s\le A\sqrt{1+2/d},\qquad
 \|u'\|_s\le \frac A d\sqrt{1+1/d}.
 \tag{101.14}
$$

导数式中的正负模均保留：其较精确界是
$2A(\sum_{k\ge1}k^2e^{-2dk})^{1/2}$，而

$$
 \sum_{k\ge1}k^2e^{-2dk}
 =\frac1{4\sinh^2d}\coth d
 \le\frac{1+1/d}{4d^2}.
$$

取

$$
 t=17/8192,\qquad V=1/400000,\qquad d_X=\sigma-t-V.
$$

实际准确平方比较给

$$
 A^2(1+2/d_X)<V^2,\qquad
 \frac{A^2}{d_X^2}(1+1/d_X)<(1/500)^2.
 \tag{101.15}
$$

故 $v\mapsto-u\circ(\operatorname{id}+v)$ 在 $\mathcal A_t$ 的闭 $V$ 球
上自映射并收缩。其固定点定义真实 $X^{-1}=\operatorname{id}+v$，
并有 $\|(X^{-1})'\|_t\le500/499$。

原完整返回的 sharp_half.J 已给
$\|G_{p_0}'\|_{9/4096}<1.000000126$，且 $t+V<9/4096$。
因此准确参考图

$$
 F_{\rm ref}=G_{p_0}\circ X^{-1}
$$

满足

$$
 H\circ F_{\rm ref}=L,\qquad
 \|F_{\rm ref}'\|_t
 \le \|G_{p_0}'\|_{t+V}\frac{500}{499}<1.003.
 \tag{101.16}
$$

第一个恒等式先在实圆由 (101.13) 成立，再解析延拓。
这不要求预先假设 $H$ 在某个未付全复域上单叶。

原 $H''$ 的已付界和 $F_{\rm ref}$ 的像域还给

$$
 \|L'\|_t<17,\qquad
 \|L'''\|_{\rho+10^{-9}}<10^{10}.
 \tag{101.17}
$$

具体地，$F_{\rm ref}$ 相对旧平移的周期位移至多为
$V+\|G_{p_0}-x-d_{\rm old}\|<V+7.768\,10^{-11}$；
它仍在 $H''$ 已付的 $5/2048+10^{-3}$ 带内。
因 $h'$ 没有常数模，$\|H'\|\le1+\|H''\|<15.336$，再乘 (101.16) 小于 17。
对 $L'$ 使用二阶 Cauchy 界，取
$g=t-\rho-10^{-9}>0$，则 $2\cdot17/g^2<10^{10}$。
全部平方/域比较在同一准确有理预算里实际执行。

## 5. 同一局部 $H^{-1}$ 和真实参数接合

直接核 endpoint_three_orders_spatial 的完整有限产品得

$$
 Q_0:=x+P_0=L+L'a+\tfrac12L''a^2.
 \tag{101.18}
$$

令 $Z=\operatorname{id}+a$、$\ell=L\circ Z-Q_0$。
由 (101.17)、原 $\|a\|_\sigma<3.017\,10^{-11}$，完整 Taylor 余项满足

$$
 \|\ell\|_{\rho+\|w\|_\rho}
 \le\frac{10^{10}}6\|a\|_\sigma^3<5\,10^{-23}.
 \tag{101.19}
$$

原报告另有较紧的 complete_Taylor_fees[0]，
其上界小于 $1.536\,10^{-30}$；实际预算把它也加上，绝不删去余项。

所有随后出现的物理端点输入都使用同一个 R63 局部逆分支。
在 $s_H=5/2048$，原报告给

$$
 R_H=\|1/H'\|_{s_H}<3.432,\quad
 B_H=\|H''\|_{s_H+10^{-3}}<14.336.
$$

取 $r_H=10^{-3}$，则 $\kappa=R_HB_Hr_H<1/20$。
在 $E\in\mathcal A_s$、$s\le s_H$、$\|E\|_s\le10^{-4}$ 的整个球上，
R63 收缩唯一求出

$$
 H(x+d_*+v)=H(x+d_*)+E,\qquad \|v\|_s\le r_H.
$$

确实 $R_H\|E\|<r_H/2$；二阶剩余与收缩费用均由 $\kappa$ 支付。
记这一 Banach 空间局部逆为 $\mathcal I$。直接微分得

$$
 D\mathcal I(E)[b]=\frac b{H'(\mathcal I(E))},\qquad
 D^2\mathcal I(E)[b,c]
 =-\frac{H''(\mathcal I(E))}{H'(\mathcal I(E))^3}bc,
$$

所以在整个球上

$$
 \|D\mathcal I\|\le \frac{R_H}{1-\kappa}<4,\qquad
 \|D^2\mathcal I\|
 \le B_H\left(\frac{R_H}{1-\kappa}\right)^3<1000.
 \tag{101.20}
$$

必须核输入球而非只写形式链式法则。(101.14) 给
$\|X-\operatorname{id}\|_{5/2048}<2.7\,10^{-6}$。
对 $s\le\rho+10^{-9}$、$Y_\lambda=Z+\lambda(X-Z)$，
均有 $s+\|Y_\lambda-\operatorname{id}\|_s<t$。
已付 $\|\Gamma_{p_0}-H(x+d_{\rm old})\|<2.208\,10^{-11}$，
新旧 half 角差小于 $8.548\,10^{-12}$。
用 (101.17) 比较 $L(Y_\lambda)$ 与 $L(X)$，并支付
$\|H'\||d_*-d_{\rm old}|$，合计小于 $5\,10^{-5}$。
下列有限、参数和 Taylor 项均远小于 $10^{-10}$。
因此所有输入及其插值线都严格留在 $10^{-4}$ 球中。
局部唯一性保证 $\mathcal I$ 与 (101.16) 的 $F_{\rm ref}$ 对应同一分支。

冻结原 $x,\mu,J$，写

$$
 Q_\mu=Q_0+\mu P_1,\qquad
 r_\mu=\Gamma_{p_0+\mu}-\Gamma_{p_0}-\mu P_1.
$$

真实实参数 Taylor 公式给

$$
 \|r_\mu\|_s\le
 |\mu|\,\|\partial_p\Gamma_{p_0}-P_1\|_s
 +\frac{\mu^2}2\sup_{p\in[p_0,p_0+\mu]}
                                  \|\partial_p^2\Gamma_p\|_s.
 \tag{101.21}
$$

整条参数线已经包含于原 $\eta=10^{-9}$ 盒；这就是旧 preNewton 中
true_first_parameter_source_fee 和 whole_box_second_parameter_Taylor_fee。
不求 $w$ 对参数的导数，不假定三个有限 $P_i$ 构成一个可微有限族。

简写同一局部逆为 $H^{-1}$，准确三段恒等式为

$$
\begin{aligned}
G_{p_0+\mu}-H^{-1}Q_\mu
={}&H^{-1}(L(X)+\mu P_1+r_\mu)-H^{-1}(L(X)+\mu P_1)\\
 &+H^{-1}(L(X)+\mu P_1)-H^{-1}(L(Z)+\mu P_1)\\
 &+H^{-1}(L(Z)+\mu P_1)-H^{-1}(Q_0+\mu P_1).
\end{aligned}
 \tag{101.22}
$$

第一、三行分别不超过 $4\|r_\mu\|$、$4\|\ell\|$。
第二行沿 $Y_\lambda$ 的准确 Frechet 乘子是

$$
 H^{-1\,\prime}(L(Y_\lambda(x))+\mu P_1(x))L'(Y_\lambda(x)).
$$

$P_1$ 始终在冻结标签 $x$ 取值，因此不遗漏 Jacobian，也不暗中换成
$P_1(Y_\lambda)$。由 (101.16)、(101.20)，这个乘子的范数至多为

$$
 1.003+|\mu|\cdot1000\,\|P_1\|_s\|L'\|_t<1.004.
 \tag{101.23}
$$

实际预算还保守加入 $|\mu|\cdot4\|P_1'\|$，其中原真实有限输入给
$\|P_1\|<.007$，Cauchy 给 $\|P_1'\|<15$。
整个额外导数费小于 $10^{-10}$，仍满足 (101.23)。

## 6. 原预校正的有限残差与真实 half 误差

R100 的完整有限 quadratic 和 composition Taylor 两项严格包围

$$
 Q_\mu\circ J-H\circ J\circ T_{d_*}.
 \tag{101.24}
$$

它们来自完整频率乘积与真实 Taylor 余项；本证明未重新选择任何有限系数。
在 $5/2048$ 带上，原报告给 $m:=\|w'\|<1.2\,10^{-9}$。
在目前更窄域及所需像球内同样以收缩构造 $J^{-1}$，其导数因子至多
$(1-m)^{-1}$。到 $5/2048$ 的严格宽度余量远大于
$2\|w\|+\|G_{\rm new}-T_{d_*}\|$。

记 $b_{\rm other}$ 为以下全部非负费用之和：

- 原 complete_finite_quadratic_residual；
- 原 complete_finite_composition_Taylor_fee；
- (101.21) 的原一阶参数源费和整盒二阶参数 Taylor 费；
- (101.19) 的完整参考复合 Taylor 费；
- 原 complete_Taylor_fees[0]，作为额外保守保留。

将 (101.22) 右复合 $J$、使用 (101.24)，最后左复合 $J^{-1}$，
得到同一真实新 half return

$$
 C_{\rm new,p_0+\mu}:=J^{-1}G_{p_0+\mu}J=T_{d_*}+v
$$

满足

$$
 \boxed{\quad
 \|v\|_\rho\le
 \epsilon_h:=
 \frac{1.004[\,j+46(r+c)\,]+4b_{\rm other}}{1-m}
 <4.564012312\,10^{-15}.
 \quad}
 \tag{101.25}
$$

这里 $b_{\rm other}<3.1345870\,10^{-20}$。
所有参数、有限残差和有限复合费用均保留了旧粗逆因子 4。
改进只来自对真实中心坐标误差使用准确参考复合及正确的函数范数。

由 R77 的真实平方关系，取 $s_0=15/8192$，实际域门
$s_0+\epsilon_h<\rho$ 给

$$
 \|C_{\rm new,p_0+\mu}^{\,2}-T_{2d_*}\|_{s_0}
 \le2\epsilon_h=:\epsilon
 <9.128024624\,10^{-15}.
 \tag{101.26}
$$

没有把存储的物理端点 $A=\mathscr P\circ H$ 直接平方。

## 7. 实际 R31 所有门

R100 对同一真实参数族的完整共轭转移已经支付整盒导数、逆域及真实
平均横截。保留新参数中心 $p_0+\mu$ 周围的半径

$$
 r_p=\frac{999999}{10^{15}},
 \qquad S=\rho=\frac{2047}{1048576}.
$$

这些域严格包含于原参数盒和原 full-return 解析域。原输入与精确转移给

$$
 P<.010753000013,\quad Q<.333126005101,\quad
 T<.118326000189,\quad B<.005574800022,
$$

$$
 \sigma_{\rm twist}>.0022316899840.
 \tag{101.27}
$$

报告保存的是更精细的准确有理界，(101.27) 只是向外展示。
R100 的完整连分数前缀与 $\overline1$ 尾给全频 $K=5/2$。
初始共轭为恒等映射，故 R31 的 $M_0=R_0=1$、$h_0=0$。

取

$$
 s_0=\frac{15}{8192},\qquad \delta_0=\frac{11}{32768}.
 \tag{101.28}
$$

使用 R31 (2.1)--(2.4) 的原公式，准确 BigInt 约分分数实际算出

| 门 | 真实保守量 | 允许值 |
|---|---:|---:|
| 小量门 | $\epsilon<9.128024624\,10^{-15}$ | 阈值 $>1.13113749236\,10^{-14}$ |
| 真实参数移动 | $2L_a\epsilon<3.272147902\,10^{-11}$ | $r_p=9.99999\,10^{-10}$ |
| 共轭移动 | $2L_H\epsilon/\delta_0<1.102524382\,10^{-8}$ | $S-s_0>1.21\,10^{-4}$ |
| 最终解析宽度 | $s_0-4\delta_0$ | $1/2048>0$ |

27 个原输入/连续域门及 23 个新增 split/domain 门均为 true，
R31 三个最终门均为 true。阈值的准确有理上下展示为

$$
1.1311374923681054826783337893046\,10^{-14}
<
\epsilon_{\rm threshold}
<
1.1311374923681054826783337893047\,10^{-14}.
$$

(101.26) 及这些门满足 R31 的全部假设，故 R31 的收敛证明直接给
$p_\infty,\Phi$ 以及 (101.3)--(101.5)。实轴导数由 (101.5) 严格为正；
$H,J$ 也已实保向，得到 (101.4) 中的实际解析圆周共轭。证毕。

## 8. 实际算术、重放和范围

实际有理报告：

    notes/2026-11-12-split-Wiener-R31-exact.json

SHA256：

    f887bcce5a5ed8f2de2fee6a398aec86b323b91b64560f7cb84a3d6b918d521a

可重放源码：

    scripts/fourfold_split_Wiener_R31_exact_v1.mjs

SHA256：

    4ac53ef933c86d9c90e5e02a54ae9e30b1482c56f511b235a81a261959bec350

原 gzip 读出的有限标量球完整保存在：

    notes/2026-11-12-split-Wiener-original-center-scalars.json

SHA256：

    4af83f17ff84a09d30649ce5e15371094b5b77c7a13b7366f3a109739c2e53a5

2026-11-12 本地恢复期间，原 actual_endpoint.json.gz 已真实解压、读取并核
原 SHA；随后执行器再次失联。有理数学核心在 functions.exec 的 JavaScript
BigInt 中实际执行，所有比较只用约分整数分数。报告逐项标明该运行环境。
完整 Node 文件的文件系统入口尚未在第二次失联前执行，不冒称其已运行；
该入口只负责从四份指定 SHA 原报告读取相同对象并调用同一个数学核心。
从课题目录可运行：

    node scripts/fourfold_split_Wiener_R31_exact_v1.mjs

打印 Arb 球被按“中心减/加打印半径”外包为准确有理区间。
64 位浮点只可能出现于原报告不参与比较的显示字段；
连分数矩阵和二次式整数均在 BigInt 中重建，不解析成不准确的 Number。

完整参数接合的另一逐式说明见
[端点与参数审计](../notes/2026-11-12-split-endpoint-wiener-parameter-audit.md)。
原 endpoint 的 false 输出和旧失败门继续保留。新的通过结论来自本篇
独立完整误差证明与实际有理预算，而不是给原 JSON 手工改一个布尔值。

下一缺口是新目标下含真实低阶相位的全频算术、有效 cutoff、
核心/双帽/返回的完整强 Schur 与全源邻域逆，随后 R37 非线性精确化、
固定开帽和同一最终族的几何预算。本篇没有把这些缺口视为已经完成。
