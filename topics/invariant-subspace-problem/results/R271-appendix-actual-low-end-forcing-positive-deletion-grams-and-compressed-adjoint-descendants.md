# R271 附录：实际低端 forcing 的全对删除正 Gram 与合法压后伴随后继

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文将原固定测试的全加权置换谐和条件提升为整个 forcing 空间上的算子正 Gram。任意两个真实尾删除列在这个来源上没有负交叉；原 $u_f$ 仍保两个缺陷之间的交叉，不能称其本身无抵消。另给真核上原 $C^*$ 后继与压后 $-D^*$ 后继的精确身份，不以环境 $\|p(C^*)\|$ 代替源度量。

依赖：[实际压后谐和方程](R271-appendix-actual-fixed-test-exchange-adjoint-harmonic-equations-and-full-generator-budget.md)、[实际缺陷及原窗口](R271-appendix-actual-projection-defect-two-sided-generator-and-all-dark-moments.md)、[完整返回的真实零源分解](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)。

## 1. 同一个 forcing 空间

沿原强联块记号，取
$$
C=A_m+D_<,\quad x=m+R,\quad
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
原闭空间仍是 $K=K_{m,Q}\subset V=V_{m,Q}$。令 $\mathcal F$ 是允许的强头张量远尾真空空间，$i_0:\mathcal F\to\mathcal H$ 为原物理等距嵌入。取 $Q\ge h=2^m+R$ 时，整个强头 forcing 及其所有 $C^*$ 多项式都在原允许输入中；也可只取实际使用的有限 forcing 子空间。

定义同一三个物理列
$$
Z_V=P_Vi_0,\qquad Z_K=P_Ki_0,\qquad
Z_e=(I-P_V)i_0 .
\tag{1.1}
$$
对任意 $g\in\mathcal F$，它们分别给 $v_g,k_g,e_g$；原
$$
u_g=v_g-k_g=i_0g-e_g-k_g,\qquad e_g\perp k_g.
$$
本稿的所有算子不等式都直接写在这个同一个 $\mathcal F$ 上。

对任意两位 $i\ne j$，令 $U_{ij}$ 为物理交换，$V_{ij}$ 为相应真实加权交换。其单占据矩阵为
$$
V_{ij}=
\begin{pmatrix}
0&b_j/b_i\\ b_i/b_j&0
\end{pmatrix},
$$
在真空及双占据上为 $I$。它与 $D$ 交换，保持原总孔 cut，且与强头算子对易。因此它保持原 $V,K$，而 $V^\perp$ 被 $V_{ij}^*$ 保持。$i_0g$ 被 $V_{ij}$ 和 $V_{ij}^*$ 同时固定。

原压后谐和论证不要求 $i,j$ 相邻。对上述三个 $Z$ 均得
$$
\boxed{Z^*V_{ij}Z=Z^*Z.}
\tag{1.2}
$$
对 $Z_e$ 可先用 $V^\perp$ 的 $V_{ij}^*$ 不变性得到伴随式，再取伴随。
(1.2) 是整个 forcing 空间上的恒等式，不只是一个固定实向量的二次型。

## 2. 全对删除交叉是实际正算子

对任意一个 $Z\in\{Z_V,Z_K,Z_e\}$，置
$$
M_i=Z^*n_iZ,\qquad M_{ij}=Z^*n_in_jZ,\qquad
K_{ij}=Z^*E_i^*E_jZ .
$$
单占据矩阵的 (1.2) 给
$$
\frac{b_j}{b_i}K_{ij}
+\frac{b_i}{b_j}K_{ij}^*
=M_i+M_j-2M_{ij},
\tag{2.1}
$$
右边是自伴正算子。将 (2.1) 与其伴随相减，原连续尾 $b_i\ne b_j$ 给
$K_{ij}=K_{ij}^*$。所以准确有
$$
\boxed{
Z^*E_i^*E_jZ
=\frac{b_ib_j}{b_i^2+b_j^2}
 Z^*(n_i+n_j-2n_in_j)Z
\succeq0\qquad(i\ne j).
}
\tag{2.2}
$$
对角 $K_{ii}=M_i\succeq0$ 当然也正。碰撞项 $2n_in_j$ 必须保留；没有把单孔公式免费条件化到每个孔层。

于是，若 $0\le c_i\le b_i$ 且
$D_c=\sum_{i\ge x}c_iE_i$，则
$$
\boxed{Z^*D_c^*D_cZ\preceq Z^*D^*DZ.}
\tag{2.3}
$$
证明是逐项展开：每个系数 $b_ib_j-c_ic_j$ 非负，而 (2.2) 的每个算子项都正。因 $b\in\ell^1$，这些有界算子双和绝对收敛；也可先证有限和，再逐项取非负极限。

更一般，若 $\{J_\alpha\}$ 是任意两两不交的尾位集合，记
$D_\alpha=\sum_{i\in J_\alpha}b_iE_i$，则
$$
\boxed{
\sum_\alpha Z^*D_\alpha^*D_\alpha Z
\preceq Z^*D^*DZ.
}
\tag{2.4}
$$
差正好是跨块的非负交叉项，加上未选位置的正项。该式直接保完整来源，不使用各块的独立环境范数。

由于只保留对角项也成立，
$$
\boxed{
Z^*D^*DZ\succeq
Z^*\left(\sum_{i\ge x}b_i^2n_i\right)Z.
}
\tag{2.5}
$$
因而在实际像 $\operatorname{Ran}Z$ 中，$Dz=0$ 迫使每个 $E_i z=0$，即 $z$ 的远尾严格为真空。这排除把任意非零高孔 primitive 坏源直接识别为本稿的实际投影列；它不给该交集附近的定量谱隙。

## 3. 共同源合同保留正 Gram，物理再次投影不免费保留

(2.2)--(2.5) 对任意共同来源算子 $R:\mathcal G\to\mathcal F$ 可作合同：
将每个 $Z$ 换成 $ZR$ 后，全部原式仍成立。
所以若某次真正 Riesz／Schur 最小化只改变同一个 forcing 代表，
其逆或平方根可以保在 $R$ 内，而不需要估计 $\|R\|$ 后再分别放大这些行。

这句话有准确限制：它是所有尾列共同右乘同一个源算子。
不能据此把 $Z$ 左乘任意物理投影，尤其不能默认
$P_EY_{u_g}$、各单独孔层或返回帽测试仍等于某个 $ZR$。
那些像识别尚需原来源方程；(2.2) 本身不提供它。

## 3a. 整个移动删除行的共同正算子分解

这里 $\mathcal F$ 是实际有限强头 forcing 空间。
对任意覆盖远尾的可数分拆 $\{J_\alpha\}$，令
$$
X=DZ,\qquad Y_\alpha=D_\alpha Z,\qquad
K_{\alpha\beta}=Y_\alpha^*Y_\beta,\qquad
A_\alpha=Y_\alpha^*X=\sum_\beta K_{\alpha\beta}.
$$
第 2 节给每个 $K_{\alpha\beta}$ 自伴且正，故
$A_\alpha\succeq Y_\alpha^*Y_\alpha\succeq0$。
定义原有限 forcing 矩阵的 MP 逆，并置
$$
\boxed{M_\alpha=Y_\alpha A_\alpha^\dagger Y_\alpha^*.}
\tag{3a.1}
$$
因为 $\ker A_\alpha\subset\ker Y_\alpha$，准确有
$$
M_\alpha X=Y_\alpha A_\alpha^\dagger A_\alpha=Y_\alpha.
\tag{3a.2}
$$
这里的伪逆只在有限 forcing Gram 内使用，不是原尾 MP 的新预算。

对任意有限支撑的 forcing 族 $(g_\alpha)$，有完整正平方身份
$$
\begin{aligned}
\sum_\alpha\langle A_\alpha g_\alpha,g_\alpha\rangle
-\left\|\sum_\alpha Y_\alpha g_\alpha\right\|^2
=\frac12\sum_{\alpha,\beta}
\langle K_{\alpha\beta}(g_\alpha-g_\beta),g_\alpha-g_\beta\rangle
\ge0.
\end{aligned}
\tag{3a.3}
$$
未选的 $g_\beta$ 读为零。将
$g_\alpha=A_\alpha^\dagger Y_\alpha^*w$ 代入任意有限子族，
得到其正算子和 $M_F=\sum_{\alpha\in F}M_\alpha$ 满足
$M_F^2\preceq M_F$。故
$$
\boxed{
M_\alpha\succeq0,\qquad
\sum_\alpha M_\alpha\preceq I,\qquad
D_\alpha Z=M_\alpha DZ .
}
\tag{3a.4}
$$
无穷和按正算子强极限。因为 $\sum_\alpha Y_\alpha=X$ 在算子范数收敛，
$(\sum_\alpha M_\alpha)X=X$。
可添余项 $I-\sum_\alpha M_\alpha\succeq0$，它严格杀 $X$。

于是整个移动分块行有共同的正收缩表示，而非分别选择的有界因子。
例如
$$
\sum_\alpha\|M_\alpha w\|^2\le\|w\|^2,\qquad
Z^*D_\alpha^*=Z^*D^*M_\alpha.
\tag{3a.5}
$$
这些同一个 $M_\alpha$ 对任何共同源合同 $ZR$ 仍有效。
它们通常不交换，也不保持原头旗或返回零源；本稿不将其当作这些空间的正交投影。

还有一个只使用真实孔上界的远位行量化。对单点分拆
$Y_i=b_iE_iZ$，若 $i\ge x$，从 (2.2) 的所有 $x\le j<i$ 项得
$$
A_i\succeq\kappa_iY_i^*Y_i,\qquad
\kappa_i=1+\frac12(i-x-Q+1)_+ .
\tag{3a.6}
$$
确实 $b_j\ge b_i$，故交叉系数
$b_i^2b_j^2/(b_i^2+b_j^2)\ge b_i^2/2$；而在 $\mathcal N\le Q$ 上
$$
\sum_{x\le j<i}(n_i+n_j-2n_in_j)
\succeq(i-x-Q+1)_+n_i .
$$
在 $n_i=1$ 时这只是在数前面必为空的位，在 $n_i=0$ 时左边非负。
所以原 $M_i$ 还满足 $0\le M_i\le\kappa_i^{-1}I$。
对 $L\ge x$，
$$
\boxed{
\sum_{i\ge L}\|M_iw\|^2\le\kappa_L^{-1}\|w\|^2,\quad
\sum_{i\ge L}\|Z^*b_iE_i^*w\|^2
\le\kappa_L^{-1}\|Z^*D^*\|^2\|w\|^2 .
}
\tag{3a.7}
$$
若右乘原源 $R$，第二式准确保 $\|R^*Z^*D^*\|$，不另估 $\|R\|$。
这是实际 fixed-forcing 压缩后的一整行；权 $b_i$ 不能去掉，
且 $L$ 必须真正超过 $x+Q$ 才得到衰减。它不宣称支付原窗口中较早位的未付反向列。

## 3b. 无 $Q$ 或头维数损失的完整 creation 行

单点情形把 (3a.1) 写为
$$
M_i=E_iZ\,(Z^*F_iZ)^\dagger Z^*E_i^*,
$$
$$
F_i=n_i+\sum_{\substack{j\ge x\\j\ne i}}
 \frac{b_j^2}{b_i^2+b_j^2}
 (n_i+n_j-2n_in_j).
\tag{3b.1}
$$
这是真正同源的正对角物理算子，而非删掉碰撞的近似。
它满足 $F_i\succeq n_i$，并有与孔数无关的准确上界
$$
F_i\preceq\left[1+\sum_{j\ne i}
 \frac{b_j^2}{b_i^2+b_j^2}\right]I
\preceq\frac43(i+1)I.
\tag{3b.2}
$$
证明最后一步时，$x\le j<i$ 的每项至多 $1$；
$j>i$ 的和至多
$(i+1)^4\sum_{k=i+2}^\infty k^{-4}\le(i+1)/3$。
因此总和实际上不超过 $\frac43(i+1)-x$。

令 $\mathcal Z=\operatorname{Ran}Z$，这是原有限 forcing 的物理像。
不需要假设 $Z^*Z$ 可逆。由 $F_i\succeq n_i$，
$\ker(Z^*F_iZ)\subset\ker(E_iZ)$。
故有限源伪逆有如下无歧义变分式：
$$
\langle M_iw,w\rangle
=\sup_{g\in\mathcal F}
 \left\{2\operatorname{Re}\langle E_iZg,w\rangle
        -\langle Z^*F_iZg,g\rangle\right\}.
$$
用 (3b.2) 代替最后的负二次项，并令 $Zg$ 遍历 $\mathcal Z$，得
$$
\boxed{
M_i\succeq\frac{3}{4(i+1)}E_iP_{\mathcal Z}E_i^*.
}
\tag{3b.3}
$$
这也避免了在奇异矩阵上错误交换 Moore--Penrose 逆与非酉源合同。

现在使用同一个 $\sum_iM_i\le I$，得到完整移动行
$$
\boxed{
\sum_{i\ge x}\frac1{i+1}E_iP_{\mathcal Z}E_i^*
\preceq\frac43 I,
\qquad
\sum_{i\ge x}\frac{\|P_{\mathcal Z}E_i^*w\|^2}{i+1}
\le\frac43\|w\|^2 .
}
\tag{3b.4}
$$
这是对整个实际 forcing 像的 creation 行，常数与 $Q,m,h$ 及 forcing
维数无关；没有对每一列使用强收敛后再相加。
保任意共同来源合同 $ZR$ 时，实际像是 $\operatorname{Ran}(ZR)$，
同样适用 (3b.4)。

## 4. 真核中合法的压后伴随后继

现在只取 $E=K$，其定义是原支撑 cut 内的完整真核。
$C,D$ 均保持 $K$，而
$$
(C+D)|_K=0.
$$
写 $C_K=C|_K$、$D_K=D|_K$。对任意多项式 $p$ 及允许 forcing $g$，
$$
\boxed{
P_Kp(C^*)i_0g
=p(C_K^*)P_Ki_0g
=p(-D_K^*)P_Ki_0g
=P_Kp(-D^*)P_Ki_0g.
}
\tag{4.1}
$$
第一和最后等号分别使用 $K$ 对 $C,D$ 的真实不变性；
多项式压缩始终保外层 $P_K$。这里不能删掉压后伴随而把
$D_K^*$ 当成完整 $D^*$。

$C^*$ 只作用于有限强头，所以 $p(C^*)i_0g$ 仍为远尾真空 forcing。
因此 (4.1) 的整族真实后继都可用 (2.2)--(2.5)，并可在同一 forcing 空间上交叉极化。其准确源度量是
$$
R^*[p(C^*)]^*\,G_K\,p(C^*)R,\qquad G_K=i_0^*P_Ki_0;
\tag{4.2}
$$
没有把它替换为 $\|p(C^*)\|^2R^*G_KR$。
若将 $p(C^*)$ 视为 $\mathcal F$ 上的原强头矩阵，(4.2) 就是普通源合同。

对原总尾截断，$C$ 降低强位孔数或只作用于旧头，故保持 $K$ 的支撑；$D$ 降低远孔。$C,D$ 都与 $C+D$ 交换，故其完整真核不变性成立。
伴随多项式可能在中间写出超 cut 行，但外层 $P_K$ 准确处理它；由于原伴随只增加相应尾孔，截在原环境后取幂与最终外投影一致。

特别，由 (2.5) 得实际交集的准确说明
$$
\operatorname{Ran}(P_Ki_0)\cap\ker D
=(\ker C)\otimes\Omega_>.
\tag{4.3}
$$
右包含因为这些向量本来属于 $K$；左包含先由 (2.5) 得远真空，再由真核方程得 $Cz=0$。这里只说实际像与真 primitive 的交集，不把它升级为角度或逆范数下界。

## 5. 两个缺陷合成 $u_g$ 时保留真实混合

对 $Z_e,Z_K$ 分别成立的 (2.3)，不能相减后用于 $u_g$。
准确有
$$
D_cu_g=-D_ce_g-D_ck_g.
$$
因而对任意 $\tau>0$，
$$
\boxed{
\|D_cu_g\|^2
\le(1+\tau)\|De_g\|^2+
 (1+\tau^{-1})\|Dk_g\|^2.
}
\tag{5.1}
$$
对任意不交分块同样有
$$
\boxed{
\sum_\alpha\|D_\alpha u_g\|^2
\le(1+\tau)\|De_g\|^2+
 (1+\tau^{-1})\|Dk_g\|^2.
}
\tag{5.2}
$$
这是两分量的共同正包络；右边保原 $De_g,Dk_g$，
不改成 $\|Du_g\|^2$。后者可能有两缺陷之间的相消。
实际整个源上也可对 (5.1)--(5.2) 极化成相应二次型不等式。

若再取未来段或输出孔集合，只能对已经形成的非负平方和删项或乘实际重叠数；不能因此宣布各个孔层分别满足 (2.2)。
原 $V,K$ 及其正交投影并不逐孔约化。


两缺陷还可保成单一共同正分解，而不先用平方三角。
令
$$
\widetilde Zg=(Z_eg,Z_Kg),\qquad
\widetilde D=\operatorname{diag}(D,D),\qquad S(a,b)=a+b.
$$
$\widetilde Z^*\widetilde E_i^*\widetilde E_j\widetilde Z$
是第 2 节两个正 Gram 的和，故第 3a 节给一个共同的
$\widetilde M_\alpha\succeq0$、$\sum_\alpha\widetilde M_\alpha\le I$，
满足
$$
\boxed{
D_\alpha u_g=-S\widetilde M_\alpha
 \begin{pmatrix}De_g\\Dk_g\end{pmatrix}.
}
\tag{5.3}
$$
这个式子保同一个二分量真实向量以及重合输出的交叉；
$\|S\|=\sqrt2$。它不是声称存在正 $M_\alpha$ 使
$D_\alpha u_g=M_\alpha Du_g$。第 (3a.6) 的孔上界同样适用于
这个直和共同分解。


第 3b 节还可对这个直和列使用。置
$$
G_\Delta=\widetilde Z^*\widetilde Z
=I-i_0^*P_Ui_0,\qquad Z_u=P_Ui_0 .
$$
它是同一真实投影缺陷的源 Gram，
$\langle G_\Delta g,g\rangle=\|i_0g-u_g\|^2$。
由 $E_iZ_u=-S\,\operatorname{diag}(E_i,E_i)\widetilde Z$，
以及
$\widetilde ZG_\Delta^\dagger\widetilde Z^*
=P_{\operatorname{Ran}\widetilde Z}$，
第 (3b.4) 式给
$$
\boxed{
\sum_{i\ge x}\frac1{i+1}
 E_iZ_uG_\Delta^\dagger Z_u^*E_i^*
\preceq\frac83 I .
}
\tag{5.4}
$$
这里 $SS^*=2I$ 是唯一的二分量常数。$\ker G_\Delta$ 上
$Z_ug=i_0g$ 为远真空，所以每个 $E_iZ_u$ 都杀这个核；
(5.4) 的奇异源写法因此准确，未添加未经支付的完整逆。

特别，对同一任意实际 $u_g$ 和任意物理 $w$，
$$
\boxed{
\sum_{i\ge x}\frac{|\langle E_i u_g,w\rangle|^2}{i+1}
\le\frac83\|i_0g-u_g\|^2\,\|w\|^2 .
}
\tag{5.5}
$$
这是同源双线性 moving 行，不是
$\sum_i\|E_i u_g\|^2$ 的上界。等价的整行形式 (5.4)
保全部 forcing 之间的交叉，因此其常数没有头维数因子。

## 6. 原返回接口保持开放的准确位置

完整返回空间为
$$
E_n=\mathscr W_n^{\mathrm{hi}}+Z_{f,n},\qquad
E_{0,n}=E_n\ominus Z_{f,n}.
$$
它被环境尾移位 $\mathbb T$ 保持，但 $(C+\mathbb T)|_{E_n}$ 一般不为零。
真正零源 $Z_{f,n}$ 和完整齐次右链才满足相应的核方程。
所以 (4.1) 不能把实际
$$
e_{g,n}=P_{E_n}Y_{u_g,n}
$$
自动写成一个远真空 forcing 的真核投影；其完整高返回强迫仍必须保留。

同样，原 $V_Q$ 的定义是截断低行方程。把强位并头后，
$D_<$ 可能把原总孔的顶端残量降入约束区，故不能未经核实就说
原 $V_Q$ 对整个强 $C$ 不变。本稿 (4.1) 仅在已经核明的完整 $K$ 上使用。

新增的实际约束是 (2.2) 的整个低端 forcing 空间正 Gram、
(2.3)--(2.5) 的同源删除单调性、第 3a 节的整行共同正分解，
第 3b／5 节的完整 creation 行与真实缺陷源 Gram，
以及 (4.1) 的合法压后伴随后继。
它们保真实零源短缩可以使用的源合同，但没有付
$Du_g$ 两分量之间的抵消、完整返回测试像识别或顺次 MP 两端部分和的负部。
普通 $N=M$ 仍未完成。
