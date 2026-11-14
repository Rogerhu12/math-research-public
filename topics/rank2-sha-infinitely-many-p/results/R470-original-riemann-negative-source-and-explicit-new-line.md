# R470 — 原 Riemann 负来源到显式新谱线的完整投影及单位域运输

日期：2026-11-14。**状态：以下来源恒等式、全部 CM 纤维规范、第一输出的
单位测试运输及保第二轴四态的中央公式已证明。** 本篇把 R414 的实际
第一辅助来源投到一条明确的质量零谱线，准确系数为 $13/90$。
该谱线的椭圆曲线身份另由 R466 支付；本篇的证明不依赖预先赋予它
某条曲线的秩、中央零或 Sha 结论。原主目标尚未完成。

## 1. 固定原来源和完整结论

沿 R414 使用同一 $E_b$ 的 reduced sigma、微分和普通周期，

$$
\delta^2=-3,\quad\omega=(-1+\delta)/2,\quad
\gamma _7=(5+\delta)/2,\quad\gamma _{19}=4+\delta.
$$

记真实 trace 的规范化为

$$
N_7=\mathscr M_{\gamma _7}/\gamma _7,\qquad
N_{19}=\mathscr M_{\gamma _{19}}/\gamma _{19}.
\tag{1}
$$

这里 $\mathscr M_a$ 完全是 R300/R407 的 division-frame trace；
不另除以 $Na$，也不添一个未定的 Weil 标量。

R414 的同一二覆盖来源为

$$
F_0=S(2z)T(2w),\qquad F_2+F_3=F_0,\qquad D=F_2-F_3.
$$

其第一、第二实际辅助来源仍记为 $A\in\mathcal S_{136}$、
$B\in\mathcal S_{288}$。它们的首项均为六次项，系数一。
以 $\Pi _0$ 表示第一轴的真实 $\mu _6$ 平均，R414 给

$$
(\Pi _0\otimes I)D=\frac{7040\delta}{9}A\otimes B.
\tag{2}
$$

在完整 principal 块上使用已付的 $N_7^{18}=I$，定义

$$
\boxed{\quad
\mathcal Q=\frac{I-\omega N_{19}}{36}
                 \sum_{j=0}^{17}\omega^jN_7^j.
\quad}
\tag{3}
$$

下面显示的首项一来源 $S_{\mathrm{new}}$ 满足完整恒等式

$$
\boxed{\mathcal QA=\frac{13}{90}S_{\mathrm{new}}.}
\tag{4}
$$

于是同一个原十二 sigma 负来源严格给出

$$
\boxed{(\mathcal Q\Pi _0\otimes I)D
       =\frac{9152\delta}{81}S_{\mathrm{new}}\otimes B.}
\tag{5}
$$

这不是在抽象同型 theta 空间中另选一条向量。
左端的 $A,D,B$ 都是 R414 的原函数，且 (3) 的每一步都是 (1) 的
实际全纤维 trace。第二轴来源及其全部状态保持原样。

## 2. 新谱线、全部相位与精确证书

先取 $b=1$，令 $X=x^3$。置

$$
\begin{aligned}
R&=X^2+20X-8,\\
Q_4&=X^4+40X^3+2112X^2+3136X+1792,\\
\widetilde Q_4&=13X^4+52X^3+1536X^2+1024X+256,\\
Q_8&=X^8+1232X^7-58688X^6-49408X^5-439040X^4\\
&\hspace{15mm}-2111488X^3-1949696X^2-851968X-32768.
\end{aligned}
$$

准确的新来源是

$$
\boxed{S_{\mathrm{new}}
 =\frac1{91}\sigma^{136}x^2
 (X+1)R(7X^2-4X+16)Q_4\widetilde Q_4Q_8.}
\tag{6}
$$

sigma 后的 $X$ 多项式次数为 $21$，首系数一，故

$$
S_{\mathrm{new}}(0)=0,\qquad S_{\mathrm{new}}(z)=z^6+O(z^{12}).
\tag{7}
$$

一般 $b\ne0$ 时，将 (6) 中 $P_{21}(X)$ 换成
$b^{21}P_{21}(X/b)$。等价地，

$$
S_{\mathrm{new},b}(z)=b^{-1}S_{\mathrm{new},1}(b^{1/6}z).
\tag{8}
$$

所有幂均为 $6$ 的倍数，故 (8) 不依赖六次根的选择。
R414 的 $A_b$ 和 R466 的两个 $W_{2,b}$ 有相同的缩放规则；
因此 (4) 的 $13/90$ 在原 $b=17$ 规范中不变。

### 2.1 完整而非投影的算子规范

真实 CM7 矩阵在完整 principal 基

$$
\mathcal E_j=\sigma^{136}x^2X^j,\qquad 0\le j\le22
\tag{9}
$$

上由二十三个完整七纤维求得；所用首项常数是
$r_{\gamma _7}=\gamma _7(X-r)$、$r=(2-6\delta)/7$。
CM19 在完整的 $N_7^3=1$ 五维子空间上由五个完整十九纤维求得。
两种计算均使用特征零商环及全部根的 trace，未以几个 Taylor 项或
几个目标素数的数值判断本征性。

在模 $272$ 的完整 theta 中心中，准确有

$$
g_7=(40,195),\quad g_{19}=(87,144),\quad
g_{19}=33(-\omega)g_7^2.
\tag{10}
$$

这里数对表示 $a+b\omega$。$33\equiv1\pmod{16}$、
$33\equiv-1\pmod{17}$，对应的实际对称 lift 记为 $D_{33}$。
在 Schrödinger 基中它是 $e_j\mapsto e_{33j}$，不是丢掉中心后的
任意置换。在 principal 块上，实际 $S(2z)$ 锚固定绝对相位为

$$
N_{19}=\omega D_{33}N_7^2.
\tag{11}
$$

证书也直接用完整五维 CM19 矩阵检验

$$
D_{33}=\omega^{-1}N_{19}N_7,\qquad D_{33}^2=I
\quad\text{在 }N_7^3=1\text{ 上}.
\tag{12}
$$

因而本篇的 $D_{33}$ 符号不依赖裸 Weil 模型的相位选择。
在整个 principal 块上，$\frac1{18}\sum_{j=0}^{17}\omega^jN_7^j$
是 $N_7=\omega^2$ 投影；在 $N_7^9=1$ 上才可缩成
$\frac19\sum_{j=0}^{8}\omega^jN_7^j$。在其像上，(11) 给
$D_{33}=\omega N_{19}$。所以 (3) 准确是

$$
\mathcal Q=\frac{I-D_{33}}2\,P_{N_7=\omega^2}.
\tag{13}
$$

它不是只由一个普通素数处的 core 负号猜出的谱投影。

### 2.2 全部二十三坐标的等式

R414(19) 给原 $A$ 的完整式

$$
A=\frac1{70}\sigma^{136}x^2
 (X+1)^2(X-8)^2R P_4P_8L,
\tag{14}
$$

其中

$$
\begin{aligned}
P_4&=X(X-8)^3-512(X+1)^3,\\
P_8&=7X^2(X-8)^6-256X(X-8)^3(X+1)^3+65536(X+1)^6,\\
L&=10X^3-24X^2+192X+64.
\end{aligned}
$$

旁列脚本将 (14)、(6) 放入同一个基 (9)，逐坐标检验 (4)。
它还完整检验

$$
N_7^9A=A,\qquad N_7S_{\mathrm{new}}=\omega^2S_{\mathrm{new}},
\quad N_{19}S_{\mathrm{new}}=-\omega^2S_{\mathrm{new}},
\quad D_{33}S_{\mathrm{new}}=-S_{\mathrm{new}}.
\tag{15}
$$

与 R466 的两个固定倍点 division-log 来源 $W_{13},W_{15}$ 比较，
完全相同的多项式还满足

$$
S_{\mathrm{new}}=-\frac5{3848}
       \frac{I+N_7^3+N_7^6}{3}(101W_{13}-64W_{15}).
\tag{16}
$$

本篇因而把 R466 的显式谱线接到 R414 的实际负来源，不仅说明
两者属于同一个 theta 块。

为准确保留被投影掉的部分，证书输出 $A-\frac{13}{90}S_{\mathrm{new}}$
的全部二十三坐标。还得到完整秩：

| 实际空间 | $K$ 上的维数 |
|---|---:|
| 完整 $N_7^9=1$ principal 块 | 17 |
| 两个 $W_i,N_7W_i,\ldots,N_7^8W_i$ 的共同张成 | 16 |
| 上一行再加入原 $A$ | 17 |
| $A,N_7A,\ldots,N_7^8A$ | 9 |

特别地，不能把原 $A$ 全部改写成两条 $W_i$ 的 CM7 轨道。
缺维出现在 $N_7=1$ 的二维空间。以下是 $A$ 的全部正三次根
分量的原点质量；它们也表明“质量零”不能从一个投影传播给余部：

| $N_7$ 特征 | $D_{33}=+1$ 的质量 | $D_{33}=-1$ 的质量 |
|---|---:|---:|
| $1$ | $-1/72576$ | $-1/120960$ |
| $\omega$ | $-1/181440$ | $0$，该分量恒零 |
| $\omega^2$ | $-1/181440$ | $0$，分量为 $13S_{\mathrm{new}}/90$ |

表中采用 $b=1$；一般 $b$ 时各质量再乘 $b^{-1}$。
另十二维的全部坐标保留在完整余来源中，未被认作零或原曲线来源。

## 3. 每个实际 CM 纤维及第一输出的单位条件

本节说明 (3) 怎样作用于同一个实际来源和测试，避免从纯代数投影
偷换出原中央零的传播。

令 $F(z,w)\in\mathcal S_N\otimes\mathcal S_{N'}$，$N$ 偶，
$a$ 是本篇出现的奇范数 CM 整数。对每个
$v\in a^{-1}\Lambda/\Lambda=E[a]$，定义带原对称相位的完整支

$$
\begin{aligned}
G_{a,v}(z,w)
&=(\mathsf T^{(N)}_{\bar av}F)(\bar az,w)\\
&=\exp\!\left[-N(Na)\eta_v(z+v/2)\right]
                 F\bigl(\bar a(z+v),w\bigr).
\end{aligned}
\tag{17}
$$

(17) 中的指数是完整 theta lift 的一部分，不能把它删掉后再积分。
它可等价地由 R300 的代数 division frame 读取，无须在 $p$-adic
正式盘中把非零挠点的对数设为零。

**逐支恒等式。** 对同一规范化 $N_a=\mathscr M_a/a$，有

$$
\boxed{(N_a^{(1)}F)(az,w)=\frac1a\sum_{v\in E[a]}G_{a,v}(z,w).}
\tag{18}
$$

证明：在 R300 的完整 trace 中令目标为 $az$，则全部原像为
$z+v$。原 division 比给

$$
\left[\frac{\sigma(az)}{\sigma(az+av)}\right]^N
                  F\bigl(\bar a(z+v),w\bigr).
$$

使用 $av\in\Lambda$、$\eta_{av}=\bar a\eta_v$，且 $N$ 偶，
这恰是 (17)，包括常数半相位。再保留 $N_a$ 的 $1/a$ 即得 (18)。
对 $z$ 加周期也可直接检查
$G_{a,v}\in\mathcal S_{NNa}\otimes\mathcal S_{N'}$：
附加因子为 $\exp(NNa(\eta_\ell v-\eta_v\ell))=1$，因为
$(Na)v\in\Lambda$。故每支都是一个真实有限覆盖上的 theta 来源。
在包含固定挠点 theta 常数的有限系数域中，它们各有有界 Amice 测度；
完整投影来源的整性则由 (4)、(6) 直接给出。

当前所有普通 $p>19$ 均与 $a$ 互素。取同一个普通周期，(18) 的
测度形式准确为

$$
\boxed{\nu_{N_a^{(1)}F}
 =\frac1a[a^{-1},1]_*\sum_{v\in E[a]}\nu_{G_{a,v}}.}
\tag{19}
$$

因此对任意真正的两输出测试 $\varphi(Y,W)$，右端必须测试
$\varphi(a^{-1}Y,W)$。特别地，第一输出的条件 $Y\in\mathbf Z_p^\times$
在每支仍然是完整的 $Y\in\mathbf Z_p^\times$，因为 $a$ 是普通单位；
第二输出不变。逐个输出环带也保留。令

$$
J_F(u,v)=\int_{Y,W\in\mathbf Z_p^\times}
              \langle Y\rangle^{du}\langle W\rangle^{dv}\,d\nu_F,
\qquad d=p-1.
$$

于是严格有

$$
J_{N_a^{(1)}F}(u,v)
 =\frac{\langle a\rangle^{-du}}a
                  \sum_{t\in E[a]}J_{G_{a,t}}(u,v).
\tag{20}
$$

例如一阶中央必保

$$
\partial_uJ_{N_a^{(1)}F}(0,v)
 =\frac1a\sum_t\left[
 \partial_uJ_{G_{a,t}}(0,v)-d\log_p\langle a\rangle J_{G_{a,t}}(0,v)
 \right].
\tag{21}
$$

本篇没有把最后的质量项逐支设为零。

对本篇的全部复合，

$$
a_{j,\epsilon}=\gamma _7^j\gamma _{19}^{\epsilon},
\quad0\le j\le17,\quad\epsilon=0,1,
$$

所选素因子与其共轭互素。原双纤维的中间 sigma 比准确相消，给
$N_{19}^{\epsilon}N_7^j=N_{a_{j,\epsilon}}$。具体地，
$aP=z,cQ=\bar aP$ 可唯一写为 $P=ct,Q=\bar at,act=z$，
因为 $(c,\bar a)=1$；这也保留了全部中心相位。因此 (3) 的完整
第一单位行就是以下有限真实支和：

$$
\boxed{J_{\mathcal Q^{(1)}F}(u,v)
 =\frac1{36}\sum_{j=0}^{17}\sum_{\epsilon=0}^{1}
  \omega^j(-\omega)^{\epsilon}
  \frac{\langle a_{j,\epsilon}\rangle^{-du}}{a_{j,\epsilon}}
  \sum_{t\in E[a_{j,\epsilon}]}J_{G_{a_{j,\epsilon},t}}(u,v).}
\tag{22}
$$

这里保留每个新的 CM 纤维、每个规范化 $1/a$ 和每个尺度质量。
若原来源附加隐藏 sigma 输入条件，必须沿 (17) 的整支共同运输；
(22) 没有许可把那些条件改成 $A$ 或 $S_{\mathrm{new}}$ 的一个边际条件。

## 4. 同一个 Riemann 关系的两个实际投影项

原 $S(2z)$ 满足 $N_7=-1$，故 (3) 中的 $N_7=\omega^2$ 投影
杀掉它。由 (2)、(4) 及 $F_2+F_3=F_0$，得到全函数身份

$$
\boxed{(\mathcal Q\Pi _0\otimes I)F_2
       =\frac{4576\delta}{81}S_{\mathrm{new}}\otimes B,
\qquad
(\mathcal Q\Pi _0\otimes I)F_3
       =-\frac{4576\delta}{81}S_{\mathrm{new}}\otimes B.}
\tag{23}
$$

真实角平均与全部 CM trace 交换；它在 principal 第一单位测试及
每条第一输出环带上保持测试。这说明 (23) 是原 mixed 来源的
真实投影，且其全部单位 Mellin 和两输出环带准确分离。
它没有把投影前的某个隐藏区域当成新纯张量来源的同名区域。

## 5. 同一普通 ray、第二轴四态与完整中央公式

沿当前共同 ray，

$$
\lambda=-1/\bar\pi _0,\quad
\kappa=p/\bar\pi _0^2,\quad\beta=\bar\pi _0^{-2}=\lambda^2.
$$

完整模 $272$ 数据给
$g_{\pi _0}=(203,136)=g_7^9$。原非零 $S(2z)$ 锚满足
$K_{136}S(2z)=S(2z)$、$N_7^9S(2z)=-S(2z)$，故在整个原
$136$ 维 theta 空间上

$$
K_{136}=-N_7^9.
\tag{24}
$$

由 (15) 得

$$
K_{136}S_{\mathrm{new}}=-S_{\mathrm{new}},\qquad
\nu_{S_{\mathrm{new}}}|_p=-\lambda[\kappa]_*\nu_{S_{\mathrm{new}}}.
\tag{25}
$$

结合质量零，准确有 $J_{S_{\mathrm{new}}}(0)=0$。
这一步只给质量，不给中央导数。

第二轴仍是 R414 的全部四条来源

$$
B_j=K_{288}^jB,\quad0\le j\le3,\qquad K_{288}^4B=-B.
\tag{26}
$$

以 $|q_i|_p<1$ 定义真实输出环带正则化，环带 $p^n\mathbf Z_p^\times$
测试单位部分 $p^{-n}Y$，再乘 $q_i^n$。令
$a(q;u)=q\lambda\langle\beta\rangle^{du}$。完整来源式给

$$
\mathcal R_{S_{\mathrm{new}}}(q;u)
 =\frac{J_{S_{\mathrm{new}}}(u)}{1+a(q;u)},\qquad
\mathcal R_B(q;v)
 =\frac{\sum_{j=0}^{3}a(q;v)^jJ_{B_j}(v)}{1+a(q;v)^4}.
\tag{27}
$$

(22) 也在这个初始收敛域逐环带成立；这里只对完整投影和 (27)
作解析延拓，不把未经支付的单个 CM 支分别在 $q_i=1$ 求值。
R407/R410 的单位分母使 (27) 在 $(q,u)=(1,0)$ 整解析。

设 $m_j=B_j(0)$。只有 $m_0=0,m_4=-m_0=0$ 已知，必须保留

$$
J_{B_j}(0)=m_j-\lambda m_{j+1},\qquad
\sum_{j=0}^3\lambda^jJ_{B_j}(0)=0.
\tag{28}
$$

因此定义

$$
\begin{aligned}
\mathfrak n_p&=\frac{J'_{S_{\mathrm{new}}}(0)}{1+\lambda},\\
\mathfrak b_p&=\frac1{1+\lambda^4}\sum_{j=0}^{3}\lambda^j
 \left[J'_{B_j}(0)+j\,d\log_p\langle\beta\rangle J_{B_j}(0)\right].
\end{aligned}
\tag{29}
$$

由 (5)、(23)、(27) 得到同一个真实正则化中的完整交叉中央：

$$
\boxed{
\begin{aligned}
\partial_{uv}\mathcal R_{(\mathcal Q\Pi _0\otimes I)D}(1,1;0,0)
 &=\frac{9152\delta}{81}\mathfrak n_p\mathfrak b_p,\\
\partial_{uv}\mathcal R_{(\mathcal Q\Pi _0\otimes I)F_2}(1,1;0,0)
 &=\frac{4576\delta}{81}\mathfrak n_p\mathfrak b_p,\\
\partial_{uv}\mathcal R_{(\mathcal Q\Pi _0\otimes I)F_3}(1,1;0,0)
 &=-\frac{4576\delta}{81}\mathfrak n_p\mathfrak b_p.
\end{aligned}}
\tag{30}
$$

全部尺度质量仍在 (21)、(22)、(28)、(29) 中。常数 $13/90$、
$9152\delta/81$ 在当前 $p>19$ 处均为单位。

## 6. 准确的新增接口与剩余条件

本篇支付了从原十二 sigma mixed 负来源到显式新谱线的实际固定
CM 投影；它有完整的第一单位域、全部有限纤维及第二轴四态表达。
所以在新谱线的曲线身份独立支付后，可以把相应曲线纳入原 mixed
来源的算术比较。

但原 $J'_S(0)=J'_T(0)=0$ 仍不推出 $J'_A(0)=0$，也不推出
$\mathfrak n_p\mathfrak b_p=0$。原 $F_2+F_3=F_0$ 在 (23) 下
只给一对相反数；这不是额外的零。原中央泛函经过 (3) 后变成
(22) 的完整新纤维行，不能从投影前一条中央零免费继承。
若要进一步使用原隐藏非零区域，必须支付它沿这些 CM 支和原
Riemann 坐标的完整运输以及补域关系。

## 7. 证书与依赖

- `scripts/check-r470-original-negative-source-new-line.py`：读取已经由
  全纤维重建的 CM7、CM19 矩阵，精确验证 (4)、(6)、(13)、(15)、(16)
  的全部二十三坐标，并输出完整余来源、各正谱质量及上述四个秩。
- 同名 JSON 保留全部向量；其中 `degree21_coefficient` 是基 (9)
  的系数，`Taylor_z6` 另扣除质量列贡献 $136m/15$，两者没有混淆。
- [R414：原负来源及全部辅助中央质量](R414-original-negative-principal-factorization-and-actual-auxiliary-sources.md)。
- [R407：同一二覆盖、完整中心与整正则化](R407-original-riemann-cover-finite-cores-and-integral-regularization.md)。
- `scripts/check-r464-degree102-cm7-exact.py` 的通用特征零全纤维构造，
  及其 `notes/2026-11-14-theta-degree136-cm7-exact.json` 完整二十三维矩阵。
- `scripts/check-r466-fixed-two-division-source.py/.json` 的完整十九纤维
  五维块、两个实际 $W_i$ 及谱线 (16)。椭圆曲线身份与秩另行支付。
