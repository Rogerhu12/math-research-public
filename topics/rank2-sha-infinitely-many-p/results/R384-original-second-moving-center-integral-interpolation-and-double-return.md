# R384：原第二移动中心的六来源整插值与完整双移动球返回

日期：2026-11-14。**状态：已证明。** 对 R381 保留下来的同一
$(Y,R)$ 联合，本文计算全部六个真实来源的秩，给出原目标向量，
并以固定整数中心 $1,2,3,4,5,9$ 构造整的同层球插值。
它与 R381 的十二球权复合后，保持同一个原输出 $Y$，
在明确的四百三十二球域内返回整个 $\nu_S^\times$。
所有参考在取 Mellin 之前消去；原单叶之外的各支仍完整保留。

## 1. 原对象和本文的有限例外

保留 R379–381 的同一模型、测度、周期及固定无穷素数族
$$
E_{17}:y^2=x^3+b,\quad b=17,\quad
\pi=\psi_{17}(\mathfrak p)\equiv1
 \pmod{M\mathcal O_K},\quad M=5346432,
$$
$$
\lambda=1/\bar\pi,\quad \kappa=p/\bar\pi^2,\quad
\int e^{zt/\Omega}d\nu_G(t)=G(z).
$$
特别 $p\equiv1\bmod M$，所以 $p>M$。
记 $X=x^3$，并继续使用真实来源
$$
D=\sigma^{16}x^2(X+b),\quad
E=\sigma^{16}x^2(X^2-28b^2),\quad
C=\sigma^{18}(X-8b)(X^2-4bX/7+16b^2/7),\quad S=DC.
\tag{1}
$$
没有更换 R381 的 $D,E,C$；这里 $E$ 是实际 degree 十六来源的名字。

以下一个固定正整数记录唯一新增的有限例外：
$$
\begin{split}
\mathcal N={}&
23318923282365151738616026730130526028494926226150500448150665439776887285725607516802822313558989210799570944.
\end{split}
\tag{2}
$$
本文取 R379 素数族中满足 $p\nmid\mathcal N$ 的素数。
这是排除一个明确固定整数的有限素因子，故仍为同一个固定无穷集合。
不需要猜测 (2) 剩余大因子的素性或按目标素数扫描。

原联合为
$$
\eta_{DC}=(Y,R)_*(\nu_D(u)\otimes\nu_C(c)),\qquad
Y=u+c,\quad R=9u-8c.
\tag{3}
$$
其 $Y$ 边际是 $\nu_S$。R379 已付保持 $Y$ 的完整 $R$-core，
所以没有在本文另猜一个 degree $2448$ 的整体标量。

## 2. 第二联合的全部真实六来源

整个变换为
$$
F(z,v)=D(z+9v)C(z-8v).
\tag{4}
$$
$z$、$v$ 两方向的 degree 分别为
$$
34,\qquad16\cdot9^2+18\cdot8^2=2448.
$$
交叉项 $16\cdot9-18\cdot8=0$；完整半特征均为原偶 degree 特征。
因此 (4) 是原
$\mathcal O(34O)\boxtimes\mathcal O(2448O)$ 的截面，
没有未支付的 Gaussian。

只在 $R$ 上作 $\mu_6$ 平均，记为 $\mathsf P_R$。
$D,C$ 均为型零，故该平均也使 $z$ 的型为零。
原输出空间准确是
$$
F_i=\sigma^{34}x^{2+3i},\qquad0\le i\le5,
\tag{5}
$$
首阶依次为 $30,24,18,12,6,0$。
于是存在唯一的实际辅助来源 $\Gamma_i(v)$ 和测度 $\tau_i=\nu_{\Gamma_i}$，
使
$$
\boxed{\mathsf P_R\eta_{DC}=\sum_{i=0}^5\nu_{F_i}\otimes\tau_i.}
\tag{6}
$$
每个 $\Gamma_i$ 属于原 $\mathcal S_{2448}$ 的型零空间。

为支付整性，设 $B_{ki}=[z^{6k}]F_i$，$0\le k,i\le5$。
$B$ 是反三角矩阵，反对角全一，故 $\det B=-1$。
系数测度由原输出矩
$$
\frac1{(6k)!\Omega^{6k}}
(\operatorname{pr}_R)_*(Y^{6k}\mathsf P_R\eta_{DC})
$$
乘 $B^{-1}$ 得到。当前 $p>M>30$，所有阶乘和周期均为单位，
且 $B,B^{-1}$ 在原整格上整。因此各 $\tau_i$ 真正整有界。
整个测度式由全部多变量矩的唯一性得到，未用有限 jet 替代全 theta 身份。

R379 的 $R$-core 与 (6) 的输出来源线性独立相结合，又给
$$
\boxed{\tau_i|_p=\lambda[\kappa]_*\tau_i\qquad(0\le i\le5).}
\tag{7}
$$
这里只断言这六条实际来源的 core；
没有把整个 $\mathcal S_{2448}$ 未经锚定地设为标量。

原目标是辅助参数 $v=0$，所以其准确向量是
$$
\boxed{
s=(\Gamma_0(0),\ldots,\Gamma_5(0))^t
=\left(-\frac{128b^4}{7},-\frac{80b^3}{7},
 -\frac{12b^2}{7},-\frac{53b}{7},1,0\right)^t,
\quad S=\sum_i s_iF_i.
}
\tag{8}
$$
该向量是原 $S$，不是另选的有限空间方向。

## 3. 六个实际系数确实满秩

令
$$
J_{kl}=[z^{6k}v^{6l}]F(z,v),\qquad0\le k,l\le5.
$$
以下是完整可复现的有理计算；先取 $b=1$。
写 $w=z^6$、
$$
x=z^{-2}\mathcal X(w),\qquad
\log(\sigma/z)=\mathcal L(w).
$$
原微分方程给
$$
x_0=1,\quad x_1=-1/7,\quad
x_n=\frac{\sum_{j=1}^{n-1}x_jx_{n-j}}{(6n+1)(n-1)}
\quad(n\ge2),
\qquad
\ell_n=-\frac{x_n}{6n(6n-1)}.
\tag{9}
$$
只需要 $n\le10$。由 (1)，真实系数序列为
$$
\begin{aligned}
D(z)&=\sum d_nw^n
=e^{16\mathcal L}\bigl(w\mathcal X^5+w^2\mathcal X^2\bigr),\\
C(z)&=\sum c_nw^n
=e^{18\mathcal L}\left(
 \mathcal X^9-\frac{60}{7}w\mathcal X^6
 +\frac{48}{7}w^2\mathcal X^3-\frac{128}{7}w^3\right).
\end{aligned}
\tag{10}
$$
因此，不省任何相加项，
$$
\boxed{
J_{kl}=
\sum_{i+j=k+l}d_i c_j
 \sum_r
 \binom{6i}{r}\binom{6j}{6l-r}
 9^r(-8)^{6l-r}.
}
\tag{11}
$$
负下标的二项式取零。

附带纯 BigInt 有理数脚本执行 (9)–(11)，给准确值
$$
\boxed{\det J\big|_{b=1}=-\mathcal N/117649=-\mathcal N/7^6.}
\tag{12}
$$
它还按 (5) 计算 $B$，验证 $\det B=-1$，
并完整求解 $G=B^{-1}J$。
其中
$$
G_{il}=[v^{6l}]\Gamma_i,\qquad
G_{\cdot0}=(-128/7,-80/7,-12/7,-53/7,1,0)^t,
$$
$$
\boxed{\det G\big|_{b=1}=\mathcal N/7^6.}
\tag{13}
$$
这同时核对了实际目标接口，不只是输出一个抽象 rank 数。

一般 $b$ 的 (10) 满足 $d_n(b)=b^{n-1}d_n(1)$、
$c_n(b)=b^nc_n(1)$。
所以
$$
J_{kl}(b)=b^{k+l-1}J_{kl}(1),\qquad
G_{il}(b)=b^{l+4-i}G_{il}(1),
$$
$$
\boxed{\det G(b)=b^{24}\mathcal N/7^6.}
\tag{14}
$$
当前 $b=17$ 和第1节素数范围使其为单位。
这是同一原模型的尺度，没有把不同曲线的周期隐式混用。

## 4. 固定六个移动中心的非零全 theta 行列式

固定真正的整数尺度
$$
\boxed{a_1,\ldots,a_6=(1,2,3,4,5,9).}
\tag{15}
$$
取整个截面
$$
\mathcal H(v)=\det[\Gamma_i(a_jv)]_
                 {0\le i\le5,\ 1\le j\le6}.
$$
每一项的 line bundle 相同，故
$$
\boxed{\mathcal H\in\mathcal S_{\mathfrak d},\qquad
 \mathfrak d=2448\sum_{j=1}^6a_j^2=2448\cdot136=332928.}
\tag{16}
$$
全部整数乘法的自动因子和偶半特征保留在这个真实 degree 中。

由 (13)–(14)，最小非零系数准确为
$$
\boxed{
[v^{90}]\mathcal H(v)
=\frac{b^{24}\mathcal N}{7^6}
 \prod_{1\le i<j\le6}(a_j^6-a_i^6).
}
\tag{17}
$$
理由是行列式中重复的 Taylor 指数相消，
最小六个互异型零指数为 $0,6,12,18,24,30$，
其和九十，系数就是 (14) 与完整 Vandermonde 的乘积。
不是假定六个任意取值点都能分离来源。

Vandermonde 非零。其任一素因子不超过
$9^6-1=531440<M$，已经被本篇 $p>M$ 排除。
(2)、(14) 处理了其余固定例外。
所以 (17) 在当前每个素数处为单位，
$\mathcal H$ 的整约化不恒零；没有额外 vertical 因子。
其非零零除子 degree 为固定的 $\mathfrak d$，且定义在 $\mathbf F_p$ 上。

## 5. 原加法球矩阵的统一整逆

对 $N\ge1$、单位 $t$，定义原球矩阵
$$
\mathcal M_N(t)_{ij}=\tau_i(a_jt+p^N\mathbf Z_p).
\tag{18}
$$
使用 R376 的原 degree $2448$ 加法标签。
所有六条来源都有同 degree、同原周期及同一个 (7)，
所以每列准确具有共同的单位因子：
$$
\mathcal M_N(t)_{ij}
=\lambda^N u_j(t)\, f_i(a_jP_t),\qquad
u_j(t)\in\mathcal O^\times,\quad
\Gamma_i=\sigma^{2448}f_i.
\tag{19}
$$
这里 $P_t$ 的精确阶为 $p^N$，
而整数 $a_j$ 使原标签满足 $P_{a_jt}=a_jP_t$。
完整 Fourier 分母、division 导数和周期已包含在 $u_j$；
它不是删除后的裸 theta 点值。

还要比较 (19) 的有理 frame 与 (16)。
准确恒等式是
$$
\mathcal H(v)=\sigma(v)^{\mathfrak d}
 \left(\prod_j r_{a_j}(v)^{2448}\right)
 \det[f_i(a_jv)],\qquad
r_a=\sigma(av)/\sigma(v)^{a^2}.
\tag{20}
$$
每个原 $r_{a_j}$ 的零极只在固定的 prime-to-$p$ 挠点，
首项 $a_j$ 为单位。因此在 $P_t$ 及其约化处，
(20) 的各个有理 frame 比都是单位。
没有把复 sigma 值不加证明地叫作 $p$ 进单位。

若 $\bar P_t$ 落在 $\overline{\mathcal H}$ 的零除子上，
它定义在某个 $\mathbf F_{p^e}$ 上，$e\le\mathfrak d$。
精确阶 $p^N$ 与
$\#E(\mathbf F_{p^e})<p^{e+1}$ 迫 $N\le e$。
所以固定阈值
$$
\boxed{N\ge332929}
\tag{21}
$$
给
$$
\boxed{\det\mathcal M_N(t)\in\mathcal O^\times
       \quad\text{对全部单位 }t.}
\tag{22}
$$
每个矩阵条目整，故逆矩阵整。
这里没有声称每个条目或每个余子式都是单位。

## 6. 第二移动中心的真实权

沿用 R381 的六球平均
$$
\chi_N(R;t)=\frac16\sum_{\zeta\in\mu_6}
                         1_{\{R-\zeta t\in p^N\}}.
$$
$\tau_i$ 为型零，故
$\int\chi_N(R;a_jt)\,d\tau_i=\mathcal M_N(t)_{ij}$。
置
$$
\boxed{w_N(t)=\mathcal M_N(t)^{-1}s,\qquad
 V_N(R;t)=\sum_{j=1}^6 w_{N,j}(t)\chi_N(R;a_jt).}
\tag{23}
$$
$w_N$ 整有界，并只依赖 $t\bmod p^N$。
因此 $V_N$ 在 $(R,t)$ 上模 $p^N$ 局部常数，
对 $R$ 的 $\mu_6$ 作用不变。
其支撑包含于三十六个明确的单位球。
这些球两两不交：其尺度六次幂的差都是当前单位。

完整目标系数现在是
$$
\boxed{\int V_N(R;t)\,d\tau_i(R)=s_i\quad(0\le i\le5).}
\tag{24}
$$
各个 $w_{N,j}$ 可以为零或非单位；(22) 不能代替余子式的逐项判断，
本文也不作这种额外断言。

由 (6)、(24)，对任意在当前域上为单位的连续中心 $t=t(Y)$，
以及任意有界原输出测试，逐点给
$$
\boxed{
Y_*(1_{\mathcal B(Y)}V_N(R;t(Y))\,\eta_{DC})
=1_{\mathcal B(Y)}\nu_S.
}
\tag{25}
$$
中心可以依赖原 $Y$。
合法性来自六个实际系数在每个 $Y$ 上准确等于原目标向量 $s$；
不是将 $Y$ 依赖权自由移出一个中央函数。

## 7. 保同一 Y 的双移动组合

令 $W_N(Q;t)$ 为 R381 的真实十二球权，
其中同层 $D/E$ 行列式在 $N\ge49$ 时为单位。
R381 的强式保持任意 $(Y,R)$ 条件：
$$
(\operatorname{pr}_{Y,R})_*
 \bigl(W_N(Q;t(Y,R))\,\mathcal J\bigr)=\eta_{DC},
$$
只要在所用域上中心为单位。
这里 $\mathcal J=(Y,R,Q)_*\eta_3$ 是原同一三输入联合。

取两个中心都等于原 $Y$，并限定 $Y$ 为单位。
因 (21) 同时保证 $N\ge49$，先用 R381，再用 (25)，准确得到
$$
\boxed{
Y_*\left(
 1_{\{Y\ {\rm unit}\}}
 W_N(Q;Y)V_N(R;Y)\,\mathcal J
\right)=\nu_S^\times.
}
\tag{26}
$$
全部未知参考联合在取 Mellin 之前消去，
没有留下需预设为零的 rank-zero 斜率。

(26) 的实际域包含于
$$
\boxed{
Y\text{ unit},\quad
Q-\xi cY\in p^N\ (c=1,2,\ \xi\in\mu_6),\quad
R-\zeta a_jY\in p^N\ (a_j\text{ 如 }(15),\ \zeta\in\mu_6).
}
\tag{27}
$$
这是十二乘三十六，共四百三十二个原坐标球的并域。
每个点上的权是 (16)–(23) 所定义的实际权乘积；
没有将全部系数替成一，也没有断言每支权均非零。
原叶的 $Q\approx Y,R\approx9Y$ 支确实包含在 (27)，
其余分支全部保留。

于是原所有 tame 的整条返回为
$$
\boxed{
\int_{Y\ {\rm unit}}
 W_N(Q;Y)V_N(R;Y)\,
 \omega_p(Y)^\ell\langle Y\rangle^{(p-1)u}\,d\mathcal J
=J_{S,\ell}(u).
}
\tag{28}
$$
原输出没有被缩放，不存在一个可遗漏的输出尺度对数。
其 principal 质量和中央导数准确为原质量和 $J'_S(0)$。
因此原中央零确能传播到这个完全指定的双移动组合，
而非只传播到原点辅助球。

## 8. 单叶、补域及粗层限制

(26)–(28) 是整个有权组合的结论。
它们没有把 R379 的单叶
$$
a\text{ unit},\quad b_1,c\in p^N
\quad\Longleftrightarrow\quad
Y\text{ unit},\ Q-Y\in p^N,\ R-9Y\in p^N
$$
单独赋零。

所有权都是模 $p^N$ 局部常数，因而在这一单叶上可按
$Y\equiv a\bmod p^N$ 读取其真实系数。
但任何同粗层的输出测试都被深 $A$ 的零质量杀掉；
完整中央 log 必须读取更高位。
尤其原 $S$ 的非原点 $p^N$ 小球质量由 R376 为单位，
所以 (26) 不能只靠这个单叶的粗层贡献实现。
其余各支在完整返回中不可免费删除。

本篇新增的实质是一个在同一原核上、整且有明确深度的双移动中心返回。
它消去全部有限参考来源，付清实际目标、权和补域，
为后续分析该**整个组合**的中央余项提供确定对象。
固定曲线的无穷素数主目标尚未由此完成。

## 证书、依赖与同步

- [原精确六来源证书](../scripts/check-jzero-second-moving-center-six-source-rank.js)：
  纯 BigInt 有理运算，执行 (9)–(11)，验证 $\det B$、原 $v=0$ 目标向量、
  $\det J$ 和 $\det G$ 四项准确身份；没有目标素数扫描。
- [R379](R379-original-third-joint-core-unit-collisions-and-three-input-return.md)：固定族、原三输入、$Y/R$ core。
- [R381](R381-original-antisymmetric-joint-twelve-balls-and-complete-reference-elimination.md)：原十二球权、任意 $R$ 强式及同层规范。
- [R376](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)：完整原加法标签、整 frame 和深层单位界。

证书的准确运算已在本会话的 JavaScript BigInt 运行时执行。
环境失联期间仅用根规则允许的小文本 GitHub 接口发表；
没有声称终端运行了脚本，也没有把 API 同步称为 git pull。
根代理负责 core 与 HANDOFF 登记。
