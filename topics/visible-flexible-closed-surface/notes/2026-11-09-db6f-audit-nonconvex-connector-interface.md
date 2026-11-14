# 凸刚性之后的非凸连接接口：固定帽法向锥、圆领与 reach 必要门

作者：/root/independent_geometry，2026-11-09。状态：来源核查、完整条件式小引理和两个纯 Fraction 账本；待独立全文审查。没有读取当前 M15 求解态或执行任何求解、积分、RK、几何后台。

本稿承接已经独审通过的 N7/Poisson 标记模型 v2。**不继续把整个凸包边界平滑成等距候选。** 那样即使几何比例、固定片与 reach 都过门，也仍受闭凸面刚性排除。较有用的结论是定位真正连接区必须做什么，以及哪些固定球面小片可以保持原位。

## 1. 凸闭面的共同 metric 障碍，含 C2 正则性范围

Pogorelov 的闭凸面唯一性定理说明：两个闭凸曲面的内蕴距离等距，则它们在三维欧氏空间中刚体全等。原论文书目可核 [S1]；现代原始研究论文 [S2] 的 Theorem A 明确列出所需定理，且没有额外光滑性假设。本稿只调用该已发表定理，不声称重新独审其长篇证明。

若两个闭嵌入 $F_i:M\to\mathbb R^3$ 满足 $F_i^*g_{\rm Eucl}=g$，材料对应给内蕴等距。若两像都凸，便有
$$
\min_{A\in E(3)}d_H(AF_1(M),F_0(M))=0.
\tag{1}
$$
因此具有本轮正刚体商间隙的两个端点不能同时是凸闭面。这里足够的否定结论是 $\delta_E=0$；不需要额外讨论材料参数或从握持区猜整体刚体。

还可把“非凸”加强到确有负高斯曲率。Ghomi–Xiong 的原始研究稿 [S3] Proposition 7.1 允许闭 C1 浸入在一个零测例外集之外为 C2 且非负曲率；取例外集为空即得：**闭 C2 曲面若处处 $K\ge0$，则凸。** 这是本题可用的 C2 版本，不能把 Sacksteder 原来较高的 $C^{n+1}$ 正则性版本直接当作 C2 证明。

由此，任何具有正刚体商端点间隙的共同 metric 闭 C2 族，至少一个有关端点必须有 $K<0$ 的点。如果实际保留的核心柱带为 $K=0$、两个球面帽为 $K=1/a^2>0$，这些负曲率点只能在其余连接区域。不能仅由这一结论判定负曲率一定在活动连接片而非固定扩展片。对 R29 的足够光滑共同 metric 真解，Gauss 方程还使该负曲率由同一 $g$ 决定；此处没有把任意低正则性 metric 的求导问题略去。

## 2. 负曲率连接点必须进入凸包包络内部

设 $E\subset\mathbb R^3$ 为具有内点的紧凸体，$T$ 为闭 C2 嵌入曲面，且 $T\subset E$。若 $p\in T\cap\partial E$，选 $E$ 在 $p$ 的支持单位法向 $u$。局部坐标下 $u\cdot F$ 在 $p$ 取最大值，所以一阶导数为零，而 Hessian 半负定。因为 $F$ 浸入，一阶条件使 $u$ 成为该点的曲面单位法向；Hessian 恰是这个法向下的第二基本型。因此
$$
K_T(p)=\frac{\det II(p)}{\det I(p)}\ge0.
$$
不要求 $\partial E$ 自身光滑或支持平面唯一。

取逆否命题：
$$
\boxed{K_T(p)<0\quad\Longrightarrow\quad p\in\operatorname{int}E.}
\tag{2}
$$
同理可把 $E$ 换成 $E+\varepsilon B_3$。结合 §1，本轮单向包围入口要求某些真实连接点严格离开凸包包络的边界、进入内部；不能把全部连接面铺在凸包表面上。

这不指定内凹的深度，也不证明给定 metric 可实现这种连接。负曲率可很小，单凭 (2) 不产生一个正的全局内凹量下界。若帽的完整 C2 jet 被保留，则帽边缘的正 $K$ 由连续性向外延伸到一个小正曲率邻域；通向负曲率区域途中还必须经过 $K=0$。这些都是接口必要事实。

## 3. 两固定帽确有全相位可保留的球面小片

以下使用 Poisson v2 的明确参数和符号：
$$
P_\pm=(-H,0,\pm z),\quad z=3/10,\quad b=1/100,\quad a=1/10,
$$
$$
L=\sqrt{4H^2+(z+b)^2},\qquad
v_\pm=(-2H,0,\pm(z+b))/L,
$$
$$
C_\pm=\{P_\pm+a\omega:|\omega|=1,\ \omega\cdot v_\pm\ge1/2\},
\quad
E_\alpha=\operatorname{conv}(A_\alpha\cup C_+\cup C_-).
$$
这里 $A_\alpha=R_\alpha\Gamma\times[-b,b]$。原模型的 entire cap 未被证明全部显露在凸包边界；下面只取两个明确的小邻域。

冻结有理端点支付
$$
R_A<6/5,\quad R_C<4/3,\quad H>1,\quad L<5/2,
\quad |(v_\pm)_z|>31/250.
\tag{3}
$$
$R_A,R_C$ 分别是活动带和任一完整标记球关于原点的半径上界。支持函数因此分别以这些半径为对单位方向的 Lipschitz 常数。

令 $\chi=1/100$，取 $|u-v_+|\le\chi$ 的单位方向。由于 $u\cdot v_+\ge1-\chi>1/2$，完整球的支持点 $P_++au$ 也属于实际帽 $C_+$，故该方向帽支持等于球支持。在中心方向 $v_+$，活动带支持至多
$$
H|(v_+)_{xy}|+b(v_+)_z,
$$
而上球支持为 $H|(v_+)_{xy}|+z(v_+)_z+a$。用 Lipschitz 界延到整个法向锥，得到
$$
h_{C_+}(u)-h_{A_\alpha}(u)
\ge a+(z-b)\frac{31}{250}
 -(6/5+4/3)\chi
=\frac{8297}{75000}>0
\tag{4}
$$
对全部 $\alpha$ 成立。另一帽的支持至多是其完整球的支持；两球等半径，所以
$$
h_{C_+}(u)-h_{C_-}(u)
\ge2z(31/250-\chi)
=\frac{171}{2500}>0.
\tag{5}
$$
下帽完全对称。于是两个闭法向锥中的球面点都在全部 $\partial E_\alpha$ 上，且在锥内部形成不随相位改变的光滑开球面片。它们包含原账本需要的轴点 $q_\pm=P_\pm+av_\pm$。

还可保留两个有理中心法向
$$
n_\pm=(-24/25,0,\pm7/25).
$$
它们是单位向量。在 $|u-n_\pm|\le\chi$ 的法向锥内，帽包含性由
$$
u\cdot v_\pm\ge96/125-\chi=379/500>1/2
$$
支付；对活动带及另一帽的严格支持余量分别为
$$
\frac{1169}{7500},\qquad\frac{81}{500}.
\tag{6}
$$
这些固定球面点在两帽上给精确垂直跨度
$$
|(P_++an_+)-(P_-+an_-)|
=2(z+7a/25)=\frac{82}{125}.
\tag{7}
$$
所以可以保留原轴点小片，并另外保留这两个小片来获得更大的固定区尺寸。这里只证明它们是整个运动凸包包络中全时外露、可原位使用的局部片；真实共同材料固定区仍须在最终曲面中逐点保留。

## 4. R29 的负曲率入口方向相容，但不证明全段可解

对 R29 的光滑活动带目标
$$
g=ds^2+a(s)^2d\vartheta^2,\qquad a>0,
$$
由 $\Gamma^s_{\vartheta\vartheta}=-aa'$、
$\Gamma^\vartheta_{s\vartheta}=a'/a$ 直接计算
$$
K_g=-\frac{a''}{a}.
\tag{8}
$$
R29 §4 已审的原 flat ramp 在入口有多项式展开
$a(s)=1+A_4s^4+O(s^5)$，$A_4>0$。使用其原多项式表达求导，而非随意对一般余项求导，得
$$
a''(s)=12A_4s^2+O(s^3)>0
$$
于足够小的 $s>0$。因此足够光滑的真实分支在这里正有 $K_g<0$。中央带的非圆凸截面和连接面的负高斯曲率并不矛盾：前者是角曲线的曲率，后者由整个二维 metric 决定。

R29 的正 Frenet 分支仍要求
$$
a>0,\quad |F_\vartheta|>0,\quad\kappa>0,\quad |a'|<a\kappa.
\tag{9}
$$
Poisson 核的角曲线最小曲率是
$$
\kappa_{\min}=1/\rho_{\max}=5/896.
\tag{10}
$$
若错误地假定所有截面只同形缩放，(9) 会变成 $|a'|<5/896$。真实截面会改变，故这不是所有真实分支的速度上限，也不是新的全局不可能性结论；它说明不能用中央最大曲率小或 reach 好来代付正分支。

R29 还已证明外向 ramp 有正的水平 $s^4$ 泄漏。因此不能要求这些连接点精确留在零泄漏中央投影内。v2 的单向完整包围允许正余量，但该实际余量须由真解的位置界支付，不能从 (8) 或一个局部 Taylor 展开推成全段存在。

## 5. 当前相位公式与直接固定帽接缝的必要协变性

只在 R29 的指定机制下讨论：
$$
F_\alpha(s,\vartheta)=R_\alpha F_0(s,\vartheta-\alpha)
$$
用于活动带，而另一侧是真正逐点固定的材料片。假设材料切口 $s=s_c$ 固定，且全时 C2 拼接。令
$$
W_j(\vartheta)=\partial_s^jF_0(s_c,\vartheta),\qquad j=0,1,2.
$$
固定侧给同一组 jet，因此必有
$$
R_\alpha W_j(\vartheta-\alpha)=W_j(\vartheta)
$$
对所有小相位成立。于是 $R_{-\vartheta}W_j(\vartheta)$ 对局部平移不变，连续性给
$$
\boxed{W_j(\vartheta)=R_\vartheta c_j\quad(j=0,1,2)}
\tag{11}
$$
其中 $c_j$ 为常向量。这个证明对 $W_2$ 只用连续性，没有偷偷要求三阶角导数。

零阶 (11) 要求非退化切口是绕共同轴的中心圆，且高度恒定；一、二阶则是完整 Cartesian 两 jet 的协变性。仅位置为圆仍不足以接合。反之，这些协变条件只支付该相位操作对已给端迹的固定性，不产生满足方程和全部匹配条件的真解。

本轮偏轴帽完全位于 $x_1\le-H+a<0$，其边界不可能直接成为上述轴心圆。故若继续使用 R29 机制，帽须属于圆领之外的更大固定区域，由另行构造的固定连接片把轴对称全两 jet 圆领接到偏轴帽；或者更换并重新证明相位机制。不能把偏轴球面帽直接替换旧圆领而声称原全时拼接自动成立。

## 6. 包络还限制真正固定圆领的高度与 reach

这条是一个有完整额外假设的接口门，不是对任意接缝的全局禁止。令半相位完整实际像满足已审 v2 的
$$
T_1\subset E_{\pi/3}+\varepsilon_1B_3,\qquad \varepsilon_1=1/200,
$$
并含轴心圆 $C(c,z_c)$，半径 $c$、高度 $z_c$。取有理单位方向
$$
u_\pm=(9,0,\pm40)/41.
$$
半相位活动带在这些方向的支持为 $(9m_0+40b)/41$。完整球的上界已经足够排除两帽：冻结端点给
$$
9(m_0+H)+40(b-z)-41a>0.
$$
故包络支持精确等于活动带支持。将圈的支持代入全像包含，得到
$$
\boxed{|z_c|\le Z(c):=
b+\frac9{40}(m_0-c)+\frac{41}{40}\varepsilon_1.}
\tag{12}
$$

若完整闭 C2 面还含两条**相同半径**、不同高度的上述轴心圈，并且在两圈上曲面切平面均水平，则任选同角点 $p,q$，$q-p$ 垂直于 $T_pT_1$。Federer 的 reach–切平面公式 [S4] 给
$$
\operatorname{reach}(T_1)
\le\frac{|p-q|^2}{2\operatorname{dist}(q-p,T_pT_1)}
=\frac{|z_+-z_-|}{2}
\le Z(c).
\tag{13}
$$
这里不假设 $p,q$ 已是全局最近点对，也不把某个局部间距自动当全局 reach 下界。

另一方面，v2 初始真实点对给自身的 $D_0\ge D_{0,\rm lo}$，所以 README 要求
$$
\operatorname{reach}(T_1)\ge .03D_0
\ge .03D_{0,\rm lo}>.0745.
$$
而用向外端点 $m_{0,\rm hi}$ 时，$Z(2/5)$ 精确等于
$$
.0726599490908<.0745.
$$
$Z(c)$ 随 $c$ 增加而严格减小，因此上述全部条件下
$$
\boxed{c\ge2/5\quad\hbox{不可能同时满足 reach 门。}}
\tag{14}
$$
这里的单调方向按 $c$ 增加而 $Z$ 下降使用；并没有用偏大的充分直径预算 $D_*$ 冒充实际 $D_0$ 下界。完整有理必要半径上限约为 $.3918038113523$，只作近似显示；正式拒绝用精确分数。

**该圈必须是真正轴对称固定圆领且满足水平切平面假设。R29 的 tail cut $c\simeq.6,w_c=.5$ 不是这个圈。** 不把它代入 (14)，也不把本模型的圈预算用于旧 M15 图。更小的圈、不同半径的两圈、非水平切平面或其它真实接合机制须另算，本文没有排除它们。

## 7. 下一可用子问题与文件范围

可以保留 §3 的两个或四个固定正曲率小片，寻找位于单向凸包包络内部的非凸连接，并在需要处通过 (8) 的负曲率活动区域；同时满足 (9)、完整边值方程和 (11) 的圆领两 jet。若使用同半径水平双圆领，先满足 (12)–(14) 的必要预算。即使这些条件全通过，也未证明任何连接面存在，更未得到等距族或新 reach 下界。

本轮没有实现凸包+球的平滑对照，也没有运行任何新的实际候选。只产生了两份可独立重放的小标量账本：

- scripts/db6f-audit-nonconvex-connector-cones.py 与同名日期 JSON：实际收据 50cf92 / exit 0，仅核支持锥与初始角曲线量。
- scripts/db6f-audit-poisson-cuff-budget.py 与同名日期 JSON：实际收据 8c8a4f / exit 0，仅核条件式圈预算。

两脚本只读取本题已冻结 Poisson/R27/R29 证据；没有求解、RK、积分、角网格极值、M15 态或 Git 操作。原 N7/Poisson 稿、数据及清单字节未改。

## 来源

- [S1] A. V. Pogorelov, *A theorem of uniqueness for convex surfaces*, Mat. Sb. 26(68):1 (1950), 147–152，[MathNet 原论文官方书目](https://www.mathnet.ru/eng/sm5873)。另有1949专论 [The rigidity of convex surfaces](https://www.mathnet.ru/eng/tm1069)。这里只核书目，不冒称下载或全文审过原俄文长证明。
- [S2] A. A. Borisenko, *Rigidity of Closed Convex Hypersurfaces in Multidimensional Spaces of Constant Curvature*, Journal of Mathematical Physics, Analysis, Geometry 21 (2025), 267–275，Theorem A，[官方期刊原研究文](https://jmag.ilt.kharkiv.ua/index.php/jmag/article/download/1105/jm21-0267e/1239)，DOI 10.15407/mag21.03.02。
- [S3] M. Ghomi and C. Xiong, *Nonnegatively Curved Hypersurfaces with Free Boundary on a Sphere*，作者稿 §7 Proposition 7.1 及 §2.2 对经典正则性范围的说明，[作者官方页面原文](https://ghomi.math.gatech.edu/Papers/nonnegative.pdf)。本稿只用其闭曲面特例，不把自由边界定理误用于本题。
- [S4] H. Federer, *Curvature Measures*, Trans. Amer. Math. Soc. 93 (1959), 418–491，Theorem 4.18，[原论文扫描的该定理全文](https://static1.squarespace.com/static/5cb91b1c70468025fd21e98b/t/5d37d6d2e6603300016d83dc/1563940577696/federer-curvature-measures-transAMS-1959.pdf)。可对照 C. Fefferman、S. Ivanov、Y. Kurylev、M. Lassas、H. Narayanan, *Fitting a Putative Manifold to Noisy Data*, PMLR 75 (2018), 688–720，Proposition 3 的相同公式，[原研究文](https://proceedings.mlr.press/v75/fefferman18a/fefferman18a.pdf)。

网页仅作文本读取；没有保存或上传 PDF，也没有渲染页面。所有新数学推论在上文逐项给出，外部定理的依赖与本轮自行证明部分分开。
