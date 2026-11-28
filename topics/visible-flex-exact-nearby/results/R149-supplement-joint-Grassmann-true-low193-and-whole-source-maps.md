# R149-GG：同一真实 low193 的联合误差正交图表及完整四源映射

**状态：已证明的计算合同；尚无 GG 实际数值结论。** 本文给出与 TF
同一个实际有限维变系数 BVP 的新认证算法。TF 原 run
`46120139018/1` 仍是 left97 第 81 格未认证的失败结果；本文不把它改标为成功。
GG 必须先实际恢复并匹配原完整载体的三个 SHA，再实际完成所有新图表、全部边界及
四个全域源映射，才有新的数值逆结论。它也仍不是原无限维完整正侧逆。

## 1. 固定对象、失败状态与真正新增的工作

固定 [R149-TF](R149-supplement-true-low193-local-flow-and-direct-response.md)
第 1–5 节的同一 $N=193$ 真实低频系统 $y'=A_L(r)y$：原 WVC 混合系数，
原 155 个 parent，原 1,424 个 refined physical cells，真实根端点，普通
$dr$，原独立 mean，及原 97+96 维输出。系数逐格取
[R141-child](R141-supplement-genuine-child-coefficients-and-unchanged-hybrid-sources.md)
的完整 closed intersections；不缩 intrinsic/mean 球，不把内部 balance 当成物理 $S$。
四个源角色仍按原顺序为 ordinary raw low、transformed low、low second-kind
correction、centre high0 return；列数仍为 $193,193,193,128$。

TF 的真实失败身份、全部 81 个已登记 left pivots、0 个 right/node pivots、
0 个完整 source maps，及原最后失败候选的精确恢复合同，见
[完整诊断](../notes/2026-11-28-TF-left81-failure-and-checkpoint-restoration.md)。
原 left97 范数指数后四项 $2,3,4,10$ 不能推出实际 BVP 奇异。
GG 不再续用该固定图表的区间盒乘积，也不重发前 81 个原 pivot 验收结论。

必要载体恢复使用已经登记的
`fourfold_codazzi_true_low193_checkpoint_carrier_restore.py`。只有原 private
prefix SHA `0be16da1dc652f830389b496eb87bb300a07dddcb564167fdbf9ef650b9ea8b6`、
checkpoint raw SHA `3916928e630d814f8ec7e0d22b1470d0a9caa4f34150d1d7ccef8f185843d105`、
gzip SHA `c0718447c4ef8e8d50c11561eb24947903090a5db2306223ec56399ba4629f33`
全部匹配后，才允许导入完整 81 格的旧 flows/moments。恢复执行原 order24 与原 outward
packing，但不重新计算旧范数指数或旧验收记录；最后失败格只恢复原 64-cuts
完整矩阵供 whole SHA，不再次尝试其失败逆。原始未压缩及 gzip SHA 均不可换成新生成值。

随后对 0–80 只使用恢复过程中已形成并完整保存的 raw forward/backward 及五个
moments；对 81–1423 才生成新 order16 whole-cell packets。新图表误差证明是
对这些同一完整流的不同表示，不是重算已完成的 TF 科学结论。

## 2. 一个完整矩阵的一颗联合误差球

写 $M\in\mathcal B_2(M_c,r)$，其中 $M_c$ 的每项均为精确 dyadic，
$\|M-M_c\|_{2\to2}\le r$。从完整有向 entry enclosure $[M_{ij}]$ 选 dyadic
中心后，取

$$r\ge\left(\sum_{ij}\sup_{z\in[M_{ij}]}|z-(M_c)_{ij}|^2\right)^{1/2}.$$

这一步包含全矩阵的舍入、Peano tail、系数球以及 packing error。后续不再把
这一个 operator-norm 半径扩展成各项独立自由变化的盒子。另可保存整个真实矩阵族
的已知范数 $n_M$，例如精确正交 frame 的 $n_M=1$；它不声称外包球内每个矩阵
都正交。使用 $\min(\|M_c\|+r,n_M)$ 始终是实际矩阵的上界。

加法的半径相加，转置保持半径。竖向或横向拼接的半径至多
$\sqrt{\sum r_j^2}$。对 $AB$ 的中心先算完整有向 $A_cB_c$，再付转换误差；
输入半径费用可取以下两式的较小者：

$$\|A\|r_B+\|B_c\|r_A,
\qquad \|A_c\|r_B+\|B\|r_A.$$

第一式来自 $AB-A_cB_c=A(B-B_c)+(A-A_c)B_c$，第二式同理；允许二者关联。
任意不重复坐标的行列投影都不增加该半径。

若完整 directed inverse 包住 $M_c^{-1}$，其中心和半径为 $(X_c,r_0)$，
$g\ge\|M_c^{-1}\|$ 且 $gr<1$，则

$$\|M^{-1}-X_c\|\le r_0+\frac{g^2r}{1-gr},
\qquad \|M^{-1}\|\le\frac g{1-gr}.$$

这直接由 resolvent identity 及 Neumann bound 得到。每个分母均在运行时做严格有向
正下界检查，不以浮点数、显示小数或假定良态代替。

## 3. 真正精确正交的自适应 frame

令 $P=97,Q=96$。浮点 Householder QR 只建议 97 个完整 dyadic 非零向量
$v_j\in\mathbb Q_2^{193}$，其前 $j$ 个分量为零。所有向量先按完整 binary64
定义保存并原样读回。实际数学 frame 是

$$H(v)=I-\frac{2vv^t}{v^tv},\qquad
\mathcal Q=H(v_0)\cdots H(v_{96}).$$

因为每个 $v^tv>0$ 且全为精确有理数，逐项代入给出
$H(v)^tH(v)=I$，故 $\mathcal Q^{-1}=\mathcal Q^t$、
$\|\mathcal Q\|=\|\mathcal Q^{-1}\|=1$。这与建议 QR 的浮点正交性无关。
程序用 Arb 完整计算上述有理公式，把全部评估误差收入 §2 的联合球。
其 dyadic 中心本身不被声明为正交矩阵。

在第 $i$ 格，取当前 left graph 的中心所给完整 $193\times97$ 列，乘该格完整
raw flow，再对其中心建议新 frame。任何这样的建议都只能改变有限图表；它不改变
实际 $A_L$、源、端点、物理 $S$ 或 mean。严格成败只由下一节的有向分母决定。

## 4. 一般非零中心的分式图表包含

在旧、新两个真实正交 frame 间令完整流为

$$E=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
Z\in\mathcal B_2(Z_c,r).$$

给任意完整精确 dyadic 新中心 $\widehat Z$，置

$$A_c=A+BZ_c,\quad
R_c=C+DZ_c-\widehat Z(A+BZ_c),\quad
L_c=D-\widehat ZB.$$

若 $g\ge\|A_c^{-1}\|$，$b\ge\|B\|$ 且 $d=1-gbr>0$，则整个 graph
有定义且

$$Z'=(C+DZ)(A+BZ)^{-1},\qquad
\|Z'-\widehat Z\|\le\frac{g(\|R_c\|+\|L_c\|r)}d.\tag{GG.1}$$

证明：写 $Z=Z_c+\Delta$，则
$(Z'-\widehat Z)(A_c+B\Delta)=R_c+L_c\Delta$；由
$\|(A_c+B\Delta)^{-1}\|\le g/d$ 得结论。与此同时，上式逆以
$A_c^{-1}$ 的完整联合中心为中心，额外半径至多 $g^2br/d$。所有
$A,B,C,D,A_c,R_c,L_c$ 本身的完整有向误差都按 §2 支付。

等价的奇异值版本分母是
$\sigma_{\min}(A+BZ_c)-\|B\|r$，分子是
$\|C+DZ_c-\widehat Z(A+BZ_c)\|+\|D-\widehat ZB\|r$。
不能省略 $BZ_c,DZ_c$。实际实现用完整 directed fractional centre 的 dyadic
中心作 $\widehat Z$，再应用 GG.1；反向 right96 graph 一般并不以零为中心。

## 5. 原边界、全部节点与 mean

根端 free97 初值正是 raw 坐标的 $[I_{97};0]$；根 frame 取 $I_{193}$。
外端完整原边界算子为

$$B_R y=(u_1+\tfrac{13}{80}v_1,\ldots,
u_{96}+\tfrac{13}{80}v_{96},v_0)^t.$$

记外端 frame $[Q_1,Q_2]$。严格逆 $B_RQ_1$ 后，外端 right graph 为
$Y_R=-(B_RQ_1)^{-1}B_RQ_2$。它保留全部 97 条实际边界方程，特别是独立 mean。
反向用完整 raw inverse flow 与同一 frame，交换 $97/96$ 分组后再应用 GG.1，
保留完整非零 $Y_c$。

每个节点严格验证 $W=(I_{96}-ZY)^{-1}$ 并定义

$$L=\mathcal Q\binom{I}{Z},\qquad R=\mathcal Q\binom{Y}{I},$$

$$\ell=(I+YWZ,-YW)\mathcal Q^t,
\qquad\rho=(-WZ,W)\mathcal Q^t.$$

直接乘法给出 $[\ell;\rho][L,R]=I_{193}$。同一完整 $193$-BVP 由 1,424
个 forward graph 包含、1,424 个 reverse graph 包含、1,425 个节点横截逆以及
上述真实外端初值逆共同给出。少一个环节均无完整逆。所有 raw identity
transmissions、真实 cell lengths、端点自由度、physical4 约定保持原 TF 定义。

## 6. 五个 moments 与四个完整源映射

局部 packet 使用 TF 的同一变系数 Peano–Baker 公式。只把新的未完成 1,343 格
的阶数从 24 改成 16；余项仍是完整阶乘尾，并验证其正分母。它不是用一个固定
中点矩阵指数替代变系数流。每格同时计算 raw forward/backward 以及五个完整
$193\times193$ moments：一个 body-output moment $X_i$ 和四个 input covariance
$J_i^a$。第四源虽然有 128 列，其 pullback covariance 仍为完整 $193$ 行。
正侧 source 全部用原 WVC family、mean、root 和物理输出；不会借用负侧 JWS 门。

设 $C_i=(A_i+B_iZ_i)^{-1}$，$D_i$ 为 reverse graph 的完整逆坐标步。
对四个源分别令

$$O_i^L=L_i^tX_iL_i,\quad O_i^R=R_i^tX_iR_i,\quad
I_i^L=\ell_iJ_i^a\ell_i^t,\quad I_i^R=\rho_iJ_i^a\rho_i^t.$$

初始化 $A_0^L=A_0^{R,a}=0$，
$A_0^0=(P_{97}L_0)^t(P_{97}L_0)$。逐格完整递推

$$\begin{aligned}
\overline A_i^L&=A_i^L+O_i^L,&
\overline A_i^{R,a}&=A_i^{R,a}+I_i^R,\\
B_a^2&\mathrel{+}=\operatorname{tr}(\overline A_i^LI_i^L)
 +\operatorname{tr}(O_i^R\overline A_i^{R,a}),&
R_a^2&\mathrel{+}=\operatorname{tr}(A_i^0I_i^L),\\
A_{i+1}^L&=C_i^t\overline A_i^LC_i,&
A_{i+1}^0&=C_i^tA_i^0C_i,\\
A_{i+1}^{R,a}&=D_i\overline A_i^{R,a}D_i^t.
\end{aligned}$$

末端令 $T_R=\Theta P_{96}^{\rm outer}R_R$，再加
$E_a^2=\operatorname{tr}(T_R^tT_RA_{1424}^{R,a})$。
这是原 TF 第 4 节完整 semiseparable 积分恒等式：同格的两个三角分别由其完整
正方形支配，两个方向都保留；跨格 signed covariance 先组合再取上界。
因此全域 body、root97、outer96 的 Hilbert–Schmidt 平方分别不超过
$B_a^2,R_a^2,E_a^2$，operator norms 分别由相应平方根控制。

联合球 trace contraction 也完整支付误差。若 $U,V$ 是 $n$ 阶方阵，
则在精确 signed 中心 trace 之外加

$$n\bigl(r_U\|V_c\|+r_V\|U_c\|+r_Ur_V\bigr).\tag{GG.2}$$

因为 $|\operatorname{tr}T|\le n\|T\|$，GG.2 是全矩阵误差，不是抽样或逐频猜测。
真实 Gram contraction 非负；任何有向计算不足以给有限非负 upper 时失败。

完整 correction source 的 body norm $b$、原全部 atoms norm $a$ 仍给

$$\|R_{\rm low}\|\le
\frac{\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2}}2,$$

因为所有 193 个独立 atom inputs 的 identity 项都保留。四源必须全部完成到
第 1,424 格并完成末端 96-row pairing 才能登记这个 whole-map 结论。

## 7. 与原物理完整链的实际接口

GG 成功后输出独立新 kind，明确其 low inverse 是本真实变系数 WVC BVP。
四源的 body/root97/outer96 全域 bounds 可以代入
[R149-TP](R149-supplement-true-flow-to-complete-positive-physical-chain.md)
的同一数学式，因为 GG 改变的仅是内部有限图表。其 ordinary $dr$、原 $S$、
root97、一次 $\Theta$ readout、独立 mean 与高源 128 列完全相同。

实际 consumer 仍必须逐 whole byte/SHA 接纳 GG 的新 kind、全部新记录、四源
和完整执行对象；旧 TP owner 的 TF-specific kind admission 不会被假冒或绕过。
最终原 $\Delta A_L,\Delta C,G_H$、完整 CFB、真实 Robin/mean 以及
$58\to224\to32\to$ PN56/CXN6 门均继续支付；GG 单独不声称这些门闭合。
后继 signed response 还须生成其真正全格 forcing increments 和原 boundary RHS。
四个 norm targets 不会被再次运行来代替该新 signed-column 输入。

## 8. 完整执行成本、阶段保存和恢复语义

原 TF 448 个 Peano subboxes 的实际 elapsed 为 4,669.906695433 秒；据此
不能再安排 1,424 格全部串行 order24 等待超时。新合同使用 4 个 native 单线程
进程，对未完成的 1,343 格从原四等分起算。对尚未积分的子盒 $I$ 取同一真实长度
$h_I$ 和同一完整 balanced 系数盒 $A_I$，以原行和有向上界
$\beta_I=\|h_I A_I\|_\infty^+$ 检验 $\operatorname{lo}(1-\beta_I/18)>0$。
仅未过者二等分，最细宽度 $1/64$。通过的兄弟不再细分。若最细仍不过，保存原格号、
区间与有向 $\beta_I$ 失败。随后只按已通过的完整分割计算一次 order16 转移、四源及五 moments；
原 Peano 核在实际计算中再次验证同一正分母。预检不计算转移、moment 或 graph。
每个 packet header 保存全部切点的分子（公分母 64）并核验递归二分叶条件；
原81格的切点均严格固定为 $(0,16,32,48,64)/64$。
parent 按原 cell 顺序接图表；总 submitted-but-not-received 最多 8 个，队列只传
小文件 receipt。各 worker 先完整写出并读回同一私有 packet，再发其 whole SHA。
单格任何失败都不产生完成的 packet；已完整写出的新格仍保留准确范围和 SHA。

每个 joint matrix 的裸载体为 $(193^2+2)\cdot8=298008$ bytes，
每格七矩阵为 2,086,056 bytes；全部 1,424 格为 2,970,543,744 bytes，另加完整
小 headers。全部 frame proposals 的裸向量载体为 213,269,632 bytes。
这些全部保存在 private job disk，parent 不把 3 GB packets 再复制到 RAM。
graph/node joint store 的 live bytes 上限为 2 GiB，其 decoded cache 至多
200,000 entries；完整私有目录上限 8 GiB。原 314,059,632-byte prefix 和
passive flow carriers 在三 SHA 匹配且全部 81 格完整转换后释放，才 fork workers。

内存预算逐次加总 parent 和全部四 workers 的实际 RSS，连 COW shared pages
也在每个进程计一次，阈值为 14 GiB；不是只看 parent 的 `RUSAGE_SELF`。
每格生成中会有完整 matrices、packing buffers 和 fork 副本，均在实际 RSS 内；
队列不传大数组。这个预算检查是运行时资源条件，不是声称已经知道新 run 的峰值。
order16 与 4 workers 的墙钟改进是工程估计，不是认证后的时间上界。

两个自然科学目标依次为完整真实 graph/BVP 逆、完整四源映射。owner 在每个已完成
whole cell、新 graph/node 以及源阶段保存完整 prefix 范围、whole carrier/index
hash、当前阶段、原恢复身份和所有未付范围；预算失败或 worker 失败不把 prefix
改称全域结论。大的可重建对象不上传 Git/Release/artifacts。它们在 runner 退出后
不是 durable carrier；后继必要恢复必须按同一完整源、参数、阶段和固定运行环境
重建，并实际匹配全部 whole SHA，不能用一个公共指数列表代替真实矩阵状态。

## 9. 对应源码与结论边界

新纯数学入口：`fourfold_codazzi_true_low193_grassmann_math.py`。
全矩阵 binary carriers、4-process ordered packets 和 aggregate RSS：
`fourfold_codazzi_true_low193_grassmann_carriers.py`。
原 TF flow/provider/restore source 均保持既有 whole identities。

本文证明这些公式认证的正是原同一个真实低频 BVP 和完整四源观察空间。
当前尚未执行新数值目标，故不列任何新的 low norm 数值、成功 chart 范围、
full positive gate 或最终闭曲面存在结论。只有真实新 outcome 满足全部合同后，
方可消费其数值结果；任何失败会保留为失败并继续推进未完成工作。
