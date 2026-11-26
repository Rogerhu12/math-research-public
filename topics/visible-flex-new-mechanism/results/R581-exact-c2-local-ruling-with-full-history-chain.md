# R581：保原变化链与真尾的局部第四 ruling 精确 C² 表达

日期：2026-11-26。**已证明；原式纸证。** 本文没有执行新符号、profile 求积、ODE、射击或秩计算。计算入口另列于文末；其尚未完成的数值输出不是本证明的前提。

本稿继续 R530 的有限尺度路线。公开 v2 计算已表明：原分子字段与代数重构相符，并不意味着把数个巨大高导项相减得到的局部 ruling 已准确求积。本稿对原局部项先作准确转置，再在整份正交库上消去唯一三导平方项，最后对剩余三导线性项作保真二尾的分部积分。得到只用母形 $u,u',u''$ 及原二次右尾的完整局部表达。

适用的是 R521 正交库，亦适用于 R578 从起点构造的六变换、六正节点实际库。母库、位置、右锚、几何和 chain 都在同一个式子中。没有使用 R480 的第三 outer 零条件，故没有把 R482(25)移入当前库。

## 1. 原局部项与固定记号

固定 $y=x+\omega_c$。在一个时刻写
$$
z=y+\eta,\quad e=hz-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad\upsilon=k_s,\quad
e_s=\gamma z-\upsilon/2,
\tag{1}
$$
并保真实水平关系 $\eta_s=\upsilon/(2h)$。
两个真实加速度记为 $a=h_{ss},b=k_{ss}$。

取 $\phi=g$、$\Delta=f\odot f-g\odot g$。由 R521/R578 的原正交平均，全相位 ruling 是 $\sin^2\theta$ 乘这个 scalar，故这不是仅检查单个未知相位。

令 $Y_i$ 为第一场 $Y_\phi$ 的分子之第 $i$ 个 $y$ 导数，$K_i$ 为原第二局部场 $K(\Delta)$ 的分子之第 $i$ 个 $y$ 导数：
$$
Y_\phi=\frac{F_{\rm fr}}zY_0,\qquad
K(\Delta)=\frac{F_{\rm fr}}zK_0 .
$$
这里 $F_{\rm fr}$ 是正交 frame，下面的 $F$ 则专指 scalar
$$
F=Q\phi''-2he\phi'+2h^2\phi,\qquad F'=Q\phi'''.
\tag{2}
$$
分子协变时间导数为
$$
\nabla_s V=\partial_sV+\Omega(k)V .
$$
$\partial_s$ 使用 (1) 和真实 $(a,b)$；profiles、原右锚及 $y$ 固定。

令
$$
v=\Phi_{M_{\rm raw}(h,k,\eta,\gamma,\upsilon)}\Delta .
\tag{3}
$$
它是原变化-profile chain。即使当前累计 $A=0$，仍有 $A_s=M_{\rm raw}$，所以 (3)不能删除。

R482 未消历史的 (22)及原 R56 分子恢复给局部项
$$
\mathscr R
=-\frac1h\int |K_1|^2
-\frac1{h^2}\int F'\eta_-
-\frac1{8h^3}\int F\phi'''(Qv'-2hev).
\tag{4}
$$
$\eta_-$ 是原第三 forcing $-2H(Y_\phi,K(\Delta))$ 的局部恢复分子。所有积分均在同一原物理窗口，使用同一个右锚。

## 2. 将第三右积分准确转置

记
$$
T=Y_1\cdot K_1,\qquad
U=Y_1\cdot K_0+Y_0\cdot K_1,
$$
$$
V=(\nabla_sY_0)\cdot K_1+(\nabla_sK_0)\cdot Y_1,
$$
$$
W=(\nabla_sY_1)\cdot K_1+Y_1\cdot(\nabla_sK_1).
\tag{5}
$$
由 R56 的原 $P,B,\eta$ 恢复式逐项代入，
$$
\eta_-=
\frac V{2h}+\frac{e_sT}{2h^2}-\frac{\gamma U}{2h^2}
+\frac{JW}{2h}-\frac{\gamma JT}{2h^2}.
\tag{6}
$$
这里 $Jq(y)=\int_y^{r_y}q(\xi)\,d\xi$，没有把它改为任何微包内的局部原函数。

第一场的 collars 使 $F$ 在物理窗口两端为零。故准确有
$$
\int F'Jq=[FJq]_{\ell_y}^{r_y}+\int Fq=\int Fq.
\tag{7}
$$
该恒等式并不要求 $Jq(\ell_y)=0$。由 (4)–(7)，
$$
\mathscr R=\int\mathcal P,
\tag{8}
$$
其中
$$
\begin{aligned}
\mathcal P={}&-\frac{|K_1|^2}{h}
-\frac{F'V}{2h^3}
-\frac{e_sF'T}{2h^4}
+\frac{\gamma F'U}{2h^4}\\
&-\frac{FW}{2h^3}
+\frac{\gamma FT}{2h^4}
-\frac{F\phi'''(Qv'-2hev)}{8h^3}.
\end{aligned}
\tag{9}
$$
第三右原函数在这里通过准确转置移除；第二场及 $v$ 中的全部真二尾仍在。

## 3. 完整微包原式及最高导数系数

在一个实际微包上写
$$
f=\alpha u,\qquad \phi=cu,\qquad d=\alpha^2-c^2,
\quad p=u',\quad r=u'',\quad t=u'''.
\tag{10}
$$
字母 $d$ 仅在本稿这一微包代数中表示系数差，不是几何量 $h\eta-k$。

保留三条真正的完整块二尾
$$
J_0=J\{(f'')^2-(g'')^2\},\quad
J_1=J\{y((f'')^2-(g'')^2)\},
$$
$$
J_2=J\{y^2((f'')^2-(g'')^2)+2((f')^2-(g')^2)\}.
\tag{11}
$$
它们在当前微包左、右一般不为零。在这个微包内部，原导数是
$$
J_0'=-dr^2,\qquad
J_1'=-ydr^2,\qquad
J_2'=-d(y^2r^2+2p^2).
\tag{12}
$$

为使 (9)可以逐式复算，令 $d_g=h\eta-k$，并写
$$
\begin{aligned}
a_h={1\over16h^2}\{&
2Qdpr-zQdr^2-2he\,dp^2\\
&+(1+k^2-h^2\eta^2)J_0-2h^2\eta J_1-h^2J_2\},\\
a_k={1\over32h^2}\{&
Qdr^2+2h(hJ_1+d_gJ_0)\}.
\end{aligned}
\tag{13}
$$
原局部恢复及其一阶空间导数为
$$
\eta_{\rm loc}=\gamma a_h+\upsilon a_k,\qquad
(\eta_{\rm loc})'=\frac{dQ(\gamma p-e_sr)t}{8h^2}.
\tag{14}
$$
另记
$$
P=\frac{(1+d_g^2)J_0+2hd_gJ_1+h^2J_2}{8h}
+\frac{e\,dp^2}{8},
$$
$$
B=\frac d{2h}\{p^2/4+(hu-ep/2)^2\},
$$
$$
P'=-\frac d{2h}\{r^2/4+(hp/2-er/2)^2\},
$$
$$
B'=\frac d h\{pr/4+(hu-ep/2)(hp/2-er/2)\}.
\tag{15}
$$
于是
$$
K_0=(\eta_{\rm loc}/h,zP+B,e\eta_{\rm loc}/h),
$$
$$
K_1=((\eta_{\rm loc})'/h,P+zP'+B',
\eta_{\rm loc}+e(\eta_{\rm loc})'/h).
\tag{16}
$$
第一分子则是
$$
Y_0=c(-p/2,0,hu-ep/2),\qquad
Y_1=c(-r/2,0,hp/2-er/2).
\tag{17}
$$
(13)–(17)都是原字段的准确等式，未取高频近似。

由原 E8 表，$v$ 是 $y,u,p,J_0,J_1,J_2$ 的多项式；因此 $v'$ 至多使用 $r$，不含 $t$。对 $K_0,K_1$ 真正作时间协变导数不会提高 $u$ 的空间导数阶数。因此 (9)关于 $t$ 的次数至多为二。

置
$$
\beta=\frac{Q(\gamma p-e_sr)}{8h^3}.
\tag{18}
$$
由 (16)，$K_1$ 中的 $t$ 系数是 $d\beta(1,0,e)$。由 (17)及原协变导数，(5)中 $t$ 的系数分别为
$$
T_t=\frac{cd\beta}{2}(ehp-Qr),\qquad
U_t=cd\beta(ehu-Qp/2),
$$
$$
V_t=cd\beta e(\gamma u-e_sp/2).
\tag{19}
$$
在 (9)中，$FW,FT$ 和原 chain 项至多线性依赖 $t$。其余三项用 (19)相加：含 $u$ 的两项相消，含 $e e_s p$ 的两项相消，留下
$$
-\frac{c^2d\beta Q^2}{4h^4}(\gamma p-e_sr)
=-\frac{2c^2dQ\beta^2}{h}.
$$
加上 $-|K_1|^2/h$ 的 $t^2$ 系数，完整最高项准确为
$$
\boxed{
[\mathcal P]_{t^2}
=-(d^2+2c^2d)\frac Qh\beta^2
=-(\alpha^4-c^4)
\frac{Q^3(\gamma p-e_sr)^2}{64h^7}.}
\tag{20}
$$
这里 (20)是完整局部式的系数，不只是某个分子的主项。

## 4. 最高项在同一实际正交库上准确消失

固定微包母形和一个参考位置时，正交旋转、反射只作用于系数向量 $(\alpha,c)$。R521 的十六元平均或 R578 的六元平均均准确有
$$
\sum_{\mathcal G}\alpha^4=\sum_{\mathcal G}c^4.
\tag{21}
$$
所以 (20)在参考同位置的群和为零。

实际副本的位置不同。不能在一个实际块内先删掉 (20)，再只称其为“平均”。对完整微包平移，(20)积分关于平移位置的次数至多八：$Q^3$ 至多六次，$(\gamma p-e_sr)^2$ 至多二次。R521/R578 给每个群元素相同的正位置矩 $0,\ldots,10$，故能先将每个群元素的完整最高项积分转到共同参考分布，再用 (21)。因此对整份实际库
$$
\boxed{\sum_{\rm actual\ blocks}\int [\mathcal P]_{t^2}t^2=0.}
\tag{22}
$$
此处只消费已经证明的有限位置矩恒等式；没有把真实不交的 blocks 当成重叠物理字段，也没有让实际幅权依赖当前几何或时间。

## 5. 剩余线性三导项的保真分部积分

将 (9)的 $t^2$ 项按 (22)从**全库总积分**中移除，余式唯一写为
$$
\mathcal P_0(y,u,p,r,J_0,J_1,J_2)
+\mathcal A(y,u,p,r,J_0,J_1,J_2)t .
\tag{23}
$$
所有几何量、真实加速度和微包常系数保留在系数中。

先在形式独立变量 $r$ 上取从零开始的多项式原函数
$$
\Psi(y,u,p,r,J)=\int_0^r
\mathcal A(y,u,p,\rho,J)\,d\rho.
\tag{24}
$$
定义
$$
\begin{aligned}
D_0={}&\partial_y+p\partial_u+r\partial_p
-dr^2\partial_{J_0}-ydr^2\partial_{J_1}\\
&-d(y^2r^2+2p^2)\partial_{J_2}.
\end{aligned}
\tag{25}
$$
由 (12)，沿原微包的完整导数准确为
$$
\frac d{dy}\Psi=D_0\Psi+\mathcal A t.
\tag{26}
$$
母形为双 collar 紧的光滑函数，故微包两端 $r=0$；(24)使 $\Psi=0$，不论二尾的 incoming 值为何。因此
$$
\int_{\rm micro}\mathcal A t=-\int_{\rm micro}D_0\Psi.
\tag{27}
$$
原函数必须先按 (24)形成，再按 (25)求导。$D_0$ 含 $r\partial_p$ 和二尾的 $r^2$ 系数，与关于 $r$ 的积分不交换；实现中不使用把它们交换的捷径。

完整块的所有间隙仍须计算。间隙内 $u=p=r=t=0$，但 $J$ 可能不为零，故 $\mathcal P_0$ 的真尾项可以不为零。不能因第一场在间隙为零，就删去局部 second 的尾能量。

由 (8)(22)(27)得到最终身份：
$$
\boxed{
\mathscr R
=\sum_{\rm actual\ blocks}
\int_{\rm whole\ block}
\{\mathcal P_0-D_0\Psi\}.}
\tag{28}
$$
右侧只用 $u,u',u''$ 和 (11)的真二尾，保所有实际微包、间隙、原 chain 和真实 $(a,b)$。全块两外 collars 中二尾严格为零是原完整三矩条件的结果，未在微包之间另设零锚。

## 6. 完整 ruling 中的准确位置与适用边界

(28)是原未消历史公式中的**完整局部项**，不是整条路径的总 ruling。对原真实八矩累计 $A$、第三投影
$$
t_j=I_{j,y}\{g,T(g;\Delta)\}
$$
及固定 Gram $\nu$，仍须使用
$$
\boxed{
\mathscr K=
\mathscr R+
\mathscr L(\Phi_A\Delta)
-\mathcal E(\Phi_A\Delta,\Phi_A\Delta)
-4\mathbf w_y\cdot t-2\mathbf w_y\cdot\nu .}
\tag{29}
$$
全部第二、第三 incoming 及原有序演化照旧保留。本文没有为 $\mathscr L,\mathcal E,t$ 另授未经证明的 C² 降阶或稳定精度，也没有用 (28)宣布一个完整反馈轨道已可准确评价。

本文特别不使用 R482 的第三记忆消去式 (25)，因为它需要 R480 从起点选择的 outer 条件。R521/R578 的母库不能仅凭本稿局部等式借用它。完整第三、第四 period 和十三规范仍是原独立端门。

## 7. 与公开计算入口的对应

对应源码为
`scripts/r530_c2_r578_evaluator_agent.py`；
请求为
`computations/request-r530-c2-r578-20261126.json`；
workflow 为
`.github/workflows/visible-r530-c2-r578-20261126.yml`。

源码先在形式变量 $(y,u,p,r,t,J_0,J_1,J_2,c,d)$ 中形成 (9)，直接核其 $t^2$ 系数与 (20)，再执行 (24)(25)。仅在整库总积分位置利用 (22)。三个加速度实例在形式系数层先相减，避免由两个巨大求积值相减读取加速度列。原 R56 direct 值只用于本次新表示的条件数诊断，不是以后重复执行的门。

**实际幅权的准确实现。** R578 每个真实 block 的正幅因子是 $w^{1/4}$。实现的 f/g/raw 数组先不乘这一因子，二尾也使用同一个未幅权完整 block；当前 (9)与(28)的所有项都是原输入的齐次四次式，所以实际幅因子可整体提出为 $w$，恰由 `block_weights` 在最终 `integral` 中乘入。每条二尾只在真正的完整 32 微包 block 外归零，内部微包和间隙没有重置。

这不是任意低次函数的加权空间积分约定。将来完整历史中若仍对固定 $A$ 的四次读出提权，须逐项保持同一齐次身份；已经是全库累计配对的 $t,\nu$ 不得再次按 block 权重相乘。更改母形、位置或宽度也不能沿用旧求积表。

在本机执行环境失联后，公开源码由同一已审公式重建，使用其新实际 SHA-256；不将原暂存稿的 hash 冒作重建文件身份。科学执行限本公开仓库 Actions。固定同一模型的求积加密可以评价 (28)的数值收敛；它尚不构成有限八矩根、真实响应秩、pose、第四 period 或主几何完成门。

### 原来源

- R56（原索引中的完整恢复稿）：原第二、第三分子恢复与真右积分。
- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原八矩、变化-profile chain 及完整有序第三累计。
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)未消历史的 (22)(24)：原局部项与完整历史分解；本稿不引用其需 R480 的 (25)。
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：完整实际正交库、十次位置矩及加速度原正积分。
- R578：六正交变换、各六正节点的实际不交库与严格双 collar 间距。
