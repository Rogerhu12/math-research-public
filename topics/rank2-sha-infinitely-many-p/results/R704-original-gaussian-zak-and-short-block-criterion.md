# R704 — 原固定 theta 的高斯 Zak 展开与真正短块判据

日期：2026-11-15。**状态：同一原 theta 幅度的精确高斯展开、绝对酉 Zak 变换、原短块及其无对数损失返回已证明。尚未证明短块的幂次节省或原迹非零。**

本篇接 R703/R705 的原实际矩形代表和原乘法角色。除去一个已知准周期后，原幅度并非任意光滑函数：其磁全纯方程将全部 Fourier 系数精确确定为只有固定 \(m\) 个系数的高斯族。这也把可用的有限 Weil 本征函数定理必须控制的观测写成实际长度 \(p\) 的短块，而不是单点范数。

## 1. 同一个原幅度与准周期

固定
\[
p=6s-1>101,\quad m\in\{34,72\},\quad
\omega=e^{2\pi i/3},\quad\delta=1+2\omega=i\sqrt3,
\]
原 \(E_{17}:y^2=x^3+17\) 的正实周期为 \(\Omega\)，格为
\(\Lambda=\Omega(\mathbf Z+\omega\mathbf Z)\)。令
\[
F_m(z)=\sigma(z)^m\phi_m(P_z),\qquad
A_m(x,y)=\mathfrak k(\Omega(x+\omega y))^m
                       \phi_m(P_{\Omega(x+\omega y)}).
\tag{1}
\]
这里的 \(\phi_m\) 就是 R700 的原有理函数，不能换来源。
它只有格点处的 \(m-6\) 阶极，故 \(F_m\) 是整个复平面上的全纯函数，在每个格点至少六阶零；它不是零函数。

等边格的 \(\eta_\lambda=B\bar\lambda\)，且 Legendre 关系
\[
\eta_\Omega\omega\Omega-\eta_{\omega\Omega}\Omega=2\pi i,\qquad
\eta_{\omega\Omega}=\omega^2\eta_\Omega
\]
给
\[
B\Omega^2=\eta_\Omega\Omega=\frac{2\pi}{\sqrt3}.
\]
因此
\[
\boxed{\;
A_m(x,y)=
e^{-\pi m|x+\omega y|^2/\sqrt3}
F_m(\Omega(x+\omega y)).
\;}
\tag{2}
\]
这是 R700 的同一个 Klein 规范；所有 \(m\) 为偶数，奇偶符号已确实消去。R703 的准周期准确为
\[
A_m(x+1,y)=e^{\pi imy}A_m(x,y),\qquad
A_m(x,y+1)=e^{-\pi imx}A_m(x,y).
\tag{3}
\]
定义
\[
\mathcal B_m(x,y)=e^{\pi imxy}A_m(x,y).
\]
则
\[
\mathcal B_m(x,y+1)=\mathcal B_m(x,y),\qquad
\mathcal B_m(x+1,y)=e^{2\pi imy}\mathcal B_m(x,y).
\tag{4}
\]
第二条不能也误写成周期条件。

## 2. 磁全纯方程给出的固定 \(m\) 个高斯系数

因为 \(F_m\) 全纯，直接对 (2) 求导得到
\[
\boxed{\;
(\partial_y-\omega\partial_x)\mathcal B_m=2\pi imx \mathcal B_m.
\;}
\tag{5}
\]
确实，置
\[
L(x,y)=\pi imxy-\frac{\pi m}{\sqrt3}(x^2-xy+y^2),
\]
则 \(\partial_yF_m=\omega\partial_xF_m\)，并且
\(L_y-\omega L_x=2\pi imx\)，这证明 (5)。

沿真正周期的 \(y\) 方向展开
\[
\mathcal B_m(x,y)=\sum_{n\in\mathbf Z}b_n(x)e^{2\pi iny},\qquad
b_n(x)=\int_0^1\mathcal B_m(x,y)e^{-2\pi iny}\,dy.
\]
函数光滑且周期，故积分分部和逐项微分合法。(5) 给
\[
b_n'(x)=\frac{2\pi i}{\omega}(n-mx)b_n(x).
\tag{6}
\]
置
\[
\gamma_m=\frac{\pi m}{2}(\sqrt3-i).
\]
解 (6)，再用 (4) 的
\(b_n(x+1)=b_{n-m}(x)\)，得到
\[
\boxed{\;
b_n(x)=d_{[n]_m}\exp\!\left[-\gamma_m
                                  \left(x-\frac nm\right)^2\right],
\quad n\in\mathbf Z.
\;}
\tag{7}
\]
其中只有 \(m\) 个固定复数 \(d_0,\ldots,d_{m-1}\)，与 \(p,r\) 无关。一个完全指定的定义是
\[
d_j=b_j(j/m),\qquad0\le j<m.
\tag{8}
\]
周期关系严格给 \(d_{n+m}=d_n\)，没有丢掉代表变化的相位。
至少一个 \(d_j\ne0\)，否则 (7) 迫 \(F_m=0\)。

(7) 在每个有界 \(x\) 区间连同任意有限阶导数绝对一致收敛。特别地，令
\[
c_m=\frac{\pi\sqrt3}{2m},\qquad D_m^{\rm an}=\max_j|d_j|,
\]
则在 \(0\le x\le1\) 上
\[
|b_n(x)|\le
 D_m^{\rm an}e^{-c_m(|n|-m)_+^2},\qquad
|b_n'(x)|\le
 2|\gamma_m|(1+|n|/m)|b_n(x)|.
\tag{9}
\]
这里 \(D_m^{\rm an}\) 只是本篇解析系数界，不能与 R700 的固定整数分母 \(D_m\) 混淆。于是固定常数
\[
\boxed{\;
V_m=\sum_{n\in\mathbf Z}
\left(\sup_{0\le x\le1}|b_n(x)|
      +\int_0^1|b_n'(x)|\,dx\right)<\infty
\;}
\tag{10}
\]
与 \(p\) 无关。

## 3. 绝对酉 Zak 变换

令 \(\mathscr H_p=\mathbf C[\mathbf Z/p^2]\)，使用未除维数的标准内积
\[
\langle f,g\rangle_{\mathscr H_p}
  =\sum_{j\bmod p^2}f(j)\overline{g(j)}.
\]
R705 的 \(\mathcal V_m\) 使用
\(\sum_{a,b\bmod p}A(a,b)\overline{B(a,b)}\)；
完整准周期为
\[
A(v+p\ell)=e_p\!\left(\frac m2[\ell,v]\right)A(v).
\]
这里 \([a+b\omega,c+d\omega]=ad-bc\)。

对整数 \(a,b\) 定义
\[
\boxed{\;
(Z_m f)(a,b)=p^{-1/2}e_{p^2}(-mab/2)
        \sum_{t\bmod p}f(a+pt)e_p(-mbt).
\;}
\tag{11}
\]
\(p\nmid m\)，所以每个固定 \(a\bmod p\) 上这是一个酉离散 Fourier 变换。平移 \(a\mapsto a+p\)、\(b\mapsto b+p\) 分别给
\(e_p(mb/2)\)、\(e_p(-ma/2)\)，恰为原准周期。因此
\[
Z_m:\mathscr H_p\xrightarrow{\ \sim\ }\mathcal V_m
\]
是具有完全指定中心与相位的酉同构，其逆为
\[
\boxed{\;
(Z_m^{-1}A)(a+pt)=p^{-1/2}
 \sum_{b\bmod p}A(a,b)e_{p^2}(mab/2)e_p(mbt).
\;}
\tag{12}
\]
所有平方根取正实值，未给每个基矢另选根单位。

R705 的
\[
(\mathsf D_{x+y\omega}A)(a,b)
 =e_{p^2}(m(xb-ya)/2)A(a+x,b+y)
\]
在本模型中准确成为
\[
\boxed{\;
(Z_m^{-1}\mathsf D_{x+y\omega}Z_m f)(j)
 =e_{p^2}(-my(j+x/2))f(j+x).
\;}
\tag{13}
\]
把 (11) 代入即可核实，(13) 没有未定 Weil 乘子。
这与 R706 的绝对 Schrödinger/Bessel 规范相同。

## 4. 原向量在标准模型中是固定数目的高斯包

将原幅度的样本
\[
\mathbf A_{m,p}(a,b)=A_m(a/p,b/p)
\]
代入 (12)。由 (7) 和 \(y\)-Fourier 正交，
\[
(Z_m^{-1}\mathbf A_{m,p})(a+pt)
 =\sqrt p\sum_{n\equiv-mt\bmod p}b_n(a/p).
\]
写 \(n=-mt+pk\)，并令 \(j=a+pt\)，得到整个
\(\mathbf Z/p^2\) 上的精确公式
\[
\boxed{\;
f_{m,p}(j):=(Z_m^{-1}\mathbf A_{m,p})(j)
 =\sqrt p\sum_{k\in\mathbf Z}d_{[pk]_m}
   \exp\!\left[-\gamma_m
                    \left(\frac jp-\frac{pk}{m}\right)^2\right].
\;}
\tag{14}
\]
它对 \(j\mapsto j+p^2\) 周期：相应将 \(k\mapsto k+m\)。
在一个完整周期内有 \(m\) 种固定中心 \(p^2k/m\)，宽度为常数倍 \(p\)；
系数只按 \(p\bmod m\) 置换。中心不必为整数，公式仍是精确的。
没有把原 theta 向量换成一个可自由选择的标准基向量。

## 5. 同一 wild 本征向量与真实短块

继续 R705 的
\[
\chi_r(v)=e_p\!\left(
 \frac{mr}{2\delta}(q_p(v)-\overline{q_p(v)})\right),
\qquad q_p(v)=\frac{v^p/\bar v-1}{p}\pmod p.
\]
全部 \(v=a+b\omega\) 都取原 \(0\le a,b<p\) 代表。置
\[
G_r(v)=\mathbf1_{\{Nv=r\bmod p\}}\chi_r(v)^{-1},
\qquad
\psi_r=\frac{Z_m^{-1}G_r}{\sqrt{p+1}}.
\tag{15}
\]
则 \(\|\psi_r\|_2=1\)，它正是 R705 指定
tame-trivial、wild \(e_p(mrt)\) 的单重本征向量。

对任意整数 \(n\) 和普通整数区间
\(I\subset\{0,\ldots,p-1\}\)，定义
\[
\boxed{\;
L_{p,m}(r,n;I)=
 \sum_{\substack{a\in I,\ 0\le b<p\\
                 a^2-ab+b^2=r\bmod p}}
 \chi_r(a+b\omega)e_{p^2}(-mab/2)e_p(nb).
\;}
\tag{16}
\]
这是指定小矩形内的原相位，不是任意 lift。
若 \(t_n\in\{0,\ldots,p-1\}\) 满足
\(mt_n\equiv-n\bmod p\)，由 (12)、(15) 有
\[
\boxed{\;
L_{p,m}(r,n;I)=
 \sqrt{p(p+1)}\sum_{a\in I}\overline{\psi_r(a+pt_n)}.
\;}
\tag{17}
\]
归一因子 \(\sqrt{p(p+1)}\) 不能删掉。

对每个 \(a\)，方程
\(b^2-ab+a^2-r=0\bmod p\) 至多有两个 \(b\)。
所以同样由 (12) 得
\[
\boxed{\;
|\psi_r(j)|\le\frac2{\sqrt{p(p+1)}}.
\;}
\tag{18}
\]
但 (18) 对 (17) 仅给
\[
|L_{p,m}(r,n;I)|\le2|I|,
\tag{19}
\]
在长度 \(p\) 上仍是 \(O(p)\)。所需改进确实是短块内的相位消去，而不是再次证明单点范数界。

## 6. 返回原迹：无 \(\log^2p\) 损失，且只需极低频短块

R703 的原和是
\[
\mathscr S_{p,m}(r)=
 \sum_{\substack{0\le a,b<p\\Nv=r\bmod p}}
       \chi_r(v)A_m(a/p,b/p).
\]
用 (7) 展开得准确恒等
\[
\boxed{\;
\mathscr S_{p,m}(r)=
 \sum_{n\in\mathbf Z}\sum_{a=0}^{p-1}b_n(a/p)
 \!\!\sum_{\substack{0\le b<p\\a^2-ab+b^2=r\bmod p}}
       \chi_r(a+b\omega)e_{p^2}(-mab/2)e_p(nb).
\;}
\tag{20}
\]
绝对收敛由 (9) 支付，故交换求和合法。
对每个 \(n\) 沿 \(a\) 做离散分部求和，(10) 给
\[
\boxed{\;
|\mathscr S_{p,m}(r)|
 \le V_m\max_{\substack{n\bmod p\\I\subset\{0,\ldots,p-1\}\\
                         I\ {\rm interval}}}
                   |L_{p,m}(r,n;I)|.
\;}
\tag{21}
\]
事实上只需从 \(0\) 开始的前缀区间；保留所有区间使可用定理的接口更直接。
(21) 的常数固定，R703 二维矩形 DFT 的
\(\log^2p\) 因子已不需要。

还可大幅缩小需要控制的 \(n\)。对 \(H\ge m+1\)，
(9) 及范数圆的 \(p+1\) 个点给
\[
\left|\sum_{|n|>H}\text{(20)中的第 \(n\) 项}\right|
 \le C_m' p\,e^{-c_m(H-m)^2}.
\tag{22}
\]
例如令
\[
H_p=m+\left\lceil\sqrt{3\log p/c_m}\right\rceil,
\]
则尾为 \(O_m(p^{-2})\)。因此
\[
\boxed{\;
|\mathscr S_{p,m}(r)|
 \le V_m\max_{\substack{|n|\le H_p\\I\ {\rm interval}}}
                 |L_{p,m}(r,n;I)|+O_m(p^{-2}).
\;}
\tag{23}
\]
这里只要控制 \(O_m(\sqrt{\log p})\) 个实际短块族；
其位置由 \(mt_n\equiv-n\bmod p\) 固定，不能任选。

等价地，酉性与 R705 的原迹公式给
\[
\boxed{\;
\mathcal T_{m,T_v}
 =\rho_v^{-m}\chi_r(v)^{-1}\sqrt{p+1}\,
                   \langle f_{m,p},\psi_r\rangle_{\mathscr H_p},
\quad Nv=r\bmod p.
\;}
\tag{24}
\]
(14) 是这里实际的测试向量；(24) 不是抽象的任意向量范数估计。

## 7. 一个可直接用于原边界的条件命题

假设对某个固定 \(0<\varepsilon\le1\)，存在与 \(p,r,n,I\) 无关的常数，使所有相关 \(p\)、所有 \(r\ne0\)、\(|n|\le H_p\) 及所有上述区间满足
\[
|L_{p,m}(r,n;I)|\le C p^{1-\varepsilon}.
\tag{25}
\]
则 (23) 给同一原和和全部原绝对迹共轭的界
\[
|\mathcal T_{m,T_v}|\le C_m''p^{1-\varepsilon}.
\tag{26}
\]
全共轭的返回使用 R696/R700/R703 已支付的 Galois 作用与复共轭，所有根单位模为一。

R700 的固定整数分母 \(D_m\)、唯一 \(p\) 位和原边界赋值恒等因而给：若原边界不为零，则
\[
\boxed{\;
v_p B_m(v_T^{p+1})
 \le1-\varepsilon+
       \frac{\log(D_m C_m'')}{\log p}-\frac1{p-1}.
\;}
\tag{27}
\]
这里末尾的 \(B_m\) 是原 LT 边界记号，不能与第1节用于去准周期的 \(\mathcal B_m(x,y)\) 混用。
(27) 是条件结论；本篇没有证明 (25)。

同样，本篇没有从原中央 \(j_m=0\) 推出 R699 的全部 \(2p-3\) 位条件，没有证明原迹非零，也没有付高 \(Q\) 重数或同 \(X\) 下降。新增的是实际测试向量的固定高斯结构与准确、无额外对数损失的短块接口。

## 依赖

- [R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：原 \(\phi_m\)、固定整数分母及 Klein 规范。
- [R703](R703-original-hall-phase-and-finite-fourier-return.md)：完整原相位、实际代表、准周期及原全迹。
- [R705](R705-original-wild-character-and-absolute-weil-projection.md)：原 wild 角色、绝对有限模型、单重投影与标准内积。
- [R706](R706-original-bessel-kernel-and-complete-stationary-fibres.md)：同一标准本征向量的完整 Bessel 核及全部例外。

本篇证明全部为显示恒等与收敛估计，不依赖数值扫描或未执行计算。
