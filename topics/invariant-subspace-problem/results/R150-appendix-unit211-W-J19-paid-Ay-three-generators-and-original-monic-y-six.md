# R150：J19 已付后整个余 W 的 A[y] 三生成元与原首一 y 六次式

**状态：已证明并实际返回。** 三条完整原二次式现在能以已付权单位同时解出 x²、xt、t²。整个当前 W 必要商在 A[y] 上由 1,x,t 生成；所有真乘法、两条重叠及原 EBo/Ns/Ps 都保留。三个固定三列原余子式实际给出 y 六次必要式，其中最小一条的首项全部已付，因此它是明确的原首一 y 六次关系。这里不声称整个 W 已空。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 原域、三条二次式与完整头因子

A 为完整 J19 排除定理所列当前 W 权参数局部环，再倒置已排除的 J19；不扩大此前权结论的原域。沿用

$$u=e+1,\quad Q=ek,\quad V=uk+2,\quad
\ell=u((k+2)^2-2ek)/(kV),\quad d=1-Q,$$

$$bc=\tfrac14(\ell^2-(u-\ell)^2/d),\quad
T_0=2u-\ell Q-2u^2,\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3.$$

完整原六式记为

$$E_1,\ E_{B,e},\ E_{B,o},\ N_1,\ N_s,\ P_s\in A[x,y,t]. \tag{1}$$

前四条为二次，后两条为三次；原 E0/N0/P1 恢复与 weighted N/P 来源均由同一 Gram 重新生成并实际核验。

取 G=(E1,EBe,N1)^t，按 x²,xt,t² 取其系数矩阵 H。因为 G 总次数不超过二，这些系数只含权参数。源码从完整原有限式提取 H，而不是输入猜测的齐次模型。实际核两条完整 determinant 身份：

$$\det H=\frac{4\ell bc}{P_{02}}
\{(1-2\ell)Z-\ell T_0^2\},$$

$$Z=4bcQ(Q+2e)+T_0(Q+2e+\ell Q),$$

$$\det H=
-\frac{4\ell bc\,e^4u(k+2)}{kV^3dP_{02}}J_{19}. \tag{2}$$

(2) 中全部非 J19 因子此前已付，J19 已由整个 588 次有限覆盖的原返回支付。此处没有 y−1、物理 D、D27 或 B239 分母。

用真实余子式定义 H逆，并将左右两次完整 3×3 乘积的全部九项各自乘回单位矩阵。设

$$
\begin{pmatrix}q_{xx}\\q_{xt}\\q_{tt}\end{pmatrix}
=H^{-1}G
=\begin{pmatrix}
x^2-a_0(y)-a_1(y)x-a_2(y)t\\
xt-b_0(y)-b_1(y)x-b_2(y)t\\
t^2-c_0(y)-c_1(y)x-c_2(y)t
\end{pmatrix}. \tag{3}
$$

所有系数均属 A[y]。实际

$$\deg_y(a_0,b_0,c_0)\le2,\qquad
\deg_y(a_1,a_2,b_1,b_2,c_1,c_2)\le1. \tag{4}$$

每条 (3) 的完整原组合都实际乘回。因 H 可逆，三个 q 与原三个 G 生成同一理想。

## 2. 三生成证明与真乘法

对任一含 x,t 的单项式，若 x,t 总次数至少二，则含 x²、xt、t² 中之一。用 (3) 代换后，每一项的 x,t 总次数严格下降。因此有限步后得到 A[y] 线性组合 1,x,t。它证明原商在 A[y] 上由这三个元素生成，不要求它们线性独立。

对实际值列

$$v=(1,x,t)^t$$

有真乘法关系

$$M_xv=xv,\qquad M_tv=tv,$$

其中

$$
M_x=\begin{pmatrix}0&1&0\\a_0&a_1&a_2\\b_0&b_1&b_2\end{pmatrix},
\qquad
M_t=\begin{pmatrix}0&0&1\\b_0&b_1&b_2\\c_0&c_1&c_2\end{pmatrix}. \tag{5}
$$

源码对六个乘积逐项记录并返回原三个 G 的组合。没有把最终原商当作自由模，也没有直接把交换子的各个矩阵系数设为零。

令

$$S_1=tq_{xx}-xq_{xt},\qquad
S_2=tq_{xt}-xq_{tt}. \tag{6}$$

它们原本就是 G 的明确组合。按 (3) 逐步约化，余式记为 O1、O2；减去的每步组合也保存，所以 O1、O2 仍为原 G 的真实组合。实际核得

$$[M_x,M_t]_{0,*}=0,\qquad
[M_x,M_t]_{1,*}=-\operatorname{row}(O_1),\quad
[M_x,M_t]_{2,*}=-\operatorname{row}(O_2).$$

该等式作用于真实非零列 v，给出两个必要行。

## 3. 七个原行与全部同点 N/P 返回

令

$$L=(u-\ell)E_{B,e}+\ell d E_{B,o}. \tag{7}$$

完整原 L 本身对 x,t 至多一次。源码实际核这一点，而非只使用它的头。另按 (3) 约化 xL、tL、原 Ns、原 Ps。由完整线性原组合，有

$$\ell d\,\operatorname{NF}(E_{B,o})=L. \tag{8}$$

因此原 EBo 没有被遗漏。最终三列行依次为

$$L,\quad \operatorname{NF}(xL),\quad \operatorname{NF}(tL),
\quad O_1,\quad O_2,\quad \operatorname{NF}(N_s),\quad
\operatorname{NF}(P_s). \tag{9}$$

每行清分母后只剥此前已付权因子。源码实际核归一化比例及其逆均在 A，并将最终行作为原六式 (1) 的完整组合乘回。

| 原行 | 三个系数的 y 次数 | 原归一化行项数 |
|---|---|---:|
| L | 2,1,1 | 123 |
| NF(xL) | 3,2,2 | 1669 |
| NF(tL) | 3,2,2 | 1992 |
| O1 | 3,2,2 | 3689 |
| O2 | 3,2,2 | 4680 |
| NF(Ns) | 3,2,2 | 7148 |
| NF(Ps) | 3,2,2 | 7128 |

这些行同时作用于同一个 v。重叠行、xL、tL 是原理想中的额外后果，并非替换掉原 G 或其它必要式。完整原值 HA/HB、个别 N/P 仍由总原系统保留。

## 4. 三个实际常数 cofactor

取下列三组三行矩阵，列均为 1,x,t：

$$\mathcal M_0=(L,\operatorname{NF}(xL),\operatorname{NF}(tL)),$$

$$\mathcal M_1=(L,O_1,O_2),\qquad
\mathcal M_2=(L,\operatorname{NF}(N_s),\operatorname{NF}(P_s)). \tag{10}$$

若 Cij 是任一矩阵，按常数列的真实余子式 cof_i，有

$$\sum_i\operatorname{cof}_i C_{ij}
=\begin{cases}\det C,&j=0,\\0,&j=1,2.\end{cases} \tag{11}$$

(11) 的三个列乘积与完整六原式组合均实际核验。只清已付分母和内容后，得到必要参数–y 多项式 F0、F1、F2。

| 必要式 | e,k,y 次数 | 项数 | 精确系数 JSON SHA256 |
|---|---:|---:|---|
| F0 | 15,20,6 | 1411 | b501d1e8c51849dae344511c0d5f5947e030fac3baab645fb7ed793bec9b48b6 |
| F1 | 32,40,6 | 6108 | 548069452dfb806894a1d6935d0bfb6f8e0ca89a7ec6ab3b60b8a49a82f35a48 |
| F2 | 38,47,6 | 8799 | d156e7ff626ce3f698ac66eb0f7f1f0002494c24f3b324cac5789e20cb23c459 |

y 次数上界六直接来自 (9)：常数列度至多三，其余列至多二；第一行分别至多二、一、一，任一 determinant 项次数至多六。实际三式均达到六。

全部参数–y 系数由公开自含源准确再生。只保存源与小回执，没有把四十余 KB 至三十余万字节的可重算系数另存为缓存。

## 5. 最小 F0 的完整首项已付

记 a_i=[y^6]Fi。对 a0 的实际有序 gcd 剥除，非平凡循环为

$$k:1,\quad d:1,\quad (k+4):1,\quad
\operatorname{num}(bc):3,\quad
\operatorname{num}(\ell-u):1,\quad C_9:1.$$

这里 (k+4) 是源码名为 Phi 的已付原因子。数字表示源码 gcd 循环次数，不将整个 bc 分子擅自解释为三次幂。设这些逐次实际 gcd 的乘积为 Pi0；每次 exact division 和最终全部乘积均已核验。实际完整余项为常数 −1024，故

$$a_0=-1024\Pi_0\in A^\times. \tag{12}$$

于是

$$p_y(y)=F_0(y)/a_0=y^6+\sum_{j<6}\alpha_j y^j \tag{13}$$

是当前全 W 图中的明确首一原式。它是 (11) 的同一实际原组合除以已付权单位，不靠有限点采样，也没有新头零纤维。

F1、F2 的首项剥已付部分后仍分别剩 353 项、双次数 (19,25) 以及 607 项、双次数 (25,32) 的未付多项式。它们没有被倒置。后续可以无新除法地取

$$\widetilde F_i=a_0F_i-a_iF_0,\qquad i=1,2, \tag{14}$$

使 y 次数不超过五；或在首一 (13) 上作余式。这个正向原组合恒等式不要求 a_i 非零。所有未付首项零面均继续存在，不能从多变量 gcd 为 1 声称不存在原点。

(3) 与 (13) 给出一个可直接操作的 A 模生成集：

$$y^j,\quad xy^j,\quad ty^j,\qquad 0\le j<6.$$

这里仅宣这十八个元素生成原商；它们不被宣称自由，也不替代以前已证的更强六生成存在结论。实际优势是全部新三列行和首一六次式已有完整固定原组合。

## 6. 唯一真实执行与范围

自含源：

notes/2026-11-27-unit211-generic-LS-W-J19-paid-Ay-three-generator-original-input-8542.py

Git blob 3fbc5c913a2f0c2d9592460108bc072e691dde89，
20523 字节，
SHA256 2698af5ab3d98e52291d68b9f707edf5f0bf82eaf7f13712d3e1a94b70f7cb3d。

唯一实际 Actions run45999541495/job140507366761；180 秒、4 GiB。
源 16.949003673 秒，驱动 17.043971757 秒，
RSS 183288 KiB，内层退出码 0。
stdout 16399 字节，SHA256：

4f0b8f394c24e2735c2d15169b50ea538a1ff241d3231b7bb231d93d8eca3311。

实际 pull 2026-11-27 12:33:03.259426 UTC，前后均为
a66e9299ad72ebe87aef17b3683a619518618f52。
根 README blob 282e86b03385d3b6245ce7100ae2e2af7b103c2d，
课题 README blob 5fbd905291dd044c88d35bd9c07ac0e586ff795a，
两者均无变化。

源码实际完成三条头规则、六个真乘法、七条三列行、全部原 EBo/Ns/Ps 返回和三组原 cofactor。没有将 workflow 成功代替内层检查；内层记录已经完整收取。

这是全余 W 的新低次原输入与实际首一关系。剩余有限原点仍须继续返回，普通 ISP 的完成状态没有改变。
