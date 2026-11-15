# R150：零点第二连接的纯切向消去、公共因子 K77 与条件来源费 8678

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿证明：在原自然有限参数 $s=0$，完整第一、第二连接的秩 $r_1,r_2$ 满足
$r_1\le4$、$r_1+r_2\le7$。因此全部原 $4354$ 阶最大子式都被 $s^{31}$ 整除。结合其他已付有限因子，得到七十七次公共下因子 $K_{77}$。

再结合已证明的指定无穷远 $60/59/56$ 阶，得到条件性的完整原来源费 $8678$。本稿不假定零点第一连接恰有秩四，不把新的有限因子当成完整 gcd，也不由这些次数界宣布原目标已有多项式来源。

## 1. 原有限图、完整余空间与第一连接

使用原十七式和次数至多三的全部来源，保持原自然参数 $s$：
$$
A(s)=A_0+sA_1+s^2A_2+\cdots:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
\tag{1.1}
$$
这里 $A_2$ 是 $s^2$ 的系数，不含额外阶乘。原函数域秩为 $4354$。

[原零点完整秩证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)
已给出 $\operatorname{rank}_{\mathbb Q}A_0=4340$，所以恰有十四个正 Smith 指数，完整常数余空间维数为二十七。其完整对偶由二十个纯切向系数泛函与七个一次横向泛函组成。

[两个原图的第一连接证明](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)
对零点给出
$$
r_1=\operatorname{rank}_{\mathbb Q}\beta_1\le4.
\tag{1.2}
$$
该稿的零点小横向包络确有秩四，但尚未把它当作零点完整来源连接的下界。本稿只使用 (1.2)。

## 2. 原二阶纯切向项

取原
$$
y(s)=(1,s,s^2,s^3,s^4,s^5)^{\mathsf T},
$$
以及保持全部物理式的可逆共动矩变换
$$
m_j(s)=\sum_{k=0}^j\binom jk s^{j-k}n_k,
\qquad c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{2.1}
$$
在 $z_2=\cdots=z_{10}=0$ 上，
$$
M=c\,yy^{\mathsf T}
+d\bigl(yy'^{\mathsf T}+y'y^{\mathsf T}\bigr).
$$
原十七式的真实恒等式为
$$
\Gamma=0,\qquad
N=4d^2g(s)yy^{\mathsf T},
\qquad
g(s)=-2s^2(s-2)(s+6).
\tag{2.2}
$$
特别，全部常数和一次纯切向项都为零，$g_2=24$。

原矩阵的首列为
$$
p_0=Ke_0=(0,0,0,0,5,-1)^{\mathsf T}.
$$
所以二阶矩阵项的原十一坐标满足
$$
[s^2]\bigl(y(\zeta)^{\mathsf T}KNK y(\zeta)\bigr)
=96d^2(5\zeta^4-\zeta^5)^2
=d^2(2400\zeta^8-960\zeta^9+96\zeta^{10}).
\tag{2.3}
$$
按 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 的固定次序，
$$
F_2(c,d,0)
=d^2(0,0,0,0,0,0,0,0,2400,-960,96,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.4}
$$
这是全部原式的二阶项，没有删除均值梯度。

由于来源乘子次数至多三，(2.4) 只能产生纯切向目标空间中的
$$
\mathcal P=d^2\mathbb Q[c,d]_{\le3}.
\tag{2.5}
$$
固定其十个单项式次序为
$$
d^2,\ d^3,\ cd^2,\ d^4,\ cd^3,\ c^2d^2,\
d^5,\ cd^4,\ c^2d^3,\ c^3d^2.
\tag{2.6}
$$

## 3. 真实小包络为零与全部原行校正

保持第一连接稿的原
$$
P_0,P_1\in\mathbb Q^{170\times135}.
$$
行是十七式乘全部 $c^ad^b$、$a+b\le3$，列是全部
$c^ad^bz_j$、$a+b\le4$、$2\le j\le10$。

取完整核基
$$
P_0Q=0,\qquad Q\in\mathbb Q^{135\times7},
$$
$$
P_0^{\mathsf T}U=0,\qquad U\in\mathbb Q^{170\times42}.
$$
原小第一连接及其完整左核为
$$
C_{\rm tr}=U^{\mathsf T}P_1Q,\qquad
\operatorname{rank}C_{\rm tr}=4,\qquad
Z:\mathbb Q^{38}\xrightarrow{\sim}\ker C_{\rm tr}^{\mathsf T}.
\tag{3.1}
$$
这里的秩四仍是已付横向包络的秩。

令 $S\in\mathbb Q^{170\times10}$ 为 (2.4) 的来源系数矩阵：行 $(i,a,b)$ 只在列 $c^ad^{b+2}$ 上非零，值为 (2.4) 的第 $i$ 个系数。新的完整有理计算给出
$$
Z^{\mathsf T}U^{\mathsf T}S=0_{38\times10},
\qquad
\operatorname{rank}[C_{\rm tr},U^{\mathsf T}S]=4.
\tag{3.2}
$$
因此 $U^{\mathsf T}S$ 的各列属于 $\operatorname{im}C_{\rm tr}$，再由
$\ker U^{\mathsf T}=\operatorname{im}P_0$，得到
$$
S=P_0W+P_1QB,
\quad
W\in\mathbb Q^{135\times10},\quad
B\in\mathbb Q^{7\times10}.
\tag{3.3}
$$
实际脚本从原 $[P_0,P_1Q]$ 的可逆子块求出校正后，验证了 (3.3) 的全部 $170\times10$ 个有理等式。它没有仅检查所选子块。

## 4. 二十条完整左二阶 jet

对于 (2.6) 的第 $\ell$ 个纯系数泛函 $\lambda_\ell$，把 $W_\ell,QB_\ell$ 视为仅支持一次横向目标的泛函，定义
$$
\lambda_\ell(s)=\lambda_\ell-sQB_\ell-s^2W_\ell.
\tag{4.1}
$$
在共动坐标中，
$$
A(s)^{\mathsf T}\lambda_\ell(s)=O(s^3)
\tag{4.2}
$$
对全部 $6188$ 个原来源成立。

对纯切向来源，零阶与一阶项由 (2.2) 及 $P_0Q=0$ 消失，二阶项就是
$S_\ell-P_1QB_\ell-P_0W_\ell=0$。对含任意横向变量的来源，$F_0,F_1$ 至少含一个横向变量，所以乘积至少含两个横向变量，均被 (4.1) 中的一次横向校正杀掉；$F_2$ 乘该来源也不能产生纯切向目标。因而没有遗漏完整来源中的横向乘子。

其余十个纯切向泛函对应
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d.
$$
它们的 $d$ 次数至多一，由 (2.4) 直接以常数泛函满足 (4.2)。所以完整二十维纯切向泛函空间都具有真实二阶左延拓。

若共动矩阵与原矩阵的关系为
$$
A_{\rm new}(s)=T(s)A_{\rm old}(s)V(s),
$$
则原目标中的左列必须取 $T(s)^{\mathsf T}\lambda_\ell(s)$。这里 $T,V$ 在 $s=0$ 可逆，转置运输到二阶全部保留；不能把共动数组直接当作未变换的原左列。

对真实第一提升对
$$
A_0v_0=0,\qquad A_1v_0+A_0v_1=0,
$$
由 (4.2) 的系数逐项得到
$$
\lambda_\ell^{\mathsf T}(A_2v_0+A_1v_1)
=-\lambda_{\ell,1}^{\mathsf T}(A_1v_0+A_0v_1)
-\lambda_{\ell,2}^{\mathsf T}A_0v_0=0.
\tag{4.3}
$$
所以这些泛函确实杀掉完整第二连接，而非仅杀裸 $A_2v_0$。

## 5. 不假定第一连接等号的三十一阶结论

记完整第一、第二连接的秩为 $r_1,r_2$。在 Smith 坐标中，它们分别是正指数等于一、等于二的个数。

完整常数余空间维数为 $27$。二十条独立的常项泛函都延拓到二阶，故第三页目标至少为二十维，得到
$$
27-r_1-r_2\ge20,\qquad r_1+r_2\le7.
\tag{5.1}
$$
结合 $r_1\le4$，十四个正指数之和满足
$$
\begin{aligned}
\delta_0
&\ge r_1+2r_2+3(14-r_1-r_2)\\
&=42-2r_1-r_2\\
&=42-r_1-(r_1+r_2)\ge42-4-7=31.
\end{aligned}
\tag{5.2}
$$
因此
$$
\boxed{s^{31}\mid\text{全部原 }4354\text{ 阶最大子式}.}
\tag{5.3}
$$
这里没有推出 $r_1=4$，也没有单独推出 $r_2\le3$；后一结论需要先有 $r_1=4$，本稿没有免费使用无穷远的下界。

## 6. 七十七次有限公共因子

沿用已付且根集合互不相交的有限下因子
$$
K_{60}
=s^{14}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2,
$$
其中
$$
F_+=5s^3-25s^2+32s-8,\qquad
F_-=5s^3+135s^2+864s+864,
$$
$E_8$ 是[原射影公共因子证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)
及其 E8 分类使用的同一个八次多项式。其余因子在零点都非零。

将零点指数从 $14$ 提高到 $31$，得到
$$
\boxed{
K_{77}=s^{17}K_{60}=s^7K_{70}
=s^{31}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{6.1}
$$
它整除每个原最大子式，次数为 $77$，最高系数仍为 $5^6$，是 $31$ 单位。本稿不称 $K_{77}$ 是完整最大子式 gcd。

结合[原无穷远公共三十一阶](R150-appendix-infinity-second-connection-pure-cancellation-and-common-order31.md)，完整自然射影公共下因子的总次数至少为 $77+31=108$。这条共同下界与下一节指定来源的额外形式核因子分开使用。

## 7. 同一指定子式给条件来源费 8678

使用[完整 Smith 与真实 Koszul 曲线的指定阶证明](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)
中完全相同的原 $I,J$、非零子式 $D=\det A_{I,J}$ 和自然权：
$$
H=8770,\qquad \max a_\ell=55,\qquad
\delta_\ell=a_\ell-10,\qquad\max\delta_\ell=45.
$$
该证明已经给出：$D_h$ 无穷远至少 $60$ 阶；换入任意原来源列至少 $59$ 阶；全部 cofactor 至少 $56$ 阶。这里只把有限除子从 $K_{70}$ 换为 $K_{77}$，不再次累加公共无穷远阶。

令
$$
d_*=D/K_{77},\qquad q=\deg d_*.
$$
同一个 $D$ 模 $31$ 非零，原模 $31$ 最大子式 gcd 的次数 $315$ 只用于给 $\deg D\ge315$。于是
$$
\boxed{238\le q\le8770-60-77=8633.}
\tag{7.1}
$$
没有把模 $31$ 的因子提升为特征零因子。

对任一原来源列 $A_\ell$，
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{77}
\in\mathbb Q[s]^J,
\qquad
A_JP_\ell=d_*A_\ell
\tag{7.2}
$$
是全部 $4367$ 输出上的身份。多项式性来自有限公共因子；完整输出身份来自原函数域秩与选定输出上的单射性。换列阶给
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-59-77.
\tag{7.3}
$$

现明确假设原目标 $b_\nu=h_0t_\nu$ 已属于
$\operatorname{im}_{\mathbb Q[s]}A$，保原目标权 $\tau_\nu\le64$。则
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{77}
\in\mathbb Q[s]^J,\qquad
\deg(T_\nu)_j\le H-a_j+\tau_\nu-56-77.
\tag{7.4}
$$
这里 $T_\nu$ 的多项式性依赖成员性前提；并未要求 $K_{77}$ 整除每一个 cofactor。任意自然目标换列也只使用 $56$ 阶，不使用原来源换列的 $59$ 阶。

从一组已有多项式来源出发，用 (7.2) 将每个非基系数除以 $d_*$ 并把商移回基来源，可令非基系数次数小于 $q$。此时
$$
d_*y_j=(T_\nu)_j-\sum_{\ell\notin J}(P_\ell)_j y_\ell.
$$
三类来源成本分别不超过
$$
\begin{aligned}
q-1+45&\le8677,\\
H+55-59-77-11&=8678,\\
H+64-56-77-10-q
&\le8770+64-56-77-10-238=8453.
\end{aligned}
\tag{7.5}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8678.}
\tag{7.6}
$$
目标分支仍为 $8453$：有限因子新增七次时，$q$ 的下界同时减少七，二者在该分支抵消。

$K_{77}$ 的最高系数是 $31$ 单位，不等于已经证明 $\operatorname{lc}D$ 是 $31$ 单位。本稿没有据此将无界次数的模 $31^n$ 来源免费压成固定分母来源，也没有完成九个原目标的 $\mathbb Q[s]$ 成员性。

## 8. 实际小计算与复现

本次实际运行是 $43679903558$，步骤 zero-second-pure-envelope，执行源码提交
a8a63f71903e59580a3e21fdbc17fab6a2382a54。数学用时为
$0.3490508780014352$ 秒，退出码 $0$。共享数学时限 $10$ 秒、地址空间上限 $512$ MiB；只生成小原式矩阵，未重算旧正常形或大 Macaulay 矩阵。

[脚本](../notes/2026-11-15-r150-zero-second-pure-envelope-789f.py)
SHA256 为
874ca61fe167563859d628f56c296628e4992cc708e36af5f493f09d0e5dd5ec，
复用已付原生成器 SHA256
2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186。
参数为
~~~text
--generator <paid-original-transverse-generator>
--first-connection-receipt <paid-both-charts-receipt>
--out <temporary-small-receipt>
--remaining-seconds 10
~~~

实际输出为 $38\times10$ 全零、$42\times17$ 增广秩 $4$，并核完全部 $1700$ 条原校正等式。主要矩阵 SHA256：

| 对象 | SHA256 |
|---|---|
| 原纯二阶矩阵 $S$ | f80b8bd023735fc77268c9dcb9593746f5a7beae14e617729e3303d9b011f6dc |
| 完整纯包络零矩阵 | 39b9c7b36d61ee382a7f087f5646bc7c3628fc248ad3b1adb734b45b3da4a07e |
| 全部原行校正 $[W;B]$ | 577a6763d0e1d9832cd836a4c719eb3df17e03c8c6b75b8449c29284ffd95dc7 |

原临时小回执 $7050$ 字节，SHA256 为
c54e5e9ce0595ddde41fcf78971a9f1d37cda36099a670579d4cd13657b5d565。
[小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-zero-second-pure-envelope.json)
保留参数、秩、哈希与全身份标志。大矩阵和可重算校正数组只在实际作业内临时使用。
