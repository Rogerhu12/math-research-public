# 原双图第一连接的四维界、无穷远精确像与公共 K70 / 条件来源 8702

日期：2026-11-15。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿证明原自然无穷远第一连接在特征零的秩准确为 $4$，并给出其完整七维横向余空间中的精确像；有限零点的第一连接秩至多 $4$。因此全部原最大子式在两端均至少消失 $24$ 阶，已付有限公共因子升为 $K_{70}$，原九目标的条件来源成本降为 $8702$。

证明从原十七式及全部 $6188$ 个来源出发，把连接上界化为一个 $42\times7$ 有理矩阵的秩。实际两个图合计仅用 $0.395984889$ 秒精确计算；不使用尚待恢复的七个所选有理核，也不把切向关系的自由提升当成已知。

## 1. 原参数、完整来源与真实余空间

在有限图取 $t=s$、$y(t)=(1,t,\ldots,t^5)^{\mathsf T}$；在无穷远取真正的自然参数 $t=u=1/s$、$y(u)=(u^5,u^4,u^3,u^2,u,1)^{\mathsf T}$。无穷远方程始终是原成本齐次化给出的物理十七式，并非有限参数的数值替代。

原每条方程乘以全部次数至多三的十一变量单项式，给

$$
A(t):\mathbb Q[[t]]^{6188}\longrightarrow\mathbb Q[[t]]^{4367},
\qquad A(t)=A_0+tA_1+\cdots.
\tag{1.1}
$$

这里来源为列，目标是原次数一至五的全部单项式。完整第一连接是

$$
\beta:\ker A_0\longrightarrow\operatorname{coker}A_0,
\qquad v\longmapsto[A_1v].
\tag{1.2}
$$

[原零点完整临界证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)及
[原无穷远完整临界证明](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md)
都已在特征零证明 $\operatorname{rank}A_0=4340$。原函数域完整秩为 $4354$。这些等号不由模 $31$ 的秩上推。

在每个图，先把切向平面记为 $c,d$，其余九个坐标为 $z_2,\ldots,z_{10}$。原目标空间分成

$$
T=T_{\rm tan}\oplus T_1\oplus T_{\ge2},
\qquad
\dim T_{\rm tan}=20,\quad\dim T_1=135,\quad\dim T_{\ge2}=4212.
\tag{1.3}
$$

三个空间分别含零、恰好一、至少两个横向变量。旧完整秩证明还给出 $T_{\ge2}\subset\operatorname{im}A_0$，原 $T_1$ 投影秩为 $128$，而像的纯切向投影为零。因此

$$
\operatorname{coker}A_0
\simeq T_{\rm tan}\oplus\bigl(T_1/\pi_1\operatorname{im}A_0\bigr),
\qquad \dim\operatorname{coker}A_0=20+7.
\tag{1.4}
$$

## 2. 在同一自然参数中固定切向平面

有限图作完整线性矩变换

$$
m_j(t)=\sum_{k=0}^j\binom jk t^{j-k}n_k,
\qquad
m_j=n_j+t\,j n_{j-1}+O(t^2).
\tag{2.1}
$$

其常项是恒等，故在每个齐次次数上都是可逆的解析基变换，保留来源次数至多三及目标次数至多五。无穷远先作物理反序 $m_j\leftrightarrow m_{10-j}$、$K_{ij}\leftrightarrow K_{5-i,5-j}$，再使用 (2.1)。反序同时保全部十一条二阶极化系数与六条均值梯度，只作它们的真实坐标置换。

在新坐标中取 $c=n_0,d=n_1$，其余为零，便得到原真实切向图

$$
m_j(t;c,d)=c t^j+d j t^{j-1},
\tag{2.2}
$$

即

$$
M=c\,yy^{\mathsf T}
+d(yy'^{\mathsf T}+y'y^{\mathsf T}).
$$

[无穷远二阶切向证明](R150-appendix-infinity-first-connection-seven-dimensional-bound-and-common-order-twentyone.md)
与[有限零点二阶切向证明](R150-appendix-zero-second-order-tangent-family-common-factor67-and-source-cost8705.md)
已逐式证明全部原方程在 (2.2) 上可被 $t^2$ 整除。具体为

$$
\Gamma=0,\qquad N=4d^2(y'^{\mathsf T}Ky')yy^{\mathsf T},
$$

$$
y'^{\mathsf T}Ky'
=
\begin{cases}
-2t^2(t-2)(t+6),&s=0,\\
-2t^2(1-2t)(1+6t),&s=\infty.
\end{cases}
\tag{2.3}
$$

故变换后的全部十七式满足

$$
F_i(t,c,d,0)=O(t^2).
\tag{2.4}
$$

特别 $F_{i,0}$ 与 $F_{i,1}$ 的每一项都至少含一个横向变量。这是以下小化成立的原因。

若完整解析来源和目标基变换将 $A$ 换成 $\widetilde A(t)=U(t)A(t)V(t)$，则在 $\ker\widetilde A_0$ 上，一次项中的 $U'(0)A_0$ 为零，$A_0V'(0)$ 落在原常数像。因此 (1.2) 只经 $U(0),V(0)$ 的可逆变换而改变基，秩不变。(2.1) 没有改变自然参数，也没有改变完整连接。

## 3. 原 $170\times135$ 两阶矩阵

计算从下面的原 $K$ 开始，不从约化的模 $31$ 系数开始：

$$
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
\tag{3.0}
$$

令 $k(z,w)=v(z)^{\mathsf T}Kv(w)$，$J_2,J_3$ 分别为 $k^2,k^3$ 的系数矩阵，$p=Ky$，$B_p$ 为乘以 $p^{\mathsf T}v(z)$ 的矩阵。使用原真实公式

$$
\mathcal L_y(M)=J_3^{-1}B_pJ_2M,\qquad
N=4MKM+6(\mathcal L_y(M))_p,
$$

$$
\Gamma=2\operatorname{tr}((KM)^2)y+8MKMp
-12\mathcal L_y(M):(KMK).
$$

$F_0,\ldots,F_{10}$ 是 $v(z)^{\mathsf T}KNKv(z)$ 的全部十一项系数，$F_{11},\ldots,F_{16}$ 是 $\Gamma$ 的六个坐标。每张图直接保留上述公式的常数与一次参数项，完整验证 $J_3^{-1}J_3=I$；没有丢掉高方程的逆或任何均值梯度。原 primitive 整数行与这些物理行之间的非零常数比例只改变来源基，不改变连接秩。

原 $F_i$ 对十一矩变量至多二次，因而恰好一个横向变量的部分可写成

$$
\pi_1F_i(t)
=\sum_{j=2}^{10}
\left(a_{ij}(t)+b_{ij}(t)c+e_{ij}(t)d\right)z_j.
\tag{3.1}
$$

按以下固定次序构造 $P(t)=P_0+tP_1+O(t^2)$：

- 行为 $(i,a,b)$，先 $i=0,\ldots,16$，再 $a+b=0,\ldots,3$，同次数内 $a=0,\ldots,a+b$；该行是 $c^a d^b F_i$ 的一次横向部分。
- 列为 $(a,b,j)$，先 $a+b=0,\ldots,4$，再 $a=0,\ldots,a+b$，最后 $j=2,\ldots,10$；该列对应 $c^a d^b z_j$。

因此 $P_0,P_1$ 的尺寸都是 $170\times135$。旧常数秩是

$$
\operatorname{rank}P_0=128.
\tag{3.2}
$$

取完整右核基及完整左核基

$$
Q:\mathbb Q^7\longrightarrow\mathbb Q^{135},
\qquad P_0Q=0,
$$

$$
U:\mathbb Q^{42}\longrightarrow\mathbb Q^{170},
\qquad P_0^{\mathsf T}U=0.
\tag{3.3}
$$

这里 $Q$ 是余空间的对偶坐标，并非原来源核；$U$ 只参数化小投影的切向来源关系，尚不声明它们全部可提升为完整来源关系。

任取原 $v\in\ker A_0$，把其十七个来源多项式记为 $a_i(c,d,z)$，并令 $a\in\mathbb Q^{170}$ 收集全部 $a_i(c,d,0)$。来源中任何含横向变量的项乘 $F_{i,0}$ 后都至少含两个横向变量，故

$$
a^{\mathsf T}P_0=0,\qquad a=U\xi
\tag{3.4}
$$

对某个 $\xi\in\mathbb Q^{42}$ 成立。同理，由 (2.4)，这些横向来源乘 $F_{i,1}$ 后也至少含两个横向变量。纯切向目标的一阶项严格为零。因此原完整连接在 (1.4) 的七维部分准确等于

$$
a^{\mathsf T}P_1Q=\xi^{\mathsf T}U^{\mathsf T}P_1Q.
\tag{3.5}
$$

定义

$$
C_{\rm tr}=U^{\mathsf T}P_1Q\in\mathbb Q^{42\times7}.
$$

便有无需任何来源提升假设的完整上界

$$
\boxed{\operatorname{rank}\beta\le\operatorname{rank}C_{\rm tr}.}
\tag{3.6}
$$

不能从 (3.6) 反推相等：完整来源的 $a$ 可能只是 $\ker P_0^{\mathsf T}$ 的真子空间。

因为 $\ker U^{\mathsf T}=\operatorname{im}P_0$，还有独立的原行列秩检验

$$
\boxed{
\operatorname{rank}C_{\rm tr}
=\operatorname{rank}[P_0,\ P_1Q]-128.}
\tag{3.7}
$$

右端仅为 $170\times142$ 矩阵的秩差。这里拼接的是列，不是把 $P_0^{\mathsf T}$ 与 $P_1Q$ 混接。

## 4. 每个小核方向都是完整原目标的真左零 jet

设 $v\in\ker C_{\rm tr}$。由 (3.7)，存在 $w\in\mathbb Q^{135}$ 使

$$
P_1Qv=P_0w.
\tag{4.1}
$$

算法选定 $P_0$ 的真实可逆 $128\times128$ 子块求 $w$，随后检查 (4.1) 的全部 $170$ 行，而非只检查该子块。

把 $q=Qv$、$w$ 当作只支持一次横向目标的泛函，则

$$
q(t)=q-tw
\tag{4.2}
$$

此处 $A(t)$ 使用第2节的共动来源和目标坐标；它在全部 $6188$ 个原来源上满足

$$
A(t)^{\mathsf T}q(t)=O(t^2).
\tag{4.3}
$$

证明如下。对于纯切向来源，常数项是 $P_0q=0$，一次项是 $P_1q-P_0w=0$。对于含横向变量的任何来源，(2.4) 使两阶输出都含至少两个横向变量，故 $q,w$ 都将其杀掉。这覆盖全部原来源，而非某个低成本子包。若返回原未共动目标坐标，把此左泛函按第2节目标基变换的转置运输，即得同一原参数下的完整左零 jet；不把共动坐标的字面数组直接当作原数组。

因此每个额外小核方向给出原完整余空间中的真实一阶左延拓。二十个纯切向泛函在相同坐标中也由 (2.4) 延拓为常数左零 jet。此构造解释了 (3.6) 的完整来源范围，并给出可逐项重建的有理证书。

## 5. 实际精确计算

使用[原十七式横向一阶连接源码](../notes/2026-11-15-r150-original-transverse-first-connection-789f.py)，参数为：

~~~text
--chart both --remaining-seconds 30
~~~

实际运行 43679903558、步骤 original-transverse-first-connection，执行源码提交为 014c5f3e5e1d5b5631cdf06b65c92401504228f5；python-flint 版本为 0.9.0。共同数学时限为 $30$ 秒，地址空间上限为 $512$ MiB。两个图合计实际数学用时 $0.395984889$ 秒，退出码 $0$。

| 原自然图 | $\operatorname{rank}P_0$ | $\operatorname{rank}[P_0,P_1Q]$ | $\operatorname{rank}C_{\rm tr}$ |
|---|---:|---:|---:|
| $s=0$ | 128 | 132 | 4 |
| $u=1/s=0$ | 128 | 132 | 4 |

全部 $170$ 条 (4.1)、$P_0Q=0$ 及完整左核身份均精确通过。两个小连接的非零四阶子式都可取零起算的行 $26,27,29,30$、列 $2,3,4,5$；完整有理行列式保存在小回执。这个小子式只证明横向上界矩阵本身的秩，不单独充当完整来源连接的下界。

两图的 $Q$ 均按 RREF 的自由列规范化，自由单项式准确为

$$
z_{10},\quad c z_{10},\quad
c^4z_6,\quad c^4z_7,\quad c^4z_8,\quad c^4z_9,\quad c^4z_{10}.
\tag{5.1}
$$

记对应七个坐标为 $0,\ldots,6$。两个小连接的右核均由 $e_0,e_1$ 及下面一个完整整数向量生成：

$$
v_0=
\begin{pmatrix}
0\\0\\
10630086829511281838106493\\
48357113412545389993943825\\
222852952946198070799929685\\
1049059558146606146418271913\\
4919271757811109694184477005
\end{pmatrix},
\tag{5.2}
$$

$$
v_\infty=
\begin{pmatrix}
0\\0\\
-152993291260222148\\
71099127243018023\\
-33106989296892398\\
7778897332808648\\
17549194631275102
\end{pmatrix}.
\tag{5.3}
$$

这里无穷远使用第 2 节的反序后坐标，因此 (5.1) 不能与旧未反序的 $P_\infty$ 自由单项式直接混用。由第 4 节，每个向量均对应完整原目标的真实一阶左零延拓。三者独立，直接给两个原完整连接的四维上界。

为钉住确定性输入与真实校正，主要矩阵 SHA256 为：

| 图 | 矩阵 | SHA256 |
|---|---|---|
| 零点 | $P_0$ | e668cfd50415292eaf88d390acc2ce34d4e35b8e773fb3e70ea84c0bc706c01f |
| 零点 | $P_1$ | ada475352f5bac004290df1170398188720126005198248217d68735e61b5043 |
| 零点 | $Q$ | 91e6c6d98c6252147db4c38c4953e3e355d3cb1f7a613c26e63cf97b34f5f291 |
| 零点 | 全 $170$ 行校正 | 5932b298254913256b474632c2a78c62c76937cce9e4af37c743be6c46acc8c2 |
| 无穷远 | $P_0$ | 09409c30bee7364d9b8596741cc7dfcbe0695dff48fdd65724cf0928dc358abd |
| 无穷远 | $P_1$ | ab984e0fc479c31d052ef8c4675f7b6f91a429f2916158007c9f69d0e76bf0de |
| 无穷远 | $Q$ | a5b10c1264632cd70b12906ff21f9e80744afa8ab0925f970cc71b01efbd093e |
| 无穷远 | 全 $170$ 行校正 | 0f0f64e9e36b6cc5502878966afae43b4e19806d72d351e9e2d9e019b00e0804 |

实际源码 SHA256 为 2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186。原临时小回执为 $33578$ 字节，SHA256 为 f4926b42b03985728f684d6430d2d9c3a0dd1a03010bee0496a5a7a4e5670dbe。[已保存的小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-original-transverse-first-connection.json)含全部上述参数、两图核坐标、RREF、非零小子式与真实校正标志。可重算矩阵只在当前作业内临时构造，没有保存大证书。

## 6. 已付有限域结果给无穷远的特征零下界

[原无穷远一阶连接证书](R150-appendix-original-infinity-jet-and-mod31-determinantal-thickness.md)
已对全部 $6188$ 个原来源计算出模 $31$ 第一连接秩 $4$。其常数纤维秩为 $4340$，恰好等于原特征零常数秩。全部原方程的整数归一在模 $31$ 都是单位。

以下一般引理说明该有限域计算能给特征零连接的下界，而非只给裸导数矩阵的下界。令 $R=\mathbb Z_{(31)}$，$A_0,A_1$ 定义在 $R$ 上，且 $A_0$ 在 $\mathbb Q$ 与 $\mathbb F_{31}$ 上的秩都为 $r$。选取一个 $r\times r$ 的 $31$ 单位子块，并对 $A_0$ 作完整 $R$ 上的单位消元。所有其余 Schur 元素在 $\mathbb Q$ 中为零，所以也在 $R$ 中为零。于是来源核与目标余空间有 $R$ 上的自由基，其约化分别是完整有限域核和余空间。第一连接在这些基中由同一个 $R$ 矩阵给出。因此

$$
\operatorname{rank}_{\mathbb Q}\beta
\ge\operatorname{rank}_{\mathbb F_{31}}\beta_{31}=4.
\tag{6.1}
$$

这里使用的是常数秩在两个特征中相等；没有从有限域 Smith 高阶直接上推特征零高阶。旧四个非零连接主元对应原来源 $3398,6154,6168,6171$，主系数分别为 $3,25,25,7$。完整来源同步消元的旧源码及小回执由上述正式证明给出，不在本稿重复计算。

结合第 5 节的上界，得到

$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_\infty=4,\qquad
\operatorname{rank}_{\mathbb Q}\beta_0\le4.}
\tag{6.2}
$$

在完整目标余空间的 $20+7$ 坐标中，无穷远连接像的纯切向部分为零，七维部分准确等于

$$
\boxed{
\operatorname{im}\beta_\infty
=\{(0,0,x_2,x_3,x_4,x_5,x_6):
\langle v_\infty,(0,0,x_2,x_3,x_4,x_5,x_6)\rangle=0\}.}
\tag{6.3}
$$

这里使用普通有理双线性配对；(6.3) 的七坐标按 (5.1) 的 $Q$ 定义。包含关系来自三条真实左零 jet，相等来自完整像维数已经是 $4$。有限零点只得到相应 $v_0$ 所定义四维空间的包含关系；本稿不把旧无穷远有限域下界移给有限零点。

## 7. 公共消失阶与有限来源界

设本稿第 5 节给出的有限零点上界为 $r_0$，无穷远上界为 $r_\infty$。每个图有十四个正 Smith 指数。第一连接秩准确等于其中指数恰为一的个数，故

$$
\operatorname{ord}_0(\text{任意原最大子式})\ge28-r_0,
\qquad
\operatorname{ord}_\infty(\text{任意原最大子式})\ge28-r_\infty.
\tag{7.1}
$$

这些是全部 $4354$ 阶最大子式的共同下界；它们不提供高阶指数的上界。

本次 $r_0=r_\infty=4$，故

$$
\boxed{s^{24}\mid\text{全部原最大子式},\qquad
u^{24}\mid\text{全部原自然无穷远最大子式}.}
\tag{7.2}
$$

无穷远十四个正 Smith 指数中，准确四个为一，其余十个至少为二；有限零点至多四个为一，至少十个不小于二。没有把其余指数都设为二。

旧有限因子为

$$
K_{60}(s)=s^{14}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2,
$$

$$
F_+=5s^3-25s^2+32s-8,\qquad
F_-=5s^3+135s^2+864s+864.
$$

原根集合互不相交，其余因子在 $s=0$ 非零，见
[原射影子式公共因子](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)。
因此

$$
\boxed{K_{70}(s)=s^{10}K_{60}(s)
=s^{24}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2}
\tag{7.3}
$$

整除全部原最大子式，次数为 $70$，最高系数仍为 $5^6$，是 $31$ 单位。两图共同给出的自然齐次公共下因子总次数为 $70+24=94$；这仍不是完整 gcd。

为了得到原来源成本，保持
[同选 Koszul 曲线的 $43/42/41$ 阶证明](R150-appendix-selected-koszul-curves-infinity-order43-and-source-cost8712.md)
的同一非零 $4354$ 阶子式 $D=\det A_{I,J}$、总权 $H=8770$。该来源证明给 $D$ 在无穷远至少 $43$ 阶，换入一列至少 $42$ 阶，cofactor 至少 $41$ 阶。本稿的公共无穷远 $24$ 阶不能再与指定 $43$ 阶相加。

令

$$
d_*=D/K_{70},\qquad q=\deg d_*.
$$

同一 $D$ 模 $31$ 非零，其约化可被原仿射 $315$ 次最大子式 gcd 整除，所以 $\deg D\ge315$。于是

$$
\boxed{245\le q\le8770-43-70=8657.}
\tag{7.4}
$$

对任一原来源列 $A_\ell$，

$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{70}
$$

为多项式，且完整 $4367$ 输出上的恒等式为

$$
A_JP_\ell=d_*A_\ell.
\tag{7.5}
$$

若原来源权为 $a_\ell$，原成本权为 $\delta_\ell=a_\ell-10$，则 $\max a_\ell=55$、$\max\delta_\ell=45$，且换列阶给

$$
\deg(P_\ell)_j\le H-a_j+a_\ell-42-70.
\tag{7.6}
$$

现在假设原目标 $b_\nu=h_0t_\nu$ 已属于 $\operatorname{im}_{\mathbb Q[s]}A$，其中 $\deg h_0=24$，原目标共同权 $\tau_\nu\le64$。在这个成员性前提下，

$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{70}
$$

为多项式，并由 cofactor 阶得到

$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-41-70.
\tag{7.7}
$$

用 (7.5) 将所有非基来源的参数次数降到 $<q$，保同一目标后有

$$
d_*y_j=(T_\nu)_j-\sum_{\ell\notin J}(P_\ell)_j y_\ell.
\tag{7.8}
$$

非基来源成本至多 $q-1+45\le8701$；基来源成本至多

$$
\begin{aligned}
\deg y_j+\delta_j
&\le\max\{H+\tau_\nu-41-70-10-q,\ H+55-42-70-11\}\\
&\le\max\{8770+64-41-70-10-245,\ 8770+55-42-70-11\}\\
&=\max\{8468,8702\}=8702.
\end{aligned}
$$

因此得到完整原来源的条件结论

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists y^{(\nu)}:\ Ay^{(\nu)}=h_0t_\nu,\quad
\operatorname{cost}(y^{(\nu)})\le8702.}
\tag{7.9}
$$

目标分支仍为 $8468$：有限因子新增三阶时 $q$ 的下界也减少三，不能把这一分支再次减三。$K_{70}$ 首项为 $31$ 单位，但没有由此证明 $\operatorname{lc}(D)$ 是 $31$ 单位，故仍不把无界次数的模 $31^n$ 成员性免费降为固定 $31$ 分母的来源。

## 8. 计算与数学范围

所用小脚本只重建原 $K,J_2,J_3$、十七个完整物理式的一次参数 jet，再做上述完整有理消元。它没有生成原 $4367\times6188$ 矩阵，没有使用新的七个所选有理核，也没有从小连接矩阵的非零小子式自动宣称完整来源的下界。

原目标的 $\mathbb Q[s]$ 成员性仍未由这些界完成；同选非零最大子式最高系数的 $31$ 单位性也不在本稿中。全部预算及来源界均保持这两个原边界。
