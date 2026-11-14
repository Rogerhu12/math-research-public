# R474 — 原六 sigma 的真实双输出核心与完整 Riemann 条件域

日期：2026-11-14。**状态：已证明。** R471 的六 sigma 因子与
两个 Theta 因子，在同一个压缩二输入上形成一个真实两态核心。
本篇独立支付六 sigma 因子的普通核心、整个 degree136 的中心相位、
两个正交输出的全部深度，并给原八输入上的可逆 Riemann 域运输。
这些结论不把压缩输出的条件改写成六个内部输入分别满足的条件。
主目标仍未完成。

## 1. 同一来源、物理周期与两个压缩输入

沿用 R471 的 $b=17$、$\Theta=x\sigma^2$、同一物理普通周期及
当前固定 ray。所有测度的 Amice 生成函数按
$z=\Omega_p\log(1+T)$ 解释。记
$$
F=\mathcal F_{72}=\sigma(z)^4\sigma(2z)\sigma(8z),\qquad
U=\mathcal U_{64}=\Theta(4z)^2,
\tag{1}
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda=\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad d=p-1.
\tag{2}
$$
R471 已在完整全纯来源中证明
$$
W_*:=101W_{13}-64W_{15}=-\frac{111}{280}FU,\qquad
F=16z^6+O(z^{12}),\quad U=1+O(z^6).
\tag{3}
$$
这里 $F$、$U$ 的测度分别是原六个、两个独立输入的**总输出**
推前。设它们的物理输出为 $A,B$，取
$$
\mu_0=\nu_F(A)\otimes\nu_U(B),\qquad
W=A+B,\qquad Q=8A-9B.
\tag{4}
$$
变换矩阵及其行列式为
$$
T=\begin{pmatrix}1&1\\8&-9\end{pmatrix},\qquad \det T=-17.
\tag{5}
$$
因此当前 $p>19$ 处，$(A,B)$ 与 $(W,Q)$ 是同一个整二输入空间
的可逆坐标。其完整生成来源是
$$
\Phi(w,q)=F(w+8q)U(w-9q)
\in\mathcal S_{136}\boxtimes\mathcal S_{9792}.
\tag{6}
$$
极化的三项计算准确为
$$
72+64=136,\qquad 72\cdot8-64\cdot9=0,\qquad
72\cdot8^2+64\cdot9^2=9792.
\tag{7}
$$
两个原次数均偶，且显示的线性系数均为整数，故 (6) 的两轴
为原标准对称线丛；没有未说明的平坦 twist。所有整数系数的
实际推前仍保 R471 的原物理周期。

记 $\nu_0=T_*\mu_0$。再定义真实第二来源
$$
\Psi(w,q)=\Phi(-w,q)=\Phi(w,-q),\qquad
\nu_1=(R_W)_*\nu_0=(R_Q)_*\nu_0.
\tag{8}
$$
第二个等号来自 $F,U$ 都是偶函数，而非只在 principal 观察下
投影。换回物理 $(A,B)$，该反射为
$$
R_{AB}=T^{-1}\begin{pmatrix}-1&0\\0&1\end{pmatrix}T
=\frac1{17}\begin{pmatrix}-1&-18\\-16&1\end{pmatrix},\qquad
R_{AB}^2=I.
\tag{9}
$$
它是实际整可逆输出变换，不能误认作两个原独立输入的交换。

## 2. 六 sigma 因子的实际 core 独立于 Theta 反卷积

取
$$
N_7=\mathscr M_{\gamma_7}/\gamma_7,\qquad
\gamma_7=(5+\delta)/2,\qquad \delta^2=-3.
$$
R413 已在整个 degree72 theta 空间支付绝对身份
$$
K_{72}=-N_7^9,\qquad
\nu_H|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_{72}H}.
\tag{10}
$$
本篇用 R464 的完整商环纤维算法，对原 principal 空间
$$
\left\{\sigma^{72}X^j:0\le j\le12\right\},\qquad X=x^3,
\tag{11}
$$
求得整个十三维 $N_7$ 矩阵。十三个目标 $X=1,\ldots,13$ 的
每一次运算均对整个七度 CM 纤维取迹；不是选取某一逆像或
使用数值近似。它们确定有限维多项式的所有系数。

对 R471 完整多项式 (11) 的实际向量 $v_F$，精确结果是
$$
\boxed{
F=F_1+F_{\omega^2},\qquad
N_7F_1=F_1,\quad N_7F_{\omega^2}=\omega^2F_{\omega^2},
\quad F_1,F_{\omega^2}\ne0.
}
\tag{12}
$$
尤其
$$
N_7^3F=F,\qquad N_7^9F=F,\qquad
P_{N_7=-1}F=0.
\tag{13}
$$
两实际分量的质量为
$$
F_1(0)=\frac1{6b},\qquad F_{\omega^2}(0)=-\frac1{6b}.
\tag{14}
$$
数据文件列出两个分量的全部十三个有理系数；$b=1$ 的第 $j$
列按 $b^{11-j}$ 恢复一般 $b$，所以最高列 $j=12$ 正是 (14)。
两分量的非零质量相消得到原 $F(0)=0$。由于对应特征在整个
十三维空间有重数，这里不为它们指定新的单条椭圆曲线身份。

由 (10)–(13) 得到独立的完整测度身份
$$
\boxed{\nu_F|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_F.}
\tag{15}
$$
这一步没有从 $FU$ 的核心除去 $U$，也没有仅凭次数七十二
或零质量认定它是原 $T$。事实上原 $T$ 的 $N_7$ 特征是 $-1$，
而 (13) 已排除 $F$ 在该特征的分量。

### 2.1 两 Theta 乘积的绝对符号

先看真实 $\Theta^2\in\mathcal S_4$。当前 ratio 在含中心模数
八上为 $g=\pi_0/\bar\pi_0\equiv3$。在 degree4 的标准
Schrödinger 基中，普通反射 $R:e_j\mapsto e_{-j}=e_{3j}$
实现两个完整 Heisenberg 生成元所需的逆变换。因此真实
$K_4$ 与 $R$ 相差一个标量。

用非零 odd 锚 $\sigma(2z)\in\mathcal S_4$ 定标。R316 的真实
sigma core 是 $\beta$，尺度二是 $p$ 单位，所以按统一外部
系数 $\lambda$ 有 $K_4\sigma(2z)=-\sigma(2z)$。而
$R\sigma(2z)=-\sigma(2z)$，故绝对标量为一：
$$
K_4=R,\qquad K_4\Theta^2=\Theta^2.
\tag{16}
$$
独立的完整 norm-seven 一维纤维还给
$N_{7,4}\Theta^2=-\omega\Theta^2$，与 (16) 相容。
再沿四倍拉回，$\nu_U=[4]_*\nu_{\Theta^2}$；$4$ 为单位，
与真实深度限制交换。因此
$$
\boxed{\nu_U|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_U.}
\tag{17}
$$
(17) 的符号与单个 $\Theta$ 的 $\beta$ 相反。两个独立
$\Theta$ 的全深域与它们总和的深域不同，所以没有矛盾。

## 3. 完整二挠 trace 支付 $W$ 轴核心

全部平移使用 R416 的对称规范
$$
(T_t^{(N)}H)(z)=e^{-N\eta_t(z+t/2)}H(z+t).
\tag{18}
$$
对 $0\ne t\in E[2]$，令 $e=x(t)$，$e^3=-b$。
原半特征准确给
$$
T_t^{(4)}\sigma(2z)=-\sigma(2z),\qquad
T_t^{(64)}\sigma(8z)=\sigma(8z).
\tag{19}
$$
前者是 odd sigma 在非零二挠对应的原始格周期处的负号；
后者对应偶格周期，符号为正。原半周期公式则给
$$
T_t^{(4)}\sigma(z)^4
=\frac{(x-e)^2}{3e^2}\sigma(z)^4.
\tag{20}
$$
其中 $c_t^4=(3e^2)^{-1}$ 的绝对号由同一个 (19) 定标，不是
任取平方根。由于三根 $e^3=-b$ 的倒数和、平方倒数和都为零，
$$
\sum_{0\ne t\in E[2]}T_t^{(4)}\sigma^4=\sigma^4.
$$
乘上 (19) 中的两个因素，得到整个来源的身份
$$
\boxed{\sum_{t\in E[2]}T_t^{(72)}F=0.}
\tag{21}
$$

另一方面 $U=[4]^*\Theta^2$ 在全部 $E[2]$ 平移下固定。对于
(6)，两轴交叉指数 $72\cdot8-64\cdot9=0$ 使 $W$ 平移在两个
原因子上准确分解，且 $q$ 不添指数。因此 (21) 也给
$$
\sum_{t\in E[2]}T_{t,W}^{(136)}\Phi=0.
\tag{22}
$$
这是完整二变量来源的式子，保留伴随输出 $Q$。

现支付整个 $\mathcal S_{136}$ 的算子，而非只使用 principal
矩阵。令
$$
B_2=\frac12\sum_{t\in E[2]}T_t^{(136)}-I.
$$
在原 $136$ 维 Schrödinger 基中，含中心的准确公式为
$$
B_2e_j=(-1)^j e_{69j+68},\qquad B_2^2=I,\qquad
B_2XB_2^{-1}=-X^{69},\quad B_2ZB_2^{-1}=-Z^{69}.
\tag{23}
$$
它实现的完整 ratio 是 $69+136\omega\bmod272$。乘普通反射
后为
$$
-(69+136\omega)\equiv203+136\omega\pmod{272},
$$
恰是 R466 当前 ray 的真实 $g$。所以 $K_{136}$ 与 $RB_2$
相差标量。原 $S(2z)$ 是偶来源，全部规范 $E[2]$ 平移固定，
且 R466 已付 $K_{136}S(2z)=S(2z)$；同时
$RB_2S(2z)=S(2z)$，故标量为一：
$$
\boxed{K_{136}=RB_2\quad\text{在整个 }\mathcal S_{136}\text{ 上成立}.}
\tag{24}
$$
由 (22)，$B_{2,W}\Phi=-\Phi$，故
$$
K_W\Phi=-\Psi,\qquad K_W\Psi=-\Phi.
\tag{25}
$$
这给同一完整二输入上的第一个实际核心：
$$
\boxed{
\nu_0|_{W\in p\mathbf Z_p}=\beta[\kappa,1]_*\nu_1,\qquad
\nu_1|_{W\in p\mathbf Z_p}=\beta[\kappa,1]_*\nu_0.
}
\tag{26}
$$

## 4. 比较实际全双深域，支付 $Q$ 轴而不猜大 level 相位

(15)、(17) 和 $\det T=-17\in\mathbf Z_p^\times$ 给
$$
\nu_i|_{\{W,Q\in p\mathbf Z_p\}}
=\beta\lambda[\kappa,\kappa]_*\nu_i,\qquad i=0,1.
\tag{27}
$$
这里 (27) 是原 $(A,B)$ 的**两个压缩输入**均深的完整推前。
再将 (26) 限制到 $Q\in p\mathbf Z_p$，与 (27) 比较，并取消
单射推前 $[\kappa,1]_*$，得到
$$
\boxed{
\nu_0|_{Q\in p\mathbf Z_p}=\lambda[1,\kappa]_*\nu_1,\qquad
\nu_1|_{Q\in p\mathbf Z_p}=\lambda[1,\kappa]_*\nu_0.
}
\tag{28}
$$
取消推前合法：$[\kappa,1]$ 是原紧空间到其闭像的同胚，
对其像上的测度有唯一逆。这里没有由交织同余猜测整个
degree9792 的绝对标量。

(26)、(28) 可以在同一个完整来源中相互迭代。任意 $n,m\ge0$
均有
$$
\boxed{
\nu_i|_{\{W\in p^n\mathbf Z_p,\ Q\in p^m\mathbf Z_p\}}
=\beta^n\lambda^m[\kappa^n,\kappa^m]_*
  \nu_{\,i+n+m\bmod2}.
}
\tag{29}
$$
因此对任意连续测试 $h(W,Q)$，右边实际代入
$h(\kappa^nW,\kappa^mQ)$，并保留显示的来源状态。
用 (8) 吸收反射，也可准确写成原单一来源上的有符号缩放：
$$
\boxed{
\nu_0|_{W\in p\mathbf Z_p}=\beta[-\kappa,1]_*\nu_0,\qquad
\nu_0|_{Q\in p\mathbf Z_p}=\lambda[1,-\kappa]_*\nu_0.
}
\tag{30}
$$
奇测试中的负号是实际物理符号，不能省略。
原 $(A,B)$ 中的两映射分别是
$T^{-1}\operatorname{diag}(-\kappa,1)T$、
$T^{-1}\operatorname{diag}(1,-\kappa)T$。

### 4.1 完整 principal 行上的伴随 core

令
$$
f_u(W)=\mathbf1_{W\in\mathbf Z_p^\times}
       \langle W\rangle^{du}.
$$
因为 $f_u(-W)=f_u(W)$，(8) 在任意完整 $Q$ 测试下给两状态
相同的 principal 行。于是 (28) 准确成为
$$
\boxed{
\int_{W\ {\rm unit},\,Q\in p^n\mathbf Z_p}
 \langle W\rangle^{du}h(Q)\,d\nu_0
=\lambda^n
 \int_{W\ {\rm unit}}\langle W\rangle^{du}
 h(\kappa^nQ)\,d\nu_0 .
}
\tag{31}
$$
例如 $h(Q)=Q^m$ 时，限制 $Q$ 为单位的 Euler 因子为
$1-\lambda\kappa^m$。同时全来源的对角 $\mu_6$ 对称性使这条
principal 行的 $Q^m$ 矩只可能在 $6\mid m$ 时非零。
所有这些都是来源与测试的真运输；并不宣称相应中央导数为零。
常数测试给的是原未投影 $W_*$ 行，而非仅 R466 的新曲线行。

## 5. 原八输入上的四 sigma 变换与准确转置

保留 R471 全部八个独立输入
$$
\mu=\nu_\sigma^{\otimes6}\otimes\nu_\Theta^{\otimes2},\qquad
A=x_1+x_2+x_3+x_4+2x_5+8x_6,\qquad B=4t_1+4t_2.
\tag{32}
$$
本节只在四个输入 $(x_1,x_2,x_5,x_6)$ 上操作，另外两个 sigma
与两个 Theta 输入完整保留。设
$$
H=\frac12
\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix},\qquad
J=\operatorname{diag}(1,1,1,-1),\qquad H^2=I.
\tag{33}
$$
对于 $f(z_1,z_2,z_3,z_4)=\prod_{j=1}^4\sigma(z_j)$，
原 sigma 加法公式准确给
$$
f(z)=f(Hz)-f(HJz).
\tag{34}
$$
为固定符号，置
$u=(z_1+z_2)/2$、$x=(z_1-z_2)/2$、
$v=(z_3+z_4)/2$、$y=(z_3-z_4)/2$。
使用
$$
\sigma(a+b)\sigma(a-b)
=\sigma(a)^2\sigma(b)^2(\wp(b)-\wp(a))
$$
后，(34) 化为
$$
(\wp(v)-\wp(u))(\wp(y)-\wp(x))
-(\wp(y)-\wp(u))(\wp(v)-\wp(x))
=(\wp(x)-\wp(u))(\wp(y)-\wp(v)).
$$
所以 (34) 是有固定符号的完整恒等式。

由 Amice 变换唯一性，**物理输入的推前使用转置**：
$$
\nu_\sigma^{\otimes4}
=H_*\nu_\sigma^{\otimes4}-(JH)_*\nu_\sigma^{\otimes4}.
\tag{35}
$$
记 $\widehat H,\widehat{JH}$ 为它们在完整八输入上的扩张，其他
四个输入保持不动。对任意真实紧开条件域 $D$（或指示函数
积分已定义的域）和连续测试 $h$，准确式是
$$
\boxed{
\int_D h\,d\mu
=\int_{\widehat H^{-1}D}h(\widehat Hx)\,d\mu
 -\int_{\widehat{JH}^{-1}D}h(\widehat{JH}x)\,d\mu .
}
\tag{36}
$$
所有域、单位指示函数及对数测试必须依照 (36) 运输。
因为 $p\ne2$，两个映射均为 $\mathrm{GL}_4(\mathbf Z_p)$；
四个选中输入**同时**在 $p^n\mathbf Z_p$ 的域保持不变。
各输入分别带不同深度条件时，像一般是新的线性条件域，
不能逐项沿用旧条件。

原四个输出权为 $a=(1,1,2,8)^t$。精确变换给
$$
Ha=(6,-4,-3,3)^t,\qquad HJa=(-2,4,5,-5)^t.
\tag{37}
$$
因此完整未限域来源也有
$$
\boxed{
F=\sigma(z)^2\sigma(3z)^2\sigma(4z)\sigma(6z)
 -\sigma(z)^2\sigma(2z)\sigma(4z)\sigma(5z)^2.
}
\tag{38}
$$
两项次数同为七十二，首系数分别为 $216$ 和 $200$，其差为
原 $16$。R471 的 $\Theta(4z)^2$ 在两个分支中始终是原两个
独立输入。对于二输出条件，$B$ 不变，$A$ 依 (37) 替换，
$W=A+B$ 和 $Q=8A-9B$ 两条输出都随同运输。
不能只改 $W$ 而丢弃 $Q$。

精确多项式证书还直接核定 (38)。在 $b=1$ 记
$$
D_2=X^2+20X-8,\qquad
A_5=32(X+1)^2D_2-27X(X+4)^3.
$$
两个分支除以 $\sigma^{72}$ 后分别为
$$
216X(X+1)(X+4)^3D_2(A_5-4D_2^2),\qquad
8(X+1)D_2A_5^2,
\tag{39}
$$
其差与 R471 原完整十一度多项式相等。一般 $b$ 由齐次性
准确恢复。

## 6. 本结果的范围与证书

本篇新付的核心是原压缩来源 $\nu_F\otimes\nu_U$ 的完整二输入
身份 (29)，以及原八输入的域恒等式 (36)。它们可相容使用，
但后者不能把 (29) 自动升级为带任意六 sigma 内部测试的核心。
同样，(38) 的差有本篇核心，不因此把两个分支各自赋予该核心
或中央零。

R471 的 $W_*$ 含新算术线与真实非零外部六维分量。
当前两态式没有删去外部谱，也没有从 $W_*$ 的普通核心或其
六阶单位矩非零推出中央导数非零。

精确复核材料：

- [复核脚本](../scripts/check-r474-six-sigma-two-output-core.py)：
  核原 $F$ 的全部十三列谱、degree4 的完整 CM 纤维、整
  $136$ 维含中心 $B_2$、两个输出的极化与物理反射，以及
  两个 Riemann 分支的完整多项式。
- [复核输出](../scripts/check-r474-six-sigma-two-output-core.json)：
  两实际谱向量及全部显示的有限矩阵。
- [完整 degree72 CM7 矩阵](../notes/2026-11-14-literature-degree72-cm7-exact.json)：
  以 R464 的完整纤维程序生成，参数为 degree $72$、offset $0$，
  $b=1$、十三个全纤维目标。
- [R471：原六 sigma × Theta 因式与八输入 carry](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R413：整个 degree72 的绝对核心](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R416：固定规范的全部二挠／四挠平移](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R466：当前完整 degree136 ratio 与原 $S(2z)$ 锚](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。

