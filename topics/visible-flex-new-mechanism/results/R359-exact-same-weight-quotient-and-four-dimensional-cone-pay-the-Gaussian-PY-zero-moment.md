# R359：同权准确商与四维正锥支付 Gaussian 的 P–Y 第零外矩

日期：2026-11-15。**有限纸面建设性证明；没有执行求积、符号程序、参数扫描、人工测试或其他研究计算。**

[R357](R357-genuine-mother-fibers-and-a-three-dimensional-ordered-profile-cone.md) 已给真实母纤维和三个完整有序坐标的正锥。本稿从原 R275/R278 全 self 恒等求出第四方向，联合控制同为权 −5 的 \(\mathcal B_1,\mathcal P_0\)，再把所有旧门的真实成本接回同一有限矩阵。所得偶弱圆保 R354 的16个完整外矩，并准确支付 \(\mathcal P_0\)；尚未支付的唯一 Gaussian 外矩是 \(\mathcal P_2\)。

所有系数均从实际有限 profiles 读取。特别，不能把同权两个目标分别按尺度压小，也不能把正半块的 \(\mathcal P_1\) 参数误当作镜像后仍自由的一个外矩。

来源：[R257](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R278](R278-third-slope-gap-masses-break-the-first-moment-halfplane.md)、[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)、[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md) 与 R357。

## 1. 原规范与四个真正同权坐标

固定
\[
0<t=\kappa^2<1/100,\qquad \kappa>0,\qquad h_e>0,
\]
\[
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e},\quad
k=\frac{db}{2}-ea\ne0.
\tag{1}
\]
记 \(W_*=aR+bS,\ Z_*=dL+eU\)，并沿用
\[
\mathcal B_j=[Z_*,W_*]_j,\quad
\mathcal C_j=[Z_*,Y]_j,\quad
\mathcal D_j=[W_*,Y]_j,\quad
\mathcal P_j=[P,Y]_j.
\]
\(\mathcal M=[W_*,P]\)、\(\mathcal A=[Z_*,P]\) 如前。

全部 \(E_{22},E_{04}\) 均为原 **\(2I_j\)** 的 even 系数，令
\(E_p=E_{22}-E_{04}\)。原十二完整副本已使 angular odd 系数为零，故 \(E_p,E_{04}\) 同时为零等价于该整个角函数为零。下面四行采用
\[
(\mathcal B_{1,p},\mathcal B_{1,04},
  \mathcal P_{0,p},\mathcal P_{0,04}).
\tag{2}
\]
它们全是权 −5。后文的常数 \(k\) 是同一实际 Gaussian 系数，不能随列独立选择。

## 2. 同一实际母包的 local 商

取 R357 的实际偶紧母 \(u\)，写 \(p=u'\)、\(r=u''\)，定义
\[
m=\int r^2,\quad C=\int r^4,\quad
\nu=\frac{\int(y^2r^2+2p^2)}m,
\]
\[
X_2=\int y^2r^4,\quad N=\int ypr^3,\quad
V_2=\int p^2r^2,\quad U_3=\int ur^3.
\]
引入两个真形状观察
\[
\mathcal J=3V_2+U_3-2N,\qquad
\mathcal K=V_2-\frac25N.
\tag{3}
\]
R357 的母纤维准确满足 \(\mathcal F_\kappa=0\)，且
\(\mathcal J/h,\mathcal K/h\) 是两个局部自由坐标；这里 \(h>0\) 为已固定的实际母宽。

由 R267 的原母恒等，
\[
D:=X_2-C\nu
=\frac85N-\frac{16e}{5(d+7e)}\mathcal J.
\tag{4}
\]
分母
\(d+7e=-\kappa(81t+7)/(4h_e)\ne0\)。

完整 R275 中的 local 项为
\[
\mathcal L=X_2-\frac83N+\frac43U_3+V_2,
\]
\[
\begin{aligned}
H_1={}&\frac{2d(a+b)+e(11a+5b)}{12}D\\
&-\frac{d(a+b)+2e(4a+b)}3N
+\frac{d(a+b)}3U_3+\frac{a(4e-d)}2V_2 ,
\end{aligned}
\]
\[
\mathcal R=H_1+k(C\nu-\mathcal L).
\tag{5}
\]
这里的 \(\mathcal R\) 是每列自己的母函数积分组合；不同母包之间不能抽出一个共同 \(\mathcal R\)。

从(5)先收成 \(A D+B N+C_UU_3+D_VV_2\)，各系数准确为
\[
A=\frac{2da-4db+23ea+5eb}{12},\quad
B=\frac{-da+3db-16ea-2eb}{3},
\]
\[
C_U=\frac{d(a-b)+4ea}{3},\qquad
D_V=3ae-\frac{d(a+b)}2.
\]
再代入
\[
U_3=\mathcal J-3\mathcal K+\frac45N,\qquad
V_2=\mathcal K+\frac25N
\]
以及(4)。\(N\) 的系数恰为
\(8A/5+B+4C_U/5+2D_V/5=0\)。因此得到准确商
\[
\boxed{\mathcal R=-\frac{G}{2}\mathcal K+R_J\mathcal J,}
\tag{6}
\]
其中
\[
G=d(3a-b)+2ae
=\frac{\kappa(8-166t+105t^2-663t^3)}{128h_e^3},
\]
\[
R_J=
\frac{5d^2(a-b)+de(47a-19b)+4e^2(12a-5b)}
 {15(d+7e)}.
\tag{7}
\]
在(1)的范围，
\(8-166t+105t^2-663t^3>
8-166/100-663/10^6>0\)，故 **\(G>0\)**。
这不是 leading 或小母宽近似；有限宽所有项均在(6)中。

## 3. 完整 primitive 给同权线性商

对一个完整强原型，令 \(q_{\rm c}=f+ig\)。R257 的合法复输入公式给
\[
\mathcal P_{0,p}=-\operatorname{Re}\mathscr Q,\qquad
\mathscr Q=\frac12\int[J(q_{\rm c}''{}^2)]^2
+\int\left(x^2q_{\rm c}''{}^4-\frac83xq_{\rm c}'q_{\rm c}''{}^3
+\frac43q_{\rm c}q_{\rm c}''{}^3+q_{\rm c}'{}^2q_{\rm c}''{}^2\right).
\tag{8}
\]
R278 (37)—(44) 保留全部 quadratic primitive 和原 Green 左尾后给
\[
\mathcal B_{1,p}
=k\operatorname{Re}\mathscr Q+\mathcal R W_{\rm act},\qquad
W_{\rm act}=\sum_i\operatorname{Re}(a_i+ib_i)^4w_i .
\]
因此
\[
\boxed{\ell:=\mathcal B_{1,p}+k\mathcal P_{0,p}
=\mathcal R W_{\rm act}.}
\tag{9}
\]
\(w_i\) 是实际正宽；完整八/十二副本的正第四幅权也包括在内。

为使用(9)，须核实真实 \(W_{\rm act}\) 的号，而非把它称为任意正系数。
记完整副本第四权和为 \(\mathcal W>0\)，主物理宽为 \(\delta>0\)。
R278 的 low/high/mid 三类在 shape 坐标的贡献分别为
\[
64nq^3(\alpha^2-6\alpha+1),\quad
n(H^2-6H+1),\quad -4nT_rq^2.
\]
利用该构造的准确关系
\[
64q(1-\alpha)=H-1,\quad
4T_r=64\alpha q(\alpha-5)+H(H-5)
\]
合并得
\[
\boxed{
W_{\rm act}=\mathcal W\delta\,n(1-q^2)(H^2-6H+1)>0 .
}
\tag{10}
\]
因为实际 \(q<1/3,\ H>13/2\)，最后两个因子均严格正。
两斜率情形是 \(T_r=0,H=\beta=(5-\alpha)/(1-\alpha)\)，此时也可写成
\[
W_{\rm act}=\mathcal W\delta\,64na_{\rm c}(1-q^2)(\alpha\beta-1)>0,
\quad a_{\rm c}=q(1-\alpha).
\tag{11}
\]
ordinary 与同源伴随的四次 real 数据相同，故均适用。
微包本身不紧的 primitive 没有被删去；正号只在完整式(8)—(10)以后使用。

## 4. R357 的三维锥恰填一个同权超平面

R357 的六个正半块取实际 \(\mathcal J=\mathcal K=0\)，并定义
\[
Q=\mathcal P_{0,p},\quad S=\mathcal P_{0,04},\quad
V=-\mathcal P_{1,04}/\xi ,
\tag{12}
\]
其中 \(\xi>0\) 为完整副本的最终第四幅中心。
它们的 \((Q,S,V)\) 矩阵满秩3且有严格正 kernel。

还需要原 common 系数，不能只用(9)。R275 (13)—(14) 准确给
\[
\mathcal B_{1,04}
=-kS-kV+\mathcal W64na_{\rm c}\delta(1-q^2)\mathcal R.
\tag{13}
\]
此式适用于 R357 使用的两排序。对于第三斜率，low/high 的推导仅用上述真实质量与方差关系，仍成立；R278 的新增 mid 项满足
\[
\Delta S=0,\qquad
\Delta(\mathcal B_{1,04}/k)=-\Delta V.
\]
mid 在这个角度的 local self 为零，故(13)也准确延伸到该完整第三排序。
完整副本的第四权中心零保证原 \(\xi\) 关系；没有把各 copy 的带中心值忽略。

由(6)，本节六列的 \(\mathcal R=0\)。因而(9)、(13)化为
\[
\boxed{
(\mathcal B_{1,p},\mathcal B_{1,04},
  \mathcal P_{0,p},\mathcal P_{0,04})
=(-kQ,-k(S+V),Q,S).
}
\tag{14}
\]
\(k\ne0\)，所以这是从 \(\mathbb R^3\) 到 \(\ker\ell\subset\mathbb R^4\) 的线性同构。
R357 六列遂给 **整个 \(\ker\ell\) 的真实正锥**，并保严格正 kernel。

(12)只是镜像以前的坐标。后面反射将 \(\mathcal P_1\) 清零，并不要求镜像后的 \(V\) 仍是一个非零实际 \(\mathcal P_1\)。

## 5. 两个真实母变化给第四方向

在同一个 R357 真母纤维内取
\[
\mathcal J=0,\qquad \mathcal K=h\zeta,\qquad
\zeta=\zeta_+>0\ \text{或}\ \zeta_-<0 ,
\]
两值充分小且非零。选择实际两斜率原型，例如
\(\alpha=19/40,\ \beta=181/21,\ q=100/441\)，并保真实方差补偿、完整三矩、八/十二副本和有限正宽。

这些新列不要求旧能量支路的 \(\mathcal H=0\) 或 \(L_c=M_c=0\)。
R357 已明确当前强原型仅需真实母 \(\mathcal F_\kappa=0\)、quartic 张量与三矩条件；前述能量不能从公式来源被暗中重新加作约束。
母 \(\nu\) 的变化纳入实际 high 间距，最后有限支撑和间隙照原构造选择。

由(6)、(9)、(11)，
\[
\ell_\pm=-\frac12 Gh\zeta_\pm W_{{\rm act},\pm}
\]
严格异号。其它三个坐标是各自完整真实数值，全部保留。

给两新列取严格正权，使其 \(\ell\) 总值为零。该正组合属于 \(\ker\ell\)，可用前六列的正锥准确抵消。若所用前六系数有零，添加其严格正 kernel，使八个系数全部正。
同时前六列张成 \(\ker\ell\)，任一新增列在其外，故
\[
\boxed{\operatorname{rank}L_4=4,\quad
\ker L_4\cap\mathbb R^8_{>0}\ne\varnothing,\quad
\operatorname{cone}_+(L_4)=\mathbb R^4.}
\tag{15}
\]
这是八个实际完整列，不是八个独立形式积分。

有限实矩阵满行秩且有严格正核时，任意目标都能用严格正系数实现：
先取实右逆给一个解，再加足够大的严格正核向量。
这一事实以后始终用于已经构造好的真实列。

## 6. 最终位置、反射与逐列恒零门

本节四个目标对完整块的共同平移不变。具体地，R357 已证 \(Q,S,V\) 的平移恒等；\(\mathcal R,W_{\rm act}\) 是母与真实宽度数据，(9)、(13)便给另外两个原系数的准确平移性。
先固定八个不同最终正中心，再取充分小但有限的正主宽，使全部包络严格分离。其它目标在这些位置的值照实记录，不能在以后代价账目中删掉。

对每列取与其完整空间反射等幅相加。R354 已用原 \(I_2\) 的两项证明：任意紧 outer 与真二次多项式尾的 \(I_0,I_1,I_2\) 全为零。每一半 inner 的三个实际矩也已为零。因此反射公式和跨完整块加法都准确适用。

(2)四个目标均为反射偶，故全部列共同乘2，(15)保持。
以下目标在每个镜像列上准确为零：
\[
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2),\quad
\mathcal B_0=\mathcal B_2=\mathcal C_1
=\mathcal P_1=\mathcal D_0=\mathcal D_2=0.
\tag{16}
\]
其中 M/A 由原母和三矩条件保持；其余由完整反射的准确奇性得到。
完整第二／第三、单 hook 和所有 angular odd 条件保持。

各强列的真实 quartic 张量为
\(A_4=5C_{22},E_4=C_{22}\)，所以 R325 的归一兼容量为
\(\Psi=\psi\sin^2\theta,\ \psi>0\)。
三个 directed 行仍为实际未调数值，留给最后同一个全72零强控制器。没有因每列是 strong 就宣称它已经满足三个 directed 门。

## 7. 接回所有旧的反射偶门：十行、三十六列

R354 的真实 \(M_8\) 有24个镜像列，行是
\[
(\mathcal B_1,\mathcal D_1,\mathcal C_0,\mathcal C_2),
\]
每项两个 even 系数。它满秩8且有严格正 kernel。
投影到 \((\mathcal D_1,\mathcal C_0)\) 的四行，得 \(M_4\)：仍满秩4、同一严格正核仍有效。
投影只表示暂不在该对角块内求解，其 \(\mathcal B_1,\mathcal P_0,\mathcal C_2\) 的实际值全部保留。

对这24列整体正伸缩 \(H\)，第四幅权乘 \(H^3\)：
\[
\mathcal B_1,\mathcal P_0:\ H^{-2},\qquad
\mathcal D_1,\mathcal C_0:\ 1 .
\]
连同(15)八个镜像列，八行矩阵在 \(H\to\infty\) 时趋于
\[
\begin{pmatrix}L_4&0\\ D_{\rm low}&M_4\end{pmatrix}.
\tag{17}
\]
\(D_{\rm low}\) 是八列真实旧门成本。
两个对角块均是满正锥，故(17)满秩并有严格正核：先取 \(L_4\) 的正核，再用 \(M_4\) 的正锥补偿底行并加其正核。
选一个固定非零八阶 minor，用右逆把任意充分小矩阵扰动的核残差纠正；严格正性开放。故存在足够大但有限 \(H\)，全部八行保持这些性质。

此时 \(\mathcal C_2\) 成本可能按 \(H^2\) 增长。
**先固定这个有限 \(H\)，把所有该成本作为实际有限数保留**，不能把它也称为小量。

再加入 R349 的四个 \(\mathcal C_2\) 原型，各自完整镜像。
对这四列作另一个整体伸缩 \(H'\)，第四幅权乘 \(H'\)：
\[
(\mathcal B_1,\mathcal P_0):H'^{-4},\qquad
(\mathcal D_1,\mathcal C_0):H'^{-2},\qquad
\mathcal C_2:1.
\]
R349 两行真正锥成为第二次分块的下对角块。对已固定的前32列再用同一非零 minor／严格正核开放性，选择充分大但有限 \(H'\)，得到
\[
\boxed{
M_{10}=(\mathcal B_1,\mathcal P_0,
\mathcal D_1,\mathcal C_0,\mathcal C_2),\quad
\operatorname{rank}M_{10}=10,\quad
\ker M_{10}\cap\mathbb R^{36}_{>0}\ne\varnothing .
}
\tag{18}
\]
每项仍为两个原 even 系数，列数 \(8+24+4=36\)。
可以把新组伸缩到先前有限包络之外；所有正半支持远离0，反射部分同步向左，内部间隙保持。
\(\mathcal P_2\) 的真实成本仍在，只是不属于本稿已付目标。

这一步没有对同权 \(\mathcal B_1,\mathcal P_0\) 使用无效的分级压小；二者自始作为同一个完整四行块联合控制。

## 8. 在同一弱基线上准确支付 P0，并保 Ψ 负储备

取 R354 §12 最后强控制器以前的实际偶弱基线。它有非零导数 rank-two 区，所有旧16个完整外矩为零，且
\[
\Psi=-\Delta\sin^2\theta,\quad \Delta>0.
\]
其弱核心、cutoff、补矩、内部位置和所有已完成有限选择都保持固定。
记该基线 \(\mathcal P_0\) 的两个实际 even 残差为 \(r\in\mathbb R^2\)。

由(18)，选一次严格正向量 \(c\in\mathbb R^{36}_{>0}\)，使
\(M_{10}c\) 的 \(\mathcal P_0\) 两行为 \(-r\)，其余八行为零。
该 \(c\) 不依赖下一公共尺度。

把36个真实完整列共同正伸缩 \(S\)，每列第四幅取 \(S^5c_i\)。原完整权给
\[
\begin{array}{c|c}
\text{目标}&\text{乘数}\\ \hline
\mathcal B_1,\mathcal P_0&S^0\\
\mathcal D_1,\mathcal C_0&S^2\\
\mathcal C_2&S^4\\
\Psi&S^{-2}
\end{array}
\tag{19}
\]
因此 \(\mathcal P_0\) 增量准确是 \(-r\)，其它八行仍严格为零。
(16)逐列恒零门也保持，不是靠幅度小而近似为零。

新增真实兼容量为
\[
\Delta\Psi=S^{-2}\left(\sum_i c_i\psi_i\right)\sin^2\theta.
\tag{20}
\]
系数有限且正。取一个足够大但有限 \(S\)，令它小于 \(\Delta/2\)，并使全部新支持位于固定弱基线外侧。如此仍有严格负 \(\Psi\) 储备。
\(\mathcal P_2\) 的真实新增值按 \(S^2\) 记录为剩余残差；没有在这里把它忽略。

最后使用 R325/R354 的同一预选 \(F^\star\) 强控制器及其镜像。
先取正幅支付剩余 \(\Psi\)，再在原有限观察纤维内取一个有限频率 \(N\)，准确清三个完整 directed 行 \(F_0,F_1,F_2\)。
该控制器的全部72 Gaussian 面积在整个纤维中为零，因此刚付的 \(\mathcal P_0\) 和全部旧门都保持。
原完整副本、母函数和弱 rank-two 核心也保持；没有将 \(S,N\) 无穷大作为最终对象。

## 9. 先全部有限支持，再选择真实几何

本稿采用 R354 §8—11 的实际安装顺序。先在 \(h_e=1\) 的归一系数下完成上述所有有限母参数、主宽、列中心、内部复制、\(H,H',S,N\) 和最后控制器，取得有限区间包络 \(I=[\ell,r]\)。

再选 \(\Omega>\max(0,-\ell)+1\)，初次选择实际足够小的 \(h_e>0\)，使整个所需 Gaussian germ 有 \(\omega>\Omega+1\)。
R354 的先正后负 boost、同 \(\omega\) 下界的真实八矩桥、保持 \(N\mathfrak H=0\) 的 hook 平移、M0 真倒行夹心和 Klein 闭合给整条真实几何
\[
M=0,\quad T\ne0\text{ 为原 hook},\quad x+\omega(s)>1
\quad(x\in I).
\]
这个共同正下界支付了全部负支撑和正支撑的物理合法性。

改变 \(h_e\) 只给目标施加同一非零行因子：
\(\mathcal B_1\) 乘 \(h_e^{-3}\)，
\(\mathcal D_1\) 乘 \(h_e^{-2}\)，
\(\mathcal C_0,\mathcal C_2\) 乘 \(h_e^{-1}\)，
\(\mathcal P_0,\mathcal P_2,\Psi\) 不变。
基线与全部纠正列使用同一因子，所有准确零式保持。
三个 directed 行也按 R354 的原表缩放，因此其零不变。
所需母方程只是同一 Gaussian 系数的齐次关系，亦保持。

最终 seed/g 在这些有限 choices 以后才一次固定。
此处不扩大任意已经冻结的旧窄区间，也不把另一条几何上的 whole pure/self、Morse、全部 period 或同一规范 joint 门移植到这里。

## 10. 已完成的精确结论

在一条真实闭正则 hook 几何与同一个实际偶弱圆上，
\[
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=\mathcal C_j
=\mathcal D_j=0\ (j=0,1,2),\qquad
\mathcal P_0=\mathcal P_1=0
}
\tag{21}
\]
对全部相位准确成立；保三矩、完整第二／第三 range、非零 rank-two 区及
\(\Psi=F_0=F_1=F_2=0\)。

这是 **17个完整 Gaussian 外矩**。唯一剩余外矩为 \(\mathcal P_2\)。
新可复用接口是(15)八列四行及(18)三十六列十行的实际正锥，不是形式 even 条数。
本稿未宣整个72面积、第四的对称 history、完整 period、同一规范 joint 或主课题完成；更高阶收敛、同一固定度量的有限连续嵌入族、闭面、全时 reach 与宏观幅度仍须继续。
