# R672. 完整同角六 jet 包围与真实欧氏曲率的自适应连续上界

日期：2026-11-20。会话：Astra-resume-public-20261120 / recover_evidence。

**状态：已证明的连续区间算法与公开 Actions 实现；发表时尚未对新候选执行本条科学计算。** 本条推广 [R670](R670-direct-same-angle-first-geometry-with-complete-tails.md) 的同角有限部分加完整余项框架，给出全六 jet 和真实主曲率的向外界。数值应用、全域 reach 及课题完成均未预报；R666 保留给实际新候选的完整曲率／reach 结果。本条没有重算 R656 的旧胞或被中断的旧0241全域任务。

## 1. 准确对象与算法结论

对象仍是 [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md) 和 R670 的原 fullclosed 场。原节点是

$$
s_i=\alpha_iS+\gamma_i,\qquad \alpha_i,\gamma_i\in\mathbb Q,
$$

其中 $S,R$ 属于同一准确 FullHold 的已付有理盒；不把 binary carrier 的网格差替换为新的数学节点。全部自由三 jet、自由 core 系数 $c_j$ 和 $H$ 按保存的 binary 数解释为准确实数；派生 core 切向槽按准确 $T_j=-\nu_jc_j$ 重建，$\nu_j=2j$，不能把分别舍入的存盘槽当作额外自由变量。

$q$ 是原共享三 jet 的逐胞五次 Hermite 场。用旋转 $\phi$ 正交架，置

$$
d_j=\frac{1-\nu_j^2}{\nu_j}c_j,\quad
\delta=\sum_{j=1}^M d_j\sin(\nu_j\phi),\quad
\rho=1+\delta_\phi,\quad \Theta=\phi+\delta,
$$

$$
e_r=(\cos\delta,\sin\delta,0),\qquad
e_\theta=(-\sin\delta,\cos\delta,0).
$$

实际物理场为

$$
X=q+f e_r+\chi H e_z,\qquad f=\chi(R+S-s),
$$

其中 $\chi$ 是原宽度 $w$ 的五次 smoothstep，准确断点为 $S-w$。原仿射端口、全部原角模和完整解析指数均保持。

**定理。** 第2至7节算法对任一原闭胞的全部位置和全部角度，或者如实返回未付的浸入盒，或者返回一个准确实上界 $\overline K_i$，使该完整胞内的两个实际欧氏主曲率满足

$$
\max(|\kappa_1|,|\kappa_2|)\le \overline K_i.
$$

若全部原胞都有有效界，则在补平圆盘和镜像后得到完整闭浸入的曲率上界 $\max_i\overline K_i$。按原材料相位接口生成的全族使用同一绝对曲率界。这个结论不以目标度量 $ds^2+a(s)^2d\theta^2$ 代替真实第一基本形式，也不要求或声称当前度量残差已经小于 $10^{-6}$。

下面给出完整包围证明，包含有限角部分、两种尾、全部径向位置、取向和两盘。严格算术模型在第9节说明。

## 2. 六 jet 与二阶解析乘子的完整 Laurent 展开

物理导数记为

$$
V=X_s,\quad T=X_\phi,\quad AA=X_{ss},\quad
VT=X_{s\phi},\quad EE=X_{\phi\phi}.
$$

在旋转架中，水平向量的物理角导数对应复算子 $\partial_\phi+i$。因此

$$
(\partial_\phi+i)e^{i\delta}=i\rho e^{i\delta},
$$

$$
(\partial_\phi+i)^2e^{i\delta}
=(-\rho^2+i\rho_\phi)e^{i\delta}.
$$

这给出完整公式

$$
\begin{aligned}
X&=q+f e_r+\chi H e_z,\\
V&=q_s+f_s e_r+\chi_sH e_z,\\
T&=q_\phi+f\rho e_\theta,\\
AA&=q_{ss}+f_{ss}e_r+\chi_{ss}H e_z,\\
VT&=q_{s\phi}+f_s\rho e_\theta,\\
EE&=q_{\phi\phi}+f(\rho_\phi e_\theta-\rho^2e_r).
\end{aligned} \tag{1}
$$

这里 $q_\phi,q_{\phi\phi}$ 都是物理导数，已经包含旋转架连接项。对于一模 $R_j\cos\nu_j\phi,T_j\sin\nu_j\phi,Z_j\cos\nu_j\phi$，一导系数分别为

$$
(-\nu_jR_j-T_j)\sin\nu_j\phi,\quad
(R_j+\nu_jT_j)\cos\nu_j\phi,\quad
-\nu_jZ_j\sin\nu_j\phi,
$$

二导系数分别为

$$
(-(\nu_j^2+1)R_j-2\nu_jT_j)\cos\nu_j\phi,
$$

$$
(-(\nu_j^2+1)T_j-2\nu_jR_j)\sin\nu_j\phi,\qquad
-\nu_j^2Z_j\cos\nu_j\phi. \tag{2}
$$

零模按同一公式处理，切向零槽为0。对已经形成的这些分量作角区间包围时，不再次添加连接项。

令 $z=e^{2i\phi}$，$a_j=(1-\nu_j^2)c_j$。则

$$
i\delta=\sum_{j=1}^M\frac{d_j}{2}(z^j-z^{-j}),\qquad
\rho=1+\sum_{j=1}^M\frac{a_j}{2}(z^j+z^{-j}),
$$

$$
i\rho_\phi=\sum_{j=1}^M\frac{\nu_ja_j}{2}(z^{-j}-z^j). \tag{3}
$$

特别地，$i\rho_\phi$ 的 $+j$ 系数是 $-\nu_ja_j/2$，$-j$ 系数是 $+\nu_ja_j/2$，均为实数。源码按此符号构造；它不是把 $\rho_\phi$ 本身误当实对称 Laurent 系数。

取整数 $K\ge1$，准确展开

$$
P_K=\sum_{k=0}^K\frac{(i\delta)^k}{k!},\qquad
B=-\rho^2+i\rho_\phi.
$$

计算 $P_K$、$\rho P_K$、$BP_K$ 时每次卷积均保留全部支撑。其支撑分别包含于

$$
[-KM,KM],\quad[-(K+1)M,(K+1)M],\quad
[-(K+2)M,(K+2)M]. \tag{4}
$$

先算完整 $\rho^2$，再加完整 $i\rho_\phi$；不在两次乘法之间截去高模。式(4)是 Laurent 指标，实际普通角频率是指标的两倍。全部有限系数都以向外区间包住准确实系数。

## 3. 指数、Laurent 高尾与二阶余项

记

$$
D_\delta=\sum_{j=1}^M|d_j|,\quad
R_\rho=1+\sum_{j=1}^M|a_j|,\quad
R_{\rho'}=\sum_{j=1}^M|\nu_ja_j|.
$$

因为 $\delta$ 为实数，对 $t\mapsto e^{it}$ 使用实变量积分 Taylor 余项，得到

$$
|e^{i\delta}-P_K|
\le\frac{|\delta|^{K+1}}{(K+1)!}
\le \tau_K:=\frac{D_\delta^{K+1}}{(K+1)!}. \tag{5}
$$

这里每阶导数的模恒为1，无需额外指数因子。也没有把式(5)误作关于复相位的统一界。

分别对每个精确 jet 的乘子使用式(5)，而不是对一个没有导数控制的余项直接求导。于是

$$
|\,\rho e^{i\delta}-\rho P_K\,|\le R_\rho\tau_K,
$$

$$
|\,Be^{i\delta}-BP_K\,|\le R_B\tau_K,\qquad
R_B=\sqrt{R_\rho^4+R_{\rho'}^2}. \tag{6}
$$

式(6)来自准确恒等式 $|-\rho^2+i\rho_\phi|^2=\rho^4+\rho_\phi^2$，不是把实部和虚部的可能抵消当作小量。

任一实系数 Laurent 多项式 $A=\sum b_jz^j$ 可写为

$$
\operatorname{Re}A=b_0+\sum_{j\ge1}(b_j+b_{-j})\cos(2j\phi),\qquad
\operatorname{Im}A=\sum_{j\ge1}(b_j-b_{-j})\sin(2j\phi).
$$

把 $j\le M$ 的 cosine/sine 系数保留用于与原 $q$ 合并。若

$$
C_{>M}=\sum_{j>M}|b_j+b_{-j}|,\qquad
S_{>M}=\sum_{j>M}|b_j-b_{-j}|,
$$

则舍入包围后的有限高尾向量范数不超过
$\sqrt{C_{>M}^2+S_{>M}^2}$。这里所有 $j>M$ 直到式(4)端点的项都计入。

据此得到三个完整水平向量误差界

$$
\varepsilon_r=\operatorname{tail}(P_K)+\tau_K,
$$

$$
\varepsilon_{\rho r}=\operatorname{tail}(\rho P_K)+R_\rho\tau_K,
$$

$$
\varepsilon_B=\operatorname{tail}(BP_K)+R_B\tau_K. \tag{7}
$$

因乘以 $i$ 不改变模，$\varepsilon_{\rho r}$ 也支付 $i\rho e^{i\delta}$ 的误差。式(1)的六个 lift 尾分别由

$$
|f|\varepsilon_r,\quad |f_s|\varepsilon_r,\quad
|f|\varepsilon_{\rho r},\quad |f_{ss}|\varepsilon_r,\quad
|f_s|\varepsilon_{\rho r},\quad |f|\varepsilon_B \tag{8}
$$

支付，顺序为 $X,V,T,AA,VT,EE$。解析尾只在水平分量；高度没有这项尾。源码给每个水平分量各加相应向量模上界，是保守但有效的分量包围。

## 4. 准确径向重建与控制点处的抵消

对准确胞宽 $h=s_{i+1}-s_i>0$，Hermite 控制点为

$$
Y_0,\quad Y_0+\frac h5U_0,\quad
Y_0+\frac{2h}5U_0+\frac{h^2}{20}A_0,
$$

$$
Y_1-\frac{2h}5U_1+\frac{h^2}{20}A_1,\quad
Y_1-\frac h5U_1,\quad Y_1.
$$

先在原胞上以 $d(b_{j+1}-b_j)/h$ 形成真实 $s$ 导数，再限制到准确 $\chi$ piece，不把原导数误解释为子胞单位参数导数。$h$ 直接由 $(\alpha_{i+1}-\alpha_i)S+(\gamma_{i+1}-\gamma_i)$ 形成，能消去的 $S$ 相关性先准确消去。

若原胞跨过 $S-w$，在该准确符号位置切分。$\chi,\chi_s,\chi_{ss}$ 来自准确 smoothstep 控制点及其真实宽度导数。用准确 Bernstein 线性乘积构造

$$
f=\chi(R+S-s),\quad
f_s=\chi_s(R+S-s)-\chi,\quad
f_{ss}=\chi_{ss}(R+S-s)-2\chi_s.
$$

所以各径向系数次数至多为

| 物理量 | $X$ | $V$ | $T$ | $AA$ | $VT$ | $EE$ |
|---|---:|---:|---:|---:|---:|---:|
| 径向次数上界 | 6 | 5 | 6 | 4 | 5 | 6 |

升阶至6后，先在相同控制点合并原 $q$ 系数与第3节的 $j\le M$ 解析有限部分。例如高度组合为 $q_{Z0}+\chi H$、$q'_{Z0}+\chi_sH$、$q''_{Z0}+\chi_{ss}H$。$EE$ 的式(2)与完整 $BP_K$ 的有限部分也在控制系数处相加。这样保留真实的大数抵消；没有先对各分量分别形成全胞大盒再相加。

随后用准确二分参数的 de Casteljau 把每个 piece 分为 $r=2^\ell$ 个闭子胞。用于式(8)的 $f,f_s,f_{ss}$ 控制向量也先按相同子胞细分，再取绝对值。固定角时，完整场对 $s$ 仍为相应次数的多项式；解析 lift 的角误差不依赖 $s$。因此每个完整径向控制点均被“有限系数角盒加相应 scalar 控制值绝对值乘完整尾”包住。Bernstein 基非负且和为1，逐控制点区间的凸包包含整个闭子胞。

即使独立区间丢掉 $S/R$ 或重复系数间的相关性，它只会放宽包围。原共享二 jet 和 $\chi$ 的 $C^2$ 接口保证闭 piece 并集及原胞并集没有遗漏接缝。

## 5. 同角低模盒、全部原高模与四分之一域

选择 $1\le L\le M$。合并后的有限系数中，第 $0$ 至 $L$ 模用严格角区间变换；第 $L+1$ 至 $M$ 模在每个径向 Bernstein 控制点以系数绝对值和支付。然后加第3节的完整解析尾。前一尾来自原有限部分的剩余模，后一尾来自完整 Laurent 支撑的 $>M$ 部分和指数余项；两者不能互相替代或省掉。

令 $Q$ 为二幂，$\phi_k=2\pi k/Q$，$\Delta=\pi/Q$。除 $Q>4L$ 的无混叠条件外，明确要求

$$
\eta=1-\frac{(2L)^2\Delta^2}{2}>0. \tag{9}
$$

源码以向外下界检查式(9)；不把 $Q>4L$ 单独当作式(9)的充分条件。默认各层均满足两者。

对任一真实低模三角多项式 $p$，在 $|p''|$ 极大点取最近网格点，用二阶 Taylor 公式和三角 Bernstein 不等式
$\|p^{(4)}\|_\infty\le(2L)^2\|p''\|_\infty$，得

$$
\|p''\|_\infty\le\frac{\max_k|p''(\phi_k)|}{\eta}.
$$

再对任意 $|\phi-\phi_k|\le\Delta$，

$$
|p(\phi)-p(\phi_k)|
\le\Delta |p'(\phi_k)|
+\frac{\Delta^2}{2\eta}\max_j|p''(\phi_j)|. \tag{10}
$$

使用 R656/R670 的 f512 向外整数 twiddle 与 radix-two 变换包围三个网格量，再向外计算式(9)、(10)。这逐个覆盖控制系数区间中的每个真实多项式，不依赖普通 FFT 经验精度。

$X,V,AA,EE$ 的旋转架分量奇偶为 $(\cos,\sin,\cos)$，$T,VT$ 为 $(\sin,\cos,\sin)$。因此对 $\phi\mapsto-\phi$，前一组按 $D=\operatorname{diag}(1,-1,1)$ 变换，后一组按 $-D$ 变换。$N=T\times V$ 按 $D$ 变换，真实形算子在相应正交切架中由 $\operatorname{diag}(1,-1)$ 共轭；两个特征值及其绝对值不变。半周平移是水平半转。故覆盖 $[0,\pi/2]$ 即覆盖全角；端点闭弧保留，允许重叠。

对一个径向子胞和一个角闭弧，所有五个求曲率向量同时位于相同盒域上的向量区间。没有把一个角的 $V$、另一个角的 $T$ 或另一个径向位置的二导值当作同一点的真实 jet；区间运算只是在同一域上进一步放宽可能值。

## 6. 真第一基本形式与形算子

在上述同一盒内，定义

$$
E=V\cdot V,\quad F_1=V\cdot T,\quad G=T\cdot T,\quad
N=T\times V,\quad W=|N|.
$$

准确恒等式

$$
W^2=|T\times V|^2=EG-F_1^2 \tag{11}
$$

给两个独立区间，源码取其交。若 $E$ 或 $W^2$ 的下界不能证明为正，该盒记为未付，不在其上除以零，不以别处正下界替代。若两个同场区间没有交，则抛出算术错误，不把不一致当作成功。

可选输入是**本次同一准确候选**已经得到的 R670 完整首 jet 报告。只有其源码 SHA、bundle SHA、准确节点报告 SHA 及全部原胞索引一致时，才把其逐原胞 $E,W^2$ 下界与式(11)取交。那些下界本来对整个原胞成立，故对任何当前子盒也有效。这里不要求旧报告支持量已正；只使用它真正给出的同场下界。未提供该报告时算法完全独立。历史0241或077等不同候选的下界不能传入。

设 $E>0,W^2>0$。真实正交切架可取

$$
u_1=\frac V{\sqrt E},\qquad
u_2=\frac{\sqrt E}{W}\left(T-\frac{F_1}{E}V\right),\qquad
n=\frac N W.
$$

令 $e=N\cdot AA,\ f_1=N\cdot VT,\ g=N\cdot EE$，由第二基本形式的双线性性，实际对称形算子矩阵为

$$
B_{11}=\frac{e}{WE},\qquad
B_{12}=\frac{f_1-(F_1/E)e}{W^2},
$$

$$
B_{22}=
\frac{E\bigl(g-2(F_1/E)f_1+(F_1/E)^2e\bigr)}{W^3}. \tag{12}
$$

可能采用相反的 Weingarten 符号约定只会把整个矩阵乘以 $-1$，不影响本条绝对曲率结论。式(12)仅用真实 $V,T$ 和真实六 jet，不使用 $E=1,F_1=0,G=a^2$ 近似，也不使用 $a$ 的离散值作为几何归一化。

对任一真实对称 $2\times2$ 矩阵，准确有

$$
\|B\|_{\rm op}=
\frac{|B_{11}+B_{22}|+
\sqrt{(B_{11}-B_{22})^2+4B_{12}^2}}2. \tag{13}
$$

因为两个特征值为 $(\operatorname{tr}B\pm\sqrt{(B_{11}-B_{22})^2+4B_{12}^2})/2$，其最大绝对值就是式(13)。

另取 $a\ge|B_{11}|,\ b\ge|B_{12}|,\ d\ge|B_{22}|$。对任一单位向量 $u$，

$$
|u^\mathsf TB u|
\le
(|u_1|,|u_2|)
\begin{pmatrix}a&b\\b&d\end{pmatrix}
\binom{|u_1|}{|u_2|}
\le
\frac{a+d+\sqrt{(a-d)^2+4b^2}}2. \tag{14}
$$

源码对式(13)、(14)分别向外代入，再取较小上界。两者都是同一真实矩阵的有效上界，取小仍有效。对子盒取最大、再对 piece 取最大，即得第1节的 $\overline K_i$。只要存在未付浸入盒，就不把其余盒的最大值冒称全胞上界。

## 7. 完整闭面、cuff 的正角速度及相位

原端口给上半末圈准确 jet

$$
X(S,\phi)=R e_r(\Theta)+H e_z,\quad
V(S,\phi)=-e_r(\Theta),\quad AA(S,\phi)=0,
$$

$$
T(S,\phi)=R\rho e_\theta(\Theta),\qquad
W^2(S,\phi)=R^2\rho(\phi)^2. \tag{15}
$$

若包含该 cuff 的最后原胞已付一个严格下界 $m_W>0$，式(15)推出 $\rho$ 在全圆无零点。$\rho$ 连续且圆周平均值准确为1，所以其符号必为正，并有

$$
\rho(\phi)\ge \frac{\sqrt{m_W}}R>0. \tag{16}
$$

源码以向外除法支付式(16)，并可与直接角盒给出的 $\rho$ 下界取大。这一步只使用当前候选最后胞的已付结果，不把旧 core 的正性作为新事实。于是 $\Theta$ 是度为1的圆周微分同胚，两平圆盘能按原接口接入；盘心用 Cartesian 图，几何无参数退化。平盘的两个主曲率均为0。

core 的原镜像二 jet 条件给上下片 $C^2$ 接合。镜像和水平旋转保持绝对主曲率，材料角换元不改变几何主曲率。因此完整原闭面，以及按已付材料相位公式生成的全部 $t$，都由同一曲率上界覆盖。这里得到的是浸入；全局自交排除仍须同一候选的正支持等独立连续结论。

若还使用 [R661](R661-complete-nonplanar-activity-and-four-fixed-markers.md) 的固定四个 $p^4$ 帽标记，在其同一参数和 $H>1,R>9/20$ 条件下，各标记片的局部曲率上界为5；整个标记后场的条件上界是 $\max(\overline K,5)$。本条代码只输出这个条件局部曲率预算，不替它补付支持、非平面、全局嵌入或非全等。

## 8. 自适应范围、分块与有限预算的含义

每个加密层用 $(Q,r,L)$ 指定角中心数、每个准确 lift piece 的二幂径向子胞数及保留低模数。默认层为

$$
(256,1,24),\ (512,2,32),\ (1024,4,48),\
(2048,8,64),\ (4096,16,96).
$$

默认解析指数阶为 $K=12$，径向块最多4。选择比首 jet 更高的指数阶是为了控制 $|f_{ss}|\tau_K$ 可能的放大；没有把这个选择写成实际误差已经足够小的数值结论。

给定正有理曲率预算 $K_{\rm target}$，只有尚无有效上界或有效上界大于预算的原胞进入下一层。不同层对同一准确原胞产生的有效上界可取最小，因为它们分别包围整个原胞。达到预算的胞不重算。预算按命令行十进制文本转换为准确 Fraction，与实际 binary 上界的准确 Fraction 比较，避免把边界舍入误作满足。

一个完整胞有有限有效上界但超过预算，与存在未付浸入盒是不同状态。报告保留所有尝试、最好有效界、未达到预算的原胞、其最坏盒索引以及有限高模／完整解析尾的分量预算。完整覆盖成立但预算不成立时，仍可以报告真实较大的全域曲率界，不能将其改写成目标已经证明。

固定 $L,K$ 时，加密 $Q,r$ 不会消除单独支付的高尾地板。提高 $L$ 会减少第 $L+1$ 至 $M$ 模的独立绝对值损失；提高 $K$ 会缩小式(5)余项，但真实解析函数在 $>M$ 的 Fourier 高尾仍按式(7)另付，不能声称仅提高 $K$ 使所有尾归零。因此本条证明是每个返回界的可靠性定理，不保证任意候选或默认参数都能通过8.1。尾诊断可决定下一次应增加 $L$、$K$、径向或角分辨率；若 $>M$ 尾成为实际瓶颈，可在不改模型下扩大有限解析带宽或采用 R656 的直接完整角函数包围。未通过有限预算不证明真实曲率超标。

按径向块计算所有五个求曲率向量。每个控制点有7个径向 Bernstein 系数，cos 和 sin 两组的最大通道数分别为8和7。源码动态缩小块数，使通常参数下每组有限变换的实数组条目数不超过 $2^{20}$；过大的单个 $Q$ 至少处理一个径向子胞，并记录实际最大组条目数。解析完整 Laurent 系数是独立的一维小数组，不与全部径向子胞做张量积。此设计减少峰值内存，但不把条目限制冒作对任意 NumPy/平台的总 RSS 定理；Actions 报告记录真实峰值 RSS 与用时。

## 9. 实现、可信度和公开调用

完整源码：[actions_closed_curvature.py](../scripts/resume_20261120/actions_closed_curvature.py)。

源码 SHA-256：

8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385

该源码仅消费已冻结 [R670 入口](../scripts/resume_20261120/actions_closed_postprocess.py)，其 SHA-256 为

eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599。

R670 再绑定 R656 几何核、R662 准确径向读者、R665 完整 Laurent 源及 f512 向外算术。实际报告包含这些输入文件、当前 bundle、准确节点报告的 SHA。可选同候选首 jet 报告另记路径与 SHA；它不是必需的前置科学执行。

四则、平方、平方根、除法及控制点运算使用 f512 的 nextafter 向外 IEEE binary64 包围，准确 Fraction 参数先向外转为二进制盒；角网格使用已证明的严格 twiddle 变换。假设标准 IEEE 运算和非 FTZ，与 R656 相同。最小／最大、区间交和已成立上界取小只是选取已包围端点，不增加舍入风险。源码不会把普通数值曲率、旧 finite screen 或采样 $a$ 混进连续上界。

CLI 要求显式提供本次实际 bundle。以下路径是公开 replay 的 continue 布局；文件内容及 SHA 必须以本次 Actions 输出为准，不预设任何历史父 SHA：

~~~bash
python topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_curvature.py \
  --repo "$GITHUB_WORKSPACE" \
  --work "$WORK" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --manifest "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses.json" \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --taylor-degree 12 --radial-block 4 --target 8.1 --cells all \
  --out "$WORK/postprocess/current-full-curvature.json"
~~~

可选参数 --first-geometry-report 只接受同一当前 bundle／准确节点报告的 R670 完整报告，用途限于第6节的有效下界交。--manifest 可以重复；入口只登记位置来源与 carrier 身份，丢弃其中全部历史几何值。全域连续覆盖完成后，这些域内位置自然也被覆盖，无须再复制一份有限点扫描。

源码强制本仓库 GitHub Actions 环境后才开始科学读取与计算。本次准备只作源码静态阅读、语法树解析和文件 SHA 读取，没有执行新候选的数值测试，没有以独立 fixture 或旧父重跑作为登记条件。

本版明确仅支持本条原 $f,\chi$ 多项式模型。[R671](R671-exact-reference-tail-affine-lift.md) 的新 $f_\lambda,h_\lambda,k_\lambda$ 包含准确 $a,I$，不能直接沿用第4节 degree6 的径向证明。其角 Laurent 和真实形算子核可复用，但需另付 $a,I$ 至二导的严格径向控制与余项后才能形成新模型证书。本版报告显式写明不支持该扩充，避免给另一数学场继承错误证书。

最后，8.1 是本次可配置的计算预算，不是课题 reach 条件的新定义。实际 reach $\ge0.03D$ 必须把同一候选的完整曲率、直径、正定流支持及 [R650](R650-positive-definite-flow-support-reach.md) 的其余条件准确合并。本条报告始终把完整嵌入、reach、metric 证明标为未支付；只在真实完整覆盖返回后填写其应有的浸入和曲率范围。


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
