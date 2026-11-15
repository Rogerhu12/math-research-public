# R798 — 原 B0 半周期投影的完整两型与物理 E 深二阶来源

日期：2026-11-15。**状态：以下完整算子、型五两线压缩和型四三维条件来源已证明。**

本篇保持 R734 的同一个 $q=q_N^*$、全部 C 分支、最高三十次权、
原 $\lambda,\kappa,\kappa^N$、全 quarter 来源与真实 E/J 门。
R796 已将 $h_W=\mathcal H_Ye_0$ 支付为全六变量身份。
现在从三个实际二挠点的加法式求出这个**绝对规范的**半周期算子，
并在完整 CM13 纤维中与两种真实第一 Y 型比较。

结论是：B0 的型五部分恰为 R732/R735 的两条原算术线；
其三维 primitive 块整条被杀掉。型四的 B0 部分则为三维，
CM13 特征多项式是 $X^3+\omega$，没有 $\mu_6$ 特征线。
这将物理 E 深的指定 $Z^2/Y^2$ 行压为三个准确的负二矩；
它没有把这些矩认作已知非零，亦没有删除原 W 外部补偿。

## 1. 原规范与真正可交换的条件

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
$\Omega$ 是原 ordinary 周期。本文没有新增射线条件或改变测试。

沿 R796，记
$$
c_B=1-\omega^2,\qquad
B_0=\frac{e_0-\omega h_W}{c_B},\qquad
h_W=\mathcal H_Ye_0,\qquad
\mathcal P_B=\frac{I-\omega\mathcal H_Y}{c_B}.
\tag{2}
$$
因而在完整原来源上 $B_0=\mathcal P_Be_0$。
原 $q,C,H_1,J,E=E_{YW},Z=W-b_YY,t$ 均在 $Y^\perp$，
$b_Y=(20+3\omega)/17$。只依这些真实伙伴的权、有限 p 门和正矩，
按 R796 的正交张量与完整 canonical 相位，均与 $\mathcal H_Y$ 交换。

下面的第一 Y 截面结论只在已经支付的标准 $S_{34}$ 来源上使用。
例如 R719 的完整 cd 来源、R773/R791/R794 的实际 J/帽首矩
均满足这一范围。任意另加混合 Y 的 W-unit、P-unit 或逆 Y 门时，
其原平移仍须转置；不由(2)把这些门自由穿过投影。

## 2. 三个二挠点与绝对半周期公式

先在 $b=1$ 写代数加法式，最后沿同一个 CM homothety 回 $b=17$。
令
$$
y^2=x^3+1,\qquad D x=2y,\qquad D y=3x^2,\qquad
\mathcal E=\{-1,-\omega,-\omega^2\}.
$$
对应 $e\in\mathcal E$ 的非零二挠点 $t_e$ 满足
$$
x(z+t_e)=\frac{e(x+2e)}{x-e},\qquad
y(z+t_e)=-\frac{3e^2y}{(x-e)^2}.
\tag{3}
$$
将原 degree2 canonical lift 写为
$\mathsf T_{t_e}\sigma^2=a_e(x-e)\sigma^2$。
二次平移的原周期符号给 $a_e^2=(3e^2)^{-1}$。
沿 R796 的固定周期代表、半特征及 $\vartheta_{t_e}=i$，
degree34 的系数是 $i a_e^{17}$；
原 $\mu_3$ 循环使三个系数相对于 $(\delta e)^{-17}$
只有同一个符号。该共同号在下方由原 S 绝对定标。
因此 degree34 的三个平移之和，
在偶多项式 $P(x)$ 上具有以下明确的无共同号部分
$$
\mathcal U_4P
=\sum_{e\in\mathcal E}(\delta e)^{-17}(x-e)^{17}
 P\!\left(\frac{e(x+2e)}{x-e}\right).
\tag{4}
$$
对 $yP(x)$ 则为
$$
\mathcal U_5P
=\sum_{e\in\mathcal E}(\delta e)^{-17}(-3e^2)(x-e)^{15}
 P\!\left(\frac{e(x+2e)}{x-e}\right).
\tag{5}
$$
上述比值是完整 canonical 比值；(4)、(5)没有删掉准周期线性项。
(3)给 rational 部分，R796(5)–(7)给其共同绝对相位。

为固定同一平方根规范，保原 S 锚：
$$
S=\sigma^{34}x^2
 \left(X^4-\frac{53}{7}X^3-\frac{12}{7}X^2
                    -\frac{80}{7}X-\frac{128}{7}\right),
\qquad X=x^3,\qquad \mathcal H_Y S=\omega^2S.
\tag{6}
$$
将(4)作用于(6)的多项式，直接得
$\mathcal U_4(S/\sigma^{34})=-\delta\,S/\sigma^{34}$。
故 R796 的同一绝对算子为
$$
\boxed{\quad
\mathcal H_Y=-\frac12(I-\mathcal U),\qquad
\mathcal H_Y^2+\mathcal H_Y+I=0,\qquad
\mathcal P_B^2=\mathcal P_B .
\quad}
\tag{7}
$$
这里偶型用(4)，奇 y 型用(5)。共同号已经由原 S 与原 lift 定标，
不是按一个未归一特征多项式猜选 $\omega$ 或 $\omega^2$。
特别不能把旧二处算子 $M_\omega^{\rm old}$ 的标签直接移给
$\mathcal H_Y$。

## 3. 两个完整有限空间与 b 缩放

在 $b=1$ 取升幂基
$$
\begin{aligned}
V_4&=S_{34}^{(4)}
   =\sigma^{34}\mathbf Q(\omega)[X]_{\le5},
 &E_j^{(4)}&=\sigma^{34}x^{3j}\quad(0\le j\le5),\\
V_5&=S_{34}^{(5)}
   =-\sigma^{34}xy\,\mathbf Q(\omega)[X]_{\le4},
 &E_j^{(5)}&=-\sigma^{34}x^{1+3j}y\quad(0\le j\le4).
\end{aligned}
\tag{8}
$$
这是完整维数6和5，非挑选的子格。原点阶分别为
$34,28,22,16,10,4$ 与 $29,23,17,11,5$；
型由 $\sigma(\zeta z)=\zeta\sigma(z)$、
$x(\zeta z)=\zeta^{-2}x(z)$、$y(\zeta z)=\zeta^{-3}y(z)$ 决定。

在一般 b，使用同总权基
$$
E_{j,b}^{(4)}=b^{5-j}\sigma_b^{34}x_b^{3j},\qquad
E_{j,b}^{(5)}=-b^{4-j}\sigma_b^{34}x_b^{1+3j}y_b.
\tag{9}
$$
若 $\theta^6=b$，则两基分别是 $\theta^{-4}$、$\theta^{-5}$
乘同一 $b=1$ 基在 $\theta z$ 的拉回。
因此下面所有矩阵、绝对号和谱按(9)原样运输到 b=17；
原 $\Omega$ 因子另按实际矩的阶保留，不引入隐藏周期比。

(4)、(5)直接保存(8)两空间。按基(8)写矩阵列为来源像，
令 $P_4,P_5$ 为 $\mathcal P_B$ 的两个矩阵。精确有
$$
P_4=\frac1{13122}
\begin{pmatrix}
6562&8&64&512&4096&32768\\
680&8464&2480&-4352&20480&-389120\\
12376&5642&3394&4256&6400&-792064\\
24310&-2431&1045&9008&-4400&-320320\\
6188&364&50&-140&5738&56056\\
136&-19&-17&-28&154&6200
\end{pmatrix},
\tag{10}
$$
以及
$$
P_5=\frac1{486}
\begin{pmatrix}
240&-16&-64&0&4096\\
-182&106&168&-640&6656\\
-429&99&204&-480&0\\
0&-22&-28&150&-2288\\
7&1&0&-10&272
\end{pmatrix}.
\tag{11}
$$
由(4)、(5)逐项展开即得(10)、(11)；它们是定义明确的全来源算子。
直接乘法给 $P_h^2=P_h$，秩分别为3、2。
所有分母只含2和3。

## 4. CM13 使用整个纤维与同一个原绝对锚

令 $\gamma=4+\omega$、$\bar\gamma=3-\omega$、$N(\gamma)=13$，
沿 R297/R732 定义完整原 CM trace，并规范
$$
\mathcal A_h=\gamma^{-1}\mathcal M_\gamma\big|_{V_h}\quad(h=4,5).
\tag{12}
$$
为使证书可由算法独立重建，实际 division 输入为
$$
q(x)=\gamma\left(x^6+(8+12\omega)x^3+\frac{64+48\omega}{13}\right),
\quad \bar q=\overline q,
$$
$$
\mathcal N(x)=13xq^2-4(x^3+1)(q''q-(q')^2)-6x^2q'q,\qquad
\mathcal D(x)=\gamma^2q^2 .
\tag{13}
$$
令 $f_a$ 为 $\mathcal N-a\mathcal D$ 的 monic 化；
它是完整 degree13 纤维。其商环中计算
$$
r=\bar q/q,\quad
x_b=\overline{\mathcal N}/\overline{\mathcal D},\quad
y_b/y=\frac{\gamma}{\bar\gamma}
 \frac{(\overline{\mathcal N}/\overline{\mathcal D})'}
      {(\mathcal N/\mathcal D)'}.
\tag{14}
$$
对输入 $x^{3j}$ 或 $x^{1+3j}y$，完整 trace 准确是
$$
\bigl[r^{34}x_b^{3j}f_a'\bmod f_a\bigr]_{x^{12}},
\quad\text{或}\quad
\bigl[r^{34}(y_b/y)x_b^{1+3j}f_a'\bmod f_a\bigr]_{x^{12}} .
\tag{15}
$$
每一纤维中的分母和 $f_a'$ 都在商环可逆。
这里含全部13个点、sigma 比的34次及真实 y 比；
不是 projective 交织或抽取一个代表。

$V_4$ 用 $a=2,3,4,5,6,7$ 的六个完整纤维恢复；
其评价矩阵是 $(a^{3j})$，行列式是非零
$\prod_{a<b}(b^3-a^3)$。
$V_5$ 用 $a=2,\ldots,6$ 的五个完整纤维，评价矩阵
$(a^{1+3j})$ 也可逆。型与全纯性已经保证 trace 留在(8)，
故这些纤维唯一决定两个完整算子。
$a=8,9$ 以及型五的 $a=7$ 是额外准确等式，不是确定性所需的新假设。

同一纤维逐个保留 $\mathcal M_\gamma S=-\gamma S$。
这固定(12)与 R732 同一个绝对相位；(7)则固定半周期的绝对相位。
从(13)–(15)的有理运算得到
$$
[\mathcal A_h,\mathcal H_Y]=0,\qquad
\mathcal A_h^{18}=I .
\tag{16}
$$
所有运算在 $\mathbf Q(\omega)$ 完成，不用辅助有限特征的不相容性
推断特征零结论。

## 5. 型五恰保原两算术线，primitive 块被整条消去

R732 的完整结果与本次同纤维重新计算一致：
$$
\chi_{\mathcal A_5}(X)
 =(X+1)(X+\omega^2)(X^3+\omega).
\tag{17}
$$
其中两线按首项 $z^5$ 规范为
$$
\begin{aligned}
D_{-,1}
 &=-\sigma^{34}xy\,(64-104X-156X^2+13X^3+X^4),\\
D_{\omega,1}
 &=-\sigma^{34}xy\,
 \left(\frac{128}{11}+\frac{368}{11}X+\frac{120}{11}X^2
                         -\frac{109}{11}X^3+X^4\right).
\end{aligned}
\tag{18}
$$
(5)在这两个完整多项式上直接给
$$
\mathcal H_Y D_{-,1}=\omega D_{-,1},\qquad
\mathcal H_Y D_{\omega,1}=\omega D_{\omega,1}.
\tag{19}
$$
由 $\operatorname{rank}P_5=2$ 与(16)，
$$
\boxed{\operatorname{im}P_5=K D_{\omega,1}\oplus K D_{-,1},\qquad
P_5\ker(\mathcal A_5^3+\omega I)=0.}
\tag{20}
$$
特别这里的“primitive 块为零”是完整算子结论，不是辅助
$\kappa=u=0$ 的五个坐标恰为零。

亦可把绝对关系写成
$$
\boxed{\mathcal H_Y|_{V_5}=-\omega\mathcal A_5^3,\qquad
P_5=\frac{\mathcal A_5^3+\omega I}{\omega-1}.}
\tag{21}
$$
证明：在两条线 $\mathcal A_5^3=-I$、$\mathcal H_Y=\omega I$；
在其余三维块，Cayley–Hamilton 给
$\mathcal A_5^3=-\omega I$，而(7)、(20)给
$\mathcal H_Y=\omega^2I$。两边在完整直和上相等。
此证明没有把旧有限 torus 的根标签移植过来。

因此 R791/R794 的实际 J 首矩、R773 的帽首矩，
只要按各篇原门作为 B0 的型五来源读取，就准确是(18)两线的组合。
各篇原先保留的三维余块是安全上界，现在可明确置零。
它们的已付两条幅度、$\lambda^N\beta^N$、$\Omega$、
实际深浅条件及原补偿都不改变。
对原帽，先读取 J/Z0/U 伙伴条件的整个 Y 来源，再作 Y-unit 负一观察；
这不声称半周期投影与 Y-unit 指示本身交换。

例如用 R791 的完整系数记
$$
\Omega^{-1}Y_*(t\,1_{J\in p^N}qB_0)
 =\lambda^N\beta^N
   \left(A_{\omega,N}D_{\omega,b}+A_{-,N}D_{-,b}\right).
\tag{22}
$$
两幅度的原单位结论不变，故其同域负一值准确为
$$
\lambda^N\beta^N\Omega
 \left(A_{\omega,N}I_{\omega,p}+A_{-,N}I_{-,p}\right)\ne0 .
\tag{23}
$$
(23)使用 R735/R733 的原同周期算术身份。
它不适用于另换 P 或 W 分母、再附一个混合单位门后的来源。

## 6. 型四只保一个三维 primitive 块

本次完整 type4 trace 给
$$
\chi_{\mathcal A_4}(X)=X^6-X^3+1
                    =(X^3+\omega)(X^3+\omega^2).
\tag{24}
$$
没有 $\mu_6$ 特征线。投影后的精确结果为
$$
\boxed{
\operatorname{rank}P_4=3,\qquad
\chi_{\mathcal A_4|\operatorname{im}P_4}(X)=X^3+\omega .}
\tag{25}
$$
其余三维块的特征多项式是 $X^3+\omega^2$。
由(7)、(16)、(25)和两块的 Cayley–Hamilton，
$$
\boxed{\mathcal H_Y|_{V_4}=-\mathcal A_4^3,\qquad
P_4=\frac{I+\omega\mathcal A_4^3}{1-\omega^2}
   =\frac{\mathcal A_4^3+\omega^2 I}{\omega^2-\omega}.}
\tag{26}
$$
这与(21)的 $\omega$ 因子不同。

一个完整有理基可取(10)的前三列，即
$$
\begin{aligned}
Q_0(X)&=(6562+680X+12376X^2+24310X^3+6188X^4+136X^5)/13122,\\
Q_1(X)&=(8+8464X+5642X^2-2431X^3+364X^4-19X^5)/13122,\\
Q_2(X)&=(64+2480X+3394X^2+1045X^3+50X^4-17X^5)/13122 .
\end{aligned}
\tag{27}
$$
一般 b 的实际来源是
$$
Q_{j,b}^{\theta}(z)=
 \sigma_b(z)^{34}\sum_{a=0}^5 [X^a]Q_j(X)\,b^{5-a}x_b(z)^{3a}.
\tag{28}
$$
(27)三列独立，张满(25)。不能因同为 degree34 就将其认成
(18)的两条型五来源，亦不能因某个正矩非零就给负二矩赋非零。

## 7. 同一个物理 E 深门的完整 Z 二阶来源

令 R719/R796 的原完整 cd 来源为 $\rho_{cd,N}^{YZ}$，并定义
$$
F_{2,N}(z)=\Omega^{-2}
 \int Z^2e^{Yz/\Omega}\,d\rho_{cd,N}^{YZ}.
\tag{29}
$$
这里使用真实二阶矩，不是未乘 $2!$ 的 $Z$ 扰动系数。
由原总角型0与 Z 二次权，$F_{2,N}\in S_{34}^{(4)}$。
其完整坐标可由阶 $4,10,16,22,28,34$ 的六个 unit 三角 jet 恢复；
所有 C 补项和三十次权仍须在(29)中保留。

R796 已付 whole 平面返回
$$
(Y,Z)_*(1_{E\in p^N}q e_0)
 =\lambda^{2N}\rho_{cd,N}^{YZ}.
$$
现在用(2)和真正的 $Z,E,q\perp Y$，得到
$$
\boxed{
\Omega^{-2}Y_*(Z^2\,1_{E\in p^N}qB_0)
 =\lambda^{2N}\nu_{P_4F_{2,N}} .}
\tag{30}
$$
这里用 $\nu_F$ 表示原普通周期下与截面 F 对应的测度。
因此存在完整实际系数 $d_{j,N}$，准确有
$$
P_4F_{2,N}=\sum_{j=0}^2d_{j,N}Q_{j,b}^{\theta}.
\tag{31}
$$
系数由(29)及(10)定义，不因(25)而改选测试。
固定 p,N 后，它们保原 $\lambda,\kappa,u=\kappa^N$、
$\eta$ 以及每个齐次块的原归一。

置
$$
I_{j,-2,p}=\int_{\mathbf Z_p^\times}Y^{-2}\,
                     d\nu_{Q_{j,b}^{\theta}}(Y).
$$
则原指定条件负二行的准确有限式为
$$
\boxed{
\int_{\substack{E\in p^N\\Y\ {\rm unit}}}
                    Z^2Y^{-2}q\,dB_0
 =\lambda^{2N}\Omega^2\sum_{j=0}^2d_{j,N}I_{j,-2,p}.}
\tag{32}
$$
本篇没有证明(31)的实际向量非零，也没有证明(32)非零。
前者需要同 q 的实际二阶读取，后者还需要该完整三维块的
真实负二算术身份或另一条同域非消失证明。
R719 的跨 k=2至5 单位线性组合不能替代(32)。

## 8. 原 W 中央与完整外部仍逐项保持

沿 R796 置
$$
G_N(z,w)=\int_{E\in p^N}
 1_{b_YY+zZ\ {\rm unit}}\langle b_YY+zZ\rangle^{d_pw}q\,dB_0.
$$
在 $z\in p\mathcal O$，单位条件严格等价 Y-unit。
原 zeroth 与 first source 均已为零，故
$$
\partial_wG_N(z,0)
=-\frac{d_pz^2}{2b_Y^2}\lambda^{2N}\Omega^2
       \sum_{j=0}^2d_{j,N}I_{j,-2,p}
 +d_p\sum_{k\ge3}\frac{(-1)^{k+1}z^k}{kb_Y^k}
       \int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^kY^{-k}q\,dB_0 .
\tag{33}
$$
全部高阶项保留。对偶 j≥2，实际 Z 核仍给
$$
\mathscr X_{N,j}(w)+\lambda^jG_N(\kappa^j,w)
 =\lambda^{2N}6\delta J_T(w)/c_B,
\tag{34}
$$
其中 $\mathscr X_{N,j}$ 是同 E 深门下的完整 $Z\notin p^j$ 部分。
只有原 $J'_T(0)=0$ 才使(34)两中央导数相反；
不把(23)、(32)或新的有限谱当成另一个可独立置零的中央。

(21)加强的是已付型五条件来源；(26)确定的是指定型四
二阶来源的完整有限载体。这两种结论都保持原 unit 域、
同 q、相位、质量及全部外部，不越过 R753 的无限点投影边界。

## 9. 精确执行与可重建性

公开仓库运行：

- source commit：`198f22cee3cb170f88766b574596e669daaf76f2`；
- GitHub Actions run：[43738922048](https://github.com/Rogerhu12/math-research-public/actions/runs/43738922048)，job：132887560988；
- 脚本：[check-r798-type-four-halfperiod-and-cm13.py](../scripts/check-r798-type-four-halfperiod-and-cm13.py)；
- 参数：`--workers=4`；依赖：python-flint 0.9.0；
- script SHA256：`f6a1fe72d01b0c804059a06395c5a9c5d78e54d5742a6ca9af957febec9661b3`；
- stdout 6407 bytes；SHA256：`8c750112266267b5640f09d66981634f16da8aa7556909d3e5475b37866b2d1d`；
- 完整结果 PASS，所有 trace 分母可逆、原 S 锚、额外纤维、
  两型保存、投影幂等、与 CM13 交换、限制特征多项式均逐项验证。

输入直接调用原 R732 division/完整 trace **算法**，
其 script SHA256 为
`d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469`。
不读取旧 JSON 输出，不把辅助 finite-field 特征当算子证明，
不持久化可重算 stdout。正文(10)、(11)、(27)是所述算子的
明确数学定义与小型基，完整重建由(3)–(15)及脚本提供。

主要依赖：

- [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)：原 CM13 全 trace 与两条型五线。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：两条原线的全 Schwartz/负一 Katz 身份。
- [R791](R791-original-j-depth-negative-moments-and-two-e-sectors.md)：同 q 的 J 首矩两幅度及负一独立。
- [R794](R794-original-e-j-intersection-and-native-w-annuli.md)：真实 E/J 交域、原两输出与全部补偿。
- [R796](R796-whole-halfperiod-and-physical-e-first-moment-cancellation.md)：全六变量半周期相位、整个 (Y,Z) 返回与 first-source 消去。
