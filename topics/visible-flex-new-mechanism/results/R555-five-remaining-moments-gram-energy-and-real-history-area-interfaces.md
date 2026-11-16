# R555：三 p 返回后的余五矩、完整 Gram 能量与真实历史面积接口

日期：2026-11-16。**完整原式纸证；没有执行数值、符号、profile、
求积、秩或开发检查。**

R552 已在同一个 R521 正交母、同一个固定第三规范 \(\chi\) 上得到
真实有限词，满足总 \(P_0=P_1=P_2=0\)、原总 \(T_1>0\)。
本稿不重复验证该构造，也不把尚未支付的后继当作已可达。
这里从 R73 完整点态矩阵与原水平关系直接推出剩余五矩的联合身份：

1. \(T_1,S_1,S_0\) 是同一个准确 \(2\times2\) 矩阵等式，包含
   静态真实时间和完整速度 Gram，不能分别自由配权；
2. \(R_1,R_0\) 还受几何与**真实累计矩**的有序面积、端项约束；
3. 非恒高度能给 \(r_1\) 正项，但它同时支付负的 \(t_1\) 速度成本。
   本稿不据此宣称存在保其它矩的同规范修复段。

所有身份适用于 R521 的任一实际合法路径，保任意真实 incoming
\(A,T_{\rm third}\)。它们不改变完整 ruling 方程，也不产生新自由规范。

## 1. 固定坐标、实际时间和全部点态系数

固定一个中心 \(\omega_c\)，使用 \(y=x+\omega_c\)。记

\[
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad
u=d/h,\quad b=1/h,\quad v=h_s/h,\quad w=d_s/h,\quad
\rho=u^2+b^2.
\tag{1}
\]

这里 \(s\) 始终是原实际几何时间；字母 \(w\) 在本稿只表示
\(d_s/h\)，不是第二规范。R521 的第二规范仍固定为零。
原水平关系 \(\eta_s=k_s/(2h)\) 给

\[
w=\eta v-\eta_s=u_s+uv,\qquad
b_s=-bv,\qquad
(\eta+u)_s=(\eta-u)v.
\tag{2}
\]

全部后文公式均保(2)，不把 \(\eta,u,h\) 当三个独立路径控制。

用 R73 的记号置

\[
a_1=2k\eta-\frac{k^2+1}{h},\qquad
a_0=k\eta^2-\frac{k^2+1}{h}\eta,
\]
\[
\mathcal A=h a_1=h^2(\eta^2-u^2)-1,\qquad
\mathcal B=h a_0,\qquad
\mathcal B=u\mathcal A+2p_0.
\tag{3}
\]

\(\mathcal A,\mathcal B\) 只是本节两个 scalar；不是累计第二算子。
原 p 列为

\[
p_2=-kh/2,\qquad p_1=2up_2=-kd,\qquad p_0=\rho p_2.
\tag{4}
\]

从 R73(6)(10)直接收常数/一次项，得到完整原矩，包含全部二次速度项：

\[
\begin{array}{c|c}
\text{坐标}&\text{准确点态值}\\ \hline
8t_1&\mathcal A-v^2\\
8t_0&\mathcal B-vw\\
4s_1&u\mathcal A-vw\\
4s_0&u\mathcal B-w^2\\
8r_1&\rho\mathcal A+\rho v^2-2uvw\\
8r_0&\rho\mathcal B+\rho vw-2uw^2 .
\end{array}
\tag{5}
\]

例如 \(s_0=d a_0/4-d_s^2/(4h^2)\)；
\(r_1=a_1(1+d^2)/(8h)+
v^2\rho/8-vuw/4\)。
这些项没有做 \(s\) 方向分部积分，没有删除变化-profile chain，
没有假设速度小、加速度零、历史零或某段静态。

原 trace 条件由(3)(5)逐点给

\[
t_0=p_0/4+s_1/2.
\tag{6}
\]

记大写字母为整条实际词上的积分，例如
\(R_1=\int r_1ds\)、\(T_1=\int t_1ds\)。
当三个总 p 已清时，余矩阵准确为

\[
\mathsf m_{\rm rem}=
\begin{pmatrix}
0&2R_1&-4R_0\\
0&2S_1&-4S_0\\
0&2T_1&-2S_1
\end{pmatrix}.
\tag{7}
\]

所以剩余五个独立目标可取
\((T_1,S_1,S_0,R_1,R_0)\)。\(T_0=S_1/2\) 不是第六个新自由目标。

## 2. 三个余槽的一个准确矩阵身份

由(3)也有

\[
\mathcal A=-2\eta p_2-p_1-1,\qquad
u\mathcal A=-\eta p_1-2p_0-\eta,\qquad
u\mathcal B=-2\eta p_0-\eta^2.
\]

因此(5)给

\[
\boxed{
\begin{aligned}
8t_1&=-2\eta p_2-p_1-1-v^2,\\
4s_1&=-\eta p_1-2p_0-\eta-vw,\\
4s_0&=-2\eta p_0-\eta^2-w^2.
\end{aligned}}
\tag{8}
\]

定义真实 signed 矩阵密度

\[
\mathsf P(s)=
\begin{pmatrix}p_2&p_1/2\\p_1/2&p_0\end{pmatrix}
=p_2
\begin{pmatrix}1&u\\u&u^2+b^2\end{pmatrix}.
\tag{9}
\]

最后一个矩阵在 \(h>0\) 时严格正定，其 determinant 为 \(b^2>0\)。
但 \(\mathsf P\) 随 \(k\) 改号，不能先把它当正测度。

在任意实际区间 \(J\) 上，记长度 \(L=|J|\)，定义

\[
G_0=\int_J\binom1\eta(1,\eta)\,ds,\qquad
G_v=\int_J\binom vw(v,w)\,ds.
\tag{10}
\]

逐点积分(8)即得完整身份

\[
\boxed{
\begin{pmatrix}8T_1&4S_1\\4S_1&4S_0\end{pmatrix}
=-2\int_J\eta\,\mathsf P\,ds
-\begin{pmatrix}P_1&2P_0\\2P_0&0\end{pmatrix}
-G_0-G_v.}
\tag{11}
\]

这里大写量可解释为该区间增量；(11)对任意前缀后的实际后继也成立，
不需要在后继入口重设 history。

特别，在三个总 p 为零的整条词上，

\[
\boxed{
\mathsf H:=
\begin{pmatrix}8T_1&4S_1\\4S_1&4S_0\end{pmatrix}
=-2\int\eta\,\mathsf P\,ds-G_0-G_v.}
\tag{12}
\]

因此同时清这三个余槽，必须而且在这些三个数值目标上恰好等价于

\[
\boxed{-2\int\eta\,\mathsf P\,ds=G_0+G_v.}
\tag{13}
\]

这不是一个只要求 \(T_1\) 改号的条件。它同时固定一个交叉速度积分
\(\int vw\) 和完整 \(\int w^2\)，并保 \(\int\eta p_0\)、
\(\int\eta p_1\) 的真实有序路径相关性。

### 2.1 严格的矩阵正定必要门

若正时长 \(L>0\) 的路径满足 \(P_0=P_1=P_2=T_1=0\)，
则 \(\eta\) 不可能为常数。否则水平式使 \(k_s=0\)，
\(P_2=-k\int h/2=0\) 又使 \(k=0\)；
此时 \(8T_1=-L-\int v^2<0\)，矛盾。

故在完整三 p 与上述三个余槽同时清零时，
\(G_0\) 已严格正定：其 determinant 为
\(L\int(\eta-\bar\eta)^2ds>0\)。
于是(13)要求

\[
\int\eta p_2<0,\qquad \int\eta p_0<0,
\]
\[
\boxed{
4\left(\int\eta p_2\right)\left(\int\eta p_0\right)
-\left(\int\eta p_1\right)^2>0.}
\tag{14}
\]

这是原真实路径的必要条件，不只是某个形式五维向量需要非零。
其中第一项已有准确简化：

\[
-2\int\eta p_2=\int k^2-P_1.
\tag{15}
\]

当 \(P_1=0\) 时它就是实际 \(\int k^2\)。
其余两个带 \(\eta\) 的积分并不由三个未加权 \(P_i=0\) 自动决定。

(14)没有证明一般路径不可达；它排除的是未能给出上述严格正定
加权矩阵的修复方案。允许真实 \(\eta\) 变化和真实历史重新分配后，
该矩阵可以变化，本稿不预先规定其可达锥。

## 3. 原时间、速度能量和真实端项

(8)第一式与(15)合并，得到原 R549/R542 的完整身份

\[
\boxed{8T_1=\int k^2\,ds-2P_1-L-\int v^2\,ds.}
\tag{16}
\]

它同时适用于 whole word 和任何后继的增量。
如果后继入口已 \(P_i=0\)，且后继结束仍保三个总 p 为零，
则该后继 \(\Delta P_i=0\)。
欲把入口 \(T_1^{\rm in}\) 清掉，必须准确支付

\[
\int_J k^2\,ds=L+\int_Jv^2\,ds-8T_1^{\rm in}.
\tag{17}
\]

R552 的正 \(T_1^{\rm in}\) 是(17)中的真实余量，不能在切换后遗忘。
若入口已 \(T_1^{\rm in}=0\)，每一单位新增时间和高度速度能量
都必须由同段真实 \(\int k^2\) 支付。

速度矩阵还给一个共同的端点下界。定义

\[
\zeta(s)=\binom{b(s)}{b(s)\eta(s)}.
\]

由(2)，

\[
\zeta_s=-b\binom vw.
\tag{18}
\]

对每个固定 \(c\in\mathbb R^2\)，一次 Cauchy 得

\[
c^tG_vc\ge
\frac{\{c^t(\zeta_+-\zeta_-)\}^2}{\int_J b^2ds}.
\]

即

\[
\boxed{
G_v\succeq
\frac{(\zeta_+-\zeta_-)(\zeta_+-\zeta_-)^t}
{\int_Jh^{-2}ds}.}
\tag{19}
\]

这保持真实两端 \(h,\eta\)，没有把它们当可自由指定的端口。
端点相同也只使这个特定下界为零，不使实际 \(G_v\) 消失。

还可分别使用

\[
\int v^2ds\ge
\frac{\{\log(h_+/h_-)\}^2}{L},
\qquad
\int b_s^2ds\ge\frac{(b_+-b_-)^2}{L}.
\tag{20}
\]

若路径在途中往返，右边可由相应实际总变差的平方除以 L 加强。
这些仍是原时间，不得在改用快/慢时钟后漏掉 Jacobian 因子。

由(10)，
\(G_0=L(1,\bar\eta)^t(1,\bar\eta)+
\operatorname{diag}(0,\int(\eta-\bar\eta)^2)\)。
因此(13)同时保真实时间、\(\eta\) 方差及(19)的端点速度成本。

## 4. 两个顶行槽的正项和交叉项

(5)与 \(u_s=w-uv\)、\(b_s=-bv\) 直接给两个逐点恒等：

\[
\boxed{
r_1=u\,s_1+(b^2-u^2)t_1+\frac14b_s^2,}
\tag{21}
\]
\[
\boxed{
r_0=u\,s_0+(b^2-u^2)t_0+
\frac14\{u b_s^2-b b_su_s\}.}
\tag{22}
\]

证明只需从(5)中相减。例如

\[
8\{r_1-u s_1+(u^2-b^2)t_1\}=2b^2v^2=2b_s^2;
\]

第二式余下 \(2b^2vw=2u b_s^2-2b b_su_s\)。
所以系数 \(1/4\) 和交叉项的负号都有原式来源。
这两式没有丢掉 r/s/t 中任何原 M2 项。

(21)说明非恒高度可给真正非负的 r1 项；但它不是独立控制：
其同一个 \(v\) 也以 \(-v^2/8\) 进入 t1，
以 \(-vw/4\) 进入 s1，并通过水平关系改变其它原矩。
(22)的交叉速度项一般不固定号，不能称它为另一个正平方。

此外，若 \(h\ge h_{\min}>0\)，则

\[
E_b:=\int b_s^2ds
=\int \frac{v^2}{h^2}ds
\le h_{\min}^{-2}\int v^2ds.
\tag{23}
\]

因此孤立读取(21)中的 \(E_b/4\) 时，每单位正 r1 收益都伴随原
高度速度成本。其它带 \(u,b\) 的项不能未经证明设为零。

## 5. 累计矩的准确有序面积与完整端项

令 \(m_a(s)\) 为从原真正起点开始的累计坐标，
\(m_a'=a\)。它们属于同一个真实 \(\mathsf m\)，不是新自由变量。
在任意修复区间 \(J=[s_-,s_+]\) 上，定义

\[
F_1(s)=u\,m_{s_1}+(b^2-u^2)m_{t_1},\qquad
F_0(s)=u\,m_{s_0}+(b^2-u^2)m_{t_0},
\]
\[
\mathcal I_1(J)=
\int_J\{u_s m_{s_1}+(b^2-u^2)_s m_{t_1}\}\,ds,
\]
\[
\mathcal I_0(J)=
\int_J\{u_s m_{s_0}+(b^2-u^2)_s m_{t_0}\}\,ds,
\]
\[
E_{bu}(J)=\int_J\{u b_s^2-b b_su_s\}\,ds.
\tag{24}
\]

对(21)(22)作一次真正分部积分，得到

\[
\boxed{
\Delta m_{r_1}=[F_1]_-^+-\mathcal I_1+\frac14E_b,}
\tag{25}
\]
\[
\boxed{
\Delta m_{r_0}=[F_0]_-^+-\mathcal I_0+\frac14E_{bu}.}
\tag{26}
\]

这些公式使用原 incoming m，不重锚。
如果为了记号给每个累计加一个常数，边项与有序积分会同时改变并
相互抵消；只改积分起点而删掉前缀会破坏(25)(26)。

对从原零历史到完整 \(M=0\) 的词，末端所有 m 也为零，
无论 scalar 端口是否返回，两端 \(F_1,F_0\) 都为零。
故完整返回必须满足

\[
\boxed{\mathcal I_1=\frac14E_b,\qquad
\mathcal I_0=\frac14E_{bu}.}
\tag{27}
\]

第一式的右端在真正非恒 h 路径上严格正。
所以，如果一种方案假设相关累计与几何的有序面积始终为零，
却依靠非恒高度产生 r1 正成本，它不能给完整 \(M=0\)。
这排除该项额外假设下的方案，不排除可以形成非零 \(\mathcal I_1\)
的一般真实路径。

### 5.1 对已有完整前缀的修复门

设末目标是所有 m 归零，入口是真前缀的 \(m^{\rm in}\)，则
(25)(26)准确改写为

\[
\boxed{
\mathcal I_1=
m_{r_1}^{\rm in}
-u_-m_{s_1}^{\rm in}
-(b_-^2-u_-^2)m_{t_1}^{\rm in}
+\frac14E_b,}
\tag{28}
\]
\[
\boxed{
\mathcal I_0=
m_{r_0}^{\rm in}
-u_-m_{s_0}^{\rm in}
-(b_-^2-u_-^2)m_{t_0}^{\rm in}
+\frac14E_{bu}.}
\tag{29}
\]

尤其 R552 的正 \(T_1^{\rm in}\)、未知的其它余槽以及完整 incoming
third 都不能在进入补偿段时删去。第三 history 不显式出现在这些
代数身份中，但它决定同一个 \(\chi\) 下后继几何实际能否存在，
不能因此从 governing ODE 中消除。

若入口 \(m_{t_1}=m_{s_1}=0\) 而 \(m_{r_1}<0\)，且某候选修复额外
证明了 \(\mathcal I_1=0\)，则(28)要求

\[
E_b=-4m_{r_1}^{\rm in}>0.
\tag{30}
\]

结合(23)，至少需要
\(\int v^2\ge-4h_{\min}^2m_{r_1}^{\rm in}\)。
若该修复还保 \(\Delta P_1=0\)、入口/出口 \(T_1=0\)，(17)再要求

\[
\int k^2\ge L-4h_{\min}^2m_{r_1}^{\rm in}.
\tag{31}
\]

(30)(31)明确依赖额外的 \(\mathcal I_1=0\) 条件；一般后继可以用
非零有序面积改变账，不能将此条件性成本误写为普遍不可达。

无需假定面积为零也有真实上界：

\[
|\mathcal I_1|\le
\operatorname{TV}(u)\sup_J|m_{s_1}|
+\operatorname{TV}(b^2-u^2)\sup_J|m_{t_1}|.
\tag{32}
\]

这给任何声称“相关累计全程很小”的有限盒方案一个可直接使用的
必要尺度比较；所有 sup/TV 都必须来自同一实际路径。

## 6. 一个完整的恒真高度障碍

在整个后继区间若 \(h\equiv H>0\)，水平式给
\(\mathfrak r=\eta+u\) 为常数。由 R549 的准确式

\[
p_1-\mathfrak r p_2=k^2/2
\tag{33}
\]

可见，若该后继还保 \(\Delta P_1=\Delta P_2=0\)，则
\(k\equiv0\)。于是 \(\eta\) 也为常数，原全部余密度恰为

\[
t_1=-1/8,\quad s_1=-\eta/4,\quad s_0=-\eta^2/4,
\]
\[
r_1=-\frac{\eta^2+H^{-2}}8,\qquad
r_0=-\frac{\eta(\eta^2+H^{-2})}8.
\tag{34}
\]

因此，**单独一段恒真高度、并要求其 p1/p2 增量都为零的修复**，
不可能补正已为负的同中心 r1；它还必使 t1 进一步减少。
这里“恒真高度”不同于一个渐近恒参考高度；
R552 的实际低尾有小而非零 k、真实 p 增量，并不被本结论替代。

(34)只描述必要的原几何值；它甚至没有自动授予同一非零 incoming
history 与固定 \(\chi\) 的长期恒态解。真实 ruling 若不容许该段，
可用集合更小。本节不排除改变高度、允许中途非零 p 增量再联合
修复的真实方案，也不排除 R521 控制能形成所需(24)面积。

## 7. 原坐标与中心坐标：t1、r1 的号何时可以比较

令原坐标为 x，固定中心坐标为 \(y=x+\omega_c\)，记 \(c=\omega_c\)。
R73 的三个尾基满足

\[
J_1^x=J_1^y-cJ_0,\qquad
J_2^{*,x}=J_2^{*,y}-2cJ_1^y+c^2J_0.
\]

同时代入 \(x=y-c\)，得到原总 p 变换与 t1 变换

\[
P_2^y=P_2^x,\quad
P_1^y=P_1^x-2cP_2^x,\quad
P_0^y=P_0^x-cP_1^x+c^2P_2^x,
\]
\[
\boxed{T_1^y=T_1^x+\frac c2P_2^x.}
\tag{35}
\]

所以三 p 归零以后，R552 的中心正 T1 就是原正 T1；
单段未清 p2 时则不能把二者混同。

在三个总 p 都为零时，剩余五槽的准确变换是

\[
\begin{aligned}
T_1^y&=T_1^x,\\
S_1^y&=S_1^x-2cT_1^x,\\
S_0^y&=S_0^x-2cS_1^x+2c^2T_1^x,\\
R_1^y&=R_1^x-cS_1^x+c^2T_1^x,\\
R_0^y&=R_0^x-cR_1^x-cS_0^x
       +\frac32c^2S_1^x-c^3T_1^x.
\end{aligned}
\tag{36}
\]

因此只清 p 和 t1 时，中心 r1 的负号还不能未经 S1 核对就移到
原 x 坐标。若再清 S1，则 r1 才坐标不变；
若三个下方余槽全清，r0 只剩 \(R_0^y=R_0^x-cR_1^x\)。

(12)的矩阵变换则恰为 congruence：

\[
\mathsf H^y=
\begin{pmatrix}1&0\\-c&1\end{pmatrix}
\mathsf H^x
\begin{pmatrix}1&-c\\0&1\end{pmatrix}.
\tag{37}
\]

故三余槽共同为零以及该 \(2\times2\) 残差矩阵的 inertia 在 p 返回后
不依固定中心；不能靠重新写坐标制造三槽归零。
整个 \(M=0\) 当然也由可逆线性变换保持。

## 8. 同一固定规范中的真实联合修复接口

本稿给必要身份，不给自由原子锥的可达性定理。
从 R552 的真实末状态出发，后继必须继续 R521 的完整系统

\[
h_s=\gamma,\quad k_s=\upsilon,\quad
\eta_s=\upsilon/(2h),\qquad
\gamma_s=a,
\]
\[
\upsilon_s=
-\{\mathcal F(S,\gamma,\upsilon,\mathsf m,\mathbf t)
+C_h(S)a-2\mathbf w(S)\cdot\nu\}/C_k(S),
\]
\[
\mathsf m_s=M_{\rm raw},\qquad
\mathbf t_s=
\bigl[-\Phi_{M_{\rm raw}}\circ\Phi_{\mathsf m}
+\mathcal C_{\rm orig}\bigr]_{\rm original\ finite\ coordinates}.
\tag{38}
\]

\(C_k>0\) 是原 R521 的非退化收据；
它不保证任意控制长期有界，也不授予任意端点矩。
\(\nu,\chi\)、profiles、原右锚及全相位保持同一次选择。
\(\mathbf t\) 不能用新自由第三常数替代。

若欲用若干参数修复余五槽，必须在同一真实解族上：

- 保留完整 incoming \((S,\gamma,\upsilon,\mathsf m,\mathbf t)\)；
- 使用真正光滑的控制及末 germ，或用原已付的平滑切换；
  仅末 h/k 值相等不够；
- 把所有桥、等待、快段、长尾的 m 和 third 继续累计；
- 同时保三个总 p，且满足(11)、(25)(26)全部端项与真实成本。

一个准确的有限维接口如下。假设已构造同一实际族，p2 由真实
横截停止准确为零，保其停止时间的一阶参数导数。
设 \(\theta\in\mathbb R^2\) 是 R552 的两个已付 p0/p1 参数，
\(\xi\in\mathbb R^5\) 是一个**尚待实际构造**的后继控制族。
记实际端点映射为

\[
\mathcal P(\theta,\xi)=(P_0,P_1),\qquad
\mathcal Q(\theta,\xi)=(T_1,S_1,S_0,R_1,R_0).
\]

如果在真实族中 \(D_\theta\mathcal P\) 仍可逆，则隐函数先保 p，
余五槽的真正一阶控制矩阵是

\[
\boxed{
D_\xi\bigl[\mathcal Q(\theta(\xi),\xi)\bigr]
=\mathcal Q_\xi-\mathcal Q_\theta
(\mathcal P_\theta)^{-1}\mathcal P_\xi.}
\tag{39}
\]

所有导数包含 actual 停止时间、控制切换和完整 history 变分。
(39)不是原 profile 矩的一个代数秩，不是可自由赋权的静态锥，
也不是仅看新增段自身的五个密度。

若以后能在真实共同零处支付(39)的满秩与合法域/germ，
有限维 IFT 才能给局部联合修复；本稿没有预授这个假设。
即使全八矩清零，第三/第四 period、frame、位置及主课题其它门
仍须随后完成。

## 9. 已闭范围与下一真实问题

本稿完整支付了：

- 原完整矩阵（含全部二次速度项）的五余槽表(5)，任意真实速度和 incoming 适用；
- 三 p 归零后的三槽矩阵能量(12)、严格正定门(14)、
  真实时间与端点成本(16)–(20)；
- r1 的正高度速度项、r0 的完整交叉项以及真实有序面积
  (21)–(29)，包含任意实际前缀；
- 一个恒真高度、单独保 p1/p2 的准确障碍，范围限于该策略；
- 原/中心坐标的全五槽变换与真正联合端点接口。

所以，R552 的三 p 返回和正 T1 余量并没有自动清余五矩，
也没有遇到本稿所证明的一般不可达定理。
真正下一问题是在同一个完整系统(38)里形成合适的加权矩阵与
有序面积，同时保已清 p，并支付准确端口和全部历史。
任何正向段都必须由该系统本身完成；本稿不以形式配权代替它。

### 来源与固定读取身份

- [R73：逐点八矩与真实第三桥](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  完整原密度(6)(10)(12)(17)，本稿只据这些原式推导；
- [R521：同母全历史非退化加速度控制](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一固定规范和完整真实系统；
- [R549：三 p 与真实水平门](R549-three-p-moment-balance-and-real-horizontal-repair-obstructions.md)：
  p 列、水平关系、原时间/速度能量；
- [R552：三 p 真实联合零与正 T1](R552-three-exact-p-moments-with-one-gauge-and-a-positive-t1-remainder.md)：
  本稿消费的真实入口，不重复其独立核验；
- [R542](R542-complete-second-matrix-sign-and-duration-gates-for-the-fast-ruling-family.md)：
  原/中心 t1 与时间能量身份；本稿没有移植其另一母库的轨道或规范。

读取固定公开提交
`3a4cdd82f27769907100eb143c40abf6de4cbd10`。
R552 原稿 blob 为
`41c3c034c33b384d3c620cb94110eea91e454dfa`；
R521 为 `dc95cb02c51922fef612713134fa0c0da88d9c77`。
全文是原式纸证，没有调用任何科学执行。
