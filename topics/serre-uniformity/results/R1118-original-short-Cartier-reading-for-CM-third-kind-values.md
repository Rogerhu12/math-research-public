# R1118. 原 full47 第三类首项的短 Cartier 读取

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：本文证明有限来源、精度和算法；尚无本算法的数学执行回执。**
固定原曲线 $X=X_{\rm ns}^{+}(47)$、辅助素数 $q=4513$，并在其原好特殊纤维上工作。
记 $C=C_\infty$ 为全部23个尖点之和，
$$
g=73,\qquad L=\Omega_X(C),\qquad \deg L=167,\qquad V_n=H^0(X,L^n).
$$
R1090、R1104 已认证原95个 Reynolds 来源、73维全纯核以及
$$
\dim V_1,\ldots,\dim V_5=95,262,429,596,763.
\tag{1118.1}
$$
每一空间均保留原836项 cusp 展开、实际乘积基和全部23个尖点。
本篇既不扩大旧 $\mathrm{Original47Source.series}$ 的有限范围，也不把另一个模曲线的微分格搬来。

目标是 R1103 的原
$$
D_{Z,y}=\operatorname{Fix}Z-2Zy,\qquad
\alpha_{Z,y}=\overline{\omega_{D_{Z,y}}^W/d(j-j(y))}(y).
\tag{1118.2}
$$
这里 $Z$ 取已经认证的 $Z_A=13R_0+4R_2$ 或 $Z_B=2R_4-7R_0$，
$y$ 为原八个指定 CM 点。
原全局高度矩阵、MW 坐标和局部尺度仍是 R1103 的同一来源。
本篇只给 $\alpha$ 的另一条精确读取路线，不从其存在性推出 QC 排盘。

## 1. 全部支撑及一个足够小的 RR 空间

沿用原角、coarse multiplicity 和全部 cusp，清分母后的除子为
$$
\begin{aligned}
6D_{A,y}={}&39R_{20}y_4+12R_5y_4+52R_4y_3+48C\\
 &-156R_0y-48R_2y,\\
6D_{B,y}={}&-21R_{20}y_4+8R_{12}y_3-28R_4y_3+48C\\
 &-24R_4y+84R_0y.
\end{aligned}
\tag{1118.3}
$$
这些是 R1106/R1107 消费的原完整 cycle，不只记录其 Picard 类。
每个闭点的系数包括所有核、自动同构轨道和实际角重数。

令 $S$ 为任一行合并整数系数后的 reduced support，$s=\deg S$。
所有23个 cusp 属于 $S$。各非恒等角均避开原规范 CM 中心；八个中心在4513的相关 $j$ 纤维彼此分开，所以这些原支撑亦避开所有八个目标点。

以下保守界已经足够：
$$
s\le159\quad(Z_A),\qquad s\le151\quad(Z_B).
\tag{1118.4}
$$
确实，$R_C(y_4)$ 对 $C\ne0,\pm1$ 的48条 raw 支由有效 $\mu_2$ 两两配对，故至多24个不同粗点。
$i$ 固定的其它 Cartan 恰在角0；所以这里 $C=20,5$ 没有遗漏固定支。
$y_3$ 的有效 $\mu_3$ 在任何非恒等角上自由，因为一个阶三元素只属于其唯一的非裂 Cartan，不能落 normalizer 的反射陪集。
故 $R_4(y_3)$ 和 $R_{12}(y_3)$ 各至多16个粗点。
变量项 $R_0y\cup R_2y$ 或 $R_4y\cup R_0y$ 的支撑度至多 $24+48=72$。
再加23个 cusp 得到 (1118.4)。相消只会减小此界。

因此
$$
W_S=H^0(X,L^2(-S)),\qquad
\deg L^2(-S)\ge175>2g,
\qquad \dim W_S=262-s.
\tag{1118.5}
$$
该线丛无基点并分离一阶 jet。这些断言由曲线 RR 及扣除一、二个几何点后的 $H^1=0$ 直接给出，亦在实际消费者中以评价矩阵维数核对。

## 2. 分子空间只需到 $V_5$：不构造残余零代数

选取 $f\in W_S$，要求：

1. $f$ 在 $S$ 的每个几何点准确为单零；
2. $f$ 在八个目标及后文共同73个 Cartier 评价点均不为零。

不要求其其它零点约化，也不分解其它零点。写
$$
\operatorname{div}(f)=S+R
$$
并保留有效 $R$ 的全部重数。

这些条件在 $\mathbb F_q$ 上确有解。
在每个闭点，坏条件是一个 proper $\mathbb F_q$ 线性子空间：
$S$ 处使用 $L^2(-S)$ 的非零纤维值，避让点使用 $L^2$ 的非零值。
一阶分离保证前者不是恒等条件，无基点保证后者不是恒等条件。
按闭点次数计，坏条件至多 $s+81<4513$ 个。
有限多个 proper 线性子空间的并集不能覆盖整个 $\mathbb F_q$ 向量空间。
可以确定性地选出这样的 $f$，无需随机前缀。将上述条件写为
非零的 $\mathbb F_q$ 线性映射 $L_j:W_S\to k(P_j)$，要求 $L_j(f)\ne0$。
从 $f=0$ 开始逐个处理；若当前条件为零，选一个基向量 $b$ 使
$L_j(b)\ne0$，再将 $f$ 换为 $f+cb$。
对每个已经满足的条件，至多一个 $c\in\mathbb F_q$ 会破坏它；
另外排除 $c=0$。条件数小于 $q$，故总能取最小的未排除 $c$。
在扩域中求出的坏比值只有实际属于 $\mathbb F_q$ 时才排除。
全部条件在结束时再直接检查；算法与存在性使用同一批真实闭点线性映射。

定义
$$
U_f=\{h\in V_3(-C):\ hW_S\subset fV_3\}.
\tag{1118.6}
$$
则有准确等式
$$
\boxed{\quad U_f=f\,H^0(X,\Omega_X(S)),\qquad
\dim U_f=72+s.\quad}
\tag{1118.7}
$$
证明如下。$W_S$ 作为 $L^2$ 的截面空间，公共零除子准确为 $S$。
所以逐点的包含条件等价于
$$
\operatorname{div}(h)+S-\operatorname{div}(f)\ge0,
$$
即 $h$ 在 $R$ 的每一点至少消失到 $R$ 的完整重数。
又 $V_3(-C)=H^0(\Omega_X L^2)$，因此
$$
U_f=H^0(\Omega_X L^2(-R)).
$$
除以 $f$ 就是 $H^0\Omega_X(S)$。因为 $s>0$，RR 给维数 $g-1+s=72+s$。
这同时证明 residual gcd、非约化残点和潜在高重数都已由 colon 条件精确处理。

所有乘法在 (1118.6) 中只有 $V_3\cdot V_2\subset V_5$，
可以用已有836项注入展开求出。
先取 $V_5$ 的763个实际 pivot 列，再逐个 $W_S$ 基向量加入线性约束。
当前空间始终包含右边的已知空间，所以一旦维数达到 $72+s$ 即可停止；
这是一条有证明的完成标准。
若尚未达到，就继续完整 $W_S$ 基，不能把少数随机乘法当成完整 colon。

## 3. 留数插值包括全部 cusp

设 (1118.3) 中一个闭点 $P$ 的整数系数是 $m_P$。
求 $h\in U_f$ 使
$$
\operatorname{Res}_P(h/f)=m_P\in\mathbb F_q.
\tag{1118.8}
$$
总留数序列给这组方程可解；原整数 degree zero 保证
$\sum_P[k(P):\mathbb F_q]m_P=0$。
其 $\mathbb F_q$ 秩准确为 $s-1$，解空间平移差是原73维全纯空间。
消费者须同时核这个秩、所有闭点方程及全部 Galois conjugates。

### 3.1 非 cusp 点的实际短 jet

在原完整 heat 流参数 $u$ 下，KS 准确为 $du$。
若 $P$ 的有效 necklace 稳定子阶为 $e\in\{1,2,3\}$，原95个系数写成 $F_i(u)$，
其首允许项为 $u^{e-1}$。
选首个非零首系数的 $F_k$ 作局部线标架，置 $r_i=F_i/F_k$。

当 $e=1$，取 $t=u$，只需一阶：
$$
r_i(P),\quad r_i'(P),\quad
s_P=(F_k\,\operatorname{KS}/dt)(P)=F_k(0).
$$
这包括 Gaussian/cubic 纤维上有效稳定子平凡的非规范 necklace；
不能把底椭圆曲线的全部自动同构强加给该点。

当 $e=2,3$，取实际粗参数 $t=j-j(P)$。
写 $j-j(P)=j_eu^e+\cdots$，则
$$
r_i'(P)=\frac{[u^e]r_i}{j_e},\qquad
s_P=\frac{[u^{e-1}]F_k}{e\,j_e}.
\tag{1118.9}
$$
须检查 $r_i$ 的 $u^1,\ldots,u^{e-1}$ 系数均为零。
只需 $F_i$ 到 $2e-1$ 阶及 $j$ 的首项：
Gaussian 为三阶，cubic 为五阶。
这些与现有 Miller 支撑来源的完整 heat 流相同；不是截掉 $A_2$ 后重复微分。

以 $F_k\operatorname{KS}$ 为标架，用原乘积基计算
$$
F=f/(F_k\operatorname{KS})^2,\qquad
H=h/(F_k\operatorname{KS})^3.
$$
这里 $F(P)=0$、$F'(P)\ne0$，准确留数为
$$
\boxed{\quad \operatorname{Res}_P(h/f)=
  \frac{H(P)s_P}{F'(P)}.\quad}
\tag{1118.10}
$$
所有计算保留真实闭点域。某个所选 fine 参数或标架未必单独在最小闭点域上下降；
比值 (1118.10) 是实际留数，须核其 Frobenius 下降。
不得先将每个扩域系数投影到 $\mathbb F_q$。

### 3.2 原23个 cusp

在每个原 cusp 的参数 $t=q_\tau^{1/47}$，使用同一个正则 $L$ 标架
$\ell=47\,dt/t$。
写 $f=F(t)\ell^2$、$h=H(t)\ell^3$。
因 $f$ 单零、$h\in V_3(-C)$，
$$
F=f_1t+\cdots,\quad f_1\ne0,\qquad H=h_1t+\cdots.
$$
于是
$$
\boxed{\quad \operatorname{Res}(h/f)=47\,h_1/f_1.\quad}
\tag{1118.11}
$$
各 cusp 使用原 Weil root 的全部23个 Galois 重标。
只需旧来源长度2的展开；不存在新的高 cusp 系数需求。
原47因子不可删，也不再乘一次 cusp width。

## 4. 同一条 Gaussian 纤维上的共同73个评价点

使用已经认证的实际模型
$$
E_B:\quad Y^2=X^3+343X+B,\qquad
\omega_E=dX/(2Y),
\tag{1118.12}
$$
在 $B=0$ 的原47基、Weil root $2$ 及完整47挠点。
其4513-Frobenius 为标量，因此全部1081个 necklace 都在 $\mathbb F_q$ 上。
有效 $i$ 作用固定25个；其它1056个组成528个无稳定子的粗点。

这些528个点各自的 completed local ring 准确由 $B$ 参数化：
在有标记 fine family 中47挠点 étale 延拓，而有效稳定子平凡。
虽然 $j-1728$ 在 $B$ 中二次消失，**$j$ 不是这些 free 点的 uniformizer**。
本节只用实际 $B$，不作错误的粗参数除法。

先从528点中删掉全部16个原除子在这条纤维上的支撑。
所需来源仅 $R_{20}y_4,R_5y_4,R_0y_4,R_2y_4,R_4y_4$；
即使只用 raw degree，删除不超过
$$
48+48+24+48+48=216
$$
个点，所以剩下至少312个。
其它六个一般 CM $j$ 及三次 $j$ 在4513不等于1728；此事实也由固定八个原模型检查。

任一非零全纯微分的零除子度为 $2g-2=144$。
故在这些剩余点上的评价映射必单射。
用原95个值及已认证73维 kernel 做确定的 greedy 选行，得到共同73个点
$P_1,\ldots,P_{73}$，其矩阵
$$
E_{a i}=(\omega_i/dB)(P_a)
\tag{1118.13}
$$
可逆。此处每个点均为真正的 $\mathbb F_q$ 粗点，所有 frame 继续保持实际 Weil root。
第2节在选择每个 $f$ 时再要求避开这73点，故所有后续分母都是单位。
这一选择只做一次，供全部尚未计算的 case 共用。

## 5. 一次长度4513的原挠点来源

R1091 的实际 Hensel/Miller 来源可直接重建：
在 (1118.12) 上将一个原47挠点提升到
$\mathbb F_q[B]/B^q$，
以 $i$ 和 $B\mapsto-B$ 运输第二基点，再按真实群律得到全部2208个非零点。
原 $47e_P$ 的 addition-chain 斜率式给同一 $G_1$ 规范。
47及所有所用 étale 分母为单位，因而这是一条纯代数、准确模 $B^q$ 的构造。
本篇不重新读取旧 CM 的高矩或首对数。

对每个 $P_a$ 的 determinant-one Cartan frame，按 R1090 的**两个不同相位**重新组合原95个 Reynolds 形式。
全部 frame 共用同一个挠点/G1 series grid。
规范 Gaussian necklace 的形式是奇函数，但 free necklace 不满足这个额外奇性；
实现不得把旧规范点的奇性检查误施到新帧。

在同一物理微分下，
$$
k(B)=\frac{\operatorname{KS}(\omega_E^2)}{dB}
=-\frac{3\cdot343}{4\cdot343^3+27B^2}.
\tag{1118.14}
$$
所以任一原 $\omega_i$ 的局部系数及任一插值形式 $\eta=h/f$ 的局部系数分别是
$$
a_{a i}(B)=k(B)F_i(B),\qquad
r_a(B)=k(B)\frac{h(B)}{f(B)}.
\tag{1118.15}
$$
这些只需模 $B^q$。
所有 $f(P_a)\ne0$，倒数采用单位 Newton 递推，故截断精度完整保留。
没有除以 $q$、形式积分或未经支付的高阶 period 识别。

## 6. Cartier 与第三类修正同时读取

对 $\mathbb F_q$ 点的 $\mathbb F_q$ 参数 $B$，Cartier 的定义直接给
$$
(C(\sum_{n\ge0}a_nB^n\,dB)/dB)(0)=a_{q-1}.
\tag{1118.16}
$$
因系数属于 $\mathbb F_q$，这里的 $q$ 次根为恒等。
此公式不适用于先投影扩域系数；第4节特意选择了实际 $\mathbb F_q$ 点和参数。

令
$$
E^C_{a i}=[B^{q-1}]a_{a i}(B).
$$
如果 $C_{\rm col}$ 以
$C\omega_j=\sum_i(C_{\rm col})_{ij}\omega_i$ 定义，则
$$
\boxed{\quad C_{\rm col}=E^{-1}E^C.\quad}
\tag{1118.17}
$$
原 Hecke row-action 是它的转置。
因此同一次73帧 series 已给全部原 Cartier 矩阵；
不另要求 normalized newform 推到第4513项，更不需要 $4513\cdot145$ 个 cusp 系数。

对插值形式 $\eta$，全部 residues 是 $\mathbb F_q$ 整数，所以
$\delta=C\eta-\eta$ 全纯。其73点值为
$$
v_a=[B^{q-1}]r_a(B)-r_a(0),
\qquad d=E^{-1}v.
\tag{1118.18}
$$
R1103 证明原 $C=\bar T_q$；
R1089 已认证
$$
\det(1-C)=\#J(\mathbb F_q)\bmod q=551\ne0.
\tag{1118.19}
$$
可将此已知值作为新矩阵的完整校验之一。令
$$
x=(1-C_{\rm col})^{-1}d,\qquad
\eta_{\rm fix}=\eta+\sum_i x_i\omega_i.
\tag{1118.20}
$$
则 $C\eta_{\rm fix}=\eta_{\rm fix}$，且原 residues 完全不变。
这是 prescribed-residue Cartier-fixed 形式的唯一解。

R1103 §3 已从原整高度规范证明
$$
\eta_{\rm fix}=N^{-1}d\log f_{N\bar D}
=\overline{\omega_D^W},\qquad N=\#J(\mathbb F_q).
\tag{1118.21}
$$
因此本篇不靠一句“Cartier-fixed 就是 $W$”代替特征零/有限域接口。
以 (1118.3) 的清分母除子插值时，最终准确读取是
$$
\boxed{\quad
\alpha_{Z,y}=\frac16
 \left\{\frac{\eta}{d(j-j(y))}(y)
       +\sum_i x_i\frac{\omega_i}{d(j-j(y))}(y)\right\}.
\quad}
\tag{1118.22}
$$
八个原粗切向和 projective frame 使用 R1103/R1105/原短 jet 的同一规范。
$1/6$ 是实际 cycle 清分母，不能删掉。

## 7. 有限执行协议与诚实的完成标准

新消费者分为以下有限阶段。

1. 重建并逐 hash 核对原95来源和 $V_1,\ldots,V_5$；只消费旧结论。
2. 在独立纯 Python/FLINT 子进程读取原 closed support 的必要一阶/frame、
   八中心 frame 和 Gaussian free fibre 常数值。
   Sage 与 pip FLINT 不得进入同一进程。
3. 在 Sage 中选共同73帧，对每个请求 case 构造 $W_S,f,U_f,h$，
   核全部秩、单零、留数、coarse phase 和避让条件。
4. 重建一次原 Gaussian length4513 grid。
   以最多四个 fork worker 按帧计算原95个 series、原 Cartier 行及全部 case 的顶系数。
   每帧只返回小的 $\mathbb F_q$ 数组；不需要把73份完整 series 跨进程复制。
5. 解 (1118.17)--(1118.22)，逐个完整 case 立即输出可独立消费的回执。
   如在某后续阶段失败，保留已经完整认证的 case；不把部分矩阵称为 $\alpha$。
6. 新 request 只列未由在途 Miller 成功给出的 case。
   不重跑已完成 $\alpha$；允许重建固定输入并逐 hash 核对。

long series 的唯一长度是4513，cusp 来源仍至836。
“每帧长度4513”是准确的有限规模说明，不是未经执行的运行时间保证。
原 complete grid、Reynolds 长乘积及 RR colon 都必须纳入预算。
算法未执行以前，不宣称任何新 $\alpha$ 非零或任何八盘已经唯一。

## 8. 与原 QC 后继的接口

将 (1118.22) 和已经实际计算的原 $K,b_y,z_Z,d_{Z,y}$ 放回 R1103：
$$
\bar f_{Z,y}(t)=t(B_{Z,y}+A_{Z,y}t),\quad
A_{Z,y}=-\operatorname{Tr}(Kz_Zb_y^2),\quad
B_{Z,y}=\operatorname{Tr}(Kb_y d_{Z,y})-\alpha_{Z,y}.
$$
仍须实际核两行秩二或该文的其它充分情形。
本篇不将 Cartier 矩阵可逆条件、全局高度单位或某个单独 $\alpha$ 的非零替换成这个最终检验。
所有非辅助局部项及整尾只消费 R1103 已付的同一原来源。

### 来源

- R1090：原全 Reynolds 两相位来源、全部23 cusp、95/73整格及 Hecke row convention。
- R1091、R1093：实际 Gaussian $A=343$、Weil root2、同一47挠点 Hensel/G1 长展开来源；不重读旧高矩结论。
- R1103 §§2--3：原粗参数、Cartier/原整 $W$ 接口和唯一有限域归一化。
- R1104：原 $L^1,\ldots,L^5$、836注入 jet 与实际乘积基。
- R1105--R1107：原八中心/全部角/closed support、完整 cycle 和短 heat 参数。
- R1086、R1089：Gaussian full47-torsion/528 free points 所用实际 Frobenius 来源，以及原 $\#J(\mathbb F_q)\bmod q=551$。
