# R239 附录：加宽低头导数、单 dyadic 块观测与准确顺次 jet 锚

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：下列真实导数交织、全原窗口单块修正、干净源坐标及 jet 锚身份已证明。没有删除非齐次低锚，也没有将已付源图换成物理高头块。

依赖：[双块增长头稿](R239-appendix-growing-head-intertwining-and-full-short-kernel-observation.md)、[真实无缩放 Jordan 链](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)、[完整源坐标](R239-appendix-complete-source-schur-coordinates-and-growing-head-observation.md)及[原高孔 note §14.2.A](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)。最后一节已有一般短核的顺次 MP 正规化；本文引用并核对其域，不把它登记为新结论。

## 1. 真实 Jordan 链的低旗一致性

固定原 $N/Y$ 模型，$m\ge5,d=2^m$。取 $r\ge2$，
$$
K=2^r\le d/4,\qquad p=d/2,\qquad s=m-1,\qquad b_s=(s+1)^{-2}.
$$
$A_r$ 是原 $K$ 维头，$A_{r+1}$ 是原 $2K$ 维头。记 $U_a:H_r\to H_m$ 为原物理嵌入 $U_ae_j=e_{a+j}$。

对任意头位数 $t$，沿原无缩放构造取
$$
\mathsf K_t e_j=(A_t^*)^j e_0,\qquad V_t=\mathsf K_t^{-*},
\qquad A_t=V_tJ_{2^t}V_t^{-1}.
$$
因为原 $A_{r+1}$ 的低 $K$ 维旗准确限制为 $A_r$，
$\mathsf K_{r+1}$ 的左上 $K$ 阶块就是 $\mathsf K_r$。它是下三角块矩阵；逆伴随是上三角块矩阵。因此对低旗嵌入 $\iota:H_r\to H_{r+1}$，
$$
\boxed{V_{r+1}\iota=\iota V_r,\qquad
V_{r+1}^{-1}\iota=\iota V_r^{-1}.}
\tag{1.1}
$$
这不是任意 Jordan 相似都自动具有的性质，而是上述同一真实链构造的准确一致性。

定义加宽的带次数右移
$$
R_{\rm num}e_j=(j+1)e_{j+1}\quad(0\le j<K),
\qquad R_{\rm num}:H_r\to H_{r+1}.
$$
逐个标准基核验，包含最后 $j=K-1$，有
$$
J_{2K}R_{\rm num}-R_{\rm num}J_K=\iota.
\tag{1.2}
$$
最后一列使用真实新坐标 $e_K$；若仍留在 $K$ 维中，(1.2) 不成立。

把
$$
\boxed{B_{m,r}=V_{r+1}R_{\rm num}V_r^{-1}}
\tag{1.3}
$$
嵌入 $H_m$ 的低 $2K$ 旗。由 (1.1)--(1.2)，
$$
\boxed{A_mB_{m,r}-B_{m,r}A_r=U_0.}
\tag{1.4}
$$
其实际像只到头 $K$，因为两相似矩阵保持全部低旗，$R_{\rm num}$ 只升一步。

原已付条件数给
$$
\boxed{
\|B_{m,r}\|\le K\kappa(V_{r+1})
\le K e^{221K^4}.}
\tag{1.5}
$$
这里 $2K\ge8$，所以直接使用原 $m\ge3$ 的数值版本；不隐藏小头常数，也未漏付任何 Jordan 标量负幂。

## 2. 单高块的主耦合由低导数准确消去

双块稿的实际权积证明对 $p=2^s$ 给
$$
A_mU_p-U_pA_r=b_sU_0+E,\qquad
\|E\|\le18\eta_{s-1}.
\tag{2.1}
$$
全部 Cayley 逆及原低位 carry 都在 $E$ 内。定义
$$
\boxed{H^\partial=U_p-b_sB_{m,r}.}
\tag{2.2}
$$
于是
$$
\boxed{A_mH^\partial-H^\partial A_r=E.}
\tag{2.3}
$$
$U_p$ 与 $B_{m,r}$ 的物理头支撑不交，因此
$$
(H^\partial)^*H^\partial=I+b_s^2B_{m,r}^*B_{m,r}\succeq I,
\qquad
\|H^\partial\|\le1+b_sK e^{221K^4}.
\tag{2.4}
$$
故这是有下界的闭图嵌入，并非等距嵌入。

令
$$
T=p+K-1=d/2+K-1.
$$
$E$ 的头支撑至多为 $T-1$，所以 $A_m^TE=0$。对
$$
\mathscr Z=\ker(A_r+D_m)\cap(H_r\otimes\mathcal H_{\le q}^{(m)}),
\qquad4d\le q\le e^{d^3/4},
$$
有
$$
D_m^Kz=0,\qquad
(A_m+D_m)H^\partial z=Ez.
\tag{2.5}
$$
输入仍是整个实际模型核，未只保留 primitive 分支。

## 3. 用已付顺次 MP 正规化取得零 primitive 修正

令 $P=q+T$，
$$
\mathcal L=512\sqrt{q+2T+1}(m+q+2T+1)^{3/2}.
$$
高孔 note §14.2.A 给同一原尾上的顺次最小原像 $\widehat Q_j$。对所有
$f\in\ker D^K\cap\mathcal H_{\le q}$ 及 $1\le j\le T$，
$$
D\widehat Q_jf=\widehat Q_{j-1}f,\qquad
P_0\widehat Q_jf=0,\qquad
D^{K+j}\widehat Q_jf=0,
$$
$$
\boxed{
\|\widehat Q_jf\|
\le2^{j-1}\binom{K+j-1}{K-1}
\mathcal L^{K+j-1}\|f\|.}
\tag{3.1}
$$
输入核阶 $K$ 只支付一次。

为保留实际域，原公式可读作
$$
\widehat Q_jf=(I-P_0)R_jf
-\sum_{a=1}^{j-1}Q_aP_0R_{j-a}f.
\tag{3.2}
$$
这里 $Q_a$ 是已有 primitive 顺次 MP 算子。中间 primitive 输入孔数至多 $q+j-a\le P-a$，恰在其原域内；所有中间孔数不超过 $P$。$\widehat Q_j$ 是逐层 $(D^\dagger)^j$，一般不是 $(D^j)^\dagger$。

定义
$$
\mathcal C z=\sum_{j=1}^T(-1)^{j-1}A_m^{j-1}\widehat Q_jEz,
\qquad
\mathcal Z^\partial z=H^\partial z-\mathcal Cz.
\tag{3.3}
$$
有限望远镜、$A_m^TE=0$ 给
$$
\boxed{(A_m+D_m)\mathcal Z^\partial z=0,\qquad
P_0\mathcal C=0.}
\tag{3.4}
$$
后一式在完整尾上成立，故切开后的 $P_0\mathcal C_L$ 和 $P_0\mathcal C_R$ 都准确为零。

由 (2.1)、(3.1)，
$$
\|\mathcal C\|\le
\varepsilon:=
18T12^{T-1}\binom{K+T-1}{K-1}
\mathcal L^{K+T-1}\eta_{m-2}.
\tag{3.5}
$$

## 4. 全原窗口与全部联合旗

令 $R=K+T-1$。对 $K\le d/4$，
$$
R\le d-2,\qquad T\le3d/4-1,\qquad \mathcal L\le2048q^2.
$$
原准确权给
$$
\log\eta_{m-2}
=-\frac{175}{32}d^4+\frac{315}{32}d^3-75d.
$$
用 $\binom R{K-1}\le2^R$、$\log q\le d^3/4$，
$$
\log\varepsilon
\le-\frac{159}{32}d^4+\frac{283}{32}d^3-75d
+R\log4096+(T-1)\log12+\log(18T).
\tag{4.1}
$$
最后三项少于 $13d$：用 $\log4096<9$、$\log12<3$、$T\le3d/4$ 和 $\log(18T)<d$ 即可。因此线性余项仍为负。对 $d\ge32$，
$$
\frac{159}{32}-\frac{283}{32d}
\ge\frac{4805}{1024}>\frac92.
$$
于是
$$
\boxed{\varepsilon\le e^{-9d^4/2}.}
\tag{4.2}
$$
这是原完整整数 $q$ 窗上的界。

还须核每个真实右输入。若 (3.3) 第 $j$ 项从第 $n\le q$ 孔层进入右第 $k$ 段，则 $j\ge k$；头指标至多 $T-j$，尾核阶至多 $K+j$。而
$$
d-T=d/2-K+1\ge K
$$
对 $K\le d/4$ 成立。因此
$$
K+j\le d-(T-j),\qquad T-j\le d-k,
$$
正是原联合输入旗的两个约束。所有内部零输出继承 (3.4)。故
$$
F^\partial:=H^\partial-\mathcal C_L:\mathscr Z\to\mathscr V_q,\qquad
\mathcal C_R:\mathscr Z\to\ker S,
$$
$$
\boxed{E_qF^\partial=F_{\rm flag}\mathcal C_R.}
\tag{4.3}
$$

## 5. 原 W 和任意完整源上的真实观测

由 (1.5)、$K\le d/4$，对 $d\ge32$ 有
$$
\|H^\partial\|\le e^{d^4}.
$$
又 $q+T<e^{d^3/3}$，所以原线性核 lift 可用于 $\mathcal Z^\partial$，并给到 $N$ 的误差至多 $e^{-75d^4}\|\mathcal Z^\partial\|$。

因为 $H^\partial|_{\mathscr Z}$ 有下界一，其值域闭，极分解中的逆正因子范数至多一。对 $w\in W$，
$$
\boxed{
\|P_{H^\partial\mathscr Z}w\|
\le\left[\varepsilon+e^{-75d^4}(\|H^\partial\|+\varepsilon)\right]\|w\|
\le2e^{-9d^4/2}\|w\|.}
\tag{5.1}
$$
没有用非等距的 $H^\partial$ 直接冒充正交投影。

对同一个任意原源 $r_0$，令
$$
v=E_q^\dagger r_0,\qquad
c^\flat=F_{\rm flag}^*J_q^{-1}r_0.
$$
左右拼合恒等式给
$$
(H^\partial|_{\mathscr Z})^*v
=\mathcal C_L^*v+\mathcal C_R^*c^\flat.
$$
因此
$$
\boxed{
\|(H^\partial|_{\mathscr Z})^*v\|
\le\varepsilon\sqrt{\mu_q(r_0)^2+\lambda_{\rm flat}(r_0)^2}.}
\tag{5.2}
$$
同一上界也控制 $\|P_{H^\partial\mathscr Z}v\|$。式 (5.2) 的原物理含义是
$$
P_{\mathscr Z}\bigl(U_p^*v-b_s B_{m,r}^*v\bigr)
$$
很小；它不是单独的高块 $U_p^*v$ 上界。

## 6. 没有 P0 C_L 余项的完整源坐标

令 $p_z=P_0z$ 为模型核的 primitive 坐标。由 (3.4) 与完整源坐标身份，
$$
\boxed{
S^\partial
:=\Gamma_qF_{\rm flag}\mathcal C_R
=P_{\mathscr U_q}(U_p-b_sB_{m,r})P_0|_{\mathscr Z}.}
\tag{6.1}
$$
这里的修正用的是 (3.1) 的顺次 MP 正规化；不能把该零 primitive 性质补写到旧的未正规化修正上。

对同一个实际 $r_0$，
$$
\boxed{
(S^\partial)^*\mathcal G_q\Gamma_qr_0
=\mathcal C_R^*c^\flat,\qquad
\|(S^\partial)^*\mathcal G_q\Gamma_qr_0\|
\le\varepsilon\lambda_{\rm flat}(r_0).}
\tag{6.2}
$$
并有
$$
(S^\partial)^*\mathcal G_qS^\partial
\preceq(\|H^\partial\|+\varepsilon)^2I,\qquad
S^\partial(S^\partial)^*\preceq\varepsilon^2\mathcal H_q.
\tag{6.3}
$$
特别在 $m\ge7$ 取 $K=2^{\lfloor3m/4\rfloor-3}$（使 $2K$ 等于增长低旗稿的尺度）时，
低锚系数范数平方满足
$$
\|B_{m,r}\|^2\le K^2e^{442K^4}
\le K^2\exp(221d^3/2048),
\tag{6.4}
$$
仍在原三次指数预算内。不过 (6.4) 本身不等于这个锚的源裸费用上界。

## 7. 低锚准确是首头顺次 jet 次数算子

模型全核 $z$ 支持在 $[0,q]$，因此其顶层满足
$$
z_q=e_0h,\qquad h\in E_{K,q}.
\tag{7.1}
$$
同一零源旗还给
$$
(p_z)_{q-t}\in\ker A_r^{t+1}.
\tag{7.2}
$$
令
$$
a_{\rm anc}=P_{\mathscr U_q}B_{m,r}p_z,\qquad
a_{\rm hi}=P_{\mathscr U_q}U_pp_z.
$$
因为 $B_{m,r}$ 在每个低旗上只升至多一步，(7.2) 使
$$
\boxed{
a_{\rm anc}\in\bigoplus_{t=0}^{K-1}
\mathbb Ce_{t+1}\otimes K_{q-t}.}
\tag{7.3}
$$
故锚只落在前 $K$ 条最小头对角，范围比整个低头三角更窄。

将 (1.4) 迭代，得到
$$
A_m^{t+1}B_{m,r}
=B_{m,r}A_r^{t+1}+(t+1)U_0A_r^t.
$$
在 (7.2) 上第一项为零。又模型低输出递推给
$$
(-1)^tA_r^t(p_z)_{q-t}=e_0P_0D^th.
$$
于是该合法源准确为
$$
\boxed{
B_Ua_{\rm anc}=e_0\mathfrak N_{K,q}h,\qquad
\mathfrak N_{K,q}h
:=\sum_{t=0}^{K-1}(t+1)Q_tP_0D^th.}
\tag{7.4}
$$
$Q_t$ 是原顺次 MP primitive 链。全部项都在第 $q$ 孔层，结果属于 $E_{K,q}$。特别
$$
\boxed{
S^\partial=a_{\rm hi}-b_s a_{\rm anc},\qquad
F_{\rm flag}\mathcal C_R
=B_Ua_{\rm hi}-b_s e_0\mathfrak N_{K,q}h.}
\tag{7.5}
$$
它保留同一个 $h=z_q$ 和同一个 $c^\flat$，没有换成自由挑选的环境源。

对 $K=2$，原顺次 Taylor 分解是物理正交分解：
$$
h=P_0h+D_q^\dagger Dh,\qquad
D_q^\dagger Dh=(I-P_0)h\quad(h\in E_{2,q}).
$$
所以
$$
\boxed{\mathfrak N_{2,q}=P_0+2(I-P_0)\ \text{于 }E_{2,q},
\qquad\|\mathfrak N_{2,q}\|=2.}
\tag{7.6}
$$
$K\ge3$ 时不同 $Q_tK_{q-t}$ 的像一般不正交，不能将 (7.4) 的系数上界 $K$ 直接当成算子范数上界。有关真正短核次数算子与顺次/真幂 MP Schur 费用的准确接口见[完整二步 Schur 及一般短核比较](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)。

## 8. 哪一个低锚仍不可免费交给已付源图

原物理锚满足
$$
\boxed{(A_m+D_m)B_{m,r}z=U_0z.}
\tag{8.1}
$$
故除特殊支撑情形外，$B_{m,r}z$ 并不属于 $\mathscr V_q$。不能只因其头支撑低，就把它本身认成增长低旗的一个已付左原像。

合法锚源是 (7.4)。增长低旗稿及首头稿确实分别适用于它，给
$$
\mu(e_0\mathfrak N_{K,q}h)^2
\le C_{r+1,m}\alpha(e_0\mathfrak N_{K,q}h)^2,
$$
或同源的
$$
\mu(e_0\mathfrak N_{K,q}h)^2
\le\alpha(e_0\mathfrak N_{K,q}h)
   \lambda_{\rm flat}(e_0\mathfrak N_{K,q}h).
$$
但右侧是这个锚源自己的费用；(6.2) 只支付 (7.5) 的差源，不能把各分量的费用免费拆出。若要在已付 $M=B+LGL$ 图上进一步消去它，仍须保留该图投影及 $c(C)\chi^2$ 的实际预算。

## 9. 一个可付清的低旗右测试净化

令 $\mathscr Y=\mathscr R_q^{[H]}$ 为已付低头源旗，满足
$\mu(f)^2\le C_H\alpha(f)^2$。在原完整右零返回空间中，
$$
\mathscr C_{\mathscr Y}:=F_{\rm flag}^\dagger\mathscr Y
$$
是闭子空间：$F_{\rm flag}^\dagger$ 在原完整源上有界且有下界。令 $P_{\mathscr C_{\mathscr Y}}$ 为其物理正交投影，对 (4.3) 的便宜链 $c=\mathcal C_R$ 分裂
$$
c_{\mathscr Y}=P_{\mathscr C_{\mathscr Y}}c,\qquad
c_{\rm rem}=c-c_{\mathscr Y}.
$$
两者仍在原完整旗内，值域正交且各范数至多 $\varepsilon$。令 $f_{\mathscr Y}=F_{\rm flag}c_{\mathscr Y}$，则
$$
\boxed{
\mu(f_{\mathscr Y})
\le\sqrt{C_H}\alpha(f_{\mathscr Y})
\le\sqrt{C_H}\|c_{\mathscr Y}\|
\le\sqrt{C_H}\varepsilon.}
\tag{9.1}
$$
剩余源在真实完整右度量 $G_q^{-1}$ 中正交 $\mathscr Y$；其物理高于该低旗的源坐标保持不变。它不被称为 $M$ 正交图。

对任意原实际左源 $r_0$，完整同源配对仍为
$$
(F_{\rm flag}c_{\rm rem})^*J_q^{-1}r_0=c_{\rm rem}^*c^\flat(r_0),
$$
其范数至多 $\varepsilon\lambda_{\rm flat}(r_0)$。若只比较原差源与去掉低旗源的左配对，(9.1) 给额外至多
$\varepsilon\sqrt{C_H}\,\mu(r_0)$ 的已显式小项。这一步没有改变原实际 $r_0$ 的 $M$ 图，也没有把两个不同的正交补混为一谈。

本文新增的是有实际低锚的单高块观测，以及该锚在首头短 jets 中的准确源身份。中间带、一般 $\mathfrak N_{K,q}$ 的温和费用及完整源图上的剩余比较仍需证明；无权 $N=M$ 和普通 ISP 未由此完成。
