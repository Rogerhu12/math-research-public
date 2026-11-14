# R528 — 十四度三轨道的普适正测试、完整三观察联合与真实混合差

日期：2026-11-14。**状态：已证明。** 本篇在原共同伴随空间中给出
三个完整十四度轴。一个显示的正 $6/12/18$ 次多项式对其余五输出
实现全部评价恒等式；对三个实际单位测试取三阶平均，严格保持
原 $(Y,W,W')$ 的整个联合，并被原几何和已付观察轴核心保留。

同一测试在原五深一单位网格上给非零第五阶。与 R522 的六次测试
相比，这次 $Y$ 与归一 $W$ 的第五阶不再成同一比例；
局部质量也不再为零。本篇保全部 log 矩和真实单位分支。
两个测试之差是整个三观察推前的零来源，因而给一条真正同域的
混合零行；其原隐藏子管及补域均明确保留。

## 1. 原三个整共同伴随轴

保 R522 的全部原规范、六输入
$\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t$、
$\rho=-\nu_\sigma^{\otimes6}/84$，
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
\tag{1}
$$
三个观察 $Y,W,W'$ 及 $W_2=W\mathcal T^2$ 都是 R522 的同一原行。
取
$$
\boxed{
D_0=(-\omega,\omega^2,1-\omega,\omega^2,1,2+3\omega),
}
$$
$$
\boxed{
D_1=D_0+(1+\omega)H_0,\qquad D_2=D_0+H_0,
\qquad H_0=(1,0,-1,1,0,0).
}
\tag{2}
$$
即
$$
D_1=(1,\omega^2,-2\omega,0,1,2+3\omega),\qquad
D_2=(1-\omega,\omega^2,-\omega,-\omega,1,2+3\omega).
$$
完整原六输入计算给
$$
\boxed{
N(D_j)=14,\qquad D_j\perp Y,W,W',W_2,\qquad
D_j\mathcal T=D_{j+1\ ({\rm mod}\ 3)}.
}
\tag{3}
$$
三个行都为 CM 整行。模二的非零系数数目分别为六、四、六，
所以原奇 sigma 半特征的乘积均为标准偶半特征。
每一行与其完整五维正交补的 Gaussian 交叉全零，故原联合在
该方向确属整个标准 $\mathcal S_{14}$ 与完整其余系数格的张量。
这也适用于由 $W,W'/2$ 操作构造的原四态，因为它们与 (3) 正交。

## 2. 十四度全空间的正次数评价恒等式

$\mathcal S_{14}$ 的 principal 子空间准确为
$$
\langle \sigma^{14}x_\wp,\ \sigma^{14}x_\wp^4,\
                                      \sigma^{14}x_\wp^7\rangle .
\tag{4}
$$
其他角型在零点的值及所有 $6k$ 阶导数都为零。
在 $b=1$ 时，(4) 的第 $6,12,18$ 阶导数组成完整矩阵
$$
\boxed{
M=\begin{pmatrix}
0&479001600&-487799901388800\\
720&-241781760&593428965949440\\
-672&179601408&-539434959372288
\end{pmatrix},
}
\tag{5}
$$
行按 (4)，列按 $6,12,18$。
其行列式是
$11200205567344074817536000\ne0$。

令
$$
\boxed{
c_1=\frac{1453483}{97883968},\qquad
c_2=-\frac{17}{542126592},\qquad
c_3=-\frac1{32475551367168}.
}
\tag{6}
$$
准确有 $M(c_1,c_2,c_3)^t=(0,0,1)^t$。
因 (4) 的首阶依次为十二、六、零，而其全部第一角型空间只有
三维，这给整个函数空间的评价式。
一般 $b$ 的齐次缩放遂得，对每个 $F\in\mathcal S_{14}$，
$$
\boxed{F(0)=\sum_{k=1}^3c_kb^{-k}F^{(6k)}(0).}
\tag{7}
$$
所以
$$
q_{14,b}(t)=\sum_{k=1}^3c_kb^{-k}t^{6k}
\tag{8}
$$
对实际输出 $D_j/\Omega$ 是其余五输出上的普适无常数正测试。

矩阵 (5) 由原 sigma/Weierstrass 递推精确生成。具体地，
$x=z^{-2}B(z^6)$、$\sigma=zA(z^6)$，只需到三阶的
$A^{14}B^r$，$r=1,4,7$。这是有限三维空间中的全函数证明，
没有把未知函数的有限 jet 相合当作全局身份。
(6) 的分母只含 $2,3,7,13$，在当前普通 ray 都是单位。

## 3. 完整十四度核心的正确绝对号

现有 ray 模 $28$ 可取
$\pi_0\equiv23+14\omega$，准确有
$$
\boxed{g_\pi=\pi_0/\bar\pi_0\equiv15=1+14\pmod{28}.}
\tag{9}
$$
在标准偶 degree14 的两个 Heisenberg 生成元上，它与恒等
的完整 lift 相同：两个生成方向均只加同向整周期，交替项为零，
偶半特征的整周期号为正。因此归一核心是 scalar。

绝对锚取真正的 $\Theta(\gamma z)\in\mathcal S_{14}$。
R471(12)–(13) 已明确支付原
$$
\nu_\Theta|_p=\beta[\kappa]_*\nu_\Theta,
\qquad\beta=-\lambda.
$$
固定普通单位 $\gamma$ 的拉回与该核心交换。
所以 (9) 的整个 scalar 准确为
$$
\boxed{K_{14}=-I,\qquad
\nu|_{D_j\in p^n}=\beta^n[\kappa^n,I_5]_*\nu.}
\tag{10}
$$
特别本篇的锚号是 $-\lambda$，不是 $+\lambda$。

逐个正矩减去 (10) 的深部分，定义
$$
\boxed{
q_{14,p}^{\times}(t)=
\sum_{k=1}^3
\frac{c_kb^{-k}}{1+\lambda\kappa^{6k}}t^{6k}.
}
\tag{11}
$$
所有新增分母模 $p$ 为一。
(7)、(10) 准确给
$$
\boxed{
(\text{忘 }D_j)_*
 \{{\bf1}_{D_j\ {\rm unit}}\,
            q_{14,p}^{\times}(D_j/\Omega)\rho\}
=(\text{忘 }D_j)_*\rho.
}
\tag{12}
$$
这是完整其余五输出的测度身份。

## 4. 三阶平均保持整个三观察联合

置一个明确的实际连续测试
$$
\boxed{
\mathfrak q_{14,p}(\xi)=
\frac13\sum_{j=0}^2{\bf1}_{D_j(\xi)\ {\rm unit}}\,
                      q_{14,p}^{\times}(D_j(\xi)/\Omega).
}
\tag{13}
$$
这是三个单位域的加权和，**不是**将三个单位指示函数相乘。
由 (3)，$\mathfrak q_{14,p}\circ\mathcal T=\mathfrak q_{14,p}$。
旧 $W$ 核和任一已经支付的观察轴收缩，只要方向在
$\operatorname{span}(Y,W,W')$ 中，也逐点固定这个测试。

记 $\pi_3=(Y,W,W')$。每个 (12) 都能继续推到这三个真正输出，
因而
$$
\boxed{(\pi_3)_*(\mathfrak q_{14,p}\rho)=(\pi_3)_*\rho.}
\tag{14}
$$
允许任意完整 $F(Y,W,W')$，包括三个观察的单位条件、混合管、
乘积 Mellin 权以及其实际导数。这里比三个单独边际更强。

由原边际规范，(14) 特别给
$$
\boxed{
\begin{aligned}
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}\mathfrak q_{14,p}\,d\rho&=J_S(u),\\
\int_{W\ {\rm unit}}\langle W\rangle^{du}\mathfrak q_{14,p}\,d\rho&=6\delta J_T(u),\\
\int_{W_2\ {\rm unit}}\langle W_2\rangle^{du}\mathfrak q_{14,p}\,d\rho
 &=-6\delta\omega^2J_T(u).
\end{aligned}}
\tag{15}
$$
$W'$ 的完整第一来源仍为零。
这些全来源身份也保原四态及第一 $Y/W$ 的实际 CM 算术投影，
因为 (3) 保相同的 degree14 方向；没有新增未经识别的中央。

## 5. 原网格内只有两个实际单位分支

保原独立域
$$
\mathcal D_n=\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\
x\ {\rm unit}\},\qquad n\ge1.
\tag{16}
$$
这里 $Y,W,W_2$ 都为单位。三个 $D_j$ 的自由 $x$ 系数准确是
$$
t_0=\omega^2,\qquad t_1=0,\qquad t_2=-\omega.
\tag{17}
$$
因此在整个 (16) 上，$D_0,D_2$ 为单位，而
$D_1\in p^n$。第一个和第三个分支保留，第二个单位分支严格为零；
不能把三项都当作无指示多项式。

将五个深输入共同乘 $T\in p\mathcal O$。对
$L\in\{Y,W,W_2\}$ 写
$$
L(T)=a_Lx+TZ_L,\qquad
a_Y=a_W=\bar\gamma,\quad a_{W_2}=3+2\omega=-\omega^2\bar\gamma.
$$
令 $\boldsymbol l_j$ 为 $D_j$ 的五个深输入系数，
$D_j(T)=t_jx+T L_j$。
定义完整解析函数
$$
\mathcal A_L(T)=\frac d3\int_{x\ {\rm unit}}\int
\log\langle a_Lx+TZ_L\rangle
\sum_{j\in\{0,2\}}
q_{14,p}^{\times}((t_jx+TL_j)/\Omega)\,d\rho.
\tag{18}
$$
这里积分内的 $\rho$ 仍含原 $-1/84$。
质量函数 $\mathcal M(T)$ 是 (18) 去掉 $d\log$ 后的同一积分。
原五个 sigma 的真实同时深核心给
$$
\boxed{
C_{L,n}=\beta^{5n}\mathcal A_L(\kappa^n),\qquad
M_n=\beta^{5n}\mathcal M(\kappa^n).
}
\tag{19}
$$

## 6. 全部第五阶：log 与质量照原样保留

对每个活跃分支 $j=0,2$、观察 $L$，定义完整五重混合系数
$$
C_r^{j,L}=r!(5-r)!\!
\sum_{\substack{I\subset\{1,\ldots,5\}\\|I|=r}}
 \prod_{i\in I}z_{L,i}\prod_{i\notin I}l_{j,i}.
$$
对 $m=6k$ 置
$$
A_{k,j,L}=
\sum_{r=1}^5\frac{(-1)^{r-1}}{r a_L^r}
 \binom m{5-r}t_j^{m-5+r}C_r^{j,L},
$$
$$
B_{k,j}=\binom m5t_j^{m-5}C_0^{j,L}.
\tag{20}
$$
$B_{k,j}$ 与观察 $L$ 无关，因为 $C_0$ 不使用 $z_L$。
全部 $32$ 个混合子集及 (20) 的各项均在证书精确保存。

写原 sigma 单位矩为
$$
I_s=\int_{\mathcal O^\times}x^s\,d\nu_\sigma,\qquad
I_{s,\log}=\int_{\mathcal O^\times}x^s\log\langle x\rangle\,d\nu_\sigma.
$$
则准确的完整第五阶为
$$
\boxed{
[T^5]\mathcal A_L
=-\frac d{252}
\sum_{\substack{j=0,2\\1\le k\le3}}
\frac{c_kb^{-k}\Omega^{5-6k}}{1+\lambda\kappa^{6k}}
\left\{A_{k,j,L}I_{6k-5}
+B_{k,j}[I_{6k-5,\log}+\log\langle a_L\rangle I_{6k-5}]\right\}.
}
\tag{21}
$$
这里确实存在 $I_{1,\log},I_{7,\log},I_{13,\log}$。
不能套用 R522 对另一个测试的局部质量零。

原正矩是
$$
I_{6k-5}=(1+\lambda\kappa^{6k-5})(6k-5)!
                         b^{k-1}a_{k-1}\Omega^{6k-5},
$$
$$
(a_0,a_1,a_2)=\left(1,\frac1{210},-\frac1{1801800}\right).
\tag{22}
$$
所有 log 因子属于 $p\mathcal O$。完整展开 (21) 后，才得到
$$
[T^5]\mathcal A_L\equiv(d/b)\alpha_L\pmod p,
\tag{23}
$$
其中三个固定代数常数共用分母
$D_0^{\rm num}=473799124850688$：
$$
\boxed{
\begin{aligned}
\alpha_Y&=\frac{74355527994491+65711835746455\omega}{D_0^{\rm num}},\\
\alpha_W&=\frac{125219651565691+9781908554473\omega}{D_0^{\rm num}},\\
\alpha_{W_2}&=\frac{44295401566533-54736801252913\omega}{D_0^{\rm num}}.
\end{aligned}}
\tag{24}
$$
这些常数与 $p,\lambda,\kappa,n$ 无关。

本次原 S/T 归一差为
$$
\boxed{
\Delta_{14}=\frac{\alpha_W}{6\delta}-\alpha_Y
=\frac{-206293619765369-203352919716157\omega}
       {1218340606758912},
}
$$
$$
\boxed{
N\Delta_{14}
=\frac{5825219716074126970934359}{206074390403675391994626048}\ne0.
}
\tag{25}
$$
它与 R522 的同一归一差在第五阶为零的结果不同。

### 6.1 完整局部质量

质量的第五阶准确由 (21) 只保 $B_{k,j}I_{6k-5}$ 得到，
且没有因子 $d$。其固定首常数为
$$
\boxed{
[T^5]\mathcal M\equiv b^{-1}m_5\pmod p,\qquad
m_5=\frac{173252865(1-2\omega)}{1370375552},
}
$$
$$
Nm_5=\frac{30016555230708225}{268275593359900672}\ne0.
\tag{26}
$$
因此局部质量不为零。

更完整地，质量是三个实际幂的有限多项式
$$
\boxed{
\mathcal M(T)=\frac1b
 \sum_{r\in\{5,11,17\}}\sum_{\substack{1\le k\le3\\6k\ge r+1}}
 m_{r,k}
 \frac{1+\lambda\kappa^{6k-r}}{1+\lambda\kappa^{6k}}\,T^r.
}
\tag{27}
$$
所有固定 $m_{r,k}\in K$ 在附 JSON 精确显示。
其有限规则如下：若
$\prod_{i=1}^5\sigma_b(l_{j,i}z)
=z^5\sum_{\ell\ge0}g_{j,\ell}b^\ell z^{6\ell}$，则
$$
m_{r,k}=-\frac{c_k(6k)!a_{(6k-r-1)/6}}{252}
 \sum_{j=0,2}g_{j,(r-5)/6}\,t_j^{6k-r}.
\tag{28}
$$
只需 $\ell=0,1,2$，由五个原 sigma 的有限乘积逐项计算。
(27) 保所有正矩 Euler 因子，不把 (26) 的模 $p$ 值冒认为全式。

## 7. 固定坏集、全尾和同一原非零域

本篇不增加新的 ray。沿现有固定无限 ray，额外删除下面固定
非零数的分母素因子及范数分子素因子：
$$
\alpha_Y,\quad\alpha_W,\quad\alpha_{W_2},
                  \quad\Delta_{14},\quad m_5.
\tag{29}
$$
(24)–(26) 已给全部常数；所有精确范数在证书中。
例如范数分子依次为
$$
\begin{gathered}
688706324877646368104767,\quad
6060291417060629480668567,\quad
18194560460031693634423,\\
5825219716074126970934359,\quad
30016555230708225.
\end{gathered}
$$
因此是完全固定的有限集合，不随深度或目标素数变化。

低于五阶的项由五个独立 sigma 的质量零消失。
对三个实际单位分支在 (18) 中的准确处理之后，余下两个解析
积分只有 $5\bmod6$ 次幂；测试次数至多十八，log 分母不超过
当前幂次。因此
$$
v_p([T^r]\mathcal A_L)\ge-\lfloor\log_pr\rfloor.
\tag{30}
$$
$p\ge71,n\ge1$ 时，第五阶之后的项在 $T=\kappa^n$ 的赋值
严格大于 $5n$。结合 (23)、(25)、(26)，得
$$
\boxed{
v_p(C_{Y,n})=v_p(C_{W,n})=v_p(C_{W_2,n})=v_p(M_n)=5n,
}
$$
$$
\boxed{
v_p\left(\frac{C_{W,n}}{6\delta}-C_{Y,n}\right)=5n
\quad(n\ge1).
}
\tag{31}
$$
这里完整 log 项仍保在 (21)，只在单位判定中使用其属于
$p\mathcal O$。若以后改变 Mellin 尺度，(27) 的非零质量所乘
log 项必须一起运输。

## 8. 与 R522 构成完整三观察零来源

把 R522 的实际单位正测试写为
$$
\mathfrak q_{3,p}
={\bf1}_{H_0\ {\rm unit}}
 \frac{H_0^6}{216b\Omega^6(1+\lambda\kappa^6)}.
$$
R522 给同一个原 $\pi_3$ 推前身份。
因此本篇有一个完整同源差
$$
\boxed{
\mathcal K_p=(\mathfrak q_{14,p}-\mathfrak q_{3,p})\rho,
\qquad(\pi_3)_*\mathcal K_p=0.
}
\tag{32}
$$
它对任意真正只依赖 $(Y,W,W')$ 的连续测试和混合条件都为零，
并非仅三个边际相同。

例如在**同一个**真实域
$\mathcal U=\{Y,W\ {\rm unit}\}$ 上，
$$
\boxed{
\int_{\mathcal U}
 d\left(\frac{\log\langle W\rangle}{6\delta}
                       -\log\langle Y\rangle\right)d\mathcal K_p=0.
}
\tag{33}
$$
另一方面，$\mathcal D_n\subset\mathcal U$。
R522 对 $\mathfrak q_{3,p}$ 的该归一局部差从十一阶起，
而 (31) 对新测试的第五阶为单位。所以
$$
\boxed{
v_p\left[
\int_{\mathcal D_n}
 d\left(\frac{\log\langle W\rangle}{6\delta}
                       -\log\langle Y\rangle\right)d\mathcal K_p
\right]=5n.
}
\tag{34}
$$
(33) 无需先假设 $J'_S$ 或 $J'_T$ 为零。
它的准确补域是 $\mathcal U\setminus\mathcal D_n$，不是两个
不同单位边际补域的含混合并。该补域仍必须给 (34) 的反号。

两个测试都被 $\mathcal T$ 及已经支付的观察轴核心固定；
(32) 也与原三观察压缩相容。但是 $\mathcal D_n$ 含原隐藏输入条件，
不是仅由 $\pi_3$ 决定的域。不能据 (32) 将其替换为
$\pi_3^{-1}(\pi_3\mathcal D_n)$，或删除其中隐藏纤维的补集。

## 9. 原算术零、几何运输与全部补域

对每个观察 $L=Y,W,W_2$，原完整中央仍按 (15) 分成
$\mathcal D_n$ 的 (19) 与真实 $\{L\ {\rm unit}\}\setminus\mathcal D_n$
上的同一测试积分。若 $J'_S=J'_T=0$，后者恰为前者的负值。
(27) 同时给质量补偿，不能以全域算术质量零抹掉局部质量。

又因 (13) 在 $\mathcal T$ 下不变，
$h=\omega^2\mathcal T_*\rho$ 上的
$\mathcal T\mathcal D_n$ 仍是原 $W$ 深管，第一 $Y$ 中央为
$\omega^2C_{Y,n}$，质量为 $\omega^2M_n$。
测试没有移动；原六个域条件和第一 Mellin 权仍按真正矩阵运输。

本篇已经支付的新增结构是三条整十四度方向、整个十四度的绝对
核心号、完整三观察评价测试、非零且带真实质量的 S/T 局部差，
以及 (32)–(34) 的同域混合零行。其隐藏补域尚未消去，
主目标仍须由这些实际来源关系继续推进。

## 精确证书与依赖

- [BigInt 十四度评价矩阵、三轨道、全部实际第五阶与质量脚本](../scripts/check-r528-degree14-three-orbit-arithmetic-test.js)；
  [完整固定系数与原单位分支数据](../scripts/check-r528-degree14-three-orbit-arithmetic-test.json)。
  同一 JavaScript 主体已在当前 V8 实际执行；三维整个评价身份、
  原六输入轨道、半特征奇偶、全部混合项及固定范数通过。
- [R522：三度普适正测试与同一原非零网格](R522-common-degree3-even-factor-and-same-st-positive-test.md)。
- [R471：原 sigma/Theta 的共同绝对核心 beta](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R516：完整原共同伴随空间](R516-original-rotated-common-companion-cores-and-word-intersections.md)。
- [R493：真正三阶几何和六输入来源](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
