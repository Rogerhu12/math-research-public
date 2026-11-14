# R707 — 层 41 的全部 129 个剩余盘与八个有理 CM 点

日期：2026-11-14。状态：**已证明（固定层 41 的完整有理点分类）**。
本篇从现存原始逐盘证明及其实际证书重建分类；最后一盘使用公开
Actions [43589296050](https://github.com/Rogerhu12/math-research-public/actions/runs/43589296050)
及 [R709]。不使用遗失的 R583 总结作为数学前提。

## 1. 定理

令 $X=X_{\mathrm{ns}}^+(41)$ 为无定向非分裂 Cartan 正规化子模曲线。
则 $X(\mathbb Q)$ 恰含八个点，均为 CM 点，没有有理尖点。其 CM 序判别式和
准确 $j$ 值为

| CM 判别式 | 准确 $j$ 值 |
|---:|---:|
| $-3$ | $0$ |
| $-7$ | $-3375$ |
| $-11$ | $-32768$ |
| $-12$ | $54000$ |
| $-19$ | $-884736$ |
| $-27$ | $-12288000$ |
| $-28$ | $16581375$ |
| $-67$ | $-147197952000$ |

这八个点各占一个实际的 $47$-进剩余盘；其余 $121$ 个盘均不含有理点。
普通盘为 $19=16+3$，超奇异盘为 $110=105+5$，其中每个等式的第二项
是所保留的 CM 点数。两个固定真实方向
$$
F_2=27T_2+4,\qquad F_3=9T_3+2
\tag{707.1}
$$
已足以给出上述上界和逐盘唯一性；无需声称全部 53 个局部高度方向已经求出。

特别地，非 CM 的 $\mathbb Q$ 上椭圆曲线不能在模 $41$ 层具有这种
有理非分裂正规化子结构。本定理只解决层 $41$，并不证明一般素数的
Serre 绝对一致性；主课题保持 OPEN。

## 2. 同一曲线的完整覆盖

### 2.1 真实模型和全部有限域点数

[R102] 在真正的 $X$ 上构造
$$
g(X)=54,\quad \deg D_{\mathrm{cusp}}=20,\quad
\mathcal L=K_X+D_{\mathrm{cusp}},\quad \deg\mathcal L=126,
$$
以及 820 个不同剩余点上的实际完整评价模型。相应截面维数是
$$
\dim H^0(\mathcal L)=73,\quad
\dim H^0(2\mathcal L)=199,\quad
\dim H^0(3\mathcal L)=325,\quad
\dim H^0(4\mathcal L)=451.
$$
所选基的模 47 单位子式、全部真实 $41$-挠点、Weil 配对及 Frobenius
下降都已在该原证书中核验。因为 $\deg\mathcal L\ge 2g+1$，这些坐标给
光滑粗模曲线的闭嵌入。实际 Hecke 局部因子的迹为 $-81$，故
$$
\#X(\mathbb F_{47})=47+1-(-81)=129.
\tag{707.2}
$$

[R228] 在完整射影坐标中去重并验证了五个超奇异剩余
$$
j=0,9,10,36,44
$$
之上各 22 个有理粗点，共 110 个。这里没有把重复栈标签重复计数：
$j=0$ 的 63 个普通有理评价行按三重表示合成 21 点，再加入一个真正椭圆
粗点；$j=36$ 的 40 行按二重表示合成 20 点，再加入两个真正椭圆粗点。
有非平凡稳定子的点使用非零粗图坐标，不使用在这些点为零的栈评价行。

[R231] 通过各自真实 $41$-挠点、Frobenius 和唯一有理项链构造其余 19 点，
其剩余 $j$ 为
$$
\{1,5,7,11,12,15,19,24,27,28,30,32,38,39,40,41,43,45,46\}.
\tag{707.3}
$$
这 19 点彼此不同，也与前述 110 点不同。于是构造出的 129 个非尖点已达到
(707.2) 的精确总数，穷尽 $X(\mathbb F_{47})$，同时排除了遗漏的有理尖点。

### 2.2 从有限域覆盖到所有有理点

$47\ne41$ 是 $X$ 的好约化素数。光滑适当模型使任意
$P\in X(\mathbb Q)\subset X(\mathbb Q_{47})$ 延拓为整点并约化到
$X(\mathbb F_{47})$。每个有理剩余点的形式邻域都有已构造的单位 étale
参数 $z$，其整个有理剩余盘是 $z\in47\mathbb Z_{47}$。
[R228] 的有理中心由真实曲线的 Hensel 提升取得，不是将两个射影点取平均；
[R231] 的普通中心也保留实际物理坐标及 Frobenius。故下面 129 个盘的处理
确实覆盖全部有理点，没有未处理的另一个参数分支。

## 3. 必要 QC 方程及有限精度为何足够

### 3.1 全局规范和共同坏分量

[R94]、[R121]、[R133] 固定实际 Hecke 代数
$$
E=\prod_{i=1}^8K_i,\qquad
([K_i:\mathbb Q])=(2,3,3,4,4,8,12,18),
$$
及 $J(\mathbb Q)\otimes\mathbb Q=EB$ 的真实基。
[R121] 的 $47$-饱和对数格和 [R222] 的完整 Miller 计算给出同一 Poincaré
高度的全部 54 个配对系数。固定层 41 的实际秩与饱和结果是已经证明的
输入；没有把一般层的 R616 条件当作本定理已经自动成立的条件。

取 $b=P_{-3}$、$C_P=P-b=a(P)B$，令 $U_b=[20b-D_{\mathrm{cusp}}]=r_3B$，
并沿用 $\eta_{D,2F}=\xi_FB$。[R228] 的真实全局项为
$$
G_F(P)=\operatorname{Tr}_{E\otimes\mathbb Q_{47}/\mathbb Q_{47}}
\bigl(s(800F\,a(P)^2+(80Fr_3-20\xi_F)a(P))\bigr).
\tag{707.4}
$$
所有 54 个坐标、实际 Chow–Heegner 平移及 $800=2\cdot20^2$ 均保留。
[R304] 已给全部 129 盘的真实全局多项式；下面局部输入仍须由各盘自己的
完整主函数 Norm、相容连接和规范纤维取得，不能从 (707.4) 代替。

令 $\Lambda_F=\lambda_{47}(\sigma_{F,b})$ 为 [R148] 的基点刚性化规范截面
高度，并记
$$
\rho_F=G_F-800\Lambda_F.
\tag{707.5}
$$
同一有理点在全部方向使用同一个坏分量标签
$$
\iota\in\{0,3,28,32\}.
$$
[R134]、[R135]、[R228] 给出必要条件
$$
\rho_{F_2}(P)=\omega_{2,\iota},\qquad
\rho_{F_3}(P)=\omega_{3,\iota}.
\tag{707.6}
$$
在 $Q=47^4=4879681$ 下，这两个真实靶向量依次为
$$
(\omega_{2,\iota})_\iota=(0,0,0,0),\qquad
(\omega_{3,\iota})_\iota=(0,0,2621472,2621472)\pmod Q.
\tag{707.7}
$$
F2 的靶准确为零；F3 的表格是同一规范的靶值模 $Q$。
两标签共享一个 F3 靶值只表示这两个方向暂时不区分标签，不产生两个点。

普通盘和非 CM SS 盘的中心高度来自各自的真实
$$
\operatorname{div}\Phi_{P-b}=m(P-b)-A_1(t)
$$
及完整第一变量 Norm。固定典范微分更换、切向换参、重复 Hecke 支、
相交支撑和真实粗参数的处理全部保留在逐盘原证书中。真实 CM 点可以使用
已证明的全局互反作已知锚；没有给非 CM 的局部中心假定一个 CM 高度。

### 3.2 整盘尾界

先在当前实际单位参数 $z$ 中完成所有必须的 Laurent 相消和有限平坦
极点条件，再用 $y=z/47$。逐盘原证明给
$$
v_{47}\!\left([z^n]\Lambda_F\right)
\ge-\lfloor\log_{47}n\rfloor-v_{47}(n).
\tag{707.8}
$$
其原因是单位 RR 逆、代数单位分母和完整 Hecke 迹都保持整级数；可能的
非整输入为一个正规第二类微分的原函数，之后高度再积分一次。
对所有 $n\ge4$，
$$
n-\lfloor\log_{47}n\rfloor-v_{47}(n)\ge4,
\tag{707.9}
$$
且左端趋向无穷。因此局部三次多项式代表整个闭盘上原高度的模 $Q$ 值。
在 $47^r\le n<47^{r+1}$ 时可用下界 $47^r-2r$；$4\le n<47$
直接成立。这覆盖全部尾，不能用有限个代入值替代。

原全局形式的一次和二次系数具有已核的 47 整除性。全纯 Abel 原函数的
$z^n$ 系数赋值至少 $-v_{47}(n)$，故遗漏的 Abel 项及保留乘积中的
五、六次项在所需精度下不贡献；全局四次项仍保留。相减后的各
$\rho_{F_i}$ 系数全部可除 47，所以
$$
\rho_{F_i}(y+47^3t)\equiv\rho_{F_i}(y)\pmod{47^4}
\quad(t\in\mathbb Z_{47}).
\tag{707.10}
$$
未知真根的更高位不会改变本篇所用的 F3 非零差。

### 3.3 全部根的逻辑

对 $f_2=\rho_{F_2}/47$ 的整收敛解析函数先枚举全部模 47 根。
无残根即整盘无根；每个单位导数残根由解析 Hensel 引理恰有一个
$\mathbb Z_{47}$ 提升，没有其它分支。其前三位 $y\bmod47^3$
足以由 (707.10) 检验每个 F3 靶。若四个共同标签的差全部非零，该 F2
分支不含满足 (707.6) 的点。

唯一需要另作多重根分析的已封存情形是 [R625] 的 SS_j0_15：
$$
f_2(y)\equiv10(y-28)^2\pmod{47},\qquad
f_2(28)\equiv658=14\cdot47\pmod{47^2}.
$$
因 $f'_2(28)\equiv0\pmod{47}$，对全部 $t\in\mathbb Z_{47}$ 有
$$
f_2(28+47t)\equiv658\not\equiv0\pmod{47^2}.
$$
这排除整个唯一二重残根管，不误用简单根 Hensel 定理。

最后，某条保留分支与已知有理 CM 点有相同简单残根时，(707.6) 由全局
互反准确成立，故该 CM 点就是这一**唯一的解析 F2 根**。这给真正点的相等；
不从仅有模 $47^4$ 坐标相同推出点相同。

## 4. 八个真实 CM 点、身份和唯一性

以下坐标均是各原文绑定的 R228/R231 实际单位图的 $y=z/47$。
导数一栏是 $f_2=\rho_{F_2}/47$ 在相应残根处的模 47 导数。

| 判别式 | 实际圆盘 | 保留 $y\bmod47^3$ | 导数模 47 | 实际坏标签 | 原始身份及局部证明 |
|---:|---|---:|---:|---:|---|
| $-3$ | SS_j0_10 | 0 | 44 | 0 | [R321]、[R328] |
| $-7$ | SS_j9_19 | 57595 | 1 | 28 | [R321]、[R323]、[R325] |
| $-11$ | ORD_j38 | 94227 | 19 | 32 | [R237]、[R277]、[R310] |
| $-12$ | SS_j44_02 | 96923 | 26 | 3 | [R321]、[R324] |
| $-19$ | ORD_j39 | 9310 | 26 | 3 | [R237]、[R278]、[R303] |
| $-27$ | SS_j9_11 | 75213 | 18 | 28 | [R292]、[R314]、[R313]、[R316] |
| $-28$ | SS_j10_05 | 86022 | 13 | 32 | [R314]、[R318]、[R319] |
| $-67$ | ORD_j40 | 13002 | 2 | 32 | [R237]、[R279]、[R309] |

### 4.1 身份不是依据同一个剩余 $j$ 猜测

$-3,-12,-7$ 的点为原 $b,u,c_7$。其确切关系 $T_2b=3u$、实际
CM 模型、完整 $41$-层运输与全部 73 坐标识别见 [R148]、[R321]。
[R237] 分别从判别式 $-11,-19,-67$ 的类数一 CM 序与真实项链取得
三个普通有理点，证明实际 divisor 类
$U_D=[20P_D-D_{\mathrm{cusp}}]=r_DB$，并在全部 73 坐标中确定其局部盘。
它们不是为配合计算根才选取的浮点近似。

余下两点由 [R292]、[R314] 的真实同源关系识别：
$$
T_3b=b+3v,\qquad j(v)=-12288000,\qquad D(v)=-27,
$$
$$
T_2c_7=2c_7+w,\qquad j(w)=16581375,\qquad D(w)=-28.
\tag{707.11}
$$
这里保留所有核分支、微分尺度、Frobenius 与原 Weil 配对；
三个非水平 T3 目标分别实算成同一个 $v$，T2 的非水平目标实算成 $w$。
全 73 坐标在原 110 个 SS 盘中各有唯一匹配。特别是
$c_7$ 与 $v$ 虽同余 $j=9\pmod{47}$，却是不同实际盘
SS_j9_19、SS_j9_11，没有合并。

这八个 CM 序均有类数一，41 在相应 CM 域惰性。其 CM 作用稳定的无定向
非分裂项链给有理正规化子结构；上述实际模型与同源计算再固定其本篇使用的
具体点。八个准确 $j$ 值两两不同，故八点互异。

### 4.2 逐个除掉同盘多余根

基点盘 [R328] 有 $f_2(y)\equiv44y\pmod{47}$，所以只留 $b$。
其余七个 CM 盘的 F2 各有两个简单根。下表列出被 F3 排除的另一根；
两列非零差分别适用于标签 $0,3$ 和 $28,32$，均模 $Q$。

| 圆盘 | 另一根 $y\bmod47^3$ | F3 差：标签 $0,3$ | F3 差：标签 $28,32$ | 证明 |
|---|---:|---:|---:|---|
| SS_j9_19 | 84793 | 3159951 | 538479 | [R325] |
| ORD_j38 | 62093 | 53063 | 2311272 | [R310] |
| SS_j44_02 | 86091 | 687375 | 2945584 | [R324] |
| ORD_j39 | 85546 | 3781150 | 1159678 | [R303] |
| SS_j9_11 | 9440 | 3810760 | 1189288 | [R316] |
| SS_j10_05 | 75296 | 3222508 | 601036 | [R319] |
| ORD_j40 | 61424 | 850512 | 3108721 | [R309] |

保留根处的实际 CM 点满足原全局必要方程。上表与全部非零导数因而证明
八个 CM 盘各恰含这一个有理点，既不遗漏同盘的另一分支，也不把同靶标签
重复计作点。

## 5. 非 CM 盘的原证明和例外图

### 5.1 19 个普通盘

无 F2 残根的八盘及其 $\rho_{F_2}/47\bmod47$ 的二次系数和判别式为

| 圆盘 | $[c_0,c_1,c_2]$ | 判别式模 47 | 原证明 |
|---|---|---:|---|
| ORD_j01 | $[29,21,45]$ | 15 | [R284] |
| ORD_j05 | $[20,44,31]$ | 20 | [R262] |
| ORD_j11 | $[28,41,34]$ | 35 | [R268] |
| ORD_j24 | $[18,3,42]$ | 40 | [R272] |
| ORD_j28 | $[43,25,1]$ | 30 | [R285] |
| ORD_j30 | $[37,31,7]$ | 19 | [R274] |
| ORD_j41 | $[27,27,23]$ | 31 | [R280] |
| ORD_j43 | $[46,26,2]$ | 26 | [R281] |

这些判别式全部为非平方，故八个整盘排除。另八个普通非 CM 盘的所有
F2 根及 F3 差如下；每个条目都来自各自的完整 Norm、实际中心和整盘证书。

| 圆盘 | F2 两根 $y\bmod47^3$ | F3 差对 $(0/3,\;28/32)$，按根顺序 | F3 证明 |
|---|---|---|---|
| ORD_j07 | 35962, 279 | $(3150363,528891);\ (4828921,2207449)$ | [R291] |
| ORD_j12 | 69875, 15127 | $(2462612,4720821);\ (718865,2977074)$ | [R296] |
| ORD_j15 | 73049, 89143 | $(2697565,76093);\ (4334434,1712962)$ | [R297] |
| ORD_j19 | 34718, 20625 | $(2673219,51747);\ (4327760,1706288)$ | [R298] |
| ORD_j27 | 20183, 78611 | $(1582443,3840652);\ (2924246,302774)$ | [R299] |
| ORD_j32 | 75915, 39733 | $(964863,3223072);\ (3660266,1038794)$ | [R300] |
| ORD_j45 | 87914, 80131 | $(3779364,1157892);\ (3373519,752047)$ | [R308] |
| ORD_j46 | 84194, 54740 | $(1266180,3524389);\ (189786,2447995)$ | [R307] |

所有差均非零，排除这八盘。加上 §4 的三个普通 CM 盘，恰为全部 19 盘。
R307/R308 表后曾有一处标签笔误；本篇直接使用其实际同标签差值表，
不依赖那句文字。其 F3 剩余表实际是标签 $0,3$ 无根、标签 $28,32$
仍有残根，后者同样被本表排除。

### 5.2 必须保留的特殊局部处理

下述原证明负责保证 §3.2 的假设确实适用于全部表中条目；它们不能被
“其余盘同理”略去。

* ORD_j28 使用 [R285] 的真实单位框架，原非单位 $f_c$ 不被倒置；
  原整主函数的最终 $f_c$ 指数准确为零。[R282] 的 candidate11 典范除子
  避让全部 129 盘，典范更换的互反项与规范纤维项相消，故 ORD_j45
  没有产生可调高度常数。
* 对 [R278] 以及 [R335 补充](R335-eta-B-removable-quadratic-denominator-and-two-F2-roots.md)、
  [R336 补充](R336-removable-fixed-fraction-repair-and-independent-audit.md)
  等辅助分式的可去共零，完整真实支撑不变，单位新分母与旧分式由全局
  交乘恒等式识别。度数至多 $5\deg\mathcal L=630<820$，忠实求值
  及逐位提升保证同一微分；并非删去失败的单位性断言。
* $j\equiv9$ 的原求值纤维碰撞由 [R399] 的两次真实翻转处理，全部新增
  初始主函数及整数指数保留。[R382]–[R385]、[R387]、[R389] 使用的是
  同一原曲线与原参数；“移动”指初始除子代表，不是换一个无关中心的高度。
* SS_j10_06、SS_j10_18 的 CM $-8$ 碰撞见 [R367]–[R371]。
  相交的两个范数因子先保留整数阶及换参单位再联合抵消；水平支与固定支
  的 Laurent 留数在原微分中相消。局部 CM $-8$ 点仅用于这种几何计算，
  没有被宣布为全局 $\mathbb Q$ 有理点或未知中心的高度锚。
* [R372] 及 [R656]、[R709] 的重复目标使用有限平坦长度条件，
  在 $\mathcal O[z]/(z(z-\delta))$ 中保留值行及整差商行，
  $\delta=0$ 时保留导数行。没有用重复的两行普通求值冒充两个独立条件，
  没有除以 $\delta$ 或 47，也没有删去对应重数。
* 非椭圆粗点上分歧的 $j$ 项按 [R435]、[R472]、[R618] 合并。令
  $\Delta=4A^3+27B^2$、$K=3BA'-2AB'$，原 F2 组合准确为
  $$
  -4\frac{j''}{j'}+\frac83\frac{j'}j+
  2\frac{j'}{j-1728}
  =\frac{10}{3}\frac{\Delta'}{\Delta}-4\frac{K'}K.
  $$
  右侧只逆已核的单位；F3 使用其一半。真正有稳定子的 CM3/CM4 粗图
  则使用 [R328]、[R554] 的原粗参数和各自的联合 Laurent 相消，
  不把同一个非单位 $j'$ 公式强行套用。

CM 盘的水平和合流情况也都在 §4 所引原文中处理：基点的二阶合流连接
见 [R328]，$c_7,u,c_{11}$ 的实际水平支及 $v$ 的三重粗参数分别见
[R323]、[R324]、[R310]、[R316]。这些证明先验证整个微分的极部相消，
再给单位系统和 (707.8)；不存在仅删除局部奇项后的假高度。

### 5.3 最后一盘 SS_j36_06 的实际封口

[R656] 的真实 F2 只有两条简单分支
$$
y\equiv51167,\ 59448\pmod{47^3};
$$
它们的剩余导数为 $36,11$，不是多重根。公开 [R709] 保留原
$\Phi_C$、原 $z$、$2^{-9}$ 规范纤维及原 R554 联合 Laurent 项的一半，
四个 3 核目标为
$$
[1152,1152,276,276].
$$
这是两对双点，有限平坦极点总长度六的约束秩为六，原 54 个校准全部保留。
其实际 F3 多项式是
$$
\rho_{F_3}(y)\equiv
3275477+3821617y+4469935y^2+2736951y^3+2595575y^4
\pmod Q.
$$
两条 F2 分支的四个差依次为
$$
[1266133,1266133,3524342,3524342],
\qquad
[3005697,3005697,384225,384225].
\tag{707.12}
$$
全部非零，(707.10) 排除其所有更高位。因此最后一盘已经排除；下面的
105 个非 CM SS 盘没有待填前提。

## 6. 全部 129 盘的逐盘证据表

每行是一个实际有理剩余盘，绝不按同 $j$ 或同靶值合并。“无”表示本篇
必要 QC 条件排除该盘的所有有理点；“唯一 CM”由 §4 的真实存在性与
简单根唯一性共同得出。F2 候选值是相应原证明绑定的参数中的全部分支；
只在同一行的真实 F2/F3 函数之间使用，不能跨盘比较或自由换参。
有双重残根的 SS_j0_15 单列其完整受阻结论。


### 普通盘：全部 19 盘

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `ORD_j01` | 无 | [R284] | 无 |
| `ORD_j05` | 无 | [R262] | 无 |
| `ORD_j07` | 35962, 279 | [R267] / [R291] | 无 |
| `ORD_j11` | 无 | [R268] | 无 |
| `ORD_j12` | 69875, 15127 | [R269] / [R296] | 无 |
| `ORD_j15` | 73049, 89143 | [R270] / [R297] | 无 |
| `ORD_j19` | 34718, 20625 | [R271] / [R298] | 无 |
| `ORD_j24` | 无 | [R272] | 无 |
| `ORD_j27` | 20183, 78611 | [R273] / [R299] | 无 |
| `ORD_j28` | 无 | [R285] | 无 |
| `ORD_j30` | 无 | [R274] | 无 |
| `ORD_j32` | 75915, 39733 | [R276] / [R300] | 无 |
| `ORD_j38` | 62093, 94227 | [R277] / [R310] | 唯一 CM -11；y = 94227 |
| `ORD_j39` | 9310, 85546 | [R278] / [R303] | 唯一 CM -19；y = 9310 |
| `ORD_j40` | 13002, 61424 | [R279] / [R309] | 唯一 CM -67；y = 13002 |
| `ORD_j41` | 无 | [R280] | 无 |
| `ORD_j43` | 无 | [R281] | 无 |
| `ORD_j45` | 87914, 80131 | [R282] / [R308] | 无 |
| `ORD_j46` | 84194, 54740 | [R283] / [R307] | 无 |

### 超奇异盘：剩余 j = 0

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `SS_j0_01` | 无 | [R436] | 无 |
| `SS_j0_02` | 无 | [R472] | 无 |
| `SS_j0_03` | 无 | [R606] | 无 |
| `SS_j0_04` | 无 | [R607] | 无 |
| `SS_j0_05` | 无 | [R609] | 无 |
| `SS_j0_06` | 8860, 37204 | [R610] / [R611] | 无 |
| `SS_j0_07` | 47126, 45023 | [R612] / [R618] | 无 |
| `SS_j0_08` | 无 | [R617] | 无 |
| `SS_j0_09` | 52693, 58193 | [R620] / [R620] | 无 |
| `SS_j0_10` | 0 | [R328] | 唯一 CM -3；y = 0 |
| `SS_j0_11` | 39152, 44685 | [R621] / [R621] | 无 |
| `SS_j0_12` | 无 | [R622] | 无 |
| `SS_j0_13` | 82842, 26024 | [R623] / [R623] | 无 |
| `SS_j0_14` | 无 | [R624] | 无 |
| `SS_j0_15` | 重根 28 在 mod 47² 受阻 | [R625] | 无 |
| `SS_j0_16` | 无 | [R626] | 无 |
| `SS_j0_17` | 3439, 66316 | [R627] / [R627] | 无 |
| `SS_j0_18` | 无 | [R628] | 无 |
| `SS_j0_19` | 无 | [R629] | 无 |
| `SS_j0_20` | 无 | [R630] | 无 |
| `SS_j0_21` | 无 | [R631] | 无 |
| `SS_j0_22` | 82095, 467 | [R632] / [R632] | 无 |

### 超奇异盘：剩余 j = 9

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `SS_j9_01` | 无 | [R382] | 无 |
| `SS_j9_02` | 55922, 68240 | [R383] / [R387] | 无 |
| `SS_j9_03` | 无 | [R384] | 无 |
| `SS_j9_04` | 32063, 39679 | [R385] / [R389] | 无 |
| `SS_j9_05` | 1318, 2729 | [R666] / [R666] | 无 |
| `SS_j9_06` | 50013, 16841 | [R667] / [R667] | 无 |
| `SS_j9_07` | 无 | [R668] | 无 |
| `SS_j9_08` | 无 | [R669] | 无 |
| `SS_j9_09` | 无 | [R670] | 无 |
| `SS_j9_10` | 无 | [R671] | 无 |
| `SS_j9_11` | 75213, 9440 | [R313] / [R316] | 唯一 CM -27；y = 75213 |
| `SS_j9_12` | 46775, 100982 | [R672] / [R672] | 无 |
| `SS_j9_13` | 无 | [R673] | 无 |
| `SS_j9_14` | 39453, 53048 | [R674] / [R674] | 无 |
| `SS_j9_15` | 无 | [R675] | 无 |
| `SS_j9_16` | 35133, 38295 | [R676] / [R676] | 无 |
| `SS_j9_17` | 19695, 15162 | [R677] / [R677] | 无 |
| `SS_j9_18` | 无 | [R678] | 无 |
| `SS_j9_19` | 84793, 57595 | [R323] / [R325] | 唯一 CM -7；y = 57595 |
| `SS_j9_20` | 无 | [R679] | 无 |
| `SS_j9_21` | 46013, 18190 | [R680] / [R680] | 无 |
| `SS_j9_22` | 44086, 6687 | [R681] / [R681] | 无 |

### 超奇异盘：剩余 j = 10

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `SS_j10_01` | 39253, 18317 | [R329] / [R349] | 无 |
| `SS_j10_02` | 6222 | [R331] / [R350] | 无 |
| `SS_j10_03` | 23906, 102035 | [R332] / [R351] | 无 |
| `SS_j10_04` | 无 | [R333] | 无 |
| `SS_j10_05` | 75296, 86022 | [R318] / [R319] | 唯一 CM -28；y = 86022 |
| `SS_j10_06` | 36947, 75637 | [R368] / [R369] | 无 |
| `SS_j10_07` | 34472, 8165 | [R334] / [R353] | 无 |
| `SS_j10_08` | 84059, 48120 | [R335] / [R354] | 无 |
| `SS_j10_09` | 无 | [R336] | 无 |
| `SS_j10_10` | 86490, 93447 | [R337] / [R356] | 无 |
| `SS_j10_11` | 无 | [R372] | 无 |
| `SS_j10_12` | 33000, 66591 | [R338] / [R357] | 无 |
| `SS_j10_13` | 80953, 99057 | [R339] / [R358] | 无 |
| `SS_j10_14` | 无 | [R340] | 无 |
| `SS_j10_15` | 无 | [R341] | 无 |
| `SS_j10_16` | 无 | [R342] | 无 |
| `SS_j10_17` | 74325, 14781 | [R343] / [R362] | 无 |
| `SS_j10_18` | 2952, 82202 | [R370] / [R371] | 无 |
| `SS_j10_19` | 77001, 6575 | [R344] / [R363] | 无 |
| `SS_j10_20` | 无 | [R345] | 无 |
| `SS_j10_21` | 无 | [R346] | 无 |
| `SS_j10_22` | 86167, 22828 | [R347] / [R366] | 无 |

### 超奇异盘：剩余 j = 36

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `SS_j36_01` | 无 | [R635] | 无 |
| `SS_j36_02` | 无 | [R656] | 无 |
| `SS_j36_03` | 3614, 28196 | [R636] / [R636] | 无 |
| `SS_j36_04` | 71113, 72433 | [R637] / [R637] | 无 |
| `SS_j36_05` | 103230, 75989 | [R638] / [R638] | 无 |
| `SS_j36_06` | 51167, 59448 | [R656] / [R709] | 无 |
| `SS_j36_07` | 102335, 67998 | [R639] / [R639] | 无 |
| `SS_j36_08` | 无 | [R640] | 无 |
| `SS_j36_09` | 无 | [R641] | 无 |
| `SS_j36_10` | 93334, 71387 | [R642] / [R642] | 无 |
| `SS_j36_11` | 34602, 84711 | [R643] / [R643] | 无 |
| `SS_j36_12` | 无 | [R644] | 无 |
| `SS_j36_13` | 无 | [R645] | 无 |
| `SS_j36_14` | 无 | [R646] | 无 |
| `SS_j36_15` | 无 | [R647] | 无 |
| `SS_j36_16` | 无 | [R648] | 无 |
| `SS_j36_17` | 无 | [R649] | 无 |
| `SS_j36_18` | 38118, 19358 | [R650] / [R650] | 无 |
| `SS_j36_19` | 无 | [R651] | 无 |
| `SS_j36_20` | 39953, 74553 | [R652] / [R652] | 无 |
| `SS_j36_21` | 2307, 64996 | [R653] / [R653] | 无 |
| `SS_j36_22` | 84486, 22082 | [R654] / [R654] | 无 |

### 超奇异盘：剩余 j = 44

| 圆盘 | F2 全部候选 y mod 47³ | F2 / 后续 F3 证明 | 最终有理点 |
|---|---|---|---|
| `SS_j44_01` | 22797, 13681 | [R391] / [R395] | 无 |
| `SS_j44_02` | 96923, 86091 | [R321] / [R324] | 唯一 CM -12；y = 96923 |
| `SS_j44_03` | 无 | [R392] | 无 |
| `SS_j44_04` | 无 | [R393] | 无 |
| `SS_j44_05` | 46984, 33932 | [R394] / [R398] | 无 |
| `SS_j44_06` | 99230, 43277 | [R400] / [R404] | 无 |
| `SS_j44_07` | 22419, 53840 | [R401] / [R405] | 无 |
| `SS_j44_08` | 55149, 83983 | [R659] / [R659] | 无 |
| `SS_j44_09` | 73527, 5911 | [R403] / [R407] | 无 |
| `SS_j44_10` | 无 | [R408] | 无 |
| `SS_j44_11` | 48863, 27352 | [R409] / [R422] | 无 |
| `SS_j44_12` | 无 | [R410] | 无 |
| `SS_j44_13` | 无 | [R411] | 无 |
| `SS_j44_14` | 无 | [R412] | 无 |
| `SS_j44_15` | 无 | [R413] | 无 |
| `SS_j44_16` | 65175, 52206 | [R660] / [R660] | 无 |
| `SS_j44_17` | 无 | [R415] | 无 |
| `SS_j44_18` | 无 | [R661] | 无 |
| `SS_j44_19` | 91095, 52677 | [R662] / [R662] | 无 |
| `SS_j44_20` | 71001, 29785 | [R663] / [R663] | 无 |
| `SS_j44_21` | 5875, 36604 | [R664] / [R664] | 无 |
| `SS_j44_22` | 无 | [R665] | 无 |


## 7. 由逐盘表得到完整分类

设 $P\in X(\mathbb Q)$。§2 使 $P$ 落在 §6 恰好一行的剩余盘中。
它必须满足 §3 的同一坏分量必要方程。若该行是被排除盘，原 F2 无根、
完整多重根障碍或 F2/F3 的非零同靶差之一给出矛盾。于是 $P$ 必须落在
八个 CM 盘之一。各盘全部简单分支已经由 §4.2 排除至恰一条；
其已知有理 CM 点满足准确的全局方程，§4 的单位导数和 Hensel 唯一性
迫使 $P$ 等于该点。八个点的准确 $j$ 值互异，故没有重复计数。

反过来，§4.1 的实际 CM 构造给这八个有理点的存在性，因而上界达到。
这证明 §1 的定理。证明使用的是整盘解析函数及严格全尾，不将模
$47^4$ 的有限同余解等同于有理点，也不把一个盘的有限阶段输出当作
其它盘已经完成。

## 8. 可审查输入和本篇新增范围

逐盘证据表的机器可读版本为
[R707-all129-disk-ledger.json](../notes/R707-all129-disk-ledger.json)。
它逐行记录原 F2/F3 证明路径、组装时的原文 SHA、全部 F2 分支、
多重根障碍、唯一保留 CM 点及 19/110/129 的互斥覆盖。
同名结果号的 R278、R335、R336 补充证明另列在相应原文项中。
账本不是把来源证明替换为若干布尔标记；完整数学论证依赖本篇明确列出的
全局接口、逐盘原始证明及其原始实际证书。

最后新增盘严格绑定公开 run 43589296050，源提交
467b161338bf3dd3a33ee95e7813e0c10ca42b3d，及以下不可变输出：

| 原产物 | SHA-256 |
|---|---|
| R656 的原 F2 多项式 | 1d62f726dd4f381b8a3181cc9902a30059cf98ac1d21f6907fc79cf85456a314 |
| R709 的实际 F3 多项式 | f4ffad925054a36ea3e9ce86ae9ae01e76f825866ea2d3345d6df352b428d90f |
| R709 的独立整数审计 | ba74e300d051e0f0a58ea6b7b5cc36773ad4ef71e243dd3488233f8e154eac47 |

原目录为
[computations/R709/43589296050-1](../computations/R709/43589296050-1)。
全部实际中心、原主函数、Norm、连接、Frobenius、切向、局部和全局多项式、
同分量筛选及相应独审均按逐盘文件保留。R620/R621 等迁移后的恢复结果
使用其公开运行最终产物；R389 使用已恢复的原始同 SHA 证书，而不使用
迁移前仅有的检查点摘要。

本篇新做的是原证明的完整拼接、八个真实 CM 点的身份/唯一性连接、
最后盘的公开结果接入和全部 129 行覆盖。没有声称在本篇重新运行 129 条
长群链或重新计算全部局部高度。各算术结论的实际运行与独立复核范围
以各原结果的说明和 source/input SHA 为准。

层 41 的分类至此闭合；一般 $p$ 的实际正规化子分支、R616 所需非消失、
真实高度外积的统一首项及变化判别式的控制仍是主课题的独立问题。
后续工作不能从本篇有限层分类推得这些统一结论。

## 原始逐盘证明索引


[R94]: R94-central-involution-and-complete-Chow-Heegner-operator.md
[R102]: R102-actual-level41-makdisi-model-at47.md
[R121]: R121-actual-cm-logarithms-and-saturated-hecke-orbit-at47.md
[R133]: R133-two-cm-points-calibrate-all-54-height-coefficients.md
[R134]: R134-actual-t2-bad-height-cancellation-at41.md
[R135]: R135-complete-actual-bad-height-spectrum-at41.md
[R148]: R148-global-correspondence-section-with-diagonal-and-basepoint.md
[R222]: R222-complete-miller-norms-and-all54-global-heights.md
[R228]: R228-global-QC-polynomials-and-rational-SS-disks.md
[R231]: R231-all-ordinary-reference-points-and-complete-residue-atlas.md
[R237]: R237-three-ordinary-CM-anchors-and-113-global-functions.md
[R259]: R259-actual-ordinary-canonical-F2-center-height.md
[R262]: R262-first-complete-ordinary-disk-exclusion.md
[R267]: R267-second-ordinary-disk-canonical-height-and-exact-F2-roots.md
[R268]: R268-ORD_j11-actual-canonical-F2-disk.md
[R269]: R269-ORD_j12-actual-canonical-F2-disk.md
[R270]: R270-ORD_j15-actual-canonical-F2-disk.md
[R271]: R271-ORD_j19-actual-canonical-F2-disk.md
[R272]: R272-ORD_j24-actual-canonical-F2-disk.md
[R273]: R273-ORD_j27-actual-canonical-F2-disk.md
[R274]: R274-ORD_j30-actual-canonical-F2-disk.md
[R276]: R276-ORD_j32-actual-canonical-F2-disk.md
[R277]: R277-ORD_j38-canonical-F2-and-independent-CM-check.md
[R278]: R278-ORD_j39-canonical-F2-and-independent-CM-check.md
[R279]: R279-ORD_j40-canonical-F2-and-independent-CM-check.md
[R280]: R280-ORD_j41-actual-canonical-F2-disk.md
[R281]: R281-ORD_j43-actual-canonical-F2-disk.md
[R282]: R282-ORD_j45-unit-canonical-divisor-and-actual-F2-disk.md
[R283]: R283-ORD_j46-actual-canonical-F2-disk.md
[R284]: R284-ORD_j01-actual-canonical-F2-disk.md
[R285]: R285-ordinary-j28-unit-frame-height-and-disk-exclusion.md
[R291]: R291-actual-F3-height-and-ORD-j07-complete-exclusion.md
[R292]: R292-actual-T3-fixed-divisor-and-basepoint-rigidification.md
[R296]: R296-ORD_j12-actual-F3-height-and-complete-exclusion.md
[R297]: R297-ORD_j15-actual-F3-height-and-complete-exclusion.md
[R298]: R298-ORD_j19-actual-F3-height-and-complete-exclusion.md
[R299]: R299-ORD_j27-actual-F3-height-and-complete-exclusion.md
[R300]: R300-ORD_j32-actual-F3-height-and-complete-exclusion.md
[R303]: R303-ordinary-CM19-F3-height-and-extra-root-exclusion.md
[R304]: R304-all129-disks-and53-actual-global-polynomials.md
[R307]: R307-ORD_j46-actual-F3-height-and-complete-exclusion.md
[R308]: R308-ORD_j45-actual-F3-height-and-complete-exclusion.md
[R309]: R309-ordinary-CM67-F3-height-and-extra-root-exclusion.md
[R310]: R310-ordinary-CM11-horizontal-Laurent-height-and-root-exclusion.md
[R313]: R313-SS-CM27-actual-F2-height-and-two-simple-roots.md
[R314]: R314-two-new-SS-CM-points-and-all53-height-anchors.md
[R316]: R316-CM27-SS-cubic-ramification-F3-and-extra-root-exclusion.md
[R318]: R318-SS-CM28-actual-F2-height-and-two-simple-roots.md
[R319]: R319-SS-CM28-actual-F3-height-and-extra-root-exclusion.md
[R321]: R321-CM12-SS-cubic-ramification-F2-and-exact-disk-roots.md
[R323]: R323-SS-CM7-double-horizontal-F2-and-two-simple-roots.md
[R324]: R324-CM12-SS-horizontal-F3-and-extra-root-exclusion.md
[R325]: R325-SS-CM7-actual-F3-and-extra-root-exclusion.md
[R328]: R328-basepoint-confluent-F2-height-and-unique-CM-root.md
[R329]: R329-first-non-CM-SS-principal-height-and-F2-disk.md
[R331]: R331-SS_j10_02-actual-principal-F2-height-and-disk.md
[R332]: R332-SS_j10_03-actual-principal-F2-height-and-disk.md
[R333]: R333-SS_j10_04-actual-principal-F2-height-and-disk.md
[R334]: R334-SS_j10_07-actual-principal-F2-height-and-disk.md
[R335]: R335-SS_j10_08-actual-principal-F2-height-and-disk.md
[R336]: R336-SS_j10_09-actual-principal-F2-height-and-disk.md
[R337]: R337-SS_j10_10-actual-principal-F2-height-and-disk.md
[R338]: R338-SS_j10_12-actual-principal-F2-height-and-disk.md
[R339]: R339-SS_j10_13-actual-principal-F2-height-and-disk.md
[R340]: R340-SS_j10_14-actual-principal-F2-height-and-disk.md
[R341]: R341-SS_j10_15-actual-principal-F2-height-and-disk.md
[R342]: R342-SS_j10_16-actual-principal-F2-height-and-disk.md
[R343]: R343-SS_j10_17-actual-principal-F2-height-and-disk.md
[R344]: R344-SS_j10_19-actual-principal-F2-height-and-disk.md
[R345]: R345-SS_j10_20-actual-principal-F2-height-and-disk.md
[R346]: R346-SS_j10_21-actual-principal-F2-height-and-disk.md
[R347]: R347-SS_j10_22-actual-principal-F2-height-and-disk.md
[R349]: R349-first-non-CM-SS-F3-height-and-complete-disk-exclusion.md
[R350]: R350-SS-j10-02-actual-F3-and-complete-disk-exclusion.md
[R351]: R351-SS-j10-03-actual-F3-and-complete-disk-exclusion.md
[R353]: R353-SS-j10-07-actual-F3-and-complete-disk-exclusion.md
[R354]: R354-SS-j10-08-actual-F3-and-complete-disk-exclusion.md
[R356]: R356-SS-j10-10-actual-F3-and-complete-disk-exclusion.md
[R357]: R357-SS-j10-12-actual-F3-and-complete-disk-exclusion.md
[R358]: R358-SS-j10-13-actual-F3-and-complete-disk-exclusion.md
[R362]: R362-SS-j10-17-actual-F3-and-complete-disk-exclusion.md
[R363]: R363-SS-j10-19-actual-F3-and-complete-disk-exclusion.md
[R366]: R366-SS-j10-22-actual-F3-and-complete-disk-exclusion.md
[R367]: R367-CM8-horizontal-level-branch-and-full-precision-joint-cancellation.md
[R368]: R368-CM8-collision-actual-F2-height-and-two-simple-roots.md
[R369]: R369-CM8-collision-disk-actual-F3-and-complete-exclusion.md
[R370]: R370-second-CM8-collision-disk-actual-F2-and-two-roots.md
[R371]: R371-second-CM8-collision-disk-actual-F3-and-complete-exclusion.md
[R372]: R372-finite-flat-T2-poles-and-SS-j10-11-complete-F2-exclusion.md
[R379]: R379-faithful-clearing-section-cover-and-invariant-j-map.md
[R382]: R382-first-j9-moved-center-actual-F2-and-complete-disk-exclusion.md
[R383]: R383-second-j9-moved-center-actual-F2-and-two-simple-branches.md
[R384]: R384-third-j9-moved-center-actual-F2-and-complete-disk-exclusion.md
[R385]: R385-fourth-j9-moved-center-actual-F2-and-two-simple-branches.md
[R387]: R387-second-j9-real-F3-and-complete-same-component-exclusion.md
[R389]: R389-fourth-j9-real-F3-and-complete-same-component-exclusion.md
[R391]: R391-SS_j44_01-actual-principal-F2-height-and-disk.md
[R392]: R392-SS_j44_03-actual-principal-F2-height-and-disk.md
[R393]: R393-SS_j44_04-actual-principal-F2-height-and-disk.md
[R394]: R394-SS_j44_05-actual-principal-F2-height-and-disk.md
[R395]: R395-SS-j44-01-actual-F3-and-complete-disk-exclusion.md
[R398]: R398-SS-j44-05-actual-F3-and-complete-disk-exclusion.md
[R399]: R399-j9-evaluation-fibre-collision-two-real-flips-and-complete-principal-Norm.md
[R400]: R400-SS_j44_06-actual-principal-F2-height-and-disk.md
[R401]: R401-SS_j44_07-actual-principal-F2-height-and-disk.md
[R403]: R403-SS_j44_09-actual-principal-F2-height-and-disk.md
[R404]: R404-SS-j44-06-actual-F3-and-complete-disk-exclusion.md
[R405]: R405-SS-j44-07-actual-F3-and-complete-disk-exclusion.md
[R407]: R407-SS-j44-09-actual-F3-and-complete-disk-exclusion.md
[R408]: R408-SS_j44_10-actual-principal-F2-height-and-disk.md
[R409]: R409-SS_j44_11-actual-principal-F2-height-and-disk.md
[R410]: R410-SS_j44_12-actual-principal-F2-height-and-disk.md
[R411]: R411-SS_j44_13-actual-principal-F2-height-and-disk.md
[R412]: R412-SS_j44_14-actual-principal-F2-height-and-disk.md
[R413]: R413-SS_j44_15-actual-principal-F2-height-and-disk.md
[R415]: R415-SS_j44_17-actual-principal-F2-height-and-disk.md
[R422]: R422-SS-j44-11-actual-F3-and-complete-disk-exclusion.md
[R435]: R435-integral-ramified-j-height-derivative-and-126-disk-frame.md
[R436]: R436-SS_j0_01-ramified-unit-parameter-F2-height-and-disk.md
[R472]: R472-SS_j0_02-ramified-unit-parameter-F2-height-and-disk.md
[R554]: R554-true-CM4-coarse-coordinate-and-joint-Laurent-height-cancellation.md
[R606]: R606-SS_j0_03-ramified-unit-parameter-F2-height-and-disk.md
[R607]: R607-SS_j0_04-ramified-unit-parameter-F2-height-and-disk.md
[R609]: R609-SS_j0_05-ramified-unit-parameter-F2-height-and-disk.md
[R610]: R610-SS_j0_06-ramified-unit-parameter-F2-height-and-two-candidates.md
[R611]: R611-SS_j0_06-ramified-unit-parameter-F3-disk-exclusion.md
[R612]: R612-SS_j0_07-ramified-unit-parameter-F2-height-and-two-candidates.md
[R617]: R617-SS_j0_08-ramified-unit-parameter-F2-height-and-disk.md
[R618]: R618-SS_j0_07-ramified-unit-parameter-F3-disk-exclusion.md
[R620]: R620-SS_j0_09-public-prefix-recovery-and-complete-F2-F3-exclusion.md
[R621]: R621-SS_j0_11-public-prefix-recovery-and-complete-F2-F3-exclusion.md
[R622]: R622-SS_j0_12-actual-ramified-height-and-complete-disk-exclusion.md
[R623]: R623-SS_j0_13-actual-ramified-height-and-complete-disk-exclusion.md
[R624]: R624-SS_j0_14-actual-ramified-height-and-complete-disk-exclusion.md
[R625]: R625-SS_j0_15-double-residual-root-has-no-integral-lift.md
[R626]: R626-SS_j0_16-actual-ramified-height-and-complete-disk-exclusion.md
[R627]: R627-SS_j0_17-actual-ramified-height-and-complete-disk-exclusion.md
[R628]: R628-SS_j0_18-actual-ramified-height-and-complete-disk-exclusion.md
[R629]: R629-SS_j0_19-actual-ramified-height-and-complete-disk-exclusion.md
[R630]: R630-SS_j0_20-actual-ramified-height-and-complete-disk-exclusion.md
[R631]: R631-SS_j0_21-actual-ramified-height-and-complete-disk-exclusion.md
[R632]: R632-SS_j0_22-actual-ramified-height-and-complete-disk-exclusion.md
[R635]: R635-SS_j36_01-actual-ramified-height-and-complete-disk-exclusion.md
[R636]: R636-SS_j36_03-actual-ramified-height-and-complete-disk-exclusion.md
[R637]: R637-SS_j36_04-actual-ramified-height-and-complete-disk-exclusion.md
[R638]: R638-SS_j36_05-actual-ramified-height-and-complete-disk-exclusion.md
[R639]: R639-SS_j36_07-actual-ramified-height-and-complete-disk-exclusion.md
[R640]: R640-SS_j36_08-actual-ramified-height-and-complete-disk-exclusion.md
[R641]: R641-SS_j36_09-actual-ramified-height-and-complete-disk-exclusion.md
[R642]: R642-SS_j36_10-actual-ramified-height-and-complete-disk-exclusion.md
[R643]: R643-SS_j36_11-actual-ramified-height-and-complete-disk-exclusion.md
[R644]: R644-SS_j36_12-actual-ramified-height-and-complete-disk-exclusion.md
[R645]: R645-SS_j36_13-actual-ramified-height-and-complete-disk-exclusion.md
[R646]: R646-SS_j36_14-actual-ramified-height-and-complete-disk-exclusion.md
[R647]: R647-SS_j36_15-actual-ramified-height-and-complete-disk-exclusion.md
[R648]: R648-SS_j36_16-actual-ramified-height-and-complete-disk-exclusion.md
[R649]: R649-SS_j36_17-actual-ramified-height-and-complete-disk-exclusion.md
[R650]: R650-SS_j36_18-actual-ramified-height-and-complete-disk-exclusion.md
[R651]: R651-SS_j36_19-actual-ramified-height-and-complete-disk-exclusion.md
[R652]: R652-SS_j36_20-actual-ramified-height-and-complete-disk-exclusion.md
[R653]: R653-SS_j36_21-actual-ramified-height-and-complete-disk-exclusion.md
[R654]: R654-SS_j36_22-actual-ramified-height-and-complete-disk-exclusion.md
[R656]: R656-two-true-CM4-original-F2-heights-and-first-exclusion.md
[R659]: R659-SS_j44_08-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R660]: R660-SS_j44_16-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R661]: R661-SS_j44_18-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R662]: R662-SS_j44_19-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R663]: R663-SS_j44_20-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R664]: R664-SS_j44_21-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R665]: R665-SS_j44_22-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R666]: R666-SS_j9_05-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R667]: R667-SS_j9_06-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R668]: R668-SS_j9_07-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R669]: R669-SS_j9_08-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R670]: R670-SS_j9_09-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R671]: R671-SS_j9_10-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R672]: R672-SS_j9_12-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R673]: R673-SS_j9_13-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R674]: R674-SS_j9_14-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R675]: R675-SS_j9_15-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R676]: R676-SS_j9_16-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R677]: R677-SS_j9_17-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R678]: R678-SS_j9_18-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R679]: R679-SS_j9_20-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R680]: R680-SS_j9_21-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R681]: R681-SS_j9_22-actual-nonelliptic-height-and-complete-disk-exclusion.md
[R709]: R709-final-true-CM4-F3-and-complete-SS-exclusion.md
