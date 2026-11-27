# R1125：原非分裂 Cartan 正规化子曲线 $X_{\rm ns}^{+}(47)$ 的全部有理点

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：已证明，使用完整公开精确计算。** 原完整曲线 $X_{\rm ns}^{+}(47)$ 恰有下列八个有理点，全部为有理 CM 点。
R1074 排除八盘之外的有理点，R1086 将候选送入同一个 CM 点的4513剩余盘，
R1122 与 R1124 分别关闭六个与两个完整原圆盘。
本篇汇合这些证明及其实际来源，并明确全部非QC关口；不作新的数学执行。
一般素数的 Serre 绝对一致性不由此完成。

## 1. 目标恰是完整原曲线

固定
$$
X=X_{\rm ns}^{+}(47),\qquad q=4513.
$$
这里没有辅助六水平、指定最低惯性型、旧 $X_1$ 商或有限高度窗口。
准确的固定曲线定理是
$$
X(\mathbf Q)=\{y_J:J\in\mathcal J\},
\qquad
\mathcal J=\{0,1728,-3375,8000,54000,287496,-12288000,16581375\}.
\tag{1125.1}
$$
$y_J$ 指原规范 CM Cartan 点，不只是一个 $j$ 值。

R1074 §6.1 已按经典十三项有理 CM 表逐项核 $47$：
八项的底域 $-3,-4,-7,-8$ 在 $47$ 惰性，给唯一原有理 CM 点；
其余五个底域在 $47$ 分裂，不给原有理 nonsplit-Cartan 点。
原 cusps 是一个次数23的 Galois 轨道，故没有有理 cusp。
所以 (1125.1) 的右侧确实在 $X(\mathbf Q)$ 中且八点互异。

这一存在性与 CM locus 的穷尽性独立于后面的 QC 数值。
对某条 $E/\mathbf Q$，若其模47像落入 nonsplit normalizer，
其真实47层给原 $X(\mathbf Q)$ 的点；由 (1125.1)，$j(E)$ 必为 CM。
若另表述“所有非 CM 的模47像均满射”，还应引用其它 maximal-subgroup
情形各自的已付排除；本链单独证明的是完整 nonsplit-normalizer 情形。

## 2. 八盘之外的排除覆盖所有有理点

### 2.1 原47局部模型没有遗漏圆盘

R1065–R1066 的原 regular proper 模型，加 R1072 的完整认证，给
$$
\mathcal M^{\rm sm}(\mathbf F_{47})
 =\coprod_{s\in\{0,9,10,36,44\}}\mathbf A^1_s(\mathbf F_{47}),
\qquad \#\mathcal M^{\rm sm}(\mathbf F_{47})=235.
\tag{1125.2}
$$
每个 $X(\mathbf Q_{47})$ 点在这个范围内。
原 $47$ 处整 $j$ 是局部 nonsplit-normalizer 结构推出的结论，
不是对待排有理点另加的假设。

R1072 保 $j=1728$ 的两个实际 quartic twists及中心合并，
$j=0$ 的三次 coarse 商，以及所有其它 supersingular 模型。
故235是原 coarse 圆盘数；不是把某个 fine 参数图当成全曲线。

### 2.2 每盘的全局候选是真唯一、同一规范

实际原 cusp 模块由 R1072 完整读取为
$$
V=\bigoplus_{R\in\{26,28,30,32,34,36,38,40,42,44\}}V_{\omega^R}.
$$
十个角色全部 Bernoulli-good。R1067 给所有原有理点的
$p$-only 标签，包含在其它素数非整 $j$ 的情形；
R1069 §3 给这全部实际 $V$ 的 global-to-$47$-local 同构。
因此没有未付的类群或2/3支撑自由度。

R1071 的真实函数/对数/Miller相位与 R1072 的完整有限读取，
为235个盘给235个互异的十维全局候选。
这一步仅区分圆盘；不把整个盘上的局部常值标签当成点的单射。

### 2.3 辅助283排除恰227盘，留下的八项是实际CM盘

R1073 给全部 affine/cusp 标签的同一 normalization，
R1074 §§3–5 的完整辅助枚举只留下下表八个原候选。
所有角色都在同一个辅助点比较；不是逐角色各挑一个点。

| 原 ID | $J$ | CM 阶判别式 |
|---:|---:|---:|
| 0 | 0 | $-3$ |
| 76 | $-3375$ | $-7$ |
| 77 | $-12288000$ | $-27$ |
| 100 | $16581375$ | $-28$ |
| 108 | $8000$ | $-8$ |
| 141 | $1728$ | $-4$ |
| 196 | $287496$ | $-16$ |
| 220 | $54000$ | $-12$ |

R1074 的原 CM first-lift/gradient 与独立 constant-profile 复核，
将八个标签逐项识别为同一 $y_J$ 的原47圆盘。
所以对于任意原 $x\in X(\mathbf Q)$，已有唯一同一个 $J$ 使
$$
x\in\mathcal U_{47,J},\qquad \Phi_x=\Phi_{y_J}\quad\text{on full }V.
\tag{1125.3}
$$
前式是实际 tube；后式是全局标签，不是仅某个有限域坐标。
此外 R1074 §7 用独立 Burnside 点数279再比较实际标签像279，
支付 $283$ 的同一点识别。它不是 (1125.3) 的额外未证前提。

## 3. 4513转移锁定同一个原点，不只是同一个j

R1086 独立计数原 $\#X(\mathbf F_{4513})=5453$，
其实际完整标签像也有5453个值。
前者由全部一般模型、特殊 twists、scalar/反射 necklaces及23cusps
的粗轨道重数给出，未从标签像反推点数。

因此该标签图在全部原 $X(\mathbf F_{4513})$ 上单射。
虽然圆单位的 $R=36$ 读数为零，比较仍保该坐标的零条件；
没有非法除零，也没有删除可能约到 cusp 的有理点。

由 (1125.3) 的同一个全局标签及好约化相容性，得
$$
\operatorname{red}_{4513}x=\operatorname{red}_{4513}y_J
\quad\text{于原曲线，不仅于 }j\text{ 直线}.
\tag{1125.4}
$$
所以任意原有理点已同时落在同一 $J$ 的坏47 tube及好4513剩余盘。
八盘之外的排除至此完全支付，不需要另外的有限辅助筛选。

## 4. q处使用的整盘与参数覆盖

R1103 §2 证明 $j$ 在这八个**规范 CM Cartan** 点的好模型上 étale。
一般 $j$ 的有效自同构平凡；在 $0,1728$ 处，
整个 CM 单位群保持规范 Cartan，coarse 商与 $j$ 端的同一稳定子相消。
故
$$
z=j-J,\qquad U_{q,J}(\mathbf Q_q)=\{z=qt:t\in\mathbf Z_q\}
\tag{1125.5}
$$
是真正完整原剩余盘的整参数化。

R1105 的三种切向读取保持这一 coarse 规范：
一般点用原 KS 点值，高斯点用 fine 一阶及 Jacobian，
三次点用 fine 二阶及 Jacobian。没有再除一次2或3。
$-7,-28$ 点在4513超奇异不妨碍这个 coarse 参数结论；
其实际 necklace 已由 R1086 固定，算法不任取其它稳定 Cartan。

## 5. 全部非q项已经在实际候选上为零

本节是进入 QC 方程的全局关口，而非由数值高度单位自动得到。

### 5.1 坏47：整个Cp管域的raw支撑避让

R1074 §9.1 给实际 coarse 完成环上的
$$
(j-J)/47^{e_J}=a_J z+47R_J(z),\qquad
e_J=1,2,3,\quad a_J\text{ 为单位}.
$$
因此 $j$ 在整个 $\mathbf C_{47}$ tube 上单射且 étale，
包含 ramified fine lifts。这个结论的高项控制来自实际整 invariant chart，
不只是特殊纤维上的有限值。

原 $Z_A=13R_0+4R_2$、$Z_B=2R_4-7R_0$ 的每个支保持$j$且无对角成分。
故 Fix及两次像的全部几何支撑避开 tube。
它们都是原对称 trace-zero 角组合；
即使 degree不为零，Lefschetz给 $\deg\operatorname{Fix}Z=2\deg Z$，
所以
$$
P=x-y_J,\qquad D=\operatorname{Fix}Z-Zx-Zy_J
$$
仍是次数零除子。

$x,y_J$ 通过同一个光滑特殊点，故 $P$ 的 admissible vertical correction
可取零；$D$ 的全部闭包避该点，水平交数也为零。
R1074 §§9.2–9.3 保有限扩张、所有共轭和实际Néron规范，给 $h_{47}(P,D)=0$。
不能把仅 $j$ 相同或仅同一不可约分量当成这个证明。

### 5.2 其它好素数，包含2、3和非整j

R1103 §6.1 使用 R1067 的原 smooth proper 模型，
将对称水平对应的 Cartier 线丛 $\mathcal B$ 整地刚化。
写 $\mathcal B_y=(\operatorname{id},y)^*\mathcal B$、
$\mathcal K=\Delta^*\mathcal B$，实际线丛为
$$
\mathcal L=\mathcal B\otimes
 \operatorname{pr}_1^*(\mathcal B_y\mathcal K^{-1})
 \otimes\operatorname{pr}_2^*\mathcal B_y^{-1}.
$$
同一 $\mathcal B(y,y)$ 评价给整轴和对角平凡化，
在 $(y,y)$ 相容且规范向量满足 $\sigma(y)=1$。
这是 R148/R43 的同一个实际范数向量，不仅是两个 Picard 类相等；
没有未核的 $\ell$-次幂标量。

$\ell=2$ 的交换符号可先用 $2Z$ 平方，不在整模型上除二或平均，
最后在 $\mathbf Q_q$ 值域线性除回。
原非$q$ Néron splitting 在整可逆向量上为零，
于是所有 $\ell\ne47,q$ 都有 $h_\ell(P,D)=0$。
properness覆盖约到 cusp 的截面，也允许 $j$ 有极。
全部23cusps和非零degree始终保留，不能套用principal组合的degree-zero特例。

合两部分，对 (1125.3)–(1125.4) 的每个原有理候选，
$$
h_\ell(P,D)=0\qquad(\ell\ne q).
\tag{1125.6}
$$
这里不再有“非q高度常数待定”的额外关口。

## 6. 高度与对数均在同一个原整全格

R1080 的原完整Jacobian rank为73。
R1081/R1096支付原未分歧整 Hecke 序及 $H=T_3+T_5$ 生成性。
R1090 的95来源和23留数的单位minor给真正73维整Hodge格；
未通过一个分母未知的Chen同源改变整格。

令 $u_4=23y_{1728}-C_\infty$、$B_q=q+1-T_q$、$P_0=B_qu_4$。
R1089及R1093证明
$$
M=(J(\mathbf Q)/\mathrm{tors})\otimes\mathbf Z_q=\mathbb T P_0,
\qquad\log M=q\operatorname{Lie}J(\mathbf Z_q).
$$
这用全部28域块的实际非零首log及完整rank73，
不是仅十六个一次块或一个循环子模的未饱和性。

R1102读取全部73个真实高度基值，保所有奇好素、2、47和移动平方项。
同一补空间 $W$ 和符号下，实际归一为
$$
q^{-1}h(SP_0,TP_0)=\operatorname{Tr}(KST)\pmod q,
\qquad K=\kappa/a,\quad a=(T_2-1)/2.
\tag{1125.7}
$$
R1106给原全部角在此帧中的作用；
R1120给实际带符号CM类坐标，其中 $c_{-4}=B_q^{-1}$，并非1。
所有 fixed-cycle 的 $1/2,2/3,1/23$ 在程序中保留。

这些是定义完整QC函数所需的原格、配对和坐标。
$K$ 的单位性本身不排盘，不能代替下面两行的实际读数。

## 7. 第三类值的规范不是额外假设

R1103 §3 先用原整双极核、完整Galois多重集和RR lift证明
$$
\overline{\omega_D^W}=N^{-1}d\log\bar f,\qquad
\operatorname{div}\bar f=N\bar D,\quad N=\#J(\mathbf F_q),\quad q\nmid N.
$$
继而用原 $C=\bar T_q$、$1-C=\bar B_q$ 可逆，证明 prescribed-residue
Cartier-fixed微分恰等于该规范约化。
因此R1118计算的是原高度里的 $\alpha_{Z,y}$，不是另选的微分补线。

R1121读取六盘十二个值；R1123读取特殊两盘四个值。
每条来自自己的完整 $6D_{Z,y}$，包括全部cusps、closed points和重数，
最后准确除六；不能用其它除子在同一目标的数值替代。
共同Cartier与Jacobi的 $1-B_q(H)$ 在原73维帧上比较完整矩阵hash，
不是仅比谱或行列式。
旧Miller、旧模平方运行的是否后来完成，已不是本链的新缺口。

## 8. 八个实际首层矩阵与整个原盘的唯一性

对 $x(t)$ 如 (1125.5)，令 $P=x(t)-y_J$，
按完整对数同构写 $A_J(t)$。
R1103 §5 证明
$$
A_J(t)\equiv t b_J\pmod q
$$
并定义整 restricted-analytic 原函数
$$
f_{Z,J}(t)=q^{-1}\{h(P,D_{Z,J}-ZP)-h_q^W(P,D_{Z,J}-ZP)\}.
$$
式(1125.6)说明每个正在研究的有理候选满足 $f_{Z,J}(t)=0$。

单积分的 $q^n/(n+1)$ 和双积分的
$q^{r+s+2}/((r+1)(s+1))$ 估值控制全部高项，
所以在整个 $t\in\mathbf Z_q$ 上有
$$
\bar f_{Z,J}(t)=t(B_{Z,J}+A_{Z,J}t),
$$
$$
A_{Z,J}=-\operatorname{Tr}(Kz_Zb_J^2),\qquad
B_{Z,J}=\operatorname{Tr}(Kb_Jd_{Z,J})-\alpha_{Z,J}.
\tag{1125.8}
$$
没有截断后未估计的尾，也没有未知缩小半径。

若两个真实多项式的gcd是$t$且至少一个 $B_{Z,J}$ 非零，
共同整零必须先落在 $t\equiv0\bmod q$。
此处该行导数为单位，Hensel给唯一提升。
已知原点 $y_J$ 对应 $t=0$，并准确满足函数等式，故唯一零就是它。
这是整个原剩余盘的结论，不仅是某个更深邻域。

R1122 实际支付六盘，R1124 实际支付最后两个盘。
全部矩阵的行次序为 $Z_A,Z_B$，列次序为 $A,B$：

| 原 ID | $A_A$ | $B_A$ | $A_B$ | $B_B$ | 实际行列式模4513 | 来源 |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 508 | 508 | 3609 | 2277 | 294 | R1124 |
| 76 | 3664 | 2667 | 4252 | 828 | 2141 | R1122 |
| 77 | 1549 | 515 | 3390 | 3945 | 884 | R1122 |
| 100 | 3881 | 2348 | 128 | 707 | 1790 | R1122 |
| 108 | 948 | 1924 | 2173 | 3060 | 1720 | R1122 |
| 141 | 2745 | 1547 | 7 | 3142 | 3157 | R1124 |
| 196 | 4320 | 700 | 1825 | 1173 | 3453 | R1122 |
| 220 | 2135 | 1366 | 3108 | 2519 | 4287 | R1122 |

这些值来自两次不同范围的完整成功请求，没有在本篇重算。
八盘均实际给 rank2、gcd$=t$、common roots$=[[0,1]]$，
且至少一个线性系数为单位。
最后两盘的完整新来源为
[run46000409994](https://github.com/Rogerhu12/math-research-public/actions/runs/46000409994) /
[job140510309243](https://github.com/Rogerhu12/math-research-public/actions/runs/46000409994/job/140510309243)，
source b0ffe03ad95291999ef104b217cd30b3cdbad93a，
数学117.687072366秒；全部步骤 success。
完整 completed 的 canonical SHA 为
23f2137019e4a98e2d0fb1976872d4233cba6f4e34e165d830167b1de6cd70cb。
两盘新请求只输出0、141，没有重算六个已成盘。

现在任取 $x\in X(\mathbf Q)$：
(1125.3)选出唯一 $y_J$，(1125.4)把它送入该点的完整$q$盘，
(1125.6)给原QC消失，(1125.8)及上述全盘判据迫
$x=y_J$ 于 $X(\mathbf Q_q)$，因而也于 $X(\mathbf Q)$。
另一包含方向已在§1付清，故 (1125.1) 成立。

这条收束不要求另一个整$j$条件、固定二次域、特定惯性子群、
未知半径、更深未算 jet、额外高度饱和或待测局部常数。
它不证明任何一般素数范围的 Serre 绝对一致性；该主目标继续。

## 9. 可直接审核的主要入口

- [R1072 全原圆盘与实际角色](R1072-certified-original-p47-cuspidal-disk-labels.md)。
- [R1074 八盘之外排除及§9坏47项](R1074-certified-original-p47-eight-CM-disks.md)。
- [R1086 同一原4513点的完整转移](R1086-certified-original-p47-ell4513-same-CM-transfer.md)。
- [R1093 全原MW整格](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)。
- [R1102 全73首高度](R1102-certified-original-level47-complete-first-global-height.md)。
- [R1103 原参数、规范第三类值、整尾与§6.1非q项](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)。
- [R1120 实际完整CM坐标](R1120-certified-original-full47-signed-CM-coordinates.md)。
- [R1121 六盘十二值](R1121-certified-original-twelve-short-Cartier-values.md)。
- [R1122 六盘已完成判据](R1122-certified-original-six-complete-CM-disks.md)。
- [R1123 特殊两盘四值](R1123-certified-original-four-special-CM-Cartier-values.md)。
- [R1124 特殊两盘已完成判据](R1124-certified-original-two-special-CM-disks.md)。

root/global已全文回读以上主链中 R1072/1074/1086/1093/1102/1103/1120/1122，
并核本轮四条第三类实际完整receipt、两盘QC完整receipt及同源哈希。
o1另逐项纸核whole-C47 raw支撑、非q范围、4513完整coarse盘与simple Hensel接口。
本篇汇合已有证明和来源，不构造新的未证跨曲线身份，
不把一般素数的未知绝对界从固定47结论中删除。
