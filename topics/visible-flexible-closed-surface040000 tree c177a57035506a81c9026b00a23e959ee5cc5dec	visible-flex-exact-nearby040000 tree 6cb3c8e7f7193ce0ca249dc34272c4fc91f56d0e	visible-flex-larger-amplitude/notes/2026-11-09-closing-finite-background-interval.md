# K6–K9 新候选的有限背景连续曲率核验

会话：Astra-visible-flex-4ffd372b / closing_geometry。2026-11-09。
状态：作者证明与 outward interval 复算，待独审。仅旋转背景。

## 明确固定背景

采用 `closing_weighted_candidate_v3_k6_width045_config.json` 的所有参数：
rCut=3/5、r_c=3/20、wCut=1/2、width=9/20、K=6、保护深度160，
cell0正权重 [1,1/2,3,1/20,1]，首pulse cap2/5，
六谷 [3.125,2.8125,4.0625,5,5.25,4.0625]。
其余细节沿用已记录的cut-preserving cap与quintic插值。

有限160个source valley校准值取
`closing_weighted_v3_k6_finite_source.json` 的alpha十进制字符串作为**精确参数**。
有限背景不需要这些值满足exact m2校准方程；它们只决定有限valley形状，
不改变cell端口值/导数。n≥160仍选用R28的任一固定exact括号根序列。
这样有限参数无需依赖Newton停止误差，且浅/深端口仍精确相接。
其余输入十进制均按对应有理数解释，prefix R_n 按原定义的2幂解释。
当前数值factory在固定calibrationSteps512下计算的值即这些字符串，
后续提高积分精度不得重新更改有限alpha或这些背景参数。

## 正权重尾部的主体

写旧径向速度 u=|r_old,x|，v=|w_x|/(1+w²)^(3/2)。新速度为

$$|r_x|=(1-\chi)j_0u+\chi v/K+\alpha\chi\lambda u/(1+w^2).$$

由λ>0、α>0，所有χ=1区立即有
|κ_mer|=v/|r_x|≤K。C²接缝由端口λ=1和quintic端点一二阶零保证；
已有独审 `2026-11-09-audit-weighted-radius.md` 检查了该wrapper的积分/调用路径。
这里要补的实质是α>0和两个χ≠1缓冲段的连续界。

## α 的严格粗下界

记 A=∫[(1−χ)j0u+χv/K]dx，B=∫χλu/(1+w²)dx，
固定总径宽使α=(target−A)/B，其中target>.45−10^-48。
上式target余量由n159起点的显式对数长度直接估计。

`closing_finite_background_interval.py` 使用mpmath 1.3.0的outward interval运算，
40位精度，每段32个有理区间；quintic及其导数用单调性包围，
cap的标量函数与导数也分别用单调增/减的端点包围。
积分只将各区间integrand的上端点乘区间长度后相加，不用浮点误差估计作认证。
它给出

$$A<.381388,\qquad B\le3(r_{old,cut}-r_c)<.005067,$$

因而 α>13.54（数值实际α≈97.645不是本证明输入）。
同时全有限尾部的w<.541553，故|κ_θ|≤w/r_c<3.611<K。
完整上端点输出 `closing_weighted_v3_k6_background_interval_s32.json`。

## 外端缓冲段

在cell0最后原始port collar，令q=S(x)、χ=1−q、
J=rCut/rOldCut、j0=1+(J−1)q。原始母线曲率记c_old。
其全部连续点可由

$$c_{old}\le c_*:=\frac{7w_*}{r_*\,(1+w_*^2)^{3/2}},\quad
w_*=\tfrac12e^{7\eta_0/\sqrt{12}},\quad
r_*=r_{old,cut}e^{-\eta_0/\sqrt{12}}$$

控制，因为w_*<1/√2且w/(1+w²)^(3/2)在此范围单调。
设C=c_*/K，E_*=1+w_*²。λ=1，故

$$\frac{|r_x|}{u}-\frac{c_{old}}K
=q\left(j_0-\frac{c_{old}}K\right)+(1-q)\frac\alpha E.$$

若J≥C且α/E_*≥max(C−1,0)，右端非负：在C≥1时它下界为
(1−q)[α/E_*−q(C−1)]；C≤1时直接非负。
区间复算给J−C>1.2028、α_lower/E_*−C+1>9.0785，
所以外缓冲段在全部x而非采样点上满足|κ_mer|≤K。

## 内端缓冲段与深部

n159首port的原始曲率≤7W159/r_c，
其中W159≤(80000/81)2^(-7·159/4)，远小于K。
该段j0=λ=1，所以同一速度表达式是足以保持κ≤K的正组合。
n≥160已由radius family的精确分数证明给|κ_mer|<1/30，
并C²接平圆盘。组合后，整个旋转背景含全部有限保护段和无穷深尾
有|κ_mer|≤6、|κ_θ|<6。

若其余参数固定而把K增加到[6,9]，A减少，B不变，α增加，
外buffer的C减小，以上不等式全部保持；主体≤K直接成立。
因此同一证明同时覆盖保存的K7/K8/K9配置。

这是背景的连续曲率证书候选，不是非旋转曲面的曲率、reach、等距误差或
全题完成证明。关于具体函数的interval包围和有限参数解释还须独立审查。
