# R436 — 原 U72 的完整四谱、精确非零质量与全部普通尺度项

日期：2026-11-14。**状态：已证明。** 对 R424 的同一个实际
\(U_{72}=SB_{38}=C_{34}D_{38}\)，原归一 CM7 算子
\(N=\mathscr M_\gamma/(\omega\gamma)\) 准确满足
\[
(N^2-1)(N^2-\omega)U_{72}=0.
\]
四条实际投影全都非零，特征值为 \(1,-1,\omega^2,-\omega^2\)；
原 \(b=17\) 上四条来源的质量依次为
\[
-\frac1{12096b},\quad-\frac1{12096b},\quad
 \frac1{12096b},\quad \frac1{12096b}.
\]
它们的完整普通 core 和各自的 principal 单位质量随之确定。
所有原尺度对中央导数贡献的质量项在下文保留。本文不为这些
辅助来源赋新的 rank-two 身份或中央零。

## 1. 固定原来源和完整 CM7 规范

保持 R424、R426 的原 \(E_b:y^2=x^3+b\)、\(b=17\)、
sigma 与普通周期，置
\[
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\gamma=3+\omega,\quad X=x^3,
\]
\[
R_2(X)=X^2+20bX-8b^2,\qquad
P_2(X)=X^2-\frac{4b}{7}X+\frac{16b^2}{7},
\]
\[
g_b(X)=X^3-30bX^2-144b^2X-32b^3.
\]
原四条实际因子给
\[
\boxed{
U_{72}=SB_{38}=C_{34}D_{38}
=\sigma^{72}X(X+b)(X-8b)^2R_2(X)P_2(X)g_b(X).
}
\tag{1}
\]
它在完整 \(\mu_6\) 型零空间
\[
\mathcal S_{72}^{(0)}
 =\sigma^{72}\langle1,X,\ldots,X^{12}\rangle
\tag{2}
\]
中，首项为 \(z^6\)，总质量为零。

使用与 R398、R413 相同的原 division trace
\[
\mathscr M_\gamma(\sigma^{72}h)
 =\sigma^{72}\operatorname{Tr}_{[\gamma]}
       \big[(r_{\bar\gamma}/r_\gamma)^{72}
                                h\circ[\bar\gamma]\big],
\qquad N=\mathscr M_\gamma/(\omega\gamma).
\tag{3}
\]
没有改变原绝对 CM 相位。

## 2. 特征零中的完整四幂身份

准确有
\[
\boxed{N^4U_{72}-(1+\omega)N^2U_{72}+\omega U_{72}=0.}
\tag{4}
\]
以下是完整而有限的计算证明，不是目标素数扫描。

取 \(b=1\)，在 R426 的原七点坐标代数中，令
\[
r=(2-6\delta)/7,\quad \bar r=(2+6\delta)/7,\quad
q(u)=u^3-r,\quad \bar q(u)=u^3-\bar r,
\]
\[
N_{\bar\gamma}(u)
 =u^6+(28\bar r+12)u^3+(7\bar r+24)\bar r,
\]
\[
\begin{aligned}
P_a(u)={}&u^7-\gamma^2au^6+(28r+12)u^4
       +2\gamma^2aru^3\\
       &+(7r+24)ru-\gamma^2ar^2 .
\end{aligned}
\tag{5}
\]
对任意 \(h(X)\) 属于 (2)，其 (3) 在 \(x=a\) 上除去
\(\sigma^{72}\) 的准确值为
\[
\operatorname{Tr}_{\mathbf Q(\delta)[u]/(P_a)}
 \left[
 \left(\frac{\bar\gamma\bar q(u)}{\gamma q(u)}\right)^{72}
 h\left(
 \left\{\frac{uN_{\bar\gamma}(u)}
             {\bar\gamma^2\bar q(u)^2}\right\}^{3}
 \right)\right].
\tag{6}
\]
每一步是七维商代数中的完整迹，全部在 \(\mathbf Q(\delta)\)
中运算。该 trace 保持 (2)，故 \(a=1,\ldots,13\) 的十三个
互异 \(a^3\) 完整确定输出多项式；不是忽略高次项的插值猜测。

从 (1) 开始，连续四次使用 (6)，各次除以同一个
\(\omega\gamma\)，得到 \(U,NU,N^2U,N^3U,N^4U\) 的全部十三项
系数。代入 (4) 后每个系数准确为零。
完整五列和下节四投影已保存于
[特征零系数证书](../notes/2026-11-14-theta-u72-exact-spectrum.json)。
其中 \([a,b,c]\) 表示 \((a+b\delta)/c\)，基为 (2) 的升幂基。
可重现脚本是
[check-r426-degree18-and-u72-cm7.js](../scripts/check-r426-degree18-and-u72-cm7.js)；
它使用内置大整数有理运算，并同时检查本篇 (4)、(9) 及 R426
两条 degree18 的完整特征恒等式。设置 \(OUT_DIR\) 可输出同一
完整系数证书。

这里四幂核算已在本地完成。不是尚未执行的 CI 队列任务，也不以
有限域投影质量代替特征零结果。

## 3. 四个实际投影及完整多项式

因为 \(\omega^4=\omega\)，(4) 的四个互异根为
\(1,-1,\omega^2,-\omega^2\)。定义
\[
Q_1=\frac{N^2-\omega}{1-\omega}U,\qquad
Q_\omega=\frac{N^2-1}{\omega-1}U=U-Q_1,
\]
\[
\boxed{\begin{aligned}
U_1&=(Q_1+NQ_1)/2,&
U_{-1}&=(Q_1-NQ_1)/2,\\
U_{\omega^2}&=(Q_\omega+\omega NQ_\omega)/2,&
U_{-\omega^2}&=(Q_\omega-\omega NQ_\omega)/2 .
\end{aligned}}
\tag{7}
\]
于是 \(U=\sum_\epsilon U_\epsilon\) 且
\[
NU_\epsilon=\epsilon U_\epsilon.
\tag{8}
\]
这些是真正原 theta 来源的算子投影。分母 \(2,1-\omega,\gamma\)
在当前 \(p>19,\ p\ne17\) 处都是单位；也可直接用下表看出完整整性。

为给出独立可读的实际来源，记下表的整数为 \(c_{\epsilon,j}\)。
对原一般 \(b\) 精确有
\[
\boxed{
U_{\epsilon,b}
=\frac{\sigma_b^{72}}{12096b}
       \sum_{j=0}^{12}c_{\epsilon,j}b^{12-j}X^j.
}
\tag{9}
\]

| \(j\) | \(c_{1,j}\) | \(c_{-1,j}\) | \(c_{\omega^2,j}\) | \(c_{-\omega^2,j}\) |
|---:|---:|---:|---:|---:|
| 0 | 8388608 | 8388608 | -33554432 | 16777216 |
| 1 | 113246208 | -113246208 | -50331648 | 503316480 |
| 2 | 975175680 | -355467264 | 528482304 | -15728640 |
| 3 | 1164443648 | -1765801984 | -2259156992 | -1407451136 |
| 4 | -189333504 | -1903951872 | -4420730880 | 3015770112 |
| 5 | -2217443328 | -38338560 | -2417983488 | 4233166848 |
| 6 | -1853417472 | 491575296 | -1387057152 | 725397504 |
| 7 | -233100288 | 3870720 | -353350656 | 557282304 |
| 8 | 12976128 | -26754048 | 124371072 | -8364672 |
| 9 | -2385664 | -2261248 | 21911104 | -23764928 |
| 10 | 105840 | -427680 | 441312 | -428784 |
| 11 | -5460 | 156 | 4068 | 13332 |
| 12 | -1 | -1 | 1 | 1 |

下表最后一行不会因原 \(U\) 的总质量为零而消失。
因为 \(\sigma^{72}X^{12}=1+O(z^6)\)，准确质量是
\[
\boxed{
m_1=m_{-1}=-\frac1{12096b},\qquad
m_{\omega^2}=m_{-\omega^2}=\frac1{12096b}.}
\tag{10}
\]
\(12096=2^6\,3^3\,7\)，故四个质量在每个当前素数处均为单位。
特别四投影均非零，四幂最小多项式准确是 (4)，而不只是它的
某个真因子。

(9) 的 \(b\) 归一不能漏掉。若 \(u^6=b\)，实际复曲线同构给
\[
U_b(z)=u^{-6}U_1(uz)=b^{-1}U_1(uz);
\tag{11}
\]
(3) 与这同构相容，所以各投影也满足 (11)。
因此从 \(b=1\) 到原 \(b=17\) 时质量确实乘 \(b^{-1}\)。
(9) 消除了辅助六次根，身份本身只含原有理 \(b\)。
这里的代数同构用于证明多项式身份，没有把辅助 \(u\) 当作同一
\(\mathbf Z_p\) 测度上的免费尺度替换。

计算记录中的早期有限域质量曾提示 \(\pm1/12\)；该猜测在完整
特征零运算中失败，未登记为结论。准确原因是
\(12096\equiv-12\pmod{1009}\)，故 (10) 在 \(b=1\) 时具有与该
错误猜测相同的模 \(1009\) 值。脚本现检查准确的 (10)。

## 4. 整个普通 core、每条真实单位质量

保持 R413 的原 ray 和归一
\[
\pi_{17}=\pi_{24}=-\pi_0,\qquad
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad \beta=\kappa/p=\lambda^2 .
\]
R413 在整个 \(\mathcal S_{72}\) 已付
\[
K_{72}=-N^9,\qquad
\nu_A|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_{72}A}.
\tag{12}
\]
所以 (8) 给每条实际来源的完整测度式
\[
\boxed{\nu_{U_\epsilon}|_{p\mathbf Z_p}
       =c_\epsilon[\kappa]_*\nu_{U_\epsilon},\qquad
       c_\epsilon=-\lambda\epsilon^9.}
\tag{13}
\]
准确分组如下。

| 来源 | \(\mathscr M_\gamma\) 特征值 | 完整普通 core \(c_\epsilon\) | 全质量 | principal 单位质量 |
|---|---|---|---|---|
| \(U_1\) | \(\omega\gamma\) | \(-\lambda\) | \(-m_0\) | \(-(1+\lambda)m_0\) |
| \(U_{-1}\) | \(-\omega\gamma\) | \(+\lambda\) | \(-m_0\) | \(-(1-\lambda)m_0\) |
| \(U_{\omega^2}\) | \(\gamma\) | \(-\lambda\) | \(+m_0\) | \(+(1+\lambda)m_0\) |
| \(U_{-\omega^2}\) | \(-\gamma\) | \(+\lambda\) | \(+m_0\) | \(+(1-\lambda)m_0\) |

这里 \(m_0=(12096b)^{-1}\)。
R410 已证明 \(1\pm\lambda\) 为单位。因此四条实际 principal Mellin
函数的常数项均为单位；其余系数因
\(\log_p\langle x\rangle\in p\mathcal O\) 而模 \(p\) 为零。
每条因而是整 Tate 单位。

与此同时，同一 ordinary 正、负块分别是
\[
U^{(+)}=U_{-1}+U_{-\omega^2},\qquad
U^{(-)}=U_1+U_{\omega^2},
\tag{14}
\]
其全质量和单位质量各自为零。
四条非零质量只能在这些明确的组合中抵消，不能逐条删除。

## 5. 全部环带和中央尺度项

为使 (13) 的归一可以直接用于原联合，记
\[
J_{\epsilon,\ell}(u)
 =\int_{\mathbf Z_p^\times}\omega_p(x)^\ell
                    \langle x\rangle^{du}\,d\nu_{U_\epsilon},
\qquad d=p-1.
\]
完整第 \(n\) 环带在单位部分 \(x/p^n\) 上的 Mellin 行准确为
\[
\boxed{
c_\epsilon^n\,\omega_p(\beta)^{n\ell}
       \langle\beta\rangle^{ndu}J_{\epsilon,\ell}(u).
}
\tag{15}
\]
这来自 \(\kappa^n/p^n=\beta^n\)，不能把它换成只含
\(c_\epsilon^n\) 的式子。

principal 分支先在 \(|q|_p<1\) 的真实收敛环带和中得到
\[
Z_\epsilon(q;u)
  =\frac{J_{\epsilon,0}(u)}
         {1-qc_\epsilon\langle\beta\rangle^{du}}.
\]
因 \(1-c_\epsilon=1\pm\lambda\) 是单位，\(q=1\) 的整正规值满足
\[
Z_\epsilon(1;0)=m_\epsilon,\qquad
\boxed{
\partial_u Z_\epsilon(1;0)
 =\frac{J'_{\epsilon,0}(0)
          +c_\epsilon d\log_p\langle\beta\rangle\,m_\epsilon}
        {1-c_\epsilon}.}
\tag{16}
\]
所以即使某个总组合质量为零，也必须先保留 (16) 四条各自的质量
项，再按实际算子和尺度相加。

对同一原测度中一个明确的物理单位尺度 \(a\)，principal 返回是
\[
J_{[a]_*U_\epsilon}(u)
 =\langle a\rangle^{du}J_{\epsilon,0}(u),
\]
\[
\boxed{J'_{[a]_*U_\epsilon}(0)
 =J'_{\epsilon,0}(0)
       +d\log_p\langle a\rangle(1-c_\epsilon)m_\epsilon.}
\tag{17}
\]
这也是把新的四谱来源接回原 \(SB_{38}\) 时必须保留的项。
(17) 的 \(a\) 是已指定的原单位坐标尺度；不包含 (11) 中尚未
连同周期运输的辅助同构参数。

## 6. 与原 T72 的准确比较和仍未付的算术身份

原 \(T_{72}=SL\) 在 R398 中满足
\[
\mathscr M_\gamma T_{72}=-\gamma T_{72},\qquad T_{72}(0)=0.
\tag{18}
\]
所以它只在 \(N=-\omega^2\) 的特征块中。
本篇 \(U_{-\omega^2}\) 虽共享该特征值，却有非零质量 \(m_0\)；
它不可能是原 \(T_{72}\) 的标量倍数。
其余三个实际 \(U_\epsilon\) 也都非零，故 (1) 本身不是原
\(T_{72}\) 的一条特征线。

已有的实际因子差
\[
B_{38}-L
=-2bJ_{12}
     \{\sigma(z)\sigma(\delta z)\sigma(3z)\}^2
\]
以及 \(U-T=S(B_{38}-L)\)，不能把 degree38 的同 core 免费提升
到 degree72。现在它们的实际总和谱由 (7)–(14) 完整指定。

本篇支付的是固定真实 theta 来源的完整四谱、整性、绝对 ordinary
core、每条质量及尺度 log。质量一类的辅助 Mellin 单位不能代替
原 rank-two 中央导数，单个 CM7 特征也不足以宣称新的全局 Hecke
插值或 rank-two 曲线。原 \(J'_S,J'_T\) 到这些谱来源的实际中央
关系仍须由同一联合和完整域运输证明。

## 依赖

- [R398：原 T72 及绝对 CM7 规范](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。
- [R413：整个 degree72 的 \(K_{72}=-N^9\)](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R424：同一个实际 U72 和四个原因子](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R426：原七点 trace 与两条 degree18 来源](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R410：固定 ray 的 \(1\pm\lambda\) 单位](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)。

