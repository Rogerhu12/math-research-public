# R692 — 同 q♯ 的四轴三态、原三中央与实际四单位分区

日期：2026-11-15。**状态：已证明。**

本篇保持 R679 的同一个 $q_N^\sharp$。不采用 R690 之后尚待构造的新测试，
也不将 R690 的真实 $B_W$ 改认成 $T$。
R686 的原 Y/Z、W/V 核可在**同一个完整三态**上合用；
其中 Y 反射是实际物理变换，不能在一个 W 管中删去。
这给任意真实核心词的原 T 返回，以及第三条秩二来源在真实进入支上的条件行。
四个深轴在原 primitive 平面中两两不交，因而还能保全原四-unit域的有限公式。

已知三中央零仍不消掉近相消支上的另一观察。
以下把这一差异写成实际坐标与完整 CM 纤维，而不把不同观察的同名核心混合。

## 1. 同一六输入、两个框架和覆盖

用 R686 的原
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
b_Y=\frac{20+3\omega}{17},
$$
$$
Z=W-b_YY,\quad V=36Y-(17-3\omega)W,\quad
E=(5+6\omega)A-29c-(58+87\omega)d.
\tag{1}
$$
其中 $N(A)=29$。准确有
$$
\operatorname{Gram}(Y,17Z,E)=\operatorname{diag}(34,8942,7627),
$$
$$
\operatorname{Gram}(W,V,E)=\operatorname{diag}(72,18936,7627).
\tag{2}
$$
原三个 A 伙伴仍逐个保留。
写 $a=17-3\omega$，则
$$
W=b_YY+Z,\qquad
V=\frac{263}{17}Y-aZ,\qquad
36Y=V+aW.
\tag{3}
$$
这些单位判断只用 $2,3,17,263,349$ 为固定好因子；当前普通 ray 已排除这些素数。特别 $N(17-3\omega)=349$，不能只检查两个框架行列式。

记
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad
\gamma=\chi_{29,p}\chi_{7627,p}\in\{\pm1\}.
\tag{4}
$$
R686 已以同一原两 sigma 锚付 $\chi_{7627,p}^2=1$；
没有为本篇增加一条射线。

用原 $W$ 四挠来源
$$
f_t=\mathsf T^{72}_{W,t}\mu_0,\quad t\in E[4],\qquad
a_t=\begin{cases}-1/4&t\in E[2],\\+1/4&t\notin E[2],\end{cases}
$$
$$
e_0=\mu_0,\qquad e_1=\sum_ta_tf_t,\qquad
e_2=-\frac14\sum_{t\in E[4]}f_t,\qquad h=e_1+e_2.
\tag{5}
$$
这里 $\mu_0$ 包括原 C 角平均；该平均逐个固定 (1) 的方向，
并与下述完整算子交换。
(5) 是 R488/R638 的原三态，不是重新选取的边际。

原两加倍坐标 $(2Y,34Z)$ 将全部 $f_t$ 放入同一个
$$
\mathcal S_{136}\otimes\mathcal S_{35768}
\tag{6}
$$
第一平面格，E 及三个原伙伴照旧保留。
确实 W 平移在未加倍 $17Z$ 生成变量的分量是 $t/17$；
加倍后其 Heisenberg 参数是 $t/34$，
且 $35768t/34=263(4t)$ 为格点。
第一 $2Y$ 的合法参数是 R501 的原参数。
所以没有把 quarter flat 特征当作原未覆盖 degree34/8942 的平凡特征。

## 2. 完整二挠算子及三态上的 Y/Z 来源

令
$$
B_{2,Y}=\frac12\sum_{u\in E[2]}\mathsf T^{136}_{Y,u}-I.
$$
其 $+1$ 部分是原 $[2]^*\mathcal S_{34}$。
在 (5) 上的二挠不变投影只保 $t\in E[2]$：
其余三个非零二挠 flat 类由实际平移参数区分。
因此整来源满足
$$
P_{2,Y}e_0=e_0,\qquad
P_{2,Y}e_1=P_{2,Y}e_2=h/2.
$$
从而
$$
\boxed{R:=B_{2,Y}:\quad e_0\mapsto e_0,\quad e_1\leftrightarrow e_2.}
\tag{7}
$$
这就是 R638 的 whole 三态身份，保所有五个 Y 伙伴。

还需要把 R686 的平面总核心付到所有三态。
原第一态上它为 $\gamma I$。
完整 Y/Z 平面核同时把 W 的 canonical 平移参数 $t$ 送到 $g_\pi t$。
当前 $g_\pi\equiv-1\bmod4$，故
$g_\pi t=-t+\ell$，其中 $\ell$ 是原格周期。
degree72 的周期特征为一；与四挠参数的交叉指数含
$72/4=18$，所以其符号也为一。
这准确给
$$
K_YK_Z f_t=\gamma f_{-t}.
\tag{8}
$$
(5) 的三个系数表都在 $t\mapsto-t$ 下不变。
所以整平面核心在三态上都是 $\gamma I$，不仅在两条边际上如此。

原 whole degree136 核是
$$
K_Y=R_YB_{2,Y},\qquad K_Y^2=I,
$$
其中 $R_Y$ 为实际第一轴反射。
与 (7)、(8) 比较，得到
$$
\boxed{K_Y=R_YR,\qquad K_Z=\gamma R_YR
\quad\text{在整个原三态及全部伙伴上成立}.}
\tag{9}
$$
这里没有把 $K_Z$ 认成整个 $\mathcal S_{35768}$ 的 scalar。
$R_Y$ 保 Z、E 和三个 A 伙伴，却改变 W；后面一直保这个物理作用。

## 3. W/V 来源、同一原权及全部实际单轴式

R488 的原 W 核是
$$
\boxed{K:\quad e_0\leftrightarrow e_1,\qquad
e_2\mapsto-e_0-e_1-e_2,\qquad K^2=I.}
\tag{10}
$$
Y/Z 与 W/V 是同一平面，所以 (8) 又给
$$
K_W=K,\qquad K_V=\gamma K
\tag{11}
$$
于全部三态。

R686 已证明 $q_N^\sharp$ 的原 C-unit、H-deep 门和完整六/十二次权
均正交于 Y、Z、W、V。以下也允许第4节的共同隐藏权 $\phi$，
并写 $\rho_i=\phi e_i$。原三个态的所有来源身份与这些权交换。

定义真实物理映射
$$
A_Y=R_YP_{Y,\kappa},\qquad A_Z=R_YP_{Z,\kappa},
\qquad A_W=P_{W,\kappa},\qquad A_V=P_{V,\kappa}.
\tag{12}
$$
于是完整测度式为
$$
\boxed{
\begin{aligned}
\rho_i|_{Y\in p}&=\lambda(A_Y)_*(R\rho_i),&
\rho_i|_{Z\in p}&=\gamma\lambda(A_Z)_*(R\rho_i),\\
\rho_i|_{W\in p}&=\lambda(A_W)_*(K\rho_i),&
\rho_i|_{V\in p}&=\gamma\lambda(A_V)_*(K\rho_i).
\end{aligned}}
\tag{13}
$$
例如 $A_Z$ 把 $(Y,Z)$ 送到 $(-Y,\kappa Z)$；
它不是只缩放 Z。$A_Y$ 把这对坐标送到 $(-\kappa Y,Z)$。
混合 unit cut 必须按这两个完整式运输。

在基 $(e_0,e_1,e_2)$ 中、列表示作用的像，
$$
R=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},\qquad
K=\begin{pmatrix}0&1&-1\\1&0&-1\\0&0&-1\end{pmatrix}.
\tag{14}
$$
原关系为 $R^2=K^2=(KR)^4=I$。
从 $e_0$ 出发的来源轨道准确为
$$
\boxed{e_0,\quad e_1,\quad e_2,\quad-e_0-e_1-e_2.}
\tag{15}
$$
来源关系不把各词的物理像格作商。

## 4. 实际词像格与原 T 的完整返回

设 $\mathfrak w=(a_1,\ldots,a_r)$，每个 $a_j$ 属于 $\{Y,Z,W,V\}$，
令
$$
M_{\mathfrak w}=A_{a_1}\cdots A_{a_r},\qquad
n_\gamma=\#\{j:a_j=Z\text{ 或 }V\}.
$$
依次按 (13) 限制并在各自整像上取逆，
准确得到
$$
\boxed{
\rho_0|_{M_{\mathfrak w}\mathcal O^6}
=\lambda^r\gamma^{n_\gamma}
(M_{\mathfrak w})_*
(S_{a_r}\cdots S_{a_1}\rho_0),
\quad S_Y=S_Z=R,\ S_W=S_V=K.
}
\tag{16}
$$
这是真正逐次像格，不是各原轴深条件的朴素交集。
任意另附原输入条件都必须按 $M_{\mathfrak w}$ 全部转置。
其余四个共同伙伴逐点固定。

现在特别取原 $\phi=q_N^\sharp$，$N\in4\mathbf Z_{>0}$。
完整 $\pi_4$ 中性可沿 Y、W 的 whole 算子逐步传递：
$\pi_4$ 行空间包含 Y、W，故这两个第一轴对应下降到其实际推前；
而 $\phi$ 与两个算子都交换。因而整个三态的 $\pi_4$ 推前，
都准确等于未加权态的 $\lambda^N$ 倍。

原 W 边际遂为
$$
\boxed{
W_*(\rho_0,\rho_1,\rho_2)
=\lambda^N6\delta\,(T,T,-T).
}
\tag{17}
$$
这一步限于**未附额外 E 门**的原 $q_N^\sharp$。
若采用 $q_N^{cd}$，R690 的正确三条边际仍是
$$
B_W,\quad K_{72}B_W,\quad
-\frac12H_{2,W}B_W-K_{72}B_W;
\tag{18}
$$
不能从 $H_{2,W}T=0$ 推得 $H_{2,W}B_W=0$。

由 (15)、(17)，每个词的返回态有一个准确符号
$\tau_{\mathfrak w}\in\{\pm1\}$。
所以同一原词域上的完整 Mellin 行是
$$
\boxed{
\int_{M_{\mathfrak w}\mathcal O^6}
 f_w(W\circ M_{\mathfrak w}^{-1})\,d\rho_0
=\tau_{\mathfrak w}\gamma^{n_\gamma}
 \lambda^{r+N}6\delta J_T(w).
}
\tag{19}
$$
$f_w(x)=1_{x\in\mathcal O^\times}\langle x\rangle^{d_pw}$。
观察是所示逆映像，包含 (12) 的 Y 反射；没有额外未记尺度 log。
系数为单位。因此原 $J_T'(0)=0$ 合法传到所有 (19)，
并不要求另给 (15) 的某个态一个中央零。

## 5. 同一三态上的原 S、新曲线及参考行

使用 R483 的 whole 第一 $2Y$ 投影 $P_S,P_{\rm new},P_H$。
原 $P_{\rm new},P_H$ 在 $h$ 上全零，因为 h 的整个第一轴仍在
$[2]^*\mathcal S_{34}$。故保完整五伴随有
$$
\boxed{
P_{\rm new}(e_0,e_1,e_2)
=(0,S_{\rm new}\otimes\Lambda_{\rm old},
       -S_{\rm new}\otimes\Lambda_{\rm old}),
}
\tag{20}
$$
$$
\boxed{
P_H(e_0,e_1,e_2)
=(0,H_{\rm ref}\otimes\Lambda_{\rm ref},
       -H_{\rm ref}\otimes\Lambda_{\rm ref}).
}
\tag{21}
$$
$P_S$ 的三条来源均为同一 $S(2\,\cdot)$ 乘各自完整伴随。
乘 $\phi$ 后仍成立，因为它独立于第一 Y 轴；
不能因此认三个完整伴随相同。

对于未附额外门的 $\phi=q_N^\sharp$，第4节的整条 $\pi_4$ 返回
给如下准确物理 Y-Mellin 系数：
$$
\begin{array}{c|ccc}
 &\rho_0&\rho_1&\rho_2\\ \hline
P_S&
\lambda^N J_S&
\lambda^N\frac{\omega^2}{2}J_S&
\lambda^N\frac{\omega^2}{2}J_S\\[1mm]
P_{\rm new}&0&
\lambda^N\frac{52}{3}\langle2\rangle^{-d_pw}J_{\rm new}&
-\lambda^N\frac{52}{3}\langle2\rangle^{-d_pw}J_{\rm new}\\[1mm]
P_H&0&
\lambda^N c_H\langle2\rangle^{-d_pw}J_H&
-\lambda^N c_H\langle2\rangle^{-d_pw}J_H
\end{array}
\tag{22}
$$
其中
$$
c_H=-\frac{1+\delta}{2016b},\qquad J_H(0)=1+\lambda.
$$
物理输出是 Y，而固定新线/参考的第一 theta 轴是 $2Y$；
因此 (22) 的 $\langle2\rangle^{-d_pw}$ 必须保留。
S 行中 $S(2z)$ 的尺度恰与它抵消。

三原中央失败的准确输入仍只是
$$
J_S'(0)=J_T'(0)=J_{\rm new}'(0)=0.
\tag{23}
$$
它消掉 (19)、(22) 的相应完整秩二行；
不消掉参考行，也不消掉第一轴其余真实谱。


### 5.1 三条原算术行随真实词一起运输

返回态按 (15) 的顺序，其完整物理第一行系数为
$
\begin{array}{c|rrrr}
 &e_0&e_1&e_2&-e_0-e_1-e_2\\ \hline
W/(6\delta T)&1&1&-1&-1\\
P_S/S&1&\omega^2/2&\omega^2/2&\omega\\
P_{\rm new}/S_{\rm new}&0&52/3&-52/3&0\\
P_H/H_{\rm ref}&0&c_H&-c_H&0 .
\end{array}
\tag{23a}
$
新线与参考行仍含 (22) 的物理 $2^{-1}$ 尺度。

在 (16) 的真像格上，先取已付整像逆，
再施完整第一轴 CM 投影，最后乘回 $M_{\mathfrak w}$。
这定义准确的运输后算子
$
P_{\alpha,\mathfrak w}
=(M_{\mathfrak w})_*P_\alpha(M_{\mathfrak w}^{-1})_* .
\tag{23b}
$
它只在 (16) 显示的受限来源上使用；逆返回后已经是 (15) 的
完整原 theta 来源，故不是把 CM 算子凭空延到任意受限测度。

取观察 $Y\circ M_{\mathfrak w}^{-1}$，
所得整条 Mellin 行正是
$\gamma^{n_\gamma}\lambda^{r+N}$ 乘 (23a) 对应曲线行。
因此 (23) 合法控制每个词的三条**实际运输后算术行**。
没有把 (23b) 改成原未运输的 $P_\alpha$，也没有把原 Y 单位门
改成一个不同的 W 单位门。

## 6. 第三中央进入实际 Y/Z 环带；参考非齐次差

由 (9)，第一 S 投影的 Z 核为 $\gamma\lambda$；
新线及参考的 Z 核为 $-\gamma\lambda$。
这些是完整来源核心，允许再带任意原共同隐藏权。
于是对 $a,b_0\ge0$，在实际
$$
\mathcal A_{a,b_0}=\{v_p(Y)=a,\ v_p(Z)=b_0\}
$$
上，用观察 $f_w(Y/p^a)$，新线的整条行等于
$$
\boxed{
(-\lambda)^a(-\gamma\lambda)^{b_0}(1+\gamma\lambda)
 \langle\lambda^2\rangle^{a d_pw}
 \lambda^N\frac{52}{3}\langle2\rangle^{-d_pw}J_{\rm new}(w)
}
\tag{24}
$$
于态 $\rho_1$，态 $\rho_2$ 取其相反数。
参考行把 $52J_{\rm new}/3$ 换成 $c_HJ_H$。
S 行相应使用 $\lambda^a(\gamma\lambda)^{b_0}(1-\gamma\lambda)$
和 (22) 的实际 S 系数。

若 $a>b_0$，(3) 准确给
$$
\boxed{v_p(W)=v_p(V)=b_0.}
\tag{25}
$$
因此 (24) 确实在 R686 的进入支及其所有后续环带中，
不是另造一个与实际失败支无关的矩形。

记参考行的中央导数为 $L_{a,b_0}$。未知 $J_H'(0)$ 和
$\log\langle2\rangle$ 在以下真环带差中同时消去：
$$
\boxed{
(-\lambda)^{-a}L_{a,b_0}-L_{0,b_0}
=\lambda^N c_H(-\gamma\lambda)^{b_0}(1+\gamma\lambda)
 (1+\lambda)\,a d_p\log\langle\lambda^2\rangle.
}
\tag{26}
$$
$a>0$ 时右边非零；显示固定因子及 $1\pm\lambda$ 均为单位。
$\log\langle\lambda^2\rangle\ne0$ 仍由其非根单位的全局 norm 得出。
这不是声称左边各项的参考导数已经为零。

(24) 与 (26) 使用同一个来源、同一 $q_N^\sharp$、
同一真实 Y/Z 条件。原三个中央只消 (24) 的秩二行；
参考的实际非齐次差仍须与其完整 CM 投影及其它谱一起保留。

## 7. 同一个四-unit 域的完整有限分区

令
$$
\mathcal G_4=\{Y,Z,W,V\in\mathcal O^\times\},\qquad
\mathcal D_{\rm pl}=\{Y,Z\in p\mathcal O\}
=\{W,V\in p\mathcal O\}.
$$
由 (3) 的四个单位系数及单位行列式，
在 primitive 平面 $\mathcal O^2\setminus\mathcal D_{\rm pl}$ 中，
四个轴深支两两不交。
所以逐点恒等式准确为
$$
\boxed{
1_{\mathcal G_4}
=1-1_{Y\in p}-1_{Z\in p}-1_{W\in p}-1_{V\in p}
 +3\,1_{\mathcal D_{\rm pl}}.
}
\tag{27}
$$
在四轴均深的点，右边为 $1-4+3=0$；
在 primitive 点至多一轴深。
这里不是把两套独立单位域误作同一个事件。

置 $P_{\rm pl}=P_{Y,\kappa}P_{Z,\kappa}$
（等于 W/V 两轴同缩放），(13) 给整个三态的有限公式
$$
\boxed{
\begin{aligned}
\rho_i|_{\mathcal G_4}
={}&\rho_i-\lambda(A_Y)_*R\rho_i
-\gamma\lambda(A_Z)_*R\rho_i\\
&-\lambda(A_W)_*K\rho_i
-\gamma\lambda(A_V)_*K\rho_i
+3\gamma\lambda^2(P_{\rm pl})_*\rho_i .
\end{aligned}}
\tag{28}
$$
所有原共同隐藏权仍保留。对任意完整连续测试均成立。
没有把这个有限式宣称为全部连续测试上的可逆算子；
例如它在常数向量上的矩阵不决定高层紧开测试的可逆性。

对一般隐藏权，记完整三态质量向量为 $m$。
(28) 的准确四-unit质量是
$$
\boxed{
\bigl((1+3\gamma\lambda^2)I
 -(1+\gamma)\lambda(R^t+K^t)\bigr)m.
}
\tag{29}
$$
这里 $m=(\rho_0(1),\rho_1(1),\rho_2(1))^t$；(14) 按列给来源像，所以质量列向量必须使用转置。也可逐态直接读 (28)。
同 $q_N^\sharp$ 未附门时 $m=0$，但局部 E 门或 $q^{cd}$ 不适用此零。
R690 的第二态和第三态质量仍要按 (18) 计算。

## 8. 完整算术投影在四-unit 域中的真正切集

不能将 $P_{\rm new}$ 或 $P_H$ 穿过 (28) 的 W/V 深支。
这些投影在第一轴作用，W/V 却混合第一轴与 Z。

为给出可直接使用的实际式，将 R483 的有限投影按 canonical
CM 纤维展开。每条第一轴分支有实际标签
$$
\alpha=\gamma_{13}^{\,j}\gamma_{19}^{\,k},
\quad0\le j\le17,\quad k\in\{0,1\},
$$
及 $\zeta\in\mu_6$；保全部原纤维、归一 $\alpha^{-1}$ 和原中心。
这条分支的物理第一轴测试准确变为
$$
Y\longmapsto\zeta Y/\alpha,
\tag{30}
$$
另外五个 Y 伙伴逐个固定。
因此四-unit域的实际拉回是
$$
\boxed{
Y,Z\ {\rm unit},\quad
b_Y\zeta Y/\alpha+Z\ {\rm unit},\quad
\frac{263}{17}\zeta Y/\alpha-aZ\ {\rm unit}.
}
\tag{31}
$$
$\phi$ 在这些分支中不变，因为它与 Y 正交；
Mellin 行另保 $\langle\alpha\rangle^{-d_pw}$ 的实际尺度。
参考行的导数尤其要保其非零质量乘该尺度 log。

所以 (22)–(26) 与 (28) 联用时，得到的是 (31) 的
**完整有限 CM 切集族**及其余两个深支；
不是把所有 (31) 免费改回 $\mathcal G_4$。
同样，在先作实际 W 核后，观察为
$Y\circ P_{W,\kappa}$，原深域必须按该整矩阵转置，
不能把它改成原第一 Y 观察。

本篇新增的原算术接点是：
全部四轴真三态词均有 (19) 的完整原 T 返回，
原第三曲线有 (24) 的实际进入支零，
参考则在同一原环带有 (26) 的非零差；
它们的同域比较准确受 (27)–(31) 约束。
主目标仍未完成。尚须控制原三单位相对行、真实近相消观察
与这些有限 CM 切集之间的完整余项，不能由一个参考或角域非零直接收尾。

## 9. 独立公开复现

只提交独立脚本，不保存可重算证书或 Actions 输出：
[check-r692-four-axis-three-state-and-unit-partition.js](../scripts/check-r692-four-axis-three-state-and-unit-partition.js)。

命令：
$$
\texttt{node scripts/check-r692-four-axis-three-state-and-unit-partition.js}
$$
脚本无外部依赖；公开 Actions 运行时将打印暂态证书和 SHA256。
本稿提交时未在会话 V8 执行该数值检查；
真实公开 run 标识与输出散列由主线程运行后登记。

脚本核三态矩阵、四挠二挠投影的全部16标签、
四态来源轨道、显示关系及四条轴的成对单位行列式。
原整个 theta 格、中心、所有测度量词及算术尺度的证明在正文。

依赖：
[R638](R638-original-yw-three-state-and-word-compensation.md) 的原 whole 二挠身份；
[R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)；
[R488](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)；
[R496](R496-original-new-axis-even-core-and-four-source-group.md)；
[R501](R501-whole-cm-exchange-and-identical-five-companion-rows.md)；
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)；
[R686](R686-original-yz-core-and-same-source-st-unit-failures.md)。
