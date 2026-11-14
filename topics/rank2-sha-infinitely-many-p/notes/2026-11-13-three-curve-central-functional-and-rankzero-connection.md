# 三曲线的完整中央泛函、新 E8 参考与单位协变导数

日期：2026-11-13。状态：本文的 E8 参考截面、缩放公式、明确非零 CM 对数方向、十七处投影及连接公式均已证明。尚未把这个非零方向由 E17、E34、E136 三个原中央导数回收；不据此宣布无穷素数结论。

本文接续 [R239](../results/R239-third-rank2-curve-and-original-sixteen-coset-transport.md)，保留同一个 Yang 有限向量和 R50/R54 的实际算术比较。以下在
$$
E_0:y^2=x^3-x,\qquad dz=dx/(2y),\qquad
x'=2y,\quad y'=3x^2-1
$$
上计算；$\sigma(z)\sim z$、$\vartheta=\sqrt{x}\sigma\sim1$。所有平方根均取原点所列的形式支。

## 1. 一个准确的 E8 秩零参考

定义
$$
S_8^{\rm b}(z)=-y(z)\vartheta(z)\sigma(z)^3
             =\sigma(z)^4x(z)^2\sqrt{1-x(z)^{-2}},
\qquad S_8^{\rm b}(0)=1.
\tag{1}
$$
它的自然 theta 次数为四，带有固定二挠线丛 twist；不把它与旧
$S_0=(x^2+1)\sigma^4$ 的线丛未经识别地相加。
二倍拉回则是普通 degree-16 截面：
$$
\boxed{
S_8(z):=S_8^{\rm b}(2z)
=\sigma(z)^{16}\bigl(x(z)^8-4x(z)^6-10x(z)^4-4x(z)^2+1\bigr).}
\tag{2}
$$

**(2) 的直接证明。** sigma duplication 与椭圆加法公式给
$$
\sigma(2z)=-2y\sigma(z)^4,\quad
\vartheta(2z)=(x^2+1)\sigma(z)^4,
\quad
y(2z)=\frac{x^6-5x^4-5x^2+1}{8y^3}.
$$
代入 (1)，即得 (2)。这些式子的符号也由
$y(z)\sim-z^{-3}$、$\sigma(2z)\sim2z$ 固定。

### 1.1 与 R239 的原十六余类向量一致

令 $w=4z$，并沿用 R239 的
$$
X=x(w/2),\quad U=X^2,\quad R^2=1-X^2,\quad R\sim iX.
$$
则
$$
\boxed{
\frac{S_8(w/4)}{\vartheta(w)}=-i\frac{XR}{X^2+1}.}
\tag{3}
$$
因为 $R=-iY/\sqrt X$，右端就是
$-Y\sqrt X/(X^2+1)$，与 (1) 和 theta duplication 相符。
由 R239 对真实 $[1+i]$ 覆盖的计算，(3) 在
$w\mapsto w+2\Omega_0,w+2i\Omega_0$ 下均变号，在
$w\mapsto iw$ 下不变。

这三个性质准确识别有限向量，而不只识别一个同维的空间。
在 R239 的十六维模型中，设 $X_{16}$ 是循环移位、
$Z_{16}$ 是乘 $\zeta_{16}^a$、$I$ 是归一 Fourier 矩阵。
同时满足 $X_{16}^8v=Z_{16}^8v=-v$ 和 $I^2v=v$ 的向量形为
$$
(0,a,0,b,0,-b,0,-a,0,-a,0,-b,0,b,0,a).
$$
在 $(a,b)$ 上，$I$ 的矩阵为
$$
\begin{pmatrix}
\cos(\pi/8)&\sin(\pi/8)\\
\sin(\pi/8)&-\cos(\pi/8)
\end{pmatrix}.
$$
其 $+1$ 特征线准确满足 $b/a=\tan(\pi/16)$。因此 (2) 对应的
正是 R239 的实际新 dyadic 向量 $v$，只差一个共同常数；以
$S_8(0)=1$ 固定归一。十七处不放 primitive 特征时，这就是
$E_8:y^2=x^3-8x$ 的原 theta 行。这里不是先猜多项式再用有限
数值样本认同它。

Yang 的平方公式遂在权零给 $L(E_8,1)\ne0$：原向量非零、
归一截面的中心值为一，局部常数均非零。其代数归一中心值是一个
固定非零数，所以只需删去固定有限个素数。

### 1.2 不依赖解析秩表的完整秩零证明

$E_8$ 与 $E_{-2}:y^2=x^3+2x$ 是标准二同源的一对。
对后者，$y^2=x(x^2+2)$ 迫非零有理点的 $x>0$，故二下降像
仅可能是正平方类 $1,2$，且 $(0,0)$ 给类 $2$。
因此 $\alpha(E_{-2})=\{1,2\}$。

对 $E_8$，像仅可能在 $\{1,-1,2,-2\}$，已含 $1,-2$。
类 $2$ 的 primitive 覆盖为
$$
N^2=2A^4-4B^4,\qquad (A,B)=1.
$$
若 $A$ 奇，则右侧模 $16$ 为 $2$ 或 $14$；若 $A$ 偶，
则 $B$ 奇，右侧为 $12$。都不是平方。群性又排除类 $-1$，
所以 $\alpha(E_8)=\{1,-2\}$。标准二同源下降等式给
$$
2^{\operatorname{rank}E_8(\mathbb Q)}
=\frac{\#\alpha(E_8)\,\#\alpha(E_{-2})}{4}=1.
$$
这与上一节的真 theta 中心非零互相独立；不以代数秩零倒推解析秩零。

## 2. 原 E136 相对于新参考的有理表达

在 R239 的原归一中
$$
D_{136}(w)=\vartheta(w)^{17}
 \frac{XR\,P_{15}(U)}{(U+1)^{17}}.
$$
直接使用 (3) 得
$$
\boxed{
\frac{D_{136}(w)}{S_8(w/4)^{17}}
       =\frac{iP_{15}(U)}{U^8(U-1)^8}.}
\tag{4}
$$
因此二次覆盖因子在**这个实际秩零参考**中准确消去。
若把截面与变量归一为
$$
A_{136}(z)=-y(z)\vartheta(z)\sigma(z)^{67}P(U),\quad U=x(z)^2,
$$
则同一式成为
$$
\boxed{\frac{A_{136}(z)}{S_8^{\rm b}(z)^{17}}
       =\frac{P(U)}{U^8(U-1)^8}.}
\tag{5}
$$
这里的 $P$ 包括从 R239 的固定相位和尺度转换；不能同时保留原
$P_{15}$ 却删除 (4) 的 $i$。

还有一个很短的准确连接式。对旧秩零参考
$S_0=(x^2+1)\sigma^4$，有
$$
r_8:=\frac{S_8^{\rm b}}{S_0}
       =-\frac{y\sqrt x}{x^2+1},\quad
r_8^2=\frac{U(U-1)}{(U+1)^2},\quad r_8(0)=1,
$$
以及
$$
\boxed{\partial_z\log r_8
       =\frac{2(3x^2-1)}{y(x^2+1)}.}
\tag{6}
$$
证明是代入 $x'=2y,y'=3x^2-1,y^2=x(x^2-1)$ 后合并三个分数。
于是两个十七次 frame 的协变微分差为
$$
\nabla_8=\nabla_0-
  \frac{34(3x^2-1)}{y(x^2+1)},\quad
\nabla_j:=\partial_z-17\partial_z\log S_j.
\tag{7}
$$
这是原截面的有理微分连接。它不是下节中央泛函对乘积的 Leibniz
法则；下降阶乘变换仍然不是乘法同态。

## 3. 任意 CM 缩放的完整中央公式

固定惰性 $p\ge7$，$d=p+1$，令 $c_0$ 为 R54 的临界 sigma
对数系数，$v_p(c_0)=-1$。对自然次数 $N$ 的截面，使用
$$
\mathcal J_{Nc_0}(F;u)=
\sum_{h\ge0}(Nc_0)^{-h}(u)_h
 [z^{dh}]\bigl(e^{-Nc_0z^d}F(z)\bigr).
\tag{8}
$$
下文排除 $p\mid N$ 及固定代数系数的有限坏集合。

令 $\beta\in\mathbb Z[i]$、$n=\beta\bar\beta$、$p\nmid n$，并置
$$
U_{\beta,p}=\frac{\beta^{p+1}}{n}\in1+p\mathbb Z_{p^2}.
$$
只要原截面满足 R54 的余项估计，准确有
$$
\boxed{
\mathcal J_{nNc_0}(F(\beta z);u)
    =U_{\beta,p}^{u}\mathcal J_{Nc_0}(F;u).}
\tag{9}
$$

**收敛与等式。** 在非负整数 $k$ 处，(8) 的有限卷积给
$\mathcal J_c(F;k)=k!c^{-k}[z^{dk}]F$，所以 (9) 成立。
令 $G=e^{-Nc_0z^d}F$。拉回后的余项为
$$
e^{-nNc_0z^d}F(\beta z)
=\exp\bigl(Nc_0(\beta^d-n)z^d\bigr)G(\beta z).
$$
其额外指数的系数整，因为 $\beta^d-n\in p\mathbb Z_{p^2}$。
在 $R=p^{-1/(2p)}$ 上，该项处于指数收敛圆盘，且 $|\beta|_p=1$。
故两边都是同一 $u$ 圆盘上的解析函数；非负整数中有序列
$k=p^a\to0$，解析唯一性给出完整等式。这里没有仅凭形式插值
认定一个未收敛级数相等。

令 $m(F)=F(0)$、$j_c(F)=\partial_u\mathcal J_c(F;0)$。
求导得到
$$
\boxed{j_{nNc_0}(F(\beta z))
       =j_{Nc_0}(F)+m(F)\log_p U_{\beta,p}.}
\tag{10}
$$
对有理整数 $k$，$n=k^2$，额外项就是
$(p-1)m(F)\log_pk$。所以三个原 rank-two 行的导数在 R239 的
二倍、四倍共同尺度间保持不变，而质量为一的参考行必须保留此项。

## 4. 新参考确实消去一个共同未知导数

记
$$
J_{8,p}(u)=\mathcal J_{4c_0}(S_8^{\rm b};u).
$$
它满足
$$
J_{8,p}\in1+p\mathbb Z_p\langle u\rangle.
\tag{11}
$$
证明与 R54 的秩零估计相同，但可在这里直接核前因子：设
$W=z^2x$，则
$$
S_8^{\rm b}=\bigl(\sigma/z\bigr)^4
              W^2\sqrt{1-z^4/W^2}.
$$
在 R54 的圆盘上，$W$ 为常数项一的单位、余下平方根为整解析
单位；去掉 $e^{4c_0z^d}$ 后范数至多一，常数项一。
R54 的下降阶乘系数估计即给 (11)。

因此对任一同一目标尺度的实际行 $F$，可以使用
$$
\widehat J_p(F;u)=\frac{\mathcal J_c(F;u)}{J_{8,p}(u)},\qquad
\widehat j_p(F)=j_c(F)-m(F)J_{8,p}'(0).
\tag{12}
$$
这里是已经收敛的解析函数除以一个已证单位。
对三个零质量 rank-two 行，$\widehat j_p(F)=j_c(F)$。
对两个由同一个 E8 参考产生的 CM 行，(9) 给出的则是**准确纯单位**：
$$
\widehat J_p(S_8^{\rm b}(\beta z);u)=U_{\beta,p}^{u}.
\tag{13}
$$
所以这个共同参考的未知导数确实已经消掉，剩下的是已知单位的对数。

这不同时消去 R231 中不同 primitive 曲线的秩零参考。
例如中心归一为一的另一个参考 $S$ 留下
$j_c(S)-J_{8,p}'(0)$，再加上 (10) 中已知的尺度项。
不同参考能否共用 (13)，须先证明它们是同一个截面的真实 CM 缩放；
“都为秩零”或“都给 Iwasawa 单位”不能代替这个等式。

还须区别 (4)–(5) 与 (12)：
$$
\mathcal J(A/S^{17}),\quad
\mathcal J(A)/\mathcal J(S)^{17},\quad
\mathcal J(A)/\mathcal J(S)
$$
不是相同构造。本文没有把它们相等作为输入。

## 5. 已知非零方向及其真实十七处位置

取 $\beta=4-i$、$\bar\beta=4+i$，范数为十七。两个截面
$S_8^{\rm b}(\beta z),S_8^{\rm b}(\bar\beta z)$ 都是 degree-68
的同一固定二挠 twist 线丛的截面，与 $A_{136}$ 的尺度相符。
(9) 立即给
$$
\boxed{
\partial_u\mathcal J_{68c_0}
 \bigl(S_8^{\rm b}(\beta z)-S_8^{\rm b}(\bar\beta z);0\bigr)
 =(p+1)\log_p\frac{4-i}{4+i}\ne0.}
\tag{14}
$$
未知的 $J_{8,p}'(0)$ 因两项质量相等而准确抵消。
右端非零的理由也无猜想：$(4-i)/(4+i)$ 是每个 $p\ne17$
处的单位，但不是根单位；其在 $\mathbb Q_{p^2}$ 中若对数为零，
就属于该局部域的有限根单位群，进而这个代数数本身为根单位，矛盾。

这给一个实际非零中央方向，但它仍位于十七处的 **trivial 二维块**。
在 split Schrödinger 模型中，两个 CM 方向由十七处的两个非紧
格方向产生；紧单位群的作用保持它们。等价地，在 R231 的有限
十七维模型里，它们由 $\delta_0$ 与非零元素上的常数向量张成。
这两个向量都对 $\mathbb F_{17}^{\times}$ 的乘法作用不变。

这里的乘法作用 $\rho$ 是 R231 同一有限模型中已去掉共同
splitting 因子的作用；不把它与重新选取 ramified splitting
character 后的“平凡”等型标签混用。对任意非平凡 tame 角色
$\chi$，其准确幂等投影为
$$
e_\chi=\frac1{16}\sum_{a\in\mathbb F_{17}^{\times}}
                       \chi(a)^{-1}\rho(a).
$$
角色正交直接给
$$
\boxed{e_\chi\delta_0=e_\chi\mathbf1_{\mathbb F_{17}^{\times}}=0.}
\tag{15}
$$
尤其 (14) 的方向不能不经比较就认作 E136 的 primitive $\lambda$
行，也不能认作 E34 的 $\lambda^2$ 行。二处可能出现的固定标量
相位不改变 (15)；它们必须在实际交织系数中保留，不能据此删除
十七处的投影。

### 5.1 范数五与范数二的准确区别

对 $\pi=2+i$，同样有
$$
\partial_u\mathcal J_{20c_0}
\bigl(S_8^{\rm b}(\pi z)-S_8^{\rm b}(\bar\pi z);0\bigr)
=(p+1)\log_p\frac{2+i}{2-i}\ne0.
\tag{16}
$$
但这里的次数是二十。若乘 $(S_8^{\rm b})^{12}$ 将次数升到六十八，
(16) 不再原样成立；必须计算完整乘积的中央泛函。
若改用 R231 式真正的 $[\pi]_*[\bar\pi]^*$ 同线丛迹，仍须将
中央行转置到这个算子，不能用 $\mathcal J(TF)=T\mathcal J(F)$。

对 $\alpha=1+i$，则
$$
U_{\alpha,p}/U_{\bar\alpha,p}
 =\left(\frac{1+i}{1-i}\right)^{p+1}=i^{p+1}=1.
$$
所以产生 R239 二次覆盖的范数二 CM 方向本身没有非零反对称
对数。其共同对数是 $(p-1)\log_p2/2$，仍须按质量乘回 (10)。

## 6. 真正允许的参考消元和交织闭环

若已证明一条完整解析关系
$$
\sum_j a_j(u)\mathcal J(F_j;u)=H(u),
$$
那么它的中央一阶关系准确是
$$
\sum_j a_j(0)j(F_j)
 =H'(0)-\sum_j a_j'(0)m(F_j).
\tag{17}
$$
将某一行改为 $\widetilde J_j=U_jJ_j$、$U_j(0)=1$，必须同时把
系数改成 $a_j/U_j$。此时
$\widetilde j_j=j_j+U_j'(0)m(F_j)$，新增项恰由 (17) 右侧的
系数导数抵消。因此任意选择一个单位把秩零行的首导数归零，并没有
消除其数学内容；内容会进入交织系数的一阶项。

R231 的 $Q_{0,+}Q_{+,0}=\Pi_0$、$Q_{+,0}Q_{0,+}=\Pi_+$
是准确的有限源恒等式。应用中央泛函后得到的是
$j\circ Q_{0,+}\circ Q_{+,0}$，不是两个独立标量乘子的乘积。
要由三条 rank-two 导数回收 (14) 或 (16)，所需的正向接口是一个
在原中央行上已经验证的关系：经过完整 frame、有限角色投影、
单位一阶项及移权项补偿后，非零 CM 行落入这三个零质量行所控制
的空间。当前仅有有限向量运输和来源空间的独立性，还没有这条
中央行关系。

## 7. 新参考的双极余类有一个固定二挠除子对数

这一段可用于新 frame 的协变二阶分解，不需要先知道其多项式
系数。令 $F=(S_8^{\rm b})^{17}$、
$\nabla_8=\partial-F'/F$，以及
$$
r(z)=\frac{x(z)-1}{x(z)+1},\qquad r(0)=1.
$$
其除子为
$\operatorname{div}(r)=2(T_+)-2(T_-)$，其中
$T_+=(1,0),T_-=(-1,0)$。直接求导给
$$
(\log r)'=\frac{4x}{y},\qquad
(\log r)''=-4-\frac8{x^2-1}.
$$
由于 $\nabla_8(Fg)=Fg'$，得到准确恒等式
$$
\boxed{\frac{F}{U-1}
       =-\frac18\nabla_8^2(F\log r)-\frac12F.}
\tag{18}
$$
$\log r$ 取原点常数项零的形式原函数；它有固定对数分歧，
不能改称有理函数。若一个实际分解出现
$$
A=\nabla_8^2(Fq)+\beta F+\gamma F/(U-1),
$$
则 (18) 将它准确改写成
$$
A=\nabla_8^2\bigl(F(q-\gamma\log r/8)\bigr)
     +(\beta-\gamma/2)F.
\tag{19}
$$
这定位了额外余类所对应的具体对数扩张，并没有使其中央积分
自动成为某个已知非零代数单位的对数；这种算术比较仍需证明。

## 8. 已发表输入的适用范围

R239 的新 dyadic 向量符合 Yang 1997 Theorem 2.6 的局部—全球平方
公式：ramified nonsplit 处用 Corollary 2.4 的实际一维特征线，split
十七处用 Corollaries 2.10、2.14 与 (2.28)。这些命题不限定为旧
四余类模型。题名是 *Theta liftings and Hecke L-functions*，
J. reine angew. Math. 485 (1997), 25–53。
[作者原文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。

BKO 2021 Theorems 6.1–6.2 对 $K=\mathbb Q(i)$、好惰性 $p\ge5$
适用；$h_K=1$，正根数和平凡特征给不带额外 $+1$ 的 Selmer
余秩上界。BKO 2024 Corollary 4.11(i) 的证明明确将单位中心值对应
的 Rubin 函数认作 $\Lambda^\times$。因此新 E8 参考在固定有限
例外之外可以取代 E0 的原始局部基；两参考的比是整解析单位，不
改变 E136 的中央零阶。新导子只带 $2,17$ 的差异、两份阶乘和
惰性 Euler 因子仍如 R50 准确抵消。

- BKO 2021，[发表全文](https://par.nsf.gov/servlets/purl/10336626)，
  Annals 194, 943–966，尤其 §6。
- BKO 2024，[发表全文](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/padic-lfunctions-and-rational-points-on-cm-elliptic-curves-at-inert-primes/7F847A218FE1F6DBB390CC0279089C34)，
  JIMJ 23, 1417–1460，Definition 3.13、Corollary 4.11(i) 的证明。

完整函数方程也不另行消掉秩零反圆导数。设自对偶 Galois 中心
$\phi^\tau=\epsilon\phi^{-1}$、反圆角色 $\rho^\tau=\rho^{-1}$。
同 CM type 的 Katz 变换为
$$
\mathcal D(\xi)=\epsilon(\xi^\tau)^{-1},\qquad
\mathcal D(\phi\rho^u)=\phi\rho^u.
$$
它逐点固定反圆线，反射的是圆分变量；不能据此令任一
$J'(0)$ 为零或取得固定的对数值。这个角色变换可在
Castella, *Tamagawa number conjecture for CM modular forms and
Rankin–Selberg convolutions*, Proc. LMS 131 (2025), e70089，
Theorem 2.2.1、Definition 2.2.2 中核对，原文追溯到 de Shalit
Theorem II.6.4。[作者原文](https://web.math.ucsb.edu/~castella/Katz.pdf)。
此处只用其角色公式，不把普通 Katz 定理当作惰性插值定理。

