# R515 — 原 S/T 的真实二维联合、四伴随与同源 sigma carry

日期：2026-11-14。**状态：已证明。** 本篇从 R509–R510 的
同一个原六 sigma 来源出发，付清原 $S/T$ 平面的四个完整伴随，
得到一个真实二维联合及其原两态核心。两个曲线条件行、第三条
合格新线及参考行都按真正推前保留；不是把两个边际拼接成联合。

原自由 sigma 与五输入残余的单位近相消，在此可完整返回同一个
来源，系数为已付单位。旧 $W$ 及原 $T_c$ 测试的隐藏坐标项
均显示保留；它们不会因为二维推前而自动消失。主目标尚未完成。

## 1. 原来源、三个低轴及固定 ray

沿用 R510 的所有原周期、$b_{\rm curve}=17$、canonical lift、
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2.
\tag{1}
$$
原变量按 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$ 排列，$x=\xi_4$。
$\nu_0=-\nu_\sigma^{\otimes6}/84$，第二态仍是
$\nu_1=\eta=K_{72,W_2}\nu_0$。

R509–R510 的实际 $Z,J,R$、$B=B_{15}$ 以及两条算术观察满足
$$
Y=Z+\bar\gamma x,\qquad
R=( (33-\omega)Z+2J)/27,
$$
$$
B=(R+\omega^2Z)/2,\qquad
W_2=-\omega^2Y+2B.
\tag{2}
$$
令
$$
c_0=17+14\omega,\quad \bar c_0=3-14\omega,\quad
P=\frac{158Z-c_0J}{27}.
$$
准确有
$$
\boxed{
B=\frac{\bar c_0 Z+J}{27},\qquad
\operatorname{Gram}(B,P)=\operatorname{diag}(15,2370).
}
\tag{3}
$$
从 $(Z,J)$ 到 $(B,P)$ 的行列式是 $-5/9$。
$P$ 保原自由输入 $x$、$K_{113918}$ 和两个原 $Q_i$。

本篇在 R509 已有固定 ray 上增加
$$
\boxed{\pi_0\equiv1\pmod{263}.}
\tag{4}
$$
这是兼容的固定单位 ray 细分，仍有无穷多个普通有理素数。
所有 (4) 以前的实际符号和原曲线规范都保持。

## 2. P2370、A3945、E41554 的 whole 标量

R510 已付整个 odd15 与 odd65 的共同标量 $\chi=\chi_{65}$，
$\chi^2=1$。对 $N=2370$，原 $79$ 条件及其余固定 ray 给
$g_\pi\equiv1+N\bmod2N$。这是 even 空间中的完整恒等交织。
原 $(Z,J)$ 共同核心为 $\lambda^2$，(3) 保同一整格和全部
伴随，因此整个 $P$ 空间的绝对核心为
$$
\boxed{K_{2370}=\chi I.}
\tag{5}
$$

现在定义完整原输出
$$
\boxed{
A=15Y-c_0B=P+15\bar\gamma x,\qquad
E=263x-\gamma A=158x-\gamma P.
}
\tag{6}
$$
$E$ 是新伴随，字母不表示椭圆曲线。
直接核得
$$
\boxed{
\operatorname{Gram}(B,A,E)=\operatorname{diag}(15,3945,41554),
}
\tag{7}
$$
其中 $3945=15\cdot263$，$41554=2\cdot79\cdot263$。
从 $(P,x)$ 到 $(A,E)$ 的行列式为 $263$，实际逆为
$$
\boxed{
P=\frac{158A-15\bar\gamma E}{263},\qquad
x=\frac{\gamma A+E}{263}.
}
\tag{8}
$$
全部原输入和测试因此仍能准确恢复。

(4) 与原 ray 给
$$
g_\pi\equiv1\pmod{7890},\qquad
g_\pi\equiv1+41554\pmod{83108}.
\tag{9}
$$
$A$ 是标准 odd 半特征，$E$ 是标准 even 半特征。
故 whole odd3945 核为 scalar $\psi$。
绝对平方使用真实两 sigma 正交联合，两个乘子可取
$$
a=54,\qquad b=\delta\gamma^3,\qquad
Na=2916,\quad Nb=1029,\quad Na+Nb=3945.
$$
一偶一奇的系数使两个输出都保持标准 odd 半特征，矩阵行列式
为 $3945$，在当前 $p$ 可逆。原两 sigma 同时深的
$\lambda^2$ 与两个输出的 $\psi^2\lambda^2$ 比较，严格给
$$
\boxed{\psi^2=1.}
\tag{10}
$$
不从质量或未知中央导数定标。

$E$ 的 entire even 核由 (9) 是 scalar。原 $P$ 与独立 sigma
同时深的标量为 $-\chi\lambda^2$；(8) 把它准确换成 $(A,E)$
同时深。因此
$$
\boxed{K_{3945}=\psi I,\qquad
 K_{41554}=\varepsilon I,\qquad \varepsilon=-\chi\psi.}
\tag{11}
$$
这里不假设存在范数 $20777$ 的单个 CM 锚。
(8)、(10) 与同一非零联合已经支付绝对标量。

## 3. 整个六输入框架和原 S/T 平面

原两条观察现在准确是
$$
\boxed{
Y=\frac{A+c_0B}{15},\qquad
W_2=\frac{(33+17\omega)B-\omega^2A}{15}.
}
\tag{12}
$$
它们只依赖真正二维平面 $(B,A)$。
$E,K,Q_1,Q_2$ 均与这两条观察正交。

取原 $W_2$ 的新正交伴随
$$
\boxed{L=36Y-(17-3\omega)W_2.}
\tag{13}
$$
它的范数为
$$
N(L)=18936=72\cdot263,\qquad \langle L,W_2\rangle=0.
$$
整个物理框架
$$
\mathcal F=(W_2,L,E,K,Q_1,Q_2)
\tag{14}
$$
满足
$$
\boxed{
\operatorname{Gram}\mathcal F=
\operatorname{diag}\left(72,18936,41554,113918,
 \frac17\begin{pmatrix}40&-6-19\delta\\-6+19\delta&46\end{pmatrix}\right),
\quad
\det\mathcal F=308164464.
}
\tag{15}
$$
最后两个伴随及其交叉项始终是 R509 的原 $Q$ 块。
附证书给整个原六输入矩阵和逆，未只列两个边际。

所需原行全部为 CM 整数。例如
$$
\begin{aligned}
A={}&(-19+2\omega,\ 10+29\omega,\ 11-13\omega,\
30-15\omega,\ 32+14\omega,\ -1-11\omega),\\
E={}&(59+15\omega,\ -1-68\omega,\ -46+15\omega,\
158,\ -82-60\omega,\ -8+23\omega),\\
L={}&(-18+61\omega,\ 26+70\omega,\ -3-6\omega,\
15-67\omega,\ 50-23\omega,\ 4+12\omega).
\end{aligned}
\tag{16}
$$
(15) 的行列式只增加已经显示的固定有限坏因子，当前 ray
中全部可逆。

## 4. 整个 18936 度核心的绝对相位

令 $N=18936$。原二进制条件和 (4) 给完整中心
$$
\boxed{g_\pi\equiv14203+18936\omega
=1+\frac{3N}{4}+N\omega\pmod{2N}.}
\tag{17}
$$
$N/8\equiv3\bmod4$。与 R510 的逐列计算相同，且这里的全部
$N$ 列也在附证书直接核过：
$$
\boxed{
A_N=\frac14\sum_{t\in E[4]}\mathsf T_t^N
-\frac12\sum_{t\in E[2]}\mathsf T_t^N,\qquad A_N^2=I,
}
\tag{18}
$$
其标准基作用为
$A_Ne_j=-(-1)^je_{(1+3N/4)j+N/2}$。
它实现 (17) 的整个 Heisenberg 交织，包括两个负中心号。

绝对锚仍是原六 sigma，而不是形式相位。
对 $t=m/4$，由 (13)
$$
Lt-\bigl[-(17-3\omega)W_2\bigr]t=9Ym.
$$
右边是六个原 sigma 的整周期向量。它的总范数为
$81N(Y)Nm=2754Nm$，为偶；完整交替项为
$$
-\frac92\,N(17-3\omega)\,Nm=-\frac92\cdot349\,Nm,
$$
为实，故交替部分为零。于是保全所有原变量有
$$
\boxed{
\mathsf T^N_{L,t}\nu_0
=\mathsf T^{72}_{W_2,-(17-3\omega)t}\nu_0.
}
\tag{19}
$$
$-(17-3\omega)\equiv\omega^2\bmod4$，所以它置换 $E[4]$
并保 $E[2]$。故 $A_N\nu_0=K_{72,W_2}\nu_0=\eta$。

原 $(B,A)$ 全深核心是 $\chi\psi\lambda^2$。
从 $(B,A)$ 到 $(W_2,L)$ 的行列式为 $24/5$，故保同一个
完整双深事件。由 $K_{72}^2=I$，得
$K_L\nu_0=\chi\psi\,\eta$。与 (19) 比较便支付 whole 身份
$$
\boxed{K_{18936}=\chi\psi A_N,\qquad K_{18936}^2=I.}
\tag{20}
$$

## 5. 原两态的全部矩形及合法四伴随推前

$E,K$ 的 whole scalars 和原 $Q$ 共同核心都与 $W_2$ 核交换，
因为 (15) 的全部相应交叉项为零。
所以不只 $\nu_0$，实际第二态 $\eta$ 也保同一四伴随核心。

对 $a,b,c,e,t\ge0$，
$$
\boxed{
\begin{aligned}
&\nu_i\big|_{\substack{W_2\in p^a,L\in p^b,E\in p^c,K\in p^e\\
                  (Q_1,Q_2)\in(p^t)^2}}\\
&\quad=(-1)^{c+e}(\chi\psi)^{b+c}
 \lambda^{a+b+c+e+2t}
 [\kappa^a,\kappa^b,\kappa^c,\kappa^e,\kappa^tI_2]_*
 \nu_{\,i+a+b\ ({\rm mod}\ 2)}.
\end{aligned}}
\tag{21}
$$
这使用原完整 (14) 坐标；原各输入域都可由附逆矩阵运输。
六轴同深时，它准确回到 $\lambda^{6n}$。

令 $\bar\nu_i$ 是忘去 $(E,K,Q_1,Q_2)$ 后的真正二维推前。
对任意只依赖 $(B,A)$、等价地只依赖 $(W_2,L)$ 的连续测试或
紧开域，准确有
$$
\boxed{
\int_{\substack{E\in p^r,K\in p^s\\(Q_1,Q_2)\in(p^t)^2}}
 f\,d\nu_i
=\varepsilon^r(-1)^s\lambda^{r+s+2t}\int f\,d\bar\nu_i.
}
\tag{22}
$$
共同深度 $n$ 的标量是 $(\chi\psi)^n\lambda^{4n}$。
(22) 是带准确 scalar 的真正推前，没有使用一个质量为零的
sigma 的卷积逆。

实际二维来源可以直接写成
$$
\boxed{
\Phi_0(b,a)=-\frac1{84}\prod_{j=1}^{6}\sigma(B_jb+A_ja)
\in\mathcal S_{15}^{\rm odd}\otimes\mathcal S_{3945}^{\rm odd}.
}
\tag{23}
$$
这是原六输入同一个乘积，$B_j,A_j$ 为 (16)、R510(32) 的
实际系数。第二态是 $\Phi_1=K_{72,W_2}\Phi_0$，保其固定
quarter 覆盖。$W_2,L$ 的整个两态核心及 (21) 的前两轴，
都在真正推前后保留。

自由 sigma 还在 (23) 中明确可见：
$$
\Phi_0(b,a)=\sigma(15\bar\gamma a)
\left[-\frac1{84}\prod_{j\ne x}\sigma(B_jb+A_ja)\right].
\tag{24}
$$
括号内是同一个原五输入的
$\mathcal S_{15}^{\rm odd}\otimes\mathcal S_{2370}$ 来源，
不是用两条边际重新构造的乘积。

## 6. 原三曲线条件行和参考行的真实下降

第一 $Y$、第一 $W_2$ 的完整 CM 投影、角平均和 canonical
fiber 都正交于被忘掉的四轴，故与真正推前逐项交换。
因此 R510 的完整秩一张量身份继续成立。

对第一 $Y$ 方向仍用原 $\mathsf Y=2Y_s$ 覆盖。可取它的平面
正交伴随
$$
L_Y=34B-(3-14\omega)Y,\qquad N(L_Y)=8942=34\cdot263.
\tag{25}
$$
取 $2L_Y$ 后，原两个来源进入同一
$\mathcal S_{136}\otimes\mathcal S_{35768}$ 格。
对 $\eta$ 的 quarter 平移，$\langle W_2,L_Y\rangle=526$，
所以二重覆盖中的平移是合法 $35768$-torsion；没有删除 flat
character。

于是存在实际单伴随来源 $\ell_0,\ell_\eta,\ell_{\rm new},
\ell_{\rm ref}$，使
$$
\boxed{
\begin{array}{c|cc}
&\bar\nu_0&\bar\nu_1\\ \hline
P_S&S(2\cdot)\otimes\ell_0&S(2\cdot)\otimes\ell_\eta\\
P_{\rm new}&0&S_{\rm new}\otimes\ell_{\rm new}\\
P_H&0&H_{\rm ref}\otimes\ell_{\rm ref}.
\end{array}}
\tag{26}
$$
这些是 R510 全五伴随的实际推前，不用质量替代来源。
准确质量为
$$
\ell_0(0)=1,\quad\ell_\eta(0)=\omega/2,\quad
\ell_{\rm new}(0)=-52\omega^2/3,\quad
\ell_{\rm ref}(0)=
-\omega^2\left(-\frac{1+\delta}{2016b_{\rm curve}}\right).
\tag{27}
$$
它们均为当前普通处的单位，整性由原 Amice 系数提取保留。

第一 $W_2$ 的同一原 $T$ 投影也给
$$
\boxed{
P_{T,W_2}\bar\nu_0=P_{T,W_2}\bar\nu_1
 =T\otimes\ell_T,\qquad \ell_T(0)=-6\delta\omega^2.
}
\tag{28}
$$
此伴随是实际 $L$ 轴，whole degree 为 $18936$。

原 $J'_S=J'_T=J'_{\rm new}=0$ 因而对 (26)、(28) 的任意完整
单伴随测试给相应中央零。原 $H_{\rm ref}$ 仍是质量一
$E_{668168}$ 来源，$J_H(0)=1+\lambda$，导数未知；
依赖 Mellin 变量的测试所产生的质量项照旧保留。
(26)、(28) 不授权把一个混合 $Y,W_2$ 单位管认成独立伴随域。

## 7. 原自由 sigma 的单位 carry 完整返回同一来源

本节保 (24) 中真正独立的自由 sigma，而非给一个边际虚构
独立性。写
$$
\mathfrak c=15\bar\gamma x,\qquad A=P+\mathfrak c.
\tag{29}
$$
$\mathfrak c$ 是原自由 sigma 的单位尺度；$P$ 仍是原五输入的
完整输出。其核心分别为 $-\lambda,\chi\lambda$，均保 $B$。
总 $A$ whole core 是 $\psi\lambda$。

由 (8)，对任意 $n\ge1$ 有准确原域身份
$$
\boxed{
\{P,\mathfrak c\ {\rm unit},\ A\in p^n\mathcal O\}
=\{A\in p^n\mathcal O,\ E\ {\rm unit}\}.
}
\tag{30}
$$
这里右边与左边都在同一个完整原联合中。
当 $A$ 深时，(8) 的 $E$ 系数均为单位，严格给这两个方向；
并未将 $A$ 深单独当作两个输入各自深。

令 $\mathcal C_n$ 为左边原域的测度，保 $B$，把 $A$ 除以
$\kappa^n$，然后真正忘去 $E,K,Q_1,Q_2$。由 (11)、(22)，
$$
\boxed{
\mathcal C_n=(\psi\lambda)^n(1+\chi\psi\lambda)\,\bar\nu_0.
}
\tag{31}
$$
对 $n=1$，系数也可写成
$$
\lambda(\psi+\chi\lambda).
$$
从“总 $A$ 深”减去“$P,\mathfrak c$ 同时深”直接计算，得到同一式：
$\psi\lambda-(-\chi\lambda^2)=\lambda(\psi+\chi\lambda)$。
(31) 保任意完整 $(B,A)$ 测试，并非只有质量关系。

$1+\chi\psi\lambda$ 是 $1+\lambda$ 或 $1-\lambda$，其单位性
已经由 R410 支付。故这一实际 sigma carry 可在同一原来源
中整消去，没有留下另一个未识别来源。

例如对整个 Mellin 变量，取
$$
Y_n=\frac{A/\kappa^n+c_0B}{15},\qquad
W_{2,n}=\frac{(33+17\omega)B-\omega^2A/\kappa^n}{15}.
\tag{32}
$$
在 (30) 的原单位 carry 上，准确有
$$
\boxed{
\begin{aligned}
\int {\bf1}_{Y_n\ {\rm unit}}\langle Y_n\rangle^{(p-1)u}\,d\nu_0
 &= (\psi\lambda)^n(1+\chi\psi\lambda)J_S(u),\\
\int {\bf1}_{W_{2,n}\ {\rm unit}}\langle W_{2,n}\rangle^{(p-1)u}\,d\nu_0
 &= -6\delta\omega^2(\psi\lambda)^n
    (1+\chi\psi\lambda)J_T(u).
\end{aligned}}
\tag{33}
$$
积分域在两式中均是 (30)，其余完整伴随按 (31) 推前。
若附 (22) 的固定 $K,Q$ 深条件，只再乘其显示标量。
所以原两中央零已经合法传入这个真实的独立 sigma 单位
近相消区域，使用的是 (32) 的确切归一权。
本篇不把 $Y_n,W_{2,n}$ 改成原未缩放的 $Y,W_2$。

## 8. 旧 W、Tc 和原非零网格不能被遗忘

旧 R465 的 $W$ 在整个 (14) 框架中的准确式为
$$
\boxed{
W=\frac{22-7\omega}{36}W_2
 +\frac{7(37+23\omega)}{36\cdot263}L
 -\frac{233+209\omega}{79\cdot263}E
 +\frac{1+\omega}{79}K.
}
\tag{34}
$$
$E,K$ 系数都非零。旧 $W'$ 由
$W+\omega^2W'+\omega W_2=0$ 得到，也保这些项。
因此旧 $W$ 管、旧四态 $K_W,F$ 的具体域操作，不会自动成为
(23) 的二维操作。需要它们时须回到 (14)、(34) 及完整
限制/测试的转置。

原 R497 的合法算术测试使用
$T_c=\gamma Z-27x$。它也不只依赖二维平面：
$$
\boxed{
T_c=\frac{\gamma c_0}{15}B
 -\frac{247\gamma}{15\cdot263}A-\frac{34}{263}E.
}
\tag{35}
$$
等价地
$$
T_c=\frac{37+45\omega}{36}W_2
 -\frac{605+876\omega}{36\cdot263}L-\frac{34}{263}E.
\tag{36}
$$
因此 R497/R509 的 $h^\times(T_c/\Omega)$ 非零同深管，不能
在 (22) 中当成与 $E$ 无关的测试。
若要保其有限多项式部分，应逐项保 $E^j$ 的真正加权推前：
$E$ 深 $r$ 会产生额外 $\kappa^{rj}$，不能只乘无权 scalar。
若保 $T_c$ 单位指示函数，则也须保 (35) 的完整条件。

同样，$\mathcal T,\mathcal U$ 的六维隐藏交叉仍按 R509 全部
保留；本文未构造一个不成立的二维几何对称。
已付的新数据是原两态的真实二维来源、四伴随核心、三条曲线
和参考的完整单伴随行，以及 (30)–(33) 的同源 sigma carry。
原未移动的 $Y/W/W_2$ 管和这些归一 carry 的剩余比较仍须支付，
主目标没有由这次推前自动完成。

## 证书与依赖

- [BigInt 有理/CM 全框架证书](../scripts/check-r515-original-two-dimensional-st-source.js)；
  [完整原矩阵、逆、Gram、Tc/旧W运输和相位数据](../scripts/check-r515-original-two-dimensional-st-source.json)。
  同一主体已在当前 V8 实际执行，全部 $18936$ 列和显示身份
  通过。无浮点近似，未在环境不可用时声称执行 Python。
- [R510：同一原两态、十五度轴与原两中央词域](R510-original-w2-companion-and-fifteen-axis-central-words.md)。
- [R509：同一原五输入与准确隐藏耦合](R509-original-five-sigma-two-y-frames-and-common-st-source.md)。
- [R504：奇六十五度的真实来源和绝对标量](R504-original-two-axis65-core-and-complete-rectangles.md)。
- [R410：原 fixed ray 上整分母的单位性](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)。
