# R464 — 固定 δ 除法来源、非恒范数、完整算术投影与普通核心

日期：2026-11-14。**状态：已证明。**

从 R460 的原两个奇伴随 \(C_{13},C_{15}\) 出发，固定同源
\(\delta^2=-3\) 给两个明确的 degree102 全纯来源。
它们的有理除法范数不是 R463 的一，而是准确的
\(-x^3/(4b)\)；完整纤维迹回到原 degree34 空间。
在整个十八维型零空间中计算真实 CM7 算子，得到两条来源
各自的十五维完整轨道、全部质量以及回原 \(S,H_3,H_5\)
的准确投影。当前同一个 ray 上，整个 degree102 的普通核心
准确为 \(-N_7^9\)，没有增加素数同余条件。

两条新来源的完整单位质量都是单位；这不是原 \(J'_S\)
的非零证明。十二个额外谱分量和两条参考导数均保留。
主目标未完成。

## 1. 同一个原 frame、伴随与固定除法函数

保持原 \(E_b:y^2=x^3+b\)、\(b=17\)、微分 \(dx/(2y)\)、
\(x=z^{-2}+\cdots\)、\(y=-z^{-3}+\cdots\)、\(\sigma=z+\cdots\)。
置
\[
X=x^3,\qquad \Theta=x\sigma^2,\qquad
\mathfrak q=17\Theta'/\Theta,\qquad
\delta=1+2\omega,\quad\delta^2=-3.
\]
原 \(C=C_{1j}\)、\(j=3,5\)，满足
\[
C'-\mathfrak qC=S-c_CH_j,\qquad C'(0)=-c_C,
\tag{1}
\]
其中
\[
c_{13}=-\frac{37}{33936b},\qquad
c_{15}=-\frac{37}{53760b}.
\tag{2}
\]
它们的完整多项式为
\[
C=\sigma^{34}y\sum_{j=1}^{5}P_jb^{4-j}X^j,
\tag{3}
\]
两组 \(P_1,\ldots,P_5\) 是
\[
\begin{aligned}
\mathbf P_{13}&=\left(
\frac{10880}{14847},-\frac{13504}{14847},
\frac{6269}{9898},-\frac{6523}{59388},-\frac{37}{33936}
\right),\\
\mathbf P_{15}&=\left(
\frac{923}{1470},\frac{107}{5880},
\frac{11399}{15680},-\frac{15919}{94080},-\frac{37}{53760}
\right).
\end{aligned}
\tag{4}
\]
这些是 R307/R460 的同一个 \(C\)，不是重新选择的奇向量。
特别 \(P_5=bc_C\)。

原 sigma 的完整同源式给
\[
\sigma(\delta z)=\delta x(z)\sigma(z)^3,\qquad
x(\delta z)=-\frac{X+4b}{3x^2},\qquad
y(\delta z)=-\frac{y(X-8b)}{3\delta X}.
\tag{5}
\]
因此对 \(r_\delta=\sigma(\delta z)/\sigma(z)^3=\delta x\)，
准确有
\[
\boxed{
u_\delta=\frac{r_\delta(\delta z)}{r_\delta(z)}
=\frac{x(\delta z)}{x(z)}
=-\frac{X+4b}{3X},\qquad
R_\delta=\partial_z\log u_\delta
=-\frac{24b\,y}{x(X+4b)}.
}
\tag{6}
\]
所有整体常数由 (5) 的原点首项支付。

## 2. δ 的真实范数及完整纤维迹

这里 \(\delta\) 不再与所取同源互素，不能应用 R463 的
\(\operatorname{Norm}u_A=1\)。
对一个一般目标点 \(Q\)，写 \(\xi=x(Q)\)。其三个
\(\delta\) 原像的 \(x\) 坐标恰为
\[
U^3+3\xi U^2+4b=0
\tag{7}
\]
的三个根。因此原点规范下
\[
\boxed{
\operatorname{Norm}_{[\delta]}x=-4b,\qquad
\operatorname{Norm}_{[\delta]}u_\delta
=\frac{x^3}{-4b}=-\frac{X}{4b}.
}
\tag{8}
\]
这也符合准确除子：
\(\operatorname{div}x=T_++T_--2O\)，而
\(\delta T_\pm=O\)；推前后范数 \(x\) 的除子为零。

令 \(\operatorname{Tr}_{[\delta]}\) 表示目标纤维三个原像的
通常和。对完整 (8) 取不变微分时须保微分尺度：
\[
d\log\operatorname{Norm}_{[\delta]}u_\delta
=\delta^{-1}\operatorname{Tr}_{[\delta]}R_\delta\,dz.
\]
故
\[
\boxed{
\delta^{-1}\operatorname{Tr}_{[\delta]}R_\delta
=\frac{X'}X=\frac{6y}{x}.
}
\tag{9}
\]
右端的极点没有被丢掉。具体地，
\(u_\delta(O)=-1/3\)，但 \(u_\delta\) 在 \(T_\pm\)
有极点，所以不能把 (8) 在零纤维写成三个有限代数值的
对数和。原点的 \(-\log_p3\) 不因此成为原中央导数。

## 3. 两个固定 degree102 全纯来源

定义
\[
\boxed{\mathcal A_C(z)=\delta^{-1}R_\delta(z)C(\delta z).}
\tag{10}
\]
\(R_\delta\) 的极点位于
\([\delta]^{-1}\{T_+,T_-\}\) 及 \(T_\pm\)。
在前一组点，\(C(\delta z)\) 至少三阶为零；在 \(T_\pm\)，
\(\delta T_\pm=O\) 且 \(C\) 在 \(O\) 恰一阶为零。
全部简单极因而被真实拉回截面支付。
\(R_\delta\) 是椭圆有理函数，\(C(\delta z)\) 是原
degree34 线丛的真正 pullback，因此
\[
\boxed{\mathcal A_C\in\mathcal S_{102},\qquad
\mathcal A_C\text{ 的 }\mu_6\text{ 型为零}.}
\tag{11}
\]
这不需要把有极点的 \(R_\delta C\) 塞进原小空间。

把 (3)、(5)、(6) 直接相乘，得到完整多项式：
\[
\boxed{
\frac{\mathcal A_C}{\sigma^{102}}
=8\cdot3^{16}b(X+b)(X-8b)
\sum_{j=1}^{5}P_jb^{4-j}
\left(-\frac1{27}\right)^j
X^{10-2j}(X+4b)^{3j-1}.
}
\tag{12}
\]
每个 \(X\) 指数非负。多项式次数恰十六，所以
\(\mathcal A_C\) 从 \(z^6\) 起，准确首项为
\[
\boxed{
[z^6]\mathcal A_{13}=\frac{37}{1414},\qquad
[z^6]\mathcal A_{15}=\frac{37}{2240}.
}
\tag{13}
\]
这也直接由 \(R_\delta=24bz^5+\cdots\)、
\(C(\delta z)=-c_C\delta z+\cdots\) 得到
\([z^6]\mathcal A_C=-24bc_C\)。

所有 \(b\) 权重准确满足
\[
\boxed{\mathcal A_{C,b}(z)
=b^{-1}\mathcal A_{C,1}(b^{1/6}z).}
\tag{14}
\]
右边仅用于恢复同一有理公式的权重；原实际 frame 和周期
仍固定在 \(b=17\)，未在乘积内混用两个模型。

由投影公式及 (9)，完整的线丛纤维迹为
\[
\boxed{
\operatorname{Tr}_{[\delta]}\mathcal A_C
=\frac{6y}{x}C
=\sigma^{34}x^2\,
6(X+b)\sum_{j=1}^{5}P_jb^{4-j}X^{j-1}.
}
\tag{15}
\]
这里结果确实属于原 \(\mathcal S_{34}\) 的六维型零空间。
其原点质量为
\[
\boxed{(\operatorname{Tr}_{[\delta]}\mathcal A_C)(0)=6c_C,}
\tag{16}
\]
而 \(\mathcal A_C(0)=0\)。两者不是同一个原点观察。
在 \(b=1\) 的基 \(\sigma^{34}x^2(1,X,\ldots,X^5)\) 中，
两条完整迹向量准确为
\[
\begin{aligned}
\mathbf t_{13}&=\left(
\frac{21760}{4949},-\frac{5248}{4949},-\frac{8201}{4949},
\frac{31091}{9898},-\frac{26351}{39592},-\frac{37}{5656}\right),\\
\mathbf t_{15}&=\left(
\frac{923}{245},\frac{3799}{980},\frac{35053}{7840},
\frac{10495}{3136},-\frac{12787}{12544},-\frac{37}{8960}\right).
\end{aligned}
\tag{17}
\]
完整纤维迹仍包含非原点支，不能替原 \(\mathcal A_C\)
中央赋值。

## 4. 整个十八维空间的真实 CM7 矩阵

令
\[
\gamma=\gamma_7=(5+\delta)/2,\qquad
N_7=\mathscr M_\gamma/\gamma.
\tag{18}
\]
\(\mathscr M\) 始终是 R300 的真实、没有除范数的 theta 迹：
\[
\mathscr M_a(\sigma^Nf)=
\sigma^N\operatorname{Tr}_{[a]}
\left[\left(\frac{r_{\bar a}}{r_a}\right)^N
f\circ[\bar a]\right].
\tag{19}
\]
其除子公式支付整个 \(\mathcal S_N\) 的稳定性及原相位，
不只是一个同像有限矩阵。

在 \(b=1\)，本篇整个型零空间为
\[
\mathcal V_{102}=\sigma^{102}K[X]_{\le17},\qquad
\dim_K\mathcal V_{102}=18.
\tag{20}
\]
这里 \(K=\mathbf Q(\delta)\)。
使用 R398 的同一个完整七次纤维，令
\[
r=(2-6\delta)/7,\quad
N_r(U)=U^6+(28r+12)U^3+7r^2+24r,
\]
\[
f_\xi(U)=UN_r(U)-\gamma^2\xi(U^3-r)^2.
\]
再置
\[
q=U^3-r,\quad \bar q=U^3-\bar r,\quad
\mathcal U=U^3N_{\bar r}(U)^3,\quad
\mathcal W=\bar\gamma^6\bar q^6.
\]
对 \(P(X)=\sum_{j=0}^{17}P_jX^j\)，准确有
\[
\boxed{
\left.\frac{N_7(\sigma^{102}P(X))}{\sigma^{102}}\right|_{x=\xi}
=\gamma^{-103}\operatorname{Tr}_{K[U]/(f_\xi)}
\left[q^{-102}\sum_{j=0}^{17}P_j\mathcal U^j\mathcal W^{17-j}\right].
}
\tag{21}
\]
分母和 \(\gamma^{-103}\) 保留原 division 常数以及
本篇额外的 \(1/\gamma\) 规范。

对整个十八个基向量，在 \(\xi=1,\ldots,18\) 的十八个
实际纤维作精确 \(K\) 运算。因为 (19) 保持 (20)，
十八个互异 \(\xi^3\) 完整决定每一列。
这得到随附 JSON 中的整个 \(18\times18\) 有理矩阵，
不是有限素数样本，也不是用低阶 jet 猜空间成员资格。

完整矩阵满足
\[
\boxed{
N_7^{18}=I,\qquad
I+N_7^3+N_7^6+N_7^9+N_7^{12}+N_7^{15}=0.
}
\tag{22}
\]
所以 \(N_7^3\) 的全部特征值及维数准确为
\[
\begin{array}{c|ccccc}
\tau&-1&\omega&\omega^2&-\omega&-\omega^2\\ \hline
\dim&3&3&3&6&3 .
\end{array}
\tag{23}
\]
没有遗漏正三次单位根的 \(N_7\) 特征空间：
\(N_7^3=1\) 的整个空间为零。

## 5. 三条原算术投影及十二个完整外谱

原三条拉回源严格满足
\[
N_7S(\delta z)=-S(\delta z),\quad
N_7H_3(\delta z)=-\omega H_3(\delta z),\quad
N_7H_5(\delta z)=-\omega^2H_5(\delta z).
\tag{24}
\]
三条是同一个原 \(S,H_3,H_5\)，每条实际特征线均一维。
令
\[
\boxed{\Pi_{\rm ar}=(I+N_7^6+N_7^{12})/3.}
\tag{25}
\]
它准确投到 (24) 的三维和。完整十八系数比较给
\[
\boxed{
\begin{aligned}
\Pi_{\rm ar}\mathcal A_{13}
={}&-\frac{667}{4242}S(\delta z)
-\frac{26}{44541b}H_3(\delta z)
-\frac{361}{712656b}H_5(\delta z),\\
\Pi_{\rm ar}\mathcal A_{15}
={}&-\frac{1279}{6720}S(\delta z)
-\frac{263}{1128960b}H_3(\delta z)
-\frac{257}{564480b}H_5(\delta z).
\end{aligned}
}
\tag{26}
\]
尤其不能忘记参考两列的 \(1/b\)；(14) 与原
\(S_b=b^{-1}S_1(b^{1/6}z)\)、\(H_{j,b}=H_{j,1}(b^{1/6}z)\)
给的就是这些权重。

全部 \(N_7^3\) 块的原点质量如下。表中列出
\(b\) 乘质量，以免隐藏这个固定周期框的权重。

| \(\tau\) | 维数 | \(b\,\mathrm{mass}(\mathcal A_{13,\tau})\) | \(b\,\mathrm{mass}(\mathcal A_{15,\tau})\) |
|---|---:|---:|---:|
| \(-1\) | 3 | \(-37/33936\) | \(-37/53760\) |
| \(\omega\) | 3 | \(811/1425312\) | \(431/1128960\) |
| \(\omega^2\) | 3 | \(743/1425312\) | \(173/564480\) |
| \(-\omega\) | 6 | \(-811/1425312\) | \(-431/1128960\) |
| \(-\omega^2\) | 3 | \(811/1425312\) | \(431/1128960\) |

五块的质量和确为零；三条算术列中只有 \(S(\delta z)\)
的质量为零。不能把整个来源的零质量分配给各块。

还可以确定两个来源各自的完整循环轨道。若
\(\tau\in\{\omega,\omega^2,-\omega,-\omega^2\}\)，
对每个 \(\zeta^3=\tau\)，其单特征投影质量为
\[
\frac1{18}\sum_{m=0}^{17}\zeta^{-m}
(N_7^m\mathcal A_C)(0).
\tag{27}
\]
把 \(\zeta^3=\tau\) 代入，这是随附数据中明确的二次多项式。
四个二次多项式都非零，而 \(X^3-\tau\) 在 \(K\) 上不可约：
若其有 \(K\) 中的根，该根是 \(K\) 的整单位，但
\(\mathcal O_K^\times=\mu_6\) 的立方只有 \(\{\pm1\}\)，
不可能等于上述 \(\tau\)。
所以这十二个单特征质量逐个严格非零。
结合 (26) 三个非零系数，两个来源的最小多项式都准确为
\[
\boxed{1+X^3+X^6+X^9+X^{12}+X^{15}.}
\tag{28}
\]
因此各自的真实来源轨道都是十五维。外谱没有被投影
或总质量零悄悄删除；它们不是新的已识别秩二有理椭圆来源。

## 6. 当前同一 ray 的整个 degree102 普通核心

继续使用 R454 的同一个固定 ray：
\[
\pi_0\equiv1428552127+2161889730\omega
\pmod{2793510720},
\]
\[
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad p>19,\quad p\equiv7\pmod{64}.
\tag{29}
\]
没有增加模条件。保持完整 Heisenberg lift 的中心模数
\(2N=204\)，准确有
\[
\boxed{
\pi_0/\bar\pi_0\equiv67,\qquad
\gamma/\bar\gamma\equiv176+59\omega,\qquad
(\gamma/\bar\gamma)^9\equiv67\pmod{204}.
}
\tag{30}
\]

R300/R413 的完整交织公式说明，原 \(K_{102}\) 与
\(N_7^9\) 在整个一百零二维 Heisenberg 表示上有相同交织，
故只差一个标量。这一步使用 (30) 的完整 \(2N\) 中心，
不是只比较模 \(N\) 的置换。

原 \(S(\delta z)\) 是非零的实际锚。\(\delta\) 在普通处为单位，
所以它的测度缩放与深限制严格交换；原 \(S\) 的核心为
\(\lambda[\kappa]_*\)。因此
\(K_{102}S(\delta z)=S(\delta z)\)，而 (24) 给
\(N_7^9S(\delta z)=-S(\delta z)\)。绝对标量被确定，得到
\[
\boxed{K_{102}=-N_7^9
\quad\text{于整个 }\mathcal S_{102}.}
\tag{31}
\]
相同的完整中心与该锚也给整个空间的 \(N_7^{18}=I\)，
与 (22) 的十八维精确矩阵相容。

在 (23) 的五块中，\(\tau=\omega,\omega^2\) 的核心为
\(-\lambda[\kappa]_*\)，其余三块为
\(+\lambda[\kappa]_*\)。令
\(\mathcal A_{C,-}\) 为前两个块之和，
\(\mathcal A_{C,+}\) 为其余块之和。上表准确给
\[
\boxed{\mathcal A_{C,-}(0)=-c_C,\qquad
\mathcal A_{C,+}(0)=c_C.}
\tag{32}
\]
所以整个真实单位质量是
\[
\boxed{
J_{\mathcal A_C}(0)
=(1-\lambda)c_C-(1+\lambda)c_C
=-2\lambda c_C.
}
\tag{33}
\]
在原固定有限坏集外，它为单位。这个明确的非零质量
不等于 \(J'_{\mathcal A_C}(0)\)，更不等于 \(J'_S(0)\)。

## 7. 原中央、尺度对数与没有删除的补分量

若用 \(\Pi_S\) 表示 (24) 中实际 \(-1\) 线的单投影，
则 (26) 已给完整来源级返回。例如
\[
\Pi_S\mathcal A_{13}=-\frac{667}{4242}S(\delta z).
\]
\(\delta\) 为普通单位，故真正的原 principal 行满足
\[
J_{F(\delta z)}(u)=
\langle\delta\rangle^{du}J_F(u),\qquad d=p-1.
\tag{34}
\]
因此
\[
\boxed{
J'_{\Pi_S\mathcal A_{13}}(0)
=-\frac{667}{4242}J'_S(0),\qquad
J'_{\Pi_S\mathcal A_{15}}(0)
=-\frac{1279}{6720}J'_S(0).
}
\tag{35}
\]
这里没有尺度对数质量项，原因是原 \(J_S(0)=0\)，
不是忽略了 \(\delta\) 的尺度。

对整个算术投影必须保留这个项。将 (26) 统一写为
\[
\Pi_{\rm ar}\mathcal A_C
=\alpha_CS(\delta z)
+\frac{\beta_C}{b}H_3(\delta z)
+\frac{\gamma_C}{b}H_5(\delta z),
\]
其中 \((\beta_C+\gamma_C)/b=c_C\)。
原两参考的单位质量均为 \(1-\lambda\)，所以
\[
\boxed{
\begin{aligned}
J'_{\Pi_{\rm ar}\mathcal A_C}(0)
={}&\alpha_CJ'_S(0)
+\frac{\beta_C}{b}J'_{H_3}(0)
+\frac{\gamma_C}{b}J'_{H_5}(0)\\
&+c_C(1-\lambda)d\log_p\langle\delta\rangle.
\end{aligned}
}
\tag{36}
\]
末项确为非零，因为
\(\log_p\langle\delta\rangle=\tfrac12\log_p3\ne0\)。
两条未知参考导数和十二个外谱中央仍然存在；不能由
(36) 只保留这个已知非零项。

完整来源 \(\mathcal A_C\)、其算术投影、通常三支纤维迹
(15) 和普通连通核 (31) 是四个已分别支付的对象。
它们不能互相替代。特别 (33) 不给 (35) 非零，
(15) 也不把非原点三挠分支删掉后变成新的中央零。
下一步需要在这些真实来源之间控制完整中央组合。

## 8. 整性、精确数据与依赖

整个 (12)、(17)、(21)、(26) 只含固定有限个代数系数。
在原 R460 有限坏集上再排这些固定矩阵和多项式分母的素因子，
以及需要整除返回时 (35) 两个有理系数的分子素因子，
所有测试、投影和返回都有同一个明确整格。
两份脚本及 JSON 保存这些完整有理数；没有随着目标
\(p\) 增长而另选来源、忽略分母或扫描素数。

- [固定 δ 源、完整范数/迹及全部 b 权重证书](../scripts/check-r464-fixed-delta-division-source.py)，
  [完整输出](../scripts/check-r464-fixed-delta-division-source.json)。
- [整个十八维 CM7 矩阵、十五谱及实际普通核心证书](../scripts/check-r464-degree102-cm7-exact.py)，
  [完整矩阵、全部质量与投影系数](../scripts/check-r464-degree102-cm7-exact.json)。
- R307/R460：原两个奇伴随、连接及完整来源规范。
- R297/R398：原 sigma 同源式和完整 CM7 七次纤维。
- R300/R413/R454：整个 theta 空间的真实迹、完整
  Heisenberg 中心、普通核心与当前固定 ray。
- R463：原 division-log 来源的尺度区别；本篇的
  \(\delta\) 范数已另行计算，不套用互素范数一。
