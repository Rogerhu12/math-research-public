# R190. 方格 theta 截面的中央投影单射与实际两层方向的存在性

日期：2026-11-12。**状态：下述旋转平均、正 Gaussian 均值和
中央投影单射由完整解析计算证明。** 它给每个固定素数处的
有限非零检验存在性；没有给其层数或行列式赋值的统一上界，
也没有把中央函数不恒为零替换成中央导数非零。

## 1. 原截面与准确结论

原 $E_0:y^2=x^3-x$ 的周期格为 $\Lambda=\Omega\mathbb Z[i]$，
$\Omega>0$。R115/R162 的两条实际截面可写成
$$
 \mathcal A(z)=\sigma(z)^{68}P_A(x_E(z)^2),\qquad
 \mathcal B(z)=\sigma(z)^{68}P_B(x_E(z)^2).
 \tag{1}
$$
它们是整函数、同一个正 theta 次数 $68$ 的截面，且对
$z\mapsto iz$ 不变。写 $w=z^4$ 后，仍用 $A(w),B(w)$ 表示
这两个固定函数，满足
$$
 A(w)=w+O(w^2),\qquad B(w)-A(w)=-22w^2+O(w^3).
 \tag{2}
$$
特别 $A,B$ 线性独立，$B/A$ 非常数。

对任意整数 $r\ge1$，定义实际中央系数投影
$$
 \mathcal C_rF(w)=\sum_{n\ge0}[w^{rn}]F(w)\,w^{rn}.
 \tag{3}
$$
本篇证明：

1. 在同一个方格上、满足 (4) 准周期的固定正 theta 次数
   $\mu_4$ 不变截面空间中，$\mathcal C_r$ 是单射。
2. 对每个 $D$，它在原实际多项式空间
   $\mathbb C[A,B]_{\le D}$ 上也是单射。
3. 对每个惰性 $p=4r-1\ge7$，R185 的同一整轴系数向量
   $(g_{rs}(A),g_{rs}(B))$ 张成 $\mathbb Q_p^2$。
   因而 R189 的实际部分和方向中，确实存在两个有限层
   $N,M$ 满足 $\det(q_N,q_M)\ne0$。

第 3 点没有断言某两个预先指定的小层有效。

## 2. 正 theta 截面的标准 Gaussian 展开

先对一个正整数 $d$ 证明解析命题。令 $F$ 是非零整函数，
具有无字符的方格 theta 准周期
$$
 \begin{aligned}
 F(z+\Omega)
 &=\exp\!\left(\frac{d\pi}{\Omega}(z+\Omega/2)\right)F(z),\\
 F(z+i\Omega)
 &=\exp\!\left(-\frac{id\pi}{\Omega}(z+i\Omega/2)\right)F(z).
 \end{aligned}
 \tag{4}
$$
本题所用的 $d=68m$ 全满足 (4)：$\sigma$ 的符号在偶数次幂
中消去，余下的椭圆函数因子周期不变。方格的 quasi-period
$\eta(\Omega)=\pi/\Omega$ 也可直接由
$\eta(i\Omega)=-i\eta(\Omega)$ 和 Legendre 关系得到。

作实尺度换元 $Z=\sqrt{d\pi}\,z/\Omega$，并置
$\ell=\sqrt{d\pi}$。在新尺度，(4) 为
$$
 F(Z+\ell)=e^{\ell Z+\ell^2/2}F(Z),\qquad
 F(Z+i\ell)=e^{-i\ell Z+\ell^2/2}F(Z).
 \tag{5}
$$
本节中 $F$ 表示已经缩放的函数。
$e^{-Z^2/2}F(Z)$ 以 $\ell$ 为实周期，其整函数 Fourier 展开
与第二条准周期给
$$
 F(Z)=e^{Z^2/2}\sum_{n\in\mathbb Z}
       a_n e^{-\pi n^2/d+2\pi i nZ/\ell},\qquad a_{n+d}=a_n.
 \tag{6}
$$
为核清周期性，若 Fourier 系数为 $b_n$，第二条式子给
$b_{n+d}=e^{-2\pi n-d\pi}b_n$，所以
$a_n=b_ne^{\pi n^2/d}$ 确实周期为 $d$。
任意紧集上的绝对正常收敛来自 Gaussian 衰减。

将变量旋转一次 $Z\mapsto iZ$、再把 $n$ 改号，得到等价的
标准形式
$$
 \boxed{\quad
 f(Z)=e^{-Z^2/2}\sum_{n\in\mathbb Z}
     a_n e^{-h^2n^2/2+\sqrt2 hnZ},
 \qquad h^2=\frac{2\pi}{d},\quad a_{n+d}=a_n.
 \quad}
 \tag{7}
$$
周期向量只作一次固定的反序。它不全为零，因为 $F\ne0$。
实缩放与这次固定旋转均与后文的所有旋转平均交换。
原 $\mu_4$ 不变函数中，这次旋转本来不改变函数。

令 $M=\max|a_n|$。配平方给
$$
 \sum_n |a_n|
 \left|e^{-Z^2/2-h^2n^2/2+\sqrt2 hnZ}\right|
 \le M e^{|Z|^2/2}
      \sum_n e^{-(hn-\sqrt2\operatorname{Re}Z)^2/2}
 \le C e^{|Z|^2/2}.
 \tag{8}
$$
最后的 Gaussian 格点和对实平移一致有界。因此所有后文的
带正 $\epsilon$ 积分和逐项双重求和都绝对收敛。

## 3. 两个旋转的准确 Gaussian 积分

对 $\epsilon>0$ 定义正内积
$$
 \langle f,g\rangle_\epsilon
 =\frac{\epsilon}{\pi}\int_{\mathbb C}
       f(Z)\overline{g(Z)}e^{-(1+\epsilon)|Z|^2}\,d^2Z.
 \tag{9}
$$
由 (8)，其值有限。置
$$
 I_\epsilon(\theta)
 =\langle f(e^{i\theta}Z),f(Z)\rangle_\epsilon,
 \qquad a=1+\epsilon,\quad D_\theta=a^2-e^{2i\theta}.
$$
对 (7) 逐项作二维 Gaussian 积分，准确得到
$$
 \boxed{\quad
 I_\epsilon(\theta)
 =\frac{\epsilon}{\sqrt{D_\theta}}
   \sum_{n,m\in\mathbb Z}a_n\overline{a_m}
    \exp\!\left(
     \frac{h^2\{2ae^{i\theta}nm
            -(a^2+e^{2i\theta})(n^2+m^2)/2\}}
          {a^2-e^{2i\theta}}
        \right).
 \quad}
 \tag{10}
$$
平方根取从 $a>1$ 的收敛 Gaussian 积分连续确定的分支。
例如该计算可直接由
$$
 \int_{\mathbb C}
 e^{-a|Z|^2+(bZ^2+c\overline Z^2)/2+uZ+v\overline Z}\,d^2Z
 =\frac{\pi}{\sqrt{a^2-bc}}
     \exp\!\left(\frac{auv+(cu^2+bv^2)/2}{a^2-bc}\right)
$$
在 $b=-e^{2i\theta},c=-1,u=\sqrt2 hn e^{i\theta},
v=\sqrt2 hm$ 的代入得到。这个积分公式由两个实变量配平方
而来；当前 $a>1$ 保证实部负定。

### 3.1. 对角项的严格正极限

当 $\theta=0$ 时，(10) 的指数准确为
$$
 -\frac{h^2}{4}\left\{
       \frac{a+1}{a-1}(n-m)^2
       +\frac{a-1}{a+1}(n+m)^2\right\}.
 \tag{11}
$$
$n\ne m$ 的总贡献，在 (10) 的前因子之后是
$O(e^{-c/\epsilon})$：先对 $n-m\ne0$ 求窄 Gaussian 和，
再对 $n+m$ 求宽度 $O(\epsilon^{-1/2})$ 的 Gaussian 和即可。
$n=m$ 的部分为
$$
 \frac{\epsilon}{\sqrt{2\epsilon+\epsilon^2}}
 \sum_n|a_n|^2
   \exp\!\left(-\frac{h^2\epsilon}{2+\epsilon}n^2\right).
$$
对周期权逐剩余类作普通 Gaussian Riemann 和，得到
$$
 \boxed{\quad
 \lim_{\epsilon\downarrow0} I_\epsilon(0)
   =\frac{\sqrt\pi}{h}\,\frac1d\sum_{j=0}^{d-1}|a_j|^2
   =:\mathcal N(f)>0.
 \quad}
 \tag{12}
$$

### 3.2. 非 Gaussian 根单位旋转的交叉项

现在固定 $\theta$，假设 $e^{i\theta}$ 是根单位且不在
$\mu_4$ 中。因此 $\sin\theta\ne0$。令 (10) 中的二次指数为
$E_\epsilon(n,m)$。在 $\epsilon=0$ 附近直接展开有
$$
 \begin{aligned}
 E_\epsilon(n,m)
 &=i h^2\left(nm\csc\theta
       -\frac{n^2+m^2}{2}\cot\theta\right)\\
 &\quad-\epsilon\frac{h^2}{2\sin^2\theta}
          (n^2+m^2-2\cos\theta\,nm)
       +O_\theta(\epsilon^2(n^2+m^2)).
 \end{aligned}
 \tag{13}
$$
显示的实二次型正定。对充分小的 $\epsilon$，
$\operatorname{Re}E_\epsilon\le-c_\theta\epsilon(n^2+m^2)$。
因此在归一的 $\epsilon$ 倍双和中，将精确指数换成 (13) 的
前两项只产生 $O_\theta(\epsilon)$ 误差。这由
$$
 \epsilon\sum_{n,m}\epsilon^2(n^2+m^2)
                  e^{-c_\theta\epsilon(n^2+m^2)/2}=O_\theta(\epsilon)
$$
直接给出。这里 $\theta$ 固定；没有声称对所有 $r$ 一致。

相位除以 $2\pi$ 后的两个二次系数为
$$
 \alpha=-\frac{\cot\theta}{2d},\qquad
 \beta=\frac{\csc\theta}{d},\qquad
 Q(n,m)=\alpha(n^2+m^2)+\beta nm.
 \tag{14}
$$
$\alpha,\beta$ 至少一个无理。否则 $\sin\theta,\cos\theta$
都为有理数，根单位 $e^{i\theta}$ 属于 $\mathbb Q(i)$；
它又是 Gaussian 整数单位，只能属于 $\mu_4$，矛盾。

下面给出所需的均值论证，避免把二次相位的抵消当作直觉。
在任一固定的 $n,m\bmod d$ 剩余类上，周期权成为常数。
重参数后的二次相位仍有至少一个无理二次系数。对矩形
Cesàro 平均使用沿第一变量的有限差分：差分步长 $k\ne0$
将二次相位变成线性相位，其两个线性系数分别含
$2k\alpha$ 和 $k\beta$。至少一个无理，故矩形平均趋于零。
有限差分的 Cauchy–Schwarz 不等式先给平均平方的上极限
至多 $O(1/H)$，再令差分长度 $H\to\infty$，得到
$$
 \frac1{L^2}\sum_{(n,m)\in L\mathcal R\cap\mathbb Z^2}
       a_n\overline{a_m}e^{2\pi iQ(n,m)}\longrightarrow0
 \tag{15}
$$
对任意固定矩形 $\mathcal R$ 成立。

有界区域内用有限矩形阶梯函数一致逼近连续 Gaussian 权，
区域外用正定型的 Gaussian 尾控制，再取 $L=\epsilon^{-1/2}$，
(15) 给
$$
 \epsilon\sum_{n,m}a_n\overline{a_m}e^{2\pi iQ(n,m)}
       e^{-\epsilon h^2(n^2+m^2-2\cos\theta nm)/(2\sin^2\theta)}
              \longrightarrow0.
$$
结合 (10)、(13)，$D_\theta\to1-e^{2i\theta}\ne0$，故
$$
 \boxed{\quad
 \lim_{\epsilon\downarrow0}I_\epsilon(\theta)=0
 \qquad(e^{i\theta}\text{ 是不属于 }\mu_4\text{ 的根单位}).
 \quad}
 \tag{16}
$$

## 4. 中央旋转平均的正范数与单射

设原 $F(z)$ 对 $\mu_4$ 不变，令
$$
 \eta_j=e^{2\pi i j/(4r)},\quad0\le j<r,\qquad
 \mathcal P_rF(z)=\frac1r\sum_{j=0}^{r-1}F(\eta_jz).
 \tag{17}
$$
这准确保留 $z$ 次数被 $4r$ 整除的项；在 $w=z^4$ 中就是
(3)。不同 $j,k$ 的比 $\eta_j/\eta_k$ 都是不属于 $\mu_4$
的根单位。带权面积积分在单位旋转下不变，因此 (12)、(16)
给准确极限
$$
 \boxed{\quad
 \lim_{\epsilon\downarrow0}
      \langle\mathcal P_rf,\mathcal P_rf\rangle_\epsilon
       =\frac1r\mathcal N(f)>0.
 \quad}
 \tag{18}
$$
所以非零的同次数 theta 截面不可能被中央平均杀掉。
此论证对任何该空间内的非零线性组合成立，因此给出真正的
线性单射，而不只是对某一条已选截面的非零性。

### 4.1. 原全部有限次数多项式

取非零 $P(A,B)=\sum_{m=0}^D P_m(A,B)$，每个 $P_m$ 原齐次。
设 $M$ 是最高的非零齐次次数。若 $M=0$，(3) 保留非零常数。
否则，由 $B/A$ 非常数，$P_M(A,B)$ 是非零的实际 theta
截面，正次数为 $68M$，且仍对 $\mu_4$ 不变。

在适合次数 $68M$ 的标准尺度中，较低次数 $m<M$ 的截面
满足 (8) 的更强增长界
$$
 |P_m(A,B)(Z)|\le C_m e^{(m/M)|Z|^2/2}.
$$
其 (9) 范数趋于零，因为相应积分已有固定的额外 Gaussian
衰减，而外面还有因子 $\epsilon$。旋转平均保持这个增长界；
与最高次数项的交叉内积由 Cauchy–Schwarz 也趋于零。
最高次数项则由 (18) 留下严格正值。因此
$$
 \boxed{\quad \mathcal C_r(P(A(w),B(w)))\ne0
                 \quad\text{对每个非零 }P\in\mathbb C[A,B].\quad}
 \tag{19}
$$
特别，全部真实中央行 $[w^{rn}]$ 联合检测原源 $E_D$。
有限维性保证其中有有限个行组成满秩矩阵；本篇没有给出
可免费用于算术预算的统一行号或单位行列式。

### 4.2. 同次数两截面的准确正 Gram 极限

对同次数的两条独立截面，(12)、(16) 可用复极化，或直接把
(10) 中的 $a_n\overline{a_m}$ 换成两个周期向量的乘积。
若原标准尺度的正 Gram 极限为 $G$，则
$$
 \lim_{\epsilon\downarrow0}
       G(\mathcal P_rf_1,\mathcal P_rf_2;\epsilon)=G/r,
 \qquad \det G>0.
 \tag{19a}
$$
还可以把这个正性写成实际中央 Taylor minor 的加权和。
令 $v_s=([Z^{4rs}]f_1,[Z^{4rs}]f_2)^{\mathsf t}$。角向积分
使不同 Taylor 次数正交，故
$$
 G(\mathcal P_rf_1,\mathcal P_rf_2;\epsilon)
   =\epsilon\sum_{s\ge0}
       \frac{(4rs)!}{(1+\epsilon)^{4rs+1}}v_sv_s^*.
$$
对本题从四阶开始的截面，$v_0=0$。Cauchy–Binet 给
$$
 \lim_{\epsilon\downarrow0}
 \epsilon^2\sum_{1\le s<t}
 \frac{(4rs)!(4rt)!}{(1+\epsilon)^{4r(s+t)+2}}
            |\det(v_s,v_t)|^2
                 =\frac{\det G}{r^2}>0.
 \tag{19b}
$$
这里 $v_s$ 是同一复标准尺度中的原 Taylor 列，不是 R185 的
$p$ 进整轴。还原原有理系数时需保留共同的复缩放因子。
(19b) 明确指出有限窗口量化所需控制的尾部；它没有给出该
尾部对所有 $r$ 一致的界。

## 5. 原整轴的二维性与两有限 Stokes 方向

固定惰性 $p=4r-1\ge7$。R185 的同一形式坐标满足
$$
 A(w)=\Gamma(w)^{17}f(\zeta(w)),\qquad
 B(w)=\Gamma(w)^{17}g(\zeta(w)),
 \tag{20}
$$
其中 $\Gamma(\epsilon w)=\Gamma(w)$、
$\zeta(\epsilon w)=\epsilon\zeta(w)$ 对 $\epsilon\in\mu_r$
成立，且 $\zeta=w+O(w^2)$。因此
$$
 \mathcal C_r A
 =\Gamma^{17}\sum_{s\ge1} f_{rs}\zeta^{rs},\qquad
 \mathcal C_r B
 =\Gamma^{17}\sum_{s\ge1} g_{rs}\zeta^{rs}.
 \tag{21}
$$
公共单位与可逆代换保留线性关系。

若向量 $(f_{rs},g_{rs})$ 只张成一维，则 (21) 使
$\mathcal C_r A,\mathcal C_r B$ 在 $\mathbb Q_p$ 上相关。
这两条中央级数的系数都是有理数，并由第 4 节分别非零。
比较任何一个非零系数可知相关比例在 $\mathbb Q$ 中。
于是同一个关系也在复数上成立，与 (18) 对原 $A,B$ 的
单射矛盾。故
$$
 \boxed{\quad
 \operatorname{span}_{\mathbb Q_p}{(f_{rs},g_{rs}):s\ge1\}
                         =\mathbb Q_p^2.
 \quad}
 \tag{22}
$$

令 $\omega_s=\lambda_{17,s}/\lambda_{17,1}$ 为 R185 的实际
非零整权，定义同一部分和方向
$$
 q_N=\sum_{s=1}^N\omega_s(f_{rs},g_{rs}),\qquad q_0=0.
 \tag{23}
$$
因为
$$
 q_N-q_{N-1}=\omega_N(f_{rN},g_{rN}),\qquad\omega_N\ne0,
$$
(22) 等价于 $\{q_N:N\ge1\}$ 张成二维。因此对每个该素数，
确实存在有限的 $N,M$ 使
$$
 \boxed{\quad\det(q_N,q_M)\ne0.\quad}
 \tag{24}
$$
即使两个完整中央导数都为零，(24) 仍成立；此时 R185 的
完整尾界另给 $q_N\in p^{N+v_p(N!)}\mathbb Z_p^2$。
这些小的部分和方向仍可在不同有限层线性独立。

所以 R189 双方向 Hasse 矩阵的秩二情形对每个固定 $p$
都有实际有限输入，不能再把“是否永远只有一个方向”作为
未付条件。仍须支付 $N,M$ 的大小、$\det(q_N,q_M)$ 的赋值，
以及从这些行到同一个真实消失前缀矩阵的比较。

### 5.1. 前两个真实秩跳处无需未知换元分母

令原有理中央行与整轴行分别为
$$
 R_s=([w^{rs}]A,[w^{rs}]B)\in\mathbb Q^2,
 \qquad v_s=(f_{rs},g_{rs})\in\mathbb Z_p^2.
$$
取 $a$ 为第一条非零 $R_s$ 的行号，取 $b>a$ 为使前 $b$ 行
秩首次成为二的行号。它们由 (22) 存在，且只由原有理
Taylor 系数确定。

置 $t=w^r$、$u=\zeta(w)^r$。由角色性质，
$u=t+O(t^2)$、$\Gamma(w)^{17}\in1+t\mathbb Q_p[[t]]$。
所以 (21) 在每个有限窗口中，都是同一个对角为一的
下三角矩阵作用于向量序列 $v_s$。这保持每个前缀的秩，
并在这两个首次跳跃处准确给
$$
 v_a=R_a,\qquad
 \det(v_a,v_b)=\det(R_a,R_b).
$$
原因是 $s<a$ 的行全为零，$a\le s<b$ 的行都在 $R_a$
张成的直线上；高阶换元在第 $b$ 行加入的只有这条直线。
因此没有任何未知高阶换元系数留在该 minor 中。

部分和 (23) 是另一个对角为 $\omega_s\ne0$ 的下三角换基。
同样的首次跳跃论证遂给
$$
 \boxed{\quad
 \det(q_a,q_b)
       =\omega_a\omega_b\det(R_a,R_b)\ne0.
 \quad}
 \tag{25}
$$
这是准确等式，不只是“至少某一个 minor”的赋值比较。
尤其
$$
 \begin{aligned}
 v_p\det(q_a,q_b)
 &=a+b-2+v_p((a-1)!)+v_p((b-1)!)\\
 &\qquad+v_p\det(R_a,R_b).
 \end{aligned}
 \tag{26}
$$

若两个完整中央导数都为零，R185 的尾界在层 $a,b$ 上给
$q_a\in p^{a+v_p(a!)}\mathbb Z_p^2$、
$q_b\in p^{b+v_p(b!)}\mathbb Z_p^2$。由 (25) 得到两个
实际有理必要条件
$$
 \boxed{\quad
 \min_i v_p((R_a)_i)\ge1+v_p(a),\qquad
 v_p\det(R_a,R_b)\ge2+v_p(ab).
 \quad}
 \tag{27}
$$
违反任一条件就证明两个原中央导数不同时为零。
例如若最先两次秩跳恰在 $a=1,b=2$，则实际原二阶中央
minor 不被 $p^2$ 整除便是充分非零证书。本文没有证明
该情形或该不等式对无穷多个 $p$ 成立。

在 R189 的适配原基 $(A,B-A)$ 中，这些行只作一次整
行列式一的换基，所以 (25)–(27) 的行列式和整范数不变。
这些结论也没有把任意两个层号都当成首次秩跳。

## 6. 当前结论的边界与依赖

(16) 中的估计按固定旋转成立；(15) 只使用定性的二次相位
均值。本篇没有从它们推出对所有 $p$ 一致的收敛速度。
特别，(24) 不是两个中央导数之一非零的证明，也没有将
R189 的精度成本从实际旗标预算中扣去。

- [R115：原 E34 次数六十八截面及准周期](R115-e34-explicit-degree68-theta-section.md)。
- [R162：同一原平面、两多项式及首项](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- [R158：原有限源与准周期增长](R158-ordinary-saturated-jets-and-degree-sensitive-budget.md)。
- [R185：真实整轴、非零 Stokes 权和完整尾界](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
- [R188：同一原源的整检测与 Hasse 运输](R188-original-source-detection-and-integral-hasse-transport.md)。
- [R189：实际单、双方向 Hasse 族及精度格](R189-complete-central-hasse-families-and-weighted-core.md)。

这里使用的 Gaussian 积分、差分均值和有限维推论都已在正文
给出证明；没有借有限素数扫描断言旋转或中央序列的独立性。
